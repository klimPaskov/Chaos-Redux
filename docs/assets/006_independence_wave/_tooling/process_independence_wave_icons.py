#!/usr/bin/env python3
"""Build Event 006 static icon PNG/DDS deliverables and review sheets.

This script only reads the icon-family source folders owned by the Event 006
icon tranche. It intentionally ignores event pictures, super-event scenes,
flags, portraits, scripted-GUI animations, and other agents' deliverables.
"""

from __future__ import annotations

import hashlib
import json
import math
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont, ImageOps


REPO_ROOT = Path(__file__).resolve().parents[4]
PACKAGE_ROOT = REPO_ROOT / "docs" / "assets" / "006_independence_wave"
SOURCE_ROOT = PACKAGE_ROOT / "source_png"
PROCESSED_ROOT = PACKAGE_ROOT / "processed_png"
CONTACT_ROOT = PACKAGE_ROOT / "contact_sheets"
CHROMA_HELPER = (
    Path.home()
    / ".codex"
    / "skills"
    / ".system"
    / "imagegen"
    / "scripts"
    / "remove_chroma_key.py"
)
DDS_CONVERTER = REPO_ROOT / ".tools" / "convert_to_dds.py"
ACHIEVEMENT_OVERLAY = (
    REPO_ROOT
    / ".agents"
    / "skills"
    / "chaos-redux-event-assets"
    / "assets"
    / "achievements"
    / "overlay.png"
)


@dataclass(frozen=True)
class Family:
    name: str
    width: int
    height: int
    max_width: int
    max_height: int
    runtime_dir: Path


FAMILIES = {
    "focuses": Family(
        "focuses",
        94,
        86,
        90,
        82,
        REPO_ROOT / "gfx" / "interface" / "goals" / "006_independence_wave",
    ),
    "ideas": Family(
        "ideas",
        64,
        64,
        60,
        60,
        REPO_ROOT / "gfx" / "interface" / "ideas" / "006_independence_wave",
    ),
    "decisions": Family(
        "decisions",
        32,
        32,
        30,
        30,
        REPO_ROOT / "gfx" / "interface" / "decisions" / "006_independence_wave",
    ),
    "achievements": Family(
        "achievements",
        64,
        64,
        60,
        60,
        REPO_ROOT / "gfx" / "achievements",
    ),
}


def run(command: list[str]) -> None:
    completed = subprocess.run(command, check=False, text=True, capture_output=True)
    if completed.returncode != 0:
        raise RuntimeError(
            f"Command failed ({completed.returncode}): {' '.join(command)}\n"
            f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}"
        )


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def alpha_bbox(image: Image.Image) -> tuple[int, int, int, int]:
    bbox = image.getchannel("A").getbbox()
    if bbox is None:
        raise ValueError("Chroma removal produced a fully transparent image")
    return bbox


def fit_icon(keyed: Image.Image, family: Family) -> Image.Image:
    cropped = keyed.convert("RGBA").crop(alpha_bbox(keyed))
    scale = min(family.max_width / cropped.width, family.max_height / cropped.height)
    resized_size = (
        max(1, round(cropped.width * scale)),
        max(1, round(cropped.height * scale)),
    )
    subject = cropped.resize(resized_size, Image.Resampling.LANCZOS)

    canvas = Image.new("RGBA", (family.width, family.height), (0, 0, 0, 0))
    x = (family.width - subject.width) // 2
    y = (family.height - subject.height) // 2

    alpha = subject.getchannel("A")
    outline = alpha.filter(ImageFilter.MaxFilter(3))
    outline_only = ImageChops.subtract(outline, alpha)
    outline_layer = Image.new("RGBA", subject.size, (14, 12, 10, 0))
    outline_layer.putalpha(outline_only.point(lambda value: min(220, value)))
    canvas.alpha_composite(outline_layer, (x, y))

    shadow = Image.new("RGBA", subject.size, (0, 0, 0, 0))
    shadow_alpha = alpha.filter(ImageFilter.GaussianBlur(0.55)).point(
        lambda value: round(value * 0.45)
    )
    shadow.putalpha(shadow_alpha)
    canvas.alpha_composite(shadow, (x + 1, y + 1))
    canvas.alpha_composite(subject, (x, y))
    return canvas


def remove_chroma(source: Path, destination: Path) -> None:
    run(
        [
            sys.executable,
            str(CHROMA_HELPER),
            "--input",
            str(source),
            "--out",
            str(destination),
            "--auto-key",
            "border",
            "--soft-matte",
            "--transparent-threshold",
            "12",
            "--opaque-threshold",
            "220",
            "--edge-contract",
            "1",
            "--despill",
            "--force",
        ]
    )


def convert_to_dds(png: Path, dds: Path, width: int, height: int) -> None:
    dds.parent.mkdir(parents=True, exist_ok=True)
    run(
        [
            sys.executable,
            str(DDS_CONVERTER),
            "--input",
            str(png),
            "--output",
            str(dds),
            "--width",
            str(width),
            "--height",
            str(height),
        ]
    )


def process_source(source: Path, family: Family, temporary_root: Path) -> tuple[Path, Path]:
    stem = source.stem.removesuffix("_source")
    processed_dir = PROCESSED_ROOT / family.name
    processed_dir.mkdir(parents=True, exist_ok=True)
    family.runtime_dir.mkdir(parents=True, exist_ok=True)

    keyed = temporary_root / f"{stem}_keyed.png"
    remove_chroma(source, keyed)
    with Image.open(keyed) as keyed_image:
        final = fit_icon(keyed_image, family)
        processed = processed_dir / f"{stem}.png"
        final.save(processed, "PNG", optimize=True)

    runtime = family.runtime_dir / f"{stem}.dds"
    convert_to_dds(processed, runtime, family.width, family.height)
    return processed, runtime


def derive_achievement_states(base_png: Path, family: Family) -> list[tuple[Path, Path]]:
    with Image.open(base_png) as image:
        base = image.convert("RGBA")
    alpha = base.getchannel("A")
    grey_rgb = ImageOps.grayscale(base.convert("RGB")).convert("RGB")
    grey = Image.merge("RGBA", (*grey_rgb.split(), alpha))

    grey_png = base_png.with_name(f"{base_png.stem}_grey.png")
    grey.save(grey_png, "PNG", optimize=True)

    with Image.open(ACHIEVEMENT_OVERLAY) as overlay_source:
        overlay = overlay_source.convert("RGBA").resize(
            (family.width, family.height), Image.Resampling.LANCZOS
        )
    not_eligible = grey.copy()
    not_eligible.alpha_composite(overlay)
    not_eligible_png = base_png.with_name(f"{base_png.stem}_not_eligible.png")
    not_eligible.save(not_eligible_png, "PNG", optimize=True)

    outputs: list[tuple[Path, Path]] = []
    for png in (grey_png, not_eligible_png):
        dds = family.runtime_dir / f"{png.stem}.dds"
        convert_to_dds(png, dds, family.width, family.height)
        outputs.append((png, dds))
    return outputs


def checker(size: tuple[int, int], cell: int = 8) -> Image.Image:
    image = Image.new("RGBA", size, (68, 72, 78, 255))
    draw = ImageDraw.Draw(image)
    for y in range(0, size[1], cell):
        for x in range(0, size[0], cell):
            color = (103, 108, 116, 255) if (x // cell + y // cell) % 2 else (62, 66, 72, 255)
            draw.rectangle((x, y, x + cell - 1, y + cell - 1), fill=color)
    return image


def load_font(size: int) -> ImageFont.ImageFont:
    candidates = [
        Path("C:/Windows/Fonts/arial.ttf"),
        Path("C:/Windows/Fonts/segoeui.ttf"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


def make_sheet(
    title: str,
    files: list[Path],
    output: Path,
    scale: int,
    columns: int,
) -> None:
    if not files:
        return
    font = load_font(15)
    label_font = load_font(11)
    opened: list[tuple[Path, Image.Image]] = []
    for file in files:
        with Image.open(file) as source:
            opened.append((file, source.convert("RGBA")))
    thumb_w = max(image.width for _, image in opened) * scale
    thumb_h = max(image.height for _, image in opened) * scale
    cell_w = max(190, thumb_w + 20)
    cell_h = thumb_h + 46
    rows = math.ceil(len(opened) / columns)
    sheet = Image.new("RGBA", (columns * cell_w, 42 + rows * cell_h), (30, 33, 38, 255))
    draw = ImageDraw.Draw(sheet)
    draw.text((12, 11), title, font=font, fill=(238, 232, 212, 255))
    for index, (path, image) in enumerate(opened):
        col = index % columns
        row = index // columns
        left = col * cell_w
        top = 42 + row * cell_h
        board = checker((thumb_w, thumb_h), max(4, scale * 2))
        enlarged = image.resize((image.width * scale, image.height * scale), Image.Resampling.NEAREST)
        x = (thumb_w - enlarged.width) // 2
        y = (thumb_h - enlarged.height) // 2
        board.alpha_composite(enlarged, (x, y))
        sheet.alpha_composite(board, (left + (cell_w - thumb_w) // 2, top))
        label = path.stem.replace("independence_wave_", "").replace("_", " ")
        draw.text((left + 8, top + thumb_h + 7), label[:28], font=label_font, fill=(224, 226, 230, 255))
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.convert("RGB").save(output, "PNG", optimize=True)


def validate_dds(path: Path, expected_width: int, expected_height: int) -> dict[str, object]:
    payload = path.read_bytes()
    if payload[:4] != b"DDS ":
        raise ValueError(f"Missing DDS magic: {path}")
    header_size = int.from_bytes(payload[4:8], "little")
    height = int.from_bytes(payload[12:16], "little")
    width = int.from_bytes(payload[16:20], "little")
    pixel_format_size = int.from_bytes(payload[76:80], "little")
    bit_count = int.from_bytes(payload[88:92], "little")
    if (header_size, pixel_format_size, bit_count) != (124, 32, 32):
        raise ValueError(f"Unexpected DDS header values: {path}")
    if (width, height) != (expected_width, expected_height):
        raise ValueError(f"Unexpected DDS dimensions: {path}: {width}x{height}")
    expected_length = 128 + width * height * 4
    if len(payload) != expected_length:
        raise ValueError(f"Unexpected DDS payload length: {path}: {len(payload)} != {expected_length}")
    alpha = payload[128 + 3 :: 4]
    return {
        "path": path.relative_to(REPO_ROOT).as_posix(),
        "width": width,
        "height": height,
        "bytes": len(payload),
        "alpha_min": min(alpha),
        "alpha_max": max(alpha),
        "sha256": hashlib.sha256(payload).hexdigest(),
    }


def make_dds_decoded_sheet(runtime_files: list[Path]) -> None:
    decoded_dir = PACKAGE_ROOT / "_tooling" / "dds_decoded_review"
    if decoded_dir.exists():
        shutil.rmtree(decoded_dir)
    decoded_dir.mkdir(parents=True)
    decoded: list[Path] = []
    for dds in runtime_files:
        try:
            with Image.open(dds) as image:
                png = decoded_dir / f"{dds.stem}.png"
                image.convert("RGBA").save(png, "PNG", optimize=True)
                decoded.append(png)
        except Exception as error:  # Pillow DDS support varies by build.
            raise RuntimeError(f"Unable to decode final DDS {dds}: {error}") from error
    make_sheet(
        "Event 006 — final DDS decode review",
        sorted(decoded),
        CONTACT_ROOT / "006_icon_dds_decoded_contact_sheet.png",
        scale=3,
        columns=6,
    )


def main() -> None:
    missing_tools = [path for path in (CHROMA_HELPER, DDS_CONVERTER, ACHIEVEMENT_OVERLAY) if not path.exists()]
    if missing_tools:
        raise FileNotFoundError("Missing required tool/asset: " + ", ".join(map(str, missing_tools)))

    results: dict[str, list[dict[str, str]]] = {name: [] for name in FAMILIES}
    runtime_files: list[Path] = []
    with tempfile.TemporaryDirectory(prefix="chaosx_006_icons_") as temporary:
        temporary_root = Path(temporary)
        for family_name, family in FAMILIES.items():
            source_dir = SOURCE_ROOT / family_name
            if not source_dir.exists():
                continue
            for source in sorted(source_dir.glob("*_source.png")):
                processed, runtime = process_source(source, family, temporary_root)
                runtime_files.append(runtime)
                results[family_name].append(
                    {
                        "source": source.relative_to(REPO_ROOT).as_posix(),
                        "source_sha256": sha256(source),
                        "processed": processed.relative_to(REPO_ROOT).as_posix(),
                        "processed_sha256": sha256(processed),
                        "runtime": runtime.relative_to(REPO_ROOT).as_posix(),
                        "runtime_sha256": sha256(runtime),
                    }
                )
                if family_name == "achievements":
                    for derived_png, derived_dds in derive_achievement_states(processed, family):
                        runtime_files.append(derived_dds)
                        results[family_name].append(
                            {
                                "source": source.relative_to(REPO_ROOT).as_posix(),
                                "source_sha256": sha256(source),
                                "processed": derived_png.relative_to(REPO_ROOT).as_posix(),
                                "processed_sha256": sha256(derived_png),
                                "runtime": derived_dds.relative_to(REPO_ROOT).as_posix(),
                                "runtime_sha256": sha256(derived_dds),
                            }
                        )

    for family_name, family in FAMILIES.items():
        files = sorted((PROCESSED_ROOT / family_name).glob("*.png"))
        if not files:
            continue
        scale = 5 if family_name == "decisions" else 3
        columns = 4 if family_name in {"focuses", "ideas"} else 5
        make_sheet(
            f"Event 006 — {family_name} target-size review",
            files,
            CONTACT_ROOT / f"006_icon_{family_name}_contact_sheet.png",
            scale=scale,
            columns=columns,
        )

    audits: list[dict[str, object]] = []
    for runtime in sorted(runtime_files):
        family = next(
            value for value in FAMILIES.values() if runtime.is_relative_to(value.runtime_dir)
        )
        audits.append(validate_dds(runtime, family.width, family.height))
    make_dds_decoded_sheet(sorted(runtime_files))

    report = {
        "families": results,
        "dds_audit": audits,
    }
    report_path = PACKAGE_ROOT / "_tooling" / "icon_build_report.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    counts = {name: len(entries) for name, entries in results.items()}
    print(json.dumps({"processed_entries": counts, "dds_files": len(audits)}, indent=2))


if __name__ == "__main__":
    main()
