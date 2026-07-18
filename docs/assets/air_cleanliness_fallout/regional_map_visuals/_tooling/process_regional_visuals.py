#!/usr/bin/env python3
"""Build the Fallout-owned Air Winter regional visual texture package.

The script performs deterministic extraction and channel derivation from the
approved image-generation source plates. It deliberately requires DirectXTex
through TEXCONV_PATH so the repository DDS helper cannot take its secondary
ffmpeg path.
"""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageOps


REPO_ROOT = Path(__file__).resolve().parents[5]
PACKAGE_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = PACKAGE_ROOT / "source_png"
PROCESSED_ROOT = PACKAGE_ROOT / "processed_png"
CONTACT_ROOT = PACKAGE_ROOT / "contact_sheets"
PREVIEW_ROOT = PACKAGE_ROOT / "previews"
MODEL_ROOT = REPO_ROOT / "gfx/models/air_cleanliness_winter/regional"
PARTICLE_ROOT = REPO_ROOT / "gfx/particles/air_cleanliness_winter"
GRADE_ROOT = REPO_ROOT / "gfx/interface/air_cleanliness_winter/regional_grades"
CONVERTER = REPO_ROOT / ".agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py"


REGIONS = [
    "boreal_continental",
    "temperate_maritime",
    "mediterranean",
    "desert_arid_plateau",
    "tropical_coast_monsoon",
    "equatorial_rainforest",
    "mountain_highland",
    "island_oceanic",
    "polar_subpolar",
]

# Class-specific frost reach. These are asset-authoring values, not gameplay
# tuning: the runtime phase and regional presentation class remain authoritative.
FROST_REACH = {
    "boreal_continental": 0.82,
    "temperate_maritime": 0.48,
    "mediterranean": 0.25,
    "desert_arid_plateau": 0.18,
    "tropical_coast_monsoon": 0.10,
    "equatorial_rainforest": 0.08,
    "mountain_highland": 0.88,
    "island_oceanic": 0.34,
    "polar_subpolar": 0.96,
}

REGION_TINTS = {
    "boreal_continental": (142, 151, 158),
    "temperate_maritime": (126, 121, 112),
    "mediterranean": (139, 126, 104),
    "desert_arid_plateau": (151, 139, 116),
    "tropical_coast_monsoon": (113, 115, 103),
    "equatorial_rainforest": (92, 104, 94),
    "mountain_highland": (134, 143, 150),
    "island_oceanic": (114, 125, 123),
    "polar_subpolar": (161, 177, 190),
}

PARTICLE_FAMILIES = {
    "snow_frost": (206, 224, 238),
    "cold_rain_mist": (147, 181, 204),
    "ash_dirty_snow": (151, 153, 157),
    "thaw_flood": (126, 160, 178),
}

PHASE_STRENGTH = (0.07, 0.16, 0.29, 0.43, 0.58, 0.72)
ASH_STRENGTH = (0.00, 0.015, 0.05, 0.22, 0.40, 0.58)
PHASE_DIMMING = (0.00, 0.025, 0.060, 0.135, 0.225, 0.315)
PHASE_SATURATION = (1.00, 0.96, 0.90, 0.78, 0.65, 0.54)
LANCZOS = Image.Resampling.LANCZOS


def ensure_dirs() -> None:
    for path in (
        PROCESSED_ROOT,
        CONTACT_ROOT,
        PREVIEW_ROOT,
        MODEL_ROOT,
        PARTICLE_ROOT,
        GRADE_ROOT,
    ):
        path.mkdir(parents=True, exist_ok=True)


def crop_grid(image: Image.Image, columns: int, rows: int) -> list[Image.Image]:
    width, height = image.size
    cells: list[Image.Image] = []
    for row in range(rows):
        for column in range(columns):
            left = round(column * width / columns)
            right = round((column + 1) * width / columns)
            top = round(row * height / rows)
            bottom = round((row + 1) * height / rows)
            cells.append(image.crop((left, top, right, bottom)))
    return cells


def rgba_from_black(source: Image.Image, tint: tuple[int, int, int] | None = None) -> Image.Image:
    rgb = np.asarray(source.convert("RGB"), dtype=np.float32)
    lum = rgb[..., 0] * 0.2126 + rgb[..., 1] * 0.7152 + rgb[..., 2] * 0.0722
    alpha = np.clip((lum - 2.0) * 1.55, 0.0, 255.0)
    alpha = np.power(alpha / 255.0, 0.82) * 255.0
    if tint is None:
        out_rgb = rgb
    else:
        intensity = np.clip(lum[..., None] / 210.0, 0.16, 1.0)
        out_rgb = np.asarray(tint, dtype=np.float32)[None, None, :] * intensity
    out = np.dstack((np.clip(out_rgb, 0, 255), alpha)).astype(np.uint8)
    return Image.fromarray(out, "RGBA")


def height_to_normal(source: Image.Image, strength: float = 4.0) -> Image.Image:
    rgba = np.asarray(source.convert("RGBA"), dtype=np.float32) / 255.0
    lum = rgba[..., :3].mean(axis=2) * rgba[..., 3]
    dy, dx = np.gradient(lum)
    nx = -dx * strength
    ny = dy * strength
    nz = np.ones_like(nx)
    length = np.sqrt(nx * nx + ny * ny + nz * nz)
    normal = np.dstack((nx / length, ny / length, nz / length))
    normal = ((normal * 0.5 + 0.5) * 255.0).astype(np.uint8)
    alpha = np.full(lum.shape, 255, dtype=np.uint8)
    return Image.fromarray(np.dstack((normal, alpha)), "RGBA")


def make_specular(source: Image.Image, low: int, high: int) -> Image.Image:
    rgba = np.asarray(source.convert("RGBA"), dtype=np.float32)
    lum = rgba[..., :3].mean(axis=2) / 255.0
    value = np.clip(low + (high - low) * lum, 0, 255).astype(np.uint8)
    alpha = np.full(value.shape, 255, dtype=np.uint8)
    return Image.fromarray(np.dstack((value, value, value, alpha)), "RGBA")


def phase_variant(base: Image.Image, region: str, phase: int) -> Image.Image:
    rgb = np.asarray(base.convert("RGB"), dtype=np.float32)
    gray = rgb.mean(axis=2)
    height = Image.fromarray(gray.astype(np.uint8), "L").filter(ImageFilter.GaussianBlur(3.2))
    height_array = np.asarray(height, dtype=np.float32) / 255.0
    local_frost = np.clip((height_array - 0.20) / 0.80, 0.0, 1.0)
    local_frost = 0.30 + local_frost * 0.70
    frost = PHASE_STRENGTH[phase - 1] * FROST_REACH[region] * local_frost
    cold_color = np.array([184.0, 202.0, 216.0], dtype=np.float32)
    out = rgb * (1.0 - frost[..., None]) + cold_color * frost[..., None]
    ash = ASH_STRENGTH[phase - 1]
    soot_color = np.array([45.0, 49.0, 53.0], dtype=np.float32)
    ash_mask = np.clip(1.0 - height_array, 0.0, 1.0) * ash
    out = out * (1.0 - ash_mask[..., None]) + soot_color * ash_mask[..., None]
    # Black Harvest onward needs a readable ash/dimming jump even in warm
    # classes. This is deliberately separate from class-specific frost reach.
    dimming = PHASE_DIMMING[phase - 1]
    out *= 1.0 - dimming
    out_lum = out[..., 0] * 0.2126 + out[..., 1] * 0.7152 + out[..., 2] * 0.0722
    saturation = PHASE_SATURATION[phase - 1]
    out = out_lum[..., None] * (1.0 - saturation) + out * saturation
    cold_lift = np.array([0.0, 4.0 + phase * 0.8, 8.0 + phase * 1.3], dtype=np.float32)
    out += cold_lift
    # Preserve strategic-map legibility while making phases 4-6 unmistakable.
    contrast = (1.03, 1.01, 0.99, 0.95, 0.91, 0.87)[phase - 1]
    midpoint = 112.0
    out = (out - midpoint) * contrast + midpoint
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8), "RGB").convert("RGBA")


def save_png(image: Image.Image, path: Path, size: tuple[int, int] | None = None) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    result = image.resize(size, LANCZOS) if size else image
    result.save(path, format="PNG", optimize=True)
    return path


def convert_dds(source: Path, output: Path, size: tuple[int, int] | None = None) -> Path:
    texconv = os.environ.get("TEXCONV_PATH") or os.environ.get("TEXCONV_EXE")
    if not texconv or not Path(texconv).is_file():
        raise RuntimeError("TEXCONV_PATH must point to the approved DirectXTex texconv executable")
    command = [
        sys.executable,
        str(CONVERTER),
        "--input",
        str(source),
        "--output",
        str(output),
    ]
    if size:
        command.extend(["--width", str(size[0]), "--height", str(size[1])])
    env = os.environ.copy()
    env["TEXCONV_PATH"] = str(Path(texconv).resolve())
    subprocess.run(command, cwd=REPO_ROOT, env=env, check=True, capture_output=True, text=True)
    return output


def build_regional_materials() -> dict[str, Image.Image]:
    atlas = Image.open(SOURCE_ROOT / "materials/regional_material_atlas_source.png").convert("RGB")
    cells = crop_grid(atlas, 3, 3)
    detail = Image.open(SOURCE_ROOT / "materials/boreal_continental_detail_source.png").convert("RGB")
    source_previews: dict[str, Image.Image] = {}

    for index, region in enumerate(REGIONS):
        base = detail if region == "boreal_continental" else cells[index]
        base = ImageOps.fit(base, (512, 512), method=LANCZOS)
        base = ImageEnhance.Contrast(base).enhance(1.05)
        source_previews[region] = base.copy()
        base_path = save_png(base, PROCESSED_ROOT / f"materials/{region}_base.png")
        normal_path = save_png(height_to_normal(base, 3.8), PROCESSED_ROOT / f"materials/{region}_n.png")
        spec_path = save_png(make_specular(base, 28, 72), PROCESSED_ROOT / f"materials/{region}_spec.png")
        convert_dds(normal_path, MODEL_ROOT / f"air_winter_{region}_n.dds", (256, 256))
        convert_dds(spec_path, MODEL_ROOT / f"air_winter_{region}_spec.dds", (256, 256))

        for phase in range(1, 7):
            variant = phase_variant(base, region, phase)
            phase_path = save_png(variant, PROCESSED_ROOT / f"materials/{region}_phase_{phase}_diff.png")
            convert_dds(phase_path, MODEL_ROOT / f"air_winter_{region}_phase_{phase}_diff.dds", (256, 256))

        # Base is retained for provenance and side-by-side review, not registered at runtime.
        _ = base_path
    return source_previews


def build_particles() -> tuple[dict[str, list[Image.Image]], dict[str, Image.Image]]:
    atlas = Image.open(SOURCE_ROOT / "particles/regional_particle_frames_source.png").convert("RGB")
    cells = crop_grid(atlas, 4, 4)
    all_frames: dict[str, list[Image.Image]] = {}
    static_frames: dict[str, Image.Image] = {}

    for row, (family, tint) in enumerate(PARTICLE_FAMILIES.items()):
        frames: list[Image.Image] = []
        for column in range(4):
            cell = cells[row * 4 + column]
            separated_source = ImageOps.fit(cell, (384, 384), method=LANCZOS)
            save_png(
                separated_source,
                SOURCE_ROOT / f"particles/source_frames/{family}/frame_{column + 1:02d}_source.png",
            )
            frame = rgba_from_black(separated_source.resize((256, 256), LANCZOS), tint)
            frame_path = save_png(frame, PROCESSED_ROOT / f"particles/frames/{family}_{column + 1:02d}.png")
            frames.append(Image.open(frame_path).convert("RGBA"))

        horizontal = Image.new("RGBA", (1024, 256), (0, 0, 0, 0))
        for column, frame in enumerate(frames):
            horizontal.alpha_composite(frame, (column * 256, 0))
        atlas_path = save_png(horizontal, PROCESSED_ROOT / f"particles/atlases/{family}_atlas.png")
        convert_dds(atlas_path, PARTICLE_ROOT / f"air_winter_{family}_atlas.dds")

        static = frames[0].copy()
        static_frames[family] = static
        static_doc_path = save_png(static, PROCESSED_ROOT / f"particles/{family}_static_fallback.png")
        convert_dds(static_doc_path, GRADE_ROOT / f"air_winter_static_{family}.dds")

        static_diff = static.copy()
        static_diff_path = save_png(static_diff, PROCESSED_ROOT / f"particles/{family}_static_mesh_diff.png")
        static_n_path = save_png(height_to_normal(static_diff, 4.5), PROCESSED_ROOT / f"particles/{family}_static_mesh_n.png")
        static_spec_path = save_png(make_specular(static_diff, 18, 82), PROCESSED_ROOT / f"particles/{family}_static_mesh_spec.png")
        convert_dds(static_diff_path, MODEL_ROOT / f"air_winter_static_{family}_diff.dds", (256, 256))
        convert_dds(static_n_path, MODEL_ROOT / f"air_winter_static_{family}_n.dds", (256, 256))
        convert_dds(static_spec_path, MODEL_ROOT / f"air_winter_static_{family}_spec.dds", (256, 256))

        frames[0].save(
            PREVIEW_ROOT / f"{family}_authored_frames.gif",
            save_all=True,
            append_images=frames[1:],
            duration=[240, 200, 180, 220],
            loop=0,
            disposal=2,
        )
        all_frames[family] = frames
    return all_frames, static_frames


def build_props() -> dict[str, dict[str, Image.Image]]:
    dead_atlas = Image.open(SOURCE_ROOT / "props/dead_vegetation_atlas_source.png").convert("RGB")
    water_atlas = Image.open(SOURCE_ROOT / "props/frozen_water_atlas_source.png").convert("RGB")
    dead_cells = crop_grid(dead_atlas, 3, 3)
    water_cells = crop_grid(water_atlas, 3, 3)
    previews: dict[str, dict[str, Image.Image]] = {}

    for index, region in enumerate(REGIONS):
        dead = rgba_from_black(ImageOps.fit(dead_cells[index], (512, 512), method=LANCZOS), REGION_TINTS[region])
        frozen = rgba_from_black(ImageOps.fit(water_cells[index], (512, 512), method=LANCZOS))
        frozen_array = np.asarray(frozen, dtype=np.float32)
        thaw_array = frozen_array.copy()
        thaw_array[..., 0] = thaw_array[..., 0] * 0.34 + 40.0
        thaw_array[..., 1] = thaw_array[..., 1] * 0.39 + 43.0
        thaw_array[..., 2] = thaw_array[..., 2] * 0.43 + 49.0
        thaw_array[..., 3] *= 0.94
        thaw = Image.fromarray(np.clip(thaw_array, 0, 255).astype(np.uint8), "RGBA")

        family_images = {
            "dead_vegetation": dead,
            "frozen_water": frozen,
            "thaw_flood": thaw,
        }
        previews[region] = family_images
        for family, image in family_images.items():
            family_root = PROCESSED_ROOT / f"props/{family}"
            diff_path = save_png(image, family_root / f"{region}_diff.png")
            normal_strength = 5.0 if family == "dead_vegetation" else 3.6
            n_path = save_png(height_to_normal(image, normal_strength), family_root / f"{region}_n.png")
            if family == "frozen_water":
                spec_range = (92, 198)
            elif family == "thaw_flood":
                spec_range = (68, 158)
            else:
                spec_range = (14, 48)
            spec_path = save_png(make_specular(image, *spec_range), family_root / f"{region}_spec.png")
            prefix = f"air_winter_{region}_{family}"
            convert_dds(diff_path, MODEL_ROOT / f"{prefix}_diff.dds", (256, 256))
            convert_dds(n_path, MODEL_ROOT / f"{prefix}_n.dds", (256, 256))
            convert_dds(spec_path, MODEL_ROOT / f"{prefix}_spec.dds", (256, 256))
    return previews


def build_grades() -> list[tuple[str, Image.Image]]:
    atlas = Image.open(SOURCE_ROOT / "grades/phase_grade_atlas_source.png").convert("RGB")
    cells = crop_grid(atlas, 3, 2)
    results: list[tuple[str, Image.Image]] = []

    grade_colors = (
        (68.0, 82.0, 94.0),
        (56.0, 70.0, 85.0),
        (45.0, 58.0, 73.0),
        (34.0, 44.0, 58.0),
        (24.0, 32.0, 44.0),
        (16.0, 23.0, 33.0),
    )
    alpha_bases = (8.0, 13.0, 19.0, 28.0, 39.0, 50.0)
    alpha_ceilings = (24.0, 33.0, 44.0, 58.0, 73.0, 88.0)
    for phase, cell in enumerate(cells, start=1):
        cell = ImageOps.fit(cell, (512, 512), method=LANCZOS)
        rgb = np.asarray(cell, dtype=np.float32)
        lum = rgb.mean(axis=2)
        alpha = np.clip(
            alpha_bases[phase - 1] + lum / 255.0 * alpha_ceilings[phase - 1],
            0.0,
            112.0,
        )
        color = np.broadcast_to(np.asarray(grade_colors[phase - 1], dtype=np.float32), rgb.shape)
        grade = Image.fromarray(np.dstack((color, alpha)).astype(np.uint8), "RGBA")
        name = f"phase_{phase}"
        path = save_png(grade, PROCESSED_ROOT / f"grades/air_winter_grade_{name}.png")
        convert_dds(path, GRADE_ROOT / f"air_winter_grade_{name}.dds")
        results.append((name, grade))

    recovery_source = cells[0].resize((512, 512), LANCZOS)
    source_rgb = np.asarray(recovery_source, dtype=np.float32)
    source_lum = source_rgb.mean(axis=2)
    recovery_defs = {
        "recovery_soot_thinning": ((112, 126, 132), 25.0),
        "recovery_uv_clear": ((102, 112, 158), 29.0),
    }
    for name, (color_value, ceiling) in recovery_defs.items():
        color = np.broadcast_to(np.asarray(color_value, dtype=np.float32), source_rgb.shape)
        alpha = np.clip(3.0 + source_lum / 255.0 * ceiling, 0.0, 32.0)
        grade = Image.fromarray(np.dstack((color, alpha)).astype(np.uint8), "RGBA")
        path = save_png(grade, PROCESSED_ROOT / f"grades/air_winter_grade_{name}.png")
        convert_dds(path, GRADE_ROOT / f"air_winter_grade_{name}.dds")
        results.append((name, grade))
    return results


def labeled_sheet(
    columns: list[str],
    rows: list[str],
    images: list[list[Image.Image]],
    output: Path,
    cell_size: int = 144,
) -> None:
    left = 214
    top = 54
    canvas = Image.new("RGB", (left + len(columns) * cell_size, top + len(rows) * cell_size), (23, 27, 33))
    draw = ImageDraw.Draw(canvas)
    for column, label in enumerate(columns):
        draw.text((left + column * cell_size + 6, 16), label, fill=(224, 232, 238))
    for row, label in enumerate(rows):
        draw.text((10, top + row * cell_size + 10), label, fill=(224, 232, 238))
        for column, image in enumerate(images[row]):
            thumb = ImageOps.fit(image.convert("RGB"), (cell_size - 8, cell_size - 8), method=LANCZOS)
            canvas.paste(thumb, (left + column * cell_size + 4, top + row * cell_size + 4))
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output, format="PNG", optimize=True)


def build_contact_sheets(
    sources: dict[str, Image.Image],
    particle_frames: dict[str, list[Image.Image]],
    static_frames: dict[str, Image.Image],
    props: dict[str, dict[str, Image.Image]],
    grades: list[tuple[str, Image.Image]],
) -> None:
    labeled_sheet(
        ["source"],
        REGIONS,
        [[sources[region]] for region in REGIONS],
        CONTACT_ROOT / "regional_material_sources.png",
    )

    phase_rows: list[list[Image.Image]] = []
    for region in REGIONS:
        phase_rows.append(
            [Image.open(PROCESSED_ROOT / f"materials/{region}_phase_{phase}_diff.png") for phase in range(1, 7)]
        )
    labeled_sheet(
        ["1 dimming", "2 crop shock", "3 hard freeze", "4 black harvest", "5 ash winter", "6 terminal"],
        REGIONS,
        phase_rows,
        CONTACT_ROOT / "regional_ground_phase_matrix.png",
    )

    labeled_sheet(
        ["dead vegetation", "frozen water", "thaw / flood"],
        REGIONS,
        [[props[region][family] for family in ("dead_vegetation", "frozen_water", "thaw_flood")] for region in REGIONS],
        CONTACT_ROOT / "regional_prop_matrix.png",
    )

    labeled_sheet(
        ["frame 1", "frame 2", "frame 3", "frame 4"],
        list(PARTICLE_FAMILIES),
        [particle_frames[family] for family in PARTICLE_FAMILIES],
        CONTACT_ROOT / "particle_authored_frames.png",
    )

    labeled_sheet(
        ["static fallback"],
        list(PARTICLE_FAMILIES),
        [[static_frames[family]] for family in PARTICLE_FAMILIES],
        CONTACT_ROOT / "particle_static_fallbacks.png",
    )

    grade_background = Image.open(PROCESSED_ROOT / "materials/temperate_maritime_phase_1_diff.png").convert("RGBA")
    grade_composites = [Image.alpha_composite(grade_background, image.resize(grade_background.size, LANCZOS)) for _, image in grades]
    labeled_sheet(
        [name for name, _ in grades],
        ["grade"],
        [grade_composites],
        CONTACT_ROOT / "phase_and_recovery_grades.png",
        cell_size=156,
    )


def dds_probe(path: Path) -> dict[str, int | str]:
    payload = path.read_bytes()
    if payload[:4] != b"DDS " or len(payload) < 128:
        raise RuntimeError(f"Invalid DDS header: {path}")
    height = int.from_bytes(payload[12:16], "little")
    width = int.from_bytes(payload[16:20], "little")
    return {"path": path.relative_to(REPO_ROOT).as_posix(), "width": width, "height": height, "bytes": len(payload)}


def build_report() -> None:
    files: list[dict[str, int | str]] = []
    for root in (MODEL_ROOT, PARTICLE_ROOT, GRADE_ROOT):
        for path in sorted(root.glob("*.dds")):
            files.append(dds_probe(path))

    source_hashes = {}
    for path in sorted(SOURCE_ROOT.rglob("*.png")):
        source_hashes[path.relative_to(PACKAGE_ROOT).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()

    report = {
        "source_hashes_sha256": source_hashes,
        "dds": files,
        "counts": {
            "regional_classes": len(REGIONS),
            "regional_phase_albedos": len(REGIONS) * 6,
            "particle_families": len(PARTICLE_FAMILIES),
            "authored_particle_frames": len(PARTICLE_FAMILIES) * 4,
            "regional_prop_materials": len(REGIONS) * 3,
            "grade_plates": 8,
            "dds_files": len(files),
        },
    }
    (PACKAGE_ROOT / "build_report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    ensure_dirs()
    sources = build_regional_materials()
    particle_frames, static_frames = build_particles()
    props = build_props()
    grades = build_grades()
    build_contact_sheets(sources, particle_frames, static_frames, props, grades)
    build_report()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
