"""Meaningful fixture checks for repeated state/event and timing diagnostics."""
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'runtime'))
from clausewitz import parse
from entity_lint import lint_state
from inventory import effective_entity


class AssetParserTests(unittest.TestCase):
    def test_repeated_events_and_comment_braces(self):
        state = parse('state = { name = "attack" # ignored }\n event = { time = 0 } event = { time = .1 } }').children('state')[0]
        self.assertEqual([n.scalar('time') for n in state.children('event')], ['0', '.1'])

    def test_clone_state_override_keeps_other_states(self):
        base = parse('entity={name=base state={name=idle} state={name=attack} state={name=attack}}').children()[0]
        child = parse('entity={name=child clone=base state={name=idle}}').children()[0]
        entities = {'base': {'node': base}, 'child': {'node': child}}
        self.assertEqual([s.scalar('name') for s in effective_entity('child', entities).children('state')], ['attack', 'attack', 'idle'])

    def test_bad_block_is_reported(self):
        with self.assertRaises(ValueError):
            parse('event={sound={soundeffect="unfinished"}')


class EntityLintTests(unittest.TestCase):
    def lint(self, text, **kwargs):
        state = parse(text).children('state')[0]
        effect = parse('soundeffect={name=shot loop=no max_audible=3}').children()[0]
        return lint_state(state, entity_name='fixture', path='fixture.asset', cycle=1,
                          cue_samples={'shot': [1.2]}, effects={'shot': {'node': effect}},
                          particles={'mg_muzzle_particle': {'max_particle_life_s': .2}}, **kwargs)

    def test_self_chain_and_overlap_are_measured(self):
        row = self.lint('state={name=attack next_state=attack event={time=.1 sound={soundeffect=shot}} event={time=.5 sound={soundeffect=shot}}}')
        rules = {f['rule'] for f in row['findings']}
        self.assertTrue(row['repeating'])
        self.assertIn('sound_samples_overlap', rules)
        self.assertIn('sample_longer_than_cycle_without_single_loop', rules)

    def test_only_hash_bound_contacts_pass(self):
        text = 'state={name=attack event={time=.2 sound={soundeffect=shot}}}'
        row = self.lint(text, animation_sha='new', contact_markers=[{'animation_sha256': 'old', 'entity': 'fixture', 'event_line': 1, 'time_s': .2}])
        self.assertIn('contact_evidence_required', {f['rule'] for f in row['findings']})
        row = self.lint(text, animation_sha='new', contact_markers=[{'animation_sha256': 'new', 'entity': 'fixture', 'event_line': 1, 'time_s': .2}])
        self.assertNotIn('contact_evidence_required', {f['rule'] for f in row['findings']})

    def test_impulse_particles_do_not_accumulate(self):
        row = self.lint('state={name=attack event={time=.1 node=muzzle particle=mg_muzzle_particle keep_particle=yes} event={time=.2 node=muzzle particle=mg_muzzle_particle}}')
        rules = {f['rule'] for f in row['findings']}
        self.assertIn('keep_particle_on_impulse_emitter', rules)
        self.assertIn('particle_overlap_on_locator', rules)

    def test_static_channels_do_not_establish_contact_timing(self):
        row = self.lint('state={name=attack event={time=.2 sound={soundeffect=shot}}}',
                        motion={'motion_peak_table': [{'bone': 'RightHand', 'time_seconds': .2,
                                                     'angular_deg': 0, 'translation_step': 0}]})
        contact = next(f for f in row['findings'] if f['rule'] == 'contact_evidence_required')
        self.assertIsNone(contact['nearest_motion_peak_offset_s'])

    def test_zero_translation_does_not_select_every_rotation_frame(self):
        row = self.lint('state={name=attack event={time=.2 sound={soundeffect=shot}}}',
                        motion={'motion_peak_table': [
                            {'bone': 'RightHand', 'time_seconds': .2, 'angular_deg': 1, 'translation_step': 0},
                            {'bone': 'RightHand', 'time_seconds': .8, 'angular_deg': 20, 'translation_step': 0}]})
        contact = next(f for f in row['findings'] if f['rule'] == 'contact_evidence_required')
        self.assertAlmostEqual(contact['nearest_motion_peak_offset_s'], .6)
        self.assertIn('measured_contact_peak_offset', {f['rule'] for f in row['findings']})


if __name__ == '__main__':
    unittest.main()
