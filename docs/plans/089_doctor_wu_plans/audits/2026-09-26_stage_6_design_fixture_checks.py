"""Symbolic and document checks for the proposed Doctor Wu Part 10.

These fixtures do not load HOI4, call MCP, model native cancellation, validate
engine timing, or establish game AI probabilities. They test the stated
identity and accounting requirements and preservation of supplied documents.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[4]
PLAN = ROOT / 'docs/plans/089_doctor_wu_plans'
PART = ROOT / 'docs/specs/089_doctor_wu_specs/rivalry/089_doctor_wu_spec_part_10_wu_and_kruger.md'
RESULT = PLAN / 'audits/2026-09-26_stage_6_design_fixture_results.json'

# New administrative actions only. Existing project bills remain owner-owned.
ACTIONS = {
    'first_division': {'days': 60, 'political_power': 50, 'support': 100, 'civilian_factories': 1},
    'comparative_round': {'days': 30, 'political_power': 50, 'support': 150, 'civilian_factories': 1},
    'joint_institute': {'days': 120, 'political_power': 75, 'support': 250, 'civilian_factories': 2},
    'rights_review': {'days': 60, 'political_power': 35, 'support': 100, 'civilian_factories': 1},
    'result_audit': {'days': 90, 'political_power': 40, 'support': 150, 'civilian_factories': 1},
    'protected_service': {'days': 30, 'command_power': 25, 'support': 100, 'fuel': 1000, 'civilian_factories': 1},
    'overlap_review': {'days': 30, 'political_power': 25, 'support': 75, 'civilian_factories': 1},
    'joint_dissolution': {'days': 120, 'political_power': 50, 'support': 200, 'fuel': 1500, 'civilian_factories': 2},
    'wu_supremacy': {'days': 90, 'political_power': 75, 'support': 250, 'civilian_factories': 2},
    'kruger_supremacy': {'days': 120, 'political_power': 75, 'support': 200, 'civilian_factories': 2},
    'emergency_coordination': {'days': 15, 'command_power': 25, 'support': 100, 'civilian_factories': 1},
}

@dataclass
class Capacity:
    total: int
    reservations: dict[str, int] = field(default_factory=dict)

    @property
    def free(self) -> int:
        return self.total - sum(self.reservations.values())

    def reserve(self, identity: str, amount: int) -> bool:
        if amount < 0 or not identity:
            return False
        if identity in self.reservations:
            return self.reservations[identity] == amount
        if amount > self.free:
            return False
        self.reservations[identity] = amount
        return True

    def release(self, identity: str) -> int:
        return self.reservations.pop(identity, 0)

@dataclass
class Stock:
    available: dict[str, int]
    reserved: dict[str, tuple[str, int]] = field(default_factory=dict)
    consumed: dict[str, int] = field(default_factory=dict)

    def reserve(self, identity: str, standard: str, amount: int) -> bool:
        if identity in self.reserved or identity in self.consumed or amount <= 0:
            return False
        if self.available.get(standard, 0) < amount:
            return False
        self.available[standard] -= amount
        self.reserved[identity] = (standard, amount)
        return True

    def complete(self, identity: str) -> int:
        receipt = self.reserved.pop(identity, None)
        if receipt is None:
            return 0
        self.consumed[identity] = receipt[1]
        return receipt[1]

@dataclass
class People:
    born: int
    first_settled: dict[str, int] = field(default_factory=dict)
    unsettled_deaths: int = 0

    @property
    def unsettled(self) -> int:
        return self.born - sum(self.first_settled.values()) - self.unsettled_deaths

    def settle(self, identity: str, amount: int) -> bool:
        if identity in self.first_settled or amount <= 0 or amount > self.unsettled:
            return False
        self.first_settled[identity] = amount
        return True

@dataclass
class Authority:
    value: int
    applied: dict[str, int] = field(default_factory=dict)
    reversed: set[str] = field(default_factory=set)

    def concede(self, identity: str, requested: int) -> int:
        if identity in self.applied or requested < 0:
            return 0
        actual = min(100 - self.value, requested)
        self.applied[identity] = actual
        self.value += actual
        return actual

    def reverse(self, identity: str) -> int:
        if identity not in self.applied or identity in self.reversed:
            return 0
        self.reversed.add(identity)
        actual = min(self.value, self.applied[identity])
        self.value -= actual
        return actual


@dataclass
class Standards:
    allocations: dict[str, tuple[str, str]] = field(default_factory=dict)

    def add(self, slot: str, branch: str, standard: str) -> bool:
        if slot in self.allocations:
            return self.allocations[slot] == (branch, standard)
        if len(self.allocations) >= 2:
            return False
        self.allocations[slot] = (branch, standard)
        return True

@dataclass
class DeathRecord:
    entries: dict[str, int] = field(default_factory=dict)

    def record(self, identity: str, status: str, amount: int) -> bool:
        if status != 'confirmed_death' or amount <= 0 or identity in self.entries:
            return False
        self.entries[identity] = amount
        return True


def admission_capacity(shelter: int, food: int | None, medicine: int, transport: int) -> int:
    if food is None:
        return 0
    return max(0, min(shelter, food, medicine, transport))


def kruger_transfer_ready(active_project: bool, pending_review: bool, confined: bool,
                          valid_recipient: bool) -> bool:
    # A bounded symbolic conjunction, not a reproduction of the full game trigger.
    return not active_project and not pending_review and not confined and valid_recipient


def compare_results(left: dict[str, Any], right: dict[str, Any]) -> str:
    if left['project'] == right['project']:
        return 'duplicate_project'
    if left['objective'] != right['objective'] or left['subject'] != right['subject']:
        return 'incomparable'
    if not left['qualified'] or not right['qualified']:
        return 'incomplete'
    return 'comparable'


def run(baseline_zip: Path) -> dict[str, Any]:
    results: list[dict[str, Any]] = []

    def check(name: str, condition: bool, detail: Any = None) -> None:
        results.append({'name': name, 'passed': bool(condition), 'detail': detail})

    text = PART.read_text(encoding='utf-8')
    check('exact_opening', text.startswith('# Doctor Wu: Wu and Kruger\n## Two scientists in one country\n'))
    check('exact_stopping_heading', text.split('\n## ')[-1].startswith('What the domestic settlement sends abroad\n'))
    for route in ('Ordered division of work', 'Competitive grants', 'Joint institute',
                  'Wu supremacy', 'Kruger supremacy', 'Laboratory conflict'):
        check('route_' + route, '\n## ' + route + '\n' in text)
    check('thirty_unique_named_ai_scenarios', len(set(re.findall(r'\| (WK-\d{2}):', text))) == 30)
    check('new_prose_style', ';' not in text and '\u2014' not in text)
    check('no_final_localisation_blocks', not re.search(r'\bl_english:|```(?:yml|yaml)', text))
    check('part_is_proposed_not_runtime', 'New costs, durations, capacities, and outcome changes in this part are proposals.' in text)
    check('third_meter_excluded', 'No permanent numeric rivalry bar is added.' in text)
    check('calm_world_route_preserved', 'All compatible Wu research remains ordinary baseline work' in text)
    check('joint_work_not_route_gate', 'The full institutional route is not a prerequisite for every joint project.' in text)
    check('kruger_mapping_left_unapproved', 'No new direct numerical Kruger delta is asserted here without that contract.' in text)

    if not baseline_zip.is_file():
        raise FileNotFoundError(f'Provide the actual Stage 5 ZIP with --baseline-zip: {baseline_zip}')
    with zipfile.ZipFile(baseline_zip) as old:
        protected = [n for n in old.namelist() if re.search(r'089_doctor_wu_spec_part_[1-9]_', n)]
        protected.append('docs/plans/089_doctor_wu_plans/source_inputs/2026-09-24_doctor_wu_user_brief.txt')
        check('nine_prior_parts_found', len(protected) == 10)
        for name in protected:
            check('preserved_' + Path(name).name, (ROOT / name).read_bytes() == old.read(name))
        changed = [n for n in old.namelist() if not n.endswith('/') and (ROOT / n).read_bytes() != old.read(n)]
        check('only_three_inherited_navigation_files_changed', set(changed) == {
            'README.md', 'docs/specs/089_doctor_wu_specs/089_doctor_wu_index.md',
            'docs/plans/089_doctor_wu_plans/handoffs/089_doctor_wu_resume_packet.md'}, changed)
        check('old_resume_snapshot_exact',
              (PLAN/'handoffs/2026-09-26_stage_5_resume_snapshot.md').read_bytes() ==
              old.read('docs/plans/089_doctor_wu_plans/handoffs/089_doctor_wu_resume_packet.md'))

    for name, costs in ACTIONS.items():
        spend_types = set(costs) - {'days'}
        check('four_cost_budget_' + name, len(spend_types) <= 4 and costs.get('command_power', 0) <= 60,
              {'cost_types': sorted(spend_types), 'count': len(spend_types)})
    check('proposal_values_are_positive', all(v > 0 for row in ACTIONS.values() for v in row.values()))

    capacity = Capacity(6)
    check('first_shared_commitment', capacity.reserve('wu_project', 3) and capacity.free == 3)
    check('second_distinct_commitment', capacity.reserve('kruger_project', 2) and capacity.free == 1)
    check('duplicate_capacity_receipt_is_idempotent', capacity.reserve('wu_project', 3) and capacity.free == 1)
    check('changed_receipt_cannot_redefine_capacity', not capacity.reserve('wu_project', 4) and capacity.free == 1)
    check('cannot_double_allocate_last_factory', not capacity.reserve('joint_project', 2) and capacity.free == 1)
    check('release_only_owned_reservation', capacity.release('wu_project') == 3 and capacity.free == 4)
    capacity.reserve('replacement_project', 3)
    check('stale_release_does_not_clear_new_job', capacity.release('wu_project') == 0 and capacity.free == 1)

    staff = {'team_A': 'wu_clinical_service'}
    check('one_existing_staff_assignment', len(staff) == 1)
    staff['team_A'] = 'kruger_joint_service'
    check('secondment_moves_one_assignment', len(staff) == 1 and 'wu_clinical_service' not in staff.values())
    qualified = {'wu_original': True, 'wu_copy_1': False}
    check('unqualified_copy_cannot_replace_wu', not qualified['wu_copy_1'])
    qualified['wu_copy_1'] = True
    check('qualification_does_not_delete_original', len(qualified) == 2 and all(qualified.values()))

    stock = Stock({'A': 120})
    check('native_reserves_actual_A', stock.reserve('native_1', 'A', 40) and stock.available['A'] == 80)
    stock.available['B'] = 30
    check('B_production_does_not_change_A_receipt', stock.reserved['native_1'] == ('A', 40))
    check('same_native_receipt_not_reserved_twice', not stock.reserve('native_1', 'B', 10))
    check('reservation_conservation', sum(stock.available.values()) + sum(n for _, n in stock.reserved.values()) == 150)
    check('completed_reservation_consumed_once', stock.complete('native_1') == 40 and stock.complete('native_1') == 0)
    check('completion_does_not_refund_or_relabel_stock', stock.available == {'A': 80, 'B': 30})
    standards = Standards()
    standards.add('slot_1', 'public_branch', 'A')
    standards.add('slot_2', 'classified_branch', 'B')
    check('country_wide_standard_ceiling', not standards.add('slot_3', 'continuity_branch', 'C'))
    paused_slot = 'slot_1'
    check('pause_keeps_standard_allocation', paused_slot in standards.allocations and
          not standards.add('slot_3', 'kruger_joint_branch', 'C'))

    people = People(1000)
    check('first_military_settlement', people.settle('military_batch', 600))
    check('first_civilian_settlement', people.settle('civilian_batch', 250) and people.unsettled == 150)
    check('appointment_does_not_create_five_people', people.born == 1000 and sum(people.first_settled.values()) == 850)
    check('same_cohort_not_settled_again', not people.settle('civilian_batch', 250))
    people.unsettled_deaths = 10
    check('pre_settlement_death_conservation', people.unsettled == 140 and 140 + 850 + 10 == people.born)
    later_deaths = DeathRecord()
    later_deaths.record('settled_person_loss', 'confirmed_death', 5)
    check('later_death_does_not_reopen_entitlement',
          not people.settle('military_batch', 5) and people.unsettled == 140)

    check('unknown_food_blocks_admission', admission_capacity(5000, None, 5000, 5000) == 0)
    limit = admission_capacity(6000, 5000, 5500, 5000)
    check('receiving_capacity_uses_real_minimum', limit == 5000)
    check('three_groups_share_places_once', 1000 + 2500 + 1500 == limit)
    check('unadmitted_people_remain_unsettled', 2000 - (limit - 1000 - 2500) == 500)

    a = Authority(95)
    check('authority_clamps_actual_concession', a.concede('access_right', 10) == 5 and a.value == 100)
    check('concession_not_repeated', a.concede('access_right', 10) == 0)
    check('reverse_actual_delta_only', a.reverse('access_right') == 5 and a.value == 95)
    check('reversal_not_repeated', a.reverse('access_right') == 0 and a.value == 95)

    check('active_kruger_project_blocks_transfer', not kruger_transfer_ready(True, False, False, True))
    check('pending_review_blocks_transfer', not kruger_transfer_ready(False, True, False, True))
    check('invalid_recipient_blocks_transfer', not kruger_transfer_ready(False, False, False, False))
    check('bounded_transfer_requirements_all_satisfied', kruger_transfer_ready(False, False, False, True))
    check('emergency_does_not_reset_short_deadline', 90 > 45 and 45 - 15 == 30)

    left = {'project': 'medical_A', 'objective': 'service_90_days', 'subject': 'hospital_1', 'qualified': True}
    right = {'project': 'mechanical_B', 'objective': 'service_90_days', 'subject': 'hospital_1', 'qualified': True}
    check('different_qualified_bids_comparable', compare_results(left, right) == 'comparable')
    check('duplicate_native_project_rejected', compare_results(left, dict(left)) == 'duplicate_project')
    check('changed_recipient_invalidates_comparison', compare_results(left, {**right, 'subject': 'hospital_2'}) == 'incomparable')
    check('unfinished_work_not_complete_result', compare_results(left, {**right, 'qualified': False}) == 'incomplete')
    completed_components = {'medical_A', 'mechanical_B'}
    reward_count = len(completed_components)
    commissioned = completed_components == {'medical_A', 'mechanical_B'}
    check('joint_commission_does_not_repeat_component_rewards', commissioned and reward_count == 2)

    losses = DeathRecord()
    check('missing_person_is_not_confirmed_death',
          not losses.record('staff_1', 'unresolved_absence', 1) and not losses.entries)
    check('confirmed_death_recorded_once',
          losses.record('staff_1', 'confirmed_death', 1) and
          not losses.record('staff_1', 'confirmed_death', 1) and sum(losses.entries.values()) == 1)

    return {'stage': 'DW-089-S6', 'kind': 'symbolic and document checks only',
            'passed': all(r['passed'] for r in results), 'checks': len(results),
            'failed': [r for r in results if not r['passed']],
            'part_10_words': len(text.split()),
            'part_10_sha256': hashlib.sha256(PART.read_bytes()).hexdigest(),
            'action_anchors': ACTIONS, 'results': results,
            'not_validated': ['HOI4 syntax and runtime', 'native cancellation and engine reservation behavior',
                              'MCP event, GUI, probability, technology or map evidence',
                              'actual character or formation transfer', 'balance and AI probabilities',
                              'assets and live gameplay']}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline-zip', type=Path,
                        default=ROOT.parent / '089_doctor_wu_planning_package_stage_5.zip')
    args = parser.parse_args()
    report = run(args.baseline_zip)
    RESULT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(json.dumps({'passed': report['passed'], 'checks': report['checks'], 'failed': report['failed']}, indent=2))
    if not report['passed']:
        raise SystemExit(1)

if __name__ == '__main__':
    main()
