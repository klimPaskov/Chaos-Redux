"""Source-contract tests for Event 032 program phases at war and peace.

Covers the wartime maintenance dead end (low readiness during war must still
show the maintenance actions), the six-action budget in the operations view,
and phase refresh at the war and peace boundaries. This is source evidence,
not an engine simulation.
"""
from pathlib import Path
import unittest
from test_event32_recipient_scope import parse, value, descendants

ROOT = Path(__file__).resolve().parents[1]


def source(path):
    return dict(parse((ROOT / path).read_text(encoding='utf-8-sig')))


EFFECTS = source('common/scripted_effects/032_missiles_operations_effects.txt')
CORE = source('common/scripted_effects/032_missiles_effects.txt')
TRIGGERS = source('common/scripted_triggers/032_missiles_operations_triggers.txt')
SITE_TRIGGERS = source('common/scripted_triggers/032_missiles_triggers.txt')
DECISIONS = dict(source('common/decisions/032_missiles_decisions.txt')['missiles_program_management_category'])
ON_ACTIONS = dict(source('common/on_actions/032_missiles_on_actions.txt')['on_actions'])
MAINTENANCE = (
    'missiles_replenish_operational_reserve', 'missiles_restore_launch_readiness',
    'missiles_improve_guidance_and_maintenance', 'missiles_secure_launch_authority',
)


def nodes(body):
    return list(descendants(body))


def maintenance_visible(phase, is_ai, can_prepare, target_selected, page_open):
    """Evaluate missiles_maintenance_actions_are_visible from its source."""
    facts = {
        ('has_country_flag', 'missiles_program_phase_maintenance'): phase == 'maintenance',
        ('has_country_flag', 'missiles_program_phase_operations'): phase == 'operations',
        ('is_ai', 'yes'): is_ai,
        ('missiles_country_can_prepare_operation', 'yes'): can_prepare,
        ('has_country_flag', 'missiles_target_selected'): target_selected,
        ('has_country_flag', 'missiles_target_country_page_open'): page_open,
    }

    def term(key, body):
        if key in ('AND',):
            return all(term(k, v) for k, v in body)
        if key == 'OR':
            return any(term(k, v) for k, v in body)
        if key == 'NOT':
            return not any(term(k, v) for k, v in body)
        return facts[(key, body)]

    return all(term(k, v) for k, v in TRIGGERS['missiles_maintenance_actions_are_visible'])


class ProgramPhaseContract(unittest.TestCase):
    def test_war_with_low_readiness_shows_the_maintenance_actions(self):
        # Low readiness or command control makes missiles_country_can_prepare_operation false.
        prepare = nodes(SITE_TRIGGERS['missiles_country_can_prepare_operation'])
        self.assertTrue(any(k == 'check_variable' and dict(v).get('var') == 'missiles_launch_readiness' for k, v in prepare))
        for is_ai in (False, True):
            for selected in (False, True):
                with self.subTest(is_ai=is_ai, selected=selected):
                    self.assertTrue(maintenance_visible('operations', is_ai, False, selected, selected))
        for name in MAINTENANCE:
            self.assertIn(('missiles_maintenance_actions_are_visible', 'yes'), value(DECISIONS[name], 'visible'))
            self.assertNotIn(('has_country_flag', 'missiles_program_phase_maintenance'), value(DECISIONS[name], 'visible'))

    def test_operations_view_stays_within_six_actions_for_humans(self):
        self.assertTrue(maintenance_visible('maintenance', False, True, False, False))
        # No target chosen: the selector entry plus four maintenance actions,
        # plus network restoration at most.
        self.assertTrue(maintenance_visible('operations', False, True, False, False))
        self.assertLessEqual(1 + len(MAINTENANCE) + 1, 6)
        # While a human chooses a target or prepares, maintenance steps aside.
        self.assertFalse(maintenance_visible('operations', False, True, True, False))
        self.assertFalse(maintenance_visible('operations', False, True, False, True))
        self.assertFalse(maintenance_visible('establishment', False, True, False, False))
        human_preparation = nodes(TRIGGERS['missiles_ordinary_preparation_action_is_visible'])
        self.assertIn(('missiles_human_target_is_complete', 'yes'), human_preparation)
        selector = nodes(value(DECISIONS['missiles_open_target_selection'], 'visible'))
        self.assertIn(('NOT', [('has_country_flag', 'missiles_target_selected')]), selector)

    def test_wartime_phase_rule_and_maintenance_refresh(self):
        phases = nodes(CORE['missiles_set_program_phases'])
        self.assertIn(('set_country_flag', 'missiles_program_phase_operations'), phases)
        self.assertIn(('has_war', 'yes'), phases)
        for effect in ('missiles_replenish_reserve', 'missiles_restore_readiness', 'missiles_improve_guidance', 'missiles_secure_launch_codes'):
            self.assertIn(('missiles_set_program_phases', 'yes'), EFFECTS[effect], effect)
        receipt = nodes(EFFECTS['missiles_resolve_warning_queue_receipt'])
        self.assertIn(('missiles_set_program_phases', 'yes'), receipt)
        self.assertNotIn(('set_country_flag', 'missiles_program_phase_operations'), receipt)

    def test_war_and_peace_boundaries_refresh_both_participants(self):
        war = nodes(ON_ACTIONS['on_war_relation_added'])
        for side in ('ROOT', 'FROM'):
            refresh = [body for key, body in war if key == side and ('missiles_set_program_phases', 'yes') in nodes(body)]
            self.assertTrue(refresh, side)
            self.assertIn(('has_country_flag', 'missiles_program_initialized'), nodes(refresh[0]))
        peace = nodes(ON_ACTIONS['on_peace'])
        self.assertIn(('missiles_set_program_phases', 'yes'), peace)
        self.assertIn(('missiles_clear_target', 'yes'), peace)
        self.assertFalse(any(key in ('every_country', 'on_daily', 'on_weekly') for key, _ in war + peace))


if __name__ == '__main__':
    unittest.main()
