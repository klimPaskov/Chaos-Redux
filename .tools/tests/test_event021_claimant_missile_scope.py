"""Actual-source Event021 claimant missile transactions under a foreign ROOT.

Country/state normal storage, globals, regular targets and unscoped temporaries
are separate. Returning helpers discard newly created temporary names. Native
state assignment, stockpile mutation, missions, modifiers and ideas are explicit
model boundaries. No engine arithmetic, callback timing or conservation proof.
Evolution notifications execute their production stamp, gate, host and cleanup
logic. Native .192 dispatch is recorded with its real recipient and hours,
without delivering the event or executing its pressure measurement/MTTH body.
"""
from copy import deepcopy
from dataclasses import dataclass, field
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path
import re
import unittest

REPO = Path(__file__).resolve().parents[2]
OPS_PATH = "common/scripted_effects/032_missiles_operations_effects.txt"


def parse(text):
    tokens = re.findall(r'#[^\n]*|"(?:\\.|[^"\\])*"|[{}=<>]|[^\s{}=<>]+', text)
    tokens = [token for token in tokens if not token.startswith("#")]
    cursor = 0

    def block():
        nonlocal cursor
        result = []
        while cursor < len(tokens) and tokens[cursor] != "}":
            key = tokens[cursor]
            cursor += 1
            if cursor == len(tokens) or tokens[cursor] not in ("=", "<", ">"):
                result.append((key, None))
                continue
            operator = tokens[cursor]
            cursor += 1
            body = tokens[cursor]
            cursor += 1
            if body == "{":
                body = block()
                assert tokens[cursor] == "}"
                cursor += 1
            assert operator == "=", ("unsupported shorthand comparison", key)
            result.append((key, body))
        return result

    # Retain shorthand comparisons as distinct keys instead of silently
    # interpreting a native greater-than test as an equality.
    for i, token in enumerate(tokens):
        if token in ("<", ">"):
            tokens[i - 1] += token
            tokens[i] = "="
    return block()


def source(path):
    return dict(parse((REPO / path).read_text(encoding="utf-8-sig")))


def value(body, name, default=None):
    return next((v for k, v in body if k == name), default)


CORE = source("common/scripted_effects/032_missiles_effects.txt")
OPS = source(OPS_PATH)
EVOLUTION = source("common/scripted_effects/032_missiles_evolution_effects.txt")
SURVEY = source("common/scripted_effects/032_missiles_survey_effects.txt")
RECOVERY = source("common/scripted_effects/032_missiles_recovery_effects.txt")
EFFECTS = {**CORE, **OPS,
           **SURVEY, **RECOVERY,
           **{name: EVOLUTION[name] for name in
              ("missiles_notify_program_numbers_changed", "missiles_notify_evolution_change",
               "missiles_cancel_all_evolution_clocks")},
           **source("common/scripted_effects/032_missiles_achievement_effects.txt"),
           **source("common/scripted_effects/032_missiles_payload_receipt_effects.txt"),
           **source("common/scripted_effects/cbrn_payload_reservation_effects.txt")}
TRIGGERS = {**source("common/scripted_triggers/032_missiles_triggers.txt"),
            **source("common/scripted_triggers/032_missiles_survey_triggers.txt"),
            **source("common/scripted_triggers/032_missiles_operations_triggers.txt"),
            **source("common/scripted_triggers/032_missiles_preparation_cost_triggers.txt")}
CONSTANTS = {**source("common/script_constants/032_missiles_constants.txt"),
             **source("common/script_constants/032_missiles_survey_constants.txt"),
             **source("common/script_constants/032_missiles_recovery_constants.txt"),
             **source("common/script_constants/cbrn_payload_reservation_constants.txt"),
             **source("common/script_constants/cbrn_system_constants.txt")}
OBSERVATION_EVENTS = [body for key, body in parse(
    (REPO / "events/032_missiles_evolution_events.txt").read_text(encoding="utf-8-sig"))
    if key == "country_event" and value(body, "id") == "chaosx.nr32.192"]
assert len(OBSERVATION_EVENTS) == 1, "Missing or duplicate native observation receiver"
assert value(OBSERVATION_EVENTS[0], "is_triggered_only") == "yes"
assert value(OBSERVATION_EVENTS[0], "immediate") == [("missiles_run_evolution_observation", "yes")]


@dataclass(eq=False)
class Object:
    name: str
    kind: str
    id: int
    variables: dict = field(default_factory=dict)
    arrays: dict = field(default_factory=dict)
    flags: set = field(default_factory=set)
    owner: object = None
    controller: object = None
    missions: set = field(default_factory=set)
    nukes: Decimal = Decimal(0)
    dynamic_modifiers: set = field(default_factory=set)


class Model:
    def __init__(self, government_program=True, operation=False):
        self.government = Object("government", "country", 10)
        self.claimant = Object("claimant", "country", 20)
        self.child = Object("child", "country", 30)
        self.root = self.government
        self.global_state = Object("global", "global", 0, {"date": Decimal("1936.10001"),
                                                          "missiles_civil_war_split_sequence": 80})
        self.temp = {}
        self.temp_arrays = {}
        self.targets = {}
        self.executed = set()
        self.boundaries = []
        self.evolution_dispatches = []  # Enqueue only. No synthetic measurement.
        self.region_queries = []
        self.sites = []
        self.setup(self.claimant, reserve=48, receipt=71, capacities=(12, 24), operation=operation)
        if government_program:
            self.setup(self.government, reserve=93, receipt=901, capacities=(30,), operation=True)

    def setup(self, country, reserve, receipt, capacities, operation):
        country.flags.add("missiles_program_initialized")
        # Explicit initialized-world/registry facts matching these seeded
        # programs. Notification eligibility is evaluated from real source.
        self.global_state.flags.add("missiles_program_ever_initialized")
        self.global_state.arrays.setdefault("missiles_program_registry", []).append(country)
        country.variables.update(missiles_operational_reserve=reserve,
                                 missiles_reserved_reserve=6 if operation else 0,
                                 missiles_program_stage=3, missiles_launch_readiness=80,
                                 missiles_command_control=90, missiles_guidance_training=13,
                                 missiles_reserve_cap=200, missiles_retaliation_posture=2,
                                 missiles_civil_war_split_receipt_id=receipt,
                                 missiles_active_operation_id=receipt if operation else 0)
        own_sites = []
        for i, capacity in enumerate(capacities):
            site = Object(f"{country.name}_{i}", "state", len(self.sites) + 1,
                          {"missiles_site_capacity": capacity, "missiles_site_reserve": 0,
                           "missiles_site_strategic_region": i + 1,
                           "missiles_site_owner_id": country.id,
                           "missiles_site_controller_id": country.id,
                           "missiles_site_current_controller": country,
                           "missiles_site_operation_id": receipt if operation and i == 0 else 0,
                           "missiles_site_operation_allocation": 6 if operation and i == 0 else 0},
                          flags={"missiles_site_active"}, owner=country, controller=country)
            self.sites.append(site)
            # Supplied native map membership, distinct from the normal cache.
            # The highest ID also exercises the unchanged inclusive probe end.
            site.region = int(self.number("constant:missiles_map.maximum_strategic_region", [country])) if i else 17
            own_sites.append(site)
        country.arrays["missiles_launch_site_states"] = own_sites
        country.arrays["missiles_operation_sites"] = own_sites[:1] if operation else []
        if operation:
            country.flags.update({"missiles_operation_active", "missiles_operation_reserve_receipt_active",
                                  "missiles_operation_payload_escrow_active", "missiles_operation_ready"})
            country.variables.update(missiles_operation_state=2, missiles_operation_missile_cost=6,
                                     missiles_operation_payload_escrow=1,
                                     missiles_operation_payload_escrow_type=self.number("constant:missiles_payload.nuclear", [country]))
            country.missions.update({"missiles_precision_strike_preparation_mission",
                                     "missiles_strategic_barrage_preparation_mission"})

    def scope(self, token, stack):
        if token == "ROOT":
            return self.root
        if token == "THIS":
            return stack[-1]
        if token == "PREV":
            return stack[-2]
        if token == "global":
            return self.global_state
        if token.lower() == "controller":
            assert stack[-1].kind == "state"
            return stack[-1].controller
        if token.startswith("event_target:") and "." not in token:
            return self.targets[token.split(":", 1)[1]]
        if token.startswith("var:"):
            mapping, name = self.storage(token[4:], stack)
            target = mapping.get(name)
            assert isinstance(target, Object), ("unproven normal scope pointer", token)
            return target
        return None

    def storage(self, token, stack, arrays=False):
        obj = stack[-1]
        if "." in token:
            prefix, token = token.split(".", 1)
            obj = self.scope(prefix, stack)
            assert obj is not None, prefix
        return (obj.arrays if arrays else obj.variables), token

    def number(self, token, stack):
        if token.startswith("constant:"):
            group, key = token[9:].split(".", 1)
            return Decimal(value(CONSTANTS[group], key))
        selected = self.scope(token, stack)
        if selected is not None:
            return selected
        if token.endswith("^num"):
            mapping, key = self.storage(token[:-4], stack, arrays=True)
            return Decimal(len(mapping.get(key, [])))
        if "." in token:
            prefix, name = token.split(".", 1)
            obj = self.scope(prefix, stack)
            assert obj is not None, prefix
            return Decimal(obj.id) if name == "id" else obj.variables.get(name, Decimal(0))
        if token in self.temp:
            return self.temp[token]
        if token == "id":
            return Decimal(stack[-1].id)  # Explicit native object identity.
        if token == "num_of_nukes":
            return stack[-1].nukes
        try:
            return Decimal(token)
        except InvalidOperation:
            return stack[-1].variables.get(token, Decimal(0))

    def conditions(self, nodes, stack):
        return all(self.term(key, body, stack) for key, body in nodes)

    def term(self, key, body, stack):
        obj = stack[-1]
        selected = self.scope(key, stack)
        if selected is not None:
            return self.conditions(body, [*stack, selected])
        if key in ("AND", "hidden_trigger", "limit"):
            return self.conditions(body, stack)
        if key == "NOT":
            return not any(self.term(k, v, stack) for k, v in body)
        if key == "OR":
            return any(self.term(k, v, stack) for k, v in body)
        if key in ("has_country_flag", "has_state_flag"):
            assert obj.kind == ("country" if key == "has_country_flag" else "state")
            return body in obj.flags
        if key == "has_global_flag":
            return body in self.global_state.flags
        if key == "has_variable":
            mapping, name = self.storage(body, stack)
            return name in mapping
        if key == "has_event_target":
            return body in self.targets
        if key == "check_variable":
            name, token = value(body, "var"), value(body, "value")
            if name is None:
                name, token = body[0]
            a, b = self.number(name, stack), self.number(token, stack)
            return {"equals": a == b, "greater_than": a > b, "less_than": a < b,
                    "greater_than_or_equals": a >= b, "less_than_or_equals": a <= b}[value(body, "compare", "equals")]
        if key in ("any_controlled_state", "any_owned_state"):
            return any(self.conditions(body, [*stack, site]) for site in self.sites
                       if (site.controller if key == "any_controlled_state" else site.owner) is obj)
        if key == "meta_trigger":
            replacements = {}
            for name, text in body:
                if name == "text":
                    continue
                match = re.fullmatch(r'"\[\?(\w+)\|\.0\]"', text)
                assert match, ("unmodelled meta replacement", text)
                replacements[name] = format(self.number(match[1], stack), ".0f")

            def expand(nodes):
                return [(k, expand(v) if isinstance(v, list) else
                         replacements.get(v[1:-1], v) if isinstance(v, str) and v.startswith("[") else v)
                        for k, v in nodes]

            return self.conditions(expand(value(body, "text")), stack)
        if key == "any_state_in":
            region = int(self.number(value(body, "strategic_region"), stack))
            self.region_queries.append((obj.name, region))
            # The native selector's membership is an explicit input boundary.
            return any(self.conditions([(k, v) for k, v in body if k != "strategic_region"], [*stack, site])
                       for site in self.sites if site.region == region)
        if key == "is_controlled_by":
            return obj.controller is self.scope(body, stack)
        if key == "is_in_array":
            mapping, name = self.storage(value(body, "array"), stack, arrays=True)
            return self.number(value(body, "value"), stack) in mapping.get(name, [])
        if key == "scope_exists":
            return True  # Existence is only a fixture assumption, never pointer proof.
        if key == "exists":
            assert obj.kind == "country"
            return body == "yes"
        if key == "impassable":
            assert obj.kind == "state"
            return body == "no"
        if key == "has_war":
            return body == "no"  # All fixture countries are at peace.
        if key == "has_dynamic_modifier":
            assert [k for k, _ in body] == ["modifier"], ("unmodelled trigger", key, body)
            return value(body, "modifier") in obj.dynamic_modifiers
        if key in TRIGGERS:
            return self.conditions(TRIGGERS[key], stack)
        raise AssertionError(("unmodelled trigger", key))

    def call(self, name, obj=None, stack=None):
        self.executed.add(name)
        existing = set(self.temp)
        existing_arrays = set(self.temp_arrays)
        try:
            self.execute(EFFECTS[name], stack if stack is not None else [obj or self.claimant])
        finally:
            for key in set(self.temp) - existing:
                del self.temp[key]
            for key in set(self.temp_arrays) - existing_arrays:
                del self.temp_arrays[key]

    def execute(self, nodes, stack):
        taken = False
        for key, body in nodes:
            obj = stack[-1]
            selected = self.scope(key, stack)
            if selected is not None:
                self.execute(body, [*stack, selected])
            elif key in ("if", "else_if", "else"):
                if key == "if":
                    taken = False
                if (key == "if" or not taken) and (key == "else" or self.conditions(value(body, "limit"), stack)):
                    self.execute([(k, v) for k, v in body if k != "limit"], stack)
                    taken = True
            elif key in ("every_controlled_state", "for_each_scope_loop"):
                if key == "every_controlled_state":
                    assert obj.kind == "country"
                    members = [site for site in self.sites if site.controller is obj]
                else:
                    mapping, name = self.storage(value(body, "array"), stack, arrays=True)
                    members = mapping.get(name, [])[:]
                for member in members:
                    nested = [*stack, member]
                    limit = value(body, "limit", [])
                    if self.conditions(limit, nested):
                        self.execute([(k, v) for k, v in body if k not in ("array", "limit", "break")], nested)
                    if key == "for_each_scope_loop" and self.temp.get(value(body, "break", "break"), 0):
                        break
            elif key == "save_event_target_as":
                self.targets[body] = obj
            elif key == "clear_temp_array":
                self.temp_arrays[body] = []
            elif key == "for_each_loop":
                name = value(body, "array")
                members = self.temp_arrays.get(name, obj.arrays.get(name, []))[:]
                for member in members[:1000]:
                    self.temp[value(body, "value")] = member
                    self.execute([(k, v) for k, v in body if k not in ("array", "value")], stack)
            elif key == "for_loop_effect":
                cursor = value(body, "value", "v")
                break_name = value(body, "break", "break")
                end = self.number(value(body, "end"), stack)
                step = self.number(value(body, "add", "1"), stack)
                self.temp[cursor] = self.number(value(body, "start"), stack)
                compare = value(body, "compare", "less_than")
                assert compare in ("less_than", "less_than_or_equals") and step > 0
                nodes = [(k, v) for k, v in body if k not in ("start", "end", "add", "value", "break", "compare")]
                iterations = 0
                while self.temp[cursor] < end or (compare == "less_than_or_equals" and self.temp[cursor] == end):
                    if self.temp.get(break_name, 0) or iterations == 1000:
                        break
                    self.execute(nodes, stack)
                    iterations += 1
                    self.temp[cursor] += step
            elif key in ("set_variable", "set_temp_variable", "add_to_variable", "add_to_temp_variable",
                         "subtract_from_variable", "subtract_from_temp_variable", "multiply_temp_variable",
                         "divide_temp_variable"):
                name = value(body, "var")
                token = value(body, "value")
                if name is None:
                    name, token = body[0]
                mapping, name = (self.temp, name) if "temp" in key else self.storage(name, stack)
                amount = self.number(token, stack)
                previous = mapping.get(name, Decimal(0))
                if key.startswith("set_"):
                    mapping[name] = amount
                elif key.startswith("add_"):
                    mapping[name] = previous + amount
                elif key.startswith("subtract_"):
                    mapping[name] = previous - amount
                elif key.startswith("multiply_"):
                    mapping[name] = previous * amount
                else:
                    mapping[name] = previous / (amount or self.number(value(body, "if_zero"), stack))
            elif key == "round_temp_variable":
                self.temp[body] = self.temp[body].quantize(Decimal(1), rounding=ROUND_HALF_UP)
            elif key == "clamp_temp_variable":
                name = value(body, "var")
                self.temp[name] = max(self.temp[name], self.number(value(body, "min"), stack))
            elif key == "clear_variable":
                mapping, name = self.storage(body, stack)
                mapping.pop(name, None)
            elif key == "clear_array":
                mapping, name = self.storage(body, stack, arrays=True)
                mapping[name] = []
            elif key == "add_to_array":
                mapping, name = self.storage(value(body, "array"), stack, arrays=True)
                mapping.setdefault(name, []).append(self.number(value(body, "value"), stack))
            elif key in ("set_country_flag", "clr_country_flag", "set_state_flag", "clr_state_flag"):
                assert obj.kind == ("state" if "state" in key else "country")
                (obj.flags.add if key.startswith("set_") else obj.flags.discard)(body)
            elif key in ("set_global_flag", "clr_global_flag"):
                assert isinstance(body, str), ("unmodelled global flag arguments", body)
                (self.global_state.flags.add if key.startswith("set_") else self.global_state.flags.discard)(body)
            elif key == "country_event":
                # Explicit native enqueue boundary. Reject every other event
                # and argument rather than silently broadening dispatch scope.
                assert obj.kind == "country" and value(body, "id") == "chaosx.nr32.192", body
                assert {k for k, _ in body} == {"id", "hours"}, body
                hours = self.number(value(body, "hours"), stack)
                assert hours > 0, ("unproven immediate observation delivery", hours)
                self.evolution_dispatches.append((obj, "chaosx.nr32.192", hours))
                self.boundaries.append((obj.name, "country_event", ("chaosx.nr32.192", hours)))
            elif key == "remove_mission":
                self.boundaries.append((obj.name, key, body))
                obj.missions.discard(body)  # No simulated native callback.
            elif key == "add_nuclear_bombs":
                self.boundaries.append((obj.name, key, body))
                obj.nukes += self.number(body, stack)  # Idealized native credit.
            elif key in ("add_dynamic_modifier", "remove_dynamic_modifier"):
                # Applied set only, so guarded removals read add/remove state.
                modifier = value(body, "modifier")
                assert modifier is not None, ("unmodelled effect", key, body)
                (obj.dynamic_modifiers.add if key == "add_dynamic_modifier" else obj.dynamic_modifiers.discard)(modifier)
                self.boundaries.append((obj.name, key, body))
            elif key in ("add_ideas", "remove_ideas"):
                self.boundaries.append((obj.name, key, body))  # Presentation only.
            elif key in EFFECTS:
                self.call(key, stack=stack)
            else:
                raise AssertionError(("unmodelled effect", key))

    def protected_snapshot(self):
        # Keep object references stable so a stored country pointer cannot be
        # mistaken for a plain numeric country ID or cloned scope object.
        protected = [self.government, *[s for s in self.sites if s.controller is self.government]]
        memo = {id(obj): obj for obj in [self.government, self.claimant, self.child, *self.sites]}
        return [deepcopy((obj.variables, obj.arrays, obj.flags, obj.missions, obj.nukes), memo) for obj in protected]


class ClaimantMissileScope(unittest.TestCase):
    def test_preflight_with_and_without_government_program(self):
        for government_program in (False, True):
            with self.subTest(government_program=government_program):
                m = Model(government_program)
                before = m.protected_snapshot()
                m.call("missiles_preflight_country_split")
                self.assertEqual(m.claimant.variables["missiles_civil_war_split_original_capacity"], 36)
                self.assertEqual(m.claimant.variables["missiles_civil_war_split_original_reserve"], 48)
                self.assertIs(m.targets["missiles_civil_war_parent"], m.claimant)
                for site in m.claimant.arrays["missiles_launch_site_states"]:
                    self.assertEqual(site.variables["missiles_site_civil_war_split_receipt_id"], 81)
                self.assertEqual(m.protected_snapshot(), before)

    def test_actual_abort_refund_payload_cleanup_and_refresh(self):
        for government_program in (False, True):
            with self.subTest(government_program=government_program):
                m = Model(government_program, operation=True)
                before = m.protected_snapshot()
                site = m.claimant.arrays["missiles_launch_site_states"][0]
                m.call("missiles_preflight_country_split")
                self.assertEqual(m.claimant.variables["missiles_civil_war_split_original_reserve"], 54)
                self.assertEqual(m.claimant.variables["missiles_reserved_reserve"], 0)
                self.assertEqual(m.claimant.variables["missiles_last_aborted_operation_id"], 71)
                self.assertEqual(m.claimant.variables["missiles_last_cleaned_operation_id"], 71)
                self.assertEqual(site.variables["missiles_site_operation_id"], 0)
                self.assertEqual(site.variables["missiles_site_operation_allocation"], 0)
                self.assertEqual(m.claimant.nukes, m.number("constant:missiles_resolution.nuclear_payload_units", [m.claimant]))
                self.assertFalse(m.claimant.missions)
                self.assertFalse(m.claimant.arrays["missiles_operation_sites"])
                self.assertEqual(m.claimant.variables["missiles_total_site_capacity"], 36)
                self.assertTrue({"missiles_abort_operation", "missiles_refund_operation_reserve",
                                 "missiles_cleanup_operation", "missiles_release_operation_payload",
                                 "missiles_recalculate_network", "missiles_rebalance_site_custody",
                                 "missiles_set_program_phases"}.issubset(m.executed))
                self.assertTrue({"missiles_notify_program_numbers_changed", "missiles_notify_evolution_change",
                                 "missiles_select_evolution_host"}.issubset(m.executed))
                self.assertEqual(m.evolution_dispatches,
                                 [(m.claimant, "chaosx.nr32.192",
                                   m.number("constant:missiles_evolution_pacing.observation_coalesce_hours", [m.claimant]))])
                self.assertIs(m.global_state.variables["missiles_evolution_host"], m.claimant)
                self.assertEqual(m.global_state.variables["missiles_evolution_observation_host_id"], m.claimant.id)
                self.assertEqual(m.claimant.variables["missiles_evolution_noted_operational_reserve"],
                                 m.claimant.variables["missiles_operational_reserve"])
                self.assertNotIn("missiles_run_evolution_observation", m.executed)
                self.assertNotIn("missiles_measure_evolution_pressure", m.executed)
                after_cleanup = m.claimant.variables.copy()
                m.call("missiles_cleanup_operation")
                self.assertEqual(m.claimant.variables, after_cleanup)
                self.assertEqual(len(m.evolution_dispatches), 1)
                self.assertEqual(m.protected_snapshot(), before)

    def test_rejection_changes_only_source_result(self):
        for reason in ("no_program", "missing_reserve", "active_transaction"):
            with self.subTest(reason=reason):
                m = Model(operation=True)
                if reason == "no_program":
                    m.claimant.flags.discard("missiles_program_initialized")
                elif reason == "missing_reserve":
                    del m.claimant.variables["missiles_operational_reserve"]
                else:
                    m.claimant.flags.add("missiles_civil_war_split_transaction_active")
                protected, sequence = m.protected_snapshot(), m.global_state.variables.copy()
                reserve, missions = m.claimant.variables.get("missiles_reserved_reserve"), m.claimant.missions.copy()
                m.call("missiles_preflight_country_split")
                self.assertEqual(m.claimant.variables["missiles_split_preflight_result"], m.number("constant:missiles_result.rejected", [m.claimant]))
                self.assertEqual(m.claimant.variables["missiles_reserved_reserve"], reserve)
                self.assertEqual(m.claimant.missions, missions)
                self.assertNotIn("missiles_civil_war_parent", m.targets)
                self.assertEqual(m.global_state.variables, sequence)
                self.assertEqual(m.protected_snapshot(), protected)

    def test_child_commit_and_parent_callback_with_foreign_or_child_root(self):
        for root_is_child in (False, True):
            with self.subTest(root_is_child=root_is_child):
                m = Model(operation=True)
                before = m.protected_snapshot()
                m.call("missiles_preflight_country_split")
                transferred = m.claimant.arrays["missiles_launch_site_states"][1]
                # Explicit native boundary: this fixture supplies the engine's
                # ownership/control result and does not simulate civil war.
                transferred.owner = transferred.controller = m.child
                m.boundaries.append((m.child.name, "native_child_assignment", transferred.name))
                if root_is_child:
                    m.root = m.child
                m.call("missiles_split_program_after_civil_war", m.child)
                original = m.claimant.variables["missiles_civil_war_split_original_reserve"]
                percent = m.number("constant:missiles_reserve.site_civil_war_reserve_share_percent", [m.child])
                expected = (original * percent / 100 * Decimal(24) / 36).quantize(Decimal(1), rounding=ROUND_HALF_UP)
                self.assertEqual(m.child.variables["missiles_operational_reserve"], expected)
                self.assertEqual(m.claimant.variables["missiles_operational_reserve"], original - expected)
                self.assertEqual(m.child.variables["missiles_civil_war_split_source_id"], m.claimant.id)
                self.assertEqual(m.claimant.variables["missiles_civil_war_split_residual"], 0)
                self.assertEqual(m.child.arrays["missiles_launch_site_states"], [transferred])
                retained = [s for s in m.sites if s.controller is m.claimant]
                self.assertEqual(m.claimant.arrays["missiles_launch_site_states"], retained)
                for country, sites in ((m.child, [transferred]), (m.claimant, retained)):
                    for site in sites:
                        self.assertEqual(site.variables["missiles_site_owner_id"], country.id)
                        self.assertIs(site.variables["missiles_site_current_controller"], country)
                        self.assertNotIn("missiles_site_civil_war_split_pending", site.flags)
                self.assertNotIn("missiles_civil_war_split_transaction_active", m.claimant.flags)
                country_before = m.claimant.variables.copy()
                m.call("missiles_finalize_civil_war_split_parent")
                self.assertEqual(m.claimant.variables, country_before)
                self.assertEqual(m.protected_snapshot(), before)
                self.assertEqual(m.temp, {})

    def test_accepted_preflight_without_native_child_retains_pending_receipt(self):
        m = Model()
        before = m.protected_snapshot()
        m.call("missiles_preflight_country_split")
        self.assertIn("missiles_civil_war_split_transaction_active", m.claimant.flags)
        self.assertTrue(all("missiles_site_civil_war_split_pending" in s.flags
                            for s in m.claimant.arrays["missiles_launch_site_states"]))
        self.assertEqual(m.claimant.variables["missiles_operational_reserve"], 48)
        self.assertEqual(m.protected_snapshot(), before)
        # No invented rollback callback. This records the parent-owned gap.

    def test_helper_return_keeps_only_caller_preinitialized_temporaries(self):
        m = Model()
        m.temp["missiles_custody_take"] = Decimal(-1)
        m.call("missiles_rebalance_site_custody")
        self.assertEqual(set(m.temp), {"missiles_custody_take"})
        self.assertGreater(m.temp["missiles_custody_take"], 0)
        self.assertEqual(m.claimant.variables["missiles_unallocated_reserve"], 12)

    def test_uncached_region_preflight_follows_claimant_controller(self):
        for government_program in (False, True):
            for foreign_owned in (False, True):
                with self.subTest(government_program=government_program, foreign_owned=foreign_owned):
                    m = Model(government_program, operation=True)
                    for site in m.claimant.arrays["missiles_launch_site_states"]:
                        del site.variables["missiles_site_strategic_region"]
                        if foreign_owned:
                            site.owner = m.government
                            site.variables["missiles_site_current_controller"] = m.government
                    # A pre-existing ROOT scratch record must survive completely.
                    m.government.variables.update(missiles_region_probe_found=77, missiles_region_probe_found_id=88)
                    m.government.arrays["missiles_region_probe_states"] = [m.sites[0]]
                    before = m.protected_snapshot()
                    m.call("missiles_preflight_country_split")
                    self.assertEqual(m.claimant.variables["missiles_civil_war_split_original_capacity"], 36)
                    self.assertEqual(m.claimant.variables["missiles_civil_war_split_original_reserve"], 54)
                    self.assertTrue(m.region_queries)
                    self.assertTrue(all(country == "claimant" for country, _ in m.region_queries))
                    for site in m.claimant.arrays["missiles_launch_site_states"]:
                        self.assertEqual(site.variables["missiles_site_strategic_region"], site.region)
                        self.assertEqual(site.variables["missiles_site_civil_war_split_receipt_id"], 81)
                    self.assertFalse(m.claimant.arrays["missiles_region_probe_states"])
                    self.assertNotIn("missiles_region_probe_found_id", m.claimant.variables)
                    self.assertEqual(m.protected_snapshot(), before)
                    self.assertEqual(m.temp, {})

    def test_network_skips_foreign_controlled_uncached_registry_entry(self):
        m = Model()
        foreign_site = next(s for s in m.sites if s.controller is m.government)
        del foreign_site.variables["missiles_site_strategic_region"]
        m.claimant.arrays["missiles_launch_site_states"].append(foreign_site)
        for site in m.sites:
            if site.controller is m.claimant:
                del site.variables["missiles_site_strategic_region"]
        before = m.protected_snapshot()
        m.call("missiles_recalculate_network")
        self.assertEqual(m.claimant.variables["missiles_total_site_capacity"], 36)
        self.assertNotIn("missiles_site_strategic_region", foreign_site.variables)
        self.assertTrue(all(country == "claimant" for country, _ in m.region_queries))
        self.assertEqual(m.protected_snapshot(), before)

    def test_cached_region_bypasses_target_capture_and_all_scratch(self):
        m = Model()
        site = m.sites[0]
        m.claimant.variables["missiles_region_probe_found_id"] = 91
        m.claimant.arrays["missiles_region_probe_states"] = [site]
        m.targets["missiles_region_probe_country"] = m.government
        m.targets["missiles_region_probe_state"] = m.sites[-1]
        before = (m.protected_snapshot(), m.claimant.variables.copy(),
                  m.claimant.arrays["missiles_region_probe_states"][:], m.targets.copy())
        m.call("missiles_assign_site_strategic_region", stack=[m.government, m.claimant, site])
        self.assertEqual((m.protected_snapshot(), m.claimant.variables,
                          m.claimant.arrays["missiles_region_probe_states"], m.targets), before)
        self.assertFalse(m.region_queries)

    def test_uncached_child_and_parent_regions_use_each_native_controller(self):
        m = Model(operation=False)
        before = m.protected_snapshot()
        m.call("missiles_preflight_country_split")
        transferred = m.claimant.arrays["missiles_launch_site_states"][1]
        transferred.owner = transferred.controller = m.child
        for site in m.sites:
            if site.controller is not m.government:
                del site.variables["missiles_site_strategic_region"]
        m.call("missiles_split_program_after_civil_war", m.child)
        self.assertEqual(m.claimant.variables["missiles_civil_war_split_residual"], 0)
        self.assertEqual({country for country, _ in m.region_queries}, {"claimant", "child"})
        self.assertEqual(transferred.variables["missiles_site_strategic_region"], transferred.region)
        self.assertEqual(m.protected_snapshot(), before)
        self.assertEqual(m.temp, {})

    def test_existing_parent_finalizer_is_settlement_not_no_child_rollback(self):
        m = Model()
        before = m.protected_snapshot()
        original_readiness = m.claimant.variables["missiles_launch_readiness"]
        original_control = m.claimant.variables["missiles_command_control"]
        m.call("missiles_preflight_country_split")
        m.call("missiles_finalize_civil_war_split_parent")
        self.assertNotIn("missiles_civil_war_split_transaction_active", m.claimant.flags)
        self.assertEqual(m.claimant.variables["missiles_operational_reserve"], 48)
        self.assertLess(m.claimant.variables["missiles_launch_readiness"], original_readiness)
        self.assertLess(m.claimant.variables["missiles_command_control"], original_control)
        self.assertIn("missiles_civil_war_command_split", m.claimant.flags)
        self.assertTrue(all("missiles_site_isolated" in site.flags for site in m.sites
                            if site.controller is m.claimant))
        self.assertEqual(m.protected_snapshot(), before)


if __name__ == "__main__":
    unittest.main()
