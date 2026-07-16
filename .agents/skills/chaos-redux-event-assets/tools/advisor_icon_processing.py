#!/usr/bin/env python3
"""Finish a style-approved portrait master for HOI4 leader or advisor use.

This tool is a deterministic finishing and presentation step. It does not
invent a person's face or draw advisor-card artwork, and it is not a substitute
for source research or the required visual review against the canonical
event-assets skill references in ``assets/vanilla_reference/portraits/leaders``
and ``assets/vanilla_reference/portraits/advisors``.

Real people must start from an attributed archival image. Pass an explicit
head-and-shoulders crop, preserve the person's recognisable features, and
reject the result if the source is too weak to survive the HOI4 finish.
Fictional portraits may start from an approved ImageGen master. Advisor mode
also requires separately generated, shadowless frame and paper sources plus
their alpha-processed overlays. The script only crops, grades, resizes, angles,
derives shadows from approved alpha, composites, validates, and exports those
approved sources. It never draws any visible advisor-card element.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageOps


LEADER_SIZE = (156, 210)
ADVISOR_SIZE = (65, 67)
PROCESSOR_VERSION = "4.3"
LEADER_RENDER_VERSION = "2.0"
ADVISOR_RENDER_VERSION = "4.3"
SKILL_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = SKILL_ROOT.parents[2]
REFERENCE_ROOT = SKILL_ROOT / "assets" / "vanilla_reference" / "portraits"
ADVISOR_REFERENCE_NAMES = (
	"generic_europe_1.png",
	"generic_female_europe.png",
	"generic_asia_1.png",
	"army_small_ger_friedrich_paulus.png",
	"army_small_ger_gunther_von_kluge.png",
	"army_small_ger_erwin_rommel.png",
)

# These native placements reproduce the shared 65x67 vanilla dossier-card
# footprint. Generated overlays remain the sole source of visible artwork: the
# processor trims their authored alpha bounds, resizes them, and places them.
ADVISOR_FRAME_SIZE = (40, 58)
ADVISOR_FRAME_POSITION = (1, 1)
ADVISOR_FRAME_ANGLE = 5.0
ADVISOR_FRAME_ALPHA_CAP = 255
ADVISOR_FRAME_GRADE_COLOR = 0.55
ADVISOR_FRAME_GRADE_BRIGHTNESS = 0.80
ADVISOR_FRAME_GRADE_CONTRAST = 1.02
ADVISOR_FRAME_ALPHA_LOW_CUTOFF = 32
ADVISOR_FRAME_ALPHA_OPAQUE_CUTOFF = 255
ADVISOR_FRAME_ALPHA_CURVE_SCALE = 181
ADVISOR_FRAME_ALPHA_CURVE_SPAN = 221
ADVISOR_FRAME_ALPHA_CURVE_EXPONENT = 4.5
# The source overlay is resized before rotation. These values are calibrated to
# the approved ImageGen paper and remain inside every measured six-reference
# vanilla paper band at native size.
ADVISOR_PAPER_SIZE = (26, 30)
ADVISOR_PAPER_POSITION = (30, 25)
ADVISOR_PAPER_ANGLE = -3.0
ADVISOR_PAPER_GRADE_COLOR = 0.85
ADVISOR_PAPER_GRADE_BRIGHTNESS = 1.15
ADVISOR_PAPER_GRADE_CONTRAST = 1.06
ADVISOR_PAPER_GRADE_SHARPNESS = 1.35
ADVISOR_PAPER_GRADE_CHANNEL_SCALE = (0.886, 0.820, 0.839)
ADVISOR_PAPER_ALPHA_OUTER_EDGE_MAX_SOURCE = 32
ADVISOR_PAPER_ALPHA_OUTER_EDGE_VALUE = 224
ADVISOR_PAPER_ALPHA_INNER_EDGE_MAX_SOURCE = 36
ADVISOR_PAPER_ALPHA_INNER_EDGE_VALUE = 250
ADVISOR_PAPER_ALPHA_OPAQUE_VALUE = 255
ADVISOR_WINDOW_ALPHA_THRESHOLD = 32
ADVISOR_CARD_SHADOW_LAYERS = (
	((3, 1), 0.17, 5.0),
	((5, 2), 0.24, 2.0),
	((5, 1), 0.18, 2.5),
	((1, 1), 0.06, 0.0),
	((3, 1), 0.06, 0.0),
	((5, 2), 0.06, 0.0),
)
ADVISOR_PAPER_SHADOW_LAYERS = (
	((2, 1), 0.15, 0.0),
	((4, 1), 0.15, 0.0),
	((5, 2), 0.15, 0.0),
)

ADVISOR_ALPHA_COVERAGE_GATES = {
	0: (0.842, 0.867),
	8: (0.785, 0.795),
	32: (0.723, 0.730),
	128: (0.584, 0.596),
	224: (0.529, 0.537),
	254: (0.496, 0.506),
}
ADVISOR_ALPHA_SEMITRANSPARENT_RANGE = (1450, 1600)
ADVISOR_ALPHA_BBOX_RANGES = (
	(0, 2),
	(0, 2),
	(61, 63),
	(63, 65),
)
ADVISOR_ALPHA_CENTROID_X_RANGE = (29.0, 30.0)
ADVISOR_ALPHA_CENTROID_Y_RANGE = (33.4, 34.5)
ADVISOR_CANONICAL_PAPER_FAMILY = {
	"bbox_gt_32": [30, 26, 57, 58],
	"width": 27,
	"height": 32,
	"area_gt_32": 733.333333,
	"coverage_gt_32": 0.168389,
	"center": [42.689167, 41.328],
	"top_edge_image_slope": 0.072006,
	"top_edge_image_angle_degrees": 4.118333,
	"mean_luminance": 209.209167,
	"mean_saturation": 0.217098,
}

# Face bounds are supplied in source pixels and mapped into the final native
# canvas. These ranges cover the canonical vanilla advisor family while
# rejecting leader-scale faces and tiny busts that disappear behind the dossier
# paper.
ADVISOR_FACE_WIDTH_RANGE = (14.0, 24.0)
ADVISOR_FACE_HEIGHT_RANGE = (16.0, 30.0)
ADVISOR_FACE_CENTER_X_RANGE = (17.0, 27.0)
ADVISOR_FACE_CENTER_Y_RANGE = (18.0, 32.0)


def parse_crop(values: list[int], image: Image.Image) -> tuple[int, int, int, int]:
	left, top, right, bottom = values
	if left < 0 or top < 0 or right > image.width or bottom > image.height:
		raise ValueError(f"Crop {values} is outside the {image.width}x{image.height} source")
	if right <= left or bottom <= top:
		raise ValueError(f"Crop must have positive width and height: {values}")
	return left, top, right, bottom


def parse_face_box(
	values: list[int],
	image: Image.Image,
	crop_box: tuple[int, int, int, int],
) -> tuple[int, int, int, int]:
	face_box = parse_crop(values, image)
	left, top, right, bottom = face_box
	crop_left, crop_top, crop_right, crop_bottom = crop_box
	if (
		left < crop_left
		or top < crop_top
		or right > crop_right
		or bottom > crop_bottom
	):
		raise ValueError(
			f"Face box {values} must be fully contained by advisor crop {crop_box}"
		)
	return face_box


def deterministic_noise(size: tuple[int, int], seed_text: str) -> Image.Image:
	seed = int(hashlib.sha256(seed_text.encode("utf-8")).hexdigest()[:8], 16)
	state = seed
	pixels: list[int] = []
	for _ in range(size[0] * size[1]):
		state = (1664525 * state + 1013904223) & 0xFFFFFFFF
		pixels.append(118 + ((state >> 24) % 21))
	noise = Image.new("L", size)
	noise.putdata(pixels)
	return noise.filter(ImageFilter.GaussianBlur(0.35))


def vignette_mask(size: tuple[int, int]) -> Image.Image:
	width, height = size
	mask = Image.new("L", size)
	pixels: list[int] = []
	for y in range(height):
		vertical = (y - height * 0.43) / (height * 0.62)
		for x in range(width):
			horizontal = (x - width * 0.5) / (width * 0.68)
			distance = math.sqrt(horizontal * horizontal + vertical * vertical)
			pixels.append(max(0, min(255, round((distance - 0.50) * 145))))
	mask.putdata(pixels)
	return mask.filter(ImageFilter.GaussianBlur(max(2, width // 24)))


def hoi4_finish(image: Image.Image, source_kind: str, seed_text: str) -> Image.Image:
	alpha = image.getchannel("A")
	rgb = image.convert("RGB")
	rgb = ImageEnhance.Contrast(rgb).enhance(1.075)
	rgb = ImageEnhance.Color(rgb).enhance(0.88 if source_kind == "real" else 0.94)

	# A restrained edge-preserving blend softens photographic micro-detail while
	# retaining the face, eyes, hairline, uniform edges, and other identity cues.
	smoothed = rgb.filter(ImageFilter.MedianFilter(3))
	rgb = Image.blend(rgb, smoothed, 0.14 if source_kind == "real" else 0.10)
	rgb = rgb.filter(ImageFilter.UnsharpMask(radius=1.15, percent=72, threshold=4))

	# Warm highlights and cool charcoal shadows mirror the restrained painted
	# palette of the bundled vanilla references without colourising a new face.
	luma = ImageOps.grayscale(rgb)
	warm = Image.new("RGB", rgb.size, (126, 91, 59))
	cool = Image.new("RGB", rgb.size, (40, 47, 53))
	warm_mask = luma.point(lambda value: max(0, min(31, round((value - 108) * 0.19))))
	cool_mask = luma.point(lambda value: max(0, min(23, round((112 - value) * 0.17))))
	rgb = Image.composite(warm, rgb, warm_mask)
	rgb = Image.composite(cool, rgb, cool_mask)

	grain = deterministic_noise(rgb.size, seed_text)
	grain_rgb = Image.merge("RGB", (grain, grain, grain))
	rgb = Image.blend(rgb, grain_rgb, 0.035)

	dark = Image.new("RGB", rgb.size, (22, 25, 27))
	rgb = Image.composite(dark, rgb, vignette_mask(rgb.size))
	result = rgb.convert("RGBA")
	result.putalpha(alpha)
	return result


def make_leader(source_crop: Image.Image, source_kind: str, seed_text: str) -> Image.Image:
	resized = ImageOps.fit(
		source_crop,
		LEADER_SIZE,
		method=Image.Resampling.LANCZOS,
		centering=(0.5, 0.44),
	)
	return hoi4_finish(resized, source_kind, seed_text)


def sha256_file(path: Path) -> str:
	digest = hashlib.sha256()
	with path.open("rb") as handle:
		for chunk in iter(lambda: handle.read(1024 * 1024), b""):
			digest.update(chunk)
	return digest.hexdigest()


def canonical_json_sha256(payload: object) -> str:
	encoded = json.dumps(
		payload,
		sort_keys=True,
		separators=(",", ":"),
		ensure_ascii=False,
	).encode("utf-8")
	return hashlib.sha256(encoded).hexdigest()


def advisor_render_configuration() -> dict[str, object]:
	configuration = {
		"schema": "chaos-redux-advisor-render-configuration-v4.3",
		"canvas_size": list(ADVISOR_SIZE),
		"frame": {
			"size": list(ADVISOR_FRAME_SIZE),
			"position": list(ADVISOR_FRAME_POSITION),
			"angle": ADVISOR_FRAME_ANGLE,
			"alpha_cap": ADVISOR_FRAME_ALPHA_CAP,
			"grade_color": ADVISOR_FRAME_GRADE_COLOR,
			"grade_brightness": ADVISOR_FRAME_GRADE_BRIGHTNESS,
			"grade_contrast": ADVISOR_FRAME_GRADE_CONTRAST,
			"composition_alpha": {
				"low_cutoff": ADVISOR_FRAME_ALPHA_LOW_CUTOFF,
				"opaque_cutoff": ADVISOR_FRAME_ALPHA_OPAQUE_CUTOFF,
				"curve_scale": ADVISOR_FRAME_ALPHA_CURVE_SCALE,
				"curve_span": ADVISOR_FRAME_ALPHA_CURVE_SPAN,
				"curve_exponent": ADVISOR_FRAME_ALPHA_CURVE_EXPONENT,
			},
		},
		"paper": {
			"size": list(ADVISOR_PAPER_SIZE),
			"position": list(ADVISOR_PAPER_POSITION),
			"angle": ADVISOR_PAPER_ANGLE,
			"grade_color": ADVISOR_PAPER_GRADE_COLOR,
			"grade_brightness": ADVISOR_PAPER_GRADE_BRIGHTNESS,
			"grade_contrast": ADVISOR_PAPER_GRADE_CONTRAST,
			"grade_sharpness": ADVISOR_PAPER_GRADE_SHARPNESS,
			"grade_channel_scale": list(ADVISOR_PAPER_GRADE_CHANNEL_SCALE),
			"composition_alpha": {
				"outer_edge_max_source_alpha": ADVISOR_PAPER_ALPHA_OUTER_EDGE_MAX_SOURCE,
				"outer_edge_value": ADVISOR_PAPER_ALPHA_OUTER_EDGE_VALUE,
				"inner_edge_max_source_alpha": ADVISOR_PAPER_ALPHA_INNER_EDGE_MAX_SOURCE,
				"inner_edge_value": ADVISOR_PAPER_ALPHA_INNER_EDGE_VALUE,
				"opaque_value": ADVISOR_PAPER_ALPHA_OPAQUE_VALUE,
			},
		},
		"window_alpha_threshold": ADVISOR_WINDOW_ALPHA_THRESHOLD,
		"card_shadow_layers": [
			[list(offset), opacity, blur]
			for offset, opacity, blur in ADVISOR_CARD_SHADOW_LAYERS
		],
		"paper_shadow_layers": [
			[list(offset), opacity, blur]
			for offset, opacity, blur in ADVISOR_PAPER_SHADOW_LAYERS
		],
		"alpha_coverage_gates": {
			str(threshold): list(bounds)
			for threshold, bounds in ADVISOR_ALPHA_COVERAGE_GATES.items()
		},
		"alpha_semitransparent_range": list(
			ADVISOR_ALPHA_SEMITRANSPARENT_RANGE
		),
		"alpha_bbox_ranges": [list(bounds) for bounds in ADVISOR_ALPHA_BBOX_RANGES],
		"alpha_centroid_x_range": list(ADVISOR_ALPHA_CENTROID_X_RANGE),
		"alpha_centroid_y_range": list(ADVISOR_ALPHA_CENTROID_Y_RANGE),
		"canonical_paper_family": ADVISOR_CANONICAL_PAPER_FAMILY,
		"canonical_reference_names": list(ADVISOR_REFERENCE_NAMES),
	}
	return {
		"values": configuration,
		"sha256": canonical_json_sha256(configuration),
	}


def decoded_rgba_sha256(image: Image.Image) -> str:
	rgba = image.convert("RGBA")
	digest = hashlib.sha256()
	digest.update(b"chaos-redux-decoded-rgba-v1\0")
	digest.update(rgba.width.to_bytes(4, "little"))
	digest.update(rgba.height.to_bytes(4, "little"))
	digest.update(rgba.tobytes())
	return digest.hexdigest()


def deterministic_seed_record(
	source: Image.Image,
	crop_box: tuple[int, int, int, int],
	face_box: tuple[int, int, int, int] | None,
	source_kind: str,
	mode: str,
	render_version: str,
	frame_overlay_sha256: str | None,
	paper_overlay_sha256: str | None,
) -> dict[str, object]:
	payload = {
		"schema": "chaos-redux-portrait-seed-v2",
		"decoded_rgba_sha256": decoded_rgba_sha256(source),
		"crop": list(crop_box),
		"face_box": list(face_box) if face_box is not None else None,
		"source_kind": source_kind,
		"mode": mode,
		"render_version": render_version,
		"frame_overlay_sha256": frame_overlay_sha256,
		"paper_overlay_sha256": paper_overlay_sha256,
	}
	payload_sha256 = canonical_json_sha256(payload)
	return {
		"schema": str(payload["schema"]),
		"decoded_rgba_sha256": str(payload["decoded_rgba_sha256"]),
		"payload": payload,
		"payload_sha256": payload_sha256,
		"numeric_seed_first_64_bits": int(payload_sha256[:16], 16),
	}


def resolve_manifest_path(value: object, label: str) -> Path:
	text = str(value or "")
	if not text:
		raise ValueError(f"Advisor overlay manifest lacks {label}")
	path = Path(text).expanduser()
	if not path.is_absolute():
		path = REPO_ROOT / path
	return path.resolve()


def verify_overlay_manifest(
	manifest_path: Path,
	frame_source: Path,
	frame_overlay: Path,
	paper_source: Path,
	paper_overlay: Path,
) -> dict[str, object]:
	if not manifest_path.is_file():
		raise FileNotFoundError(f"Missing advisor overlay manifest: {manifest_path}")
	manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
	if manifest.get("schema_version") != 4:
		raise ValueError("Advisor overlay manifest must use provenance schema 4")
	if "built_in_store_root" in manifest:
		raise ValueError(
			"Advisor overlay manifest must be self-contained; external ImageGen store "
			"roots are audit history, not reusable processing dependencies"
		)
	generator = str(manifest.get("generator", ""))
	if "imagegen" not in generator.lower():
		raise ValueError(
			"Advisor overlay manifest must identify ImageGen as the visible-art source"
		)
	expected_roles = {"advisor_frame_shadowless", "advisor_paper_shadowless"}
	if set(manifest.get("final_roles", [])) != expected_roles:
		raise ValueError("Advisor overlay manifest active roles are incomplete or stale")
	approved_record_ids = manifest.get("approved_role_record_ids")
	if not isinstance(approved_record_ids, list) or len(approved_record_ids) != 2:
		raise ValueError("Advisor overlay manifest needs two approved role record IDs")
	if len(set(str(value) for value in approved_record_ids)) != 2:
		raise ValueError("Advisor overlay approved role record IDs must be unique")
	style_reference_record = manifest.get("canonical_style_references")
	if not isinstance(style_reference_record, dict):
		raise ValueError(
			"Advisor overlay manifest must pin the canonical advisor style references"
		)
	style_reference_root = resolve_manifest_path(
		style_reference_record.get("root"), "canonical_style_references.root"
	)
	canonical_reference_root = (REFERENCE_ROOT / "advisors").resolve()
	if style_reference_root != canonical_reference_root:
		raise ValueError(
			"Advisor overlay manifest must use the skill-local canonical advisor "
			f"reference root: {canonical_reference_root}"
		)
	style_reference_entries = style_reference_record.get("files")
	if not isinstance(style_reference_entries, list):
		raise ValueError("Advisor canonical style-reference list is missing")
	style_references: list[dict[str, str]] = []
	for name in ADVISOR_REFERENCE_NAMES:
		matches = [
			entry
			for entry in style_reference_entries
			if isinstance(entry, dict) and entry.get("name") == name
		]
		if len(matches) != 1:
			raise ValueError(
				f"Advisor manifest needs exactly one canonical style reference for {name}"
			)
		path = canonical_reference_root / name
		if not path.is_file():
			raise FileNotFoundError(path)
		actual_hash = sha256_file(path)
		expected_hash = str(matches[0].get("sha256", ""))
		if actual_hash != expected_hash:
			raise ValueError(
				f"Canonical advisor style reference hash differs for {name}: "
				f"{actual_hash} != {expected_hash}"
			)
		style_references.append(
			{"name": name, "path": str(path), "sha256": actual_hash}
		)
	if len(style_reference_entries) != len(ADVISOR_REFERENCE_NAMES):
		raise ValueError(
			"Advisor manifest canonical style-reference list contains unapproved entries"
		)
	assets = manifest.get("assets")
	if not isinstance(assets, list):
		raise ValueError("Advisor overlay manifest has no assets list")

	def verify_role(
		role: str,
		source_path: Path,
		overlay_path: Path,
	) -> dict[str, object]:
		matches = [
			asset
			for asset in assets
			if isinstance(asset, dict)
			and asset.get("role") == role
			and asset.get("status") == "approved_for_processing"
		]
		if len(matches) != 1:
			raise ValueError(
				f"Advisor overlay manifest needs exactly one approved_for_processing "
				f"{role} entry"
			)
		entry = matches[0]
		record_id = str(entry.get("record_id", ""))
		if record_id not in {str(value) for value in approved_record_ids}:
			raise ValueError(f"Advisor overlay role {role} has no approved record ID")
		handle = str(entry.get("imagegen_handle", ""))
		if not handle.startswith("exec-"):
			raise ValueError(f"Advisor overlay role {role} lacks an ImageGen handle")
		declared_source = resolve_manifest_path(entry.get("source"), f"{role} source")
		declared_overlay = resolve_manifest_path(
			entry.get("processed"), f"{role} processed overlay"
		)
		if source_path.resolve() != declared_source:
			raise ValueError(
				f"Advisor {role} source argument is not the manifest-approved source"
			)
		if overlay_path.resolve() != declared_overlay:
			raise ValueError(
				f"Advisor {role} overlay argument is not the manifest-approved overlay"
			)
		expected_source_hash = str(entry.get("source_sha256", ""))
		expected_overlay_hash = str(entry.get("processed_sha256", ""))
		actual_source_hash = sha256_file(source_path)
		actual_overlay_hash = sha256_file(overlay_path)
		if actual_source_hash != expected_source_hash:
			raise ValueError(
				f"Advisor {role} source does not match its frozen ImageGen manifest hash: "
				f"{actual_source_hash} != {expected_source_hash}"
			)
		if actual_overlay_hash != expected_overlay_hash:
			raise ValueError(
				f"Advisor {role} overlay does not match its frozen manifest hash: "
				f"{actual_overlay_hash} != {expected_overlay_hash}"
			)
		if entry.get("exact_source_byte_copy") is not True:
			raise ValueError(f"Advisor {role} lacks the exact source-copy assertion")
		if "built_in_store_object" in entry or "event_package_copy" in entry:
			raise ValueError(
				f"Advisor {role} manifest entry contains event- or machine-specific "
				"provenance dependencies"
			)

		prompt_record = resolve_manifest_path(
			entry.get("prompt_record"), f"{role} prompt record"
		)
		if not prompt_record.is_file():
			raise FileNotFoundError(f"Advisor {role} prompt record is missing")
		prompt_sha256 = sha256_file(prompt_record)
		if prompt_sha256 != str(entry.get("prompt_sha256", "")):
			raise ValueError(f"Advisor {role} prompt record hash differs")

		generation_inputs = entry.get("generation_inputs")
		if not isinstance(generation_inputs, list) or len(generation_inputs) < 2:
			raise ValueError(f"Advisor {role} generation inputs are incomplete")
		verified_inputs: list[dict[str, str]] = []
		for input_record in generation_inputs:
			if not isinstance(input_record, dict):
				raise ValueError(f"Advisor {role} has a malformed generation input")
			input_path = resolve_manifest_path(
				input_record.get("path"), f"{role} generation input"
			)
			if not input_path.is_file():
				raise FileNotFoundError(input_path)
			input_sha256 = sha256_file(input_path)
			if input_sha256 != str(input_record.get("sha256", "")):
				raise ValueError(f"Advisor {role} generation input hash differs")
			verified_inputs.append(
				{
					"role": str(input_record.get("role", "")),
					"path": str(input_path),
					"sha256": input_sha256,
				}
			)

		alpha_extraction = entry.get("alpha_extraction")
		if not isinstance(alpha_extraction, dict):
			raise ValueError(f"Advisor {role} lacks alpha-extraction provenance")
		alpha_tool = str(alpha_extraction.get("tool", ""))
		alpha_tool_sha256 = str(alpha_extraction.get("tool_sha256", ""))
		if not alpha_tool or len(alpha_tool_sha256) != 64:
			raise ValueError(
				f"Advisor {role} alpha-extraction tool provenance is incomplete"
			)
		arguments = alpha_extraction.get("arguments")
		if not isinstance(arguments, list) or not arguments:
			raise ValueError(f"Advisor {role} alpha-extraction arguments are missing")
		if str(alpha_extraction.get("input_sha256", "")) != actual_source_hash:
			raise ValueError(f"Advisor {role} alpha-extraction input hash differs")
		if str(alpha_extraction.get("output_sha256", "")) != actual_overlay_hash:
			raise ValueError(f"Advisor {role} alpha-extraction output hash differs")

		with Image.open(source_path) as source_image:
			source_dimensions = list(source_image.size)
		with Image.open(overlay_path) as overlay_image:
			overlay_dimensions = list(overlay_image.size)
		if source_dimensions != list(entry.get("source_dimensions", [])):
			raise ValueError(f"Advisor {role} source dimensions differ")
		if overlay_dimensions != list(entry.get("processed_dimensions", [])):
			raise ValueError(f"Advisor {role} overlay dimensions differ")
		if overlay_dimensions != list(alpha_extraction.get("output_dimensions", [])):
			raise ValueError(f"Advisor {role} alpha-extraction dimensions differ")
		return {
			"role": role,
			"record_id": record_id,
			"status": "approved_for_processing",
			"imagegen_handle": handle,
			"source_sha256": actual_source_hash,
			"overlay_sha256": actual_overlay_hash,
			"prompt_record": str(prompt_record),
			"prompt_sha256": prompt_sha256,
			"generation_inputs": verified_inputs,
			"alpha_extraction": {
				"tool": alpha_tool,
				"tool_sha256": alpha_tool_sha256,
				"tool_version": str(alpha_extraction.get("tool_version", "")),
				"arguments": [str(value) for value in arguments],
				"input_sha256": actual_source_hash,
				"output_sha256": actual_overlay_hash,
			},
		}

	return {
		"path": str(manifest_path),
		"sha256": sha256_file(manifest_path),
		"package": str(manifest.get("package", "")),
		"generator": generator,
		"canonical_style_references": style_references,
		"frame": verify_role(
			"advisor_frame_shadowless", frame_source, frame_overlay
		),
		"paper": verify_role(
			"advisor_paper_shadowless", paper_source, paper_overlay
		),
	}


def threshold_bbox(alpha: Image.Image, threshold: int = 8) -> tuple[int, int, int, int]:
	box = alpha.point(lambda value: 255 if value > threshold else 0).getbbox()
	if box is None:
		raise ValueError("Generated overlay has no visible alpha bounds")
	return box


def largest_alpha_component_bbox(
	alpha: Image.Image,
	threshold: int,
) -> tuple[tuple[int, int, int, int], int, int]:
	"""Find the principal authored layer while ignoring detached keying specks."""
	width, height = alpha.size
	visible = bytearray(value > threshold for value in alpha.getdata())
	visited = bytearray(width * height)
	largest_bbox: tuple[int, int, int, int] | None = None
	largest_area = 0
	component_count = 0
	for start, is_visible in enumerate(visible):
		if not is_visible or visited[start]:
			continue
		component_count += 1
		visited[start] = 1
		stack = [start]
		area = 0
		min_x = width
		min_y = height
		max_x = -1
		max_y = -1
		while stack:
			index = stack.pop()
			x = index % width
			y = index // width
			area += 1
			min_x = min(min_x, x)
			min_y = min(min_y, y)
			max_x = max(max_x, x)
			max_y = max(max_y, y)
			if x:
				neighbor = index - 1
				if visible[neighbor] and not visited[neighbor]:
					visited[neighbor] = 1
					stack.append(neighbor)
			if x + 1 < width:
				neighbor = index + 1
				if visible[neighbor] and not visited[neighbor]:
					visited[neighbor] = 1
					stack.append(neighbor)
			if y:
				neighbor = index - width
				if visible[neighbor] and not visited[neighbor]:
					visited[neighbor] = 1
					stack.append(neighbor)
			if y + 1 < height:
				neighbor = index + width
				if visible[neighbor] and not visited[neighbor]:
					visited[neighbor] = 1
					stack.append(neighbor)
		if area > largest_area:
			largest_area = area
			largest_bbox = (min_x, min_y, max_x + 1, max_y + 1)
	if largest_bbox is None:
		raise ValueError("Generated overlay has no connected authored alpha component")
	return largest_bbox, largest_area, component_count


def alpha_coverage(alpha: Image.Image, threshold: int) -> float:
	return sum(1 for value in alpha.getdata() if value > threshold) / (
		alpha.width * alpha.height
	)


def binary_alpha_centroid(alpha: Image.Image, threshold: int) -> tuple[float, float]:
	points = [
		(index % alpha.width, index // alpha.width)
		for index, value in enumerate(alpha.getdata())
		if value > threshold
	]
	if not points:
		raise ValueError("Advisor alpha has no pixels above the centroid threshold")
	return (
		sum(x for x, _ in points) / len(points),
		sum(y for _, y in points) / len(points),
	)


def load_generated_layer(
	overlay_path: Path,
	source_path: Path,
	label: str,
) -> tuple[Image.Image, dict[str, object]]:
	if not overlay_path.is_file():
		raise FileNotFoundError(f"Missing {label} alpha overlay: {overlay_path}")
	if not source_path.is_file():
		raise FileNotFoundError(f"Missing {label} ImageGen source: {source_path}")
	with Image.open(overlay_path) as image:
		overlay = image.convert("RGBA")
	with Image.open(source_path) as image:
		source = image.convert("RGB")
	if overlay.size != source.size:
		raise ValueError(
			f"{label} overlay/source dimensions differ: {overlay.size} versus {source.size}"
		)
	if overlay.width < 512 or overlay.height < 512:
		raise ValueError(
			f"{label} ImageGen source must remain a full-resolution master; got {overlay.size}"
		)
	alpha = overlay.getchannel("A")
	minimum, maximum = alpha.getextrema()
	if minimum != 0 or maximum != 255:
		raise ValueError(
			f"{label} overlay needs full transparent/opaque alpha; extrema were "
			f"{(minimum, maximum)} for {overlay_path}"
		)
	component_bbox, component_area, component_count = largest_alpha_component_bbox(
		alpha, ADVISOR_WINDOW_ALPHA_THRESHOLD
	)
	# The built-in keyer can leave isolated full-alpha sensor-like flecks on a
	# large ImageGen canvas. Keep the untouched RGB master, but restrict alpha to
	# the bounding envelope of its principal connected authored component before
	# native-size fitting. This does not create or redraw any visible artwork.
	clipped_alpha = Image.new("L", overlay.size)
	clipped_alpha.paste(alpha.crop(component_bbox), component_bbox)
	overlay.putalpha(clipped_alpha)
	alpha = clipped_alpha
	coverage = alpha_coverage(alpha, 8)
	if coverage < 0.02 or coverage > 0.50:
		raise ValueError(
			f"{label} overlay has implausible authored coverage {coverage:.3f}: "
			f"{overlay_path}"
		)
	# Ignore the sub-32 edge flecks that chroma-key cleanup can leave on the
	# master canvas. They are not part of the authored visible overlay and would
	# otherwise distort the native-size fit.
	visible_bbox = threshold_bbox(alpha, ADVISOR_WINDOW_ALPHA_THRESHOLD)

	# Chroma-key cleanup can alter edge RGB, but visible pixels must still be
	# recognisably derived from the retained ImageGen source rather than locally
	# redrawn artwork.
	difference = ImageChops.difference(source, overlay.convert("RGB"))
	difference_values = difference.getdata()
	alpha_values = alpha.getdata()
	visible_difference = 0.0
	visible_count = 0
	for channels, value in zip(difference_values, alpha_values):
		if value > 128:
			visible_difference += sum(channels) / 3
			visible_count += 1
	mean_visible_difference = visible_difference / max(1, visible_count)
	if mean_visible_difference > 24.0:
		raise ValueError(
			f"{label} overlay differs too far from its ImageGen source on visible "
			f"pixels ({mean_visible_difference:.2f} mean RGB delta)"
		)

	return overlay, {
		"source": str(source_path),
		"source_sha256": sha256_file(source_path),
		"overlay": str(overlay_path),
		"overlay_sha256": sha256_file(overlay_path),
		"source_size": list(source.size),
		"alpha_extrema": [minimum, maximum],
		"source_visible_bbox": list(visible_bbox),
		"principal_component_area_gt_32": component_area,
		"component_count_gt_32_before_clipping": component_count,
		"source_alpha_coverage_gt_8": round(coverage, 6),
		"mean_visible_source_rgb_delta": round(mean_visible_difference, 4),
	}


def normalize_generated_layer(
	image: Image.Image,
	target_size: tuple[int, int],
	position: tuple[int, int],
	angle: float = 0.0,
) -> tuple[Image.Image, tuple[int, int, int, int]]:
	visible_bbox = threshold_bbox(
		image.getchannel("A"), ADVISOR_WINDOW_ALPHA_THRESHOLD
	)
	trimmed = image.crop(visible_bbox)
	resized = trimmed.resize(target_size, Image.Resampling.LANCZOS)
	if angle:
		resized = resized.rotate(
			angle,
			resample=Image.Resampling.BICUBIC,
			expand=True,
			fillcolor=(0, 0, 0, 0),
		)
	canvas = Image.new("RGBA", ADVISOR_SIZE, (0, 0, 0, 0))
	canvas.alpha_composite(resized, position)
	return canvas, visible_bbox


def frame_palette_metrics(
	frame: Image.Image,
	stage: str,
) -> dict[str, float]:
	luminance_values: list[float] = []
	saturation_values: list[float] = []
	gold_pixels = 0
	warm_pixels = 0
	for red, green, blue, alpha in frame.getdata():
		if alpha <= 64:
			continue
		luminance = (54 * red + 183 * green + 19 * blue) / 256
		luminance_values.append(luminance)
		maximum = max(red, green, blue)
		saturation_values.append(
			0.0 if maximum == 0 else (maximum - min(red, green, blue)) / maximum
		)
		if red - blue > 20:
			warm_pixels += 1
		if (
			red > 75
			and green > 45
			and blue < green * 0.78
			and red > green * 1.12
			and red - blue > 35
		):
			gold_pixels += 1
	if not luminance_values:
		raise ValueError("Advisor frame has no visible palette samples")
	metrics = {
		"mean_luminance": sum(luminance_values) / len(luminance_values),
		"mean_saturation": sum(saturation_values) / len(saturation_values),
		"dark_pixel_ratio": sum(value < 110 for value in luminance_values)
		/ len(luminance_values),
		"gold_pixel_ratio": gold_pixels / len(luminance_values),
		"warm_pixel_ratio": warm_pixels / len(luminance_values),
	}
	if stage == "authored":
		# Inspect normalized ImageGen-authored pixels before neutral grading. This
		# prevents the processor from laundering an ornamental, bright, or warm
		# source into a superficially compliant final frame.
		if (
			not 25 <= metrics["mean_luminance"] <= 75
			or metrics["dark_pixel_ratio"] < 0.90
			or metrics["mean_saturation"] > 0.21
			or metrics["warm_pixel_ratio"] > 0.03
			or metrics["gold_pixel_ratio"] > 0.005
		):
			raise ValueError(
				"Authored advisor frame is not a restrained dark dossier frame; "
				f"metrics were {metrics}"
			)
	elif stage == "final":
		if (
			not 35 <= metrics["mean_luminance"] <= 50
			or metrics["dark_pixel_ratio"] < 0.95
		):
			raise ValueError(
				"Advisor frame must be predominantly charcoal/black at native size; "
				f"metrics were {metrics}"
			)
		if metrics["gold_pixel_ratio"] > 0.005:
			raise ValueError(
				"Advisor frame contains an ornamental gold/bronze treatment; "
				f"gold-like pixel ratio was {metrics['gold_pixel_ratio']:.3f}"
			)
		if (
			not 0.03 <= metrics["mean_saturation"] <= 0.125
			or metrics["warm_pixel_ratio"] > 0.03
		):
			raise ValueError(
				"Advisor frame is not the neutral charcoal of the vanilla dossier family; "
				f"metrics were {metrics}"
			)
	else:
		raise ValueError(f"Unknown advisor frame palette stage: {stage}")
	return {key: round(value, 6) for key, value in metrics.items()}


def grade_advisor_frame(frame: Image.Image) -> Image.Image:
	"""Match the neutral, slightly translucent charcoal of vanilla small cards."""
	alpha = frame.getchannel("A").point(
		lambda value: min(value, ADVISOR_FRAME_ALPHA_CAP)
	)
	rgb = ImageEnhance.Color(frame.convert("RGB")).enhance(
		ADVISOR_FRAME_GRADE_COLOR
	)
	rgb = ImageEnhance.Brightness(rgb).enhance(
		ADVISOR_FRAME_GRADE_BRIGHTNESS
	)
	rgb = ImageEnhance.Contrast(rgb).enhance(
		ADVISOR_FRAME_GRADE_CONTRAST
	)
	graded = rgb.convert("RGBA")
	graded.putalpha(alpha)
	return graded


def advisor_frame_composition_alpha(alpha: Image.Image) -> Image.Image:
	"""Calibrate authored frame alpha without changing its visible RGB artwork."""
	def remap(value: int) -> int:
		if value <= ADVISOR_FRAME_ALPHA_LOW_CUTOFF:
			return value
		if value == ADVISOR_FRAME_ALPHA_OPAQUE_CUTOFF:
			return 255
		normalized = (
			(value - ADVISOR_FRAME_ALPHA_LOW_CUTOFF - 1)
			/ ADVISOR_FRAME_ALPHA_CURVE_SPAN
		)
		return 33 + round(
			ADVISOR_FRAME_ALPHA_CURVE_SCALE
			* (normalized ** ADVISOR_FRAME_ALPHA_CURVE_EXPONENT)
		)

	return alpha.point(remap)


def grade_advisor_portrait(portrait: Image.Image) -> Image.Image:
	"""Keep small-card facial landmarks open, neutral, and painterly at 65x67."""
	alpha = portrait.getchannel("A")
	rgb = ImageEnhance.Color(portrait.convert("RGB")).enhance(0.58)
	# A restrained gamma lift opens eyes, cheeks, and dark uniforms without
	# flattening the painted highlights or inventing source detail.
	lut = [round(255 * ((value / 255) ** 0.86)) for value in range(256)]
	rgb = rgb.point(lut * 3)
	rgb = ImageEnhance.Contrast(rgb).enhance(1.02)
	graded = rgb.convert("RGBA")
	graded.putalpha(alpha)
	return graded


def grade_advisor_paper(paper: Image.Image) -> Image.Image:
	"""Reduce generated parchment chroma to the pale vanilla dossier-note range."""
	alpha = paper.getchannel("A")
	rgb = ImageEnhance.Color(paper.convert("RGB")).enhance(
		ADVISOR_PAPER_GRADE_COLOR
	)
	rgb = ImageEnhance.Brightness(rgb).enhance(
		ADVISOR_PAPER_GRADE_BRIGHTNESS
	)
	rgb = ImageEnhance.Contrast(rgb).enhance(ADVISOR_PAPER_GRADE_CONTRAST)
	rgb = ImageEnhance.Sharpness(rgb).enhance(ADVISOR_PAPER_GRADE_SHARPNESS)
	channels = [
		channel.point(
			lambda value, scale=scale: min(255, round(value * scale))
		)
		for channel, scale in zip(rgb.split(), ADVISOR_PAPER_GRADE_CHANNEL_SCALE)
	]
	rgb = Image.merge("RGB", channels)
	graded = rgb.convert("RGBA")
	graded.putalpha(alpha)
	return graded


def advisor_paper_composition_alpha(alpha: Image.Image) -> Image.Image:
	"""Make the authored slip visually opaque while preserving its antialias edge."""
	def remap(value: int) -> int:
		if value <= ADVISOR_WINDOW_ALPHA_THRESHOLD:
			return value
		if value <= ADVISOR_PAPER_ALPHA_OUTER_EDGE_MAX_SOURCE:
			return ADVISOR_PAPER_ALPHA_OUTER_EDGE_VALUE
		if value <= ADVISOR_PAPER_ALPHA_INNER_EDGE_MAX_SOURCE:
			return ADVISOR_PAPER_ALPHA_INNER_EDGE_VALUE
		return ADVISOR_PAPER_ALPHA_OPAQUE_VALUE

	return alpha.point(remap)


def layer_palette_metrics(
	layer: Image.Image,
	alpha_threshold: int = 64,
) -> dict[str, object]:
	luminance_values: list[float] = []
	saturation_values: list[float] = []
	red_values: list[int] = []
	green_values: list[int] = []
	blue_values: list[int] = []
	for red, green, blue, alpha in layer.getdata():
		if alpha <= alpha_threshold:
			continue
		red_values.append(red)
		green_values.append(green)
		blue_values.append(blue)
		luminance_values.append((54 * red + 183 * green + 19 * blue) / 256)
		maximum = max(red, green, blue)
		saturation_values.append(
			0.0 if maximum == 0 else (maximum - min(red, green, blue)) / maximum
		)
	if not luminance_values:
		raise ValueError("Advisor layer has no visible palette samples")
	return {
		"mean_luminance": round(sum(luminance_values) / len(luminance_values), 6),
		"mean_saturation": round(sum(saturation_values) / len(saturation_values), 6),
		"mean_rgb": [
			round(sum(red_values) / len(red_values), 6),
			round(sum(green_values) / len(green_values), 6),
			round(sum(blue_values) / len(blue_values), 6),
		],
		"alpha_threshold": alpha_threshold,
	}


def geometry_metrics_from_points(
	points: list[tuple[int, int]],
) -> dict[str, object]:
	if not points:
		raise ValueError("Advisor geometry mask has no visible points")
	x_values = [x for x, _ in points]
	y_values = [y for _, y in points]
	bbox = (
		min(x_values),
		min(y_values),
		max(x_values) + 1,
		max(y_values) + 1,
	)
	point_set = set(points)
	top_edge: list[tuple[int, int]] = []
	for x in range(bbox[0], bbox[2]):
		column = [y for y in range(bbox[1], bbox[3]) if (x, y) in point_set]
		if len(column) >= 3:
			top_edge.append((x, min(column)))
	# The generated and vanilla paper slips have an irregular overlapping notch
	# at the far left. Fit the authored top edge after that notch, matching the
	# stable central/right edge seen in all six canonical references.
	left_skip = max(2, len(top_edge) // 5)
	fit_edge = top_edge[left_skip:-1]
	if len(fit_edge) < 3:
		raise ValueError("Advisor paper top edge is too short to measure")
	mean_x = sum(x for x, _ in fit_edge) / len(fit_edge)
	mean_y = sum(y for _, y in fit_edge) / len(fit_edge)
	denominator = sum((x - mean_x) ** 2 for x, _ in fit_edge)
	if denominator == 0:
		raise ValueError("Advisor paper top edge has no measurable horizontal run")
	slope = sum(
		(x - mean_x) * (y - mean_y) for x, y in fit_edge
	) / denominator
	return {
		"bbox_gt_32": list(bbox),
		"width": bbox[2] - bbox[0],
		"height": bbox[3] - bbox[1],
		"area_gt_32": len(points),
		"center": [
			round(sum(x_values) / len(points), 6),
			round(sum(y_values) / len(points), 6),
		],
		"top_edge_image_slope": round(slope, 6),
		"top_edge_image_angle_degrees": round(math.degrees(math.atan(slope)), 6),
	}


def paper_geometry_metrics(paper: Image.Image) -> dict[str, object]:
	alpha = paper.getchannel("A")
	points = [
		(x, y)
		for y in range(ADVISOR_SIZE[1])
		for x in range(ADVISOR_SIZE[0])
		if alpha.getpixel((x, y)) > ADVISOR_WINDOW_ALPHA_THRESHOLD
	]
	metrics = geometry_metrics_from_points(points)
	bbox = metrics["bbox_gt_32"]
	center = metrics["center"]
	if (
		any(
			not lower <= int(value) <= upper
			for value, (lower, upper) in zip(
				bbox,
				((29, 31), (25, 27), (56, 58), (57, 59)),
			)
		)
		or not 26 <= int(metrics["width"]) <= 28
		or not 31 <= int(metrics["height"]) <= 33
		or not 710 <= int(metrics["area_gt_32"]) <= 760
		or not 3.25 <= float(metrics["top_edge_image_angle_degrees"]) <= 5.25
		or not 0.0568 <= float(metrics["top_edge_image_slope"]) <= 0.0919
		or not 42.2 <= float(center[0]) <= 43.2
		or not 40.8 <= float(center[1]) <= 41.9
	):
		raise ValueError(
			"Advisor paper geometry does not match the six-reference vanilla dossier "
			f"family: {metrics}"
		)
	return metrics


def canonical_paper_family_metrics(
	references: list[Image.Image],
) -> dict[str, object]:
	if len(references) != len(ADVISOR_REFERENCE_NAMES):
		raise ValueError("Canonical advisor paper calibration requires all six references")
	if any(reference.size != ADVISOR_SIZE for reference in references):
		raise ValueError("Canonical advisor paper calibration references must be 65x67")
	# These bands are the independently measured mean of the six frozen bundled
	# vanilla references. Their hashes are emitted with every candidate, so any
	# reference replacement invalidates downstream review evidence.
	return {
		key: list(value) if isinstance(value, list) else value
		for key, value in ADVISOR_CANONICAL_PAPER_FAMILY.items()
	}


def enclosed_alpha_window(
	frame: Image.Image,
) -> tuple[Image.Image, tuple[int, int, int, int], int]:
	alpha = frame.getchannel("A")
	width, height = alpha.size
	transparent = [
		value <= ADVISOR_WINDOW_ALPHA_THRESHOLD for value in alpha.getdata()
	]
	exterior = [False] * (width * height)
	stack: list[tuple[int, int]] = []
	for x in range(width):
		stack.extend(((x, 0), (x, height - 1)))
	for y in range(1, height - 1):
		stack.extend(((0, y), (width - 1, y)))
	while stack:
		x, y = stack.pop()
		index = y * width + x
		if exterior[index] or not transparent[index]:
			continue
		exterior[index] = True
		if x:
			stack.append((x - 1, y))
		if x + 1 < width:
			stack.append((x + 1, y))
		if y:
			stack.append((x, y - 1))
		if y + 1 < height:
			stack.append((x, y + 1))

	interior_points = [
		(index % width, index // width)
		for index, is_transparent in enumerate(transparent)
		if is_transparent and not exterior[index]
	]
	if not interior_points:
		raise ValueError(
			"Advisor frame alpha does not contain a closed portrait window"
		)
	window_bbox = (
		min(x for x, _ in interior_points),
		min(y for _, y in interior_points),
		max(x for x, _ in interior_points) + 1,
		max(y for _, y in interior_points) + 1,
	)
	window_width = window_bbox[2] - window_bbox[0]
	window_height = window_bbox[3] - window_bbox[1]
	window_area = len(interior_points)
	window_fill = window_area / (window_width * window_height)
	if not (
		32 <= window_width <= 38
		and 49 <= window_height <= 53
		and 4 <= window_bbox[0] <= 8
		and 4 <= window_bbox[1] <= 9
		and 40 <= window_bbox[2] <= 44
		and 55 <= window_bbox[3] <= 59
		and window_fill >= 0.80
	):
		raise ValueError(
			"Advisor frame portrait window is not the canonical narrow native-size "
			f"window: bbox={window_bbox}, area={window_area}, fill={window_fill:.3f}"
		)
	mask_values = [0] * (width * height)
	for x, y in interior_points:
		mask_values[y * width + x] = 255
	window_mask = Image.new("L", ADVISOR_SIZE)
	window_mask.putdata(mask_values)
	return window_mask, window_bbox, window_area


def alpha_shadow(layer: Image.Image, opacity: float, blur: float) -> Image.Image:
	alpha = layer.getchannel("A").point(lambda value: round(value * opacity))
	shadow = Image.new("RGBA", layer.size, (0, 0, 0, 255))
	shadow.putalpha(alpha.filter(ImageFilter.GaussianBlur(blur)))
	return shadow


def composite_alpha_shadow(
	canvas: Image.Image,
	alpha: Image.Image,
	offset: tuple[int, int],
	opacity: float,
	blur: float,
) -> None:
	layer = Image.new("RGBA", ADVISOR_SIZE, (0, 0, 0, 255))
	layer.putalpha(alpha)
	shadow = alpha_shadow(layer, opacity, blur)
	canvas.alpha_composite(shadow, offset)


def fit_advisor_portrait(
	source_crop: Image.Image,
	source_kind: str,
	seed_text: str,
	crop_box: tuple[int, int, int, int],
	face_box: tuple[int, int, int, int],
	window_bbox: tuple[int, int, int, int],
) -> tuple[Image.Image, tuple[float, float, float, float], tuple[float, float, float, float]]:
	window_width = window_bbox[2] - window_bbox[0]
	window_height = window_bbox[3] - window_bbox[1]
	source_width, source_height = source_crop.size
	target_ratio = window_width / window_height
	source_ratio = source_width / source_height
	if source_ratio > target_ratio:
		fit_height = float(source_height)
		fit_width = fit_height * target_ratio
		fit_left = (source_width - fit_width) * 0.5
		fit_top = 0.0
	else:
		fit_width = float(source_width)
		fit_height = fit_width / target_ratio
		fit_left = 0.0
		fit_top = (source_height - fit_height) * 0.38
	fit_box = (fit_left, fit_top, fit_left + fit_width, fit_top + fit_height)
	portrait = source_crop.resize(
		(window_width, window_height),
		Image.Resampling.LANCZOS,
		box=fit_box,
	)
	portrait = hoi4_finish(portrait, source_kind, seed_text + ":advisor")
	portrait = grade_advisor_portrait(portrait)

	local_face = (
		face_box[0] - crop_box[0],
		face_box[1] - crop_box[1],
		face_box[2] - crop_box[0],
		face_box[3] - crop_box[1],
	)
	scale_x = window_width / fit_width
	scale_y = window_height / fit_height
	mapped_face = (
		window_bbox[0] + (local_face[0] - fit_left) * scale_x,
		window_bbox[1] + (local_face[1] - fit_top) * scale_y,
		window_bbox[0] + (local_face[2] - fit_left) * scale_x,
		window_bbox[1] + (local_face[3] - fit_top) * scale_y,
	)
	return portrait, mapped_face, fit_box


def validate_face_placement(
	mapped_face: tuple[float, float, float, float],
	window_bbox: tuple[int, int, int, int],
	paper: Image.Image,
) -> dict[str, object]:
	left, top, right, bottom = mapped_face
	width = right - left
	height = bottom - top
	center_x = (left + right) / 2
	center_y = (top + bottom) / 2
	if not (
		ADVISOR_FACE_WIDTH_RANGE[0] <= width <= ADVISOR_FACE_WIDTH_RANGE[1]
		and ADVISOR_FACE_HEIGHT_RANGE[0] <= height <= ADVISOR_FACE_HEIGHT_RANGE[1]
		and ADVISOR_FACE_CENTER_X_RANGE[0] <= center_x <= ADVISOR_FACE_CENTER_X_RANGE[1]
		and ADVISOR_FACE_CENTER_Y_RANGE[0] <= center_y <= ADVISOR_FACE_CENTER_Y_RANGE[1]
	):
		raise ValueError(
			"Advisor face placement does not match the six native vanilla examples: "
			f"mapped bbox={tuple(round(value, 2) for value in mapped_face)}, "
			f"size=({width:.2f}, {height:.2f}), center=({center_x:.2f}, {center_y:.2f})"
		)
	intersection_left = max(left, window_bbox[0])
	intersection_top = max(top, window_bbox[1])
	intersection_right = min(right, window_bbox[2])
	intersection_bottom = min(bottom, window_bbox[3])
	intersection_area = max(0.0, intersection_right - intersection_left) * max(
		0.0, intersection_bottom - intersection_top
	)
	if intersection_area / (width * height) < 0.90:
		raise ValueError("Advisor face box is clipped by the generated frame window")

	integer_box = (
		max(0, int(left)),
		max(0, int(top)),
		min(ADVISOR_SIZE[0], int(math.ceil(right))),
		min(ADVISOR_SIZE[1], int(math.ceil(bottom))),
	)
	face_area = max(1, (integer_box[2] - integer_box[0]) * (integer_box[3] - integer_box[1]))
	paper_alpha = paper.getchannel("A").crop(integer_box)
	paper_overlap_ratio = sum(value > 32 for value in paper_alpha.getdata()) / face_area
	if paper_overlap_ratio > 0.18:
		raise ValueError(
			"Generated dossier paper obscures the native-size face placement: "
			f"overlap ratio {paper_overlap_ratio:.3f}"
		)
	return {
		"mapped_bbox": [round(value, 4) for value in mapped_face],
		"width": round(width, 4),
		"height": round(height, 4),
		"center": [round(center_x, 4), round(center_y, 4)],
		"paper_overlap_ratio": round(paper_overlap_ratio, 6),
	}


def advisor_face_palette_metrics(
	portrait: Image.Image,
	mapped_face: tuple[float, float, float, float],
	window_bbox: tuple[int, int, int, int],
) -> dict[str, float]:
	local_box = (
		max(0, int(math.floor(mapped_face[0] - window_bbox[0]))),
		max(0, int(math.floor(mapped_face[1] - window_bbox[1]))),
		min(portrait.width, int(math.ceil(mapped_face[2] - window_bbox[0]))),
		min(portrait.height, int(math.ceil(mapped_face[3] - window_bbox[1]))),
	)
	metrics = layer_palette_metrics(portrait.crop(local_box))
	if not (
		80 <= metrics["mean_luminance"] <= 175
		and 0.08 <= metrics["mean_saturation"] <= 0.38
	):
		raise ValueError(
			"Advisor face values do not remain readable in the vanilla small-card "
			f"range: bbox={local_box}, metrics={metrics}"
		)
	metrics["local_bbox_left"] = float(local_box[0])
	metrics["local_bbox_top"] = float(local_box[1])
	metrics["local_bbox_right"] = float(local_box[2])
	metrics["local_bbox_bottom"] = float(local_box[3])
	return metrics


def make_advisor(
	source_crop: Image.Image,
	source_kind: str,
	seed_text: str,
	frame_overlay: Image.Image,
	paper_overlay: Image.Image,
	crop_box: tuple[int, int, int, int],
	face_box: tuple[int, int, int, int],
) -> tuple[Image.Image, dict[str, object]]:
	frame, frame_source_bbox = normalize_generated_layer(
		frame_overlay,
		ADVISOR_FRAME_SIZE,
		ADVISOR_FRAME_POSITION,
		ADVISOR_FRAME_ANGLE,
	)
	authored_frame_palette = frame_palette_metrics(frame, "authored")
	frame = grade_advisor_frame(frame)
	raw_frame_alpha = frame.getchannel("A")
	frame_coverage = alpha_coverage(raw_frame_alpha, 32)
	if not 0.09 <= frame_coverage <= 0.26:
		raise ValueError(
			f"Advisor frame native coverage {frame_coverage:.3f} is outside vanilla bounds"
		)
	final_frame_palette = frame_palette_metrics(frame, "final")
	frame_grade_delta_luminance = abs(
		float(authored_frame_palette["mean_luminance"])
		- float(final_frame_palette["mean_luminance"])
	)
	frame_grade_delta_saturation = abs(
		float(authored_frame_palette["mean_saturation"])
		- float(final_frame_palette["mean_saturation"])
	)
	if frame_grade_delta_luminance > 15 or frame_grade_delta_saturation > 0.09:
		raise ValueError(
			"Advisor frame grading exceeds the restrained vanilla calibration delta: "
			f"luminance={frame_grade_delta_luminance:.4f}, "
			f"saturation={frame_grade_delta_saturation:.4f}"
		)
	window_mask, window_bbox, window_area = enclosed_alpha_window(frame)
	frame_alpha = advisor_frame_composition_alpha(raw_frame_alpha)
	frame.putalpha(frame_alpha)

	paper, paper_source_bbox = normalize_generated_layer(
		paper_overlay,
		ADVISOR_PAPER_SIZE,
		ADVISOR_PAPER_POSITION,
		ADVISOR_PAPER_ANGLE,
	)
	paper = grade_advisor_paper(paper)
	raw_paper_alpha = paper.getchannel("A")
	paper_palette = layer_palette_metrics(paper, ADVISOR_WINDOW_ALPHA_THRESHOLD)
	paper_geometry = paper_geometry_metrics(paper)
	paper_mean_rgb = paper_palette["mean_rgb"]
	if not (
		204 <= paper_palette["mean_luminance"] <= 214
		and 0.190 <= paper_palette["mean_saturation"] <= 0.245
		and 220 <= paper_mean_rgb[0] <= 231
		and 202 <= paper_mean_rgb[1] <= 213
		and 171 <= paper_mean_rgb[2] <= 183
		and 12 <= paper_mean_rgb[0] - paper_mean_rgb[1] <= 24
		and 24 <= paper_mean_rgb[1] - paper_mean_rgb[2] <= 38
	):
		raise ValueError(
			"Advisor paper does not match the pale low-chroma vanilla note: "
			f"metrics were {paper_palette}"
		)
	paper_coverage = alpha_coverage(raw_paper_alpha, 32)
	if not 0.163 <= paper_coverage <= 0.175:
		raise ValueError(
			f"Advisor paper native coverage {paper_coverage:.3f} is outside vanilla bounds"
		)
	paper_window_overlap = sum(
		paper_value > 32 and window_value > 0
		for paper_value, window_value in zip(
			raw_paper_alpha.getdata(), window_mask.getdata()
		)
	) / window_area
	if not 0.12 <= paper_window_overlap <= 0.32:
		raise ValueError(
			"Advisor paper does not overlap the portrait window like vanilla: "
			f"ratio={paper_window_overlap:.3f}"
		)
	paper_alpha = advisor_paper_composition_alpha(raw_paper_alpha)
	paper_support_alpha = [
		mapped_value
		for raw_value, mapped_value in zip(raw_paper_alpha.getdata(), paper_alpha.getdata())
		if raw_value > ADVISOR_WINDOW_ALPHA_THRESHOLD
	]
	paper_fully_opaque_ratio = sum(
		value == ADVISOR_PAPER_ALPHA_OPAQUE_VALUE for value in paper_support_alpha
	) / len(paper_support_alpha)
	paper_mean_alpha = sum(paper_support_alpha) / len(paper_support_alpha)
	paper_opacity = {
		"support_pixel_count": len(paper_support_alpha),
		"minimum_alpha": min(paper_support_alpha),
		"maximum_alpha": max(paper_support_alpha),
		"mean_alpha": round(paper_mean_alpha, 6),
		"fully_opaque_ratio": round(paper_fully_opaque_ratio, 6),
		"outer_edge_ratio": round(
			sum(value <= ADVISOR_PAPER_ALPHA_OUTER_EDGE_VALUE for value in paper_support_alpha)
			/ len(paper_support_alpha),
			6,
		),
	}
	if not (
		paper_opacity["minimum_alpha"] >= ADVISOR_PAPER_ALPHA_OUTER_EDGE_VALUE
		and paper_opacity["maximum_alpha"] == ADVISOR_PAPER_ALPHA_OPAQUE_VALUE
		and paper_mean_alpha >= 254.4
		and paper_fully_opaque_ratio >= 0.94
		and paper_opacity["outer_edge_ratio"] <= 0.01
	):
		raise ValueError(
			"Advisor paper must remain visually opaque after composition; "
			f"metrics were {paper_opacity}"
		)
	paper.putalpha(paper_alpha)

	portrait, mapped_face, portrait_fit_box = fit_advisor_portrait(
		source_crop,
		source_kind,
		seed_text,
		crop_box,
		face_box,
		window_bbox,
	)
	face_metrics = validate_face_placement(mapped_face, window_bbox, paper)
	face_palette = advisor_face_palette_metrics(portrait, mapped_face, window_bbox)
	portrait_layer = Image.new("RGBA", ADVISOR_SIZE, (0, 0, 0, 0))
	portrait_layer.alpha_composite(portrait, (window_bbox[0], window_bbox[1]))
	portrait_layer.putalpha(
		ImageChops.multiply(portrait_layer.getchannel("A"), window_mask)
	)

	canvas = Image.new("RGBA", ADVISOR_SIZE, (0, 0, 0, 0))
	card_alpha = ImageChops.lighter(frame_alpha, window_mask)
	# Vanilla cards combine a broad low-opacity shadow with a one-pixel hard
	# contact shadow. Both are derived exclusively from the generated layer alpha.
	for offset, opacity, blur in ADVISOR_CARD_SHADOW_LAYERS:
		composite_alpha_shadow(canvas, card_alpha, offset, opacity, blur)
	canvas.alpha_composite(portrait_layer)
	canvas.alpha_composite(frame)
	for offset, opacity, blur in ADVISOR_PAPER_SHADOW_LAYERS:
		composite_alpha_shadow(canvas, paper_alpha, offset, opacity, blur)
	canvas.alpha_composite(paper)

	return canvas, {
		"frame_source_visible_bbox": list(frame_source_bbox),
		"frame_native_size": list(ADVISOR_FRAME_SIZE),
		"frame_native_position": list(ADVISOR_FRAME_POSITION),
		"frame_angle_degrees": ADVISOR_FRAME_ANGLE,
		"frame_native_alpha_coverage_gt_32": round(frame_coverage, 6),
		"frame_composition_alpha_coverage_gt_32": round(
			alpha_coverage(frame_alpha, 32), 6
		),
		"authored_frame_palette": authored_frame_palette,
		"final_frame_palette": final_frame_palette,
		"frame_grade_delta": {
			"mean_luminance": round(frame_grade_delta_luminance, 6),
			"mean_saturation": round(frame_grade_delta_saturation, 6),
		},
		"portrait_window_bbox": list(window_bbox),
		"portrait_window_area": window_area,
		"portrait_fit_source_box": [round(value, 4) for value in portrait_fit_box],
		"face_placement": face_metrics,
		"face_palette": face_palette,
		"paper_source_visible_bbox": list(paper_source_bbox),
		"paper_native_size": list(ADVISOR_PAPER_SIZE),
		"paper_native_position": list(ADVISOR_PAPER_POSITION),
		"paper_angle_degrees": ADVISOR_PAPER_ANGLE,
		"paper_geometry": paper_geometry,
		"paper_palette": paper_palette,
		"paper_composition_alpha_coverage_gt_32": round(
			alpha_coverage(paper_alpha, 32), 6
		),
		"paper_composition_opacity": paper_opacity,
		"paper_window_overlap_ratio": round(paper_window_overlap, 6),
		"shadow_contract": "alpha_derived_soft_plus_hard_contact_shadows",
	}


def validate_advisor_output(
	finished: Image.Image,
	reference_dir: Path,
	composition_metadata: dict[str, object],
) -> dict[str, object]:
	if finished.size != ADVISOR_SIZE:
		raise ValueError(f"Advisor output must be exactly 65x67, got {finished.size}")
	alpha = finished.getchannel("A")
	if alpha.getextrema() != (0, 255):
		raise ValueError(
			f"Advisor output needs transparent and opaque pixels, got {alpha.getextrema()}"
		)
	corner_values = [
		alpha.getpixel((0, 0)),
		alpha.getpixel((ADVISOR_SIZE[0] - 1, 0)),
		alpha.getpixel((0, ADVISOR_SIZE[1] - 1)),
		alpha.getpixel((ADVISOR_SIZE[0] - 1, ADVISOR_SIZE[1] - 1)),
	]
	if any(corner_values):
		raise ValueError(
			f"Advisor output must keep all four canvas corners transparent: {corner_values}"
		)

	reference_metrics: list[dict[str, object]] = []
	reference_masks: list[list[bool]] = []
	reference_images: list[Image.Image] = []
	for name in ADVISOR_REFERENCE_NAMES:
		path = reference_dir / name
		if not path.is_file():
			raise FileNotFoundError(f"Missing canonical advisor reference: {path}")
		with Image.open(path) as image:
			reference = image.convert("RGBA")
		if reference.size != ADVISOR_SIZE:
			raise ValueError(f"Canonical advisor reference is not 65x67: {path}")
		reference_images.append(reference)
		reference_alpha = reference.getchannel("A")
		reference_masks.append(
			[value > ADVISOR_WINDOW_ALPHA_THRESHOLD for value in reference_alpha.getdata()]
		)
		reference_metrics.append(
			{
				"name": name,
				"sha256": sha256_file(path),
				"bbox_gt_32": list(
					threshold_bbox(reference_alpha, ADVISOR_WINDOW_ALPHA_THRESHOLD)
				),
				"coverage_gt_0": alpha_coverage(reference_alpha, 0),
				"coverage_gt_8": alpha_coverage(reference_alpha, 8),
				"coverage_gt_32": alpha_coverage(reference_alpha, 32),
				"coverage_gt_128": alpha_coverage(reference_alpha, 128),
				"coverage_gt_224": alpha_coverage(reference_alpha, 224),
				"coverage_gt_254": alpha_coverage(reference_alpha, 254),
				"semitransparent_count": sum(
					0 < value < 255 for value in reference_alpha.getdata()
				),
				"binary_centroid_gt_32": list(
					binary_alpha_centroid(reference_alpha, 32)
				),
			}
		)

	thresholds = tuple(ADVISOR_ALPHA_COVERAGE_GATES)
	candidate_coverage = {
		f"coverage_gt_{threshold}": alpha_coverage(alpha, threshold)
		for threshold in thresholds
	}
	reference_means = {
		f"coverage_gt_{threshold}": sum(
			float(metrics[f"coverage_gt_{threshold}"])
			for metrics in reference_metrics
		)
		/ len(reference_metrics)
		for threshold in thresholds
	}
	deltas = {
		key: abs(candidate_coverage[key] - reference_means[key])
		for key in candidate_coverage
	}
	failed_coverage_gates = {
		threshold: candidate_coverage[f"coverage_gt_{threshold}"]
		for threshold, (lower, upper) in ADVISOR_ALPHA_COVERAGE_GATES.items()
		if not lower
		<= candidate_coverage[f"coverage_gt_{threshold}"]
		<= upper
	}
	if failed_coverage_gates:
		raise ValueError(
			"Advisor alpha coverage is outside the measured six-reference vanilla "
			f"bands: failed={failed_coverage_gates}, candidate={candidate_coverage}"
		)
	semitransparent_count = sum(0 < value < 255 for value in alpha.getdata())
	if not (
		ADVISOR_ALPHA_SEMITRANSPARENT_RANGE[0]
		<= semitransparent_count
		<= ADVISOR_ALPHA_SEMITRANSPARENT_RANGE[1]
	):
		raise ValueError(
			"Advisor semitransparent pixel count is outside the vanilla family: "
			f"{semitransparent_count}"
		)
	candidate_bbox = threshold_bbox(alpha, 32)
	if any(
		not lower <= value <= upper
		for value, (lower, upper) in zip(
			candidate_bbox, ADVISOR_ALPHA_BBOX_RANGES
		)
	):
		raise ValueError(
			"Advisor native alpha bbox does not match the vanilla footprint: "
			f"candidate={candidate_bbox}, ranges={ADVISOR_ALPHA_BBOX_RANGES}"
		)
	candidate_centroid = binary_alpha_centroid(alpha, 32)
	if not (
		ADVISOR_ALPHA_CENTROID_X_RANGE[0]
		<= candidate_centroid[0]
		<= ADVISOR_ALPHA_CENTROID_X_RANGE[1]
		and ADVISOR_ALPHA_CENTROID_Y_RANGE[0]
		<= candidate_centroid[1]
		<= ADVISOR_ALPHA_CENTROID_Y_RANGE[1]
	):
		raise ValueError(
			"Advisor binary alpha centroid is outside the vanilla footprint: "
			f"candidate={candidate_centroid}"
		)

	candidate_mask = [
		value > ADVISOR_WINDOW_ALPHA_THRESHOLD for value in alpha.getdata()
	]
	jaccard_scores: list[float] = []
	for reference_mask in reference_masks:
		intersection = sum(
			candidate and reference
			for candidate, reference in zip(candidate_mask, reference_mask)
		)
		union = sum(
			candidate or reference
			for candidate, reference in zip(candidate_mask, reference_mask)
		)
		jaccard_scores.append(intersection / max(1, union))
	row_counts = [
		sum(candidate_mask[y * ADVISOR_SIZE[0] + x] for x in range(ADVISOR_SIZE[0]))
		for y in range(ADVISOR_SIZE[1])
	]
	column_counts = [
		sum(candidate_mask[y * ADVISOR_SIZE[0] + x] for y in range(ADVISOR_SIZE[1]))
		for x in range(ADVISOR_SIZE[0])
	]
	reference_row_means = [
		sum(
			sum(mask[y * ADVISOR_SIZE[0] + x] for x in range(ADVISOR_SIZE[0]))
			for mask in reference_masks
		)
		/ len(reference_masks)
		for y in range(ADVISOR_SIZE[1])
	]
	reference_column_means = [
		sum(
			sum(mask[y * ADVISOR_SIZE[0] + x] for y in range(ADVISOR_SIZE[1]))
			for mask in reference_masks
		)
		/ len(reference_masks)
		for x in range(ADVISOR_SIZE[0])
	]
	row_mae = sum(
		abs(candidate - reference)
		for candidate, reference in zip(row_counts, reference_row_means)
	) / (ADVISOR_SIZE[0] * ADVISOR_SIZE[1])
	column_mae = sum(
		abs(candidate - reference)
		for candidate, reference in zip(column_counts, reference_column_means)
	) / (ADVISOR_SIZE[0] * ADVISOR_SIZE[1])
	if min(jaccard_scores) < 0.925 or row_mae > 0.03 or column_mae > 0.05:
		raise ValueError(
			"Advisor row/column alpha envelope is not the vanilla dossier silhouette: "
			f"jaccard={jaccard_scores}, row_mae={row_mae:.4f}, "
			f"column_mae={column_mae:.4f}"
		)

	canonical_paper = canonical_paper_family_metrics(reference_images)
	candidate_paper = composition_metadata["paper_geometry"]
	candidate_paper_palette = composition_metadata["paper_palette"]
	canonical_paper_bbox = canonical_paper["bbox_gt_32"]
	candidate_paper_bbox = candidate_paper["bbox_gt_32"]
	canonical_paper_center = canonical_paper["center"]
	candidate_paper_center = candidate_paper["center"]
	paper_area_delta_ratio = abs(
		float(candidate_paper["area_gt_32"])
		- float(canonical_paper["area_gt_32"])
	) / float(canonical_paper["area_gt_32"])
	paper_angle_delta = abs(
		float(candidate_paper["top_edge_image_angle_degrees"])
		- float(canonical_paper["top_edge_image_angle_degrees"])
	)
	paper_luminance_delta = abs(
		float(candidate_paper_palette["mean_luminance"])
		- float(canonical_paper["mean_luminance"])
	)
	paper_saturation_delta = abs(
		float(candidate_paper_palette["mean_saturation"])
		- float(canonical_paper["mean_saturation"])
	)
	if (
		any(
			abs(int(candidate) - int(canonical)) > 1
			for candidate, canonical in zip(candidate_paper_bbox, canonical_paper_bbox)
		)
		or paper_area_delta_ratio > 0.12
		or paper_angle_delta > 1.75
		or any(
			abs(float(candidate) - float(canonical)) > 1.5
			for candidate, canonical in zip(candidate_paper_center, canonical_paper_center)
		)
		or paper_luminance_delta > 10
		or paper_saturation_delta > 0.06
	):
		raise ValueError(
			"Advisor paper does not match the measured geometry and values of all six "
			"canonical vanilla references: "
			f"candidate_geometry={candidate_paper}, canonical={canonical_paper}, "
			f"candidate_palette={candidate_paper_palette}"
		)

	return {
		"size": list(finished.size),
		"alpha_extrema": list(alpha.getextrema()),
		"transparent_corners": corner_values,
		"bbox_gt_32": list(candidate_bbox),
		"binary_centroid_gt_32": [
			round(candidate_centroid[0], 6),
			round(candidate_centroid[1], 6),
		],
		"semitransparent_count": semitransparent_count,
		"coverage": {key: round(value, 6) for key, value in candidate_coverage.items()},
		"coverage_gates": {
			f"coverage_gt_{threshold}": list(bounds)
			for threshold, bounds in ADVISOR_ALPHA_COVERAGE_GATES.items()
		},
		"canonical_mean_coverage": {
			key: round(value, 6) for key, value in reference_means.items()
		},
		"canonical_absolute_delta": {
			key: round(value, 6) for key, value in deltas.items()
		},
		"canonical_alpha_jaccard": [round(value, 6) for value in jaccard_scores],
		"canonical_row_occupancy_mae": round(row_mae, 6),
		"canonical_column_occupancy_mae": round(column_mae, 6),
		"candidate_paper_geometry": candidate_paper,
		"canonical_paper_family": canonical_paper,
		"canonical_paper_deltas": {
			"area_ratio": round(paper_area_delta_ratio, 6),
			"angle_degrees": round(paper_angle_delta, 6),
			"mean_luminance": round(paper_luminance_delta, 6),
			"mean_saturation": round(paper_saturation_delta, 6),
		},
		"canonical_references": [
			{
				"path": str(reference_dir / str(metrics["name"])),
				"sha256": str(metrics["sha256"]),
			}
			for metrics in reference_metrics
		],
	}


def checker(size: tuple[int, int], tile: int = 8) -> Image.Image:
	background = Image.new("RGBA", size, (92, 92, 92, 255))
	draw = ImageDraw.Draw(background)
	for y in range(0, size[1], tile):
		for x in range(0, size[0], tile):
			if (x // tile + y // tile) % 2:
				draw.rectangle((x, y, min(x + tile - 1, size[0] - 1), min(y + tile - 1, size[1] - 1)), fill=(132, 132, 132, 255))
	return background


def make_review_sheet(
	source_crop: Image.Image,
	finished: Image.Image,
	mode: str,
	reference_dir: Path,
	output: Path,
) -> None:
	if mode == "advisor":
		items: list[tuple[str, Image.Image]] = [
			(
				"explicit source crop",
				ImageOps.fit(source_crop, ADVISOR_SIZE, Image.Resampling.LANCZOS),
			),
			("processed candidate", finished),
		]
		for name in ADVISOR_REFERENCE_NAMES:
			path = reference_dir / name
			if not path.is_file():
				raise FileNotFoundError(f"Missing review reference: {path}")
			with Image.open(path) as image:
				items.append((name.removesuffix(".png"), image.convert("RGBA")))

		scale = 4
		native_width, native_height = ADVISOR_SIZE
		enlarged_size = (native_width * scale, native_height * scale)
		cell_width = enlarged_size[0] + 24
		cell_height = native_height + enlarged_size[1] + 72
		sheet = Image.new(
			"RGBA",
			(cell_width * len(items), cell_height),
			(28, 30, 32, 255),
		)
		draw = ImageDraw.Draw(sheet)
		for index, (label, image) in enumerate(items):
			native = checker(ADVISOR_SIZE)
			native.alpha_composite(
				ImageOps.fit(image, ADVISOR_SIZE, Image.Resampling.LANCZOS)
			)
			enlarged = native.resize(enlarged_size, Image.Resampling.NEAREST)
			x = index * cell_width + 12
			native_x = x + (enlarged_size[0] - native_width) // 2
			sheet.alpha_composite(native, (native_x, 10))
			sheet.alpha_composite(enlarged, (x, native_height + 22))
			draw.text((x, native_height + enlarged_size[1] + 34), label, fill=(236, 236, 232, 255))
		output.parent.mkdir(parents=True, exist_ok=True)
		sheet.save(output)
		if not output.is_file() or output.stat().st_size == 0:
			raise RuntimeError(f"Advisor comparison sheet was not generated: {output}")
		return

	reference_names = ("den_thorvald_stauning.png", "fin_carl_mannerheim.png")
	display_size = LEADER_SIZE
	scale = 2

	items: list[tuple[str, Image.Image]] = [
		("explicit source crop", ImageOps.fit(source_crop, display_size, Image.Resampling.LANCZOS)),
		("processed candidate", finished),
	]
	for name in reference_names:
		path = reference_dir / name
		if not path.is_file():
			raise FileNotFoundError(f"Missing review reference: {path}")
		with Image.open(path) as image:
			items.append((name.removeprefix("vanilla_").removesuffix(".png"), image.convert("RGBA")))

	cell_width = display_size[0] * scale + 24
	cell_height = display_size[1] * scale + 44
	sheet = Image.new("RGBA", (cell_width * len(items), cell_height), (28, 30, 32, 255))
	draw = ImageDraw.Draw(sheet)
	for index, (label, image) in enumerate(items):
		preview = ImageOps.fit(image, display_size, Image.Resampling.LANCZOS).resize(
			(display_size[0] * scale, display_size[1] * scale),
			Image.Resampling.NEAREST if mode == "advisor" else Image.Resampling.LANCZOS,
		)
		base = checker(preview.size)
		base.alpha_composite(preview)
		x = index * cell_width + 12
		sheet.alpha_composite(base, (x, 10))
		draw.text((x, preview.height + 20), label, fill=(236, 236, 232, 255))
	output.parent.mkdir(parents=True, exist_ok=True)
	sheet.save(output)


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("mode", choices=("leader", "advisor"))
	parser.add_argument("source", type=Path)
	parser.add_argument("output", type=Path)
	parser.add_argument(
		"--crop",
		nargs=4,
		type=int,
		metavar=("LEFT", "TOP", "RIGHT", "BOTTOM"),
		required=True,
		help="Required head-and-shoulders crop in source pixels",
	)
	parser.add_argument(
		"--source-kind",
		choices=("real", "fictional", "collective", "symbolic"),
		required=True,
	)
	parser.add_argument(
		"--face-box",
		nargs=4,
		type=int,
		metavar=("LEFT", "TOP", "RIGHT", "BOTTOM"),
		help=(
			"Advisor-only visible face bounds in original source pixels; required "
			"for native-size scale and placement validation"
		),
	)
	parser.add_argument("--review-sheet", type=Path, required=True)
	parser.add_argument("--metadata", type=Path)
	parser.add_argument("--reference-dir", type=Path)
	parser.add_argument(
		"--advisor-overlay-manifest",
		type=Path,
		help=(
			"Required advisor-mode manifest that pins the approved ImageGen frame, "
			"paper, and skill-local canonical style-reference hashes"
		),
	)
	parser.add_argument(
		"--advisor-frame-overlay",
		type=Path,
		help="Required alpha-processed ImageGen frame overlay for advisor mode",
	)
	parser.add_argument(
		"--advisor-frame-source",
		type=Path,
		help="Required retained full-resolution ImageGen source for the frame overlay",
	)
	parser.add_argument(
		"--advisor-paper-overlay",
		type=Path,
		help="Required alpha-processed shadowless ImageGen paper overlay for advisor mode",
	)
	parser.add_argument(
		"--advisor-paper-source",
		type=Path,
		help="Required retained full-resolution shadowless ImageGen paper source",
	)
	return parser.parse_args()


def main() -> None:
	args = parse_args()
	if not args.source.is_file():
		raise FileNotFoundError(args.source)
	with Image.open(args.source) as image:
		source = image.convert("RGBA")
	crop_box = parse_crop(args.crop, source)
	source_crop = source.crop(crop_box)
	face_box: tuple[int, int, int, int] | None = None
	render_version = LEADER_RENDER_VERSION if args.mode == "leader" else ADVISOR_RENDER_VERSION
	source_sha256 = sha256_file(args.source)
	if args.mode == "leader":
		seed_record = deterministic_seed_record(
			source,
			crop_box,
			None,
			args.source_kind,
			args.mode,
			render_version,
			None,
			None,
		)
		seed_text = str(seed_record["payload_sha256"])
		finished = make_leader(source_crop, args.source_kind, seed_text)
		reference_dir = args.reference_dir or REFERENCE_ROOT / "leaders"
		overlay_metadata = None
		composition_metadata = None
		validation_metadata = None
		render_configuration = None
	else:
		if args.face_box is None:
			raise ValueError("advisor mode requires --face-box in original source pixels")
		face_box = parse_face_box(args.face_box, source, crop_box)
		if args.advisor_frame_overlay is None or args.advisor_frame_source is None:
			raise ValueError(
				"advisor mode requires --advisor-frame-source and --advisor-frame-overlay; "
				"the processor never draws fallback dossier artwork"
			)
		if args.advisor_paper_overlay is None or args.advisor_paper_source is None:
			raise ValueError(
				"advisor mode requires --advisor-paper-source and --advisor-paper-overlay; "
				"paperless output is not the calibrated vanilla dossier family"
			)
		if args.advisor_overlay_manifest is None:
			raise ValueError(
				"advisor mode requires --advisor-overlay-manifest; unpinned overlay "
				"sources are not a reproducible ImageGen-authored dossier kit"
			)
		canonical_advisor_references = (REFERENCE_ROOT / "advisors").resolve()
		if (
			args.reference_dir is not None
			and args.reference_dir.resolve() != canonical_advisor_references
		):
			raise ValueError(
				"advisor mode requires the skill-local canonical advisor references; "
				"do not substitute event-specific style references"
			)
		overlay_manifest_metadata = verify_overlay_manifest(
			args.advisor_overlay_manifest,
			args.advisor_frame_source,
			args.advisor_frame_overlay,
			args.advisor_paper_source,
			args.advisor_paper_overlay,
		)
		frame_overlay, frame_metadata = load_generated_layer(
			args.advisor_frame_overlay,
			args.advisor_frame_source,
			"frame",
		)
		paper_overlay, paper_metadata = load_generated_layer(
			args.advisor_paper_overlay,
			args.advisor_paper_source,
			"paper",
		)
		seed_record = deterministic_seed_record(
			source,
			crop_box,
			face_box,
			args.source_kind,
			args.mode,
			render_version,
			str(frame_metadata["overlay_sha256"]),
			str(paper_metadata["overlay_sha256"]),
		)
		seed_text = str(seed_record["payload_sha256"])
		finished, composition_metadata = make_advisor(
			source_crop,
			args.source_kind,
			seed_text,
			frame_overlay,
			paper_overlay,
			crop_box,
			face_box,
		)
		reference_dir = canonical_advisor_references
		validation_metadata = validate_advisor_output(
			finished,
			reference_dir,
			composition_metadata,
		)
		overlay_metadata = {
			"manifest": overlay_manifest_metadata,
			"frame": frame_metadata,
			"paper": paper_metadata,
		}
		render_configuration = advisor_render_configuration()

	args.output.parent.mkdir(parents=True, exist_ok=True)
	finished.save(args.output)
	make_review_sheet(source_crop, finished, args.mode, reference_dir, args.review_sheet)

	metadata_path = args.metadata or args.output.with_suffix(args.output.suffix + ".json")
	metadata_path.parent.mkdir(parents=True, exist_ok=True)
	metadata = {
		"processor": ".agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py",
		"processor_version": PROCESSOR_VERSION,
		"processor_sha256": sha256_file(Path(__file__).resolve()),
		"render_version": render_version,
		"mode": args.mode,
		"source": str(args.source),
		"source_kind": args.source_kind,
		"crop": list(crop_box),
		"face_box": list(face_box) if face_box is not None else None,
		"output": str(args.output),
		"size": list(finished.size),
		"review_sheet": str(args.review_sheet),
		"reference_dir": str(reference_dir),
		"source_sha256": source_sha256,
		"determinism": seed_record,
		"render_configuration": render_configuration,
		"generated_overlays": overlay_metadata,
		"advisor_composition": composition_metadata,
		"advisor_validation": validation_metadata,
		"composition_contract": (
			"crop_grade_resize_angle_alpha_shadow_composite_validate_export_only; "
			"all visible frame_paper artwork is ImageGen-authored; "
			"no programmatically drawn advisor-card artwork"
			if args.mode == "advisor"
			else "crop_grade_export_only; no programmatically drawn leader subject, emblem, or institutional scene"
		),
		"status": "candidate_requires_visual_approval",
	}
	metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
	main()
