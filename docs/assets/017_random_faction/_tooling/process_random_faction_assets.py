from __future__ import annotations

import math
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageOps


ROOT = Path(__file__).resolve().parents[4]
PACKAGE = ROOT / "docs" / "assets" / "017_random_faction"
SOURCE = PACKAGE / "source"
PROCESSED = PACKAGE / "processed_png"
DDS_PACKAGE = PACKAGE / "dds"
CONTACT = PACKAGE / "contact_sheets"
ANIM = PACKAGE / "animations"
ACHIEVEMENT_NOT_ELIGIBLE_OVERLAY = ROOT / ".agents" / "skills" / "chaos-redux-event-assets" / "assets" / "achievements" / "overlay.png"


def ensure_dirs() -> None:
	for path in [
		PROCESSED,
		DDS_PACKAGE,
		CONTACT,
		ROOT / "gfx" / "event_pictures" / "017_random_faction",
		ROOT / "gfx" / "interface" / "decisions" / "017_random_faction",
		ROOT / "gfx" / "interface" / "ideas" / "017_random_faction",
		ROOT / "gfx" / "interface" / "animated" / "017_random_faction",
		ROOT / "gfx" / "achievements",
		ANIM,
	]:
		path.mkdir(parents=True, exist_ok=True)


def remove_chroma(img: Image.Image) -> Image.Image:
	rgba = img.convert("RGBA")
	pixels = rgba.load()
	width, height = rgba.size
	for y in range(height):
		for x in range(width):
			r, g, b, a = pixels[x, y]
			dist = math.sqrt((r - 0) ** 2 + (g - 255) ** 2 + (b - 0) ** 2)
			if g > 150 and r < 130 and b < 130:
				if dist < 34:
					a = 0
				elif dist < 145:
					a = int(max(0, min(255, (dist - 34) / 111 * 255)))
				despill = min(g, max(r, b) + 20)
				pixels[x, y] = (r, despill, b, a)
			else:
				pixels[x, y] = (r, g, b, a)
	return rgba


def trim_alpha(img: Image.Image) -> Image.Image:
	rgba = img.convert("RGBA")
	alpha = rgba.getchannel("A")
	bbox = alpha.point(lambda p: 255 if p > 8 else 0).getbbox()
	if not bbox:
		return rgba
	return rgba.crop(bbox)


def fit_icon(source_path: Path, size: tuple[int, int], padding: int = 2) -> Image.Image:
	img = remove_chroma(Image.open(source_path))
	img = trim_alpha(img)
	canvas_w, canvas_h = size
	max_w = max(1, canvas_w - padding * 2)
	max_h = max(1, canvas_h - padding * 2)
	img.thumbnail((max_w, max_h), Image.Resampling.LANCZOS)
	canvas = Image.new("RGBA", size, (0, 0, 0, 0))
	canvas.paste(img, ((canvas_w - img.width) // 2, (canvas_h - img.height) // 2), img)
	return canvas


def cover_crop(source_path: Path, size: tuple[int, int]) -> Image.Image:
	img = Image.open(source_path).convert("RGBA")
	src_ratio = img.width / img.height
	dst_ratio = size[0] / size[1]
	if src_ratio > dst_ratio:
		new_w = int(img.height * dst_ratio)
		left = (img.width - new_w) // 2
		img = img.crop((left, 0, left + new_w, img.height))
	else:
		new_h = int(img.width / dst_ratio)
		top = (img.height - new_h) // 2
		img = img.crop((0, top, img.width, top + new_h))
	return img.resize(size, Image.Resampling.LANCZOS)


def save_png_and_dds(img: Image.Image, processed_path: Path, dds_path: Path, package_dds_path: Path | None = None) -> None:
	processed_path.parent.mkdir(parents=True, exist_ok=True)
	dds_path.parent.mkdir(parents=True, exist_ok=True)
	img.save(processed_path)
	img.save(dds_path)
	if package_dds_path is not None:
		package_dds_path.parent.mkdir(parents=True, exist_ok=True)
		shutil.copy2(dds_path, package_dds_path)


def add_not_eligible_overlay(grey: Image.Image) -> Image.Image:
	grey = grey.convert("RGBA")
	overlay = Image.open(ACHIEVEMENT_NOT_ELIGIBLE_OVERLAY).convert("RGBA")
	if overlay.size != grey.size:
		overlay = overlay.resize(grey.size, Image.Resampling.LANCZOS)
	return Image.alpha_composite(grey, overlay)


def achievement_variant(img: Image.Image, kind: str) -> Image.Image:
	if kind == "base":
		return img
	alpha = img.getchannel("A")
	grey = ImageOps.grayscale(img.convert("RGB")).convert("RGBA")
	grey = ImageEnhance.Brightness(grey).enhance(0.62)
	grey.putalpha(alpha)
	if kind == "grey":
		return grey
	return add_not_eligible_overlay(grey)


def make_contact(items: list[tuple[str, Image.Image]], out: Path, thumb: tuple[int, int] = (96, 96), cols: int = 6) -> None:
	if not items:
		return
	cell_w = thumb[0] + 20
	cell_h = thumb[1] + 36
	rows = math.ceil(len(items) / cols)
	sheet = Image.new("RGB", (cols * cell_w, rows * cell_h), (18, 18, 18))
	draw = ImageDraw.Draw(sheet)
	for idx, (label, image) in enumerate(items):
		im = image.convert("RGBA").copy()
		im.thumbnail(thumb, Image.Resampling.LANCZOS)
		x = (idx % cols) * cell_w
		y = (idx // cols) * cell_h
		sheet.paste(im, (x + (cell_w - im.width) // 2, y + 4), im)
		draw.text((x + 4, y + thumb[1] + 10), label[:18], fill=(235, 235, 235))
	out.parent.mkdir(parents=True, exist_ok=True)
	sheet.save(out)


def process_static_assets() -> list[str]:
	processed_items: list[tuple[str, Image.Image]] = []
	rows: list[str] = []

	report_assets = {
		"report_event_random_faction_cabinet": "GFX_report_event_random_faction_cabinet",
		"report_event_random_faction_border": "GFX_report_event_random_faction_border",
		"report_event_random_faction_liaison": "GFX_report_event_random_faction_liaison",
		"report_event_random_faction_regional_cascade": "GFX_report_event_random_faction_regional_cascade",
	}
	for stem, sprite in report_assets.items():
		img = cover_crop(SOURCE / f"{stem}_source.png", (210, 176))
		processed = PROCESSED / f"{stem}.png"
		runtime = ROOT / "gfx" / "event_pictures" / "017_random_faction" / f"{stem}.dds"
		package_dds = DDS_PACKAGE / f"{stem}.dds"
		save_png_and_dds(img, processed, runtime, package_dds)
		processed_items.append((stem, img))
		rows.append(f"| `{sprite}` | report image | `docs/assets/017_random_faction/source/{stem}_source.png` | `docs/assets/017_random_faction/processed_png/{stem}.png` | `gfx/event_pictures/017_random_faction/{stem}.dds` | 210x176 |")

	decision_assets = {
		"decision_category_random_faction_bloc_pressure": "GFX_decision_category_random_faction_bloc_pressure",
		"decision_random_faction_stabilize_alignment": "GFX_decision_random_faction_stabilize_alignment",
		"decision_random_faction_liaison": "GFX_decision_random_faction_liaison",
		"decision_random_faction_opposition": "GFX_decision_random_faction_opposition",
		"decision_random_faction_neutrality_council": "GFX_decision_random_faction_neutrality_council",
		"decision_random_faction_border_posts": "GFX_decision_random_faction_border_posts",
		"decision_random_faction_observers": "GFX_decision_random_faction_observers",
		"decision_random_faction_neutrality_press": "GFX_decision_random_faction_neutrality_press",
		"decision_random_faction_staff_mission": "GFX_decision_random_faction_staff_mission",
		"decision_random_faction_radio_networks": "GFX_decision_random_faction_radio_networks",
		"decision_random_faction_corridor": "GFX_decision_random_faction_corridor",
		"decision_random_faction_commitment": "GFX_decision_random_faction_commitment",
	}
	for stem, sprite in decision_assets.items():
		img = fit_icon(SOURCE / f"{stem}_source.png", (32, 32), 1)
		processed = PROCESSED / f"{stem}.png"
		runtime = ROOT / "gfx" / "interface" / "decisions" / "017_random_faction" / f"{stem}.dds"
		package_dds = DDS_PACKAGE / f"{stem}.dds"
		save_png_and_dds(img, processed, runtime, package_dds)
		processed_items.append((stem, img))
		rows.append(f"| `{sprite}` | decision icon | `docs/assets/017_random_faction/source/{stem}_source.png` | `docs/assets/017_random_faction/processed_png/{stem}.png` | `gfx/interface/decisions/017_random_faction/{stem}.dds` | 32x32 |")

	bg = "random_faction_bloc_pressure_bg"
	img = cover_crop(SOURCE / f"{bg}_source.png", (114, 101))
	save_png_and_dds(
		img,
		PROCESSED / f"{bg}.png",
		ROOT / "gfx" / "interface" / "decisions" / "017_random_faction" / f"{bg}.dds",
		DDS_PACKAGE / f"{bg}.dds",
	)
	processed_items.append((bg, img))
	rows.append(f"| `GFX_random_faction_bloc_pressure_bg` | decision category picture | `docs/assets/017_random_faction/source/{bg}_source.png` | `docs/assets/017_random_faction/processed_png/{bg}.png` | `gfx/interface/decisions/017_random_faction/{bg}.dds` | 114x101 |")

	idea_assets = {
		"idea_random_faction_alignment_shock": "GFX_idea_random_faction_alignment_shock",
		"idea_random_faction_border_pressure": "GFX_idea_random_faction_border_pressure",
		"idea_random_faction_bloc_polarization": "GFX_idea_random_faction_bloc_polarization",
		"idea_random_faction_neutrality_exhaustion": "GFX_idea_random_faction_neutrality_exhaustion",
		"idea_random_faction_liaison_mission": "GFX_idea_random_faction_liaison_mission",
	}
	for stem, sprite in idea_assets.items():
		img = fit_icon(SOURCE / f"{stem}_source.png", (64, 64), 3)
		save_png_and_dds(
			img,
			PROCESSED / f"{stem}.png",
			ROOT / "gfx" / "interface" / "ideas" / "017_random_faction" / f"{stem}.dds",
			DDS_PACKAGE / f"{stem}.dds",
		)
		processed_items.append((stem, img))
		rows.append(f"| `{sprite}` | idea icon | `docs/assets/017_random_faction/source/{stem}_source.png` | `docs/assets/017_random_faction/processed_png/{stem}.png` | `gfx/interface/ideas/017_random_faction/{stem}.dds` | 64x64 |")

	achievement_stems = [
		"017_random_faction_four_doors",
		"017_random_faction_hold_the_line",
		"017_random_faction_crowded_border",
		"017_random_faction_liaison_web",
		"017_random_faction_frontier_commitment",
		"017_random_faction_not_everyone",
	]
	not_eligible_items: list[tuple[str, Image.Image]] = []
	for stem in achievement_stems:
		base = fit_icon(SOURCE / f"{stem}_source.png", (64, 64), 3)
		for suffix, kind in [("", "base"), ("_grey", "grey"), ("_not_eligible", "not_eligible")]:
			img = achievement_variant(base, kind)
			name = f"{stem}{suffix}"
			save_png_and_dds(
				img,
				PROCESSED / f"{name}.png",
				ROOT / "gfx" / "achievements" / f"{name}.dds",
				DDS_PACKAGE / f"{name}.dds",
			)
			processed_items.append((name, img))
			if kind == "not_eligible":
				not_eligible_items.append((name, img))
		rows.append(f"| `GFX_achievement_{stem}` triplet | achievement icons | `docs/assets/017_random_faction/source/{stem}_source.png` | `docs/assets/017_random_faction/processed_png/{stem}*.png` | `gfx/achievements/{stem}*.dds` | 64x64 |")

	make_contact(processed_items, CONTACT / "event17_processed_static_contact_sheet.png", cols=6)
	make_contact(not_eligible_items, CONTACT / "achievement_not_eligible_red_cross_contact_sheet.png", cols=6)
	return rows


def process_animation(slug: str, sprite_static: str, sprite_animated: str, description: str) -> list[str]:
	frame_count = 8
	frame_size = (64, 64)
	source_atlas = SOURCE / f"{slug}_source_atlas.png"
	source_dir = ANIM / slug / "source_frames"
	processed_dir = ANIM / slug / "processed_frames"
	sheet_dir = ANIM / slug / "sheets"
	preview_dir = ANIM / slug / "previews"
	for path in [source_dir, processed_dir, sheet_dir, preview_dir]:
		path.mkdir(parents=True, exist_ok=True)
	atlas = Image.open(source_atlas).convert("RGB")
	frame_w = atlas.width // frame_count
	source_frames: list[Image.Image] = []
	processed_frames: list[Image.Image] = []
	for idx in range(frame_count):
		left = idx * frame_w
		right = (idx + 1) * frame_w if idx < frame_count - 1 else atlas.width
		src = atlas.crop((left, 0, right, atlas.height))
		source_path = source_dir / f"{slug}_{idx:03d}_source.png"
		src.save(source_path)
		source_frames.append(src)
		processed = remove_chroma(src)
		processed = trim_alpha(processed)
		processed.thumbnail((56, 56), Image.Resampling.LANCZOS)
		canvas = Image.new("RGBA", frame_size, (0, 0, 0, 0))
		canvas.paste(processed, ((64 - processed.width) // 2, (64 - processed.height) // 2), processed)
		canvas.save(processed_dir / f"{slug}_{idx:03d}.png")
		processed_frames.append(canvas)
	static = processed_frames[0]
	static.save(processed_dir / f"{slug}_static.png")
	sheet = Image.new("RGBA", (frame_size[0] * frame_count, frame_size[1]), (0, 0, 0, 0))
	for idx, frame in enumerate(processed_frames):
		sheet.paste(frame, (idx * frame_size[0], 0), frame)
	sheet_png = sheet_dir / f"{slug}_sheet.png"
	sheet.save(sheet_png)
	static_dds = ROOT / "gfx" / "interface" / "animated" / "017_random_faction" / f"{slug}_static.dds"
	sheet_dds = ROOT / "gfx" / "interface" / "animated" / "017_random_faction" / f"{slug}_sheet.dds"
	static.save(static_dds)
	sheet.save(sheet_dds)
	shutil.copy2(static_dds, DDS_PACKAGE / f"{slug}_static.dds")
	shutil.copy2(sheet_dds, DDS_PACKAGE / f"{slug}_sheet.dds")
	processed_frames[0].save(
		preview_dir / f"{slug}_preview.gif",
		save_all=True,
		append_images=processed_frames[1:] + [processed_frames[0]],
		duration=125,
		loop=0,
		disposal=2,
	)
	make_contact([(f"{idx:03d}", frame) for idx, frame in enumerate(processed_frames)], preview_dir / f"{slug}_contact.png", thumb=(64, 64), cols=8)
	brief = ANIM / slug / "brief.md"
	frame_plan = ANIM / slug / "frame_plan.md"
	brief.write_text(
		f"# {slug} Animation Brief\n\n"
		f"- In-game use: {description}\n"
		f"- Source mode: generated frame source atlas with eight separately drawn states.\n"
		f"- Static sprite: `{sprite_static}`\n"
		f"- Animated sprite: `{sprite_animated}`\n"
		f"- Frame count: 8\n"
		f"- Frame size: 64x64\n"
		f"- Sheet size: 512x64\n"
		f"- FPS: 8\n"
		f"- Looping: yes, play_on_show = yes\n"
		f"- Anchor: centered icon/emblem\n"
		f"- Final static DDS: `gfx/interface/animated/017_random_faction/{slug}_static.dds`\n"
		f"- Final sheet DDS: `gfx/interface/animated/017_random_faction/{slug}_sheet.dds`\n",
		encoding="utf-8",
	)
	frame_plan.write_text(
		"# Frame Plan\n\n"
		"| Frame | Motion state | Visual change |\n"
		"|---|---|---|\n"
		"| 000 | rest | lowest pressure state |\n"
		"| 001 | rising | pressure signal begins |\n"
		"| 002 | rising | subject tightens and light grows |\n"
		"| 003 | high | warning or seal light strengthens |\n"
		"| 004 | peak | strongest cable/pressure state |\n"
		"| 005 | easing | pressure starts falling |\n"
		"| 006 | easing | subject relaxes |\n"
		"| 007 | rest return | visually close to frame 000 for loop continuity |\n",
		encoding="utf-8",
	)
	return [
		f"| `{sprite_static}` | animated static fallback | `docs/assets/017_random_faction/source/{slug}_source_atlas.png` | `docs/assets/017_random_faction/animations/{slug}/processed_frames/{slug}_static.png` | `gfx/interface/animated/017_random_faction/{slug}_static.dds` | 64x64 |",
		f"| `{sprite_animated}` | 8-frame animation sheet | `docs/assets/017_random_faction/animations/{slug}/source_frames/` | `docs/assets/017_random_faction/animations/{slug}/sheets/{slug}_sheet.png` | `gfx/interface/animated/017_random_faction/{slug}_sheet.dds` | 512x64 |",
	]


def validate() -> list[str]:
	expected = {
		ROOT / "gfx" / "event_pictures" / "017_random_faction" / "report_event_random_faction_cabinet.dds": (210, 176),
		ROOT / "gfx" / "event_pictures" / "017_random_faction" / "report_event_random_faction_border.dds": (210, 176),
		ROOT / "gfx" / "event_pictures" / "017_random_faction" / "report_event_random_faction_liaison.dds": (210, 176),
		ROOT / "gfx" / "event_pictures" / "017_random_faction" / "report_event_random_faction_regional_cascade.dds": (210, 176),
		ROOT / "gfx" / "interface" / "decisions" / "017_random_faction" / "random_faction_bloc_pressure_bg.dds": (114, 101),
		ROOT / "gfx" / "interface" / "animated" / "017_random_faction" / "random_faction_bloc_pressure_seal_sheet.dds": (512, 64),
		ROOT / "gfx" / "interface" / "animated" / "017_random_faction" / "random_faction_border_warning_sheet.dds": (512, 64),
	}
	for path in (ROOT / "gfx" / "interface" / "decisions" / "017_random_faction").glob("decision_*.dds"):
		expected[path] = (32, 32)
	for path in (ROOT / "gfx" / "interface" / "ideas" / "017_random_faction").glob("idea_*.dds"):
		expected[path] = (64, 64)
	for path in (ROOT / "gfx" / "achievements").glob("017_random_faction*.dds"):
		expected[path] = (64, 64)
	for path in (ROOT / "gfx" / "interface" / "animated" / "017_random_faction").glob("*_static.dds"):
		expected[path] = (64, 64)
	lines = []
	for path, size in sorted(expected.items(), key=lambda x: str(x[0])):
		img = Image.open(path)
		ok = img.size == size
		lines.append(f"{path.relative_to(ROOT)}\t{img.size[0]}x{img.size[1]}\t{'OK' if ok else 'BAD'}")
		if not ok:
			raise RuntimeError(f"{path} expected {size}, got {img.size}")
	return lines


def write_docs(rows: list[str], validation: list[str]) -> None:
	manifest = PACKAGE / "manifest.md"
	handoff = PACKAGE / "gfx_handoff.md"
	row_text = "\n".join(rows)
	validation_text = "\n".join(f"- `{line}`" for line in validation)
	manifest.write_text(
		"# Event 017 Random Faction Asset Manifest\n\n"
		"Event id: `017`\n"
		"Event slug: `random_faction`\n"
		"Runtime sprite registry: `interface/017_random_faction.gfx`\n\n"
		"## Source Mode\n\n"
		"Static icons, achievements, event pictures, category picture, and animation frames use generated source art created through the built-in `$imagegen` workflow and partial Event 17 asset subagent output. The asset subagent stalled before landing final runtime DDS files, so the main implementation pass completed deterministic processing locally. Processing was limited to chroma-key alpha removal, crop/fit, exact-size resizing, contact-sheet assembly, frame-sheet assembly, GIF preview creation, and DDS export.\n\n"
		"Animation source frames come from generated source atlases with separately drawn frame states, then are sliced into source frames before deterministic processing. No final animation was made by moving, scaling, rotating, warping, blurring, recoloring, or filtering one still image.\n\n"
		"Achievement not-eligible variants copy the matching grey achievement icon and composite `.agents/skills/chaos-redux-event-assets/assets/achievements/overlay.png` on top. They do not use a red tint or red filter on the base icon.\n\n"
		"## Final Runtime Assets\n\n"
		"| Sprite or group | Type | Source | Processed PNG | Final DDS | Size |\n"
		"|---|---|---|---|---|---|\n"
		f"{row_text}\n\n"
		"## Review Files\n\n"
		"- Static contact sheet: `docs/assets/017_random_faction/contact_sheets/event17_processed_static_contact_sheet.png`\n"
		"- Not-eligible achievement red-cross overlay review sheet: `docs/assets/017_random_faction/contact_sheets/achievement_not_eligible_red_cross_contact_sheet.png`\n"
		"- Decision source contact sheet: `docs/assets/017_random_faction/contact_sheets/decision_source_contact_sheet.png`\n"
		"- Animation contact sheets and GIF previews under `docs/assets/017_random_faction/animations/*/previews/`\n"
		"- Package DDS copies under `docs/assets/017_random_faction/dds/`\n\n"
		"## Validation\n\n"
		f"{validation_text}\n\n"
		"Blocked assets: none.\n",
		encoding="utf-8",
	)
	handoff.write_text(
		"# Event 017 Random Faction GFX Handoff\n\n"
		"Runtime sprite definitions are already registered in `interface/017_random_faction.gfx` and `interface/chaosx_achievements.gfx`.\n\n"
		"## Ready Runtime Paths\n\n"
		"- Report images: `gfx/event_pictures/017_random_faction/*.dds`\n"
		"- Decision/category assets: `gfx/interface/decisions/017_random_faction/*.dds`\n"
		"- Idea icons: `gfx/interface/ideas/017_random_faction/*.dds`\n"
		"- Animated static fallbacks and sheets: `gfx/interface/animated/017_random_faction/*.dds`\n"
		"- Achievement triplets: `gfx/achievements/017_random_faction*.dds`\n\n"
		"## Animated Sprites\n\n"
		"- `GFX_random_faction_bloc_pressure_seal_static` -> `random_faction_bloc_pressure_seal_static.dds`\n"
		"- `GFX_random_faction_bloc_pressure_seal_animated` -> `random_faction_bloc_pressure_seal_sheet.dds`, 8 frames, 8 FPS, looped; visible on `random_faction_convene_neutrality_council`\n"
		"- `GFX_random_faction_border_warning_static` -> `random_faction_border_warning_static.dds`\n"
		"- `GFX_random_faction_border_warning_animated` -> `random_faction_border_warning_sheet.dds`, 8 frames, 8 FPS, looped; visible on `random_faction_reinforce_border_posts` and `random_faction_guarantee_corridor_mission`\n\n"
		"## Validation Summary\n\n"
		f"{validation_text}\n\n"
		"No missing runtime DDS paths were found by the processor.\n",
		encoding="utf-8",
	)


def main() -> None:
	ensure_dirs()
	rows = process_static_assets()
	rows += process_animation(
		"random_faction_bloc_pressure_seal",
		"GFX_random_faction_bloc_pressure_seal_static",
		"GFX_random_faction_bloc_pressure_seal_animated",
		"decision category pressure seal",
	)
	rows += process_animation(
		"random_faction_border_warning",
		"GFX_random_faction_border_warning_static",
		"GFX_random_faction_border_warning_animated",
		"low-resilience border warning emblem",
	)
	validation = validate()
	write_docs(rows, validation)
	print("\n".join(validation))


if __name__ == "__main__":
	main()
