"""Event 35 visible-action budget (part 3, Decision-surface budget).

Evaluates the production visibility rules of every ordinary decision in the
Great Depression category against fixture countries and counts what a human
player sees in each phase, with and without each evolution. Partner-targeted
decisions are counted once each, assuming one valid partner exists; state-targeted
decisions are evaluated against one selected center in each physical stage.
The center selector and the missions are not counted.

Budget:
  national actions (no target)        at most 5; six while the doctrine is chosen and during an emergency
                                      (Economic Paralysis, an open social incident, the worldwide depression)
  partner actions (country targeted)  at most 5, six during the worldwide depression
  selected-center operations          at most 6

Run directly with --table to print the measured peaks.
"""
import collections
import sys
import unittest

import test_event035_center_projects as H

DECISIONS = H.ROOT / "common/decisions/035_great_depression_decisions.txt"
SELECTOR = "great_depression_select_depression_center"
STAGES = ("distressed", "idled", "shuttered", "abandoned")
DOCTRINES = (1, 2, 3, 4, 5, 6)
UNASSIGNED = 0
EVOLUTIONS = {
    "baseline": dict(evo=0),
    "contagion": dict(evo=1),
    "social_early": dict(evo=2, social=1),
    "social_late": dict(evo=2, social=3),
    "worldwide_shock": dict(evo=3, gstage=1),
    "worldwide_coordination": dict(evo=3, gstage=3),
    "worldwide_recovery": dict(evo=3, gstage=4),
}


class SurfaceRuntime(H.Event35Runtime):
    """Adds the `FROM` selector of target decisions and owner-read fixtures."""

    def __init__(self):
        super().__init__()
        self.from_scope = None

    def _condition(self, node, scope):
        key = node.key
        if key == "FROM" and node.op == "=":
            if self.from_scope is None:
                return True  # a valid partner is assumed to exist
            self.scope_stack.append(self.from_scope)
            try:
                return self._conditions(node.value, self.from_scope)
            finally:
                self.scope_stack.pop()
        if key == "any_controlled_state":
            for candidate in scope.values.get("owned_states", []):
                self.scope_stack.append(candidate)
                try:
                    if self._conditions(node.value, candidate):
                        return True
                finally:
                    self.scope_stack.pop()
            return False
        if key in ("is_major", "is_subject_of", "is_ally_with", "is_in_faction_with"):
            return True
        return super()._condition(node, scope)


_RUNTIME = None
_ENTRIES = None


def runtime():
    global _RUNTIME
    if _RUNTIME is None:
        _RUNTIME = SurfaceRuntime()
    return _RUNTIME


def entries():
    global _ENTRIES
    if _ENTRIES is None:
        tokens = H.lex(H.uncomment(DECISIONS.read_text(encoding="utf-8-sig")))
        nodes, _ = H.parse_nodes(tokens, 0, "decisions")
        category = next(n for n in nodes if n.key == "great_depression_category")
        _ENTRIES = [
            n for n in category.value
            if isinstance(n.value, list)
            and H.first(n.value, "days_mission_timeout") is None  # missions
            and H.first(n.value, "icon") is not None
        ]
    return _ENTRIES


def kind_of(entry):
    if any(n.key == "state_target" for n in entry.value):
        return "center"
    if H.first(entry.value, "target_trigger") is not None:
        return "partner"
    return "national"


def build(phase, doctrine, stage, evo=0, social=None, gstage=None):
    rt = runtime()
    real = H.Event35Runtime
    H.Event35Runtime = lambda: None  # registered_case would parse every source file again
    try:
        _unused, owner, site = H.registered_case(stage=stage)
    finally:
        H.Event35Runtime = real
    rt.globals = {"num_days": 300}
    rt.global_arrays = {}
    rt.global_flags = set()
    rt.temp_frames = [{}]
    rt.call_stack = []
    owner.values.update({
        "great_depression_phase": phase,
        "great_depression_doctrine": doctrine,
        "great_depression_evolution_floor": evo,
        "num_of_factories": 30,
    })
    if evo >= 1:
        owner.flags.add("great_depression_evolution_financial_contagion")
    if evo >= 2:
        owner.flags.add("great_depression_evolution_social_collapse")
        if social is not None:
            owner.flags.add("great_depression_social_incident_open")
            owner.values["great_depression_social_ladder_stage"] = social
    if evo >= 3:
        owner.flags.add("great_depression_evolution_second_great_depression")
        rt.global_flags.add("great_depression_worldwide_episode_active")
        rt.globals["great_depression_global_stage"] = gstage
        rt.globals["great_depression_global_episode_id"] = 1
    return rt, owner, site


def is_visible(rt, owner, site, entry):
    body = entry.value
    rt.root = owner
    rt.scope_stack = [owner]
    rt.from_scope = None
    target_root, target, visible = (H.first(body, key) for key in ("target_root_trigger", "target_trigger", "visible"))
    try:
        if target_root is not None and not rt._conditions(target_root, owner):
            return False
        if kind_of(entry) == "center":
            rt.from_scope = site
            if target is not None and not rt._conditions(target, owner):
                return False
        return visible is None or rt._conditions(visible, owner)
    finally:
        rt.from_scope = None


def visible_groups(phase, doctrine, stage, **evolution):
    rt, owner, site = build(phase, doctrine, stage, **evolution)
    groups = collections.defaultdict(list)
    for entry in entries():
        if is_visible(rt, owner, site, entry):
            groups["selector" if entry.key == SELECTOR else kind_of(entry)].append(entry.key)
    return groups


def peaks(doctrines=DOCTRINES):
    """Largest visible group per phase and evolution over doctrines and center stages."""
    result = {}
    for phase in range(1, 6):
        for name, evolution in EVOLUTIONS.items():
            peak = {"national": [], "partner": [], "center": []}
            for doctrine in doctrines:
                for stage in STAGES:
                    groups = visible_groups(phase, doctrine, stage, **evolution)
                    for kind in peak:
                        if len(groups[kind]) > len(peak[kind]) :
                            peak[kind] = groups[kind]
            result[(phase, name)] = peak
    return result


class VisibleActionBudgetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.peaks = peaks()
        cls.unassigned = {name: visible_groups(1, UNASSIGNED, stage, **evolution)
                          for name, evolution in EVOLUTIONS.items() for stage in ("shuttered",)}

    def test_national_actions_stay_within_budget(self):
        for (phase, name), peak in self.peaks.items():
            limit = 6 if name.startswith(("social", "worldwide")) or phase == 5 else 5
            with self.subTest(phase=phase, evolution=name):
                self.assertLessEqual(len(peak["national"]), limit, peak["national"])

    def test_doctrine_choice_shows_only_the_six_choices(self):
        for name, groups in self.unassigned.items():
            with self.subTest(evolution=name):
                self.assertEqual(len(groups["national"]), 6, groups["national"])
                self.assertTrue(all("_choose_" in action for action in groups["national"]))
                self.assertEqual(groups["partner"], [])

    def test_partner_actions_stay_within_budget(self):
        for (phase, name), peak in self.peaks.items():
            limit = 6 if name.startswith("worldwide") else 5
            with self.subTest(phase=phase, evolution=name):
                self.assertLessEqual(len(peak["partner"]), limit, peak["partner"])

    def test_selected_center_operations_stay_within_six(self):
        for (phase, name), peak in self.peaks.items():
            with self.subTest(phase=phase, evolution=name):
                self.assertLessEqual(len(peak["center"]), 6, peak["center"])

    def test_recovery_offers_no_new_center_operations(self):
        for name in EVOLUTIONS:
            self.assertEqual(self.peaks[(4, name)]["center"], [], name)

    def test_reopen_and_rebuild_split_by_stage(self):
        reopen, rebuild = "great_depression_reopen_idled_plants", "great_depression_rebuild_shuttered_center"
        idled = visible_groups(2, 1, "idled")["center"]
        shuttered = visible_groups(2, 1, "shuttered")["center"]
        self.assertIn(reopen, idled)
        self.assertNotIn(rebuild, idled)
        self.assertIn(rebuild, shuttered)
        self.assertNotIn(reopen, shuttered)


def print_table():
    table = peaks()
    print("phase evolution: national / partner / center")
    for (phase, name), peak in table.items():
        print(f"P{phase} {name}: {len(peak['national'])} / {len(peak['partner'])} / {len(peak['center'])}")


if __name__ == "__main__":
    if "--table" in sys.argv:
        sys.argv.remove("--table")
        print_table()
    else:
        unittest.main(verbosity=2)
