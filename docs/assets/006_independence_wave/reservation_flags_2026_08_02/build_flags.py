"""Build the Event 006 dormant reservation-art flag ladders.

Each source is an official ImageGen result. Processing only center-crops the
generated flat flag to the HOI4 ratio, resizes the source geometry, and writes
opaque 32-bit BGRA bottom-origin TGAs. No gameplay or .gfx files are touched.
"""

from __future__ import annotations

import hashlib
import json
import shutil
import struct
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


PACKAGE_ROOT = Path(__file__).resolve().parent
MOD_ROOT = PACKAGE_ROOT.parents[3]
SOURCE_ROOT = PACKAGE_ROOT / "source_png"
PROCESSED_ROOT = PACKAGE_ROOT / "processed_png"
FINAL_ROOT = PACKAGE_ROOT / "final_tga"
CONTACT_ROOT = PACKAGE_ROOT / "contact_sheets"
PROMPT_ROOT = PACKAGE_ROOT / "prompts"
METADATA_ROOT = PACKAGE_ROOT / "metadata"

FLAG_SIZES = {
    "normal": (82, 52),
    "medium": (41, 26),
    "small": (10, 7),
}

PROMPTS = {
    "DJX": "Create one clean flat graphic flag design for fictional dormant API reservation tag DJX. This is reservation_art only, not a historical country and not playable statehood. Single horizontal 5:3 flag fills the canvas edge to edge, orthographic front view, no flagpole, no fabric, no folds, no waving, no shadows, no perspective, no gradients, no texture, no scene, no text, no letters, no watermark. Use a restrained desert palette of deep indigo, sand gold, and muted teal. Center a distinctive layered civic emblem: an abstract three-point desert star around a small caravan-ring motif, with balanced heraldic geometry and clear silhouette at tiny size. Flat vector-like screenprint, crisp edges, high contrast, intentional authored flag, no modern logos.",
    "DMX": "Create one clean flat graphic flag design for fictional dormant API reservation tag DMX, a Toubou/Teda-Daza reservation_art marker only, not a historical country, not statehood, not playable. Single horizontal 5:3 flag fills the canvas. Flat orthographic vector-like design, crisp heraldic edges, no fabric, folds, waving, pole, shadow, perspective, gradient, texture, scene, text, lettering, watermark. Palette charcoal blue, rust orange, pale turquoise, ivory. Center a distinctive layered emblem: two angular desert-dune arcs framing a small geometric well-ring and four balanced sun shards, abstract civic identity, readable at 10x7.",
    "DNX": "Create one clean flat graphic flag design for fictional dormant API reservation tag DNX, an Atlas/Kabyle-adjacent reservation_art marker only, not a historical country, not statehood, not playable. Single horizontal 5:3 flag fills the canvas. Flat orthographic vector-like design, crisp heraldic edges, no fabric, folds, waving, pole, shadow, perspective, gradient, texture, scene, text, lettering, watermark. Palette cobalt blue, terracotta, ivory, dark green. Center a layered mountain-chevron emblem with a small eight-lobed rosette and stepped ridge bars, abstract civic identity, readable at 10x7.",
    "ENX": "Create one clean flat graphic flag design for fictional dormant API reservation tag ENX, a Maasai territorial reservation_art marker only, not a historical country, not statehood, not playable. Single horizontal 5:3 flag fills the canvas. Flat orthographic vector-like design, crisp heraldic edges, no fabric, folds, waving, pole, shadow, perspective, gradient, texture, scene, text, lettering, watermark. Palette deep maroon, black, ochre, cream, muted teal. Center a layered civic shield surrounded by a bead-like ring of simple dots and chevrons, abstract institutional identity with no literal weapons or people, readable at 10x7.",
    "EXX": "Create one clean flat graphic flag design for fictional dormant API reservation tag EXX, a Nama reservation_art marker only, not a historical country, not statehood, not playable. Single horizontal 5:3 flag fills the canvas. Flat orthographic vector-like design, crisp heraldic edges, no fabric, folds, waving, pole, shadow, perspective, gradient, texture, scene, text, lettering, watermark. Palette deep navy, copper, sage green, sand ivory. Center a layered desert-flower compass emblem over a clean horizon band and small geometric star points, abstract civic identity, readable at 10x7.",
    "EYX": "Create one clean flat graphic flag design for fictional dormant API reservation tag EYX, an Ovambo reservation_art marker only, not a historical country, not statehood, not playable. Single horizontal 5:3 flag fills the canvas. Flat orthographic vector-like design, crisp heraldic edges, no fabric, folds, waving, pole, shadow, perspective, gradient, texture, scene, text, lettering, watermark. Palette emerald green, white, ochre gold, charcoal. Center a layered civic emblem of braided river rectangles around a small sun-disc and four linked bars, abstract institutional identity, readable at 10x7.",
    "FPX": "Create one clean flat graphic flag design for fictional dormant API reservation tag FPX, a Naga reservation_art marker only, not a historical country, not statehood, not playable. Single horizontal 5:3 flag fills the canvas. Flat orthographic vector-like design, crisp heraldic edges, no fabric, folds, waving, pole, shadow, perspective, gradient, texture, scene, text, lettering, watermark. Palette crimson, forest green, ivory, black, muted amber. Center a distinctive layered woven-chevron emblem with an abstract arched ridge and small central lozenge, no literal weapons or people, readable at 10x7.",
    "GDX": "Create one clean flat graphic flag design for fictional dormant API reservation tag GDX, a Karen reservation_art marker only, not a historical country, not statehood, not playable. Single horizontal 5:3 flag fills the canvas. Flat orthographic vector-like design, crisp heraldic edges, no fabric, folds, waving, pole, shadow, perspective, gradient, texture, scene, text, lettering, watermark. Palette vermilion red, deep navy, cream, jade. Center a layered mountain-and-river glyph nested in a ring of nine small dots and stepped bands, abstract civic identity, readable at 10x7.",
    "GGX": "Create one clean flat graphic flag design for fictional dormant API reservation tag GGX, a Chin/Zo reservation_art marker only, not a historical country, not statehood, not playable. Single horizontal 5:3 flag fills the canvas. Flat orthographic vector-like design, crisp heraldic edges, no fabric, folds, waving, pole, shadow, perspective, gradient, texture, scene, text, lettering, watermark. Palette plum purple, slate blue, gold, ivory. Center a layered stacked-ridge emblem with a three-petal civic rosette and angular border bars, abstract institutional identity, readable at 10x7.",
    "GHX": "Create one clean flat graphic flag design for fictional dormant API reservation tag GHX, an Arakan/Rakhine reservation_art marker only, not a historical country, not statehood, not playable. Single horizontal 5:3 flag fills the canvas. Flat orthographic vector-like design, crisp heraldic edges, no fabric, folds, waving, pole, shadow, perspective, gradient, texture, scene, text, lettering, watermark. Palette sea teal, saffron gold, white, deep blue. Center a layered coastal wave-crown emblem around a compact roundel and three rising bars, abstract civic identity, readable at 10x7.",
    "GLX": "Create one clean flat graphic flag design for fictional dormant API reservation tag GLX, a Hmong reservation_art marker only, not a historical country, not statehood, not playable. Single horizontal 5:3 flag fills the canvas. Flat orthographic vector-like design, crisp heraldic edges, no fabric, folds, waving, pole, shadow, perspective, gradient, texture, scene, text, lettering, watermark. Palette midnight blue, moss green, copper, ivory. Center a layered spiral seed-pod geometry inside a stepped shield and narrow border bands, abstract civic identity, readable at 10x7.",
    "HHX": "Create one clean flat graphic flag design for fictional dormant API reservation tag HHX, a Pueblo member reservation_art marker only, not a historical country, not statehood, not playable. Single horizontal 5:3 flag fills the canvas. Flat orthographic vector-like design, crisp heraldic edges, no fabric, folds, waving, pole, shadow, perspective, gradient, texture, scene, text, lettering, watermark. Palette clay red, turquoise, cream, charcoal. Center a layered stepped-window emblem with a small sun-disc and nested masonry bars, abstract institutional identity without copying any historical flag, readable at 10x7.",
    "HMX": "Create one clean flat graphic flag design for fictional dormant API reservation tag HMX, a Garifuna coastal reservation_art marker only, not a historical country, not statehood, not playable. Single horizontal 5:3 flag fills the canvas. Flat orthographic vector-like design, crisp heraldic edges, no fabric, folds, waving, pole, shadow, perspective, gradient, texture, scene, text, lettering, watermark. Palette ocean blue, coral, cream, leaf green. Center a layered interlocking tide-arc emblem around a small coastal star and three horizon bars, abstract civic identity with no people or instruments, readable at 10x7.",
    "HQX": "Create one clean flat graphic flag design for fictional dormant API reservation tag HQX, a specific Quechua member reservation_art marker only, not a historical country, not statehood, not playable. Single horizontal 5:3 flag fills the canvas. Flat orthographic vector-like design, crisp heraldic edges, no fabric, folds, waving, pole, shadow, perspective, gradient, texture, scene, text, lettering, watermark. Palette rust red, maize gold, teal blue, ivory. Center a layered stepped mountain-lozenge emblem with a small starburst and nested terrace bars, abstract civic identity without copying a historical state flag, readable at 10x7.",
    "HTX": "Create one clean flat graphic flag design for fictional dormant API reservation tag HTX, a Gran Chaco member reservation_art marker only, not a historical country, not statehood, not playable. Single horizontal 5:3 flag fills the canvas. Flat orthographic vector-like design, crisp heraldic edges, no fabric, folds, waving, pole, shadow, perspective, gradient, texture, scene, text, lettering, watermark. Palette dry green, ochre, charcoal, cream. Center a layered branching thorn-tree emblem inside a compact sun-disc and angular border, abstract civic identity with no people or weapons, readable at 10x7.",
    "HWX": "Create one clean flat graphic flag design for fictional dormant API reservation tag HWX, an Amazonian river peoples reservation_art marker only, not a historical country, not statehood, not playable. Single horizontal 5:3 flag fills the canvas. Flat orthographic vector-like design, crisp heraldic edges, no fabric, folds, waving, pole, shadow, perspective, gradient, texture, scene, text, lettering, watermark. Palette rainforest green, river blue, amber, cream. Center a layered braided-tributary emblem around a seed-like shield and small river diamonds, abstract civic identity, readable at 10x7.",
    "HXX": "Create one clean flat graphic flag design for fictional dormant API reservation tag HXX, a historic maroon community reservation_art marker only, not a historical country, not statehood, not playable. Single horizontal 5:3 flag fills the canvas. Flat orthographic vector-like design, crisp heraldic edges, no fabric, folds, waving, pole, shadow, perspective, gradient, texture, scene, text, lettering, watermark. Palette dark umber, deep red, gold, forest green. Center a layered broken-chain-to-mountain-ring emblem with a small civic star and balanced border bars, abstract resistance memory marker without naming or claiming any maroon republic, readable at 10x7.",
}

GENERATED_PATHS = {
    "DJX": "C:/Users/klimp/.codex/generated_images/019fc3cc-64c4-7e41-9a9a-b1e91c45cba0/exec-8b75488f-10bc-44eb-859a-80a2a7cfe49a.png",
    "DMX": "C:/Users/klimp/.codex/generated_images/019fc3cc-64c4-7e41-9a9a-b1e91c45cba0/exec-aaee0b2c-eee4-41f1-af57-a5225439c39b.png",
    "DNX": "C:/Users/klimp/.codex/generated_images/019fc3cc-64c4-7e41-9a9a-b1e91c45cba0/exec-8bb1cac6-3393-4a25-8144-d0c468be0d24.png",
    "ENX": "C:/Users/klimp/.codex/generated_images/019fc3cc-64c4-7e41-9a9a-b1e91c45cba0/exec-7281877a-4f94-4c01-ac4d-168fbe876e7c.png",
    "EXX": "C:/Users/klimp/.codex/generated_images/019fc3cc-64c4-7e41-9a9a-b1e91c45cba0/exec-22971780-352a-4db5-9ea8-f623f00d97df.png",
    "EYX": "C:/Users/klimp/.codex/generated_images/019fc3cc-64c4-7e41-9a9a-b1e91c45cba0/exec-b753c81d-fa38-4ef6-b58d-d7009cd31c3f.png",
    "FPX": "C:/Users/klimp/.codex/generated_images/019fc3cc-64c4-7e41-9a9a-b1e91c45cba0/exec-1366dbd2-b28d-4ee5-876e-eddc9fc682f5.png",
    "GDX": "C:/Users/klimp/.codex/generated_images/019fc3cc-64c4-7e41-9a9a-b1e91c45cba0/exec-176a546b-6cd2-4a0a-a80e-d41c2e197940.png",
    "GGX": "C:/Users/klimp/.codex/generated_images/019fc3cc-64c4-7e41-9a9a-b1e91c45cba0/exec-19ee7b05-78f7-4465-9352-243041b6ad4f.png",
    "GHX": "C:/Users/klimp/.codex/generated_images/019fc3cc-64c4-7e41-9a9a-b1e91c45cba0/exec-657cee82-9fda-4e8c-8901-1b05ee47e3bc.png",
    "GLX": "C:/Users/klimp/.codex/generated_images/019fc3cc-64c4-7e41-9a9a-b1e91c45cba0/exec-6ffe8187-a413-4cad-aed9-a78bc2dbca21.png",
    "HHX": "C:/Users/klimp/.codex/generated_images/019fc3cc-64c4-7e41-9a9a-b1e91c45cba0/exec-99117167-d17f-4117-a0eb-966bb270c7bc.png",
    "HMX": "C:/Users/klimp/.codex/generated_images/019fc3cc-64c4-7e41-9a9a-b1e91c45cba0/exec-dcc6bb67-9914-4f42-94e7-dff5a8c4aeb0.png",
    "HQX": "C:/Users/klimp/.codex/generated_images/019fc3cc-64c4-7e41-9a9a-b1e91c45cba0/exec-6c8f1725-eb22-4f1f-98c2-b715d798a129.png",
    "HTX": "C:/Users/klimp/.codex/generated_images/019fc3cc-64c4-7e41-9a9a-b1e91c45cba0/exec-5b3b6f36-6ba9-4b08-b21b-64ca579a6c3a.png",
    "HWX": "C:/Users/klimp/.codex/generated_images/019fc3cc-64c4-7e41-9a9a-b1e91c45cba0/exec-dc5e7ada-5564-448c-8c47-483ac8565d27.png",
    "HXX": "C:/Users/klimp/.codex/generated_images/019fc3cc-64c4-7e41-9a9a-b1e91c45cba0/exec-0b1a871a-613d-42e9-a4c9-2dc9d10f1e81.png",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def crop_to_flag(image: Image.Image) -> Image.Image:
    target_ratio = FLAG_SIZES["normal"][0] / FLAG_SIZES["normal"][1]
    width, height = image.size
    source_ratio = width / height
    if source_ratio > target_ratio:
        crop_width = round(height * target_ratio)
        left = (width - crop_width) // 2
        image = image.crop((left, 0, left + crop_width, height))
    elif source_ratio < target_ratio:
        crop_height = round(width / target_ratio)
        top = (height - crop_height) // 2
        image = image.crop((0, top, width, top + crop_height))
    return image.convert("RGBA")


def write_bottom_origin_tga(image: Image.Image, path: Path) -> None:
    rgba = image.convert("RGBA")
    width, height = rgba.size
    pixels = rgba.load()
    payload = bytearray()
    for y in range(height - 1, -1, -1):
        for x in range(width):
            red, green, blue, alpha = pixels[x, y]
            payload.extend((blue, green, red, alpha))
    header = struct.pack("<BBBHHBHHHHBB", 0, 0, 2, 0, 0, 0, 0, 0, width, height, 32, 8)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(header + payload)


def inspect_tga(path: Path, expected: tuple[int, int]) -> dict[str, object]:
    data = path.read_bytes()
    header = struct.unpack("<BBBHHBHHHHBB", data[:18])
    width, height, depth, descriptor = header[8:12]
    decoded = Image.open(path).convert("RGBA")
    checks = {
        "header_type_2": header[2] == 2,
        "dimensions": (width, height) == expected,
        "depth_32": depth == 32,
        "bottom_origin": descriptor & 0x20 == 0,
        "alpha_bits_8": descriptor & 0x0F == 8,
        "opaque_alpha": decoded.getchannel("A").getextrema() == (255, 255),
        "exact_file_size": len(data) == 18 + width * height * 4,
    }
    return {"width": width, "height": height, "descriptor": descriptor, "bytes": len(data), "sha256": sha256(path), "checks": checks, "valid": all(checks.values())}


def font(size: int) -> ImageFont.ImageFont:
    path = Path("C:/Windows/Fonts/arial.ttf")
    return ImageFont.truetype(str(path), size) if path.exists() else ImageFont.load_default()


def contact_sheet(rows: dict[str, dict[str, Image.Image]]) -> Path:
    columns = ("source", "master", "normal", "medium", "small")
    label_w, cell_w, cell_h = 250, 205, 142
    margin, title_h = 18, 54
    sheet = Image.new("RGB", (margin * 2 + label_w + cell_w * len(columns), title_h + cell_h * len(rows) + margin), (33, 36, 42))
    draw = ImageDraw.Draw(sheet)
    draw.text((margin, 14), "Event 006 dormant reservation_art flags — ImageGen source and HOI4 ladders", fill=(245, 245, 245), font=font(20))
    for index, column in enumerate(columns):
        draw.text((margin + label_w + index * cell_w + 8, 36), column, fill=(212, 215, 221), font=font(13))
    for row_index, (tag, images) in enumerate(rows.items()):
        top = title_h + row_index * cell_h
        draw.rectangle((margin, top, sheet.width - margin, top + cell_h - 3), fill=(45, 49, 57) if row_index % 2 == 0 else (39, 43, 50))
        draw.text((margin + 10, top + 56), f"{tag}  reservation_art", fill=(250, 250, 250), font=font(17))
        for col_index, key in enumerate(columns):
            image = images[key].convert("RGB")
            scale = min((cell_w - 18) / image.width, (cell_h - 20) / image.height)
            display = image.resize((max(1, round(image.width * scale)), max(1, round(image.height * scale))), Image.Resampling.NEAREST)
            x = margin + label_w + col_index * cell_w + (cell_w - display.width) // 2
            y = top + (cell_h - display.height) // 2
            sheet.paste(display, (x, y))
    path = CONTACT_ROOT / "reservation_flag_ladders_contact_sheet.png"
    sheet.save(path, optimize=True)
    return path


def main() -> None:
    for root in (PROCESSED_ROOT, FINAL_ROOT, CONTACT_ROOT, PROMPT_ROOT, METADATA_ROOT):
        root.mkdir(parents=True, exist_ok=True)
    validation: dict[str, object] = {"package": "006_independence_wave_reservation_flags_2026_08_02", "classification": "reservation_art", "status": "dormant_api_reservations", "runtime_wiring": "none", "format": {"normal": "82x52", "medium": "41x26", "small": "10x7", "tga": "uncompressed 32-bit BGRA, bottom-origin, opaque"}, "flags": {}}
    rows: dict[str, dict[str, Image.Image]] = {}
    for tag in PROMPTS:
        source_path = SOURCE_ROOT / f"{tag}_imagegen_source.png"
        source = crop_to_flag(Image.open(source_path))
        source_master = source.resize((820, 520), Image.Resampling.LANCZOS)
        master_path = PROCESSED_ROOT / f"{tag}_flat_master_820x520.png"
        source_master.save(master_path, optimize=True)
        prompt_path = PROMPT_ROOT / f"{tag}.txt"
        prompt_path.write_text(PROMPTS[tag] + "\n", encoding="utf-8")
        row = {"source": source, "master": source_master}
        spec: dict[str, object] = {"source": source_path.relative_to(MOD_ROOT).as_posix(), "source_sha256": sha256(source_path), "source_dimensions": list(Image.open(source_path).size), "source_mode": "imagegen", "generated_path": GENERATED_PATHS[tag], "prompt": PROMPTS[tag], "processed_master": master_path.relative_to(MOD_ROOT).as_posix(), "processed_master_sha256": sha256(master_path), "ladder": {}, "dormant": True, "playable": False, "statehood_claim": False}
        for name, dimensions in FLAG_SIZES.items():
            image = source_master.resize(dimensions, Image.Resampling.NEAREST if name == "small" else Image.Resampling.LANCZOS)
            png_path = PROCESSED_ROOT / name / f"{tag}.png"
            png_path.parent.mkdir(parents=True, exist_ok=True)
            image.save(png_path, optimize=True)
            runtime = MOD_ROOT / "gfx" / "flags" / (f"{tag}.tga" if name == "normal" else f"{name}/{tag}.tga")
            write_bottom_origin_tga(image, runtime)
            package_tga = FINAL_ROOT / f"{tag}_{name}_{dimensions[0]}x{dimensions[1]}.tga"
            shutil.copy2(runtime, package_tga)
            result = inspect_tga(runtime, dimensions)
            if Image.open(runtime).convert("RGBA").tobytes() != image.tobytes():
                raise RuntimeError(f"TGA round-trip mismatch: {runtime}")
            if not result["valid"]:
                raise RuntimeError(f"TGA validation failed: {runtime}")
            row[name] = Image.open(runtime).convert("RGBA")
            spec["ladder"][name] = {"dimensions": list(dimensions), "processed_png": png_path.relative_to(MOD_ROOT).as_posix(), "processed_png_sha256": sha256(png_path), "runtime_tga": runtime.relative_to(MOD_ROOT).as_posix(), "runtime_tga_sha256": sha256(runtime), "package_tga": package_tga.relative_to(MOD_ROOT).as_posix(), "package_tga_sha256": sha256(package_tga), "validation": result}
        validation["flags"][tag] = spec
        rows[tag] = row
    contact = contact_sheet(rows)
    validation["contact_sheet"] = contact.relative_to(MOD_ROOT).as_posix()
    validation["contact_sheet_sha256"] = sha256(contact)
    (METADATA_ROOT / "flag_validation.json").write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")
    hash_paths = [p for p in SOURCE_ROOT.glob("*.png")] + [p for p in PROCESSED_ROOT.rglob("*.png")] + [p for p in FINAL_ROOT.glob("*.tga")] + [contact]
    (METADATA_ROOT / "hashes.sha256").write_text("\n".join(f"{sha256(p)}  {p.relative_to(MOD_ROOT).as_posix()}" for p in sorted(hash_paths)) + "\n", encoding="utf-8")
    print(f"Built {len(PROMPTS) * len(FLAG_SIZES)} runtime TGA files; all_valid={all(item['valid'] for flag in validation['flags'].values() for item in (ladder['validation'] for ladder in flag['ladder'].values()))}")


if __name__ == "__main__":
    main()
