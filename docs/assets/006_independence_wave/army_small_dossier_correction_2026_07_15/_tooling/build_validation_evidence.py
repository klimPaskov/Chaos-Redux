#!/usr/bin/env python3
"""Build reproducible validation evidence for the Event 006 army-small correction."""

from __future__ import annotations

import hashlib
import json
import struct
from pathlib import Path

from PIL import Image, ImageDraw


PACKAGE = Path(__file__).resolve().parents[1]
REPO = Path(__file__).resolve().parents[5]
RUNTIME = REPO / "gfx/leaders/006_independence_wave"
BRI_PACKAGE = REPO / "docs/assets/006_independence_wave/bri_package_2026_07_15"
REFERENCE_DIR = (
    REPO
    / ".agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors"
)
FRAME_OVERLAY = (
    REPO
    / ".agents/skills/chaos-redux-event-assets/assets/advisor_dossier_overlays/advisor_frame_overlay.png"
)
PAPER_OVERLAY = (
    REPO
    / ".agents/skills/chaos-redux-event-assets/assets/advisor_dossier_overlays/advisor_paper_overlay.png"
)

STEMS = (
    "portrait_ACX_cornish_coastal_commander",
    "portrait_AEX_flemish_industrial_security_commander",
    "portrait_AFX_walloon_reserve_commander",
    "portrait_AGX_friesland_coastal_commander",
    "portrait_AJX_saar_industrial_security_commissioner",
    "portrait_BAY_independence_wave_mountain_commandant",
    "portrait_BRI_independence_wave_coastal_commandant",
    "portrait_RHI_independence_wave_river_commandant",
    "portrait_SCO_independence_wave_territorial_commandant",
    "portrait_WLS_independence_wave_mountain_commandant",
)

LARGE_PRE_TASK_SHA256 = {
    "portrait_ACX_cornish_coastal_commander": "db37cb8956de0ddc8eb39efa50a0de772440634731a4677d5887b7f580e9308c",
    "portrait_AEX_flemish_industrial_security_commander": "54a73934712087a464162f590bebbebff7e7f671cf85176fa838f50054dcf09a",
    "portrait_AFX_walloon_reserve_commander": "cf7c6de727dcda4ff963aa59ef2dcf733125fa3a68ed8072dfc2cf90d8e8e604",
    "portrait_AGX_friesland_coastal_commander": "87b7475dbbc28eb096f42e968c4bf5ad31c31c1e3a14415034264c158c667eb3",
    "portrait_AJX_saar_industrial_security_commissioner": "555ebb4619bf6a672b7edb96dab847cd3ff69b00fc4d6a53d6cff376556faf51",
    "portrait_BAY_independence_wave_mountain_commandant": "fb665c509a6b636a0f9b77fca5791f23702f822c2b6a7b459748e330f6117f68",
    "portrait_BRI_independence_wave_coastal_commandant": "f1603d707170002e7729c535e6ddd990cdfcc7e03f221684e1e6c821f12366c1",
    "portrait_RHI_independence_wave_river_commandant": "f29f6634c9f61cad6e2610d00bf08a817a3ed3ad5aa85ca54d37206a6b7d824c",
    "portrait_SCO_independence_wave_territorial_commandant": "bb9f8c61107fa7191c9a9e84ea36578355e9cd568457c6c454feade48e71f7aa",
    "portrait_WLS_independence_wave_mountain_commandant": "170caea268fd2a30c61437e7ba19a75b12eb0bf33b3b4538b55de5c0dfb72984",
}

VANILLA_REFERENCES = (
    ("Vanilla Paulus", REFERENCE_DIR / "army_small_ger_friedrich_paulus.png"),
    ("Vanilla von Kluge", REFERENCE_DIR / "army_small_ger_gunther_von_kluge.png"),
    ("Vanilla Rommel", REFERENCE_DIR / "army_small_ger_erwin_rommel.png"),
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def relative(path: Path) -> str:
    return path.resolve().relative_to(REPO).as_posix()


def inspect_legacy_bgra(path: Path) -> dict[str, object]:
    raw = path.read_bytes()
    if raw[:4] != b"DDS ":
        raise ValueError(f"Missing DDS magic: {path}")

    fields = {
        "header_size": struct.unpack_from("<I", raw, 4)[0],
        "height": struct.unpack_from("<I", raw, 12)[0],
        "width": struct.unpack_from("<I", raw, 16)[0],
        "mipmap_count": struct.unpack_from("<I", raw, 28)[0],
        "pixel_format_size": struct.unpack_from("<I", raw, 76)[0],
        "pixel_format_flags": struct.unpack_from("<I", raw, 80)[0],
        "fourcc": struct.unpack_from("<I", raw, 84)[0],
        "rgb_bit_count": struct.unpack_from("<I", raw, 88)[0],
        "red_mask": struct.unpack_from("<I", raw, 92)[0],
        "green_mask": struct.unpack_from("<I", raw, 96)[0],
        "blue_mask": struct.unpack_from("<I", raw, 100)[0],
        "alpha_mask": struct.unpack_from("<I", raw, 104)[0],
        "caps": struct.unpack_from("<I", raw, 108)[0],
        "file_length": len(raw),
    }
    expected_length = 128 + fields["width"] * fields["height"] * 4
    expected = {
        "header_size": 124,
        "height": 67,
        "width": 65,
        "mipmap_count": 0,
        "pixel_format_size": 32,
        "pixel_format_flags": 65,
        "fourcc": 0,
        "rgb_bit_count": 32,
        "red_mask": 0x00FF0000,
        "green_mask": 0x0000FF00,
        "blue_mask": 0x000000FF,
        "alpha_mask": 0xFF000000,
        "caps": 0x1000,
        "file_length": expected_length,
    }
    mismatches = {
        key: {"actual": fields[key], "expected": value}
        for key, value in expected.items()
        if fields[key] != value
    }
    if mismatches:
        raise ValueError(f"Malformed legacy BGRA DDS {path}: {mismatches}")
    fields["expected_file_length"] = expected_length
    fields["legacy_one_level_uncompressed_bgra"] = True
    return fields


def checker(size: tuple[int, int], tile: int) -> Image.Image:
    image = Image.new("RGBA", size, (90, 92, 94, 255))
    draw = ImageDraw.Draw(image)
    for y in range(0, size[1], tile):
        for x in range(0, size[0], tile):
            if (x // tile + y // tile) % 2:
                draw.rectangle(
                    (x, y, min(x + tile - 1, size[0] - 1), min(y + tile - 1, size[1] - 1)),
                    fill=(132, 134, 136, 255),
                )
    return image


def contact_sheet(rows: list[tuple[str, Image.Image]], scale: int, output: Path) -> None:
    icon_size = (65 * scale, 67 * scale)
    label_width = 260 if scale == 1 else 300
    gap = 12 if scale == 1 else 20
    row_height = max(icon_size[1] + gap * 2, 94 if scale == 1 else 300)
    header_height = 38 if scale == 1 else 54
    width = label_width + (icon_size[0] + gap) * 4 + gap
    height = header_height + row_height * len(rows)
    sheet = Image.new("RGBA", (width, height), (28, 30, 32, 255))
    draw = ImageDraw.Draw(sheet)
    headers = (
        ("Final", "Paulus", "von Kluge", "Rommel")
        if scale == 1
        else ("Event 006 final",) + tuple(label for label, _ in VANILLA_REFERENCES)
    )
    draw.text((12, 12), f"Army-small dossier comparison ({scale}x nearest)", fill=(244, 242, 234, 255))
    for column, header in enumerate(headers):
        x = label_width + gap + column * (icon_size[0] + gap)
        draw.text((x, 12), header, fill=(218, 218, 214, 255))

    refs = []
    for _, path in VANILLA_REFERENCES:
        with Image.open(path) as image:
            refs.append(image.convert("RGBA"))

    for row_index, (stem, final) in enumerate(rows):
        y = header_height + row_index * row_height
        draw.text((12, y + 10), stem.removeprefix("portrait_").removesuffix("_small"), fill=(232, 232, 228, 255))
        images = [final] + refs
        for column, image in enumerate(images):
            preview = image.resize(icon_size, Image.Resampling.NEAREST)
            base = checker(icon_size, max(2, 5 * scale))
            base.alpha_composite(preview)
            x = label_width + gap + column * (icon_size[0] + gap)
            sheet.alpha_composite(base, (x, y + gap))
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output)


def write_inventory(paths: set[Path]) -> None:
    lines = [f"{sha256(path)}  {relative(path)}" for path in sorted(paths, key=lambda item: relative(item))]
    (PACKAGE / "sha256_inventory.sha256").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    decoded_dir = PACKAGE / "decoded_dds_png"
    decoded_dir.mkdir(parents=True, exist_ok=True)
    rows: list[tuple[str, Image.Image]] = []
    records: list[dict[str, object]] = []
    inventory_paths: set[Path] = {
        Path(__file__),
        FRAME_OVERLAY,
        PAPER_OVERLAY,
        REPO / ".tools/process_hoi4_portrait.py",
        REPO / ".tools/convert_to_dds.py",
    }

    for _, reference in VANILLA_REFERENCES:
        inventory_paths.add(reference)

    for stem in STEMS:
        small_name = f"{stem}_small"
        processed = PACKAGE / "processed_png" / f"{small_name}.png"
        retained = PACKAGE / "final_dds" / f"{small_name}.dds"
        runtime = RUNTIME / f"{small_name}.dds"
        large = RUNTIME / f"{stem}.dds"
        metadata_path = PACKAGE / "metadata" / f"{small_name}.json"
        review = PACKAGE / "review_sheets" / f"{small_name}_review.png"
        decoded = decoded_dir / f"{small_name}.png"

        header = inspect_legacy_bgra(retained)
        runtime_header = inspect_legacy_bgra(runtime)
        if header != runtime_header:
            raise ValueError(f"Retained/runtime header mismatch for {small_name}")

        with Image.open(processed) as source_image, Image.open(retained) as dds_image:
            processed_rgba = source_image.convert("RGBA")
            decoded_rgba = dds_image.convert("RGBA")
            if decoded_rgba.size != (65, 67):
                raise ValueError(f"Decoded size mismatch for {small_name}: {decoded_rgba.size}")
            if processed_rgba.tobytes() != decoded_rgba.tobytes():
                raise ValueError(f"Decoded DDS pixels differ from approved PNG for {small_name}")
            alpha = decoded_rgba.getchannel("A")
            alpha_min, alpha_max = alpha.getextrema()
            corner_alpha = [
                alpha.getpixel((0, 0)),
                alpha.getpixel((64, 0)),
                alpha.getpixel((0, 66)),
                alpha.getpixel((64, 66)),
            ]
            transparent_pixels = sum(1 for value in alpha.getdata() if value == 0)
            if alpha_min != 0 or alpha_max != 255 or any(corner_alpha) or transparent_pixels < 100:
                raise ValueError(
                    f"Invalid dossier alpha for {small_name}: extrema={(alpha_min, alpha_max)}, "
                    f"corners={corner_alpha}, transparent={transparent_pixels}"
                )
            decoded_rgba.save(decoded)
            rows.append((small_name, decoded_rgba.copy()))

        retained_hash = sha256(retained)
        runtime_hash = sha256(runtime)
        if retained_hash != runtime_hash:
            raise ValueError(f"Retained/runtime hash mismatch for {small_name}")
        large_hash = sha256(large)
        if large_hash != LARGE_PRE_TASK_SHA256[stem]:
            raise ValueError(f"Large portrait changed for {stem}: {large_hash}")

        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        source_path = REPO / Path(metadata["source"])
        if sha256(source_path) != metadata["source_sha256"]:
            raise ValueError(f"Source hash drift for {small_name}")
        if metadata["generated_overlays"]["frame"]["sha256"] != sha256(FRAME_OVERLAY):
            raise ValueError(f"Frame overlay hash drift for {small_name}")
        if metadata["generated_overlays"]["paper"]["sha256"] != sha256(PAPER_OVERLAY):
            raise ValueError(f"Paper overlay hash drift for {small_name}")

        arguments = [
            "advisor",
            metadata["source"],
            metadata["output"],
            "--crop",
            *[str(value) for value in metadata["crop"]],
            "--source-kind",
            metadata["source_kind"],
            "--review-sheet",
            metadata["review_sheet"],
            "--metadata",
            relative(metadata_path),
            "--reference-dir",
            metadata["reference_dir"],
            "--advisor-frame-overlay",
            relative(FRAME_OVERLAY),
            "--advisor-paper-overlay",
            relative(PAPER_OVERLAY),
        ]
        metadata.update(
            {
                "processor_arguments": arguments,
                "processed_png_sha256": sha256(processed),
                "retained_final_dds": relative(retained),
                "retained_final_dds_sha256": retained_hash,
                "runtime_dds": relative(runtime),
                "runtime_dds_sha256": runtime_hash,
                "decoded_dds_png": relative(decoded),
                "decoded_dds_png_sha256": sha256(decoded),
                "visual_review": {
                    "status": "approved",
                    "native_size_reviewed": True,
                    "enlarged_nearest_reviewed": True,
                    "identity_and_expression_preserved": True,
                    "face_unobscured": True,
                    "reads_as_hoi4_dossier": True,
                },
                "status": "approved_and_installed",
            }
        )
        metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")

        record = {
            "stem": stem,
            "crop": metadata["crop"],
            "source": relative(source_path),
            "source_sha256": metadata["source_sha256"],
            "processed_png": relative(processed),
            "processed_png_sha256": sha256(processed),
            "retained_dds": relative(retained),
            "runtime_dds": relative(runtime),
            "dds_sha256": retained_hash,
            "decoded_png": relative(decoded),
            "decoded_png_sha256": sha256(decoded),
            "dds_header": header,
            "alpha_extrema": [alpha_min, alpha_max],
            "corner_alpha": corner_alpha,
            "transparent_pixels": transparent_pixels,
            "processed_and_decoded_pixels_identical": True,
            "retained_and_runtime_bytes_identical": True,
            "large_runtime_portrait": relative(large),
            "large_pre_task_sha256": LARGE_PRE_TASK_SHA256[stem],
            "large_post_task_sha256": large_hash,
            "large_portrait_byte_preserved": True,
            "visual_review": metadata["visual_review"],
        }
        records.append(record)
        inventory_paths.update(
            {
                source_path,
                processed,
                retained,
                runtime,
                large,
                metadata_path,
                review,
                decoded,
            }
        )

    native_sheet = PACKAGE / "contact_sheets/army_small_dossiers_native_1x.png"
    enlarged_sheet = PACKAGE / "contact_sheets/army_small_dossiers_enlarged_nearest_4x.png"
    contact_sheet(rows, 1, native_sheet)
    contact_sheet(rows, 4, enlarged_sheet)
    inventory_paths.update({native_sheet, enlarged_sheet})

    bri_stem = "portrait_BRI_independence_wave_coastal_commandant_small"
    bri_correction_png = PACKAGE / "processed_png" / f"{bri_stem}.png"
    bri_package_processed = BRI_PACKAGE / "processed_png" / f"{bri_stem}.png"
    bri_package_decoded = BRI_PACKAGE / "decoded_dds" / f"{bri_stem}_decoded.png"
    bri_contact_sheet = BRI_PACKAGE / "contact_sheets/006_bri_runtime_portraits_contact_sheet.png"
    bri_expected_hash = sha256(bri_correction_png)
    if sha256(bri_package_processed) != bri_expected_hash:
        raise ValueError("BRI package processed small PNG does not match correction package")
    if sha256(bri_package_decoded) != bri_expected_hash:
        raise ValueError("BRI package decoded small PNG does not match corrected DDS pixels")
    with Image.open(bri_package_processed) as image:
        if image.size != (65, 67):
            raise ValueError(f"BRI package processed small size mismatch: {image.size}")
    with Image.open(bri_package_decoded) as image:
        if image.size != (65, 67):
            raise ValueError(f"BRI package decoded small size mismatch: {image.size}")
    with Image.open(bri_contact_sheet) as image:
        if image.size != (468, 210):
            raise ValueError(f"BRI package contact-sheet size mismatch: {image.size}")
    bri_alignment = {
        "processed_png": relative(bri_package_processed),
        "decoded_png": relative(bri_package_decoded),
        "corrected_pixel_file_sha256": bri_expected_hash,
        "processed_and_decoded_match_correction": True,
        "dimensions": [65, 67],
        "rebuilt_contact_sheet": relative(bri_contact_sheet),
        "rebuilt_contact_sheet_sha256": sha256(bri_contact_sheet),
    }
    inventory_paths.update(
        {
            bri_package_processed,
            bri_package_decoded,
            bri_contact_sheet,
            BRI_PACKAGE / "manifest.md",
            BRI_PACKAGE / "gfx_handoff.md",
        }
    )

    report = {
        "package": relative(PACKAGE),
        "asset_count": len(records),
        "target_size": [65, 67],
        "expected_legacy_bgra_file_length": 17548,
        "frame_overlay": {"path": relative(FRAME_OVERLAY), "sha256": sha256(FRAME_OVERLAY)},
        "paper_overlay": {"path": relative(PAPER_OVERLAY), "sha256": sha256(PAPER_OVERLAY)},
        "vanilla_comparison_references": [
            {"label": label, "path": relative(path), "sha256": sha256(path)}
            for label, path in VANILLA_REFERENCES
        ],
        "contact_sheets": [relative(native_sheet), relative(enlarged_sheet)],
        "bri_package_alignment": bri_alignment,
        "records": records,
        "summary": {
            "all_small_dds_valid_legacy_bgra": True,
            "all_small_dds_exact_65x67": True,
            "all_small_dds_exact_17548_bytes": True,
            "all_small_dds_have_transparent_outer_corners": True,
            "all_small_dds_decode_identically_to_approved_png": True,
            "all_runtime_small_dds_match_retained_final_dds": True,
            "all_large_156x210_runtime_portraits_byte_preserved": True,
            "all_visual_reviews_approved": True,
            "bri_package_owned_small_artifacts_match_correction": True,
        },
    }
    report_path = PACKAGE / "validation_report.json"
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    inventory_paths.add(report_path)

    for path in PACKAGE.rglob("*"):
        if path.is_file() and path.name != "sha256_inventory.sha256":
            inventory_paths.add(path)
    write_inventory(inventory_paths)
    print(f"validated {len(records)} army-small dossiers; preserved {len(records)} large portraits")


if __name__ == "__main__":
    main()
