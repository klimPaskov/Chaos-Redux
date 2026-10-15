"""Source-runtime regression for immediate humanitarian panel publishers.

Usage: python .tools/test_humanitarian_panel_publishers.py
The production migration flight/trapped writers, action-tail publisher, panel
API, and panel projections execute at an unchanged global date. Owner-registry
setup and unrelated subsystem effects are fixtures. The transfer-tail scenario
supplies a committed or rejected finalize receipt; it does not execute the
physical transfer primitive. This is source-model evidence, not native HOI4 QA.
"""
from pathlib import Path
import sys
import unittest
import contextlib
import io

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".tools"))
with contextlib.redirect_stdout(io.StringIO()):
    import test_humanitarian_panels as H
import test_national_policy_panel_updates as Panel

P = Panel.P


class WriterRuntime(Panel.Runtime):
    EXTERNAL_FIXTURES = Panel.Runtime.EXTERNAL_FIXTURES | {
        "humanitarian_initialize_runtime",
        "migration_initialize_state",
        "migration_register_active_state",
        "migration_register_active_country",
        "migration_register_initial_incident",
        "migration_refresh_decision_phase_from_state",
        "migration_publish_reception_demand",
        "famine_consume_migration_reception_demand",
        "famine_initialize_state",
        "famine_initialize_runtime",
        "famine_register_state_in_runtime",
        "famine_register_active_country",
        "humanitarian_project_legacy_cost_quote",
        "migration_mark_reception_capacity_dirty_if_candidate",
    }

    def __init__(self, states):
        super().__init__(states)
        core = "common/scripted_effects/migration_core_effects.txt"
        for name in ("migration_apply_flight_request", "migration_register_trapped_population"):
            self.effect_defs[name] = H.read_named(core, name)
        self.effect_defs["migration_gui_publish_transfer_participants"] = H.read_named(
            "common/scripted_effects/migration_gui_action_effects.txt", "migration_gui_publish_transfer_participants"
        )
        famine = "common/scripted_effects/famine_core_effects.txt"
        for name in ("famine_apply_pressure_request", "famine_submit_surface_context", "famine_register_active_state"):
            self.effect_defs[name] = H.read_named(famine, name)
        trigger = "common/scripted_triggers/migration_core_triggers.txt"
        self.trigger_defs["migration_pressure_request_is_valid"] = H.read_named(trigger, "migration_pressure_request_is_valid")
        self.trigger_defs["humanitarian_state_is_valid"] = H.read_named(
            "common/scripted_triggers/humanitarian_validation_triggers.txt", "humanitarian_state_is_valid"
        )
        famine_trigger = "common/scripted_triggers/famine_core_triggers.txt"
        for name in ("famine_pressure_request_is_valid", "famine_surface_context_request_is_valid"):
            self.trigger_defs[name] = H.read_named(famine_trigger, name)

    def run_scoped_effect(self, name, scope, caller_temps=None):
        previous = self.root, self.scope_stack, self.temp_frames
        self.root, self.scope_stack, self.temp_frames = scope, [scope], [dict(caller_temps or {})]
        try:
            self._effects(self.effect_defs[name].body, scope)
            return dict(self.temp_frames[0])
        finally:
            self.root, self.scope_stack, self.temp_frames = previous

    def _call_effect(self, name, scope):
        if name == "famine_register_state_in_runtime":
            self.temp_frames[-1]["humanitarian_registry_result"] = 1
            return
        return super()._call_effect(name, scope)

    def _condition(self, node, scope):
        if node.key == "is_owned_and_controlled_by":
            target = scope.owner if node.value == "OWNER" else self._value(node.value)
            return scope.owner is target and scope.controller is target
        if node.key in ("OWNER", "CONTROLLER", "owner", "controller"):
            target = scope.owner if node.key.lower() == "owner" else scope.controller
            return target is not None and self._conditions(node.value, target)
        return super()._condition(node, scope)

    def _write_path(self, path, value, clear=False):
        container, field, global_scope = self._path_container(path)
        if not global_scope and (container.kind == "state" or (field.startswith(("migration_", "famine_")) and not field.startswith(("migration_panel_", "famine_panel_")))):
            return P.Event35Runtime._write_path(self, path, value, clear)
        if not field.startswith(("famine_panel_", "migration_panel_", "national_policy_panel_", "camp_admin_gui_")):
            raise AssertionError(f"unexpected non-state gameplay write {path} in {container.kind}; global={global_scope}")
        return super()._write_path(path, value, clear)

    def _effects(self, nodes, scope):
        chunk = []
        for node in nodes:
            if node.key in ("OWNER", "CONTROLLER", "owner", "controller"):
                if chunk:
                    super()._effects(chunk, scope)
                    chunk = []
                target = scope.owner if node.key.lower() == "owner" else scope.controller
                if target is not None:
                    self.scope_stack.append(target)
                    try:
                        self._effects(node.value, target)
                    finally:
                        self.scope_stack.pop()
            else:
                chunk.append(node)
        if chunk:
            super()._effects(chunk, scope)


class WriterPublicationTests(unittest.TestCase):
    def test_actual_flight_and_trapped_writers_update_open_owner_and_controller_at_same_date(self):
        owner, controller = H.country("FRA"), H.country("GER")
        state = H.state(11, owner, controller=controller, flags=["migration_displacement_active"],
                        state_population_k=100, migration_state_flight_population=5, migration_state_trapped_population=2)
        runtime = WriterRuntime([state])
        runtime.run_effect("migration_panel_open_window", owner)
        runtime.run_effect("migration_panel_open_window", controller)
        starting_date = runtime.globals["date"]

        result = runtime.run_scoped_effect("migration_apply_flight_request", state, {
            "migration_pressure_request_proven": 1,
            "migration_pressure_request_amount": 40,
            "migration_pressure_request_source": 1,
            "migration_pressure_request_actor_proven": 1,
        })
        self.assertEqual(result["migration_pressure_request_result"], 1)
        for viewer in (owner, controller):
            self.assertEqual(viewer.values["migration_panel_fleeing"], 45)
            self.assertEqual(viewer.arrays["migration_panel_states"], [state])

        runtime.run_scoped_effect("migration_register_trapped_population", state, {
            "migration_trapped_request_amount": 7,
        })
        for viewer in (owner, controller):
            self.assertEqual(viewer.values["migration_panel_trapped"], 9)
            self.assertEqual(viewer.values["migration_panel_selected_trapped"], 9)
            self.assertEqual(viewer.arrays["migration_panel_states"], [state])
        self.assertEqual(state.values["migration_state_flight_population"], 45)
        self.assertEqual(state.values["migration_state_trapped_population"], 9)
        self.assertEqual(runtime.globals["date"], starting_date)
        self.assertEqual(runtime.queue, [])

    def test_actual_writer_does_not_touch_closed_panel_projection(self):
        owner, controller = H.country("FRA"), H.country("GER")
        state = H.state(12, owner, controller=controller, flags=["migration_displacement_active"],
                        state_population_k=100, migration_state_flight_population=3)
        runtime = WriterRuntime([state])
        runtime.run_effect("migration_panel_open_window", owner)
        runtime.run_effect("migration_panel_open_window", controller)
        runtime.run_effect("migration_panel_close_window", owner)
        runtime.run_effect("migration_panel_close_window", controller)
        before = {
            viewer.id: (
                {k: v for k, v in viewer.values.items() if k.startswith(("migration_panel_", "national_policy_panel_"))},
                {k: v for k, v in viewer.arrays.items() if k.startswith(("migration_panel_", "national_policy_panel_"))},
                {k for k in viewer.flags if k.startswith(("migration_panel_", "national_policy_panel_"))},
            ) for viewer in (owner, controller)
        }
        refreshes = list(runtime.refreshes)
        runtime.run_scoped_effect("migration_apply_flight_request", state, {
            "migration_pressure_request_proven": 1,
            "migration_pressure_request_amount": 9,
            "migration_pressure_request_source": 1,
            "migration_pressure_request_actor_proven": 1,
        })
        after = {
            viewer.id: (
                {k: v for k, v in viewer.values.items() if k.startswith(("migration_panel_", "national_policy_panel_"))},
                {k: v for k, v in viewer.arrays.items() if k.startswith(("migration_panel_", "national_policy_panel_"))},
                {k for k in viewer.flags if k.startswith(("migration_panel_", "national_policy_panel_"))},
            ) for viewer in (owner, controller)
        }
        self.assertEqual(after, before)
        self.assertEqual(runtime.refreshes, refreshes)
        self.assertEqual(state.values["migration_state_flight_population"], 12)
        self.assertEqual(runtime.queue, [])

    def test_famine_pressure_and_surface_inputs_publish_without_reassessment(self):
        owner, controller = H.country("FRA"), H.country("GER")
        state = H.state(15, owner, controller=controller, state_population_k=100)
        runtime = WriterRuntime([state])
        runtime.run_effect("famine_panel_open_window", owner)
        runtime.run_effect("famine_panel_open_window", controller)
        start_date = runtime.globals["date"]
        for viewer in (owner, controller):
            self.assertEqual(viewer.arrays.get("famine_panel_states", []), [])

        pressure = runtime.run_scoped_effect("famine_apply_pressure_request", state, {
            "famine_pressure_request_proven": 1,
            "famine_pressure_request_amount": 5,
            "famine_pressure_request_source": 13,
            "famine_pressure_request_actor_proven": 1,
        })
        self.assertEqual(pressure["famine_pressure_request_result"], 1)
        for viewer in (owner, controller):
            self.assertEqual(viewer.arrays["famine_panel_states"], [state])
            self.assertEqual(viewer.values["famine_panel_food_stage"], 0)
        self.assertGreater(state.values["famine_food_pressure"], 0)
        self.assertNotIn("famine_food_security_score", state.values)

        # CXT setup uses this accepted input adapter; the publisher makes the
        # new active-state facts visible without running the food evaluator.
        context = runtime.run_scoped_effect("famine_submit_surface_context", state, {
            "famine_surface_context_proven": 1,
            "famine_surface_context_actor_proven": 1,
        })
        self.assertEqual(context["famine_surface_context_result"], 1)
        self.assertIn("famine_surface_context_active", state.flags)
        self.assertNotIn("famine_food_security_score", state.values)
        self.assertEqual(runtime.globals["date"], start_date)

    def test_settled_transfer_tail_refreshes_both_endpoints_and_rollback_is_idle(self):
        origin_owner, origin_controller = H.country("FRA"), H.country("GER")
        destination_owner, destination_controller = H.country("ENG"), H.country("SOV")
        origin = H.state(13, origin_owner, controller=origin_controller,
                         flags=["migration_displacement_active", "migration_population_trapped"],
                         state_population_k=100, migration_state_flight_population=20,
                         migration_state_trapped_population=8)
        destination = H.state(14, destination_owner, controller=destination_controller,
                              flags=["migration_displacement_active"], state_population_k=100,
                              migration_state_flight_population=0, migration_state_trapped_population=0,
                              migration_state_reception_load=0)
        runtime = WriterRuntime([origin, destination])
        viewers = (origin_owner, origin_controller, destination_owner, destination_controller)
        for viewer in viewers:
            runtime.run_effect("migration_panel_open_window", viewer)
        start_date = runtime.globals["date"]
        runtime.targets["civilian_transfer_route_origin"] = origin
        runtime.targets["civilian_transfer_route_destination"] = destination

        # The source model supplies a committed finalize receipt; the production
        # action-tail helper and both production panel publishers execute.
        origin.values["migration_state_trapped_population"] = 0
        origin.flags.discard("migration_population_trapped")
        destination.values["migration_state_reception_load"] = 33
        runtime.run_scoped_effect("migration_gui_publish_transfer_participants", origin_owner, {
            "civilian_transfer_finalize_result": runtime.constants[
                "constant:migration_core_reconciliation.transfer_finalize_valid"
            ],
            "civilian_transfer_actual_origin_debit": 40,
        })
        for viewer in (origin_owner, origin_controller):
            self.assertEqual(viewer.values["migration_panel_trapped"], 0)
        for viewer in (destination_owner, destination_controller):
            self.assertEqual(viewer.values["migration_panel_sheltered"], 33)
        self.assertEqual(runtime.globals["date"], start_date)

        # A failed or rolled-back attempt has an invalid terminal receipt and
        # leaves both currently published endpoint views untouched.
        before = {
            viewer.id: (
                dict(viewer.values), dict(viewer.arrays), set(viewer.flags)
            ) for viewer in viewers
        }
        refreshes = list(runtime.refreshes)
        runtime.run_scoped_effect("migration_gui_publish_transfer_participants", origin_owner, {
            "civilian_transfer_finalize_result": runtime.constants[
                "constant:migration_core_reconciliation.transfer_finalize_invalid"
            ],
            "civilian_transfer_actual_origin_debit": 0,
        })
        after = {
            viewer.id: (
                dict(viewer.values), dict(viewer.arrays), set(viewer.flags)
            ) for viewer in viewers
        }
        self.assertEqual(after, before)
        self.assertEqual(runtime.refreshes, refreshes)
        self.assertEqual(runtime.globals["date"], start_date)


if __name__ == "__main__":
    unittest.main(verbosity=2)
