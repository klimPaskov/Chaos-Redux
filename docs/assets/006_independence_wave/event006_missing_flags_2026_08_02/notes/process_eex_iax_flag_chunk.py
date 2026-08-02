from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


PACKAGE = Path(__file__).resolve().parents[1]
SOURCE_DIR = PACKAGE / "source_png"
PROCESSED_DIR = PACKAGE / "processed_png"
FINAL_DIR = PACKAGE / "final_tga"
RUNTIME_ROOT = Path(__file__).resolve().parents[5]
RUNTIME_DIR = RUNTIME_ROOT / "gfx" / "flags"
CONTACT_DIR = PACKAGE / "contact_sheets"
METADATA_DIR = PACKAGE / "metadata"

IDENTITIES = {
    "EEX": "Bunyoro",
    "EHX": "Ankole",
    "ERX": "Ndebele",
    "ESX": "Xhosa",
    "EWX": "Herero State",
    "FAX": "Comoros",
    "FBX": "Mauritius",
    "FDX": "Punjab",
    "FLX": "Travancore",
    "FNX": "Dravidian Federation",
    "FOX": "Assam",
    "FSX": "Himalayan Confederation",
    "FUX": "Minangkabau",
    "FVX": "Riau",
    "FXX": "Bugis State",
    "GBX": "Pattani",
    "GCX": "Shan Federation",
    "IAX": "Mon State",
}

SIZES = {
    "normal": (82, 52),
    "medium": (41, 26),
    "small": (10, 7),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def crop_ratio(image: Image.Image) -> Image.Image:
    target = 82 / 52
    width, height = image.size
    ratio = width / height
    if ratio > target:
        new_width = int(round(height * target))
        left = (width - new_width) // 2
        return image.crop((left, 0, left + new_width, height))
    new_height = int(round(width / target))
    top = (height - new_height) // 2
    return image.crop((0, top, width, top + new_height))


def write_bottom_left_tga(image: Image.Image, path: Path) -> None:
    image = image.convert("RGBA")
    width, height = image.size
    pixels = image.load()
    header = bytearray(18)
    header[2] = 2
    header[12:14] = width.to_bytes(2, "little")
    header[14:16] = height.to_bytes(2, "little")
    header[16] = 32
    header[17] = 8
    body = bytearray()
    for y in range(height - 1, -1, -1):
        for x in range(width):
            red, green, blue, alpha = pixels[x, y]
            body.extend((blue, green, red, alpha))
    path.write_bytes(bytes(header) + bytes(body))


def expected_tga_bytes(image: Image.Image) -> bytes:
    image = image.convert("RGBA")
    width, height = image.size
    pixels = image.load()
    body = bytearray()
    for y in range(height - 1, -1, -1):
        for x in range(width):
            red, green, blue, alpha = pixels[x, y]
            body.extend((blue, green, red, alpha))
    return bytes(body)


def tga_header(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    width = int.from_bytes(data[12:14], "little")
    height = int.from_bytes(data[14:16], "little")
    return {
        "image_type": data[2],
        "width": width,
        "height": height,
        "pixel_depth": data[16],
        "descriptor": data[17],
        "origin": "bottom-left" if (data[17] & 0x30) == 0 else "non-bottom-left",
        "byte_length": len(data),
        "expected_byte_length": 18 + width * height * 4,
    }


def make_contact_sheet(paths: list[Path], output: Path, title: str, cell_size: tuple[int, int]) -> None:
    cell_width, cell_height = cell_size
    columns = 3
    rows = math.ceil(len(paths) / columns)
    margin = 18
    label_height = 38
    canvas = Image.new("RGB", (columns * cell_width + margin * 2, rows * (cell_height + label_height) + margin * 2 + 36), (27, 29, 32))
    draw = ImageDraw.Draw(canvas)
    draw.text((margin, 10), title, fill=(240, 240, 240))
    try:
        font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 14)
    except OSError:
        font = ImageFont.load_default()
    for index, path in enumerate(paths):
        row, column = divmod(index, columns)
        x = margin + column * cell_width
        y = margin + 36 + row * (cell_height + label_height)
        image = Image.open(path).convert("RGB")
        image.thumbnail((cell_width - 12, cell_height - 12), Image.Resampling.NEAREST)
        tile = Image.new("RGB", (cell_width, cell_height), (55, 58, 62))
        tile.paste(image, ((cell_width - image.width) // 2, (cell_height - image.height) // 2))
        canvas.paste(tile, (x, y))
        draw.text((x + 4, y + cell_height + 4), path.stem, fill=(240, 240, 240), font=font)
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output)


def make_comparison_sheet(tags: list[str], output: Path) -> None:
    cell_width, cell_height = 240, 150
    columns = 4
    rows = math.ceil(len(tags) / 2)
    margin = 18
    label_height = 28
    title_height = 38
    canvas = Image.new("RGB", (columns * cell_width + margin * 2, rows * (cell_height + label_height) + margin * 2 + title_height), (27, 29, 32))
    draw = ImageDraw.Draw(canvas)
    draw.text((margin, 10), "Event 006 EEX-IAX source and normal/medium/small ladders", fill=(240, 240, 240))
    try:
        font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 13)
    except OSError:
        font = ImageFont.load_default()
    for index, tag in enumerate(tags):
        row, pair = divmod(index, 2)
        x = margin + pair * 2 * cell_width
        y = margin + title_height + row * (cell_height + label_height)
        source = Image.open(SOURCE_DIR / f"{tag}_imagegen_raw.png").convert("RGB")
        normal = Image.open(PROCESSED_DIR / "normal" / f"{tag}.png").convert("RGB")
        medium = Image.open(PROCESSED_DIR / "medium" / f"{tag}.png").convert("RGB")
        small = Image.open(PROCESSED_DIR / "small" / f"{tag}.png").convert("RGB")
        images = [source, normal, medium, small]
        for offset, image in enumerate(images):
            tile = Image.new("RGB", (cell_width, cell_height), (55, 58, 62))
            image.thumbnail((cell_width - 12, cell_height - 12), Image.Resampling.NEAREST)
            tile.paste(image, ((cell_width - image.width) // 2, (cell_height - image.height) // 2))
            canvas.paste(tile, (x + (offset % 2) * cell_width, y + (offset // 2) * cell_height))
        draw.text((x + 4, y + cell_height * 2 + 4), f"{tag} {IDENTITIES[tag]} | source+normal / medium+small", fill=(240, 240, 240), font=font)
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output)


def main() -> None:
    for directory in (PROCESSED_DIR, FINAL_DIR, RUNTIME_DIR, RUNTIME_DIR / "medium", RUNTIME_DIR / "small", CONTACT_DIR, METADATA_DIR):
        directory.mkdir(parents=True, exist_ok=True)

    records: dict[str, dict[str, object]] = {}
    source_sheet: list[Path] = []
    normal_sheet: list[Path] = []
    for tag, identity in IDENTITIES.items():
        source_path = SOURCE_DIR / f"{tag}_imagegen_raw.png"
        image = Image.open(source_path).convert("RGB")
        source_sheet.append(source_path)
        cropped = crop_ratio(image)
        master = cropped.resize((820, 520), Image.Resampling.LANCZOS)
        master_path = PROCESSED_DIR / f"{tag}_flat_master_820x520.png"
        master.save(master_path)
        records[tag] = {
            "identity": identity,
            "source_mode": "imagegen",
            "source_png": str(source_path.relative_to(PACKAGE)).replace("\\", "/"),
            "source_dimensions": list(image.size),
            "source_sha256": sha256(source_path),
            "processed_master": str(master_path.relative_to(PACKAGE)).replace("\\", "/"),
            "processed_master_dimensions": list(master.size),
            "processed_master_sha256": sha256(master_path),
            "sizes": {},
            "status": "converted",
        }
        for size_name, (width, height) in SIZES.items():
            sized = master.resize((width, height), Image.Resampling.LANCZOS)
            processed_dir = PROCESSED_DIR / size_name
            processed_dir.mkdir(parents=True, exist_ok=True)
            processed_path = processed_dir / f"{tag}.png"
            sized.save(processed_path)
            final_path = FINAL_DIR / f"{tag}_{size_name}_{width}x{height}.tga"
            runtime_path = RUNTIME_DIR / ("medium" if size_name == "medium" else "small" if size_name == "small" else "") / f"{tag}.tga"
            write_bottom_left_tga(sized, final_path)
            write_bottom_left_tga(sized, runtime_path)
            header = tga_header(final_path)
            if header["image_type"] != 2 or header["pixel_depth"] != 32 or header["descriptor"] != 8 or header["origin"] != "bottom-left":
                raise RuntimeError(f"Invalid TGA header for {final_path}: {header}")
            if header["byte_length"] != header["expected_byte_length"]:
                raise RuntimeError(f"Invalid TGA length for {final_path}: {header}")
            readback_match = final_path.read_bytes()[18:] == expected_tga_bytes(sized)
            if not readback_match:
                raise RuntimeError(f"TGA pixel readback mismatch for {final_path}")
            if size_name == "normal":
                normal_sheet.append(processed_path)
            records[tag]["sizes"][size_name] = {
                "dimensions": [width, height],
                "processed_png": str(processed_path.relative_to(PACKAGE)).replace("\\", "/"),
                "processed_png_sha256": sha256(processed_path),
                "package_tga": str(final_path.relative_to(PACKAGE)).replace("\\", "/"),
                "package_tga_sha256": sha256(final_path),
                "runtime_tga": str(runtime_path.relative_to(RUNTIME_ROOT)).replace("\\", "/"),
                "runtime_tga_sha256": sha256(runtime_path),
                "tga_header": header,
                "readback_match": readback_match,
            }

    make_contact_sheet(source_sheet, CONTACT_DIR / "eex_iax_source_masters_contact_sheet.png", "Event 006 EEX-IAX ImageGen source masters", (360, 225))
    make_contact_sheet(normal_sheet, CONTACT_DIR / "eex_iax_normal_flags_contact_sheet.png", "Event 006 EEX-IAX normal flag exports", (246, 156))
    make_comparison_sheet(list(IDENTITIES), CONTACT_DIR / "eex_iax_source_and_ladders_contact_sheet.png")
    metadata_path = METADATA_DIR / "eex_iax_flag_validation.json"
    metadata_path.write_text(json.dumps({
        "package": "006_independence_wave/event006_missing_flags_2026_08_02",
        "chunk": "EEX-IAX",
        "asset_type": "historical and historically grounded flat flags",
        "target_sizes": {key: list(value) for key, value in SIZES.items()},
        "flags": records,
        "contact_sheets": [
            "contact_sheets/eex_iax_source_masters_contact_sheet.png",
            "contact_sheets/eex_iax_normal_flags_contact_sheet.png",
            "contact_sheets/eex_iax_source_and_ladders_contact_sheet.png",
        ],
    }, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
