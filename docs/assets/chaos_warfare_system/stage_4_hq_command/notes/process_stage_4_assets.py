"""Mechanical Stage 4 asset processing and DDS export.

This helper only crops transparent generated masters, pads them to the verified
runtime canvases, applies the active/muted presentation treatment, builds
review sheets, and writes the uncompressed DDS contract used by Stage 3.
It does not create artwork or invent visual changes between source frames.
"""

from pathlib import Path
import struct

from PIL import Image, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[1]
RUNTIME = ROOT.parents[3]


def fit_to_canvas(source: Path, size: tuple[int, int], inner: tuple[int, int], muted: bool = False) -> Image.Image:
    image = Image.open(source).convert("RGBA")
    alpha = image.getchannel("A")
    bbox = alpha.getbbox()
    if bbox is None:
        raise ValueError(f"transparent master has no visible subject: {source}")
    image = image.crop(bbox)
    image.thumbnail(inner, Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", size, (0, 0, 0, 0))
    x = (size[0] - image.width) // 2
    y = (size[1] - image.height) // 2
    canvas.alpha_composite(image, (x, y))
    if muted:
        gray = ImageOps.grayscale(canvas.convert("RGB"))
        rgb = ImageOps.colorize(gray, black=(34, 35, 31), white=(190, 190, 183))
        canvas = Image.merge("RGBA", (*rgb.split(), canvas.getchannel("A")))
    return canvas


def save_png(image: Image.Image, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path, "PNG")


def save_dds(image: Image.Image, path: Path) -> None:
    """Write the established 32-bit uncompressed Chaos Redux DDS layout."""
    image = image.convert("RGBA")
    width, height = image.size
    rgba = image.tobytes()
    bgra = bytearray(len(rgba))
    for offset in range(0, len(rgba), 4):
        r, g, b, a = rgba[offset : offset + 4]
        bgra[offset : offset + 4] = bytes((b, g, r, a))

    header = struct.pack(
        "<31I",
        124,
        135183,
        height,
        width,
        width * 4,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        32,
        65,
        0,
        32,
        0x00FF0000,
        0x0000FF00,
        0x000000FF,
        0xFF000000,
        0,
        0,
        0,
        0,
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(b"DDS " + header + bytes(bgra))


def checkerboard(size: tuple[int, int], tile: int = 8) -> Image.Image:
    image = Image.new("RGB", size, (44, 48, 46))
    draw = ImageDraw.Draw(image)
    for y in range(0, size[1], tile):
        for x in range(0, size[0], tile):
            if ((x // tile) + (y // tile)) % 2 == 0:
                draw.rectangle((x, y, x + tile - 1, y + tile - 1), fill=(76, 82, 78))
    return image


def contact_sheet(items: list[tuple[str, Image.Image]], path: Path, title: str, scale: int) -> None:
    font = ImageFont.load_default()
    cell_width = max(image.width for _, image in items) * scale + 32
    cell_height = max(image.height for _, image in items) * scale + 44
    columns = 3
    rows = (len(items) + columns - 1) // columns
    sheet = Image.new("RGB", (columns * cell_width, rows * cell_height + 30), (26, 29, 28))
    draw = ImageDraw.Draw(sheet)
    draw.text((12, 8), title, fill=(225, 229, 220), font=font)
    for index, (label, image) in enumerate(items):
        col = index % columns
        row = index // columns
        x0 = col * cell_width + 16
        y0 = row * cell_height + 36
        checker = checkerboard((image.width * scale, image.height * scale), max(4, scale * 2))
        enlarged = image.resize(checker.size, Image.Resampling.NEAREST)
        checker.paste(enlarged, (0, 0), enlarged.getchannel("A"))
        sheet.paste(checker, (x0, y0))
        draw.text((x0, y0 + checker.height + 4), label, fill=(220, 222, 214), font=font)
    path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(path, "PNG")


def process_counter_family(folder: str, frame_size: tuple[int, int], runtime_folder: str, runtime_prefix: str, scale: int) -> None:
    source_dir = ROOT / "source_png" / folder
    processed_dir = ROOT / "processed_png" / folder
    processed_dir.mkdir(parents=True, exist_ok=True)
    items = []
    for frame_zero in sorted(source_dir.glob("*_frame_000_master.png")):
        slug = frame_zero.name.removesuffix("_frame_000_master.png")
        frame_one = source_dir / f"{slug}_frame_001_master.png"
        if not frame_one.exists():
            raise FileNotFoundError(frame_one)
        active = fit_to_canvas(frame_zero, frame_size, (frame_size[0] - 4, frame_size[1] - 4))
        muted = fit_to_canvas(frame_one, frame_size, (frame_size[0] - 4, frame_size[1] - 4), muted=True)
        active_path = processed_dir / f"{slug}_frame_active.png"
        muted_path = processed_dir / f"{slug}_frame_muted.png"
        sheet_path = processed_dir / f"{slug}_sheet.png"
        save_png(active, active_path)
        save_png(muted, muted_path)
        sheet = Image.new("RGBA", (frame_size[0] * 2, frame_size[1]), (0, 0, 0, 0))
        sheet.alpha_composite(active, (0, 0))
        sheet.alpha_composite(muted, (frame_size[0], 0))
        save_png(sheet, sheet_path)
        runtime = RUNTIME / runtime_folder / f"{runtime_prefix}{slug}_icon.dds"
        save_dds(sheet, runtime)
        items.append((slug, sheet))
    contact_sheet(items, ROOT / "contact_sheets" / f"{folder}_contact_sheet_checker.png", f"Stage 4 HQ {folder} counters", scale)


def process_single_family(folder: str, size: tuple[int, int], runtime_folder: str, names: list[str], scale: int, title: str) -> None:
    source_dir = ROOT / "source_png" / folder
    processed_dir = ROOT / "processed_png" / folder
    processed_dir.mkdir(parents=True, exist_ok=True)
    items = []
    for slug in names:
        master = source_dir / f"{slug}_master.png"
        image = fit_to_canvas(master, size, (size[0] - 4, size[1] - 4))
        preview = processed_dir / f"{slug}.png"
        save_png(image, preview)
        save_dds(image, RUNTIME / runtime_folder / f"{slug}.dds")
        items.append((slug, image))
    contact_sheet(items, ROOT / "contact_sheets" / f"{folder}_contact_sheet_checker.png", title, scale)


HQ_SLUGS = [
    "cbrn_hq_operations_section",
    "cbrn_hq_intelligence_weather_cell",
    "cbrn_hq_protective_logistics_section",
    "cbrn_hq_mobile_decontamination_column",
    "cbrn_hq_medical_countermeasure_directorate",
    "cbrn_hq_biological_security_section",
]

ABILITY_SLUGS = [
    "cbrn_prepare_chemical_offensive",
    "cbrn_theater_protective_posture",
    "cbrn_decontamination_corridor",
    "cbrn_seal_operational_area",
    "cbrn_mass_antidote_response",
    "cbrn_seal_infection_corridor",
    "cbrn_combined_overmatch",
]


if __name__ == "__main__":
    process_counter_family(
        "unit_large",
        (76, 42),
        "gfx/interface/counters/divisions_large",
        "unit_",
        3,
    )
    process_counter_family(
        "unit_small",
        (30, 12),
        "gfx/interface/counters/divisions_small",
        "onmap_unit_",
        8,
    )
    process_single_family(
        "abilities",
        (34, 33),
        "gfx/interface/abilitylist",
        ABILITY_SLUGS,
        4,
        "Stage 4 HQ commander abilities (34x33)",
    )
    process_single_family(
        "technology",
        (64, 64),
        "gfx/interface/technologies",
        ["cbrn_theater_cbrn_headquarters"],
        4,
        "Stage 4 Theater CBRN Headquarters technology (64x64)",
    )
