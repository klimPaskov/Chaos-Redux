"""Source-level shared-toggle and retained-adoption contract tests.

Evaluates only documented boolean trigger composition and the explicit gate
variables. It does not simulate HOI4 decisions, stockpiles, or probabilities.
"""
from pathlib import Path
import re
import unittest
from test_event32_recipient_scope import parse, value, descendants, CONSTANTS, reserve_package

ROOT_DIR = Path(__file__).resolve().parents[1]
GENERAL = dict(parse((ROOT_DIR / 'common/scripted_triggers/032_missiles_triggers.txt').read_text(encoding='utf-8-sig')))
OPERATIONS = dict(parse((ROOT_DIR / 'common/scripted_triggers/032_missiles_operations_triggers.txt').read_text(encoding='utf-8-sig')))
DEFINITIONS = {**GENERAL, **OPERATIONS}
TRACKS = (
    ('saturation', 'missiles_evolution_saturation_arsenals'),
    ('guidance_evolution', 'missiles_evolution_unreliable_guidance'),
    ('special_warheads', 'missiles_evolution_special_warheads'),
    ('rogue_commands', 'missiles_evolution_rogue_launch_commands'),
    ('automatic_retaliation', 'missiles_evolution_automatic_retaliation'),
)


def constant(token):
    group, key = token[9:].split('.', 1)
    return float(value(CONSTANTS[group], key))


def evaluate(name, disabled, flags, variables=None):
    variables = variables or {}

    def operand(token):
        return constant(token) if token.startswith('constant:') else variables.get(token, float(token) if token.replace('.', '', 1).isdigit() else None)

    def term(key, body):
        if key in ('hidden_trigger', 'AND'):
            return all(term(k, v) for k, v in body)
        if key == 'OR':
            return any(term(k, v) for k, v in body)
        if key == 'NOT':
            return not any(term(k, v) for k, v in body)
        if key == 'has_global_flag':
            return body in disabled
        if key == 'has_country_flag':
            return body in flags
        if key == 'check_variable':
            fields = dict(body)
            left, right = operand(fields['var']), operand(fields['value'])
            if fields.get('compare', 'equals') != 'equals':
                raise AssertionError('Gate test requires explicit support for this comparison')
            return left == right
        if key in DEFINITIONS:
            return all(term(k, v) for k, v in DEFINITIONS[key])
        raise AssertionError(f'Unbound gate input {key}')

    return term(name, 'yes')


class EvolutionGateContract(unittest.TestCase):
    def setUp(self):
        self.flags = {flag for _, flag in TRACKS}

    def test_shared_toggle_suspends_each_retained_adoption(self):
        shared = (ROOT_DIR / 'common/scripted_effects/chaosx_events_log_effects.txt').read_text(encoding='utf-8-sig')
        self.assertIn('events_log_disabled_evolution_[EVOLUTION_EVENT_ID]_[EVOLUTION_TYPE]_[EVOLUTION_STAGE]', shared)
        for track_type, (name, _) in enumerate(TRACKS, 1):
            with self.subTest(track=name):
                helper = f'missiles_{name}_active'
                self.assertTrue(evaluate(helper, set(), self.flags))
                self.assertFalse(evaluate(helper, {f'events_log_disabled_evolution_32_{track_type}_1'}, self.flags))

    def test_special_custody_cannot_override_disabled_track(self):
        flags = self.flags | {'missiles_nuclear_integration_operational'}
        self.assertTrue(evaluate('missiles_special_payload_available', set(), flags))
        self.assertFalse(evaluate('missiles_special_payload_available', {'events_log_disabled_evolution_32_3_1'}, flags))

    def test_preparation_and_commit_share_the_track_gate(self):
        for name in ('missiles_operation_can_be_prepared', 'missiles_operation_can_be_committed'):
            self.assertEqual(dict(OPERATIONS[name]).get('missiles_operation_tracks_are_enabled'), 'yes')
        conventional = {'missiles_operation_strike_profile': constant('constant:missiles_strike_profile.precision'),
                        'missiles_operation_type': constant('constant:missiles_operation.precision'),
                        'missiles_operation_payload': constant('constant:missiles_payload.conventional')}
        disabled = {f'events_log_disabled_evolution_32_{i}_1' for i in range(1, 6)}
        self.assertTrue(evaluate('missiles_operation_tracks_are_enabled', disabled, self.flags, conventional))
        for field, token, track_type in (
            ('missiles_operation_strike_profile', 'constant:missiles_strike_profile.saturation', 1),
            ('missiles_operation_payload', 'constant:missiles_payload.nuclear', 3),
            ('missiles_operation_type', 'constant:missiles_operation.retaliation', 5),
        ):
            case = {**conventional, field: constant(token)}
            self.assertTrue(evaluate('missiles_operation_tracks_are_enabled', set(), self.flags, case))
            self.assertFalse(evaluate('missiles_operation_tracks_are_enabled', {f'events_log_disabled_evolution_32_{track_type}_1'}, self.flags, case))

    def test_saturation_suspension_retains_baseline_creation(self):
        ordinary = reserve_package(17, 7, True, True, False)
        suspended = reserve_package(17, 7, True, True, True, saturation_disabled=True)
        enabled = reserve_package(17, 7, True, True, True)
        self.assertEqual(suspended, ordinary)
        self.assertGreater(enabled, ordinary)

    def test_rogue_preparation_retains_its_track_identity(self):
        variables = {'missiles_operation_strike_profile': constant('constant:missiles_strike_profile.strategic'),
                     'missiles_operation_type': constant('constant:missiles_operation.strategic'),
                     'missiles_operation_payload': constant('constant:missiles_payload.conventional')}
        flags = self.flags | {'missiles_operation_rogue_origin'}
        self.assertTrue(evaluate('missiles_operation_tracks_are_enabled', set(), flags, variables))
        self.assertFalse(evaluate('missiles_operation_tracks_are_enabled', {'events_log_disabled_evolution_32_4_1'}, flags, variables))

    def test_no_reader_uses_unwritten_legacy_flags(self):
        files = [*ROOT_DIR.glob('common/**/032_missiles*.txt'), ROOT_DIR / 'events/032_missile_crisis.txt']
        for path in files:
            self.assertIsNone(re.search(r'event_evolution_disabled_32_[1-5]\b', path.read_text(encoding='utf-8-sig')), str(path))


EFFECTS = dict(parse((ROOT_DIR / 'common/scripted_effects/032_missiles_operations_effects.txt').read_text(encoding='utf-8-sig')))
CORE_EFFECTS = dict(parse((ROOT_DIR / 'common/scripted_effects/032_missiles_effects.txt').read_text(encoding='utf-8-sig')))
EVENT_LIST = parse((ROOT_DIR / 'events/032_missile_crisis.txt').read_text(encoding='utf-8-sig'))
PACING = (
    ('rogue_launch_commands', 'rogue_commands', 4, 'rogue_days', 120),
    ('unreliable_guidance', 'unreliable_guidance', 2, 'guidance_days', 105),
    ('saturation', 'saturation', 1, 'saturation_days', 90),
    ('special_warheads', 'special_warheads', 3, 'special_days', 120),
    ('automatic_retaliation', 'automatic_retaliation', 5, 'retaliation_days', 150),
)


def eligible(trigger, temps, chaos, world_end=False):
    """Evaluate an eligibility trigger against published pressure temporaries."""
    def operand(token):
        if token.startswith('constant:'):
            return constant(token)
        if token == 'global.chaos_meter_value':
            return chaos
        return temps[token]

    def term(key, body):
        if key in ('AND', 'hidden_trigger'):
            return all(term(k, v) for k, v in body)
        if key == 'OR':
            return any(term(k, v) for k, v in body)
        if key == 'NOT':
            return not any(term(k, v) for k, v in body)
        if key == 'has_global_flag':
            return world_end and body == 'world_end'
        if key == 'check_variable':
            fields = dict(body)
            left, right = operand(fields['var']), operand(fields['value'])
            return {'greater_than_or_equals': left >= right, 'less_than': left < right, 'greater_than': left > right, 'equals': left == right}[fields['compare']]
        raise AssertionError(f'Unbound eligibility input {key}')

    return all(term(k, v) for k, v in OPERATIONS[trigger])


BASE = {
    'missiles_pressure_programs': 4, 'missiles_pressure_operational': 2, 'missiles_pressure_war': 2,
    'missiles_pressure_vulnerable': 0, 'missiles_pressure_low_readiness': 0, 'missiles_pressure_overstocked': 0,
    'missiles_pressure_launches': 0, 'missiles_pressure_unmaintained_share': 0, 'missiles_pressure_operational_share': 0.5,
    'missiles_pressure_payload_owners': 0, 'missiles_pressure_hostile_pairs': 0,
}


class EvolutionPacingContract(unittest.TestCase):
    def test_each_track_arms_from_its_base_mtth(self):
        pulse = list(descendants(EFFECTS['missiles_evaluate_evolution_unlocks']))
        for key, enum, index, timing, days in PACING:
            with self.subTest(track=key):
                self.assertEqual(constant(f'constant:missiles_evolution_timing.{timing}'), days)
                self.assertIn(('missiles_evolution_delay_days', f'constant:missiles_evolution_timing.{timing}'), pulse)
                self.assertIn((f'missiles_evolution_{key}_is_eligible', 'yes'), pulse)
                self.assertIn((f'missiles_evolution_{key}_pressure_is_high', 'yes'), pulse)
                self.assertIn(('has_global_flag', f'events_log_disabled_evolution_32_{index}_1'), pulse)

    def test_armed_delay_is_random_pressure_scaled_and_staggered(self):
        arm = list(descendants(EFFECTS['missiles_arm_evolution_track']))
        keys = [k for k, _ in arm]
        self.assertIn('set_temp_variable_to_random', keys)
        self.assertIn(('missiles_evolution_delay_days', 'constant:missiles_evolution_pressure.delay_lengthening_multiplier'), arm)
        self.assertIn(('missiles_evolution_stagger', 'constant:missiles_evolution_pacing.first_fire_stagger_days'), arm)
        self.assertIn(('has_global_flag', 'missiles_evolution_first_pulse_done'), arm)
        self.assertLess(keys.index('chaosx_convert_days_to_date_offset'), keys.index('missiles_queue_evolution_job'))
        self.assertEqual(constant('constant:missiles_evolution_pacing.spread_min'), 0.75)
        self.assertEqual(constant('constant:missiles_evolution_pacing.spread_min') + constant('constant:missiles_evolution_pacing.spread_width'), 1.25)

    def test_job_runs_on_a_registered_host_without_a_world_scan(self):
        events = {value(body, 'id'): body for key, body in EVENT_LIST if key == 'country_event'}
        self.assertIn(('immediate', [('missiles_run_evolution_job', 'yes')]), events['chaosx.nr32.190'])
        self.assertIn(('immediate', [('missiles_refresh_evolution_access_from_receiver', 'yes')]), events['chaosx.nr32.8'])
        queue = list(descendants(EFFECTS['missiles_queue_evolution_job']))
        self.assertIn(('missiles_select_evolution_host', 'yes'), queue)
        self.assertTrue(any(k == 'country_event' and dict(v)['id'] == 'chaosx.nr32.190' for k, v in queue))
        for name in ('missiles_measure_evolution_pressure', 'missiles_run_evolution_job', 'missiles_evaluate_evolution_unlocks', 'missiles_select_evolution_host'):
            nodes = list(descendants(EFFECTS[name]))
            self.assertFalse(any(k in ('every_country', 'any_country', 'random_country') for k, _ in nodes), name)
        loop = value(EFFECTS['missiles_measure_evolution_pressure'], 'for_each_scope_loop')
        self.assertEqual(value(loop, 'array'), 'global.missiles_program_registry')

    def test_job_commits_once_through_the_enabled_log_guard(self):
        commit = EFFECTS['missiles_commit_evolution_track']
        guarded = value(commit, 'if')
        self.assertEqual(value(guarded, 'limit'), [('is_current_evolution_enabled', 'yes')])
        self.assertIn(('missiles_record_evolution_unlock', 'yes'), guarded)
        refresh = value(guarded, 'for_each_scope_loop')
        self.assertEqual(value(refresh, 'array'), 'global.missiles_program_registry')
        job = list(descendants(EFFECTS['missiles_run_evolution_job']))
        self.assertIn(('missiles_measure_evolution_pressure', 'yes'), job)
        self.assertEqual(sum(1 for k, v in job if k == 'missiles_commit_evolution_track'), len(PACING))
        self.assertIn(('missiles_evolution_due_remaining', 'constant:missiles_program_value.one'), job)

    def test_disabling_a_track_clears_its_pending_job(self):
        clear = list(descendants(EFFECTS['missiles_clear_disabled_evolution_pending']))
        for key, enum, index, timing, days in PACING:
            self.assertIn(('has_global_flag', f'events_log_disabled_evolution_32_{index}_1'), clear)
            self.assertIn(('clr_global_flag', f'missiles_evolution_{key}_pending'), clear)
        for name in ('missiles_evaluate_evolution_unlocks', 'missiles_run_evolution_job'):
            self.assertIn(('missiles_clear_disabled_evolution_pending', 'yes'), list(descendants(EFFECTS[name])))

    def test_spec_eligibility_rules(self):
        rogue = 'missiles_evolution_rogue_launch_commands_is_eligible'
        self.assertFalse(eligible(rogue, BASE, 300))
        self.assertTrue(eligible(rogue, {**BASE, 'missiles_pressure_vulnerable': 1}, 300))
        self.assertFalse(eligible(rogue, {**BASE, 'missiles_pressure_vulnerable': 1}, 150))
        guidance = 'missiles_evolution_unreliable_guidance_is_eligible'
        self.assertFalse(eligible(guidance, BASE, 450))
        for strain in ({'missiles_pressure_low_readiness': 2}, {'missiles_pressure_overstocked': 1}, {'missiles_pressure_launches': 3}, {'missiles_pressure_unmaintained_share': 0.5}):
            self.assertTrue(eligible(guidance, {**BASE, **strain}, 450), strain)
        saturation = 'missiles_evolution_saturation_is_eligible'
        self.assertTrue(eligible(saturation, BASE, 650))
        self.assertFalse(eligible(saturation, {**BASE, 'missiles_pressure_operational_share': 0.25}, 650))
        self.assertFalse(eligible(saturation, {**BASE, 'missiles_pressure_war': 1}, 650))
        special = 'missiles_evolution_special_warheads_is_eligible'
        self.assertFalse(eligible(special, BASE, 850))
        self.assertTrue(eligible(special, {**BASE, 'missiles_pressure_payload_owners': 1}, 850))
        self.assertIn(('missiles_country_has_nuclear_payload_candidate', 'yes'), list(descendants(OPERATIONS['missiles_program_owns_special_payload'])))
        retaliation = 'missiles_evolution_automatic_retaliation_is_eligible'
        paired = {**BASE, 'missiles_pressure_hostile_pairs': 1}
        self.assertTrue(eligible(retaliation, paired, 950))
        self.assertFalse(eligible(retaliation, paired, 950, world_end=True))
        self.assertFalse(eligible(retaliation, paired, 850))
        self.assertFalse(eligible(retaliation, BASE, 950))
        responder = list(descendants(OPERATIONS['missiles_program_can_answer_retaliation']))
        for need in ('missiles_site_is_secure', 'missiles_program_is_operational'):
            self.assertIn((need, 'yes'), responder)
        self.assertTrue(any(k == 'check_variable' and dict(v)['value'] == 'constant:missiles_reserve.retaliation_reserve_cap' for k, v in responder))
        self.assertTrue(any(k == 'check_variable' and dict(v)['value'] == 'constant:missiles_stage.advanced' for k, v in responder))

    def test_programmes_join_and_leave_the_registry(self):
        self.assertIn(('missiles_register_program', 'yes'), CORE_EFFECTS['missiles_initialize_or_advance_program'])
        capture = list(descendants(EFFECTS['missiles_initialize_capture_shell']))
        self.assertIn(('missiles_register_program', 'yes'), capture)
        removal = list(descendants(EFFECTS['missiles_cleanup_removed_country']))
        self.assertIn(('remove_from_array', [('array', 'global.missiles_program_registry'), ('value', 'THIS')]), removal)
        self.assertIn(('missiles_requeue_pending_evolution_jobs', 'yes'), removal)
        adoption = list(descendants(EFFECTS['missiles_refresh_evolution_access_from_receiver']))
        self.assertIn(('missiles_evaluate_country_evolution_adoption', 'yes'), adoption)


if __name__ == '__main__':
    unittest.main()
