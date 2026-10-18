"""Execute Event 025's recovery-arbitration source against deterministic fixtures.

This interpreter is deliberately limited to the effects under test. It does
not emulate HOI4 scheduling, RNG, missions, or the external technology API.
"""
from dataclasses import dataclass, field
from itertools import permutations
from pathlib import Path
import operator
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
RUNTIME = ROOT / "common/scripted_effects/025_alien_technology_in_antarctica_runtime_effects.txt"
EVENTS = ROOT / "events/025_alien_technology_in_antarctica.txt"
CONSTANTS = ROOT / "common/script_constants/025_alien_technology_in_antarctica_constants.txt"
TOKEN = re.compile(r'"[^"]*"|[{}=]|[^\s{}=]+')
SOURCE = re.sub(r"#[^\n]*", "", RUNTIME.read_text(encoding="utf-8-sig"))


def block(name, source=SOURCE):
    start = re.search(r"\b" + re.escape(name) + r"\s*=\s*\{", source)
    if not start:
        raise AssertionError(f"Missing recovery effect {name}")
    tokens = TOKEN.findall(source[start.end():])
    at = 0

    def parse():
        nonlocal at
        result = []
        while tokens[at] != "}":
            key = tokens[at]
            if tokens[at + 1] != "=":
                raise AssertionError(f"Unsupported assignment in {name}: {tokens[at:at + 4]}")
            at += 2
            value = tokens[at]
            at += 1
            if value == "{":
                value = parse()
            result.append((key, value))
        at += 1
        return result
    return parse()


@dataclass
class Country:
    id: int
    values: dict = field(default_factory=dict)
    flags: set = field(default_factory=lambda: {
        "chaosx_nr25_participant", "chaosx_nr25_recovery_proof_submitted",
    })
    exists: bool = True
    subject: bool = False
    capitulated: bool = False


class Runtime:
    fields = ("survey", "readiness", "outpost", "exposure", "ready_date")
    effects = {
        name: block("chaosx_nr25_" + name) for name in (
            "capture_recovery_proof", "store_final_candidate",
            "candidate_is_better_same_day", "submit_final_candidate",
            "reselect_final_candidate", "resolve_final_candidate",
        )
    }

    def __init__(self, countries):
        self.countries = countries
        self.global_values = {
            "date": 101, "chaosx_nr25_final_candidate_date": 100,
            "chaosx_nr25_final_resolution_pending": 1,
            "chaosx_nr25_participants": countries,
        }
        self.global_flags = {"chaosx_nr25_active"}
        self.temporary = {}
        self.targets = {}
        self.grants = []
        self.reports = []
        self.constants = {}
        raw = re.sub(r"#[^\n]*", "", CONSTANTS.read_text(encoding="utf-8-sig"))
        for category, body in re.findall(r"(chaosx_nr25_\w+)\s*=\s*\{(.*?)(?=\n\})", raw, re.S):
            for key, value in re.findall(r"^\s*(\w+)\s*=\s*(-?\d+(?:\.\d+)?)\s*$", body, re.M):
                self.constants[f"constant:{category}.{key}"] = float(value)

    def value(self, token, actor):
        if token.startswith("constant:"):
            return self.constants[token]
        if token.startswith("global."):
            return self.global_values.get(token[7:], 0)
        if token == "THIS.id":
            return actor.id
        if token in self.temporary:
            return self.temporary[token]
        try:
            return float(token)
        except ValueError:
            return actor.values.get(token, 0)

    def condition(self, nodes, actor):
        for key, data in nodes:
            if key == "NOT":
                result = not self.condition(data, actor)
            elif key == "OR":
                result = any(self.condition([item], actor) for item in data)
            elif key in ("AND", "hidden_trigger"):
                # hidden_trigger only hides the tooltip; the engine evaluates it like AND.
                result = self.condition(data, actor)
            elif key == "any_of_scopes":
                array = dict(data)["array"]
                predicates = [(k, v) for k, v in data if k != "array"]
                result = any(self.condition(predicates, c) for c in self.value(array, actor))
            elif key == "check_variable":
                args = dict(data)
                comparisons = {
                    "equals": operator.eq, "less_than": operator.lt,
                    "greater_than": operator.gt, "less_than_or_equals": operator.le,
                    "greater_than_or_equals": operator.ge,
                }
                result = comparisons[args["compare"]](
                    self.value(args["var"], actor), self.value(args["value"], actor))
            elif key == "has_country_flag":
                result = data in actor.flags
            elif key == "has_global_flag":
                result = data in self.global_flags
            elif key == "has_event_target":
                result = data in self.targets
            elif key in ("exists", "is_subject", "has_capitulated"):
                actual = {"exists": actor.exists, "is_subject": actor.subject,
                          "has_capitulated": actor.capitulated}[key]
                result = actual == (data == "yes")
            else:
                raise AssertionError(f"Unchecked trigger: {key}")
            if not result:
                return False
        return True

    def run(self, name, actor):
        self.execute(self.effects[name], actor)

    def execute(self, nodes, actor):
        branch_taken = False
        for key, data in nodes:
            if key in ("if", "else_if", "else"):
                if key == "if":
                    branch_taken = False
                limit = next((v for k, v in data if k == "limit"), [])
                matched = (key == "if" or not branch_taken) and self.condition(limit, actor)
                if matched:
                    self.execute([(k, v) for k, v in data if k != "limit"], actor)
                    branch_taken = True
            elif key in ("set_variable", "set_temp_variable", "add_to_variable"):
                var, value = data[0]
                target = self.temporary if key == "set_temp_variable" else actor.values
                if var.startswith("global."):
                    target, var = self.global_values, var[7:]
                number = self.value(value, actor)
                target[var] = number + target.get(var, 0) if key == "add_to_variable" else number
            elif key in ("set_country_flag", "clr_country_flag"):
                (actor.flags.add if key.startswith("set") else actor.flags.discard)(data)
            elif key in ("set_global_flag", "clr_global_flag"):
                (self.global_flags.add if key.startswith("set") else self.global_flags.discard)(data)
            elif key == "save_global_event_target_as":
                self.targets[data] = actor
            elif key == "clear_global_event_target":
                self.targets.pop(data, None)
            elif key == "for_each_scope_loop":
                array = dict(data)["array"]
                for country in list(self.value(array, actor)):
                    self.execute([(k, v) for k, v in data if k != "array"], country)
            elif key.startswith("event_target:"):
                self.execute(data, self.targets[key.split(":", 1)[1]])
            elif key == "country_event" or key == "news_event":
                self.reports.append((actor.id, dict(data)["id"]))
            elif key == "chaosx_nr25_apply_winner_settlement":
                self.grants.append(actor.id)
                actor.flags.add("chaosx_nr25_winner_settlement_complete")
            elif key == "chaosx_nr25_apply_loser_settlement":
                actor.flags.add("chaosx_nr25_loser_settlement_complete")
            elif key in (
                "chaosx_nr25_remove_phase_missions", "chaosx_nr25_remove_final_missions",
                "chaosx_nr25_clear_selection_state", "chaosx_nr25_record_winner_history",
                "chaosx_nr25_clear_pending_evolutions",
            ):
                pass  # Separate effects, outside this arbitration fixture.
            elif key.startswith("chaosx_nr25_"):
                self.run(key.removeprefix("chaosx_nr25_"), actor)
            else:
                raise AssertionError(f"Unchecked effect: {key}")


def candidate(identifier, survey=30, readiness=70, outpost=40,
              exposure=15, ready_date=90, entry=None, day=100):
    values = dict(zip(("survey", "readiness", "outpost", "exposure", "ready_date"),
                      (survey, readiness, outpost, exposure, ready_date)))
    country = Country(identifier)
    country.values.update({f"chaosx_nr25_recovery_proof_{k}": v for k, v in values.items()})
    country.values["chaosx_nr25_entry_order"] = identifier if entry is None else entry
    country.values["chaosx_nr25_recovery_proof_day"] = day
    return country


class RecoveryTests(unittest.TestCase):
    def test_each_tie_breaker_and_registry_order(self):
        improvements = (
            {"survey": 31}, {"readiness": 71}, {"outpost": 41},
            {"exposure": 14}, {"ready_date": 89}, {"entry": 0},
        )
        for change in improvements:
            for reverse in (False, True):
                with self.subTest(change=change, reverse=reverse):
                    countries = [candidate(1), candidate(2, **change)]
                    if reverse:
                        countries.reverse()
                    rt = Runtime(countries)
                    rt.run("resolve_final_candidate", countries[0])
                    self.assertEqual(rt.grants, [2])

    def test_earlier_priority_overrides_later_priority(self):
        rt = Runtime([candidate(1, survey=31, readiness=60, exposure=80, entry=9),
                      candidate(2, survey=30, readiness=100, exposure=0, entry=0)])
        rt.run("resolve_final_candidate", rt.countries[0])
        self.assertEqual(rt.grants, [1])

    def test_invalid_first_finalist_promotes_valid_same_day_receipt(self):
        for invalid in ("exists", "subject", "capitulated", "terminal", "participant"):
            a, b = candidate(1, survey=99), candidate(2)
            if invalid == "terminal":
                a.flags.add("chaosx_nr25_terminal")
            elif invalid == "participant":
                a.flags.remove("chaosx_nr25_participant")
            else:
                setattr(a, invalid, invalid != "exists")
            rt = Runtime([a, b])
            rt.targets["chaosx_nr25_final_candidate_country"] = a
            rt.run("resolve_final_candidate", b)
            self.assertEqual(rt.grants, [2], invalid)

    def test_five_country_permutations_have_one_winner(self):
        countries = [candidate(i) for i in range(1, 6)]
        for ordering in permutations(countries):
            # Each fixture gets fresh flags so a previous outcome cannot leak.
            fresh = [candidate(c.id) for c in ordering]
            rt = Runtime(fresh)
            rt.run("resolve_final_candidate", fresh[0])
            self.assertEqual(rt.grants, [1])

    def test_next_day_receipt_cannot_replace_first_day(self):
        a = candidate(1)
        b = candidate(2, survey=99, day=101)
        rt = Runtime([a, b])
        rt.run("resolve_final_candidate", b)
        self.assertEqual(rt.grants, [1])

    def test_values_changed_after_submission_do_not_change_arbitration(self):
        a, b = candidate(1, survey=31), candidate(2, survey=30)
        a.values["chaosx_nr25_survey_evidence"] = 0
        b.values["chaosx_nr25_survey_evidence"] = 100
        rt = Runtime([a, b])
        rt.run("resolve_final_candidate", b)
        self.assertEqual(rt.grants, [1])

    def test_same_day_waits_and_multiple_callbacks_are_idempotent(self):
        countries = [candidate(1), candidate(2)]
        rt = Runtime(countries)
        rt.global_values["date"] = 100
        rt.run("resolve_final_candidate", countries[0])
        self.assertFalse(rt.grants)
        rt.global_values["date"] = 101
        for actor in countries * 3:
            rt.run("resolve_final_candidate", actor)
        self.assertEqual(rt.grants, [1])
        self.assertEqual(sum(e == "chaosx.news.26" for _, e in rt.reports), 1)
        self.assertEqual(rt.global_values["chaosx_nr25_winner"], 1)

    def test_no_valid_receipt_closes_without_main_reward(self):
        a = candidate(1)
        a.capitulated = True
        rt = Runtime([a])
        rt.run("resolve_final_candidate", a)
        self.assertFalse(rt.grants)
        self.assertNotIn("chaosx_nr25_active", rt.global_flags)
        self.assertIn("chaosx_nr25_closed_after_expeditions", rt.global_flags)

    def test_report_acknowledgement_has_no_grant_or_repeatable_news(self):
        text = EVENTS.read_text(encoding="utf-8-sig")
        for event_id, next_id in (("81", "82"), ("82", "83")):
            report = text.split(f"id = chaosx.nr25.{event_id}\n", 1)[1].split(
                f"id = chaosx.nr25.{next_id}\n", 1)[0]
            self.assertNotIn("chaosx_nr25_apply_winner_settlement = yes", report)
            self.assertNotIn("chaosx_nr25_apply_loser_settlement = yes", report)
            self.assertNotIn("news_event =", report)
            self.assertIn("_report_seen", report)


if __name__ == "__main__":
    unittest.main()
