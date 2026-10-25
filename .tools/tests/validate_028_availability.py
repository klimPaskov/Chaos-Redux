"""Evaluate Event 028's read-only preflight against explicit source fixtures.

This deliberately models only the trigger subset used by target availability.
Unknown evaluated tokens fail the test. It is not an HOI4 engine validator.
"""
import argparse
import json
import re
from pathlib import Path


def parse_source(path, rows=False):
    source = re.sub(r"#[^\n]*", "", path.read_text(encoding="utf-8-sig"))
    tokens = re.findall(r'"[^"\n]*"|[{}=<>]|[^\s{}=<>]+', source)
    index = 0

    def block(nested=False):
        nonlocal index
        rows = []
        while index < len(tokens) and tokens[index] != "}":
            key, op = tokens[index:index + 2]
            index += 2
            if op not in ("=", "<", ">"):
                raise AssertionError(f"Unsupported source operator {op!r} in {path}")
            value = tokens[index]
            index += 1
            if value == "{":
                value = block(True)
            rows.append((key, op, value))
        if nested:
            assert tokens[index] == "}"
            index += 1
        return rows

    parsed = block()
    return parsed if rows else dict((key, value) for key, _, value in parsed)


class TriggerModel:
    def __init__(self, root, fixture, before=False):
        suffix = "docs/plans/028_asteroid_incoming_plans/availability_20261003/before"
        trigger_path = root / suffix / "028_asteroid_incoming_triggers.txt" if before else root / "common/scripted_triggers/028_asteroid_incoming_triggers.txt"
        constant_path = root / suffix / "028_asteroid_incoming_constants.txt" if before else root / "common/script_constants/028_asteroid_incoming_constants.txt"
        self.defs = parse_source(trigger_path)
        self.constants = parse_source(constant_path)
        self.fixture = fixture
        self.countries = {c["id"]: dict(c, kind="country") for c in fixture["countries"]}
        self.states = {s["id"]: dict(s, kind="state") for c in fixture["countries"] for s in c.get("states", [])}
        self.actor = self.countries[fixture["actor"]]
        self.targets = {"asteroid_incoming_chooser": self.actor}

    def resolve(self, value, scope, prev, ancestors=()):
        if value == "PREV.PREV":
            return ancestors[0]
        if value in ("OWNER", "CONTROLLER"):
            return self.countries[scope[value.lower()]]
        if value == "PREV":
            return prev
        if value in ("ROOT", "THIS"):
            return self.actor if value == "ROOT" else scope
        if value.startswith("event_target:"):
            return self.targets.get(value.split(":", 1)[1])
        if value.startswith("@"):
            return float(self.defs[value])
        if value.startswith("constant:"):
            category, key = value[9:].split(".")
            return float(dict((k, v) for k, _, v in self.constants[category])[key])
        return value

    def evaluate(self, rows, scope, prev=None, ancestors=()):
        def node(key, op, value):
            if key in ("hidden_trigger", "AND"):
                return self.evaluate(value, scope, prev, ancestors)
            if key == "OR":
                return any(node(*row) for row in value)
            if key == "NOT":
                return not self.evaluate(value, scope, prev, ancestors)
            if key in self.defs and not key.startswith("@"):
                result = self.evaluate(self.defs[key], scope, prev, ancestors)
                return result == (value == "yes")
            if key in ("OWNER", "CONTROLLER"):
                target = self.countries.get(scope[key.lower()])
                return target is not None and self.evaluate(value, target, scope, (prev,) + ancestors)
            if key in ("any_owned_state", "any_country"):
                count = next((self.resolve(v, scope, prev, ancestors) for k, _, v in value if k == "count"), 1)
                candidates = self.countries.values() if key == "any_country" else (s for s in self.states.values() if s["owner"] == scope["id"])
                conditions = [row for row in value if row[0] != "count"]
                matches = sum(self.evaluate(conditions, candidate, scope, (prev,) + ancestors) for candidate in candidates if candidate.get("exists", True))
                return matches >= float(count)
            if key == "exists":
                return bool(scope.get("exists", True)) == (value == "yes")
            if key == "scope_exists":
                return (scope is not None) == (value == "yes")
            if key == "is_actual_nonhuman_country":
                return bool(scope.get("nonhuman", False)) == (value == "yes")
            if key == "tag":
                target = self.resolve(value, scope, prev, ancestors)
                return scope["id"] == (target["id"] if isinstance(target, dict) else target)
            if key == "is_owned_and_controlled_by":
                target = self.resolve(value, scope, prev, ancestors)["id"]
                return scope["owner"] == target and scope["controller"] == target
            if key == "is_fully_controlled_by":
                target = self.resolve(value, scope, prev, ancestors)["id"]
                return scope["controller"] == target and scope.get("fullControl", True)
            if key == "state":
                return scope["id"] == self.resolve(value, scope, prev, ancestors)["id"]
            if key == "has_event_target":
                return value in self.targets
            if key == "has_global_flag":
                return value in self.fixture.get("globalFlags", [])
            if key == "has_state_flag":
                return value in scope.get("flags", [])
            if key == "has_state_category":
                return value == scope.get("category", "town")
            if key == "impassable":
                return bool(scope.get("impassable", False)) == (value == "yes")
            if key in ("state_population_k", "industrial_complex", "arms_factory", "dockyard", "infrastructure", "rail_way", "supply_node", "air_base", "naval_base", "state_strategic_value"):
                actual = scope.get(key, 0)
                expected = float(self.resolve(value, scope, prev, ancestors))
                return actual > expected if op == ">" else actual < expected if op == "<" else actual == expected
            raise AssertionError(f"Unmodeled evaluated token: {key} {op} {value}")
        return all(node(*row) for row in rows)

    def trigger(self, name, scope=None, prev=None):
        return self.evaluate(self.defs[name], scope or self.actor, prev)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixture", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    suite = json.loads(args.fixture.read_text(encoding="utf-8"))
    base_country = {"id": "GER", "exists": True, "states": []}
    for case in suite["cases"]:
        countries = [dict(base_country, id=case.get("actor", "GER"))]
        for definition in case["targets"]:
            country = {"id": definition["id"], "exists": definition.get("exists", True), "nonhuman": definition.get("nonhuman", False), "states": []}
            for number in range(definition.get("states", 2)):
                state = {"id": f'{country["id"]}_{number}', "owner": country["id"], "controller": country["id"], "state_population_k": 10, "infrastructure": 3, "category": "town"}
                state.update(definition.get("stateOverrides", {}).get(str(number), {}))
                country["states"].append(state)
            countries.append(country)
        world = {"actor": case.get("actor", "GER"), "countries": countries, "globalFlags": case.get("globalFlags", [])}
        model = TriggerModel(root, world)
        result = model.trigger("asteroid_incoming_automatic_event_is_available")
        assert result == case["available"], (case["id"], result, case["available"])
        eligible = sum(model.trigger("asteroid_incoming_country_is_valid_target", c) for c in model.countries.values())
        assert eligible == case["eligible"], (case["id"], eligible, case["eligible"])
        before = TriggerModel(root, world, before=True)
        before_eligible = sum(before.trigger("asteroid_incoming_country_is_valid_target", c) for c in before.countries.values())
        for country, expected in case.get("centers", {}).items():
            centers = sorted(s["id"] for s in model.states.values() if s["owner"] == country and model.trigger("asteroid_incoming_state_is_valid_main_center", s, model.countries[country]))
            assert centers == sorted(expected), (case["id"], centers, expected)
        print(f'{case["id"]}: available={result}, eligible={eligible}, before_eligible={before_eligible}')
    model = TriggerModel(root, world)
    for literal, key in (("@asteroid_target_pair_count", "minimum_target_pair_count"), ("@asteroid_target_country_state_count", "target_country_minimum_usable_states")):
        assert model.resolve(literal, model.actor, None) == model.resolve(f"constant:asteroid_incoming_runtime.{key}", model.actor, None)

    events = {}
    for key, _, body in parse_source(root / "events/028_asteroid_impact.txt", rows=True):
        if key == "country_event":
            events[dict((k, v) for k, _, v in body)["id"]] = body
    entry = dict((k, v) for k, _, v in events["chaosx.nr28.1"])
    returned = dict((k, v) for k, _, v in events["chaosx.nr28.8"])
    assert entry["fire_only_once"] == "yes"
    assert "fire_only_once" not in returned
    # The reopened board only refreshes the stored board result; it must not repeat the entry setup.
    assert returned.get("immediate", []) == [("asteroid_incoming_refresh_board_ready", "=", "yes")]
    # Both boards are paginated report events (docs/systems/event_system/report_event_choice_pages.md):
    # their AI-only companion keeps the complete original option pool, so compare those pools.
    def complete_option_pool(event_id):
        options = [dict((k, v) for k, _, v in b) for k, _, b in events[event_id] if k == "option"]
        resolution = [o for o in options if o.get("name") == "chaosx_event_ai_resolution"]
        assert len(resolution) == 1, f"{event_id} has no single AI resolution route"
        companion = [v for k, _, v in resolution[0]["hidden_effect"] if k == "country_event"]
        assert len(companion) == 1
        companion_id = dict((k, v) for k, _, v in companion[0])["id"]
        return [dict((k, v) for k, _, v in b) for k, _, b in events[companion_id] if k == "option"]

    entry_options = complete_option_pool("chaosx.nr28.1")
    return_options = complete_option_pool("chaosx.nr28.8")
    assert len(entry_options) == len(return_options) == 5
    for first, again in zip(entry_options, return_options):
        assert first["ai_chance"] == again["ai_chance"]
        assert first["trigger"] == again["trigger"]
        assert first["hidden_effect"] == again["hidden_effect"]
    runtime = parse_source(root / "common/scripted_effects/028_asteroid_incoming_runtime_effects.txt")
    cancel = runtime["asteroid_incoming_cancel_selected_target"]
    assert [v for k, _, v in cancel if k == "country_event"] == [[("id", "=", "chaosx.nr28.8")]]
    assert all(k not in ("asteroid_incoming_prepare_random_event_fire", "asteroid_incoming_build_target_pool", "asteroid_incoming_clear_target_pool") for k, _, _ in cancel)
    for flags, expected in ((["asteroid_incoming_transaction_active"], True), (["asteroid_incoming_transaction_active", "asteroid_incoming_target_locked"], False), (["asteroid_incoming_transaction_active", "asteroid_incoming_transaction_resolved"], False), ([], False)):
        world["globalFlags"] = flags
        board_model = TriggerModel(root, world)
        assert board_model.evaluate(returned["trigger"], board_model.actor) == expected
        assert not board_model.evaluate(returned["trigger"], board_model.countries["FRA"])
    settings = parse_source(root / "common/scripted_effects/chaosx_settings_effects.txt")
    dispatcher = settings["fire_event_by_temp_id_no_cluster"]
    preflight_position = next(i for i, (k, _, b) in enumerate(dispatcher) if k == "if" and any(x == "asteroid_incoming_prepare_random_event_fire" for x, _, _ in b))

    def contains(rows, key, predicate=lambda value: True):
        return any((name == key and predicate(value)) or
                   (isinstance(value, list) and contains(value, key, predicate))
                   for name, _, value in rows)

    # The shared dispatcher may nest package-specific paths inside the single
    # authorized-fire branch. Inspect its actual recursive body, not one shape.
    dispatch_position = next(i for i, (k, _, b) in enumerate(dispatcher)
                             if k == "if" and contains(b, "set_temp_variable", lambda value: ("event_fire_dispatched", "=", "1") in value)
                             and contains(b, "on_major_event_fired")
                             and contains(b, "country_event", lambda value: ("id", "=", "chaosx.nr[EVENT_ID].1") in value))
    assert preflight_position < dispatch_position
    dispatch_limit = next(b for k, _, b in dispatcher[dispatch_position][2] if k == "limit")
    assert contains(dispatch_limit, "check_variable", lambda value:
                    ("event_single_fire_allowed", ">", "0") in value or
                    all(term in value for term in (("var", "=", "event_single_fire_allowed"),
                                                   ("value", "=", "0"),
                                                   ("compare", "=", "greater_than"))))
    preflight = dispatcher[preflight_position][2]
    assert "event_single_fire_allowed" in str(preflight) and "asteroid_incoming_prefire_ready" in str(preflight)
    ready_call = next(i for i, (k, _, _) in enumerate(preflight) if k == "asteroid_incoming_prepare_random_event_fire")
    ready_init = next(i for i, (k, _, b) in enumerate(preflight) if k == "set_temp_variable" and
                      ("asteroid_incoming_prefire_ready", "=", "constant:asteroid_incoming_runtime.zero") in b)
    assert ready_init < ready_call
    for output in ("events_log_history_payload_override", "events_log_history_payload_override_active"):
        output_init = next(i for i, (k, _, b) in enumerate(preflight) if k == "set_temp_variable" and
                           (output, "=", "constant:asteroid_incoming_runtime.zero") in b)
        assert output_init < ready_call
    acceptance = next(b for k, _, b in runtime["asteroid_incoming_accept_selected_target"]
                      if k == "if" and any(x == "asteroid_incoming_lock_candidate_pair" for x, _, _ in b))
    lock_call = next(i for i, (k, _, _) in enumerate(acceptance) if k == "asteroid_incoming_lock_candidate_pair")
    lock_init = next(i for i, (k, _, b) in enumerate(acceptance) if k == "set_temp_variable" and
                     ("asteroid_incoming_lock_result", "=", "constant:asteroid_incoming_runtime.zero") in b)
    assert lock_init < lock_call
    print("AST_RETURN_BOARD: five matching option bodies, unchanged weights, correct chooser/lock guards, no reroll or repeated opening effects.")
    print("AST_DISPATCH_ORDER: target readiness gate precedes event dispatch and Major fire accounting.")
    print("AST_HELPER_OUTPUT_BOUNDARIES: readiness, history override/value-active, and lock outputs are initialized by their callers before helper invocation.")
    print(f'{len(suite["cases"])} source-model cases passed; native count and engine behavior remain unverified.')


if __name__ == "__main__":
    main()
