"""Combine generated source, processed PNG, candidate DDS, and reference evidence."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
REPO = next(parent for parent in ROOT.parents if (parent / "interface/014_cannibalism.gfx").is_file())
EVIDENCE = ROOT / "evidence"
PNG_AUDIT = json.loads((EVIDENCE / "png_review_audit.json").read_text(encoding="utf-8"))
DDS_AUDIT = json.loads((EVIDENCE / "dds_roundtrip_audit.json").read_text(encoding="utf-8"))
INSTALL = json.loads((EVIDENCE / "runtime_install_receipt.json").read_text(encoding="utf-8"))
PARENT_REVIEW_PATH = REPO / "docs/plans/014_cannibalism_plans/evidence/2026-10-03_europe_portrait_parent_review.json"
PARENT_REVIEW = json.loads(PARENT_REVIEW_PATH.read_text(encoding="utf-8"))
GFX_PATH = REPO / "interface/014_cannibalism.gfx"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes())


def image_info(path: Path) -> dict:
    with Image.open(path) as image:
        return {"format": image.format, "dimensions": list(image.size), "mode": image.mode}


def main() -> None:
    gfx_text = GFX_PATH.read_text(encoding="utf-8")
    gfx_lines = gfx_text.splitlines()
    crosswalk = []
    dds_by_slot = {record["slot"]: record for record in DDS_AUDIT["records"]}
    png_by_slot = {record["slot"]: record for record in PNG_AUDIT["records"]}
    installed_by_runtime = {record["RuntimePath"]: record for record in INSTALL["installed"]}
    backup_by_runtime = {record["RuntimePath"]: record for record in INSTALL["backups"]}
    for slot in ("CBA", "CBB", "CBC", "CBD", "CBE", "CBF", "CBG", "CBH"):
        entries = []
        pattern = re.compile(rf'name = "(GFX_portrait_{slot}_warlord(?:_europe)?)" texturefile = "([^"]+)"')
        for number, line in enumerate(gfx_lines, 1):
            match = pattern.search(line)
            if match:
                entries.append({"line": number, "sprite": match.group(1), "runtime_dds_path": match.group(2)})
        dds_record = dds_by_slot[slot]
        png_record = png_by_slot[slot]
        runtime_path = REPO / dds_record["existing_runtime_dds_path"]
        installed_record = installed_by_runtime[dds_record["existing_runtime_dds_path"]]
        backup_record = backup_by_runtime[dds_record["existing_runtime_dds_path"]]
        crosswalk.append({
            "slot": slot,
            "sprites": entries,
            "selected_source_path": png_record["source_path"],
            "selected_source_sha256": png_record["source_sha256"],
            "selected_source_dimensions": png_record["source_dimensions"],
            "selected_processed_png_path": png_record["processed_path"],
            "selected_processed_png_sha256": png_record["processed_sha256"],
            "selected_processed_png_dimensions": png_record["processed_dimensions"],
            "crop_evidence_path": png_record["crop_evidence_path"],
            "crop_box": png_record["crop_box"],
            "candidate_dds_path": dds_record["candidate_dds_path"],
            "candidate_dds_sha256": dds_record["candidate_dds_sha256"],
            "candidate_dds_dimensions": dds_record["candidate_dds_dimensions"],
            "candidate_dds_bytes": dds_record["candidate_dds_bytes"],
            "decoded_pixel_sha256": dds_record["decoded_pixel_sha256"],
            "runtime_dds_path": dds_record["existing_runtime_dds_path"],
            "runtime_preinstall_sha256": dds_record["existing_runtime_sha256_before"],
            "runtime_installed_sha256": file_sha(runtime_path),
            "runtime_matches_parent_approved_candidate": file_sha(runtime_path) == dds_record["candidate_dds_sha256"],
            "runtime_install_receipt_previous_sha256": installed_record["PreviousSHA256"],
            "runtime_install_receipt_installed_sha256": installed_record["InstalledSHA256"],
            "preinstall_backup_path": backup_record["BackupPath"],
            "preinstall_backup_sha256": backup_record["SHA256"],
        })

    cba_alt_source = ROOT / "source_png/leader_CBA_warlord_europe_source.png"
    cba_alt_crop = ROOT / "processed_png/leader_CBA_warlord_europe_source_crop.png"
    cba_alt_processed = ROOT / "processed_png/leader_CBA_warlord_europe_156x210.png"
    cba_alt_crop_record = {
        "slot": "CBA",
        "candidate_id": "CBA-v03",
        "selection_status": "unselected; parent selected CBA-v02",
        "source_path": str(cba_alt_source.relative_to(ROOT)).replace("\\", "/"),
        "source_dimensions": image_info(cba_alt_source)["dimensions"],
        "source_mode": image_info(cba_alt_source)["mode"],
        "source_sha256": file_sha(cba_alt_source),
        "crop_box_left_top_right_bottom": [0, 0, 1081, 1455],
        "crop_path": str(cba_alt_crop.relative_to(ROOT)).replace("\\", "/"),
        "crop_dimensions": image_info(cba_alt_crop)["dimensions"],
        "crop_sha256": file_sha(cba_alt_crop),
        "processed_path": str(cba_alt_processed.relative_to(ROOT)).replace("\\", "/"),
        "processed_dimensions": image_info(cba_alt_processed)["dimensions"],
        "processed_sha256": file_sha(cba_alt_processed),
        "resampling": "Pillow Image.Resampling.LANCZOS",
        "background": "opaque RGB; no alpha processing",
    }
    (EVIDENCE / "CBA_v03_alternate_crop.json").write_text(json.dumps(cba_alt_crop_record, indent=2) + "\n", encoding="utf-8")
    cba_alternate = {
        "source": {"path": str(cba_alt_source.relative_to(ROOT)).replace("\\", "/"), **image_info(cba_alt_source), "sha256": file_sha(cba_alt_source)},
        "crop": {"path": str(cba_alt_crop.relative_to(ROOT)).replace("\\", "/"), **image_info(cba_alt_crop), "sha256": file_sha(cba_alt_crop)},
        "processed": {"path": str(cba_alt_processed.relative_to(ROOT)).replace("\\", "/"), **image_info(cba_alt_processed), "sha256": file_sha(cba_alt_processed)},
        "crop_evidence_path": "evidence/CBA_v03_alternate_crop.json",
    }

    reference_names = [
        "contact_sheet.png",
        "den_thorvald_stauning.png",
        "eth_haile_selassie.png",
        "afg_mohammed_zahir_shah.png",
    ]
    ref_root = REPO / ".agents/skills/chaos-redux-event-assets/assets/gfx_references/portraits/leaders"
    references = []
    for name in reference_names:
        path = ref_root / name
        references.append({"path": str(path.relative_to(REPO)).replace("\\", "/"), **image_info(path), "bytes": path.stat().st_size, "sha256": file_sha(path), "role": "reference-only palette, painted rendering, and framing; never source identity or shipping art"})

    hannibal_names = [
        "hannibal.dds",
        "hannibal_wendigo.dds",
        "leader_CBL_hannibal_sheet.dds",
        "leader_ZZZ_hannibal_wendigo_sheet.dds",
    ]
    hannibal_root = REPO / "gfx/leaders/014_cannibalism"
    protected_hannibal = []
    for name in hannibal_names:
        path = hannibal_root / name
        protected_hannibal.append({"path": str(path.relative_to(REPO)).replace("\\", "/"), **image_info(path), "bytes": path.stat().st_size, "sha256": file_sha(path), "status": "read-only; not edited by this candidate work"})

    result = {
        "event": {"id": "014", "slug": "cannibalism"},
        "package_date": "2026-10-03",
        "package_status": "eight_parent_approved_Europe_DDS_installed; other_48_regional_portraits_queued",
        "source_classification": "fictional_high_chaos; CBA-CBH are invented Cannibal Warlord identities, not real people or offices",
        "source_mode": "built-in native ImageGen; no Internet or user-supplied raster sources",
        "parent_review": {"status": "final_Europe_source_PNG_DDS_decoded_contact_and_hash_approval_recorded", "selection": "CBA-v02 selected by parent for the skull-and-blood action within the user's authorized scope; this is not a new explicit user art decision", "evidence_path": str(PARENT_REVIEW_PATH.relative_to(REPO)).replace("\\", "/"), "evidence_sha256": file_sha(PARENT_REVIEW_PATH), "acceptance_scope": PARENT_REVIEW["acceptance_scope"]},
        "full_matrix": {"required": 56, "slots": 8, "regions": ["Europe", "Asia", "Africa", "Middle East", "North America", "South America", "Oceania"], "this_tranche": "Europe", "candidate_pngs_ready": 8, "candidate_dds_ready": 8, "installed_runtime_portraits": 8, "remaining_regions_queued": 48, "full_goal_complete": False},
        "imagegen_call_log": "evidence/imagegen_call_log.json",
        "exact_prompts": "evidence/prompts.json",
        "CBA_lineage": "evidence/CBA_lineage.json",
        "PNG_QA": PNG_AUDIT,
        "candidate_DDS_QA_pre_install": DDS_AUDIT,
        "GFX_and_runtime_crosswalk": crosswalk,
        "runtime_install_receipt_path": "evidence/runtime_install_receipt.json",
        "runtime_preinstall_snapshot_path": "evidence/runtime_preinstall_snapshot.json",
        "runtime_installation": {"installed_count": INSTALL["installed_count"], "preinstall_backups": INSTALL["backup_count"], "protected_other_dds_count": INSTALL["protected_other_dds_count"], "protected_other_dds_unchanged": INSTALL["protected_other_dds_unchanged"], "protected_gfx_character_hannibal_files_unchanged": INSTALL["protected_gfx_character_hannibal_files_unchanged"], "modified_runtime_paths": INSTALL["modified_runtime_paths"], "modified_portrait_gfx_or_character_files": []},
        "unselected_CBA_v03_edit_alternative": cba_alternate,
        "reference_only_nonshipping_assets": references,
        "protected_Hannibal_art_current_hashes": protected_hannibal,
        "modified_runtime_files": INSTALL["modified_runtime_paths"],
        "modified_portrait_GFX_or_character_files": [],
        "skipped_or_pending": [
            "The other 48 region-slot portraits remain queued for later production.",
            "No HOI4 process or live in-game consumer validation was run."
        ],
        "simplifications": [],
        "committed": False,
    }
    out = EVIDENCE / "output_inventory.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"{out.relative_to(ROOT)}|sha256={file_sha(out)}|bytes={out.stat().st_size}")


if __name__ == "__main__":
    main()
