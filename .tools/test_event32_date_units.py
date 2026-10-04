"""Source regression for Event 032 stored dates and scope-bound writes.

Stored dates (global.date and copies of it) count one game hour as 0.00001,
so a day count must pass through chaosx_convert_days_to_date_offset before it
is added to one, and a date difference must pass through
chaosx_convert_date_offset_to_days before it feeds a native days field.
The test also pins the country-scoped repair flags, the bare natural-disaster
temporaries, and the country-only secondary-site completion path.
This is source evidence, not an engine simulation.
"""
from pathlib import Path
import re
import unittest
from test_event32_recipient_scope import parse, value, descendants

ROOT = Path(__file__).resolve().parents[1]
EFFECT_FILES = (
    'common/scripted_effects/032_missiles_achievement_effects.txt',
    'common/scripted_effects/032_missiles_effects.txt',
    'common/scripted_effects/032_missiles_operations_effects.txt',
    'common/scripted_effects/032_missiles_scenario_effects.txt',
)
DATE_OFFSETS = {'chaosx_date_offset', 'missiles_evolution_delay_offset'}


def text(path):
    return (ROOT / path).read_text(encoding='utf-8-sig')


def source(path):
    return dict(parse(text(path)))


def flat_pairs(nodes):
    for key, body in nodes:
        if isinstance(body, list):
            for inner_key, inner_value in body:
                if not isinstance(inner_value, list):
                    yield key, inner_key, inner_value
            yield from flat_pairs(body)


class MissileDateUnitContract(unittest.TestCase):
    def test_day_counts_are_converted_before_reaching_stored_dates(self):
        for path in EFFECT_FILES:
            nodes = parse(text(path))
            date_vars = {name for op, name, val in flat_pairs(nodes) if op == 'set_variable' and val == 'global.date'}
            for op, name, val in flat_pairs(nodes):
                if op == 'add_to_variable' and name in date_vars:
                    with self.subTest(path=path, variable=name):
                        self.assertIn(val, DATE_OFFSETS)

    def test_warning_dates_share_one_converted_deadline_helper(self):
        operations = source('common/scripted_effects/032_missiles_operations_effects.txt')
        scenario = source('common/scripted_effects/032_missiles_scenario_effects.txt')
        helper = operations['missiles_set_warning_deadlines']
        calls = [k for k, _ in descendants(helper) if k.startswith('chaosx_convert_')]
        self.assertEqual(calls, ['chaosx_convert_days_to_date_offset', 'chaosx_convert_days_to_date_offset'])
        seed = scenario['missiles_scenario_seed_retaliation_warning']
        self.assertIn('missiles_set_warning_deadlines', [k for k, _ in descendants(seed)])
        schedule = operations['missiles_schedule_warning_response']
        names = [k for k, _ in descendants(schedule)]
        self.assertLess(names.index('chaosx_convert_date_offset_to_days'), names.index('country_event'))

    def test_long_reach_hold_compares_date_offsets(self):
        achievements = text('common/scripted_effects/032_missiles_achievement_effects.txt')
        self.assertNotRegex(achievements, r'var = chaosx_032_long_reach_clock_days value = @missiles_achievement_long_reach_days')
        self.assertRegex(achievements, r'var = missiles_long_reach_elapsed_offset value = missiles_long_reach_required_offset compare = greater_than_or_equals')

    def test_disaster_penalties_read_bare_temporaries(self):
        operations = text('common/scripted_effects/032_missiles_operations_effects.txt')
        self.assertNotRegex(operations, r'PREV\.missiles_disaster_(readiness_loss|control_loss|guidance_backlog|warning_pressure)')

    def test_repair_flags_are_written_on_the_program_country(self):
        operations = source('common/scripted_effects/032_missiles_operations_effects.txt')
        body = value(operations['missiles_suspend_damaged_site'], 'if')
        self.assertNotIn('set_country_flag', [k for k, _ in body])
        root = value(body, 'ROOT')
        self.assertEqual([v for k, v in root if k == 'set_country_flag'], ['missiles_site_repair_active', 'missiles_site_repair_started'])

    def test_secondary_site_completion_never_tests_the_country_as_a_state(self):
        operations = source('common/scripted_effects/032_missiles_operations_effects.txt')
        body = operations['missiles_establish_secondary_site']
        self.assertNotIn('else_if', [k for k, _ in body])
        top_level_state_checks = [k for k, _ in body if k in ('missiles_state_is_valid_secondary_site', 'missiles_register_site')]
        self.assertEqual(top_level_state_checks, [])


if __name__ == '__main__':
    unittest.main()
