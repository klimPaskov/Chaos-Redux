"""Execute the production field-slot predicates on declared field fixtures.

The disturbance and breach slots are the only state-dependent slots and are independent of each
other (ba19b98377 removed the foreign pressure slot and the breach override on disturbance); a
suspended field shows neither.
This checks mutual exclusion and empty/history gates, not native rendering.
Stored state validity and country history availability are fixture inputs.
"""
from itertools import product
from pathlib import Path
import unittest

from test_event020_outbreak_entry import parse, ROOT


SOURCE = ROOT / 'common/scripted_guis/018_resources_found_scripted_gui.txt'
TRIGGERS = dict(dict(dict(parse(SOURCE.read_text(encoding='utf-8-sig')))['scripted_gui'])["resources_found_field_scripted_gui"])
TRIGGERS = dict(TRIGGERS['triggers'])
SLOTS = ('disturbance', 'breach')


def evaluate(nodes, flags, valid=True, history=True):
    def one(key, value):
        if key == 'OR':
            return any(one(k, v) for k, v in value)
        if key == 'AND':
            return all(one(k, v) for k, v in value)
        if key == 'NOT':
            return not any(one(k, v) for k, v in value)
        if key.startswith('var:'):
            return evaluate(value, flags, valid, history)
        if key == 'has_state_flag':
            return value in flags
        if key == 'has_country_flag':
            assert value == 'resources_found_gui_closed_history_view'
            return history
        if key in ('resources_found_country_has_valid_selected_field', 'resources_found_gui_has_closed_field_history'):
            return valid
        raise AssertionError((key, value))
    return all(one(k, v) for k, v in nodes)


class SlotTests(unittest.TestCase):
    def test_active_and_history_slots_are_exclusive(self):
        for closed in (False, True):
            prefix = 'resources_found_gui_closed_' if closed else 'resources_found_gui_'
            for disturbance, breach, suspended in product((False, True), repeat=3):
                flags = {name for name, enabled in (
                    ('resources_found_disturbance_revealed', disturbance),
                    ('resources_found_breach_revealed', breach),
                    ('resources_found_field_suspended', suspended)) if enabled}
                visible = [slot for slot in SLOTS
                           if evaluate(TRIGGERS[prefix + slot + '_visible'], flags)]
                expected = [] if suspended else [slot for slot, revealed in (('disturbance', disturbance), ('breach', breach)) if revealed]
                with self.subTest(closed=closed, flags=flags):
                    self.assertEqual(visible, expected)
                    self.assertFalse(any(evaluate(TRIGGERS[prefix + slot + '_visible'], flags, valid=False)
                                         for slot in SLOTS))

    def test_history_does_not_leak_into_active_view(self):
        for slot in SLOTS:
            flags = {'resources_found_breach_revealed', 'resources_found_disturbance_revealed'}
            self.assertTrue(evaluate(TRIGGERS['resources_found_gui_' + slot + '_visible'], flags))
            self.assertFalse(evaluate(TRIGGERS['resources_found_gui_closed_' + slot + '_visible'], flags, history=False))


if __name__ == '__main__':
    unittest.main()
