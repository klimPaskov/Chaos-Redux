"""Bounded production-source regressions for the famine takeover.

This executes selected real effect/trigger bodies with conservative temporary
call frames. It models only scoped engine facts and native primitives reached
by these paths. Registry, report, achievement, and live-game behavior remain
outside the fixture; unsupported reached commands raise SourceContractError.
"""
from decimal import Decimal, ROUND_HALF_UP
from functools import lru_cache
import importlib.util
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
_SPEC = importlib.util.spec_from_file_location(
    "event035_scaffolding", ROOT / ".tools" / "test_event035_center_projects.py"
)
_PARSER = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_PARSER)
Node = _PARSER.Node
Definition = _PARSER.Definition
SourceContractError = _PARSER.SourceContractError

EFFECT_FILES = (
    r"common\scripted_effects\famine_core_effects.txt",
    r"common\scripted_effects\famine_adapter_effects.txt",
    r"common\scripted_effects\chaosx_dynamic_effects.txt",
)
TRIGGER_FILES = (
    r"common\scripted_triggers\famine_core_triggers.txt",
    r"common\scripted_triggers\humanitarian_validation_triggers.txt",
    r"common\scripted_triggers\famine_decision_owner_triggers.txt",
)
CONSTANT_GROUPS = {
    "chaos_meter_deaths", "chaosx_date_units", "civilian_transfer_route_result",
    "famine_food_component", "famine_food_reserve", "famine_food_score",
    "famine_food_stage", "famine_food_timing", "famine_food_weight",
    "famine_mission_contract", "famine_occupation_profile", "famine_profile_context",
    "famine_profile_id", "famine_profile_mode", "famine_profile_state_id",
    "famine_surface_context", "humanitarian_legacy_cost", "humanitarian_population",
    "humanitarian_pressure_source", "humanitarian_runtime", "migration_border_policy",
}
CONSTANT_FILES = (
    "chaos_meter_constants.txt", "chaosx_date_units_constants.txt", "civilian_transfer_constants.txt",
    "famine_core_constants.txt", "famine_mission_constants.txt", "humanitarian_legacy_cost_constants.txt",
    "humanitarian_runtime_constants.txt", "migration_core_constants.txt",
)
SCOPE_NAMES = {"OWNER": "event_target:__famine_owner__", "CONTROLLER": "event_target:__famine_controller__", "FROM": "event_target:__famine_from__"}
HEADER = re.compile(r"(?m)^([A-Za-z_][A-Za-z0-9_]*)[ \t]*=[ \t]*\{")
NUMBER = re.compile(r"^-?\d+(?:\.\d+)?$")


def read_one(relative_path, name):
    """Use the shared lexer/parser on one named block, avoiding unrelated syntax."""
    path = ROOT / relative_path
    source = _PARSER.uncomment(path.read_text(encoding="utf-8-sig"))
    tokens = _PARSER.lex(source)
    for index, token in enumerate(tokens[:-2]):
        if token.text == name and tokens[index + 1].text == "=" and tokens[index + 2].text == "{":
            body, cursor = _PARSER.parse_nodes(tokens, index + 3, f"{path.name}:{name}")
            if cursor >= len(tokens) or tokens[cursor].text != "}":
                raise SourceContractError(f"{path.name}:{name}: unclosed source block")
            return Definition(name, path, token.line, adapt_nodes(body))
    raise SourceContractError(f"missing source definition {name} in {path}")


def read_parseable_definitions(relative_path):
    """Parse each top-level body independently; unrelated list syntax may be skipped."""
    path = ROOT / relative_path
    source = _PARSER.uncomment(path.read_text(encoding="utf-8-sig"))
    tokens = _PARSER.lex(source)
    token_at = {token.offset: index for index, token in enumerate(tokens)}
    result = {}
    for match in HEADER.finditer(source):
        name = match.group(1)
        opening = token_at.get(match.end() - 1)
        if opening is None or tokens[opening].text != "{":
            continue
        try:
            body, cursor = _PARSER.parse_nodes(tokens, opening + 1, f"{path.name}:{name}")
            if cursor >= len(tokens) or tokens[cursor].text != "}":
                continue
        except SourceContractError:
            continue
        result[name] = Definition(name, path, tokens[opening].line, adapt_nodes(body))
    return result


def _decimal(value):
    return value if isinstance(value, Decimal) else Decimal(str(value))


def adapt_nodes(nodes):
    return [Node(SCOPE_NAMES.get(n.key, n.key), n.op,
                 adapt_nodes(n.value) if isinstance(n.value, list) else SCOPE_NAMES.get(n.value, n.value) if isinstance(n.value, str) else n.value,
                 n.line) for n in nodes]


@lru_cache(maxsize=1)
def load_constants():
    values = {}
    base = ROOT / "common" / "script_constants"
    for filename in CONSTANT_FILES:
        path = base / filename
        for group, definition in read_parseable_definitions(str(path.relative_to(ROOT))).items():
            if group not in CONSTANT_GROUPS:
                continue
            for node in definition.body:
                if isinstance(node.value, str) and NUMBER.fullmatch(node.value):
                    values[f"constant:{group}.{node.key}"] = _decimal(node.value)
    if not values:
        raise SourceContractError("no famine constants were loaded")
    return values


class FamineRuntime(_PARSER.Event35Runtime):
    """Reuse Event35Runtime frames, scopes, primitives, and executor."""
    EXTERNAL_EFFECTS = {
        "famine_register_active_state", "famine_register_historical_profile_candidate_state",
        "famine_unregister_historical_profile_candidate_state", "famine_register_initial_incident",
        "famine_submit_survivor_flight_request", "famine_refresh_dynamic_modifiers",
        "famine_cleanup_state_registration", "famine_show_report_generic",
        "famine_show_report_island_blockade", "migration_mark_reception_capacity_dirty_if_candidate",
        "humanitarian_achievement_process_state",
    }
    EXTERNAL_FIXTURES = EXTERNAL_EFFECTS
    EXTERNAL_FACTS = {"genocide_state_has_active_camps", "genocide_state_has_atrocity_evidence"}
    OUTPUTS = {"famine_occupation_profile", "famine_local_war_evidence", "famine_profile_mapping_result",
               "famine_historical_profile_state_proven", "famine_historical_profile_context_proven"}

    def __init__(self):
        self.helper_returns, self.from_scope = [], None
        saved = (_PARSER.EFFECT_FILES, _PARSER.TRIGGER_FILES, _PARSER.read_definitions)
        _PARSER.EFFECT_FILES, _PARSER.TRIGGER_FILES = EFFECT_FILES[:2], TRIGGER_FILES
        _PARSER.read_definitions = lambda path: read_parseable_definitions(str(path))
        try:
            super().__init__()
        finally:
            _PARSER.EFFECT_FILES, _PARSER.TRIGGER_FILES, _PARSER.read_definitions = saved
        self.effect_defs["chaosx_convert_days_to_date_offset"] = read_one(
            r"common\scripted_effects\chaosx_dynamic_effects.txt", "chaosx_convert_days_to_date_offset")
        self.effects, self.triggers = self.effect_defs, self.trigger_defs
        self.globals["date"] = Decimal(0)
        self.calendar_date = (1936, 1, 1)
        self.file_constants = {key: _decimal(value) for key, value in self.file_constants.items()}

    def _read_constants(self):
        return load_constants()

    def _value(self, token):
        if token == "event_target:__famine_owner__": return self.current.owner
        if token == "event_target:__famine_controller__": return self.current.controller
        if token == "event_target:__famine_from__":
            if self.from_scope is None: raise SourceContractError("FROM without decision target")
            return self.from_scope
        value = super()._value(token)
        if isinstance(value, str) and token.startswith(("famine_", "humanitarian_", "migration_", "air_", "camp_", "nuclear_", "forced_labor_")):
            return self._variable(token)
        return value

    def _condition(self, node, scope):
        key, op, value = node.key, node.op, node.value
        if op in ("<", ">") and key in scope.values:
            return scope.values[key] < self._value(value) if op == "<" else scope.values[key] > self._value(value)
        if op in ("<", ">") and key == "gulag_labor_camp_network":
            fact = _decimal(scope.values.get(key, 0))
            return fact < self._value(value) if op == "<" else fact > self._value(value)
        if key == "date":
            right = tuple(int(part) for part in value.split("."))
            return self.calendar_date < right if op == "<" else self.calendar_date > right if op == ">" else self.calendar_date == right
        if key == "scope_exists": return True
        if key == "state": return scope.kind == "state" and scope.id == self._value(value)
        if key == "tag":
            target = self._value(value)
            tag = target.values.get("tag") if isinstance(target, ScopeType) else target
            return scope.kind == "country" and scope.values.get("tag") == tag
        if key == "has_war": return scope.kind == "country" and bool(scope.values.get("at_war", False)) == (value == "yes")
        if key == "has_war_with":
            target = self._value(value)
            return scope.kind == "country" and target.values.get("tag") in scope.values.get("wars_with", set())
        if key == "has_resistance": return bool(scope.values.get("has_resistance", False)) == (value == "yes")
        if key == "occupation_law": return scope.values.get("occupation_law") == value
        if key == "is_core_of": return self._value(value).values.get("tag") in scope.values.get("core_tags", set())
        if key == "is_owned_and_controlled_by": return scope.owner is scope.controller is self._value(value)
        if key == "has_dynamic_modifier": return value in scope.modifiers
        if key in self.EXTERNAL_FACTS: return bool(scope.values.get(key, False)) == (value == "yes")
        if key == "any_neighbor_state":
            for neighbor in scope.values.get("neighbors", []):
                self.scope_stack.append(neighbor)
                try:
                    if self._conditions(value, neighbor): return True
                finally: self.scope_stack.pop()
            return False
        return super()._condition(node, scope)

    def _call_effect(self, name, scope):
        if name in self.EXTERNAL_EFFECTS:
            self.external_calls.append(name); return
        super()._call_effect(name, scope)
        if self.temp_frames:
            self.helper_returns.append((name, {k: self.temp_frames[-1][k] for k in self.OUTPUTS if k in self.temp_frames[-1]}))

    def _effects(self, nodes, scope):
        i = 0
        while i < len(nodes):
            node = nodes[i]
            if node.key in ("if", "else_if", "else"):
                end = i + 1
                while end < len(nodes) and nodes[end].key in ("else_if", "else"): end += 1
                super()._effects(nodes[i:end], scope); i = end; continue
            if node.key in ("divide_variable", "divide_temp_variable", "clamp_variable", "clamp_temp_variable"):
                if node.key.startswith("divide"):
                    name, divisor = node.value[0].key, _decimal(self._value(node.value[0].value))
                    value = _decimal(self._variable(name)) / divisor
                else:
                    args = {c.key: self._value(c.value) for c in node.value}; name = next(c.value for c in node.value if c.key == "var")
                    value = _decimal(self._variable(name))
                    if "min" in args: value = max(value, _decimal(args["min"]))
                    if "max" in args: value = min(value, _decimal(args["max"]))
                self._set_temp(name, value) if node.key.endswith("temp_variable") else self._write_path(name, value)
            else:
                try: super()._effects([node], scope)
                except TypeError as exc:
                    raise SourceContractError(f"unsupported arithmetic input {node.key} {node.value}; caller stack={self.call_stack}") from exc
            i += 1

    def run_trigger(self, name, scope, root=None):
        return self.test_trigger(name, scope, root=root)

    def run_nodes(self, nodes, scope, root=None, caller_temps=None, from_scope=None):
        old = (self.root, self.scope_stack, self.temp_frames, self.from_scope)
        self.root = root if root is not None else (scope if scope.kind == "country" else scope.owner)
        self.scope_stack, self.temp_frames, self.from_scope = [scope], [dict(caller_temps or {})], from_scope
        try: return self._effects(nodes, scope) or dict(self.temp_frames[0])
        finally: self.root, self.scope_stack, self.temp_frames, self.from_scope = old

    def run_effect(self, name, scope, root=None, caller_temps=None):
        old = (self.root, self.scope_stack, self.temp_frames)
        self.root = root if root is not None else (scope if scope.kind == "country" else scope.owner)
        self.scope_stack, self.temp_frames = [scope], [dict(caller_temps or {})]
        try:
            self._call_effect(name, scope)
            return dict(self.temp_frames[0])
        finally: self.root, self.scope_stack, self.temp_frames = old

    def advance_days(self, days):
        self.globals["date"] += _decimal(days) * Decimal("0.00024")

ScopeType = _PARSER.Scope


def country(tag, at_war=False, wars_with=()):
    return ScopeType("country", tag, values={"tag": tag, "at_war": at_war, "wars_with": set(wars_with)})


def state(state_id, owner, controller=None, population_k=100):
    return ScopeType("state", state_id, owner=owner, controller=controller or owner, population_k=population_k,
                     values={"state_population_k": Decimal(population_k)})


def _children(node, key):
    return [child for child in node.value if child.key == key]


def _effect_body(runtime, name):
    body = runtime.effects[name].body
    outer = next(node for node in body if node.key == "if")
    return [node for node in outer.value if node.key != "limit"]


def component_pipeline_nodes(runtime):
    body = _effect_body(runtime, "famine_evaluate_food_security")
    resetters = [node for node in body if node.key == "set_temp_variable" and _PARSER.first(node.value, "famine_external_production") is not None]
    resets = []
    for node in body:
        if node in resetters:
            start = body.index(node)
            resets = body[start:start + 8]
            break
    collect = next(node for node in body if node.key == "famine_collect_surface_context")
    rebuild = next(node for node in body if node.key == "famine_rebuild_food_components")
    score_init = [node for node in body if node.key == "set_temp_variable" and _PARSER.first(node.value, "famine_food_score_raw") is not None]
    requested_init = [node for node in body if node.key == "set_temp_variable" and _PARSER.first(node.value, "famine_requested_food_stage") is not None]
    calculate = next(node for node in body if node.key == "famine_calculate_food_score")
    if len(resets) != 8 or not score_init or not requested_init:
        raise SourceContractError("evaluator caller output initialization changed")
    return resets + [collect, rebuild, score_init[0], requested_init[0], calculate]


def stage_clock_nodes(runtime):
    body = _effect_body(runtime, "famine_evaluate_food_security")
    for index, node in enumerate(body):
        if node.key not in ("if", "else_if"):
            continue
        limit = _PARSER.first(node.value, "limit", [])
        if any(
            child.key == "check_variable"
            and _PARSER.first(child.value, "var") == "famine_requested_food_stage"
            and _PARSER.first(child.value, "compare") == "greater_than"
            and _PARSER.first(child.value, "value") == "famine_food_stage"
            for child in limit
        ):
            chain = [node]
            for sibling in body[index + 1:]:
                if sibling.key not in ("else_if", "else"):
                    break
                chain.append(sibling)
            return chain
    raise SourceContractError("candidate/recovery clock block not found in evaluator")


def execute_evaluation_slice(runtime, scope):
    previous = (runtime.root, runtime.scope_stack, runtime.temp_frames)
    runtime.root, runtime.scope_stack, runtime.temp_frames = scope.owner, [scope], [{}]
    runtime._call_effect("famine_apply_historical_profile_context", scope)
    runtime._effects(component_pipeline_nodes(runtime), scope)
    runtime._effects(stage_clock_nodes(runtime), scope)
    result = dict(runtime.temp_frames[0])
    runtime.root, runtime.scope_stack, runtime.temp_frames = previous
    return result


class FamineTakeoverRegressions(unittest.TestCase):
    def setUp(self):
        self.runtime = FamineRuntime()

    def test_selector_local_war_and_profile_proof_cross_real_call_frames(self):
        owner = country("MAN", at_war=True, wars_with={"JAP"})
        controller = country("CHI", at_war=True, wars_with={"JAP"})
        province = state(607, owner, controller)
        province.values.update(has_resistance=True, occupation_law="no_garrison")
        self.runtime.calendar_date = (1942, 5, 1)
        self.runtime.run_effect("famine_select_historical_profile_id", province)

        self.assertEqual(province.values["famine_historical_profile_id"], self.runtime.constants["constant:famine_profile_id.hist_china_henan_1942"])
        occupation_return = next(values for name, values in self.runtime.helper_returns if name == "famine_resolve_occupation_profile")
        war_return = next(values for name, values in self.runtime.helper_returns if name == "famine_resolve_local_war_evidence")
        self.assertEqual(occupation_return["famine_occupation_profile"], self.runtime.constants["constant:famine_occupation_profile.standard"])
        self.assertEqual(war_return["famine_local_war_evidence"], self.runtime.constants["constant:humanitarian_runtime.one"])

        self.runtime.run_effect("famine_apply_historical_profile_context", province)
        profile_return = [values for name, values in self.runtime.helper_returns if name == "famine_resolve_historical_profile_context"][-1]
        self.assertEqual(profile_return["famine_historical_profile_state_proven"], self.runtime.constants["constant:humanitarian_runtime.one"])
        self.assertEqual(profile_return["famine_historical_profile_context_proven"], self.runtime.constants["constant:humanitarian_runtime.one"])
        self.assertIn("famine_profile_context_active", province.flags)
        self.assertEqual(province.values["famine_profile_context_id"], self.runtime.constants["constant:famine_profile_id.hist_china_henan_1942"])

    def test_china_ceara_and_congo_cause_gates(self):
        rt = self.runtime
        required = {"famine_china_policy_profile_cause_proven", "famine_ceara_profile_cause_proven", "famine_congo_profile_cause_proven"}
        if not required.issubset(rt.trigger_defs):
            self.skipTest("round3 cause-gate source is unpublished on this checkout")
        chi = country("CHI")
        henan = state(607, chi)
        henan.values["famine_food_pressure"] = 5
        henan.flags.add("famine_extraction_active")
        self.assertTrue(rt.run_trigger("famine_china_policy_profile_cause_proven", henan))
        henan.values["famine_food_pressure"] = 0
        self.assertFalse(rt.run_trigger("famine_china_policy_profile_cause_proven", henan))

        bra = country("BRA")
        ceara = state(935, bra)
        ceara.values.update(famine_food_pressure=5, famine_last_pressure_source=rt.constants["constant:humanitarian_pressure_source.natural_disaster"])
        self.assertTrue(rt.run_trigger("famine_ceara_profile_cause_proven", ceara))
        ceara.values["famine_last_pressure_source"] = 0
        self.assertFalse(rt.run_trigger("famine_ceara_profile_cause_proven", ceara))

        bel = country("BEL")
        congo = state(295, bel)
        congo.values["famine_food_pressure"] = 5
        self.assertTrue(rt.run_trigger("famine_congo_profile_cause_proven", congo))
        congo.values["core_tags"] = {"BEL"}
        self.assertFalse(rt.run_trigger("famine_congo_profile_cause_proven", congo))

    def test_weighted_surface_score_context_expiry_and_stage_recovery(self):
        rt = self.runtime
        required = {"famine_open_outbreak_food_context", "famine_open_disaster_food_context"}
        if not required.issubset(rt.effect_defs):
            self.skipTest("round3 outbreak/disaster context source is unpublished on this checkout")
        peaceful_country = country("BRA")
        province = state(99, peaceful_country)
        province.flags.add("famine_blockade_candidate_active")  # retain registry through recovery
        rt.run_effect("famine_initialize_state", province)
        score = execute_evaluation_slice(rt, province)
        self.assertEqual(score["famine_food_score_raw"], Decimal(0))
        self.assertEqual(province.values["famine_food_security_score"], Decimal(0))

        rt.run_effect("famine_open_outbreak_food_context", province)
        outbreak_until = province.values["famine_outbreak_context_until_date"]
        self.assertEqual(outbreak_until - rt.globals["date"], Decimal("0.0072"))
        score = execute_evaluation_slice(rt, province)
        self.assertGreater(score["famine_food_score_raw"], Decimal(25))
        self.assertEqual(province.values["famine_component_production"], Decimal(20))
        rt.advance_days(7)
        score = execute_evaluation_slice(rt, province)
        self.assertEqual(province.values["famine_food_stage"], Decimal(1))

        rt.advance_days(23)
        score = execute_evaluation_slice(rt, province)
        self.assertEqual(score["famine_food_score_raw"], Decimal(0))
        recovery_start = province.values["famine_food_recovery_since_date"]
        rt.advance_days(13)
        execute_evaluation_slice(rt, province)
        self.assertEqual(province.values["famine_food_stage"], Decimal(1))
        rt.advance_days(1)
        execute_evaluation_slice(rt, province)
        self.assertEqual(province.values["famine_food_stage"], Decimal(0))
        self.assertNotIn("famine_food_recovery_since_date", province.values)

        rt.run_effect("famine_open_disaster_food_context", province)
        disaster_until = province.values["famine_disaster_context_until_date"]
        self.assertEqual(disaster_until - rt.globals["date"], Decimal("0.0144"))
        rt.advance_days(59)
        active = execute_evaluation_slice(rt, province)
        self.assertGreater(active["famine_food_score_raw"], Decimal(25))
        rt.advance_days(1)
        expired = execute_evaluation_slice(rt, province)
        self.assertEqual(expired["famine_food_score_raw"], Decimal(0))

        wartime_owner = country("FRA", at_war=True, wars_with={"GER"})
        wartime_controller = country("GER", at_war=True, wars_with={"FRA"})
        occupied = state(120, wartime_owner, wartime_controller)
        occupied.values.update(has_resistance=True, occupation_law="no_garrison")
        rt.run_effect("famine_initialize_state", occupied)
        stable = execute_evaluation_slice(rt, occupied)
        war_return = [values for name, values in rt.helper_returns if name == "famine_resolve_local_war_evidence"][-1]
        self.assertGreater(war_return["famine_local_war_evidence"], Decimal(0))
        self.assertGreater(occupied.values["famine_component_transport"], Decimal(0))
        self.assertLess(stable["famine_food_score_raw"], Decimal(25))

    def test_reserve_consumer_caps_rounds_and_rejects_without_debit(self):
        rt = self.runtime
        owner = country("BRA")

        def consume(relief, stock, request_days=10, valid=True):
            target = state(935, owner, population_k=100)
            target.values.update(
                famine_food_reserve_amount=Decimal(stock), famine_food_reserve_relief=Decimal(relief),
                famine_food_reserve_daily_need=Decimal(100), famine_food_reserve_initialized=Decimal(1),
                famine_food_reserve_release_amount=Decimal(request_days * 100),
                famine_food_reserve_release_request_proven=Decimal(1 if valid else 0),
                famine_food_reserve_release_actor_proven=Decimal(1), infrastructure_level=5,
            )
            target.flags.add("famine_food_reserve_initialized")
            frame = rt.run_effect("famine_release_reserves", target, caller_temps={
                "famine_food_reserve_consume_result": rt.constants["constant:civilian_transfer_route_result.invalid"],
                "famine_food_reserve_consumed_output": Decimal(0),
                "famine_food_reserve_relief_granted_output": Decimal(0),
                "famine_food_reserve_remaining_output": Decimal(0),
            })
            return target, frame

        near_cap, output = consume(32, 1000)
        self.assertEqual(output["famine_food_reserve_consumed_output"], Decimal(200))
        self.assertEqual(output["famine_food_reserve_relief_granted_output"], Decimal(3))
        self.assertEqual(near_cap.values["famine_food_reserve_amount"], Decimal(800))

        full, output = consume(35, 1000)
        self.assertEqual(output["famine_food_reserve_consumed_output"], Decimal(0))
        self.assertEqual(full.values["famine_food_reserve_amount"], Decimal(1000))

        low_stock, output = consume(0, 75)
        self.assertEqual(output["famine_food_reserve_consumed_output"], Decimal(75))
        self.assertEqual(output["famine_food_reserve_relief_granted_output"], Decimal("1.125"))
        self.assertEqual(low_stock.values["famine_food_reserve_amount"], Decimal(0))

        rejected, output = consume(0, 1000, valid=False)
        self.assertEqual(output["famine_food_reserve_consumed_output"], Decimal(0))
        self.assertEqual(rejected.values["famine_food_reserve_amount"], Decimal(1000))
        self.assertNotIn("famine_food_reserve_release_request_proven", rejected.values)

    def test_decision_refunds_zero_consumption_only_for_its_receipt(self):
        decision = read_one(r"common\decisions\famine_decisions.txt", "famine_release_reserves")
        remove_effect = next(node for node in decision.body if node.key == "remove_effect")
        receipt = next(index for index, node in enumerate(remove_effect.value) if node.key == "if")
        receipt_branch = remove_effect.value[receipt:receipt + 2]
        owner = country("BRA")
        target = state(935, owner, population_k=100)
        target.values.update(
            famine_food_reserve_amount=Decimal(1000), famine_food_reserve_relief=Decimal(35),
            famine_food_reserve_daily_need=Decimal(100), famine_food_reserve_initialized=Decimal(1),
            infrastructure_level=5, famine_release_reserves_cost_payer=owner,
        )
        target.flags.update({"famine_food_reserve_initialized", "famine_release_reserves_cost_paid"})
        owner.resources.update(political_power=Decimal(0), support_equipment=Decimal(0), fuel=Decimal(0))
        rt = self.runtime
        rt.run_nodes(receipt_branch, owner, root=owner, from_scope=target)
        self.assertGreater(owner.resources["political_power"], Decimal(0))
        self.assertGreater(owner.resources["support_equipment"], Decimal(0))
        self.assertGreater(owner.resources["fuel"], Decimal(0))
        self.assertEqual(target.values["famine_food_reserve_amount"], Decimal(1000))
        self.assertNotIn("famine_release_reserves_cost_paid", target.flags)
        refunded = dict(owner.resources)
        rt.run_nodes(receipt_branch, owner, root=owner, from_scope=target)
        self.assertEqual(owner.resources, refunded)

    def test_stage_clock_reversals_and_recovery_step_reset(self):
        rt = self.runtime
        owner = country("BRA")
        now = rt.globals["date"]
        province = state(99, owner)
        province.values.update(famine_food_stage=Decimal(1), famine_food_stage_candidate=Decimal(1),
                               famine_food_recovery_since_date=now - Decimal("0.001"))
        rt.run_nodes(stage_clock_nodes(rt), province, caller_temps={
            "famine_requested_food_stage": Decimal(2), "famine_food_score_raw": Decimal(0)})
        self.assertNotIn("famine_food_recovery_since_date", province.values)
        self.assertEqual(province.values["famine_food_stage_candidate_since_date"], now)

        province.values["famine_food_stage_candidate_since_date"] = now - Decimal("0.001")
        province.values["famine_food_stage_candidate"] = Decimal(1)
        rt.run_nodes(stage_clock_nodes(rt), province, caller_temps={
            "famine_requested_food_stage": Decimal(0), "famine_food_score_raw": Decimal(0)})
        self.assertNotIn("famine_food_stage_candidate_since_date", province.values)
        self.assertEqual(province.values["famine_food_recovery_since_date"], now)

        province.values.update(famine_food_stage=Decimal(2), famine_food_recovery_since_date=now - Decimal("0.00504"))
        rt.run_nodes(stage_clock_nodes(rt), province, caller_temps={
            "famine_requested_food_stage": Decimal(1), "famine_food_score_raw": Decimal(0)})
        self.assertEqual(province.values["famine_food_stage"], Decimal(1))
        self.assertNotIn("famine_food_recovery_since_date", province.values)
        rt.run_nodes(stage_clock_nodes(rt), province, caller_temps={
            "famine_requested_food_stage": Decimal(0), "famine_food_score_raw": Decimal(0)})
        self.assertEqual(province.values["famine_food_stage"], Decimal(1))
        self.assertEqual(province.values["famine_food_recovery_since_date"], now)


if __name__ == "__main__":
    unittest.main(verbosity=2)
