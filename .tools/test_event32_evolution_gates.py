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


if __name__ == '__main__':
    unittest.main()
