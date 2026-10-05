"""Source-contract tests for ordinary missile preparation, not engine simulation.

Checks the actual nested transaction, native mission wiring, inclusive resource
boundaries, timer arithmetic, and the bounded human selector's visible phases.
Probability/engine acceptance remains the separate HOI4 MCP and live-QA route.
"""
from pathlib import Path
from decimal import Decimal
import unittest
from test_event32_recipient_scope import parse, value, descendants

ROOT = Path(__file__).resolve().parents[1]


def source(path):
    return dict(parse((ROOT / path).read_text(encoding='utf-8-sig')))


EFFECTS = source('common/scripted_effects/032_missiles_operations_effects.txt')
TRIGGERS = source('common/scripted_triggers/032_missiles_operations_triggers.txt')
COSTS = source('common/scripted_triggers/032_missiles_preparation_cost_triggers.txt')
CONSTANTS = source('common/script_constants/032_missiles_constants.txt')
DECISIONS = dict(source('common/decisions/032_missiles_decisions.txt')['missiles_program_management_category'])
MISSION_FILE = source('common/decisions/032_missiles_missions.txt')
MISSIONS = dict(MISSION_FILE['missiles_program_management_category'])
ROUTES = {
    'precision': ('precision_strike', 'precision_strike'),
    'strategic': ('strategic_barrage', 'strategic_barrage'),
    'saturation': ('saturation_barrage', 'saturation_barrage'),
    'counterforce': ('counterforce_strike', 'counterforce_strike'),
}


def number(token):
    if token.startswith('constant:'):
        group, field = token[9:].split('.', 1)
        token = value(CONSTANTS[group], field)
    return Decimal(token)


def afford(route, balances, special=False):
    """Evaluate only the documented, read-only affordability helper's inputs."""
    parameters = {field: number(token) for k, body in COSTS[f'missiles_can_afford_{route}_preparation'] if k == 'set_temp_variable' for field, token in body}

    def operand(token):
        if token.startswith('constant:'):
            return number(token)
        return parameters[token] if token in parameters else Decimal(str(balances[token]))

    def term(key, body):
        if key in ('AND', 'hidden_trigger'):
            return all(term(k, v) for k, v in body)
        if key == 'OR':
            return any(term(k, v) for k, v in body)
        if key == 'NOT':
            return not any(term(k, v) for k, v in body)
        if key == 'missiles_preparation_has_special_payload':
            return special
        if key == 'check_variable':
            fields = dict(body)
            left, right = operand(fields['var']), operand(fields['value'])
            if fields['compare'] == 'greater_than':
                return left > right
            assert fields['compare'] == 'greater_than_or_equals'
            return left >= right
        raise AssertionError(f'Unmodeled affordability input: {key}')

    return all(term(k, v) for k, v in COSTS['missiles_can_afford_preparation'])


class OrdinaryPreparationContract(unittest.TestCase):
    def test_shared_affordability_is_inclusive_and_fresh(self):
        for route in ROUTES:
            params = {field: token for k, body in COSTS[f'missiles_can_afford_{route}_preparation'] if k == 'set_temp_variable' for field, token in body}
            for special in (False, True):
                balances = {
                    'command_power': number(params['missiles_preparation_command_quote']),
                    'fuel_k': number(params['missiles_preparation_fuel_quote']),
                    'num_equipment@support_equipment': number(params['missiles_preparation_support_quote']),
                    'missiles_operational_reserve': number(params['missiles_preparation_special_quote' if special else 'missiles_preparation_base_quote']),
                }
                with self.subTest(route=route, special=special):
                    self.assertTrue(afford(route, balances, special))
                    for field in balances:
                        step = Decimal('.001') if field == 'fuel_k' else Decimal('1')
                        self.assertFalse(afford(route, {**balances, field: balances[field] - step}, special), field)
        self.assertFalse(any('reserve_cost' in str(body) for _, body in descendants(COSTS['missiles_can_afford_preparation'])))

    def test_special_quotes_match_actual_operation_cost(self):
        for route in ROUTES:
            quoted = number(f'constant:missiles_preparation_cost.{route}_special_reserve')
            actual = number(f'constant:missiles_tuning.operation_{route}_missiles') + number('constant:missiles_tuning.operation_special_missiles')
            self.assertEqual(quoted, actual)

    def test_disabled_special_track_does_not_lock_retained_selection_into_new_orders(self):
        self.assertIn(('missiles_special_warheads_active', 'yes'), COSTS['missiles_preparation_has_special_payload'])
        copy = value(EFFECTS['missiles_prepare_operation_payload'], 'if')
        self.assertIn(('missiles_special_warheads_active', 'yes'), value(copy, 'limit'))
        fallback = value(EFFECTS['missiles_prepare_operation_payload'], 'else')
        self.assertEqual(value(fallback, 'set_variable'), [('missiles_operation_payload', 'constant:missiles_payload.conventional')])
        self.assertEqual(value(value(EFFECTS['missiles_refresh_operation_cost_preview'], 'if'), 'limit'), [('missiles_preparation_has_special_payload', 'yes')])

    def test_four_transactions_pay_only_after_accepted_preflight(self):
        for route, (action, mission) in ROUTES.items():
            decision = DECISIONS[f'missiles_prepare_{action}']
            affordability = f'missiles_can_afford_{route}_preparation'
            self.assertEqual(value(decision, 'custom_cost_trigger'), [(affordability, 'yes')])
            self.assertIn((affordability, 'yes'), list(descendants(value(decision, 'available'))))
            outer = value(value(value(decision, 'complete_effect'), 'hidden_effect'), 'if')
            self.assertIn((affordability, 'yes'), value(outer, 'limit'))
            self.assertLess([k for k, _ in outer].index(f'missiles_prepare_{action}'), [k for k, _ in outer].index('if'))
            accepted = value(outer, 'if')
            result = dict(value(value(accepted, 'limit'), 'check_variable'))
            self.assertEqual(result, {'var': 'missiles_operation_preflight_result', 'value': 'constant:missiles_result.accepted', 'compare': 'equals'})
            for fee in ('add_command_power', 'add_fuel', 'add_equipment_to_stockpile'):
                self.assertEqual(sum(k == fee for k, _ in accepted), 1)
                self.assertEqual(sum(k == fee for k, _ in descendants(outer)), 1)
            self.assertEqual(value(accepted, 'missiles_activate_preparation_mission'), 'yes')
            self.assertNotIn('days_re_enable', dict(decision))
            self.assertIn('set_country_flag', dict(accepted))

    def test_missions_set_ready_instead_of_waiting_for_it(self):
        for route, (_, mission) in ROUTES.items():
            body = MISSIONS[f'missiles_{mission}_preparation_mission']
            self.assertIn(('missiles_operation_preparation_is_due', 'yes'), value(body, 'available'))
            self.assertNotIn(('has_country_flag', 'missiles_operation_ready'), list(descendants(value(body, 'available'))))
            self.assertIn(('missiles_complete_preparation', 'yes'), list(descendants(value(body, 'complete_effect'))))
            cancellation = list(descendants(value(body, 'cancel_trigger')))
            self.assertIn(('missiles_operation_preparation_remains_valid', 'yes'), cancellation)
            self.assertNotIn(('missiles_country_can_prepare_operation', 'yes'), cancellation)
            self.assertFalse(any(k == 'has_event_target' for k, _ in cancellation))

    def test_timer_arithmetic_tracks_every_supported_duration(self):
        activation = value(EFFECTS['missiles_activate_preparation_mission'], 'if')
        self.assertEqual(dict(value(activation, 'set_temp_variable'))['missiles_mission_timeout_adjustment'], 'missiles_operation_preparation_days')
        anchor = number('constant:missiles_tuning.operation_mission_anchor_days')
        grace = number('constant:missiles_tuning.operation_mission_deadline_grace_days')
        self.assertEqual(number(MISSION_FILE['@m32_mission_operation_anchor_days']), anchor)
        for days in range(10, 46):
            self.assertEqual(anchor + (Decimal(days) - anchor + grace), Decimal(days) + grace)
        self.assertEqual(grace, 1)
        literals = {v for k, v in descendants(activation) if k == 'activate_mission'}
        self.assertEqual(literals, {f'missiles_{mission}_preparation_mission' for _, mission in ROUTES.values()})
        cleanup = value(EFFECTS['missiles_cleanup_operation'], 'if')
        self.assertEqual({v for k, v in cleanup if k == 'remove_mission'}, {f'missiles_{mission}_preparation_mission' for _, mission in ROUTES.values()})

    def test_launch_and_mission_share_receipt_validity(self):
        requirements = dict(TRIGGERS['missiles_operation_preparation_remains_valid'])
        for name in ('missiles_operation_before_commitment', 'missiles_operation_tracks_are_enabled', 'missiles_selected_target_state_is_valid', 'missiles_operation_has_valid_site', 'missiles_operation_has_reliable_payload_custody'):
            self.assertEqual(requirements[name], 'yes')
        self.assertEqual(dict(TRIGGERS['missiles_operation_can_be_committed'])['missiles_operation_preparation_remains_valid'], 'yes')
        self.assertIn(('missiles_operation_can_be_committed', 'yes'), list(descendants(value(DECISIONS['missiles_launch_prepared_operation'], 'available'))))

    def test_failure_reason_precedes_abort_and_scope_cleanup(self):
        transaction = value(EFFECTS['missiles_cancel_preparation'], 'if')
        keys = [k for k, _ in transaction]
        self.assertLess(keys.index('missiles_record_preparation_failure'), keys.index('missiles_abort_operation'))
        self.assertLess(keys.index('missiles_abort_operation'), keys.index('missiles_cleanup_operation'))
        for _, (_, mission) in ROUTES.items():
            for outcome in ('cancel_effect', 'timeout_effect'):
                self.assertIn(('missiles_cancel_preparation', 'yes'), list(descendants(value(MISSIONS[f'missiles_{mission}_preparation_mission'], outcome))))
        cleanup = value(EFFECTS['missiles_cleanup_operation'], 'if')
        self.assertIn(('missiles_back_to_target_profiles', 'yes'), cleanup)
        self.assertNotIn(('clear_variable', 'missiles_last_preparation_failure'), cleanup)

    def test_nonoperation_missions_cannot_abort_a_successor_launch(self):
        ordinary = {f'missiles_{mission}_preparation_mission' for _, mission in ROUTES.values()}
        for mission, body in MISSIONS.items():
            if mission in ordinary:
                continue
            for outcome in ('cancel_effect', 'timeout_effect'):
                calls = list(descendants(value(body, outcome)))
                self.assertFalse(any(k in ('missiles_abort_operation', 'missiles_cleanup_operation', 'missiles_cancel_preparation') for k, _ in calls), (mission, outcome))
                for key, _ in calls:
                    if key in EFFECTS:
                        self.assertFalse(any(k in ('missiles_abort_operation', 'missiles_cleanup_operation') for k, _ in descendants(EFFECTS[key])))

    def test_precision_gate_and_saturation_capacity_are_enforced_before_escrow(self):
        command = list(descendants(TRIGGERS['missiles_operation_command_is_operational']))
        self.assertTrue(any(k == 'check_variable' and dict(v).get('value') == 'constant:missiles_program_value.precision_readiness_gate' for k, v in command))
        preflight = value(EFFECTS['missiles_preflight_operation'], 'if')
        conditions = list(descendants(value(preflight, 'limit')))
        self.assertIn(('missiles_operation_command_is_operational', 'yes'), conditions)
        for threshold in ('operation_saturation_min_sites', 'operation_saturation_min_capacity'):
            self.assertTrue(any(k == 'check_variable' and dict(v).get('value') == f'constant:missiles_tuning.{threshold}' for k, v in conditions))
        self.assertIn(('any_of_scopes', [('array', 'missiles_operation_sites'), ('is_controlled_by', 'ROOT')]), TRIGGERS['missiles_operation_sites_remain_valid'])

    def test_state_selector_owns_from_scope_not_preparation_buttons(self):
        selector = dict(DECISIONS['missiles_select_target_state'])
        self.assertEqual(selector['state_target'], 'yes')
        self.assertEqual(selector['target_array'], 'missiles_target_selection_page')
        for _, (action, _) in ROUTES.items():
            body = DECISIONS[f'missiles_prepare_{action}']
            self.assertNotIn('state_target', dict(body))
            self.assertFalse(any(k == 'FROM' for k, _ in descendants(body)))
        selected = value(EFFECTS['missiles_select_operation_target_state'], 'if')
        self.assertIn(('has_variable', 'missiles_pending_target_state'), value(selected, 'limit'))
        self.assertIn(('missiles_operation_target_state', 'PREV'), list(descendants(selected)))

    def test_launch_site_api_never_treats_country_from_as_a_state(self):
        sites = list(descendants(EFFECTS['missiles_select_operation_site']))
        self.assertFalse(any(k == 'FROM' for k, _ in sites))
        self.assertTrue(any(k == 'var:missiles_requested_launch_site' for k, _ in sites))
        self.assertIn(('clear_variable', 'missiles_operation_launch_site'), EFFECTS['missiles_select_operation_site'])

    def test_counterforce_cannot_fall_through_to_broad_strategic(self):
        first = value(EFFECTS['missiles_select_operation_profile'], 'if')
        self.assertEqual(dict(value(value(first, 'limit'), 'check_variable'))['value'], 'constant:missiles_operation.counterforce')
        self.assertEqual(dict(value(first, 'set_variable'))['missiles_operation_target_profile'], 'constant:missiles_target_profile.counterforce')
        self.assertIn(('set_country_flag', 'missiles_operation_target_profile_locked'), first)
        proof = list(descendants(TRIGGERS['missiles_counterforce_target_is_proven']))
        self.assertTrue(any(k == 'intel_level_over' for k, _ in proof))
        self.assertTrue(any(k == 'cw_facility' for k, _ in proof))

    def test_scripted_helpers_do_not_require_undocumented_argument_blocks(self):
        helpers = {**EFFECTS, **TRIGGERS, **COSTS}
        for definitions in (EFFECTS, TRIGGERS, COSTS, DECISIONS):
            for body in definitions.values():
                if not isinstance(body, list):
                    continue
                for key, token in descendants(body):
                    if key in helpers:
                        self.assertIn(token, ('yes', 'no'), key)
                    if isinstance(token, str):
                        self.assertNotRegex(token, r'\$[A-Z_]+\$')

    def test_site_receipt_is_positive_unchanged_and_projected_before_escrow(self):
        conditions = list(descendants(TRIGGERS['missiles_operation_sites_remain_valid']))
        self.assertIn(('has_variable', 'missiles_site_operation_allocation'), conditions)
        comparisons = [dict(v) for k, v in conditions if k == 'check_variable']
        self.assertIn({'var': 'missiles_site_operation_allocation', 'value': 'constant:missiles_program_value.zero', 'compare': 'greater_than'}, comparisons)
        self.assertIn({'var': 'missiles_site_operation_allocation', 'value': 'missiles_site_capacity', 'compare': 'less_than_or_equals'}, comparisons)
        self.assertIn({'var': 'missiles_site_operation_id', 'value': 'ROOT.missiles_active_operation_id', 'compare': 'equals'}, comparisons)
        fit = list(descendants(TRIGGERS['missiles_operation_projected_site_allocations_fit']))
        fit_checks = [dict(v) for k, v in fit if k == 'check_variable']
        self.assertIn({'var': 'missiles_operation_site_capacity', 'value': 'missiles_operation_missile_cost', 'compare': 'greater_than_or_equals'}, fit_checks)
        self.assertIn({'var': 'missiles_operation_allocation_result', 'value': 'constant:missiles_result.accepted', 'compare': 'equals'}, fit_checks)
        # The first if divides the quote; the later guarded branch performs escrow.
        payment = next(v for k, v in EFFECTS['missiles_reserve_operation_resources'] if k == 'if' and ('missiles_reserve_for_operation', 'yes') in v)
        self.assertIn(('missiles_operation_projected_site_allocations_fit', 'yes'), value(payment, 'limit'))

    def test_random_fallback_never_overwrites_a_scored_best(self):
        def visit(nodes, guards=()):
            for key, body in nodes:
                if key == 'random_owned_controlled_state':
                    self.assertTrue(any(dict(v).get('var') == 'missiles_target_state_selection_result' and dict(v).get('value') == 'constant:missiles_program_value.zero' for k, v in guards if k == 'check_variable'))
                if isinstance(body, list):
                    extra = tuple(descendants(value(body, 'limit'))) if key == 'if' and 'limit' in dict(body) else ()
                    visit(body, guards + extra)
        visit(EFFECTS['missiles_select_operation_target_state'])

    def test_three_object_pages_cover_a_frozen_pool_without_duplicates(self):
        size = int(number('constant:missiles_tuning.operation_target_page_size'))
        self.assertEqual(size, 3)
        for count in (0, 1, 3, 4, 9, 40):
            pool = list(range(count))
            pages = [pool[offset:offset + size] for offset in range(0, count, size)]
            self.assertEqual([obj for page in pages for obj in page], pool)
            self.assertTrue(all(len(page) + 2 + 1 <= 6 for page in pages))
        # Two family choices + clear; three profile choices + back + clear;
        # four preparations + optional integration + clear.
        self.assertLessEqual(max(2 + 1, 3 + 1 + 1, 4 + 1 + 1), 6)


def project_allocations(cost, capacities, passes):
    """Python model of missiles_project_operation_site_allocations."""
    planned = [0] * len(capacities)
    remaining = cost
    for _ in range(passes):
        open_sites = [i for i, cap in enumerate(capacities) if planned[i] < cap]
        if remaining <= 0 or not open_sites:
            break
        exact = Decimal(remaining) / Decimal(len(open_sites))
        share = int(exact.to_integral_value(rounding='ROUND_HALF_UP'))
        if share > exact:
            share -= 1
        share = max(share, 1)
        for i in open_sites:
            if remaining <= 0:
                break
            give = min(share, capacities[i] - planned[i], remaining)
            planned[i] += give
            remaining -= give
    return planned, remaining


class WholeMissileAllocation(unittest.TestCase):
    PASSES = int(number('constant:missiles_tuning.operation_max_sites_per_strike')) + 1

    def test_projection_steps_match_the_model(self):
        body = EFFECTS['missiles_project_operation_site_allocations']
        nodes = list(descendants(body))
        loop = value(body, 'for_loop_effect')
        self.assertEqual(value(loop, 'end'), 'constant:missiles_tuning.operation_max_sites_per_strike')
        self.assertEqual(value(loop, 'compare'), 'less_than_or_equals')
        self.assertIn(('round_temp_variable', 'missiles_allocation_share'), nodes)
        self.assertIn(('subtract_from_temp_variable', [('missiles_allocation_remaining', 'missiles_allocation_give')]), nodes)
        self.assertIn(('add_to_variable', [('missiles_site_planned_allocation', 'missiles_allocation_give')]), nodes)
        self.assertNotIn('divide_variable', [k for k, _ in descendants(EFFECTS['missiles_reserve_operation_resources'])])
        marked = list(descendants(EFFECTS['missiles_mark_operation_sites_reserved']))
        self.assertIn(('missiles_site_operation_allocation', 'missiles_site_planned_allocation'), marked)
        self.assertIn(('remove_from_array', [('array', 'missiles_operation_sites'), ('value', 'PREV')]), marked)

    def test_uneven_capacities_fill_whole_missiles_exactly(self):
        cases = [
            (10, [10, 2]), (10, [2, 10]), (7, [4, 4]), (9, [6, 6, 6]), (24, [10, 8, 6, 4]),
            (3, [10, 10, 10, 10]), (5, [1, 1, 1, 10]), (12, [10, 2]), (16, [6, 4, 4, 4]),
        ]
        for cost, capacities in cases:
            with self.subTest(cost=cost, capacities=capacities):
                planned, remaining = project_allocations(cost, capacities, self.PASSES)
                self.assertEqual(remaining, 0)
                self.assertEqual(sum(planned), cost)
                self.assertTrue(all(isinstance(a, int) and 0 <= a <= cap for a, cap in zip(planned, capacities)))
        # The old equal split rejected 10 missiles over capacities 10 and 2.
        self.assertGreater(Decimal(10) / 2, 2)
        self.assertEqual(project_allocations(10, [10, 2], self.PASSES)[0], [8, 2])

    def test_capacity_shortfall_is_refused(self):
        planned, remaining = project_allocations(13, [10, 2], self.PASSES)
        self.assertGreater(remaining, 0)

    def test_lost_reserving_site_settles_its_allocation_once(self):
        settle = EFFECTS['missiles_settle_lost_site_allocation']
        guarded = value(settle, 'if')
        keys = [k for k, _ in guarded]
        self.assertLess(keys.index('missiles_abort_operation'), keys.index('missiles_cleanup_operation'))
        loss = list(descendants(guarded))
        self.assertIn(('subtract_from_variable', [('missiles_operational_reserve', 'missiles_lost_allocation')]), loss)
        self.assertIn(('NOT', [('has_country_flag', 'missiles_operation_committed')]), value(guarded, 'limit'))
        for caller in ('missiles_handle_site_control_changed', 'missiles_scuttle_site', 'missiles_scuttle_site_from_current_controller', 'missiles_apply_natural_disaster_site_damage'):
            self.assertIn(('missiles_settle_lost_site_allocation', 'yes'), list(descendants(EFFECTS[caller])), caller)


if __name__ == '__main__':
    unittest.main()
