from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import shutil

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[4]
ASSET_ROOT = ROOT / "docs/assets/011_secret_alliance"
SOURCE_DIR = ASSET_ROOT / "source_png"
PROCESSED_DIR = ASSET_ROOT / "processed_png"
DDS_DIR = ASSET_ROOT / "dds"
CONTACT_DIR = ASSET_ROOT / "contact_sheets"
ANIM_ROOT = ASSET_ROOT / "animations"

RUNTIME_DECISIONS = ROOT / "gfx/interface/decisions/011_secret_alliance"
RUNTIME_IDEAS = ROOT / "gfx/interface/ideas/011_secret_alliance"
RUNTIME_ACHIEVEMENTS = ROOT / "gfx/achievements"
RUNTIME_ANIMATED = ROOT / "gfx/interface/animated/011_secret_alliance"

GEN_ROOT = Path.home() / ".codex/generated_images"


DECISION_NAMES = [
    "decision_category_secret_alliance_dossier",
    "decision_secret_alliance_courier",
    "decision_secret_alliance_rail_guard",
    "decision_secret_alliance_expose",
    "decision_secret_alliance_backchannel",
    "decision_secret_alliance_border_watch",
    "decision_secret_alliance_factory_shield",
    "decision_secret_alliance_false_leak",
    "decision_secret_alliance_strike_first",
]

IDEA_NAMES = [
    "idea_secret_alliance_dossier_pressure",
    "idea_secret_alliance_counter_network",
    "idea_secret_alliance_protocol_discipline",
    "idea_secret_alliance_patron_liaisons",
    "idea_secret_alliance_exposed_signatory",
    "idea_secret_alliance_war_coordination",
    "idea_secret_alliance_credibility_restored",
]

ACHIEVEMENT_NAMES = [
    "secret_alliance_empty_chair",
    "secret_alliance_all_names",
    "secret_alliance_three_knocks",
    "secret_alliance_lone_target",
    "secret_alliance_counter_protocol",
    "secret_alliance_wrong_room",
    "secret_alliance_no_patrons",
    "secret_alliance_paid_in_promises",
]


@dataclass(frozen=True)
class AnimationSpec:
    slug: str
    source_sheet: str
    size: tuple[int, int]
    frame_count: int = 8
    cols: int = 4
    rows: int = 2
    fps: int = 8
    static_frame: int = 0
    scale: float = 0.92


ANIMATIONS = [
    AnimationSpec("secret_alliance_evidence_pulse", "secret_alliance_evidence_pulse_sheet_source.png", (64, 64)),
    AnimationSpec("secret_alliance_readiness_warning", "secret_alliance_readiness_warning_sheet_source.png", (64, 64)),
    AnimationSpec("secret_alliance_exposed_card_glow", "secret_alliance_exposed_card_glow_sheet_source.png", (96, 64), scale=0.96),
    AnimationSpec("secret_alliance_war_countdown_ticker", "secret_alliance_war_countdown_ticker_sheet_source.png", (128, 32), scale=0.98),
    AnimationSpec("secret_alliance_hidden_protocol_overlay", "secret_alliance_hidden_protocol_overlay_sheet_source.png", (96, 96), scale=0.94),
]


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def repo_rel(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT)).replace("\\", "/")


def save_dds(image: Image.Image, path: Path) -> None:
    ensure_parent(path)
    image.convert("RGBA").save(path)


def remove_green_key(image: Image.Image) -> Image.Image:
    image = ImageOps.exif_transpose(image.convert("RGBA"))
    pixels = image.load()
    for y in range(image.height):
        for x in range(image.width):
            r, g, b, a = pixels[x, y]
            if g > 135 and g > r * 1.25 and g > b * 1.25:
                pixels[x, y] = (r, g, b, 0)
            elif g > 90 and g > r * 1.15 and g > b * 1.15:
                pixels[x, y] = (r, g, b, min(a, 90))
    alpha = image.getchannel("A").filter(ImageFilter.MinFilter(3))
    image.putalpha(alpha)
    return image


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
    canvas.alpha_composite(fitted, ((size[0] - fitted.width) // 2, (size[1] - fitted.height) // 2))
    return canvas


def crop_cover(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    image = ImageOps.exif_transpose(image.convert("RGBA"))
    target_ratio = size[0] / size[1]
    source_ratio = image.width / image.height
    if source_ratio > target_ratio:
        new_w = round(image.height * target_ratio)
        left = (image.width - new_w) // 2
        image = image.crop((left, 0, left + new_w, image.height))
    else:
        new_h = round(image.width / target_ratio)
        top = (image.height - new_h) // 2
        image = image.crop((0, top, image.width, top + new_h))
    return image.resize(size, Image.Resampling.LANCZOS)


def make_checker(size: tuple[int, int], cell: int = 8) -> Image.Image:
    base = Image.new("RGBA", size, (48, 48, 48, 255))
    draw = ImageDraw.Draw(base)
    for y in range(0, size[1], cell):
        for x in range(0, size[0], cell):
            if (x // cell + y // cell) % 2 == 0:
                draw.rectangle((x, y, x + cell - 1, y + cell - 1), fill=(88, 88, 88, 255))
    return base


def create_contact_sheet(paths: list[Path], out: Path, thumb_size: tuple[int, int], columns: int) -> None:
    if not paths:
        return
    font = ImageFont.load_default()
    label_h = 18
    rows = (len(paths) + columns - 1) // columns
    sheet = Image.new("RGBA", (columns * thumb_size[0], rows * (thumb_size[1] + label_h)), (24, 24, 24, 255))
    for idx, path in enumerate(paths):
        image = Image.open(path).convert("RGBA")
        bg = make_checker(image.size, max(4, min(image.size) // 8))
        bg.alpha_composite(image)
        bg.thumbnail(thumb_size, Image.Resampling.LANCZOS)
        x = (idx % columns) * thumb_size[0]
        y = (idx // columns) * (thumb_size[1] + label_h)
        sheet.alpha_composite(bg, (x + (thumb_size[0] - bg.width) // 2, y + (thumb_size[1] - bg.height) // 2))
        ImageDraw.Draw(sheet).text((x + 2, y + thumb_size[1]), path.stem[:28], fill=(230, 230, 230, 255), font=font)
    ensure_parent(out)
    sheet.save(out)


def create_generated_source_review(limit: int = 30) -> Path:
    files = sorted(GEN_ROOT.rglob("*.png"), key=lambda p: p.stat().st_mtime, reverse=True)[:limit]
    thumb = (180, 180)
    label_h = 38
    cols = 5
    rows = (len(files) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * thumb[0], rows * (thumb[1] + label_h)), (30, 30, 30))
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()
    for idx, path in enumerate(files):
        image = Image.open(path).convert("RGB")
        image.thumbnail(thumb, Image.Resampling.LANCZOS)
        x = (idx % cols) * thumb[0]
        y = (idx // cols) * (thumb[1] + label_h)
        sheet.paste(image, (x + (thumb[0] - image.width) // 2, y + (thumb[1] - image.height) // 2))
        draw.text((x + 2, y + thumb[1]), f"{idx}: {path.name[:18]}", fill=(230, 230, 230), font=font)
        draw.text((x + 2, y + thumb[1] + 12), path.parent.name[-18:], fill=(185, 185, 185), font=font)
    out = ASSET_ROOT / "generated_source_review.png"
    ensure_parent(out)
    sheet.save(out)
    return out


def copy_selected_sources(selection: dict[str, str]) -> None:
    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    for dest_name, source_path in selection.items():
        dest = SOURCE_DIR / dest_name
        ensure_parent(dest)
        shutil.copy2(source_path, dest)


def slice_grid(source_path: Path, cols: int, rows: int, names: list[str], out_dir: Path, trim_ratio: float = 0.02) -> list[Path]:
    source = Image.open(source_path).convert("RGBA")
    cell_w = source.width // cols
    cell_h = source.height // rows
    trim_x = round(cell_w * trim_ratio)
    trim_y = round(cell_h * trim_ratio)
    out_paths: list[Path] = []
    for idx, name in enumerate(names):
        col = idx % cols
        row = idx // cols
        cell = source.crop((
            col * cell_w + trim_x,
            row * cell_h + trim_y,
            (col + 1) * cell_w - trim_x,
            (row + 1) * cell_h - trim_y,
        ))
        out = out_dir / f"{name}_source.png"
        ensure_parent(out)
        cell.save(out)
        out_paths.append(out)
    return out_paths


def process_transparent_icons(paths: list[Path], size: tuple[int, int], processed_dir: Path, runtime_dir: Path, scale: float) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    for path in paths:
        stem = path.name.replace("_source.png", "")
        keyed = remove_green_key(Image.open(path).convert("RGBA"))
        processed = fit_transparent(keyed, size, scale)
        processed_path = processed_dir / f"{stem}.png"
        dds_path = DDS_DIR / f"{stem}.dds"
        runtime_path = runtime_dir / f"{stem}.dds"
        ensure_parent(processed_path)
        processed.save(processed_path)
        save_dds(processed, dds_path)
        save_dds(processed, runtime_path)
        records.append({
            "asset": stem,
            "source": repo_rel(path),
            "processed": repo_rel(processed_path),
            "dds": repo_rel(runtime_path),
            "size": f"{size[0]}x{size[1]}",
        })
    return records


def process_achievements(paths: list[Path]) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    for path in paths:
        stem = path.name.replace("_source.png", "")
        base = crop_cover(Image.open(path).convert("RGBA"), (64, 64)).convert("RGBA")
        if base.getchannel("A").getextrema()[0] < 255:
            bg = Image.new("RGBA", (64, 64), (25, 22, 20, 255))
            bg.alpha_composite(base)
            base = bg
        grey = ImageOps.grayscale(base).convert("RGBA")
        not_eligible = grey.copy()
        draw = ImageDraw.Draw(not_eligible)
        draw.line((10, 10, 54, 54), fill=(190, 26, 24, 255), width=7)
        draw.line((54, 10, 10, 54), fill=(190, 26, 24, 255), width=7)
        for variant_stem, image in [
            (stem, base),
            (f"{stem}_grey", grey),
            (f"{stem}_not_eligible", not_eligible),
        ]:
            processed_path = PROCESSED_DIR / f"{variant_stem}.png"
            dds_path = DDS_DIR / f"{variant_stem}.dds"
            runtime_path = RUNTIME_ACHIEVEMENTS / f"{variant_stem}.dds"
            ensure_parent(processed_path)
            image.save(processed_path)
            save_dds(image, dds_path)
            save_dds(image, runtime_path)
            records.append({
                "asset": variant_stem,
                "source": repo_rel(path),
                "processed": repo_rel(processed_path),
                "dds": repo_rel(runtime_path),
                "size": "64x64",
            })
    return records


def process_animation(spec: AnimationSpec) -> dict[str, object]:
    package = ANIM_ROOT / spec.slug
    source_dir = package / "source_frames"
    processed_dir = package / "processed_frames"
    sheets_dir = package / "sheets"
    previews_dir = package / "previews"
    for directory in (source_dir, processed_dir, sheets_dir, previews_dir):
        directory.mkdir(parents=True, exist_ok=True)

    source_sheet = Image.open(SOURCE_DIR / spec.source_sheet).convert("RGBA")
    cell_w = source_sheet.width // spec.cols
    cell_h = source_sheet.height // spec.rows
    source_paths: list[Path] = []
    processed_paths: list[Path] = []
    frames: list[Image.Image] = []
    for idx in range(spec.frame_count):
        col = idx % spec.cols
        row = idx // spec.cols
        cell = source_sheet.crop((col * cell_w, row * cell_h, (col + 1) * cell_w, (row + 1) * cell_h))
        transparent = remove_green_key(cell)
        source_path = source_dir / f"{spec.slug}_{idx:03d}_source.png"
        transparent.save(source_path)
        frame = fit_transparent(transparent, spec.size, spec.scale)
        processed_path = processed_dir / f"{spec.slug}_{idx:03d}.png"
        frame.save(processed_path)
        source_paths.append(source_path)
        processed_paths.append(processed_path)
        frames.append(frame)

    sheet = Image.new("RGBA", (spec.size[0] * len(frames), spec.size[1]), (0, 0, 0, 0))
    for idx, frame in enumerate(frames):
        sheet.alpha_composite(frame, (idx * spec.size[0], 0))

    sheet_png = sheets_dir / f"{spec.slug}_sheet.png"
    static_png = PROCESSED_DIR / f"{spec.slug}_static.png"
    preview_gif = previews_dir / f"{spec.slug}_preview.gif"
    contact_png = previews_dir / f"{spec.slug}_contact.png"
    sheet.save(sheet_png)
    frames[spec.static_frame].save(static_png)
    frames[0].save(
        preview_gif,
        save_all=True,
        append_images=frames[1:],
        duration=round(1000 / spec.fps),
        loop=0,
        disposal=2,
    )
    create_contact_sheet(processed_paths, contact_png, spec.size, min(4, len(processed_paths)))

    sheet_dds = DDS_DIR / f"{spec.slug}_sheet.dds"
    static_dds = DDS_DIR / f"{spec.slug}_static.dds"
    runtime_sheet = RUNTIME_ANIMATED / f"{spec.slug}_sheet.dds"
    runtime_static = RUNTIME_ANIMATED / f"{spec.slug}_static.dds"
    save_dds(sheet, sheet_dds)
    save_dds(frames[spec.static_frame], static_dds)
    save_dds(sheet, runtime_sheet)
    save_dds(frames[spec.static_frame], runtime_static)

    brief = package / "brief.md"
    frame_plan = package / "frame_plan.md"
    brief.write_text(
        f"# {spec.slug}\n\n"
        f"- In-game use: Event 011 Secret Alliance scripted GUI sidecar animation.\n"
        f"- Target frame size: `{spec.size[0]}x{spec.size[1]}`\n"
        f"- Frame count: `{len(frames)}`\n"
        f"- Sheet size: `{sheet.width}x{sheet.height}`\n"
        f"- FPS: `{spec.fps}`\n"
        f"- Looping: `yes`\n"
        f"- Play on show expectation: `yes`\n"
        f"- Anchor: center\n"
        f"- Source mode: `$imagegen` generated source sheet, cropped into per-frame source PNGs.\n"
        f"- Static sprite: `GFX_{spec.slug}_static`\n"
        f"- Animated sprite: `GFX_{spec.slug}_animated`\n"
        f"- Final static DDS: `{repo_rel(runtime_static)}`\n"
        f"- Final sheet DDS: `{repo_rel(runtime_sheet)}`\n",
        encoding="utf-8",
    )
    frame_plan.write_text(
        "| Frame | Visual state | Loop note |\n"
        "| --- | --- | --- |\n"
        + "\n".join(
            f"| `{idx:03d}` | Separately generated source-frame state from `{spec.source_sheet}` | "
            f"{'dormant start' if idx == 0 else 'peak/mid loop state' if idx in (3, 4) else 'return state'} |"
            for idx in range(len(frames))
        )
        + "\n",
        encoding="utf-8",
    )

    return {
        "asset": spec.slug,
        "source_sheet": repo_rel(SOURCE_DIR / spec.source_sheet),
        "source_frames": [repo_rel(p) for p in source_paths],
        "processed_frames": [repo_rel(p) for p in processed_paths],
        "static_png": repo_rel(static_png),
        "sheet_png": repo_rel(sheet_png),
        "preview_gif": repo_rel(preview_gif),
        "contact_png": repo_rel(contact_png),
        "static_dds": repo_rel(runtime_static),
        "sheet_dds": repo_rel(runtime_sheet),
        "frame_count": len(frames),
        "frame_size": f"{spec.size[0]}x{spec.size[1]}",
        "sheet_size": f"{sheet.width}x{sheet.height}",
        "fps": spec.fps,
    }


def process_all() -> dict[str, object]:
    decisions = slice_grid(SOURCE_DIR / "secret_alliance_decision_atlas_source.png", 5, 2, DECISION_NAMES, SOURCE_DIR)
    ideas = slice_grid(SOURCE_DIR / "secret_alliance_idea_atlas_source.png", 4, 2, IDEA_NAMES, SOURCE_DIR)
    achievements = slice_grid(SOURCE_DIR / "secret_alliance_achievement_atlas_source.png", 4, 2, ACHIEVEMENT_NAMES, SOURCE_DIR, trim_ratio=0.0)

    decision_records = process_transparent_icons(decisions, (32, 32), PROCESSED_DIR, RUNTIME_DECISIONS, 0.94)
    idea_records = process_transparent_icons(ideas, (64, 64), PROCESSED_DIR, RUNTIME_IDEAS, 0.92)
    achievement_records = process_achievements(achievements)
    animation_records = [process_animation(spec) for spec in ANIMATIONS]

    create_contact_sheet([PROCESSED_DIR / f"{name}.png" for name in DECISION_NAMES], CONTACT_DIR / "secret_alliance_decision_icons_contact.png", (64, 64), 5)
    create_contact_sheet([PROCESSED_DIR / f"{name}.png" for name in IDEA_NAMES], CONTACT_DIR / "secret_alliance_idea_icons_contact.png", (96, 96), 4)
    create_contact_sheet([PROCESSED_DIR / f"{name}.png" for name in ACHIEVEMENT_NAMES], CONTACT_DIR / "secret_alliance_achievement_icons_contact.png", (96, 96), 4)
    achievement_variants = []
    for name in ACHIEVEMENT_NAMES:
        achievement_variants.extend([
            PROCESSED_DIR / f"{name}.png",
            PROCESSED_DIR / f"{name}_grey.png",
            PROCESSED_DIR / f"{name}_not_eligible.png",
        ])
    create_contact_sheet(achievement_variants, CONTACT_DIR / "secret_alliance_achievement_variants_contact.png", (80, 80), 6)

    return {
        "decisions": decision_records,
        "ideas": idea_records,
        "achievements": achievement_records,
        "animations": animation_records,
    }


if __name__ == "__main__":
    print(create_generated_source_review())
