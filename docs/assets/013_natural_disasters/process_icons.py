#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image, ImageChops, ImageFilter, ImageOps


def remove_green_screen(img: Image.Image, key=(0, 255, 0), tolerance: int = 24) -> Image.Image:
    img = img.convert("RGBA")
    pixels = img.load()
    width, height = img.size
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            if abs(r - key[0]) <= tolerance and abs(g - key[1]) <= tolerance and abs(b - key[2]) <= tolerance:
                pixels[x, y] = (0, 0, 0, 0)
    return img


def trim_alpha(img: Image.Image, padding: int = 0) -> Image.Image:
    alpha = img.getchannel("A")
    bbox = alpha.getbbox()
    if not bbox:
        return img
    left, top, right, bottom = bbox
    left = max(0, left - padding)
    top = max(0, top - padding)
    right = min(img.width, right + padding)
    bottom = min(img.height, bottom + padding)
    return img.crop((left, top, right, bottom))


def fit_to_canvas(img: Image.Image, size: int, scale: float = 0.84, shadow: bool = True) -> Image.Image:
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    max_dim = int(size * scale)
    img.thumbnail((max_dim, max_dim), Image.Resampling.LANCZOS)
    if shadow:
        shadow_img = Image.new("RGBA", img.size, (0, 0, 0, 0))
        shadow_alpha = img.getchannel("A").filter(ImageFilter.GaussianBlur(1.2))
        shadow_img.putalpha(shadow_alpha)
        shadow_pos = ((size - img.width) // 2 + 1, (size - img.height) // 2 + 2)
        canvas.alpha_composite(shadow_img, shadow_pos)
    pos = ((size - img.width) // 2, (size - img.height) // 2)
    canvas.alpha_composite(img, pos)
    return canvas


def add_outline(img: Image.Image, size: int = 2) -> Image.Image:
    alpha = img.getchannel("A")
    expanded = alpha.filter(ImageFilter.MaxFilter(size * 2 + 1))
    outline = Image.new("RGBA", img.size, (0, 0, 0, 0))
    outline.putalpha(ImageChops.subtract(expanded, alpha))
    combined = Image.alpha_composite(outline, img)
    return combined


def process_icon(source: Path, dest: Path, size: int, scale: float) -> None:
    img = Image.open(source)
    img = remove_green_screen(img)
    img = trim_alpha(img, padding=4)
    img = add_outline(img, size=2 if size >= 48 else 1)
    img = fit_to_canvas(img, size=size, scale=scale)
    dest.parent.mkdir(parents=True, exist_ok=True)
    img.save(dest)


def make_contact_sheet(inputs: list[Path], dest: Path, thumb_size: int = 96, cols: int = 4) -> None:
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

    icon = sub.add_parser("icon")
    icon.add_argument("--source", required=True, type=Path)
    icon.add_argument("--dest", required=True, type=Path)
    icon.add_argument("--size", required=True, type=int)
    icon.add_argument("--scale", type=float, default=0.84)

    sheet = sub.add_parser("sheet")
    sheet.add_argument("--dest", required=True, type=Path)
    sheet.add_argument("inputs", nargs="+", type=Path)
    sheet.add_argument("--thumb-size", type=int, default=96)
    sheet.add_argument("--cols", type=int, default=4)

    args = parser.parse_args()
    if args.cmd == "icon":
        process_icon(args.source, args.dest, args.size, args.scale)
    else:
        make_contact_sheet(args.inputs, args.dest, args.thumb_size, args.cols)


if __name__ == "__main__":
    main()
