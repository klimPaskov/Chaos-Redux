"""Check the actual near-miss award branch and shared settings predicates.

This is a limited source model, not native HOI4 or probability evidence.
The external shared country classifier is an explicit scenario input.
"""
import copy
import hashlib
import re
import subprocess
from pathlib import Path

from validate_028_availability import parse_source

ROOT = Path(__file__).resolve().parents[2]
BEFORE_COMMIT = "829f4db894d90a08570e5483377189ca51638771"
RUNTIME = "common/scripted_effects/028_asteroid_incoming_runtime_effects.txt"
AWARD = "asteroid_incoming_achievement_near_miss"


class TextSource:
    def __init__(self, text):
        self.text = text

    def read_text(self, encoding):
        return self.text


def tier_constants_source():
    # Other categories use enum/list schema not interpreted by this model.
    # Read only the actual balanced category consumed by the shared predicate.
    text = (ROOT / "common/script_constants/chaos_meter_constants.txt").read_text(encoding="utf-8-sig")
    text = re.sub(r"#[^\n]*", "", text)
    match = re.search(r"(?m)^chaos_meter_tier_range\s*=\s*\{", text)
    assert match
    depth = 1
    for index in range(match.end(), len(text)):
        depth += (text[index] == "{") - (text[index] == "}")
        if depth == 0:
            category = text[match.start():index + 1]
            leaves = re.findall(r"\btier_(?:\d+|final)\s*=\s*\{[^{}]*\}", category)
            assert leaves
            # Native schema contains an anonymous list, outside this model.
            return TextSource("chaos_meter_tier_range = { " + " ".join(leaves) + " }")
    raise AssertionError("Unclosed tier range category")


class Model:
    def __init__(self, fixture):
        self.fixture = copy.deepcopy(fixture)
        self.temp = {}
        self.country_flags = set(fixture.get("country_flags", []))
        self.global_flags = set(fixture.get("global_flags", []))
        self.defs = parse_source(ROOT / "common/scripted_triggers/chaosx_settings_triggers.txt")
        self.defs.update(parse_source(ROOT / "common/scripted_triggers/028_asteroid_incoming_achievement_triggers.txt"))
        self.constants = parse_source(ROOT / "common/script_constants/028_asteroid_incoming_constants.txt")
        self.constants.update(parse_source(tier_constants_source()))

    def value(self, token):
        if token.startswith("constant:"):
            result = self.constants
            for part in token[9:].split("."):
                result = dict((key, value) for key, _, value in result)[part] if isinstance(result, list) else result[part]
            return float(result)
        if token == "global.chaos_meter_value":
            return self.fixture["chaos"]
        try:
            return float(token)
        except ValueError:
            assert token in self.temp, ("unknown variable", token)
            return self.temp[token]

    def trigger(self, rows):
        def node(key, op, val):
            if key in ("hidden_trigger", "AND"):
                return self.trigger(val)
            if key == "OR":
                return any(node(*row) for row in val)
            if key == "NOT":
                return not any(node(*row) for row in val)
            if key in self.defs:
                return self.trigger(self.defs[key]) == (val == "yes")
            if key == "meta_trigger":
                body = next(value for name, _, value in val if name == "text")
                args = {}
                for name, _, value in val:
                    if name == "text":
                        continue
                    match = re.fullmatch(r'"\[\?([^|]+)\|0\]"', value)
                    assert match, (name, value)
                    args[name] = str(int(self.value(match[1])))

                def expand(value):
                    if isinstance(value, list):
                        return [(name, op, expand(item)) for name, op, item in value]
                    for name, argument in args.items():
                        value = value.replace("[" + name + "]", argument)
                    return value

                return self.trigger(expand(body))
            if key in ("has_global_flag", "has_country_flag"):
                flag = dict((name, value) for name, _, value in val)["flag"] if isinstance(val, list) else val
                return flag in (self.global_flags if key == "has_global_flag" else self.country_flags)
            if key == "has_variable":
                return val in self.temp
            if key == "check_variable":
                terms = dict((name, value) for name, _, value in val)
                left, right = self.value(terms["var"]), self.value(terms["value"])
                compare = terms.get("compare", "greater_than_or_equals")
                return {"equals": left == right, "less_than": left < right,
                        "greater_than_or_equals": left >= right}[compare]
            if key in ("exists", "is_ai", "is_debug", "is_special_chaos_country"):
                return self.fixture.get(key, key == "exists") == (val == "yes")
            raise AssertionError(("unknown evaluated trigger", key, op, val))

        return all(node(*row) for row in rows)

    def execute(self, rows):
        for key, _, val in rows:
            if key == "set_temp_variable":
                name, _, value = val[0]
                self.temp[name] = self.value(value)
            elif key == "set_country_flag":
                assert val == AWARD
                self.country_flags.add(val)
            elif key == "if":
                limit = next(value for name, _, value in val if name == "limit")
                if self.trigger(limit):
                    self.execute([row for row in val if row[0] != "limit"])
            else:
                raise AssertionError(("unknown evaluated effect", key, val))


def has_award(rows):
    return any((key == "set_country_flag" and value == AWARD) or
               (isinstance(value, list) and has_award(value)) for key, _, value in rows)


def award_branch(source):
    body = parse_source(source)["asteroid_incoming_resolve_miss"]
    selected = []
    for row in body:
        if row[0] == "set_temp_variable":
            selected.append(row)
        if row[0] == "if" and has_award(row[2]):
            selected.append(row)
            return selected
    raise AssertionError("Near-miss award branch absent")


before_bytes = subprocess.check_output(["git", "show", BEFORE_COMMIT + ":" + RUNTIME], cwd=ROOT)
before = award_branch(TextSource(before_bytes.decode("utf-8-sig")))
after = award_branch(ROOT / RUNTIME)


def without_award(body):
    return [row for row in body if not (row[0] == "if" and has_award(row[2])) and
            not (row[0] == "set_temp_variable" and row[2][0][0].startswith("events_log_evolution_"))]


before_body = parse_source(TextSource(before_bytes.decode("utf-8-sig")))["asteroid_incoming_resolve_miss"]
after_body = parse_source(ROOT / RUNTIME)["asteroid_incoming_resolve_miss"]
assert without_award(before_body) == without_award(after_body), "Non-award miss path changed"
preview = ["asteroid_incoming_evolution_i_eligible", "asteroid_incoming_evolution_ii_eligible"]
cases = [
    ("AST_MISS_ENABLED_800", {}, True, True),
    ("AST_MISS_FRAGMENTATION_DISABLED_AFTER_OPENING", {"extra_flags": ["events_log_disabled_evolution_28_2801_1"]}, False, True),
    ("AST_MISS_MINERALS_DISABLED_AFTER_OPENING", {"extra_flags": ["events_log_disabled_evolution_28_2802_1"]}, False, True),
    ("AST_MISS_BOTH_DISABLED_AFTER_OPENING", {"extra_flags": ["events_log_disabled_evolution_28_2801_1", "events_log_disabled_evolution_28_2802_1"]}, False, True),
    ("AST_MISS_MISSING_FRAGMENTATION_PREVIEW", {"global_flags": preview[1:]}, False, False),
    ("AST_MISS_MISSING_MINERALS_PREVIEW", {"global_flags": preview[:1]}, False, False),
    ("AST_MISS_CHAOS_799", {"chaos": 799}, False, False),
    ("AST_MISS_PRIOR_IMPACT", {"extra_flags": ["asteroid_incoming_impact_recorded"]}, False, False),
    ("AST_MISS_DUST_PRESENT", {"extra_flags": ["asteroid_incoming_dust_stage_veil"]}, False, False),
    ("AST_MISS_CRATER_PRESENT", {"extra_flags": ["asteroid_incoming_main_crater_registered"]}, False, False),
    ("AST_MISS_DEBUG", {"is_debug": True}, False, False),
    ("AST_MISS_MANUAL", {"extra_flags": ["asteroid_incoming_achievement_manual_disqualified"]}, False, False),
    ("AST_MISS_FORCE_TRIGGER", {"country_flags": ["force_trigger_mode_enabled"]}, False, False),
    ("AST_MISS_NONHUMAN", {"is_special_chaos_country": True}, False, False),
    ("AST_MISS_AI", {"is_ai": True}, False, False),
    ("AST_MISS_ENABLED_900", {"chaos": 900}, True, True),
]
for name, changes, expected, old_expected in cases:
    fixture = dict(chaos=800, global_flags=preview)
    fixture.update(changes)
    fixture["global_flags"] = fixture["global_flags"] + changes.get("extra_flags", [])
    old, current = Model(fixture), Model(fixture)
    old.execute(before)
    current.execute(after)
    assert (AWARD in old.country_flags) == old_expected, (name, "before")
    assert (AWARD in current.country_flags) == expected, (name, "after")
    assert current.global_flags == set(fixture["global_flags"]), name
    print(f"{name}: before={old_expected}, after={expected}")
print(f"{len(cases)} actual-source award scenarios passed. Native settings and achievement acceptance remain unverified.")
print("AST_MISS_NO_AFTERMATH_CHANGE: non-award miss operations match the before source exactly.")
print("Before commit runtime SHA256:", hashlib.sha256(before_bytes).hexdigest())
