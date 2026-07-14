from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[4]


def repo_rel(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT)).replace("\\", "/")


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def save_dds(image: Image.Image, path: Path) -> None:
    ensure_parent(path)
    image.save(path)


def fit_icon(image: Image.Image, size: tuple[int, int], scale: float = 0.9) -> Image.Image:
    image = image.convert("RGBA")
    bbox = image.getbbox()
    if bbox:
        image = image.crop(bbox)
    canvas = Image.new("RGBA", size, (0, 0, 0, 0))
    max_w = max(1, int(size[0] * scale))
    max_h = max(1, int(size[1] * scale))
    ratio = min(max_w / image.width, max_h / image.height)
    new_size = (max(1, int(image.width * ratio)), max(1, int(image.height * ratio)))
    fitted = image.resize(new_size, Image.Resampling.LANCZOS)
    x = (size[0] - fitted.width) // 2
    y = (size[1] - fitted.height) // 2
    canvas.alpha_composite(fitted, (x, y))
    return canvas


def slice_grid(
    source_path: Path,
    cols: int,
    rows: int,
    names: Iterable[str],
    out_dir: Path,
    trim: int = 0,
) -> list[Path]:
    source = Image.open(source_path).convert("RGBA")
    cell_w = source.width // cols
    cell_h = source.height // rows
    out_paths: list[Path] = []
    for idx, name in enumerate(names):
        col = idx % cols
        row = idx // cols
        left = col * cell_w + trim
        upper = row * cell_h + trim
        right = (col + 1) * cell_w - trim
        lower = (row + 1) * cell_h - trim
        tile = source.crop((left, upper, right, lower))
        out_path = out_dir / f"{name}_source.png"
        ensure_parent(out_path)
        tile.save(out_path)
        out_paths.append(out_path)
    return out_paths


def process_icon_batch(
    source_paths: Iterable[Path],
    processed_dir: Path,
    dds_dir: Path,
    final_dir: Path,
    size: tuple[int, int],
    scale: float = 0.9,
) -> list[dict]:
    records = []
    for source_path in source_paths:
        base_name = source_path.name.replace("_source.png", "")
        image = Image.open(source_path).convert("RGBA")
        processed = fit_icon(image, size, scale=scale)
        processed_path = processed_dir / f"{base_name}.png"
        dds_path = dds_dir / f"{base_name}.dds"
        final_dds_path = final_dir / f"{base_name}.dds"
        ensure_parent(processed_path)
        processed.save(processed_path)
        save_dds(processed, dds_path)
        save_dds(processed, final_dds_path)
        records.append(
            {
                "name": base_name,
                "source": repo_rel(source_path),
                "processed": repo_rel(processed_path),
                "dds": repo_rel(final_dds_path),
                "size": f"{size[0]}x{size[1]}",
            }
        )
    return records


def make_achievement_variants(
    source_path: Path,
    processed_dir: Path,
    dds_dir: Path,
    final_dir: Path,
) -> list[dict]:
    base_name = source_path.name.replace("_source.png", "")
    base = fit_icon(Image.open(source_path).convert("RGBA"), (64, 64), scale=1.0)
    grey = ImageOps.grayscale(base).convert("RGBA")
    not_eligible = grey.copy()
    draw = ImageDraw.Draw(not_eligible)
    draw.line((10, 10, 54, 54), fill=(200, 32, 32, 255), width=7)
    draw.line((54, 10, 10, 54), fill=(200, 32, 32, 255), width=7)
    variants = [
        (base_name, base),
        (f"{base_name}_grey", grey),
        (f"{base_name}_not_eligible", not_eligible),
    ]
    records = []
    for variant_name, image in variants:
        processed_path = processed_dir / f"{variant_name}.png"
        dds_path = dds_dir / f"{variant_name}.dds"
        final_dds_path = final_dir / f"{variant_name}.dds"
        image.save(processed_path)
        save_dds(image, dds_path)
        save_dds(image, final_dds_path)
        records.append(
            {
                "name": variant_name,
                "source": repo_rel(source_path),
                "processed": repo_rel(processed_path),
                "dds": repo_rel(final_dds_path),
                "size": "64x64",
            }
        )
    return records


def create_contact_sheet(image_paths: Iterable[Path], output_path: Path, thumb_size: tuple[int, int], columns: int = 4) -> None:
    image_paths = list(image_paths)
    if not image_paths:
        return
    font = ImageFont.load_default()
    labels = [path.stem for path in image_paths]
    label_h = 14
    rows = (len(image_paths) + columns - 1) // columns
    sheet = Image.new("RGBA", (columns * thumb_size[0], rows * (thumb_size[1] + label_h)), (24, 24, 24, 255))
    for idx, path in enumerate(image_paths):
        image = Image.open(path).convert("RGBA")
        image.thumbnail(thumb_size, Image.Resampling.LANCZOS)
        x = (idx % columns) * thumb_size[0]
        y = (idx // columns) * (thumb_size[1] + label_h)
        paste_x = x + (thumb_size[0] - image.width) // 2
        paste_y = y + (thumb_size[1] - image.height) // 2
        sheet.alpha_composite(image, (paste_x, paste_y))
        ImageDraw.Draw(sheet).text((x + 2, y + thumb_size[1]), labels[idx][:28], fill=(220, 220, 220, 255), font=font)
    ensure_parent(output_path)
    sheet.save(output_path)


def split_animation_sheet(
    source_path: Path,
    cols: int,
    rows: int,
    asset_slug: str,
    frame_count: int,
    source_dir: Path,
) -> list[Path]:
    names = [f"{asset_slug}_{idx:03d}" for idx in range(frame_count)]
    return slice_grid(source_path, cols, rows, names, source_dir, trim=0)


def build_animation_package(
    asset_slug: str,
    source_frame_paths: Iterable[Path],
    processed_dir: Path,
    sheets_dir: Path,
    previews_dir: Path,
    dds_dir: Path,
    final_dir: Path,
    frame_size: tuple[int, int],
    fps: int,
    static_frame_index: int = 0,
    scale: float = 0.95,
) -> dict:
    source_frame_paths = list(source_frame_paths)
    processed_paths: list[Path] = []
    processed_images: list[Image.Image] = []
    for path in source_frame_paths:
        frame = fit_icon(Image.open(path).convert("RGBA"), frame_size, scale=scale)
        processed_path = processed_dir / f"{path.stem.replace('_source', '')}.png"
        frame.save(processed_path)
        processed_paths.append(processed_path)
        processed_images.append(frame)

    sheet = Image.new("RGBA", (frame_size[0] * len(processed_images), frame_size[1]), (0, 0, 0, 0))
    for idx, frame in enumerate(processed_images):
        sheet.alpha_composite(frame, (idx * frame_size[0], 0))

    sheet_png = sheets_dir / f"{asset_slug}_sheet.png"
    static_png = ROOT / "docs/assets/015_utopia_manifesto/processed_png" / f"{asset_slug}_static.png"
    preview_gif = previews_dir / f"{asset_slug}_preview.gif"
    contact_png = previews_dir / f"{asset_slug}_contact.png"
    sheet.save(sheet_png)
    processed_images[static_frame_index].save(static_png)
    processed_images[0].save(
        preview_gif,
        save_all=True,
        append_images=processed_images[1:],
        duration=int(1000 / fps),
        loop=0,
        disposal=2,
        transparency=0,
    )
    create_contact_sheet(processed_paths, contact_png, frame_size, columns=min(5, len(processed_paths)))

    sheet_dds = dds_dir / f"{asset_slug}_sheet.dds"
    static_dds = dds_dir / f"{asset_slug}_static.dds"
    final_sheet_dds = final_dir / f"{asset_slug}_sheet.dds"
    final_static_dds = final_dir / f"{asset_slug}_static.dds"
    save_dds(sheet, sheet_dds)
    save_dds(processed_images[static_frame_index], static_dds)
    save_dds(sheet, final_sheet_dds)
    save_dds(processed_images[static_frame_index], final_static_dds)

    return {
        "asset_slug": asset_slug,
        "source_frames": [repo_rel(path) for path in source_frame_paths],
        "processed_frames": [repo_rel(path) for path in processed_paths],
        "sheet_png": repo_rel(sheet_png),
        "preview_gif": repo_rel(preview_gif),
        "contact_png": repo_rel(contact_png),
        "sheet_dds": repo_rel(final_sheet_dds),
        "static_dds": repo_rel(final_static_dds),
        "frame_count": len(source_frame_paths),
        "frame_size": f"{frame_size[0]}x{frame_size[1]}",
        "sheet_size": f"{sheet.width}x{sheet.height}",
        "fps": fps,
    }


if __name__ == "__main__":
    raise SystemExit("Use this module from task-specific python commands.")
