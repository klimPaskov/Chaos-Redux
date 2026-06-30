from __future__ import annotations

import math
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageChops, ImageOps, ImageDraw


ROOT = Path(__file__).resolve().parents[3]
DOCS = ROOT / "docs" / "assets" / "011_secret_alliance"
SOURCE = DOCS / "source_png"
PROCESSED = DOCS / "processed_png"
CONTACTS = DOCS / "contact_sheets"
ANIM = DOCS / "animations"
TEXCONV = Path(r"C:\Program Files\XnConvert\plugins\texconv.exe")
REMOVE_KEY = Path.home() / ".codex" / "skills" / ".system" / "imagegen" / "scripts" / "remove_chroma_key.py"


@dataclass
class TransparentAsset:
    source: str
    processed: str
    final_dds: str
    size: tuple[int, int]
    margin: int


@dataclass
class AchievementAsset:
    source: str
    base_name: str


@dataclass
class AnimationAsset:
    slug: str
    grid_source: str
    final_static_dds: str
    final_sheet_dds: str
    margin: int
    frame_size: tuple[int, int] = (36, 36)


TRANSPARENT_ASSETS = [
    TransparentAsset("decision_category_secret_alliance_source.png", "decision_category_secret_alliance.png", "gfx/interface/decisions/011_secret_alliance/decision_category_secret_alliance.dds", (32, 32), 2),
    TransparentAsset("decision_secret_alliance_investigate_source.png", "decision_secret_alliance_investigate.png", "gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_investigate.dds", (32, 32), 2),
    TransparentAsset("decision_secret_alliance_security_source.png", "decision_secret_alliance_security.png", "gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_security.dds", (32, 32), 2),
    TransparentAsset("decision_secret_alliance_split_source.png", "decision_secret_alliance_split.png", "gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_split.dds", (32, 32), 2),
    TransparentAsset("decision_secret_alliance_border_watch_source.png", "decision_secret_alliance_border_watch.png", "gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_border_watch.dds", (32, 32), 2),
    TransparentAsset("decision_secret_alliance_confront_source.png", "decision_secret_alliance_confront.png", "gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_confront.dds", (32, 32), 2),
    TransparentAsset("idea_secret_alliance_friction_source.png", "idea_secret_alliance_friction.png", "gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_friction.dds", (64, 64), 4),
    TransparentAsset("idea_secret_alliance_bureau_source.png", "idea_secret_alliance_bureau.png", "gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_bureau.dds", (64, 64), 4),
    TransparentAsset("idea_secret_alliance_prepared_network_source.png", "idea_secret_alliance_prepared_network.png", "gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_prepared_network.dds", (64, 64), 4),
    TransparentAsset("idea_secret_alliance_exposed_member_source.png", "idea_secret_alliance_exposed_member.png", "gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_exposed_member.dds", (64, 64), 4),
    TransparentAsset("idea_secret_alliance_patron_shield_source.png", "idea_secret_alliance_patron_shield.png", "gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_patron_shield.dds", (64, 64), 4),
]

ACHIEVEMENTS = [
    AchievementAsset("achievement_sa_every_thread_named_source.png", "sa_every_thread_named"),
    AchievementAsset("achievement_sa_paper_collapse_source.png", "sa_paper_collapse"),
    AchievementAsset("achievement_sa_turn_the_knife_source.png", "sa_turn_the_knife"),
    AchievementAsset("achievement_sa_prepared_for_every_border_source.png", "sa_prepared_for_every_border"),
    AchievementAsset("achievement_sa_small_country_large_shadow_source.png", "sa_small_country_large_shadow"),
    AchievementAsset("achievement_sa_ten_signatures_source.png", "sa_ten_signatures"),
    AchievementAsset("achievement_sa_bad_evidence_backfire_source.png", "sa_bad_evidence_backfire"),
    AchievementAsset("achievement_sa_no_factory_lost_source.png", "sa_no_factory_lost"),
]

ANIMATIONS = [
    AnimationAsset("secret_alliance_hidden_seal", "secret_alliance_hidden_seal_grid_source.png", "gfx/interface/animated/011_secret_alliance/secret_alliance_hidden_seal.dds", "gfx/interface/animated/011_secret_alliance/secret_alliance_hidden_seal_animated.dds", 3),
    AnimationAsset("secret_alliance_evidence_meter_highlight", "secret_alliance_evidence_meter_highlight_grid_source.png", "gfx/interface/animated/011_secret_alliance/secret_alliance_evidence_meter_highlight.dds", "gfx/interface/animated/011_secret_alliance/secret_alliance_evidence_meter_highlight_animated.dds", 2),
    AnimationAsset("secret_alliance_crisis_frame", "secret_alliance_crisis_frame_grid_source.png", "gfx/interface/animated/011_secret_alliance/secret_alliance_crisis_frame.dds", "gfx/interface/animated/011_secret_alliance/secret_alliance_crisis_frame_animated.dds", 1),
]


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True, cwd=ROOT)


def remove_chroma(src: Path, dst: Path) -> None:
    ensure_parent(dst)
    run(
        [
            "py",
            "-3",
            str(REMOVE_KEY),
            "--input",
            str(src),
            "--out",
            str(dst),
            "--force",
            "--auto-key",
            "border",
            "--soft-matte",
            "--transparent-threshold",
            "12",
            "--opaque-threshold",
            "220",
            "--despill",
            "--edge-contract",
            "1",
        ]
    )


def crop_alpha(img: Image.Image) -> Image.Image:
    if img.mode != "RGBA":
        img = img.convert("RGBA")
    alpha = img.getchannel("A")
    bbox = alpha.getbbox()
    return img.crop(bbox) if bbox else img


def fit_to_canvas(img: Image.Image, size: tuple[int, int], margin: int, fill=(0, 0, 0, 0)) -> Image.Image:
    img = crop_alpha(img)
    max_w = max(1, size[0] - margin * 2)
    max_h = max(1, size[1] - margin * 2)
    scale = min(max_w / img.width, max_h / img.height)
    new_size = (max(1, round(img.width * scale)), max(1, round(img.height * scale)))
    resample = Image.Resampling.LANCZOS
    resized = img.resize(new_size, resample)
    canvas = Image.new("RGBA", size, fill)
    x = (size[0] - resized.width) // 2
    y = (size[1] - resized.height) // 2
    canvas.alpha_composite(resized, (x, y))
    return canvas


def resize_square(img: Image.Image, size: int) -> Image.Image:
    img = img.convert("RGBA")
    width, height = img.size
    if width != height:
        side = min(width, height)
        left = (width - side) // 2
        top = (height - side) // 2
        img = img.crop((left, top, left + side, top + side))
    return img.resize((size, size), Image.Resampling.LANCZOS)


def save_png(img: Image.Image, path: Path) -> None:
    ensure_parent(path)
    img.save(path)


def convert_dds(src_png: Path, dst_dds: Path) -> None:
    ensure_parent(dst_dds)
    temp_dir = DOCS / "_dds_tmp"
    temp_dir.mkdir(parents=True, exist_ok=True)
    run([str(TEXCONV), "-y", "-nologo", "-f", "B8G8R8A8_UNORM", "-o", str(temp_dir), str(src_png)])
    produced = temp_dir / (src_png.stem + ".DDS")
    if not produced.exists():
        produced = temp_dir / (src_png.stem + ".dds")
    shutil.move(str(produced), dst_dds)


def checker_preview(img: Image.Image) -> Image.Image:
    tile = 8
    bg = Image.new("RGBA", img.size, (200, 200, 200, 255))
    draw = ImageDraw.Draw(bg)
    for y in range(0, img.height, tile):
        for x in range(0, img.width, tile):
            if ((x // tile) + (y // tile)) % 2:
                draw.rectangle((x, y, x + tile - 1, y + tile - 1), fill=(145, 145, 145, 255))
    bg.alpha_composite(img)
    return bg


def process_transparent_assets() -> None:
    previews = []
    for asset in TRANSPARENT_ASSETS:
        src = SOURCE / asset.source
        alpha_path = PROCESSED / (Path(asset.processed).stem + "_alpha.png")
        out = PROCESSED / asset.processed
        remove_chroma(src, alpha_path)
        final = fit_to_canvas(Image.open(alpha_path), asset.size, asset.margin)
        save_png(final, out)
        convert_dds(out, ROOT / asset.final_dds)
        previews.append(checker_preview(final))
    if previews:
        save_contact_sheet(previews, [Path(a.processed).stem for a in TRANSPARENT_ASSETS], CONTACTS / "secret_alliance_icons_contact.png", columns=4)


def process_achievements() -> None:
    previews = []
    labels = []
    for asset in ACHIEVEMENTS:
        src = SOURCE / asset.source
        img = resize_square(Image.open(src), 64)
        processed = PROCESSED / f"achievement_{asset.base_name}.png"
        save_png(img, processed)
        base = ROOT / "gfx" / "achievements" / f"{asset.base_name}.dds"
        grey = ROOT / "gfx" / "achievements" / f"{asset.base_name}_grey.dds"
        not_eligible = ROOT / "gfx" / "achievements" / f"{asset.base_name}_not_eligible.dds"
        convert_dds(processed, base)
        grey_img = ImageOps.grayscale(img).convert("RGBA")
        grey_png = PROCESSED / f"achievement_{asset.base_name}_grey.png"
        save_png(grey_img, grey_png)
        convert_dds(grey_png, grey)
        blocked = grey_img.copy()
        draw = ImageDraw.Draw(blocked)
        draw.line((12, 12, 52, 52), fill=(180, 25, 25, 255), width=7)
        draw.line((52, 12, 12, 52), fill=(180, 25, 25, 255), width=7)
        blocked_png = PROCESSED / f"achievement_{asset.base_name}_not_eligible.png"
        save_png(blocked, blocked_png)
        convert_dds(blocked_png, not_eligible)
        previews.append(img)
        labels.append(asset.base_name)
    if previews:
        save_contact_sheet(previews, labels, CONTACTS / "secret_alliance_achievements_contact.png", columns=4)


def split_grid(grid: Image.Image) -> list[Image.Image]:
    width, height = grid.size
    cell_w = width // 4
    cell_h = height // 2
    frames = []
    for row in range(2):
        for col in range(4):
            box = (col * cell_w, row * cell_h, (col + 1) * cell_w, (row + 1) * cell_h)
            frames.append(grid.crop(box))
    return frames


def save_contact_sheet(images: list[Image.Image], labels: list[str], path: Path, columns: int = 4) -> None:
    if not images:
        return
    thumb_w = max(img.width for img in images)
    thumb_h = max(img.height for img in images)
    label_h = 18
    rows = math.ceil(len(images) / columns)
    sheet = Image.new("RGBA", (columns * thumb_w, rows * (thumb_h + label_h)), (24, 24, 24, 255))
    draw = ImageDraw.Draw(sheet)
    for index, (img, label) in enumerate(zip(images, labels)):
        x = (index % columns) * thumb_w
        y = (index // columns) * (thumb_h + label_h)
        frame = Image.new("RGBA", (thumb_w, thumb_h), (24, 24, 24, 255))
        frame.alpha_composite(img, ((thumb_w - img.width) // 2, (thumb_h - img.height) // 2))
        sheet.alpha_composite(frame, (x, y))
        draw.text((x + 2, y + thumb_h + 2), label[:24], fill=(230, 230, 230, 255))
    save_png(sheet, path)


def process_animations() -> None:
    all_preview_frames = []
    all_labels = []
    for asset in ANIMATIONS:
        base = ANIM / asset.slug
        grid = Image.open(base / "source_frames" / asset.grid_source)
        frames = split_grid(grid)
        processed_frames = []
        labels = []
        for idx, frame in enumerate(frames):
            raw_frame = base / "source_frames" / f"{asset.slug}_{idx:03d}_source.png"
            save_png(frame, raw_frame)
            alpha_frame = base / "source_frames" / f"{asset.slug}_{idx:03d}_alpha.png"
            remove_chroma(raw_frame, alpha_frame)
            fitted = fit_to_canvas(Image.open(alpha_frame), asset.frame_size, asset.margin)
            processed_path = base / "processed_frames" / f"{asset.slug}_{idx:03d}.png"
            save_png(fitted, processed_path)
            processed_frames.append(fitted)
            labels.append(f"{asset.slug}_{idx:03d}")
        static_png = PROCESSED / f"{asset.slug}.png"
        save_png(processed_frames[0], static_png)
        convert_dds(static_png, ROOT / asset.final_static_dds)
        sheet = Image.new("RGBA", (asset.frame_size[0] * len(processed_frames), asset.frame_size[1]), (0, 0, 0, 0))
        for idx, frame in enumerate(processed_frames):
            sheet.alpha_composite(frame, (idx * asset.frame_size[0], 0))
        sheet_png = base / "sheets" / f"{asset.slug}_animated_sheet.png"
        save_png(sheet, sheet_png)
        convert_dds(sheet_png, ROOT / asset.final_sheet_dds)
        preview_gif = base / "previews" / f"{asset.slug}_preview.gif"
        processed_frames[0].save(preview_gif, save_all=True, append_images=processed_frames[1:], duration=125, loop=0, disposal=2, transparency=0)
        save_contact_sheet([checker_preview(img) for img in processed_frames], labels, base / "previews" / f"{asset.slug}_contact.png", columns=4)
        all_preview_frames.append(checker_preview(processed_frames[0]))
        all_labels.append(asset.slug)
    if all_preview_frames:
        save_contact_sheet(all_preview_frames, all_labels, CONTACTS / "secret_alliance_animation_statics_contact.png", columns=3)


def verify_outputs() -> None:
    expected = [ROOT / a.final_dds for a in TRANSPARENT_ASSETS]
    expected.extend(ROOT / "gfx" / "achievements" / f"{a.base_name}.dds" for a in ACHIEVEMENTS)
    expected.extend(ROOT / "gfx" / "achievements" / f"{a.base_name}_grey.dds" for a in ACHIEVEMENTS)
    expected.extend(ROOT / "gfx" / "achievements" / f"{a.base_name}_not_eligible.dds" for a in ACHIEVEMENTS)
    expected.extend(ROOT / a.final_static_dds for a in ANIMATIONS)
    expected.extend(ROOT / a.final_sheet_dds for a in ANIMATIONS)
    missing = [str(path) for path in expected if not path.exists()]
    if missing:
        raise FileNotFoundError("\n".join(missing))


if __name__ == "__main__":
    process_transparent_assets()
    process_achievements()
    process_animations()
    verify_outputs()
