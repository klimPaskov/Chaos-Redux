"""Narrow R1 source receipts, adapted from the session R3 subset evaluator.
Supplies native primitives; does not claim a native VM or score/balance result.
Run from the Chaos Redux root. Writes only case_receipt.json beside this file.
"""
from pathlib import Path
from copy import deepcopy
import hashlib
import json
import re

ROOT = Path.cwd()
OUT = Path(__file__).parent


def read(path):
    return (ROOT / path).read_bytes().decode("utf-8-sig")


def parse(source):
    tokens = [m.group() for m in re.finditer(r'"(?:\\.|[^"\\])*"|#[^\r\n]*|[^\s{}=<>]+|[{}=<>]', source) if not m.group().startswith("#")]
    cursor = 0

    def block():
        nonlocal cursor
        result = []
        while cursor < len(tokens) and tokens[cursor] != "}":
            key = tokens[cursor]
            cursor += 1
            if cursor >= len(tokens) or tokens[cursor] not in ["=", ">", "<"]:
                result.append((key, "", None))
                continue
            operator = tokens[cursor]
            cursor += 1
            if tokens[cursor] == "{":
                cursor += 1
                value = block()
                cursor += 1
            else:
                value = tokens[cursor]
                cursor += 1
            result.append((key, operator, value))
        return result

    return block()


def extract(source, name):
    match = re.search(r"^" + re.escape(name) + r"\s*=\s*\{", source, re.M)
    assert match, name
    start, depth = match.end(), 1
    for token in re.finditer(r'"(?:\\.|[^"\\])*"|#[^\r\n]*|[{}]', source[start:]):
        if token.group() == "{":
            depth += 1
        elif token.group() == "}":
            depth -= 1
        if not depth:
            return parse(source[start:start + token.start()])
    raise AssertionError(name)


def vals(body, key):
    return [value for name, op, value in body if name == key]


TR = {}
for path, names in [
    ("common/scripted_triggers/006_independence_wave_diplomatic_target_triggers.txt", ["is_independence_wave_current_diplomatic_target"]),
    ("common/scripted_triggers/006_independence_wave_triggers.txt", ["is_independence_wave_active_country", "has_independence_wave_force_package_for_current_generation", "independence_wave_active_country_arrays_are_aligned"]),
    ("common/scripted_triggers/006_independence_wave_package_triggers.txt", ["is_independence_wave_registry_event6_owned_tag"]),
]:
    for name in names:
        TR[name] = extract(read(path), name)

FX = {name: extract(read("common/scripted_effects/006_independence_wave_effects.txt"), name) for name in ["independence_wave_register_active_country", "independence_wave_reconcile_active_registry"]}
CONSTANTS = {}
for path, categories in [
    ("common/script_constants/006_independence_wave_constants_registry.txt", ["independence_wave_value", "independence_wave_plan", "independence_wave_formable_tuning"]),
    ("common/script_constants/chaosx_liberation_release_constants.txt", ["liberation_origin"]),
]:
    for category in categories:
        for key, op, value in extract(read(path), category):
            if isinstance(value, str):
                try:
                    CONSTANTS["constant:" + category + "." + key] = int(value)
                except ValueError:
                    pass

# Numeric tag values are explicit native-getter surrogates, not engine IDs.
TAG_IDS = {"AFX": 501, "AGX": 502, "SOV": 503, "CHU": 504}
IDS = {"D01": 1001, "D02": 1002, "ACTOR": 1003, "SOV": 1004}
G = "independence_wave_generation_id"
P = "independence_wave_package_id"
RP = "independence_wave_registered_package_id"
RO = "independence_wave_registered_original_tag"
RG = "independence_wave_registered_generation_id"
COUNTRIES = "independence_wave_active_countries"
GENERATIONS = "independence_wave_active_country_generation_entries"


class VM:
    def __init__(self, world, current=1001, root=1003):
        self.world, self.root, self.stack = world, root, [root, current]
        self.temp, self.targets, self.writes = {}, {}, []

    def obj(self):
        return self.world["countries"].get(self.stack[-1], self.world["states"].get(self.stack[-1], {"exists": False, "vars": {}, "flags": [], "original": "NONE", "dynamic": False}))

    def array(self, name):
        assert name.startswith("global."), name
        return self.world["arrays"].get(name[7:], [])

    def value(self, token):
        if token in CONSTANTS:
            return CONSTANTS[token]
        if token == "THIS":
            return self.stack[-1]
        if token == "ROOT":
            return self.root
        if token == "PREV":
            return self.stack[-2]
        if token == "original_tag":
            return TAG_IDS[self.obj()["original"]]
        if token.startswith("event_target:"):
            return self.targets.get(token[13:], 0)
        if "^" in token:
            name, index = token.split("^", 1)
            array = self.array(name)
            if index == "num":
                return len(array)
            index = int(self.value(index))
            return array[index] if 0 <= index < len(array) else 0
        try:
            return int(token)
        except ValueError:
            return self.temp.get(token, self.obj()["vars"].get(token, 0))

    def scope(self, identity, body, effect=False):
        self.stack.append(int(identity))
        try:
            return self.effects(body) if effect else self.test(body)
        finally:
            self.stack.pop()

    def call(self, name, effect=False):
        owned = set(self.temp)
        result = self.effects(FX[name]) if effect else self.test(TR[name])
        self.temp = {key: value for key, value in self.temp.items() if key in owned}
        return result

    def test(self, body):
        for key, op, value in body:
            if key == "set_temp_variable":
                self.temp[value[0][0]] = self.value(value[0][2])
                continue
            if key in TR:
                result = self.call(key)
            elif key in ["AND", "hidden_trigger"]:
                result = self.test(value)
            elif key == "OR":
                result = any(self.test([node]) for node in value)
            elif key == "NOT":
                result = not self.test(value)
            elif key == "exists":
                result = self.obj()["exists"] == (value == "yes")
            elif key == "is_dynamic_country":
                result = self.obj()["dynamic"] == (value == "yes")
            elif key == "original_tag":
                result = self.obj()["original"] == value
            elif key == "tag":
                result = self.stack[-1] == self.value(value)
            elif key == "has_variable":
                result = value in self.obj()["vars"]
            elif key == "has_country_flag":
                result = value in self.obj()["flags"]
            elif key == "check_variable":
                fields = {a: c for a, o, c in value}
                if "var" in fields:
                    left, right = self.value(fields["var"]), self.value(fields["value"])
                    comparison = fields.get("compare", "equals")
                else:
                    left, right = self.value(value[0][0]), self.value(value[0][2])
                    comparison = {"=": "equals", ">": "greater_than", "<": "less_than"}[value[0][1]]
                result = {"equals": left == right, "greater_than": left > right, "less_than": left < right}[comparison]
            elif key == "is_in_array":
                fields = {a: c for a, o, c in value}
                result = self.value(fields["value"]) in self.array(fields["array"])
            elif key == "any_of":
                fields = {a: c for a, o, c in value}
                result = False
                for index, entry in enumerate(list(self.array(fields["array"]))):
                    self.temp[fields["value"]], self.temp[fields["index"]] = entry, index
                    if self.test([n for n in value if n[0] not in ["array", "value", "index"]]):
                        result = True
                        break
            elif key.startswith("var:"):
                result = self.scope(self.value(key[4:]), value)
            elif key in ["is_owned_by", "is_controlled_by"]:
                result = self.obj()["owner" if key == "is_owned_by" else "controller"] == self.value(value)
            else:
                raise AssertionError(("unmodelled production trigger", key))
            if not result:
                return False
        return True

    def effects(self, body):
        for key, op, value in body:
            if key in FX:
                self.call(key, effect=True)
            elif key == "if":
                if self.test(vals(value, "limit")[0]):
                    self.effects([n for n in value if n[0] != "limit"])
            elif key == "while_loop_effect":
                count = 0
                while self.test(vals(value, "limit")[0]):
                    assert count < 1000, "native loop ceiling"
                    self.effects([n for n in value if n[0] != "limit"])
                    count += 1
            elif key in ["set_temp_variable", "add_to_temp_variable", "subtract_from_temp_variable"]:
                name, token = value[0][0], value[0][2]
                number = self.value(token)
                self.temp[name] = number if key == "set_temp_variable" else self.temp.get(name, 0) + (number if key == "add_to_temp_variable" else -number)
            elif key == "set_variable":
                name, token = value[0][0], value[0][2]
                store = self.world["vars"] if name.startswith("global.") else self.obj()["vars"]
                name = name[7:] if name.startswith("global.") else name
                store[name] = self.value(token)
                self.writes.append((self.stack[-1], name, store[name]))
            elif key == "save_event_target_as":
                self.targets[value] = self.stack[-1]
            elif key.startswith("var:"):
                self.scope(self.value(key[4:]), value, effect=True)
            elif key in ["add_to_array", "remove_from_array"]:
                fields = {a: c for a, o, c in value}
                array = self.array(fields["array"])
                if key == "add_to_array":
                    array.append(self.value(fields["value"]))
                else:
                    array.pop(int(self.value(fields["index"])))
            else:
                raise AssertionError(("unmodelled production effect", key))


def country(original, dynamic=False, generation=101, package=6):
    return {"exists": True, "original": original, "dynamic": dynamic, "flags": ["independence_wave_active_origin", "independence_wave_package_setup_complete"], "vars": {G: generation, P: package, "independence_wave_anchor_state": 34, "liberation_origin": CONSTANTS["constant:liberation_origin.independence_wave"], "independence_wave_force_package_generation_id": generation, RP: package, RO: TAG_IDS[original], RG: generation}}


def fixture():
    return {"countries": {1001: country("AFX", True), 1002: country("AFX", True, 102), 1003: country("CHU", False, 999, 43), 1004: country("SOV")}, "states": {34: {"owner": 1001, "controller": 1001, "vars": {}, "flags": []}}, "arrays": {COUNTRIES: [1001], GENERATIONS: [101]}, "vars": {}}


receipts = []


def target_case(name, modify=None, current=1001, expected=True):
    world = fixture()
    if modify:
        modify(world)
    before = deepcopy(world)
    vm = VM(world, current)
    result = vm.call("is_independence_wave_current_diplomatic_target")
    assert world == before, "trigger persistent mutation"
    assert not vm.temp, "callee private temporary escaped"
    assert result == expected, (name, result)
    receipts.append({"case": name, "input": before, "current": current, "root": 1003, "result": result})


target_case("legal_D01_AFX_root_actor_generation_differs")
target_case("missing_registration", lambda w: (w["arrays"][COUNTRIES].clear(), w["arrays"][GENERATIONS].clear()), expected=False)
target_case("wrong_generation_row", lambda w: w["arrays"][GENERATIONS].__setitem__(0, 100), expected=False)
target_case("D02_same_original_same_generation_is_not_D01_row", lambda w: (w["countries"][1002]["vars"].update({G: 101, RG: 101, "independence_wave_force_package_generation_id": 101}), w["states"][34].__setitem__("owner", 1002), w["states"][34].__setitem__("controller", 1002)), current=1002, expected=False)
target_case("missing_package_receipt", lambda w: w["countries"][1001]["vars"].pop(RP), expected=False)
target_case("missing_original_receipt", lambda w: w["countries"][1001]["vars"].pop(RO), expected=False)
target_case("missing_generation_receipt", lambda w: w["countries"][1001]["vars"].pop(RG), expected=False)
target_case("wrong_package_receipt", lambda w: w["countries"][1001]["vars"].__setitem__(RP, 7), expected=False)
target_case("wrong_original_receipt", lambda w: w["countries"][1001]["vars"].__setitem__(RO, TAG_IDS["AGX"]), expected=False)
target_case("wrong_birth_generation_receipt", lambda w: w["countries"][1001]["vars"].__setitem__(RG, 100), expected=False)
target_case("stale_force_generation", lambda w: w["countries"][1001]["vars"].__setitem__("independence_wave_force_package_generation_id", 100), expected=False)
target_case("lost_anchor_control", lambda w: w["states"][34].__setitem__("controller", 1003), expected=False)
target_case("event021_dynamic_origin", lambda w: w["countries"][1001]["vars"].__setitem__("liberation_origin", CONSTANTS["constant:liberation_origin.none"]), expected=False)
target_case("same_original_civil_war_not_event6", lambda w: w["countries"][1001]["flags"].remove("independence_wave_active_origin"), expected=False)
target_case("ordinary_static_SOV_no_registry_required", lambda w: (w["countries"][1004]["flags"].clear(), w["countries"][1004]["vars"].clear()), current=1004)
target_case("invalid_static_custom_AFX", lambda w: (w["countries"][1001].__setitem__("dynamic", False), w["countries"][1001]["flags"].clear()), expected=False)

world = fixture()
world["arrays"][COUNTRIES].clear()
world["arrays"][GENERATIONS].clear()
world["countries"][1001]["vars"].pop(RP)
world["countries"][1001]["vars"].pop(RO)
world["countries"][1001]["vars"].pop(RG)
before = deepcopy(world)
vm = VM(world)
vm.call("independence_wave_register_active_country", effect=True)
assert world["arrays"][COUNTRIES] == [1001] and world["arrays"][GENERATIONS] == [101]
assert world["countries"][1001]["vars"][RP] == 6 and world["countries"][1001]["vars"][RO] == TAG_IDS["AFX"] and world["countries"][1001]["vars"][RG] == 101
receipts.append({"case": "first_publication_all_three_receipts_missing", "input": before, "result": deepcopy(world), "snapshot_writes": deepcopy(vm.writes)})
world["countries"][1001]["vars"][P] = 7
before = deepcopy(world)
vm.writes.clear()
vm.call("independence_wave_register_active_country", effect=True)
assert world["countries"][1001]["vars"][RP] == 6 and world["countries"][1001]["vars"][RG] == 101 and not any(name in [RP, RO, RG] for _, name, _ in vm.writes)
receipts.append({"case": "repeated_present_registration_cannot_restamp", "input": before, "result": deepcopy(world), "snapshot_writes": deepcopy(vm.writes)})

# Same-generation repair after loss of a cache row is the narrow risk probe.
world["arrays"][COUNTRIES].clear()
world["arrays"][GENERATIONS].clear()
before = deepcopy(world)
vm.writes.clear()
vm.call("independence_wave_register_active_country", effect=True)
restamped = world["countries"][1001]["vars"][RP] == 7
accepted = vm.call("is_independence_wave_current_diplomatic_target")
assert not restamped and not accepted and world["countries"][1001]["vars"][RG] == 101
assert not any(name in [RP, RO, RG] for _, name, _ in vm.writes)
receipts.append({"case": "same_generation_missing_row_changed_package_rejected", "input": before, "result": deepcopy(world), "snapshot_writes": deepcopy(vm.writes), "restamped": restamped, "target_result_after": accepted})


def registration_case(name, modify, expected_target, expected_tuple, expect_snapshot_writes=False):
    world = fixture()
    modify(world)
    before = deepcopy(world)
    vm = VM(world)
    vm.call("independence_wave_register_active_country", effect=True)
    target = vm.call("is_independence_wave_current_diplomatic_target")
    observed_tuple = [world["countries"][1001]["vars"].get(key) for key in [RP, RO, RG]]
    stamp_writes = [entry for entry in vm.writes if entry[1] in [RP, RO, RG]]
    assert target == expected_target and observed_tuple == expected_tuple, (name, target, observed_tuple)
    assert bool(stamp_writes) == expect_snapshot_writes, (name, stamp_writes)
    receipts.append({"case": name, "input": before, "result": deepcopy(world), "target_result_after": target, "observed_tuple": observed_tuple, "snapshot_writes": stamp_writes})


def drop_row(world):
    world["arrays"][COUNTRIES].clear()
    world["arrays"][GENERATIONS].clear()


registration_case("valid_same_generation_missing_row_repair", drop_row, True, [6, TAG_IDS["AFX"], 101])
registration_case("valid_same_generation_stale_cache_row_repair", lambda w: w["arrays"][GENERATIONS].__setitem__(0, 100), True, [6, TAG_IDS["AFX"], 101])


def renew(world):
    # A new-generation AGX/7 identity fixture; no native original-tag mutation is implied.
    actor = world["countries"][1001]
    actor["original"] = "AGX"
    actor["vars"].update({G: 102, P: 7, "independence_wave_force_package_generation_id": 102, "independence_wave_anchor_state": 36})
    world["states"][36] = {"owner": 1001, "controller": 1001, "vars": {}, "flags": []}


registration_case("genuinely_new_generation_captures_tuple", renew, True, [7, TAG_IDS["AGX"], 102], True)
registration_case("older_generation_does_not_restamp", lambda w: (drop_row(w), w["countries"][1001]["vars"].update({G: 100, P: 7, "independence_wave_force_package_generation_id": 100})), False, [6, TAG_IDS["AFX"], 101])
registration_case("partial_missing_package_same_generation_fails_closed", lambda w: (drop_row(w), w["countries"][1001]["vars"].pop(RP)), False, [None, TAG_IDS["AFX"], 101])
registration_case("partial_missing_original_same_generation_fails_closed", lambda w: (drop_row(w), w["countries"][1001]["vars"].pop(RO)), False, [6, None, 101])
registration_case("partial_missing_generation_same_generation_fails_closed", lambda w: (drop_row(w), w["countries"][1001]["vars"].pop(RG)), False, [6, TAG_IDS["AFX"], None])

files = ["common/scripted_triggers/006_independence_wave_diplomatic_target_triggers.txt", "common/scripted_effects/006_independence_wave_effects.txt", "common/decisions/006_independence_wave_iw043_iw058_decisions.txt"]
receipt = {"model": "actual-source subset; native primitives supplied; original-tag scalar IDs are surrogate fixture values, not native IDs", "source_hashes": {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in files}, "cases": receipts, "definite_registration_risk": restamped, "target_accepted_after_restamp": accepted, "third_receipt_epoch_guard_passed": True}
(OUT / "case_receipt.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"cases": len(receipts), "definite_registration_risk": restamped, "target_accepted_after_restamp": accepted, "receipt": str(OUT / "case_receipt.json")}, indent=2))
