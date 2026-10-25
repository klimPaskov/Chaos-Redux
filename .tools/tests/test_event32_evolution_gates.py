"""Source-level shared-toggle and retained-adoption contract tests.

Evaluates only documented boolean trigger composition and the explicit gate
variables. It does not simulate HOI4 decisions, stockpiles, or probabilities.
"""
from pathlib import Path
import re
import unittest
from test_event32_recipient_scope import parse, value, descendants, CONSTANTS, reserve_package

ROOT_DIR = Path(__file__).resolve().parents[2]
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
        if key == 'custom_trigger_tooltip':
            # The engine evaluates the block's triggers as AND; `tooltip` is only the shown text.
            return all(term(k, v) for k, v in body if k != 'tooltip')
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
                self.assertFalse(evaluate(helper, {f'events_log_disabled_evolution_32_32_{track_type}'}, self.flags))

    def test_special_custody_cannot_override_disabled_track(self):
        flags = self.flags | {'missiles_nuclear_integration_operational'}
        self.assertTrue(evaluate('missiles_special_payload_available', set(), flags))
        self.assertFalse(evaluate('missiles_special_payload_available', {'events_log_disabled_evolution_32_32_3'}, flags))

    def test_preparation_and_commit_share_the_track_gate(self):
        for name in ('missiles_operation_can_be_prepared', 'missiles_operation_can_be_committed'):
            self.assertEqual(dict(OPERATIONS[name]).get('missiles_operation_tracks_are_enabled'), 'yes')
        conventional = {'missiles_operation_strike_profile': constant('constant:missiles_strike_profile.precision'),
                        'missiles_operation_type': constant('constant:missiles_operation.precision'),
                        'missiles_operation_payload': constant('constant:missiles_payload.conventional')}
        disabled = {f'events_log_disabled_evolution_32_32_{i}' for i in range(1, 6)}
        self.assertTrue(evaluate('missiles_operation_tracks_are_enabled', disabled, self.flags, conventional))
        for field, token, track_type in (
            ('missiles_operation_strike_profile', 'constant:missiles_strike_profile.saturation', 1),
            ('missiles_operation_payload', 'constant:missiles_payload.nuclear', 3),
            ('missiles_operation_type', 'constant:missiles_operation.retaliation', 5),
        ):
            case = {**conventional, field: constant(token)}
            self.assertTrue(evaluate('missiles_operation_tracks_are_enabled', set(), self.flags, case))
            self.assertFalse(evaluate('missiles_operation_tracks_are_enabled', {f'events_log_disabled_evolution_32_32_{track_type}'}, self.flags, case))

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
        self.assertFalse(evaluate('missiles_operation_tracks_are_enabled', {'events_log_disabled_evolution_32_32_4'}, flags, variables))

    def test_no_reader_uses_unwritten_legacy_flags(self):
        files = [*ROOT_DIR.glob('common/**/032_missiles*.txt'), ROOT_DIR / 'events/032_missile_crisis.txt']
        for path in files:
            self.assertIsNone(re.search(r'event_evolution_disabled_32_[1-5]\b', path.read_text(encoding='utf-8-sig')), str(path))


EFFECTS = dict(parse((ROOT_DIR / 'common/scripted_effects/032_missiles_operations_effects.txt').read_text(encoding='utf-8-sig')))
CORE_EFFECTS = dict(parse((ROOT_DIR / 'common/scripted_effects/032_missiles_effects.txt').read_text(encoding='utf-8-sig')))
EVENT_LIST = parse((ROOT_DIR / 'events/032_missile_crisis.txt').read_text(encoding='utf-8-sig'))


class EvolutionRegistryContract(unittest.TestCase):
    """Registry and recipient integration retained across the native rewrite."""

    def test_programmes_join_and_leave_the_registry(self):
        self.assertIn(('missiles_register_program', 'yes'), CORE_EFFECTS['missiles_initialize_or_advance_program'])
        capture = list(descendants(EFFECTS['missiles_initialize_capture_shell']))
        self.assertIn(('missiles_register_program', 'yes'), capture)
        removal = list(descendants(EFFECTS['missiles_cleanup_removed_country']))
        self.assertIn(('remove_from_array', [('array', 'global.missiles_program_registry'), ('value', 'THIS')]), removal)
        self.assertIn(('missiles_requeue_pending_evolution_jobs', 'yes'), removal)
        adoption = list(descendants(EFFECTS['missiles_refresh_evolution_access_from_receiver']))
        self.assertIn(('missiles_evaluate_country_evolution_adoption', 'yes'), adoption)

    def test_short_job_and_adoption_receivers_remain_wired(self):
        events = {value(body, 'id'): body for key, body in EVENT_LIST if key == 'country_event'}
        self.assertIn(('immediate', [('missiles_run_evolution_job', 'yes')]), events['chaosx.nr32.190'])
        self.assertIn(('immediate', [('missiles_refresh_evolution_access_from_receiver', 'yes')]), events['chaosx.nr32.8'])


# Catalog order: (missiles_evolution key, roman numeral, loc track key, minimum chaos key).
LOG_TRACKS = (
    ('saturation', 'i', 'saturation', 'minimum_chaos_saturation'),
    ('unreliable_guidance', 'ii', 'unreliable_guidance', 'minimum_chaos_guidance'),
    ('special_warheads', 'iii', 'special_warheads', 'minimum_chaos_special'),
    ('rogue_commands', 'iv', 'rogue_commands', 'minimum_chaos_rogue'),
    ('automatic_retaliation', 'v', 'automatic_retaliation', 'minimum_chaos_retaliation'),
)
# The tier schema holds an anonymous block the source parser does not model,
# so the tier table is read directly.
_TIER_SOURCE = (ROOT_DIR / 'common/script_constants/chaos_meter_constants.txt').read_text(encoding='utf-8-sig')
TIER_RANGES = {name: (float(low), float(high) if high else None) for name, low, high in
               re.findall(r'\b(tier_\w+) = \{ min = (\d+)(?: max = (\d+))?', _TIER_SOURCE)}
_TIER_ID_BLOCK = re.search(r'chaos_meter_tier_id = \{(.*?)\n\}', _TIER_SOURCE, re.S).group(1)
TIER_IDS = {name: float(number) for name, number in re.findall(r'\b(tier_\w+) = (\d+)', _TIER_ID_BLOCK)}
LOG_EFFECTS = dict(parse((ROOT_DIR / 'common/scripted_effects/chaosx_events_log_effects.txt').read_text(encoding='utf-8-sig')))
LOG_TEXTS = {}
for _key, _body in parse((ROOT_DIR / 'common/scripted_localisation/chaosx_scripted_localisation_events_log.txt').read_text(encoding='utf-8-sig')):
    if _key == 'defined_text':
        LOG_TEXTS[value(_body, 'name')] = [dict(text) for key, text in _body if key == 'text']
LOCALISATION = (ROOT_DIR / 'localisation/english/032_missile_crisis_l_english.yml').read_text(encoding='utf-8-sig')


def tier_id(chaos):
    for name, (low, high) in TIER_RANGES.items():
        if low <= chaos and (high is None or chaos <= high):
            return TIER_IDS[name]
    raise AssertionError(chaos)


def keys_matching(surface, *needles):
    """Localisation keys of the surface's text blocks whose trigger holds every needle."""
    found = []
    for text in LOG_TEXTS[surface]:
        trigger = list(descendants(text['trigger']))
        if all(needle in trigger for needle in needles):
            found.append(text['localization_key'])
    return found


class EvolutionLogIdentity(unittest.TestCase):
    """Event Logs identity: type is the event id and stage is the catalog number."""

    def test_constants_use_the_event_id_type_and_real_tiers(self):
        self.assertEqual(constant('constant:missiles_event.evolution_type'), constant('constant:missiles_event.id'))
        for track, roman, _, minimum in LOG_TRACKS:
            with self.subTest(track=track):
                self.assertEqual(constant(f'constant:missiles_event.evolution_{roman}_stage'), constant(f'constant:missiles_evolution.{track}'))
                chaos = constant(f'constant:missiles_evolution_pressure.{minimum}')
                self.assertEqual(constant(f'constant:missiles_event.evolution_{roman}_tier'), tier_id(chaos))

    def test_record_and_commit_share_one_log_context(self):
        context = EFFECTS['missiles_set_evolution_log_context']
        self.assertIn(('set_temp_variable', [('events_log_evolution_event_id', 'constant:missiles_event.id')]), context)
        self.assertIn(('set_temp_variable', [('events_log_evolution_type', 'constant:missiles_event.evolution_type')]), context)
        self.assertIn(('set_temp_variable', [('events_log_evolution_stage', 'missiles_evolution_log_stage_input')]), context)
        branches = [body for key, body in context if key in ('if', 'else_if')]
        self.assertEqual(len(branches), len(LOG_TRACKS))
        for (track, roman, _, _), branch in zip(LOG_TRACKS, branches):
            check = dict(value(value(branch, 'limit'), 'check_variable'))
            self.assertEqual(check['value'], f'constant:missiles_evolution.{track}')
            self.assertIn(('set_temp_variable', [('events_log_evolution_tier', f'constant:missiles_event.evolution_{roman}_tier')]), branch)
        commit = EFFECTS['missiles_commit_evolution_track']
        # Every nested helper output read by commit needs caller-owned storage.
        context_index = commit.index(('missiles_set_evolution_log_context', 'yes'))
        initialized = {body[0][0]: body[0][1] for key, body in commit[:context_index]
                       if key == 'set_temp_variable'}
        self.assertEqual(initialized['missiles_evolution_logged_stage'], 'constant:missiles_event.zero')
        self.assertEqual(initialized['missiles_evolution_log_stage_input'], 'missiles_evolution_selection')
        for key in ('event_id', 'type', 'stage', 'tier', 'has_actor'):
            self.assertIn(f'events_log_evolution_{key}', initialized)
        guarded = value(commit, 'if')
        self.assertIn(('is_current_evolution_enabled', 'yes'), value(guarded, 'limit'))
        acknowledgement = value(guarded, 'if')
        self.assertEqual(value(acknowledgement, 'limit'),
                         [('check_variable', [('missiles_evolution_logged_stage', 'constant:missiles_event.zero')])])
        self.assertIn(('add_to_temp_variable', [('missiles_evolution_commits', 'constant:missiles_program_value.one')]), acknowledgement)
        self.assertEqual(EFFECTS['missiles_record_evolution_unlock'][0],
                         ('set_temp_variable', [('missiles_evolution_logged_stage', 'constant:missiles_event.zero')]))
        writes = [body for key, body in descendants(EFFECTS['missiles_record_evolution_unlock']) if key == 'set_temp_variable']
        for track, *_ in LOG_TRACKS:
            self.assertIn([('missiles_evolution_logged_stage', f'constant:missiles_evolution.{track}')], writes)
        # The record never writes a track number into the shared type.
        self.assertFalse([body for body in writes if body[0][0] == 'events_log_evolution_type'])
        logged = [body for key, body in EFFECTS['missiles_record_evolution_unlock'] if key == 'if'][-1]
        keys = [key for key, _ in logged]
        self.assertLess(keys.index('missiles_set_evolution_log_context'), keys.index('record_events_log_evolution_entry'))
        self.assertIn(('set_temp_variable', [('missiles_evolution_log_stage_input', 'missiles_evolution_logged_stage')]), logged)

    def test_no_reader_uses_the_old_toggle_spelling(self):
        old = re.compile(r'events_log_disabled_evolution_32_[1-5]_1\b|events_log_disabled_evolution_32_\{\w+\}_1')
        paths = [*ROOT_DIR.glob('common/*/032_*'), *ROOT_DIR.glob('events/032_*'), *ROOT_DIR.glob('.tools/tests/test_event32_*.py'),
                 ROOT_DIR / 'common/scripted_effects/chaosx_events_log_effects.txt',
                 ROOT_DIR / 'common/scripted_localisation/chaosx_scripted_localisation_events_log.txt']
        self.assertGreater(len(paths), 10)
        for path in paths:
            if path.suffix in ('.txt', '.py', '.yml'):
                with self.subTest(path=str(path.relative_to(ROOT_DIR))):
                    self.assertIsNone(old.search(path.read_text(encoding='utf-8-sig', errors='replace')))

    def test_event_details_preview_offers_every_track_toggle(self):
        rebuild = LOG_EFFECTS['events_log_rebuild_open_event_details_view']
        blocks = [body for key, body in descendants(rebuild) if key == 'if' and ('check_variable', [('var', 'event_id'), ('value', 'constant:missiles_event.id'), ('compare', 'equals')]) in value(body, 'limit')]
        self.assertEqual(len(blocks), 1)
        rows = [body for key, body in blocks[0] if key == 'set_temp_variable']
        self.assertEqual(sum(1 for key, _ in blocks[0] if key == 'events_log_add_event_detail_evolution_preview'), len(LOG_TRACKS))
        for _, roman, _, _ in LOG_TRACKS:
            self.assertIn([('events_log_event_detail_preview_stage', f'constant:missiles_event.evolution_{roman}_stage')], rows)
            self.assertIn([('events_log_event_detail_preview_tier', f'constant:missiles_event.evolution_{roman}_tier')], rows)
        self.assertEqual(rows.count([('events_log_event_detail_preview_type', 'constant:missiles_event.evolution_type')]), len(LOG_TRACKS))

    def test_every_log_surface_names_the_event_32_tracks(self):
        type_needle = 'constant:missiles_event.evolution_type'
        for surface in ('GetEventsLogEvolutionTypeView', 'GetEventsLogSelectedHistoryEvolutionTypeView', 'GetEventsLogEventDetailEvolutionTypeView'):
            with self.subTest(surface=surface):
                keys = [text['localization_key'] for text in LOG_TEXTS[surface] if any(v == type_needle for _, v in descendants(text['trigger']))]
                self.assertEqual(keys, ['missiles.evolution.type'])
        stage_surfaces = {
            'GetEventsLogEvolutionNameView': 'title',
            'GetEventsLogSelectedHistoryEvolutionNameView': 'title',
            'GetEventsLogEventDetailEvolutionTitle': 'title',
            'GetEventsLogSelectedEvolutionTitle': 'title',
            'GetEventsLogSelectedEvolutionBody': 'body',
        }
        for surface, suffix in stage_surfaces.items():
            for _, roman, loc, _ in LOG_TRACKS:
                stage = f'constant:missiles_event.evolution_{roman}_stage'
                with self.subTest(surface=surface, stage=roman):
                    keys = [text['localization_key'] for text in LOG_TEXTS[surface]
                            if {type_needle, stage} <= {v for _, v in descendants(text['trigger']) if isinstance(v, str)}]
                    self.assertEqual(keys, [f'missiles.evolution.{loc}.{suffix}'])
        summary = [text['localization_key'] for text in LOG_TEXTS['GetEventsLogSelectedEvolutionSummary'] if any(v == type_needle for _, v in descendants(text['trigger']))]
        self.assertEqual(summary, ['missiles.evolution.summary'])
        detail = [text['localization_key'] for text in LOG_TEXTS['GetEventsLogEventDetailDescription'] if any(v == 'constant:missiles_event.id' for _, v in descendants(text['trigger']))]
        self.assertEqual(detail, ['missiles.event_log.detail'])
        # History rows show the event name like every other event; Event 32
        # keeps no bespoke recipient-count row on the shared history surface.
        history = [text['localization_key'] for text in LOG_TEXTS['GetEventsLogHistoryRowText'] if any(v == 'constant:missiles_event.id' for _, v in descendants(text['trigger']))]
        self.assertEqual(history, [])
        used = {'missiles.evolution.type', 'missiles.evolution.summary', 'missiles.event_log.detail'}
        used |= {f'missiles.evolution.{loc}.{suffix}' for _, _, loc, _ in LOG_TRACKS for suffix in ('title', 'body')}
        for key in sorted(used):
            self.assertRegex(LOCALISATION, rf'(?m)^{re.escape(key)}: "')


if __name__ == '__main__':
    unittest.main()
