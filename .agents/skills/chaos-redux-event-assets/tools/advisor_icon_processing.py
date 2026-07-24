#!/usr/bin/env python3
"""Finish a style-approved portrait master for HOI4 leader or advisor use.

This tool is a deterministic finishing and presentation step. It does not
invent a person's face or draw advisor-card artwork, and it is not a substitute
for source research or the required visual review against the canonical
event-assets skill references in ``assets/vanilla_reference/portraits/leaders``
``assets/vanilla_reference/portraits/commanders``, and
``assets/vanilla_reference/portraits/advisors``.

Full-size ``leader`` mode keeps the positional mode name for compatibility and
selects a deterministic style family with ``--role-family leader|commander``;
the default is ``leader``. Commander runs must opt into ``--role-family
commander`` so the review sheet and evidence use commander references.

Real people must start from an attributed archival image. Pass an explicit
head-and-shoulders crop, preserve the person's recognisable features, and
reject the result if the source is too weak to survive the HOI4 finish.
Fictional portraits may start from an approved ImageGen master. Advisor mode
also requires separately generated, shadowless frame and paper sources plus
their alpha-processed overlays. The script only crops, grades, resizes, angles,
derives shadows from approved alpha, composites, applies the verified
per-pixel mean alpha envelope of six frozen vanilla advisor references,
validates, and exports those approved sources. It never draws any visible
advisor-card element.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import itertools
import json
import math
import os
import platform
import sys
import tempfile
from pathlib import Path

from PIL import (
	Image,
	ImageChops,
	ImageDraw,
	ImageEnhance,
	ImageFilter,
	ImageOps,
	ImageStat,
	__version__ as PILLOW_VERSION,
)


LEADER_SIZE = (156, 210)
ADVISOR_SIZE = (65, 67)
PROCESSOR_VERSION = "5.0"
LEADER_RENDER_VERSION = "2.0"
ADVISOR_RENDER_VERSION = "5.0"
ADVISOR_SUPPORTED_PYTHON_VERSION = "3.9.12"
ADVISOR_SUPPORTED_PILLOW_VERSION = "11.1.0"
SKILL_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = SKILL_ROOT.parents[2]
REFERENCE_ROOT = SKILL_ROOT / "assets" / "vanilla_reference" / "portraits"
ROLE_FAMILY_REFERENCE_NAMES = {
	"leader": ("den_thorvald_stauning.png", "fin_carl_mannerheim.png"),
	"commander": (
		"eng_bernard_montgomery.png",
		"ger_erwin_von_witzleben.png",
	),
}
ROLE_FAMILY_REFERENCE_DIRS = {
	role_family: REFERENCE_ROOT / f"{role_family}s"
	for role_family in ROLE_FAMILY_REFERENCE_NAMES
}
PROCESSOR_INPUT_CROP_LABEL = "processor input crop"
IMAGEGEN_ALPHA_TOOL_MANIFEST_PATH = "imagegen/scripts/remove_chroma_key.py"
IMAGEGEN_ALPHA_TOOL = (
	Path.home()
	/ ".codex"
	/ "skills"
	/ ".system"
	/ "imagegen"
	/ "scripts"
	/ "remove_chroma_key.py"
)
IMAGEGEN_ALPHA_TOOL_SHA256 = (
	"7e51236919203b61d07ddffdc6e0b5f501a28661003f5851f26ffbb64bdec1ea"
)
IMAGEGEN_ALPHA_TOOL_ARGUMENTS = (
	"--auto-key",
	"border",
	"--soft-matte",
	"--transparent-threshold",
	"12",
	"--opaque-threshold",
	"220",
	"--despill",
	"--force",
)
ADVISOR_REFERENCE_NAMES = (
	"generic_europe_1.png",
	"generic_female_europe.png",
	"generic_asia_1.png",
	"army_small_ger_friedrich_paulus.png",
	"army_small_ger_gunther_von_kluge.png",
	"army_small_ger_erwin_rommel.png",
)
ADVISOR_CANONICAL_ALPHA_METHOD = "rounded_per_pixel_mean_of_six_frozen_vanilla_alpha_channels"
ADVISOR_CANONICAL_ALPHA_SHA256 = "5d33afdd1adc0349e33b52bb141ddd1449107fd34727d19fcc45bcd7809d2993"

# These native placements reproduce the shared 65x67 vanilla dossier-card
# footprint. Generated overlays remain the sole source of visible artwork: the
# processor trims their authored alpha bounds, resizes them, and places them.
ADVISOR_FRAME_SIZE = (40, 58)
ADVISOR_FRAME_POSITION = (1, 1)
ADVISOR_FRAME_ANGLE = 5.0
ADVISOR_FRAME_ALPHA_CAP = 255
ADVISOR_FRAME_GRADE_COLOR = 0.40
ADVISOR_FRAME_GRADE_BRIGHTNESS = 0.48
ADVISOR_FRAME_GRADE_CONTRAST = 1.30
ADVISOR_FRAME_GRADE_SHARPNESS = 1.75
ADVISOR_FRAME_UNSHARP_RADIUS = 0.65
ADVISOR_FRAME_UNSHARP_PERCENT = 200
ADVISOR_FRAME_UNSHARP_THRESHOLD = 1
ADVISOR_FRAME_MAX_LUMINANCE_GRADE_DELTA = 22.0
ADVISOR_FRAME_MAX_SATURATION_GRADE_DELTA = 0.09
ADVISOR_FRAME_ALPHA_LOW_CUTOFF = 32
ADVISOR_FRAME_ALPHA_OPAQUE_CUTOFF = 255
ADVISOR_FRAME_ALPHA_CURVE_SCALE = 181
ADVISOR_FRAME_ALPHA_CURVE_SPAN = 221
ADVISOR_FRAME_ALPHA_CURVE_EXPONENT = 4.5
# The source overlay is resized before rotation. These values are calibrated to
# the approved ImageGen paper and remain inside every measured six-reference
# vanilla paper band at native size.
ADVISOR_PAPER_SIZE = (25, 30)
ADVISOR_PAPER_POSITION = (29, 26)
ADVISOR_PAPER_ANGLE = -4.25
ADVISOR_PAPER_GRADE_COLOR = 0.64
ADVISOR_PAPER_GRADE_BRIGHTNESS = 1.02
ADVISOR_PAPER_GRADE_CONTRAST = 1.03
ADVISOR_PAPER_GRADE_SHARPNESS = 1.20
ADVISOR_PAPER_GRADE_CHANNEL_SCALE = (1.0, 1.0, 1.0)
ADVISOR_PAPER_ALPHA_OUTER_EDGE_MAX_SOURCE = 128
ADVISOR_PAPER_ALPHA_OUTER_EDGE_VALUE = 224
ADVISOR_PAPER_ALPHA_INNER_EDGE_MAX_SOURCE = 200
ADVISOR_PAPER_ALPHA_INNER_EDGE_VALUE = 250
ADVISOR_PAPER_ALPHA_OPAQUE_VALUE = 255
ADVISOR_WINDOW_ALPHA_THRESHOLD = 32
ADVISOR_SEARCH_SCHEMA = "chaos-redux-advisor-native-search-v2"
ADVISOR_NORMALIZATION_SCHEMA = (
	"chaos-redux-advisor-face-protected-background-luminance-affine-v1"
)
ADVISOR_MIN_NATIVE_STYLE_MARGIN = 0.03
ADVISOR_MAX_RETAINED_PORTRAIT_CANDIDATES_PER_STAGE = 128
ADVISOR_PORTRAIT_BASE_COLOR = 0.96
ADVISOR_PORTRAIT_BASE_CONTRAST = 1.04
ADVISOR_PORTRAIT_BASE_SMOOTH_BLEND = 0.05
ADVISOR_PORTRAIT_BASE_UNSHARP_RADIUS = 0.55
ADVISOR_PORTRAIT_BASE_UNSHARP_PERCENT = 35
ADVISOR_PORTRAIT_BASE_UNSHARP_THRESHOLD = 2
ADVISOR_PORTRAIT_GRADE_COLOR = 0.50
ADVISOR_PORTRAIT_GRADE_CONTRAST = 1.02
ADVISOR_PORTRAIT_GAMMA_LATTICE = (0.55, 0.65, 0.75, 0.85, 0.95)
ADVISOR_BACKGROUND_MEAN_LATTICE = tuple(float(value) for value in range(45, 101, 5))
ADVISOR_BACKGROUND_STD_LATTICE = tuple(float(value) for value in range(15, 51, 5))
ADVISOR_BACKGROUND_PROTECTION_EXPANSION = 2.0
ADVISOR_BACKGROUND_PROTECTION_FEATHER = 3.0
ADVISOR_BACKGROUND_SMOOTHING_RADIUS = 2.0
# The first stage preserves every authored background edge. The second stage is
# a face-protected, source-pixel-only last resort for painterly vanilla-scale
# backgrounds; the final selection key always prefers stage zero.
ADVISOR_BACKGROUND_SEARCH_STAGES = (
	(
		"unsmoothed",
		ADVISOR_PORTRAIT_GAMMA_LATTICE,
		ADVISOR_BACKGROUND_MEAN_LATTICE,
		ADVISOR_BACKGROUND_STD_LATTICE,
		(("none", 0.0),),
	),
	(
		"bounded_background_smoothing_last_resort",
		(0.45, 0.55, 0.65, 0.75, 0.85),
		(60.0, 65.0, 70.0, 75.0, 80.0, 82.5, 85.0, 87.5, 90.0, 95.0),
		(10.0, 12.5, 15.0, 17.5, 20.0),
		(("blur", 0.50), ("blur", 0.75), ("blur", 1.0)),
	),
)
ADVISOR_PAPER_MEAN_LATTICE = (205.0, 207.0, 209.0, 211.0, 213.0)
ADVISOR_PAPER_STD_LATTICE = (
	12.0,
	14.0,
	16.0,
	18.0,
	20.0,
	22.0,
	24.0,
	25.0,
	26.0,
	27.0,
)
ADVISOR_FACE_MAX_NEW_CLIPPING_RATIO = 0.005
ADVISOR_FACE_STD_RATIO_RANGE = (0.80, 1.20)
ADVISOR_FACE_GRADIENT_ENERGY_RATIO_RANGE = (0.85, 1.15)
ADVISOR_FACE_MIN_GRADIENT_CORRELATION = 0.95
ADVISOR_SOURCE_FACE_MAX_NEW_CLIPPING_RATIO = 0.02
ADVISOR_SOURCE_FACE_STD_RATIO_RANGE = (0.65, 1.35)
ADVISOR_SOURCE_FACE_GRADIENT_ENERGY_RATIO_RANGE = (0.65, 1.35)
ADVISOR_SOURCE_FACE_MIN_GRADIENT_CORRELATION = 0.95
ADVISOR_BACKGROUND_MAX_NEW_CLIPPING_RATIO = 0.02
ADVISOR_BACKGROUND_STD_RATIO_RANGE = (0.20, 1.30)
ADVISOR_BACKGROUND_GRADIENT_ENERGY_RATIO_RANGE = (0.10, 1.30)
ADVISOR_BACKGROUND_MIN_GRADIENT_CORRELATION = 0.65
ADVISOR_PAPER_MAX_NEW_CLIPPING_RATIO = 0.065
ADVISOR_PAPER_GRADIENT_ENERGY_RATIO_RANGE = (0.80, 2.05)
ADVISOR_CANONICAL_BACKING_SHADOW_OPACITY = 0.12
ADVISOR_CANONICAL_BACKING_MAX_ALPHA = 64
ADVISOR_RGB_SUBSTANTIVE_ALPHA_THRESHOLD = 64
ADVISOR_CARD_SHADOW_LAYERS = (
	((3, 0), 0.012, 8.0),
	((4, 0), 0.32, 3.5),
	((5, 1), 0.08, 2.0),
)
ADVISOR_PAPER_SHADOW_LAYERS = (
	((2, 1), 0.10, 1.5),
	((4, 1), 0.10, 1.0),
	((5, 2), 0.08, 0.5),
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
	"area_gt_32": 738.166667,
	"coverage_gt_32": 0.169499,
	"center": [42.777671, 41.30914],
	"top_edge_image_slope": 0.050649,
	"top_edge_image_angle_degrees": 2.899493,
	"mean_luminance": 208.830141,
	"mean_saturation": 0.21758,
}
ADVISOR_CANONICAL_PAPER_FAMILY_SHA256 = (
	"c751cbe5f1178c8b894c56a4cebe01bb4dae88ae859b7238c2c68f39a6224dbc"
)

# Face bounds are supplied in source pixels and mapped into the final native
# canvas. These ranges cover the canonical vanilla advisor family while
# rejecting leader-scale faces and tiny busts that disappear behind the dossier
# paper.
ADVISOR_FACE_WIDTH_RANGE = (14.0, 24.0)
ADVISOR_FACE_HEIGHT_RANGE = (16.0, 30.0)
ADVISOR_FACE_CENTER_X_RANGE = (17.0, 27.0)
ADVISOR_FACE_CENTER_Y_RANGE = (18.0, 32.0)

# These final-composite proxy gates are frozen from the six canonical 65x67
# vanilla advisor references. RGB values are unlinearized sRGB code values;
# alpha is not premultiplied. Boxes are zero-based and right/bottom-exclusive.
# "variation" is the mean absolute luminance difference over visible horizontal
# and vertical four-connected neighbour pairs. The paper standard deviation is
# the tonal spread across the frozen paper-colour classifier, not synthetic
# noise. Keeping the formulas here makes the 1:1 native-size claim executable.
ADVISOR_NATIVE_STYLE_ROIS = {
	"top_frame": (0, 0, 43, 12),
	"left_rail": (0, 0, 10, 59),
	"portrait": (7, 7, 36, 54),
	"bottom_area": (0, 50, 46, 65),
	"paper_zone": (26, 20, 65, 63),
}
ADVISOR_NATIVE_STYLE_BANDS = {
	"top_frame_variation": (16.402607, 24.640581),
	"left_rail_variation": (18.656585, 21.158895),
	"left_rail_mean": (40.169762, 51.022137),
	"left_rail_std": (33.351124, 41.734322),
	"paper_mean": (198.866806, 201.553207),
	"paper_std": (28.069763, 30.740780),
	"paper_samples": (830, 929),
	"portrait_mean": (101.212746, 124.481598),
	"bottom_area_variation": (12.158621, 15.613644),
}


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


def repo_relative_path(path: Path) -> str:
	"""Return one stable repository-relative path or reject external state."""
	resolved = path.expanduser().resolve()
	try:
		return resolved.relative_to(REPO_ROOT.resolve()).as_posix()
	except ValueError as error:
		raise ValueError(f"Path must remain inside the repository: {resolved}") from error


def selected_reference_records(
	reference_dir: Path,
	reference_names: tuple[str, ...],
	expected_size: tuple[int, int],
) -> list[dict[str, str]]:
	"""Validate and hash the exact role references shown in a review sheet."""
	reference_dir = reference_dir.expanduser().resolve()
	repo_relative_path(reference_dir)
	records: list[dict[str, str]] = []
	for name in reference_names:
		path = reference_dir / name
		if not path.is_file():
			raise FileNotFoundError(f"Missing role-family reference: {path}")
		with Image.open(path) as image:
			if image.size != expected_size:
				raise ValueError(
					f"Role-family reference is not {expected_size[0]}x{expected_size[1]}: "
					f"{path} ({image.size[0]}x{image.size[1]})"
				)
		records.append(
			{
				"name": name,
				"path": repo_relative_path(path),
				"sha256": sha256_file(path),
			}
		)
	return records


def resolve_full_size_references(
	role_family: str,
	reference_dir: Path | None = None,
) -> tuple[Path, list[dict[str, str]]]:
	"""Resolve the deterministic full-size style family and its evidence."""
	if role_family not in ROLE_FAMILY_REFERENCE_NAMES:
		raise ValueError(f"Unsupported full-size role family: {role_family}")
	resolved_dir = (
		reference_dir or ROLE_FAMILY_REFERENCE_DIRS[role_family]
	).expanduser().resolve()
	references = selected_reference_records(
		resolved_dir,
		ROLE_FAMILY_REFERENCE_NAMES[role_family],
		LEADER_SIZE,
	)
	return resolved_dir, references


def validate_output_contract(
	output: Path,
	review_sheet: Path,
	metadata: Path,
	forbidden_inputs: list[Path],
	force: bool,
) -> tuple[Path, Path, Path]:
	"""Freeze exact formats and prove every write path is disjoint from inputs."""
	targets = (
		output.expanduser().resolve(),
		review_sheet.expanduser().resolve(),
		metadata.expanduser().resolve(),
	)
	if targets[0].suffix != ".png":
		raise ValueError("Portrait output must use the exact .png suffix")
	if targets[1].suffix != ".png":
		raise ValueError("Review-sheet output must use the exact .png suffix")
	if targets[2].suffix != ".json":
		raise ValueError("Metadata output must use the exact .json suffix")
	if len(set(targets)) != len(targets):
		raise ValueError("Output, review-sheet, and metadata paths must be distinct")
	for target in targets:
		repo_relative_path(target)
	forbidden = {path.expanduser().resolve() for path in forbidden_inputs}
	overlaps = [str(target) for target in targets if target in forbidden]
	if overlaps:
		raise ValueError(
			"Write targets alias immutable portrait, overlay, manifest, prompt, tool, "
			f"or vanilla-reference inputs: {overlaps}"
		)
	for target in targets:
		if target.exists() and not target.is_file():
			raise ValueError(f"Write target exists but is not a regular file: {target}")
		if target.exists() and not force:
			raise FileExistsError(
				f"Refusing to replace existing artifact without --force: {target}"
			)
	return targets


def png_bytes(image: Image.Image) -> bytes:
	"""Encode a deterministic exact-RGBA PNG under the frozen Pillow runtime."""
	buffer = io.BytesIO()
	image.convert("RGBA").save(
		buffer,
		format="PNG",
		optimize=False,
		compress_level=9,
	)
	return buffer.getvalue()


def prepare_bytes(
	target: Path,
	payload: bytes,
	label: str,
	expected_image: Image.Image | None = None,
) -> dict[str, object]:
	"""Write one hidden candidate and verify its encoded and decoded payload."""
	target.parent.mkdir(parents=True, exist_ok=True)
	file_descriptor, temporary_name = tempfile.mkstemp(
		dir=str(target.parent),
		prefix=f".{target.name}.",
		suffix=".prepared",
	)
	temporary = Path(temporary_name)
	try:
		with os.fdopen(file_descriptor, "wb") as handle:
			handle.write(payload)
			handle.flush()
			os.fsync(handle.fileno())
		decoded_sha256: str | None = None
		if expected_image is not None:
			with Image.open(temporary) as decoded_file:
				if decoded_file.format != "PNG":
					raise ValueError(f"Prepared {label} did not decode as PNG")
				decoded = decoded_file.convert("RGBA")
			expected = expected_image.convert("RGBA")
			if decoded.size != expected.size or decoded.tobytes() != expected.tobytes():
				raise ValueError(
					f"Prepared {label} does not decode to the validated RGBA pixels"
				)
			decoded_sha256 = decoded_rgba_sha256(decoded)
		return {
			"target": target,
			"temporary": temporary,
			"label": label,
			"file_sha256": sha256_file(temporary),
			"decoded_rgba_sha256": decoded_sha256,
		}
	except Exception:
		if temporary.exists():
			temporary.unlink()
		raise


def commit_prepared_artifacts(
	prepared: list[dict[str, object]],
	force: bool,
) -> None:
	"""Commit all prepared files together, rolling back any failed replacement."""
	backups: dict[Path, Path] = {}
	committed: list[Path] = []
	try:
		for record in prepared:
			target = Path(record["target"])
			if target.exists() and not force:
				raise FileExistsError(
					f"Write target appeared after validation; refusing replacement: {target}"
				)
		for record in prepared:
			target = Path(record["target"])
			if not target.exists():
				continue
			file_descriptor, backup_name = tempfile.mkstemp(
				dir=str(target.parent),
				prefix=f".{target.name}.",
				suffix=".backup",
			)
			os.close(file_descriptor)
			backup = Path(backup_name)
			backup.unlink()
			os.replace(target, backup)
			backups[target] = backup
		for record in prepared:
			target = Path(record["target"])
			temporary = Path(record["temporary"])
			os.replace(temporary, target)
			committed.append(target)
		for record in prepared:
			target = Path(record["target"])
			if sha256_file(target) != str(record["file_sha256"]):
				raise RuntimeError(f"Committed artifact hash changed: {target}")
			decoded_sha256 = record.get("decoded_rgba_sha256")
			if decoded_sha256 is not None:
				with Image.open(target) as decoded_file:
					if decoded_file.format != "PNG":
						raise ValueError(f"Committed artifact is not PNG: {target}")
					decoded = decoded_file.convert("RGBA")
				if decoded_rgba_sha256(decoded) != decoded_sha256:
					raise RuntimeError(f"Committed PNG pixels changed: {target}")
	except Exception:
		for target in reversed(committed):
			if target.exists():
				target.unlink()
		for target, backup in backups.items():
			if backup.exists():
				os.replace(backup, target)
		raise
	else:
		for backup in backups.values():
			if backup.exists():
				backup.unlink()
	finally:
		for record in prepared:
			temporary = Path(record["temporary"])
			if temporary.exists():
				temporary.unlink()


def discard_prepared_artifacts(prepared: list[dict[str, object]]) -> None:
	"""Remove uncommitted hidden candidates after any pre-commit failure."""
	for record in prepared:
		temporary = Path(record["temporary"])
		if temporary.exists():
			temporary.unlink()


def normalized_command_record(
	args: argparse.Namespace,
	metadata_path: Path,
	role_family: str,
	effective_reference_dir: Path,
	selected_references: list[dict[str, str]],
) -> dict[str, object]:
	"""Record every effective CLI argument using stable repository paths."""
	def optional_path(value: Path | None) -> str | None:
		return repo_relative_path(value) if value is not None else None

	arguments = {
		"mode": args.mode,
		"source": repo_relative_path(args.source),
		"output": repo_relative_path(args.output),
		"crop": list(args.crop),
		"source_kind": args.source_kind,
		"face_box": list(args.face_box) if args.face_box is not None else None,
		"review_sheet": repo_relative_path(args.review_sheet),
		"metadata": repo_relative_path(metadata_path),
		"role_family": role_family,
		"reference_dir": optional_path(args.reference_dir),
		"effective_reference_dir": repo_relative_path(effective_reference_dir),
		"selected_references": selected_references,
		"advisor_overlay_manifest": optional_path(args.advisor_overlay_manifest),
		"portrait_provenance_manifest": optional_path(
			args.portrait_provenance_manifest
		),
		"advisor_frame_overlay": optional_path(args.advisor_frame_overlay),
		"advisor_frame_source": optional_path(args.advisor_frame_source),
		"advisor_paper_overlay": optional_path(args.advisor_paper_overlay),
		"advisor_paper_source": optional_path(args.advisor_paper_source),
		"force": bool(args.force),
	}
	return {
		"schema": "chaos-redux-normalized-portrait-command-v1",
		"role_family": role_family,
		"effective_reference_dir": repo_relative_path(effective_reference_dir),
		"selected_references": selected_references,
		"python": {
			"implementation": platform.python_implementation(),
			"version": platform.python_version(),
			"executable_name": Path(sys.executable).name,
		},
		"processor": repo_relative_path(Path(__file__)),
		"arguments": arguments,
		"arguments_sha256": canonical_json_sha256(arguments),
	}


def advisor_render_configuration() -> dict[str, object]:
	configuration = {
		"schema": "chaos-redux-advisor-render-configuration-v5.0",
		"runtime": {
			"python": ADVISOR_SUPPORTED_PYTHON_VERSION,
			"pillow": ADVISOR_SUPPORTED_PILLOW_VERSION,
		},
		"canvas_size": list(ADVISOR_SIZE),
		"frame": {
			"size": list(ADVISOR_FRAME_SIZE),
			"position": list(ADVISOR_FRAME_POSITION),
			"angle": ADVISOR_FRAME_ANGLE,
			"alpha_cap": ADVISOR_FRAME_ALPHA_CAP,
			"grade_color": ADVISOR_FRAME_GRADE_COLOR,
			"grade_brightness": ADVISOR_FRAME_GRADE_BRIGHTNESS,
			"grade_contrast": ADVISOR_FRAME_GRADE_CONTRAST,
			"grade_sharpness": ADVISOR_FRAME_GRADE_SHARPNESS,
			"unsharp_mask": {
				"radius": ADVISOR_FRAME_UNSHARP_RADIUS,
				"percent": ADVISOR_FRAME_UNSHARP_PERCENT,
				"threshold": ADVISOR_FRAME_UNSHARP_THRESHOLD,
			},
			"maximum_grade_delta": {
				"mean_luminance": ADVISOR_FRAME_MAX_LUMINANCE_GRADE_DELTA,
				"mean_saturation": ADVISOR_FRAME_MAX_SATURATION_GRADE_DELTA,
			},
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
		"portrait": {
			"base_finish": {
				"color": ADVISOR_PORTRAIT_BASE_COLOR,
				"contrast": ADVISOR_PORTRAIT_BASE_CONTRAST,
				"median_blend": ADVISOR_PORTRAIT_BASE_SMOOTH_BLEND,
				"unsharp_radius": ADVISOR_PORTRAIT_BASE_UNSHARP_RADIUS,
				"unsharp_percent": ADVISOR_PORTRAIT_BASE_UNSHARP_PERCENT,
				"unsharp_threshold": ADVISOR_PORTRAIT_BASE_UNSHARP_THRESHOLD,
				"procedural_grain": False,
				"procedural_vignette": False,
			},
			"search": {
				"schema": ADVISOR_SEARCH_SCHEMA,
				"normalization_schema": ADVISOR_NORMALIZATION_SCHEMA,
				"color": ADVISOR_PORTRAIT_GRADE_COLOR,
				"gamma": list(ADVISOR_PORTRAIT_GAMMA_LATTICE),
				"final_contrast": ADVISOR_PORTRAIT_GRADE_CONTRAST,
				"background_target_mean": list(ADVISOR_BACKGROUND_MEAN_LATTICE),
				"background_target_std": list(ADVISOR_BACKGROUND_STD_LATTICE),
				"background_face_protection_expansion": (
					ADVISOR_BACKGROUND_PROTECTION_EXPANSION
				),
				"background_face_protection_feather": (
					ADVISOR_BACKGROUND_PROTECTION_FEATHER
				),
				"background_smoothing_radius": ADVISOR_BACKGROUND_SMOOTHING_RADIUS,
				"background_search_stages": [
					{
						"name": name,
						"gamma": list(gamma),
						"target_mean": list(means),
						"target_std": list(stds),
						"smoothing": [list(values) for values in smoothing],
					}
					for name, gamma, means, stds, smoothing in (
						ADVISOR_BACKGROUND_SEARCH_STAGES
					)
				],
				"minimum_native_band_margin": ADVISOR_MIN_NATIVE_STYLE_MARGIN,
				"maximum_retained_portrait_candidates_per_stage": (
					ADVISOR_MAX_RETAINED_PORTRAIT_CANDIDATES_PER_STAGE
				),
			},
			"identity_gates": {
				"maximum_new_clipping_ratio": ADVISOR_FACE_MAX_NEW_CLIPPING_RATIO,
				"std_ratio": list(ADVISOR_FACE_STD_RATIO_RANGE),
				"gradient_energy_ratio": list(ADVISOR_FACE_GRADIENT_ENERGY_RATIO_RANGE),
				"minimum_gradient_correlation": ADVISOR_FACE_MIN_GRADIENT_CORRELATION,
			},
			"source_face_identity_gates": {
				"maximum_new_clipping_ratio": (
					ADVISOR_SOURCE_FACE_MAX_NEW_CLIPPING_RATIO
				),
				"std_ratio": list(ADVISOR_SOURCE_FACE_STD_RATIO_RANGE),
				"gradient_energy_ratio": list(
					ADVISOR_SOURCE_FACE_GRADIENT_ENERGY_RATIO_RANGE
				),
				"minimum_gradient_correlation": (
					ADVISOR_SOURCE_FACE_MIN_GRADIENT_CORRELATION
				),
			},
			"background_identity_gates": {
				"maximum_new_clipping_ratio": (
					ADVISOR_BACKGROUND_MAX_NEW_CLIPPING_RATIO
				),
				"std_ratio": list(ADVISOR_BACKGROUND_STD_RATIO_RANGE),
				"gradient_energy_ratio": list(
					ADVISOR_BACKGROUND_GRADIENT_ENERGY_RATIO_RANGE
				),
				"minimum_gradient_correlation": (
					ADVISOR_BACKGROUND_MIN_GRADIENT_CORRELATION
				),
			},
		},
		"paper_residual_search": {
			"normalization_schema": ADVISOR_NORMALIZATION_SCHEMA,
			"target_mean": list(ADVISOR_PAPER_MEAN_LATTICE),
			"target_std": list(ADVISOR_PAPER_STD_LATTICE),
			"maximum_new_clipping_ratio": ADVISOR_PAPER_MAX_NEW_CLIPPING_RATIO,
			"gradient_energy_ratio": list(ADVISOR_PAPER_GRADIENT_ENERGY_RATIO_RANGE),
			"geometry_alpha_blur_sharpen_are_search_variables": False,
		},
		"window_alpha_threshold": ADVISOR_WINDOW_ALPHA_THRESHOLD,
		"card_shadow_layers": [
			[list(offset), opacity, blur]
			for offset, opacity, blur in ADVISOR_CARD_SHADOW_LAYERS
		],
		"canonical_backing_shadow": {
			"source": "verified_canonical_alpha_envelope",
			"opacity": ADVISOR_CANONICAL_BACKING_SHADOW_OPACITY,
			"maximum_envelope_alpha": ADVISOR_CANONICAL_BACKING_MAX_ALPHA,
			"rgb": [0, 0, 0],
			"purpose": (
				"cover only the low-alpha antialiased/contact-shadow fringe with "
				"permitted alpha-derived shadow RGB"
			),
		},
		"rgb_support_substantive_alpha_threshold": (
			ADVISOR_RGB_SUBSTANTIVE_ALPHA_THRESHOLD
		),
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
		"canonical_paper_family": {
			"values": ADVISOR_CANONICAL_PAPER_FAMILY,
			"derived_aggregate_sha256": ADVISOR_CANONICAL_PAPER_FAMILY_SHA256,
		},
		"canonical_reference_names": list(ADVISOR_REFERENCE_NAMES),
		"canonical_alpha_envelope": {
			"method": ADVISOR_CANONICAL_ALPHA_METHOD,
			"decoded_alpha_sha256": ADVISOR_CANONICAL_ALPHA_SHA256,
			"purpose": (
				"reproduce the shared native vanilla opacity, edge, and shadow "
				"envelope without copying visible vanilla artwork"
			),
		},
		"native_style_proxy": {
			"formula": (
				"unlinearized_unpremultiplied_srgb_luminance; alpha_gt_64_rois; "
				"four_connected_mean_absolute_luminance_difference; population_std"
			),
			"rois": {
				name: list(box) for name, box in ADVISOR_NATIVE_STYLE_ROIS.items()
			},
			"bands": {
				name: list(band) for name, band in ADVISOR_NATIVE_STYLE_BANDS.items()
			},
		},
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


def advisor_srgb_luminance(pixel: tuple[int, int, int, int]) -> float:
	"""Return the frozen vanilla-audit luminance for one unpremultiplied pixel."""
	red, green, blue, _ = pixel
	return 0.2126 * red + 0.7152 * green + 0.0722 * blue


def advisor_native_roi_metrics(
	image: Image.Image,
	box: tuple[int, int, int, int],
) -> dict[str, float | int]:
	"""Measure one final-composite ROI with the frozen alpha and neighbour rules."""
	rgba = image.convert("RGBA")
	left, top, right, bottom = box
	values: list[float] = []
	variation_total = 0.0
	variation_pairs = 0
	for y in range(top, bottom):
		for x in range(left, right):
			pixel = rgba.getpixel((x, y))
			if pixel[3] > 64:
				values.append(advisor_srgb_luminance(pixel))
			if x + 1 < right:
				right_pixel = rgba.getpixel((x + 1, y))
				if pixel[3] > 64 and right_pixel[3] > 64:
					variation_total += abs(
						advisor_srgb_luminance(pixel)
						- advisor_srgb_luminance(right_pixel)
					)
					variation_pairs += 1
			if y + 1 < bottom:
				bottom_pixel = rgba.getpixel((x, y + 1))
				if pixel[3] > 64 and bottom_pixel[3] > 64:
					variation_total += abs(
						advisor_srgb_luminance(pixel)
						- advisor_srgb_luminance(bottom_pixel)
					)
					variation_pairs += 1
	if not values or not variation_pairs:
		raise ValueError(f"Advisor native-style ROI has no visible samples: {box}")
	mean = sum(values) / len(values)
	population_variance = sum((value - mean) ** 2 for value in values) / len(values)
	return {
		"mean": mean,
		"std": math.sqrt(population_variance),
		"variation": variation_total / variation_pairs,
		"samples": len(values),
	}


def advisor_native_paper_metrics(image: Image.Image) -> dict[str, float | int]:
	"""Measure the frozen paper-colour proxy inside the final 65x67 composite."""
	rgba = image.convert("RGBA")
	left, top, right, bottom = ADVISOR_NATIVE_STYLE_ROIS["paper_zone"]
	values: list[float] = []
	for y in range(top, bottom):
		for x in range(left, right):
			red, green, blue, alpha = rgba.getpixel((x, y))
			luminance = advisor_srgb_luminance((red, green, blue, alpha))
			maximum = max(red, green, blue)
			minimum = min(red, green, blue)
			if (
				alpha > 192
				and luminance > 105
				and maximum - minimum < 105
				and red >= blue * 0.88
				and green >= blue * 0.78
			):
				values.append(luminance)
	if not values:
		raise ValueError("Advisor native paper proxy has no classified samples")
	mean = sum(values) / len(values)
	population_variance = sum((value - mean) ** 2 for value in values) / len(values)
	return {
		"mean": mean,
		"std": math.sqrt(population_variance),
		"samples": len(values),
	}


def advisor_native_style_metrics(image: Image.Image) -> dict[str, object]:
	"""Return the exact final-composite measurements frozen from vanilla."""
	return {
		"top_frame": advisor_native_roi_metrics(
			image, ADVISOR_NATIVE_STYLE_ROIS["top_frame"]
		),
		"left_rail": advisor_native_roi_metrics(
			image, ADVISOR_NATIVE_STYLE_ROIS["left_rail"]
		),
		"portrait": advisor_native_roi_metrics(
			image, ADVISOR_NATIVE_STYLE_ROIS["portrait"]
		),
		"bottom_area": advisor_native_roi_metrics(
			image, ADVISOR_NATIVE_STYLE_ROIS["bottom_area"]
		),
		"paper": advisor_native_paper_metrics(image),
	}


def validate_advisor_native_style_metrics(image: Image.Image) -> dict[str, object]:
	"""Reject native dossier composites outside every measured vanilla band."""
	record = advisor_native_style_band_record(
		image,
		ADVISOR_MIN_NATIVE_STYLE_MARGIN,
	)
	metrics = record["metrics"]
	failures = record["failures"]
	if failures:
		raise ValueError(
			"Advisor final composite is outside the frozen six-reference native-style "
			f"bands or minimum interior margin: {failures}"
		)
	return {
		"formula": (
			"unlinearized_unpremultiplied_srgb_luminance; alpha_gt_64_rois; "
			"four_connected_mean_absolute_luminance_difference; population_std"
		),
		"rois": {name: list(box) for name, box in ADVISOR_NATIVE_STYLE_ROIS.items()},
		"bands": {name: list(band) for name, band in ADVISOR_NATIVE_STYLE_BANDS.items()},
		"required_minimum_normalized_margin": ADVISOR_MIN_NATIVE_STYLE_MARGIN,
		"margins": record["margins"],
		"minimum_margin": record["minimum_margin"],
		"center_sse": record["center_sse"],
		"metrics": {
			family: {
				name: round(value, 6) if isinstance(value, float) else value
				for name, value in family_metrics.items()
			}
			for family, family_metrics in metrics.items()
		},
	}


def verify_advisor_runtime() -> dict[str, str]:
	python_version = platform.python_version()
	if python_version != ADVISOR_SUPPORTED_PYTHON_VERSION:
		raise RuntimeError(
			"Advisor rendering requires the frozen Python runtime "
			f"{ADVISOR_SUPPORTED_PYTHON_VERSION}; found {python_version}"
		)
	if PILLOW_VERSION != ADVISOR_SUPPORTED_PILLOW_VERSION:
		raise RuntimeError(
			"Advisor rendering requires the frozen Pillow runtime "
			f"{ADVISOR_SUPPORTED_PILLOW_VERSION}; found {PILLOW_VERSION}"
		)
	return {"python": python_version, "pillow": PILLOW_VERSION}


def deterministic_seed_record(
	source: Image.Image,
	crop_box: tuple[int, int, int, int],
	face_box: tuple[int, int, int, int] | None,
	source_kind: str,
	mode: str,
	render_version: str,
	frame_overlay_sha256: str | None,
	paper_overlay_sha256: str | None,
	portrait_provenance_sha256: str | None = None,
	overlay_manifest_sha256: str | None = None,
	render_configuration_sha256: str | None = None,
	runtime: dict[str, str] | None = None,
	processor_sha256: str | None = None,
) -> dict[str, object]:
	payload = {
		"schema": "chaos-redux-portrait-seed-v3",
		"decoded_rgba_sha256": decoded_rgba_sha256(source),
		"crop": list(crop_box),
		"face_box": list(face_box) if face_box is not None else None,
		"source_kind": source_kind,
		"mode": mode,
		"render_version": render_version,
		"frame_overlay_sha256": frame_overlay_sha256,
		"paper_overlay_sha256": paper_overlay_sha256,
		"portrait_provenance_sha256": portrait_provenance_sha256,
		"overlay_manifest_sha256": overlay_manifest_sha256,
		"render_configuration_sha256": render_configuration_sha256,
		"runtime": runtime,
		"processor_sha256": processor_sha256,
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
	resolved = path.resolve()
	try:
		resolved.relative_to(REPO_ROOT.resolve())
	except ValueError as error:
		raise ValueError(
			f"Advisor manifest {label} must remain inside the repository: {resolved}"
		) from error
	return resolved


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
		if not isinstance(generation_inputs, list) or len(generation_inputs) != 2:
			raise ValueError(f"Advisor {role} generation inputs are incomplete")
		input_roles = [
			str(record.get("role", ""))
			for record in generation_inputs
			if isinstance(record, dict)
		]
		if (
			len(set(input_roles)) != 2
			or "vanilla_style_reference_contact_sheet" not in input_roles
			or sum(value.startswith("prior_imagegen_") for value in input_roles) != 1
		):
			raise ValueError(
				f"Advisor {role} generation-input roles are not the frozen two-step "
				f"ImageGen route: {input_roles}"
			)
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
		if (
			alpha_tool != IMAGEGEN_ALPHA_TOOL_MANIFEST_PATH
			or alpha_tool_sha256 != IMAGEGEN_ALPHA_TOOL_SHA256
		):
			raise ValueError(
				f"Advisor {role} alpha-extraction tool is not the frozen ImageGen "
				"skill keyer"
			)
		if not IMAGEGEN_ALPHA_TOOL.is_file():
			raise FileNotFoundError(IMAGEGEN_ALPHA_TOOL)
		if sha256_file(IMAGEGEN_ALPHA_TOOL) != IMAGEGEN_ALPHA_TOOL_SHA256:
			raise ValueError("Installed ImageGen alpha keyer hash differs")
		arguments = alpha_extraction.get("arguments")
		if (
			not isinstance(arguments, list)
			or tuple(str(value) for value in arguments)
			!= IMAGEGEN_ALPHA_TOOL_ARGUMENTS
		):
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


def verify_portrait_provenance_manifest(
	manifest_path: Path,
	source_path: Path,
	source_kind: str,
	crop_box: tuple[int, int, int, int],
	face_box: tuple[int, int, int, int],
) -> dict[str, object]:
	"""Verify one approved portrait master without machine-local dependencies."""
	manifest_path = manifest_path.resolve()
	try:
		manifest_path.relative_to(REPO_ROOT.resolve())
	except ValueError as error:
		raise ValueError(
			f"Portrait provenance manifest must remain inside the repository: "
			f"{manifest_path}"
		) from error
	if not manifest_path.is_file():
		raise FileNotFoundError(manifest_path)
	manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
	if manifest.get("schema_version") != 1:
		raise ValueError("Portrait provenance manifest must use schema 1")
	assets = manifest.get("assets")
	if not isinstance(assets, list):
		raise ValueError("Portrait provenance manifest has no assets list")
	manifest_prompt_record = resolve_manifest_path(
		manifest.get("prompt_record"), "package prompt record"
	)
	if not manifest_prompt_record.is_file():
		raise FileNotFoundError(manifest_prompt_record)
	manifest_prompt_sha256 = sha256_file(manifest_prompt_record)
	if manifest_prompt_sha256 != str(manifest.get("prompt_sha256", "")):
		raise ValueError("Portrait package prompt-record hash differs")
	resolved_source = source_path.resolve()
	matches: list[dict[str, object]] = []
	for entry in assets:
		if not isinstance(entry, dict):
			continue
		if (
			entry.get("role") == "advisor_portrait_master"
			and entry.get("status") == "approved_for_processing"
			and resolve_manifest_path(
				entry.get("source"), "portrait source"
			) == resolved_source
		):
			matches.append(entry)
	if len(matches) != 1:
		raise ValueError(
			"Portrait provenance manifest needs exactly one approved record for "
			f"{resolved_source}; found {len(matches)}"
		)
	entry = matches[0]
	record_id = str(entry.get("record_id", ""))
	if not record_id:
		raise ValueError("Portrait provenance record lacks record_id")
	if str(entry.get("source_kind", "")) != source_kind:
		raise ValueError("Portrait provenance source_kind differs from the CLI")
	actual_source_hash = sha256_file(resolved_source)
	if actual_source_hash != str(entry.get("source_sha256", "")):
		raise ValueError("Portrait source hash differs from its provenance record")
	if entry.get("exact_source_byte_copy") is not True:
		raise ValueError("Portrait provenance lacks exact source-copy assertion")
	with Image.open(resolved_source) as source_image:
		source_dimensions = list(source_image.size)
	if source_dimensions != list(entry.get("source_dimensions", [])):
		raise ValueError("Portrait source dimensions differ from provenance")
	if list(crop_box) != list(entry.get("approved_crop", [])):
		raise ValueError("Portrait crop differs from the approved provenance record")
	if list(face_box) != list(entry.get("approved_face_box", [])):
		raise ValueError("Portrait face box differs from the approved provenance record")
	prompt_record = resolve_manifest_path(
		entry.get("prompt_record", manifest.get("prompt_record")),
		"portrait prompt record",
	)
	if not prompt_record.is_file():
		raise FileNotFoundError(prompt_record)
	prompt_hash = sha256_file(prompt_record)
	if prompt_hash != str(
		entry.get("prompt_sha256", manifest.get("prompt_sha256", ""))
	):
		raise ValueError("Portrait prompt record hash differs")
	if (
		prompt_record != manifest_prompt_record
		or prompt_hash != manifest_prompt_sha256
	):
		raise ValueError("Portrait record does not use the package-pinned prompt record")
	prompt_section = str(entry.get("prompt_section", ""))
	if not prompt_section:
		raise ValueError("Portrait provenance lacks its exact prompt section")
	prompt_text = prompt_record.read_text(encoding="utf-8")
	if f"### `{prompt_section}`" not in prompt_text:
		raise ValueError(
			f"Portrait prompt section is absent from the pinned prompt record: "
			f"{prompt_section}"
		)
	generation_mode = str(
		entry.get("generation_mode", manifest.get("generation_mode", ""))
	)
	generation_inputs = entry.get(
		"generation_inputs", manifest.get("generation_inputs")
	)
	if generation_mode not in {"text_to_image", "image_edit", "archival_source"}:
		raise ValueError("Portrait provenance generation_mode is unsupported")
	if not isinstance(generation_inputs, list):
		raise ValueError("Portrait provenance generation_inputs must be a list")
	verified_inputs: list[dict[str, str]] = []
	for input_record in generation_inputs:
		if not isinstance(input_record, dict):
			raise ValueError("Portrait provenance generation input is malformed")
		input_path = resolve_manifest_path(
			input_record.get("path"), "portrait generation input"
		)
		if not input_path.is_file():
			raise FileNotFoundError(input_path)
		input_hash = sha256_file(input_path)
		if input_hash != str(input_record.get("sha256", "")):
			raise ValueError("Portrait generation-input hash differs")
		verified_inputs.append(
			{
				"role": str(input_record.get("role", "")),
				"path": str(input_path),
				"sha256": input_hash,
			}
		)
	if generation_mode == "text_to_image" and verified_inputs:
		raise ValueError("Text-to-image portrait record must not invent input images")
	if generation_mode == "image_edit" and not verified_inputs:
		raise ValueError("Image-edit portrait record requires generation inputs")
	if source_kind in {"fictional", "collective", "symbolic"}:
		generator = str(manifest.get("generator", ""))
		handle = str(entry.get("imagegen_handle", ""))
		if "imagegen" not in generator.lower() or not handle.startswith("exec-"):
			raise ValueError(
				"Fictional/symbolic advisor portraits require pinned ImageGen provenance"
			)
	else:
		handle = ""
		if generation_mode != "archival_source":
			raise ValueError("Real portraits require archival_source provenance")
		if not str(entry.get("attribution", "")) or not str(
			entry.get("license", "")
		):
			raise ValueError("Archival portrait provenance lacks attribution/license")
	return {
		"path": str(manifest_path),
		"sha256": sha256_file(manifest_path),
		"package": str(manifest.get("package", "")),
		"record_id": record_id,
		"source": str(resolved_source),
		"source_sha256": actual_source_hash,
		"source_dimensions": source_dimensions,
		"source_kind": source_kind,
		"approved_crop": list(crop_box),
		"approved_face_box": list(face_box),
		"generation_mode": generation_mode,
		"imagegen_handle": handle,
		"prompt_record": str(prompt_record),
		"prompt_sha256": prompt_hash,
		"prompt_section": prompt_section,
		"generation_inputs": verified_inputs,
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

	# Chroma-key cleanup may despill only semitransparent edge pixels. Fully
	# opaque RGB must be byte-identical to the retained ImageGen source, and the
	# edge deltas are tightly bounded to the measured keyer output.
	difference = ImageChops.difference(source, overlay.convert("RGB"))
	difference_values = list(difference.getdata())
	alpha_values = list(alpha.getdata())
	opaque_mismatches = sum(
		value == 255 and any(channels)
		for channels, value in zip(difference_values, alpha_values)
	)
	semitransparent_deltas = [
		sum(channels) / 3
		for channels, value in zip(difference_values, alpha_values)
		if 0 < value < 255
	]
	strong_edge_deltas = [
		sum(channels) / 3
		for channels, value in zip(difference_values, alpha_values)
		if 128 < value < 255
	]
	mean_semitransparent_delta = sum(semitransparent_deltas) / max(
		1, len(semitransparent_deltas)
	)
	maximum_semitransparent_delta = max(semitransparent_deltas, default=0.0)
	mean_strong_edge_delta = sum(strong_edge_deltas) / max(
		1, len(strong_edge_deltas)
	)
	maximum_strong_edge_delta = max(strong_edge_deltas, default=0.0)
	if opaque_mismatches:
		raise ValueError(
			f"{label} overlay changes {opaque_mismatches} fully opaque ImageGen RGB "
			"pixels; alpha extraction may alter semitransparent despill edges only"
		)
	if (
		mean_semitransparent_delta > 32.0
		or maximum_semitransparent_delta > 67.0
		or mean_strong_edge_delta > 25.0
		or maximum_strong_edge_delta > 42.0
	):
		raise ValueError(
			f"{label} overlay edge RGB deltas exceed the frozen chroma-despill "
			"contract: "
			f"semi_mean={mean_semitransparent_delta:.3f}, "
			f"semi_max={maximum_semitransparent_delta:.3f}, "
			f"strong_mean={mean_strong_edge_delta:.3f}, "
			f"strong_max={maximum_strong_edge_delta:.3f}"
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
		"opaque_source_rgb_mismatches": opaque_mismatches,
		"mean_semitransparent_source_rgb_delta": round(
			mean_semitransparent_delta, 6
		),
		"maximum_semitransparent_source_rgb_delta": round(
			maximum_semitransparent_delta, 6
		),
		"mean_strong_edge_source_rgb_delta": round(mean_strong_edge_delta, 6),
		"maximum_strong_edge_source_rgb_delta": round(
			maximum_strong_edge_delta, 6
		),
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
	rgb = ImageEnhance.Sharpness(rgb).enhance(
		ADVISOR_FRAME_GRADE_SHARPNESS
	)
	rgb = rgb.filter(
		ImageFilter.UnsharpMask(
			radius=ADVISOR_FRAME_UNSHARP_RADIUS,
			percent=ADVISOR_FRAME_UNSHARP_PERCENT,
			threshold=ADVISOR_FRAME_UNSHARP_THRESHOLD,
		)
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


def advisor_portrait_base_finish(portrait: Image.Image) -> Image.Image:
	"""Apply only identity-preserving small-card preparation to authored art.

	Advisor mode intentionally does not call :func:`hoi4_finish`: dossier cards
	must inherit all visible texture from the ImageGen portrait, frame, and paper,
	not from procedural grain or a programmatically drawn vignette.
	"""
	alpha = portrait.getchannel("A")
	rgb = ImageEnhance.Color(portrait.convert("RGB")).enhance(
		ADVISOR_PORTRAIT_BASE_COLOR
	)
	rgb = ImageEnhance.Contrast(rgb).enhance(ADVISOR_PORTRAIT_BASE_CONTRAST)
	smoothed = rgb.filter(ImageFilter.MedianFilter(3))
	rgb = Image.blend(rgb, smoothed, ADVISOR_PORTRAIT_BASE_SMOOTH_BLEND)
	rgb = rgb.filter(
		ImageFilter.UnsharpMask(
			radius=ADVISOR_PORTRAIT_BASE_UNSHARP_RADIUS,
			percent=ADVISOR_PORTRAIT_BASE_UNSHARP_PERCENT,
			threshold=ADVISOR_PORTRAIT_BASE_UNSHARP_THRESHOLD,
		)
	)
	finished = rgb.convert("RGBA")
	finished.putalpha(alpha)
	return finished


def advisor_luminance_statistics(values: list[float]) -> tuple[float, float]:
	if not values:
		raise ValueError("Advisor normalization has no visible luminance samples")
	mean = sum(values) / len(values)
	variance = sum((value - mean) ** 2 for value in values) / len(values)
	return mean, math.sqrt(variance)


def advisor_apply_luminance_affine(
	image: Image.Image,
	target_mean: float,
	target_std: float,
	alpha_threshold: int,
) -> Image.Image:
	"""Normalize luminance uniformly while preserving every pixel's chroma."""
	rgba = image.convert("RGBA")
	pixels = list(rgba.getdata())
	indices = [
		index for index, pixel in enumerate(pixels) if pixel[3] > alpha_threshold
	]
	values = [advisor_srgb_luminance(pixels[index]) for index in indices]
	mean, std = advisor_luminance_statistics(values)
	if std <= 0.000001:
		raise ValueError("Advisor luminance normalization source has zero contrast")
	scale = target_std / std
	result = list(pixels)
	for index in indices:
		red, green, blue, alpha = pixels[index]
		luminance = advisor_srgb_luminance((red, green, blue, alpha))
		target = target_mean + (luminance - mean) * scale
		delta = target - luminance
		result[index] = (
			max(0, min(255, round(red + delta))),
			max(0, min(255, round(green + delta))),
			max(0, min(255, round(blue + delta))),
			alpha,
		)
	output = Image.new("RGBA", rgba.size)
	output.putdata(result)
	return output


def advisor_region_identity_metrics(
	baseline: Image.Image,
	candidate: Image.Image,
	box: tuple[int, int, int, int],
	alpha_threshold: int = ADVISOR_WINDOW_ALPHA_THRESHOLD,
) -> dict[str, float | int]:
	"""Measure clipping and landmark-preserving tonal changes in one region."""
	base = baseline.convert("RGBA")
	changed = candidate.convert("RGBA")
	left, top, right, bottom = box
	base_values: list[float] = []
	changed_values: list[float] = []
	base_gradients: list[float] = []
	changed_gradients: list[float] = []
	newly_clipped = 0
	visible_pixels = 0
	for y in range(top, bottom):
		for x in range(left, right):
			base_pixel = base.getpixel((x, y))
			changed_pixel = changed.getpixel((x, y))
			if base_pixel[3] <= alpha_threshold:
				continue
			visible_pixels += 1
			base_values.append(advisor_srgb_luminance(base_pixel))
			changed_values.append(advisor_srgb_luminance(changed_pixel))
			base_clipped = min(base_pixel[:3]) <= 0 or max(base_pixel[:3]) >= 255
			changed_clipped = min(changed_pixel[:3]) <= 0 or max(changed_pixel[:3]) >= 255
			if changed_clipped and not base_clipped:
				newly_clipped += 1
			if x + 1 < right:
				base_right = base.getpixel((x + 1, y))
				changed_right = changed.getpixel((x + 1, y))
				if base_right[3] > alpha_threshold:
					base_gradients.append(
						advisor_srgb_luminance(base_right)
						- advisor_srgb_luminance(base_pixel)
					)
					changed_gradients.append(
						advisor_srgb_luminance(changed_right)
						- advisor_srgb_luminance(changed_pixel)
					)
			if y + 1 < bottom:
				base_bottom = base.getpixel((x, y + 1))
				changed_bottom = changed.getpixel((x, y + 1))
				if base_bottom[3] > alpha_threshold:
					base_gradients.append(
						advisor_srgb_luminance(base_bottom)
						- advisor_srgb_luminance(base_pixel)
					)
					changed_gradients.append(
						advisor_srgb_luminance(changed_bottom)
						- advisor_srgb_luminance(changed_pixel)
					)
	if not base_values or not base_gradients:
		raise ValueError(f"Advisor identity region has no usable samples: {box}")
	base_mean, base_std = advisor_luminance_statistics(base_values)
	changed_mean, changed_std = advisor_luminance_statistics(changed_values)
	base_gradient_energy = sum(abs(value) for value in base_gradients) / len(base_gradients)
	changed_gradient_energy = sum(abs(value) for value in changed_gradients) / len(changed_gradients)
	gradient_base_mean = sum(base_gradients) / len(base_gradients)
	gradient_changed_mean = sum(changed_gradients) / len(changed_gradients)
	numerator = sum(
		(base_value - gradient_base_mean) * (changed_value - gradient_changed_mean)
		for base_value, changed_value in zip(base_gradients, changed_gradients)
	)
	base_denominator = sum(
		(value - gradient_base_mean) ** 2 for value in base_gradients
	)
	changed_denominator = sum(
		(value - gradient_changed_mean) ** 2 for value in changed_gradients
	)
	denominator = math.sqrt(base_denominator * changed_denominator)
	gradient_correlation = numerator / denominator if denominator else 1.0
	return {
		"visible_pixels": visible_pixels,
		"baseline_mean": round(base_mean, 6),
		"candidate_mean": round(changed_mean, 6),
		"baseline_std": round(base_std, 6),
		"candidate_std": round(changed_std, 6),
		"std_ratio": round(changed_std / max(base_std, 0.000001), 6),
		"baseline_gradient_energy": round(base_gradient_energy, 6),
		"candidate_gradient_energy": round(changed_gradient_energy, 6),
		"gradient_energy_ratio": round(
			changed_gradient_energy / max(base_gradient_energy, 0.000001), 6
		),
		"gradient_correlation": round(gradient_correlation, 6),
		"newly_clipped_pixels": newly_clipped,
		"newly_clipped_ratio": round(newly_clipped / visible_pixels, 6),
		"normalized_luminance_mae": round(
			sum(
				abs(base_value - changed_value)
				for base_value, changed_value in zip(base_values, changed_values)
			) / (len(base_values) * 255),
			6,
		),
	}


def advisor_face_identity_passes(metrics: dict[str, float | int]) -> bool:
	return (
		float(metrics["newly_clipped_ratio"]) <= ADVISOR_FACE_MAX_NEW_CLIPPING_RATIO
		and ADVISOR_FACE_STD_RATIO_RANGE[0]
		<= float(metrics["std_ratio"])
		<= ADVISOR_FACE_STD_RATIO_RANGE[1]
		and ADVISOR_FACE_GRADIENT_ENERGY_RATIO_RANGE[0]
		<= float(metrics["gradient_energy_ratio"])
		<= ADVISOR_FACE_GRADIENT_ENERGY_RATIO_RANGE[1]
		and float(metrics["gradient_correlation"])
		>= ADVISOR_FACE_MIN_GRADIENT_CORRELATION
	)


def advisor_source_face_identity_passes(
	metrics: dict[str, float | int],
) -> bool:
	return (
		float(metrics["newly_clipped_ratio"])
		<= ADVISOR_SOURCE_FACE_MAX_NEW_CLIPPING_RATIO
		and ADVISOR_SOURCE_FACE_STD_RATIO_RANGE[0]
		<= float(metrics["std_ratio"])
		<= ADVISOR_SOURCE_FACE_STD_RATIO_RANGE[1]
		and ADVISOR_SOURCE_FACE_GRADIENT_ENERGY_RATIO_RANGE[0]
		<= float(metrics["gradient_energy_ratio"])
		<= ADVISOR_SOURCE_FACE_GRADIENT_ENERGY_RATIO_RANGE[1]
		and float(metrics["gradient_correlation"])
		>= ADVISOR_SOURCE_FACE_MIN_GRADIENT_CORRELATION
	)


def advisor_background_weights(
	size: tuple[int, int],
	face_box: tuple[int, int, int, int],
	expansion: float,
	feather: float,
) -> list[float]:
	"""Return deterministic background weights around an invisible face guard."""
	if feather <= 0.0:
		raise ValueError("Advisor face-protection feather must be positive")
	left = float(face_box[0]) - expansion
	top = float(face_box[1]) - expansion
	right = float(face_box[2]) + expansion
	bottom = float(face_box[3]) + expansion
	weights: list[float] = []
	for y in range(size[1]):
		pixel_y = y + 0.5
		for x in range(size[0]):
			pixel_x = x + 0.5
			delta_x = max(left - pixel_x, 0.0, pixel_x - right)
			delta_y = max(top - pixel_y, 0.0, pixel_y - bottom)
			distance = math.hypot(delta_x, delta_y)
			weights.append(min(1.0, distance / feather))
	return weights


def advisor_weighted_identity_metrics(
	baseline: Image.Image,
	candidate: Image.Image,
	weights: list[float],
	minimum_weight: float = 0.95,
) -> dict[str, float | int]:
	"""Measure clipping and structure in the transformed portrait background."""
	base = baseline.convert("RGBA")
	changed = candidate.convert("RGBA")
	if base.size != changed.size or len(weights) != base.width * base.height:
		raise ValueError("Advisor background identity inputs have different geometry")
	base_pixels = list(base.getdata())
	changed_pixels = list(changed.getdata())
	base_values: list[float] = []
	changed_values: list[float] = []
	base_gradients: list[float] = []
	changed_gradients: list[float] = []
	newly_clipped = 0
	for index, (base_pixel, changed_pixel, weight) in enumerate(
		zip(base_pixels, changed_pixels, weights)
	):
		if (
			weight < minimum_weight
			or base_pixel[3] <= ADVISOR_WINDOW_ALPHA_THRESHOLD
		):
			continue
		base_values.append(advisor_srgb_luminance(base_pixel))
		changed_values.append(advisor_srgb_luminance(changed_pixel))
		base_clipped = min(base_pixel[:3]) <= 0 or max(base_pixel[:3]) >= 255
		changed_clipped = (
			min(changed_pixel[:3]) <= 0 or max(changed_pixel[:3]) >= 255
		)
		if changed_clipped and not base_clipped:
			newly_clipped += 1
		x = index % base.width
		y = index // base.width
		for neighbour in (
			index + 1 if x + 1 < base.width else None,
			index + base.width if y + 1 < base.height else None,
		):
			if neighbour is None or weights[neighbour] < minimum_weight:
				continue
			base_neighbour = base_pixels[neighbour]
			changed_neighbour = changed_pixels[neighbour]
			if base_neighbour[3] <= ADVISOR_WINDOW_ALPHA_THRESHOLD:
				continue
			base_gradients.append(
				advisor_srgb_luminance(base_neighbour)
				- advisor_srgb_luminance(base_pixel)
			)
			changed_gradients.append(
				advisor_srgb_luminance(changed_neighbour)
				- advisor_srgb_luminance(changed_pixel)
			)
	if not base_values or not base_gradients:
		raise ValueError("Advisor background identity region has no usable samples")
	base_mean, base_std = advisor_luminance_statistics(base_values)
	changed_mean, changed_std = advisor_luminance_statistics(changed_values)
	base_gradient_energy = sum(abs(value) for value in base_gradients) / len(
		base_gradients
	)
	changed_gradient_energy = sum(abs(value) for value in changed_gradients) / len(
		changed_gradients
	)
	gradient_base_mean = sum(base_gradients) / len(base_gradients)
	gradient_changed_mean = sum(changed_gradients) / len(changed_gradients)
	numerator = sum(
		(base_value - gradient_base_mean)
		* (changed_value - gradient_changed_mean)
		for base_value, changed_value in zip(base_gradients, changed_gradients)
	)
	base_denominator = sum(
		(value - gradient_base_mean) ** 2 for value in base_gradients
	)
	changed_denominator = sum(
		(value - gradient_changed_mean) ** 2 for value in changed_gradients
	)
	denominator = math.sqrt(base_denominator * changed_denominator)
	gradient_correlation = numerator / denominator if denominator else 1.0
	return {
		"visible_pixels": len(base_values),
		"selection_weight_threshold": minimum_weight,
		"baseline_mean": round(base_mean, 6),
		"candidate_mean": round(changed_mean, 6),
		"baseline_std": round(base_std, 6),
		"candidate_std": round(changed_std, 6),
		"std_ratio": round(changed_std / max(base_std, 0.000001), 6),
		"baseline_gradient_energy": round(base_gradient_energy, 6),
		"candidate_gradient_energy": round(changed_gradient_energy, 6),
		"gradient_energy_ratio": round(
			changed_gradient_energy / max(base_gradient_energy, 0.000001), 6
		),
		"gradient_correlation": round(gradient_correlation, 6),
		"newly_clipped_pixels": newly_clipped,
		"newly_clipped_ratio": round(newly_clipped / len(base_values), 6),
		"normalized_luminance_mae": round(
			sum(
				abs(base_value - changed_value)
				for base_value, changed_value in zip(
					base_values, changed_values
				)
			) / (len(base_values) * 255),
			6,
		),
	}


def advisor_background_identity_passes(metrics: dict[str, float | int]) -> bool:
	return (
		float(metrics["newly_clipped_ratio"])
		<= ADVISOR_BACKGROUND_MAX_NEW_CLIPPING_RATIO
		and ADVISOR_BACKGROUND_STD_RATIO_RANGE[0]
		<= float(metrics["std_ratio"])
		<= ADVISOR_BACKGROUND_STD_RATIO_RANGE[1]
		and ADVISOR_BACKGROUND_GRADIENT_ENERGY_RATIO_RANGE[0]
		<= float(metrics["gradient_energy_ratio"])
		<= ADVISOR_BACKGROUND_GRADIENT_ENERGY_RATIO_RANGE[1]
		and float(metrics["gradient_correlation"])
		>= ADVISOR_BACKGROUND_MIN_GRADIENT_CORRELATION
	)


def advisor_paper_identity_passes(metrics: dict[str, float | int]) -> bool:
	return (
		float(metrics["newly_clipped_ratio"]) <= ADVISOR_PAPER_MAX_NEW_CLIPPING_RATIO
		and ADVISOR_PAPER_GRADIENT_ENERGY_RATIO_RANGE[0]
		<= float(metrics["gradient_energy_ratio"])
		<= ADVISOR_PAPER_GRADIENT_ENERGY_RATIO_RANGE[1]
	)


def grade_advisor_portrait_candidate(
	portrait: Image.Image,
	gamma: float,
	background_target_mean: float,
	background_target_std: float,
	smoothing: tuple[str, float],
	face_local_box: tuple[int, int, int, int],
) -> tuple[Image.Image, Image.Image, dict[str, float | int], dict[str, object]]:
	"""Grade an authored portrait while keeping the supplied face untouched.

	The explicit face box is an invisible control field, never visible artwork.
	Only portrait RGB is transformed: a feathered background-only luminance
	affine preserves chroma, and the optional blur stage mixes neighbouring
	authored portrait pixels. No fill, noise, texture, vignette, or dossier art is
	created here.
	"""
	alpha = portrait.getchannel("A")
	rgb = ImageEnhance.Color(portrait.convert("RGB")).enhance(
		ADVISOR_PORTRAIT_GRADE_COLOR
	)
	lut = [round(255 * ((value / 255) ** gamma)) for value in range(256)]
	rgb = rgb.point(lut * 3)
	rgb = ImageEnhance.Contrast(rgb).enhance(ADVISOR_PORTRAIT_GRADE_CONTRAST)
	baseline = rgb.convert("RGBA")
	baseline.putalpha(alpha)
	weights = advisor_background_weights(
		portrait.size,
		face_local_box,
		ADVISOR_BACKGROUND_PROTECTION_EXPANSION,
		ADVISOR_BACKGROUND_PROTECTION_FEATHER,
	)
	pixels = list(baseline.getdata())
	weighted_luminance = [
		(advisor_srgb_luminance(pixel), weight)
		for pixel, weight in zip(pixels, weights)
		if pixel[3] > ADVISOR_WINDOW_ALPHA_THRESHOLD and weight > 0.0
	]
	weight_sum = sum(weight for _, weight in weighted_luminance)
	if weight_sum <= 0.0:
		raise ValueError("Advisor background normalization has no visible samples")
	background_mean = sum(
		value * weight for value, weight in weighted_luminance
	) / weight_sum
	background_std = math.sqrt(
		sum(
			weight * ((value - background_mean) ** 2)
			for value, weight in weighted_luminance
		) / weight_sum
	)
	if background_std <= 0.000001:
		raise ValueError("Advisor background normalization source has zero contrast")
	scale = background_target_std / background_std
	changed_pixels: list[tuple[int, int, int, int]] = []
	for pixel, weight in zip(pixels, weights):
		red, green, blue, pixel_alpha = pixel
		if pixel_alpha <= ADVISOR_WINDOW_ALPHA_THRESHOLD or weight <= 0.0:
			changed_pixels.append(pixel)
			continue
		luminance = advisor_srgb_luminance(pixel)
		target = background_target_mean + (luminance - background_mean) * scale
		delta = (target - luminance) * weight
		changed_pixels.append(
			(
				max(0, min(255, round(red + delta))),
				max(0, min(255, round(green + delta))),
				max(0, min(255, round(blue + delta))),
				pixel_alpha,
			)
		)
	candidate = Image.new("RGBA", baseline.size)
	candidate.putdata(changed_pixels)
	mode, strength = smoothing
	if mode == "blur":
		blurred_pixels = list(
			candidate.convert("RGB")
			.filter(ImageFilter.GaussianBlur(ADVISOR_BACKGROUND_SMOOTHING_RADIUS))
			.getdata()
		)
		smoothed_pixels: list[tuple[int, int, int, int]] = []
		for pixel, blurred, weight in zip(
			candidate.getdata(), blurred_pixels, weights
		):
			blend = strength * weight
			smoothed_pixels.append(
				(
					round(pixel[0] * (1.0 - blend) + blurred[0] * blend),
					round(pixel[1] * (1.0 - blend) + blurred[1] * blend),
					round(pixel[2] * (1.0 - blend) + blurred[2] * blend),
					pixel[3],
				)
			)
		candidate.putdata(smoothed_pixels)
	elif mode != "none":
		raise ValueError(f"Unknown advisor background smoothing mode: {smoothing}")
	background_identity = advisor_weighted_identity_metrics(
		baseline,
		candidate,
		weights,
	)
	return baseline, candidate, background_identity, {
		"source_weighted_mean": round(background_mean, 6),
		"source_weighted_std": round(background_std, 6),
		"target_mean": background_target_mean,
		"target_std": background_target_std,
		"protection_expansion": ADVISOR_BACKGROUND_PROTECTION_EXPANSION,
		"protection_feather": ADVISOR_BACKGROUND_PROTECTION_FEATHER,
		"smoothing_mode": mode,
		"smoothing_radius": (
			ADVISOR_BACKGROUND_SMOOTHING_RADIUS if mode == "blur" else 0.0
		),
		"smoothing_strength": strength,
	}


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


def grade_advisor_paper_candidate(
	paper: Image.Image,
	target_mean: float,
	target_std: float,
) -> tuple[Image.Image, dict[str, float | int]]:
	"""Apply the only permitted per-source paper adjustment: uniform RGB tone."""
	candidate = advisor_apply_luminance_affine(
		paper,
		target_mean,
		target_std,
		ADVISOR_WINDOW_ALPHA_THRESHOLD,
	)
	identity = advisor_region_identity_metrics(
		paper,
		candidate,
		(0, 0, paper.width, paper.height),
	)
	if not advisor_paper_identity_passes(identity):
		raise ValueError(f"Advisor paper normalization exceeds identity gates: {identity}")
	return candidate, identity


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


def validate_advisor_paper_palette(paper: Image.Image) -> dict[str, object]:
	metrics = layer_palette_metrics(paper, ADVISOR_WINDOW_ALPHA_THRESHOLD)
	mean_rgb = metrics["mean_rgb"]
	if not (
		204 <= metrics["mean_luminance"] <= 214
		and 0.190 <= metrics["mean_saturation"] <= 0.245
		and 220 <= mean_rgb[0] <= 231
		and 202 <= mean_rgb[1] <= 213
		and 171 <= mean_rgb[2] <= 183
		and 12 <= mean_rgb[0] - mean_rgb[1] <= 24
		and 24 <= mean_rgb[1] - mean_rgb[2] <= 38
	):
		raise ValueError(
			"Advisor paper does not match the pale low-chroma vanilla note: "
			f"metrics were {metrics}"
		)
	return metrics


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

	def paper_component(reference: Image.Image) -> set[tuple[int, int]]:
		"""Return the largest connected pale-parchment component in one reference."""
		rgba = reference.convert("RGBA")
		eligible: set[tuple[int, int]] = set()
		for y in range(rgba.height):
			for x in range(rgba.width):
				red, green, blue, alpha = rgba.getpixel((x, y))
				if (
					alpha > 192
					and red > 150
					and green > 120
					and blue > 80
					and red >= green >= blue
				):
					eligible.add((x, y))
		components: list[set[tuple[int, int]]] = []
		unvisited = set(eligible)
		while unvisited:
			start = min(unvisited)
			component = {start}
			stack = [start]
			unvisited.remove(start)
			while stack:
				x, y = stack.pop()
				for neighbour in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
					if neighbour in unvisited:
						unvisited.remove(neighbour)
						component.add(neighbour)
						stack.append(neighbour)
			components.append(component)
		if not components:
			raise ValueError("Canonical advisor reference has no parchment component")
		return max(components, key=lambda component: (len(component), -min(component)[0], -min(component)[1]))

	per_reference: list[dict[str, object]] = []
	for name, reference in zip(ADVISOR_REFERENCE_NAMES, references):
		rgba = reference.convert("RGBA")
		component = paper_component(rgba)
		geometry = geometry_metrics_from_points(sorted(component))
		luminance_values: list[float] = []
		saturation_values: list[float] = []
		for point in component:
			red, green, blue, _ = rgba.getpixel(point)
			luminance_values.append(
				advisor_srgb_luminance((red, green, blue, 255))
			)
			maximum = max(red, green, blue)
			saturation_values.append(
				0.0 if maximum == 0 else (maximum - min(red, green, blue)) / maximum
			)
		per_reference.append(
			{
				"name": name,
				"decoded_rgba_sha256": decoded_rgba_sha256(rgba),
				**geometry,
				"coverage_gt_32": round(len(component) / (ADVISOR_SIZE[0] * ADVISOR_SIZE[1]), 6),
				"mean_luminance": round(
					sum(luminance_values) / len(luminance_values), 6
				),
				"mean_saturation": round(
					sum(saturation_values) / len(saturation_values), 6
				),
			}
		)

	for invariant in ("bbox_gt_32", "width", "height"):
		values = [record[invariant] for record in per_reference]
		if any(value != values[0] for value in values[1:]):
			raise ValueError(
				f"Canonical advisor paper {invariant} is not shared by all six references: "
				f"{values}"
			)

	def mean(key: str) -> float:
		return round(
			sum(float(record[key]) for record in per_reference) / len(per_reference),
			6,
		)

	aggregate = {
		"bbox_gt_32": list(per_reference[0]["bbox_gt_32"]),
		"width": int(per_reference[0]["width"]),
		"height": int(per_reference[0]["height"]),
		"area_gt_32": mean("area_gt_32"),
		"coverage_gt_32": mean("coverage_gt_32"),
		"center": [
			round(
				sum(float(record["center"][axis]) for record in per_reference)
				/ len(per_reference),
				6,
			)
			for axis in range(2)
		],
		"top_edge_image_slope": mean("top_edge_image_slope"),
		"top_edge_image_angle_degrees": mean("top_edge_image_angle_degrees"),
		"mean_luminance": mean("mean_luminance"),
		"mean_saturation": mean("mean_saturation"),
	}
	aggregate_sha256 = canonical_json_sha256(aggregate)
	if aggregate != ADVISOR_CANONICAL_PAPER_FAMILY:
		raise ValueError(
			"Canonical advisor paper derivation changed: "
			f"expected={ADVISOR_CANONICAL_PAPER_FAMILY}, actual={aggregate}"
		)
	if aggregate_sha256 != ADVISOR_CANONICAL_PAPER_FAMILY_SHA256:
		raise ValueError(
			"Canonical advisor paper derivation hash changed: "
			f"expected={ADVISOR_CANONICAL_PAPER_FAMILY_SHA256}, actual={aggregate_sha256}"
		)
	return {
		**aggregate,
		"derivation": {
			"schema": "largest_four_connected_pale_parchment_component_v1",
			"selection": (
				"alpha_gt_192; red_gt_150; green_gt_120; blue_gt_80; "
				"red_gte_green_gte_blue"
			),
			"aggregate_sha256": aggregate_sha256,
			"references": per_reference,
		},
	}


def canonical_advisor_alpha_envelope(
	reference_dir: Path,
) -> tuple[Image.Image, dict[str, object]]:
	"""Return the verified native alpha envelope shared by vanilla advisors.

	The six frozen references differ in their visible portraits, but their
	65x67 dossier silhouettes are effectively the same.  A rounded per-pixel
	mean preserves their real soft edges and contact shadow exactly; it is used
	only as an opacity matte over the ImageGen-authored frame and paper RGB.
	No visible vanilla artwork is copied into the candidate.
	"""
	alpha_layers: list[list[int]] = []
	reference_records: list[dict[str, str]] = []
	for name in ADVISOR_REFERENCE_NAMES:
		path = reference_dir / name
		if not path.is_file():
			raise FileNotFoundError(f"Missing canonical advisor reference: {path}")
		with Image.open(path) as image:
			reference = image.convert("RGBA")
		if reference.size != ADVISOR_SIZE:
			raise ValueError(f"Canonical advisor reference is not 65x67: {path}")
		alpha_layers.append(list(reference.getchannel("A").getdata()))
		reference_records.append({"path": str(path), "sha256": sha256_file(path)})

	mean_values = [
		round(sum(values) / len(values))
		for values in zip(*alpha_layers)
	]
	decoded_alpha_sha256 = hashlib.sha256(bytes(mean_values)).hexdigest()
	if decoded_alpha_sha256 != ADVISOR_CANONICAL_ALPHA_SHA256:
		raise ValueError(
			"Canonical advisor alpha envelope changed: "
			f"expected={ADVISOR_CANONICAL_ALPHA_SHA256}, "
			f"actual={decoded_alpha_sha256}"
		)
	alpha = Image.new("L", ADVISOR_SIZE)
	alpha.putdata(mean_values)
	return alpha, {
		"method": ADVISOR_CANONICAL_ALPHA_METHOD,
		"decoded_alpha_sha256": decoded_alpha_sha256,
		"reference_count": len(reference_records),
		"references": reference_records,
		"visible_artwork_source": "ImageGen frame, ImageGen paper, and approved portrait only",
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
) -> tuple[
	Image.Image,
	Image.Image,
	tuple[float, float, float, float],
	tuple[float, float, float, float],
]:
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
	portrait_source_native = source_crop.resize(
		(window_width, window_height),
		Image.Resampling.LANCZOS,
		box=fit_box,
	)
	# The source kind and deterministic seed remain part of the public function
	# contract and provenance, but advisor mode must not synthesize grain or a
	# vignette from either value. All visible texture comes from authored inputs.
	_ = (source_kind, seed_text)
	portrait = advisor_portrait_base_finish(portrait_source_native)

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
	return portrait_source_native, portrait, mapped_face, fit_box


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


def advisor_native_style_check_values(metrics: dict[str, object]) -> dict[str, float | int]:
	return {
		"top_frame_variation": float(metrics["top_frame"]["variation"]),
		"left_rail_variation": float(metrics["left_rail"]["variation"]),
		"left_rail_mean": float(metrics["left_rail"]["mean"]),
		"left_rail_std": float(metrics["left_rail"]["std"]),
		"paper_mean": float(metrics["paper"]["mean"]),
		"paper_std": float(metrics["paper"]["std"]),
		"paper_samples": int(metrics["paper"]["samples"]),
		"portrait_mean": float(metrics["portrait"]["mean"]),
		"bottom_area_variation": float(metrics["bottom_area"]["variation"]),
	}


def advisor_native_style_band_record(
	image: Image.Image,
	minimum_margin: float = 0.0,
) -> dict[str, object]:
	metrics = advisor_native_style_metrics(image)
	values = advisor_native_style_check_values(metrics)
	margins: dict[str, float] = {}
	center_sse = 0.0
	failures: dict[str, object] = {}
	for name, value in values.items():
		lower, upper = ADVISOR_NATIVE_STYLE_BANDS[name]
		width = upper - lower
		margin = min((float(value) - lower) / width, (upper - float(value)) / width)
		margins[name] = margin
		center = (lower + upper) / 2
		center_sse += ((float(value) - center) / (width / 2)) ** 2
		if margin < minimum_margin:
			failures[name] = {
				"value": value,
				"band": [lower, upper],
				"normalized_margin": round(margin, 6),
				"required_margin": minimum_margin,
			}
	return {
		"metrics": metrics,
		"values": values,
		"margins": {name: round(value, 6) for name, value in margins.items()},
		"minimum_margin": round(min(margins.values()), 6),
		"center_sse": round(center_sse, 6),
		"failures": failures,
		"passed": not failures,
	}


def advisor_portrait_layer(
	portrait: Image.Image,
	window_bbox: tuple[int, int, int, int],
	window_mask: Image.Image,
) -> Image.Image:
	layer = Image.new("RGBA", ADVISOR_SIZE, (0, 0, 0, 0))
	layer.alpha_composite(portrait, (window_bbox[0], window_bbox[1]))
	layer.putalpha(ImageChops.multiply(layer.getchannel("A"), window_mask))
	return layer


def advisor_shifted_alpha(
	alpha: Image.Image,
	offset: tuple[int, int],
	opacity: float,
	blur: float,
) -> Image.Image:
	shifted = Image.new("L", ADVISOR_SIZE, 0)
	source = alpha.point(lambda value: round(value * opacity))
	if blur:
		source = source.filter(ImageFilter.GaussianBlur(blur))
	shifted.paste(source, offset)
	return shifted


def compose_advisor_candidate(
	frame: Image.Image,
	frame_alpha: Image.Image,
	window_mask: Image.Image,
	portrait_layer: Image.Image,
	paper: Image.Image | None,
	paper_alpha: Image.Image | None,
	canonical_alpha: Image.Image,
	enforce_support: bool = True,
) -> tuple[Image.Image, dict[str, int]]:
	"""Compose through the production layer order and prove RGB provenance."""
	canvas = Image.new("RGBA", ADVISOR_SIZE, (0, 0, 0, 0))
	shadow_support = Image.new("L", ADVISOR_SIZE, 0)
	authored_support = Image.new("L", ADVISOR_SIZE, 0)
	# A low-opacity backing shadow derived only from the verified vanilla alpha
	# envelope supplies RGB only at the proven faint antialiased fringe. Every
	# substantive alpha pixel must still be supported by authored layers or their
	# permitted alpha-derived shadows.
	backing_alpha = canonical_alpha.point(
		lambda value: (
			max(1, round(value * ADVISOR_CANONICAL_BACKING_SHADOW_OPACITY))
			if 0 < value <= ADVISOR_CANONICAL_BACKING_MAX_ALPHA
			else 0
		)
	)
	backing = Image.new("RGBA", ADVISOR_SIZE, (0, 0, 0, 255))
	backing.putalpha(backing_alpha)
	canvas.alpha_composite(backing)
	card_alpha = ImageChops.lighter(frame_alpha, window_mask)
	for offset, opacity, blur in ADVISOR_CARD_SHADOW_LAYERS:
		composite_alpha_shadow(canvas, card_alpha, offset, opacity, blur)
		shadow_support = ImageChops.lighter(
			shadow_support,
			advisor_shifted_alpha(card_alpha, offset, opacity, blur),
		)
	canvas.alpha_composite(portrait_layer)
	authored_support = ImageChops.lighter(
		authored_support, portrait_layer.getchannel("A")
	)
	canvas.alpha_composite(frame)
	authored_support = ImageChops.lighter(authored_support, frame.getchannel("A"))
	if paper is not None and paper_alpha is not None:
		for offset, opacity, blur in ADVISOR_PAPER_SHADOW_LAYERS:
			composite_alpha_shadow(canvas, paper_alpha, offset, opacity, blur)
			shadow_support = ImageChops.lighter(
				shadow_support,
				advisor_shifted_alpha(paper_alpha, offset, opacity, blur),
			)
		canvas.alpha_composite(paper)
		authored_support = ImageChops.lighter(
			authored_support, paper.getchannel("A")
		)
	canvas.putalpha(canonical_alpha)
	canonical_values = list(canonical_alpha.getdata())
	authored_values = list(authored_support.getdata())
	shadow_values = list(shadow_support.getdata())
	backing_values = list(backing_alpha.getdata())
	unsupported_visible = sum(
		canonical_value > 0
		and authored_value == 0
		and shadow_value == 0
		and backing_value == 0
		for canonical_value, authored_value, shadow_value, backing_value in zip(
			canonical_values,
			authored_values,
			shadow_values,
			backing_values,
		)
	)
	unsupported_substantive = sum(
		canonical_value > ADVISOR_RGB_SUBSTANTIVE_ALPHA_THRESHOLD
		and authored_value == 0
		and shadow_value == 0
		for canonical_value, authored_value, shadow_value in zip(
			canonical_values, authored_values, shadow_values
		)
	)
	unsupported_high_alpha_source = sum(
		canonical_value > 128
		and authored_value == 0
		and shadow_value == 0
		for canonical_value, authored_value, shadow_value in zip(
			canonical_values, authored_values, shadow_values
		)
	)
	if enforce_support and (
		unsupported_visible
		or unsupported_substantive
		or unsupported_high_alpha_source
	):
		raise ValueError(
			"Canonical advisor alpha exposes RGB outside authored portrait/dossier "
			"layers, permitted alpha-derived shadows, or the faint fringe backing: "
			f"visible={unsupported_visible}, substantive={unsupported_substantive}, "
			f"high_alpha_without_authored_or_shadow={unsupported_high_alpha_source}"
		)
	return canvas, {
		"canonical_visible_pixels": sum(value > 0 for value in canonical_values),
		"authored_supported_pixels": sum(value > 0 for value in authored_values),
		"shadow_supported_pixels": sum(value > 0 for value in shadow_values),
		"faint_fringe_backing_pixels": sum(value > 0 for value in backing_values),
		"unsupported_visible_pixels": unsupported_visible,
		"unsupported_substantive_pixels": unsupported_substantive,
		"unsupported_high_alpha_source_pixels": unsupported_high_alpha_source,
	}


def advisor_face_local_box(
	mapped_face: tuple[float, float, float, float],
	window_bbox: tuple[int, int, int, int],
	portrait: Image.Image,
) -> tuple[int, int, int, int]:
	return (
		max(0, int(math.floor(mapped_face[0] - window_bbox[0]))),
		max(0, int(math.floor(mapped_face[1] - window_bbox[1]))),
		min(portrait.width, int(math.ceil(mapped_face[2] - window_bbox[0]))),
		min(portrait.height, int(math.ceil(mapped_face[3] - window_bbox[1]))),
	)


def make_advisor(
	source_crop: Image.Image,
	source_kind: str,
	seed_text: str,
	frame_overlay: Image.Image,
	paper_overlay: Image.Image,
	crop_box: tuple[int, int, int, int],
	face_box: tuple[int, int, int, int],
	reference_dir: Path,
) -> tuple[Image.Image, dict[str, object]]:
	"""Build one advisor card with a fail-closed vanilla-native search.

	The ImageGen frame and paper, their geometry, every alpha rule, every shadow,
	the crop, and the face box are immutable. Search is limited to bounded,
	chroma-preserving RGB normalization of the authored portrait and paper.
	"""
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
	if (
		frame_grade_delta_luminance > ADVISOR_FRAME_MAX_LUMINANCE_GRADE_DELTA
		or frame_grade_delta_saturation > ADVISOR_FRAME_MAX_SATURATION_GRADE_DELTA
	):
		raise ValueError(
			"Advisor frame grading exceeds the restrained vanilla calibration delta: "
			f"luminance={frame_grade_delta_luminance:.4f}, "
			f"saturation={frame_grade_delta_saturation:.4f}"
		)
	window_mask, window_bbox, window_area = enclosed_alpha_window(frame)
	frame_alpha = advisor_frame_composition_alpha(raw_frame_alpha)
	frame.putalpha(frame_alpha)

	paper_base, paper_source_bbox = normalize_generated_layer(
		paper_overlay,
		ADVISOR_PAPER_SIZE,
		ADVISOR_PAPER_POSITION,
		ADVISOR_PAPER_ANGLE,
	)
	paper_base = grade_advisor_paper(paper_base)
	raw_paper_alpha = paper_base.getchannel("A")
	base_paper_palette = validate_advisor_paper_palette(paper_base)
	base_paper_luminance_values = [
		advisor_srgb_luminance(pixel)
		for pixel in paper_base.getdata()
		if pixel[3] > ADVISOR_WINDOW_ALPHA_THRESHOLD
	]
	base_paper_luminance_mean, base_paper_luminance_std = advisor_luminance_statistics(
		base_paper_luminance_values
	)
	paper_geometry = paper_geometry_metrics(paper_base)
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
	paper_base.putalpha(paper_alpha)

	(
		portrait_source_native,
		portrait_base,
		mapped_face,
		portrait_fit_box,
	) = fit_advisor_portrait(
		source_crop,
		source_kind,
		seed_text,
		crop_box,
		face_box,
		window_bbox,
	)
	face_metrics = validate_face_placement(mapped_face, window_bbox, paper_base)
	face_local_box = advisor_face_local_box(
		mapped_face,
		window_bbox,
		portrait_base,
	)
	canonical_alpha, canonical_alpha_metadata = canonical_advisor_alpha_envelope(
		reference_dir
	)

	rejections: dict[str, int] = {}

	def reject(reason: str) -> None:
		rejections[reason] = rejections.get(reason, 0) + 1

	portrait_attempted = 0
	portrait_candidates: list[dict[str, object]] = []
	for (
		search_stage_index,
		(
			search_stage_name,
			gamma_options,
			background_mean_options,
			background_std_options,
			smoothing_options,
		),
	) in enumerate(
		ADVISOR_BACKGROUND_SEARCH_STAGES
	):
		stage_candidates: list[dict[str, object]] = []
		for gamma, background_mean, background_std, smoothing in itertools.product(
			gamma_options,
			background_mean_options,
			background_std_options,
			smoothing_options,
		):
			portrait_attempted += 1
			(
				baseline,
				portrait,
				background_identity,
				background_processing,
			) = grade_advisor_portrait_candidate(
				portrait_base,
				gamma,
				background_mean,
				background_std,
				smoothing,
				face_local_box,
			)
			if not advisor_background_identity_passes(background_identity):
				reject("portrait_background_identity")
				continue
			identity = advisor_region_identity_metrics(
				baseline,
				portrait,
				face_local_box,
			)
			if not advisor_face_identity_passes(identity):
				reject("portrait_face_identity")
				continue
			source_identity = advisor_region_identity_metrics(
				portrait_source_native,
				portrait,
				face_local_box,
			)
			if not advisor_source_face_identity_passes(source_identity):
				reject("portrait_source_face_identity")
				continue
			try:
				face_palette = advisor_face_palette_metrics(
					portrait,
					mapped_face,
					window_bbox,
				)
			except ValueError:
				reject("portrait_palette")
				continue
			portrait_layer = advisor_portrait_layer(
				portrait,
				window_bbox,
				window_mask,
			)
			try:
				prefilter_canvas, _ = compose_advisor_candidate(
					frame,
					frame_alpha,
					window_mask,
					portrait_layer,
					None,
					None,
					canonical_alpha,
					False,
				)
			except ValueError:
				reject("rgb_support_prefilter")
				continue
			top = advisor_native_roi_metrics(
				prefilter_canvas,
				ADVISOR_NATIVE_STYLE_ROIS["top_frame"],
			)
			left = advisor_native_roi_metrics(
				prefilter_canvas,
				ADVISOR_NATIVE_STYLE_ROIS["left_rail"],
			)
			prefilter_values = {
				"top_frame_variation": float(top["variation"]),
				"left_rail_variation": float(left["variation"]),
				"left_rail_mean": float(left["mean"]),
				"left_rail_std": float(left["std"]),
			}
			prefilter_margins: dict[str, float] = {}
			prefilter_sse = 0.0
			for name, value in prefilter_values.items():
				lower, upper = ADVISOR_NATIVE_STYLE_BANDS[name]
				width = upper - lower
				prefilter_margins[name] = min(
					(value - lower) / width,
					(upper - value) / width,
				)
				center = (lower + upper) / 2
				prefilter_sse += ((value - center) / (width / 2)) ** 2
			if min(prefilter_margins.values()) < ADVISOR_MIN_NATIVE_STYLE_MARGIN:
				reject("portrait_top_left_native_bands")
				continue
			mode, strength = smoothing
			parameters = {
				"search_stage_index": search_stage_index,
				"search_stage_name": search_stage_name,
				"gamma": gamma,
				"background_target_mean": background_mean,
				"background_target_std": background_std,
				"background_smoothing_mode": mode,
				"background_smoothing_radius": (
					ADVISOR_BACKGROUND_SMOOTHING_RADIUS
					if mode == "blur"
					else 0.0
				),
				"background_smoothing_strength": strength,
			}
			minimum_prefilter_margin = min(prefilter_margins.values())
			preliminary_key = (
				int(mode != "none"),
				strength,
				float(background_identity["newly_clipped_ratio"]),
				-minimum_prefilter_margin,
				prefilter_sse,
				float(background_identity["normalized_luminance_mae"]),
				max(
					0.0,
					1.0 - float(background_identity["gradient_correlation"]),
				),
				float(identity["newly_clipped_ratio"]),
				max(0.0, 1.0 - float(identity["gradient_correlation"])),
				float(source_identity["newly_clipped_ratio"]),
				max(
					0.0,
					1.0 - float(source_identity["gradient_correlation"]),
				),
				abs(gamma - 0.65),
				gamma,
				background_mean,
				background_std,
				mode,
				strength,
				decoded_rgba_sha256(portrait),
			)
			stage_candidates.append(
				{
					"portrait": portrait,
					"layer": portrait_layer,
					"parameters": parameters,
					"background_processing": background_processing,
					"background_identity": background_identity,
					"identity": identity,
					"source_identity": source_identity,
					"face_palette": face_palette,
					"prefilter_values": prefilter_values,
					"prefilter_margins": {
						name: round(value, 6)
						for name, value in prefilter_margins.items()
					},
					"preliminary_key": preliminary_key,
					"decoded_rgba_sha256": decoded_rgba_sha256(portrait),
				}
			)
		stage_candidates.sort(key=lambda record: record["preliminary_key"])
		portrait_candidates.extend(
			stage_candidates[
				:ADVISOR_MAX_RETAINED_PORTRAIT_CANDIDATES_PER_STAGE
			]
		)
	if not portrait_candidates:
		raise ValueError(
			"No face-protected portrait candidate reaches the frozen vanilla top/left "
			f"bands; attempted={portrait_attempted}, rejections={rejections}"
		)

	paper_attempted = 0
	paper_candidates: list[dict[str, object]] = []
	for target_mean, target_std in itertools.product(
		ADVISOR_PAPER_MEAN_LATTICE,
		ADVISOR_PAPER_STD_LATTICE,
	):
		paper_attempted += 1
		try:
			paper, paper_identity = grade_advisor_paper_candidate(
				paper_base,
				target_mean,
				target_std,
			)
			paper.putalpha(paper_alpha)
			paper_palette = validate_advisor_paper_palette(paper)
		except ValueError:
			reject("paper_identity_or_palette")
			continue
		paper_candidates.append(
			{
				"paper": paper,
				"parameters": {
					"target_mean": target_mean,
					"target_std": target_std,
				},
				"identity": paper_identity,
				"palette": paper_palette,
				"decoded_rgba_sha256": decoded_rgba_sha256(paper),
			}
		)
	if not paper_candidates:
		raise ValueError(
			"No fixed-geometry ImageGen paper candidate passes the vanilla palette "
			f"and identity gates; attempted={paper_attempted}, rejections={rejections}"
		)

	final_attempted = 0
	feasible_count = 0
	chosen: dict[str, object] | None = None
	closest_rejected: dict[str, object] | None = None
	base_paper_mean = float(base_paper_palette["mean_luminance"])
	for portrait_record, paper_record in itertools.product(
		portrait_candidates,
		paper_candidates,
	):
		final_attempted += 1
		try:
			canvas, support = compose_advisor_candidate(
				frame,
				frame_alpha,
				window_mask,
				portrait_record["layer"],
				paper_record["paper"],
				paper_alpha,
				canonical_alpha,
			)
		except ValueError:
			reject("rgb_support_final")
			continue
		band_record = advisor_native_style_band_record(
			canvas,
			ADVISOR_MIN_NATIVE_STYLE_MARGIN,
		)
		if not band_record["passed"]:
			closest_key = (
				-float(band_record["minimum_margin"]),
				float(band_record["center_sse"]),
				str(portrait_record["decoded_rgba_sha256"]),
				str(paper_record["decoded_rgba_sha256"]),
			)
			if (
				closest_rejected is None
				or closest_key < closest_rejected["selection_key"]
			):
				closest_rejected = {
					"selection_key": closest_key,
					"portrait_parameters": portrait_record["parameters"],
					"paper_parameters": paper_record["parameters"],
					"native_style": band_record,
				}
			for name in band_record["failures"]:
				reject(f"native_band_{name}")
			continue
		portrait_parameters = portrait_record["parameters"]
		paper_parameters = paper_record["parameters"]
		mode = str(portrait_parameters["background_smoothing_mode"])
		strength = float(portrait_parameters["background_smoothing_strength"])
		identity = portrait_record["identity"]
		background_identity = portrait_record["background_identity"]
		paper_displacement = (
			abs(float(paper_parameters["target_mean"]) - base_paper_mean) / 8
			+ abs(float(paper_parameters["target_std"]) - base_paper_luminance_std) / 6
		)
		parameter_tuple = (
			float(portrait_parameters["gamma"]),
			float(portrait_parameters["background_target_mean"]),
			float(portrait_parameters["background_target_std"]),
			mode,
			float(portrait_parameters["background_smoothing_radius"]),
			strength,
			float(paper_parameters["target_mean"]),
			float(paper_parameters["target_std"]),
		)
		selection_key = (
			int(mode != "none"),
			strength,
			float(background_identity["newly_clipped_ratio"]),
			float(identity["newly_clipped_ratio"]),
			-float(band_record["minimum_margin"]),
			float(band_record["center_sse"]),
			float(background_identity["normalized_luminance_mae"]),
			max(
				0.0,
				1.0 - float(background_identity["gradient_correlation"]),
			),
			max(0.0, 1.0 - float(identity["gradient_correlation"])),
			paper_displacement,
			abs(float(portrait_parameters["gamma"]) - 0.65),
			parameter_tuple,
			decoded_rgba_sha256(canvas),
		)
		candidate_record = {
			"canvas": canvas,
			"portrait": portrait_record,
			"paper": paper_record,
			"native_style": band_record,
			"support": support,
			"selection_key": selection_key,
			"decoded_rgba_sha256": decoded_rgba_sha256(canvas),
		}
		feasible_count += 1
		if chosen is None or selection_key < chosen["selection_key"]:
			chosen = candidate_record
	if chosen is None:
		raise ValueError(
			"No advisor candidate passes every frozen vanilla native-style band with "
			f"the required margin; final_attempted={final_attempted}, "
			f"portrait_retained={len(portrait_candidates)}, "
			f"paper_retained={len(paper_candidates)}, rejections={rejections}, "
			f"closest_rejected={closest_rejected}"
		)
	canvas = chosen["canvas"]
	chosen_portrait = chosen["portrait"]
	chosen_paper = chosen["paper"]
	paper_palette = chosen_paper["palette"]
	face_palette = chosen_portrait["face_palette"]
	lattice = {
		"background_search_stages": [
			{
				"name": name,
				"gamma": list(gamma),
				"target_mean": list(means),
				"target_std": list(stds),
				"smoothing": [list(values) for values in smoothing],
			}
			for name, gamma, means, stds, smoothing in (
				ADVISOR_BACKGROUND_SEARCH_STAGES
			)
		],
		"background_protection_expansion": ADVISOR_BACKGROUND_PROTECTION_EXPANSION,
		"background_protection_feather": ADVISOR_BACKGROUND_PROTECTION_FEATHER,
		"background_smoothing_radius": ADVISOR_BACKGROUND_SMOOTHING_RADIUS,
		"maximum_retained_portrait_candidates_per_stage": (
			ADVISOR_MAX_RETAINED_PORTRAIT_CANDIDATES_PER_STAGE
		),
		"paper_target_mean": list(ADVISOR_PAPER_MEAN_LATTICE),
		"paper_target_std": list(ADVISOR_PAPER_STD_LATTICE),
	}

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
		"portrait_source_native_decoded_rgba_sha256": decoded_rgba_sha256(
			portrait_source_native
		),
		"face_placement": face_metrics,
		"face_palette": face_palette,
		"source_face_identity": chosen_portrait["source_identity"],
		"face_identity": chosen_portrait["identity"],
		"background_processing": chosen_portrait["background_processing"],
		"background_identity": chosen_portrait["background_identity"],
		"paper_source_visible_bbox": list(paper_source_bbox),
		"paper_native_size": list(ADVISOR_PAPER_SIZE),
		"paper_native_position": list(ADVISOR_PAPER_POSITION),
		"paper_angle_degrees": ADVISOR_PAPER_ANGLE,
		"paper_geometry": paper_geometry,
		"paper_palette": paper_palette,
		"paper_base_palette": base_paper_palette,
		"paper_base_luminance_statistics": {
			"mean": round(base_paper_luminance_mean, 6),
			"std": round(base_paper_luminance_std, 6),
		},
		"paper_identity": chosen_paper["identity"],
		"paper_composition_alpha_coverage_gt_32": round(
			alpha_coverage(paper_alpha, 32), 6
		),
		"paper_composition_opacity": paper_opacity,
		"paper_window_overlap_ratio": round(paper_window_overlap, 6),
		"shadow_contract": (
			"alpha_derived_rgb_shadows_plus_verified_six_reference_mean_alpha_envelope"
		),
		"canonical_alpha_envelope": canonical_alpha_metadata,
		"native_search": {
			"schema": ADVISOR_SEARCH_SCHEMA,
			"normalization_schema": ADVISOR_NORMALIZATION_SCHEMA,
			"python_version": platform.python_version(),
			"pillow_version": PILLOW_VERSION,
			"lattice": lattice,
			"lattice_sha256": canonical_json_sha256(lattice),
			"minimum_native_style_margin": ADVISOR_MIN_NATIVE_STYLE_MARGIN,
			"portrait_search_stages_attempted": len(
				ADVISOR_BACKGROUND_SEARCH_STAGES
			),
			"portrait_search_stage_used": chosen_portrait["parameters"][
				"search_stage_index"
			],
			"portrait_search_stage_name": chosen_portrait["parameters"][
				"search_stage_name"
			],
			"attempted": {
				"portrait": portrait_attempted,
				"paper": paper_attempted,
				"final_cross_product": final_attempted,
			},
			"retained": {
				"portrait": len(portrait_candidates),
				"paper": len(paper_candidates),
				"feasible_final": feasible_count,
			},
			"rejections": dict(sorted(rejections.items())),
			"chosen_portrait_parameters": chosen_portrait["parameters"],
			"chosen_background_processing": chosen_portrait[
				"background_processing"
			],
			"chosen_background_identity": chosen_portrait["background_identity"],
			"chosen_paper_parameters": chosen_paper["parameters"],
			"chosen_selection_key": list(chosen["selection_key"]),
			"chosen_native_style": chosen["native_style"],
			"chosen_rgb_support": chosen["support"],
			"chosen_portrait_layer_sha256": chosen_portrait["decoded_rgba_sha256"],
			"chosen_paper_layer_sha256": chosen_paper["decoded_rgba_sha256"],
			"chosen_final_decoded_rgba_sha256": chosen["decoded_rgba_sha256"],
			"candidate_status": "candidate_requires_visual_approval",
		},
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

	native_style_validation = validate_advisor_native_style_metrics(finished)

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
		"native_style_validation": native_style_validation,
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
	role_family: str = "leader",
) -> Image.Image:
	if mode == "advisor":
		items: list[tuple[str, Image.Image]] = [
			(
				PROCESSOR_INPUT_CROP_LABEL,
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
		return sheet

	if role_family not in ROLE_FAMILY_REFERENCE_NAMES:
		raise ValueError(f"Unsupported full-size role family: {role_family}")
	reference_names = ROLE_FAMILY_REFERENCE_NAMES[role_family]
	display_size = LEADER_SIZE
	scale = 2

	items: list[tuple[str, Image.Image]] = [
		(
			PROCESSOR_INPUT_CROP_LABEL,
			ImageOps.fit(source_crop, display_size, Image.Resampling.LANCZOS),
		),
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
	return sheet


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
		"--role-family",
		choices=("leader", "commander"),
		default="leader",
		help=(
			"Full-size style-reference family. Use --role-family commander for an "
			"army or navy commander; leader is the backward-compatible default."
		),
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
		"--portrait-provenance-manifest",
		type=Path,
		help=(
			"Required advisor-mode manifest that pins the portrait source, prompt, "
			"generation mode, source hash, and ImageGen or archival provenance"
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
	parser.add_argument(
		"--force",
		action="store_true",
		help="Replace existing output/review/metadata files after all validation passes",
	)
	return parser.parse_args()


def main() -> None:
	args = parse_args()
	if not args.source.is_file():
		raise FileNotFoundError(args.source)
	source_path = args.source.expanduser().resolve()
	with Image.open(source_path) as image:
		source = image.convert("RGBA")
	crop_box = parse_crop(args.crop, source)
	source_crop = source.crop(crop_box)
	face_box: tuple[int, int, int, int] | None = None
	render_version = LEADER_RENDER_VERSION if args.mode == "leader" else ADVISOR_RENDER_VERSION
	source_sha256 = sha256_file(source_path)
	if args.mode == "advisor" and args.role_family != "leader":
		raise ValueError(
			"--role-family applies to full-size leader mode; advisor mode uses its "
			"canonical advisor reference family"
		)
	role_family = args.role_family if args.mode == "leader" else "advisor"
	metadata_requested = args.metadata or args.output.with_suffix(
		args.output.suffix + ".json"
	)
	forbidden_inputs = [source_path, Path(__file__).resolve()]
	portrait_provenance_metadata: dict[str, object] | None = None
	overlay_metadata: dict[str, object] | None = None
	composition_metadata: dict[str, object] | None = None
	validation_metadata: dict[str, object] | None = None
	render_configuration: dict[str, object] | None = None
	selected_references: list[dict[str, str]] = []
	if args.mode == "leader":
		runtime = {
			"python": platform.python_version(),
			"pillow": PILLOW_VERSION,
		}
		reference_dir, selected_references = resolve_full_size_references(
			role_family,
			args.reference_dir,
		)
		for reference in selected_references:
			name = str(reference["name"])
			forbidden_inputs.append(reference_dir / name)
		output_path, review_path, metadata_path = validate_output_contract(
			args.output,
			args.review_sheet,
			metadata_requested,
			forbidden_inputs,
			args.force,
		)
		seed_record = deterministic_seed_record(
			source,
			crop_box,
			None,
			args.source_kind,
			args.mode,
			render_version,
			None,
			None,
			runtime=runtime,
			processor_sha256=sha256_file(Path(__file__).resolve()),
		)
		seed_text = str(seed_record["payload_sha256"])
		finished = make_leader(source_crop, args.source_kind, seed_text)
	else:
		runtime = verify_advisor_runtime()
		render_configuration = advisor_render_configuration()
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
		if args.portrait_provenance_manifest is None:
			raise ValueError(
				"advisor mode requires --portrait-provenance-manifest; unpinned "
				"portrait masters cannot enter the vanilla advisor workflow"
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
		portrait_provenance_metadata = verify_portrait_provenance_manifest(
			args.portrait_provenance_manifest,
			source_path,
			args.source_kind,
			crop_box,
			face_box,
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
		forbidden_inputs.extend(
			[
				args.advisor_overlay_manifest,
				args.portrait_provenance_manifest,
				args.advisor_frame_source,
				args.advisor_frame_overlay,
				args.advisor_paper_source,
				args.advisor_paper_overlay,
				Path(str(portrait_provenance_metadata["prompt_record"])),
				IMAGEGEN_ALPHA_TOOL,
			]
		)
		for input_record in portrait_provenance_metadata["generation_inputs"]:
			forbidden_inputs.append(Path(str(input_record["path"])))
		for overlay_role in ("frame", "paper"):
			overlay_role_metadata = overlay_manifest_metadata[overlay_role]
			forbidden_inputs.append(
				Path(str(overlay_role_metadata["prompt_record"]))
			)
			for input_record in overlay_role_metadata["generation_inputs"]:
				forbidden_inputs.append(Path(str(input_record["path"])))
		for name in ADVISOR_REFERENCE_NAMES:
			forbidden_inputs.append(canonical_advisor_references / name)
		selected_references = selected_reference_records(
			canonical_advisor_references,
			ADVISOR_REFERENCE_NAMES,
			ADVISOR_SIZE,
		)
		output_path, review_path, metadata_path = validate_output_contract(
			args.output,
			args.review_sheet,
			metadata_requested,
			forbidden_inputs,
			args.force,
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
			portrait_provenance_sha256=str(
				portrait_provenance_metadata["sha256"]
			),
			overlay_manifest_sha256=str(overlay_manifest_metadata["sha256"]),
			render_configuration_sha256=str(render_configuration["sha256"]),
			runtime=runtime,
			processor_sha256=sha256_file(Path(__file__).resolve()),
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
			canonical_advisor_references,
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

	review_image = make_review_sheet(
		source_crop,
		finished,
		args.mode,
		reference_dir,
		role_family,
	)
	output_payload = png_bytes(finished)
	review_payload = png_bytes(review_image)
	output_file_sha256 = hashlib.sha256(output_payload).hexdigest()
	review_file_sha256 = hashlib.sha256(review_payload).hexdigest()
	output_decoded_sha256 = decoded_rgba_sha256(finished)
	review_decoded_sha256 = decoded_rgba_sha256(review_image)
	command_record = normalized_command_record(
		args,
		metadata_path,
		role_family,
		reference_dir,
		selected_references,
	)
	metadata = {
		"processor": ".agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py",
		"processor_version": PROCESSOR_VERSION,
		"processor_sha256": sha256_file(Path(__file__).resolve()),
		"render_version": render_version,
		"runtime": runtime,
		"mode": args.mode,
		"role_family": role_family,
		"source": repo_relative_path(source_path),
		"source_kind": args.source_kind,
		"crop": list(crop_box),
		"face_box": list(face_box) if face_box is not None else None,
		"output": repo_relative_path(output_path),
		"size": list(finished.size),
		"review_sheet": repo_relative_path(review_path),
		"reference_dir": repo_relative_path(reference_dir),
		"selected_references": selected_references,
		"source_sha256": source_sha256,
		"portrait_provenance": portrait_provenance_metadata,
		"determinism": seed_record,
		"render_configuration": render_configuration,
		"generated_overlays": overlay_metadata,
		"advisor_composition": composition_metadata,
		"advisor_validation": validation_metadata,
		"command": command_record,
		"artifact_integrity": {
			"output": {
				"path": repo_relative_path(output_path),
				"format": "PNG",
				"file_sha256": output_file_sha256,
				"decoded_rgba_sha256": output_decoded_sha256,
				"decode_after_save_pixel_equality": True,
			},
			"review_sheet": {
				"path": repo_relative_path(review_path),
				"format": "PNG",
				"file_sha256": review_file_sha256,
				"decoded_rgba_sha256": review_decoded_sha256,
				"decode_after_save_pixel_equality": True,
			},
		},
		"composition_contract": (
			"crop_grade_resize_angle_alpha_shadow_composite_validate_export_only; "
			"all visible frame_paper artwork is ImageGen-authored; "
			"no programmatically drawn advisor-card artwork"
			if args.mode == "advisor"
			else "crop_grade_export_only; no programmatically drawn leader subject, emblem, or institutional scene"
		),
		"status": "candidate_requires_visual_approval",
	}
	metadata["metadata_integrity"] = {
		"schema": "canonical_json_sha256_excluding_metadata_integrity_v1",
		"payload_sha256": canonical_json_sha256(metadata),
	}
	metadata_payload = (
		json.dumps(metadata, indent=2, ensure_ascii=False) + "\n"
	).encode("utf-8")
	prepared: list[dict[str, object]] = []
	try:
		prepared.append(
			prepare_bytes(
				output_path,
				output_payload,
				"portrait candidate",
				finished,
			)
		)
		prepared.append(
			prepare_bytes(
				review_path,
				review_payload,
				"comparison review sheet",
				review_image,
			)
		)
		prepared.append(
			prepare_bytes(
				metadata_path,
				metadata_payload,
				"portrait metadata",
			)
		)
		commit_prepared_artifacts(prepared, args.force)
	except Exception:
		discard_prepared_artifacts(prepared)
		raise
	print(
		json.dumps(
			{
				"status": "candidate_requires_visual_approval",
				"output": repo_relative_path(output_path),
				"output_sha256": output_file_sha256,
				"decoded_rgba_sha256": output_decoded_sha256,
				"review_sheet": repo_relative_path(review_path),
				"metadata": repo_relative_path(metadata_path),
			},
			indent=2,
		)
	)


if __name__ == "__main__":
	main()
