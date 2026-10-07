"""Read-only, actual-source AI option calculation for declared Event028 fixtures.

This is an independent ideal-rational source model, not native execution or
retrieved MCP analysis payloads. Unknown evaluated predicates fail closed.
It never writes a file or changes source. --literal-tag models the documented
adapter bug for diagnostic controls only and does not endorse normalization.
"""
import argparse
import hashlib
import json
import runpy
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
parse = runpy.run_path(str(ROOT / ".tools/validation/validate_028_availability.py"))["parse_source"]
EVENT = ROOT / "events/028_asteroid_impact.txt"
TRIGGERS = ROOT / "common/scripted_triggers/028_asteroid_incoming_triggers.txt"
CONSTANTS = ROOT / "common/script_constants/028_asteroid_incoming_constants.txt"
DEFS = parse(TRIGGERS)
CONSTS = {group: dict((key, val) for key, _, val in body if key != "schema")
          for group, _, body in parse(CONSTANTS, rows=True) if isinstance(body, list)}
EVENTS = {}
for key, _, body in parse(EVENT, rows=True):
    if key == "country_event":
        EVENTS[next(v for k, _, v in body if k == "id")] = body

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()

def exact(value):
    return {"fraction": str(value), "value": float(value)}

def number(value):
    return Fraction(str(value))

def compare(left, right, op):
    if op == "=": return left == right
    if op == ">": return left > right
    if op == "<": return left < right
    raise AssertionError(("Unsupported comparison", op))

class Model:
    def __init__(self, scenario, literal_tag=False):
        self.s = scenario
        self.literal_tag = literal_tag
        self.root = {"id": scenario["actor"], "actor": scenario["actor"],
                     "type": "country", "state": scenario["state"],
                     "flags": scenario["flags"], "_expression": "ROOT"}
        self.used_helpers = set()
        self.input_paths = set()

    def scope(self, name, stack):
        current = stack[-1]
        if name == "ROOT": return self.root
        if name == "THIS": return current
        if name == "PREV": return stack[-2]
        expression = name if current["_expression"] == "ROOT" else current["_expression"] + "." + name
        if expression in self.s["scopes"]:
            return dict(self.s["scopes"][expression], _expression=expression)
        if name in self.s["scopes"]:
            return dict(self.s["scopes"][name], _expression=name)
        if name.startswith("event_target:"):
            target_id = self.s["eventTargets"][name[13:]]
            bindings = [v for v in self.s["scopes"].values() if v["id"] == target_id]
            if not bindings and target_id == self.s["actor"]: return dict(self.root, _expression=name)
            assert bindings, ("Missing event target binding", name, target_id)
            return dict(bindings[0], _expression=name)
        raise AssertionError(("Unknown scope", name, expression))

    def value(self, token, stack):
        if isinstance(token, (bool, int, float)): return token
        if token.startswith("constant:"):
            group, key = token[9:].split(".")
            return number(CONSTS[group][key])
        if token in ("ROOT", "THIS", "PREV"):
            return self.scope(token, stack)["id"]
        if token.startswith("event_target:"):
            return self.scope(token, stack)["id"]
        if token in ("yes", "no"): return token == "yes"
        try: return number(token)
        except (ValueError, ZeroDivisionError):
            if token in stack[-1]["state"]: return stack[-1]["state"][token]
            if token in self.s["state"]: return self.s["state"][token]
            return token.strip('"')

    def condition(self, rows, stack):
        return all(self.node(*row, stack) for row in rows)

    def node(self, key, op, val, stack):
        current = stack[-1]
        if isinstance(val, list):
            if key in ("hidden_trigger", "AND"): return self.condition(val, stack)
            if key == "OR": return any(self.node(*row, stack) for row in val)
            if key == "NOT": return not any(self.node(*row, stack) for row in val)
            if key == "check_variable":
                args = dict((k, v) for k, _, v in val)
                path = args["var"]
                self.input_paths.add(path)
                left = number(self.s["state"][path] if path.startswith("global.") else current["state"][path])
                right = number(self.value(args["value"], stack))
                mode = args.get("compare", "equals")
                return {"equals": left == right, "greater_than": left > right,
                        "greater_than_or_equals": left >= right,
                        "less_than": left < right, "less_than_or_equals": left <= right}[mode]
            if key == "any_neighbor_state":
                self.input_paths.add("scope.any_neighbor_state")
                assert self.s["state"]["scope.any_neighbor_state"] is False, "No complete neighbor world supplied"
                return False
            return self.condition(val, stack + [self.scope(key, stack)])
        if key in DEFS:
            self.used_helpers.add(key)
            result = self.condition(DEFS[key], stack)
            return result if val == "yes" else not result
        if key in ("has_global_flag", "has_country_flag", "has_state_flag"):
            if key == "has_global_flag":
                override = self.s["state"].get("flag." + val)
                if override is not None:
                    assert override in (0, 1, False, True)
                    return bool(override)
                return val in self.s["flags"]
            return val in current.get("flags", [])
        if key == "has_event_target": return val in self.s["eventTargets"]
        if key == "tag":
            right = val if self.literal_tag else self.value(val, stack)
            return compare(current.get("actor", current["id"]), right, op)
        assert key in current["state"], ("Unmodelled input", key, current["_expression"])
        self.input_paths.add(current["_expression"] + "." + key)
        left, right = current["state"][key], self.value(val, stack)
        if isinstance(right, bool):
            assert isinstance(left, (bool, int, float))
            return bool(left) == right
        if isinstance(right, Fraction):
            return compare(number(left), right, op)
        return compare(left, right, op)

    def scores(self, event_id):
        output = []
        for key, _, body in EVENTS[event_id]:
            if key != "option": continue
            name = next(v for k, _, v in body if k == "name")
            trigger = next((v for k, _, v in body if k == "trigger"), [])
            eligible = self.condition(trigger, [self.root])
            chance = next(v for k, _, v in body if k == "ai_chance")
            base = next(v for k, _, v in chance if k == "base")
            score = number(self.value(base, [self.root]))
            trace = []
            if eligible:
                for k, _, modifier in chance:
                    if k != "modifier": continue
                    conditions = [r for r in modifier if r[0] not in ("add", "factor", "base")]
                    matched = self.condition(conditions, [self.root])
                    operations = [(a, self.value(v, [self.root])) for a, _, v in modifier if a in ("add", "factor")]
                    before = score
                    if matched:
                        for operation, value in operations:
                            score = score + number(value) if operation == "add" else score * number(value)
                    trace.append({"matched": matched, "before": exact(before), "after": exact(score),
                                  "operations": [(a, str(v)) for a, v in operations]})
                    if matched and any(a == "factor" and number(v) == 0 for a, v in operations): break
            output.append({"id": name, "eligible": eligible, "raw": exact(score) if eligible else None, "trace": trace})
        return output

def same_board_scores():
    a = [b for k, _, b in EVENTS["chaosx.nr28.1"] if k == "option"]
    b = [b for k, _, b in EVENTS["chaosx.nr28.8"] if k == "option"]
    assert len(a) == len(b) == 5
    for first, second in zip(a, b):
        aa = [(k, op, v) for k, op, v in first if k in ("trigger", "ai_chance")]
        bb = [(k, op, v) for k, op, v in second if k in ("trigger", "ai_chance")]
        assert aa == bb
    return True

def audit(path, literal_tag=False, summary=False, compact=False):
    fixture = json.loads(path.read_text(encoding="utf-8"))
    results = []
    for scenario in fixture["scenarios"]:
        assert "candidateOverrides" not in scenario and scenario["actor"] != "ROOT"
        states = [scenario["eventTargets"]["asteroid_incoming_target_" + str(i) + "_state"] for i in (1, 2, 3)]
        countries = [scenario["eventTargets"]["asteroid_incoming_target_" + str(i) + "_country"] for i in (1, 2, 3)]
        assert len(set(states)) == len(set(countries)) == 3
        model = Model(scenario, literal_tag)
        scores = model.scores("chaosx.nr28.1")
        active = [c for c in scores if c["eligible"]]
        assert len(active) == 4 and not scores[-1]["eligible"]
        total = sum((number(c["raw"]["fraction"]) for c in active), Fraction(0))
        assert total > 0
        normalization = not scenario["id"].startswith("AST_ADAPTER_") and not literal_tag
        if normalization:
            for candidate in active:
                candidate["conditionalIdealSourceShare"] = exact(number(candidate["raw"]["fraction"]) / total)
        ordered = sorted(active, key=lambda c: -number(c["raw"]["fraction"]))
        if summary:
            for candidate in scores: candidate.pop("trace", None)
        results.append({"id": scenario["id"], "scores": scores, "rawPoolTotal": exact(total),
                        "ordering": [c["id"] for c in ordered], "normalizationPermitted": normalization,
                        "usedHelpers": sorted(model.used_helpers), "queriedInputs": [] if summary else sorted(model.input_paths),
                        "idealRatioDiagnosticOnly": float(max(number(c["raw"]["fraction"]) for c in active) / total) if not normalization else None})
    if compact:
        results = [{"id": r["id"], "raw": [c["raw"]["value"] if c["raw"] else None for c in r["scores"]],
                    "shares": [c.get("conditionalIdealSourceShare", {}).get("value") for c in r["scores"]],
                    "ordering": r["ordering"], "normalizationPermitted": r["normalizationPermitted"]} for r in results]
    print(json.dumps({"classification": "independent-actual-source-ideal-rational-model-not-native-not-MCP-payload",
                      "literalTagDiagnosticMode": literal_tag, "optionBodiesEquivalent": same_board_scores(),
                      "sources": {str(p.relative_to(ROOT)): sha(p) for p in (EVENT, TRIGGERS, CONSTANTS)},
                      "fixtureSha256": sha(path), "scenarios": results}, separators=(",", ":")))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("fixture", nargs="?", default=str(HERE / "populated_cases.json"))
    parser.add_argument("--literal-tag", action="store_true")
    parser.add_argument("--summary", action="store_true")
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()
    audit(Path(args.fixture), args.literal_tag, args.summary, args.compact)

