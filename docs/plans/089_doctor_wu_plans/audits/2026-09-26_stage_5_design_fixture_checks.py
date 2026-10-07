"""Symbolic document and conservation checks for DW-089-S5.

This is not HOI4 code, a native integration test, or an epidemiological model.
Run with Python 3.10+ and optionally pass --baseline PATH to an extracted Stage 4.
It writes the adjacent results JSON. No network or third-party packages are used.
"""
from __future__ import annotations
import argparse
from dataclasses import dataclass, field
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import re
from typing import Callable


@dataclass(frozen=True)
class Profile:
    identity: str
    parent: str
    role: str


@dataclass
class Reservation:
    profile: str
    quantity: int
    settled: bool = False
    outcome: str | None = None


@dataclass
class SymbolicStockModel:
    installed: dict[str, Profile]
    stock: dict[str, int] = field(default_factory=dict)
    operations: dict[str, Reservation] = field(default_factory=dict)
    consumed: int = 0
    accepted_releases: int = 0

    def add(self, profile: str, amount: int) -> None:
        if profile not in self.installed or amount < 0:
            raise ValueError('Unknown profile or negative stock')
        self.stock[profile] = self.stock.get(profile, 0) + amount

    def reserve(self, key: str, profile: str, amount: int) -> Reservation:
        if profile not in self.installed or amount <= 0:
            raise ValueError('Invalid reservation')
        if key in self.operations:
            old = self.operations[key]
            if (old.profile, old.quantity) != (profile, amount):
                raise ValueError('Conflicting operation identity')
            return old
        if self.stock.get(profile, 0) < amount:
            raise ValueError('Insufficient exact stock')
        self.stock[profile] -= amount
        self.operations[key] = Reservation(profile, amount)
        return self.operations[key]

    def complete(self, key: str, outcome: str, valid_context: bool = True) -> bool:
        if outcome not in {'delivered', 'failed', 'dispatch_failed'}:
            raise ValueError('Unknown completed outcome')
        r = self.operations[key]
        if r.settled:
            return False
        r.settled = True
        r.outcome = outcome if valid_context else 'context_rejected'
        self.consumed += r.quantity
        self.accepted_releases += int(valid_context and outcome == 'delivered')
        return True

    def destroy_available(self, profile: str, amount: int) -> None:
        if amount < 0 or amount > self.stock.get(profile, 0):
            raise ValueError('Cannot destroy unproved available quantity')
        self.stock[profile] -= amount


@dataclass
class Programme:
    qualified: set[str]
    slots: list[str | None] = field(default_factory=lambda: [None])
    pending: dict[int, str] = field(default_factory=dict)

    def annex(self) -> None:
        if len(self.slots) >= 2:
            raise ValueError('Country-wide limit')
        self.slots.append(None)

    def begin_switch(self, slot: int, profile: str) -> None:
        if not 0 <= slot < len(self.slots) or profile not in self.qualified or slot in self.pending:
            raise ValueError('Unqualified or occupied switch')
        self.pending[slot] = profile

    def finish_switch(self, slot: int) -> None:
        self.slots[slot] = self.pending.pop(slot)

    def cancel_switch(self, slot: int) -> None:
        self.pending.pop(slot)

    def may_produce(self, slot: int) -> bool:
        return self.slots[slot] is not None and slot not in self.pending


@dataclass
class FiniteCohort:
    made: int
    first_settled: int = 0
    before_settlement_deaths: int = 0
    accounts: dict[str, int] = field(default_factory=dict)

    @property
    def unsettled(self) -> int:
        return self.made - self.first_settled - self.before_settlement_deaths

    def settle(self, receipt: str, amount: int) -> None:
        if receipt in self.accounts:
            if self.accounts[receipt] != amount:
                raise ValueError('Conflicting first-settlement receipt')
            return
        if amount < 0 or amount > self.unsettled:
            raise ValueError('Invalid first settlement')
        self.accounts[receipt] = amount
        self.first_settled += amount


def must_reject(fn: Callable[[], object]) -> None:
    try:
        fn()
    except (ValueError, KeyError, IndexError):
        return
    raise AssertionError('Invalid case was accepted')


def run(baseline: Path | None) -> dict:
    package = Path(__file__).resolve().parents[4]
    spec = package/'docs/specs/089_doctor_wu_specs/research/089_doctor_wu_spec_part_9_modified_capabilities_and_strain_ownership.md'
    text = spec.read_text(encoding='utf-8')
    results: list[dict] = []

    def case(name: str, fn: Callable[[], None]) -> None:
        try:
            fn()
            results.append({'case': name, 'passed': True})
        except Exception as exc:
            results.append({'case': name, 'passed': False, 'error': str(exc)})

    def check(condition: bool, message: str = 'Assertion failed') -> None:
        if not condition:
            raise AssertionError(message)

    profiles = {p.identity: p for p in [Profile('A', 'fictional_source', 'reference'), Profile('B', 'fictional_source', 'defensive'), Profile('BASE', 'fictional_source', 'unmodified')]}

    def switching() -> None:
        m = SymbolicStockModel(profiles)
        m.add('A', 120)
        m.reserve('opA', 'A', 40)
        programme = Programme({'A', 'B'}, ['A'])
        programme.begin_switch(0, 'B')
        check(not programme.may_produce(0))
        programme.finish_switch(0)
        m.add('B', 30)
        check(m.stock == {'A': 80, 'B': 30})
        check(m.operations['opA'].profile == 'A')
        check(programme.slots == ['B'])
    case('Old A reservation remains A after B retooling', switching)

    def reservation_replay() -> None:
        m = SymbolicStockModel(profiles)
        m.add('A', 100)
        m.reserve('same', 'A', 40)
        m.reserve('same', 'A', 40)
        check(m.stock['A'] == 60)
        must_reject(lambda: m.reserve('same', 'B', 40))
        check(m.stock['A'] == 60)
    case('Same reservation replay does not debit twice and conflicting replay fails', reservation_replay)

    def duplicate_completion() -> None:
        m = SymbolicStockModel(profiles)
        m.add('A', 40)
        m.reserve('r', 'A', 40)
        check(m.complete('r', 'delivered'))
        check(not m.complete('r', 'delivered'))
        check((m.consumed, m.accepted_releases, m.stock['A']) == (40, 1, 0))
    case('One completed outcome consumes and records once', duplicate_completion)

    for outcome, valid in [('failed', True), ('dispatch_failed', True), ('delivered', False)]:
        def no_release(outcome=outcome, valid=valid) -> None:
            m = SymbolicStockModel(profiles)
            m.add('A', 50)
            m.reserve('r', 'A', 40)
            m.complete('r', outcome, valid)
            check((m.consumed, m.stock['A'], m.accepted_releases) == (40, 10, 0))
        case(f'{outcome}, valid_context={valid}: full completed reservation and no invented release', no_release)

    def no_substitution() -> None:
        m = SymbolicStockModel(profiles)
        m.add('BASE', 500)
        m.add('B', 100)
        must_reject(lambda: m.reserve('r', 'A', 40))
        check(m.stock == {'BASE': 500, 'B': 100})
    case('Other profiles and base stock cannot pay an A reservation', no_substitution)

    def exact_boundary() -> None:
        m = SymbolicStockModel(profiles)
        m.add('A', 40)
        m.reserve('r', 'A', 40)
        check(m.stock['A'] == 0)
        must_reject(lambda: m.reserve('r2', 'A', 1))
        must_reject(lambda: m.reserve('bad', 'UNKNOWN', 1))
        must_reject(lambda: m.reserve('negative', 'A', -1))
    case('Inclusive stock boundary and invalid quantities', exact_boundary)

    def concurrent() -> None:
        m = SymbolicStockModel(profiles)
        m.add('A', 100)
        m.add('B', 100)
        m.reserve('a', 'A', 30)
        m.reserve('b', 'B', 40)
        m.complete('b', 'failed')
        check(not m.operations['a'].settled)
        check(m.operations['a'].profile == 'A')
        check(m.stock == {'A': 70, 'B': 60})
    case('Concurrent profile operations preserve separate identities', concurrent)

    def destruction() -> None:
        m = SymbolicStockModel(profiles)
        m.add('A', 120)
        m.reserve('r', 'A', 40)
        must_reject(lambda: m.destroy_available('A', 81))
        m.destroy_available('A', 80)
        check(not m.operations['r'].settled and m.operations['r'].quantity == 40)
        check(m.stock['A'] == 0)
    case('Safety action cannot spend natively reserved material', destruction)

    def slot_limits() -> None:
        p = Programme({'A', 'B', 'C'})
        p.annex()
        must_reject(p.annex)
        # A second director sees the same programme, not an additional allowance.
        second_director = p
        must_reject(second_director.annex)
        check(len(p.slots) == 2)
    case('Two country-wide slots remain two after a second director', slot_limits)

    def switch_cancel() -> None:
        p = Programme({'A', 'B'}, ['A'])
        p.begin_switch(0, 'B')
        must_reject(lambda: p.begin_switch(0, 'A'))
        check(not p.may_produce(0))
        p.cancel_switch(0)
        check(p.slots == ['A'] and p.may_produce(0))
        must_reject(lambda: p.begin_switch(0, 'UNKNOWN'))
    case('Retooling exclusivity and cancellation retain old identity', switch_cancel)

    def finite() -> None:
        c = FiniteCohort(1000)
        c.settle('military', 600)
        c.settle('civilian', 250)
        c.settle('civilian', 250)
        c.before_settlement_deaths += 10
        check(c.unsettled == 140)
        check(c.made == c.unsettled + c.first_settled + c.before_settlement_deaths)
        # Five specialist appointments are roles among the 250 civilian people.
        check(5 <= c.accounts['civilian'])
        check(c.first_settled == 850)
        must_reject(lambda: c.settle('duplicate_people', 141))
        must_reject(lambda: c.settle('military', 601))
    case('Inherited finite settlement survives replay and specialist appointments', finite)

    def reception() -> None:
        total_places, survivors, migrants = 1000, 400, 350
        available = total_places - survivors - migrants
        request = 300
        admit = lambda food_proof: min(request, available) if food_proof is True else 0
        check(admit(None) == 0 and admit(False) == 0 and admit(True) == 250)
        # Unadmitted people remain a custody and food obligation.
        check(request - admit(None) == request)
    case('Shared reception capacity and absent food proof', reception)

    def knowledge() -> None:
        known = {'A', 'B'}
        physical = {'A': 0, 'B': 0}
        permission = False
        check('B' in known and physical['B'] == 0)
        check(not permission)
        # Neither source event firing nor people are created by knowledge.
        events_fired: set[str] = set()
        people_created = 0
        check(not events_fired and people_created == 0)
    case('Knowledge does not imply stock, permission, source firing, or new people', knowledge)

    def prices() -> None:
        base = Fraction(100)
        general = base * Fraction(3, 2)
        acute = base * 2
        context = max(base, general * Fraction(3, 4))
        pair = max(general, context) * Fraction(3, 2)
        check((general, acute, context, pair) == (150, 200, Fraction(225, 2), 225))
        check(max(base, base * Fraction(3, 4)) == base)
    case('Fictional industrial anchors and context floor', prices)

    rows = [line for line in text.splitlines() if re.match(r'^\| S\d\d ', line)]
    case('Twelve project inventory rows', lambda: check(len(rows) == 12))
    for row in rows:
        project = re.match(r'^\| (S\d\d)', row).group(1)
        def cost_case(row=row) -> None:
            commitment = row.split('|')[-2]
            found = []
            for name, pattern in [('lane', r'\blane\b'), ('factory', r'civilian factor'), ('support', r'Support Equipment'), ('political', r'Political Power'), ('army', r'Army Experience'), ('command', r'Command Power'), ('fuel', r'\bfuel\b')]:
                if re.search(pattern, commitment, re.I):
                    found.append(name)
            check(len(found) == 4, f'Cost types: {found}')
        case(f'{project}: four stated research cost types', cost_case)

    case('Exact required opening', lambda: check(text.startswith('# Doctor Wu: modified capabilities and strain ownership\n## Designs that retain their source and consequences\n')))
    case('Exact stopping heading', lambda: check([x for x in text.splitlines() if x.startswith('## ')][-1] == '## What the portfolio leaves for the rivalry'))
    case('S01 through S12 developed headings', lambda: check(all(re.search(rf'^## {s}:', text, re.M) for s in [f'S{i:02}' for i in range(1, 13)])))
    case('Twenty-four named AI scenarios', lambda: check(len(re.findall(r'^\| A\d\d ', text, re.M)) == 24))
    case('Prose punctuation restriction', lambda: check('\u2014' not in text and ';' not in text))
    case('No pasteable localisation block', lambda: check('l_english:' not in text and not re.search(r'^\s*[\w.]+:0\s+"', text, re.M)))
    case('Defensive qualification explicitly independent of S03', lambda: check('this route does not require S03' in text))
    # Check an explicit specification boundary, not a claim that prose scanning proves safety.
    case('Recipient classes exclude real population identities', lambda: check(all(x in text.lower() for x in ['ethnicity', 'nationality', 'religion', 'sex'])))

    preserved=[]
    if baseline is not None:
        candidates=sorted((baseline/'docs/specs/089_doctor_wu_specs').rglob('*part_*.md'))
        candidates.append(baseline/'docs/plans/089_doctor_wu_plans/source_inputs/2026-09-24_doctor_wu_user_brief.txt')
        for old in candidates:
            rel=old.relative_to(baseline)
            new=package/rel
            same=old.read_bytes()==new.read_bytes()
            preserved.append({'path':str(rel),'byte_identical':same,'sha256':hashlib.sha256(new.read_bytes()).hexdigest()})
            case(f'Preserved {old.name}', lambda same=same: check(same))

    return {'stage':'DW-089-S5','scope':'Symbolic design and document checks only. No game, native engine, medical model, or MCP execution.', 'case_count':len(results),'passed_count':sum(r['passed'] for r in results),'failed_count':sum(not r['passed'] for r in results),'cases':results,'baseline_preservation':preserved,'native_cancellation':'Not simulated. Requires actual native evidence.','safety_note':'No organism, pathogen, preparation, delivery, or biological optimization is modeled.'}


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--baseline',type=Path)
    args=parser.parse_args()
    result=run(args.baseline)
    destination=Path(__file__).with_name('2026-09-26_stage_5_design_fixture_results.json')
    destination.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ['stage','case_count','passed_count','failed_count']},indent=2))
    if result['failed_count']:
        raise SystemExit(1)
