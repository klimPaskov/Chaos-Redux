#!/usr/bin/env python3
"""Build the registered SCO/WLS/BRI/RHI/BAY Event 006 portrait package.

The source PNGs were generated independently with ImageGen. This script only
performs deterministic crops, tonal finishing, resizing, DDS conversion,
runtime-file decoding, validation, hash inventory generation, and contact-sheet
assembly. It does not edit character or interface definitions.
"""

from __future__ import annotations

import hashlib
import struct
import subprocess
import sys
from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[4]
ASSET_ROOT = ROOT / "docs" / "assets" / "006_independence_wave"
SOURCE_ROOT = ASSET_ROOT / "source_png" / "generated_nwe"
PROCESSED_ROOT = ASSET_ROOT / "processed_png" / "generated_nwe"
DECODED_ROOT = ASSET_ROOT / "dds_decoded_png" / "generated_nwe"
CONTACT_ROOT = ASSET_ROOT / "contact_sheets"
RUNTIME_ROOT = ROOT / "gfx" / "leaders" / "006_independence_wave"
DDS_CONVERTER = ROOT / ".agents" / "skills" / "chaos-redux-event-assets" / "tools" / "convert_to_dds.py"
HASH_LEDGER = ASSET_ROOT / "generated_nwe_registered_civic_portraits_hashes.sha256"


PORTRAITS = {
    "institutional": {
        "source_dir": "registered_institutional_portraits",
        "processed_dir": "registered_institutional_portraits",
        "decoded_dir": "registered_institutional_portraits",
        "records": {
            "SCO": {
                "stem": "portrait_SCO_scottish_provisional_council",
                "label": "Scottish Provisional Council",
            },
            "WLS": {
                "stem": "portrait_WLS_welsh_national_emergency_council",
                "label": "Welsh National Emergency Council",
            },
            "BRI": {
                "stem": "portrait_BRI_breton_civic_commission",
                "label": "Breton Civic Commission",
            },
            "RHI": {
                "stem": "portrait_RHI_rhenish_civic_directorate",
                "label": "Rhenish Civic Directorate",
            },
            "BAY": {
                "stem": "portrait_BAY_bavarian_state_council",
                "label": "Bavarian State Council",
            },
        },
    },
    "command": {
        "source_dir": "registered_command_portraits",
        "processed_dir": "registered_command_portraits",
        "decoded_dir": "registered_command_portraits",
        "records": {
            "SCO": {
                "stem": "portrait_SCO_territorial_defence_commander",
                "label": "Ewan Clacher - territorial defence commander",
            },
            "WLS": {
                "stem": "portrait_WLS_territorial_defence_commander",
                "label": "Iorwerth Driscoll - territorial defence commander",
            },
            "BRI": {
                "stem": "portrait_BRI_territorial_defence_commander",
                "label": "Jodoc Tanet - territorial defence commander",
            },
            "RHI": {
                "stem": "portrait_RHI_security_commander",
                "label": "Theodor Berglen - security commander",
            },
            "BAY": {
                "stem": "portrait_BAY_landwehr_commander",
                "label": "Emil Wilbs - Landwehr commander",
            },
        },
    },
}


def font(size: int, *, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    filename = "arialbd.ttf" if bold else "arial.ttf"
    candidates = (
        Path("C:/Windows/Fonts") / filename,
        Path(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
            if bold
            else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        ),
    )
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


def prepare_directories() -> None:
    directories = [CONTACT_ROOT, RUNTIME_ROOT]
    for category in PORTRAITS.values():
        directories.extend(
            (
                PROCESSED_ROOT / str(category["processed_dir"]),
                DECODED_ROOT / str(category["decoded_dir"]),
            )
        )
    directories.extend(
        (
            PROCESSED_ROOT / "registered_command_portraits_small",
            DECODED_ROOT / "registered_command_portraits_small",
        )
    )
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)


def finish_portrait(source: Image.Image, size: tuple[int, int]) -> Image.Image:
    image = ImageOps.fit(
        source.convert("RGB"),
        size,
        method=Image.Resampling.LANCZOS,
        centering=(0.5, 0.46),
    )
    image = ImageOps.autocontrast(image, cutoff=0.35)
    image = ImageEnhance.Color(image).enhance(0.92)
    image = ImageEnhance.Contrast(image).enhance(1.035)
    image = image.filter(ImageFilter.UnsharpMask(radius=0.72, percent=92, threshold=2))
    return image.convert("RGBA")


def convert_dds(png_path: Path, dds_path: Path, size: tuple[int, int]) -> None:
    command = [
        sys.executable,
        str(DDS_CONVERTER),
        "--input",
        str(png_path),
        "--output",
        str(dds_path),
        "--width",
        str(size[0]),
        "--height",
        str(size[1]),
    ]
    result = subprocess.run(command, check=False, text=True, capture_output=True)
    if result.returncode:
        raise RuntimeError(
            f"DDS conversion failed for {png_path}:\n{result.stdout}\n{result.stderr}"
        )


def validate_dds(path: Path, expected_size: tuple[int, int]) -> None:
    raw = path.read_bytes()
    if len(raw) < 128 or raw[:4] != b"DDS ":
        raise ValueError(f"Invalid DDS magic/header: {path}")
    header_size = struct.unpack_from("<I", raw, 4)[0]
    height = struct.unpack_from("<I", raw, 12)[0]
    width = struct.unpack_from("<I", raw, 16)[0]
    pitch = struct.unpack_from("<I", raw, 20)[0]
    pf_size = struct.unpack_from("<I", raw, 76)[0]
    pf_flags = struct.unpack_from("<I", raw, 80)[0]
    rgb_bits = struct.unpack_from("<I", raw, 88)[0]
    masks = struct.unpack_from("<IIII", raw, 92)
    caps = struct.unpack_from("<I", raw, 108)[0]
    expected_masks = (0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000)
    if (width, height) != expected_size:
        raise ValueError(f"Unexpected DDS dimensions in {path}: {(width, height)}")
    if header_size != 124 or pf_size != 32 or pf_flags != 0x41 or rgb_bits != 32:
        raise ValueError(f"DDS is not uncompressed 32-bit BGRA: {path}")
    if masks != expected_masks or caps != 0x1000 or pitch != width * 4:
        raise ValueError(f"Unexpected DDS masks/caps/pitch: {path}")
    if len(raw) != 128 + width * height * 4:
        raise ValueError(f"Unexpected DDS payload length: {path}")


def decode_bgra_dds(path: Path, expected_size: tuple[int, int]) -> Image.Image:
    validate_dds(path, expected_size)
    raw = path.read_bytes()
    height, width = struct.unpack_from("<II", raw, 12)
    data = raw[128:]
    rgba = bytearray(len(data))
    for index in range(0, len(data), 4):
        blue, green, red, alpha = data[index : index + 4]
        rgba[index : index + 4] = bytes((red, green, blue, alpha))
    image = Image.frombytes("RGBA", (width, height), bytes(rgba))
    extrema = image.getchannel("A").getextrema()
    if extrema != (255, 255):
        raise ValueError(f"Unexpected alpha range in {path}: {extrema}")
    return image


def verify_round_trip(processed: Image.Image, decoded: Image.Image, path: Path) -> None:
    difference = ImageChops.difference(processed.convert("RGBA"), decoded.convert("RGBA"))
    if difference.getbbox() is not None:
        raise ValueError(f"Decoded DDS pixels differ from processed PNG: {path}")


def process_portraits() -> dict[str, dict[str, dict[str, Path]]]:
    outputs: dict[str, dict[str, dict[str, Path]]] = {"institutional": {}, "command": {}}
    for category_name, category in PORTRAITS.items():
        source_directory = SOURCE_ROOT / str(category["source_dir"])
        processed_directory = PROCESSED_ROOT / str(category["processed_dir"])
        decoded_directory = DECODED_ROOT / str(category["decoded_dir"])
        records = category["records"]
        assert isinstance(records, dict)
        for tag, record in records.items():
            assert isinstance(record, dict)
            stem = str(record["stem"])
            source_path = source_directory / f"{stem}_source.png"
            source = Image.open(source_path)
            large = finish_portrait(source, (156, 210))
            png_output = processed_directory / f"{stem}.png"
            large.save(png_output)
            dds_output = RUNTIME_ROOT / f"{stem}.dds"
            convert_dds(png_output, dds_output, (156, 210))
            decoded = decode_bgra_dds(dds_output, (156, 210))
            verify_round_trip(large, decoded, dds_output)
            decoded_output = decoded_directory / f"{stem}.png"
            decoded.save(decoded_output)
            outputs[category_name][tag] = {
                "source": source_path,
                "processed": png_output,
                "dds": dds_output,
                "decoded": decoded_output,
            }

            if category_name == "command":
                small = finish_portrait(large, (50, 67))
                small_png = PROCESSED_ROOT / "registered_command_portraits_small" / f"{stem}_small.png"
                small.save(small_png)
                small_dds = RUNTIME_ROOT / f"{stem}_small.dds"
                convert_dds(small_png, small_dds, (50, 67))
                small_decoded_image = decode_bgra_dds(small_dds, (50, 67))
                verify_round_trip(small, small_decoded_image, small_dds)
                small_decoded = DECODED_ROOT / "registered_command_portraits_small" / f"{stem}_small.png"
                small_decoded_image.save(small_decoded)
                outputs[category_name][tag].update(
                    {
                        "small_processed": small_png,
                        "small_dds": small_dds,
                        "small_decoded": small_decoded,
                    }
                )
    return outputs


def draw_contain(
    canvas: Image.Image,
    image: Image.Image,
    box: tuple[int, int, int, int],
    *,
    nearest: bool = False,
) -> None:
    left, top, right, bottom = box
    target = image.copy().convert("RGBA")
    resampling = Image.Resampling.NEAREST if nearest else Image.Resampling.LANCZOS
    target.thumbnail((right - left, bottom - top), resampling)
    x = left + ((right - left) - target.width) // 2
    y = top + ((bottom - top) - target.height) // 2
    canvas.alpha_composite(target, (x, y))


def draw_centered_lines(
    draw: ImageDraw.ImageDraw,
    text: str,
    box: tuple[int, int, int, int],
    *,
    size: int,
    bold: bool = False,
    wrap_width: int = 32,
) -> None:
    left, top, right, _ = box
    text_font = font(size, bold=bold)
    y = top
    for line in wrap(text, width=wrap_width):
        bounds = draw.textbbox((0, 0), line, font=text_font)
        width = bounds[2] - bounds[0]
        draw.text(
            (left + ((right - left) - width) // 2, y),
            line,
            font=text_font,
            fill="#f4f0e8",
        )
        y += size + 4


def build_category_contact_sheet(
    category_name: str,
    outputs: dict[str, dict[str, dict[str, Path]]],
) -> Path:
    category = PORTRAITS[category_name]
    records = category["records"]
    assert isinstance(records, dict)
    card_w, card_h, header_h = 320, 390, 88
    sheet = Image.new("RGBA", (card_w * 5, header_h + card_h), "#161b22")
    draw = ImageDraw.Draw(sheet)
    title = "registered institutional councils" if category_name == "institutional" else "registered fictional officers"
    draw.text((28, 18), f"Event 006 - {title}", font=font(29, bold=True), fill="#f4f0e8")
    draw.text((29, 53), "Independent ImageGen sources; final 156x210 processed portrait crop shown", font=font(16), fill="#b8c1cc")
    for index, (tag, record) in enumerate(records.items()):
        assert isinstance(record, dict)
        left, top = index * card_w, header_h
        draw.rounded_rectangle(
            (left + 10, top + 10, left + card_w - 10, top + card_h - 10),
            radius=10,
            fill="#252c35",
            outline="#5b6878",
            width=2,
        )
        image = Image.open(outputs[category_name][tag]["processed"]).convert("RGBA")
        draw_contain(sheet, image.resize((218, 294), Image.Resampling.LANCZOS), (left + 50, top + 28, left + 270, top + 324))
        draw_centered_lines(
            draw,
            f"{tag} - {record['label']}",
            (left + 22, top + 328, left + card_w - 22, top + card_h - 18),
            size=16,
            bold=True,
        )
    filename = (
        "006_nwe_registered_institutional_portraits_contact_sheet.png"
        if category_name == "institutional"
        else "006_nwe_registered_command_portraits_contact_sheet.png"
    )
    output = CONTACT_ROOT / filename
    sheet.convert("RGB").save(output, quality=95)
    return output


def build_decoded_contact_sheets(
    outputs: dict[str, dict[str, dict[str, Path]]]
) -> tuple[Path, Path]:
    card_w, card_h, header_h = 300, 360, 88
    sheet = Image.new("RGBA", (card_w * 5, header_h + card_h * 2), "#161b22")
    draw = ImageDraw.Draw(sheet)
    draw.text((28, 18), "Event 006 - registered portrait DDS decode", font=font(29, bold=True), fill="#f4f0e8")
    draw.text((29, 53), "Actual runtime files decoded after conversion: 156x210 uncompressed BGRA", font=font(16), fill="#b8c1cc")
    for row, category_name in enumerate(("institutional", "command")):
        records = PORTRAITS[category_name]["records"]
        assert isinstance(records, dict)
        for column, (tag, record) in enumerate(records.items()):
            assert isinstance(record, dict)
            left, top = column * card_w, header_h + row * card_h
            draw.rounded_rectangle(
                (left + 10, top + 10, left + card_w - 10, top + card_h - 10),
                radius=10,
                fill="#252c35",
                outline="#5b6878",
                width=2,
            )
            image = Image.open(outputs[category_name][tag]["decoded"]).convert("RGBA")
            draw_contain(sheet, image.resize((202, 272), Image.Resampling.NEAREST), (left + 48, top + 24, left + 252, top + 298), nearest=True)
            draw_centered_lines(
                draw,
                f"{tag} - {record['label']}",
                (left + 20, top + 302, left + card_w - 20, top + card_h - 14),
                size=15,
                bold=True,
            )
    large_output = CONTACT_ROOT / "006_nwe_registered_final_dds_decoded_contact_sheet.png"
    sheet.convert("RGB").save(large_output, quality=95)

    small_sheet = Image.new("RGBA", (240 * 5, 248), "#161b22")
    small_draw = ImageDraw.Draw(small_sheet)
    small_draw.text((24, 14), "Event 006 - officer thumbnail DDS decode", font=font(25, bold=True), fill="#f4f0e8")
    small_draw.text((25, 45), "Actual 50x67 army portrait files enlarged with nearest-neighbour sampling", font=font(15), fill="#b8c1cc")
    records = PORTRAITS["command"]["records"]
    assert isinstance(records, dict)
    for column, (tag, record) in enumerate(records.items()):
        assert isinstance(record, dict)
        left = column * 240
        image = Image.open(outputs["command"][tag]["small_decoded"]).convert("RGBA")
        draw_contain(small_sheet, image.resize((150, 201), Image.Resampling.NEAREST), (left + 45, 68, left + 195, 204), nearest=True)
        person_name = str(record["label"]).split(" - ", 1)[0]
        draw_centered_lines(
            small_draw,
            f"{tag} - {person_name}",
            (left + 10, 207, left + 230, 242),
            size=15,
            bold=True,
            wrap_width=25,
        )
    small_output = CONTACT_ROOT / "006_nwe_registered_officer_small_dds_decoded_contact_sheet.png"
    small_sheet.convert("RGB").save(small_output, quality=95)
    return large_output, small_output


def runtime_paths() -> list[Path]:
    paths: list[Path] = []
    for category_name, category in PORTRAITS.items():
        records = category["records"]
        assert isinstance(records, dict)
        for record in records.values():
            assert isinstance(record, dict)
            stem = str(record["stem"])
            paths.append(RUNTIME_ROOT / f"{stem}.dds")
            if category_name == "command":
                paths.append(RUNTIME_ROOT / f"{stem}_small.dds")
    return paths


def write_hash_ledger(contact_sheets: list[Path]) -> None:
    paths: list[Path] = []
    for category in PORTRAITS.values():
        paths.extend((SOURCE_ROOT / str(category["source_dir"])).glob("*.png"))
        paths.extend((PROCESSED_ROOT / str(category["processed_dir"])).glob("*.png"))
        paths.extend((DECODED_ROOT / str(category["decoded_dir"])).glob("*.png"))
    paths.extend((PROCESSED_ROOT / "registered_command_portraits_small").glob("*.png"))
    paths.extend((DECODED_ROOT / "registered_command_portraits_small").glob("*.png"))
    paths.extend(contact_sheets)
    paths.extend(runtime_paths())
    rows = []
    for path in sorted(set(paths), key=lambda item: item.relative_to(ROOT).as_posix().lower()):
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        rows.append(f"{digest}  {path.relative_to(ROOT).as_posix()}")
    HASH_LEDGER.write_text("\n".join(rows) + "\n", encoding="utf-8")


def main() -> int:
    prepare_directories()
    outputs = process_portraits()
    contact_sheets = [
        build_category_contact_sheet("institutional", outputs),
        build_category_contact_sheet("command", outputs),
    ]
    contact_sheets.extend(build_decoded_contact_sheets(outputs))
    write_hash_ledger(contact_sheets)
    print("Built 10 large portraits and 5 officer thumbnails.")
    print("All 15 runtime DDS files passed exact PNG-to-DDS pixel round-trip validation.")
    print(f"Hash ledger: {HASH_LEDGER.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
