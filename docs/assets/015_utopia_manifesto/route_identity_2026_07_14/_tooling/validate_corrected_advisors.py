#!/usr/bin/env python3
"""Generate or strictly validate the Event 015 advisor-v5 candidate package.

The default invocation is read-only.  ``--regenerate`` may write PNG
candidates, review sheets, processor metadata, candidate contact sheets, the
candidate validation report, checksums, and ``needs_user_review`` asset rows.
Aggregate sheets/records are replaced only after a fresh full 16-card run;
``--only`` leaves them untouched. It never converts or writes DDS files.
``--validate-installed`` is a read-only
post-install check that requires separate approval evidence. This tool never
creates approval evidence and never promotes a candidate to an approved state.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import os
import platform
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps, __version__ as PILLOW_VERSION


REPO = Path(__file__).resolve().parents[5]
BASE = REPO / "docs/assets/015_utopia_manifesto/route_identity_2026_07_14"
GENERATED = Path.home() / ".codex/generated_images"
SOURCE = BASE / "source_png/advisors"
PROCESSED = BASE / "processed_png/advisors"
FINAL = BASE / "final_dds/advisors"
DECODED = BASE / "decoded_png/advisors"
REVIEWS = BASE / "contact_sheets/advisor_reviews"
METADATA = BASE / "metadata/advisors"
CONTACT = BASE / "contact_sheets"
RUNTIME = REPO / "gfx/leaders/015_utopia_manifesto/advisors"
PROCESSOR = REPO / ".agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py"
CONVERTER = REPO / ".agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py"
OVERLAY_PACKAGE = REPO / ".agents/skills/chaos-redux-event-assets/assets/advisor_dossier_overlays"
OVERLAY_MANIFEST = OVERLAY_PACKAGE / "advisor_dossier_overlay_manifest.json"
OVERLAY_V3 = OVERLAY_PACKAGE / "v3"
FRAME_SOURCE = OVERLAY_V3 / "advisor_frame_shadowless_imagegen_source.png"
FRAME_OVERLAY = OVERLAY_V3 / "advisor_frame_shadowless_overlay.png"
PAPER_SOURCE = OVERLAY_V3 / "advisor_paper_shadowless_imagegen_source.png"
PAPER_OVERLAY = OVERLAY_V3 / "advisor_paper_shadowless_overlay.png"
PORTRAIT_MANIFEST = BASE / "advisor_portrait_source_manifest.json"
REFERENCE_DIR = REPO / ".agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors"
V2_HISTORY = BASE / "rejected_superseded_history/advisor_v2_rejected_2026_07_16"
VALIDATION_PATH = BASE / "advisor_validation_2026_07_16.json"
ASSET_RECORDS_PATH = BASE / "asset_records.json"
CHECKSUMS_PATH = BASE / "advisor_checksums.sha256"
INSTALLED_VALIDATION_PATH = BASE / "advisor_installed_validation_2026_07_16.json"
INSTALLED_NOTES = "The immutable candidate metadata remains pre-approval evidence. A separate producer-independent visual approval accepted this exact PNG, and installed validation proved the package/runtime DDS bytes identical and their decoded RGBA pixels equal to the approved PNG."

# Freeze boundary.  Keep all replaceable tool/asset hashes in this one block.
EXPECTED_PROCESSOR_SHA256 = "e248979f21784c016e69c5458b9925c32177d6af29f2cca1a82bfaaffbe1f23c"
EXPECTED_CONVERTER_SHA256 = "d8aa0ba6a16ba8b6b698ccd6cf599b90e81db6f6c6132009f07115c728f6b8a0"
EXPECTED_OVERLAY_MANIFEST_SHA256 = "8f355b36ba2a3a621c8b8e4ad0b1048ec50737e352f1d6d1a02a79ae4dd0c0db"
EXPECTED_FRAME_SOURCE_SHA256 = "a25ab14c0ac375b0d179c3d92b014de3fc03e2f25c41d34f4fe8fa02013b4ca0"
EXPECTED_FRAME_OVERLAY_SHA256 = "ebdab7434a05ad4eb8efffcf99606905a04080793780d5587aef83f146f4319c"
EXPECTED_PAPER_SOURCE_SHA256 = "2dd14d34497d5fdd18a41c7afd210118f458e64aeb7237ed928065e222d6e439"
EXPECTED_PAPER_OVERLAY_SHA256 = "98aa91005c6df3ef58954536ba23473db7a08e8f25d719dfd030319f0b5874ab"
EXPECTED_RENDER_CONFIGURATION_SHA256 = "e9f8d54d1ea7fc8845bf22675c09686acc7196556a56f96f5a1b46268b134637"
EXPECTED_PROCESSOR_VERSION = "5.0"
EXPECTED_RENDER_VERSION = "5.0"
EXPECTED_RUNTIME = {"python": "3.9.12", "pillow": "11.1.0"}
EXPECTED_ALPHA_SHA256 = "5d33afdd1adc0349e33b52bb141ddd1449107fd34727d19fcc45bcd7809d2993"
EXPECTED_ALPHA_METHOD = "rounded_per_pixel_mean_of_six_frozen_vanilla_alpha_channels"
EXPECTED_PAPER_FAMILY_SHA256 = "c751cbe5f1178c8b894c56a4cebe01bb4dae88ae859b7238c2c68f39a6224dbc"
EXPECTED_SEARCH_SCHEMA = "chaos-redux-advisor-native-search-v2"
EXPECTED_NORMALIZATION_SCHEMA = "chaos-redux-advisor-face-protected-background-luminance-affine-v1"
EXPECTED_MINIMUM_STYLE_MARGIN = 0.03

REFERENCE_HASHES = {
	"generic_europe_1.png": "b9f658f367325268674d079460c30e6ff38f1125d80deb2087bc50e81639cbdc",
	"generic_female_europe.png": "6c2ae2cf867a620eb0855a05adfde73550ef84528b876d4d4019ba6488c8bafb",
	"generic_asia_1.png": "0daaeee97f241e8b4bfe5ed99da44bd26fd5a60669874f55ccef6c47ed65910f",
	"army_small_ger_friedrich_paulus.png": "68bef2980360a8148cbb8e644677508887bcc23691ff76cd329fd3540a4bfcf7",
	"army_small_ger_gunther_von_kluge.png": "73c11ed580fa7b836dba0c434ff9d3648052336e0c7a41b35225cdd1277a5d9f",
	"army_small_ger_erwin_rommel.png": "46d8a65f55d98aba8fcecf68e738a98c47bfb1d5ad31d9ed37a4e832b8556cd9",
}

STYLE_ROIS = {
	"top_frame": (0, 0, 43, 12),
	"left_rail": (0, 0, 10, 59),
	"portrait": (7, 7, 36, 54),
	"bottom_area": (0, 50, 46, 65),
	"paper_zone": (26, 20, 65, 63),
}
STYLE_BANDS = {
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

# Identifiers and ImageGen handles are immutable.  The approved crop/face boxes
# are loaded from the required portrait manifest so a reviewed recrop updates a
# single source of truth rather than silently diverging from the processor.
ADVISORS = {
	"advisor_utopia_manifesto_advocate_of_limits": "exec-5719ffab-e9e6-4438-bb4d-3d83e10db5e5",
	"advisor_utopia_manifesto_chief_surveyor": "exec-729994e1-13a2-45a9-bcc4-975363fe8109",
	"advisor_utopia_manifesto_civic_engineer": "exec-bf4c97ae-06d8-4094-ace4-83c890a045fd",
	"advisor_utopia_manifesto_constitutional_jurist": "exec-2bd33604-a9fc-4ac3-a386-521f0d9d094f",
	"advisor_utopia_manifesto_contract_broker": "exec-c2d49770-163f-4430-ace5-6c9d3e3af528",
	"advisor_utopia_manifesto_council_organizer": "exec-72e6c3bc-46b9-4ea5-a67c-2ec02439dfa8",
	"advisor_utopia_manifesto_general_provisioner": "exec-6b0c1b48-d330-4144-91d1-dc367319e57d",
	"advisor_utopia_manifesto_interpreter": "exec-318c2c63-58d6-4a2f-9cb5-718ef18c6de1",
	"advisor_utopia_manifesto_keeper_of_stores": "exec-e5a3b596-fc22-4135-b3c0-589b6db39a11",
	"advisor_utopia_manifesto_league_envoy": "exec-b18eea3a-aed0-4c2e-8e50-794b2782a512",
	"advisor_utopia_manifesto_public_auditor": "exec-e6aa840a-ac49-4724-ae1b-f3acd81c166b",
	"advisor_utopia_manifesto_secretary_of_callings": "exec-f3e680fa-37a2-4b9d-970e-beee317232b7",
	"advisor_utopia_manifesto_social_workshop_planner": "exec-1cf9ae16-4a2d-46e8-b38e-afe3c91d937d",
	"advisor_utopia_manifesto_standards_engineer": "exec-169da878-4be4-400c-9a78-dd454aea8550",
	"advisor_utopia_manifesto_steward_of_service": "exec-cd7f2d8e-156c-4b28-8128-6afd643dbed9",
	"advisor_utopia_manifesto_surveyor_of_shores": "exec-3fc3983f-f015-4b6e-a927-2eef3849e010",
}


def rel(path: Path) -> str:
	return path.resolve().relative_to(REPO.resolve()).as_posix()


def sha256(path: Path) -> str:
	digest = hashlib.sha256()
	with path.open("rb") as handle:
		for chunk in iter(lambda: handle.read(1024 * 1024), b""):
			digest.update(chunk)
	return digest.hexdigest()


def canonical_json_sha256(payload: object) -> str:
	encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
	return hashlib.sha256(encoded).hexdigest()


def decoded_rgba_sha256(image: Image.Image) -> str:
	rgba = image.convert("RGBA")
	digest = hashlib.sha256()
	digest.update(b"chaos-redux-decoded-rgba-v1\0")
	digest.update(rgba.width.to_bytes(4, "little"))
	digest.update(rgba.height.to_bytes(4, "little"))
	digest.update(rgba.tobytes())
	return digest.hexdigest()


def require_hash(path: Path, expected: str) -> None:
	if not path.is_file():
		raise FileNotFoundError(path)
	actual = sha256(path)
	if actual != expected:
		raise ValueError(f"hash differs for {rel(path)}: expected {expected}, got {actual}")


def require(condition: bool, message: str) -> None:
	if not condition:
		raise ValueError(message)


def same_image(left: Image.Image, right: Image.Image) -> bool:
	if left.size != right.size:
		return False
	return left.convert("RGBA").tobytes() == right.convert("RGBA").tobytes()


def atomic_json(path: Path, payload: object) -> None:
	data = (json.dumps(payload, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
	atomic_bytes(path, data)


def atomic_bytes(path: Path, data: bytes) -> None:
	path.parent.mkdir(parents=True, exist_ok=True)
	fd, temporary_name = tempfile.mkstemp(dir=str(path.parent), prefix=f".{path.name}.", suffix=".tmp")
	temporary = Path(temporary_name)
	try:
		with os.fdopen(fd, "wb") as handle:
			handle.write(data)
		os.replace(temporary, path)
	finally:
		if temporary.exists():
			temporary.unlink()


def atomic_image(path: Path, image: Image.Image) -> None:
	path.parent.mkdir(parents=True, exist_ok=True)
	fd, temporary_name = tempfile.mkstemp(dir=str(path.parent), prefix=f".{path.name}.", suffix=".png")
	os.close(fd)
	temporary = Path(temporary_name)
	try:
		image.save(temporary, format="PNG", optimize=False, compress_level=9)
		os.replace(temporary, path)
	finally:
		if temporary.exists():
			temporary.unlink()


def run(command: list[str]) -> None:
	result = subprocess.run(command, cwd=str(REPO), text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if result.returncode:
		raise RuntimeError(
			"subprocess failed:\n" + subprocess.list2cmdline(command) +
			"\nstdout:\n" + result.stdout + "\nstderr:\n" + result.stderr
		)


_FROZEN_PROCESSOR = None


def frozen_processor():
	"""Load the hash-pinned processor for independent one-candidate reconstruction."""
	global _FROZEN_PROCESSOR
	if _FROZEN_PROCESSOR is not None:
		return _FROZEN_PROCESSOR
	spec = importlib.util.spec_from_file_location(
		"chaos_redux_frozen_advisor_processor_v5",
		PROCESSOR,
	)
	if spec is None or spec.loader is None:
		raise RuntimeError("could not load the frozen advisor processor")
	sys.dont_write_bytecode = True
	module = importlib.util.module_from_spec(spec)
	sys.modules[spec.name] = module
	spec.loader.exec_module(module)
	_FROZEN_PROCESSOR = module
	return module


def independently_reconstruct_candidate(
	stem: str,
	spec: dict[str, object],
	metadata: dict[str, object],
	candidate: Image.Image,
) -> dict[str, object]:
	"""Rebuild the selected candidate once, without trusting support metadata.

	This follows the frozen processor's production layer order with the selected
	portrait/paper parameters.  It deliberately does not rerun the search lattice;
	it proves that the declared selection reconstructs the exact candidate pixels
	and that the reconstructed authored/shadow/backing support has no exposed RGB.
	"""
	p = frozen_processor()
	p.verify_advisor_runtime()
	require(
		p.advisor_render_configuration().get("sha256")
		== EXPECTED_RENDER_CONFIGURATION_SHA256,
		f"independent render configuration differs for {stem}",
	)
	source_path = Path(str(spec["source_path"]))
	crop = tuple(int(value) for value in spec["approved_crop"])
	face_box = tuple(int(value) for value in spec["approved_face_box"])
	with Image.open(source_path) as opened:
		source = opened.convert("RGBA")
	source_crop = source.crop(crop)
	frame_overlay, _ = p.load_generated_layer(
		FRAME_OVERLAY,
		FRAME_SOURCE,
		"frame",
	)
	paper_overlay, _ = p.load_generated_layer(
		PAPER_OVERLAY,
		PAPER_SOURCE,
		"paper",
	)
	frame, _ = p.normalize_generated_layer(
		frame_overlay,
		p.ADVISOR_FRAME_SIZE,
		p.ADVISOR_FRAME_POSITION,
		p.ADVISOR_FRAME_ANGLE,
	)
	frame = p.grade_advisor_frame(frame)
	raw_frame_alpha = frame.getchannel("A")
	window_mask, window_bbox, _ = p.enclosed_alpha_window(frame)
	frame_alpha = p.advisor_frame_composition_alpha(raw_frame_alpha)
	frame.putalpha(frame_alpha)
	paper_base, _ = p.normalize_generated_layer(
		paper_overlay,
		p.ADVISOR_PAPER_SIZE,
		p.ADVISOR_PAPER_POSITION,
		p.ADVISOR_PAPER_ANGLE,
	)
	paper_base = p.grade_advisor_paper(paper_base)
	paper_alpha = p.advisor_paper_composition_alpha(paper_base.getchannel("A"))
	paper_base.putalpha(paper_alpha)
	(
		portrait_source_native,
		portrait_base,
		mapped_face,
		_,
	) = p.fit_advisor_portrait(
		source_crop,
		str(spec["source_kind"]),
		str(metadata.get("determinism", {}).get("payload_sha256", "")),
		crop,
		face_box,
		window_bbox,
	)
	face_placement = p.validate_face_placement(mapped_face, window_bbox, paper_base)
	face_local_box = p.advisor_face_local_box(
		mapped_face,
		window_bbox,
		portrait_base,
	)
	native_search = metadata.get("advisor_composition", {}).get("native_search", {})
	portrait_parameters = native_search.get("chosen_portrait_parameters", {})
	baseline, portrait, background_identity, background_processing = p.grade_advisor_portrait_candidate(
		portrait_base,
		float(portrait_parameters["gamma"]),
		float(portrait_parameters["background_target_mean"]),
		float(portrait_parameters["background_target_std"]),
		(
			str(portrait_parameters["background_smoothing_mode"]),
			float(portrait_parameters["background_smoothing_strength"]),
		),
		face_local_box,
	)
	require(
		p.advisor_background_identity_passes(background_identity),
		f"independent background identity gate failed for {stem}",
	)
	face_identity = p.advisor_region_identity_metrics(
		baseline,
		portrait,
		face_local_box,
	)
	require(
		p.advisor_face_identity_passes(face_identity),
		f"independent face identity gate failed for {stem}",
	)
	source_face_identity = p.advisor_region_identity_metrics(
		portrait_source_native,
		portrait,
		face_local_box,
	)
	require(
		p.advisor_source_face_identity_passes(source_face_identity),
		f"independent source-face identity gate failed for {stem}",
	)
	portrait_layer = p.advisor_portrait_layer(
		portrait,
		window_bbox,
		window_mask,
	)
	paper_parameters = native_search.get("chosen_paper_parameters", {})
	paper, paper_identity = p.grade_advisor_paper_candidate(
		paper_base,
		float(paper_parameters["target_mean"]),
		float(paper_parameters["target_std"]),
	)
	paper.putalpha(paper_alpha)
	require(
		p.advisor_paper_identity_passes(paper_identity),
		f"independent paper identity gate failed for {stem}",
	)
	p.validate_advisor_paper_palette(paper)
	face_palette = p.advisor_face_palette_metrics(
		portrait,
		mapped_face,
		window_bbox,
	)
	composition = metadata.get("advisor_composition", {})
	require(
		face_placement == composition.get("face_placement"),
		f"independent face-placement evidence differs for {stem}",
	)
	require(
		face_palette == composition.get("face_palette"),
		f"independent face-palette evidence differs for {stem}",
	)
	require(
		background_processing == composition.get("background_processing")
		and background_processing
		== native_search.get("chosen_background_processing"),
		f"independent background-processing evidence differs for {stem}",
	)
	require(
		background_identity == composition.get("background_identity")
		and background_identity == native_search.get("chosen_background_identity"),
		f"independent background-identity evidence differs for {stem}",
	)
	require(
		face_identity == composition.get("face_identity"),
		f"independent face-identity evidence differs for {stem}",
	)
	require(
		source_face_identity == composition.get("source_face_identity"),
		f"independent source-face evidence differs for {stem}",
	)
	require(
		paper_identity == composition.get("paper_identity"),
		f"independent paper-identity evidence differs for {stem}",
	)
	require(
		decoded_rgba_sha256(portrait)
		== native_search.get("chosen_portrait_layer_sha256"),
		f"independent portrait-layer hash differs for {stem}",
	)
	require(
		decoded_rgba_sha256(paper)
		== native_search.get("chosen_paper_layer_sha256"),
		f"independent paper-layer hash differs for {stem}",
	)
	canonical_alpha, _ = p.canonical_advisor_alpha_envelope(REFERENCE_DIR)
	reconstructed, support = p.compose_advisor_candidate(
		frame,
		frame_alpha,
		window_mask,
		portrait_layer,
		paper,
		paper_alpha,
		canonical_alpha,
		True,
	)
	require(
		same_image(candidate, reconstructed),
		f"independent source/overlay reconstruction differs from candidate for {stem}",
	)
	require(
		support == native_search.get("chosen_rgb_support"),
		f"independent RGB-support proof differs from metadata for {stem}",
	)
	return {
		"exact_rgba_reconstruction": True,
		"decoded_rgba_sha256": decoded_rgba_sha256(reconstructed),
		"rgb_support": support,
		"background_identity_passed": True,
		"face_identity_passed": True,
		"source_face_identity_passed": True,
		"paper_identity_passed": True,
		"stored_identity_and_layer_evidence_matches": True,
	}


def load_portrait_manifest() -> tuple[dict[str, dict[str, object]], str]:
	if not PORTRAIT_MANIFEST.is_file():
		raise FileNotFoundError(PORTRAIT_MANIFEST)
	manifest = json.loads(PORTRAIT_MANIFEST.read_text(encoding="utf-8"))
	require(manifest.get("schema_version") == 1, "portrait provenance manifest must use schema 1")
	prompt = REPO / str(manifest.get("prompt_record", ""))
	require_hash(prompt, str(manifest.get("prompt_sha256", "")))
	inputs = manifest.get("generation_inputs")
	require(isinstance(inputs, list) and bool(inputs), "portrait manifest generation inputs are missing")
	for item in inputs:
		require_hash(REPO / str(item.get("path", "")), str(item.get("sha256", "")))
	assets = manifest.get("assets")
	require(isinstance(assets, list) and len(assets) == len(ADVISORS), "portrait manifest must contain exactly 16 assets")
	records: dict[str, dict[str, object]] = {}
	for entry in assets:
		require(entry.get("role") == "advisor_portrait_master", "portrait manifest contains a non-advisor role")
		require(entry.get("status") == "approved_for_processing", "portrait source is not approved for processing")
		require(entry.get("source_kind") == "fictional", "Event 015 advisor source kind differs")
		require(entry.get("exact_source_byte_copy") is True, "portrait exact-source assertion is missing")
		generation_mode = entry.get("generation_mode", manifest.get("generation_mode"))
		require(generation_mode in {"text_to_image", "image_edit", "archival_source"}, "portrait generation mode is unsupported")
		entry_inputs = entry.get("generation_inputs", inputs)
		require(isinstance(entry_inputs, list) and bool(entry_inputs), "portrait generation inputs are missing")
		for item in entry_inputs:
			require(isinstance(item, dict), "portrait generation input is malformed")
			require_hash(REPO / str(item.get("path", "")), str(item.get("sha256", "")))
		source = REPO / str(entry.get("source", ""))
		stem = source.name.removesuffix("_source.png")
		require(stem in ADVISORS and stem not in records, f"unexpected/duplicate portrait manifest source: {source}")
		require(entry.get("imagegen_handle") == ADVISORS[stem], f"ImageGen handle differs for {stem}")
		require_hash(source, str(entry.get("source_sha256", "")))
		with Image.open(source) as opened:
			require(list(opened.size) == entry.get("source_dimensions"), f"source dimensions differ for {stem}")
		crop = entry.get("approved_crop")
		face_box = entry.get("approved_face_box")
		require(isinstance(crop, list) and len(crop) == 4, f"approved crop missing for {stem}")
		require(isinstance(face_box, list) and len(face_box) == 4, f"approved face box missing for {stem}")
		require(crop[0] <= face_box[0] < face_box[2] <= crop[2] and crop[1] <= face_box[1] < face_box[3] <= crop[3], f"face box is outside crop for {stem}")
		matches = list(GENERATED.rglob(f"{ADVISORS[stem]}.png"))
		require(len(matches) == 1, f"expected one built-in ImageGen object for {stem}, found {len(matches)}")
		require(source.read_bytes() == matches[0].read_bytes(), f"source is not exact built-in ImageGen output for {stem}")
		records[stem] = {**entry, "source_path": source, "built_in_store_object": matches[0].relative_to(GENERATED).as_posix()}
	require(set(records) == set(ADVISORS), "portrait manifest identifier coverage differs")
	return records, sha256(PORTRAIT_MANIFEST)


def validate_overlay_package() -> dict[str, object]:
	require_hash(OVERLAY_MANIFEST, EXPECTED_OVERLAY_MANIFEST_SHA256)
	require_hash(FRAME_SOURCE, EXPECTED_FRAME_SOURCE_SHA256)
	require_hash(FRAME_OVERLAY, EXPECTED_FRAME_OVERLAY_SHA256)
	require_hash(PAPER_SOURCE, EXPECTED_PAPER_SOURCE_SHA256)
	require_hash(PAPER_OVERLAY, EXPECTED_PAPER_OVERLAY_SHA256)
	manifest = json.loads(OVERLAY_MANIFEST.read_text(encoding="utf-8"))
	require(manifest.get("schema_version") == 4, "overlay manifest must use schema 4")
	require(set(manifest.get("final_roles", [])) == {"advisor_frame_shadowless", "advisor_paper_shadowless"}, "overlay final roles differ")
	declared_references = manifest.get("canonical_style_references", {}).get("files", [])
	require({item.get("name"): item.get("sha256") for item in declared_references} == REFERENCE_HASHES, "overlay manifest reference set differs")
	selected: dict[str, dict[str, object]] = {}
	for entry in manifest.get("assets", []):
		role = str(entry.get("role", ""))
		if role not in {"advisor_frame_shadowless", "advisor_paper_shadowless"}:
			continue
		require(entry.get("status") == "approved_for_processing", f"overlay {role} is not approved for processing")
		require(entry.get("exact_source_byte_copy") is True, f"overlay {role} lacks exact-source assertion")
		source = REPO / str(entry.get("source", ""))
		overlay = REPO / str(entry.get("processed", ""))
		require_hash(source, str(entry.get("source_sha256", "")))
		require_hash(overlay, str(entry.get("processed_sha256", "")))
		prompt = REPO / str(entry.get("prompt_record", ""))
		require_hash(prompt, str(entry.get("prompt_sha256", "")))
		for generation_input in entry.get("generation_inputs", []):
			require_hash(REPO / str(generation_input.get("path", "")), str(generation_input.get("sha256", "")))
		selected[role] = entry
	require(len(selected) == 2, "overlay manifest must select exactly frame and paper")
	return selected


def derive_references() -> dict[str, object]:
	references: list[Image.Image] = []
	alpha_layers: list[list[int]] = []
	for name, expected_hash in REFERENCE_HASHES.items():
		path = REFERENCE_DIR / name
		require_hash(path, expected_hash)
		with Image.open(path) as opened:
			reference = opened.convert("RGBA")
		require(reference.size == (65, 67), f"canonical reference dimensions differ: {name}")
		references.append(reference)
		alpha_layers.append(list(reference.getchannel("A").getdata()))
	mean_alpha = bytes(round(sum(values) / len(values)) for values in zip(*alpha_layers))
	require(hashlib.sha256(mean_alpha).hexdigest() == EXPECTED_ALPHA_SHA256, "six-reference alpha derivation differs")
	per_reference = []
	for name, reference in zip(REFERENCE_HASHES, references):
		eligible = set()
		for y in range(67):
			for x in range(65):
				red, green, blue, alpha = reference.getpixel((x, y))
				if alpha > 192 and red > 150 and green > 120 and blue > 80 and red >= green >= blue:
					eligible.add((x, y))
		components = []
		while eligible:
			start = min(eligible)
			component = {start}
			stack = [start]
			eligible.remove(start)
			while stack:
				x, y = stack.pop()
				for point in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
					if point in eligible:
						eligible.remove(point)
						component.add(point)
						stack.append(point)
			components.append(component)
		require(bool(components), f"no canonical paper component in {name}")
		component = max(components, key=lambda points: (len(points), -min(points)[0], -min(points)[1]))
		geometry = geometry_metrics(sorted(component))
		luminance = []
		saturation = []
		for point in component:
			red, green, blue, _ = reference.getpixel(point)
			luminance.append(0.2126 * red + 0.7152 * green + 0.0722 * blue)
			maximum = max(red, green, blue)
			saturation.append(0.0 if maximum == 0 else (maximum - min(red, green, blue)) / maximum)
		per_reference.append({
			"name": name,
			"decoded_rgba_sha256": decoded_rgba_sha256(reference),
			**geometry,
			"coverage_gt_32": round(len(component) / (65 * 67), 6),
			"mean_luminance": round(sum(luminance) / len(luminance), 6),
			"mean_saturation": round(sum(saturation) / len(saturation), 6),
		})
	for key in ("bbox_gt_32", "width", "height"):
		require(all(item[key] == per_reference[0][key] for item in per_reference), f"canonical paper {key} differs")
	def mean(key: str) -> float:
		return round(sum(float(item[key]) for item in per_reference) / len(per_reference), 6)
	aggregate = {
		"bbox_gt_32": list(per_reference[0]["bbox_gt_32"]),
		"width": int(per_reference[0]["width"]),
		"height": int(per_reference[0]["height"]),
		"area_gt_32": mean("area_gt_32"),
		"coverage_gt_32": mean("coverage_gt_32"),
		"center": [round(sum(float(item["center"][axis]) for item in per_reference) / 6, 6) for axis in range(2)],
		"top_edge_image_slope": mean("top_edge_image_slope"),
		"top_edge_image_angle_degrees": mean("top_edge_image_angle_degrees"),
		"mean_luminance": mean("mean_luminance"),
		"mean_saturation": mean("mean_saturation"),
	}
	require(canonical_json_sha256(aggregate) == EXPECTED_PAPER_FAMILY_SHA256, "six-reference paper derivation differs")
	return {"alpha_bytes": mean_alpha, "paper": aggregate, "paper_references": per_reference}


def geometry_metrics(points: list[tuple[int, int]]) -> dict[str, object]:
	x_values = [x for x, _ in points]
	y_values = [y for _, y in points]
	bbox = (min(x_values), min(y_values), max(x_values) + 1, max(y_values) + 1)
	point_set = set(points)
	top_edge = []
	for x in range(bbox[0], bbox[2]):
		column = [y for y in range(bbox[1], bbox[3]) if (x, y) in point_set]
		if len(column) >= 3:
			top_edge.append((x, min(column)))
	left_skip = max(2, len(top_edge) // 5)
	fit_edge = top_edge[left_skip:-1]
	mean_x = sum(x for x, _ in fit_edge) / len(fit_edge)
	mean_y = sum(y for _, y in fit_edge) / len(fit_edge)
	denominator = sum((x - mean_x) ** 2 for x, _ in fit_edge)
	slope = sum((x - mean_x) * (y - mean_y) for x, y in fit_edge) / denominator
	return {
		"bbox_gt_32": list(bbox), "width": bbox[2] - bbox[0], "height": bbox[3] - bbox[1],
		"area_gt_32": len(points),
		"center": [round(sum(x_values) / len(points), 6), round(sum(y_values) / len(points), 6)],
		"top_edge_image_slope": round(slope, 6),
		"top_edge_image_angle_degrees": round(math.degrees(math.atan(slope)), 6),
	}


def roi_metrics(image: Image.Image, box: tuple[int, int, int, int]) -> dict[str, object]:
	values = []
	variation = 0.0
	pairs = 0
	for y in range(box[1], box[3]):
		for x in range(box[0], box[2]):
			pixel = image.getpixel((x, y))
			lum = 0.2126 * pixel[0] + 0.7152 * pixel[1] + 0.0722 * pixel[2]
			if pixel[3] > 64:
				values.append(lum)
			for nx, ny in ((x + 1, y), (x, y + 1)):
				if nx < box[2] and ny < box[3]:
					other = image.getpixel((nx, ny))
					if pixel[3] > 64 and other[3] > 64:
						variation += abs(lum - (0.2126 * other[0] + 0.7152 * other[1] + 0.0722 * other[2]))
						pairs += 1
	mean = sum(values) / len(values)
	return {"mean": mean, "std": math.sqrt(sum((value - mean) ** 2 for value in values) / len(values)), "variation": variation / pairs, "samples": len(values)}


def style_values(image: Image.Image) -> tuple[dict[str, object], dict[str, float]]:
	rgba = image.convert("RGBA")
	metrics = {name: roi_metrics(rgba, STYLE_ROIS[name]) for name in ("top_frame", "left_rail", "portrait", "bottom_area")}
	paper_values = []
	for y in range(STYLE_ROIS["paper_zone"][1], STYLE_ROIS["paper_zone"][3]):
		for x in range(STYLE_ROIS["paper_zone"][0], STYLE_ROIS["paper_zone"][2]):
			red, green, blue, alpha = rgba.getpixel((x, y))
			luminance = 0.2126 * red + 0.7152 * green + 0.0722 * blue
			if alpha > 192 and luminance > 105 and max(red, green, blue) - min(red, green, blue) < 105 and red >= blue * 0.88 and green >= blue * 0.78:
				paper_values.append(luminance)
	mean = sum(paper_values) / len(paper_values)
	metrics["paper"] = {"mean": mean, "std": math.sqrt(sum((value - mean) ** 2 for value in paper_values) / len(paper_values)), "samples": len(paper_values)}
	values = {
		"top_frame_variation": float(metrics["top_frame"]["variation"]),
		"left_rail_variation": float(metrics["left_rail"]["variation"]),
		"left_rail_mean": float(metrics["left_rail"]["mean"]),
		"left_rail_std": float(metrics["left_rail"]["std"]),
		"paper_mean": float(metrics["paper"]["mean"]),
		"paper_std": float(metrics["paper"]["std"]),
		"paper_samples": float(metrics["paper"]["samples"]),
		"portrait_mean": float(metrics["portrait"]["mean"]),
		"bottom_area_variation": float(metrics["bottom_area"]["variation"]),
	}
	return metrics, values


def validate_style(image: Image.Image, metadata: dict[str, object], stem: str) -> None:
	metrics, values = style_values(image)
	validation = metadata["advisor_validation"]["native_style_validation"]
	require(validation.get("bands") == {key: list(value) for key, value in STYLE_BANDS.items()}, f"nine style bands differ for {stem}")
	require(set(values) == set(STYLE_BANDS) and len(values) == 9, f"style-band coverage differs for {stem}")
	for key, value in values.items():
		lower, upper = STYLE_BANDS[key]
		margin = min((value - lower) / (upper - lower), (upper - value) / (upper - lower))
		require(margin >= EXPECTED_MINIMUM_STYLE_MARGIN - 1e-9, f"style band {key} failed for {stem}: {value}")
	declared_metrics = validation.get("metrics", {})
	for family, family_metrics in metrics.items():
		for key, value in family_metrics.items():
			expected = round(value, 6) if isinstance(value, float) else value
			require(declared_metrics.get(family, {}).get(key) == expected, f"style metric {family}.{key} differs for {stem}")


def validate_dds(path: Path) -> tuple[dict[str, object], Image.Image]:
	data = path.read_bytes()
	require(len(data) == 17548 and data[:4] == b"DDS ", f"DDS size/magic differs: {rel(path)}")
	read = lambda offset: int.from_bytes(data[offset:offset + 4], "little")
	require(read(4) == 124 and read(8) == 0x100F, f"DDS header/flags differ: {rel(path)}")
	require((read(16), read(12), read(20), read(24), read(28)) == (65, 67, 260, 0, 0), f"DDS dimensions/pitch/depth/mips differ: {rel(path)}")
	require(all(read(offset) == 0 for offset in range(32, 76, 4)), f"DDS reserved fields differ: {rel(path)}")
	require((read(76), read(80), read(84), read(88)) == (32, 0x41, 0, 32), f"DDS pixel format differs: {rel(path)}")
	require(tuple(read(offset) for offset in (92, 96, 100, 104)) == (0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000), f"DDS channel masks differ: {rel(path)}")
	require((read(108), read(112), read(116), read(120), read(124)) == (0x1000, 0, 0, 0, 0), f"DDS caps differ: {rel(path)}")
	with Image.open(path) as opened:
		decoded = opened.convert("RGBA")
	require(decoded.size == (65, 67), f"DDS decoded dimensions differ: {rel(path)}")
	alpha = decoded.getchannel("A")
	return {
		"dimensions": [65, 67], "header_size": 124, "flags": 0x100F,
		"pitch_or_linear_size": 260, "mipmap_count": 0, "pixel_format_flags": 0x41,
		"four_cc": 0, "rgb_bit_count": 32,
		"channel_masks": ["0x00ff0000", "0x0000ff00", "0x000000ff", "0xff000000"],
		"caps": "0x00001000", "alpha_range": list(alpha.getextrema()),
		"corner_alpha": [alpha.getpixel(point) for point in ((0, 0), (64, 0), (0, 66), (64, 66))],
		"byte_length": len(data), "sha256": sha256(path),
	}, decoded


def expected_command(stem: str, source: Path, processed: Path, review: Path, metadata_path: Path, crop: list[int], face_box: list[int]) -> dict[str, object]:
	return {
		"mode": "advisor", "source": rel(source), "output": rel(processed), "crop": crop,
		"source_kind": "fictional", "face_box": face_box, "review_sheet": rel(review),
		"metadata": rel(metadata_path), "reference_dir": None,
		"advisor_overlay_manifest": rel(OVERLAY_MANIFEST),
		"portrait_provenance_manifest": rel(PORTRAIT_MANIFEST),
		"advisor_frame_overlay": rel(FRAME_OVERLAY), "advisor_frame_source": rel(FRAME_SOURCE),
		"advisor_paper_overlay": rel(PAPER_OVERLAY), "advisor_paper_source": rel(PAPER_SOURCE),
		"force": True,
	}


def regenerate(stem: str, spec: dict[str, object]) -> None:
	source = Path(spec["source_path"])
	processed = PROCESSED / f"{stem}.png"
	review = REVIEWS / f"{stem}_comparison.png"
	metadata_path = METADATA / f"{stem}.json"
	command = [
		sys.executable, "-B", str(PROCESSOR), "advisor", str(source), str(processed),
		"--source-kind", "fictional", "--crop", *[str(value) for value in spec["approved_crop"]],
		"--face-box", *[str(value) for value in spec["approved_face_box"]],
		"--advisor-overlay-manifest", str(OVERLAY_MANIFEST),
		"--portrait-provenance-manifest", str(PORTRAIT_MANIFEST),
		"--advisor-frame-source", str(FRAME_SOURCE), "--advisor-frame-overlay", str(FRAME_OVERLAY),
		"--advisor-paper-source", str(PAPER_SOURCE), "--advisor-paper-overlay", str(PAPER_OVERLAY),
		"--review-sheet", str(review), "--metadata", str(metadata_path), "--force",
	]
	run(command)


def validate_candidate(stem: str, spec: dict[str, object], portrait_manifest_sha: str, references: dict[str, object]) -> tuple[dict[str, object], dict[str, object]]:
	source = Path(spec["source_path"])
	processed = PROCESSED / f"{stem}.png"
	review = REVIEWS / f"{stem}_comparison.png"
	metadata_path = METADATA / f"{stem}.json"
	for path in (source, processed, review, metadata_path):
		if not path.is_file():
			raise FileNotFoundError(path)
	with Image.open(processed) as opened:
		png = opened.convert("RGBA")
	require(png.size == (65, 67), f"processed dimensions differ for {stem}")
	require(png.getchannel("A").tobytes() == references["alpha_bytes"], f"canonical alpha envelope differs for {stem}")
	metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
	integrity = metadata.get("metadata_integrity", {})
	payload = {key: value for key, value in metadata.items() if key != "metadata_integrity"}
	require(integrity.get("schema") == "canonical_json_sha256_excluding_metadata_integrity_v1" and integrity.get("payload_sha256") == canonical_json_sha256(payload), f"metadata integrity differs for {stem}")
	require(metadata.get("status") == "candidate_requires_visual_approval", f"metadata status is not candidate-only for {stem}")
	require("visual_review" not in metadata, f"metadata contains a visual-approval claim for {stem}")
	require(metadata.get("processor_version") == EXPECTED_PROCESSOR_VERSION and metadata.get("render_version") == EXPECTED_RENDER_VERSION, f"processor/render version differs for {stem}")
	require(metadata.get("processor_sha256") == EXPECTED_PROCESSOR_SHA256, f"processor hash differs in metadata for {stem}")
	require(metadata.get("runtime") == EXPECTED_RUNTIME, f"runtime differs for {stem}")
	require(metadata.get("source_sha256") == sha256(source), f"source hash differs in metadata for {stem}")
	require(metadata.get("crop") == spec["approved_crop"] and metadata.get("face_box") == spec["approved_face_box"], f"crop/face mapping differs in metadata for {stem}")
	render = metadata.get("render_configuration", {})
	require(render.get("sha256") == EXPECTED_RENDER_CONFIGURATION_SHA256 and canonical_json_sha256(render.get("values")) == EXPECTED_RENDER_CONFIGURATION_SHA256, f"render configuration differs for {stem}")
	provenance = metadata.get("portrait_provenance", {})
	require(provenance.get("sha256") == portrait_manifest_sha and Path(str(provenance.get("path"))).resolve() == PORTRAIT_MANIFEST.resolve(), f"portrait manifest provenance differs for {stem}")
	require(provenance.get("source_sha256") == sha256(source) and provenance.get("record_id") == spec["record_id"], f"portrait provenance record differs for {stem}")
	overlays = metadata.get("generated_overlays", {})
	require(overlays.get("manifest", {}).get("sha256") == EXPECTED_OVERLAY_MANIFEST_SHA256, f"overlay manifest hash differs for {stem}")
	for role, source_hash, overlay_hash in (("frame", EXPECTED_FRAME_SOURCE_SHA256, EXPECTED_FRAME_OVERLAY_SHA256), ("paper", EXPECTED_PAPER_SOURCE_SHA256, EXPECTED_PAPER_OVERLAY_SHA256)):
		require(overlays.get(role, {}).get("source_sha256") == source_hash and overlays.get(role, {}).get("overlay_sha256") == overlay_hash, f"overlay layer hash differs for {stem}/{role}")
		require(overlays.get("manifest", {}).get(role, {}).get("source_sha256") == source_hash and overlays.get("manifest", {}).get(role, {}).get("overlay_sha256") == overlay_hash, f"overlay provenance hash differs for {stem}/{role}")
	seed = metadata.get("determinism", {})
	require(seed.get("payload_sha256") == canonical_json_sha256(seed.get("payload")), f"seed hash differs for {stem}")
	require(seed.get("payload", {}).get("processor_sha256") == EXPECTED_PROCESSOR_SHA256 and seed.get("payload", {}).get("render_configuration_sha256") == EXPECTED_RENDER_CONFIGURATION_SHA256, f"seed freeze hashes differ for {stem}")
	command = metadata.get("command", {})
	expected_arguments = expected_command(stem, source, processed, review, metadata_path, spec["approved_crop"], spec["approved_face_box"])
	require(command.get("arguments") == expected_arguments and command.get("arguments_sha256") == canonical_json_sha256(expected_arguments), f"processor command differs for {stem}")
	artifacts = metadata.get("artifact_integrity", {})
	require(artifacts.get("output", {}).get("file_sha256") == sha256(processed) and artifacts.get("output", {}).get("decoded_rgba_sha256") == decoded_rgba_sha256(png), f"PNG artifact hash differs for {stem}")
	with Image.open(review) as opened:
		review_image = opened.convert("RGBA")
	require(artifacts.get("review_sheet", {}).get("file_sha256") == sha256(review) and artifacts.get("review_sheet", {}).get("decoded_rgba_sha256") == decoded_rgba_sha256(review_image), f"review artifact hash differs for {stem}")
	composition = metadata.get("advisor_composition", {})
	native_search = composition.get("native_search", {})
	require(native_search.get("schema") == EXPECTED_SEARCH_SCHEMA and native_search.get("normalization_schema") == EXPECTED_NORMALIZATION_SCHEMA, f"native-search schema differs for {stem}")
	require(native_search.get("lattice_sha256") == canonical_json_sha256(native_search.get("lattice")), f"native-search lattice hash differs for {stem}")
	require(native_search.get("candidate_status") == "candidate_requires_visual_approval", f"native-search status differs for {stem}")
	require(native_search.get("minimum_native_style_margin") == EXPECTED_MINIMUM_STYLE_MARGIN, f"native-search style margin differs for {stem}")
	chosen_style = native_search.get("chosen_native_style", {})
	require(chosen_style.get("passed") is True and chosen_style.get("failures") == {}, f"chosen native style is not a strict pass for {stem}")
	require(native_search.get("chosen_final_decoded_rgba_sha256") == decoded_rgba_sha256(png), f"chosen candidate hash differs for {stem}")
	support = native_search.get("chosen_rgb_support", {})
	for key in ("unsupported_visible_pixels", "unsupported_substantive_pixels", "unsupported_high_alpha_source_pixels"):
		require(support.get(key) == 0, f"RGB support gate {key} failed for {stem}")
	reconstruction = independently_reconstruct_candidate(
		stem,
		spec,
		metadata,
		png,
	)
	require(composition.get("canonical_alpha_envelope", {}).get("decoded_alpha_sha256") == EXPECTED_ALPHA_SHA256 and composition.get("canonical_alpha_envelope", {}).get("method") == EXPECTED_ALPHA_METHOD, f"alpha derivation metadata differs for {stem}")
	validation = metadata.get("advisor_validation", {})
	require(validation.get("canonical_paper_family", {}).get("derivation", {}).get("aggregate_sha256") == EXPECTED_PAPER_FAMILY_SHA256, f"paper derivation metadata differs for {stem}")
	for key, value in references["paper"].items():
		require(validation.get("canonical_paper_family", {}).get(key) == value, f"paper derivation value {key} differs for {stem}")
	require({Path(item["path"]).name: item["sha256"] for item in validation.get("canonical_references", [])} == REFERENCE_HASHES, f"six-reference metadata differs for {stem}")
	validate_style(png, metadata, stem)
	validation_record = {
		"identifier": stem, "status": "candidate_requires_visual_approval",
		"source": rel(source), "source_sha256": sha256(source), "crop": spec["approved_crop"], "face_box": spec["approved_face_box"],
		"processed_png": rel(processed), "processed_sha256": sha256(processed),
		"metadata": rel(metadata_path), "metadata_sha256": sha256(metadata_path), "comparison_sheet": rel(review), "comparison_sha256": sha256(review),
		"processor_sha256": EXPECTED_PROCESSOR_SHA256, "render_configuration_sha256": EXPECTED_RENDER_CONFIGURATION_SHA256,
		"portrait_manifest_sha256": portrait_manifest_sha, "overlay_manifest_sha256": EXPECTED_OVERLAY_MANIFEST_SHA256,
		"independent_reconstruction": reconstruction,
		"dds_state": "not_converted_pending_independent_visual_approval",
	}
	asset_record = {
		"kind": "advisor_portrait", "identifier": stem, "status": "needs_user_review",
		"source": rel(source), "source_dimensions": spec["source_dimensions"], "source_sha256": sha256(source),
		"imagegen_handle": spec["imagegen_handle"], "built_in_store_object": spec["built_in_store_object"], "source_exact_built_in_output": True,
		"source_kind": "fictional", "crop": spec["approved_crop"], "face_box": spec["approved_face_box"],
		"portrait_provenance_manifest": rel(PORTRAIT_MANIFEST), "portrait_provenance_manifest_sha256": portrait_manifest_sha,
		"processor": rel(PROCESSOR), "processor_version": EXPECTED_PROCESSOR_VERSION, "render_version": EXPECTED_RENDER_VERSION,
		"processor_sha256": EXPECTED_PROCESSOR_SHA256, "render_configuration_sha256": EXPECTED_RENDER_CONFIGURATION_SHA256,
		"converter": rel(CONVERTER), "converter_sha256": EXPECTED_CONVERTER_SHA256,
		"overlay_manifest": rel(OVERLAY_MANIFEST), "overlay_manifest_sha256": EXPECTED_OVERLAY_MANIFEST_SHA256,
		"processed": rel(processed), "processed_dimensions": [65, 67], "processed_sha256": sha256(processed),
		"review_sheet": rel(review), "metadata": rel(metadata_path),
		"validation": {"metadata_status": "candidate_requires_visual_approval", "nine_native_style_bands": True, "independent_exact_rgba_reconstruction": True, "independent_rgb_support_gate": True, "six_reference_alpha_and_paper_derivation": True, "visual_approval_record_present": False, "dds_state": "not_converted_pending_independent_visual_approval"},
		"notes": "Automated v5 candidate validation only; native and 4x contact sheets require independent visual review before DDS use can be approved.",
	}
	return validation_record, asset_record


def load_approval_records(paths: list[Path]) -> dict[str, dict[str, object]]:
	"""Read independent evidence without creating, editing, or normalising it."""
	require(len(paths) == 1, "installed validation requires one complete approval package")
	records: dict[str, dict[str, object]] = {}
	for requested in paths:
		path = requested if requested.is_absolute() else REPO / requested
		path = path.resolve()
		if not path.is_file():
			raise FileNotFoundError(path)
		payload = json.loads(path.read_text(encoding="utf-8"))
		require(isinstance(payload, dict), f"approval package is not an object: {path}")
		require(payload.get("schema_version") == 1, f"approval schema differs: {path}")
		require(
			payload.get("record_type")
			== "chaos_redux_advisor_v5_independent_visual_approval",
			f"approval record type differs: {path}",
		)
		package = payload.get("package")
		require(isinstance(package, dict), f"approval package pins are missing: {path}")
		package_pins = {
			"event_id": "015",
			"asset_family": "advisor_v5",
			"candidate_state_at_review": "candidate_requires_visual_approval",
			"approval_decision": "approved",
			"approved_asset_count": len(ADVISORS),
			"processor": rel(PROCESSOR),
			"processor_sha256": EXPECTED_PROCESSOR_SHA256,
			"render_configuration_sha256": EXPECTED_RENDER_CONFIGURATION_SHA256,
			"portrait_provenance_manifest": rel(PORTRAIT_MANIFEST),
			"portrait_provenance_manifest_sha256": sha256(PORTRAIT_MANIFEST),
			"overlay_manifest": rel(OVERLAY_MANIFEST),
			"overlay_manifest_sha256": EXPECTED_OVERLAY_MANIFEST_SHA256,
			"candidate_validation_report": rel(VALIDATION_PATH),
			"candidate_validation_report_sha256": sha256(VALIDATION_PATH),
			"candidate_checksum_manifest": rel(CHECKSUMS_PATH),
			"candidate_checksum_manifest_sha256": sha256(CHECKSUMS_PATH),
		}
		for key, expected in package_pins.items():
			require(package.get(key) == expected, f"approval package pin differs: {key}")
		producer = str(package.get("producer_identity", "")).strip()
		reviewer = str(package.get("reviewer_identity", "")).strip()
		review_date = str(package.get("review_date", "")).strip()
		require(
			bool(producer)
			and bool(reviewer)
			and producer.casefold() != reviewer.casefold(),
			"approval package producer/reviewer separation failed",
		)
		require(bool(review_date), "approval package review date is missing")
		require(
			bool(str(package.get("visual_review_summary", "")).strip()),
			"approval package visual-review summary is missing",
		)
		expected_review_evidence = {
			"native_contact_sheet": {
				"path": rel(CONTACT / "advisor_portraits_native_contact_sheet.png"),
				"sha256": sha256(CONTACT / "advisor_portraits_native_contact_sheet.png"),
			},
			"four_x_nearest_contact_sheet": {
				"path": rel(CONTACT / "advisor_portraits_enlarged_nearest_contact_sheet.png"),
				"sha256": sha256(CONTACT / "advisor_portraits_enlarged_nearest_contact_sheet.png"),
			},
			"source_crop_contact_sheet": {
				"path": rel(CONTACT / "advisor_sources_contact_sheet.png"),
				"sha256": sha256(CONTACT / "advisor_sources_contact_sheet.png"),
			},
			"canonical_advisor_contact_sheet": {
				"path": rel(REFERENCE_DIR / "contact_sheet.png"),
				"sha256": sha256(REFERENCE_DIR / "contact_sheet.png"),
			},
		}
		require(
			package.get("aggregate_review_evidence") == expected_review_evidence,
			"approval aggregate review evidence differs",
		)
		expected_references = [
			{"name": name, "sha256": digest}
			for name, digest in REFERENCE_HASHES.items()
		]
		require(
			package.get("canonical_six_reference_set") == expected_references,
			"approval canonical reference pins differ",
		)
		entries = payload.get("assets")
		require(
			isinstance(entries, list) and len(entries) == len(ADVISORS),
			f"approval package must contain exactly {len(ADVISORS)} assets: {path}",
		)
		identifiers = [
			str(entry.get("identifier", "")) if isinstance(entry, dict) else ""
			for entry in entries
		]
		require(
			len(set(identifiers)) == len(ADVISORS)
			and set(identifiers) == set(ADVISORS),
			"approval package must contain every advisor exactly once",
		)
		for entry in entries:
			require(isinstance(entry, dict), f"approval entry is malformed: {path}")
			stem = str(entry.get("identifier", entry.get("stem", "")))
			require(stem in ADVISORS and stem not in records, f"approval identifier is unexpected/duplicate: {stem}")
			require(
				str(field(entry, "producer_identity", "producer") or "").strip()
				== producer,
				f"approval producer differs from package for {stem}",
			)
			require(
				str(field(entry, "reviewer_identity", "reviewer") or "").strip()
				== reviewer,
				f"approval reviewer differs from package for {stem}",
			)
			require(
				str(field(entry, "review_date", "date") or "").strip()
				== review_date,
				f"approval date differs from package for {stem}",
			)
			require(
				str(field(entry, "approval_decision", "decision", "verdict") or "").lower()
				== "approved",
				f"approval decision differs from package for {stem}",
			)
			entry = dict(entry)
			entry["record_path"] = path
			records[stem] = entry
	return records


def field(record: dict[str, object], *names: str) -> object:
	for name in names:
		if name in record:
			return record[name]
	return None


def require_approval(stem: str, record: dict[str, object]) -> None:
	processed = PROCESSED / f"{stem}.png"
	review = REVIEWS / f"{stem}_comparison.png"
	candidate_path = Path(str(field(record, "candidate_png", "processed_png", "candidate")))
	review_path = Path(str(field(record, "review_sheet", "comparison_sheet")))
	if not candidate_path.is_absolute():
		candidate_path = REPO / candidate_path
	if not review_path.is_absolute():
		review_path = REPO / review_path
	require(candidate_path.resolve() == processed.resolve(), f"approval candidate path differs for {stem}")
	require(review_path.resolve() == review.resolve(), f"approval review path differs for {stem}")
	require(field(record, "candidate_sha256", "processed_sha256") == sha256(processed), f"approval candidate hash differs for {stem}")
	require(field(record, "review_sheet_sha256", "comparison_sha256") == sha256(review), f"approval review hash differs for {stem}")
	producer = str(field(record, "producer_identity", "producer") or "").strip()
	reviewer = str(field(record, "reviewer_identity", "reviewer") or "").strip()
	require(
		bool(producer)
		and bool(reviewer)
		and producer.casefold() != reviewer.casefold(),
		f"approval producer/reviewer separation failed for {stem}",
	)
	require(bool(str(field(record, "review_date", "date") or "").strip()), f"approval review date is missing for {stem}")
	require(bool(str(field(record, "review_notes", "notes") or "").strip()), f"approval notes are missing for {stem}")
	passing = {"pass", "passed", "approve", "approved"}
	native = str(field(record, "native_size_verdict", "native_verdict") or "").lower()
	enlarged = str(field(record, "four_x_all_six_reference_verdict", "four_x_verdict", "nearest_neighbour_verdict") or "").lower()
	decision = str(field(record, "approval_decision", "decision", "verdict") or "").lower()
	require(native in passing and enlarged in passing and decision in {"approve", "approved"}, f"independent approval verdict is not affirmative for {stem}")


def validate_installed(stem: str, approval: dict[str, object]) -> dict[str, object]:
	"""Read-only proof for DDS files installed outside this candidate tool."""
	require_approval(stem, approval)
	processed = PROCESSED / f"{stem}.png"
	package = FINAL / f"{stem}.dds"
	runtime = RUNTIME / f"{stem}.dds"
	decoded_path = DECODED / f"{stem}.png"
	for path in (package, runtime, decoded_path):
		if not path.is_file():
			raise FileNotFoundError(path)
	with Image.open(processed) as opened:
		candidate = opened.convert("RGBA")
	package_record, package_image = validate_dds(package)
	runtime_record, runtime_image = validate_dds(runtime)
	require(package.read_bytes() == runtime.read_bytes(), f"package/runtime DDS bytes differ for {stem}")
	require(same_image(candidate, package_image) and same_image(candidate, runtime_image), f"installed DDS decode differs from approved PNG for {stem}")
	with Image.open(decoded_path) as opened:
		decoded = opened.convert("RGBA")
	require(same_image(candidate, decoded), f"decoded installed preview differs for {stem}")
	return {
		"identifier": stem,
		"package": package_record,
		"runtime": runtime_record,
		"package_runtime_byte_identical": True,
		"decoded_pixel_equal_to_approved_png": True,
		"approval_record": rel(Path(approval["record_path"])),
	}


def font(size: int) -> ImageFont.ImageFont:
	for path in (Path("C:/Windows/Fonts/arial.ttf"), Path("C:/Windows/Fonts/segoeui.ttf")):
		if path.is_file():
			return ImageFont.truetype(str(path), size=size)
	return ImageFont.load_default()


def checker(size: tuple[int, int], tile: int) -> Image.Image:
	image = Image.new("RGBA", size, (92, 92, 92, 255))
	draw = ImageDraw.Draw(image)
	for y in range(0, size[1], tile):
		for x in range(0, size[0], tile):
			if (x // tile + y // tile) % 2:
				draw.rectangle((x, y, min(x + tile - 1, size[0] - 1), min(y + tile - 1, size[1] - 1)), fill=(132, 132, 132, 255))
	return image


def source_sheet(specs: dict[str, dict[str, object]]) -> Image.Image:
	display = (195, 201)
	sheet = Image.new("RGB", (4 * 223, 4 * 247), (28, 30, 32))
	draw = ImageDraw.Draw(sheet)
	for index, stem in enumerate(ADVISORS):
		spec = specs[stem]
		with Image.open(Path(spec["source_path"])) as opened:
			preview = ImageOps.fit(opened.convert("RGB").crop(tuple(spec["approved_crop"])), display, Image.Resampling.LANCZOS)
		x, y = (index % 4) * 223 + 14, (index // 4) * 247 + 8
		sheet.paste(preview, (x, y))
		draw.text((x, y + 209), stem.removeprefix("advisor_utopia_manifesto_"), font=font(11), fill=(238, 238, 234))
	return sheet


def icon_sheet(folder: Path, scale: int) -> Image.Image:
	icon_size = (65 * scale, 67 * scale)
	cell_width = max(icon_size[0] + 28, 195)
	cell_height = icon_size[1] + 46
	sheet = Image.new("RGBA", (4 * cell_width, 4 * cell_height), (28, 30, 32, 255))
	draw = ImageDraw.Draw(sheet)
	for index, stem in enumerate(ADVISORS):
		path = folder / f"{stem}.png"
		with Image.open(path) as opened:
			icon = opened.convert("RGBA").resize(icon_size, Image.Resampling.NEAREST)
		base = checker(icon_size, max(2, 8 * scale))
		base.alpha_composite(icon)
		x, y = (index % 4) * cell_width + 14, (index // 4) * cell_height + 8
		sheet.alpha_composite(base, (x, y))
		draw.text((x, y + icon_size[1] + 8), stem.removeprefix("advisor_utopia_manifesto_"), font=font(11), fill=(238, 238, 234, 255))
	return sheet


def handle_contact_sheets(specs: dict[str, dict[str, object]], write: bool, include_decoded: bool = False) -> None:
	sheets = {
		CONTACT / "advisor_sources_contact_sheet.png": source_sheet(specs),
		CONTACT / "advisor_portraits_native_contact_sheet.png": icon_sheet(PROCESSED, 1),
		CONTACT / "advisor_portraits_enlarged_nearest_contact_sheet.png": icon_sheet(PROCESSED, 4),
	}
	if include_decoded:
		sheets[CONTACT / "advisor_portraits_decoded_contact_sheet.png"] = icon_sheet(DECODED, 4)
	for path, expected in sheets.items():
		if write:
			atomic_image(path, expected)
		elif not path.is_file():
			raise FileNotFoundError(path)
		else:
			with Image.open(path) as opened:
				require(same_image(opened, expected), f"contact sheet differs: {rel(path)}")


def update_records(replacements: dict[str, dict[str, object]]) -> None:
	require(
		set(replacements) == set(ADVISORS),
		"aggregate asset-record update requires a freshly validated full 16-card set",
	)
	existing = json.loads(ASSET_RECORDS_PATH.read_text(encoding="utf-8"))
	require(sum(row.get("kind") == "advisor_portrait" for row in existing) == 16, "asset_records advisor coverage differs")
	seen = set()
	merged = []
	for row in existing:
		identifier = row.get("identifier")
		if identifier in replacements:
			merged.append(replacements[identifier])
			seen.add(identifier)
		elif row.get("kind") == "advisor_portrait":
			raise ValueError(
				f"aggregate asset-record update has no fresh replacement for {identifier}"
			)
		else:
			merged.append(row)
	require(seen == set(ADVISORS), "asset_records is missing freshly validated advisors")
	atomic_json(ASSET_RECORDS_PATH, merged)


def candidate_report_payload(
	records: dict[str, dict[str, object]],
	regenerated: list[str],
) -> dict[str, object]:
	require(
		set(records) == set(ADVISORS),
		"aggregate candidate report requires a freshly validated full 16-card set",
	)
	ordered = [records[stem] for stem in ADVISORS]
	return {
		"status": "candidate_requires_visual_approval", "date": "2026-07-16",
		"expected_advisor_count": 16, "validated_advisor_count": 16, "coverage_complete": True,
		"regenerated_identifiers": regenerated, "processor": rel(PROCESSOR), "processor_version": EXPECTED_PROCESSOR_VERSION,
		"render_version": EXPECTED_RENDER_VERSION, "processor_sha256": EXPECTED_PROCESSOR_SHA256,
		"render_configuration_sha256": EXPECTED_RENDER_CONFIGURATION_SHA256, "runtime": EXPECTED_RUNTIME,
		"converter": rel(CONVERTER), "converter_sha256": EXPECTED_CONVERTER_SHA256,
		"portrait_provenance_manifest": rel(PORTRAIT_MANIFEST), "portrait_provenance_manifest_sha256": sha256(PORTRAIT_MANIFEST),
		"overlay_manifest": rel(OVERLAY_MANIFEST), "overlay_manifest_sha256": EXPECTED_OVERLAY_MANIFEST_SHA256,
		"canonical_alpha_sha256": EXPECTED_ALPHA_SHA256, "canonical_paper_family_sha256": EXPECTED_PAPER_FAMILY_SHA256,
		"style_band_count": 9, "visual_approval": "not_performed_by_this_tool",
		"rejected_v2_history": {"path": rel(V2_HISTORY), "file_count_at_validation": sum(path.is_file() for path in V2_HISTORY.rglob("*"))},
		"source_review_sheet": rel(CONTACT / "advisor_sources_contact_sheet.png"),
		"native_review_sheet": rel(CONTACT / "advisor_portraits_native_contact_sheet.png"),
		"nearest_neighbour_review_sheet": rel(CONTACT / "advisor_portraits_enlarged_nearest_contact_sheet.png"),
		"files": ordered,
	}


def update_report(records: dict[str, dict[str, object]], regenerated: list[str]) -> None:
	atomic_json(VALIDATION_PATH, candidate_report_payload(records, regenerated))


def checksum_paths() -> list[Path]:
	paths = [PROCESSOR, CONVERTER, OVERLAY_MANIFEST, PORTRAIT_MANIFEST, FRAME_SOURCE, FRAME_OVERLAY, PAPER_SOURCE, PAPER_OVERLAY, VALIDATION_PATH]
	paths.extend([CONTACT / name for name in ("advisor_sources_contact_sheet.png", "advisor_portraits_native_contact_sheet.png", "advisor_portraits_enlarged_nearest_contact_sheet.png")])
	for stem in ADVISORS:
		paths.extend([SOURCE / f"{stem}_source.png", PROCESSED / f"{stem}.png", REVIEWS / f"{stem}_comparison.png", METADATA / f"{stem}.json"])
	return list(dict.fromkeys(path for path in paths if path.is_file()))


def handle_checksums(write: bool) -> None:
	payload = "\n".join(f"{sha256(path)}  {rel(path)}" for path in checksum_paths()) + "\n"
	if write:
		atomic_bytes(CHECKSUMS_PATH, payload.encode("utf-8"))
	else:
		require(CHECKSUMS_PATH.is_file() and CHECKSUMS_PATH.read_text(encoding="utf-8") == payload, "advisor checksums differ")


def validate_catalog(
	records: dict[str, dict[str, object]],
	asset_records: dict[str, dict[str, object]],
	require_complete: bool,
	approval_records: dict[str, dict[str, object]] | None = None,
) -> None:
	report = json.loads(VALIDATION_PATH.read_text(encoding="utf-8"))
	expected_report = candidate_report_payload(records, list(ADVISORS))
	require(report == expected_report, "candidate report differs from a fresh full reconstruction")
	rows = {row.get("identifier"): row for row in report.get("files", [])}
	if require_complete:
		require(report.get("coverage_complete") is True and set(rows) == set(ADVISORS), "candidate report is not complete")
	assets = json.loads(ASSET_RECORDS_PATH.read_text(encoding="utf-8"))
	advisor_rows = [row for row in assets if row.get("kind") == "advisor_portrait"]
	advisor_identifiers = [row.get("identifier") for row in advisor_rows]
	require(
		len(advisor_rows) == len(ADVISORS)
		and len(set(advisor_identifiers)) == len(ADVISORS)
		and set(advisor_identifiers) == set(ADVISORS),
		"asset-record advisor rows must contain every identifier exactly once",
	)
	asset_rows = {row["identifier"]: row for row in advisor_rows}
	require(set(asset_rows) == set(ADVISORS), "asset-record advisor coverage differs")
	if approval_records is not None:
		require(set(approval_records) == set(ADVISORS), "installed asset-record validation requires complete approval evidence")
		approval_paths = {Path(str(row["record_path"])).resolve() for row in approval_records.values()}
		require(len(approval_paths) == 1, "installed asset-record approval evidence is not one package")
		approval_path = next(iter(approval_paths))
		decoded_sheet = CONTACT / "advisor_portraits_decoded_contact_sheet.png"
		expected_installed_assets = []
		for stem in ADVISORS:
			processed = PROCESSED / f"{stem}.png"
			package = FINAL / f"{stem}.dds"
			runtime = RUNTIME / f"{stem}.dds"
			decoded = DECODED / f"{stem}.png"
			for path in (processed, package, runtime, decoded):
				if not path.is_file():
					raise FileNotFoundError(path)
			require(package.read_bytes() == runtime.read_bytes(), f"package/runtime DDS differs for {stem}")
			with Image.open(processed) as opened:
				approved_rgba = opened.convert("RGBA")
			with Image.open(decoded) as opened:
				decoded_rgba = opened.convert("RGBA")
			require(same_image(approved_rgba, decoded_rgba), f"decoded PNG differs from approved PNG for {stem}")
			expected_installed_assets.append({
				"identifier": stem,
				"approved_png_sha256": sha256(processed),
				"dds_sha256": sha256(package),
				"decoded_png_sha256": sha256(decoded),
				"pixel_equal": True,
			})
		expected_installed_report = {
			"schema_version": 1,
			"record_type": "chaos_redux_advisor_v5_installed_validation",
			"event_id": "015",
			"asset_family": "advisor_v5",
			"validation_date": "2026-07-16",
			"status": "passed",
			"approved_asset_count": len(ADVISORS),
			"processor": rel(PROCESSOR),
			"processor_sha256": EXPECTED_PROCESSOR_SHA256,
			"converter": rel(CONVERTER),
			"converter_sha256": EXPECTED_CONVERTER_SHA256,
			"validator": rel(Path(__file__)),
			"validator_sha256": sha256(Path(__file__)),
			"approval_record": rel(approval_path),
			"approval_record_sha256": sha256(approval_path),
			"decoded_contact_sheet": rel(decoded_sheet),
			"decoded_contact_sheet_sha256": sha256(decoded_sheet),
			"contract": {
				"dimensions": [65, 67],
				"dds_format": "one-level uncompressed BGRA 32-bit",
				"package_runtime_byte_equality": True,
				"decoded_rgba_equality_to_approved_png": True,
				"visual_approval_required": True,
				"visual_approval_present": True,
			},
			"assets": expected_installed_assets,
		}
		installed_report = json.loads(INSTALLED_VALIDATION_PATH.read_text(encoding="utf-8"))
		require(installed_report == expected_installed_report, "installed validation report differs from a fresh reconstruction")
		installed_report_hash = sha256(INSTALLED_VALIDATION_PATH)
		approval_hash = sha256(approval_path)
		for stem, candidate in asset_records.items():
			actual = dict(asset_rows[stem])
			processed = PROCESSED / f"{stem}.png"
			package = FINAL / f"{stem}.dds"
			runtime = RUNTIME / f"{stem}.dds"
			decoded = DECODED / f"{stem}.png"
			require(actual.get("status") == "approved", f"installed asset record status differs for {stem}")
			require(actual.get("approval_record") == rel(approval_path) and actual.get("approval_record_sha256") == approval_hash, f"installed approval pins differ for {stem}")
			require(actual.get("installed_validation_report") == rel(INSTALLED_VALIDATION_PATH) and actual.get("installed_validation_report_sha256") == installed_report_hash, f"installed validation pins differ for {stem}")
			require(actual.get("package_final") == rel(package) and actual.get("package_final_sha256") == sha256(package), f"package DDS pins differ for {stem}")
			require(actual.get("runtime_final") == rel(runtime) and actual.get("runtime_sha256") == sha256(runtime), f"runtime DDS pins differ for {stem}")
			require(actual.get("decoded") == rel(decoded) and actual.get("decoded_sha256") == sha256(decoded), f"decoded PNG pins differ for {stem}")
			require(actual.get("notes") == INSTALLED_NOTES, f"installed asset-record notes differ for {stem}")
			require(actual.get("validation", {}).get("visual_approval_record_present") is True, f"installed approval marker differs for {stem}")
			require(actual.get("validation", {}).get("dds_state") == "installed_and_pixel_verified_against_approved_png", f"installed DDS state differs for {stem}")
			for key in ("approval_record", "approval_record_sha256", "installed_validation_report", "installed_validation_report_sha256", "package_final", "package_final_sha256", "runtime_final", "runtime_sha256", "decoded", "decoded_sha256"):
				actual.pop(key)
			actual["status"] = "needs_user_review"
			actual["validation"] = dict(actual["validation"])
			actual["validation"]["visual_approval_record_present"] = False
			actual["validation"]["dds_state"] = "not_converted_pending_independent_visual_approval"
			actual["notes"] = "Automated v5 candidate validation only; native and 4x contact sheets require independent visual review before DDS use can be approved."
			require(actual == candidate, f"installed asset record candidate projection differs for {stem}")
		return
	for stem, expected in asset_records.items():
		require(asset_rows.get(stem) == expected, f"asset record differs for {stem}")


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description=__doc__)
	modes = parser.add_mutually_exclusive_group()
	modes.add_argument("--regenerate", action="store_true", help="Write/rewrite PNG candidates and candidate-only records; never DDS")
	modes.add_argument("--validate-installed", action="store_true", help="Read-only DDS/decode validation after independent approval")
	parser.add_argument("--only", action="append", default=[], metavar="STEM", help="Repeatable exact advisor stem; default is all sixteen; partial runs never update aggregate records")
	parser.add_argument("--approval-record", action="append", default=[], type=Path, metavar="JSON", help="Repeatable independent approval record; required by --validate-installed")
	return parser.parse_args()


def main() -> None:
	args = parse_args()
	require_hash(PROCESSOR, EXPECTED_PROCESSOR_SHA256)
	require_hash(CONVERTER, EXPECTED_CONVERTER_SHA256)
	require(platform.python_version() == EXPECTED_RUNTIME["python"] and PILLOW_VERSION == EXPECTED_RUNTIME["pillow"], f"validator runtime differs: python={platform.python_version()}, pillow={PILLOW_VERSION}")
	require(V2_HISTORY.is_dir(), "rejected advisor v2 history is missing")
	v2_count = sum(path.is_file() for path in V2_HISTORY.rglob("*"))
	require(v2_count >= 86, f"rejected advisor v2 preservation is incomplete: {v2_count} files")
	validate_overlay_package()
	specs, portrait_manifest_sha = load_portrait_manifest()
	references = derive_references()
	selected = args.only or list(ADVISORS)
	unknown = [stem for stem in selected if stem not in ADVISORS]
	require(not unknown, f"unknown --only advisor stem(s): {unknown}")
	selected = list(dict.fromkeys(selected))
	full_selection = set(selected) == set(ADVISORS)
	require(args.validate_installed or not args.approval_record, "--approval-record is only valid with --validate-installed")
	require(not args.validate_installed or bool(args.approval_record), "--validate-installed requires --approval-record")
	if args.regenerate:
		for stem in selected:
			regenerate(stem, specs[stem])
	validation_records: dict[str, dict[str, object]] = {}
	asset_records: dict[str, dict[str, object]] = {}
	for stem in selected:
		validation_record, asset_record = validate_candidate(stem, specs[stem], portrait_manifest_sha, references)
		validation_records[stem] = validation_record
		asset_records[stem] = asset_record
	aggregate_updated = False
	if args.regenerate and full_selection:
		handle_contact_sheets(specs, True)
		update_records(asset_records)
		update_report(validation_records, selected)
		handle_checksums(True)
		aggregate_updated = True
	approvals: dict[str, dict[str, object]] = {}
	if args.validate_installed:
		approvals = load_approval_records(args.approval_record)
		require(all(stem in approvals for stem in selected), "approval records do not cover every selected advisor")
	elif not args.regenerate and full_selection:
		handle_contact_sheets(specs, False)
		validate_catalog(validation_records, asset_records, True)
		handle_checksums(False)
	if args.validate_installed and full_selection:
		handle_contact_sheets(specs, False)
		validate_catalog(validation_records, asset_records, True, approvals)
		handle_checksums(False)
	installed = []
	if args.validate_installed:
		installed = [validate_installed(stem, approvals[stem]) for stem in selected]
		if full_selection:
			handle_contact_sheets(specs, False, include_decoded=True)
	mode = "regenerated_png_candidates" if args.regenerate else ("read_only_installed_validation" if args.validate_installed else "read_only_candidate_validation")
	print(json.dumps({"status": "candidate_requires_visual_approval", "mode": mode, "validated": selected, "aggregate_updated": aggregate_updated, "installed_validation": installed, "visual_approval": "not_performed_by_this_tool"}, indent=2))


if __name__ == "__main__":
	main()
