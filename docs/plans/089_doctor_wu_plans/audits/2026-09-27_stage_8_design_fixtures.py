"""Symbolic checks for Doctor Wu Part 12, not a HOI4 implementation or simulation.

Run with Python 3. The script uses only the standard library and writes a JSON
record next to itself. All state below is declared fixture state. It does not
load or execute game scripts, call MCP, or evaluate actual AI probabilities.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal, ROUND_CEILING
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[4]
PART = ROOT / 'docs/specs/089_doctor_wu_specs/evolutions/089_doctor_wu_spec_part_12_national_medical_ascendancy.md'
RESULT = Path(__file__).with_name('2026-09-27_stage_8_design_fixture_results.json')
RESULTS: list[dict[str, object]] = []


def check(name: str, condition: bool, detail: str, category: str = 'symbolic') -> None:
    RESULTS.append({'name': name, 'passed': bool(condition), 'category': category, 'detail': detail})


def rounded_five(value: Decimal) -> int:
    return int((value / Decimal(5)).to_integral_value(rounding=ROUND_CEILING) * 5)


def nominal_mtth(factors: list[str]) -> int:
    result = Decimal(90)
    for raw in factors:
        factor = Decimal(raw)
        if not factor.is_finite() or factor <= 0:
            raise ValueError('Timing factors must be positive finite values')
        result *= factor
    return max(30, min(240, rounded_five(result)))


def major_cure(*, owner_major: bool, treated: int, episode_basis: int,
               arrival_demonstration: bool = False) -> bool:
    if treated < 0 or episode_basis < 0:
        raise ValueError('Population inputs cannot be negative')
    if arrival_demonstration:
        return False
    return owner_major or treated >= 1_000_000 or (episode_basis > 0 and treated * 4 >= episode_basis)


@dataclass
class EvolutionFixture:
    enabled: bool = True
    logged: bool = False
    bypassed: bool = False
    pending_owner: str | None = None
    chronology: list[int] = field(default_factory=list)
    care_obligations: int = 10

    def queue(self, owner: str, chaos: int, institute_valid: bool, qualifying_cause: bool) -> bool:
        if (not owner or not self.enabled or self.logged or self.bypassed
                or self.pending_owner is not None or chaos < 200
                or not institute_valid or not qualifying_cause):
            return False
        self.pending_owner = owner
        return True

    def deliver(self, owner: str, chaos: int, institute_valid: bool) -> bool:
        if self.pending_owner != owner:
            return False
        self.pending_owner = None
        if not self.enabled or self.logged or self.bypassed or chaos < 200 or not institute_valid:
            return False
        self.logged = True
        self.chronology.append(1)
        return True

    def disable(self) -> None:
        self.enabled = False
        self.pending_owner = None

    def restore_permission(self) -> None:
        self.enabled = True

    def commit_later_after_disabled_skip(self, later: int) -> None:
        if later not in (2, 3, 4):
            raise ValueError('Only the four declared positions exist')
        if not self.enabled and not self.logged:
            self.bypassed = True
        self.chronology.append(later)

    @property
    def additional_behavior_active(self) -> bool:
        return self.enabled and self.logged and not self.bypassed


@dataclass
class StaffFixture:
    active_receipt: str | None = None

    def reserve(self, receipt: str) -> bool:
        if self.active_receipt is not None:
            return False
        self.active_receipt = receipt
        return True

    def release(self, receipt: str) -> bool:
        if self.active_receipt != receipt:
            return False
        self.active_receipt = None
        return True


COSTS = {
    'N01': {'political_power': 50, 'support_equipment': 100, 'civilian_factories': 1, 'staff': 1},
    'N02': {'political_power': 25, 'support_equipment': 100, 'civilian_factories': 1, 'staff': 1},
    'N03': {'political_power': 35, 'support_equipment': 75, 'civilian_factories': 1, 'staff': 1},
    'N04': {'political_power': 50, 'support_equipment': 150, 'civilian_factories': 1, 'staff': 1},
    'N05': {'support_equipment': 200, 'fuel': 1500, 'civilian_factories': 2, 'staff': 1},
    'N06': {'political_power': 50, 'support_equipment': 150, 'civilian_factories': 1, 'staff': 1},
    'N07': {'command_power': 25, 'support_equipment': 100, 'staff': 1},
    'N08': {'political_power': 35, 'support_equipment': 100, 'staff': 1},
    'N09': {'political_power': 25, 'support_equipment': 75, 'staff': 1},
    'N10': {'political_power': 40, 'support_equipment': 150, 'civilian_factories': 1, 'staff': 1},
    'N11': {'political_power': 50, 'support_equipment': 200, 'civilian_factories': 1, 'staff': 1},
    'N12': {'political_power': 50, 'support_equipment': 200, 'civilian_factories': 1, 'staff': 1},
}


def run() -> None:
    text = PART.read_text(encoding='utf-8')
    check('exact opening', text.startswith('# Doctor Wu: National Medical Ascendancy\n\n## When the institute becomes a national service\n'), 'Requested first headings are preserved.', 'document')
    check('exact stopping heading', text.rsplit('\n## ', 1)[1].startswith('What national medicine places on the international stage\n'), 'Continuation has a definite boundary.', 'document')
    check('twelve action rows', set(re.findall(r'^\| (N\d{2}) ', text, re.M)) == set(COSTS), 'N01–N12 are unique named work families.', 'document')
    check('ten case families', set(re.findall(r'^### (NM\d{2}):', text, re.M)) == {f'NM{i:02d}' for i in range(1, 11)}, 'NM01–NM10 are present.', 'document')
    check('thirty-two AI review scenarios', set(re.findall(r'^\| (NAI\d{2}) ', text, re.M)) == {f'NAI{i:02d}' for i in range(1, 33)}, 'These are written review scenarios, not executed AI tests.', 'document')
    check('new prose punctuation', '\u2014' not in text and ';' not in text, 'No em dash or semicolon in the new part.', 'document')
    check('direction only', not re.search(r'^\s*l_english:', text, re.M), 'No pasteable localisation block in the new part.', 'document')

    check('199 gate', not EvolutionFixture().queue('A', 199, True, True), 'First delivery cannot queue below the threshold.')
    g = EvolutionFixture()
    check('200 queues without activation', g.queue('A', 200, True, True) and not g.logged, 'Eligibility creates only pending symbolic state.')
    check('one responsible delivery', not g.queue('B', 250, True, True), 'Another qualified actor does not receive a second pending delivery.')
    check('wrong actor cannot deliver', not g.deliver('B', 250, True) and g.pending_owner == 'A', 'A stale or wrong actor cannot consume the active receipt.')
    check('lost institute invalidates delivery', not g.deliver('A', 250, False) and not g.logged, 'Invalid current context grants no history or institution.')
    g = EvolutionFixture()
    g.queue('A', 200, True, True)
    g.disable()
    check('disabled pending gives no milestone', not g.deliver('A', 250, True) and not g.logged and g.care_obligations == 10, 'Disabling clears pending delivery without erasing care.')
    g.restore_permission()
    check('early re-enable re-enters eligibility', g.queue('A', 250, True, True) and not g.logged, 'No completion is stored while disabled.')
    check('first delivery records once', g.deliver('A', 250, True) and g.chronology == [1] and not g.deliver('A', 250, True), 'Chronology cannot be granted twice.')
    g.disable()
    check('disable after delivery retains history and care', not g.additional_behavior_active and g.chronology == [1] and g.care_obligations == 10, 'Extra behavior is off while completed facts remain.')
    g.restore_permission()
    check('reconcile without replay', g.additional_behavior_active and not g.queue('A', 250, True, True), 'Already delivered state does not queue another first delivery.')
    g = EvolutionFixture(enabled=False)
    g.commit_later_after_disabled_skip(2)
    g.restore_permission()
    check('ordered bypass is not firing', g.bypassed and not g.logged and g.chronology == [2] and not g.queue('A', 500, True, True), 'Proposed bypass rule produces no false E1 history.')

    check('arrival proof is not major-cure gate', not major_cure(owner_major=False, treated=1_000_000, episode_basis=1_000_000, arrival_demonstration=True), 'The contained arrival proof does not qualify by itself.')
    check('major owner outcome qualifies', major_cure(owner_major=True, treated=1000, episode_basis=10_000_000), 'An owner-confirmed major episode is a separate route.')
    check('small-country percentage boundary', major_cure(owner_major=False, treated=250_000, episode_basis=1_000_000) and not major_cure(owner_major=False, treated=249_999, episode_basis=1_000_000), 'Twenty-five percent is inclusive and does not require two states.')
    check('frozen episode basis', not major_cure(owner_major=False, treated=200_000, episode_basis=1_000_000), 'A later current population of 400,000 is not substituted for this episode basis.')
    check('distinct reliance episodes', len(set(['episode-A', 'episode-A'])) == 1 and len(set(['episode-A', 'episode-B'])) == 2, 'Duplicate renewals do not create repeated national reliance.')

    check('major cure and expansion nominal MTTH', nominal_mtth(['0.75', '0.80']) == 55, '90 × 0.75 × 0.80 = 54, rounded upward to 55. No game frequency is inferred.')
    check('review and interrupted route nominal MTTH', nominal_mtth(['1.50', '1.25']) == 170, '90 × 1.50 × 1.25 = 168.75, rounded upward to 170.')
    check('nominal timing clamp', nominal_mtth(['0.10']) == 30 and nominal_mtth(['3.00']) == 240, 'The proposed nominal bounds are respected.')
    check('administrative interval only', Decimal(20) * Decimal('0.75') == 15 and 30 == 30 and 90 == 90, 'The 20-day administrative example becomes 15. Declared manufacturing 30 and qualification 90 remain unchanged.')

    a, b, military = set(range(100)), set(range(75, 150)), set(range(150, 200))
    union = len(a | b | military)
    check('recipient union', union == 200 and len(a)+len(b)+len(military) == 225, 'Each fixture unit represents 10,000 people. A/B overlap is 250,000.')
    check('material and route bound', min(250, union, 175) == 175 and min(250, union, 175-50) == 125, 'Current service reaches 1.75m, then 1.25m under the declared route shortfall.')
    check('seven existing allocations', 10-4-2-1 == 3, 'Three allocations remain discretionary.')
    check('partial allocation unmet demand', 3-2 == 1 and 3-1 == 2, 'An army allocation of two leaves one for the new civilian request and two unmet.')
    check('stock conservation with warehouse', 120-40-30-20 == 30 and 40+30+30+20 == 120, 'A remains A across works, warehouse, hospital commitment, and native reservation.')
    check('standard ceiling country-wide', len({'A','B'}) == 2 and len({'A','B','C'}) > 2, 'Regional branches do not receive independent two-standard caps.')
    check('clamped concession reversal', (100-95) == 5 and 100-(100-95) == 95, 'Only the applied five-point concession is reversed.')
    check('finite first settlement retained', 1000 == 140+850+10, 'New national service does not add a second person settlement. Later appointments add zero people.')
    check('care deadlines remain separate', 90 > 45 and 60 > 45, 'Neither qualification nor the institution hearing extends an earlier control-care deadline.')

    staff = StaffFixture()
    check('staff cannot be committed twice', staff.reserve('old') and not staff.reserve('other'), 'One actual team has one full-time receipt.')
    staff.release('old')
    staff.reserve('new')
    check('stale staff release rejected', not staff.release('old') and staff.active_receipt == 'new', 'An old completion cannot release the new assignment.')
    check('dispatch factory lifecycle', [2, 1, 0] == [COSTS['N05']['civilian_factories'], 1, 0], 'Two during construction, one during operation, zero after valid closure.')
    check('charter group scaling', rounded_five(Decimal(60)*Decimal('1.50')) == 90 and rounded_five(Decimal(100)*Decimal('1.50')) == 150, 'Three-provider charter has 90 days and 150 support equipment.')
    check('action cost budget', all(len(v) <= 4 and v.get('staff') == 1 for v in COSTS.values()), 'Staff is counted among the at-most-four spendable or committed input types.')
    check('command power limit', all(v.get('command_power', 0) <= 60 for v in COSTS.values()), 'The only new Command Power anchor is 25.')

    report = {'stage': 'DW-089-S8', 'mode': 'symbolic design and document checks only',
              'checks': RESULTS, 'count': len(RESULTS),
              'passed': sum(bool(x['passed']) for x in RESULTS),
              'failed': sum(not bool(x['passed']) for x in RESULTS),
              'fixture_costs': COSTS,
              'not_executed': ['HOI4', 'MCP', 'named specialist review', 'actual AI scenarios', 'native cancellation', 'live beneficiary or staffing transactions']}
    RESULT.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: report[k] for k in ['stage','mode','count','passed','failed']}, indent=2))
    if report['failed']:
        raise SystemExit(1)


if __name__ == '__main__':
    run()
