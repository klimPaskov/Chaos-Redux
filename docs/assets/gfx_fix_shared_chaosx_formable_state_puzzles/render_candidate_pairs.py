"""Render exact-source/candidate texture pairs for assigned formable puzzle sprites."""

from pathlib import Path
import json
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "docs/assets/gfx_fix_shared_chaosx_formable_state_puzzles"
INV = json.loads((WORK / "input_inventory_v2.json").read_text(encoding="utf-8"))
CAND = json.loads((WORK / "processed_v3/puzzle_candidates_v3.json").read_text(encoding="utf-8"))
inventory_by = {(a["family"], a["state_id"], a["variant"]): a for a in INV["assets"]}
candidate_by = {(a["family"], a["state_id"], a["variant"]): a for a in CAND["assets"]}
OUT = WORK / "contact_sheets/candidate_pairs_v3"
OUT.mkdir(parents=True, exist_ok=True)
FONT = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 12)
SMALL = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 10)

def thumb(path: Path, slot: tuple[int, int] = (82, 60)) -> Image.Image:
	image = Image.open(path).convert("RGBA")
	scale = min(4, slot[0] / image.width, slot[1] / image.height)
	size = (max(1, round(image.width * scale)), max(1, round(image.height * scale)))
	image = image.resize(size, Image.Resampling.NEAREST)
	canvas = Image.new("RGBA", slot, (35, 37, 40, 255))
	canvas.alpha_composite(image, ((slot[0] - size[0]) // 2, (slot[1] - size[1]) // 2))
	return canvas.convert("RGB")

index = []
for family in INV["palette_families"]:
	state_ids = sorted({s for f, s, _v in candidate_by if f == family})
	for page, start in enumerate(range(0, len(state_ids), 10), 1):
		batch = state_ids[start:start + 10]
		cell_w, cell_h, rows = 368, 112, 5
		page_img = Image.new("RGB", (cell_w * 2, 35 + rows * cell_h), (27, 29, 31))
		draw = ImageDraw.Draw(page_img)
		draw.text((7, 6), f"{family} | exact registered state masks | page {page}", font=FONT, fill=(238, 235, 226))
		for n, state_id in enumerate(batch):
			cell_x = (n % 2) * cell_w
			cell_y = 35 + (n // 2) * cell_h
			draw.rectangle((cell_x, cell_y, cell_x + cell_w - 3, cell_y + cell_h - 4), fill=(39, 41, 43))
			draw.text((cell_x + 5, cell_y + 3), f"state {state_id}", font=FONT, fill=(244, 241, 230))
			for j, (variant, before_label, after_label) in enumerate((("unresolved", "Before U", "Candidate U"), ("qualifying", "Before Q", "Candidate Q"))):
				asset = candidate_by[(family, state_id, variant)]
				source = inventory_by[(family, state_id, variant)]
				paths = ((source["before_png"], before_label), (asset["processed_png"], after_label))
				for k, (path_text, label) in enumerate(paths):
					col = j * 2 + k
					x = cell_x + 5 + col * 90
					draw.text((x, cell_y + 22), label, font=SMALL, fill=(205, 204, 197))
					page_img.paste(thumb(ROOT / path_text), (x, cell_y + 38))
					variant_asset = asset if k else source
					# Native dimensions remain visible in the label for exact-size interpretation.
					if k:
						dims = Image.open(ROOT / path_text).size
					else:
						dims = tuple(source["canvas_size"])
					draw.text((x, cell_y + 100), f"{dims[0]}x{dims[1]}", font=SMALL, fill=(153, 154, 152))
		out = OUT / f"{family}_page_{page:02d}.png"
		page_img.save(out)
		index.append({"family": family, "page": page, "state_ids": batch, "path": str(out.relative_to(ROOT)).replace("\\", "/")})

(OUT / "index.json").write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")
print(f"rendered {len(index)} paired pages for {sum(len(x['state_ids']) for x in index)} palette state pairs")
for entry in index:
	print(entry["path"])
