"""Execute production open-panel observation and cache projection contracts.

Usage: python .tools/tests/test_national_policy_panel_updates.py
All source publication scenarios retain the same game date; scheduling is rejected.
Camp authority/provenance predicates and sale quote consumers are declared fixtures.
Actual publisher, panel collection, selection, work and camp cache bodies execute.
This verifies source contracts, not native GUI rendering or engine scheduling.
"""
from pathlib import Path
from contextlib import redirect_stdout
import io, sys, importlib.util, unittest, copy, re

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / '.tools/tests'))
with redirect_stdout(io.StringIO()):
    import test_humanitarian_panels as H
P, Scope = H.P, H.Scope


class Runtime(H.Runtime):
    EXTERNAL_FIXTURES = H.Runtime.EXTERNAL_FIXTURES | {
        'camp_admin_refresh_command_quotes', 'camp_admin_generic_reform_refresh_quote',
        'national_policy_reconcile_country', 'national_policy_initialize_cost_modifiers',
        'national_policy_apply_starting_profile'
    }

    def __init__(self, states=()):
        super().__init__(states)
        self.queue, self.refreshes = [], []
        self.effect_defs.update(P.read_definitions('common/scripted_effects/national_policy_panel_effects.txt'))
        self.trigger_defs.update(P.read_definitions('common/scripted_triggers/national_policy_panel_triggers.txt'))
        self.trigger_defs.update(P.read_definitions('common/scripted_triggers/camp_administration_ui_triggers.txt'))
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

    def _run_trigger(self,name,scope):
        # Same conservative lifetime used for effect helpers: outputs require caller storage.
        self.temp_frames.append({})
        try:return super()._run_trigger(name,scope)
        finally:self.temp_frames.pop()

    def _array_values(self,path):
        if isinstance(path,str) and '.' not in path:
            for frame in reversed(self.temp_frames):
                if path in frame and isinstance(frame[path],list):return frame[path]
        return super()._array_values(path)

    def _array_value(self,container,path):
        base,sep,index=path.partition('^')
        for frame in reversed(self.temp_frames):
            if base in frame and isinstance(frame[base],list):
                values=frame[base]
                if index=='num':return len(values)
                if index:
                    idx=int(self._value(index));return values[idx] if 0<=idx<len(values) else 0
                return values
        return super()._array_value(container,path)

    def _write_path(self, path, value, clear=False):
        country, field, global_scope = self._path_container(path)
        assert not global_scope and country.kind == 'country'
        assert field.startswith(('famine_panel_', 'migration_panel_', 'national_policy_panel_', 'camp_admin_gui_')) or field in {'camp_admin_view', 'camp_admin_location_filter', 'camp_selected_state_id'}
        P.Event35Runtime._write_path(self, path, value, clear)

    def _value(self, token):
        value = super()._value(token)
        if isinstance(value, str) and token.startswith(('camp_', 'national_policy_panel_')):
            return self._variable(token)
        return value

    def _condition(self, node, scope):
        if node.key=='clear_temp_array':self._set_temp(node.value,[]);return True
        if node.key=='add_to_temp_array':
            name=P.first(node.value,'array');values=list(self._array_values(name))
            values.append(self._value(P.first(node.value,'value','THIS')))
            self._set_temp(name,values);return True
        if node.key=='all_of_scopes':
            for target in list(self._array_values(P.first(node.value,'array'))):
                self.scope_stack.append(target)
                try:
                    if not self._conditions([n for n in node.value if n.key!='array'],target):return False
                finally:self.scope_stack.pop()
            return True
        if node.key in ('add_to_temp_variable','multiply_temp_variable','divide_temp_variable','round_temp_variable','clamp_temp_variable','if'):
            self._effects([node],scope)
            return True
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
            if node.key in ('clear_temp_array','add_to_temp_array'):
                if chunk:
                    super()._effects(chunk,scope);chunk=[]
                self._condition(node,scope)
            elif node.key in ('owner','controller'):
                if chunk:
                    super()._effects(chunk,scope)
                    chunk=[]
                target=getattr(scope,node.key)
                if target is not None:
                    self.scope_stack.append(target)
                    try:self._effects(node.value,target)
                    finally:self.scope_stack.pop()
            elif node.key in ('for_each_scope_loop', 'for_each_loop'):
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
            assert P.first(value,'id')=='national_policy_panel.2'
            assert len(value)==1, 'Presentation event must have no delay or random fields'
            # Documented event boundary: fresh temporaries, actor ROOT, copied regular targets.
            old=self.temp_frames,self.root,self.scope_stack,self.targets
            self.temp_frames=[{}];self.root=scope;self.scope_stack=[scope];self.targets=dict(self.targets)
            try:
                raw=(ROOT/'events/national_policy_panel_events.txt').read_text()
                event=next(n for n in P.parse_nodes(P.lex(P.uncomment(raw)),0,'events')[0] if n.key=='country_event' and P.first(n.value,'id')=='national_policy_panel.2')
                self._effects(P.first(event.value,'immediate'),scope)
            finally:self.temp_frames,self.root,self.scope_stack,self.targets=old
            return
        return super()._native_effect(key, value, scope, line)

    def run_nodes(self, nodes, actor):
        old = self.root, self.scope_stack
        self.root, self.scope_stack = actor, [actor]
        try:
            self._effects(nodes, actor)
        finally:
            self.root, self.scope_stack = old


class LiveCampRuntime(Runtime):
    EXTERNAL_FIXTURES=Runtime.EXTERNAL_FIXTURES | {'apply_state_population_loss_without_recruitable_manpower_gain'}
    # Native row-shape/authority facts are fixtures; freshness and UI projections execute source.
    def __init__(self,states=()):
        super().__init__(states)
        for name in ('camp_origin_host_provenance_ready',):
            self.trigger_defs[name]=H.read_named('common/scripted_triggers/camp_administration_origin_triggers.txt',name)
        self.effect_defs['apply_exact_state_civilian_population_loss']=H.read_named('common/scripted_effects/chaosx_dynamic_effects.txt','apply_exact_state_civilian_population_loss')
        for group in ('chaos_meter_deaths','chaos_meter_deaths_reason'):
            definition=H.read_named('common/script_constants/chaos_meter_constants.txt',group)
            for node in definition.body:
                if isinstance(node.value,str) and P.NUMBER.fullmatch(node.value):self.constants['constant:'+group+'.'+node.key]=H.Decimal(node.value)

    def _value(self,token):
        if token=='state_population_k':return H.Decimal(str(self.current.population_k))
        if token=='chaos_state_civilian_deaths_total':return self.current.values.get(token,0)
        return super()._value(token)

    def _variable(self,token):
        if token in ('state_population_k','chaos_state_civilian_deaths_total'):return self._value(token)
        return super()._variable(token)

    def _condition(self,node,scope):
        if node.key=='has_variable' and any(node.value in f for f in self.temp_frames):return True
        if node.key in ('camp_admin_gui_host_records_uncertain','camp_admin_gui_site_record_visible'):
            return self._run_trigger(node.key,scope)
        if node.key=='camp_origin_host_rows_valid':
            self._set_temp('camp_origin_inspect_shortfall_k',0);return True
        if node.key=='camp_admin_known_site_ready_for_reform':return False
        if node.key=='camp_admin_site_authority_is_valid':return True
        if node.key=='state_uses_normal_civilian_systems':return node.value=='yes'
        return super()._condition(node,scope)

    def _call_effect(self,name,scope):
        if name=='apply_state_population_loss_without_recruitable_manpower_gain':
            scope.population_k-=self._variable('state_population_transaction_loss')/1000
            return
        return super()._call_effect(name,scope)

    def live_rows(self,actor):
        self.temp_frames[0]['camp_admin_live_location_sources']=[]
        self.temp_frames[0]['camp_admin_live_location_states']=[]
        self.test_trigger('camp_admin_gui_read_live_locations',actor)
        return list(self.temp_frames[0]['camp_admin_live_location_states'])

    def live_warning(self,actor):
        self.temp_frames[0]['camp_admin_live_uncertain_locations']=0
        self.test_trigger('camp_admin_gui_read_live_uncertainty',actor)
        return self.temp_frames[0]['camp_admin_live_uncertain_locations']


class UpdateTests(unittest.TestCase):
    def test_paused_state_publication_updates_both_open_viewers_without_reopening(self):
        actor, controller = H.country(), H.country('GER')
        site = H.state(7, actor, controller=controller, flags=['migration_displacement_active'], migration_state_flight_population=20)
        runtime = Runtime([site])
        runtime.run_effect('migration_panel_open_window', actor)
        runtime.run_effect('migration_panel_open_window', controller)
        before_date = runtime.globals['date']
        self.assertEqual(actor.values['migration_panel_fleeing'],20)
        self.assertEqual(controller.values['migration_panel_fleeing'],20)
        # Actual authoritative state field changes; the publisher executes production source.
        site.values['migration_state_flight_population']=80
        site.values['migration_state_trapped_population']=9
        runtime.run_effect('national_policy_panel_publish_state', site)
        for viewer in (actor,controller):
            self.assertEqual(viewer.values['migration_panel_fleeing'],80)
            self.assertEqual(viewer.values['migration_panel_selected_trapped'],9)
            self.assertEqual(viewer.arrays['migration_panel_states'],[site])
        self.assertEqual(runtime.globals['date'],before_date)
        self.assertEqual(runtime.queue,[])

    def test_nested_transaction_coalesces_until_final_synchronous_commit(self):
        actor=H.country()
        site=H.state(7,actor,flags=['migration_displacement_active'],migration_state_flight_population=2)
        runtime=Runtime([site]);runtime.run_effect('migration_panel_open_window',actor)
        runtime.refreshes.clear()
        runtime.run_effect('national_policy_panel_begin_update',actor)
        runtime.run_effect('national_policy_panel_begin_update',actor)
        site.values['migration_state_flight_population']=9
        for _ in range(3):runtime.run_effect('national_policy_panel_publish_state',site)
        self.assertEqual(actor.values['migration_panel_fleeing'],2)
        self.assertEqual(runtime.refreshes,[])
        runtime.run_effect('national_policy_panel_end_update',actor)
        self.assertEqual(runtime.refreshes,[])
        runtime.run_effect('national_policy_panel_end_update',actor)
        self.assertEqual(actor.values['migration_panel_fleeing'],9)
        self.assertEqual(runtime.refreshes,[('migration_panel_refresh',actor.id)])
        self.assertNotIn('national_policy_panel_publication_pending',actor.flags)
        self.assertNotIn('national_policy_panel_update_depth',actor.values)
        self.assertEqual(runtime.globals['date'],0)

    def test_closed_panel_publication_and_obsolete_delivery_are_idle(self):
        actor=H.country();runtime=Runtime()
        before=(dict(actor.values),set(actor.flags),dict(actor.arrays))
        runtime.run_effect('national_policy_panel_begin_update',actor)
        runtime.run_effect('national_policy_panel_refresh_open',actor)
        runtime.run_effect('national_policy_panel_end_update',actor)
        event=H.read_named('events/national_policy_panel_events.txt','country_event')
        runtime.run_nodes(P.first(event.body,'immediate'),actor)
        self.assertEqual((actor.values,actor.flags,actor.arrays),before)
        self.assertEqual(runtime.refreshes,[])
        self.assertEqual(runtime.queue,[])

    def test_capture_notifies_old_controller_and_new_controller_synchronously(self):
        owner,old,new=H.country(),H.country('GER'),H.country('ENG')
        site=H.state(7,owner,controller=old,flags=['migration_displacement_active'],migration_state_flight_population=8)
        runtime=Runtime([site])
        for viewer in (old,new):runtime.run_effect('migration_panel_open_window',viewer)
        site.controller=new
        runtime.run_effect('national_policy_panel_publish_state',site)
        # The documented control callback separately publishes the former controller.
        runtime.run_effect('national_policy_panel_refresh_open',old)
        self.assertEqual(old.arrays['migration_panel_states'],[])
        self.assertEqual(new.arrays['migration_panel_states'],[site])
        self.assertEqual(runtime.globals['date'],0)

    def test_camp_projection_reads_registered_records_without_progression(self):
        actor=H.country();actor.values.update(fixture_camp_eligible=True,camp_admin_economy_progress=5,camp_admin_economy_target=10)
        actor.flags.add('camp_repression_ledger_open')
        site=H.state(7,actor,flags=['camp_admin_initialized'],camp_admin_responsible_country=actor,camp_admin_capacity_k=2,camp_admin_detainees_k=1,camp_admin_support_ratio=1)
        actor.arrays['camp_active_site_states']=[site];runtime=Runtime([site])
        runtime.run_effect('national_policy_panel_refresh_open',actor)
        self.assertEqual(actor.arrays['camp_admin_gui_states'],[site])
        self.assertEqual(actor.values['camp_admin_gui_site_capacity_k'],2)
        site.values['camp_admin_capacity_k']=3
        runtime.run_effect('national_policy_panel_publish_state',site)
        self.assertEqual(actor.values['camp_admin_gui_site_capacity_k'],3)
        self.assertEqual(actor.values['camp_admin_economy_progress'],5)
        self.assertEqual(runtime.globals['date'],0)
        self.assertNotIn('camp_admin_monthly_country',[name for name,*_ in runtime.external_calls])
        actor.flags.remove('camp_repression_ledger_open')
        calls=list(runtime.refreshes);values=dict(actor.values)
        runtime.run_effect('national_policy_panel_publish_state',site)
        self.assertEqual(runtime.refreshes,calls);self.assertEqual(actor.values,values)

    def test_retirement_and_inherited_actor_identity_clear_only_ui(self):
        actor,child=H.country(),H.country('GER');runtime=Runtime()
        child.flags.update({'migration_panel_open','camp_repression_ledger_open'})
        child.values['national_policy_panel_owner']=actor
        child.values['national_policy_panel_update_depth']=2
        runtime.run_effect('national_policy_panel_reconcile_identity',child)
        self.assertNotIn('migration_panel_open',child.flags)
        self.assertNotIn('camp_repression_ledger_open',child.flags)
        self.assertNotIn('national_policy_panel_update_depth',child.values)
        self.assertEqual(runtime.queue,[])

    def test_publication_preserves_caller_quote_date_origin_and_capacity_scratch(self):
        actor=H.country();actor.values['fixture_camp_eligible']=True
        actor.flags.add('camp_repression_ledger_open')
        runtime=Runtime()
        inherited={'camp_admin_quote_support':83,'camp_admin_quote_pp':29,'camp_admin_reform_quote_pp':51,'camp_sale_ratio':H.Decimal('0.9'),'black_friday_price_payable':17,'chaosx_date_days':73,'camp_origin_rows_valid':1,'camp_admin_reconcile_live_k':400,'migration_reception_preparation_population':22}
        runtime.temp_frames[0].update(inherited)
        runtime.run_effect('national_policy_panel_refresh_open',actor)
        for name,value in inherited.items():self.assertEqual(runtime._variable(name),value,name)

    def test_live_meter_trigger_arithmetic_reads_changed_progress_without_publication(self):
        actor=H.country();runtime=Runtime()
        actor.flags.add('camp_admin_economy_slot_active')
        actor.values.update(camp_admin_economy_progress=5,camp_admin_economy_target=10)
        gui=P.read_definitions('common/scripted_guis/camp_repression_ledger_scripted_gui.txt')['scripted_gui']
        definition=P.first(gui.body,'camp_repression_ledger_scripted_gui')
        if definition is None:
            definition=next(node.value for node in gui.body if P.first(node.value,'window_name')=='camp_repression_ledger_window')
        trigger=P.first(P.first(definition,'triggers'),'camp_admin_economy_meter_visible')
        runtime.root, runtime.scope_stack=actor,[actor]
        self.assertTrue(runtime._conditions(trigger,actor))
        self.assertEqual(runtime._variable('camp_admin_live_economy_frame'),6)
        actor.values['camp_admin_economy_progress']=10
        self.assertTrue(runtime._conditions(trigger,actor))
        self.assertEqual(runtime._variable('camp_admin_live_economy_frame'),11)
        self.assertEqual(runtime.globals['date'],0)
        self.assertEqual(runtime.refreshes,[])

    def test_external_exact_population_loss_updates_independent_record_authority_live_list(self):
        owner,authority=H.country(),H.country('GER')
        authority.flags.add('camp_repression_ledger_open')
        authority.values['camp_admin_location_filter']=4
        site=H.state(7,owner,flags=['camp_admin_initialized','camp_origin_observation_initialized'],camp_admin_responsible_country=authority,camp_admin_detainees_k=2,camp_admin_support_ratio=1,camp_origin_observed_population_k=100,camp_origin_observed_state_deaths_people=0)
        authority.arrays['camp_active_site_states']=[site]
        authority.arrays['camp_admin_known_site_states']=[site]
        authority.arrays['camp_occ_states']=[site]
        authority.arrays['camp_admin_gui_states']=[]
        authority.values['camp_admin_gui_uncertain_locations']=0
        runtime=LiveCampRuntime([site])
        self.assertEqual(runtime.live_rows(authority),[])
        self.assertEqual(runtime.live_warning(authority),0)
        # Execute the real exact-loss boundary used by outside loss owners.
        runtime.temp_frames[0].update(state_civilian_population_loss_contract_supplied=1,state_civilian_population_loss_requested=1000,state_civilian_population_loss_minimum_remaining=0,state_civilian_population_loss_reason=0,state_civilian_population_loss_log_deaths=0,state_civilian_population_loss_target_country=owner,state_civilian_population_loss_has_target_country=0,state_civilian_population_loss_applied=0,state_civilian_population_loss_result=0)
        runtime.run_effect('apply_exact_state_civilian_population_loss',site)
        self.assertEqual(site.population_k,99)
        self.assertEqual(runtime.live_rows(authority),[site])
        self.assertEqual(runtime.live_warning(authority),1) # co-located registries deduplicate
        self.assertEqual(authority.arrays['camp_admin_gui_states'],[])
        self.assertEqual(authority.values['camp_admin_gui_uncertain_locations'],0)
        self.assertEqual(runtime.refreshes,[])
        self.assertEqual(runtime.globals['date'],0)
        # A fresh population value with a changed death observation also invalidates proof.
        site.population_k=100;site.values['chaos_state_civilian_deaths_total']=1000
        self.assertEqual(runtime.live_rows(authority),[site]);self.assertEqual(runtime.live_warning(authority),1)
        site.values['chaos_state_civilian_deaths_total']=0
        self.assertEqual(runtime.live_rows(authority),[]);self.assertEqual(runtime.live_warning(authority),0)

    def test_live_location_filters_order_selection_and_empty_state_share_current_rows(self):
        actor=H.country();actor.flags.add('camp_repression_ledger_open');actor.values['camp_admin_location_filter']=1
        first=H.state(7,actor,flags=['camp_admin_initialized'],camp_admin_responsible_country=actor,camp_admin_role=2,camp_admin_support_ratio=1)
        second=H.state(8,actor,flags=['camp_admin_initialized','camp_admin_site_suspended'],camp_admin_responsible_country=actor,camp_admin_role=1,camp_admin_support_ratio=1)
        actor.arrays.update(camp_active_site_states=[first],camp_admin_civilian_states=[second],camp_admin_known_site_states=[first,second],camp_admin_gui_states=[first])
        runtime=LiveCampRuntime([first,second])
        self.assertEqual(runtime.live_rows(actor),[first,second])
        actor.values['camp_admin_location_filter']=2;self.assertEqual(runtime.live_rows(actor),[first])
        actor.values['camp_admin_location_filter']=3;self.assertEqual(runtime.live_rows(actor),[second])
        actor.values['camp_admin_location_filter']=4;self.assertEqual(runtime.live_rows(actor),[second])
        definition=P.first(P.read_definitions('common/scripted_guis/camp_repression_ledger_scripted_gui.txt')['scripted_gui'].body,'camp_repression_ledger_scripted_gui')
        effects=P.first(definition,'effects');triggers=P.first(definition,'triggers')
        runtime.root=actor;runtime.scope_stack=[actor,second]
        runtime._effects(P.first(effects,'camp_admin_location_select_click'),second)
        self.assertIs(actor.values['camp_selected_state_id'],second)
        self.assertTrue(runtime._conditions(P.first(triggers,'camp_admin_location_selected_visible'),second))
        runtime.scope_stack=[actor]
        self.assertTrue(runtime._conditions(P.first(triggers,'camp_admin_selected_panel_visible'),actor))
        second.flags.remove('camp_admin_site_suspended')
        self.assertTrue(runtime._conditions(P.first(triggers,'camp_admin_location_empty_visible'),actor))
        self.assertFalse(runtime._conditions(P.first(triggers,'camp_admin_selected_panel_visible'),actor))
        self.assertEqual(runtime.globals['date'],0)

    def test_live_native_bindings_have_no_dirty_or_clock_dependency(self):
        for name in ('migration_management','famine_management','camp_repression_ledger'):
            source=(ROOT/f'common/scripted_guis/{name}_scripted_gui.txt').read_text()
            self.assertNotRegex(source,r'(?m)^\s*dirty\s*=')
        effects=(ROOT/'common/scripted_effects/national_policy_panel_effects.txt').read_text()
        self.assertIn('country_event = { id = national_policy_panel.2 }',effects)
        self.assertNotRegex(effects,r'\b(hours|days|months|random_hours|random_days)\s*=')
        self.assertNotIn('global.date',effects)
        self.assertNotIn('national_policy_panel_request_observer',effects)

if __name__=='__main__':unittest.main(verbosity=2)
