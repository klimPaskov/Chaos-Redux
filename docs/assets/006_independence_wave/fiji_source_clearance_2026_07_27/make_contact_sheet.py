from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).parent
OUT = ROOT / "fiji_portrait_source_contact_sheet.png"
CANVAS = (1420, 1260)
BG = (238, 238, 238)
TILE = (430, 475)
GAP = 25
FONT = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 22)
SMALL = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 18)


def fit(path: Path, size: tuple[int, int]) -> Image.Image:

	with Image.open(path) as opened:
		opened.load()
		image = opened.convert("RGB")
	return ImageOps.contain(image, size, method=Image.Resampling.LANCZOS)


sheet = Image.new("RGB", CANVAS, BG)
draw = ImageDraw.Draw(sheet)
draw.text((25, 18), "IW-177 Fiji source clearance — candidate comparison", fill=(0, 0, 0), font=FONT)
draw.text((25, 48), "Sources and exact crops are evidence; 156x210 previews are non-runtime review outputs.", fill=(40, 40, 40), font=SMALL)

rows = [
	(
		"Ratu Sir Lala Sukuna — source 2520x3128, circa 1940s",
		"ratu_sir_lala_sukuna_source.jpg",
		"ratu_sir_lala_sukuna_crop.png",
		"ratu_sir_lala_sukuna_preview_156x210.png",
	),
	(
		"Vishnu Deo — source 277x543, 1929",
		"vishnu_deo_fiji_source.jpg",
		"vishnu_deo_fiji_crop.png",
		"vishnu_deo_fiji_preview_156x210.png",
	),
]

for row_index, (label, source_name, crop_name, preview_name) in enumerate(rows):
	top = 90 + row_index * 580
	draw.text((25, top), label, fill=(0, 0, 0), font=FONT)
	for column, (caption, filename) in enumerate(
		[("unchanged source", source_name), ("exact Pillow crop", crop_name), ("156x210 review preview", preview_name)]
	):
		left = 25 + column * (TILE[0] + GAP)
		draw.text((left, top + 34), caption, fill=(40, 40, 40), font=SMALL)
		panel = (left, top + 62, left + TILE[0], top + 62 + TILE[1])
		draw.rectangle(panel, fill=(255, 255, 255), outline=(130, 130, 130), width=2)
		image = fit(ROOT / filename, (TILE[0] - 20, TILE[1] - 20))
		paste_left = panel[0] + (TILE[0] - image.width) // 2
		paste_top = panel[1] + (TILE[1] - image.height) // 2
		sheet.paste(image, (paste_left, paste_top))

sheet.save(OUT, format="PNG", optimize=False, compress_level=9)
print(OUT)
