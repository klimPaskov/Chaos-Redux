"""Build the Event 016 decision and decision-category icon package.

The three generated atlas PNGs are retained as immutable source evidence. Each
tile is cropped to its own source master, keyed with the official imagegen
chroma-key helper, normalized to the exact HOI4 surface size, converted to DDS
with the repository converter, and recorded in a machine-checkable ledger.
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[4]
SRC_D = ROOT / "docs/assets/016_brilliant_scientist/source_png/decision_icons"
SRC_C = ROOT / "docs/assets/016_brilliant_scientist/source_png/decision_categories"
PROC_D = ROOT / "docs/assets/016_brilliant_scientist/processed_png/decision_icons"
PROC_C = ROOT / "docs/assets/016_brilliant_scientist/processed_png/decision_categories"
ALPHA_D = ROOT / "docs/assets/016_brilliant_scientist/alpha_png/decision_icons"
ALPHA_C = ROOT / "docs/assets/016_brilliant_scientist/alpha_png/decision_categories"
RUNTIME_D = ROOT / "gfx/interface/decisions/016_brilliant_scientist/decisions"
RUNTIME_C = ROOT / "gfx/interface/decisions/016_brilliant_scientist/categories"
CONTACT = ROOT / "docs/assets/016_brilliant_scientist/contact_sheets"
RECORDS = ROOT / "docs/assets/016_brilliant_scientist/package_records"
VALIDATION = ROOT / "docs/assets/016_brilliant_scientist/validation"
REMOVE_KEY = Path(r"C:/Users/klimp/.codex/skills/.system/imagegen/scripts/remove_chroma_key.py")
CONVERTER = ROOT / ".agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py"

DECISION_SPRITES = [
    ("foundation_repair", "foundation repair, state-system initialization"),
    ("power_grid_relay", "power-grid restoration and independent reactor network"),
    ("rail_port_link", "rail, port, and transit logistics"),
    ("supply_depot", "supply spine, transport, and containment logistics"),
    ("hardened_laboratory", "laboratory hardening and secure command doors"),
    ("prototype_press", "prototype works and fabrication press"),
    ("staff_recruitment", "staff, handlers, scientists, and specialists"),
    ("scientific_assembly", "scientific councils, assemblies, and synthesis boards"),
    ("publication", "decrees, ledgers, demonstrations, and public method"),
    ("compartmentalized_network", "compartmentalization and restricted networks"),
    ("security_assignment", "guards, officers, air warning, and counterintelligence"),
    ("relocation_convoy", "relocation and evacuation movement"),
    ("foreign_invitation", "foreign registry and recognition invitations"),
    ("archive_theft", "foreign intelligence and archive theft"),
    ("sabotage_charge", "sabotage and coalition disruption"),
    ("protection_pact", "protection, security corridor, and scientific compact"),
    ("project_approval", "project demonstrations, approvals, and activation"),
    ("project_suspension", "interrupted-project review and pause authority"),
    ("independent_replication", "independent replication and autonomous research"),
    ("charter_negotiation", "charter, administration, settlement, and submission"),
    ("confinement", "containment, closure, and confining a dangerous node"),
    ("assassination", "last-resort raid or targeted removal authority"),
    ("military_seizure", "military seizure, conquest administration, and field takeover"),
    ("clone_growth", "bounded clone growth and maturation"),
    ("robot_assembly", "robot frames, repair, and autonomous assembly"),
    ("paleogenetic_hatchery", "paleogenetic reserve, hatchery, breeding, and handlers"),
    ("xenobiological_vat", "xenobiological vat, medical fabrication, and control"),
    ("portal_terminal", "portal terminals, rings, transit batches, and insertion"),
    ("temporal_anchor", "temporal anchors, observation, ledgers, and succession"),
    ("exotic_guard", "exotic interface specialists and guard batches"),
    ("biological_quarantine", "biological quarantine and lockdown"),
    ("singularity_component", "singularity intelligence, audits, and world-order review"),
    ("singularity_arming", "arming, fail-deadly activation, and detonation protocol"),
    ("controlled_disarmament", "controlled disarmament and non-terminal settlement"),
    ("archive_recovery", "archive recovery and interrupted-project evidence"),
    ("staff_rotation", "ministry consolidation, officer recall, and network staffing"),
    ("facility_hardening", "engineer support, maintenance, and structural hardening"),
    ("emergency_containment", "emergency response, breach closure, and incident missions"),
    ("foreign_extraction", "strategic insertion and extracting foreign personnel"),
    ("project_unit_deployment", "project-army recruitment and field deployment"),
]
CATEGORY_SPRITES = [
    ("foundation_administration", "brilliant_scientist_krg_foundation_category"),
    ("security_logistics", "brilliant_scientist_krg_security_and_logistics_category"),
    ("clone_machine", "brilliant_scientist_krg_clone_and_machine_category"),
    ("paleogenetics", "brilliant_scientist_krg_paleogenetics_category"),
    ("xenobiology", "brilliant_scientist_krg_xenobiology_category"),
    ("portal_temporal", "brilliant_scientist_krg_portal_and_temporal_category"),
    ("exotic_biological", "brilliant_scientist_krg_exotic_and_biological_category"),
    ("foreign_policy", "brilliant_scientist_krg_foreign_policy_category"),
    ("integration", "brilliant_scientist_krg_integration_category"),
    ("terminal_program", "brilliant_scientist_krg_terminal_program_category"),
]

ATLAS_1 = SRC_D / "decision_icons_atlas_01_source.png"
ATLAS_2 = SRC_D / "decision_icons_atlas_02_source.png"
ATLAS_C = SRC_C / "decision_categories_atlas_source.png"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def crop_atlas(source: Path, out_dir: Path, names: list[str], cols: int, rows: int, bounds: tuple[list[int], list[int]]) -> None:
    image = Image.open(source).convert("RGB")
    xs, ys = bounds
    for i, name in enumerate(names):
        row, col = divmod(i, cols)
        tile = image.crop((xs[col] + 3, ys[row] + 3, xs[col + 1] - 3, ys[row + 1] - 3))
        tile.save(out_dir / f"{name}_source.png")


def key_tile(source: Path, alpha_path: Path) -> None:
    subprocess.run(
        ["python", str(REMOVE_KEY), "--input", str(source), "--out", str(alpha_path),
         "--auto-key", "border", "--soft-matte", "--transparent-threshold", "12",
         "--opaque-threshold", "220", "--edge-contract", "1", "--despill", "--force"],
        check=True,
    )


def normalize(alpha_path: Path, out_path: Path, size: tuple[int, int]) -> None:
    source = Image.open(alpha_path).convert("RGBA")
    # The atlas tile is square. Keep the complete emblem and letterbox only for
    # the 50x40 category surface, matching vanilla category framing.
    if size[0] == size[1]:
        result = source.resize(size, Image.Resampling.LANCZOS)
    else:
        inner = source.resize((size[0] - 6, size[1] - 4), Image.Resampling.LANCZOS)
        result = Image.new("RGBA", size, (0, 0, 0, 0))
        result.alpha_composite(inner, ((size[0] - inner.width) // 2, (size[1] - inner.height) // 2))
    # The generated deep-green background and dark bronze paint can leave the
    # chroma-key helper's matte below 255 even across the emblem core. Normalize
    # the retained alpha matte so the icon has an actual opaque interior while
    # preserving all edge gradations and transparent corners.
    alpha = result.getchannel("A")
    maximum = alpha.getextrema()[1]
    if maximum and maximum < 255:
        alpha = alpha.point(lambda value: min(255, round(value * 255 / maximum)))
        result.putalpha(alpha)
    # Keep the four texture corners fully transparent, matching vanilla icon
    # framing and preventing a one-pixel matte leak after DDS conversion.
    alpha = result.getchannel("A")
    for point in [(0, 0), (result.width - 1, 0), (0, result.height - 1), (result.width - 1, result.height - 1)]:
        alpha.putpixel(point, 0)
    result.putalpha(alpha)
    result.save(out_path)


def dds(processed: Path, output: Path, size: tuple[int, int]) -> None:
    subprocess.run(["python", "-B", str(CONVERTER), "--input", str(processed), "--output", str(output), "--width", str(size[0]), "--height", str(size[1])], check=True)


def alpha_bbox(path: Path) -> tuple[int, int, int, int] | None:
    a = Image.open(path).convert("RGBA").getchannel("A")
    return a.getbbox()


def load_decision_ids() -> list[str]:
    ids: list[str] = []
    for path in sorted((ROOT / "common/decisions").glob("016_brilliant_scientist_kruger_state_*.txt")):
        for line in path.read_text(encoding="utf-8").splitlines():
            match = re.match(r"^\t([^\t#][^=]+) = \{$", line)
            if match:
                ids.append(match.group(1).strip())
    return ids


def assign(identifier: str) -> str:
    # Narrow overrides preserve semantics for IDs whose name is not enough.
    overrides = {
        "brilliant_scientist_krg_review_interrupted_project_audit": "project_suspension",
        "brilliant_scientist_krg_secure_enclave_corridor": "hardened_laboratory",
        "brilliant_scientist_krg_begin_ministry_consolidation": "staff_rotation",
        "brilliant_scientist_krg_ministry_consolidation_mission": "staff_rotation",
        "brilliant_scientist_krg_convene_founding_audit": "publication",
        "brilliant_scientist_krg_define_constitutional_purpose": "charter_negotiation",
        "brilliant_scientist_krg_issue_laboratory_decrees": "publication",
        "brilliant_scientist_krg_write_conventional_battle_plans": "military_seizure",
        "brilliant_scientist_krg_recall_defector_officers": "staff_rotation",
        "brilliant_scientist_krg_begin_primary_facility_defense": "security_assignment",
        "brilliant_scientist_krg_primary_facility_defense_mission": "emergency_containment",
        "brilliant_scientist_krg_establish_air_warning_network": "security_assignment",
        "brilliant_scientist_krg_open_foreign_interest_registry": "foreign_invitation",
        "brilliant_scientist_krg_clean_invalid_foreign_target": "foreign_invitation",
        "brilliant_scientist_krg_seek_formal_recognition": "foreign_invitation",
        "brilliant_scientist_krg_settle_accounts_with_former_host": "assassination",
        "brilliant_scientist_krg_issue_submission_ultimatum": "charter_negotiation",
        "brilliant_scientist_krg_secure_laboratory_corridor": "protection_pact",
        "brilliant_scientist_krg_integrate_state_by_project": "military_seizure",
        "brilliant_scientist_krg_activate_world_conquest_administration": "military_seizure",
        "brilliant_scientist_krg_establish_paleogenetic_veterinary_support": "staff_recruitment",
        "brilliant_scientist_krg_execute_paleogenetic_escape_response": "emergency_containment",
        "brilliant_scientist_krg_evacuate_and_recapture_paleogenetic_site": "relocation_convoy",
        "brilliant_scientist_krg_clone_drift_review_mission": "independent_replication",
        "brilliant_scientist_krg_execute_strategic_insertion": "foreign_extraction",
        "brilliant_scientist_krg_temporal_rescue_survival_mission": "foreign_extraction",
        "brilliant_scientist_krg_begin_temporal_stabilization_supervision": "temporal_anchor",
        "brilliant_scientist_krg_temporal_stabilization_supervision_mission": "temporal_anchor",
        "brilliant_scientist_krg_settle_temporal_succession": "charter_negotiation",
        "brilliant_scientist_krg_open_canonical_last_resort_raid_authority": "assassination",
        "brilliant_scientist_krg_disrupt_containment_coalition_planning": "sabotage_charge",
        "brilliant_scientist_krg_administer_accepted_submissions": "charter_negotiation",
        "brilliant_scientist_krg_arbitrate_synthesis_project_burdens": "charter_negotiation",
        "brilliant_scientist_krg_quarantine_and_sequence_clone_lineages": "biological_quarantine",
        "brilliant_scientist_krg_isolate_rogue_machine_node": "emergency_containment",
        "brilliant_scientist_krg_service_primary_facility": "foundation_repair",
        "brilliant_scientist_krg_seal_transit_breach": "portal_terminal",
    }
    if identifier in overrides:
        return overrides[identifier]
    s = identifier
    ordered = [
        ("recruit_interface_specialist", "exotic_guard"), ("fabricate_exotic_guard_batch", "exotic_guard"),
        ("designate_clone_growth_site", "clone_growth"), ("write_clone_identity_register", "publication"),
        ("bounded_clone_growth_cycle", "clone_growth"), ("clone_drift_review", "archive_recovery"),
        ("clone_identity_pressure", "confinement"), ("reconcile_clone_identity_pressure", "confinement"),
        ("clone_personhood_hearing", "charter_negotiation"), ("clone_settlements", "charter_negotiation"),
        ("clone_maturation_priority", "clone_growth"), ("clone_property_prohibition", "charter_negotiation"),
        ("clone_population_transition", "clone_growth"), ("machine_power_node", "power_grid_relay"),
        ("bounded_robot_assembly", "robot_assembly"), ("frame_repair", "facility_hardening"),
        ("machine_command_protocol", "compartmentalized_network"), ("human_supervisory_keys", "security_assignment"),
        ("rogue_node_containment", "confinement"), ("rogue_node_containment_mission", "emergency_containment"),
        ("red_team_autonomous_nest", "security_assignment"), ("machine_network", "scientific_assembly"),
        ("ministry_replacement", "staff_rotation"), ("machine_population_transition", "robot_assembly"),
        ("continuity_network_government", "charter_negotiation"),
        ("foreign_intelligence_operation", "archive_theft"), ("voluntary_scientific_compact", "protection_pact"),
        ("recover_stolen_facility_archive", "archive_recovery"), ("pay_expansion_maintenance", "supply_depot"),
        ("refresh_continental_administration", "charter_negotiation"),
        ("initialize_state_systems", "foundation_repair"), ("ratify_charter_transfer_network", "charter_negotiation"),
        ("count_and_recruit_surviving_staff", "staff_recruitment"), ("convene_scientific_assembly", "scientific_assembly"),
        ("stage_public_project_demonstration", "project_approval"), ("restore_human_civil_service", "staff_recruitment"),
        ("repair_primary_site", "foundation_repair"), ("restore_power_grid", "power_grid_relay"),
        ("reconnect_rail_and_port", "rail_port_link"), ("repair_supply_spine", "supply_depot"),
        ("reopen_prototype_works", "prototype_press"), ("laboratory_guard_recruitment", "security_assignment"),
        ("guard_training_cycle", "security_assignment"), ("engineer_support", "facility_hardening"),
        ("counterintelligence_sweep", "security_assignment"), ("coordinate_project_commanders", "project_unit_deployment"),
        ("maintenance_audit", "facility_hardening"),
        ("paleogenetic_reserve", "paleogenetic_hatchery"), ("paleogenetic_hatchery", "paleogenetic_hatchery"),
        ("paleogenetic_handler", "staff_recruitment"), ("paleogenetic_transport_pen", "supply_depot"),
        ("paleogenetic_shock_pack", "project_unit_deployment"), ("paleogenetic_breeding_cycle", "paleogenetic_hatchery"),
        ("paleogenetic_escape_response", "emergency_containment"), ("construct_xenobiological_vat", "xenobiological_vat"),
        ("xenobiological_medical_fabrication", "xenobiological_vat"), ("xenobiological_control_mode", "xenobiological_vat"),
        ("xenobiological_assault_recruitment", "project_unit_deployment"), ("xenobiological_production_cycle", "xenobiological_vat"),
        ("engineered_population_transition", "xenobiological_vat"),
        ("audit_transit_logs", "portal_terminal"), ("construct_transit_terminal", "portal_terminal"),
        ("harden_terminal_rings", "facility_hardening"), ("link_terminal_supply_network", "supply_depot"),
        ("transit_breach_closure", "emergency_containment"), ("fabricate_portal_transit_batch", "portal_terminal"),
        ("discover_temporal_anchor", "temporal_anchor"), ("authenticate_temporal_anchor", "temporal_anchor"),
        ("temporal_observer_teams", "temporal_anchor"), ("synchronization_bureau", "temporal_anchor"),
        ("bounded_future_warning", "temporal_anchor"), ("fabricate_temporal_guard_batch", "temporal_anchor"),
        ("authenticate_kruger_continuity", "temporal_anchor"), ("independent_reactor_grid", "power_grid_relay"),
        ("consequence_ledger", "publication"), ("dual_key", "controlled_disarmament"),
        ("restricted_delivery_chain", "compartmentalized_network"), ("restricted_material_custody", "archive_recovery"),
        ("compartmentalize_restricted_network", "compartmentalized_network"), ("segregate_containment_logistics", "supply_depot"),
        ("harden_restricted_command_node", "facility_hardening"), ("quarantine_and_lockdown", "biological_quarantine"),
        ("global_submission_administration", "charter_negotiation"), ("project_synthesis_council", "scientific_assembly"),
        ("singularity_component_intelligence", "singularity_component"), ("singularity_facility_intelligence", "singularity_component"),
        ("singularity_arming", "singularity_arming"), ("singularity_fail_deadly", "singularity_arming"),
        ("deliberate_singularity_detonation", "singularity_arming"), ("controlled_singularity_disarmament", "controlled_disarmament"),
        ("laboratory_world_order", "singularity_component"), ("complete_laboratory_world", "singularity_component"),
        ("singularity_disarmament_hold", "controlled_disarmament"), ("durable_nonterminal_settlement", "controlled_disarmament"),
    ]
    for token, sprite in ordered:
        if token in s:
            return sprite
    raise KeyError(f"No semantic sprite assignment for {identifier}")


def make_contact(paths: list[tuple[str, Path]], out: Path, title: str, columns: int = 8) -> None:
    thumbs: list[tuple[str, Image.Image]] = []
    for label, path in paths:
        thumbs.append((label, Image.open(path).convert("RGBA")))
    cell_w, cell_h = 160, 150
    rows = (len(thumbs) + columns - 1) // columns
    sheet = Image.new("RGBA", (columns * cell_w, rows * cell_h + 30), (26, 28, 30, 255))
    draw = ImageDraw.Draw(sheet)
    draw.text((10, 7), title, fill=(240, 240, 240, 255))
    for i, (label, image) in enumerate(thumbs):
        row, col = divmod(i, columns)
        image.thumbnail((128, 112), Image.Resampling.NEAREST)
        x = col * cell_w + (cell_w - image.width) // 2
        y = row * cell_h + 31 + (112 - image.height) // 2
        sheet.alpha_composite(image, (x, y))
        draw.text((col * cell_w + 4, row * cell_h + 137), label[:23], fill=(220, 220, 220, 255))
    sheet.convert("RGB").save(out)


def main() -> None:
    for d in [PROC_D, PROC_C, ALPHA_D, ALPHA_C, RUNTIME_D, RUNTIME_C, CONTACT, RECORDS, VALIDATION]:
        d.mkdir(parents=True, exist_ok=True)
    decision_names = [name for name, _ in DECISION_SPRITES]
    category_names = [name for name, _ in CATEGORY_SPRITES]
    crop_atlas(ATLAS_1, SRC_D, decision_names[:20], 5, 4, ([8, 287, 566, 845, 1124, 1402], [7, 283, 558, 833, 1122]))
    crop_atlas(ATLAS_2, SRC_D, decision_names[20:], 5, 4, ([8, 287, 566, 845, 1124, 1402], [7, 283, 558, 833, 1122]))
    crop_atlas(ATLAS_C, SRC_C, category_names, 5, 2, ([8, 287, 566, 845, 1124, 1402], [180, 523, 867]))

    records: list[dict[str, object]] = []
    for name, rationale in DECISION_SPRITES:
        source = SRC_D / f"{name}_source.png"
        alpha = ALPHA_D / f"{name}_alpha.png"
        processed = PROC_D / f"{name}.png"
        runtime = RUNTIME_D / f"decision_{name}.dds"
        key_tile(source, alpha)
        normalize(alpha, processed, (32, 32))
        dds(processed, runtime, (32, 32))
        records.append({"type": "decision", "name": name, "source_mode": "imagegen_atlas_crop", "sprite": f"GFX_decision_brilliant_scientist_krg_{name}", "size": "32x32", "source": str(source.relative_to(ROOT)).replace("\\", "/"), "alpha": str(alpha.relative_to(ROOT)).replace("\\", "/"), "processed": str(processed.relative_to(ROOT)).replace("\\", "/"), "runtime": str(runtime.relative_to(ROOT)).replace("\\", "/"), "source_sha256": sha256(source), "processed_sha256": sha256(processed), "runtime_sha256": sha256(runtime), "alpha_bbox": alpha_bbox(processed), "rationale": rationale, "status": "complete"})
    for name, category_id in CATEGORY_SPRITES:
        source = SRC_C / f"{name}_source.png"
        alpha = ALPHA_C / f"{name}_alpha.png"
        processed = PROC_C / f"{name}.png"
        runtime = RUNTIME_C / f"decision_category_{name}.dds"
        key_tile(source, alpha)
        normalize(alpha, processed, (50, 40))
        dds(processed, runtime, (50, 40))
        records.append({"type": "decision_category", "name": name, "source_mode": "imagegen_atlas_crop", "category_id": category_id, "sprite": f"GFX_decision_category_brilliant_scientist_krg_{name}", "size": "50x40", "source": str(source.relative_to(ROOT)).replace("\\", "/"), "alpha": str(alpha.relative_to(ROOT)).replace("\\", "/"), "processed": str(processed.relative_to(ROOT)).replace("\\", "/"), "runtime": str(runtime.relative_to(ROOT)).replace("\\", "/"), "source_sha256": sha256(source), "processed_sha256": sha256(processed), "runtime_sha256": sha256(runtime), "alpha_bbox": alpha_bbox(processed), "rationale": category_id, "status": "complete"})

    ids = load_decision_ids()
    if len(ids) != 134:
        raise RuntimeError(f"Expected 134 current KRG decision/mission IDs, parsed {len(ids)}")
    assignments = [(identifier, assign(identifier)) for identifier in ids]
    assigned = {sprite for _, sprite in assignments}
    expected = set(decision_names)
    if assigned != expected:
        raise RuntimeError(f"Assignment mismatch; missing={sorted(expected - assigned)}, extra={sorted(assigned - expected)}")
    with (RECORDS / "decision_category_icon_manifest.json").open("w", encoding="utf-8") as handle:
        json.dump({"source_mode": "imagegen_atlas_crops", "decision_count": len(decision_names), "category_count": len(category_names), "parsed_current_ids": len(ids), "assets": records}, handle, indent=2)
    with (RECORDS / "decision_assignment_ledger.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["decision_or_mission_id", "sprite_name", "sprite_identifier"])
        for identifier, sprite in assignments:
            writer.writerow([identifier, sprite, f"GFX_decision_brilliant_scientist_krg_{sprite}"])
    with (RECORDS / "decision_category_assignment_ledger.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["category_id", "sprite_name", "sprite_identifier"])
        for name, category_id in CATEGORY_SPRITES:
            writer.writerow([category_id, name, f"GFX_decision_category_brilliant_scientist_krg_{name}"])
    make_contact([(name, PROC_D / f"{name}.png") for name, _ in DECISION_SPRITES], CONTACT / "decision_icons_016_processed_contact_sheet.png", "Event 016 decision icons — processed 32x32", 8)
    make_contact([(name, PROC_C / f"{name}.png") for name, _ in CATEGORY_SPRITES], CONTACT / "decision_categories_016_processed_contact_sheet.png", "Event 016 decision categories — processed 50x40", 5)
    make_contact([(name, SRC_D / f"{name}_source.png") for name, _ in DECISION_SPRITES], CONTACT / "decision_icons_016_sources_contact_sheet.png", "Event 016 decision icons — source masters", 8)
    make_contact([(name, SRC_C / f"{name}_source.png") for name, _ in CATEGORY_SPRITES], CONTACT / "decision_categories_016_sources_contact_sheet.png", "Event 016 decision categories — source masters", 5)
    # A compact TSV with pixel dimensions, alpha range, and expected BGRA length.
    with (VALIDATION / "decision_category_icon_validation.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["type", "name", "width", "height", "alpha_min", "alpha_max", "corner_alpha", "dds_length", "expected_length", "source_sha256", "processed_sha256", "runtime_sha256"])
        for row in records:
            image = Image.open(ROOT / str(row["processed"])).convert("RGBA")
            alpha = image.getchannel("A")
            w, h = image.size
            writer.writerow([row["type"], row["name"], w, h, alpha.getextrema()[0], alpha.getextrema()[1], ",".join(str(alpha.getpixel(p)) for p in [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)]), (ROOT / str(row["runtime"])).stat().st_size, 128 + w * h * 4, row["source_sha256"], row["processed_sha256"], row["runtime_sha256"]])
    print(json.dumps({"decisions": len(decision_names), "categories": len(category_names), "assignments": len(assignments), "runtime_decisions": str(RUNTIME_D), "runtime_categories": str(RUNTIME_C)}, indent=2))


if __name__ == "__main__":
    main()
