"""Build the FORM-48 individual-leader contact sheet and validation record."""

from __future__ import annotations

import hashlib
import json
import struct
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


PACKAGE = Path(__file__).resolve().parent
REPO = PACKAGE.parents[3]
TARGET_SIZE = (156, 210)
EXPECTED_DDS_LENGTH = 128 + TARGET_SIZE[0] * TARGET_SIZE[1] * 4

ASSETS = (
    {
        "id": "IW-184",
        "subject": "Daniel Mercer",
        "stem": "portrait_HBX_independence_wave_civic_convention",
        "source": "portrait_HBX_independence_wave_civic_convention_imagegen_master.png",
        "crop": (0, 0, 1081, 1455),
        "candidate_sha256": "40fc48f166fdccb3b2777ecbcf402ed487d043366d80e5ff55382f78cd0c0242",
        "review_sha256": "4dc693f5291b439510ab287d75628e248e356a382a7d72726d9d4c7583703f50",
    },
    {
        "id": "IW-179",
        "subject": "Elias Kihleng",
        "stem": "portrait_FSM_independence_wave_inter_island_congress_chair",
        "source": "portrait_FSM_independence_wave_inter_island_congress_chair_imagegen_master.png",
        "crop": (0, 1, 1080, 1455),
        "candidate_sha256": "0ab2385c51562af1557bf3839dbe3fedcf9f5bc19a1a76564709fe997cc68310",
        "review_sha256": "d3f81fe9b994a78d25cfb9d79d417544dfab06e096864851b83ed13d611e5560",
    },
)

PROTECTED = {
    "gfx/leaders/006_independence_wave/portrait_BAY_rupprecht_of_bavaria.dds":
        "7f0af64fdf4fecd49df454d1198935bb3ce6a8f74afc1ac82f8223704eaaad2b",
    "gfx/leaders/006_independence_wave/portrait_RHI_josef_friedrich_matthes.dds":
        "aa61cc3a12fb6670b690c7685feb9383383ce58599c9e6d6e7c14f20fab3bce2",
}


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def rgba_sha256(image: Image.Image) -> str:
    return hashlib.sha256(image.convert("RGBA").tobytes()).hexdigest()


def parse_legacy_dds(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    if data[:4] != b"DDS ":
        raise ValueError(f"{path}: missing DDS magic")

    header = {
        "magic": "DDS ",
        "header_size": struct.unpack_from("<I", data, 4)[0],
        "height": struct.unpack_from("<I", data, 12)[0],
        "width": struct.unpack_from("<I", data, 16)[0],
        "pixel_format_size": struct.unpack_from("<I", data, 76)[0],
        "pixel_format_flags": struct.unpack_from("<I", data, 80)[0],
        "four_cc": struct.unpack_from("<I", data, 84)[0],
        "rgb_bit_count": struct.unpack_from("<I", data, 88)[0],
        "r_mask": f"0x{struct.unpack_from('<I', data, 92)[0]:08x}",
        "g_mask": f"0x{struct.unpack_from('<I', data, 96)[0]:08x}",
        "b_mask": f"0x{struct.unpack_from('<I', data, 100)[0]:08x}",
        "a_mask": f"0x{struct.unpack_from('<I', data, 104)[0]:08x}",
        "caps": f"0x{struct.unpack_from('<I', data, 108)[0]:08x}",
        "file_length": len(data),
    }

    expected = {
        "header_size": 124,
        "height": TARGET_SIZE[1],
        "width": TARGET_SIZE[0],
        "pixel_format_size": 32,
        "pixel_format_flags": 65,
        "four_cc": 0,
        "rgb_bit_count": 32,
        "r_mask": "0x00ff0000",
        "g_mask": "0x0000ff00",
        "b_mask": "0x000000ff",
        "a_mask": "0xff000000",
        "caps": "0x00001000",
        "file_length": EXPECTED_DDS_LENGTH,
    }
    failures = {key: {"actual": header[key], "expected": value}
                for key, value in expected.items() if header[key] != value}
    if failures:
        raise ValueError(f"{path}: malformed legacy BGRA DDS: {failures}")
    header["legacy_bgra_header_valid"] = True
    return header


def build_contact_sheet() -> Path:
    canvas = Image.new("RGB", (1260, 540), (24, 27, 31))
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default()
    draw.text((24, 18), "Event 006 FORM-48 individual country-leader portraits", fill=(240, 240, 236), font=font)
    draw.text((24, 38), "Official ImageGen master crop -> approved 156x210 leader finish (displayed enlarged)", fill=(176, 184, 191), font=font)

    panel_width = 594
    for index, asset in enumerate(ASSETS):
        panel_x = 24 + index * (panel_width + 24)
        panel_y = 70
        draw.rounded_rectangle((panel_x, panel_y, panel_x + panel_width, 516), radius=8, fill=(39, 43, 48))
        draw.text((panel_x + 16, panel_y + 14), f"{asset['id']} - {asset['subject']}", fill=(242, 236, 218), font=font)

        source_path = PACKAGE / "source_png" / str(asset["source"])
        processed_path = PACKAGE / "processed_png" / f"{asset['stem']}.png"
        with Image.open(source_path) as source:
            source_crop = source.convert("RGB").crop(asset["crop"]).resize((234, 315), Image.Resampling.LANCZOS)
        with Image.open(processed_path) as processed:
            processed_large = processed.convert("RGB").resize((234, 315), Image.Resampling.NEAREST)

        left = panel_x + 38
        right = panel_x + 322
        top = panel_y + 54
        canvas.paste(source_crop, (left, top))
        canvas.paste(processed_large, (right, top))
        draw.rectangle((left - 1, top - 1, left + 234, top + 315), outline=(104, 111, 119))
        draw.rectangle((right - 1, top - 1, right + 234, top + 315), outline=(104, 111, 119))
        draw.text((left, top + 326), "selected source crop", fill=(198, 204, 209), font=font)
        draw.text((right, top + 326), "approved runtime image", fill=(198, 204, 209), font=font)
        draw.text((right, top + 344), "native 156x210; shown 1.5x nearest", fill=(151, 162, 171), font=font)

    output = PACKAGE / "contact_sheets" / "006_form48_pacific_individual_leader_portraits.png"
    canvas.save(output)
    return output


def main() -> None:
    results: list[dict[str, object]] = []
    for asset in ASSETS:
        stem = str(asset["stem"])
        source_path = PACKAGE / "source_png" / str(asset["source"])
        processed_path = PACKAGE / "processed_png" / f"{stem}.png"
        retained_dds = PACKAGE / "final_dds" / f"{stem}.dds"
        runtime_dds = REPO / "gfx" / "leaders" / "006_independence_wave" / f"{stem}.dds"
        review_path = PACKAGE / "review_sheets" / f"{stem}_review.png"
        decoded_path = PACKAGE / "dds_decoded_png" / f"{stem}.png"

        if file_sha256(processed_path) != asset["candidate_sha256"]:
            raise ValueError(f"{processed_path}: approved candidate hash changed")
        if file_sha256(review_path) != asset["review_sha256"]:
            raise ValueError(f"{review_path}: approved review-sheet hash changed")
        if retained_dds.read_bytes() != runtime_dds.read_bytes():
            raise ValueError(f"{runtime_dds}: runtime DDS differs from retained DDS")

        dds_header = parse_legacy_dds(retained_dds)
        with Image.open(source_path) as source:
            source_rgba = source.convert("RGBA")
            source_record = {
                "path": source_path.relative_to(REPO).as_posix(),
                "dimensions": list(source_rgba.size),
                "file_sha256": file_sha256(source_path),
                "decoded_rgba_sha256": rgba_sha256(source_rgba),
            }
        with Image.open(processed_path) as processed:
            processed_rgba = processed.convert("RGBA")
            processed_pixels = processed_rgba.tobytes()
            alpha = processed_rgba.getchannel("A")
            alpha_min, alpha_max = alpha.getextrema()
        with Image.open(retained_dds) as decoded:
            decoded_rgba = decoded.convert("RGBA")
            decoded_rgba.save(decoded_path)
            decoded_pixels = decoded_rgba.tobytes()

        pixel_equal = decoded_pixels == processed_pixels
        if decoded_rgba.size != TARGET_SIZE or not pixel_equal:
            raise ValueError(f"{retained_dds}: decoded DDS is not pixel-equal to the approved PNG")

        results.append({
            "requirement_id": asset["id"],
            "subject": asset["subject"],
            "gender_presentation": "adult male",
            "source": source_record,
            "processed_png": {
                "path": processed_path.relative_to(REPO).as_posix(),
                "dimensions": list(processed_rgba.size),
                "file_sha256": file_sha256(processed_path),
                "decoded_rgba_sha256": hashlib.sha256(processed_pixels).hexdigest(),
                "alpha_min": alpha_min,
                "alpha_max": alpha_max,
                "independent_visual_approval": True,
            },
            "independent_approval": {
                "reviewer": "/root",
                "producer": "/root/form48_leader_portraits",
                "date": "2026-07-17",
                "candidate_png_sha256": asset["candidate_sha256"],
                "review_sheet": {
                    "path": review_path.relative_to(REPO).as_posix(),
                    "file_sha256": asset["review_sha256"],
                },
                "native_size_verdict": (
                    "approved at 156x210: face, shoulders, expression, and civilian "
                    "country-leader silhouette remain readable"
                ),
                "enlarged_reference_comparison_verdict": (
                    "approved against the canonical eight-leader reference family and "
                    "the 1.5x nearest-neighbor contact-sheet view"
                ),
                "approved_for_conversion": True,
            },
            "retained_dds": {
                "path": retained_dds.relative_to(REPO).as_posix(),
                "file_sha256": file_sha256(retained_dds),
                "header": dds_header,
            },
            "runtime_dds": {
                "path": runtime_dds.relative_to(REPO).as_posix(),
                "file_sha256": file_sha256(runtime_dds),
                "byte_identical_to_retained": True,
            },
            "decoded_dds_png": {
                "path": decoded_path.relative_to(REPO).as_posix(),
                "dimensions": list(decoded_rgba.size),
                "file_sha256": file_sha256(decoded_path),
                "decoded_rgba_sha256": hashlib.sha256(decoded_pixels).hexdigest(),
                "pixel_equal_to_approved_png": pixel_equal,
            },
        })

    protected_results: dict[str, object] = {}
    for relative_path, expected_hash in PROTECTED.items():
        path = REPO / relative_path
        actual_hash = file_sha256(path)
        if actual_hash != expected_hash:
            raise ValueError(f"protected portrait changed: {relative_path}")
        protected_results[relative_path] = {
            "expected_sha256": expected_hash,
            "actual_sha256": actual_hash,
            "byte_identical_guard_passed": True,
        }

    contact_sheet = build_contact_sheet()
    report = {
        "schema": "chaos-redux-form48-leader-portrait-validation-v1",
        "date": "2026-07-17",
        "status": "pass",
        "target_format": "156x210 legacy one-level uncompressed 32-bit BGRA DDS",
        "assets": results,
        "contact_sheet": {
            "path": contact_sheet.relative_to(REPO).as_posix(),
            "file_sha256": file_sha256(contact_sheet),
        },
        "protected_portraits": protected_results,
    }
    output = PACKAGE / "notes" / "validation.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    inventory = PACKAGE / "hashes.sha256"
    package_files = sorted(
        path for path in PACKAGE.rglob("*")
        if path.is_file()
        and path != inventory
        and "__pycache__" not in path.parts
    )
    inventory.write_text(
        "".join(
            f"{file_sha256(path)}  {path.relative_to(REPO).as_posix()}\n"
            for path in package_files
        ),
        encoding="utf-8",
    )
    print(json.dumps({
        "status": "pass",
        "validation": output.relative_to(REPO).as_posix(),
        "hash_inventory": inventory.relative_to(REPO).as_posix(),
    }, indent=2))


if __name__ == "__main__":
    main()
