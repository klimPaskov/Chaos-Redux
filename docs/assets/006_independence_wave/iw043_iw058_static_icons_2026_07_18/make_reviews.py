from __future__ import annotations

import hashlib
import json
import struct
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[3]


def font(size: int):
    for p in (Path("C:/Windows/Fonts/arial.ttf"), Path("C:/Windows/Fonts/segoeui.ttf")):
        if p.exists():
            return ImageFont.truetype(str(p), size)
    return ImageFont.load_default()


def checker(size: tuple[int, int], cell: int = 8) -> Image.Image:
    board = Image.new("RGBA", size, (62, 66, 72, 255))
    draw = ImageDraw.Draw(board)
    for y in range(0, size[1], cell):
        for x in range(0, size[0], cell):
            if ((x // cell) + (y // cell)) % 2:
                draw.rectangle((x, y, x + cell - 1, y + cell - 1), fill=(103, 108, 116, 255))
    return board


def sheet(family: str, scale: int, output: Path) -> None:
    files = sorted((ROOT / "processed_png" / family).glob("*.png"))
    if not files:
        return
    items = []
    for p in files:
        with Image.open(p) as im:
            items.append((p, im.convert("RGBA")))
    cols = 5 if family in {"decisions", "ideas"} else 3
    label = font(11)
    title = font(16)
    maxw = max(i.width for _, i in items) * scale
    maxh = max(i.height for _, i in items) * scale
    cw, ch = max(190, maxw + 20), maxh + 44
    rows = (len(items) + cols - 1) // cols
    out = Image.new("RGBA", (cw * cols, 38 + ch * rows), (30, 33, 38, 255))
    d = ImageDraw.Draw(out)
    d.text((10, 9), f"Event 006 IW-043 / IW-058 — {family} {'native' if scale == 1 else f'{scale}x'} review", fill=(238, 232, 212, 255), font=title)
    for n, (p, im) in enumerate(items):
        left, top = (n % cols) * cw, 38 + (n // cols) * ch
        board = checker((maxw, maxh), max(4, scale * 2))
        enlarged = im.resize((im.width * scale, im.height * scale), Image.Resampling.NEAREST)
        board.alpha_composite(enlarged, ((maxw - enlarged.width) // 2, (maxh - enlarged.height) // 2))
        out.alpha_composite(board, (left + (cw - maxw) // 2, top))
        d.text((left + 8, top + maxh + 6), p.stem[:29], fill=(224, 226, 230, 255), font=label)
    output.parent.mkdir(parents=True, exist_ok=True)
    out.convert("RGB").save(output, "PNG", optimize=True)


def dds_audit(path: Path, png: Path) -> dict[str, object]:
    payload = path.read_bytes()
    if payload[:4] != b"DDS ":
        raise ValueError(f"bad magic: {path}")
    height = struct.unpack_from("<I", payload, 12)[0]
    width = struct.unpack_from("<I", payload, 16)[0]
    pf_size, pf_flags = struct.unpack_from("<II", payload, 76)
    bitcount = struct.unpack_from("<I", payload, 88)[0]
    masks = struct.unpack_from("<IIII", payload, 92)
    caps = struct.unpack_from("<I", payload, 108)[0]
    header = struct.unpack_from("<I", payload, 4)[0]
    expected = 128 + width * height * 4
    if (header, pf_size, pf_flags, bitcount, masks, caps) != (124, 32, 65, 32, (0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000), 0x1000):
        raise ValueError(f"bad header fields: {path}")
    if len(payload) != expected:
        raise ValueError(f"bad length: {path}")
    alpha = payload[131::4]
    with Image.open(png) as im:
        rgba = im.convert("RGBA")
        if (rgba.width, rgba.height) != (width, height):
            raise ValueError(f"dimension mismatch: {path}")
        # Converter stores BGRA; compare decoded channels with processed PNG pixels.
        raw = payload[128:]
        decoded = bytearray()
        for i in range(0, len(raw), 4):
            b, g, r, a = raw[i:i+4]
            decoded.extend((r, g, b, a))
        if bytes(decoded) != rgba.tobytes():
            raise ValueError(f"pixel mismatch: {path}")
    return {"runtime": path.relative_to(REPO).as_posix(), "processed": png.relative_to(REPO).as_posix(), "width": width, "height": height, "bytes": len(payload), "alpha_min": min(alpha), "alpha_max": max(alpha), "sha256": hashlib.sha256(payload).hexdigest(), "pixel_exact": True}


def main() -> None:
    sheet("decision_categories", 1, ROOT / "review/native/decision_categories_native.png")
    sheet("decisions", 1, ROOT / "review/native/decisions_native.png")
    sheet("ideas", 1, ROOT / "review/native/ideas_native.png")
    sheet("achievements", 1, ROOT / "review/native/achievements_native.png")
    sheet("decision_categories", 4, ROOT / "review/enlarged/decision_categories_4x.png")
    sheet("decisions", 5, ROOT / "review/enlarged/decisions_5x.png")
    sheet("ideas", 3, ROOT / "review/enlarged/ideas_3x.png")
    sheet("achievements", 4, ROOT / "review/enlarged/achievements_4x.png")
    audits = []
    for png in sorted((ROOT / "processed_png").rglob("*.png")):
        if png.parent.name == "achievements":
            dds = REPO / "gfx/achievements" / f"{png.stem}.dds"
        elif png.parent.name == "ideas":
            dds = REPO / "gfx/interface/ideas/006_independence_wave/volga_assyria" / f"{png.stem}.dds"
        else:
            dds = REPO / "gfx/interface/decisions/006_independence_wave/volga_assyria" / f"{png.stem}.dds"
        audits.append(dds_audit(dds, png))
    (ROOT / "validation/dds_audit.json").write_text(json.dumps(audits, indent=2) + "\n", encoding="utf-8")
    # Keep one auditable hash ledger for the source, processed, package DDS,
    # and installed runtime DDS artifacts. Exclude generated scripts/reviews
    # so the ledger remains stable when a contact sheet is regenerated.
    hash_paths = []
    hash_paths.extend(sorted((ROOT / "source_png").rglob("*.png")))
    hash_paths.extend(sorted((ROOT / "processed_png").rglob("*.png")))
    hash_paths.extend(sorted((ROOT / "final_dds").rglob("*.dds")))
    hash_paths.extend(sorted((REPO / "gfx/interface/decisions/006_independence_wave/volga_assyria").glob("*.dds")))
    hash_paths.extend(sorted((REPO / "gfx/interface/ideas/006_independence_wave/volga_assyria").glob("*.dds")))
    hash_paths.extend(sorted((REPO / "gfx/achievements").glob("chaosx_006_assyria_survives*.dds")))
    unique_paths = {p.resolve(): p for p in hash_paths}
    ledger = []
    for path in sorted(unique_paths.values(), key=lambda p: p.as_posix().lower()):
        ledger.append(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.relative_to(REPO).as_posix()}")
    (ROOT / "validation/hashes.sha256").write_text("\n".join(ledger) + "\n", encoding="utf-8")
    print(json.dumps({"audits": len(audits), "native_sheets": 4, "enlarged_sheets": 4}))


if __name__ == "__main__":
    main()
