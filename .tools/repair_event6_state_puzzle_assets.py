#!/usr/bin/env python3
"""Repair Event 006 state-puzzle presentation assets from installed DDS geometry.

The accepted Event 006 state-puzzle contract requires a non-colour distinction:
unresolved pieces use a neutral grey fill with diagonal hatching, while
qualifying pieces use a green fill with a solid inner keyline.  The original
source/processed PNG paths declared by the fourteen Event 006 manifests were
absent, so this bounded repair recovers the exact existing silhouettes from
their engine-facing DDS files, records that provenance, emits processed PNGs,
rebuilds the runtime DDS files through the shared converter, and refreshes the
manifest hashes and presentation previews.  It does not change geometry, GUI,
sprite names, gameplay, or any non-Event-006 state-puzzle asset.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_GLOB = ROOT / "docs/formables/state_puzzles"
DDS_CONVERTER = ROOT / ".agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py"
CONTACT_SHEET = ROOT / "docs/assets/006_independence_wave/contact_sheets/state_puzzles_repaired_contact_sheet.png"

UNRESOLVED_FILL = (98, 101, 108)
UNRESOLVED_HATCH = (66, 69, 75)
UNRESOLVED_OUTLINE = (151, 154, 161)
QUALIFYING_FILL = (70, 148, 103)
QUALIFYING_OUTLINE = (25, 56, 45)
QUALIFYING_KEYLINE = (155, 216, 165)
HATCH_PERIOD = 6


def sha256_file(path: Path) -> str:

	hash_obj = hashlib.sha256()
	with path.open("rb") as handle:
		for chunk in iter(lambda: handle.read(1024 * 1024), b""):
			hash_obj.update(chunk)
	return hash_obj.hexdigest()


def canonical_hash(value: object) -> str:

	encoded = json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(",", ":")).encode("utf-8")
	return hashlib.sha256(encoded).hexdigest()


def png_bytes(image: Image.Image) -> bytes:

	from io import BytesIO

	buffer = BytesIO()
	image.save(buffer, format="PNG", optimize=False)
	return buffer.getvalue()


def recovered_source(runtime_dds: Path) -> Image.Image:

	return Image.open(runtime_dds).convert("RGBA")


def process_state(source: Image.Image, variant: str) -> Image.Image:

	array = np.asarray(source, dtype=np.uint8)
	mask = array[:, :, 3] > 0
	result = np.zeros_like(array)
	if variant == "unresolved":
		result[mask, :3] = np.asarray(UNRESOLVED_FILL, dtype=np.uint8)
		result[mask, 3] = array[mask, 3]
		up = np.zeros_like(mask)
		down = np.zeros_like(mask)
		left = np.zeros_like(mask)
		right = np.zeros_like(mask)
		up[1:] = mask[:-1]
		down[:-1] = mask[1:]
		left[:, 1:] = mask[:, :-1]
		right[:, :-1] = mask[:, 1:]
		inner_outline = mask & ~(up & down & left & right)
		result[inner_outline, :3] = np.asarray(UNRESOLVED_OUTLINE, dtype=np.uint8)
		height, width = mask.shape
		yy, xx = np.indices(mask.shape)
		hatch = ((xx + yy) % HATCH_PERIOD) < 1
		hatch_pixels = mask & ~inner_outline & hatch
		result[hatch_pixels, :3] = np.asarray(UNRESOLVED_HATCH, dtype=np.uint8)
	else:
		result[mask, :3] = np.asarray(QUALIFYING_FILL, dtype=np.uint8)
		result[mask, 3] = array[mask, 3]
		up = np.zeros_like(mask)
		down = np.zeros_like(mask)
		left = np.zeros_like(mask)
		right = np.zeros_like(mask)
		up[1:] = mask[:-1]
		down[:-1] = mask[1:]
		left[:, 1:] = mask[:, :-1]
		right[:, :-1] = mask[:, 1:]
		inner_outline = mask & ~(up & down & left & right)
		result[inner_outline, :3] = np.asarray(QUALIFYING_OUTLINE, dtype=np.uint8)
		eroded = up & down & left & right
		eroded_up = np.zeros_like(mask)
		eroded_down = np.zeros_like(mask)
		eroded_left = np.zeros_like(mask)
		eroded_right = np.zeros_like(mask)
		eroded_up[1:] = eroded[:-1]
		eroded_down[:-1] = eroded[1:]
		eroded_left[:, 1:] = eroded[:, :-1]
		eroded_right[:, :-1] = eroded[:, 1:]
		inset_keyline = eroded & ~(eroded_up & eroded_down & eroded_left & eroded_right)
		result[inset_keyline, :3] = np.asarray(QUALIFYING_KEYLINE, dtype=np.uint8)
	return Image.fromarray(result, mode="RGBA")


def convert_to_dds(source: Path, output: Path) -> None:

	completed = subprocess.run(
		[sys.executable, str(DDS_CONVERTER), "--input", str(source), "--output", str(output)],
		text=True,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
	)
	if completed.returncode != 0 or not output.is_file():
		raise RuntimeError(f"DDS conversion failed for {source}: {completed.stderr.strip()}")


def rebuild_manifest(manifest_path: Path) -> tuple[int, list[tuple[str, Image.Image, Image.Image]]]:

	manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
	if manifest.get("schema") != "chaos-redux-formable-state-puzzle/v1":
		raise RuntimeError(f"unsupported manifest schema: {manifest_path}")
	preview_records: list[tuple[str, Image.Image, Image.Image]] = []
	for asset in manifest.get("assets", []):
		runtime_dds = ROOT / asset["dds"]
		source_png = ROOT / asset["source_png"]
		processed_png = ROOT / asset["processed_png"]
		if not runtime_dds.is_file():
			raise RuntimeError(f"missing runtime DDS: {runtime_dds}")
		source = Image.open(source_png).convert("RGBA") if source_png.is_file() else recovered_source(runtime_dds)
		processed = process_state(source, asset["variant"])
		source_png.parent.mkdir(parents=True, exist_ok=True)
		processed_png.parent.mkdir(parents=True, exist_ok=True)
		source_png.write_bytes(png_bytes(source))
		processed_png.write_bytes(png_bytes(processed))
		convert_to_dds(processed_png, runtime_dds)
		asset["source_png_sha256"] = sha256_file(source_png)
		asset["png_sha256"] = sha256_file(processed_png)
		asset["dds_sha256"] = sha256_file(runtime_dds)
		asset["source_mode"] = "runtime_recovered_exact_geometry"
		asset["source_note"] = "Original authored PNG was absent; source was recovered from the pre-repair engine DDS without changing its silhouette or alpha mask."
		asset["processing"] = (
			"grey_diagonal_hatch_and_inner_outline_clipped_to_alpha"
			if asset["variant"] == "unresolved"
			else "green_dark_inner_outline_and_pale_keyline_clipped_to_alpha"
		)
		preview_records.append((asset["variant"], processed, source))
	manifest["asset_source_mode"] = "runtime_recovered_exact_geometry"
	manifest["asset_processing"] = {
		"unresolved": {
			"fill_rgb": list(UNRESOLVED_FILL),
			"hatch_rgb": list(UNRESOLVED_HATCH),
			"inner_outline_rgb": list(UNRESOLVED_OUTLINE),
			"hatch_period": HATCH_PERIOD,
		},
		"qualifying": {
			"fill_rgb": list(QUALIFYING_FILL),
			"inner_outline_rgb": list(QUALIFYING_OUTLINE),
			"inner_keyline_rgb": list(QUALIFYING_KEYLINE),
		},
		"alpha_source": "preserved_from_pre_repair_runtime_dds",
	}
	manifest.pop("manifest_sha256", None)
	manifest["manifest_sha256"] = canonical_hash(manifest)
	manifest_path.write_text(json.dumps(manifest, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
	return len(manifest.get("assets", [])), preview_records


def write_previews(manifest_path: Path, processed_images: list[tuple[str, Image.Image, Image.Image]]) -> None:

	manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
	preview_dir = manifest_path.parent
	canvas = tuple(manifest["projection"]["canvas"])
	unresolved_preview = Image.new("RGBA", canvas, (0, 0, 0, 0))
	qualifying_preview = Image.new("RGBA", canvas, (0, 0, 0, 0))
	for state, (unresolved_record, qualifying_record) in zip(manifest["states"], zip(processed_images[::2], processed_images[1::2])):
		unresolved = unresolved_record[1]
		qualifying = qualifying_record[1]
		bbox = next(item["bbox"] for item in manifest["assets"] if item["state_id"] == state["state_id"] and item["variant"] == "unresolved")
		unresolved_preview.alpha_composite(unresolved, dest=(bbox[0], bbox[1]))
		qualifying_preview.alpha_composite(qualifying, dest=(bbox[0], bbox[1]))
	category = manifest["category_id"]
	unresolved_preview.save(preview_dir / f"{category}_projection_{canvas[0]}x{canvas[1]}.png", format="PNG", optimize=False)
	qualifying_preview.save(preview_dir / f"{category}_projection_{canvas[0]}x{canvas[1]}_qualifying.png", format="PNG", optimize=False)


def build_contact_sheet(records: list[tuple[str, str, Image.Image]]) -> None:

	if not records:
		return
	thumb_w, thumb_h = 180, 140
	label_h = 24
	columns = 8
	rows = (len(records) + columns - 1) // columns
	sheet = Image.new("RGBA", (columns * thumb_w, rows * (thumb_h + label_h)), (28, 31, 35, 255))
	draw = ImageDraw.Draw(sheet)
	for index, (label, variant, image) in enumerate(records):
		x = (index % columns) * thumb_w
		y = (index // columns) * (thumb_h + label_h)
		preview = image.copy()
		preview.thumbnail((thumb_w - 10, thumb_h - 10), Image.Resampling.NEAREST)
		px = x + (thumb_w - preview.width) // 2
		py = y + (thumb_h - preview.height) // 2
		sheet.alpha_composite(preview, dest=(px, py))
		draw.text((x + 4, y + thumb_h + 4), f"{label} {variant}", fill=(235, 238, 242, 255))
	CONTACT_SHEET.parent.mkdir(parents=True, exist_ok=True)
	sheet.save(CONTACT_SHEET, format="PNG", optimize=False)


def main() -> int:

	manifests = sorted(MANIFEST_GLOB.glob("006_form*_state_puzzle/manifest.json"))
	if len(manifests) != 14:
		raise RuntimeError(f"expected 14 Event 006 state-puzzle manifests, found {len(manifests)}")
	total = 0
	contact_records: list[tuple[str, str, Image.Image]] = []
	for manifest_path in manifests:
		count, processed = rebuild_manifest(manifest_path)
		write_previews(manifest_path, processed)
		manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
		for index in range(0, len(processed), 2):
			state_id = manifest["assets"][index]["state_id"]
			contact_records.append((f"{manifest['formable_id']}/S{state_id}", "unresolved", processed[index][1]))
			contact_records.append((f"{manifest['formable_id']}/S{state_id}", "qualifying", processed[index + 1][1]))
		total += count
	build_contact_sheet(contact_records)
	print(f"Repaired {total} Event 006 state-puzzle assets across {len(manifests)} manifests.")
	print(f"Contact sheet: {CONTACT_SHEET}")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
