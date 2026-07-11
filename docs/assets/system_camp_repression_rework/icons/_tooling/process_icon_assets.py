from __future__ import annotations

import hashlib
import math
import shutil
import struct
import subprocess
import textwrap
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[5]
PACKAGE = Path(__file__).resolve().parents[2]
ICON_PACKAGE = PACKAGE / "icons"
SOURCE = ICON_PACKAGE / "source"
ALPHA = ROOT / "tmp" / "camp_repression_icon_alpha"
PROCESSED = ICON_PACKAGE / "processed"
DDS_PACKAGE = ICON_PACKAGE / "dds"
CONTACT = ICON_PACKAGE / "contact_sheets"
LIVE_INTERFACE = ROOT / "gfx" / "interface" / "camp_repression" / "icons"
LIVE_ACHIEVEMENTS = ROOT / "gfx" / "achievements"
CONVERTER = ROOT / ".tools" / "convert_to_dds.py"
RECOVERED_OVERLAY = (
    ROOT
    / "docs"
    / "assets"
    / "011_secret_alliance"
    / "source_png"
    / "achievement_not_eligible_overlay_recovered.png"
)
PACKAGE_OVERLAY = SOURCE / "achievements" / "achievement_not_eligible_overlay_recovered.png"


DECISIONS = [
    "GFX_decision_bel_colonial_inspection",
    "GFX_decision_bel_congo_concession_quota",
    "GFX_decision_bel_congo_transport_corridor",
    "GFX_decision_camp_dismantlement",
    "GFX_decision_camp_evidence_destruction",
    "GFX_decision_camp_guard_allocation",
    "GFX_decision_fr_camp_legacy_review",
    "GFX_decision_fr_north_africa_labor",
    "GFX_decision_generic_destroy_evidence",
    "GFX_decision_generic_dismantle_network",
    "GFX_decision_generic_expand_labor_network",
    "GFX_decision_generic_guard_allocation",
    "GFX_decision_germany_auschwitz_transfer",
    "GFX_decision_germany_military_review",
    "GFX_decision_germany_ss_camp_administration",
    "GFX_decision_germany_ss_laboratory_annex",
    "GFX_decision_ita_camp_closure",
    "GFX_decision_ita_colonial_road_labor",
    "GFX_decision_ita_desert_camp_admin",
    "GFX_decision_japan_army_medical_review",
    "GFX_decision_japan_epidemic_containment",
    "GFX_decision_japan_pingfang_bureau",
    "GFX_decision_japan_pingfang_records",
    "GFX_decision_japan_prisoner_experiment",
    "GFX_decision_sov_famine_relief",
    "GFX_decision_sov_grain_confiscation",
    "GFX_decision_sov_gulag_dismantlement",
    "GFX_decision_sov_gulag_expansion",
    "GFX_decision_sov_nkvd_review",
    "GFX_decision_sov_prisoner_transfer",
    "GFX_decision_sov_records_retreat",
    "GFX_decision_uk_colonial_labor_works",
    "GFX_decision_uk_raj_detention",
    "GFX_decision_usa_court_review",
    "GFX_decision_usa_emergency_relocation",
    "GFX_decision_usa_redress_commission",
    "GFX_decision_vichy_internment_admin",
]

IDEAS = [
    "GFX_idea_bel_congo_extraction_pressure",
    "GFX_idea_camp_democratic_legitimacy_crisis",
    "GFX_idea_camp_dismantlement_reform",
    "GFX_idea_camp_network_overreach",
    "GFX_idea_camp_repression_overstretch",
    "GFX_idea_camp_repression_reform_pressure",
    "GFX_idea_congo_concession_labor_burden",
    "GFX_idea_fr_camp_legacy",
    "GFX_idea_generic_detention_network",
    "GFX_idea_generic_overextended_repression_network",
    "GFX_idea_germany_auschwitz_evidence_pressure",
    "GFX_idea_germany_dormant_ss_camp_legacy",
    "GFX_idea_germany_ss_camp_administration",
    "GFX_idea_ita_desert_camp_administration",
    "GFX_idea_ita_libyan_resistance_pressure",
    "GFX_idea_japan_ishii_influence",
    "GFX_idea_japan_kwantung_autonomy",
    "GFX_idea_japan_occupation_apparatus",
    "GFX_idea_japan_outbreak_pressure",
    "GFX_idea_japan_program_review",
    "GFX_idea_raj_colonial_labor_burden",
    "GFX_idea_sov_famine_pressure",
    "GFX_idea_sov_gulag_authority",
    "GFX_idea_sov_gulag_legacy",
    "GFX_idea_sov_gulag_reform",
    "GFX_idea_sov_republic_fear",
    "GFX_idea_uk_imperial_detention_administration",
    "GFX_idea_usa_civil_liberties_damage",
    "GFX_idea_usa_wartime_security_authority",
    "GFX_idea_vichy_collaboration_repression",
]

SPECIAL_PROJECTS = [
    "GFX_sp_japan_cherry_blossom_dossier",
    "GFX_sp_japan_epidemic_mapping_bureau",
    "GFX_sp_japan_kwantung_medical_intelligence",
    "GFX_sp_japan_occupation_test_ledger",
    "GFX_sp_japan_pingfang_records_office",
]

ACHIEVEMENTS = [
    "000_chaos_redux_60_inherit_the_ledger_close_the_ledger",
    "000_chaos_redux_61_papers_for_the_liberated",
    "000_chaos_redux_62_the_doctor_loses_his_war",
    "000_chaos_redux_63_no_pingfang_shadow",
    "000_chaos_redux_64_grain_before_fear",
    "000_chaos_redux_65_dominion_without_chains",
    "000_chaos_redux_66_redress_before_victory",
    "000_chaos_redux_67_congo_reformed",
    "000_chaos_redux_68_roads_without_camps",
    "000_chaos_redux_69_gurs_closed",
]


def trim_alpha(image: Image.Image) -> Image.Image:
    rgba = image.convert("RGBA")
    alpha = rgba.getchannel("A")
    bbox = alpha.point(lambda value: 255 if value > 8 else 0).getbbox()
    if bbox is None:
        raise RuntimeError("Generated source has no visible pixels after chroma-key removal")
    return rgba.crop(bbox)


def fit_alpha(
    source: Path,
    size: tuple[int, int],
    padding: int,
    outline_width: float,
    shadow_offset: float,
) -> Image.Image:
    scale = 4
    target_w, target_h = size
    image = trim_alpha(Image.open(source))
    maximum = (
        max(1, (target_w - padding * 2 - math.ceil(outline_width * 2)) * scale),
        max(1, (target_h - padding * 2 - math.ceil(outline_width * 2)) * scale),
    )
    ratio = min(maximum[0] / image.width, maximum[1] / image.height)
    resized = image.resize(
        (max(1, round(image.width * ratio)), max(1, round(image.height * ratio))),
        Image.Resampling.LANCZOS,
    )

    high_size = (target_w * scale, target_h * scale)
    x = (high_size[0] - resized.width) // 2
    y = (high_size[1] - resized.height) // 2
    subject_alpha = Image.new("L", high_size, 0)
    subject_alpha.paste(resized.getchannel("A"), (x, y))

    shadow = Image.new("RGBA", high_size, (0, 0, 0, 0))
    shadow_alpha = subject_alpha.filter(ImageFilter.GaussianBlur(radius=2.0 * scale))
    shadow_alpha = shadow_alpha.point(lambda value: round(value * 0.42))
    shifted_shadow = Image.new("L", high_size, 0)
    shifted_shadow.paste(
        shadow_alpha,
        (round(shadow_offset * scale), round(shadow_offset * scale)),
    )
    shadow.putalpha(shifted_shadow)

    outline_pixels = max(1, round(outline_width * scale))
    kernel = outline_pixels * 2 + 1
    outline_alpha = subject_alpha.filter(ImageFilter.MaxFilter(kernel))
    outline_alpha = outline_alpha.point(lambda value: round(value * 0.90))
    outline = Image.new("RGBA", high_size, (24, 18, 14, 255))
    outline.putalpha(outline_alpha)

    subject = Image.new("RGBA", high_size, (0, 0, 0, 0))
    subject.alpha_composite(resized, (x, y))
    canvas = Image.alpha_composite(shadow, outline)
    canvas = Image.alpha_composite(canvas, subject)
    return canvas.resize(size, Image.Resampling.LANCZOS)


def cover_opaque(source: Path, size: tuple[int, int]) -> Image.Image:
    image = Image.open(source).convert("RGB")
    return ImageOps.fit(image, size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5)).convert("RGBA")


def checker(size: tuple[int, int], tile: int = 8) -> Image.Image:
    background = Image.new("RGBA", size, (70, 70, 70, 255))
    draw = ImageDraw.Draw(background)
    colors = ((69, 69, 69, 255), (112, 112, 112, 255))
    for y in range(0, size[1], tile):
        for x in range(0, size[0], tile):
            draw.rectangle(
                (x, y, min(x + tile - 1, size[0] - 1), min(y + tile - 1, size[1] - 1)),
                fill=colors[((x // tile) + (y // tile)) % 2],
            )
    return background


def font(size: int) -> ImageFont.ImageFont:
    for path in (
        Path("C:/Windows/Fonts/segoeui.ttf"),
        Path("C:/Windows/Fonts/arial.ttf"),
    ):
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def make_contact(
    entries: list[tuple[str, Image.Image]],
    output: Path,
    columns: int,
    cell_size: tuple[int, int],
    preview_size: tuple[int, int],
) -> None:
    rows = math.ceil(len(entries) / columns)
    sheet = Image.new("RGBA", (columns * cell_size[0], rows * cell_size[1]), (29, 31, 34, 255))
    draw = ImageDraw.Draw(sheet)
    label_font = font(13)
    for index, (name, image) in enumerate(entries):
        column = index % columns
        row = index // columns
        x0 = column * cell_size[0]
        y0 = row * cell_size[1]
        draw.rectangle((x0 + 3, y0 + 3, x0 + cell_size[0] - 4, y0 + cell_size[1] - 4), outline=(92, 96, 102, 255), width=1)
        preview = image.resize(preview_size, Image.Resampling.NEAREST)
        plate = checker(preview_size, max(4, min(preview_size) // 12))
        plate.alpha_composite(preview)
        px = x0 + (cell_size[0] - preview_size[0]) // 2
        py = y0 + 9
        sheet.alpha_composite(plate, (px, py))
        label = name.removeprefix("GFX_")
        lines = textwrap.wrap(label, width=max(18, cell_size[0] // 8))[:3]
        ly = py + preview_size[1] + 7
        for line in lines:
            bbox = draw.textbbox((0, 0), line, font=label_font)
            draw.text((x0 + (cell_size[0] - (bbox[2] - bbox[0])) // 2, ly), line, font=label_font, fill=(232, 232, 232, 255))
            ly += 16
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.convert("RGB").save(output, optimize=True)


def make_achievement_contact(entries: list[tuple[str, list[Image.Image]]], output: Path) -> None:
    columns = 2
    cell_w, cell_h = 640, 180
    rows = math.ceil(len(entries) / columns)
    sheet = Image.new("RGB", (columns * cell_w, rows * cell_h), (29, 31, 34))
    draw = ImageDraw.Draw(sheet)
    label_font = font(14)
    variant_font = font(12)
    variant_labels = ("normal", "grey", "not eligible")
    for index, (name, variants) in enumerate(entries):
        column = index % columns
        row = index // columns
        x0 = column * cell_w
        y0 = row * cell_h
        draw.rectangle((x0 + 3, y0 + 3, x0 + cell_w - 4, y0 + cell_h - 4), outline=(92, 96, 102), width=1)
        label = name.removeprefix("000_chaos_redux_")
        lines = textwrap.wrap(label, width=53)[:2]
        ly = y0 + 10
        for line in lines:
            draw.text((x0 + 14, ly), line, font=label_font, fill=(240, 240, 240))
            ly += 17
        start_x = x0 + 155
        for variant_index, variant in enumerate(variants):
            preview = variant.resize((96, 96), Image.Resampling.NEAREST).convert("RGB")
            px = start_x + variant_index * 145
            py = y0 + 50
            sheet.paste(preview, (px, py))
            draw.text((px + 8, py + 102), variant_labels[variant_index], font=variant_font, fill=(210, 210, 210))
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output, optimize=True)


def convert_to_dds(png: Path, package_dds: Path, live_dds: Path, size: tuple[int, int]) -> None:
    package_dds.parent.mkdir(parents=True, exist_ok=True)
    live_dds.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            "python",
            str(CONVERTER),
            "--input",
            str(png),
            "--output",
            str(package_dds),
            "--width",
            str(size[0]),
            "--height",
            str(size[1]),
        ],
        check=True,
    )
    shutil.copy2(package_dds, live_dds)


def save_runtime_group(
    names: list[str],
    group: str,
    size: tuple[int, int],
    padding: int,
    outline: float,
    shadow: float,
) -> list[tuple[str, Image.Image]]:
    contact_entries: list[tuple[str, Image.Image]] = []
    for name in names:
        alpha_source = ALPHA / f"{name}_source.png"
        if not alpha_source.exists():
            raise FileNotFoundError(alpha_source)
        image = fit_alpha(alpha_source, size, padding, outline, shadow)
        processed = PROCESSED / group / f"{name}.png"
        processed.parent.mkdir(parents=True, exist_ok=True)
        image.save(processed, optimize=True)
        package_dds = DDS_PACKAGE / group / f"{name}.dds"
        live_dds = LIVE_INTERFACE / f"{name}.dds"
        convert_to_dds(processed, package_dds, live_dds, size)
        contact_entries.append((name, image))
    return contact_entries


def dds_header(path: Path) -> tuple[int, int, int, tuple[int, int, int, int]]:
    data = path.read_bytes()[:128]
    if len(data) != 128 or data[:4] != b"DDS ":
        raise RuntimeError(f"Invalid DDS magic/header: {path}")
    height = struct.unpack_from("<I", data, 12)[0]
    width = struct.unpack_from("<I", data, 16)[0]
    mip_count = struct.unpack_from("<I", data, 28)[0]
    masks = tuple(struct.unpack_from("<I", data, offset)[0] for offset in (92, 96, 100, 104))
    return width, height, mip_count, masks


def main() -> None:
    for directory in (PROCESSED, DDS_PACKAGE, CONTACT, LIVE_INTERFACE, LIVE_ACHIEVEMENTS):
        directory.mkdir(parents=True, exist_ok=True)

    if not RECOVERED_OVERLAY.exists():
        raise FileNotFoundError(
            "The accepted recovered achievement not-eligible overlay is missing; do not substitute a generated or manually drawn cross."
        )
    PACKAGE_OVERLAY.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(RECOVERED_OVERLAY, PACKAGE_OVERLAY)

    decisions = save_runtime_group(DECISIONS, "decisions", (32, 32), 1, 0.85, 0.75)
    ideas = save_runtime_group(IDEAS, "ideas", (64, 64), 3, 1.0, 1.0)
    projects = save_runtime_group(SPECIAL_PROJECTS, "special_projects", (161, 98), 3, 0.8, 0.8)

    overlay = Image.open(PACKAGE_OVERLAY).convert("RGBA")
    if overlay.size != (64, 64):
        raise RuntimeError(f"Achievement overlay is {overlay.size}, expected 64x64")
    if sum(1 for value in overlay.getchannel("A").getdata() if value > 0) != 939:
        raise RuntimeError("Recovered achievement overlay alpha coverage no longer matches the accepted 939-pixel source")

    achievement_contact: list[tuple[str, list[Image.Image]]] = []
    for name in ACHIEVEMENTS:
        source = SOURCE / "achievements" / f"{name}_source.png"
        if not source.exists():
            raise FileNotFoundError(source)
        normal = cover_opaque(source, (64, 64))
        grey = ImageOps.grayscale(normal.convert("RGB")).convert("RGBA")
        grey.putalpha(normal.getchannel("A"))
        not_eligible = Image.alpha_composite(grey, overlay)
        variants = [normal, grey, not_eligible]
        for suffix, image in zip(("", "_grey", "_not_eligible"), variants):
            variant_name = f"{name}{suffix}"
            processed = PROCESSED / "achievements" / f"{variant_name}.png"
            processed.parent.mkdir(parents=True, exist_ok=True)
            image.save(processed, optimize=True)
            package_dds = DDS_PACKAGE / "achievements" / f"{variant_name}.dds"
            live_dds = LIVE_ACHIEVEMENTS / f"{variant_name}.dds"
            convert_to_dds(processed, package_dds, live_dds, (64, 64))
        achievement_contact.append((name, variants))

    make_contact(decisions, CONTACT / "decision_icons_contact_sheet.png", 6, (220, 155), (96, 96))
    make_contact(ideas, CONTACT / "idea_icons_contact_sheet.png", 5, (265, 185), (112, 112))
    make_contact(projects, CONTACT / "special_project_icons_contact_sheet.png", 2, (470, 275), (322, 196))
    make_achievement_contact(achievement_contact, CONTACT / "achievement_triplets_contact_sheet.png")

    expected_masks = (0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000)
    normal_hashes: dict[str, str] = {}
    checks: list[tuple[Path, tuple[int, int], bool]] = []
    for name in DECISIONS:
        checks.append((PROCESSED / "decisions" / f"{name}.png", (32, 32), True))
    for name in IDEAS:
        checks.append((PROCESSED / "ideas" / f"{name}.png", (64, 64), True))
    for name in SPECIAL_PROJECTS:
        checks.append((PROCESSED / "special_projects" / f"{name}.png", (161, 98), True))
    for name in ACHIEVEMENTS:
        checks.append((PROCESSED / "achievements" / f"{name}.png", (64, 64), False))

    for png, expected_size, needs_transparency in checks:
        image = Image.open(png).convert("RGBA")
        if image.size != expected_size:
            raise RuntimeError(f"Wrong PNG dimensions for {png}: {image.size}, expected {expected_size}")
        alpha = image.getchannel("A")
        if needs_transparency and alpha.getextrema()[0] != 0:
            raise RuntimeError(f"Transparent UI sprite lost its transparent background: {png}")
        if not needs_transparency and alpha.getextrema() != (255, 255):
            raise RuntimeError(f"Achievement base is not fully opaque: {png}")
        digest = hashlib.sha256(image.tobytes()).hexdigest()
        if digest in normal_hashes:
            raise RuntimeError(f"Duplicate normalized artwork: {png} duplicates {normal_hashes[digest]}")
        normal_hashes[digest] = str(png)

    dds_checks: list[tuple[Path, tuple[int, int]]] = []
    for name in DECISIONS:
        dds_checks.append((LIVE_INTERFACE / f"{name}.dds", (32, 32)))
    for name in IDEAS:
        dds_checks.append((LIVE_INTERFACE / f"{name}.dds", (64, 64)))
    for name in SPECIAL_PROJECTS:
        dds_checks.append((LIVE_INTERFACE / f"{name}.dds", (161, 98)))
    for name in ACHIEVEMENTS:
        for suffix in ("", "_grey", "_not_eligible"):
            dds_checks.append((LIVE_ACHIEVEMENTS / f"{name}{suffix}.dds", (64, 64)))
    for dds, expected_size in dds_checks:
        width, height, mip_count, masks = dds_header(dds)
        if (width, height) != expected_size:
            raise RuntimeError(f"Wrong DDS dimensions for {dds}: {(width, height)}, expected {expected_size}")
        if mip_count not in (0, 1):
            raise RuntimeError(f"DDS is not one-mip: {dds} reports {mip_count}")
        if masks != expected_masks:
            raise RuntimeError(f"DDS channel masks are not BGRA8 for {dds}: {masks}")

    print(
        "processed and validated "
        f"{len(DECISIONS)} decisions, {len(IDEAS)} ideas, {len(SPECIAL_PROJECTS)} special projects, "
        f"and {len(ACHIEVEMENTS)} achievement triplets ({len(dds_checks)} live DDS files total)"
    )


if __name__ == "__main__":
    main()
