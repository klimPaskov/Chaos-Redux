#!/usr/bin/env python3
"""Process the Event 006 HBX/HAW Pacific focus-icon tranche."""

from __future__ import annotations

import hashlib
import json
import math
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[5]
PACKAGE = ROOT / "docs" / "assets" / "006_independence_wave" / "pacific_focus_icons_2026_07_18"
SOURCE_DIR = PACKAGE / "source_png" / "focuses"
PROCESSED_DIR = PACKAGE / "processed_png" / "focuses"
RUNTIME_DIR = ROOT / "gfx" / "interface" / "goals" / "006_independence_wave"
CONTACT_DIR = PACKAGE / "contact_sheets"
VALIDATION_DIR = PACKAGE / "validation"
CHROMA = Path.home() / ".codex" / "skills" / ".system" / "imagegen" / "scripts" / "remove_chroma_key.py"
CONVERTER = ROOT / ".agents" / "skills" / "chaos-redux-event-assets" / "tools" / "convert_to_dds.py"
WIDTH, HEIGHT = 94, 86
MAX_WIDTH, MAX_HEIGHT = 90, 82


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def run(command: list[str]) -> None:
    result = subprocess.run(command, check=False, text=True, capture_output=True)
    if result.returncode:
        raise RuntimeError(f"command failed: {' '.join(command)}\n{result.stdout}\n{result.stderr}")


def remove_chroma(source: Path, output: Path) -> None:
    run([
        sys.executable,
        str(CHROMA),
        "--input", str(source),
        "--out", str(output),
        "--auto-key", "border",
        "--soft-matte",
        "--transparent-threshold", "12",
        "--opaque-threshold", "220",
        "--edge-contract", "1",
        "--despill",
        "--force",
    ])


def fit_icon(keyed: Image.Image) -> Image.Image:
    rgba = keyed.convert("RGBA")
    bbox = rgba.getchannel("A").getbbox()
    if bbox is None:
        raise ValueError("source became fully transparent after chroma removal")
    subject = rgba.crop(bbox)
    scale = min(MAX_WIDTH / subject.width, MAX_HEIGHT / subject.height)
    size = (max(1, round(subject.width * scale)), max(1, round(subject.height * scale)))
    subject = subject.resize(size, Image.Resampling.LANCZOS)

    canvas = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    x = (WIDTH - subject.width) // 2
    y = (HEIGHT - subject.height) // 2
    alpha = subject.getchannel("A")
    outline = ImageChops.subtract(alpha.filter(ImageFilter.MaxFilter(3)), alpha)
    outline_layer = Image.new("RGBA", subject.size, (13, 15, 17, 0))
    outline_layer.putalpha(outline.point(lambda value: min(220, value)))
    canvas.alpha_composite(outline_layer, (x, y))
    shadow = Image.new("RGBA", subject.size, (0, 0, 0, 0))
    shadow.putalpha(alpha.filter(ImageFilter.GaussianBlur(0.55)).point(lambda value: round(value * 0.45)))
    canvas.alpha_composite(shadow, (x + 1, y + 1))
    canvas.alpha_composite(subject, (x, y))
    return canvas


def dds(path: Path) -> dict[str, object]:
    payload = path.read_bytes()
    if payload[:4] != b"DDS ":
        raise ValueError(f"missing DDS magic: {path}")
    width = int.from_bytes(payload[16:20], "little")
    height = int.from_bytes(payload[12:16], "little")
    pixel_format = {
        "size": int.from_bytes(payload[76:80], "little"),
        "flags": int.from_bytes(payload[80:84], "little"),
        "fourcc": int.from_bytes(payload[84:88], "little"),
        "bits": int.from_bytes(payload[88:92], "little"),
        "r_mask": int.from_bytes(payload[92:96], "little"),
        "g_mask": int.from_bytes(payload[96:100], "little"),
        "b_mask": int.from_bytes(payload[100:104], "little"),
        "a_mask": int.from_bytes(payload[104:108], "little"),
    }
    caps = int.from_bytes(payload[108:112], "little")
    alpha = payload[128 + 3::4]
    expected_header = {
        "header_size": int.from_bytes(payload[4:8], "little"),
        "width": width,
        "height": height,
        "pixel_format": pixel_format,
        "caps": caps,
        "bytes": len(payload),
    }
    if expected_header["header_size"] != 124 or (width, height) != (WIDTH, HEIGHT):
        raise ValueError(f"invalid DDS dimensions/header: {path}")
    if pixel_format != {
        "size": 32,
        "flags": 65,
        "fourcc": 0,
        "bits": 32,
        "r_mask": 0x00FF0000,
        "g_mask": 0x0000FF00,
        "b_mask": 0x000000FF,
        "a_mask": 0xFF000000,
    }:
        raise ValueError(f"invalid BGRA DDS pixel format: {path}")
    if caps & 0x1000 == 0 or len(payload) != 128 + WIDTH * HEIGHT * 4:
        raise ValueError(f"invalid DDS caps/length: {path}")
    return {
        "path": path.relative_to(ROOT).as_posix(),
        "width": width,
        "height": height,
        "bytes": len(payload),
        "alpha_min": min(alpha),
        "alpha_max": max(alpha),
        "header": expected_header,
        "sha256": sha256(path),
    }


def font(size: int) -> ImageFont.ImageFont:
    for candidate in (Path("C:/Windows/Fonts/arial.ttf"), Path("C:/Windows/Fonts/segoeui.ttf")):
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


def checker(size: tuple[int, int], cell: int = 8) -> Image.Image:
    board = Image.new("RGBA", size, (60, 64, 70, 255))
    draw = ImageDraw.Draw(board)
    for y in range(0, size[1], cell):
        for x in range(0, size[0], cell):
            if (x // cell + y // cell) % 2:
                draw.rectangle((x, y, x + cell - 1, y + cell - 1), fill=(100, 105, 112, 255))
    return board


def sheet(files: list[Path], output: Path, scale: int, title: str) -> None:
    opened: list[tuple[Path, Image.Image]] = []
    for path in files:
        with Image.open(path) as image:
            opened.append((path, image.convert("RGBA")))
    columns = 4
    thumb = (WIDTH * scale, HEIGHT * scale)
    cell_w, cell_h = max(250, thumb[0] + 24), thumb[1] + 44
    rows = math.ceil(len(opened) / columns)
    board = Image.new("RGBA", (columns * cell_w, 42 + rows * cell_h), (28, 31, 36, 255))
    draw = ImageDraw.Draw(board)
    draw.text((12, 10), title, fill=(240, 234, 215, 255), font=font(16))
    for index, (path, image) in enumerate(opened):
        col, row = index % columns, index // columns
        left, top = col * cell_w, 42 + row * cell_h
        checkerboard = checker(thumb, max(4, scale * 2))
        checkerboard.alpha_composite(image.resize(thumb, Image.Resampling.NEAREST))
        board.alpha_composite(checkerboard, (left + (cell_w - thumb[0]) // 2, top))
        label = path.stem.replace("goal_independence_wave_", "").replace("_source", "").replace("_", " ")
        draw.text((left + 8, top + thumb[1] + 7), label[:34], fill=(225, 226, 230, 255), font=font(11))
    output.parent.mkdir(parents=True, exist_ok=True)
    board.convert("RGB").save(output, "PNG", optimize=True)


def main() -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    RUNTIME_DIR.mkdir(parents=True, exist_ok=True)
    CONTACT_DIR.mkdir(parents=True, exist_ok=True)
    VALIDATION_DIR.mkdir(parents=True, exist_ok=True)
    sources = sorted(SOURCE_DIR.glob("*_source.png"))
    if len(sources) != 14:
        raise ValueError(f"expected 14 Pacific focus sources, found {len(sources)}")
    records: list[dict[str, object]] = []
    with tempfile.TemporaryDirectory(prefix="chaosx_006_pacific_focus_") as temporary:
        tmp = Path(temporary)
        for source in sources:
            stem = source.stem.removesuffix("_source")
            keyed = tmp / f"{stem}_keyed.png"
            remove_chroma(source, keyed)
            with Image.open(keyed) as image:
                final = fit_icon(image)
                processed = PROCESSED_DIR / f"{stem}.png"
                final.save(processed, "PNG", optimize=True)
            runtime = RUNTIME_DIR / f"{stem}.dds"
            run([sys.executable, str(CONVERTER), "--input", str(processed), "--output", str(runtime), "--width", str(WIDTH), "--height", str(HEIGHT)])
            with Image.open(processed) as png:
                corners = [png.getpixel(point)[3] for point in ((0, 0), (WIDTH - 1, 0), (0, HEIGHT - 1), (WIDTH - 1, HEIGHT - 1))]
            if any(corners):
                raise ValueError(f"transparent corners failed: {processed}")
            records.append({
                "sprite": f"GFX_{stem}",
                "source": source.relative_to(ROOT).as_posix(),
                "source_sha256": sha256(source),
                "processed": processed.relative_to(ROOT).as_posix(),
                "processed_sha256": sha256(processed),
                "runtime": runtime.relative_to(ROOT).as_posix(),
                "runtime_sha256": sha256(runtime),
                "dds": dds(runtime),
            })
    processed = sorted(PROCESSED_DIR.glob("*.png"))
    sheet(processed, CONTACT_DIR / "006_pacific_focus_icons_1x_contact_sheet.png", 1, "Event 006 — Pacific HBX + HAW focus icons — native 94x86")
    sheet(processed, CONTACT_DIR / "006_pacific_focus_icons_3x_contact_sheet.png", 3, "Event 006 — Pacific HBX + HAW focus icons — 3x review")
    source_files = sorted(SOURCE_DIR.glob("*_source.png"))
    sheet(source_files, CONTACT_DIR / "006_pacific_focus_icons_source_contact_sheet.png", 1, "Event 006 — ImageGen Pacific focus sources")
    payload = {
        "package": "006_independence_wave/pacific_focus_icons_2026_07_18",
        "source_mode": "built-in ImageGen with chroma-key removal",
        "target_size": "94x86",
        "references_inspected": ".agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/national_focus/contact_sheet.png",
        "records": records,
    }
    (VALIDATION_DIR / "validation.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    lines = []
    for record in records:
        lines.extend([
            f"{record['source_sha256']}  {record['source']}",
            f"{record['processed_sha256']}  {record['processed']}",
            f"{record['runtime_sha256']}  {record['runtime']}",
        ])
    (VALIDATION_DIR / "hashes.sha256").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"icons": len(records), "dds": len(records), "size": [WIDTH, HEIGHT]}))


if __name__ == "__main__":
    main()
