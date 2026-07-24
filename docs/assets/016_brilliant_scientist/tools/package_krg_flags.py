#!/usr/bin/env python3
"""Package the seven ImageGen-authored KRG flags for HOI4.

The script performs technical finishing only: exact-ratio centre cropping,
solid-palette cleanup that preserves the generated geometry, native-size
resampling, bottom-left 32-bit TGA encoding, runtime installation, review
contacts, provenance, hashes, and decoded-output validation.
"""

from __future__ import annotations

import hashlib
import json
import shutil
import struct
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[4]
SOURCE_DIR = PACKAGE_ROOT / "source_png" / "flags"
PROCESSED_DIR = PACKAGE_ROOT / "processed_png" / "flags"
FINAL_DIR = PACKAGE_ROOT / "final_tga" / "flags"
CONTACT_DIR = PACKAGE_ROOT / "contact_sheets"
RECORD_DIR = PACKAGE_ROOT / "package_records"

MASTER_SIZE = (820, 520)
SIZES = {"normal": (82, 52), "medium": (41, 26), "small": (10, 7)}


@dataclass(frozen=True)
class FlagSpec:
	tag: str
	identity: str
	expected_source_size: tuple[int, int]
	imagegen_handle: str
	palette: tuple[tuple[int, int, int], ...]


SPECS = (
	FlagSpec("KRG", "Kruger provisional laboratory state", (1573, 1000), "exec-9c7c2a67-7c24-4f18-bce0-59de43bab083", ((38, 39, 42), (239, 232, 213), (116, 31, 37), (184, 145, 66), (248, 246, 237))),
	FlagSpec("KRG_SCIENTIFIC_REPUBLIC", "Scientific Republic", (1576, 998), "exec-6d5f3f82-1b71-4be5-8c1b-def65cba61ba", ((20, 61, 82), (22, 105, 112), (239, 232, 213), (184, 145, 66), (248, 246, 237))),
	FlagSpec("KRG_REPLICATED_STATE", "Replicated State", (1581, 995), "exec-2200f3b9-883e-4d33-a87c-515a4018043c", ((105, 28, 37), (54, 16, 24), (239, 232, 213), (184, 145, 66), (248, 246, 237))),
	FlagSpec("KRG_MACHINE_STATE", "Machine State", (1577, 997), "exec-566ecf5c-b8b1-411e-9edc-9637c43196db", ((47, 50, 52), (20, 21, 22), (184, 145, 66), (151, 158, 160), (248, 246, 237))),
	FlagSpec("KRG_TEMPORAL_CONTINUUM", "Temporal Continuum", (1573, 1000), "exec-7422be9c-68b8-434b-81f8-7ec0adc2614e", ((20, 27, 54), (48, 43, 91), (239, 232, 213), (184, 145, 66), (248, 246, 237))),
	FlagSpec("KRG_XENOBIOLOGICAL_ASCENDANCY", "Xenobiological Ascendancy", (1581, 995), "exec-357503bf-d415-4488-a1b9-e661a5731e1e", ((13, 76, 58), (8, 60, 68), (239, 232, 213), (184, 145, 66), (248, 246, 237))),
	FlagSpec("KRG_PROJECT_SYNTHESIS", "Project Synthesis", (1576, 998), "exec-e1c8878c-e6dc-40fd-8f62-dd20ef7f0008", ((102, 29, 35), (49, 51, 52), (5, 90, 102), (239, 232, 213), (184, 145, 66), (248, 246, 237))),
)


def sha256(path: Path) -> str:
	digest = hashlib.sha256()
	with path.open("rb") as handle:
		for block in iter(lambda: handle.read(65536), b""):
			digest.update(block)
	return digest.hexdigest()


def exact_ratio_crop(size: tuple[int, int]) -> tuple[int, int, int, int]:
	width, height = size
	crop_width = min(width, height * 41 // 26)
	crop_height = crop_width * 26 // 41
	if crop_height > height:
		crop_height = height
		crop_width = crop_height * 41 // 26
	left = (width - crop_width) // 2
	top = (height - crop_height) // 2
	return left, top, left + crop_width, top + crop_height


def quantize(image: Image.Image, palette: tuple[tuple[int, int, int], ...]) -> Image.Image:
	pixels = np.asarray(image.convert("RGB"), dtype=np.int32)
	colours = np.asarray(palette, dtype=np.int32)
	distance = ((pixels[:, :, None, :] - colours[None, None, :, :]) ** 2).sum(axis=3)
	return Image.fromarray(colours[distance.argmin(axis=2)].astype(np.uint8), "RGB")


def write_tga(path: Path, image: Image.Image) -> None:
	rgba = np.asarray(image.convert("RGBA"), dtype=np.uint8)
	height, width = rgba.shape[:2]
	header = struct.pack("<BBBHHBHHHHBB", 0, 0, 2, 0, 0, 0, 0, 0, width, height, 32, 8)
	path.write_bytes(header + rgba[::-1, :, [2, 1, 0, 3]].tobytes())


def tga_metadata(path: Path) -> dict[str, object]:
	raw = path.read_bytes()
	header = struct.unpack("<BBBHHBHHHHBB", raw[:18])
	width, height, descriptor = header[8], header[9], header[11]
	return {
		"image_type": header[2], "width": width, "height": height,
		"pixel_depth": header[10], "alpha_bits": descriptor & 15,
		"origin": "top-left" if descriptor & 0x20 else "bottom-left",
		"byte_length": len(raw), "expected_byte_length": 18 + width * height * 4,
	}


def labelled_sheet(rows: list[tuple[str, Image.Image, Image.Image, dict[str, Image.Image]]]) -> None:
	font = ImageFont.load_default()
	sheet = Image.new("RGB", (1510, 1510), (230, 230, 226))
	draw = ImageDraw.Draw(sheet)
	draw.text((20, 14), "Event 016 KRG flags: ImageGen source, solid-palette master, and decoded native TGA ladder", fill=(15, 15, 15), font=font)
	for index, (label, source, master, sizes) in enumerate(rows):
		y = 50 + index * 205
		draw.text((20, y), label, fill=(15, 15, 15), font=font)
		source_preview = source.resize((315, 200), Image.Resampling.LANCZOS)
		master_preview = master.resize((315, 200), Image.Resampling.NEAREST)
		sheet.paste(source_preview, (20, y + 18))
		sheet.paste(master_preview, (355, y + 18))
		x = 690
		for role, scale in (("normal", 4), ("medium", 8), ("small", 28)):
			image = sizes[role]
			enlarged = image.resize((image.width * scale, image.height * scale), Image.Resampling.NEAREST)
			draw.text((x, y), f"{role} {image.width}x{image.height}", fill=(15, 15, 15), font=font)
			sheet.paste(enlarged, (x, y + 18))
			x += max(enlarged.width, 160) + 12
	sheet.save(CONTACT_DIR / "krg_flag_source_vs_runtime_contact_sheet.png")


def process() -> None:
	for directory in (PROCESSED_DIR, FINAL_DIR, CONTACT_DIR, RECORD_DIR):
		directory.mkdir(parents=True, exist_ok=True)
	record: dict[str, object] = {
		"classification": "seven distinct ImageGen-authored KRG flag identities",
		"processing": "exact-ratio crop, palette cleanup preserving generated geometry, native resampling, bottom-left 32-bit uncompressed TGA",
		"flags": {},
	}
	contact_rows = []
	for spec in SPECS:
		source_path = SOURCE_DIR / f"{spec.tag}_imagegen_raw.png"
		source = Image.open(source_path).convert("RGB")
		if source.size != spec.expected_source_size:
			raise ValueError(f"{spec.tag}: {source.size} != {spec.expected_source_size}")
		crop_box = exact_ratio_crop(source.size)
		master = quantize(source.crop(crop_box).resize(MASTER_SIZE, Image.Resampling.LANCZOS), spec.palette)
		master_path = PROCESSED_DIR / f"{spec.tag}_master_820x520.png"
		master.save(master_path)
		size_images: dict[str, Image.Image] = {}
		size_records: dict[str, object] = {}
		for role, size in SIZES.items():
			resample = Image.Resampling.LANCZOS if role != "small" else Image.Resampling.NEAREST
			candidate = quantize(master.resize(size, resample), spec.palette)
			png_path = PROCESSED_DIR / f"{spec.tag}_{role}_{size[0]}x{size[1]}.png"
			package_path = FINAL_DIR / f"{spec.tag}_{role}_{size[0]}x{size[1]}.tga"
			candidate.save(png_path)
			write_tga(package_path, candidate)
			runtime = REPO_ROOT / "gfx" / "flags" / (f"{spec.tag}.tga" if role == "normal" else f"{role}/{spec.tag}.tga")
			runtime.parent.mkdir(parents=True, exist_ok=True)
			shutil.copy2(package_path, runtime)
			decoded = Image.open(runtime).convert("RGB")
			matches = np.array_equal(np.asarray(decoded), np.asarray(candidate))
			metadata = tga_metadata(runtime)
			if not matches or metadata["origin"] != "bottom-left" or metadata["byte_length"] != metadata["expected_byte_length"]:
				raise ValueError(f"{spec.tag} {role}: decoded TGA validation failed")
			size_images[role] = decoded
			size_records[role] = {
				"dimensions": list(size), "processed_png": png_path.relative_to(PACKAGE_ROOT).as_posix(),
				"package_tga": package_path.relative_to(PACKAGE_ROOT).as_posix(),
				"runtime_tga": runtime.relative_to(REPO_ROOT).as_posix(), "tga": metadata,
				"decoded_matches_png": matches, "package_sha256": sha256(package_path),
				"runtime_sha256": sha256(runtime), "runtime_matches_package": sha256(package_path) == sha256(runtime),
			}
		contact_rows.append((f"{spec.tag} — {spec.identity}", source, master, size_images))
		record["flags"][spec.tag] = {
			"identity": spec.identity, "imagegen_handle": spec.imagegen_handle,
			"source": source_path.relative_to(PACKAGE_ROOT).as_posix(), "source_dimensions": list(source.size),
			"source_sha256": sha256(source_path), "crop_box": list(crop_box),
			"master": master_path.relative_to(PACKAGE_ROOT).as_posix(),
			"palette": ["#%02X%02X%02X" % colour for colour in spec.palette], "sizes": size_records,
		}
	labelled_sheet(contact_rows)
	(RECORD_DIR / "krg_flag_package.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
	(PACKAGE_ROOT / "prompts" / "krg_flag_prompts.md").parent.mkdir(parents=True, exist_ok=True)
	(PACKAGE_ROOT / "prompts" / "krg_flag_prompts.md").write_text(
		"# Event 016 KRG flag prompt record\n\nEach source is a distinct ImageGen-authored flat alternate-history flag. The shared family grammar is a severe laboratory-state banner with a central disc and simple route emblem; every route received a separate generated emblem and colour identity. Handles and exact source hashes are recorded in `package_records/krg_flag_package.json`. Local processing only cropped, palette-cleaned, resized, encoded, and validated the generated geometry.\n",
		encoding="utf-8",
	)


if __name__ == "__main__":
	process()
