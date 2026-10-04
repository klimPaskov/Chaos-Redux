"""Execute bounded arithmetic/branch subsets from actual Event033 source.

Native scope/building facts are explicit injected fixtures, not engine evidence.
Unknown commands fail rather than silently executing an invented fallback.
No game launch, source mutation, or validator mutation.
"""
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[5]
REL = "common/scripted_effects/"
FILES = [
    REL + "033_acid_rain_effects.txt",
    REL + "033_acid_rain_aftermath_effects.txt",
    "common/script_constants/033_acid_rain_constants.txt",
    "common/scripted_triggers/033_acid_rain_triggers.txt",
    "events/033_acid_rain.txt",
]


def parse(text):
    text = re.sub(r'#[^\n]*', '', text)
    tokens = re.findall(r'"[^"]*"|[{}=<>]|[^\s{}=<>]+', text)
    pos = 0

    def block(nested=False):
        nonlocal pos
        result = []
        while pos < len(tokens):
            key = tokens[pos]
            pos += 1
            if key == '}':
                if not nested:
                    raise AssertionError("unexpected top-level closing brace at token " + str(pos))
                return result
            if tokens[pos] not in ('=', '<', '>'):
                raise AssertionError((key, tokens[pos], pos))
            op = tokens[pos]
            pos += 1
            value = tokens[pos]
            pos += 1
            if value == '{':
                value = block(True)
            result.append((key, op, value))
        if nested:
            raise AssertionError("unterminated block")
        return result
    return block()


SOURCES = {f: (ROOT / f).read_text(encoding="utf-8-sig") for f in FILES}
TREES = {f: parse(t) for f, t in SOURCES.items()}
EFFECTS = {k: v for f in FILES[:2] for k, _, v in TREES[f] if isinstance(v, list)}
CONSTANTS = {g + "." + k: Decimal(v) for g, _, b in TREES[FILES[2]]
             for k, _, v in b if k != "schema"}


class Machine:
    def __init__(self, **values):
        self.v = {k: Decimal(str(v)) for k, v in values.items()}
        self.flags = set()
        self.facts = {}
        self.mods = set()
        self.calls = []

    def value(self, token):
        if token.startswith("constant:"):
            return CONSTANTS[token[9:]]
        try:
            return Decimal(token)
        except Exception:
            return self.v.get(token, Decimal(0))

    def cond(self, body):
        results = []
        for key, op, arg in body:
            if key in ("AND", "hidden_trigger"):
                result = self.cond(arg)
            elif key == "OR":
                result = any(self.cond([n]) for n in arg)
            elif key == "NOT":
                result = not self.cond(arg)
            elif key == "check_variable":
                a = {k: v for k, _, v in arg}
                if "var" in a:
                    left, right = self.value(a["var"]), self.value(a["value"])
                    comparison = a.get("compare", "equals")
                else:
                    k, comparison, token = arg[0]
                    left, right = self.value(k), self.value(token)
                result = {"equals": left == right, "not_equals": left != right,
                          "greater_than": left > right, "less_than": left < right,
                          "greater_than_or_equals": left >= right,
                          "less_than_or_equals": left <= right,
                          ">": left > right, "<": left < right, "=": left == right}[comparison]
            elif key == "has_variable":
                result = arg in self.v
            elif key.startswith("has_") and key.endswith("_flag"):
                result = arg in self.flags
            elif key in self.facts:
                result = self.facts[key]
                if arg == "no":
                    result = not result
            elif key == "CONTROLLER":
                result = self.cond(arg)
            elif op in ("<", ">"):
                result = self.value(key) < self.value(arg) if op == "<" else self.value(key) > self.value(arg)
            else:
                raise AssertionError("unknown condition: " + key)
            results.append(result)
        return all(results)

    def run(self, name):
        self.calls.append(name)
        self.body(EFFECTS[name])

    def body(self, nodes):
        branch = False
        for key, _, arg in nodes:
            if key in ("if", "else_if", "else"):
                limit = next((v for k, _, v in arg if k == "limit"), [])
                take = (not branch or key == "if") and (key == "else" or self.cond(limit))
                if key == "if":
                    branch = False
                if take:
                    branch = True
                    self.body([n for n in arg if n[0] != "limit"])
                continue
            if key in ("set_variable", "set_temp_variable", "add_to_variable", "add_to_temp_variable",
                       "subtract_from_variable", "subtract_from_temp_variable", "multiply_variable",
                       "multiply_temp_variable", "divide_variable", "divide_temp_variable"):
                k, _, token = arg[0]
                value = self.value(token)
                old = self.v.get(k, Decimal(0))
                self.v[k] = (value if key.startswith("set_") else old + value if key.startswith("add_")
                             else old - value if key.startswith("subtract_") else old * value
                             if key.startswith("multiply_") else old / value)
            elif key in ("clamp_variable", "clamp_temp_variable"):
                a = {k: v for k, _, v in arg}
                k = a["var"]
                val = self.v.get(k, Decimal(0))
                if "min" in a:
                    val = max(val, self.value(a["min"]))
                if "max" in a:
                    val = min(val, self.value(a["max"]))
                self.v[k] = val
            elif key in ("round_variable", "round_temp_variable"):
                self.v[arg] = self.value(arg).quantize(Decimal(1), rounding=ROUND_HALF_UP)
            elif key in ("clear_variable",):
                self.v.pop(arg, None)
            elif key.startswith("set_") and key.endswith("_flag"):
                self.flags.add(arg)
            elif key.startswith("clr_") and key.endswith("_flag"):
                self.flags.discard(arg)
            elif key in ("CONTROLLER",):
                self.body(arg)
            elif key in ("add_dynamic_modifier", "remove_dynamic_modifier"):
                modifier = dict((k, v) for k, _, v in arg)["modifier"]
                self.mods.add(modifier) if key == "add_dynamic_modifier" else self.mods.discard(modifier)
            elif key in self.facts:
                # Explicit native/owner fixture with no inferred side effects.
                pass
            elif key in EFFECTS:
                self.run(key)
            else:
                raise AssertionError("unknown command: " + key)


CASES = []


def check(name, actual, expected):
    assert actual == expected, (name, actual, expected)
    CASES.append(name)


def classifier(score):
    m = Machine(**{"global.date": 100, "acid_rain_window_days": score * 12})
    # Use exposure plus damage to reach high scores without a fake score input.
    m.v["acid_rain_window_days"] = Decimal(min(score, 6) * 12)
    m.v["acid_rain_window_damage"] = Decimal(max(0, score - 6) * 4)
    m.flags.add("acid_rain_window_has_impact")
    m.facts.update(natural_disaster_state_has_open_card=False, acid_rain_state_has_proven_transport_damage=False)
    m.run("acid_rain_assess_window_aftermath")
    return m


for score, tier in [(2, 0), (3, 1), (5, 1), (6, 2), (9, 2), (10, 3)]:
    check("score_" + str(score), classifier(score).value("acid_rain_state_aftermath_tier"), tier)
m = classifier(10)
m.v["acid_rain_state_aftermath_tier"] = Decimal(2)
m.run("acid_rain_assess_window_aftermath")
check("paid_3_to_2_no_refill", m.value("acid_rain_state_aftermath_tier"), 2)
check("deadline_not_reset", m.value("acid_rain_aftercare_deadline"), 280)

m = Machine(**{"global.date": 12, "acid_rain_consequence_clock_day": 0})
m.flags.add("acid_rain_consequence_interval_active")
m.run("acid_rain_advance_consequence_interval")
m.run("acid_rain_advance_consequence_interval")
check("same_date_union_not_per_layer", m.value("acid_rain_window_days"), 12)
m.v.update({"acid_rain_window_water_tier": Decimal(4), "global.date": Decimal(24)})
m.run("acid_rain_advance_consequence_interval")
check("timeweighted_water_12_plus_12", m.value("acid_rain_window_water_days") / m.value("acid_rain_window_days"), 2)
m.facts.update(natural_disaster_state_has_open_card=False, acid_rain_state_has_proven_transport_damage=False)
m.flags.add("acid_rain_window_has_impact")
m.run("acid_rain_assess_window_aftermath")
check("water_average_credit", m.value("acid_rain_aftermath_score"), 1)
m = Machine(**{"global.date": 12, "acid_rain_window_water_until": 5})
m.flags.add("acid_rain_consequence_interval_active")
m.run("acid_rain_advance_consequence_interval")
check("emergency_water_clipped_expiry", m.value("acid_rain_window_water_days"), 5)
m = Machine(**{"global.date": 12})
m.run("acid_rain_advance_consequence_interval")
check("forecast_zero_exposure", m.value("acid_rain_window_days"), 0)


def profile(pop, applied=0, waterdays=0, water=0, capclass=1, baseline=1_000_000):
    m = Machine(**{"state_population_k": pop / 1000, "global.date": 20,
                   "acid_rain_consequence_clock_day": 20,
                   "acid_rain_ordinary_cap_population_people": baseline,
                   "acid_rain_ordinary_episode_loss": applied,
                   "acid_rain_pulse_class": capclass, "acid_rain_pulse_opening": 0,
                   "acid_rain_pulse_intensity": 1,
                   "acid_rain_window_days": waterdays, "acid_rain_water_tier": water})
    m.facts.update(natural_disaster_state_has_low_infrastructure=False,
                   natural_disaster_state_has_war_logistics=False,
                   natural_disaster_state_has_dense_population=False,
                   is_controlled_by=True, has_war=False)
    m.v["rail_way"] = Decimal(3)
    m.run("acid_rain_calculate_mortality_profile")
    return m


floor = float(CONSTANTS["acid_rain_mortality.minimum_remaining_people"])
m = profile(floor + 17, capclass=4)
# Seed actual global baseline for the profile's global/storm ledger.
m.v["acid_rain_global_cap_population_people"] = Decimal(1_000_000)
m.v["acid_rain_pulse_opening"] = Decimal(1)
m.v["acid_rain_pulse_intensity"] = Decimal("1.55")
m.run("acid_rain_calculate_mortality_profile")
check("protectedFloorPartial_request", m.value("acid_rain_pulse_applied_request"), 17)
check("protectedFloorPartial_estimate", m.value("acid_rain_unprotected_requested_people"), 17)
check("protectedFloorPartial_no_fake_prevention", m.value("acid_rain_unprotected_requested_people") - 17, 0)
check("floor_zero", profile(floor).value("acid_rain_pulse_applied_request"), 0)
check("missing_episode_baseline_fail_closed", profile(1_000_000, baseline=0).value("acid_rain_pulse_applied_request"), 0)
check("ordinary_exhausted", profile(1_000_000, applied=15000).value("acid_rain_pulse_applied_request"), 0)
check("fractional_available_floor", profile(floor + 17.9).value("acid_rain_protected_available_people"), 17)
check("water_before_12", profile(1_000_000, waterdays=11, water=4).value("acid_rain_protection"), 1)
check("water_at_12", profile(1_000_000, waterdays=12, water=4).value("acid_rain_protection"), Decimal("0.96"))

print(json.dumps({"kind": "actual-source subset execution, NOT engine/live proof", "passed": CASES,
                  "source_sha256": {f: hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in FILES}},
                 indent=2))
