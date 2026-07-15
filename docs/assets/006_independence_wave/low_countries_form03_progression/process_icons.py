#!/usr/bin/env python3
"""Mechanically finish the ImageGen-authored FORM-03 icon sources.

The script starts from the retained full-resolution chroma-keyed alpha PNGs.
It only crops transparent bounds, resizes to the locked canvas, and adds the
dark silhouette/soft shadow treatment required for small HOI4 UI assets.  It
does not draw, replace, trace, or otherwise originate any icon artwork.
"""

from __future__ import annotations

from pathlib import Path
import textwrap

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parent
PROCESSED = ROOT / "processed_png"
CONTACT_SHEETS = ROOT / "contact_sheets"

FAMILY_SPECS = {
	"goal_": {
		"canvas": (94, 86),
		"content": (88, 80),
		"outline_alpha": 132,
		"shadow_alpha": 58,
		"shadow_blur": 0.75,
	},
	"idea_": {
		"canvas": (64, 64),
		"content": (58, 58),
		"outline_alpha": 144,
		"shadow_alpha": 62,
		"shadow_blur": 0.70,
	},
	"decision_": {
		"canvas": (32, 32),
		"content": (28, 28),
		"outline_alpha": 168,
		"shadow_alpha": 68,
		"shadow_blur": 0.55,
	},
}


def family_spec(name: str) -> dict[str, object]:
	for prefix, spec in FAMILY_SPECS.items():
		if name.startswith(prefix):
			return spec
	raise ValueError(f"Unrecognized FORM-03 icon family: {name}")


def finish_icon(keyed_path: Path) -> tuple[Path, tuple[int, int, int, int]]:
	name = keyed_path.stem.removesuffix("_keyed")
	spec = family_spec(name)
	canvas_w, canvas_h = spec["canvas"]
	content_w, content_h = spec["content"]

	image = Image.open(keyed_path).convert("RGBA")
	alpha = image.getchannel("A")
	bbox = alpha.getbbox()
	if bbox is None:
		raise ValueError(f"No visible subject after chroma removal: {keyed_path}")

	cropped = image.crop(bbox)
	scale = min(content_w / cropped.width, content_h / cropped.height)
	resized_w = max(1, round(cropped.width * scale))
	resized_h = max(1, round(cropped.height * scale))
	resized = cropped.resize((resized_w, resized_h), Image.Resampling.LANCZOS)

	# Re-trim the antialiased resize before centering to prevent a source-side
	# transparent gutter from shifting the visible silhouette.
	resized_bbox = resized.getchannel("A").getbbox()
	if resized_bbox is None:
		raise ValueError(f"No visible subject after resize: {keyed_path}")
	resized = resized.crop(resized_bbox)

	x = (canvas_w - resized.width) // 2
	y = (canvas_h - resized.height) // 2
	mask = resized.getchannel("A")
	dilated = mask.filter(ImageFilter.MaxFilter(3))
	outline_mask = ImageChops.subtract(dilated, mask).point(
		lambda value: value * spec["outline_alpha"] // 255
	)
	shadow_mask = dilated.filter(ImageFilter.GaussianBlur(spec["shadow_blur"])).point(
		lambda value: value * spec["shadow_alpha"] // 255
	)

	canvas = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
	shadow = Image.new("RGBA", (resized.width, resized.height), (5, 8, 12, 0))
	shadow.putalpha(shadow_mask)
	canvas.alpha_composite(shadow, (min(canvas_w - resized.width, x + 1), min(canvas_h - resized.height, y + 1)))

	outline = Image.new("RGBA", (resized.width, resized.height), (8, 11, 16, 0))
	outline.putalpha(outline_mask)
	canvas.alpha_composite(outline, (x, y))
	canvas.alpha_composite(resized, (x, y))

	output_path = PROCESSED / f"{name}.png"
	canvas.save(output_path, optimize=True)
	return output_path, canvas.getchannel("A").getbbox() or (0, 0, 0, 0)


def review_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
	font_path = Path("C:/Windows/Fonts/segoeui.ttf")
	if font_path.exists():
		return ImageFont.truetype(str(font_path), size=size)
	return ImageFont.load_default()


def checker(width: int, height: int, cell: int) -> Image.Image:
	image = Image.new("RGBA", (width, height), (164, 164, 164, 255))
	draw = ImageDraw.Draw(image)
	for y in range(0, height, cell):
		for x in range(0, width, cell):
			if (x // cell + y // cell) % 2:
				draw.rectangle((x, y, min(width - 1, x + cell - 1), min(height - 1, y + cell - 1)), fill=(106, 106, 106, 255))
	return image


def make_contact_sheet(prefix: str, title: str, scale: int) -> None:
	paths = sorted(path for path in PROCESSED.glob(f"{prefix}*.png") if not path.stem.endswith("_keyed"))
	if len(paths) != 6:
		raise ValueError(f"Expected six {prefix} icons, found {len(paths)}")

	font = review_font(14)
	title_font = review_font(20)
	for mode, columns, display_scale in (("native", 3, 1), ("enlarged_nearest", 2, scale)):
		with Image.open(paths[0]) as sample:
			icon_w, icon_h = sample.size
		display_w, display_h = icon_w * display_scale, icon_h * display_scale
		cell_w = max(340 if mode == "native" else 420, display_w + 60)
		label_h = 66
		cell_h = display_h + label_h + 26
		rows = (len(paths) + columns - 1) // columns
		sheet = Image.new("RGBA", (columns * cell_w, 46 + rows * cell_h), (24, 27, 31, 255))
		draw = ImageDraw.Draw(sheet)
		draw.text((18, 12), f"{title} — {mode.replace('_', ' ')}", fill=(236, 233, 222, 255), font=title_font)

		for index, path in enumerate(paths):
			column = index % columns
			row = index // columns
			cell_x = column * cell_w
			cell_y = 46 + row * cell_h
			with Image.open(path) as icon:
				icon = icon.convert("RGBA")
				if display_scale != 1:
					icon = icon.resize((display_w, display_h), Image.Resampling.NEAREST)
			background = checker(display_w, display_h, max(2, 4 * display_scale))
			background.alpha_composite(icon)
			x = cell_x + (cell_w - display_w) // 2
			y = cell_y + 8
			sheet.alpha_composite(background, (x, y))
			draw.rectangle((x - 1, y - 1, x + display_w, y + display_h), outline=(72, 78, 84, 255), width=1)
			label = path.stem
			wrapped = textwrap.wrap(label, width=45 if mode == "native" else 54)
			draw.multiline_text((cell_x + 12, y + display_h + 10), "\n".join(wrapped), fill=(226, 224, 216, 255), font=font, spacing=2)

		output = CONTACT_SHEETS / f"form03_{prefix.rstrip('_')}_{mode}.png"
		sheet.convert("RGB").save(output, optimize=True)


def main() -> int:
	keyed_paths = sorted(PROCESSED.glob("*_keyed.png"))
	if not keyed_paths:
		raise SystemExit("No keyed FORM-03 PNGs found")

	for keyed_path in keyed_paths:
		output_path, bbox = finish_icon(keyed_path)
		with Image.open(output_path) as output:
			print(f"{output_path.name}: {output.size[0]}x{output.size[1]}, alpha_bbox={bbox}")

	CONTACT_SHEETS.mkdir(parents=True, exist_ok=True)
	make_contact_sheet("goal_", "FORM-03 national focus icons", scale=4)
	make_contact_sheet("idea_", "FORM-03 idea / national-spirit icons", scale=4)
	make_contact_sheet("decision_", "FORM-03 decision-family icons", scale=8)
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
