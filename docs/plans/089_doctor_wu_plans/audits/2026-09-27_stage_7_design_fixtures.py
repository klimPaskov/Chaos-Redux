"""Symbolic Doctor Wu design fixtures. These do not execute HOI4 or its scripts.

Run this file in the extracted cumulative package. It checks its own illustrative
models and protected input bytes. Passing results do not validate a native API.
"""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import hashlib
import json
import re

PROTECTED = {'docs/plans/089_doctor_wu_plans/source_inputs/2026-09-24_doctor_wu_user_brief.txt': 'c4198c71de96ba6e9eb52bf2abada028b87b24cc5d6b4abbd1b7096a706821e1', 'docs/specs/089_doctor_wu_specs/core/089_doctor_wu_spec_part_1_core.md': '68731605426172e8c2290e38be48fc24ca128c13a71562c5df2b90bdf3668186', 'docs/specs/089_doctor_wu_specs/core/089_doctor_wu_spec_part_2_institute_and_authority.md': '83756dee7f6d855a0ec55cbea92fd586688051932cb19163e053f0b1a34378d8', 'docs/specs/089_doctor_wu_specs/medicine/089_doctor_wu_spec_part_3_universal_cures.md': '17ae5ba2371d369ac6c8ce1555f164c437dcfd5660bfdcf5d6eb72225dd96130', 'docs/specs/089_doctor_wu_specs/medicine/089_doctor_wu_spec_part_4_production_and_access.md': '57931714e52e5eb56afb374fa7ef47e275093d3d134e90ab557326a20ab44740', 'docs/specs/089_doctor_wu_specs/rivalry/089_doctor_wu_spec_part_10_wu_and_kruger.md': '8e0fa41ff9e1ef957d0d13abe339ff735f897d15fd3e5e376c98a748562ac95d', 'docs/specs/089_doctor_wu_specs/research/089_doctor_wu_spec_part_9_modified_capabilities_and_strain_ownership.md': '901682b7455bbd340e4e3d0d85aa007fd376c626d59153c1baee97130bd0af18', 'docs/specs/089_doctor_wu_specs/research/089_doctor_wu_spec_part_6_military_medicine_and_controlled_biology.md': '97d47644b6462aa7ce18af8b0b273350b81ab460354c489a629cae2e53b15e20', 'docs/specs/089_doctor_wu_specs/research/089_doctor_wu_spec_part_5_baseline_medical_research.md': '6e615cea0649f10bddb97f8668b753d8144bc339f32a96690bc1590568682c27', 'docs/specs/089_doctor_wu_specs/research/089_doctor_wu_spec_part_8_designed_life_and_biological_systems.md': '912cf42b74e0565f081f617f7cf3edbb58d4b9a493770e484125e0a67b4db1dd', 'docs/specs/089_doctor_wu_specs/research/089_doctor_wu_spec_part_7_replication_and_continuity.md': 'cc6e0693ba81c6d82de243a5d2b6865aff617d130bbf77e0ab29e63e0f5ef6f1'}
ROOT = Path(__file__).resolve().parents[4]
PART = ROOT / "docs/specs/089_doctor_wu_specs/foreign/089_doctor_wu_spec_part_11_foreign_medicine_and_scientific_competition.md"
RESULT = Path(__file__).with_name("2026-09-27_stage_7_design_fixture_results.json")
checks: list[dict] = []


def check(name: str, passed: bool, observed: object, kind: str = "symbolic") -> None:
    checks.append({"name": name, "kind": kind, "passed": bool(passed), "observed": observed})


@dataclass(frozen=True)
class Receipt:
    actor: int
    host: int
    generation: int
    case: int
    subject: int
    phase: str


def matches(left: Receipt, right: Receipt) -> bool:
    return left == right


def admission(capacity: int, occupied: int, requested: int, food_proven: bool) -> int:
    if min(capacity, occupied, requested) < 0:
        raise ValueError("Counts must be nonnegative")
    return min(requested, max(0, capacity - occupied)) if food_proven else 0


def safe_handover(deadline: int, qualified_at: int, arrived_at: int, handover_days: int) -> bool:
    if min(deadline, qualified_at, arrived_at, handover_days) < 0:
        raise ValueError("Dates and durations must be nonnegative")
    return max(qualified_at, arrived_at) + handover_days <= deadline


def main() -> int:
    text = PART.read_text(encoding="utf-8")
    check("Exact opening headings", text.startswith("# Doctor Wu: foreign medicine and scientific competition\n\n## What other governments can obtain\n"), text.splitlines()[:3], "document")
    headings = re.findall(r"^## (F[0-9]{2})[.]", text, re.M)
    check("Seventeen complete action-family headings", headings == [f"F{i:02}" for i in range(1, 18)], headings, "document")
    ai = sorted(set(re.findall(r"FAI[0-9]{2}", text)))
    check("Thirty-six named scenario identifiers", ai == [f"FAI{i:02}" for i in range(1, 37)], ai, "document")
    check("Exact stopping heading", re.findall(r"^## (.*)$", text, re.M)[-1] == "What international medicine leaves for national ascendancy", re.findall(r"^## (.*)$", text, re.M)[-1], "document")
    check("New prose punctuation", chr(0x2014) not in text and ";" not in text, {"em_dash": text.count(chr(0x2014)), "semicolon": text.count(";")}, "document")
    preservation = {}
    for path, expected in PROTECTED.items():
        p = ROOT / path
        preservation[path] = p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == expected
    check("Parts 1–10 and original brief preserved", len(preservation) == 11 and all(preservation.values()), preservation, "preservation")

    # Quoted costs for newly proposed actions. Native-owner actions are excluded
    # because their complete implementation costs have not been validated here.
    cost_types = {
        "F01 new dispatch": ["allocation", "team", "transport", "fuel"],
        "F03 teaching": ["civilian_factory", "support_equipment", "teaching_team"],
        "F03 sponsor travel": ["transport", "fuel"],
        "F04 review": ["political_power", "support_equipment"],
        "F04 physical transfer": ["material", "transport", "fuel", "custody_service"],
        "F05 new embedded dispatch": ["care_stock", "team", "transport", "fuel"],
        "F06 access conference": ["political_power", "civilian_factory"],
        "F07 standing protection": ["political_power", "civilian_factory"],
        "F08 open recruitment": ["political_power", "support_equipment", "civilian_factory"],
        "F08 covert recruitment": ["political_power", "support_equipment", "civilian_factory", "operative"],
        "F09 archive theft": ["political_power", "support_equipment", "operative"],
        "F10 abduction": ["political_power", "support_equipment", "operative"],
        "F11 assassination": ["political_power", "support_equipment", "operative"],
        "F12 review": ["political_power", "support_equipment", "civilian_factory"],
        "F15 foundation": ["political_power", "civilian_factory"],
        "F17 evaluation": ["civilian_factory", "support_equipment", "evaluation_team"]
    }
    check("New action cost inventory within four types", all(len(set(v)) <= 4 for v in cost_types.values()), {k: len(set(v)) for k, v in cost_types.items()}, "design inventory")

    principal, deposit, quantity, unit_price = 200, 100, 10, 20
    delivered = 6
    earned = delivered * unit_price
    check("Six allocations earn 120 principal", earned == 120, earned)
    check("Six-allocation closure owes 20 more", max(0, earned - deposit) == 20, max(0, earned - deposit))
    check("Four allocations remain worth 80", principal - earned == 80 and quantity - delivered == 4, {"unearned_principal": principal-earned, "undelivered": quantity-delivered})
    earned = 4 * unit_price
    restitution = max(0, deposit-earned)
    check("Four-allocation closure owes restitution 20", restitution == 20, restitution)
    actual_seller_stock = 0
    paid_restitution = min(restitution, actual_seller_stock)
    check("Unpaid restitution creates no stock", paid_restitution == 0 and restitution-paid_restitution == 20, {"paid": paid_restitution, "remaining_claim": restitution-paid_restitution})

    initial, native_reserved, other_reserved = 120, 40, 30
    available = initial-native_reserved-other_reserved
    transferred = 20
    check("Reserved items excluded from availability", available == 50, available)
    check("Overdraw transfer rejected in model", not 51 <= available, {"request": 51, "available": available})
    available -= transferred
    standard_at_reservation = "A"
    works_standard = "B"
    check("Retooling leaves reservation identity intact", standard_at_reservation == "A" and works_standard == "B", {"reserved": standard_at_reservation, "works": works_standard})
    consumed = native_reserved
    native_reserved = 0
    check("Completed native-model accounting conserves 120", available + other_reserved + transferred + consumed == initial, {"available_A": available, "other_reserved_A": other_reserved, "foreign_A": transferred, "consumed_A": consumed})
    script_refund = 0
    check("No second Wu native debit or refund in model", available == 30 and script_refund == 0, {"available": available, "script_refund": script_refund})

    count = admission(5000, 3500, 1600, True)
    check("Receiving places shared by all origins", count == 1500, count)
    check("Unadmitted finite people remain in custody", 1600-count == 100, 1600-count)
    check("Missing food proof admits nobody", admission(5000, 0, 1600, False) == 0, admission(5000, 0, 1600, False))
    check("Full reception has no spare places", admission(5000, 5000, 1600, True) == 0, admission(5000, 5000, 1600, True))
    origin_debit, route_deaths = 1000, 20
    survivor_credit = origin_debit-route_deaths
    check("Settled movement conserves population", survivor_credit == 980 and survivor_credit+route_deaths == origin_debit, {"debit": origin_debit, "deaths": route_deaths, "survivors": survivor_credit})
    named_person_overlay_credit = 0
    check("Roster transfer does not duplicate included survivor", survivor_credit+named_person_overlay_credit == 980, survivor_credit+named_person_overlay_credit)
    unsettled = 80
    origin_population_debit = 0
    first_settled = 30
    unsettled -= first_settled
    check("Unsettled movement uses no fake civilian origin", origin_population_debit == 0 and unsettled+first_settled == 80, {"origin_debit": origin_population_debit, "unsettled": unsettled, "first_settled": first_settled})

    check("Ninety-day qualification misses forty-five-day care", not safe_handover(45,90,15,15), safe_handover(45,90,15,15))
    check("Existing qualified provider can complete a real handover", safe_handover(45,0,15,15), {"completion": 30, "deadline": 45})
    check("Exact care deadline accepted", safe_handover(45,0,30,15), safe_handover(45,0,30,15))
    check("One day late is not safe completion", not safe_handover(45,0,31,15), safe_handover(45,0,31,15))

    original = Receipt(1,2,3,4,5,"response")
    check("Exact response receipt accepted", matches(original, Receipt(1,2,3,4,5,"response")), True)
    check("Re-released host cannot answer old response", not matches(original, Receipt(1,2,4,4,5,"response")), False)
    check("Different person cannot replace target", not matches(original, Receipt(1,2,3,4,6,"response")), False)
    check("Old result phase cannot accept offer", not matches(original, Receipt(1,2,3,4,5,"settled")), False)
    claims = {"condemnation", "air_treaty", "great_embargo", "external"}
    claims.discard("condemnation")
    check("Own sanction release preserves other claims", claims == {"air_treaty","great_embargo","external"}, sorted(claims))
    carveout = True
    transfer_exception = False
    check("Carve-out is not transfer proof", carveout and not transfer_exception, {"carveout": carveout, "transfer_exception": transfer_exception})
    purposes = {"clinical"}
    check("Clinical access grants no military purpose", "military" not in purposes and "archive" not in purposes, sorted(purposes))
    existing_people = {"Wu-A": "living", "Wu-B": "qualified_living"}
    existing_people["Wu-A"] = "confirmed_dead"
    check("One confirmed death leaves existing copy independent", existing_people == {"Wu-A":"confirmed_dead","Wu-B":"qualified_living"}, existing_people)
    appointed = False
    captive = True
    check("Custody alone is not an appointment", captive and not appointed, {"captive":captive,"appointed":appointed})
    check("New prose covers provisional refuge explicitly", "A provisional refuge can be accepted" in text and "wait 90 days" in text, "provisional refuge and standing institution separated", "document")

    result = {"stage":"DW-089-S7", "scope":"Symbolic design models, document structure, and protected bytes only", "native_game_execution":False, "tests":checks, "passed":all(x["passed"] for x in checks), "check_count":len(checks), "new_part_words":len(text.split()), "full_specification_words":sum(len(p.read_text(encoding="utf-8").split()) for p in (ROOT/"docs/specs/089_doctor_wu_specs").rglob("*part_*.md"))}
    RESULT.write_text(json.dumps(result, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    print(json.dumps({"passed":result["passed"],"checks":len(checks),"new_part_words":result["new_part_words"],"total_spec_words":result["full_specification_words"]}))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
