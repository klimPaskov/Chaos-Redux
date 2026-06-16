#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageOps


def resize_base(source: Path, dest: Path, size: int = 64) -> None:
    img = Image.open(source).convert("RGBA")
    img = ImageOps.fit(img, (size, size), Image.Resampling.LANCZOS)
    dest.parent.mkdir(parents=True, exist_ok=True)
    img.save(dest)


def make_grey(source: Path, dest: Path) -> None:
    img = Image.open(source).convert("RGBA")
    rgb = img.convert("RGB")
    grey = ImageOps.grayscale(rgb).convert("RGBA")
    grey = ImageEnhance.Contrast(grey).enhance(1.15)
    base = Image.blend(grey, Image.new("RGBA", grey.size, (142, 142, 142, 255)), 0.18)
    dest.parent.mkdir(parents=True, exist_ok=True)
    base.save(dest)


def make_not_eligible(source: Path, dest: Path) -> None:
    img = Image.open(source).convert("RGBA")
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle((8, 8, 56, 56), radius=6, outline=(150, 0, 0, 255), width=4)
    draw.line((14, 50, 50, 14), fill=(170, 0, 0, 255), width=6)
    img = img.filter(ImageFilter.UnsharpMask(radius=1, percent=120, threshold=3))
    dest.parent.mkdir(parents=True, exist_ok=True)
    img.save(dest)


def make_contact_sheet(inputs: list[Path], dest: Path, thumb_size: int = 80, cols: int = 4) -> None:
    images = [Image.open(path).convert("RGBA") for path in inputs]
    rows = math.ceil(len(images) / cols)
    sheet = Image.new("RGBA", (cols * thumb_size, rows * thumb_size), (24, 24, 24, 255))
    for idx, img in enumerate(images):
        img = ImageOps.contain(img, (thumb_size - 8, thumb_size - 8), Image.Resampling.LANCZOS)
        x = (idx % cols) * thumb_size + (thumb_size - img.width) // 2
        y = (idx // cols) * thumb_size + (thumb_size - img.height) // 2
        sheet.alpha_composite(img, (x, y))
    dest.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(dest)


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)

    base = sub.add_parser("base")
    base.add_argument("--source", required=True, type=Path)
    base.add_argument("--dest", required=True, type=Path)

    grey = sub.add_parser("grey")
    grey.add_argument("--source", required=True, type=Path)
    grey.add_argument("--dest", required=True, type=Path)

    ne = sub.add_parser("not-eligible")
    ne.add_argument("--source", required=True, type=Path)
    ne.add_argument("--dest", required=True, type=Path)

    sheet = sub.add_parser("sheet")
    sheet.add_argument("--dest", required=True, type=Path)
    sheet.add_argument("inputs", nargs="+", type=Path)
    sheet.add_argument("--thumb-size", type=int, default=80)
    sheet.add_argument("--cols", type=int, default=4)

    args = parser.parse_args()
    if args.cmd == "base":
        resize_base(args.source, args.dest)
    elif args.cmd == "grey":
        make_grey(args.source, args.dest)
    elif args.cmd == "not-eligible":
        make_not_eligible(args.source, args.dest)
    else:
        make_contact_sheet(args.inputs, args.dest, args.thumb_size, args.cols)


if __name__ == "__main__":
    main()
