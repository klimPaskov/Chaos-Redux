"""Read-only F03 source-contract check for declared finite worlds.

This is a source subset evaluator, not native HOI4 or MCP probability evidence.
It writes no files and rejects every evaluated token without an explicit model.
"""
import argparse
import copy
import hashlib
import json
import runpy
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[5]
HERE = Path(__file__).resolve().parent
parse = runpy.run_path(str(ROOT / ".tools/validation/validate_028_availability.py"))["parse_source"]
BEFORE = ROOT / "docs/plans/028_asteroid_incoming_plans/fragment_eligibility_20261004/before/028_asteroid_incoming_triggers.txt"
BEFORE_SHARED = BEFORE.parent / "chaosx_dynamic_triggers.txt"
AFTER = ROOT / "common/scripted_triggers/028_asteroid_incoming_triggers.txt"
SHARED = ROOT / "common/scripted_triggers/chaosx_dynamic_triggers.txt"
RUNTIME = ROOT / "common/scripted_effects/028_asteroid_incoming_runtime_effects.txt"
CONSTANTS = ROOT / "common/script_constants/028_asteroid_incoming_constants.txt"
SITE = "asteroid_incoming_state_is_valid_fragment_site"
HOST = "asteroid_incoming_country_can_host_fragment_center"
NEIGHBOR = "asteroid_incoming_fragment_site_has_valid_land_neighbor"
SELECT = "asteroid_incoming_state_is_valid_fragment_selection"
RING = "asteroid_incoming_state_is_valid_ring_candidate"
PREF = "asteroid_incoming_fragment_neighbor_pool_available"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def ast_sha(body):
    return hashlib.sha256(json.dumps(body, separators=(",", ":")).encode()).hexdigest()


def contract():
    before, after = parse(BEFORE), parse(AFTER)
    assert sha(BEFORE) == "D591180EDE589C319D6077028736EDAFC184DECB86F62E2D48BFEC3F8AF81A4B"
    assert sha(BEFORE_SHARED) == sha(SHARED) == "4BC09B54327C90AE73C6ED90446093658BD1E941071AD97ECF7499EC66389FDE"
    added = sorted(set(after) - set(before))
    removed = sorted(set(before) - set(after))
    changed = sorted(k for k in before if k in after and before[k] != after[k])
    assert added == [HOST] and not removed and changed == [SITE], (added, removed, changed)
    assert after[HOST] == [("hidden_trigger", "=", [
        ("exists", "=", "yes"), ("uses_normal_civilian_systems", "=", "yes"),
        ("NOT", "=", [("tag", "=", "CXT")])])]
    before_site = before[SITE][0][2]
    after_site = after[SITE][0][2]
    owner_call = ("OWNER", "=", [(HOST, "=", "yes")])
    controller_call = ("CONTROLLER", "=", [(HOST, "=", "yes")])
    at = after_site.index(("asteroid_incoming_state_is_valid_target", "=", "yes"))
    assert after_site[at + 1:at + 3] == [owner_call, controller_call]
    assert after_site[:at + 1] + after_site[at + 3:] == before_site
    constants = parse(CONSTANTS)
    values = {group: dict((k, v) for k, _, v in constants[group]) for group in
              ("asteroid_incoming_target", "asteroid_incoming_runtime")}
    return {
        "sources": {str(p.relative_to(ROOT)): sha(p) for p in
                    (BEFORE, BEFORE_SHARED, AFTER, SHARED, RUNTIME, CONSTANTS)},
        "added": added, "removed": removed, "changed": changed,
        "unchangedTriggerCount": len(before) - 1,
        "unchangedScopeHashes": {k: ast_sha(before[k]) for k in
                                 ("asteroid_incoming_state_is_valid_target", NEIGHBOR, SELECT, RING,
                                  "asteroid_incoming_fragmentation_is_enabled",
                                  "asteroid_incoming_ai_chooser_holds_mineral_advantage")},
        "constants": {
            "minimum_population_k": float(values["asteroid_incoming_target"]["minimum_population_k"]),
            "minimum_building_level": float(values["asteroid_incoming_target"]["minimum_building_level"]),
            "minimum_strategic_value": float(values["asteroid_incoming_target"]["minimum_strategic_value"]),
            "maximum_fragment_sites": float(values["asteroid_incoming_runtime"]["maximum_fragment_sites"])
        }
    }


class Model:
    def __init__(self, world, after):
        self.world = copy.deepcopy(world)
        self.defs = parse(AFTER if after else BEFORE)
        self.defs.update(parse(SHARED if after else BEFORE_SHARED))
        self.constants = parse(CONSTANTS)
        self.countries = {x["id"]: x for x in self.world["countries"]}
        self.states = {x["id"]: x for x in self.world["states"]}
        self.root = self.countries[self.world["actor"]]
        self.flags = set(self.world["globalFlags"])

    def value(self, token, obj, stack):
        if token == "THIS": return obj["id"]
        if token == "ROOT": return self.root["id"]
        if token == "PREV": return stack[-2]["id"]
        if token.startswith("constant:"):
            category, key = token[9:].split(".")
            return float(dict((k, v) for k, _, v in self.constants[category])[key])
        if token.startswith("global."):
            return self.world["globalVariables"][token[7:]]
        if token.startswith("event_target:"):
            return self.world["eventTargets"][token[13:]]
        try: return float(token)
        except ValueError: return token

    def trigger(self, name, obj):
        return self.test(self.defs[name], [self.root, obj])

    def test(self, rows, stack):
        obj = stack[-1]
        def node(key, op, val):
            if key in ("hidden_trigger", "AND"): return self.test(val, stack)
            if key == "OR": return any(node(*r) for r in val)
            if key == "NOT": return not self.test(val, stack)
            if key in self.defs and not key.startswith("@"):
                return self.test(self.defs[key], stack) == (val == "yes")
            if key in ("OWNER", "CONTROLLER"):
                return self.test(val, stack + [self.countries[obj[key.lower()]]])
            if key == "any_neighbor_state":
                return any(self.test(val, stack + [self.states[x]]) for x in obj["neighbors"])
            if key == "any_state":
                return any(self.test(val, stack + [s]) for s in self.states.values())
            if key in ("exists", "scope_exists"):
                return obj["exists"] == (val == "yes")
            if key in ("tag", "original_tag", "has_cosmetic_tag"):
                actual = obj["id"] if key == "tag" else obj.get("originalTag" if key == "original_tag" else "cosmeticTag", "")
                return actual == self.value(val, obj, stack)
            if key in ("has_country_flag", "has_state_flag"):
                return val in obj["flags"]
            if key == "has_global_flag": return val in self.flags
            if key == "has_state_category": return obj["category"] == val
            if key == "impassable": return obj["impassable"] == (val == "yes")
            if key == "check_variable":
                t = dict((k, v) for k, _, v in val)
                left, right = self.value(t["var"], obj, stack), self.value(t["value"], obj, stack)
                compare = t.get("compare", "greater_than_or_equals")
                return {"equals": left == right, "less_than": left < right,
                        "greater_than_or_equals": left >= right}[compare]
            if key == "is_in_array":
                t = dict((k, v) for k, _, v in val)
                return self.value(t["value"], obj, stack) in self.value(t["array"], obj, stack)
            if key == "is_on_same_continent_as":
                other = self.states[self.value(val, obj, stack)]
                return obj["continent"] == other["continent"]
            numeric = ("state_population_k", "industrial_complex", "arms_factory", "dockyard",
                       "infrastructure", "rail_way", "supply_node", "air_base", "naval_base", "state_strategic_value")
            if key in numeric:
                left, right = obj[key], self.value(val, obj, stack)
                return left > right if op == ">" else left < right if op == "<" else left == right
            if key in obj.get("externalPredicates", {}):
                return obj["externalPredicates"][key] == (val == "yes")
            raise AssertionError(("unmodeled evaluated token", key, op, val))
        return all(node(*row) for row in rows)

    def selection_pool(self):
        site = {sid: self.trigger(SITE, s) for sid, s in self.states.items()}
        neighbor = {sid: self.trigger(NEIGHBOR, s) for sid, s in self.states.items()}
        pref = any(site[sid] and neighbor[sid] for sid in self.states)
        self.flags.add(PREF) if pref else self.flags.discard(PREF)
        selected = {sid: self.trigger(SELECT, s) for sid, s in self.states.items()}
        return site, neighbor, selected, pref

    def actual_routing_pool(self):
        runtime = parse(RUNTIME)["asteroid_incoming_choose_fragment_sites"]
        outer = next(v for k, _, v in runtime if k == "if")
        loop = next(v for k, _, v in outer if k == "while_loop_effect")
        branches = [(k, v) for k, _, v in loop if k in ("if", "else_if", "else")
                    and any(child == "random_state" for child, _, _ in v)]
        assert len(branches) == 4
        for key, body in branches:
            limit = next((v for k, _, v in body if k == "limit"), [])
            if key == "else" or self.test(limit, [self.root]):
                random = next(v for k, _, v in body if k == "random_state")
                conditions = next(v for k, _, v in random if k == "limit")
                return {sid for sid, s in self.states.items() if self.test(conditions, [self.root, s])}
        raise AssertionError("No source routing branch selected")


def expression_value(expression, values):
    text = expression.replace("true", "True").replace("false", "False")
    return bool(eval(text, {"__builtins__": {}}, {"state": SimpleNamespace(**values)}))


def audit(conjunctive=False, boolean_category=False):
    receipt = contract()
    fixture = json.loads((HERE / "finite_worlds.json").read_text(encoding="utf-8"))
    suffix = "_boolean" if boolean_category else "_conjunctive" if conjunctive else ""
    scenario_name = "mcp_scenarios" + suffix + ".json"
    manifest_names = ("manifest_before" + suffix + ".json", "manifest_after" + suffix + ".json")
    scenarios = json.loads((HERE / scenario_name).read_text(encoding="utf-8"))
    manifests = [json.loads((HERE / name).read_text(encoding="utf-8")) for name in
                 manifest_names]
    by_scenario = {s["id"]: s for s in scenarios["scenarios"]}
    output = []
    for case in fixture["cases"]:
        world = case["world"]
        assert set(by_scenario[case["id"]]["state"]) == set(manifests[0]["state"])
        for s in world["states"]:
            assert s["owner"] in {c["id"] for c in world["countries"]}
            assert s["controller"] in {c["id"] for c in world["countries"]}
            assert all(s["id"] in next(t["neighbors"] for t in world["states"] if t["id"] == n) for n in s["neighbors"])
        assert world["globalVariables"]["asteroid_incoming_fragment_site_count"] == len(world["globalVariables"]["asteroid_incoming_fragment_site_states"])
        phases = []
        for after, manifest in zip((False, True), manifests):
            model = Model(world, after)
            for country in model.countries.values():
                assert model.trigger("is_actual_nonhuman_country", country) == country["declaredActualNonhuman"]
                assert model.trigger("is_special_chaos_country", country) == country["declaredSpecialChaos"]
            site, neighbors, selected, pref = model.selection_pool()
            pool = model.actual_routing_pool()
            assert pool == {sid for sid, yes in selected.items() if yes}, (case["id"], "routing projection incomplete", pool, selected)
            values = by_scenario[case["id"]]["state"]
            assert values["neighbor_pool_available"] == pref, (case["id"], "neighbor mode input")
            assert (PREF in by_scenario[case["id"]]["flags"]) == pref
            for index, (sid, s) in enumerate(model.states.items()):
                prefix = "abcde"[index]
                owner, controller = model.countries[s["owner"]], model.countries[s["controller"]]
                assert values[prefix + "_owner_exists"] == owner["exists"]
                assert values[prefix + "_controller_exists"] == controller["exists"]
                assert values[prefix + "_owner_uses_normal"] == model.trigger("uses_normal_civilian_systems", owner)
                assert values[prefix + "_controller_uses_normal"] == model.trigger("uses_normal_civilian_systems", controller)
                assert values[prefix + "_owner_is_CXT"] == (owner["id"] == "CXT")
                assert values[prefix + "_controller_is_CXT"] == (controller["id"] == "CXT")
                assert values[prefix + "_has_valid_land_neighbor"] == neighbors[sid]
                if conjunctive or boolean_category:
                    assert values[prefix + "_source_meaningful_settlement"] == model.trigger("asteroid_incoming_state_has_meaningful_settlement", s)
                    assert values[prefix + "_source_neighbor_gate"] == (not pref or neighbors[sid])
                if boolean_category:
                    assert values[prefix + "_source_is_wasteland"] == (s["category"] == "wasteland")
            for candidate in manifest["candidates"]:
                sid = candidate["id"]
                assert expression_value(candidate["eligibleWhen"], values) == selected[sid], (case["id"], after, sid)
            rings = {sid: model.trigger(RING, s) for sid, s in model.states.items()}
            phases.append({"site": site, "neighbor": neighbors, "selection": selected, "ring": rings, "neighborMode": pref})
        assert phases[0]["neighbor"] == phases[1]["neighbor"] and phases[0]["ring"] == phases[1]["ring"]
        assert phases[0]["selection"]["f03_probe"] == case["expectedProbeBefore"]
        assert phases[1]["selection"]["f03_probe"] == case["expectedProbeAfter"]
        assert phases[0]["selection"]["f03_anchor"] and phases[1]["selection"]["f03_anchor"]
        output.append({"id": case["id"], "beforePool": [k for k, yes in phases[0]["selection"].items() if yes],
                       "afterPool": [k for k, yes in phases[1]["selection"].items() if yes],
                       "neighborUnchanged": True, "ringUnchanged": True,
                       "beforeNeighborMode": phases[0]["neighborMode"], "afterNeighborMode": phases[1]["neighborMode"]})
    receipt["caseCount"] = len(output)
    receipt["cases"] = output
    receipt["fixtureHashes"] = {name: sha(HERE / name) for name in ("finite_worlds.json", scenario_name, *manifest_names)}
    receipt["serialization"] = "boolean-conjunctive-source-verified-derived-helper-inputs" if boolean_category else "conjunctive-source-verified-derived-helper-inputs" if conjunctive else "parenthesized-initial-encoding"
    receipt["evidenceKind"] = "actual-source-subset-and-declared-projection-contract-only"
    print(json.dumps(receipt, separators=(",", ":")))


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--contract", action="store_true")
    args.add_argument("--conjunctive", action="store_true")
    args.add_argument("--boolean-category", action="store_true")
    options = args.parse_args()
    if options.contract: print(json.dumps(contract(), separators=(",", ":")))
    else: audit(options.conjunctive, options.boolean_category)
