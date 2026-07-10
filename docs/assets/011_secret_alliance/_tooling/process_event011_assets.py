from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageOps


ROOT = Path(__file__).resolve().parents[4]
PACKAGE = ROOT / "docs" / "assets" / "011_secret_alliance"
SOURCE = PACKAGE / "source_png"
PROCESSED = PACKAGE / "processed_png"
CONTACT = PACKAGE / "contact_sheets"
ALPHA = ROOT / "tmp" / "imagegen" / "011_secret_alliance" / "source_png"
ANIMATION = PACKAGE / "animations" / "coalition_closure_warning"
ANIMATION_ALPHA = ROOT / "tmp" / "imagegen" / "011_secret_alliance" / "animation"
OVERLAY = SOURCE / "achievement_not_eligible_overlay_recovered.png"


CATEGORY = [
    "decision_category_foreign_interference",
    "decision_category_coalition_crisis",
]

METERS = [
    "evidence_meter_frame",
    "evidence_meter_fill",
    "preparedness_meter_frame",
    "preparedness_meter_fill",
]

SUSPECT_STATES = [
    "suspect_card_unknown",
    "suspect_card_possible",
    "suspect_card_likely",
    "suspect_card_confirmed",
]

STATUS = [
    "status_recent_operation",
    "status_turned_channel",
    "status_false_lead",
    "status_war_pressure",
]

DECISIONS = [
    "decision_compare_traffic",
    "decision_trace_courier",
    "decision_compare_sabotage",
    "decision_compartmentalize",
    "decision_secure_industry",
    "decision_harden_border",
    "decision_quiet_approach",
    "decision_security_guarantee",
    "decision_feed_false_plans",
    "decision_turn_member",
    "decision_disrupt_conference",
    "decision_border_intercept",
    "decision_release_dossier",
    "decision_emergency_mobilization",
    "decision_preempt_coalition",
    "decision_offer_separate_terms",
    "decision_strike_depots",
]

IDEAS = [
    "idea_unexplained_interference",
    "idea_compromised_channels",
    "idea_hardened_networks",
    "idea_public_coalition_pressure",
    "idea_known_enemy_plans",
    "idea_coalition_opening_coordination",
    "idea_fractured_coalition",
]

ACHIEVEMENTS = [
    "011_secret_alliance_the_empty_chair",
    "011_secret_alliance_every_thread",
    "011_secret_alliance_their_man_in_the_room",
    "011_secret_alliance_divide_the_table",
    "011_secret_alliance_surrounded_not_buried",
    "011_secret_alliance_two_giants_one_grave",
]


def trim_alpha(image: Image.Image) -> Image.Image:
    rgba = image.convert("RGBA")
    alpha = rgba.getchannel("A")
    bbox = alpha.point(lambda value: 255 if value > 8 else 0).getbbox()
    if bbox is None:
        raise RuntimeError("Generated source has no visible pixels after chroma-key removal")
    return rgba.crop(bbox)


def fit_alpha(source: Path, size: tuple[int, int], padding: int) -> Image.Image:
    image = trim_alpha(Image.open(source))
    target_w, target_h = size
    maximum = (max(1, target_w - padding * 2), max(1, target_h - padding * 2))
    image.thumbnail(maximum, Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", size, (0, 0, 0, 0))
    x = (target_w - image.width) // 2
    y = (target_h - image.height) // 2
    canvas.alpha_composite(image, (x, y))
    return canvas


def cover(source: Path, size: tuple[int, int]) -> Image.Image:
    image = Image.open(source).convert("RGBA")
    return ImageOps.fit(image, size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))


def checker(size: tuple[int, int], tile: int = 8) -> Image.Image:
    background = Image.new("RGBA", size, (0, 0, 0, 255))
    draw = ImageDraw.Draw(background)
    colors = ((78, 78, 78, 255), (126, 126, 126, 255))
    for y in range(0, size[1], tile):
        for x in range(0, size[0], tile):
            draw.rectangle(
                (x, y, min(x + tile - 1, size[0] - 1), min(y + tile - 1, size[1] - 1)),
                fill=colors[((x // tile) + (y // tile)) % 2],
            )
    return background


def make_contact(
    items: list[tuple[str, Image.Image]],
    destination: Path,
    columns: int,
    preview_size: tuple[int, int],
) -> None:
    cell_w = preview_size[0] + 24
    cell_h = preview_size[1] + 42
    rows = math.ceil(len(items) / columns)
    sheet = Image.new("RGB", (columns * cell_w, rows * cell_h), (18, 18, 18))
    draw = ImageDraw.Draw(sheet)
    for index, (label, source) in enumerate(items):
        cell_x = (index % columns) * cell_w
        cell_y = (index // columns) * cell_h
        preview = checker(preview_size)
        image = source.convert("RGBA").copy()
        image.thumbnail((preview_size[0] - 8, preview_size[1] - 8), Image.Resampling.LANCZOS)
        preview.alpha_composite(
            image,
            ((preview_size[0] - image.width) // 2, (preview_size[1] - image.height) // 2),
        )
        sheet.paste(preview.convert("RGB"), (cell_x + 12, cell_y + 4))
        draw.text((cell_x + 8, cell_y + preview_size[1] + 10), label[:26], fill=(238, 238, 238))
    destination.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(destination)


def save(image: Image.Image, name: str) -> Path:
    PROCESSED.mkdir(parents=True, exist_ok=True)
    path = PROCESSED / f"{name}.png"
    image.save(path)
    return path


def register(
    conversions: list[tuple[Path, Path, tuple[int, int]]],
    png: Path,
    dds: Path,
    size: tuple[int, int],
) -> None:
    conversions.append((png, dds, size))


def main() -> None:
    PROCESSED.mkdir(parents=True, exist_ok=True)
    CONTACT.mkdir(parents=True, exist_ok=True)
    conversions: list[tuple[Path, Path, tuple[int, int]]] = []

    decision_contact: list[tuple[str, Image.Image]] = []
    for name in CATEGORY + DECISIONS:
        image = fit_alpha(ALPHA / f"{name}_source.png", (32, 32), 1)
        png = save(image, name)
        register(
            conversions,
            png,
            ROOT / "gfx" / "interface" / "decisions" / "011_secret_alliance" / f"{name}.dds",
            (32, 32),
        )
        decision_contact.append((name, image))

    idea_contact: list[tuple[str, Image.Image]] = []
    for name in IDEAS:
        image = fit_alpha(ALPHA / f"{name}_source.png", (64, 64), 3)
        png = save(image, name)
        register(
            conversions,
            png,
            ROOT / "gfx" / "interface" / "ideas" / "011_secret_alliance" / f"{name}.dds",
            (64, 64),
        )
        idea_contact.append((name, image))

    panel = cover(SOURCE / "counter_network_panel_source.png", (720, 360))
    panel_png = save(panel, "counter_network_panel")
    register(
        conversions,
        panel_png,
        ROOT / "gfx" / "interface" / "011_secret_alliance" / "counter_network_panel.dds",
        (720, 360),
    )

    ui_contact: list[tuple[str, Image.Image]] = [("counter_network_panel", panel)]
    for name in METERS:
        image = fit_alpha(ALPHA / f"{name}_source.png", (256, 24), 1)
        png = save(image, name)
        register(
            conversions,
            png,
            ROOT / "gfx" / "interface" / "011_secret_alliance" / f"{name}.dds",
            (256, 24),
        )
        ui_contact.append((name, image))

    suspect_frames: list[Image.Image] = []
    for name in SUSPECT_STATES:
        image = fit_alpha(ALPHA / f"{name}_source.png", (184, 96), 1)
        save(image, name)
        suspect_frames.append(image)
        ui_contact.append((name, image))
    suspect_sheet = Image.new("RGBA", (736, 96), (0, 0, 0, 0))
    for index, frame in enumerate(suspect_frames):
        suspect_sheet.paste(frame, (index * 184, 0))
    suspect_sheet_png = save(suspect_sheet, "suspect_card_states")
    register(
        conversions,
        suspect_sheet_png,
        ROOT / "gfx" / "interface" / "011_secret_alliance" / "suspect_card_states.dds",
        (736, 96),
    )

    for name in STATUS:
        image = fit_alpha(ALPHA / f"{name}_source.png", (32, 32), 1)
        png = save(image, name)
        register(
            conversions,
            png,
            ROOT / "gfx" / "interface" / "011_secret_alliance" / f"{name}.dds",
            (32, 32),
        )
        ui_contact.append((name, image))

    faction_name = "faction_anti_target_pact_emblem"
    faction = fit_alpha(ALPHA / f"{faction_name}_source.png", (64, 64), 3)
    faction_png = save(faction, faction_name)
    register(
        conversions,
        faction_png,
        ROOT / "gfx" / "interface" / "011_secret_alliance" / f"{faction_name}.dds",
        (64, 64),
    )
    idea_contact.append((faction_name, faction))

    overlay = Image.open(OVERLAY).convert("RGBA")
    if overlay.size != (64, 64):
        raise RuntimeError(f"Achievement overlay is {overlay.size}, expected 64x64")
    achievement_contact: list[tuple[str, Image.Image]] = []
    for name in ACHIEVEMENTS:
        base = cover(SOURCE / f"{name}_source.png", (64, 64))
        alpha = base.getchannel("A")
        grey = ImageOps.grayscale(base.convert("RGB")).convert("RGBA")
        grey.putalpha(alpha)
        not_eligible = Image.alpha_composite(grey, overlay)
        for suffix, image in (("", base), ("_grey", grey), ("_not_eligible", not_eligible)):
            variant_name = f"{name}{suffix}"
            png = save(image, variant_name)
            register(
                conversions,
                png,
                ROOT / "gfx" / "achievements" / f"{variant_name}.dds",
                (64, 64),
            )
            achievement_contact.append((variant_name, image))

    processed_frames_dir = ANIMATION / "processed_frames"
    sheets_dir = ANIMATION / "sheets"
    previews_dir = ANIMATION / "previews"
    for directory in (processed_frames_dir, sheets_dir, previews_dir):
        directory.mkdir(parents=True, exist_ok=True)
    animation_frames: list[Image.Image] = []
    for index in range(8):
        source = ANIMATION_ALPHA / f"coalition_closure_warning_{index:03d}_source.png"
        frame = cover(source, (128, 96))
        frame_path = processed_frames_dir / f"coalition_closure_warning_{index:03d}.png"
        frame.save(frame_path)
        animation_frames.append(frame)
    static = animation_frames[4]
    static_png = sheets_dir / "coalition_closure_warning_static.png"
    static.save(static_png)
    sheet = Image.new("RGBA", (1024, 96), (0, 0, 0, 0))
    for index, frame in enumerate(animation_frames):
        sheet.paste(frame, (index * 128, 0))
    sheet_png = sheets_dir / "coalition_closure_warning_sheet.png"
    sheet.save(sheet_png)
    register(
        conversions,
        static_png,
        ROOT / "gfx" / "interface" / "011_secret_alliance" / "coalition_closure_warning_static.dds",
        (128, 96),
    )
    register(
        conversions,
        sheet_png,
        ROOT / "gfx" / "interface" / "011_secret_alliance" / "coalition_closure_warning_sheet.dds",
        (1024, 96),
    )
    animation_frames[0].save(
        previews_dir / "coalition_closure_warning_preview.gif",
        save_all=True,
        append_images=animation_frames[1:] + [animation_frames[0]],
        duration=125,
        loop=0,
        disposal=2,
    )
    make_contact(
        [(f"frame_{index:03d}", frame) for index, frame in enumerate(animation_frames)],
        previews_dir / "coalition_closure_warning_contact.png",
        4,
        (192, 144),
    )

    make_contact(
        decision_contact,
        CONTACT / "event011_decision_icons_contact.png",
        5,
        (112, 112),
    )
    make_contact(
        idea_contact,
        CONTACT / "event011_idea_and_faction_icons_contact.png",
        4,
        (128, 128),
    )
    make_contact(
        ui_contact,
        CONTACT / "event011_counter_network_ui_contact.png",
        3,
        (256, 128),
    )
    make_contact(
        achievement_contact,
        CONTACT / "event011_achievement_triplets_contact.png",
        3,
        (128, 128),
    )

    conversion_manifest = PACKAGE / "conversion_manifest.tsv"
    conversion_manifest.write_text(
        "processed_png\tfinal_dds\twidth\theight\n"
        + "\n".join(
            f"{png.relative_to(ROOT).as_posix()}\t{dds.relative_to(ROOT).as_posix()}\t{size[0]}\t{size[1]}"
            for png, dds, size in conversions
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"Processed {len(conversions)} runtime DDS targets.")


if __name__ == "__main__":
    main()
