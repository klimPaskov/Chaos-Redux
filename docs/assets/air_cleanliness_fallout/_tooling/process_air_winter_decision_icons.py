from __future__ import annotations

import hashlib
import math
import os
import struct
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[4]
PACKAGE = ROOT / "docs" / "assets" / "air_cleanliness_fallout"
SOURCE = PACKAGE / "source_png" / "decisions"
MASTER = PACKAGE / "source_png" / "decisions" / "transparent_master"
PROCESSED = PACKAGE / "processed_png" / "decisions"
DECODED = PACKAGE / "dds_decoded_png" / "decisions"
CONTACT = PACKAGE / "contact_sheets" / "air_winter_decision_icons_dds_decoded_contact_sheet.png"
RUNTIME = ROOT / "gfx" / "interface" / "air_cleanliness_winter" / "decisions"
CONVERTER = ROOT / ".tools" / "convert_to_dds.py"
APPROVED_TEXCONV = Path(
    "C:/Users/klimp/AppData/Local/Temp/chaos_redux_tools/texconv-may2026.exe"
)
APPROVED_TEXCONV_SHA256 = (
    "dcfdec10244e02cf5037fba089c55fb7e1326b1c8181742d77d15fa5cb5eef06"
)
EXPECTED_MASKS = (0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000)


@dataclass(frozen=True)
class Asset:
    stem: str
    sprite: str
    size: tuple[int, int]
    kind: str


ASSETS = [
    Asset(
        "decision_air_winter_response_category",
        "GFX_decision_air_winter_response_category",
        (52, 40),
        "decision category icon",
    ),
    Asset(
        "decision_air_winter_response_priority",
        "GFX_decision_air_winter_response_priority",
        (32, 32),
        "decision icon",
    ),
    Asset("decision_air_winter_reception", "GFX_decision_air_winter_reception", (32, 32), "decision icon"),
    Asset("decision_air_winter_respirators", "GFX_decision_air_winter_respirators", (32, 32), "decision icon"),
    Asset("decision_air_winter_clinics", "GFX_decision_air_winter_clinics", (32, 32), "decision icon"),
    Asset("decision_air_winter_samplers", "GFX_decision_air_winter_samplers", (32, 32), "decision icon"),
    Asset("decision_air_winter_crop_trials", "GFX_decision_air_winter_crop_trials", (32, 32), "decision icon"),
    Asset("decision_air_winter_ash_clearance", "GFX_decision_air_winter_ash_clearance", (32, 32), "decision icon"),
    Asset("decision_air_winter_rail_corridors", "GFX_decision_air_winter_rail_corridors", (32, 32), "decision icon"),
    Asset("decision_air_winter_airfield_closure", "GFX_decision_air_winter_airfield_closure", (32, 32), "decision icon"),
    Asset("decision_air_winter_evacuation_ledger", "GFX_decision_air_winter_evacuation_ledger", (32, 32), "decision icon"),
    Asset("decision_air_winter_shelter_law", "GFX_decision_air_winter_shelter_law", (32, 32), "decision icon"),
    Asset("decision_air_winter_greenhouse_refuge", "GFX_decision_air_winter_greenhouse_refuge", (32, 32), "decision icon"),
    Asset("decision_air_winter_controlled_evacuation", "GFX_decision_air_winter_controlled_evacuation", (32, 32), "decision icon"),
    Asset("decision_air_winter_medical_triage", "GFX_decision_air_winter_medical_triage", (32, 32), "decision icon"),
    Asset("decision_air_winter_abandonment_vote", "GFX_decision_air_winter_abandonment_vote", (32, 32), "decision icon"),
    Asset("decision_air_winter_bunker_seal", "GFX_decision_air_winter_bunker_seal", (32, 32), "decision icon"),
    Asset("decision_air_winter_final_evacuation", "GFX_decision_air_winter_final_evacuation", (32, 32), "decision icon"),
    Asset("decision_air_winter_decontamination", "GFX_decision_air_winter_decontamination", (32, 32), "decision icon"),
]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_backend() -> None:
    if not APPROVED_TEXCONV.is_file():
        raise FileNotFoundError(f"Approved texconv is missing: {APPROVED_TEXCONV}")
    actual = sha256_file(APPROVED_TEXCONV)
    if actual != APPROVED_TEXCONV_SHA256:
        raise RuntimeError(
            f"Approved texconv hash mismatch: {actual}. Expected {APPROVED_TEXCONV_SHA256}"
        )


def trim_alpha(image: Image.Image) -> Image.Image:
    rgba = image.convert("RGBA")
    threshold = rgba.getchannel("A").point(lambda value: 255 if value > 8 else 0)
    bbox = threshold.getbbox()
    if bbox is None:
        raise RuntimeError("Transparent master has no visible subject")
    return rgba.crop(bbox)


def render_icon(master: Image.Image, target: tuple[int, int]) -> Image.Image:
    scale = 4
    high_size = (target[0] * scale, target[1] * scale)
    padding = 2 * scale
    subject = trim_alpha(master)
    subject.thumbnail(
        (high_size[0] - padding * 2, high_size[1] - padding * 2),
        Image.Resampling.LANCZOS,
    )

    layer = Image.new("RGBA", high_size, (0, 0, 0, 0))
    x = (high_size[0] - subject.width) // 2
    y = (high_size[1] - subject.height) // 2
    layer.paste(subject, (x, y), subject)
    alpha = layer.getchannel("A")

    shadow_alpha = alpha.filter(ImageFilter.GaussianBlur(radius=3.0))
    shadow_shifted = Image.new("L", high_size, 0)
    shadow_shifted.paste(shadow_alpha, (scale, scale))
    shadow_shifted = shadow_shifted.point(lambda value: round(value * 0.34))
    shadow = Image.new("RGBA", high_size, (0, 0, 0, 0))
    shadow.putalpha(shadow_shifted)

    outline_alpha = alpha.filter(ImageFilter.MaxFilter(9))
    outline = Image.new("RGBA", high_size, (8, 11, 14, 255))
    outline.putalpha(outline_alpha)

    composed = Image.new("RGBA", high_size, (0, 0, 0, 0))
    composed = Image.alpha_composite(composed, shadow)
    composed = Image.alpha_composite(composed, outline)
    composed = Image.alpha_composite(composed, layer)
    return composed.resize(target, Image.Resampling.LANCZOS)


def convert_dds(png: Path, dds: Path, size: tuple[int, int]) -> None:
    env = os.environ.copy()
    env["TEXCONV_PATH"] = str(APPROVED_TEXCONV)
    env.pop("TEXCONV_EXE", None)
    env.pop("TEXCONV_DOCKER_IMAGE", None)
    subprocess.run(
        [
            sys.executable,
            str(CONVERTER),
            "--input",
            str(png),
            "--output",
            str(dds),
            "--width",
            str(size[0]),
            "--height",
            str(size[1]),
        ],
        cwd=ROOT,
        env=env,
        check=True,
    )


def parse_dds(path: Path) -> dict[str, object]:
    raw = path.read_bytes()
    if len(raw) < 128 or raw[:4] != b"DDS ":
        raise RuntimeError(f"Invalid DDS magic/header: {path}")
    values = struct.unpack("<31I", raw[4:128])
    width = values[3]
    height = values[2]
    mip_count = values[6]
    bits = values[21]
    masks = (values[22], values[23], values[24], values[25])
    expected_size = 128 + width * height * 4
    if len(raw) != expected_size:
        raise RuntimeError(
            f"Unexpected DDS byte size for {path}: {len(raw)}. Expected {expected_size}"
        )
    return {
        "width": width,
        "height": height,
        "mip_count": mip_count,
        "bits": bits,
        "masks": masks,
        "byte_size": len(raw),
    }


def checker(size: tuple[int, int], tile: int = 8) -> Image.Image:
    board = Image.new("RGBA", size, (54, 59, 66, 255))
    draw = ImageDraw.Draw(board)
    for y in range(0, size[1], tile):
        for x in range(0, size[0], tile):
            if (x // tile + y // tile) % 2:
                draw.rectangle((x, y, x + tile - 1, y + tile - 1), fill=(82, 88, 96, 255))
    return board


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    name = "arialbd.ttf" if bold else "arial.ttf"
    path = Path("C:/Windows/Fonts") / name
    try:
        return ImageFont.truetype(path, size=size)
    except OSError:
        return ImageFont.load_default()


def short_label(stem: str) -> str:
    return stem.removeprefix("decision_air_winter_").replace("_", " ").title()


def make_contact_sheet() -> None:
    columns = 4
    cell_w = 285
    cell_h = 205
    rows = math.ceil(len(ASSETS) / columns)
    sheet = Image.new("RGB", (columns * cell_w, rows * cell_h + 54), (18, 21, 26))
    draw = ImageDraw.Draw(sheet)
    title_font = load_font(22, bold=True)
    label_font = load_font(15, bold=True)
    meta_font = load_font(11)
    draw.text(
        (18, 14),
        "Air Winter decision icons: DDS-decoded alpha and native-size review",
        font=title_font,
        fill=(236, 240, 245),
    )

    for index, asset in enumerate(ASSETS):
        col = index % columns
        row = index // columns
        left = col * cell_w
        top = 54 + row * cell_h
        draw.rounded_rectangle(
            (left + 6, top + 6, left + cell_w - 7, top + cell_h - 7),
            radius=8,
            fill=(29, 33, 40),
            outline=(76, 84, 94),
            width=1,
        )
        decoded = Image.open(DECODED / f"{asset.stem}.png").convert("RGBA")
        scale = 3 if asset.kind == "decision category icon" else 4
        enlarged = decoded.resize(
            (decoded.width * scale, decoded.height * scale), Image.Resampling.NEAREST
        )
        preview = checker((174, 128))
        preview.alpha_composite(
            enlarged,
            ((preview.width - enlarged.width) // 2, (preview.height - enlarged.height) // 2),
        )
        sheet.paste(preview.convert("RGB"), (left + 14, top + 43))

        native = checker((68, 54), tile=4)
        native.alpha_composite(
            decoded,
            ((native.width - decoded.width) // 2, (native.height - decoded.height) // 2),
        )
        sheet.paste(native.convert("RGB"), (left + 199, top + 92))
        draw.text((left + 14, top + 15), short_label(asset.stem), font=label_font, fill=(235, 238, 243))
        draw.text((left + 14, top + 176), asset.sprite, font=meta_font, fill=(176, 187, 199))
        draw.text(
            (left + 199, top + 151),
            f"native {asset.size[0]}x{asset.size[1]}",
            font=meta_font,
            fill=(157, 169, 181),
        )

    CONTACT.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(CONTACT)


def count_magenta(image: Image.Image) -> int:
    return sum(
        1
        for red, green, blue, alpha in image.convert("RGBA").getdata()
        if alpha > 8 and red > 180 and blue > 180 and green < 100
    )


def require_exact_inventory(label: str, actual: set[str], expected: set[str]) -> None:
    missing = sorted(expected - actual)
    extra = sorted(actual - expected)
    if missing or extra:
        raise RuntimeError(f"{label} inventory mismatch. Missing={missing}. Extra={extra}")


def main() -> None:
    validate_backend()
    for path in (PROCESSED, DECODED, RUNTIME):
        path.mkdir(parents=True, exist_ok=True)

    expected_source = {f"{asset.stem}_source.png" for asset in ASSETS}
    expected_master = {f"{asset.stem}_master.png" for asset in ASSETS}
    expected_png = {f"{asset.stem}.png" for asset in ASSETS}
    expected_dds = {f"{asset.stem}.dds" for asset in ASSETS}
    require_exact_inventory(
        "Raw source PNG",
        {path.name for path in SOURCE.glob("decision_air_winter_*_source.png")},
        expected_source,
    )
    require_exact_inventory(
        "Transparent master PNG",
        {path.name for path in MASTER.glob("decision_air_winter_*_master.png")},
        expected_master,
    )

    results: list[dict[str, object]] = []
    source_hashes: set[str] = set()
    master_hashes: set[str] = set()
    processed_hashes: set[str] = set()
    dds_hashes: set[str] = set()

    for asset in ASSETS:
        source = SOURCE / f"{asset.stem}_source.png"
        master = MASTER / f"{asset.stem}_master.png"
        processed = PROCESSED / f"{asset.stem}.png"
        dds = RUNTIME / f"{asset.stem}.dds"
        decoded_path = DECODED / f"{asset.stem}.png"
        if not source.is_file() or not master.is_file():
            raise FileNotFoundError(f"Missing source/master for {asset.stem}")

        icon = render_icon(Image.open(master), asset.size)
        icon.save(processed)
        convert_dds(processed, dds, asset.size)
        decoded = Image.open(dds).convert("RGBA")
        decoded.save(decoded_path)

        if decoded.size != asset.size or icon.size != asset.size:
            raise RuntimeError(f"Dimension mismatch for {asset.stem}")
        if ImageChops.difference(icon, decoded).getbbox() is not None:
            raise RuntimeError(f"DDS decoded pixels differ from processed PNG: {asset.stem}")
        alpha = decoded.getchannel("A")
        bbox = alpha.point(lambda value: 255 if value > 8 else 0).getbbox()
        if bbox is None:
            raise RuntimeError(f"No visible pixels in {asset.stem}")
        if any(decoded.getpixel(corner)[3] != 0 for corner in [(0, 0), (asset.size[0] - 1, 0), (0, asset.size[1] - 1), (asset.size[0] - 1, asset.size[1] - 1)]):
            raise RuntimeError(f"Opaque corner in {asset.stem}")
        center_error = (
            abs(((bbox[0] + bbox[2]) / 2) - asset.size[0] / 2),
            abs(((bbox[1] + bbox[3]) / 2) - asset.size[1] / 2),
        )
        if center_error[0] > 2.0 or center_error[1] > 2.0:
            raise RuntimeError(f"Alignment drift in {asset.stem}: {center_error}")
        if count_magenta(decoded):
            raise RuntimeError(f"Visible chroma-magenta remains in {asset.stem}")

        metadata = parse_dds(dds)
        if (
            (metadata["width"], metadata["height"]) != asset.size
            or metadata["mip_count"] not in (0, 1)
            or metadata["bits"] != 32
            or metadata["masks"] != EXPECTED_MASKS
        ):
            raise RuntimeError(f"DDS format mismatch for {asset.stem}: {metadata}")

        hashes = {
            "source": sha256_file(source),
            "master": sha256_file(master),
            "processed": sha256_file(processed),
            "dds": sha256_file(dds),
        }
        source_hashes.add(hashes["source"])
        master_hashes.add(hashes["master"])
        processed_hashes.add(hashes["processed"])
        dds_hashes.add(hashes["dds"])
        results.append(
            {
                "asset": asset,
                "bbox": bbox,
                "center_error": center_error,
                "transparent_pixels": sum(1 for value in alpha.getdata() if value == 0),
                "hashes": hashes,
                "metadata": metadata,
            }
        )

    expected_count = len(ASSETS)
    if not all(
        len(values) == expected_count
        for values in (source_hashes, master_hashes, processed_hashes, dds_hashes)
    ):
        raise RuntimeError("Asset uniqueness validation failed")
    require_exact_inventory(
        "Processed PNG",
        {path.name for path in PROCESSED.glob("decision_air_winter_*.png")},
        expected_png,
    )
    require_exact_inventory(
        "DDS-decoded PNG",
        {path.name for path in DECODED.glob("decision_air_winter_*.png")},
        expected_png,
    )
    require_exact_inventory(
        "Runtime DDS",
        {path.name for path in RUNTIME.glob("decision_air_winter_*.dds")},
        expected_dds,
    )

    make_contact_sheet()
    print("sprite\tsize\tbbox\tcenter_error\ttransparent\tprocessed_sha256\tdds_sha256")
    for result in results:
        asset = result["asset"]
        hashes = result["hashes"]
        print(
            f"{asset.sprite}\t{asset.size[0]}x{asset.size[1]}\t{result['bbox']}\t"
            f"({result['center_error'][0]:.1f},{result['center_error'][1]:.1f})\t"
            f"{result['transparent_pixels']}\t{hashes['processed']}\t{hashes['dds']}"
        )
    print(f"contact_sheet\t{CONTACT.relative_to(ROOT)}\t{sha256_file(CONTACT)}")
    print(f"approved_texconv_sha256\t{APPROVED_TEXCONV_SHA256}")


if __name__ == "__main__":
    main()
