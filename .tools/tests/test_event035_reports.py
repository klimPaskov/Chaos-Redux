"""Execute Event 035 report guards from production source.

Native event delivery is recorded, not emulated. These tests cover scheduling
and conservative helper frames, not native popup rendering or delayed delivery.
"""
import unittest
from test_event035_center_projects import (
    Event35Runtime, Scope, country, read_definitions, first,
)


class ReportRuntime(Event35Runtime):
    NATIVE_PRIMITIVES = Event35Runtime.NATIVE_PRIMITIVES | {"clamp_temp_variable"}

    def _effects(self, nodes, scope):
        normalized = []
        for node in nodes:
            if node.key in ("set_temp_variable", "set_variable") and isinstance(node.value, list) and first(node.value, "var") is not None:
                name = first(node.value, "var")
                rhs = first(node.value, "value")
                field = type(node)(name, "=", rhs, node.line)
                node = type(node)(node.key, node.op, [field], node.line)
            normalized.append(node)
        return super()._effects(normalized, scope)

    def _native_effect(self, key, value, scope, line):
        if key == "clamp_temp_variable":
            args = {n.key: n.value for n in value}
            self._set_temp(args["var"], max(self._value(args["min"]), min(self._variable(args["var"]), self._value(args["max"]))))
            return
        return super()._native_effect(key, value, scope, line)

    def _condition(self, node, scope):
        if node.key == "has_event_target":
            return node.value in self.targets
        if node.key == "has_disabled_current_evolution":
            # Shared Settings evaluation is outside this source closure.
            # Fixture declares that Evolution III is enabled.
            return False
        return super()._condition(node, scope)

    def _path_exists(self, path):
        if any(path in frame for frame in self.temp_frames):
            return True
        return super()._path_exists(path)

    def _array_value(self, container, path):
        if container is not None:
            return super()._array_value(container, path)
        base, _, index = path.partition("^")
        row = self.global_arrays.get(base, [])
        if index == "num":
            return len(row)
        if index:
            offset = int(self._value(index))
            return row[offset] if 0 <= offset < len(row) else 0
        return row

    def _path_container(self, path):
        if "@var:" in path:
            base, target = path.split("@var:", 1)
            path = base + str(int(self._variable(target)))
        return super()._path_container(path)

    def event_body(self, event_id, country_scope, section="immediate"):
        # Native event headers repeat; use the source parser's nodes, not its
        # dictionary's last country_event definition.
        from test_event035_center_projects import ROOT, lex, uncomment, parse_nodes
        path = ROOT / "events/035_great_depression.txt"
        nodes, _ = parse_nodes(lex(uncomment(path.read_text(encoding="utf-8"))), 0, str(path))
        event = next(n.value for n in nodes if isinstance(n.value, list) and first(n.value, "id") == event_id)
        self.root = country_scope
        self.scope_stack = [country_scope]
        trigger = first(event, "trigger", [])
        if not self._conditions(trigger, country_scope):
            return False
        self._effects(first(event, section, []), country_scope)
        return True


def episode(r, actor, episode_id, caller="independent_event_35", source=None):
    actor.values.update({
        "great_depression_active_episode_id": episode_id,
        "great_depression_call_caller_type": r.constants["constant:great_depression_caller." + caller],
        "great_depression_call_started": 1,
        "great_depression_call_report_policy": 1,
        "great_depression_call_news_policy": 1,
    })
    if source:
        actor.values["great_depression_call_source_country_scope"] = source
    r.run_effect("great_depression_initialize_report_chain", actor)


class ReportSchedulingTests(unittest.TestCase):
    def test_worldwide_28_conversions_queue_no_routine_world_news(self):
        r = ReportRuntime()
        r.global_flags.add("great_depression_worldwide_episode_active")
        r.globals["great_depression_global_episode_id"] = 100
        for i in range(28):
            actor = country("W" + str(i))
            episode(r, actor, i + 1, "worldwide_depression_conversion")
            r.run_effect("great_depression_queue_external_surfaces", actor)
            r.event_body("chaosx.nr35.2", actor)
            self.assertEqual(actor.values["great_depression_report_chain_episode"], 100)
            self.assertIn("great_depression_spread_news_sent", actor.flags)
        self.assertEqual(len(r.events), 28)
        self.assertTrue(all(e[1] == "chaosx.nr35.2" for e in r.events))
        r.global_flags.clear()
        descendant = country("AFTER")
        episode(r, descendant, 200, "financial_contagion_conversion", actor)
        r.run_effect("great_depression_queue_external_surfaces", descendant)
        r.root = actor
        r.scope_stack = [actor, descendant]
        r._call_effect("great_depression_mark_first_contagion_spread", descendant)
        r.event_body("chaosx.nr35.2", descendant)
        self.assertEqual(sum(e[1] == "chaosx.nr35.15" for e in r.events), 0)

    def test_one_secondary_news_across_all_financial_descendants(self):
        r = ReportRuntime()
        origin = country("AAA")
        episode(r, origin, 1)
        r.run_effect("great_depression_queue_external_surfaces", origin)
        r.event_body("chaosx.nr35.2", origin)
        source = origin
        for i in range(28):
            actor = country("C" + str(i))
            episode(r, actor, i + 2, "financial_contagion_conversion", source)
            r.run_effect("great_depression_queue_external_surfaces", actor)
            r.root = source
            r.scope_stack = [source, actor]
            r._call_effect("great_depression_mark_first_contagion_spread", actor)
            r.event_body("chaosx.nr35.2", actor)
            self.assertEqual(actor.values["great_depression_report_chain_episode"], 1)
            if i % 2:
                source = actor
        self.assertEqual(sum(e[1] == "chaosx.news.40" for e in r.events), 1)
        self.assertEqual(sum(e[1] == "chaosx.nr35.15" for e in r.events), 1)

    def test_deepening_replay_no_extra_report_or_news_and_new_episode_can_report(self):
        r = ReportRuntime()
        a = country("AAA")
        episode(r, a, 1)
        r.run_effect("great_depression_queue_external_surfaces", a)
        self.assertTrue(r.event_body("chaosx.nr35.2", a))
        a.values["great_depression_call_started"] = 0
        for _ in range(30):
            r.run_effect("great_depression_queue_external_surfaces", a)
            self.assertFalse(r.event_body("chaosx.nr35.2", a))
        self.assertEqual(len(r.events), 2)
        episode(r, a, 2)
        r.run_effect("great_depression_queue_external_surfaces", a)
        self.assertTrue(r.event_body("chaosx.nr35.2", a))
        self.assertEqual(len(r.events), 4)

    def test_recipient_aggregates_independent_origins_and_ignores_descendants(self):
        r = ReportRuntime()
        receiver = country("REC")
        r.targets["great_depression_exposure_target"] = receiver
        for i in range(3):
            source = country("S" + str(i))
            episode(r, source, i + 1)
            r.run_effect("great_depression_queue_exposed_partner_report", source)
        self.assertEqual(len(r.events), 1)
        self.assertTrue(r.event_body("chaosx.nr35.14", receiver))
        self.assertEqual(receiver.values["great_depression_exposure_report_other_count"], 2)
        self.assertEqual(receiver.arrays["great_depression_exposure_report_origins"], [])
        descendant = country("DES")
        episode(r, descendant, 4, "financial_contagion_conversion", source)
        r.run_effect("great_depression_queue_exposed_partner_report", descendant)
        self.assertEqual(len(r.events), 1)
        self.assertFalse(r.event_body("chaosx.nr35.14", receiver))
        # A later independent episode is a separate chain and remains visible.
        episode(r, source, 5)
        r.run_effect("great_depression_queue_exposed_partner_report", source)
        self.assertEqual(len(r.events), 2)

    def test_inherited_start_keeps_its_report_and_news(self):
        r = ReportRuntime()
        a = country("AAA")
        episode(r, a, 1, "industrial_boom_collapse")
        r.run_effect("great_depression_queue_external_surfaces", a)
        r.event_body("chaosx.nr35.2", a)
        self.assertEqual([e[1] for e in r.events], ["chaosx.nr35.2", "chaosx.news.40"])

    def test_surviving_clearing_bloc_does_not_reannounce_next_world_episode(self):
        r = ReportRuntime()
        a = country("AAA")
        r.global_flags.add("great_depression_worldwide_episode_active")
        r.globals["great_depression_global_episode_id"] = 1
        r.temp_frames[0].update({
            "great_depression_global_news_kind": r.constants["constant:great_depression_global_news.clearing_bloc"],
            "great_depression_bloc_member_count": 3,
        })
        r.global_arrays["great_depression_clearing_bloc_members"] = [a, country("BBB"), country("CCC")]
        r.run_effect("great_depression_queue_global_news", a)
        self.assertEqual(sum(e[1] == "chaosx.nr35.20" for e in r.events), 1)
        r.globals["great_depression_global_episode_id"] = 2
        r.run_effect("great_depression_queue_global_news", a)
        self.assertEqual(sum(e[1] == "chaosx.nr35.20" for e in r.events), 1)
        r.global_arrays["great_depression_clearing_bloc_members"] = [a]
        r.run_effect("great_depression_reset_clearing_bloc_announcement_if_small", a)
        self.assertNotIn("great_depression_clearing_bloc_formation_announced", r.global_flags)
        r.global_arrays["great_depression_clearing_bloc_members"] = [a, country("DDD"), country("EEE")]
        r.run_effect("great_depression_queue_global_news", a)
        self.assertEqual(sum(e[1] == "chaosx.nr35.20" for e in r.events), 2)


class SupplierQuoteTests(unittest.TestCase):
    def setup_supplier(self):
        r = ReportRuntime()
        a = country("SUP")
        a.flags.add("industrial_boom_active")
        a.resources["civilian_factories_available"] = 12
        a.values.update({"num_of_civilian_factories": 12, "num_of_military_factories": 6, "num_of_naval_factories": 2})
        self.assertFalse(r.test_trigger("great_depression_costs_are_ready", a))
        r.run_effect("great_depression_event34_supplier_adapter", a)
        self.assertTrue(r.test_trigger("great_depression_costs_are_ready", a))
        self.assertNotIn(a, r.global_arrays.get("great_depression_global_supplier_risk_countries", []))
        for resource, quote in (("political_power", "political_power"), ("fuel", "fuel"), ("convoy_1", "convoys"), ("civilian_factories_available", "civilian")):
            a.resources[resource] = a.values["great_depression_cost_" + quote]
        return r, a

    def test_contractless_supplier_gets_quote_and_exact_reserves_are_affordable(self):
        r, a = self.setup_supplier()
        self.assertTrue(r.test_trigger("great_depression_can_pay_conference_share", a))
        for resource in ("political_power", "fuel", "convoy_1", "civilian_factories_available"):
            a.resources[resource] -= 1
            self.assertFalse(r.test_trigger("great_depression_can_pay_conference_share", a), resource)
            a.resources[resource] += 2
            self.assertTrue(r.test_trigger("great_depression_can_pay_conference_share", a), resource)
            a.resources[resource] -= 1

    def test_join_executes_real_payment_and_adds_one_aligned_seat(self):
        r, a = self.setup_supplier()
        self.assertTrue(r.test_trigger("great_depression_can_pay_conference_share", a))
        civilian_quote = a.values["great_depression_cost_civilian"]
        r.run_effect("great_depression_join_global_recovery_conference", a)
        self.assertEqual(a.resources["political_power"], 0)
        self.assertEqual(a.resources["fuel"], 0)
        self.assertEqual(a.resources["convoy_1"], 0)
        self.assertEqual(a.values["great_depression_committed_civilian"], civilian_quote)
        self.assertIn("great_depression_action_lock", a.flags)
        self.assertFalse(r.test_trigger("great_depression_can_pay_conference_share", a))
        self.assertEqual(r.global_arrays["great_depression_conference_participants"], [a])
        self.assertEqual(r.global_arrays["great_depression_conference_participant_weights"], [32])
        self.assertEqual(len(r.resource_writes), 3)
        self.assertEqual(r.external_calls, [])

    def test_participant_industrial_weight_stays_bounded(self):
        r, a = self.setup_supplier()
        a.values["num_of_civilian_factories"] = 200
        r.run_effect("great_depression_add_conference_participant", a)
        self.assertEqual(r.global_arrays["great_depression_conference_participant_weights"], [100])


class LateBoomSupplierEntryTests(unittest.TestCase):
    def activation_slice(self):
        # Event 34 opens a boom through industrial_boom_open on the selected
        # country (chaosx.nr34.1). The supplier adapter guard sits near the
        # end of that body, after the flag, so take the two nodes by content.
        body = read_definitions("common/scripted_effects/034_industrial_boom_effects.txt")["industrial_boom_open"].body
        active_index = next(i for i, n in enumerate(body) if n.key == "set_country_flag" and n.value == "industrial_boom_active")
        guard_index = next(
            i for i, n in enumerate(body)
            if n.key == "if" and first(n.value, "limit") is not None
            and any(c.key == "great_depression_event34_supplier_adapter" for c in n.value)
        )
        guard = body[guard_index]
        self.assertEqual(first(first(guard.value, "limit"), "has_global_flag"), "great_depression_worldwide_episode_active")
        return [body[active_index], guard]

    def run_activation(self, runtime, supplier, host):
        runtime.root = host
        runtime.scope_stack = [supplier]
        runtime._effects(self.activation_slice(), supplier)

    def supplier(self):
        runtime, supplier, host = ReportRuntime(), country("SUP"), country("HOST")
        supplier.resources["civilian_factories_available"] = 12
        supplier.values.update({"num_of_civilian_factories": 12, "num_of_military_factories": 6, "num_of_naval_factories": 2})
        return runtime, supplier, host

    def test_late_boom_initializes_real_quote_on_selected_country_under_foreign_root(self):
        runtime, supplier, host = self.supplier()
        runtime.global_flags.add("great_depression_worldwide_episode_active")
        self.assertFalse(runtime.test_trigger("great_depression_costs_are_ready", supplier))
        self.run_activation(runtime, supplier, host)
        self.assertTrue(runtime.test_trigger("great_depression_costs_are_ready", supplier))
        self.assertFalse(runtime.test_trigger("great_depression_costs_are_ready", host))
        self.assertIn("great_depression_event34_supplier_pressure", supplier.flags)
        self.assertEqual(runtime.resource_writes, [])
        self.assertNotIn(supplier, runtime.global_arrays.get("great_depression_global_supplier_risk_countries", []))

    def test_ordinary_boom_does_not_open_worldwide_supplier_quote(self):
        runtime, supplier, host = self.supplier()
        self.run_activation(runtime, supplier, host)
        self.assertIn("industrial_boom_active", supplier.flags)
        self.assertFalse(runtime.test_trigger("great_depression_costs_are_ready", supplier))
        self.assertNotIn("great_depression_event34_supplier_pressure", supplier.flags)

    def test_actual_adapter_risk_replay_adds_one_supplier_and_one_risk_unit(self):
        runtime, supplier, host = self.supplier()
        runtime.global_flags.add("great_depression_worldwide_episode_active")
        supplier.flags.add("industrial_boom_supplier_contract_at_risk")
        self.run_activation(runtime, supplier, host)
        self.run_activation(runtime, supplier, host)
        self.assertEqual(runtime.global_arrays["great_depression_global_supplier_risk_countries"], [supplier])
        self.assertEqual(runtime.globals["great_depression_global_supplier_risk"], 1)
        self.assertEqual(runtime.resource_writes, [])


class CxtRegistrationTests(unittest.TestCase):
    def test_daily_discovery_marks_pending_without_applying_then_replay_is_inert(self):
        from test_event035_center_projects import ROOT, lex, uncomment, parse_nodes
        r = ReportRuntime()
        r.effect_defs.update(read_definitions("common/scripted_effects/035_great_depression_cxt_effects.txt"))
        registry = read_definitions("common/scripted_effects/chaosx_test_country_effects.txt")
        r.effect_defs["chaosx_test_country_register_extension_effect"] = registry["chaosx_test_country_register_extension_effect"]
        path = ROOT / "common/on_actions/035_great_depression_cxt_on_actions.txt"
        nodes, _ = parse_nodes(lex(uncomment(path.read_text(encoding="utf-8"))), 0, str(path))
        daily = first(first(first(nodes, "on_actions"), "on_daily_CXT"), "effect")
        actor = country("CXT")
        actor.flags.add("chaosx_test_country_initialized")
        r.root = actor
        r.scope_stack = [actor]
        r._effects(daily, actor)
        self.assertIn("chaosx_test_country_registered_sync_pending", actor.flags)
        self.assertNotIn("great_depression_cxt_fixture_ready", actor.flags)
        self.assertEqual(r.temp_frames[0]["chaosx_test_country_extension_registration_added"], 1)
        self.assertEqual(len(r.global_arrays["chaosx_test_country_registered_extension_effects"]), 1)
        actor.flags.discard("chaosx_test_country_registered_sync_pending")
        r._effects(daily, actor)
        self.assertNotIn("chaosx_test_country_registered_sync_pending", actor.flags)
        self.assertEqual(len(r.global_arrays["chaosx_test_country_registered_extension_effects"]), 1)
        self.assertEqual(r.events, [])
        self.assertEqual(r.resource_writes, [])
        self.assertEqual(r.external_calls, [])
        # The player-triggered application owns the readiness outcome.
        r.run_effect("chaosx_cxt_extension_event035_great_depression_apply", actor)
        self.assertIn("great_depression_cxt_fixture_ready", actor.flags)


class TooltipLifetimeTests(unittest.TestCase):
    def test_first_quote_populates_owner_cache_and_state_tooltip_reads_root(self):
        from test_event035_center_projects import state
        r = ReportRuntime()
        actor = country("ACT")
        sender = country("HOST")
        actor.resources["civilian_factories_available"] = 12
        r.run_effect("great_depression_refresh_costs", actor, root=sender)
        fields = {k: v for k, v in actor.values.items() if k.startswith("great_depression_tt_")}
        self.assertEqual(len(fields), 17)
        self.assertTrue(all(isinstance(value, (int, float)) for value in fields.values()))
        self.assertEqual(fields["great_depression_tt_strong_relief"], 5)
        self.assertEqual(fields["great_depression_tt_whiplash_days"], 42)
        self.assertEqual(fields["great_depression_tt_bank_audit_days"], 21)
        self.assertEqual(fields["great_depression_tt_bank_recapitalization_days"], 42)
        self.assertEqual(fields["great_depression_tt_bank_holiday_output"], 0.03)
        self.assertFalse(any(k.startswith("great_depression_tt_") for k in sender.values))
        self.assertEqual(r.temp_frames, [{}])
        site = state(1, actor)
        r.root = actor
        r.scope_stack = [actor, site]
        self.assertEqual(r._value("ROOT.great_depression_tt_strong_relief"), 5)
        self.assertNotIn("great_depression_tt_strong_relief", site.values)


if __name__ == "__main__":
    unittest.main(verbosity=2)
