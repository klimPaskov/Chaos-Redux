from __future__ import annotations

import csv
import hashlib
import math
import os
import re
import shutil
import struct
import subprocess
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


SUBSET = Path(__file__).resolve().parent
PACKAGE = SUBSET.parents[1]
ROOT = SUBSET.parents[6]
SOURCE = PACKAGE / "source_png"
PROCESSED = PACKAGE / "processed_png"
RUNTIME = ROOT / "gfx" / "interface" / "decisions" / "014_cannibalism"
GFX_FILE = ROOT / "interface" / "014_cannibalism.gfx"
ALPHA_WORK = SUBSET / "_alpha_work"
CONVERTER = ROOT / ".tools" / "convert_to_dds.py"
CHROMA_HELPER = Path(
    "C:/Users/klimp/.codex/skills/.system/imagegen/scripts/remove_chroma_key.py"
)
APPROVED_TEXCONV = Path(
    "C:/Users/klimp/AppData/Local/Temp/chaos_redux_tools/texconv-may2026.exe"
)
APPROVED_TEXCONV_SHA256 = (
    "dcfdec10244e02cf5037fba089c55fb7e1326b1c8181742d77d15fa5cb5eef06"
)

ASSETS = [
    (10, "cannibalism_unified_rapid_consumption", "Burn Through the Near State", "larder", "An open wartime furnace mouth devouring two blood-streaked ration sacks, orange flame and gore bursting from one bold black silhouette."),
    (11, "cannibalism_unified_managed_consumption", "Rotate a Managed Feeding District", "larder", "A circular steel butcher carousel with three anonymous wrapped meat bundles turning around one greasy blood-coated crank."),
    (12, "cannibalism_unified_mobile_consumption", "Move the Prisoner Trains", "larder", "A huge 1940s prison railcar wheel fused to a barred wagon door, wrapped in bloody transport chain and caked with track mud."),
    (13, "cannibalism_unified_battlefield_consumption", "Process the Battlefield Yield", "larder", "A torn wartime field stretcher tipping anonymous bloody remains into a compact recovery hopper, with one dented helmet beside it."),
    (14, "cannibalism_unified_larder_mission", "Keep the Continental Ledger Moving", "larder", "A blood-smeared blank ledger book strapped to a toothed conveyor wheel, its pages whipping while the mechanism keeps turning."),
    (15, "cannibalism_unified_establish_air_program_foundation", "Establish an Air Program Foundation", "war_machine", "A battered 1940s aircraft propeller freshly bolted to a bloodied industrial anvil, with one rivet hammer and no complete aircraft."),
    (16, "cannibalism_unified_create_cannibal_legion", "Create a Cannibal Legion", "war_machine", "An empty 1940s steel infantry helmet rising above a blood-filled mess tin, backed by one worn rifle bayonet and torn webbing."),
    (17, "cannibalism_unified_surge_cannibal_legion", "Surge a Cannibal Legion", "war_machine", "Three battered 1940s infantry helmets bursting upward from a blood-soaked deployment crate under a snapped chain."),
    (18, "cannibalism_unified_recruit_island_reavers", "Recruit Island Reavers", "war_machine", "A rusted naval grappling hook driven through a torn wartime life ring, tangled with bloody rope and a chipped boarding knife."),
    (19, "cannibalism_unified_recruit_siege_eaters", "Recruit Siege Eaters", "war_machine", "A massive sledgehammer crushing a concrete bunker ration hatch, broken masonry and dark blood spraying from the impact."),
    (20, "cannibalism_unified_recruit_march_predation_column", "Recruit a March Predation Column", "war_machine", "A mud-caked 1940s truck tire wrapped in butcher chain, driven forward over a blood-stamped marching boot sole."),
    (22, "cannibalism_unified_raise_bone_guard", "Raise a Bone Guard", "war_machine", "A 1940s steel helmet reinforced with anonymous jawbones, crossed with one chipped bayonet and one blood-darkened long bone."),
    (23, "cannibalism_unified_launch_continental_hunt", "Launch a Continental Hunt", "war_machine", "Wartime field binoculars trapped in a wide butcher snare, crossed by a bloodied bayonet that points aggressively forward."),
    (24, "cannibalism_unified_collapse_enemy_front", "Collapse an Enemy Front", "war_machine", "A sandbag barricade collapsing under one brutal tank-tread segment, snapping barbed wire and crushing an abandoned bloodied helmet."),
]


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalized_hash(image: Image.Image) -> str:
    rgba = image.convert("RGBA")
    payload = struct.pack("<II", rgba.width, rgba.height) + rgba.tobytes()
    return hashlib.sha256(payload).hexdigest()


def validate_tools() -> None:
    if not (ROOT / "AGENTS.md").exists():
        raise RuntimeError(f"Repository root resolution failed: {ROOT}")
    if not CHROMA_HELPER.exists():
        raise FileNotFoundError(CHROMA_HELPER)
    if not CONVERTER.exists():
        raise FileNotFoundError(CONVERTER)
    if not APPROVED_TEXCONV.exists():
        raise FileNotFoundError(APPROVED_TEXCONV)
    digest = file_sha256(APPROVED_TEXCONV)
    if digest != APPROVED_TEXCONV_SHA256:
        raise RuntimeError(
            f"Approved texconv hash mismatch: {digest}; expected {APPROVED_TEXCONV_SHA256}"
        )


def remove_chroma(name: str) -> Path:
    source = SOURCE / f"decision_{name}_source.png"
    output = ALPHA_WORK / f"decision_{name}_alpha.png"
    subprocess.run(
        [
            "python",
            str(CHROMA_HELPER),
            "--input",
            str(source),
            "--out",
            str(output),
            "--auto-key",
            "border",
            "--soft-matte",
            "--transparent-threshold",
            "12",
            "--opaque-threshold",
            "220",
            "--despill",
            "--force",
        ],
        check=True,
    )
    return output


def trim_alpha(image: Image.Image) -> Image.Image:
    rgba = image.convert("RGBA")
    bbox = rgba.getchannel("A").point(lambda value: 255 if value > 8 else 0).getbbox()
    if bbox is None:
        raise RuntimeError("Imagegen source has no visible pixels after chroma removal")
    return rgba.crop(bbox)


def fit_alpha(source: Path) -> Image.Image:
    size = (32, 32)
    padding = 2
    outline_width = 0.85
    shadow_offset = 0.75
    scale = 4
    image = trim_alpha(Image.open(source))
    maximum = (
        max(1, (size[0] - padding * 2 - math.ceil(outline_width * 2)) * scale),
        max(1, (size[1] - padding * 2 - math.ceil(outline_width * 2)) * scale),
    )
    ratio = min(maximum[0] / image.width, maximum[1] / image.height)
    resized = image.resize(
        (max(1, round(image.width * ratio)), max(1, round(image.height * ratio))),
        Image.Resampling.LANCZOS,
    )
    high_size = (size[0] * scale, size[1] * scale)
    x = (high_size[0] - resized.width) // 2
    y = (high_size[1] - resized.height) // 2
    subject_alpha = Image.new("L", high_size, 0)
    subject_alpha.paste(resized.getchannel("A"), (x, y))

    shadow_alpha = subject_alpha.filter(ImageFilter.GaussianBlur(radius=2.0 * scale))
    shadow_alpha = shadow_alpha.point(lambda value: round(value * 0.42))
    shifted_shadow = Image.new("L", high_size, 0)
    shifted_shadow.paste(
        shadow_alpha,
        (round(shadow_offset * scale), round(shadow_offset * scale)),
    )
    shadow = Image.new("RGBA", high_size, (0, 0, 0, 0))
    shadow.putalpha(shifted_shadow)

    outline_pixels = max(1, round(outline_width * scale))
    outline_alpha = subject_alpha.filter(ImageFilter.MaxFilter(outline_pixels * 2 + 1))
    outline_alpha = outline_alpha.point(lambda value: round(value * 0.9))
    outline = Image.new("RGBA", high_size, (21, 16, 13, 255))
    outline.putalpha(outline_alpha)

    subject = Image.new("RGBA", high_size, (0, 0, 0, 0))
    subject.alpha_composite(resized, (x, y))
    canvas = Image.alpha_composite(shadow, outline)
    canvas = Image.alpha_composite(canvas, subject)
    final = canvas.resize(size, Image.Resampling.LANCZOS)
    alpha = final.getchannel("A")
    draw = ImageDraw.Draw(alpha)
    draw.rectangle((0, 0, 31, 0), fill=0)
    draw.rectangle((0, 31, 31, 31), fill=0)
    draw.rectangle((0, 0, 0, 31), fill=0)
    draw.rectangle((31, 0, 31, 31), fill=0)
    final.putalpha(alpha)
    return final


def convert_to_dds(png: Path, dds: Path) -> None:
    env = os.environ.copy()
    env["TEXCONV_PATH"] = str(APPROVED_TEXCONV)
    env.pop("TEXCONV_EXE", None)
    env.pop("TEXCONV_DOCKER_IMAGE", None)
    subprocess.run(
        [
            "python",
            str(CONVERTER),
            "--input",
            str(png),
            "--output",
            str(dds),
            "--width",
            "32",
            "--height",
            "32",
        ],
        check=True,
        env=env,
    )


def dds_metadata(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    if len(data) < 128 or data[:4] != b"DDS ":
        raise RuntimeError(f"Invalid DDS: {path}")
    height = struct.unpack_from("<I", data, 12)[0]
    width = struct.unpack_from("<I", data, 16)[0]
    mip_count = struct.unpack_from("<I", data, 28)[0]
    pixel_flags = struct.unpack_from("<I", data, 80)[0]
    fourcc = struct.unpack_from("<I", data, 84)[0]
    bit_count = struct.unpack_from("<I", data, 88)[0]
    masks = tuple(struct.unpack_from("<I", data, offset)[0] for offset in (92, 96, 100, 104))
    payload = data[128:]
    expected_payload = width * height * 4
    if len(payload) != expected_payload:
        raise RuntimeError(
            f"Unexpected DDS payload for {path}: {len(payload)}; expected {expected_payload}"
        )
    return {
        "width": width,
        "height": height,
        "mip_count": mip_count,
        "pixel_flags": pixel_flags,
        "fourcc": fourcc,
        "bit_count": bit_count,
        "masks": masks,
        "payload": payload,
        "file_size": len(data),
    }


def decode_dds(path: Path) -> Image.Image:
    meta = dds_metadata(path)
    return Image.frombytes(
        "RGBA",
        (int(meta["width"]), int(meta["height"])),
        meta["payload"],
        "raw",
        "BGRA",
    )


def visible_key_green(image: Image.Image) -> int:
    return sum(
        1
        for red, green, blue, alpha in image.convert("RGBA").getdata()
        if alpha > 10 and green > 190 and green > red * 1.55 and green > blue * 1.55
    )


def validate_registered_mapping(asset_id: str, runtime: Path) -> str:
    sprite = f"GFX_decision_{asset_id}"
    texture = runtime.relative_to(ROOT).as_posix()
    text = GFX_FILE.read_text(encoding="utf-8-sig")
    pattern = re.compile(
        r'spriteType\s*=\s*\{\s*name\s*=\s*"'
        + re.escape(sprite)
        + r'"\s*texturefile\s*=\s*"'
        + re.escape(texture)
        + r'"\s*\}'
    )
    matches = pattern.findall(text)
    if len(matches) != 1:
        raise RuntimeError(
            f"Expected one registered mapping for {sprite} -> {texture}; found {len(matches)}"
        )
    return texture


def checker(size: tuple[int, int], tile: int) -> Image.Image:
    image = Image.new("RGBA", size, (70, 70, 70, 255))
    draw = ImageDraw.Draw(image)
    for y in range(0, size[1], tile):
        for x in range(0, size[0], tile):
            color = (70, 70, 70, 255) if ((x // tile) + (y // tile)) % 2 == 0 else (122, 122, 122, 255)
            draw.rectangle((x, y, min(x + tile - 1, size[0] - 1), min(y + tile - 1, size[1] - 1)), fill=color)
    return image


def font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    candidates = [
        Path("C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf"),
        Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


def make_contact(decoded: dict[str, Image.Image]) -> None:
    columns = 4
    cell_w, cell_h = 360, 250
    header_h = 58
    rows = math.ceil(len(ASSETS) / columns)
    sheet = Image.new("RGB", (columns * cell_w, header_h + rows * cell_h), (25, 27, 30))
    draw = ImageDraw.Draw(sheet)
    draw.text((18, 12), "Event 014 unified decision icons — rows 10–24", font=font(24, True), fill=(242, 238, 226))
    draw.text((20, 39), "Left: processed/decoded pixels at 4×. Right: native 32×32 DDS on checker.", font=font(12), fill=(184, 190, 198))
    for index, (row_number, asset_id, title, _category, _brief) in enumerate(ASSETS):
        col, row = index % columns, index // columns
        x0 = col * cell_w
        y0 = header_h + row * cell_h
        draw.rectangle((x0 + 4, y0 + 4, x0 + cell_w - 5, y0 + cell_h - 5), outline=(84, 89, 96), width=1)
        image = decoded[asset_id]
        enlarged = image.resize((128, 128), Image.Resampling.NEAREST)
        large = checker((158, 158), 12)
        large.alpha_composite(enlarged, (15, 15))
        sheet.paste(large.convert("RGB"), (x0 + 12, y0 + 10))
        native = checker((110, 158), 8)
        native.alpha_composite(image, ((110 - 32) // 2, (158 - 32) // 2))
        sheet.paste(native.convert("RGB"), (x0 + 182, y0 + 10))
        draw.text((x0 + 300, y0 + 72), "32×32", font=font(12, True), fill=(198, 203, 208))
        draw.text((x0 + 12, y0 + 174), f"Row {row_number}: {title}", font=font(14, True), fill=(240, 236, 224))
        y = y0 + 195
        for line in textwrap.wrap(asset_id, width=44)[:2]:
            draw.text((x0 + 12, y), line, font=font(11), fill=(188, 194, 201))
            y += 14
    output = SUBSET / "rows_10_24_contact_sheet.png"
    sheet.save(output, optimize=True)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def write_manifest(runtime_texture_count: int, comparison_count: int) -> None:
    lines = [
        "# Event 014 Unified Decision Icons — Rows 10–24",
        "",
        "- Scope: the 14 current ledger rows in the original rows 10-24 subset.",
        "- Source mode: `$imagegen` built-in generation, one independent call per asset.",
        "- Common prompt: `docs/assets/014_cannibalism/static_icons_imagegen/unified_decisions/prompts/common_prompt.md`.",
        "- Processing: official chroma-key removal, alpha trim, 32×32 centered fit with 2 px padding and restrained dark outline/drop shadow.",
        "- Runtime format: one-mip uncompressed 32-bit BGRA/B8G8R8A8-style DDS.",
        "- DDS backend: approved DirectXTex texconv May 2026 build.",
        f"- Backend SHA-256: `{APPROVED_TEXCONV_SHA256.upper()}`.",
        "- Reference review: the skill's named decision reference folder was absent; the surviving vanilla-derived decision reference sheet and existing Event 014 decision-icon contact sheet were inspected under the skill's missing-folder rule.",
        f"- Runtime hash comparison surface at validation: {runtime_texture_count} Event 014 decision-folder textures total; every owned icon was compared against {comparison_count} non-owned textures.",
        "- Contact sheet: `rows_10_24_contact_sheet.png`.",
        "- Detailed validation: `validation.tsv` and `runtime_hash_ledger.tsv`.",
        "",
        "| Row | Decision id | Category | Subject brief | Source PNG | Processed PNG | Runtime DDS | Registered sprite | Status |",
        "|---:|---|---|---|---|---|---|---|---|",
    ]
    for row_number, asset_id, _title, category, brief in ASSETS:
        source = SOURCE / f"decision_{asset_id}_source.png"
        processed = PROCESSED / f"decision_{asset_id}.png"
        runtime = RUNTIME / f"decision_{asset_id}.dds"
        lines.append(
            f"| {row_number} | `{asset_id}` | `{category}` | {brief} | `{rel(source)}` | `{rel(processed)}` | `{rel(runtime)}` | `GFX_decision_{asset_id}` | complete |"
        )
    lines.extend(
        [
            "",
            "## Completion",
            "",
            "All 14 current source PNGs, processed PNGs, and runtime DDS files exist at their exact registered paths. DDS decoding reproduces the processed PNG pixels exactly. Normalized RGBA hashes are unique inside the subset and against every non-owned Event 014 decision texture present during validation.",
            "",
            "No fallback, placeholder, reused source, cross-type reuse, transform-only substitute, simplification, omission, or blocker was used.",
            "",
        ]
    )
    (SUBSET / "manifest.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    validate_tools()
    PROCESSED.mkdir(parents=True, exist_ok=True)
    RUNTIME.mkdir(parents=True, exist_ok=True)
    if ALPHA_WORK.exists():
        shutil.rmtree(ALPHA_WORK)
    ALPHA_WORK.mkdir(parents=True)

    source_paths = [SOURCE / f"decision_{asset_id}_source.png" for _, asset_id, _, _, _ in ASSETS]
    missing = [str(path) for path in source_paths if not path.exists()]
    if missing:
        raise RuntimeError(f"Missing owned source paths: {missing}")
    source_hashes = [file_sha256(path) for path in source_paths]
    if len(source_hashes) != len(set(source_hashes)):
        raise RuntimeError("Owned generated source files are not byte-unique")

    processed_images: dict[str, Image.Image] = {}
    for _row_number, asset_id, _title, _category, _brief in ASSETS:
        alpha_path = remove_chroma(asset_id)
        image = fit_alpha(alpha_path)
        png = PROCESSED / f"decision_{asset_id}.png"
        dds = RUNTIME / f"decision_{asset_id}.dds"
        image.save(png, optimize=True)
        convert_to_dds(png, dds)
        processed_images[asset_id] = image

    expected_masks = (0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000)
    validation_rows: list[list[str]] = []
    decoded: dict[str, Image.Image] = {}
    owned_hash_to_id: dict[str, str] = {}
    for row_number, asset_id, title, category, _brief in ASSETS:
        source = SOURCE / f"decision_{asset_id}_source.png"
        png = PROCESSED / f"decision_{asset_id}.png"
        dds = RUNTIME / f"decision_{asset_id}.dds"
        image = Image.open(png).convert("RGBA")
        if image.size != (32, 32):
            raise RuntimeError(f"Wrong processed dimensions for {asset_id}: {image.size}")
        alpha = image.getchannel("A")
        alpha_min, alpha_max = alpha.getextrema()
        corners = tuple(alpha.getpixel(point) for point in ((0, 0), (31, 0), (0, 31), (31, 31)))
        transparent = sum(1 for value in alpha.getdata() if value == 0)
        partial = sum(1 for value in alpha.getdata() if 0 < value < 255)
        opaque = sum(1 for value in alpha.getdata() if value == 255)
        key_green = visible_key_green(image)
        bbox = alpha.point(lambda value: 255 if value > 8 else 0).getbbox()
        if alpha_min != 0 or alpha_max != 255 or corners != (0, 0, 0, 0):
            raise RuntimeError(f"Invalid icon alpha for {asset_id}: extrema={(alpha_min, alpha_max)} corners={corners}")
        if transparent == 0 or opaque == 0 or bbox is None:
            raise RuntimeError(f"Invalid visible/transparent coverage for {asset_id}")
        if key_green:
            raise RuntimeError(f"Visible key green remains in {asset_id}: {key_green} pixels")
        digest = normalized_hash(image)
        if digest in owned_hash_to_id:
            raise RuntimeError(f"Owned normalized-pixel collision: {asset_id} duplicates {owned_hash_to_id[digest]}")
        owned_hash_to_id[digest] = asset_id

        meta = dds_metadata(dds)
        if (meta["width"], meta["height"]) != (32, 32):
            raise RuntimeError(f"Wrong DDS dimensions for {asset_id}: {(meta['width'], meta['height'])}")
        if meta["mip_count"] not in (0, 1):
            raise RuntimeError(f"Unexpected DDS mip count for {asset_id}: {meta['mip_count']}")
        if meta["pixel_flags"] != 0x41 or meta["fourcc"] != 0 or meta["bit_count"] != 32 or meta["masks"] != expected_masks:
            raise RuntimeError(f"DDS is not uncompressed BGRA8 for {asset_id}: {meta}")
        decoded_image = decode_dds(dds)
        if decoded_image.tobytes() != image.tobytes():
            raise RuntimeError(f"DDS decode differs from processed PNG: {asset_id}")
        decoded[asset_id] = decoded_image
        registered_texture = validate_registered_mapping(asset_id, dds)
        validation_rows.append(
            [
                str(row_number), asset_id, title, category, "32x32", str(alpha_min), str(alpha_max),
                str(transparent), str(partial), str(opaque), "/".join(map(str, corners)),
                str(key_green), str(bbox), file_sha256(source), digest, file_sha256(dds),
                str(meta["file_size"]), str(meta["mip_count"]), "BGRA8_uncompressed",
                f"GFX_decision_{asset_id}", registered_texture, "complete",
            ]
        )

    owned_paths = {RUNTIME / f"decision_{asset_id}.dds" for _, asset_id, _, _, _ in ASSETS}
    runtime_rows: list[list[str]] = []
    runtime_digest_to_paths: dict[str, list[Path]] = {}
    runtime_files = sorted(RUNTIME.glob("*.dds"), key=lambda path: path.name.lower())
    for path in runtime_files:
        image = decode_dds(path)
        digest = normalized_hash(image)
        runtime_digest_to_paths.setdefault(digest, []).append(path)
        runtime_rows.append(
            [
                path.name,
                "owned_rows_10_24" if path in owned_paths else "existing_other",
                f"{image.width}x{image.height}",
                digest,
                file_sha256(path),
                "decoded",
            ]
        )
    for digest, asset_id in owned_hash_to_id.items():
        collisions = [path for path in runtime_digest_to_paths.get(digest, []) if path != RUNTIME / f"decision_{asset_id}.dds"]
        if collisions:
            raise RuntimeError(f"Runtime normalized-pixel collision for {asset_id}: {collisions}")

    with (SUBSET / "validation.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow([
            "row", "decision_id", "title", "category", "dimensions", "alpha_min", "alpha_max",
            "transparent_pixels", "partial_alpha_pixels", "opaque_pixels", "corner_alpha_tl_tr_bl_br",
            "visible_key_green_pixels", "alpha_bbox", "source_sha256", "normalized_rgba_sha256",
            "runtime_dds_sha256", "dds_file_size", "dds_mip_count", "dds_format", "registered_sprite",
            "registered_texture_path", "status",
        ])
        writer.writerows(validation_rows)
    with (SUBSET / "runtime_hash_ledger.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["runtime_texture", "ownership", "dimensions", "normalized_rgba_sha256", "file_sha256", "decode_status"])
        writer.writerows(runtime_rows)

    make_contact(decoded)
    comparison_count = len(runtime_files) - len(owned_paths)
    write_manifest(len(runtime_files), comparison_count)
    shutil.rmtree(ALPHA_WORK)
    print(
        f"Processed and validated {len(ASSETS)} owned icons; compared against "
        f"{comparison_count} non-owned Event 014 decision textures."
    )


if __name__ == "__main__":
    main()
