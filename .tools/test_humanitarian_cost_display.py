"""Run transport display getters with conservative helper temporary frames.

Usage: python .tools/test_humanitarian_cost_display.py
Reads the production display resolver, selected-state guards, six localisation
selectors and original transport predicates through the humanitarian fixture.
Writes .tmp/national_policy_panels/cost_display_test_results.json.
Native geography/resources are fixture facts, not observed engine behavior.
"""
from pathlib import Path
import hashlib
import json
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.tools'))
import test_humanitarian_gui_actions as H

SOURCE = 'common/scripted_localisation/migration_transport_cost_scripted_localisation.txt'
RESOLVER = 'humanitarian_cost_display_resolve_target'
TARGET = 'migration_transport_target'
FAMILIES = ('Light', 'Standard', 'Heavy')


class Runtime(H.Runtime):
    def __init__(self):
        super().__init__()
        for name in ('humanitarian_panel_triggers', 'humanitarian_cost_display_triggers'):
            self.trigger_defs.update(H.read_defs('common/scripted_triggers/' + name + '.txt'))
        self.helper_output_at_return = []
        raw = (ROOT / SOURCE).read_text(encoding='utf-8-sig')
        nodes, _ = H.P.parse_nodes(H.P.lex(H.P.uncomment(raw)), 0, SOURCE)
        self.getters = {H.P.first(n.value, 'name'): H.F.adapt_nodes(n.value) for n in nodes}

    def _run_trigger(self, name, scope):
        # Match the documented conservative lifetime at every helper boundary.
        self.temp_frames.append({})
        try:
            result = super()._run_trigger(name, scope)
        finally:
            self.temp_frames.pop()
        if name == RESOLVER:
            self.helper_output_at_return.append((result, self._variable(TARGET)))
        return result

    def display(self, getter, actor, native_from=None, seed=None):
        self.root = actor
        self.scope_stack = [actor]
        self.temp_frames = [dict(seed or {})]
        self.from_scope = native_from
        for entry in self.getters[getter]:
            if entry.key != 'text':
                continue
            if self._conditions(H.P.first(entry.value, 'trigger', []), actor):
                return H.P.first(entry.value, 'localization_key'), self._variable(TARGET)
        raise AssertionError('No localisation fallback: ' + getter)


_runtime = None


def case(context='migration', mainland=True, fuel=100000, convoys=100):
    # Source definitions/constants are read once. Each case gets fresh scopes,
    # caller frames and return evidence, while read-only helper bodies are reused.
    global _runtime
    if _runtime is None:
        _runtime = Runtime()
    runtime = _runtime
    runtime.helper_output_at_return = []
    actor = H.F.country('FRA')
    selected = H.F.state(42, actor)
    native = H.F.state(43, actor)
    selected.values['is_in_home_area'] = mainland
    native.values['is_in_home_area'] = mainland
    actor.resources.update(fuel=fuel, convoy_1=convoys)
    if context != 'native':
        actor.flags.add(context + '_panel_open')
        actor.values[context + '_panel_selected_state'] = selected
        actor.arrays[context + '_panel_states'] = [selected]
    return runtime, actor, selected, native


class ContractTests(unittest.TestCase):
    def test_valid_panel_and_native_targets_survive_helper_return(self):
        for context in ('famine', 'migration', 'native'):
            for mainland in (True, False):
                for family in FAMILIES:
                    tier = family.lower()
                    for kind in ('Fuel', 'Convoys'):
                        with self.subTest(context=context, mainland=mainland, family=family, kind=kind):
                            runtime, actor, selected, native = case(context, mainland)
                            before = (dict(actor.resources), set(actor.flags), dict(actor.values), {k: list(v) for k, v in actor.arrays.items()})
                            key, target = runtime.display('GetMigrationTransport' + family + kind + 'Cost', actor, native)
                            expected = native if context == 'native' else selected
                            self.assertIs(target, expected)
                            suffix = 'fuel_land_ready' if mainland else 'fuel_sea_ready'
                            if kind == 'Convoys':
                                suffix = 'no_convoys' if mainland else tier + '_convoys_sea_ready'
                                expected_key = 'migration_transport_' + suffix
                            else:
                                expected_key = 'migration_transport_' + tier + '_' + suffix
                            self.assertEqual(key, expected_key)
                            self.assertTrue(runtime.helper_output_at_return)
                            self.assertTrue(all(ok and out is expected for ok, out in runtime.helper_output_at_return))
                            self.assertEqual((actor.resources, actor.flags, actor.values, actor.arrays), before)
                            self.assertEqual(runtime.resource_writes, [])

    def test_ready_and_blocked_states_use_existing_affordability_thresholds(self):
        for context in ('famine', 'migration', 'native'):
            for family in FAMILIES:
                for mainland in (True, False):
                    for delta in (-1, 0, 1):
                        runtime, actor, selected, native = case(context, mainland)
                        tier = family.lower()
                        route = 'land' if mainland else 'sea'
                        fee = runtime.constants['constant:migration_transport_cost.' + tier + '_fuel_' + route]
                        actor.resources['fuel'] = fee + delta
                        key, _ = runtime.display('GetMigrationTransport' + family + 'FuelCost', actor, native)
                        self.assertEqual(key, 'migration_transport_' + tier + '_fuel_' + route + ('_blocked' if delta < 0 else '_ready'))
                        if not mainland:
                            convoy_fee = runtime.constants['constant:migration_transport_cost.' + tier + '_convoys_sea']
                            actor.resources['convoy_1'] = convoy_fee + delta
                            key, _ = runtime.display('GetMigrationTransport' + family + 'ConvoysCost', actor, native)
                            self.assertEqual(key, 'migration_transport_' + tier + '_convoys_sea' + ('_blocked' if delta < 0 else '_ready'))

    def test_invalid_selection_resets_stale_output_and_fails_closed(self):
        for context in ('famine', 'migration'):
            for invalid in ('missing', 'not_in_list', 'lost_control'):
                for family in FAMILIES:
                    for kind in ('Fuel', 'Convoys'):
                        runtime, actor, selected, native = case(context)
                        if invalid == 'missing':
                            actor.values.pop(context + '_panel_selected_state')
                        elif invalid == 'not_in_list':
                            actor.arrays[context + '_panel_states'] = []
                        else:
                            selected.owner = selected.controller = H.F.country('ENG')
                        key, target = runtime.display('GetMigrationTransport' + family + kind + 'Cost', actor, native, {TARGET: native})
                        self.assertEqual(key, 'migration_transport_unavailable')
                        self.assertEqual(target, 0)
                        self.assertTrue(all(not ok and out == 0 for ok, out in runtime.helper_output_at_return))

    def test_missing_caller_initialization_reproduces_lost_output(self):
        runtime, actor, selected, native = case()
        runtime.root, runtime.scope_stack, runtime.temp_frames = actor, [actor], [{}]
        self.assertTrue(runtime._run_trigger(RESOLVER, actor))
        self.assertEqual(runtime._variable(TARGET), 0)
        # Exercise every production branch as parsed, rather than duplicating it.
        guarded_calls = 0
        for family in FAMILIES:
            for kind in ('Fuel', 'Convoys'):
                body = runtime.getters['GetMigrationTransport' + family + kind + 'Cost']
                for entry in body:
                    if entry.key != 'text':
                        continue
                    trigger = H.P.first(entry.value, 'trigger', [])
                    calls = [i for i, n in enumerate(trigger) if n.key == RESOLVER]
                    for index in calls:
                        guarded_calls += 1
                        self.assertGreater(index, 0)
                        initialize = trigger[index - 1]
                        self.assertEqual(initialize.key, 'set_temp_variable')
                        self.assertEqual([(n.key, n.value) for n in initialize.value], [(TARGET, 'constant:migration_transport_cost.zero')])
        self.assertEqual(guarded_calls, 21)


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(ContractTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    evidence = {
        'tests_run': result.testsRun,
        'passed': result.wasSuccessful(),
        'coverage': ['36 valid native/panel land/sea resource displays', '54 fuel boundary cases and 27 sea-convoy boundary cases', '36 missing/stale/lost-control selection displays with stale output seeded', 'Negative control loses helper-created output without caller initialization', 'All 21 production calls have immediate caller-owned zero initialization'],
        'source_sha256': {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in (SOURCE, 'common/scripted_triggers/humanitarian_cost_display_triggers.txt', 'common/scripted_triggers/humanitarian_panel_triggers.txt', 'common/scripted_triggers/migration_transport_cost_triggers.txt', '.tools/test_humanitarian_cost_display.py', '.tools/test_humanitarian_gui_actions.py', '.tools/test_famine_takeover_20261006.py', '.tools/test_event035_center_projects.py')},
        'limitations': ['Conservative source interpreter, not native localisation execution', 'Native geography and resource stocks are declared fixture facts', 'No GUI render, game run or payment change'],
    }
    output = ROOT / '.tmp/national_policy_panels/cost_display_test_results.json'
    output.write_text(json.dumps(evidence, indent=2) + '\n', encoding='utf-8')
    raise SystemExit(0 if result.wasSuccessful() else 1)
