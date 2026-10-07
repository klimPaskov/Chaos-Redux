"""Source-backed Event 021 calendar regressions, not a game simulation."""
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
import os
import re
import subprocess
import unittest

from test_event021_evolution_log import ROOT, parse


EFFECT_DIR = 'common/scripted_effects/'
DATE_SOURCE = EFFECT_DIR + '021_random_civil_war_date_effects.txt'
CALENDAR_SOURCE = 'common/script_constants/chaosx_date_units_constants.txt'
SHARED_SOURCE = EFFECT_DIR + 'chaosx_dynamic_effects.txt'
SOURCES = [EFFECT_DIR + '021_random_civil_war_' + name + '.txt' for name in (
    'effects', 'parent_effects', 'decision_effects', 'evidence_effects', 'treaty_effects')]
DATE_KEY = re.compile(r'(?:date|until|deadline|expiry)$')


def source(path):
    revision = os.environ.get('CHAOSX_EVENT021_TEST_REVISION')
    if revision:
        return subprocess.run(['git', 'show', revision + ':' + path], cwd=ROOT,
                              check=True, capture_output=True, encoding='utf-8').stdout
    return (ROOT / path).read_text(encoding='utf-8-sig')


def blocks(nodes):
    yield nodes
    for _, data in nodes:
        if isinstance(data, list):
            yield from blocks(data)


def calendar_surfaces():
    """Include every Event 021 engine file, including later added adapters."""
    revision = os.environ.get('CHAOSX_EVENT021_TEST_REVISION')
    if revision:
        paths = subprocess.run(['git', 'ls-tree', '-r', '--name-only', revision,
                                '--', 'common', 'events'], cwd=ROOT, check=True,
                               capture_output=True, encoding='utf-8').stdout.splitlines()
        return [path for path in paths if Path(path).name.startswith('021') and path.endswith('.txt')]
    return sorted(str(path.relative_to(ROOT)).replace('\\', '/')
                  for folder in ('common', 'events')
                  for path in (ROOT / folder).rglob('021*.txt'))


class Clock:
    def __init__(self, days):
        self.temporary = {'event021_date_offset': Decimal(str(days))}
        category = dict(parse(source(CALENDAR_SOURCE)))['chaosx_date_units']
        self.constants = {f'constant:chaosx_date_units.{key}': Decimal(data)
                          for key, data in category if key != 'schema'}

    def value(self, token):
        return self.constants[token] if token.startswith('constant:') else self.temporary[token]

    def run(self, nodes):
        for key, data in nodes:
            if key == 'chaosx_convert_days_to_date_offset':
                self.call(dict(parse(source(SHARED_SOURCE)))[key])
                continue
            if key == 'round_temp_variable':
                self.temporary[data] = self.temporary[data].to_integral_value(rounding=ROUND_HALF_UP)
            elif key == 'if':
                test = dict(dict(data)['limit'][0][1])
                if self.value(test['var']) < self.value(test['value']):
                    self.run([(k, v) for k, v in data if k != 'limit'])
            else:
                name, token = data[0]
                value = self.value(token)
                if key == 'set_temp_variable':
                    self.temporary[name] = value
                elif key == 'multiply_temp_variable':
                    self.temporary[name] *= value
                elif key == 'divide_temp_variable':
                    self.temporary[name] /= value
                elif key == 'add_to_temp_variable':
                    self.temporary[name] += value
                else:
                    raise AssertionError(f'Unsupported calendar effect {key}')

    def call(self, helper):
        # Conservative scripted-effect boundary: only temporaries that existed
        # before the call survive its return.
        caller = set(self.temporary)
        self.run(helper)
        self.temporary = {k: v for k, v in self.temporary.items() if k in caller}

    def offset(self):
        self.call(dict(parse(source(DATE_SOURCE)))['event021_days_to_date_offset'])
        return self.temporary['event021_date_offset']


class CalendarTests(unittest.TestCase):
    def test_two_days_are_48_hours_not_two_encoded_units(self):
        self.assertEqual(Clock(2).offset(), Decimal('0.00048'))
        self.assertEqual(Decimal(2) / Decimal('0.00001'), 200000)

    def test_all_configured_whole_day_durations_are_exact(self):
        for days in (0, 1, 2, 7, 14, 30, 60, 90, 120, 180, 365, 730):
            with self.subTest(days=days):
                clock = Clock(days)
                self.assertEqual(clock.offset() * 100000, days * 24)
                self.assertEqual(set(clock.temporary), {'event021_date_offset'})

    def test_fractional_mtth_days_resolve_on_or_after_requested_hour(self):
        for days in ('60.03125', '86.0625', '90.01234', '179.99999'):
            with self.subTest(days=days):
                intended_hours = Decimal(days) * 24
                actual_hours = Clock(days).offset() * 100000
                self.assertGreaterEqual(actual_hours, intended_hours)
                self.assertLess(actual_hours - intended_hours, 1)

    def test_exact_deadline_boundaries_and_copied_anchors(self):
        anchor = Decimal('607.42420')
        for days in (1, 2, 7, 30, 90, 180, 730):
            with self.subTest(days=days):
                deadline = anchor + Clock(days).offset()
                self.assertLess(deadline - Decimal('0.00001'), deadline)
                self.assertEqual(deadline - anchor, Decimal(days * 24) / 100000)
                self.assertTrue(deadline >= deadline)
                self.assertTrue(deadline + Decimal('0.00001') >= deadline)

    def test_every_deadline_addition_uses_caller_owned_converted_days(self):
        count = 0
        for path in calendar_surfaces():
            for nodes in blocks(parse(source(path))):
                for index, (key, data) in enumerate(nodes):
                    if key not in ('add_to_variable', 'add_to_temp_variable'):
                        continue
                    name, operand = data[0]
                    if not DATE_KEY.search(name):
                        continue
                    with self.subTest(path=path, target=name):
                        self.assertEqual(operand, 'event021_date_offset')
                        self.assertGreaterEqual(index, 2)
                        seed_key, seed = nodes[index - 2]
                        self.assertEqual(seed_key, 'set_temp_variable')
                        self.assertEqual(seed[0][0], 'event021_date_offset')
                        self.assertNotEqual(seed[0][1], 'event021_date_offset')
                        self.assertEqual(nodes[index - 1], ('event021_days_to_date_offset', 'yes'))
                    count += 1
        # Includes the active-war Evolution I retry added after the first audit.
        self.assertEqual(count, 44)

    def test_native_day_fields_and_mtth_day_values_are_unchanged_from_head(self):
        def day_fields(text):
            result = []
            for nodes in blocks(parse(text)):
                for key, data in nodes:
                    if key in ('days', 'days_mission_timeout', 'days_remove', 'days_re_enable'):
                        result.append((key, data))
            return result

        baseline_revision = os.environ.get('CHAOSX_EVENT021_DATE_BASELINE', 'HEAD')
        for path in SOURCES:
            before = subprocess.run(['git', 'show', baseline_revision + ':' + path], cwd=ROOT,
                                    check=True, capture_output=True, encoding='utf-8').stdout
            # Regional cleanup adds an approved timer expressed in native days.
            current = day_fields(source(path))
            added = ('days', 'event021_exposure_decay_days')
            if added in current and added not in day_fields(before):
                current.remove(added)
            self.assertEqual(day_fields(before), current, path)
        mtth = 'common/mtth/021_random_civil_war_mtth.txt'
        if os.environ.get('CHAOSX_EVENT021_TEST_REVISION'):
            before = subprocess.run(['git', 'show', baseline_revision + ':' + mtth], cwd=ROOT,
                                    check=True, capture_output=True, encoding='utf-8').stdout
        else:
            before = (ROOT / 'docs/plans/021_random_civil_war_plans/probability_snapshots/'
                      'event021_date_units_before_2026-10-03/021_random_civil_war_mtth.txt').read_text(encoding='utf-8-sig')
        self.assertEqual(parse(before), parse(source(mtth)))


if __name__ == '__main__':
    unittest.main()
