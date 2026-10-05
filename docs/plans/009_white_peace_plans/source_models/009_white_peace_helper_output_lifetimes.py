"""Bounded execution model for Event 009 helper-output lifetimes.

Reads the current Clausewitz helper bodies and applies the conservative helper
frame rule documented by the event skill.  It models only the candidate
counting, evolution stage, branch selection and bounded settlement loop used
by the five fixtures below.  It does not emulate HOI4 or certify engine RNG,
scope resolution, white_peace side effects, or probability values.
"""
from __future__ import annotations

from contextlib import contextmanager
from dataclasses import dataclass, field
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
import unittest


EFFECT_PATH = "common/scripted_effects/009_white_peace_effects.txt"
CONSTANT_PATH = "common/script_constants/009_white_peace_constants.txt"
ROOT = next(parent for parent in Path(__file__).resolve().parents
            if (parent / EFFECT_PATH).is_file())
TOKEN = re.compile(r'#[^\r\n]*|"[^"\r\n]*"|[{}=<>]|[^\s{}=<>]+')


def parse(text):
    tokens = [m.group() for m in TOKEN.finditer(text)
              if not m.group().startswith("#")]
    cursor = 0

    def body():
        nonlocal cursor
        result = []
        while cursor < len(tokens) and tokens[cursor] != "}":
            key = tokens[cursor]
            cursor += 1
            if key == "{":
                nested = body()
                if cursor >= len(tokens) or tokens[cursor] != "}":
                    raise AssertionError("Unclosed anonymous block")
                cursor += 1
                result.append(("_anonymous", nested))
                continue
            if cursor < len(tokens) and tokens[cursor] in ("<", ">"):
                operator = tokens[cursor]
                right = tokens[cursor + 1]
                cursor += 2
                result.append(("_comparison", (key, operator, right)))
                continue
            if cursor >= len(tokens) or tokens[cursor] != "=":
                result.append((key, None))
                continue
            cursor += 1
            if cursor < len(tokens) and tokens[cursor] == "{":
                cursor += 1
                value = body()
                if cursor >= len(tokens) or tokens[cursor] != "}":
                    raise AssertionError(f"Unclosed {key} block")
                cursor += 1
            else:
                value = tokens[cursor]
                cursor += 1
            result.append((key, value))
        return result

    parsed = body()
    if cursor != len(tokens):
        raise AssertionError("Unexpected trailing source tokens")
    return parsed


def blocks(path):
    text = (ROOT / path).read_text(encoding="utf-8-sig")
    return {key: value for key, value in parse(text)
            if isinstance(value, list)}


def number(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        try:
            return float(value)
        except (TypeError, ValueError):
            return value


EFFECTS = blocks(EFFECT_PATH)
CONSTANTS = {}
for group, data in parse((ROOT / CONSTANT_PATH).read_text(encoding="utf-8-sig")):
    if isinstance(data, list):
        CONSTANTS[group] = {
            key: number(value)
            for key, value in data
            if key != "schema" and not isinstance(value, list)
        }
FILE_CONSTANTS = {
    name: number(value)
    for name, value in re.findall(r"^@(\w+)\s*=\s*(-?\d+(?:\.\d+)?)\s*$",
                                 (ROOT / EFFECT_PATH).read_text(encoding="utf-8-sig"),
                                 re.M)
}


def child(nodes, name, default=None):
    for key, value in nodes:
        if key == name:
            return value
    return default


def without(nodes, *keys):
    excluded = set(keys)
    return [(key, value) for key, value in nodes if key not in excluded]


@dataclass(eq=False)
class Country:
    tag: str
    major: bool = False
    faction: str | None = None
    ai: bool = True
    eligible: bool = True
    exists: bool = True
    subject: bool = False
    surrendered: float = 0.0
    capital_safe: bool = True
    war_length_months: int = 8
    enemies: list["Country"] = field(default_factory=list)
    flags: set[str] = field(default_factory=set)


class DesiredBranchRng:
    """A native-random-list stub that only selects a requested positive entry."""
    def __init__(self, desired_branch):
        self.desired_branch = desired_branch
        self.draws = []

    def select(self, entries):
        for token, weight, effect in entries:
            if effect[0][0] == "set_temp_variable":
                value = dict(effect[0][1])
                if value.get("white_peace_branch", "").endswith("." + self.desired_branch) and weight > 0:
                    self.draws.append({"native": "random_list", "selected": token,
                                       "positive_weight": weight})
                    return effect
        available = [(token, weight, effect[:2]) for token, weight, effect in entries]
        raise AssertionError(f"Requested branch {self.desired_branch!r} has no positive source weight: {available}")


class WhitePeaceModel:
    """Actual Event 009 effects under conservative temp cleanup and narrow stubs."""
    def __init__(self, desired_branch=None):
        self.root = Country("OBS", eligible=False)
        self.countries: list[Country] = [self.root]
        self.scopes = [self.root]
        self.temporary = {}
        self.arrays = {}
        self.globals = {
            "default_event_weight": 1000,
            "event_max_caps": [],
            "chaos_meter_value": 100000,
        }
        self.global_flags = set()
        self.targets = {}
        self.desired_branch = desired_branch
        self.rng = DesiredBranchRng(desired_branch) if desired_branch else None
        self.applied_pairs = []
        self.native_calls = []
        self.report_notifications = []
        self.news_notifications = []

    @property
    def current(self):
        return self.scopes[-1]

    @property
    def previous(self):
        return self.scopes[-2] if len(self.scopes) > 1 else self.root

    @contextmanager
    def scope(self, country):
        self.scopes.append(country)
        try:
            yield
        finally:
            self.scopes.pop()

    def call(self, name):
        """Execute a real helper body and discard callee-created temp storage."""
        if name == "apply_white_peace_pair":
            self.apply_white_peace_pair_stub()
            return
        if name in ("apply_white_peace_pending_chaos_delta",
                    "record_white_peace_evolution_if_needed",
                    "mark_recent_white_peace_pair"):
            return
        if name not in EFFECTS:
            raise AssertionError(f"Unmodelled Event 009 helper: {name}")
        caller_temps = set(self.temporary)
        caller_arrays = set(self.arrays)
        self.execute(EFFECTS[name])
        for key in set(self.temporary) - caller_temps:
            del self.temporary[key]
        for key in set(self.arrays) - caller_arrays:
            del self.arrays[key]

    def value(self, token):
        if token is None:
            return 0
        if isinstance(token, (int, float)):
            return token
        if token in ("yes", "no"):
            return token == "yes"
        if token == "THIS":
            return self.current
        if token == "ROOT":
            return self.root
        if token == "PREV":
            return self.previous
        if token.startswith("constant:"):
            group, key = token[len("constant:"):].split(".", 1)
            return CONSTANTS[group][key]
        if token.startswith("global."):
            key = token[len("global."):]
            if key.endswith("^num"):
                return len(self.globals.get(key[:-4], []))
            if "^" in key:
                name, index = key.split("^", 1)
                values = self.globals.get(name, [])
                return values[int(self.value(index))]
            return self.globals.get(key, 0)
        if token.startswith("event_target:"):
            return self.targets.get(token[len("event_target:"):])
        if token.startswith("PREV.PREV"):
            return self.scopes[-3] if len(self.scopes) > 2 else self.root
        if token.startswith("PREV."):
            attr = token[len("PREV."):]
            return getattr(self.previous, attr, 0)
        if token.startswith("ROOT."):
            attr = token[len("ROOT."):]
            return getattr(self.root, attr, self.root.flags.__contains__(attr))
        if token.startswith("THIS."):
            attr = token[len("THIS."):]
            return getattr(self.current, attr, self.current.flags.__contains__(attr))
        if token == "surrender_progress":
            return self.current.surrendered
        if token == "num_of_controlled_states":
            return 1 if self.current.eligible else 0
        if token == "has_war":
            return bool(self.current.enemies)
        if token.startswith("@"):
            return FILE_CONSTANTS[token[1:]]
        if token in self.temporary:
            return self.temporary[token]
        try:
            return number(token)
        except Exception:
            return self.current.flags.__contains__(token)

    def check(self, nodes):
        for key, data in nodes:
            if key == "_comparison":
                left, operator, right = data
                left, right = self.value(left), self.value(right)
                if operator == "<" and not left < right: return False
                if operator == ">" and not left > right: return False
            elif key == "check_variable":
                values = dict(data)
                if "var" in values:
                    left, right = self.value(values["var"]), self.value(values["value"])
                    op = values.get("compare", "equals")
                else:
                    cmp = next((value for child_key, value in data if child_key == "_comparison"), None)
                    if cmp:
                        left, symbol, right = cmp
                        left, right = self.value(left), self.value(right)
                        op = {"<": "less_than", ">": "greater_than"}[symbol]
                    elif len(data) == 1:
                        left, right = data[0]
                        left, right = self.value(left), self.value(right)
                        op = "equals"
                    else:
                        raise AssertionError(f"Unsupported check_variable {data}")
                fn = {
                    "equals": lambda: left == right,
                    "greater_than": lambda: left > right,
                    "greater_than_or_equals": lambda: left >= right,
                    "less_than": lambda: left < right,
                    "less_than_or_equals": lambda: left <= right,
                }[op]
                if not fn(): return False
            elif key == "OR":
                if not any(self.check([node]) for node in data): return False
            elif key == "AND":
                if not self.check(data): return False
            elif key == "NOT":
                if self.check(data): return False
            elif key == "ROOT":
                if not self._check_in_scope(self.root, data): return False
            elif key == "PREV":
                if not self._check_in_scope(self.previous, data): return False
            elif key == "has_global_flag":
                if data not in self.global_flags: return False
            elif key == "has_event_target":
                if data not in self.targets: return False
            elif key.startswith("event_target:"):
                target = self.targets.get(key[len("event_target:"):])
                if target is None or not self._check_in_scope(target, data): return False
            elif key == "has_country_flag":
                if data not in self.current.flags: return False
            elif key == "has_variable":
                if data not in self.current.flags and data not in self.temporary: return False
            elif key == "exists":
                if self.current.exists != (data == "yes"): return False
            elif key == "has_war":
                if bool(self.current.enemies) != (data == "yes"): return False
            elif key == "is_major":
                if self.current.major != (data == "yes"): return False
            elif key == "is_ai":
                if self.current.ai != (data == "yes"): return False
            elif key == "is_subject":
                if self.current.subject != (data == "yes"): return False
            elif key == "is_in_faction":
                if bool(self.current.faction) != (data == "yes"): return False
            elif key == "has_war_with_major":
                actual = any(country.major for country in self.current.enemies)
                if actual != (data == "yes"): return False
            elif key == "is_in_faction_with":
                other = self.value(data)
                if (self.current.faction is not None and
                        self.current.faction == getattr(other, "faction", None)) != (data != "no"):
                    return False
            elif key == "has_war_with":
                other = self.value(data)
                if (other in self.current.enemies) != (data != "no"): return False
            elif key == "uses_normal_civilian_systems":
                if not self.current.eligible: return False
            elif key == "num_of_controlled_states":
                if not self.current.eligible: return False
            elif key == "surrender_progress":
                # The parser represents this as a direct comparison in source.
                if not self.current.eligible: return False
            elif key in ("is_special_chaos_country", "is_actual_nonhuman_country"):
                if data == "yes": return False
                if data == "no": return True
            elif key == "has_recent_white_peace_pair_with_prev":
                if data == "yes": return False
            elif key == "PREV":
                if not self._check_in_scope(self.previous, data): return False
            elif key == "capital_scope":
                if not self.current.capital_safe: return False
            elif key == "war_length_with":
                if self.current.war_length_months <= FILE_CONSTANTS.get("WHITE_PEACE_LONG_WAR_MONTHS", 5):
                    return False
            elif key == "can_country_be_white_peace_target":
                if not self.current.eligible or self.current.faction or self.current.subject or not self.current.enemies:
                    return False
            elif key == "can_country_be_white_peace_major_target":
                if (not self.current.eligible or self.current.faction or self.current.subject
                        or not self.current.enemies or "white_peace_major_branch_enabled" not in self.global_flags
                        or self.globals.get("white_peace_stage", 0) <= CONSTANTS["white_peace_event_log"]["stage_repeated_minor"]):
                    return False
            elif key in ("can_pair_receive_white_peace", "can_minor_pair_receive_white_peace",
                         "can_major_pair_receive_white_peace", "can_major_pair_receive_white_peace_if_stage_unlocked"):
                partner = self.current
                primary = self.previous
                safe = (partner in primary.enemies and primary in partner.enemies
                        and len(partner.enemies) == 1 and len(primary.enemies) == 1
                        and partner.eligible and primary.eligible
                        and partner.faction is None and primary.faction is None
                        and not partner.subject and not primary.subject)
                minor = not partner.major and not primary.major
                major = partner.major or primary.major
                if key == "can_pair_receive_white_peace" and not (safe and (minor or major)):
                    return False
                if key == "can_minor_pair_receive_white_peace" and not (safe and minor):
                    return False
                if key == "can_major_pair_receive_white_peace" and not (safe and major):
                    return False
                if key == "can_major_pair_receive_white_peace_if_stage_unlocked" and not (safe and major):
                    return False
            elif key == "is_white_peace_minor_pair_for_prev":
                if self.current.major or self.previous.major: return False
            elif key == "is_white_peace_major_pair_for_prev":
                if not (self.current.major or self.previous.major): return False
            elif key == "is_current_evolution_enabled":
                stage = int(self.temporary.get("events_log_evolution_stage", 0))
                if stage in self.disabled_evolution_stages: return False
                tier = int(self.temporary.get("events_log_evolution_tier", 0))
                if tier > self.available_chaos_tier: return False
            elif key == "any_enemy_country":
                if not any(self._check_in_scope(enemy, data) for enemy in self.current.enemies):
                    return False
            elif key == "any_country":
                if not any(self._check_in_scope(country, data) for country in self.countries):
                    return False
            elif key == "tag":
                if self.current.tag != (self.value(data).tag if isinstance(self.value(data), Country) else data):
                    return False
            elif key == "always":
                if data != "yes": return False
            else:
                raise AssertionError(f"Unsupported Event 009 trigger {key}: {data}")
        return True

    @property
    def disabled_evolution_stages(self):
        return set()

    @property
    def available_chaos_tier(self):
        return 3

    def _check_in_scope(self, country, nodes):
        with self.scope(country):
            return self.check(nodes)

    def execute(self, nodes):
        index = 0
        while index < len(nodes):
            key, data = nodes[index]
            if key == "if":
                chain = [(key, data)]
                next_index = index + 1
                while next_index < len(nodes) and nodes[next_index][0] in ("else_if", "else"):
                    chain.append(nodes[next_index])
                    next_index += 1
                for branch_key, branch in chain:
                    if branch_key == "else" or self.check(child(branch, "limit", [])):
                        self.execute(without(branch, "limit"))
                        break
                index = next_index
                continue
            elif key == "every_country":
                limit = child(data, "limit", [])
                effects = without(data, "limit")
                for country in self.countries:
                    with self.scope(country):
                        if self.check(limit): self.execute(effects)
            elif key == "every_enemy_country":
                limit = child(data, "limit", [])
                effects = without(data, "limit")
                for country in list(self.current.enemies):
                    with self.scope(country):
                        if self.check(limit): self.execute(effects)
            elif key == "random_list":
                self.run_random_list(data)
            elif key == "random_scope_in_array":
                array_name = child(data, "array")
                candidates = self.arrays.get(array_name, [])
                self.native_calls.append({"native": "random_scope_in_array", "candidate_count": len(candidates)})
                if candidates:
                    with self.scope(candidates[0]):
                        self.execute(without(data, "array"))
            elif key == "while_loop_effect":
                limit = child(data, "limit", [])
                effects = without(data, "limit")
                bulk = self._bulk_weight_pool_append(limit, effects)
                if bulk:
                    array_name, value_token, count_name, remaining_name = bulk
                    remaining = int(round(self.temporary.get(remaining_name, 0)))
                    if remaining < 0 or remaining > 1000:
                        raise AssertionError("Fixture weight exceeds the verified source loop bound")
                    self.arrays.setdefault(array_name, []).extend(
                        [self.value(value_token)] * remaining)
                    self.temporary[count_name] = self.temporary.get(count_name, 0) + remaining
                    self.temporary[remaining_name] = 0
                    index += 1
                    continue
                iterations = 0
                while self.check(limit):
                    self.execute(effects)
                    iterations += 1
                    if iterations > 1000:
                        raise AssertionError("Source loop exceeded its declared engine ceiling")
            elif key in EFFECTS and data == "yes":
                self.call(key)
            elif key == "set_temp_variable":
                name, token = data[0]
                self.temporary[name] = self.value(token)
            elif key in ("set_variable", "set_temp_variable_to_random"):
                name, token = data[0]
                if key == "set_variable": self._set_normal(name, self.value(token))
                else: raise AssertionError("Unneeded random setter in bounded model")
            elif key in ("add_to_temp_variable", "subtract_from_temp_variable",
                         "multiply_temp_variable", "divide_temp_variable",
                         "add_to_variable", "subtract_from_variable", "multiply_variable"):
                name, token = data[0]
                target = self.temporary if key.endswith("temp_variable") else None
                if key in ("add_to_variable", "subtract_from_variable", "multiply_variable"):
                    current = self._normal_get(name)
                else:
                    current = self.temporary.get(name, 0)
                amount = self.value(token)
                if key.startswith("add_to"): current += amount
                elif key.startswith("subtract_from"): current -= amount
                elif key.startswith("multiply"): current *= amount
                elif key == "divide_temp_variable": current = current / amount
                if target is not None: target[name] = current
                else: self._set_normal(name, current)
            elif key in ("round_temp_variable", "round_variable"):
                name = data if isinstance(data, str) else child(data, "var")
                if key == "round_temp_variable": self.temporary[name] = round(self.temporary.get(name, 0))
                else: self._set_normal(name, round(self._normal_get(name)))
            elif key in ("clamp_temp_variable", "clamp_variable"):
                values = dict(data)
                name = values["var"]
                value = self.temporary.get(name, 0) if key == "clamp_temp_variable" else self._normal_get(name)
                if "min" in values: value = max(value, self.value(values["min"]))
                if "max" in values: value = min(value, self.value(values["max"]))
                if key == "clamp_temp_variable": self.temporary[name] = value
                else: self._set_normal(name, value)
            elif key == "clear_variable":
                self.temporary.pop(data, None)
                self.current.flags.discard(data)
            elif key == "clear_temp_array":
                self.arrays[data] = []
            elif key == "add_to_temp_array":
                values = dict(data)
                if "array" in values:
                    array_name, array_value = values["array"], values["value"]
                else:
                    array_name, array_value = next(iter(values.items()))
                self.arrays.setdefault(array_name, []).append(self.value(array_value))
            elif key == "set_global_flag":
                flag = data if isinstance(data, str) else child(data, "flag")
                self.global_flags.add(flag)
            elif key == "clr_global_flag":
                self.global_flags.discard(data)
            elif key == "set_country_flag":
                flag = data if isinstance(data, str) else child(data, "flag")
                self.current.flags.add(flag)
            elif key == "clr_country_flag":
                self.current.flags.discard(data)
            elif key == "save_event_target_as":
                self.targets[data] = self.current
            elif key.startswith("event_target:"):
                target_name = key[len("event_target:"):]
                target = self.targets.get(target_name)
                if target is None:
                    raise AssertionError(f"Missing event target {target_name}")
                with self.scope(target): self.execute(data)
            elif key == "ROOT":
                with self.scope(self.root): self.execute(data)
            elif key == "PREV":
                with self.scope(self.previous): self.execute(data)
            elif key == "white_peace":
                partner = self.value(child(data, "tag"))
                if partner and partner in self.current.enemies and self.current in partner.enemies:
                    self.current.enemies.remove(partner)
                    partner.enemies.remove(self.current)
                    self.applied_pairs.append((self.current.tag, partner.tag))
            elif key == "country_event":
                event_id = child(data, "id")
                if event_id in ("chaosx.nr9.2", "chaosx.nr9.3", "chaosx.nr9.4", "chaosx.nr9.5"):
                    self.report_notifications.append((self.current.tag, event_id))
            elif key == "news_event":
                self.news_notifications.append(child(data, "id"))
            elif key in ("add_opinion_modifier", "add_chaos_meter_value", "set_timed_country_flag"):
                # The settlement transaction itself is stubbed only at its own
                # helper boundary; these optional presentation/history effects
                # are not on the output-lifetime path under test.
                continue
            else:
                raise AssertionError(f"Unsupported Event 009 effect {key}: {data}")
            index += 1

    def _bulk_weight_pool_append(self, limit, effects):
        """Collapse the exact source weight-to-array loop without changing it."""
        if len(effects) != 3:
            return None
        by_key = {key: value for key, value in effects}
        if set(by_key) != {"add_to_temp_array", "add_to_temp_variable", "subtract_from_temp_variable"}:
            return None
        array_args = dict(by_key["add_to_temp_array"])
        if "array" in array_args:
            array_name, value_token = array_args["array"], array_args["value"]
        else:
            array_name, value_token = next(iter(array_args.items()))
        count_name, count_value = by_key["add_to_temp_variable"][0]
        remaining_name, decrement = by_key["subtract_from_temp_variable"][0]
        if self.value(count_value) != 1 or self.value(decrement) != 1:
            return None
        if len(limit) != 1 or limit[0][0] != "check_variable":
            return None
        predicate = limit[0][1]
        comparison = next((value for key, value in predicate if key == "_comparison"), None)
        if comparison:
            left, operator, right = comparison
            if left != remaining_name or operator != ">" or self.value(right) != 0:
                return None
        else:
            values = dict(predicate)
            if values.get("var") != remaining_name or values.get("compare") != "greater_than" or self.value(values.get("value")) != 0:
                return None
        return array_name, value_token, count_name, remaining_name

    def _set_normal(self, name, value):
        if name.startswith("global."):
            self.globals[name[len("global."):]] = value
        else:
            self.current.flags.add(name) if value is True else None

    def _normal_get(self, name):
        if name.startswith("global."):
            return self.globals.get(name[len("global."):], 0)
        return 0

    def run_random_list(self, nodes):
        entries = []
        for key, data in nodes:
            if key in ("seed", "modifier") or not isinstance(data, list):
                continue
            weight = self.value(key)
            for mod in (value for child_key, value in data if child_key == "modifier"):
                factor = self.value(child(mod, "factor", 1))
                conditions = without(mod, "factor")
                if self.check(conditions): weight *= factor
            body = without(data, "modifier")
            entries.append((key, max(0, weight), body))
        chosen = self.rng.select(entries)
        self.execute(chosen)

    def apply_white_peace_pair_stub(self):
        """Model only the native peace transaction and actual-pair receipt."""
        primary = self.current
        partner = self.targets.get("white_peace_partner")
        if (partner is None or partner not in primary.enemies or primary not in partner.enemies
                or len(primary.enemies) != 1 or len(partner.enemies) != 1):
            return
        primary.enemies.remove(partner)
        partner.enemies.remove(primary)
        self.applied_pairs.append((primary.tag, partner.tag))
        self.globals["white_peace_pairs_settled"] += 1
        if primary.major or partner.major:
            self.globals["white_peace_last_major_involved"] = 1
        if self.temporary.get("white_peace_branch") == CONSTANTS["white_peace_branch"]["broad_settlement"]:
            self.globals["white_peace_broad_conflicts_settled"] += 1

    def mark_pair_human_report_recipients(self, primary, partner):
        """Execute the actual human-marking if blocks from the pair helper."""
        helper = EFFECTS["apply_white_peace_pair"]
        def descendants(nodes):
            for key, data in nodes:
                yield key, data
                if isinstance(data, list):
                    yield from descendants(data)
        branches = [data for key, data in descendants(helper) if key == "if"]
        primary_branch = next((data for data in branches
                               if ("set_country_flag", "white_peace_human_report_pending") in data), None)
        if primary_branch is None:
            raise AssertionError(f"Primary queue if block not found in source branches: {branches!r}")
        partner_branch = next(
            data for data in branches
            if any(key == "event_target:white_peace_partner" and
                   ("set_country_flag", "white_peace_human_report_pending") in value
                   for key, value in data))
        self.targets["white_peace_partner"] = partner
        with self.scope(primary):
            self.execute([("if", primary_branch), ("if", partner_branch)])

    def _normal_get_by_path(self, name):
        return self._normal_get(name)


class OutputLifetimeScenarios(unittest.TestCase):
    def fixture(self, branch, minor_pairs=0, faction_wars=0, major_pairs=0):
        rt = WhitePeaceModel(desired_branch=branch)
        for pair_index in range(minor_pairs):
            left = Country(f"A{pair_index:02d}")
            right = Country(f"B{pair_index:02d}")
            left.enemies.append(right)
            right.enemies.append(left)
            rt.countries.extend((left, right))
        for pair_index in range(major_pairs):
            left = Country(f"M{pair_index:02d}", major=True)
            right = Country(f"N{pair_index:02d}")
            left.enemies.append(right)
            right.enemies.append(left)
            rt.countries.extend((left, right))
        for pair_index in range(faction_wars):
            faction = f"F{pair_index:02d}"
            left = Country(f"X{pair_index:02d}", faction=faction, eligible=False)
            right = Country(f"Y{pair_index:02d}", faction=faction, eligible=False)
            left.enemies.append(right)
            right.enemies.append(left)
            rt.countries.extend((left, right))
        rt.globals["chaos_meter_value"] = 100000
        return rt

    def scenario(self, label):
        if label == "base":
            return self.fixture("single_minor", minor_pairs=1), "single_minor", 1, 1, 1
        if label == "minor":
            # Three safe wars plus two in-faction wars satisfy Stage I pressure
            # while leaving the Stage I settlement cap at two pairs.
            return self.fixture("single_minor", minor_pairs=3, faction_wars=2), "single_minor", 1, 1, 3
        if label == "multi":
            return self.fixture("multi_minor", minor_pairs=3, faction_wars=2), "multi_minor", 2, 2, 3
        if label == "major":
            # Four safe minor wars meet the Stage II pair pressure. One isolated
            # major war supplies the major candidate, with faction wars adding
            # active-war pressure without becoming eligible pairs.
            return self.fixture("major_country", minor_pairs=4, faction_wars=6, major_pairs=1), "major_country", 1, 1, 4
        if label == "broad":
            # Six isolated eligible wars are required by Stage III pressure.
            # Four raw directed candidate edges would normalize to two wars and
            # cannot pass this stage's six-war pressure threshold.
            return self.fixture("broad_settlement", minor_pairs=6, faction_wars=6), "broad_settlement", 5, 5, 6
        raise AssertionError(label)

    def test_weight_pool_repeat_loop_is_exactly_bounded_for_bulk_model(self):
        rt = WhitePeaceModel()
        for helper in ("add_current_white_peace_primary_to_weighted_pool",
                       "add_current_white_peace_partner_to_weighted_pool"):
            loop = next(data for key, data in EFFECTS[helper] if key == "while_loop_effect")
            self.assertIsNotNone(rt._bulk_weight_pool_append(child(loop, "limit"), without(loop, "limit")))

    def resolve_and_route(self, rt):
        rt.root.flags.add("white_peace_current_invocation_has_human")
        rt.execute([("clr_country_flag", "white_peace_current_invocation_has_human")])
        rt.call("clear_white_peace_human_report_queue")
        rt.call("prepare_white_peace_runtime_context")
        rt.call("apply_white_peace_current_context")
        for primary_tag, partner_tag in rt.applied_pairs:
            primary = next(country for country in rt.countries if country.tag == primary_tag)
            partner = next(country for country in rt.countries if country.tag == partner_tag)
            rt.mark_pair_human_report_recipients(primary, partner)
        rt.call("fire_white_peace_report_event")
        self.assertFalse(any("white_peace_human_report_pending" in country.flags
                             for country in rt.countries))
        self.assertNotIn("white_peace_current_invocation_has_human", rt.root.flags)

    def test_all_five_real_source_chains_preserve_stage_branch_pair_and_cap(self):
        for label in ("base", "minor", "multi", "major", "broad"):
            with self.subTest(scenario=label):
                rt, wanted_branch, expected_cap, expected_settled, safe_minor_pairs = self.scenario(label)
                # The setup is a closed, declared 1v1 candidate set. The only
                # extra wars in Stage I/II/III are ineligible faction wars.
                rt.call("prepare_white_peace_runtime_context")
                self.assertEqual(rt.globals["white_peace_available"], 1)
                self.assertEqual(rt.globals["white_peace_safe_minor_pair_count"], safe_minor_pairs)
                expected_stage = {"base": 0, "minor": 1, "multi": 1, "major": 2, "broad": 3}[label]
                self.assertEqual(rt.globals["white_peace_selected_stage"], expected_stage)
                self.assertEqual(rt.globals["white_peace_selected_branch"],
                                 CONSTANTS["white_peace_branch"][wanted_branch])
                self.assertEqual(rt.globals["white_peace_selected_pair_cap"], expected_cap)
                self.assertTrue(rt.globals["white_peace_context_ready"])
                self.assertIn("white_peace_primary", rt.targets)
                self.assertIn("white_peace_partner", rt.targets)
                self.assertIs(rt.targets["event_cluster_actor"], rt.targets["white_peace_primary"])
                self.assertIs(rt.targets["white_peace_report_primary"], rt.targets["white_peace_primary"])
                self.assertIs(rt.targets["white_peace_report_partner"], rt.targets["white_peace_partner"])
                self.assertTrue(all(call["positive_weight"] > 0 for call in rt.rng.draws))

                if label == "base":
                    # The base entry is deterministic and makes no random-list call.
                    self.assertEqual(rt.rng.draws, [])
                else:
                    self.assertEqual(len(rt.rng.draws), 1)

                rt.call("apply_white_peace_current_context")
                self.assertEqual(rt.globals["white_peace_last_settled_pair_count"], expected_settled)
                self.assertEqual(len(rt.applied_pairs), expected_settled)
                self.assertEqual(len({tag for pair in rt.applied_pairs for tag in pair}), expected_settled * 2)
                if label in ("multi", "broad"):
                    self.assertEqual(expected_settled, expected_cap)
                if label == "major":
                    self.assertTrue(any(
                        next(c for c in rt.countries if c.tag == pair[0]).major or
                        next(c for c in rt.countries if c.tag == pair[1]).major
                        for pair in rt.applied_pairs))

    def test_actual_stage_helper_output_survives_nested_cleanup(self):
        thresholds = CONSTANTS["white_peace_stage_pressure"]
        cases = ((0, 1, 1, 0), (1, 5, 3, 1), (2, 8, 4, 2), (3, 12, 6, 3))
        for enabled_stage, wars, pairs, expected in cases:
            with self.subTest(stage=expected):
                rt = self.fixture("single_minor", minor_pairs=1)
                rt.global_flags.update({"white_peace_multi_branch_enabled",
                                        "white_peace_major_branch_enabled",
                                        "white_peace_broad_branch_enabled"})
                rt.globals["white_peace_active_war_count"] = wars
                rt.globals["white_peace_safe_minor_pair_count"] = pairs
                rt.temporary["white_peace_stage"] = 0
                rt.call("determine_white_peace_stage")
                self.assertEqual(rt.temporary["white_peace_stage"], expected)
                self.assertEqual(rt.globals["white_peace_stage"], expected)

    def test_branch_helper_outputs_disappear_without_outer_storage(self):
        rt, *_ = self.scenario("multi")
        # Recreate the already-calculated stage and candidate globals so this
        # bounded case isolates the select-branch return boundary.
        rt.globals.update(white_peace_stage=1, white_peace_safe_minor_pair_count=3,
                          white_peace_major_candidate_count=0)
        rt.global_flags.update({"white_peace_multi_branch_enabled"})
        rt.temporary["white_peace_stage"] = 1
        rt.rng.desired_branch = "multi_minor"
        rt.call("select_white_peace_branch")
        self.assertNotIn("white_peace_branch", rt.temporary)
        self.assertNotIn("white_peace_settlement_pair_cap", rt.temporary)

        rt.temporary.update(white_peace_branch=0, white_peace_settlement_pair_cap=0)
        rt.call("select_white_peace_branch")
        self.assertEqual(rt.temporary["white_peace_branch"], CONSTANTS["white_peace_branch"]["multi_minor"])
        self.assertEqual(rt.temporary["white_peace_settlement_pair_cap"], CONSTANTS["white_peace_settlement_cap"]["stage_1_pairs"])

    def test_both_human_endpoints_receive_one_major_result_and_queue_cleanup(self):
        rt, *_ = self.scenario("major")
        for tag in ("M00", "N00"):
            next(country for country in rt.countries if country.tag == tag).ai = False
        stale = Country("STALE", ai=False, eligible=False)
        stale.flags.add("white_peace_human_report_pending")
        rt.countries.append(stale)
        self.resolve_and_route(rt)
        self.assertEqual(len(rt.applied_pairs), 1)
        self.assertEqual(rt.globals["white_peace_last_settled_pair_count"], 1)
        self.assertEqual(rt.report_notifications,
                         [("M00", "chaosx.nr9.4"), ("N00", "chaosx.nr9.4")])
        self.assertEqual(rt.news_notifications, [])
        self.assertNotIn("white_peace_human_report_pending", stale.flags)

    def test_successive_human_pairs_each_receive_one_aggregate_result(self):
        rt, *_ = self.scenario("multi")
        for tag in ("A00", "B00", "A01", "B01"):
            next(country for country in rt.countries if country.tag == tag).ai = False
        self.resolve_and_route(rt)
        self.assertEqual(rt.globals["white_peace_selected_branch"],
                         CONSTANTS["white_peace_branch"]["multi_minor"])
        self.assertEqual(rt.globals["white_peace_last_settled_pair_count"], 2)
        self.assertEqual(rt.report_notifications,
                         [(tag, "chaosx.nr9.3") for tag in ("A00", "B00", "A01", "B01")])
        self.assertEqual(rt.news_notifications, [])

    def test_mixed_human_pair_gets_one_report_and_all_ai_gets_one_news_item(self):
        mixed, *_ = self.scenario("base")
        next(country for country in mixed.countries if country.tag == "A00").ai = False
        self.resolve_and_route(mixed)
        self.assertEqual(mixed.report_notifications, [("A00", "chaosx.nr9.2")])
        self.assertEqual(mixed.news_notifications, [])

        all_ai, *_ = self.scenario("base")
        self.resolve_and_route(all_ai)
        self.assertEqual(all_ai.report_notifications, [])
        self.assertEqual(all_ai.news_notifications, ["chaosx.nr9.7"])


def collect_source_model_evidence():
    harness = OutputLifetimeScenarios()
    branch_results = []
    for label in ("base", "minor", "multi", "major", "broad"):
        rt, wanted_branch, expected_cap, expected_settled, expected_safe_pairs = harness.scenario(label)
        rt.call("prepare_white_peace_runtime_context")
        selection = {
            "scenario": label,
            "wars_in_fixture": len([country for country in rt.countries if country.enemies]) // 2,
            "safe_minor_pair_count": rt.globals["white_peace_safe_minor_pair_count"],
            "major_candidate_count": rt.globals["white_peace_major_candidate_count"],
            "stage": rt.globals["white_peace_selected_stage"],
            "branch": next(name for name, value in CONSTANTS["white_peace_branch"].items()
                            if value == rt.globals["white_peace_selected_branch"]),
            "expected_branch": wanted_branch,
            "selected_pair_cap": rt.globals["white_peace_selected_pair_cap"],
            "expected_pair_cap": expected_cap,
            "selected_primary": rt.targets["white_peace_primary"].tag,
            "selected_partner": rt.targets["white_peace_partner"].tag,
            "event_log_actor": rt.targets["event_cluster_actor"].tag,
            "report_primary": rt.targets["white_peace_report_primary"].tag,
            "report_partner": rt.targets["white_peace_report_partner"].tag,
            "native_branch_rng_stub": rt.rng.draws,
        }
        rt.call("apply_white_peace_current_context")
        selection["settled_pair_count"] = rt.globals["white_peace_last_settled_pair_count"]
        selection["settled_pairs"] = [list(pair) for pair in rt.applied_pairs]
        selection["expected_settled_pair_count"] = expected_settled
        selection["fixture_expected_safe_minor_pairs"] = expected_safe_pairs
        branch_results.append(selection)

    notification_results = []
    scenarios = ("both_humans_major", "four_humans_multi", "mixed_human_ai", "all_ai")
    for scenario_name in scenarios:
        if scenario_name == "both_humans_major":
            rt, *_ = harness.scenario("major")
            for tag in ("M00", "N00"):
                next(country for country in rt.countries if country.tag == tag).ai = False
        elif scenario_name == "four_humans_multi":
            rt, *_ = harness.scenario("multi")
            for tag in ("A00", "B00", "A01", "B01"):
                next(country for country in rt.countries if country.tag == tag).ai = False
        elif scenario_name == "mixed_human_ai":
            rt, *_ = harness.scenario("base")
            next(country for country in rt.countries if country.tag == "A00").ai = False
        else:
            rt, *_ = harness.scenario("base")
        stale = Country("STALE", ai=False, eligible=False)
        stale.flags.add("white_peace_human_report_pending")
        rt.countries.append(stale)
        harness.resolve_and_route(rt)
        notification_results.append({
            "scenario": scenario_name,
            "settled_pairs": [list(pair) for pair in rt.applied_pairs],
            "reports_by_country": [list(row) for row in rt.report_notifications],
            "observer_news": list(rt.news_notifications),
            "pending_queue_after_dispatch": sorted(
                country.tag for country in rt.countries
                if "white_peace_human_report_pending" in country.flags),
            "invocation_flag_after_dispatch": "white_peace_current_invocation_has_human" in rt.root.flags,
        })

    relevant = (
        "common/scripted_effects/009_white_peace_effects.txt",
        "common/scripted_triggers/009_white_peace_triggers.txt",
        "common/script_constants/009_white_peace_constants.txt",
        "events/009_white_peace.txt",
    )
    current_hashes = {
        path: hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
        for path in relevant
    }
    baseline_path = ROOT / "docs/plans/009_white_peace_plans/evidence_2026_10_05/baseline/009_white_peace_effects.txt"
    baseline_hash = hashlib.sha256(baseline_path.read_bytes()).hexdigest() if baseline_path.is_file() else None
    return {
        "evidence_type": "bounded_actual_source_model",
        "model_sha256": hashlib.sha256(Path(__file__).resolve().read_bytes()).hexdigest(),
        "model_contract": "Conservative helper-frame cleanup; temporary scalars/arrays created in a returning helper are discarded unless caller storage existed first.",
        "model_limits": [
            "The interpreter executes the current Event 009 source bodies, but fixture candidate eligibility is a declared isolated-pair model and does not certify HOI4 PREV/event-target scope semantics.",
            "The deterministic native random_list stub selects a requested branch only when its computed source weight is positive; no event probability is estimated.",
            "The deterministic native random_scope_in_array stub selects the first scope in the source-built candidate array; candidate frequency is not estimated.",
            "The apply_white_peace_pair transaction helper is stubbed to remove one reciprocal isolated war and increment the source-consumed settlement counters. Other settlement side effects are outside this lifetime model.",
            "country_event/news_event are captured as recipient/event-id rows; no GUI or game session is emulated."
        ],
        "source_hashes_sha256": current_hashes,
        "preserved_prepatch_effects_path": "docs/plans/009_white_peace_plans/evidence_2026_10_05/baseline/009_white_peace_effects.txt",
        "preserved_prepatch_effects_hash_sha256": baseline_hash,
        "branch_and_cap_scenarios": branch_results,
        "notification_scenarios": notification_results,
        "probability_compare": {
            "status": "blocked_by_mcp_timeout",
            "handoff": "docs/plans/009_white_peace_plans/subagent_handoffs/white_peace_probability_compare_2026-10-06.md",
            "numeric_delta": None
        }
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-evidence", nargs="?", const="default")
    args, extra = parser.parse_known_args()
    if args.write_evidence is not None:
        if extra and args.write_evidence == "default":
            result_path = Path(extra[0])
        elif args.write_evidence == "default":
            result_path = ROOT / "docs/plans/009_white_peace_plans/source_models/009_white_peace_helper_output_lifetimes_results.json"
        else:
            result_path = Path(args.write_evidence)
        result_path.parent.mkdir(parents=True, exist_ok=True)
        result_path.write_text(json.dumps(collect_source_model_evidence(), indent=2) + "\n", encoding="utf-8")
        print(result_path)
    else:
        unittest.main(argv=[sys.argv[0]] + extra)
