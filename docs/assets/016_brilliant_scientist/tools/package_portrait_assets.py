#!/usr/bin/env python3
"""Package Event 016 generated Kruger portraits and authored animation frames."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


REPO = Path(__file__).resolve().parents[4]
ASSET_ROOT = REPO / "docs/assets/016_brilliant_scientist"
CONVERTER = REPO / ".agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py"
FRAME_SIZE = (156, 210)

ROUTES = {
    "clone": {"frames": 10, "fps": 5, "pause_ms": 400},
    "machine": {"frames": 10, "fps": 5, "pause_ms": 300},
    "temporal": {"frames": 12, "fps": 4, "pause_ms": 500},
    "xenobiological": {"frames": 10, "fps": 4, "pause_ms": 500},
    "alien_revealed": {"frames": 10, "fps": 4, "pause_ms": 500},
    "synthesis": {"frames": 12, "fps": 4, "pause_ms": 400},
}


def cover(im: Image.Image, size: tuple[int, int]) -> Image.Image:
    """Return a centered, aspect-preserving cover crop."""
    im = im.convert("RGBA")
    scale = max(size[0] / im.width, size[1] / im.height)
    resized = im.resize(
        (round(im.width * scale), round(im.height * scale)),
        Image.Resampling.LANCZOS,
    )
    left = (resized.width - size[0]) // 2
    top = (resized.height - size[1]) // 2
    return resized.crop((left, top, left + size[0], top + size[1]))


def convert_to_dds(src: Path, dst: Path, width: int, height: int) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            sys.executable,
            "-B",
            str(CONVERTER),
            "--input",
            str(src),
            "--output",
            str(dst),
            "--width",
            str(width),
            "--height",
            str(height),
        ],
        cwd=REPO,
        check=True,
    )


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def font(size: int) -> ImageFont.ImageFont:
    candidates = [
        Path("C:/Windows/Fonts/arial.ttf"),
        Path("C:/Windows/Fonts/segoeui.ttf"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


def package_static_portraits(records: list[dict[str, object]]) -> None:
    src_root = ASSET_ROOT / "source_png/portraits/generated_static"
    preview_root = ASSET_ROOT / "processed_png/portraits"
    runtime_root = REPO / "gfx/leaders/KRG"
    preview_root.mkdir(parents=True, exist_ok=True)
    runtime_root.mkdir(parents=True, exist_ok=True)

    for src in sorted(src_root.glob("leader_doctor_warren_kruger_stage_*_source.png")):
        stem = src.stem.removesuffix("_source")
        png = preview_root / f"{stem}.png"
        dds = runtime_root / f"{stem}.dds"
        with Image.open(src) as opened:
            processed = cover(opened, FRAME_SIZE)
        processed.save(png)
        convert_to_dds(png, dds, *FRAME_SIZE)
        records.append(
            {
                "kind": "static_leader",
                "source": src.relative_to(REPO).as_posix(),
                "processed_png": png.relative_to(REPO).as_posix(),
                "runtime_dds": dds.relative_to(REPO).as_posix(),
                "dimensions": list(FRAME_SIZE),
                "source_method": "separate ImageGen portrait master; centered cover crop",
                "sha256_png": sha256(png),
                "sha256_dds": sha256(dds),
            }
        )


def make_contact_sheet(
    route: str,
    frames: list[Image.Image],
    static: Image.Image,
    output: Path,
) -> None:
    cols = 5
    cell_w, cell_h = 176, 246
    title_h = 54
    count = len(frames) + 1
    rows = (count + cols - 1) // cols
    sheet = Image.new("RGB", (cols * cell_w, title_h + rows * cell_h), (28, 30, 32))
    draw = ImageDraw.Draw(sheet)
    title_font = font(24)
    label_font = font(16)
    draw.text((16, 12), f"Event 016 — Stage IV {route.replace('_', ' ').title()}", fill=(235, 228, 210), font=title_font)
    items = [(f"frame {i:03d}", frame) for i, frame in enumerate(frames)]
    items.append(("static fallback", static))
    for index, (label, image) in enumerate(items):
        col = index % cols
        row = index // cols
        x = col * cell_w + 10
        y = title_h + row * cell_h + 4
        sheet.paste(image.convert("RGB"), (x, y))
        draw.rectangle((x - 1, y - 1, x + FRAME_SIZE[0], y + FRAME_SIZE[1]), outline=(185, 164, 120), width=1)
        draw.text((x, y + FRAME_SIZE[1] + 6), label, fill=(225, 225, 225), font=label_font)
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output)


def package_animations(records: list[dict[str, object]]) -> None:
    processed_root = ASSET_ROOT / "processed_png/animations"
    preview_root = ASSET_ROOT / "previews"
    contact_root = ASSET_ROOT / "contact_sheets"
    runtime_root = REPO / "gfx/interface/leader_frames/016_brilliant_scientist"
    for directory in (processed_root, preview_root, contact_root, runtime_root):
        directory.mkdir(parents=True, exist_ok=True)

    for route, config in ROUTES.items():
        package = ASSET_ROOT / "animations" / f"doctor_warren_kruger_stage_4_{route}"
        source_root = package / "source_frames"
        frame_root = package / "processed_frames"
        frame_root.mkdir(parents=True, exist_ok=True)
        prefix = f"doctor_warren_kruger_stage_4_{route}"
        frames: list[Image.Image] = []
        source_paths: list[str] = []
        processed_paths: list[str] = []

        for index in range(int(config["frames"])):
            src = source_root / f"{prefix}_frame_{index:03d}_source.png"
            if not src.exists():
                raise FileNotFoundError(f"Missing authored source frame: {src}")
            dst = frame_root / f"{prefix}_frame_{index:03d}.png"
            with Image.open(src) as opened:
                frame = cover(opened, FRAME_SIZE)
            frame.save(dst)
            frames.append(frame)
            source_paths.append(src.relative_to(REPO).as_posix())
            processed_paths.append(dst.relative_to(REPO).as_posix())

        sheet = Image.new("RGBA", (FRAME_SIZE[0] * len(frames), FRAME_SIZE[1]), (0, 0, 0, 0))
        for index, frame in enumerate(frames):
            sheet.paste(frame, (index * FRAME_SIZE[0], 0))
        sheet_png = processed_root / f"{prefix}_sheet.png"
        sheet.save(sheet_png)
        sheet_dds = runtime_root / f"{prefix}_sheet.dds"
        convert_to_dds(sheet_png, sheet_dds, sheet.width, sheet.height)

        static_png = ASSET_ROOT / "processed_png/portraits" / f"leader_{prefix}.png"
        if not static_png.exists():
            raise FileNotFoundError(f"Missing packaged static fallback: {static_png}")
        with Image.open(static_png) as opened:
            static = opened.convert("RGBA")

        gif = preview_root / f"{prefix}_preview.gif"
        durations = [round(1000 / int(config["fps"]))] * len(frames)
        durations[-1] += int(config["pause_ms"])
        frames[0].convert("P", palette=Image.Palette.ADAPTIVE).save(
            gif,
            save_all=True,
            append_images=[f.convert("P", palette=Image.Palette.ADAPTIVE) for f in frames[1:]],
            duration=durations,
            loop=0,
            disposal=2,
        )

        contact = contact_root / f"{prefix}_contact_sheet.png"
        make_contact_sheet(route, frames, static, contact)
        records.append(
            {
                "kind": "animated_leader",
                "route": route,
                "source_frames": source_paths,
                "processed_frames": processed_paths,
                "frame_count": len(frames),
                "frame_dimensions": list(FRAME_SIZE),
                "sheet_dimensions": [sheet.width, sheet.height],
                "fps": int(config["fps"]),
                "loop_pause_ms": int(config["pause_ms"]),
                "sheet_png": sheet_png.relative_to(REPO).as_posix(),
                "runtime_dds": sheet_dds.relative_to(REPO).as_posix(),
                "static_fallback_png": static_png.relative_to(REPO).as_posix(),
                "static_fallback_dds": (REPO / "gfx/leaders/KRG" / f"leader_{prefix}.dds").relative_to(REPO).as_posix(),
                "preview_gif": gif.relative_to(REPO).as_posix(),
                "contact_sheet": contact.relative_to(REPO).as_posix(),
                "source_method": "each source frame separately generated/drawn with route-specific pose and apparatus state",
                "sha256_sheet_png": sha256(sheet_png),
                "sha256_sheet_dds": sha256(sheet_dds),
            }
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--record",
        default=str(ASSET_ROOT / "package_records/portrait_animation_package.json"),
    )
    args = parser.parse_args()
    records: list[dict[str, object]] = []
    package_static_portraits(records)
    package_animations(records)
    record = Path(args.record)
    record.parent.mkdir(parents=True, exist_ok=True)
    record.write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")
    print(f"Packaged {sum(r['kind'] == 'static_leader' for r in records)} static leaders")
    print(f"Packaged {sum(r['kind'] == 'animated_leader' for r in records)} animation families")
    print(record)


if __name__ == "__main__":
    main()
