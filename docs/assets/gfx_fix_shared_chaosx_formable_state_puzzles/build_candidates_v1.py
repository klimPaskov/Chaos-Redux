"""Build variant-faithful state-puzzle palette and minimum-footprint ring candidates."""

from pathlib import Path
import hashlib
import importlib.util
import json
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "docs/assets/gfx_fix_shared_chaosx_formable_state_puzzles"
INVENTORY = json.loads((WORK / "input_inventory_v2.json").read_text(encoding="utf-8"))
TOOL = ROOT / ".tools/repair_event6_state_puzzle_assets.py"
spec = importlib.util.spec_from_file_location("event6_state_palette", TOOL)
palette_tool = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(palette_tool)

UNRESOLVED_RING = tuple(palette_tool.UNRESOLVED_OUTLINE)
QUALIFYING_RING = tuple(palette_tool.QUALIFYING_KEYLINE)
ring_by_state = {(item["family"], item["state_id"]): item for item in INVENTORY["island_ring_states"]}

def sha(path: Path) -> str:
	return hashlib.sha256(path.read_bytes()).hexdigest()

def path_from_inventory(value: str) -> Path:
	return ROOT / value

def draw_marker_ring(size: tuple[int, int], color: tuple[int, int, int], diameter: int = 12) -> Image.Image:
	scale = 4
	width, height = size
	high = Image.new("RGBA", (width * scale, height * scale), (0, 0, 0, 0))
	draw = ImageDraw.Draw(high)
	cx = (width - 1) / 2 * scale
	cy = (height - 1) / 2 * scale
	radius = diameter / 2 * scale
	draw.ellipse((cx - radius, cy - radius, cx + radius, cy + radius), outline=(*color, 255), width=scale)
	ring = high.resize(size, Image.Resampling.LANCZOS)
	return ring

def expand_for_ring(core: Image.Image, plan: dict, variant: str) -> Image.Image:
	width, height = plan["new_canvas"]
	pad_x, pad_y = plan["core_padding"]
	canvas = Image.new("RGBA", (width, height), (0, 0, 0, 0))
	canvas.paste(core, (pad_x, pad_y))
	color = UNRESOLVED_RING if variant == "unresolved" else QUALIFYING_RING
	ring = draw_marker_ring(canvas.size, color, plan["ring_diameter_px"])
	# Lanczos may leave tiny antialias alpha in the marker center. Keep the
	# registered state core byte-for-byte identical and restrict the ring to
	# pixels outside that original geometry.
	ring_data = ring.load()
	for y in range(pad_y, pad_y + core.height):
		for x in range(pad_x, pad_x + core.width):
			if ring_data[x, y][3] != 0:
				ring_data[x, y] = (0, 0, 0, 0)
	canvas.alpha_composite(ring)
	return canvas

assets = INVENTORY["assets"]
pair_map = {}
for item in assets:
	pair_map.setdefault((item["family"], item["state_id"]), {})[item["variant"]] = item

records = []
for (family, state_id), pair in sorted(pair_map.items()):
	if set(pair) != {"unresolved", "qualifying"}:
		raise RuntimeError(f"incomplete source pair: {family} state {state_id}")
	unresolved_source = Image.open(path_from_inventory(pair["unresolved"]["before_png"])).convert("RGBA")
	qualifying_source = Image.open(path_from_inventory(pair["qualifying"]["before_png"])).convert("RGBA")
	alpha_u = unresolved_source.getchannel("A")
	alpha_q = qualifying_source.getchannel("A")
	binary_u = alpha_u.point(lambda value: 255 if value > 0 else 0)
	binary_q = alpha_q.point(lambda value: 255 if value > 0 else 0)
	if unresolved_source.size != qualifying_source.size or binary_u.tobytes() != binary_q.tobytes():
		raise RuntimeError(f"source map masks differ: {family} state {state_id}")
	ring_plan = ring_by_state.get((family, state_id))
	for variant in ("unresolved", "qualifying"):
		record = pair[variant]
		variant_source = Image.open(path_from_inventory(record["before_png"])).convert("RGBA")
		if record["palette_repair"]:
			# Preserve each variant's own exact alpha plane, including antialiased edges.
			base = palette_tool.process_state(variant_source, variant)
		else:
			# The outside families need a footprint marker only, so their existing
			# pixels and family palette remain untouched inside the state core.
			base = variant_source
		if ring_plan:
			final = expand_for_ring(base, ring_plan, variant)
			pad_x, pad_y = ring_plan["core_padding"]
			core = final.crop((pad_x, pad_y, pad_x + base.width, pad_y + base.height))
			if core.tobytes() != base.tobytes():
				raise RuntimeError(f"ring changed exact inner core: {family} state {state_id} {variant}")
		else:
			final = base
			if final.getchannel("A").tobytes() != variant_source.getchannel("A").tobytes():
				raise RuntimeError(f"palette changed alpha geometry: {family} state {state_id} {variant}")
		folder = "palette" if record["palette_repair"] else "island_ring"
		out_dir = WORK / "processed_v3" / folder / family
		out_dir.mkdir(parents=True, exist_ok=True)
		out = out_dir / f"state_{state_id}_{variant}.png"
		final.save(out, format="PNG", optimize=False)
		alpha = final.getchannel("A")
		records.append({
			"family": family,
			"state_id": state_id,
			"variant": variant,
			"runtime_dds": record["runtime_dds"],
			"before_snapshot": record["before_snapshot"],
			"before_sha256": record["before_sha256"],
			"source_png": record["before_png"],
			"source_png_sha256": record["before_png_sha256"],
			"source_mode": "runtime_recovered_exact_geometry",
			"palette_repair": bool(record["palette_repair"]),
			"ring_repair": bool(ring_plan),
			"processed_png": str(out.relative_to(ROOT)).replace("\\", "/"),
			"processed_sha256": sha(out),
			"before_canvas": record["canvas_size"],
			"processed_canvas": final.size,
			"before_alpha_bbox": record["alpha_bbox"],
			"processed_alpha_bbox": alpha.getbbox(),
			"before_binary_mask_pixels": record["visible_pixel_count_alpha_gt0"],
			"processed_core_exact": True,
			"ring_color_rgb": list(UNRESOLVED_RING if variant == "unresolved" else QUALIFYING_RING) if ring_plan else None,
			"new_gui_position": ring_plan["new_gui_position"] if ring_plan else None,
		})

report = {
	"status": "candidate_pngs_ready_for_parent_review",
	"palette_families": INVENTORY["palette_families"],
	"palette_asset_count": INVENTORY["palette_asset_count"],
	"island_marker_state_count": len(ring_by_state),
	"candidate_asset_count": len(records),
	"generator": str(TOOL.relative_to(ROOT)).replace("\\", "/"),
	"palette": {
		"unresolved_fill": list(palette_tool.UNRESOLVED_FILL),
		"unresolved_hatch": list(palette_tool.UNRESOLVED_HATCH),
		"unresolved_outline": list(palette_tool.UNRESOLVED_OUTLINE),
		"qualifying_fill": list(palette_tool.QUALIFYING_FILL),
		"qualifying_outline": list(palette_tool.QUALIFYING_OUTLINE),
		"qualifying_keyline": list(palette_tool.QUALIFYING_KEYLINE),
		"hatch_period": palette_tool.HATCH_PERIOD,
	},
	"ring_policy": "12px antialiased status-colored outline around the exact unchanged runtime-recovered state core; parent GUI offsets are per ring state.",
	"assets": records,
}
out = WORK / "processed_v3" / "puzzle_candidates_v3.json"
out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
print("candidate PNGs:", len(records), "palette:", sum(1 for record in records if record["palette_repair"]), "ring:", sum(1 for record in records if record["ring_repair"]))
print("candidate report:", out.relative_to(ROOT), sha(out))
