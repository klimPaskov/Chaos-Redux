"""Mechanical Stage 5 icon processing and DDS export.

This script only removes no artwork and invents no concepts. It crops the
alpha-bearing imagegen masters, fits each asset to its verified native canvas,
creates explicit disabled state variants for reward/milestone sheets, builds
review contact sheets, writes the established uncompressed 32-bit BGRA DDS
layout, and records dimension/alpha checks.
"""

from pathlib import Path
import struct

from PIL import Image, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[3]


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
        32,
        65,
        0,
        32,
        0x00FF0000,
        0x0000FF00,
        0x000000FF,
        0xFF000000,
        0x00001000,
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


def contact_sheet(items: list[tuple[str, Image.Image]], path: Path, title: str, scale: int = 3, columns: int = 4) -> None:
    font = ImageFont.load_default()
    cell_width = max(image.width for _, image in items) * scale + 28
    cell_height = max(image.height for _, image in items) * scale + 38
    rows = (len(items) + columns - 1) // columns
    sheet = Image.new("RGB", (columns * cell_width, rows * cell_height + 28), (26, 29, 28))
    draw = ImageDraw.Draw(sheet)
    draw.text((10, 7), title, fill=(225, 229, 220), font=font)
    for index, (label, image) in enumerate(items):
        col = index % columns
        row = index // columns
        x0 = col * cell_width + 12
        y0 = row * cell_height + 30
        checker = checkerboard((image.width * scale, image.height * scale), max(4, scale * 2))
        enlarged = image.resize(checker.size, Image.Resampling.NEAREST)
        checker.paste(enlarged, (0, 0), enlarged.getchannel("A"))
        sheet.paste(checker, (x0, y0))
        draw.text((x0, y0 + checker.height + 3), label, fill=(220, 222, 214), font=font)
    path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(path, "PNG")


def single_family(name: str, size: tuple[int, int], runtime: str, slugs: list[str], title: str, scale: int = 4) -> list[tuple[str, Image.Image]]:
    source_dir = ROOT / "source_png" / name
    processed_dir = ROOT / "processed_png" / name
    items: list[tuple[str, Image.Image]] = []
    for slug in slugs:
        image = fit_to_canvas(source_dir / f"{slug}_master.png", size, (size[0] - 4, size[1] - 4))
        save_png(image, processed_dir / f"{slug}.png")
        save_dds(image, REPO / runtime / f"{slug}.dds")
        items.append((slug, image))
    contact_sheet(items, ROOT / "contact_sheets" / f"{name}_contact_sheet_checker.png", title, scale)
    return items


def state_strip_family(track: str, slugs: list[str], runtime_name: str) -> tuple[list[tuple[str, Image.Image]], Image.Image]:
    source_dir = ROOT / "source_png" / "rewards"
    processed_dir = ROOT / "processed_png" / "rewards" / track
    active_items: list[tuple[str, Image.Image]] = []
    disabled_items: list[tuple[str, Image.Image]] = []
    sheet = Image.new("RGBA", (1000, 88), (0, 0, 0, 0))
    for index, slug in enumerate(slugs):
        active = fit_to_canvas(source_dir / f"{slug}_master.png", (100, 88), (96, 84))
        disabled = fit_to_canvas(source_dir / f"{slug}_master.png", (100, 88), (96, 84), muted=True)
        save_png(active, processed_dir / f"{slug}_active.png")
        save_png(disabled, processed_dir / f"{slug}_disabled.png")
        sheet.alpha_composite(active, (index * 100, 0))
        active_items.append((f"{index + 1} {slug}", active))
        disabled_items.append((f"{index + 6} {slug}", disabled))
    for index, slug in enumerate(slugs):
        disabled = fit_to_canvas(source_dir / f"{slug}_master.png", (100, 88), (96, 84), muted=True)
        sheet.alpha_composite(disabled, ((index + 5) * 100, 0))
    save_png(sheet, ROOT / "processed_png" / "rewards" / f"{track}_reward_strip.png")
    save_dds(sheet, REPO / "gfx/interface/doctrines/rewards/stage_5_chaos_warfare" / runtime_name)
    return active_items + disabled_items, sheet


def milestone_family(slugs: list[str]) -> list[tuple[str, Image.Image]]:
    source_dir = ROOT / "source_png" / "milestones"
    processed_dir = ROOT / "processed_png" / "milestones"
    items: list[tuple[str, Image.Image]] = []
    for slug in slugs:
        active = fit_to_canvas(source_dir / f"{slug}_master.png", (106, 83), (102, 79))
        disabled = fit_to_canvas(source_dir / f"{slug}_master.png", (106, 83), (102, 79), muted=True)
        save_png(active, processed_dir / f"{slug}_active.png")
        save_png(disabled, processed_dir / f"{slug}_disabled.png")
        sheet = Image.new("RGBA", (212, 83), (0, 0, 0, 0))
        sheet.alpha_composite(active, (0, 0))
        sheet.alpha_composite(disabled, (106, 0))
        save_png(sheet, processed_dir / f"{slug}_milestone_sheet.png")
        save_dds(sheet, REPO / "gfx/interface/doctrines/milestones/stage_5_chaos_warfare" / f"{slug}.dds")
        items.extend([(f"{slug} active", active), (f"{slug} disabled", disabled)])
    contact_sheet(items, ROOT / "contact_sheets" / "milestones_contact_sheet_checker.png", "Stage 5 grand-doctrine milestones: active / disabled", 3, 4)
    return items


DOCTRINE = ["doctrine_chaos_warfare", "doctrine_hazard_assault_formations", "doctrine_toxic_armored_warfare", "doctrine_contaminant_fire_support", "doctrine_integrated_cbrn_command"]
REWARD_TRACKS = {
    "hazard_assault": (["mask_discipline_reward", "contaminated_terrain_movement_reward", "chaos_assault_battalion_reward", "shock_exploitation_columns_reward", "terminal_hazard_offensive_reward"], "hazard_assault_reward_strip.dds"),
    "toxic_armor": (["sealed_crew_compartments_reward", "armored_agent_delivery_reward", "mobile_nerve_suppression_reward", "protected_breakthrough_logistics_reward", "catastrophic_shock_breakthrough_reward"], "toxic_armor_reward_strip.dds"),
    "contaminant_fire": (["projector_fire_control_cells_reward", "counterbattery_chemical_fire_reward", "chemical_shell_logistics_reward", "persistent_agent_distribution_reward", "deep_contamination_fire_plan_reward"], "contaminant_fire_reward_strip.dds"),
    "integrated_command": (["chemical_intelligence_weather_cells_reward", "protected_signal_networks_reward", "countercontamination_routing_reward", "air_surface_biological_coordination_reward", "theater_cbrn_overmatch_reward"], "integrated_command_reward_strip.dds"),
}
MILESTONES = ["protective_foundation", "delivery_integration", "theater_exploitation", "terminal_command"]
SPIRITS = ["controlled_retaliation_doctrine", "theater_contamination_doctrine", "terminal_hazard_doctrine", "mask_discipline", "hazard_assault_cadres", "contaminant_fire_coordination"]
ROLES = ["cbrn_operations_director", "civil_defence_coordinator", "chemical_logistics_inspector", "biological_security_director"]
DECISIONS = [
    "cbrn_chaos_warfare_establishment_mission", "cbrn_complete_delayed_establishment", "cbrn_claim_protective_foundation", "cbrn_claim_delivery_integration", "cbrn_claim_theater_exploitation", "cbrn_claim_terminal_command", "cbrn_hazard_assault_training", "cbrn_set_defensive_preparation_policy", "cbrn_set_retaliation_authority_policy", "cbrn_set_limited_battlefield_policy", "cbrn_set_strategic_release_policy", "cbrn_set_unrestricted_policy", "cbrn_commission_sealed_tank_crews", "cbrn_commission_persistent_shell_filling", "cbrn_commission_nerve_suppression", "cbrn_commission_biological_security_assault", "cbrn_assign_decontamination_corridor", "cbrn_convene_institutional_review"
]


if __name__ == "__main__":
    single_family("doctrine", (64, 64), "gfx/interface/doctrines/icons/stage_5_chaos_warfare", DOCTRINE, "Stage 5 doctrine adoption icons (64x64)")
    reward_items: list[tuple[str, Image.Image]] = []
    for track, (slugs, runtime_name) in REWARD_TRACKS.items():
        items, _ = state_strip_family(track, slugs, runtime_name)
        reward_items.extend(items)
    contact_sheet(reward_items, ROOT / "contact_sheets" / "rewards_contact_sheet_checker.png", "Stage 5 mastery rewards: active / disabled", 2, 5)
    milestone_family(MILESTONES)
    single_family("spirits", (45, 45), "gfx/interface/officer_corp/spirits/stage_5_chaos_warfare", SPIRITS, "Stage 5 officer-corps spirits (45x45)", 4)
    single_family("roles", (60, 68), "gfx/interface/ideas/stage_5_chaos_warfare", ROLES, "Stage 5 generic high-command roles (60x68)", 3)
    single_family("trait", (23, 33), "gfx/interface/traits/stage_5_chaos_warfare", ["trait_cbrn_operations_commander"], "Stage 5 prepared-command trait (23x33)", 5)
    single_family("decisions", (32, 32), "gfx/interface/decisions/stage_5_chaos_warfare", DECISIONS, "Stage 5 doctrine decisions and missions (32x32)", 6)
    single_family("category", (52, 40), "gfx/interface/decisions/stage_5_chaos_warfare", ["cbrn_chemical_operations_category"], "Stage 5 CBRN chemical-operations category (52x40)", 5)
    single_family("technology", (64, 64), "gfx/interface/technologies/stage_5_chaos_warfare", ["cbrn_mobile_decontamination_columns", "cbrn_chemical_air_interdiction"], "Stage 5 doctrine technology icons (64x64)", 4)
    report = []
    for png in sorted((ROOT / "processed_png").rglob("*.png")):
        image = Image.open(png).convert("RGBA")
        report.append(f"{png.relative_to(ROOT)}\t{image.width}x{image.height}\talpha={image.getchannel('A').getextrema()}\n")
    (ROOT / "notes" / "dimension_alpha_validation.tsv").write_text("path\tdimensions\talpha\n" + "".join(report), encoding="utf-8")
