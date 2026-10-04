"""Source-contract tests for Event 032 evolution access choices.

An evolution unlock grants access only: Saturation Arsenals is adopted through
its own costed decision, and retaliation posture starts Off and changes
through a costed, cooled-down decision that is blocked during a warning or
committed response. This is source evidence, not an engine simulation.
"""
from pathlib import Path
import unittest
from test_event32_recipient_scope import parse, value, descendants

ROOT = Path(__file__).resolve().parents[1]


def source(path):
    return dict(parse((ROOT / path).read_text(encoding='utf-8-sig')))


EFFECTS = source('common/scripted_effects/032_missiles_operations_effects.txt')
CORE = source('common/scripted_effects/032_missiles_effects.txt')
SCENARIO = source('common/scripted_effects/032_missiles_scenario_effects.txt')
TRIGGERS = source('common/scripted_triggers/032_missiles_operations_triggers.txt')
DECISIONS = dict(source('common/decisions/032_missiles_decisions.txt')['missiles_program_management_category'])
EVENTS = parse((ROOT / 'events/032_missile_crisis.txt').read_text(encoding='utf-8-sig'))


def nodes(body):
    return list(descendants(body))


class EvolutionChoices(unittest.TestCase):
    def test_unlock_evaluation_grants_access_only(self):
        adoption = nodes(EFFECTS['missiles_evaluate_country_evolution_adoption'])
        for flag in ('missiles_evolution_saturation_arsenals', 'missiles_saturation_doctrine_adopted', 'missiles_retaliation_network_active'):
            self.assertNotIn(('set_country_flag', flag), adoption)
        self.assertIn(('set_country_flag', 'missiles_evolution_automatic_retaliation'), adoption)
        self.assertNotIn(('set_variable', [('missiles_retaliation_posture', 'constant:missiles_retaliation_posture.supervised')]), adoption)
        record = nodes(CORE['missiles_initialize_program_record'])
        self.assertTrue(any(k == 'set_variable' and dict(v).get('missiles_retaliation_posture') == 'constant:missiles_retaliation_posture.off' for k, v in record))

    def test_saturation_doctrine_is_a_costed_country_decision(self):
        decision = dict(DECISIONS['missiles_adopt_saturation_doctrine'])
        self.assertIn(('missiles_adopt_saturation_doctrine', 'yes'), nodes(decision['complete_effect']))
        self.assertIn(('missiles_saturation_doctrine_is_offered', 'yes'), nodes(decision['visible']))
        self.assertIn(('missiles_saturation_doctrine_requirements_met', 'yes'), nodes(decision['available']))
        self.assertEqual(len(decision['custom_cost_trigger']), 3)
        self.assertIn('ai_will_do', decision)
        requirements = nodes(TRIGGERS['missiles_saturation_doctrine_requirements_met'])
        self.assertIn(('check_variable', [('var', 'missiles_program_stage'), ('value', 'constant:missiles_stage.guided'), ('compare', 'greater_than_or_equals')]), requirements)
        self.assertIn(('missiles_country_has_active_site', 'yes'), requirements)
        self.assertIn('num_of_factories', [k for k, _ in requirements])
        self.assertTrue(any(k == 'check_variable' and dict(v)['var'] == 'missiles_command_control' for k, v in requirements))
        self.assertIn(('NOT', [('has_country_flag', 'missiles_rogue_command_active')]), requirements)
        offered = nodes(TRIGGERS['missiles_saturation_doctrine_is_offered'])
        self.assertIn(('has_global_flag', 'missiles_evolution_saturation_unlocked'), offered)
        self.assertIn(('missiles_saturation_enabled', 'yes'), offered)
        adopt = nodes(EFFECTS['missiles_adopt_saturation_doctrine'])
        for flag in ('missiles_evolution_saturation_arsenals', 'missiles_saturation_doctrine_adopted'):
            self.assertIn(('set_country_flag', flag), adopt)

    def test_reserve_packages_read_the_live_saturation_trigger(self):
        for body in (CORE['missiles_add_first_reserve_package'], CORE['missiles_add_repeat_reserve_package'], EFFECTS['missiles_apply_mature_program_package']):
            found = nodes(body)
            self.assertNotIn(('has_country_flag', 'missiles_evolution_saturation_arsenals'), found)
            self.assertIn(('missiles_saturation_active', 'yes'), found)

    def test_posture_decision_costs_cools_down_and_respects_responses(self):
        decision = dict(DECISIONS['missiles_set_retaliation_posture'])
        self.assertIn(('country_event', [('id', 'chaosx.nr32.40')]), nodes(decision['complete_effect']))
        self.assertIn('days_re_enable', decision)
        payment = nodes(decision['complete_effect'])
        self.assertTrue(any(k == 'add_command_power' for k, _ in payment))
        self.assertTrue(any(k == 'subtract_from_variable' and 'missiles_launch_readiness' in dict(v) for k, v in payment))
        change = nodes(TRIGGERS['missiles_retaliation_posture_can_change'])
        self.assertIn(('NOT', [('has_country_flag', 'missiles_warning_active')]), change)
        self.assertTrue(any(k == 'check_variable' and dict(v).get('value') == 'constant:missiles_operation.retaliation' for k, v in change))
        events = {value(body, 'id'): body for key, body in EVENTS if key == 'country_event'}
        automatic = next(body for key, body in events['chaosx.nr32.40'] if key == 'option' and value(body, 'name') == 'chaosx.nr32.40.d')
        self.assertEqual(value(automatic, 'trigger'), [('missiles_posture_can_be_automatic', 'yes')])
        self.assertIn(('missiles_automatic_posture_allowed', 'yes'), nodes(TRIGGERS['missiles_posture_can_be_automatic']))
        for key, option in events['chaosx.nr32.40']:
            if key == 'option':
                self.assertIn('custom_effect_tooltip', dict(option))

    def test_scenario_profiles_still_preset_doctrine_and_posture(self):
        scenario = nodes(list(SCENARIO.items()))
        self.assertIn(('set_country_flag', 'missiles_evolution_saturation_arsenals'), scenario)
        self.assertIn(('set_country_flag', 'missiles_saturation_doctrine_adopted'), scenario)
        self.assertIn(('set_country_flag', 'missiles_retaliation_network_active'), scenario)


if __name__ == '__main__':
    unittest.main()
