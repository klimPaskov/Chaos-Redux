from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[4]
ASSET_ROOT = ROOT / "docs/assets/015_utopia_manifesto"
SOURCE_DIR = ASSET_ROOT / "source_png"
PROCESSED_DIR = ASSET_ROOT / "processed_png"
DDS_DIR = ASSET_ROOT / "dds"
CONTACT_DIR = ASSET_ROOT / "contact_sheets"


PALETTE = {
    "paper": (219, 199, 154, 255),
    "ink": (38, 33, 28, 255),
    "wood": (115, 72, 42, 255),
    "gold": (208, 164, 65, 255),
    "green": (70, 118, 82, 255),
    "blue": (58, 88, 132, 255),
    "red": (152, 53, 45, 255),
    "grey": (104, 107, 102, 255),
    "cream": (238, 225, 192, 255),
}


def ensure(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def save_png_dds(image: Image.Image, png_path: Path, dds_path: Path) -> None:
    ensure(png_path.parent)
    ensure(dds_path.parent)
    image.save(png_path)
    image.save(dds_path)


def font(size: int) -> ImageFont.ImageFont:
    candidates = [
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/georgia.ttf",
        "C:/Windows/Fonts/times.ttf",
    ]
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def textured_background(size: tuple[int, int], base: tuple[int, int, int, int], accent: tuple[int, int, int, int]) -> Image.Image:
    image = Image.new("RGBA", size, base)
    draw = ImageDraw.Draw(image, "RGBA")
    w, h = size
    for y in range(0, h, 4):
        tone = 10 if (y // 4) % 2 else -8
        color = tuple(max(0, min(255, c + tone)) for c in base[:3]) + (255,)
        draw.rectangle((0, y, w, y + 3), fill=color)
    for i in range(16):
        x = (i * 37) % w
        y = (i * 53) % h
        draw.ellipse((x - w // 5, y - h // 5, x + w // 4, y + h // 4), fill=accent[:3] + (22,))
    return image.filter(ImageFilter.GaussianBlur(0.3))


def draw_book(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], color=PALETTE["paper"]) -> None:
    x1, y1, x2, y2 = box
    mid = (x1 + x2) // 2
    draw.rounded_rectangle((x1, y1, mid + 2, y2), radius=4, fill=color, outline=PALETTE["ink"], width=2)
    draw.rounded_rectangle((mid - 2, y1, x2, y2), radius=4, fill=color, outline=PALETTE["ink"], width=2)
    draw.line((mid, y1 + 3, mid, y2 - 3), fill=PALETTE["wood"], width=2)
    for off in (8, 15, 22):
        draw.line((x1 + 7, y1 + off, mid - 6, y1 + off + 2), fill=PALETTE["ink"], width=1)
        draw.line((mid + 7, y1 + off + 2, x2 - 7, y1 + off), fill=PALETTE["ink"], width=1)


def draw_storehouse(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], fill=PALETTE["wood"]) -> None:
    x1, y1, x2, y2 = box
    roof_y = y1 + (y2 - y1) // 4
    draw.polygon([(x1, roof_y), ((x1 + x2) // 2, y1), (x2, roof_y)], fill=PALETTE["red"], outline=PALETTE["ink"])
    draw.rectangle((x1 + 4, roof_y, x2 - 4, y2), fill=fill, outline=PALETTE["ink"], width=2)
    draw.rectangle(((x1 + x2) // 2 - 5, y2 - 16, (x1 + x2) // 2 + 5, y2), fill=PALETTE["ink"])
    for x in range(x1 + 9, x2 - 8, 14):
        draw.ellipse((x, roof_y + 8, x + 7, roof_y + 15), fill=PALETTE["gold"], outline=PALETTE["ink"])


def draw_scales(draw: ImageDraw.ImageDraw, center: tuple[int, int], scale: int, color=PALETTE["gold"]) -> None:
    x, y = center
    draw.line((x, y - scale, x, y + scale), fill=PALETTE["ink"], width=2)
    draw.line((x - scale, y - 4, x + scale, y - 4), fill=PALETTE["ink"], width=2)
    for side in (-1, 1):
        cx = x + side * scale
        draw.line((cx, y - 4, cx - side * 5, y + 10), fill=PALETTE["ink"], width=1)
        draw.line((cx, y - 4, cx + side * 5, y + 10), fill=PALETTE["ink"], width=1)
        draw.arc((cx - 9, y + 7, cx + 9, y + 21), 0, 180, fill=color, width=3)
    draw.polygon([(x - 8, y + scale), (x + 8, y + scale), (x + 12, y + scale + 8), (x - 12, y + scale + 8)], fill=color, outline=PALETTE["ink"])


def draw_tool_ring(draw: ImageDraw.ImageDraw, center: tuple[int, int], radius: int) -> None:
    x, y = center
    for i, col in enumerate([PALETTE["gold"], PALETTE["green"], PALETTE["blue"], PALETTE["red"], PALETTE["grey"]]):
        ang = math.tau * i / 5 - math.pi / 2
        ex = x + int(math.cos(ang) * radius)
        ey = y + int(math.sin(ang) * radius)
        draw.line((x, y, ex, ey), fill=col, width=4)
        draw.ellipse((ex - 5, ey - 5, ex + 5, ey + 5), fill=col, outline=PALETTE["ink"])
    draw.ellipse((x - 9, y - 9, x + 9, y + 9), fill=PALETTE["paper"], outline=PALETTE["ink"], width=2)


def draw_boundary(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], hard: bool = False) -> None:
    x1, y1, x2, y2 = box
    stake = PALETTE["red"] if hard else PALETTE["wood"]
    draw.line((x1 + 8, y2 - 8, x2 - 8, y1 + 8), fill=PALETTE["ink"], width=2)
    for t in (0.25, 0.5, 0.75):
        x = int(x1 + (x2 - x1) * t)
        y = int(y2 - (y2 - y1) * t)
        draw.rectangle((x - 3, y - 12, x + 3, y + 12), fill=stake, outline=PALETTE["ink"])
    if hard:
        draw.polygon([(x2 - 16, y1 + 5), (x2 - 4, y1 + 12), (x2 - 16, y1 + 19)], fill=PALETTE["red"], outline=PALETTE["ink"])


def draw_ship(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int]) -> None:
    x1, y1, x2, y2 = box
    draw.polygon([(x1, y2 - 16), (x2, y2 - 16), (x2 - 10, y2 - 4), (x1 + 10, y2 - 4)], fill=PALETTE["blue"], outline=PALETTE["ink"])
    mast_x = (x1 + x2) // 2
    draw.line((mast_x, y1 + 4, mast_x, y2 - 16), fill=PALETTE["ink"], width=2)
    draw.polygon([(mast_x + 2, y1 + 8), (mast_x + 2, y2 - 22), (x2 - 8, y2 - 22)], fill=PALETTE["cream"], outline=PALETTE["ink"])
    for i in range(3):
        draw.arc((x1 + i * 16, y2 - 9, x1 + i * 16 + 24, y2 + 5), 0, 180, fill=PALETTE["cream"], width=2)


def draw_guard(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int]) -> None:
    x1, y1, x2, y2 = box
    cx = (x1 + x2) // 2
    draw.polygon([(cx, y1 + 4), (x2 - 8, y1 + 16), (x2 - 13, y2 - 8), (cx, y2 - 2), (x1 + 13, y2 - 8), (x1 + 8, y1 + 16)], fill=PALETTE["blue"], outline=PALETTE["ink"])
    draw.line((cx, y1 + 12, cx, y2 - 8), fill=PALETTE["paper"], width=3)
    draw.line((x1 + 13, y1 + 21, x2 - 13, y1 + 21), fill=PALETTE["paper"], width=3)


def icon_canvas(size: tuple[int, int], family: str) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    bases = {
        "human": (116, 88, 61, 255),
        "store": (92, 93, 66, 255),
        "guild": (82, 96, 108, 255),
        "island": (50, 84, 120, 255),
        "need": (115, 71, 62, 255),
        "military": (67, 83, 71, 255),
        "league": (67, 98, 91, 255),
        "late": (83, 74, 104, 255),
    }
    base = bases.get(family, (91, 82, 70, 255))
    image = textured_background(size, base, PALETTE["gold"])
    draw = ImageDraw.Draw(image, "RGBA")
    draw.rounded_rectangle((1, 1, size[0] - 2, size[1] - 2), radius=max(4, min(size) // 10), outline=PALETTE["ink"], width=2)
    return image, draw


def draw_motif(draw: ImageDraw.ImageDraw, size: tuple[int, int], motif: str, label: str | None = None) -> None:
    w, h = size
    box = (int(w * 0.18), int(h * 0.18), int(w * 0.82), int(h * 0.82))
    if motif == "book":
        draw_book(draw, box)
    elif motif == "store":
        draw_storehouse(draw, box)
    elif motif == "scales":
        draw_scales(draw, (w // 2, h // 2), min(w, h) // 4)
    elif motif == "tools":
        draw_tool_ring(draw, (w // 2, h // 2), min(w, h) // 3)
    elif motif == "boundary":
        draw_boundary(draw, box)
    elif motif == "hard_boundary":
        draw_boundary(draw, box, hard=True)
    elif motif == "ship":
        draw_ship(draw, box)
    elif motif == "guard":
        draw_guard(draw, box)
    elif motif == "route":
        draw.line((w * 0.18, h * 0.68, w * 0.82, h * 0.35), fill=PALETTE["paper"], width=max(3, w // 18))
        for x, y in [(0.25, 0.62), (0.45, 0.52), (0.65, 0.43), (0.8, 0.35)]:
            draw.ellipse((w * x - 4, h * y - 4, w * x + 4, h * y + 4), fill=PALETTE["gold"], outline=PALETTE["ink"])
    elif motif == "council":
        for i in range(6):
            ang = math.tau * i / 6
            x = w // 2 + int(math.cos(ang) * w * 0.26)
            y = h // 2 + int(math.sin(ang) * h * 0.25)
            draw.ellipse((x - 5, y - 5, x + 5, y + 5), fill=PALETTE["paper"], outline=PALETTE["ink"])
        draw.ellipse((w * 0.38, h * 0.38, w * 0.62, h * 0.62), fill=PALETTE["gold"], outline=PALETTE["ink"])
    else:
        draw.ellipse((w * 0.24, h * 0.24, w * 0.76, h * 0.76), fill=PALETTE["paper"], outline=PALETTE["ink"], width=2)
    if label:
        fnt = font(max(8, min(w, h) // 5))
        bbox = draw.textbbox((0, 0), label, font=fnt)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        draw.rounded_rectangle((w - tw - 8, h - th - 7, w - 3, h - 3), radius=3, fill=(20, 20, 20, 180))
        draw.text((w - tw - 6, h - th - 6), label, font=fnt, fill=PALETTE["cream"])


FOCUS_MOTIFS = {
    "manifesto": ("human", "book", "I"),
    "translation": ("human", "book", "T"),
    "household_census": ("human", "council", "C"),
    "reading_halls": ("human", "book", "R"),
    "storehouse": ("store", "store", "S"),
    "useful_arts": ("guild", "tools", "A"),
    "need": ("need", "scales", "N"),
    "boundaries": ("need", "boundary", "B"),
    "four_readings": ("human", "book", "4"),
    "living_humanism": ("human", "council", "H"),
    "councils": ("human", "council", None),
    "six_hours": ("human", "tools", "6"),
    "healers": ("human", "scales", "+"),
    "assemblies": ("human", "council", "A"),
    "mercy": ("human", "book", "M"),
    "renunciation": ("need", "boundary", "X"),
    "living_commonwealth": ("human", "council", "L"),
    "store_state": ("store", "store", "ST"),
    "grain": ("store", "store", "G"),
    "measures": ("store", "scales", "M"),
    "trains": ("store", "route", "R"),
    "surplus": ("store", "store", "+"),
    "auditors": ("store", "scales", "A"),
    "crisis_rations": ("store", "store", "!"),
    "guild_commonwealth": ("guild", "tools", "G"),
    "guilds": ("guild", "tools", None),
    "apprentices": ("guild", "tools", "A"),
    "second_trade": ("guild", "tools", "2"),
    "workshops": ("guild", "tools", "W"),
    "engineers": ("guild", "tools", "E"),
    "common_patents": ("guild", "book", "P"),
    "guild_charter": ("guild", "book", "G"),
    "island_discipline": ("island", "ship", "I"),
    "harbors": ("island", "ship", "H"),
    "convoys": ("island", "ship", "C"),
    "sea_watch": ("island", "guard", "S"),
    "ring_councils": ("island", "council", "R"),
    "shore_engineers": ("island", "tools", "E"),
    "lighthouse": ("island", "ship", "L"),
    "island_compact": ("island", "council", "I"),
    "storehouse_spine": ("store", "route", "S"),
    "bread_boards": ("store", "council", "B"),
    "granaries": ("store", "store", "G"),
    "routes": ("store", "route", None),
    "foreign_aid": ("league", "ship", "A"),
    "store_network": ("store", "route", "N"),
    "vocation_balance": ("guild", "tools", "V"),
    "labor_register": ("guild", "book", "L"),
    "learning": ("guild", "book", "L"),
    "rotation": ("guild", "route", "R"),
    "colleges": ("guild", "book", "C"),
    "healers_engineers": ("guild", "tools", "+"),
    "all_useful_arts": ("guild", "tools", "5"),
    "just_war": ("military", "scales", "J"),
    "household_guard": ("military", "guard", "H"),
    "defensive_drill": ("military", "guard", "D"),
    "no_glory": ("military", "book", "N"),
    "reinforcement_paths": ("military", "route", "R"),
    "guard_ledger": ("military", "guard", "L"),
    "need_not_conquest": ("military", "scales", "N"),
    "neighbors": ("league", "council", "N"),
    "arbitration_tables": ("league", "scales", "A"),
    "storehouses_abroad": ("league", "store", "A"),
    "friends": ("league", "council", "F"),
    "league": ("league", "council", "L"),
    "aid_corridors": ("league", "route", "A"),
    "observers": ("league", "book", "O"),
    "no_secret_empire": ("league", "scales", "N"),
    "needful_land": ("need", "boundary", "N"),
    "prove_need": ("need", "scales", "P"),
    "settlement_charter": ("need", "book", "S"),
    "mark_districts": ("need", "hard_boundary", "M"),
    "registers": ("need", "book", "R"),
    "local_storehouses": ("need", "store", "L"),
    "common_administration": ("need", "council", "A"),
    "integration": ("need", "route", "I"),
    "compliance_core": ("need", "scales", "C"),
    "needful_land_commission": ("need", "scales", "C"),
    "coastal_routes": ("island", "ship", "C"),
    "landlocked_stores": ("store", "route", "L"),
    "subject_ledger": ("league", "book", "S"),
    "tiny_ledger": ("human", "book", "T"),
    "adaptation": ("late", "route", "A"),
    "marked_bounds": ("need", "hard_boundary", "B"),
    "survey_idle_soil": ("need", "hard_boundary", "S"),
    "hard_maps": ("need", "hard_boundary", "H"),
    "boundary_posts": ("need", "hard_boundary", "P"),
    "guarded_settlement": ("military", "guard", "G"),
    "necessary_war": ("military", "scales", "!"),
    "marked_wardens": ("military", "guard", "M"),
    "bounds_state": ("need", "hard_boundary", "S"),
    "no_idle_acre": ("need", "hard_boundary", "A"),
    "paper_utopia": ("late", "book", "P"),
    "new_utopia": ("late", "store", "N"),
    "necessary_commonwealth": ("late", "guard", "C"),
    "marked_bounds_state": ("late", "hard_boundary", "M"),
    "proclamation": ("late", "book", "!"),
    "manifesto_survives": ("late", "book", "V"),
}


IDEA_SPRITES = [
    "idea_utopia_found_manifesto",
    "idea_utopia_common_stores_unproven",
    "idea_utopia_vocation_confusion",
    "idea_utopia_foreign_laughter",
    "idea_utopia_living_humanism",
    "idea_utopia_store_state",
    "idea_utopia_guilds",
    "idea_utopia_island_discipline",
    "idea_utopia_marked_bounds",
    "idea_utopia_public_storehouses",
    "idea_utopia_useful_arts",
    "idea_utopia_household_guard",
    "idea_utopia_arbitration_tables",
    "idea_utopia_common_administration",
    "idea_utopia_needful_land",
    "idea_utopia_league_of_need",
    "idea_utopia_new_utopia",
    "idea_utopia_necessary_commonwealth",
    "idea_utopia_paper_utopia",
]


DECISION_SPRITES = [
    "decision_category_utopia_ledger",
    "decision_category_utopia_league",
    "decision_utopia_household_census",
    "decision_utopia_common_storehouse",
    "decision_utopia_storehouse_audit",
    "decision_utopia_open_stores",
    "decision_utopia_collect_petitions",
    "decision_utopia_fund_apprenticeships",
    "decision_utopia_urgent_service",
    "decision_utopia_rural_rotation",
    "decision_utopia_household_guard",
    "decision_utopia_guard_shore",
    "decision_utopia_just_cause_review",
    "decision_utopia_boundary_arbitration",
    "decision_utopia_mark_needed_district",
    "decision_utopia_settlement_charter",
    "decision_utopia_common_administration",
    "decision_utopia_local_store",
    "decision_utopia_local_households",
    "decision_utopia_boundary_wardens",
    "decision_utopia_storehouse_aid",
    "decision_utopia_send_magistrates",
    "decision_utopia_recognize_friend",
    "decision_utopia_league_aid_corridor",
    "decision_utopia_renunciation_vote",
]


ACHIEVEMENTS = [
    "015_utopia_new_utopia",
    "015_utopia_need_not_greed",
    "015_utopia_friends_without_treaties",
    "015_utopia_six_hour_country",
    "015_utopia_inland_island",
    "015_utopia_no_bloody_glory",
    "015_utopia_storehouses_abroad",
    "015_utopia_marked_bounds_survivor",
    "015_utopia_renounced_bounds",
    "015_utopia_all_useful_arts",
    "015_utopia_league_of_need",
    "015_utopia_paper_no_more",
]


def motif_for_name(name: str) -> tuple[str, str, str | None]:
    stem = name.replace("goal_utopia_", "").replace("decision_utopia_", "").replace("decision_category_utopia_", "")
    if stem in FOCUS_MOTIFS:
        return FOCUS_MOTIFS[stem]
    if "ledger" in stem or "manifesto" in stem or "paper" in stem:
        return ("human", "book", None)
    if "store" in stem or "surplus" in stem or "aid" in stem:
        return ("store", "store", None)
    if "guild" in stem or "art" in stem or "vocation" in stem or "apprentice" in stem:
        return ("guild", "tools", None)
    if "shore" in stem or "convoy" in stem or "harbor" in stem:
        return ("island", "ship", None)
    if "bound" in stem or "district" in stem or "land" in stem:
        return ("need", "hard_boundary", None)
    if "guard" in stem or "war" in stem:
        return ("military", "guard", None)
    if "league" in stem or "friend" in stem or "magistrate" in stem:
        return ("league", "council", None)
    return ("late", "book", None)


def make_icon(name: str, size: tuple[int, int], output_dir: Path) -> Path:
    family, motif, label = motif_for_name(name)
    image, draw = icon_canvas(size, family)
    draw_motif(draw, size, motif, label)
    source_path = SOURCE_DIR / f"{name}_source.png"
    processed_path = PROCESSED_DIR / f"{name}.png"
    dds_path = DDS_DIR / f"{name}.dds"
    final_path = output_dir / f"{name}.dds"
    save_png_dds(image, source_path, dds_path)
    save_png_dds(image, processed_path, final_path)
    return processed_path


def contact(paths: list[Path], path: Path, thumb: tuple[int, int], columns: int = 6) -> None:
    if not paths:
        return
    ensure(path.parent)
    rows = math.ceil(len(paths) / columns)
    label_h = 14
    sheet = Image.new("RGBA", (columns * thumb[0], rows * (thumb[1] + label_h)), (28, 28, 28, 255))
    draw = ImageDraw.Draw(sheet)
    fnt = ImageFont.load_default()
    for idx, img_path in enumerate(paths):
        img = Image.open(img_path).convert("RGBA")
        img.thumbnail(thumb, Image.Resampling.LANCZOS)
        x = idx % columns * thumb[0]
        y = idx // columns * (thumb[1] + label_h)
        sheet.alpha_composite(img, (x + (thumb[0] - img.width) // 2, y + (thumb[1] - img.height) // 2))
        draw.text((x + 2, y + thumb[1]), img_path.stem[:22], font=fnt, fill=(230, 230, 220, 255))
    sheet.save(path)


def make_achievement(name: str) -> Path:
    family, motif, label = motif_for_name(name.replace("015_", "goal_"))
    image, draw = icon_canvas((64, 64), family)
    draw_motif(draw, (64, 64), motif, label)
    draw.ellipse((4, 4, 60, 60), outline=PALETTE["gold"], width=3)
    source_path = SOURCE_DIR / f"{name}_source.png"
    source_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(source_path)
    variants = {
        name: image,
        f"{name}_grey": ImageOps.grayscale(image).convert("RGBA"),
    }
    not_eligible = variants[f"{name}_grey"].copy()
    nd = ImageDraw.Draw(not_eligible, "RGBA")
    nd.line((13, 13, 51, 51), fill=(190, 45, 45, 255), width=6)
    nd.line((51, 13, 13, 51), fill=(190, 45, 45, 255), width=6)
    variants[f"{name}_not_eligible"] = not_eligible
    processed_path = PROCESSED_DIR / f"{name}.png"
    for variant, variant_image in variants.items():
        save_png_dds(variant_image, PROCESSED_DIR / f"{variant}.png", ROOT / "gfx/achievements" / f"{variant}.dds")
        save_png_dds(variant_image, DDS_DIR / f"{variant}.dds", DDS_DIR / f"{variant}.dds")
    return processed_path


def make_animation(asset: str, frame_size: tuple[int, int], frames: int, motif: str, family: str, output_dir: Path, fps: int = 8) -> None:
    anim_root = ASSET_ROOT / "animations" / asset
    source_dir = anim_root / "source_frames"
    processed_dir = anim_root / "processed_frames"
    sheet_dir = anim_root / "sheets"
    preview_dir = anim_root / "previews"
    for directory in (source_dir, processed_dir, sheet_dir, preview_dir):
        ensure(directory)
    processed_images: list[Image.Image] = []
    processed_paths: list[Path] = []
    for idx in range(frames):
        image, draw = icon_canvas(frame_size, family)
        pulse = idx / max(1, frames - 1)
        if asset == "utopia_storehouse_fill":
            draw_storehouse(draw, (2, 1, frame_size[0] - 2, frame_size[1] - 2), fill=PALETTE["wood"])
            fill_w = int((frame_size[0] - 8) * pulse)
            draw.rectangle((4, frame_size[1] - 6, 4 + fill_w, frame_size[1] - 3), fill=PALETTE["gold"])
        else:
            draw_motif(draw, frame_size, motif, None)
            glow = int(40 + 95 * math.sin(math.tau * pulse))
            draw.ellipse((4, 4, frame_size[0] - 4, frame_size[1] - 4), outline=PALETTE["gold"][:3] + (glow,), width=3)
            if "bounds" in asset or "overreach" in asset:
                draw.line((8, frame_size[1] - 10, frame_size[0] - 8, 10), fill=PALETTE["red"][:3] + (120 + idx * 8,), width=3)
        source_path = source_dir / f"{asset}_{idx:03d}_source.png"
        processed_path = processed_dir / f"{asset}_{idx:03d}.png"
        image.save(source_path)
        image.save(processed_path)
        processed_images.append(image)
        processed_paths.append(processed_path)
    sheet = Image.new("RGBA", (frame_size[0] * frames, frame_size[1]), (0, 0, 0, 0))
    for idx, image in enumerate(processed_images):
        sheet.alpha_composite(image, (idx * frame_size[0], 0))
    save_png_dds(sheet, sheet_dir / f"{asset}_sheet.png", output_dir / f"{asset}_sheet.dds")
    save_png_dds(processed_images[0], PROCESSED_DIR / f"{asset}_static.png", output_dir / f"{asset}_static.dds")
    sheet.save(DDS_DIR / f"{asset}_sheet.dds")
    processed_images[0].save(DDS_DIR / f"{asset}_static.dds")
    processed_images[0].save(
        preview_dir / f"{asset}_preview.gif",
        save_all=True,
        append_images=processed_images[1:],
        duration=int(1000 / fps),
        loop=0,
        disposal=2,
    )
    contact(processed_paths, preview_dir / f"{asset}_contact.png", frame_size, columns=min(frames, 5))


def main() -> None:
    focus_names = sorted({line.strip().split()[2].replace("GFX_", "") for line in (ROOT / "common/national_focus/015_utopia_manifesto_focus_tree.txt").read_text().splitlines() if "icon = GFX_goal_" in line})
    focus_paths = [make_icon(name, (94, 86), ROOT / "gfx/interface/goals/015_utopia_manifesto") for name in focus_names]
    idea_paths = [make_icon(name, (64, 64), ROOT / "gfx/interface/ideas/015_utopia_manifesto") for name in IDEA_SPRITES]
    decision_paths = [make_icon(name, (32, 32), ROOT / "gfx/interface/decisions/015_utopia_manifesto") for name in DECISION_SPRITES]
    achievement_paths = [make_achievement(name) for name in ACHIEVEMENTS]
    make_animation("utopia_overreach_warning", (64, 64), 8, "hard_boundary", "need", ROOT / "gfx/interface/utopia_manifesto")
    make_animation("utopia_storehouse_fill", (64, 16), 8, "store", "store", ROOT / "gfx/interface/utopia_manifesto")
    make_animation("utopia_new_utopia_seal", (96, 96), 10, "store", "late", ROOT / "gfx/interface/utopia_manifesto")
    make_animation("utopia_marked_bounds_seal", (96, 96), 10, "hard_boundary", "need", ROOT / "gfx/interface/utopia_manifesto")
    contact(focus_paths, CONTACT_DIR / "focus_complete_contact.png", (94, 86), columns=6)
    contact(idea_paths, CONTACT_DIR / "ideas_complete_contact.png", (64, 64), columns=6)
    contact(decision_paths, CONTACT_DIR / "decisions_complete_contact.png", (32, 32), columns=8)
    contact(achievement_paths, CONTACT_DIR / "achievements_complete_contact.png", (64, 64), columns=6)


if __name__ == "__main__":
    main()
