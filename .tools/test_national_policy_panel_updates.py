"""Execute production open-panel observation and cache projection contracts.

Usage: python .tools/test_national_policy_panel_updates.py
Native event delivery is a deterministic queue with copied chain-local targets.
Camp authority/provenance predicates and sale quote consumers are declared fixtures.
Actual observer, panel collection, selection, work and camp cache bodies execute.
This verifies source contracts, not native GUI rendering or engine scheduling.
"""
from pathlib import Path
from contextlib import redirect_stdout
import io, sys, importlib.util, unittest, copy, re

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.tools'))
with redirect_stdout(io.StringIO()):
    import test_humanitarian_panels as H
P, Scope = H.P, H.Scope


class Runtime(H.Runtime):
    EXTERNAL_FIXTURES = (H.Runtime.EXTERNAL_FIXTURES - {'national_policy_panel_request_observer'}) | {
        'camp_admin_refresh_command_quotes', 'camp_admin_generic_reform_refresh_quote',
        'national_policy_reconcile_country', 'national_policy_initialize_cost_modifiers',
        'national_policy_apply_starting_profile'
    }

    def __init__(self, states=()):
        super().__init__(states)
        self.queue, self.refreshes = [], []
        self.effect_defs.update(P.read_definitions('common/scripted_effects/national_policy_panel_effects.txt'))
        self.trigger_defs.update(P.read_definitions('common/scripted_triggers/national_policy_panel_triggers.txt'))
        for name in ('national_policy_initialize_country', 'national_policy_initialize_released_country'):
            self.effect_defs[name] = H.read_named('common/scripted_effects/national_policy_effects.txt', name)
        for name in ('camp_admin_refresh_interface', 'camp_admin_project_origin_uncertainty',
                     'camp_admin_project_institution_progress', 'camp_admin_cache_selected_site',
                     'camp_admin_append_display_source', 'camp_admin_close_pickers'):
            self.effect_defs[name] = H.read_named('common/scripted_effects/camp_administration_ui_effects.txt', name)
        self.effect_defs['camp_admin_prepare_project_quote'] = H.read_named('common/scripted_effects/camp_administration_effects.txt', 'camp_admin_prepare_project_quote')
        self.trigger_defs['camp_admin_site_is_original_record'] = H.read_named('common/scripted_triggers/camp_administration_triggers.txt', 'camp_admin_site_is_original_record')
        for path in (ROOT / 'common/script_constants').glob('camp*.txt'):
            for group, definition in P.read_definitions(str(path.relative_to(ROOT))).items():
                for node in definition.body:
                    if isinstance(node.value, str) and P.NUMBER.fullmatch(node.value):
                        self.constants['constant:' + group + '.' + node.key] = H.Decimal(node.value)
        raw = (ROOT / 'common/scripted_effects/national_policy_panel_effects.txt').read_text()
        self.file_constants['national_policy_panel_refresh_hours'] = int(re.search(r'@national_policy_panel_refresh_hours = (\d+)', raw)[1])

    def _write_path(self, path, value, clear=False):
        country, field, global_scope = self._path_container(path)
        assert not global_scope and country.kind == 'country'
        assert field.startswith(('famine_panel_', 'migration_panel_', 'national_policy_panel_', 'camp_admin_gui_')) or field in {'camp_admin_view', 'camp_admin_location_filter', 'camp_selected_state_id'}
        P.Event35Runtime._write_path(self, path, value, clear)

    def _value(self, token):
        value = super()._value(token)
        if isinstance(value, str) and token.startswith('camp_'):
            return self._variable(token)
        return value

    def _condition(self, node, scope):
        if node.key == 'has_event_target':
            return node.value in self.targets
        if node.key == 'tag':
            return self._same(scope, self._value(node.value))
        if node.key in ('camp_rework_country_is_eligible', 'has_camp_category_visible_action'):
            return scope.values.get('fixture_camp_eligible', False)
        if node.key == 'camp_admin_gui_host_records_uncertain':
            return 'camp_origin_records_unresolved' in scope.flags
        if node.key == 'camp_admin_gui_site_record_visible':
            return self._conditions(self.trigger_defs['camp_admin_site_is_original_record'].body, scope) and (scope.controller is self._scope_for_prefix('PREV') or 'camp_admin_closed' in scope.flags)
        if node.key == 'camp_admin_gui_site_has_current_output':
            return self._conditions(self.trigger_defs['camp_admin_site_is_original_record'].body, scope) and scope.controller is self._scope_for_prefix('PREV') and 'camp_admin_closed' not in scope.flags
        if node.key == 'camp_admin_country_is_major_kit':
            return False
        if node.key in ('national_policy_country_uses_civilian_laws', 'national_policy_country_uses_warfare_laws'):
            return False
        return super()._condition(node, scope)

    def _call_effect(self, name, scope):
        if name in ('famine_panel_refresh', 'migration_panel_refresh', 'camp_admin_refresh_interface'):
            self.refreshes.append((name, scope.id))
        return super()._call_effect(name, scope)

    def _effects(self, nodes, scope):
        # Preserve normal if/else grouping, but honor the documented inherited
        # break variable before entering a foreach in the projection model.
        chunk = []
        for node in nodes:
            if node.key in ('for_each_scope_loop', 'for_each_loop'):
                if chunk:
                    super()._effects(chunk, scope)
                    chunk = []
                stop = P.first(node.value, 'break', 'break')
                if self._variable(stop) == 0:
                    super()._effects([node], scope)
            else:
                chunk.append(node)
        if chunk:
            super()._effects(chunk, scope)

    def _native_effect(self, key, value, scope, line):
        if key == 'country_event':
            assert P.first(value, 'id') == 'national_policy_panel.1'
            hours = self._value(P.first(value, 'hours'))
            assert hours == 1
            due = H.Decimal(str(self.globals['date'])) + H.Decimal(str(hours)) / H.Decimal(100000)
            self.queue.append((scope, dict(self.targets), hours, due))
            return
        return super()._native_effect(key, value, scope, line)

    def deliver(self, advance=True):
        actor, targets, hours, due = self.queue.pop(0)
        if advance:
            self.globals['date'] = max(H.Decimal(str(self.globals['date'])), due)
        old = self.targets
        self.targets = targets
        try:
            definition = H.read_named('events/national_policy_panel_events.txt', 'country_event')
            self.run_nodes(P.first(definition.body, 'immediate'), actor)
        finally:
            self.targets = old

    def run_nodes(self, nodes, actor):
        old = self.root, self.scope_stack
        self.root, self.scope_stack = actor, [actor]
        try:
            self._effects(nodes, actor)
        finally:
            self.root, self.scope_stack = old


class UpdateTests(unittest.TestCase):
    def test_native_gui_getters_are_not_dirty_gated_and_refresh_button_is_unbound(self):
        for name in ('migration_management', 'famine_management', 'camp_repression_ledger'):
            source = (ROOT / f'common/scripted_guis/{name}_scripted_gui.txt').read_text()
            self.assertNotRegex(source, r'(?m)^\s*dirty\s*=')
            self.assertNotIn('_panel_refresh_button_', source)

    def test_quiet_open_close_reopen_reuses_one_delivery_and_closed_delivery_does_no_refresh(self):
        actor = H.country()
        runtime = Runtime()
        runtime.run_effect('famine_panel_open_window', actor)
        self.assertEqual(len(runtime.queue), 1)
        runtime.run_effect('famine_panel_close_window', actor)
        runtime.run_effect('migration_panel_open_window', actor)
        self.assertEqual(len(runtime.queue), 1)
        runtime.deliver()
        self.assertEqual(len(runtime.queue), 1)
        self.assertEqual(runtime.refreshes[-1], ('migration_panel_refresh', actor.id))
        runtime.run_effect('migration_panel_close_window', actor)
        before = H.gameplay(runtime, actor)
        refreshes = list(runtime.refreshes)
        runtime.deliver()
        self.assertEqual(runtime.queue, [])
        self.assertEqual(runtime.refreshes, refreshes)
        self.assertEqual(H.gameplay(runtime, actor), before)
        self.assertNotIn('national_policy_panel_observer_pending', actor.flags)
        self.assertNotIn('national_policy_panel_observer_owner', actor.values)
        self.assertEqual(runtime.global_arrays, {})

    def test_hourly_delivery_reprojects_published_changes_capture_selection_and_real_progress(self):
        actor, foreign = H.country(), H.country('GER')
        first = H.state(1, actor, flags=['famine_food_security_active'], famine_food_stage=1)
        second = H.state(2, actor, flags=['famine_food_security_active'], famine_food_stage=2)
        runtime = Runtime([first, second])
        runtime.run_effect('famine_panel_open_window', actor)
        self.assertIs(actor.values['famine_panel_selected_state'], second)
        second.owner = second.controller = foreign
        first.values['famine_food_stage'] = 4
        actor.arrays.update(famine_action_ids=[7], famine_action_types=[1], famine_action_states=[first], famine_action_starts=[0], famine_action_dates=[0.0048])
        runtime.globals['date'] = 0.0024
        before = H.gameplay(runtime, actor)
        runtime.deliver()
        self.assertEqual(actor.arrays['famine_panel_states'], [first])
        self.assertIs(actor.values['famine_panel_selected_state'], first)
        self.assertEqual(actor.values['famine_panel_food_stage'], 4)
        self.assertEqual(actor.values['famine_panel_work_frame'], 6)
        self.assertEqual(H.gameplay(runtime, actor), before)

    def test_eligibility_loss_retires_chain_and_closes_the_window(self):
        actor = H.country()
        runtime = Runtime()
        runtime.run_effect('famine_panel_open_window', actor)
        actor.ai = True
        runtime.deliver()
        self.assertNotIn('famine_panel_open', actor.flags)
        self.assertNotIn('national_policy_panel_observer_pending', actor.flags)
        self.assertEqual(runtime.queue, [])

    def test_migration_delivery_updates_live_amounts_capacity_proof_and_progress(self):
        actor = H.country()
        site = H.state(9, actor, migration_state_flight_population=100)
        runtime = Runtime([site])
        runtime.run_effect('migration_panel_open_window', actor)
        site.values['migration_state_flight_population'] = 250
        actor.values.update(migration_reception_capacity_schema_version=runtime.constants['constant:migration_capacity.schema_version'], migration_reception_capacity_valid=1, migration_reception_capacity_dirty=0, migration_reception_capacity_revision=1, migration_reception_capacity=300, migration_reception_load=250, migration_reception_candidate_count=1, migration_reception_safe_candidate_count=1, migration_reception_invalid_candidate_count=0)
        actor.arrays.update(migration_action_ids=[8], migration_action_types=[2], migration_action_states=[site], migration_action_starts=[0], migration_action_dates=[0.0048])
        runtime.globals['date'] = 0.0024
        before = H.gameplay(runtime, actor)
        runtime.deliver()
        self.assertEqual(actor.values['migration_panel_fleeing'], 250)
        self.assertEqual(actor.values['migration_panel_capacity'], 300)
        self.assertIn('migration_panel_capacity_assessed', actor.flags)
        self.assertEqual(actor.values['migration_panel_work_frame'], 6)
        self.assertEqual(H.gameplay(runtime, actor), before)
        actor.values['migration_reception_capacity_dirty'] = 1
        runtime.deliver()
        self.assertNotIn('migration_panel_capacity_assessed', actor.flags)

    def test_inherited_pending_owner_cannot_suppress_child_or_refresh_another_country(self):
        actor, child = H.country(), H.country('D01')
        runtime = Runtime()
        runtime.run_effect('famine_panel_open_window', actor)
        child.values['national_policy_panel_observer_owner'] = actor
        child.flags.add('national_policy_panel_observer_pending')
        runtime.run_effect('famine_panel_open_window', child)
        self.assertEqual(len(runtime.queue), 2)
        self.assertIs(child.values['national_policy_panel_observer_owner'], child)
        runtime.targets['national_policy_panel_observer_actor'] = actor
        count = len(runtime.refreshes)
        runtime.run_effect('national_policy_panel_observe', child)
        self.assertEqual(len(runtime.refreshes), count)
        runtime.deliver()
        runtime.deliver()
        self.assertEqual(sorted(item[0].id for item in runtime.queue), ['D01', 'FRA'])

    def test_annex_cancellation_rerelease_and_old_delivery_cannot_consume_new_hour(self):
        actor = H.country()
        runtime = Runtime()
        runtime.run_effect('famine_panel_open_window', actor)
        old_event = runtime.queue.pop(0)  # The native queue may cancel it on annexation.
        actor.exists = False
        on_actions = H.read_named('common/on_actions/humanitarian_runtime_on_actions.txt', 'on_actions')
        annex = P.first(P.first(on_actions.body, 'on_annex'), 'effect')
        old_country_body = P.first(annex, 'FROM')
        self.assertEqual(old_country_body[0].key, 'national_policy_panel_retire_country')
        runtime.run_nodes([old_country_body[0]], actor)
        self.assertNotIn('national_policy_panel_observer_pending', actor.flags)
        self.assertNotIn('national_policy_panel_observer_earliest', actor.values)
        self.assertNotIn('famine_panel_open', actor.flags)
        actor.exists = True
        runtime.globals['date'] = H.Decimal('0.00001')
        runtime.run_effect('national_policy_initialize_released_country', actor)
        runtime.run_effect('famine_panel_open_window', actor)
        self.assertEqual(len(runtime.queue), 1)
        self.assertEqual(actor.values['national_policy_panel_observer_earliest'], H.Decimal('0.00002'))
        fresh_event = runtime.queue.pop(0)
        runtime.queue = [old_event, fresh_event]
        before = dict(actor.values), set(actor.flags), list(runtime.refreshes)
        runtime.deliver(advance=False)  # An old chain arrives before the fresh reservation.
        self.assertEqual((actor.values, actor.flags, runtime.refreshes), before)
        self.assertEqual(len(runtime.queue), 1)
        runtime.deliver()
        self.assertEqual(len(runtime.queue), 1)
        self.assertEqual(actor.values['national_policy_panel_observer_earliest'], H.Decimal('0.00003'))
        # A duplicate old delivery at the same hour also cannot steal the next slot.
        runtime.queue.insert(0, old_event)
        count = len(runtime.refreshes)
        runtime.deliver(advance=False)
        self.assertEqual(len(runtime.refreshes), count)
        self.assertEqual(len(runtime.queue), 1)

    def test_country_initialization_cleans_copied_identity_but_preserves_own_chain(self):
        actor, child = H.country(), H.country('D01')
        runtime = Runtime()
        runtime.run_effect('famine_panel_open_window', actor)
        pending = actor.values['national_policy_panel_observer_earliest']
        runtime.run_effect('national_policy_initialize_country', actor)
        self.assertEqual(actor.values['national_policy_panel_observer_earliest'], pending)
        self.assertIn('famine_panel_open', actor.flags)
        child.values.update(national_policy_panel_observer_owner=actor, national_policy_panel_observer_earliest=pending)
        child.flags.update({'national_policy_panel_observer_pending', 'famine_panel_open', 'camp_repression_ledger_open'})
        runtime.run_effect('national_policy_initialize_country', child)
        self.assertNotIn('famine_panel_open', child.flags)
        self.assertNotIn('camp_repression_ledger_open', child.flags)
        self.assertNotIn('national_policy_panel_observer_pending', child.flags)
        self.assertNotIn('national_policy_panel_observer_earliest', child.values)
        runtime.run_effect('famine_panel_open_window', child)
        self.assertEqual(len(runtime.queue), 2)

    def test_old_and_fresh_delivery_at_same_due_hour_leave_one_successor(self):
        for old_first in (False, True):
            actor = H.country()
            runtime = Runtime()
            runtime.run_effect('famine_panel_open_window', actor)
            old = runtime.queue.pop(0)
            runtime.run_effect('national_policy_panel_retire_country', actor)
            runtime.run_effect('famine_panel_open_window', actor)
            fresh = runtime.queue.pop(0)
            runtime.queue = [old, fresh] if old_first else [fresh, old]
            count = len(runtime.refreshes)
            runtime.deliver()
            runtime.deliver()
            self.assertEqual(len(runtime.refreshes), count + 1)
            self.assertEqual(len(runtime.queue), 1)
            self.assertEqual(actor.values['national_policy_panel_observer_earliest'], H.Decimal('0.00002'))

    def test_camp_terminal_close_uses_same_pure_ui_retirement(self):
        actor = H.country()
        actor.values['fixture_camp_eligible'] = True
        actor.flags.add('camp_repression_ledger_open')
        runtime = Runtime()
        runtime.run_effect('national_policy_panel_request_observer', actor)
        close = H.read_named('common/scripted_effects/camp_administration_integration_effects.txt', 'camp_admin_integration_close_country')
        self.assertEqual(close.body[0].key, 'national_policy_panel_retire_country')
        runtime.run_nodes([close.body[0]], actor)
        self.assertNotIn('camp_repression_ledger_open', actor.flags)
        self.assertNotIn('national_policy_panel_observer_pending', actor.flags)
        refreshes = list(runtime.refreshes)
        runtime.deliver()
        self.assertEqual(runtime.refreshes, refreshes)
        self.assertEqual(runtime.queue, [])

    def test_camp_projection_reads_registered_records_and_never_initializes_or_ticks_them(self):
        actor = H.country()
        actor.values.update(fixture_camp_eligible=True, camp_admin_economy_progress=5, camp_admin_economy_target=10)
        actor.flags.update({'camp_repression_ledger_open', 'camp_admin_civil_review_active'})
        actor.values['camp_admin_civil_review_progress'] = 1
        site = H.state(7, actor, flags=['camp_admin_initialized'], camp_admin_responsible_country=actor, camp_admin_capacity_k=2, camp_admin_detainees_k=1, camp_admin_support_ratio=1)
        actor.arrays['camp_active_site_states'] = [site]
        runtime = Runtime([site])
        runtime.temp_frames[0]['break'] = 1
        before_site = copy.deepcopy((site.flags, site.resources, site.population_k, {k: v for k, v in site.values.items() if k != 'camp_admin_responsible_country'}))
        runtime.run_effect('national_policy_panel_refresh_open', actor)
        self.assertEqual(actor.arrays['camp_admin_gui_states'], [site])
        self.assertIs(actor.values['camp_selected_state_id'], site)
        self.assertEqual(actor.values['camp_admin_gui_site_capacity_k'], 2)
        self.assertEqual(actor.values['camp_admin_gui_economy_frame'], 6)
        self.assertEqual(actor.values['camp_admin_gui_project_pp'], runtime.constants['constant:camp_admin_value.project_pp'])
        site.values['camp_admin_capacity_k'] = 3
        runtime.run_effect('national_policy_panel_refresh_open', actor)
        self.assertEqual(actor.values['camp_admin_gui_site_capacity_k'], 3)
        site.values['camp_admin_capacity_k'] = 2
        self.assertEqual((site.flags, site.resources, site.population_k, {k: v for k, v in site.values.items() if k != 'camp_admin_responsible_country'}), before_site)
        self.assertNotIn('camp_admin_monthly_country', [name for name, *_ in runtime.external_calls])
        site.controller = H.country('GER')
        runtime.run_effect('national_policy_panel_refresh_open', actor)
        self.assertEqual(actor.arrays['camp_admin_gui_states'], [])
        self.assertNotIn('camp_selected_state_id', actor.values)
        actor.flags.remove('camp_repression_ledger_open')
        refreshes, values = list(runtime.refreshes), dict(actor.values)
        runtime.run_effect('national_policy_panel_refresh_open', actor)
        self.assertEqual(runtime.refreshes, refreshes)
        self.assertEqual(actor.values, values)

    def test_native_action_bridges_refresh_open_panels_after_accounting_while_paused(self):
        import test_humanitarian_gui_actions as A
        runtime, actor, site, host = A.case()
        runtime.effect_defs['national_policy_panel_refresh_open'] = H.read_named('common/scripted_effects/national_policy_panel_effects.txt', 'national_policy_panel_refresh_open')
        runtime.EXTERNAL_EFFECTS = runtime.EXTERNAL_EFFECTS - {'national_policy_panel_refresh_open'}
        runtime.EXTERNAL_FIXTURES = runtime.EXTERNAL_FIXTURES - {'national_policy_panel_refresh_open'}
        runtime.trigger_defs['humanitarian_panel_is_eligible'] = H.read_named('common/scripted_triggers/humanitarian_panel_triggers.txt', 'humanitarian_panel_is_eligible')
        actor.flags.add('famine_panel_open')
        A.start(runtime, actor, 1)
        self.assertIn(('famine_panel_refresh', actor.id), runtime.panel_refresh_requests)


if __name__ == '__main__':
    unittest.main(verbosity=2)
