"""Generate the exact Event 015 decision, mission, and category icon handoff.

The output is documentation-only. The parent implementation agent owns adding
the corresponding ``icon =`` assignments to gameplay script.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[4]
DECISION_FILE = REPO_ROOT / "common/decisions/015_utopia_manifesto_decisions.txt"
OUTPUT = REPO_ROOT / "docs/assets/015_utopia_manifesto/decision_icon_mapping.csv"

CATEGORY_SPRITES = {
    "utopia_manifesto_ledger_category": "decision_category_utopia_ledger",
    "utopia_manifesto_district_category": "decision_category_utopia_district",
    "utopia_manifesto_island_category": "decision_category_utopia_island",
    "utopia_manifesto_necessary_ground_category": "decision_category_utopia_necessary_ground",
    "utopia_manifesto_stewardship_category": "decision_category_utopia_stewardship",
    "utopia_manifesto_league_category": "decision_category_utopia_league",
    "utopia_manifesto_defense_category": "decision_category_utopia_defense",
    "utopia_manifesto_governance_category": "decision_category_utopia_governance",
    "utopia_manifesto_formation_category": "decision_category_utopia_formation",
}

ENTRY_GROUPS = {
    "decision_utopia_household_census": [
        "decision_utopia_count_houses_and_hands",
        "mission_utopia_count_houses_and_hands",
        "decision_utopia_recount_the_country",
        "decision_utopia_extend_the_service_register",
    ],
    "decision_utopia_publish_accounts": [
        "decision_utopia_publish_the_accounts",
        "decision_utopia_publish_corrected_tenure_tables",
    ],
    "decision_utopia_common_storehouse": [
        "decision_utopia_establish_capital_store",
        "mission_utopia_establish_capital_store",
    ],
    "decision_utopia_seasonal_reserve": [
        "decision_utopia_fill_seasonal_reserve",
        "mission_utopia_fill_seasonal_reserve",
        "decision_utopia_two_years_against_hunger",
        "mission_utopia_two_years_against_hunger",
        "decision_utopia_complete_capital_provision_ring",
    ],
    "decision_utopia_rural_rotation": [
        "decision_utopia_rotate_old_stores",
    ],
    "decision_utopia_open_stores": [
        "decision_utopia_release_emergency_stores",
    ],
    "decision_utopia_local_store": [
        "decision_utopia_select_provisioning_calling",
    ],
    "decision_utopia_fund_apprenticeships": [
        "decision_utopia_select_workshops_calling",
        "decision_utopia_select_learning_and_care_calling",
    ],
    "decision_utopia_common_administration": [
        "decision_utopia_select_civic_works_calling",
        "decision_utopia_convene_the_calling_councils",
    ],
    "decision_utopia_guard_shore": [
        "decision_utopia_select_maritime_and_settlement_calling",
        "decision_utopia_fortify_without_sealing",
        "decision_utopia_close_the_gates",
    ],
    "decision_utopia_household_guard": [
        "decision_utopia_select_defense_and_watches_calling",
        "decision_utopia_clean_up_stewardship_revolt",
        "decision_utopia_call_mutual_defense_council",
        "decision_utopia_guard_the_common_stores",
        "mission_utopia_guard_the_common_stores",
    ],
    "decision_utopia_collect_petitions": [
        "decision_utopia_issue_open_call",
        "mission_utopia_wait_for_need_answer",
    ],
    "decision_utopia_local_households": [
        "decision_utopia_guarantee_placement",
        "decision_utopia_offer_stewardship_autonomy",
    ],
    "decision_utopia_urgent_service": [
        "decision_utopia_set_assignment_quota",
        "decision_utopia_emergency_calling_levy",
        "mission_utopia_fill_unpopular_calling",
        "decision_utopia_suspend_the_short_day",
        "mission_utopia_short_day_suspension",
    ],
    "decision_utopia_second_trade": [
        "decision_utopia_prove_every_calling_chosen",
        "mission_utopia_sustain_every_calling_chosen",
        "decision_utopia_learn_second_trade",
        "mission_utopia_learn_second_trade",
    ],
    "decision_utopia_land_register": [
        "decision_utopia_register_public_land",
        "mission_utopia_register_public_land",
        "decision_utopia_convert_estate_to_land_trust",
        "decision_utopia_transfer_factory_to_worker_council",
        "decision_utopia_assign_productive_tenure",
        "decision_utopia_revoke_idle_grant",
        "mission_utopia_property_transition",
    ],
    "decision_utopia_district_survey": [
        "decision_utopia_survey_district_site",
        "mission_utopia_survey_district_site",
    ],
    "decision_utopia_district_foundation": [
        "decision_utopia_found_market_garden_district",
        "decision_utopia_found_industrial_housing_district",
        "decision_utopia_found_rail_junction_town",
        "decision_utopia_found_refugee_municipality",
        "mission_utopia_build_garden_district",
    ],
    "decision_utopia_settlement_charter": [
        "decision_utopia_complete_district_charter",
        "mission_utopia_complete_district_charter",
        "decision_utopia_confirm_stewardship_obligation",
        "decision_utopia_restore_stewardship_route",
        "mission_utopia_restore_stewardship_route",
        "decision_utopia_convene_local_charter",
        "decision_utopia_hold_charter_period",
        "mission_utopia_hold_charter_period",
        "decision_utopia_refresh_post_formation_charters",
    ],
    "decision_utopia_island_project": [
        "decision_utopia_prepare_national_island_variant",
        "decision_utopia_adopt_existing_island_capital",
        "decision_utopia_adopt_coastal_refuge",
        "decision_utopia_adopt_inland_island",
        "decision_utopia_secure_island_site",
        "mission_utopia_build_island_stage",
        "decision_utopia_make_an_island",
        "mission_utopia_make_an_island",
    ],
    "decision_utopia_common_harbor": [
        "decision_utopia_build_common_harbor",
    ],
    "decision_utopia_inland_terminal": [
        "decision_utopia_build_inland_terminal",
    ],
    "decision_utopia_mark_needed_district": [
        "decision_utopia_select_necessary_ground_target",
        "decision_utopia_clear_necessary_ground_target",
        "decision_utopia_survey_domestic_alternatives",
        "mission_utopia_survey_domestic_alternatives",
    ],
    "decision_utopia_need_case": [
        "decision_utopia_draft_need_case",
        "decision_utopia_select_need_case_state",
        "mission_utopia_need_case_expiry",
    ],
    "decision_utopia_purchase": [
        "decision_utopia_offer_purchase",
        "decision_utopia_offer_long_supply_contract",
    ],
    "decision_utopia_lease": [
        "decision_utopia_request_lease",
        "decision_utopia_convert_case_to_lease",
    ],
    "decision_utopia_joint_administration": [
        "decision_utopia_propose_joint_administration",
        "decision_utopia_convert_case_to_joint_administration",
    ],
    "decision_utopia_recognize_friend": [
        "decision_utopia_invite_associate_municipality",
        "decision_utopia_initialize_league",
        "decision_utopia_invite_to_league",
        "mission_utopia_league_invitation_answer",
    ],
    "decision_utopia_just_cause_review": [
        "decision_utopia_revise_need_offer",
        "decision_utopia_prove_league_not_mask",
        "mission_utopia_prove_league_not_mask",
        "decision_utopia_prove_the_commonwealth",
        "mission_utopia_prove_the_commonwealth",
    ],
    "decision_utopia_ultimatum": [
        "decision_utopia_issue_need_ultimatum",
        "decision_utopia_enforce_need_case",
    ],
    "decision_utopia_renunciation_vote": [
        "decision_utopia_renounce_need_case",
        "decision_utopia_hold_stewardship_status_vote",
        "decision_utopia_return_stewardship",
        "decision_utopia_expel_exploitative_member",
    ],
    "decision_utopia_emergency_provision": [
        "decision_utopia_begin_emergency_provision",
        "mission_utopia_emergency_provision",
    ],
    "decision_utopia_send_magistrates": [
        "decision_utopia_impose_assigned_administration",
    ],
    "decision_utopia_long_integration": [
        "decision_utopia_begin_long_integration",
        "mission_utopia_long_integration",
        "decision_utopia_integrate_post_formation_institutions",
    ],
    "decision_utopia_storehouse_aid": [
        "decision_utopia_send_surplus_abroad",
    ],
    "decision_utopia_technical_mission": [
        "decision_utopia_send_technical_mission",
        "mission_utopia_technical_mission",
    ],
    "decision_utopia_reserve_compact": [
        "decision_utopia_open_reserve_compact",
        "mission_utopia_reserve_compact_answer",
    ],
    "decision_utopia_engineer_companies": [
        "decision_utopia_pool_reconstruction_brigades",
        "decision_utopia_form_engineer_companies",
        "mission_utopia_form_engineer_companies",
    ],
    "decision_utopia_league_aid_corridor": [
        "decision_utopia_accept_league_sponsorship",
    ],
    "decision_utopia_citizen_watch": [
        "decision_utopia_raise_a_citizen_watch",
        "mission_utopia_raise_a_citizen_watch",
        "decision_utopia_reinforce_post_formation_defense",
    ],
    "decision_utopia_auxiliary_contract": [
        "decision_utopia_hire_auxiliary_contracts",
        "decision_utopia_end_the_auxiliary_contract",
        "mission_utopia_end_the_auxiliary_contract",
    ],
    "decision_utopia_constitutional_correction": [
        "decision_utopia_open_constitutional_correction",
        "mission_utopia_constitutional_correction",
        "decision_utopia_call_a_household_referendum",
        "decision_utopia_add_a_sunset_clause",
    ],
    "decision_utopia_storehouse_audit": [
        "decision_utopia_request_a_new_forecast",
    ],
    "decision_utopia_boundary_arbitration": [
        "decision_utopia_negotiate_district_appeals",
    ],
    "decision_utopia_formation_proclamation": [
        "decision_utopia_proclaim_the_commonwealth",
    ],
}


def strip_comment(line: str) -> str:
    return line.split("#", 1)[0]


def parse_decisions() -> tuple[list[str], list[tuple[str, str]]]:
    text = DECISION_FILE.read_text(encoding="utf-8-sig")
    categories: list[str] = []
    entries: list[tuple[str, str]] = []
    depth = 0
    current_category: str | None = None
    assignment = re.compile(r"^([a-z0-9_]+)\s*=\s*\{")
    for raw_line in text.splitlines():
        code = strip_comment(raw_line).strip()
        match = assignment.match(code)
        if match:
            identifier = match.group(1)
            if depth == 0 and identifier.endswith("_category"):
                current_category = identifier
                categories.append(identifier)
            elif depth == 1 and current_category:
                entries.append((current_category, identifier))
        depth += code.count("{") - code.count("}")
        if depth == 0:
            current_category = None
    return categories, entries


def flatten_entry_mapping() -> dict[str, str]:
    mapping: dict[str, str] = {}
    for sprite, identifiers in ENTRY_GROUPS.items():
        for identifier in identifiers:
            if identifier in mapping:
                raise ValueError(f"Duplicate mapping for {identifier}")
            mapping[identifier] = sprite
    return mapping


def asset_file(sprite: str) -> str:
    return f"gfx/interface/decisions/015_utopia_manifesto/{sprite}.dds"


def source_family(sprite: str) -> str:
    generated = {
        "decision_category_utopia_district",
        "decision_category_utopia_island",
        "decision_category_utopia_necessary_ground",
        "decision_category_utopia_stewardship",
        "decision_category_utopia_defense",
        "decision_category_utopia_governance",
        "decision_category_utopia_formation",
        "decision_utopia_publish_accounts",
        "decision_utopia_seasonal_reserve",
        "decision_utopia_second_trade",
        "decision_utopia_land_register",
        "decision_utopia_district_survey",
        "decision_utopia_district_foundation",
        "decision_utopia_island_project",
        "decision_utopia_common_harbor",
        "decision_utopia_inland_terminal",
        "decision_utopia_need_case",
        "decision_utopia_purchase",
        "decision_utopia_lease",
        "decision_utopia_joint_administration",
        "decision_utopia_ultimatum",
        "decision_utopia_emergency_provision",
        "decision_utopia_long_integration",
        "decision_utopia_technical_mission",
        "decision_utopia_reserve_compact",
        "decision_utopia_citizen_watch",
        "decision_utopia_engineer_companies",
        "decision_utopia_auxiliary_contract",
        "decision_utopia_constitutional_correction",
        "decision_utopia_formation_proclamation",
    }
    return "imagegen_final_atlas_2026-07-14" if sprite in generated else "existing_event_015_final_family"


def main() -> None:
    categories, entries = parse_decisions()
    entry_mapping = flatten_entry_mapping()
    parsed_ids = {identifier for _, identifier in entries}
    missing_categories = set(categories) - set(CATEGORY_SPRITES)
    extra_categories = set(CATEGORY_SPRITES) - set(categories)
    missing_entries = parsed_ids - set(entry_mapping)
    stale_entries = set(entry_mapping) - parsed_ids
    if missing_categories or extra_categories or missing_entries or stale_entries:
        raise ValueError(
            "Mapping drift: "
            f"missing_categories={sorted(missing_categories)}, "
            f"extra_categories={sorted(extra_categories)}, "
            f"missing_entries={sorted(missing_entries)}, "
            f"stale_entries={sorted(stale_entries)}"
        )
    if len(categories) != 9 or len(entries) != 130:
        raise ValueError(
            f"Expected 9 categories and 130 entries; got {len(categories)} and {len(entries)}"
        )
    mission_count = sum(identifier.startswith("mission_") for _, identifier in entries)
    if mission_count != 32:
        raise ValueError(f"Expected 32 missions; got {mission_count}")

    fields = [
        "entry_type",
        "category_id",
        "script_id",
        "sprite_name",
        "icon_value",
        "asset_file",
        "source_family",
    ]
    rows: list[dict[str, str]] = []
    for category_id in categories:
        sprite = CATEGORY_SPRITES[category_id]
        rows.append(
            {
                "entry_type": "category",
                "category_id": category_id,
                "script_id": category_id,
                "sprite_name": f"GFX_{sprite}",
                "icon_value": f"GFX_{sprite}",
                "asset_file": asset_file(sprite),
                "source_family": source_family(sprite),
            }
        )
    for category_id, identifier in entries:
        sprite = entry_mapping[identifier]
        rows.append(
            {
                "entry_type": "mission" if identifier.startswith("mission_") else "decision",
                "category_id": category_id,
                "script_id": identifier,
                "sprite_name": f"GFX_{sprite}",
                "icon_value": f"GFX_{sprite}",
                "asset_file": asset_file(sprite),
                "source_family": source_family(sprite),
            }
        )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(
        f"Wrote {len(rows)} rows: {len(categories)} categories, "
        f"{len(entries) - mission_count} decisions, {mission_count} missions."
    )


if __name__ == "__main__":
    main()
