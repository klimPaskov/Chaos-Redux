from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[4]
ASSET_ROOT = ROOT / "docs/assets/015_utopia_manifesto"
SOURCE_DIR = ASSET_ROOT / "source_png"
PROCESSED_DIR = ASSET_ROOT / "processed_png"
DDS_DIR = ASSET_ROOT / "dds"
ANIM_DIR = ASSET_ROOT / "animations"
RUNTIME_DIR = ROOT / "gfx/interface/utopia_manifesto"


ANIMATIONS = {
    "utopia_ledger_seal": {
        "source": SOURCE_DIR / "utopia_ledger_seal_sheet_source.png",
        "cols": 4,
        "rows": 2,
        "frames": 8,
        "size": (64, 64),
        "fps": 8,
        "scale": 0.92,
        "static_frame": 0,
    },
    "utopia_overreach_warning": {
        "source": SOURCE_DIR / "utopia_overreach_warning_sheet_source.png",
        "cols": 4,
        "rows": 2,
        "frames": 8,
        "size": (64, 64),
        "fps": 8,
        "scale": 0.92,
        "static_frame": 0,
    },
    "utopia_storehouse_fill": {
        "source": SOURCE_DIR / "utopia_storehouse_fill_sheet_source.png",
        "cols": 4,
        "rows": 2,
        "frames": 8,
        "size": (64, 16),
        "fps": 8,
        "scale": 0.98,
        "static_frame": 6,
    },
    "utopia_new_utopia_seal": {
        "source": SOURCE_DIR / "utopia_new_utopia_seal_sheet_source.png",
        "cols": 5,
        "rows": 2,
        "frames": 10,
        "size": (96, 96),
        "fps": 8,
        "scale": 0.92,
        "static_frame": 0,
    },
    "utopia_marked_bounds_seal": {
        "source": SOURCE_DIR / "utopia_marked_bounds_seal_sheet_source.png",
        "cols": 5,
        "rows": 2,
        "frames": 10,
        "size": (96, 96),
        "fps": 8,
        "scale": 0.92,
        "static_frame": 0,
    },
}


PANELS = {
    "utopia_ledger_background_panel": {
        "source": SOURCE_DIR / "utopia_ledger_background_panel_source.png",
        "size": (700, 500),
        "mode": "cover",
    },
    "utopia_ledger_header_plate": {
        "source": SOURCE_DIR / "utopia_ledger_header_plate_source.png",
        "size": (700, 96),
        "mode": "trim_dark",
    },
    "utopia_ledger_warning_panel": {
        "source": SOURCE_DIR / "utopia_ledger_warning_panel_source.png",
        "size": (320, 128),
        "mode": "cover",
    },
}


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def repo_rel(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT)).replace("\\", "/")


def crop_cover(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    image = ImageOps.exif_transpose(image.convert("RGBA"))
    target_ratio = size[0] / size[1]
    source_ratio = image.width / image.height
    if source_ratio > target_ratio:
        new_w = int(image.height * target_ratio)
        left = (image.width - new_w) // 2
        image = image.crop((left, 0, left + new_w, image.height))
    else:
        new_h = int(image.width / target_ratio)
        top = (image.height - new_h) // 2
        image = image.crop((0, top, image.width, top + new_h))
    return image.resize(size, Image.Resampling.LANCZOS)


def crop_non_dark(image: Image.Image, threshold: int = 16) -> Image.Image:
    image = ImageOps.exif_transpose(image.convert("RGBA"))
    grey = ImageOps.grayscale(image)
    mask = grey.point(lambda p: 255 if p > threshold else 0)
    bbox = mask.getbbox()
    if not bbox:
        return image
    left, top, right, bottom = bbox
    pad_x = max(0, int((right - left) * 0.01))
    pad_y = max(0, int((bottom - top) * 0.03))
    left = max(0, left - pad_x)
    top = max(0, top - pad_y)
    right = min(image.width, right + pad_x)
    bottom = min(image.height, bottom + pad_y)
    return image.crop((left, top, right, bottom))


def remove_green_key(image: Image.Image) -> Image.Image:
    image = ImageOps.exif_transpose(image.convert("RGBA"))
    pixels = image.load()
    for y in range(image.height):
        for x in range(image.width):
            r, g, b, a = pixels[x, y]
            if g > 95 and g > r * 1.18 and g > b * 1.18:
                alpha = 0
                if g < 165 or abs(r - b) > 70:
                    alpha = 80
                pixels[x, y] = (r, g, b, alpha)
            elif g > 75 and g > r * 1.08 and g > b * 1.08:
                pixels[x, y] = (r, g, b, min(a, 120))
    alpha = image.getchannel("A")
    alpha = alpha.filter(ImageFilterMin())
    image.putalpha(alpha)
    return image


def ImageFilterMin() -> ImageFilter.Filter:
    from PIL import ImageFilter

    return ImageFilter.MinFilter(3)


def fit_transparent(image: Image.Image, size: tuple[int, int], scale: float) -> Image.Image:
    image = image.convert("RGBA")
    bbox = image.getchannel("A").getbbox()
    if bbox:
        image = image.crop(bbox)
    canvas = Image.new("RGBA", size, (0, 0, 0, 0))
    if not image.getbbox():
        return canvas
    max_w = max(1, int(size[0] * scale))
    max_h = max(1, int(size[1] * scale))
    ratio = min(max_w / image.width, max_h / image.height)
    new_size = (max(1, round(image.width * ratio)), max(1, round(image.height * ratio)))
    fitted = image.resize(new_size, Image.Resampling.LANCZOS)
    x = (size[0] - fitted.width) // 2
    y = (size[1] - fitted.height) // 2
    canvas.alpha_composite(fitted, (x, y))
    return canvas


def save_dds(image: Image.Image, path: Path) -> None:
    ensure_parent(path)
    image.convert("RGBA").save(path)


def make_checker(size: tuple[int, int], cell: int = 8) -> Image.Image:
    base = Image.new("RGBA", size, (48, 48, 48, 255))
    draw = ImageDraw.Draw(base)
    for y in range(0, size[1], cell):
        for x in range(0, size[0], cell):
            if (x // cell + y // cell) % 2 == 0:
                draw.rectangle((x, y, x + cell - 1, y + cell - 1), fill=(88, 88, 88, 255))
    return base


def create_contact_sheet(paths: list[Path], out: Path, thumb_size: tuple[int, int], columns: int) -> None:
    font = ImageFont.load_default()
    label_h = 14
    rows = (len(paths) + columns - 1) // columns
    sheet = Image.new("RGBA", (columns * thumb_size[0], rows * (thumb_size[1] + label_h)), (24, 24, 24, 255))
    for idx, path in enumerate(paths):
        frame = Image.open(path).convert("RGBA")
        bg = make_checker(frame.size, max(4, min(frame.size) // 8))
        bg.alpha_composite(frame)
        bg.thumbnail(thumb_size, Image.Resampling.LANCZOS)
        x = (idx % columns) * thumb_size[0]
        y = (idx // columns) * (thumb_size[1] + label_h)
        sheet.alpha_composite(bg, (x + (thumb_size[0] - bg.width) // 2, y + (thumb_size[1] - bg.height) // 2))
        ImageDraw.Draw(sheet).text((x + 2, y + thumb_size[1]), path.stem[-24:], fill=(230, 230, 230, 255), font=font)
    ensure_parent(out)
    sheet.save(out)


def process_panels() -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    panel_contact_images = []
    for slug, cfg in PANELS.items():
        source = Image.open(cfg["source"]).convert("RGBA")
        if cfg["mode"] == "trim_dark":
            source = crop_non_dark(source)
        processed = crop_cover(source, cfg["size"])
        processed_path = PROCESSED_DIR / f"{slug}.png"
        dds_path = DDS_DIR / f"{slug}.dds"
        runtime_path = RUNTIME_DIR / f"{slug}.dds"
        ensure_parent(processed_path)
        processed.save(processed_path)
        save_dds(processed, dds_path)
        save_dds(processed, runtime_path)
        panel_contact_images.append(processed_path)
        records.append(
            {
                "asset": slug,
                "source": repo_rel(cfg["source"]),
                "processed": repo_rel(processed_path),
                "dds": repo_rel(runtime_path),
                "size": f"{cfg['size'][0]}x{cfg['size'][1]}",
            }
        )
    create_contact_sheet(panel_contact_images, ASSET_ROOT / "contact_sheets/utopia_runtime_panels_regenerated_contact.png", (350, 250), 1)
    return records


def process_animation(slug: str, cfg: dict) -> dict[str, object]:
    package = ANIM_DIR / slug
    source_dir = package / "source_frames"
    processed_dir = package / "processed_frames"
    sheets_dir = package / "sheets"
    previews_dir = package / "previews"
    for directory in (source_dir, processed_dir, sheets_dir, previews_dir):
        directory.mkdir(parents=True, exist_ok=True)

    source_sheet = Image.open(cfg["source"]).convert("RGBA")
    cell_w = source_sheet.width // cfg["cols"]
    cell_h = source_sheet.height // cfg["rows"]
    source_paths: list[Path] = []
    processed_paths: list[Path] = []
    frames: list[Image.Image] = []
    for idx in range(cfg["frames"]):
        col = idx % cfg["cols"]
        row = idx // cfg["cols"]
        cell = source_sheet.crop((col * cell_w, row * cell_h, (col + 1) * cell_w, (row + 1) * cell_h))
        transparent = remove_green_key(cell)
        source_path = source_dir / f"{slug}_{idx:03d}_source.png"
        transparent.save(source_path)
        frame = fit_transparent(transparent, cfg["size"], cfg["scale"])
        processed_path = processed_dir / f"{slug}_{idx:03d}.png"
        frame.save(processed_path)
        source_paths.append(source_path)
        processed_paths.append(processed_path)
        frames.append(frame)

    frame_w, frame_h = cfg["size"]
    sheet = Image.new("RGBA", (frame_w * len(frames), frame_h), (0, 0, 0, 0))
    for idx, frame in enumerate(frames):
        sheet.alpha_composite(frame, (idx * frame_w, 0))
    sheet_png = sheets_dir / f"{slug}_sheet.png"
    sheet.save(sheet_png)

    static_png = PROCESSED_DIR / f"{slug}_static.png"
    frames[cfg["static_frame"]].save(static_png)
    gif_path = previews_dir / f"{slug}_preview.gif"
    frames[0].save(
        gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=int(1000 / cfg["fps"]),
        loop=0,
        disposal=2,
    )
    contact_path = previews_dir / f"{slug}_contact.png"
    create_contact_sheet(processed_paths, contact_path, cfg["size"], min(5, len(processed_paths)))

    dds_sheet = DDS_DIR / f"{slug}_sheet.dds"
    dds_static = DDS_DIR / f"{slug}_static.dds"
    runtime_sheet = RUNTIME_DIR / f"{slug}_sheet.dds"
    runtime_static = RUNTIME_DIR / f"{slug}_static.dds"
    save_dds(sheet, dds_sheet)
    save_dds(frames[cfg["static_frame"]], dds_static)
    save_dds(sheet, runtime_sheet)
    save_dds(frames[cfg["static_frame"]], runtime_static)

    return {
        "asset": slug,
        "sheet_source": repo_rel(cfg["source"]),
        "source_frames": [repo_rel(p) for p in source_paths],
        "processed_frames": [repo_rel(p) for p in processed_paths],
        "static_png": repo_rel(static_png),
        "sheet_png": repo_rel(sheet_png),
        "preview_gif": repo_rel(gif_path),
        "contact_png": repo_rel(contact_path),
        "sheet_dds": repo_rel(runtime_sheet),
        "static_dds": repo_rel(runtime_static),
        "frame_count": len(frames),
        "frame_size": f"{frame_w}x{frame_h}",
        "sheet_size": f"{sheet.width}x{sheet.height}",
        "fps": cfg["fps"],
    }


def process_animations() -> list[dict[str, object]]:
    return [process_animation(slug, cfg) for slug, cfg in ANIMATIONS.items()]


def main() -> None:
    panel_records = process_panels()
    animation_records = process_animations()
    print("PANELS")
    for record in panel_records:
        print(record)
    print("ANIMATIONS")
    for record in animation_records:
        print(record["asset"], record["frame_count"], record["frame_size"], record["sheet_size"])


if __name__ == "__main__":
    main()
