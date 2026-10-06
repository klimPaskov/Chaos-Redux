"""Bounded source interpreter, not HOI4 execution or probability evidence.

Every helper call drops newly created temporary scalar/array storage on return.
Caller-preinitialized storage retains mutations. Regular variables/arrays and
event targets live separately, partitioned by object scope. Unsupported executed
nodes raise, and external predicate fixtures are named explicitly.
"""
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path
import hashlib
import json
import re
import unittest

REPO = Path(__file__).resolve().parents[5]
DEST = Path(__file__).resolve().parent
TOKEN = re.compile(r'#[^\n]*|"(?:\\.|[^"\\])*"|[{}=<>]|[^\s{}=<>]+')


@dataclass
class Node:
    key: str
    op: str
    body: object
    start: int
    end: int
    path: str


def parse(path):
    text = path.read_text(encoding="utf-8-sig")
    matches = [m for m in TOKEN.finditer(text) if not m.group().startswith("#")]
    cursor = 0

    def block():
        nonlocal cursor
        nodes = []
        while cursor < len(matches) and matches[cursor].group() != "}":
            first = matches[cursor]
            key, op, body = first.group(), "", None
            cursor += 1
            if cursor < len(matches) and matches[cursor].group() in ("=", "<", ">"):
                op = matches[cursor].group()
                cursor += 1
                token = matches[cursor].group()
                cursor += 1
                if token == "{":
                    body = block()
                    assert matches[cursor].group() == "}"
                    cursor += 1
                else:
                    body = token
            last = matches[cursor - 1]
            nodes.append(Node(key, op, body, text.count("\n", 0, first.start()) + 1,
                              text.count("\n", 0, last.end()) + 1, str(path)))
        return nodes
    return block()


def field(nodes, key, default=None):
    return next((n.body for n in nodes if n.key == key), default)


def walk(nodes):
    for node in nodes:
        yield node
        if isinstance(node.body, list):
            yield from walk(node.body)


PATHS = [
    "common/scripted_effects/024_video_game_in_sweden_effects.txt",
    "common/scripted_effects/024_video_game_in_sweden_cxt_effects.txt",
    "common/scripted_effects/024_video_game_in_sweden_runtime_effects.txt",
    "common/scripted_triggers/024_video_game_in_sweden_triggers.txt",
    "common/scripted_localisation/024_video_game_in_sweden.txt",
    "common/decisions/024_video_game_in_sweden_decisions.txt",
    "events/024_hearts_of_iron.txt",
    "common/on_actions/024_video_game_in_sweden_cxt_on_actions.txt",
    "common/on_actions/024_video_game_in_sweden_lifecycle_on_actions.txt",
    "common/scripted_effects/individual_crisis_targeting_effects.txt",
    "common/scripted_triggers/individual_crisis_targeting_triggers.txt",
    "common/scripted_effects/chaosx_test_country_effects.txt",
]
BASELINE = "docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_pre_output_lifetime/024_video_game_in_sweden_effects.txt"
BEFORE_TRIGGERS = "docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_post_emergency_restriction/024_video_game_in_sweden_triggers.txt"
BEFORE_CXT = "docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_pre_remaining_routes/common/on_actions/024_video_game_in_sweden_cxt_on_actions.txt"
BEFORE_EVENTS = "docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_post_emergency_restriction/024_hearts_of_iron.txt"
SOURCES = {path: parse(REPO / path) for path in PATHS}
APIS = {n.key: n for path, nodes in SOURCES.items()
        if "/scripted_effects/" in path or "/scripted_triggers/" in path
        for n in nodes if isinstance(n.body, list)}
CONSTANTS = {}
for name in ("024_video_game_in_sweden_constants.txt", "individual_crisis_targeting_constants.txt"):
    for group in parse(REPO / "common/script_constants" / name):
        for item in group.body:
            if item.key != "schema" and isinstance(item.body, str):
                CONSTANTS[group.key + "." + item.key] = Decimal(item.body)


class Unsupported(RuntimeError):
    pass


class FrameModel:
    def __init__(self, root="SWE", actor="SWE"):
        self.root, self.actor, self.prev = root, actor, None
        self.temp, self.temp_arrays, self.saved, self.arrays = {}, {}, {}, {}
        self.flags, self.targets, self.facts, self.debits = {}, {}, {}, []
        self.trace, self.executed = [], set()

    def number(self, token):
        if token.startswith("constant:"):
            return CONSTANTS[token[9:]]
        if token == "THIS":
            return self.actor
        if token.startswith("token:"):
            return token
        if "^" in token:
            array, index = token.split("^", 1)
            values = self.temp_arrays.get(array, self.arrays.get(array, []))
            return Decimal(len(values)) if index == "num" else values[int(self.number(index))]
        if token in self.temp:
            return self.temp[token]
        if token in self.facts:
            return self.facts[token]
        try:
            return Decimal(token)
        except Exception:
            return self.saved.get((self.actor, token), Decimal(0))

    def call(self, name):
        scalars, arrays = set(self.temp), set(self.temp_arrays)
        try:
            return self.run(APIS[name].body)
        finally:
            dropped = sorted(set(self.temp) - scalars)
            dropped_arrays = sorted(set(self.temp_arrays) - arrays)
            self.trace.append({"callee": name, "dropped_scalars": dropped,
                               "dropped_arrays": dropped_arrays})
            for key in dropped:
                del self.temp[key]
            for key in dropped_arrays:
                del self.temp_arrays[key]

    def compare(self, node):
        if isinstance(node.body, list):
            name = field(node.body, "var", node.body[0].key)
            rhs = field(node.body, "value", node.body[0].body)
            operation = field(node.body, "compare", node.body[0].op)
        else:
            name, rhs, operation = node.key, node.body, node.op
        a, b = self.number(name), self.number(rhs)
        return {"equals": a == b, "=": a == b, "less_than": a < b,
                "<": a < b, "greater_than": a > b, ">": a > b,
                "less_than_or_equals": a <= b,
                "greater_than_or_equals": a >= b}[operation]

    def scope(self, actor, nodes):
        old_actor, old_prev = self.actor, self.prev
        self.actor, self.prev = actor, self.actor
        try:
            return self.run(nodes)
        finally:
            self.actor, self.prev = old_actor, old_prev

    def run(self, nodes):
        results, selected = [], False
        for n in nodes:
            k, b = n.key, n.body
            self.executed.add((n.path, n.start, k))
            if k in APIS:
                results.append(self.call(k))
            elif k in ("AND", "hidden_trigger"):
                results.append(self.run(b))
            elif k == "OR":
                results.append(any(self.run([child]) for child in b))
            elif k == "NOT":
                results.append(not any(self.run([child]) for child in b))
            elif k in ("if", "else_if"):
                take = (k == "if" or not selected) and self.run(field(b, "limit", []))
                if k == "if":
                    selected = False
                if take:
                    selected = True
                    self.run([child for child in b if child.key != "limit"])
            elif k == "else":
                if not selected:
                    self.run(b)
            elif k == "while_loop_effect":
                count = 0
                while self.run(field(b, "limit", [])):
                    count += 1
                    if count > 1000:
                        raise Unsupported("loop bound")
                    self.run([child for child in b if child.key != "limit"])
            elif k.endswith("_temp_variable") or k in ("set_variable", "add_to_variable"):
                name = field(b, "var", b[0].key)
                rhs = field(b, "value", b[0].body)
                regular = k in ("set_variable", "add_to_variable")
                store, key = (self.saved, (self.actor, name)) if regular else (self.temp, name)
                old = store.get(key, Decimal(0))
                if k.startswith("clamp"):
                    store[key] = min(self.number(field(b, "max")), max(self.number(field(b, "min")), old))
                elif k.startswith("set"):
                    store[key] = self.number(rhs)
                elif k.startswith("add"):
                    store[key] = old + self.number(rhs)
                elif k.startswith("subtract"):
                    store[key] = old - self.number(rhs)
                elif k.startswith("multiply"):
                    store[key] = old * self.number(rhs)
                else:
                    raise Unsupported(k)
            elif k == "clear_temp_array":
                # Allocating on clear is a declared model assumption, not engine proof.
                self.temp_arrays[b] = []
            elif k in ("add_to_temp_array", "add_to_array"):
                name = field(b, "array", b[0].key)
                rhs = field(b, "value", b[0].body)
                store = self.temp_arrays if k == "add_to_temp_array" else self.arrays
                store.setdefault(name, []).append(self.number(rhs))
            elif k == "check_variable":
                results.append(self.compare(n))
            elif k == "has_variable":
                results.append(b in self.temp or (self.actor, b) in self.saved)
            elif k == "has_country_flag":
                if not isinstance(b, str):
                    raise Unsupported("timed flag arguments")
                results.append(b in self.flags.get(self.actor, set()))
            elif k == "set_country_flag":
                self.flags.setdefault(self.actor, set()).add(b)
            elif k == "has_event_target":
                results.append(b in self.targets)
            elif k == "is_in_array":
                name = field(b, "array", b[0].key)
                rhs = field(b, "value", b[0].body)
                results.append(self.number(rhs) in self.arrays.get(name, []))
            elif k.startswith("event_target:"):
                if k[13:] not in self.targets:
                    results.append(False)
                else:
                    results.append(self.scope(self.targets[k[13:]], b))
            elif k == "ROOT":
                results.append(self.scope(self.root, b))
            elif k == "tag":
                target = self.root if b == "ROOT" else self.actor if b == "THIS" else self.prev if b == "PREV" else b
                results.append(self.actor == target)
            elif k in ("add_political_power", "add_stability", "add_war_support"):
                self.debits.append((self.actor, k, str(self.number(b))))
            elif k == "always":
                results.append(b == "yes")
            elif k == "tooltip_evaluation":
                pass
            elif (self.actor, k, str(b)) in self.facts:
                results.append(self.facts[(self.actor, k, str(b))])
            else:
                raise Unsupported(f"{n.path}:{n.start} {k}")
        return all(results)


CASES = []


class ActualSourceLifetime(unittest.TestCase):
    def test_preserved_before_payer_loses_new_quote_outputs(self):
        name = "video_game_in_sweden_pay_restriction"
        before = next(n for n in parse(REPO / BASELINE) if n.key == name)
        current = APIS[name]
        try:
            APIS[name] = before
            model = FrameModel()
            model.facts.update({"has_political_power": Decimal(100), "has_stability": Decimal(".8"),
                                "has_war_support": Decimal(".75")})
            model.call(name)
            self.assertEqual([Decimal(x[2]) for x in model.debits], [Decimal(0)] * 3)
            CASES.append({"case": "immutable before payer", "debits": model.debits,
                          "before_source": BASELINE, "before_sha256": hashlib.sha256((REPO / BASELINE).read_bytes()).hexdigest(),
                          "quote_source": "current trigger, whose output arithmetic is unchanged",
                          "proof_kind": "actual before payer with conservative helper return"})
        finally:
            APIS[name] = current

    def test_ticket_forwarded_scalar_and_load(self):
        outer = "video_game_in_sweden_add_current_country_to_prefire_pool"
        load = "individual_crisis_active_load"
        output = "individual_crisis_candidate_adjusted_weight"
        # External provider classifier truth is declared, not executed or inferred.
        model = FrameModel()
        for n in walk(APIS["individual_crisis_load_is_below_cap"].body):
            if n.key in APIS and n.key != "individual_crisis_load_is_below_cap":
                model.facts[("SWE", n.key, "yes")] = False
        model.flags["SWE"] = {"video_game_in_sweden_program_active"}
        # Replace only external classifiers at their exact source call sites with
        # explicit scenario false predicates, preserving the source load arithmetic.
        provider_names = {n.key for n in walk(APIS["individual_crisis_load_is_below_cap"].body)
                          if n.key not in APIS and n.key not in (
                              "hidden_trigger", "tooltip_evaluation", "set_temp_variable", "if", "limit",
                              "OR", "AND", "NOT", "has_country_flag", "check_variable", "var", "value", "compare",
                              "add_to_temp_variable", "individual_crisis_active_load", "any_controlled_state")}
        for name in provider_names:
            model.facts[("SWE", name, "yes")] = False
        for n in walk(APIS["individual_crisis_load_is_below_cap"].body):
            if n.key == "any_controlled_state":
                model.facts[("SWE", n.key, str(n.body))] = False
        # Actor active program alone gives one load. Other provider subtrees are
        # deliberately supplied false via source-node fixtures for this test.
        original_run = model.run
        def external_fixture_run(nodes):
            if len(nodes) == 1 and nodes[0].key in provider_names:
                return False
            return original_run(nodes)
        model.run = external_fixture_run
        # any_controlled_state is treated as a fixture predicate in original_run.
        results = []
        current = APIS[outer]
        before = next(n for n in parse(REPO / BASELINE) if n.key == outer)
        try:
            APIS[outer] = before
            for preinitialized in ((), (output,), (output, load)):
                model.temp, model.temp_arrays, model.trace = {}, {"video_game_in_sweden_prefire_host_pool": []}, []
                for key in preinitialized:
                    model.temp[key] = Decimal(0)
                model.call(outer)
                results.append(len(model.temp_arrays["video_game_in_sweden_prefire_host_pool"]))
            # This archives only the Event 24 wrapper. Its shared helpers and
            # tuning are today's source, so the middle result is an observed
            # compatibility case, not a frozen historical ticket count.
            self.assertEqual(results[0], 0)
        finally:
            APIS[outer] = current
        model.temp, model.temp_arrays = {}, {"video_game_in_sweden_prefire_host_pool": []}
        model.call(outer)
        after_tickets = len(model.temp_arrays["video_game_in_sweden_prefire_host_pool"])
        self.assertEqual(after_tickets, 2)
        self.assertEqual(results[2], after_tickets)
        model.temp = {output: Decimal(0), load: Decimal(0)}
        model.temp_arrays = {}
        model.call(outer)
        self.assertNotIn("video_game_in_sweden_prefire_host_pool", model.temp_arrays)
        self.assertIn("video_game_in_sweden_prefire_host_pool", model.trace[-1]["dropped_arrays"])
        CASES.append({"case": "archived wrapper under current shared dependencies", "archived_wrapper_tickets": results,
                      "after_tickets_without_external_scalar_storage": after_tickets, "before_source": BASELINE,
                      "dependency_basis": "current shared helper, trigger and tuning, not a frozen historical baseline",
                      "declared_external_predicates": sorted(provider_names),
                      "new_callee_array_dropped": True,
                      "proof_kind": "conservative source arithmetic under explicit false-provider fixtures"})

    def test_cxt_forwarded_receipt(self):
        helper = "video_game_in_sweden_register_cxt_test_content"
        receipt = "chaosx_test_country_extension_registration_added"
        model = FrameModel(actor="CXT")
        model.call(helper)
        self.assertNotIn(receipt, model.temp)
        self.assertEqual(len(model.arrays["global.chaosx_test_country_registered_extension_effects"]), 1)
        model.arrays.clear()
        model.temp[receipt] = Decimal(0)
        model.call(helper)
        self.assertEqual(model.temp[receipt], Decimal(1))
        def daily_prefix(source):
            actions = field(source, "on_actions")
            effect = field(field(actions, "on_daily_CXT"), "effect")
            guarded = next(n.body for n in effect if n.key == "if")
            prefix = []
            for n in guarded:
                if n.key != "limit":
                    prefix.append(n)
                if n.key == helper:
                    break
            return prefix
        before_model = FrameModel(actor="CXT")
        before_model.run(daily_prefix(parse(REPO / BEFORE_CXT)))
        self.assertNotIn(receipt, before_model.temp)
        after_model = FrameModel(actor="CXT")
        after_model.run(daily_prefix(SOURCES["common/on_actions/024_video_game_in_sweden_cxt_on_actions.txt"]))
        self.assertEqual(after_model.temp[receipt], Decimal(1))
        CASES.append({"case": "CXT nested receipt", "uninitialized_return": "absent",
                      "preinitialized_return": "1", "persistent_registration_survives": True,
                      "before_actual_daily_receipt": "absent", "after_actual_daily_receipt": "1",
                      "before_daily_source": BEFORE_CXT, "daily_sync_execution": "not executed",
                      "proof_kind": "source call-frame and persistent-array separation"})

    def test_payer_and_getters(self):
        for pp, stability, support in (("100", ".8", ".75"), ("0", ".02", ".01"),
                                       ("-2", "-.1", "-.3"), ("29.12345", ".01337", ".02001")):
            model = FrameModel()
            model.facts.update({"has_political_power": Decimal(pp), "has_stability": Decimal(stability),
                                "has_war_support": Decimal(support)})
            model.call("video_game_in_sweden_pay_restriction")
            expected = [-min(Decimal(30), max(Decimal(0), Decimal(pp))),
                        -min(Decimal(".04"), max(Decimal(0), Decimal(stability))),
                        -min(Decimal(".03"), max(Decimal(0), Decimal(support)))]
            self.assertEqual([Decimal(x[2]) for x in model.debits], expected)
            CASES.append({"case": "current payer", "reserves": [pp, stability, support], "debits": model.debits,
                          "proof_kind": "actual source arithmetic, no native currency binding"})
        texts = SOURCES["common/scripted_localisation/024_video_game_in_sweden.txt"]
        for name, output in (("GetVideoGameRestrictionPoliticalPowerCost", "political_power"),
                             ("GetVideoGameRestrictionStabilityCost", "stability"),
                             ("GetVideoGameRestrictionWarSupportCost", "war_support")):
            definition = next(n for n in texts if field(n.body, "name") == name)
            trigger = field(next(n.body for n in definition.body if n.key == "text"), "trigger")
            model = FrameModel()
            model.facts.update({"has_political_power": Decimal(100), "has_stability": Decimal(".8"),
                                "has_war_support": Decimal(".75")})
            model.run(trigger)
            key = "video_game_in_sweden_restriction_" + output + "_quote"
            self.assertIn(key, model.temp)
            CASES.append({"case": name, "retained_consumed_output": key, "value": str(model.temp[key]),
                          "proof_kind": "trigger-frame storage, excludes localisation rendering"})

    def test_current_host_root_shift(self):
        guard = "video_game_in_sweden_is_current_host"
        before_guard = next(n for n in parse(REPO / BEFORE_TRIGGERS) if n.key == guard)
        current_guard = APIS[guard]
        for root, before_expected in (("SWE", True), ("NOR", False), ("GER", False)):
            model = FrameModel(root=root)
            model.targets["video_game_in_sweden_host"] = "SWE"
            model.flags["SWE"] = {"video_game_in_sweden_host_selected", "video_game_in_sweden_program_active"}
            model.facts.update({("SWE", "has_global_flag", "world_end"): False,
                                ("SWE", "exists", "yes"): True, ("SWE", "original_tag", "SWE"): True,
                                ("SWE", "has_capitulated", "yes"): False,
                                ("SWE", "owns_state", "constant:video_game_in_sweden_event.stockholm_state"): True,
                                ("SWE", "controls_state", "constant:video_game_in_sweden_event.stockholm_state"): True})
            try:
                APIS[guard] = before_guard
                self.assertEqual(model.call(guard), before_expected)
            finally:
                APIS[guard] = current_guard
            self.assertTrue(model.call(guard))
            CASES.append({"case": "host guard with entered Sweden", "ROOT": root, "THIS": "SWE",
                          "before_result": before_expected, "after_result": True,
                          "before_source": BEFORE_TRIGGERS, "proof_kind": "source scope model with explicit native facts"})
        foreign_event = next(n for n in SOURCES["events/024_hearts_of_iron.txt"]
                             if n.key == "country_event" and field(n.body, "id") == "chaosx.nr24.40")
        before_foreign_event = next(n for n in parse(REPO / BEFORE_EVENTS)
                             if n.key == "country_event" and field(n.body, "id") == "chaosx.nr24.40")
        model = FrameModel(root="NOR", actor="NOR")
        model.targets.update({"video_game_in_sweden_host": "SWE", "video_game_in_sweden_foreign_partner": "NOR"})
        model.flags.update({"SWE": {"video_game_in_sweden_host_selected", "video_game_in_sweden_program_active"},
                            "NOR": {"video_game_in_sweden_foreign_response_pending"}})
        model.facts.update({("SWE", "has_global_flag", "world_end"): False,
                            ("SWE", "exists", "yes"): True, ("SWE", "original_tag", "SWE"): True,
                            ("SWE", "has_capitulated", "yes"): False,
                            ("SWE", "owns_state", "constant:video_game_in_sweden_event.stockholm_state"): True,
                            ("SWE", "controls_state", "constant:video_game_in_sweden_event.stockholm_state"): True,
                            ("NOR", "exists", "yes"): True, ("NOR", "has_capitulated", "yes"): False,
                            ("NOR", "has_war_with", "event_target:video_game_in_sweden_host"): False})
        try:
            APIS[guard] = before_guard
            self.assertFalse(model.run(field(before_foreign_event.body, "trigger")))
        finally:
            APIS[guard] = current_guard
        self.assertTrue(model.run(field(foreign_event.body, "trigger")))
        CASES.append({"case": "actual chaosx.nr24.40 trigger", "ROOT": "NOR", "before_result": False, "after_result": True,
                      "before_event_source": BEFORE_EVENTS,
                      "proof_kind": "whole source trigger under explicit valid host/partner native facts"})
        model.root, model.actor = "SWE", "NOR"
        model.flags["NOR"].update({"video_game_in_sweden_host_selected", "video_game_in_sweden_program_active"})
        model.facts.update({("NOR", "has_global_flag", "world_end"): False,
                            ("NOR", "original_tag", "SWE"): False,
                            ("NOR", "owns_state", "constant:video_game_in_sweden_event.stockholm_state"): False,
                            ("NOR", "controls_state", "constant:video_game_in_sweden_event.stockholm_state"): False})
        for n in walk(APIS["video_game_in_sweden_is_valid_host"].body):
            if n.key == "any_controlled_state":
                model.facts[("NOR", n.key, str(n.body))] = False
        self.assertFalse(model.call(guard))
        CASES.append({"case": "current identity guard entered NOR from SWE ROOT", "ROOT": "SWE", "THIS": "NOR",
                      "after_result": False, "proof_kind": "whole actual guard under explicit foreign eligibility facts"})

    def test_regular_state_is_separate(self):
        model = FrameModel(actor="CXT")
        key = "video_game_in_sweden_cxt_fixture_event_id"
        model.flags["CXT"] = {"chaosx_test_country_initialized"}
        model.temp[key] = Decimal(99)
        model.saved[("SWE", key)] = Decimal(38)
        model.call("chaosx_cxt_extension_event024_video_game_in_sweden_apply")
        self.assertEqual(model.saved[("CXT", key)], Decimal(24))
        self.assertEqual(model.saved[("SWE", key)], Decimal(38))
        self.assertEqual(model.temp[key], Decimal(99))
        with self.assertRaises(Unsupported):
            model.run([Node("is_supplied", "=", "yes", 1, 1, "unsupported fixture")])


def inventory():
    rows = []
    for name, api in APIS.items():
        if "024_" not in api.path:
            continue
        writes, calls = [], []
        for n in walk(api.body):
            if "temp_variable" in n.key or "temp_array" in n.key:
                writes.append({"command": n.key, "line": n.start,
                               "storage": n.body if isinstance(n.body, str) else field(n.body, "var", n.body[0].key)})
            if n.key in APIS:
                calls.append({"callee": n.key, "line": n.start})
        rows.append({"api": name, "path": api.path, "span": [api.start, api.end],
                     "temporary_writes": writes, "calls": calls,
                     "owner_scope": "current caller country, inherited ROOT remains unchanged",
                     "execution_status": "inventory only unless separately covered by a named case"})
    for api in SOURCES["common/scripted_localisation/024_video_game_in_sweden.txt"]:
        if api.key != "defined_text":
            continue
        rows.append({"api": field(api.body, "name"), "path": api.path, "span": [api.start, api.end],
                     "owner_scope": "country selected by the localisation namespace",
                     "temporary_writes": [{"command": n.key, "line": n.start,
                         "storage": n.body if isinstance(n.body, str) else field(n.body, "var", n.body[0].key)}
                         for n in walk(api.body) if "temp_variable" in n.key or "temp_array" in n.key],
                     "calls": [{"callee": n.key, "line": n.start} for n in walk(api.body) if n.key in APIS],
                     "execution_status": "inventory only unless separately covered by a named case"})
    return rows


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEST / "actual_source_lifetime_results.json")
    args = parser.parse_args()
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(ActualSourceLifetime))
    report = {"proof_kind": "bounded conservative actual-source model, not HOI4 execution",
              "source_sha256": {p: hashlib.sha256((REPO / p).read_bytes()).hexdigest() for p in PATHS},
              "constants_sha256": {name: hashlib.sha256((REPO / "common/script_constants" / name).read_bytes()).hexdigest()
                  for name in ("024_video_game_in_sweden_constants.txt", "individual_crisis_targeting_constants.txt")},
              "test_source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "api_inventory": inventory(), "cases": CASES,
              "before_source_sha256": {p: hashlib.sha256((REPO / p).read_bytes()).hexdigest()
                  for p in (BASELINE, BEFORE_TRIGGERS, BEFORE_CXT, BEFORE_EVENTS)},
              "caller_inventory": [{"caller_path": path, "line": n.start, "callee": n.key}
                  for path, nodes in SOURCES.items() for n in walk(nodes)
                  if n.key in APIS and (n.key.startswith("video_game_in_sweden_") or "event024" in n.key)],
              "tests_run": result.testsRun, "model_tests_successful": result.wasSuccessful(),
              "unsupported_execution": ["native stockpile/currency binding", "supply satisfaction per division",
                  "engine temporary array allocation on clear", "delayed event delivery", "save/reload",
                  "native character retirement/transfer", "random selection and probability",
                  "complete mission lifecycle", "meta expansion", "tooltip/localisation rendering"],
              "failures": [str(err) for _, err in result.failures + result.errors]}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({"apis_inventoried": len(report["api_inventory"]), "tests_run": result.testsRun,
                      "model_tests_successful": result.wasSuccessful(), "artifact": str(args.output)}))
    raise SystemExit(0 if result.wasSuccessful() else 1)
