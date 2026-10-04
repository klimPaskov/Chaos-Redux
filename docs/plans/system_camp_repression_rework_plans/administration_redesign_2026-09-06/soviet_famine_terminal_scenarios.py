"""Execute the production Soviet state effects against finite terminal-state fixtures.

The evidence registry is mocked; this is source execution, not Clausewitz runtime.
"""
from pathlib import Path
import unittest

from foundation_source_tests import Runtime, parse

ROOT = Path(__file__).resolve().parents[4]


class SovietFamineRuntime(Runtime):
    def __init__(self):
        super().__init__()
        wanted = {
            'camp_rework_soviet_conceal_current_famine_state',
            'camp_rework_soviet_admit_current_famine_state',
        }
        source = (ROOT / 'common/scripted_effects/camp_repression_major_country_effects.txt').read_text(encoding='utf-8-sig')
        self.effects.update({name: body for name, _, body in parse(source) if name in wanted})
        self.effects['camp_rework_register_evidence_state'] = []
        trigger_source = (ROOT / 'common/scripted_triggers/camp_repression_rework_triggers.txt').read_text(encoding='utf-8-sig')
        self.triggers.update({name: body for name, _, body in parse(trigger_source)
                              if name == 'camp_rework_state_can_accept_responsibility_from_root'})
        constant_source = (ROOT / 'common/script_constants/camp_repression_rework_constants.txt').read_text(encoding='utf-8-sig')
        for category, _, body in parse(constant_source):
            if isinstance(body, list):
                for key, _, value in body:
                    if key != 'schema' and not isinstance(value, list):
                        try:
                            self.constants[f'{category}.{key}'] = float(value)
                        except ValueError:
                            pass

    def target(self, value, scope, previous):
        if value == 'ROOT':
            return 'SOV'
        return super().target(value, scope, previous)


class SovietFamineTerminalScenarios(unittest.TestCase):
    def setUp(self):
        self.runtime = SovietFamineRuntime()
        self.runtime.country('SOV')
        self.site = self.runtime.state('S1', country='SOV')
        self.site['flags'].add('genocide_soviet_famine_pressure_site')

    def test_concealment_records_one_state_outcome(self):
        self.runtime.run('camp_rework_soviet_conceal_current_famine_state', 'S1')
        first_depth = self.site['camp_state_evidence_depth']
        self.assertIn('camp_rework_soviet_records_concealed', self.site['flags'])
        self.assertEqual(self.runtime.temp['camp_soviet_famine_state_selected'], 1)
        self.runtime.temp['camp_soviet_famine_state_selected'] = 0
        self.runtime.run('camp_rework_soviet_conceal_current_famine_state', 'S1')
        self.assertEqual(self.site['camp_state_evidence_depth'], first_depth)
        self.assertEqual(self.runtime.temp['camp_soviet_famine_state_selected'], 0)

    def test_admission_records_one_state_outcome(self):
        self.runtime.run('camp_rework_soviet_admit_current_famine_state', 'S1')
        first_depth = self.site['camp_state_evidence_depth']
        self.assertIn('genocide_site_discovered', self.site['flags'])
        self.assertEqual(self.runtime.temp['camp_soviet_famine_state_selected'], 1)
        self.runtime.temp['camp_soviet_famine_state_selected'] = 0
        self.runtime.run('camp_rework_soviet_admit_current_famine_state', 'S1')
        self.assertEqual(self.site['camp_state_evidence_depth'], first_depth)
        self.assertEqual(self.runtime.temp['camp_soviet_famine_state_selected'], 0)


if __name__ == '__main__':
    unittest.main()
