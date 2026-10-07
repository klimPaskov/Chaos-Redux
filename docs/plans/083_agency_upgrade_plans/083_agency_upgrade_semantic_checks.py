#!/usr/bin/env python3
"""Executable reference checks for the authored Event 83 behavior.

This is NOT HOI4 code, an engine adapter, a probability-service audit, or a
simulation of native operative recruitment. Synthetic upgrade names and
abstract claim tokens make the design's counting and lifetime rules testable.
Python 3.10+ and the standard library are sufficient.
"""
from __future__ import annotations
import argparse
from dataclasses import asdict, dataclass, field
from fractions import Fraction
import json
from pathlib import Path
import random
import sys
import unittest
from typing import Iterable

SIZES = (1, 2, 3, 5)
THRESHOLDS = (0, 200, 400, 600)
SPECIALTIES = {"network": 25, "preparation": 25, "counter": 15,
               "decryption": 15, "encryption": 15}
SUITE = {"network": 50, "preparation": 50, "counter": 25,
         "decryption": 25, "encryption": 25}


def select_tier(chaos: int, enabled: frozenset[int] = frozenset({1, 2, 3})) -> int:
    if chaos < 0 or not enabled <= {1, 2, 3}:
        raise ValueError("Invalid abstract Chaos value or evolution selection")
    return max([0] + [i for i in enabled if chaos >= THRESHOLDS[i]])


@dataclass(frozen=True)
class Increment:
    key: str
    prerequisites: frozenset[str] = frozenset()
    country: str | None = None


@dataclass(frozen=True)
class Bonus:
    category: str
    percent: int
    start: int
    expires: int


@dataclass(frozen=True)
class Receipt:
    tier: int
    upgrades: tuple[str, ...]
    conversions: tuple[str, ...]
    slots_added: int
    recruits_added: int


@dataclass
class Country:
    key: str
    exists: bool = True
    agency: bool = False
    owned: set[str] = field(default_factory=set)
    event_slots: int = 0
    pending: set[str] = field(default_factory=set)
    recruited: set[str] = field(default_factory=set)
    bonuses: list[Bonus] = field(default_factory=list)
    receipts: dict[str, Receipt] = field(default_factory=dict)
    usable: set[str] = field(default_factory=lambda: set(SPECIALTIES))
    other_owner_network: int = 0

    def active_percent(self, category: str, day: int) -> int:
        return sum(b.percent for b in self.bonuses
                   if b.category == category and b.start <= day < b.expires)

    def claim(self, token: str) -> bool:
        """Abstract entitlement consumption, not a native recruitment UI."""
        if token not in self.pending:
            return False
        self.pending.remove(token)
        self.recruited.add(token)
        return True


def validate_registry(registry: tuple[Increment, ...], expected: set[str]) -> None:
    keys = [i.key for i in registry]
    if len(keys) != len(set(keys)) or set(keys) != expected:
        raise ValueError("Synthetic registry coverage mismatch")
    if any(not i.prerequisites <= set(keys) for i in registry):
        raise ValueError("Unknown synthetic prerequisite")


def conversion_families(usable: set[str]) -> list[str]:
    families = ["slot"]
    families += [c for c in ("network", "preparation", "counter") if c in usable]
    if usable & {"decryption", "encryption"}:
        families.append("cryptology")
    return families


def award(country: Country, serial: str, tier: int, day: int,
          registry: tuple[Increment, ...], rng: random.Random) -> Receipt:
    if serial in country.receipts:
        return country.receipts[serial]
    if not country.exists or tier not in range(4):
        raise ValueError("Invalid abstract recipient or tier")
    size = SIZES[tier]
    country.agency = True
    start_slots = country.event_slots
    country.event_slots += size
    for i in range(size):
        country.pending.add(f"{country.key}:{serial}:recruit:{i}")
    upgrades: list[str] = []
    converted: list[str] = []
    for _ in range(size):
        eligible = sorted(i.key for i in registry
                          if i.key not in country.owned
                          and i.prerequisites <= country.owned
                          and i.country in (None, country.key))
        if eligible:
            selected = rng.choice(eligible)
            country.owned.add(selected)
            upgrades.append(selected)
        else:
            family = rng.choice(conversion_families(country.usable))
            if family == "slot":
                country.event_slots += 1
                converted.append("slot")
            else:
                category = (rng.choice(sorted(country.usable & {"decryption", "encryption"}))
                            if family == "cryptology" else family)
                country.bonuses.append(Bonus(category, SPECIALTIES[category], day, day + 90))
                converted.append(category)
    if tier == 2:
        candidates = sorted(country.usable & set(SPECIALTIES))
        if candidates:
            category = rng.choice(candidates)
            country.bonuses.append(Bonus(category, SPECIALTIES[category], day, day + 180))
        else:
            country.event_slots += 1
    elif tier == 3:
        for category, magnitude in SUITE.items():
            country.bonuses.append(Bonus(category, magnitude, day, day + 180))
    receipt = Receipt(tier, tuple(upgrades), tuple(converted),
                      country.event_slots - start_slots, size)
    country.receipts[serial] = receipt
    return receipt


@dataclass
class World:
    chaos: int
    countries: dict[str, Country]
    committed: set[str] = field(default_factory=set)
    capability: bool = True

    def fire(self, serial: str, day: int, registry: tuple[Increment, ...],
             rng: random.Random, enabled: frozenset[int] = frozenset({1, 2, 3})) -> None:
        if serial in self.committed:
            return
        if not self.capability:
            raise ValueError("Global capability preflight failed")
        tier = select_tier(self.chaos, enabled)
        recipients = [c for _, c in sorted(self.countries.items()) if c.exists]
        if not recipients:
            raise ValueError("No existing recipients")
        for country in recipients:
            award(country, serial, tier, day, registry, rng)
        self.chaos += 5
        self.committed.add(serial)

    def save(self) -> str:
        states = {}
        for key, country in self.countries.items():
            record = asdict(country)
            for name in ("owned", "pending", "recruited", "usable"):
                record[name] = sorted(record[name])
            states[key] = record
        return json.dumps({"chaos": self.chaos, "countries": states,
                           "committed": sorted(self.committed), "capability": self.capability}, sort_keys=True)

    @classmethod
    def load(cls, text: str) -> World:
        data = json.loads(text)
        countries = {}
        for key, raw in data["countries"].items():
            for name in ("owned", "pending", "recruited", "usable"):
                raw[name] = set(raw[name])
            raw["bonuses"] = [Bonus(**b) for b in raw["bonuses"]]
            raw["receipts"] = {serial: Receipt(r["tier"], tuple(r["upgrades"]),
                                tuple(r["conversions"]), r["slots_added"], r["recruits_added"])
                               for serial, r in raw["receipts"].items()}
            countries[key] = Country(**raw)
        return cls(data["chaos"], countries, set(data["committed"]), data["capability"])


class Prefer(random.Random):
    """Force an eligible family where possible to exercise duplicate outcomes."""
    def __init__(self, preference: str):
        super().__init__(0)
        self.preference = preference

    def choice(self, seq):
        return self.preference if self.preference in seq else seq[0]


OPEN = tuple(Increment(f"synthetic_{i}") for i in range(12))
CHAIN = (Increment("branch_1"), Increment("branch_2", frozenset({"branch_1"})),
         Increment("branch_3", frozenset({"branch_2"})))


class DesignChecks(unittest.TestCase):
    def test_01_thresholds(self):
        self.assertEqual([select_tier(n) for n in (0, 199, 200, 399, 400, 599, 600, 999)],
                         [0, 0, 1, 1, 2, 2, 3, 3])

    def test_02_independent_enable_controls(self):
        self.assertEqual(select_tier(650, frozenset({2})), 2)
        self.assertEqual(select_tier(650, frozenset({3})), 3)
        self.assertEqual(select_tier(650, frozenset()), 0)

    def test_03_new_agency_does_not_consume_roll(self):
        c = Country("A")
        r = award(c, "1", 0, 0, OPEN, random.Random(1))
        self.assertTrue(c.agency)
        self.assertEqual((len(r.upgrades), c.event_slots, len(c.pending)), (1, 1, 1))

    def test_04_replacement_package_not_twelve(self):
        c = Country("A")
        r = award(c, "1", 3, 0, OPEN, random.Random(2))
        self.assertEqual((len(r.upgrades), r.slots_added, r.recruits_added), (5, 5, 5))

    def test_05_no_owned_or_same_firing_duplicate(self):
        c = Country("A", owned={"synthetic_0"})
        r = award(c, "1", 3, 0, OPEN, random.Random(3))
        self.assertEqual(len(set(r.upgrades)), 5)
        self.assertNotIn("synthetic_0", r.upgrades)

    def test_06_prerequisite_recomputed_per_draw(self):
        c = Country("A")
        r = award(c, "1", 2, 0, CHAIN, random.Random(4))
        self.assertEqual(r.upgrades, ("branch_1", "branch_2", "branch_3"))

    def test_07_two_remaining_three_conversions(self):
        c = Country("A")
        r = award(c, "1", 3, 0, OPEN[:2], Prefer("slot"))
        self.assertEqual((len(r.upgrades), len(r.conversions), r.slots_added, r.recruits_added), (2, 3, 8, 5))

    def test_08_exhaustion_every_package(self):
        for tier, size in enumerate(SIZES):
            with self.subTest(tier=tier):
                c = Country("A")
                r = award(c, "1", tier, 0, (), Prefer("slot"))
                self.assertEqual((len(r.conversions), r.recruits_added), (size, size))
                self.assertEqual(r.slots_added, size * 2)

    def test_09_native_candidate_entitlements_are_distinct(self):
        # Only abstract entitlement identity is tested, not native recruitment.
        c = Country("A")
        award(c, "1", 3, 0, OPEN, random.Random(5))
        award(c, "2", 3, 1, OPEN, random.Random(6))
        self.assertEqual(len(c.pending), 10)
        self.assertTrue(all(c.claim(token) for token in list(c.pending)))
        self.assertEqual(len(c.recruited), 10)

    def test_10_claim_cannot_be_redeemed_twice(self):
        c = Country("A")
        award(c, "1", 0, 0, OPEN, random.Random(7))
        token = next(iter(c.pending))
        self.assertTrue(c.claim(token))
        self.assertFalse(c.claim(token))

    def test_11_duplicate_recipient_is_idempotent(self):
        c = Country("A")
        first = award(c, "1", 3, 0, OPEN, random.Random(8))
        second = award(c, "1", 0, 50, OPEN, random.Random(9))
        self.assertEqual(first, second)
        self.assertEqual((c.event_slots, len(c.pending)), (5, 5))

    def test_12_world_chaos_once_not_per_country(self):
        w = World(0, {k: Country(k) for k in ("A", "B", "C")})
        w.fire("1", 0, OPEN, random.Random(10))
        w.fire("1", 0, OPEN, random.Random(11))
        self.assertEqual(w.chaos, 5)
        self.assertEqual([c.event_slots for c in w.countries.values()], [1, 1, 1])

    def test_13_tier_snapshot_before_own_chaos(self):
        w = World(198, {"A": Country("A"), "B": Country("B")})
        w.fire("1", 0, OPEN, random.Random(12))
        self.assertEqual(w.chaos, 203)
        self.assertEqual([c.receipts["1"].tier for c in w.countries.values()], [0, 0])
        w.fire("2", 1, OPEN, random.Random(13))
        self.assertEqual(w.countries["A"].receipts["2"].tier, 1)

    def test_14_fixed_suite_exact(self):
        c = Country("A")
        award(c, "1", 3, 0, OPEN, random.Random(14))
        self.assertEqual({k: c.active_percent(k, 0) for k in SUITE}, SUITE)
        self.assertEqual({k: c.active_percent(k, 180) for k in SUITE}, {k: 0 for k in SUITE})

    def test_15_duplicate_network_conversions_add(self):
        c = Country("A")
        award(c, "1", 3, 0, OPEN[:3], Prefer("network"))
        self.assertEqual(c.active_percent("network", 0), 100)
        self.assertEqual(c.active_percent("network", 89), 100)
        self.assertEqual(c.active_percent("network", 90), 50)
        self.assertEqual(c.active_percent("network", 180), 0)

    def test_16_staggered_expiration_no_refresh(self):
        c = Country("A")
        award(c, "1", 3, 0, OPEN, random.Random(15))
        award(c, "2", 3, 60, OPEN, random.Random(16))
        self.assertEqual([c.active_percent("network", t) for t in (59, 60, 179, 180, 239, 240)],
                         [50, 100, 100, 50, 50, 0])

    def test_17_capacity_survives_expiration(self):
        c = Country("A")
        award(c, "1", 3, 0, OPEN, random.Random(17))
        self.assertEqual(c.active_percent("network", 1000), 0)
        self.assertEqual(c.event_slots, 5)

    def test_18_other_owner_preserved(self):
        c = Country("A", other_owner_network=35)
        award(c, "1", 3, 0, OPEN, random.Random(18))
        self.assertEqual(c.other_owner_network, 35)
        self.assertEqual(c.active_percent("network", 180) + c.other_owner_network, 35)

    def test_19_restricted_families(self):
        self.assertEqual(conversion_families(set()), ["slot"])
        self.assertEqual(conversion_families({"network", "encryption"}), ["slot", "network", "cryptology"])

    def test_20_cryptology_with_one_usable_branch(self):
        c = Country("A", usable={"encryption"})
        r = award(c, "1", 0, 0, (), Prefer("cryptology"))
        self.assertEqual(r.conversions, ("encryption",))
        self.assertEqual(c.active_percent("encryption", 0), 15)

    def test_21_specialty_is_one_eligible_bonus(self):
        c = Country("A", usable={"counter"})
        award(c, "1", 2, 0, OPEN, random.Random(19))
        self.assertEqual(c.bonuses, [Bonus("counter", 15, 0, 180)])

    def test_22_no_usable_specialty_exception(self):
        c = Country("A", usable=set())
        r = award(c, "1", 2, 0, OPEN, random.Random(20))
        self.assertEqual((r.slots_added, r.recruits_added, len(c.bonuses)), (4, 3, 0))

    def test_23_country_restriction(self):
        registry = (Increment("A_only", country="A"), Increment("universal"))
        c = Country("B")
        r = award(c, "1", 1, 0, registry, Prefer("slot"))
        self.assertEqual(r.upgrades, ("universal",))
        self.assertEqual(r.conversions, ("slot",))

    def test_24_dormant_country_excluded(self):
        w = World(0, {"A": Country("A"), "Z": Country("Z", exists=False)})
        w.fire("1", 0, OPEN, random.Random(21))
        self.assertFalse(w.countries["Z"].agency)
        self.assertFalse(w.countries["Z"].receipts)

    def test_25_capability_failure_no_mutation(self):
        w = World(600, {"A": Country("A")}, capability=False)
        before = w.save()
        with self.assertRaises(ValueError):
            w.fire("1", 0, OPEN, random.Random(22))
        self.assertEqual(w.save(), before)

    def test_26_registry_coverage_failure(self):
        with self.assertRaises(ValueError):
            validate_registry(OPEN[:2], {i.key for i in OPEN})
        validate_registry(OPEN, {i.key for i in OPEN})

    def test_27_json_roundtrip_claims_and_expirations(self):
        w = World(600, {"A": Country("A")})
        w.fire("1", 0, OPEN, random.Random(23))
        c = w.countries["A"]
        token = next(iter(c.pending))
        c.claim(token)
        restored = World.load(w.save())
        restored.fire("1", 60, OPEN, random.Random(24))
        rc = restored.countries["A"]
        self.assertEqual((restored.chaos, len(rc.pending), len(rc.recruited)), (605, 4, 1))
        self.assertFalse(rc.claim(token))
        self.assertEqual([rc.active_percent("network", t) for t in (179, 180)], [50, 0])

    def test_28_exact_design_probability_arithmetic(self):
        self.assertEqual(Fraction(1, 5) * Fraction(1, 2), Fraction(1, 10))
        self.assertEqual(5 * Fraction(1, 5), 1)
        self.assertEqual(1 - Fraction(4, 5) ** 5, Fraction(2101, 3125))
        self.assertEqual(float(1 - Fraction(4, 5) ** 5) * 100, 67.232)

    def test_29_later_weaker_package_does_not_revoke(self):
        c = Country("A")
        award(c, "1", 3, 0, OPEN, random.Random(25))
        award(c, "2", 0, 10, OPEN, random.Random(26))
        self.assertEqual((c.event_slots, len(c.pending), c.active_percent("network", 10)), (6, 6, 50))

    def test_30_same_day_separate_firings(self):
        w = World(600, {"A": Country("A")})
        w.fire("1", 0, OPEN, random.Random(27))
        w.fire("2", 0, OPEN, random.Random(28))
        self.assertEqual((w.chaos, w.countries["A"].event_slots), (610, 10))
        self.assertEqual(w.countries["A"].active_percent("network", 0), 100)
        self.assertEqual(w.countries["A"].active_percent("network", 180), 0)


def flatten(suite: unittest.TestSuite) -> Iterable[str]:
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from flatten(item)
        else:
            yield item.id()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, help="Optional JSON result path")
    args = parser.parse_args()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(DesignChecks)
    names = list(flatten(suite))
    result = unittest.TextTestRunner(verbosity=2, stream=sys.stdout).run(suite)
    report = {"evidence_type": "abstract_design_reference_tests_not_HOI4",
              "tests_run": result.testsRun, "failures": len(result.failures),
              "errors": len(result.errors), "successful": result.wasSuccessful(),
              "test_names": names,
              "limitations": ["No HOI4 execution", "No native recruitment UI validation",
                              "No engine modifier-key validation", "No actual upgrade database coverage",
                              "No native save compatibility proof", "No multiplayer proof",
                              "No independent subagent or MCP probability audit"]}
    if args.report:
        args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
