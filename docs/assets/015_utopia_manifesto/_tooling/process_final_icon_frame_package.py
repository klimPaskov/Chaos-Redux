"""Build Event 015's final icon and authored-frame package.

This script performs only deterministic asset operations: fixed-grid crops,
the repository imagegen chroma helper, alpha fitting, achievement variants,
frame-sheet assembly, review contacts, GIF previews, and DDS conversion.
The image content itself is authored in the frozen imagegen atlases and
storyboards under docs/assets/015_utopia_manifesto/.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[4]
ASSET_ROOT = REPO_ROOT / "docs/assets/015_utopia_manifesto"
SOURCE_ROOT = ASSET_ROOT / "source_png/final_icons"
PROCESSED_ROOT = ASSET_ROOT / "processed_png/final_icons"
DDS_ROOT = ASSET_ROOT / "dds/final_icons"

CHROMA_HELPER = Path(
    "C:/Users/klimp/.codex/skills/.system/imagegen/scripts/remove_chroma_key.py"
)
DDS_HELPER = REPO_ROOT / ".agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py"
ACHIEVEMENT_OVERLAY = (
    REPO_ROOT
    / ".agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/achievements/overlay.png"
)

DECISION_SOURCE = SOURCE_ROOT / "utopia_final_decision_category_imagegen_atlas.png"
IDEA_SOURCE = SOURCE_ROOT / "utopia_final_idea_imagegen_atlas.png"
ACHIEVEMENT_SOURCE = SOURCE_ROOT / "utopia_final_achievement_imagegen_atlas.png"

DECISION_SPRITES = [
    "decision_category_utopia_district",
    "decision_category_utopia_island",
    "decision_category_utopia_necessary_ground",
    "decision_category_utopia_stewardship",
    "decision_category_utopia_defense",
    "decision_category_utopia_governance",
    "decision_category_utopia_formation",
    "decision_utopia_publish_accounts",
    "decision_utopia_seasonal_reserve",
    "decision_utopia_second_trade",
    "decision_utopia_land_register",
    "decision_utopia_district_survey",
    "decision_utopia_district_foundation",
    "decision_utopia_island_project",
    "decision_utopia_common_harbor",
    "decision_utopia_inland_terminal",
    "decision_utopia_need_case",
    "decision_utopia_purchase",
    "decision_utopia_lease",
    "decision_utopia_joint_administration",
    "decision_utopia_ultimatum",
    "decision_utopia_emergency_provision",
    "decision_utopia_long_integration",
    "decision_utopia_technical_mission",
    "decision_utopia_reserve_compact",
    "decision_utopia_citizen_watch",
    "decision_utopia_engineer_companies",
    "decision_utopia_auxiliary_contract",
    "decision_utopia_constitutional_correction",
    "decision_utopia_formation_proclamation",
]

IDEA_SPRITES = [
    "idea_utopia_unmeasured_country",
    "idea_utopia_inherited_order",
    "idea_utopia_charter_of_households",
    "idea_utopia_common_table",
    "idea_utopia_perfect_measure",
    "idea_utopia_closed_island",
    "idea_utopia_practical_commonwealth",
    "idea_utopia_garden_district_network",
    "idea_utopia_auxiliary_dependency",
    "idea_utopia_stewardship_burden",
]

ACHIEVEMENT_IDS = [
    "utopia_manifesto_no_place_but_home",
    "utopia_manifesto_need_not_greed",
    "utopia_manifesto_every_calling_chosen",
    "utopia_manifesto_two_year_table",
    "utopia_manifesto_archipelago_of_small_places",
    "utopia_manifesto_inland_island",
    "utopia_manifesto_gold_for_common_use",
    "utopia_manifesto_the_joke_understood",
    "utopia_manifesto_consent_of_the_governed",
    "utopia_manifesto_the_perfect_measure",
    "utopia_manifesto_closed_circle",
    "utopia_manifesto_no_foreign_hands",
    "utopia_manifesto_the_stores_remain",
    "utopia_manifesto_no_one_in_chains",
]

ANIMATIONS = [
    {
        "name": "utopia_need_warning",
        "cols": 4,
        "rows": 2,
        "count": 8,
        "size": (64, 64),
        "fps": 5,
        "static_index": 4,
        "source": ASSET_ROOT
        / "animations/utopia_need_warning/source_storyboards/utopia_need_warning_imagegen_storyboard.png",
        "stretch": False,
        "fixed_crop": True,
        "fit_reference_indices": list(range(8)),
        "center_on_bbox": False,
    },
    {
        "name": "utopia_reserve_fill",
        "cols": 4,
        "rows": 2,
        "count": 8,
        "size": (300, 24),
        "fps": 4,
        "static_index": 4,
        "source": ASSET_ROOT
        / "animations/utopia_reserve_fill/source_storyboards/utopia_reserve_fill_imagegen_storyboard.png",
        "stretch": True,
        "fixed_crop": False,
        "fit_reference_indices": list(range(8)),
        "center_on_bbox": False,
    },
    {
        "name": "utopia_formation_ready_seal",
        "cols": 5,
        "rows": 2,
        "count": 10,
        "size": (96, 96),
        "fps": 5,
        "static_index": 5,
        "source": ASSET_ROOT
        / "animations/utopia_formation_ready_seal/source_storyboards/utopia_formation_ready_seal_imagegen_storyboard.png",
        "stretch": False,
        "fixed_crop": True,
        "fit_reference_indices": [0, 1, 2, 3, 4, 5, 6, 8, 9],
        "center_on_bbox": True,
    },
]


def require_inputs() -> None:
    for path in [
        CHROMA_HELPER,
        DDS_HELPER,
        ACHIEVEMENT_OVERLAY,
        DECISION_SOURCE,
        IDEA_SOURCE,
        ACHIEVEMENT_SOURCE,
        *(item["source"] for item in ANIMATIONS),
    ]:
        if not Path(path).is_file():
            raise FileNotFoundError(path)


def ensure_dirs() -> None:
    for path in [PROCESSED_ROOT, DDS_ROOT]:
        path.mkdir(parents=True, exist_ok=True)
    for item in ANIMATIONS:
        base = ASSET_ROOT / "animations" / item["name"]
        for child in ["source_frames", "processed_frames", "sheets", "previews"]:
            (base / child).mkdir(parents=True, exist_ok=True)


def crop_grid(image: Image.Image, cols: int, rows: int, count: int, inset: int = 3):
    width, height = image.size
    for index in range(count):
        col = index % cols
        row = index // cols
        left = round(col * width / cols) + inset
        top = round(row * height / rows) + inset
        right = round((col + 1) * width / cols) - inset
        bottom = round((row + 1) * height / rows) - inset
        yield image.crop((left, top, right, bottom))


def remove_chroma(source: Path, output: Path, key: str) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            sys.executable,
            str(CHROMA_HELPER),
            "--input",
            str(source),
            "--out",
            str(output),
            "--key-color",
            key,
            "--soft-matte",
            "--transparent-threshold",
            "14",
            "--opaque-threshold",
            "92",
            "--edge-feather",
            "0.35",
            "--spill-cleanup",
            "--force",
        ],
        check=True,
        stdout=subprocess.DEVNULL,
    )


def alpha_bbox(image: Image.Image, threshold: int = 24):
    alpha = image.getchannel("A")
    mask = alpha.point(lambda value: 255 if value >= threshold else 0)
    return mask.getbbox()


def fit_rgba(
    image: Image.Image,
    target_size: tuple[int, int],
    margin: int,
    stretch: bool = False,
) -> Image.Image:
    rgba = image.convert("RGBA")
    bbox = alpha_bbox(rgba)
    if bbox is None:
        raise ValueError("Chroma removal produced an empty image")
    subject = rgba.crop(bbox)
    available = (target_size[0] - margin * 2, target_size[1] - margin * 2)
    if stretch:
        fitted = subject.resize(available, Image.Resampling.LANCZOS)
    else:
        fitted = ImageOps.contain(subject, available, Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", target_size, (0, 0, 0, 0))
    x = (target_size[0] - fitted.width) // 2
    y = (target_size[1] - fitted.height) // 2
    canvas.alpha_composite(fitted, (x, y))
    return canvas


def crop_with_padding(
    image: Image.Image,
    box: tuple[int, int, int, int],
) -> Image.Image:
    left, top, right, bottom = box
    output = Image.new("RGBA", (right - left, bottom - top), (0, 0, 0, 0))
    source_box = (
        max(0, left),
        max(0, top),
        min(image.width, right),
        min(image.height, bottom),
    )
    if source_box[2] > source_box[0] and source_box[3] > source_box[1]:
        target = (source_box[0] - left, source_box[1] - top)
        output.alpha_composite(image.crop(source_box).convert("RGBA"), target)
    return output


def fit_fixed_sequence(
    images: list[Image.Image],
    target_size: tuple[int, int],
    margin: int,
    reference_indices: list[int],
    center_on_bbox: bool,
) -> list[Image.Image]:
    """Fit a sequence through one shared source crop and scale.

    A shared crop preserves the imagegen-authored camera and center anchor.
    Outlier effects such as the formation seal's flare can be excluded from
    the reference measurements while remaining visible inside the crop.
    """

    reference_boxes = []
    for index in reference_indices:
        bbox = alpha_bbox(images[index].convert("RGBA"))
        if bbox is None:
            raise ValueError(f"Empty reference frame {index}")
        reference_boxes.append(bbox)
    crop_width = round(max(box[2] - box[0] for box in reference_boxes) * 1.08)
    crop_height = round(max(box[3] - box[1] for box in reference_boxes) * 1.08)
    crop_width = max(1, crop_width)
    crop_height = max(1, crop_height)

    fitted_frames: list[Image.Image] = []
    for image in images:
        rgba = image.convert("RGBA")
        if center_on_bbox:
            current_box = alpha_bbox(rgba)
            if current_box is None:
                raise ValueError("Empty animation frame")
            center_x = (current_box[0] + current_box[2]) // 2
            center_y = (current_box[1] + current_box[3]) // 2
        else:
            center_x = rgba.width // 2
            center_y = rgba.height // 2
        left = center_x - crop_width // 2
        top = center_y - crop_height // 2
        fixed = crop_with_padding(
            rgba,
            (left, top, left + crop_width, top + crop_height),
        )
        available = (target_size[0] - margin * 2, target_size[1] - margin * 2)
        resized = ImageOps.contain(fixed, available, Image.Resampling.LANCZOS)
        canvas = Image.new("RGBA", target_size, (0, 0, 0, 0))
        x = (target_size[0] - resized.width) // 2
        y = (target_size[1] - resized.height) // 2
        canvas.alpha_composite(resized, (x, y))
        fitted_frames.append(canvas)
    return fitted_frames


def convert_dds(source: Path, output: Path, size: tuple[int, int]) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            sys.executable,
            str(DDS_HELPER),
            "--input",
            str(source),
            "--output",
            str(output),
            "--width",
            str(size[0]),
            "--height",
            str(size[1]),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
    )


def dark_preview(image: Image.Image) -> Image.Image:
    background = Image.new("RGBA", image.size, (24, 25, 27, 255))
    background.alpha_composite(image.convert("RGBA"))
    return background.convert("RGB")


def contact_sheet(
    images: list[Image.Image],
    names: list[str],
    cols: int,
    output: Path,
    preview_size: tuple[int, int],
) -> None:
    rows = (len(images) + cols - 1) // cols
    label_height = 32
    gutter = 12
    cell_width = preview_size[0] + gutter * 2
    cell_height = preview_size[1] + label_height + gutter * 2
    sheet = Image.new(
        "RGB",
        (cell_width * cols, cell_height * rows),
        (18, 19, 21),
    )
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()
    for index, (image, name) in enumerate(zip(images, names)):
        col = index % cols
        row = index // cols
        x = col * cell_width + gutter
        y = row * cell_height + gutter
        preview = dark_preview(image).resize(preview_size, Image.Resampling.NEAREST)
        sheet.paste(preview, (x, y))
        label = name if len(name) <= 34 else name[:31] + "..."
        draw.text((x, y + preview_size[1] + 7), label, fill=(225, 218, 197), font=font)
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output)


def process_chroma_atlas(
    source_path: Path,
    sprites: list[str],
    cols: int,
    rows: int,
    size: tuple[int, int],
    runtime_root: Path,
    margin: int,
) -> list[Image.Image]:
    atlas = Image.open(source_path).convert("RGB")
    processed: list[Image.Image] = []
    for sprite, cell in zip(sprites, crop_grid(atlas, cols, rows, len(sprites))):
        source_cell = SOURCE_ROOT / f"{sprite}_source.png"
        keyed_cell = PROCESSED_ROOT / f"{sprite}_keyed.png"
        processed_cell = PROCESSED_ROOT / f"{sprite}.png"
        cell.save(source_cell)
        remove_chroma(source_cell, keyed_cell, "#ff00ff")
        fitted = fit_rgba(Image.open(keyed_cell), size, margin=margin)
        fitted.save(processed_cell)
        docs_dds = DDS_ROOT / f"{sprite}.dds"
        runtime_dds = runtime_root / f"{sprite}.dds"
        convert_dds(processed_cell, docs_dds, size)
        runtime_dds.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(docs_dds, runtime_dds)
        processed.append(fitted)
    return processed


def process_achievements() -> list[Image.Image]:
    atlas = Image.open(ACHIEVEMENT_SOURCE).convert("RGB")
    overlay = Image.open(ACHIEVEMENT_OVERLAY).convert("RGBA")
    runtime_root = REPO_ROOT / "gfx/achievements"
    runtime_root.mkdir(parents=True, exist_ok=True)
    processed: list[Image.Image] = []
    contact_images: list[Image.Image] = []
    contact_names: list[str] = []
    for achievement_id, cell in zip(
        ACHIEVEMENT_IDS,
        crop_grid(atlas, 4, 4, len(ACHIEVEMENT_IDS), inset=2),
    ):
        source_cell = SOURCE_ROOT / f"achievement_{achievement_id}_source.png"
        base_png = PROCESSED_ROOT / f"achievement_{achievement_id}.png"
        grey_png = PROCESSED_ROOT / f"achievement_{achievement_id}_grey.png"
        not_eligible_png = (
            PROCESSED_ROOT / f"achievement_{achievement_id}_not_eligible.png"
        )
        cell.save(source_cell)
        base = ImageOps.fit(cell, (64, 64), Image.Resampling.LANCZOS).convert("RGBA")
        grey = ImageOps.grayscale(base.convert("RGB")).convert("RGBA")
        not_eligible = Image.alpha_composite(grey, overlay)
        variants = {
            achievement_id: (base, base_png),
            f"{achievement_id}_grey": (grey, grey_png),
            f"{achievement_id}_not_eligible": (not_eligible, not_eligible_png),
        }
        for stem, (image, png_path) in variants.items():
            image.save(png_path)
            docs_dds = DDS_ROOT / f"{stem}.dds"
            runtime_dds = runtime_root / f"{stem}.dds"
            convert_dds(png_path, docs_dds, (64, 64))
            shutil.copy2(docs_dds, runtime_dds)
            contact_images.append(image)
            contact_names.append(stem)
        processed.append(base)
    contact_sheet(
        contact_images,
        contact_names,
        3,
        PROCESSED_ROOT / "utopia_final_achievement_triplets_contact.png",
        (128, 128),
    )
    return processed


def process_animation(item: dict) -> list[Image.Image]:
    name = item["name"]
    base = ASSET_ROOT / "animations" / name
    source_dir = base / "source_frames"
    processed_dir = base / "processed_frames"
    sheet_dir = base / "sheets"
    preview_dir = base / "previews"
    storyboard = Image.open(item["source"]).convert("RGB")
    keyed_frames: list[Image.Image] = []
    for index, cell in enumerate(
        crop_grid(storyboard, item["cols"], item["rows"], item["count"])
    ):
        source_frame = source_dir / f"{name}_source_{index:03d}.png"
        keyed_frame = processed_dir / f"{name}_keyed_{index:03d}.png"
        processed_frame = processed_dir / f"{name}_frame_{index:03d}.png"
        cell.save(source_frame)
        remove_chroma(source_frame, keyed_frame, "#00ff00")
        keyed_frames.append(Image.open(keyed_frame).convert("RGBA"))

    if item["fixed_crop"]:
        frames = fit_fixed_sequence(
            keyed_frames,
            item["size"],
            margin=1,
            reference_indices=item["fit_reference_indices"],
            center_on_bbox=item["center_on_bbox"],
        )
    else:
        frames = [
            fit_rgba(
                image,
                item["size"],
                margin=1,
                stretch=item["stretch"],
            )
            for image in keyed_frames
        ]

    for index, fitted in enumerate(frames):
        processed_frame = processed_dir / f"{name}_frame_{index:03d}.png"
        fitted.save(processed_frame)

    frame_width, frame_height = item["size"]
    sheet = Image.new(
        "RGBA",
        (frame_width * item["count"], frame_height),
        (0, 0, 0, 0),
    )
    for index, frame in enumerate(frames):
        sheet.alpha_composite(frame, (index * frame_width, 0))
    sheet_png = sheet_dir / f"{name}_sheet.png"
    static_png = sheet_dir / f"{name}_static.png"
    sheet.save(sheet_png)
    frames[item["static_index"]].save(static_png)

    preview_frames = [dark_preview(frame) for frame in frames]
    preview_frames[0].save(
        preview_dir / f"{name}_preview.gif",
        save_all=True,
        append_images=preview_frames[1:],
        duration=round(1000 / item["fps"]),
        loop=0,
        disposal=2,
        optimize=False,
    )
    preview_scale = 3 if frame_width <= 100 else 2
    contact_sheet(
        frames,
        [f"frame {index:03d}" for index in range(len(frames))],
        item["cols"],
        preview_dir / f"{name}_contact.png",
        (frame_width * preview_scale, frame_height * preview_scale),
    )

    runtime_root = REPO_ROOT / "gfx/interface/015_utopia_manifesto"
    convert_dds(
        static_png,
        runtime_root / f"{name}_static.dds",
        item["size"],
    )
    convert_dds(
        sheet_png,
        runtime_root / f"{name}_sheet.dds",
        (frame_width * item["count"], frame_height),
    )
    return frames


def main() -> None:
    require_inputs()
    ensure_dirs()

    decision_images = process_chroma_atlas(
        DECISION_SOURCE,
        DECISION_SPRITES,
        cols=5,
        rows=6,
        size=(32, 32),
        runtime_root=REPO_ROOT / "gfx/interface/decisions/015_utopia_manifesto",
        margin=1,
    )
    idea_images = process_chroma_atlas(
        IDEA_SOURCE,
        IDEA_SPRITES,
        cols=5,
        rows=2,
        size=(64, 64),
        runtime_root=REPO_ROOT / "gfx/interface/ideas/015_utopia_manifesto",
        margin=2,
    )
    achievement_images = process_achievements()

    contact_sheet(
        decision_images,
        DECISION_SPRITES,
        5,
        PROCESSED_ROOT / "utopia_final_decision_category_contact.png",
        (128, 128),
    )
    contact_sheet(
        idea_images,
        IDEA_SPRITES,
        5,
        PROCESSED_ROOT / "utopia_final_idea_contact.png",
        (160, 160),
    )
    contact_sheet(
        achievement_images,
        ACHIEVEMENT_IDS,
        4,
        PROCESSED_ROOT / "utopia_final_achievement_contact.png",
        (160, 160),
    )

    for item in ANIMATIONS:
        process_animation(item)

    print(
        "Built "
        f"{len(DECISION_SPRITES)} decision/category sprites, "
        f"{len(IDEA_SPRITES)} idea sprites, "
        f"{len(ACHIEVEMENT_IDS) * 3} achievement variants, and "
        f"{sum(item['count'] for item in ANIMATIONS)} authored animation frames."
    )


if __name__ == "__main__":
    main()
