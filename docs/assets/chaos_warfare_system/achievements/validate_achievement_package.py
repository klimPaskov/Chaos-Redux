"""Validate and document the Chaos Warfare achievement icon triplets."""

from __future__ import annotations

import hashlib
import json
import struct
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parent
REPO_ROOT = ROOT.parents[3]
SOURCE_DIR = ROOT / "source_png"
ALPHA_DIR = ROOT / "archive" / "alpha_png"
PROCESSED_DIR = ROOT / "processed_png"
GFX_DIR = REPO_ROOT / "gfx" / "achievements"
MANIFEST_DIR = ROOT / "manifest"
VALIDATION_DIR = ROOT / "validation"
TARGET_GFX = "interface/chaosx_achievements.gfx"

IDS = [
    "chaos_warfare_air_still_breathable",
    "chaos_warfare_masks_before_guns",
    "chaos_warfare_prepared_army",
    "chaos_warfare_poisoned_victory",
    "chaos_warfare_clean_hands_dirty_work",
    "chaos_warfare_evidence_survives",
    "chaos_warfare_no_wind_is_friendly",
    "chaos_warfare_antidote_arrived",
    "chaos_warfare_quarantine_without_collapse",
    "chaos_warfare_arsenal_dismantled",
    "chaos_warfare_terminal_contagion",
    "chaos_warfare_mask_for_every_door",
    "chaos_warfare_weapon_turns_home",
    "chaos_warfare_unbroken_supply_corridor",
    "chaos_warfare_first_user_pays",
]

PROMPT_DIRECTION = {
    "chaos_warfare_air_still_breathable": "intact respirator, clear sky, contaminated front haze",
    "chaos_warfare_masks_before_guns": "stacked respirator crates and filters before an arsenal gate",
    "chaos_warfare_prepared_army": "masked staff officer and protected formation",
    "chaos_warfare_poisoned_victory": "corroded victory wreath, sword, medal, chemical droplets",
    "chaos_warfare_clean_hands_dirty_work": "gloved hand and unmarked amber sample vial beside blank dossier",
    "chaos_warfare_evidence_survives": "sealed evidence case and broken CBRN facility door",
    "chaos_warfare_no_wind_is_friendly": "torn windsock, wrong-way wind, masked troops",
    "chaos_warfare_antidote_arrived": "medical countermeasure ampoule above respirator and field kit",
    "chaos_warfare_quarantine_without_collapse": "closed railway gate, blank medical seal, halted train",
    "chaos_warfare_arsenal_dismantled": "crushed chemical shell under inspection lamp and empty racks",
    "chaos_warfare_terminal_contagion": "sealed command mask and four doctrine emblems",
    "chaos_warfare_mask_for_every_door": "row of household doors with respirator boxes",
    "chaos_warfare_weapon_turns_home": "damaged depot, split shell, inward-pointing hazard arrow",
    "chaos_warfare_unbroken_supply_corridor": "covered convoy on washed road through contaminated territory",
    "chaos_warfare_first_user_pays": "sealed chemical shell beneath level brass scales",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def dds_info(path: Path, png: Image.Image) -> dict[str, object]:
    data = path.read_bytes()
    result: dict[str, object] = {
        "dds_exists": path.exists(),
        "dds_magic": data[:4] == b"DDS ",
        "dds_header_size": struct.unpack_from("<I", data, 4)[0] if len(data) >= 8 else None,
        "dds_width": struct.unpack_from("<I", data, 16)[0] if len(data) >= 20 else None,
        "dds_height": struct.unpack_from("<I", data, 12)[0] if len(data) >= 16 else None,
        "dds_mipmap_count": struct.unpack_from("<I", data, 28)[0] if len(data) >= 32 else None,
        "dds_format": "unknown",
        "dds_pixel_identical": False,
    }
    if len(data) < 128 or not result["dds_magic"]:
        return result

    pf_flags, fourcc, bpp, r_mask, g_mask, b_mask, a_mask = struct.unpack_from("<IIIIIII", data, 80)
    if pf_flags == 65 and fourcc == 0 and bpp == 32 and (r_mask, g_mask, b_mask, a_mask) == (
        16711680,
        65280,
        255,
        4278190080,
    ):
        result["dds_format"] = "uncompressed BGRA"

    payload = data[128:]
    expected_bytes = int(result["dds_width"] or 0) * int(result["dds_height"] or 0) * 4
    if expected_bytes == len(payload) and result["dds_width"] == 64 and result["dds_height"] == 64:
        decoded = Image.frombytes("RGBA", (64, 64), payload, "raw", "BGRA")
        result["dds_pixel_identical"] = decoded.tobytes("raw", "BGRA") == png.tobytes("raw", "BGRA")
    return result


def png_info(path: Path, variant: str) -> dict[str, object]:
    image = Image.open(path).convert("RGBA")
    pixels = list(image.getdata())
    alpha_values = [pixel[3] for pixel in pixels]
    alpha_pixels = sum(value > 0 for value in alpha_values)
    partial_alpha = sum(0 < value < 255 for value in alpha_values)
    corners = [image.getpixel(point)[3] for point in ((0, 0), (63, 0), (0, 63), (63, 63))]
    green_pixels = sum(1 for r, g, b, a in pixels if a > 0 and r < 40 and g > 160 and b < 40)
    grey_monochrome = None
    if variant == "grey":
        grey_monochrome = all(r == g == b for r, g, b, _ in pixels)
    red_overlay = None
    if variant == "not_eligible":
        red_overlay = sum(1 for r, g, b, a in pixels if a > 0 and r > 90 and r > g + 25 and r > b + 25)
    return {
        "png_width": image.width,
        "png_height": image.height,
        "png_mode": image.mode,
        "alpha_pixels": alpha_pixels,
        "partial_alpha": partial_alpha,
        "corner_alpha_zero": corners == [0, 0, 0, 0],
        "green_visible_pixels": green_pixels,
        "grey_monochrome": grey_monochrome,
        "red_overlay_pixels": red_overlay,
        "image": image,
    }


def main() -> None:
    VALIDATION_DIR.mkdir(parents=True, exist_ok=True)
    MANIFEST_DIR.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, object]] = []
    manifest_entries: list[dict[str, object]] = []
    failures: list[str] = []
    variants = (("completed", ""), ("grey", "_grey"), ("not_eligible", "_not_eligible"))

    for asset_id in IDS:
        source_path = SOURCE_DIR / f"{asset_id}_source.png"
        alpha_path = ALPHA_DIR / f"{asset_id}_alpha_master.png"
        source_archive_path = ROOT / "archive" / f"{asset_id}_source_archive.png"
        if not source_path.exists() or not alpha_path.exists() or not source_archive_path.exists():
            failures.append(f"missing source evidence for {asset_id}")

        for variant, suffix in variants:
            processed_path = PROCESSED_DIR / f"{asset_id}{suffix}.png"
            dds_path = GFX_DIR / f"{asset_id}{suffix}.dds"
            if not processed_path.exists() or not dds_path.exists():
                failures.append(f"missing {variant} output for {asset_id}")
                continue
            info = png_info(processed_path, variant)
            dds = dds_info(dds_path, info["image"])
            info.pop("image")
            row = {
                "asset_id": asset_id,
                "variant": variant,
                "source_png": str(source_path.relative_to(REPO_ROOT)).replace("\\", "/"),
                "source_sha256": sha256(source_path),
                "source_archive_sha256": sha256(source_archive_path),
                "alpha_master_sha256": sha256(alpha_path),
                "processed_png": str(processed_path.relative_to(REPO_ROOT)).replace("\\", "/"),
                "final_dds": str(dds_path.relative_to(REPO_ROOT)).replace("\\", "/"),
                **info,
                **dds,
                "processed_sha256": sha256(processed_path),
                "dds_sha256": sha256(dds_path),
            }
            row["status"] = "complete" if (
                row["png_width"] == 64
                and row["png_height"] == 64
                and row["png_mode"] == "RGBA"
                and row["alpha_pixels"] > 0
                and row["corner_alpha_zero"]
                and row["green_visible_pixels"] == 0
                and row["dds_magic"]
                and row["dds_header_size"] == 124
                and row["dds_width"] == 64
                and row["dds_height"] == 64
                and row["dds_format"] == "uncompressed BGRA"
                and row["dds_pixel_identical"]
                and (variant != "grey" or row["grey_monochrome"])
                and (variant != "not_eligible" or int(row["red_overlay_pixels"] or 0) > 100)
            ) else "needs_user_review"
            if row["status"] != "complete":
                failures.append(f"validation failure for {asset_id} {variant}")
            rows.append(row)
            manifest_entries.append(
                {
                    "asset_type": "achievement_icon",
                    "working_identifier": asset_id,
                    "final_identifier": f"{asset_id}{suffix}",
                    "variant": variant,
                    "source_mode": "generated",
                    "generation_tool": "official built-in image_generation skill",
                    "prompt_direction": PROMPT_DIRECTION[asset_id],
                    "target_size": "64x64",
                    "source_png": row["source_png"],
                    "source_archive_png": str(source_archive_path.relative_to(REPO_ROOT)).replace("\\", "/"),
                    "source_sha256": row["source_sha256"],
                    "source_archive_sha256": row["source_archive_sha256"],
                    "alpha_master_sha256": row["alpha_master_sha256"],
                    "processed_png": row["processed_png"],
                    "final_dds": row["final_dds"],
                    "sprite_name": f"GFX_achievement_{asset_id}{suffix}",
                    "intended_gfx_file": TARGET_GFX,
                    "related_gameplay_id": asset_id,
                    "status": row["status"],
                    "uncertainty": "none for asset production; parent-owned gameplay and GFX wiring remains outside scope",
                    "processed_sha256": row["processed_sha256"],
                    "dds_sha256": row["dds_sha256"],
                }
            )

    completed_hashes = {entry["processed_sha256"] for entry in manifest_entries if entry["variant"] == "completed"}
    report = {
        "package": "chaos_warfare_system achievements",
        "target_size": "64x64",
        "achievement_count": len(IDS),
        "variant_count": len(rows),
        "completed_unique_processed_masters": len(completed_hashes),
        "expected_completed_unique_processed_masters": len(IDS),
        "status": "complete" if not failures and len(rows) == 45 and len(completed_hashes) == len(IDS) else "needs_user_review",
        "failures": failures,
        "dds_contract": "one-level uncompressed BGRA, 64x64, pixel-identical to processed PNG",
    }
    (VALIDATION_DIR / "validation_report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    columns = [
        "asset_id",
        "variant",
        "source_png",
        "source_sha256",
        "source_archive_sha256",
        "alpha_master_sha256",
        "processed_png",
        "final_dds",
        "png_width",
        "png_height",
        "png_mode",
        "alpha_pixels",
        "partial_alpha",
        "corner_alpha_zero",
        "green_visible_pixels",
        "grey_monochrome",
        "red_overlay_pixels",
        "dds_exists",
        "dds_magic",
        "dds_header_size",
        "dds_width",
        "dds_height",
        "dds_mipmap_count",
        "dds_format",
        "dds_pixel_identical",
        "processed_sha256",
        "dds_sha256",
        "status",
    ]
    lines = ["\t".join(columns)]
    for row in rows:
        lines.append("\t".join(str(row.get(column, "")) for column in columns))
    (VALIDATION_DIR / "achievement_icon_validation.tsv").write_text("\n".join(lines) + "\n", encoding="utf-8")
    manifest = {
        "package": "chaos_warfare_system",
        "asset_family": "achievements",
        "generated_at": "2026-07-28",
        "target_folder": "gfx/achievements/",
        "target_gfx_file": TARGET_GFX,
        "variant_contract": ["completed", "grey", "not_eligible"],
        "entries": manifest_entries,
    }
    (MANIFEST_DIR / "achievement_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    if failures:
        raise SystemExit("; ".join(failures))


if __name__ == "__main__":
    main()
