"""Symbolic tests of the DW-089-S4 design, not a HOI4 implementation or simulator.

Run with Python 3 from any directory. All inputs are authored design fixtures.
No game, network, model provider, or connected repository is accessed.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from pathlib import Path
import json
import math
import re

RESULTS: list[dict[str, str]] = []


def check(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(name)
    RESULTS.append({"name": name, "status": "passed"})


def ceil_fraction(value: Fraction) -> int:
    return math.ceil(value)


@dataclass
class LivingGroup:
    """Whole individual identities in the proposed finite first-settlement model."""
    created: set[int]
    unsettled: set[int]
    settled: set[int] = field(default_factory=set)
    died_before_settlement: set[int] = field(default_factory=set)
    died_after_settlement: set[int] = field(default_factory=set)
    civilian: set[int] = field(default_factory=set)
    military: set[int] = field(default_factory=set)
    specialists: set[int] = field(default_factory=set)

    @classmethod
    def born(cls, count: int) -> LivingGroup:
        ids = set(range(count))
        return cls(created=ids, unsettled=set(ids))

    def admit(self, people: set[int], destination: str) -> bool:
        if destination not in {"civilian", "military"} or not people <= self.unsettled:
            return False
        self.unsettled -= people
        self.settled |= people
        getattr(self, destination).update(people)
        return True

    def qualify(self, people: set[int]) -> bool:
        if not people <= self.civilian or people & self.died_after_settlement:
            return False
        self.specialists |= people
        return True

    def lose_unsettled(self, people: set[int]) -> bool:
        if not people <= self.unsettled:
            return False
        self.unsettled -= people
        self.died_before_settlement |= people
        return True

    def lose_settled(self, people: set[int]) -> bool:
        if not people <= self.settled or people & self.died_after_settlement:
            return False
        self.died_after_settlement |= people
        self.civilian -= people
        self.military -= people
        self.specialists -= people
        return True

    def conserved(self) -> bool:
        parts = (self.unsettled, self.settled, self.died_before_settlement)
        return (set.union(*parts) == self.created
                and sum(map(len, parts)) == len(self.created))


@dataclass
class ServiceStock:
    available: set[int]
    assigned: dict[str, set[int]] = field(default_factory=dict)
    retired: set[int] = field(default_factory=set)

    def assign(self, job: str, units: set[int]) -> bool:
        if job in self.assigned or not units or not units <= self.available:
            return False
        self.available -= units
        self.assigned[job] = set(units)
        return True

    def retire(self, job: str) -> bool:
        if job not in self.assigned:
            return False
        self.retired |= self.assigned.pop(job)
        return True

    def conserved(self, original: set[int]) -> bool:
        parts = [self.available, self.retired, *self.assigned.values()]
        return set.union(*parts) == original and sum(map(len, parts)) == len(original)


@dataclass
class OwnerWork:
    live_burden: Fraction
    consumed: set[tuple[str, int]] = field(default_factory=set)

    def accept(self, job: str, generation: int, expected: int,
               offered: Fraction, valid: bool = True) -> Fraction:
        key = (job, generation)
        if not valid or generation != expected or key in self.consumed or offered < 0:
            return Fraction(0)
        actual = min(self.live_burden, offered)
        self.consumed.add(key)
        self.live_burden -= actual
        return actual


def receiving_capacity(shelter: int, food: int | None, clinical: int,
                       route_valid: bool) -> int:
    if food is None or not route_valid:
        return 0
    return max(0, min(shelter, food, clinical, 5000))


def main() -> None:
    root = Path(__file__).resolve().parents[4]
    part = root / "docs/specs/089_doctor_wu_specs/research/089_doctor_wu_spec_part_8_designed_life_and_biological_systems.md"
    text = part.read_text(encoding="utf-8")
    check("exact requested opening", text.startswith("# Doctor Wu: designed life and biological systems\n\n## Living systems beyond human replication\n"))
    check("fifteen separate project sections", re.findall(r"^## (L\d\d):", text, re.M) == [f"L{i:02}" for i in range(1, 16)])
    check("fifteen project-map rows", len(re.findall(r"^\| L\d\d \|", text, re.M)) == 15)
    check("twenty named AI scenarios", re.findall(r"^\| (S4-A\d\d)\b", text, re.M) == [f"S4-A{i:02}" for i in range(1, 21)])
    check("new prose punctuation", "—" not in text and ";" not in text)
    check("husbandry food conversion remains unapproved", "amount is deliberately left to a reviewed crosswalk" in text)
    check("exact transfer remains unresolved", "unresolved engine boundary" in text)
    check("no age identity reset", "reset the historical age and identity" in text)
    check("baseline access retained", "Calm World, low Authority, and disabled evolutions do not close these families" in text)

    profiles = {
        "substantial research": {"lane", "CIC", "support", "PP"},
        "exceptional research": {"lane", "CIC", "support", "PP"},
        "joint qualification": {"lane", "CIC", "support", "PP"},
        "service production": {"CIC", "support", "fuel", "clinical"},
        "cleanup production": {"CIC", "support", "fuel", "clinical"},
        "camouflage production": {"CIC", "support", "fuel", "clinical"},
        "recon animal production": {"CIC", "support", "fuel", "husbandry"},
        "support animal production": {"CIC", "support", "fuel", "husbandry"},
        "assault animal production": {"CIC", "support", "fuel", "husbandry"},
        "husbandry production": {"CIC", "support", "fuel", "food allocation"},
        "corrective qualification": {"lane", "CIC", "support", "PP"},
        "fixed installation": {"units", "clinical", "support", "fuel"},
        "fixed repair": {"CIC", "clinical", "support", "fuel"},
        "cleanup deployment": {"units", "clinical", "support", "fuel"},
        "cleanup recovery": {"team", "clinical", "support", "fuel"},
        "ward animal operation": {"animals", "handlers", "husbandry", "support"},
        "nonhuman clinic": {"patients", "CIC", "clinical", "support"},
        "recon assignment": {"animals", "handlers", "husbandry", "support"},
        "camouflage fitting": {"allocations", "clinical", "support", "CP"},
        "support commissioning": {"animals", "handlers", "support", "husbandry"},
        "assault commissioning": {"animals", "handlers", "support", "husbandry"},
        "assault preparation": {"formation", "husbandry", "support", "CP"},
        "assault recovery": {"formation", "CIC", "clinical", "support"},
        "tender construction": {"CIC", "robot equipment", "fuel", "clinical"},
        "observation works": {"CIC", "instruments", "fuel", "clinical"},
        "cradle works": {"CIC", "support", "fuel", "clinical"},
        "reconstruction": {"CIC", "support", "fuel", "PP"},
        "longevity": {"patient", "CIC", "clinical", "support"},
        "behavioural care": {"group", "CIC", "clinical", "support"},
    }
    for name, costs in profiles.items():
        check(f"four-cost admission: {name}", len(costs) <= 4)

    check("one unit covers only one tenth of a million", min(100000, 1000000) / 1000000 == .1)
    check("partial filter contribution", Fraction(1,2) * Fraction(100000,1000000) == Fraction(1,20))
    check("five-unit service-site capacity", 5 * 100000 == 500000)
    check("tender expands places but not organisms", 5 + 2 == 7)
    check("one purpose takes strongest contribution", max(Fraction(1,4),Fraction(1,2)) == Fraction(1,2))

    stock = ServiceStock(set(range(5)))
    check("first site assignment", stock.assign("port",{0,1,2}))
    check("same physical units unavailable elsewhere", not stock.assign("hospital",{2,3}))
    check("remaining real units can serve another site", stock.assign("hospital",{3,4}))
    check("stock conserved across active sites", stock.conserved(set(range(5))))
    check("retirement consumes only its assignment", stock.retire("port"))
    check("retired units cannot redeploy", not stock.assign("depot",{0}))
    check("retirement replay is harmless", not stock.retire("port"))
    check("stock conserved after retirement", stock.conserved(set(range(5))))

    cleanup = OwnerWork(Fraction(100))
    check("full work ceiling", cleanup.accept("district",1,1,Fraction(40)) == 40)
    check("accepted result replay cannot repeat", cleanup.accept("district",1,1,Fraction(40)) == 0)
    check("wrong generation cannot apply", cleanup.accept("new",2,3,Fraction(40)) == 0)
    check("invalid owner result cannot apply", cleanup.accept("invalid",1,1,Fraction(40),False) == 0)
    check("rejections leave live burden unchanged", cleanup.live_burden == 60)
    residual = OwnerWork(Fraction(20))
    check("cleanup capped at remaining burden", residual.accept("later",1,1,Fraction(40)) == 20)
    check("cleanup cannot create negative burden", residual.live_burden == 0)
    check("agriculture correct component only", 80 - Fraction(1,2)*40 == 60)
    check("partial scout return", Fraction(1,4)*Fraction(10,20) == Fraction(1,8))
    check("camouflage reference recipients", 10*500 == 5000)
    check("five thousand recipients still require ten allocations", ceil_fraction(Fraction(5000,500)) == 10)
    check("machine quarter-shorter time has four-thirds rate", 1/(1-Fraction(1,4)) == Fraction(4,3))
    check("machine and specialist rates do not compound", max(Fraction(5,4),Fraction(4,3)) == Fraction(4,3))
    check("ten serviced days preserve actual work only", 10*Fraction(4,3) == Fraction(40,3))
    check("resting animal bill rounds upward", ceil_fraction(Fraction(15,2)) == 8)
    check("all recon-team splits cannot reduce husbandry", all(ceil_fraction(Fraction(n,4))+ceil_fraction(Fraction(20-n,4)) >= 5 for n in range(1,20)))

    check("missing food proof blocks reception", receiving_capacity(5000,None,5000,True) == 0)
    check("lost route blocks reception", receiving_capacity(5000,5000,5000,False) == 0)
    check("limited clinical capacity limits district", receiving_capacity(5000,5000,2000,True) == 2000)
    check("planning ceiling cannot mint larger capacity", receiving_capacity(10000,10000,10000,True) == 5000)
    check("one shared reservation pool", 3000+1000+1000 == 5000)
    check("mixed arrivals leave real vacant places", 5000-2500-1000-1000 == 500)
    check("partial new arrivals leave unfilled places", 5000-2500-1000-900 == 600)

    group = LivingGroup.born(1000)
    check("initial birth conserved", group.conserved())
    check("civilian first settlement", group.admit(set(range(600)),"civilian"))
    check("external demand removed exactly once on civilian settlement", len(group.unsettled)+len(group.civilian)+len(group.military) == 1000)
    check("military first settlement of distinct people", group.admit(set(range(600,850)),"military"))
    check("civilian people cannot receive another first manpower credit", not group.admit({0},"military"))
    check("specialist role uses existing civilian identity", group.qualify(set(range(5))))
    check("role does not create people", len(group.created)==1000 and len(group.settled)==850)
    check("pre-settlement death debits actual unsettled people", group.lose_unsettled(set(range(850,860))))
    check("pre-settlement deaths cannot repeat", not group.lose_unsettled({850}))
    check("worked history equation", len(group.unsettled)==140 and len(group.settled)==850 and len(group.died_before_settlement)==10)
    check("first-settlement history conserved", group.conserved())
    check("later real civilian death", group.lose_settled({0}))
    check("later death preserves first-settlement history", len(group.settled)==850 and group.conserved())
    check("death cannot reopen entitlement", not group.admit({0},"civilian"))
    check("live food accounting excludes actual deaths", len(group.unsettled)+len(group.civilian)+len(group.military)==989)
    check("normal civilian production and orientation", 270+90==360)
    check("four reference cells produce at most a thousand people", 4*250==1000)

    output = {
        "stage":"DW-089-S4", "kind":"symbolic design fixtures",
        "count":len(RESULTS),"all_passed":True,
        "scope":"Authored arithmetic, cost-type inventories, and small abstract custody/work models only",
        "does_not_prove":["HOI4 engine effects", "actual AI probabilities", "game balance", "native population side effects", "actual unit transfer", "shared-owner acceptance", "MCP validation"],
        "results":RESULTS,
    }
    out = Path(__file__).with_name("2026-09-26_stage_4_design_fixture_results.json")
    out.write_text(json.dumps(output,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"count":len(RESULTS),"all_passed":True,"output":str(out)}))


if __name__ == "__main__":
    main()
