#!/usr/bin/env python3
"""Build the Event 006 IW-043/IW-058 national-focus icon package."""
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
PACKAGE = ROOT / "docs/assets/006_independence_wave/iw043_iw058_focus_icons_2026_07_18"
SOURCE = PACKAGE / "source_png/focuses"
PROCESSED = PACKAGE / "processed_png/focuses"
PROMPTS = PACKAGE / "prompts"
CONTACT = PACKAGE / "contact_sheets"
VALIDATION = PACKAGE / "validation"
REVIEW_NATIVE = PACKAGE / "review_native"
REVIEW_3X = PACKAGE / "review_3x"
RUNTIME = ROOT / "gfx/interface/goals/006_independence_wave/volga_assyria"
CHROMA = Path.home() / ".codex/skills/.system/imagegen/scripts/remove_chroma_key.py"
CONVERTER = ROOT / ".agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py"
W, H = 94, 86
MAX_W, MAX_H = 90, 82

PROMPT_TEXT = {
    "iw043_congress": "Original ornate painterly 1930s strategy-game emblem of a civic congress: open ledger on a wood lectern beneath distinct delegate medallions, drafting pen, bronze and deep teal, compact central silhouette, no text.",
    "iw043_navigation": "Original ornate painterly emblem of Volga navigation: sturdy river wheel and ferry bow cutting through stylized waves, tiny bridge silhouette, brass and steel with blue-green water highlights, no text.",
    "iw043_rights_charter": "Original ornate painterly emblem of a rights charter: rolled parchment around a balanced civic scale and four small seal dots, warm ivory paper, bronze scale, blue ribbon, no readable writing.",
    "iw043_muftiate_civic_courts": "Original ornate painterly emblem of religious and civic jurisdiction: domed civic courthouse beside a crescent-topped minaret silhouette, two linked seals at base, respectful non-exclusive symbolism, bronze, stone, muted turquoise.",
    "iw043_river_guard": "Original ornate painterly emblem of a civilian river guard: patrol boat prow with a shield and coiled rope, small river waves, restrained brass, dark green and blue steel, defensive civic tone.",
    "iw043_bolgar_constitution": "Original ornate painterly emblem of a modern constitutional heritage proclamation: stone Bolgar-style minaret and civic column joined by a parchment seal, small historical crescent accent, inclusive civic tone, bronze, sandstone, teal.",
    "iw043_federal_chamber": "Original ornate painterly emblem of an equal federal chamber: two symmetric arched hall doors around a central round seal, paired bronze columns and blue ribbon, institutional rather than royal.",
    "iw043_form12_congress": "Original ornate painterly emblem of a Volga-Ural federal accession congress: river delta lines converging on a handshake seal over a bronze relief, no borders or text, blue-green and brass.",
    "iw043_form13_compact": "Original ornate painterly emblem of an inclusive Volga-Ural compact: interlocking bronze rings around a river knot and civic seal, subtle patterned textile texture, deep teal and copper.",
    "iw058_provisional_council": "Original ornate painterly emblem of a provisional national council in Mosul: circular council seal above a stone civic arch with distinct blank delegate medallions, bronze, sandstone, muted blue, no faces or text.",
    "iw058_four_guarantees": "Original ornate painterly emblem of four community guarantees: four equal linked shield plaques around a central olive-branch seal, inclusive non-exclusionary composition, bronze, ivory, deep blue.",
    "iw058_church_civil_jurisdiction": "Original ornate painterly emblem of church and civil jurisdiction in balance: modest stone church arch and civic courthouse scales sharing one foundation, equal institutions, bronze, parchment, cool teal.",
    "iw058_diaspora_liaison": "Original ornate painterly emblem of a diaspora liaison bureau: sealed letters and telegraph key crossing over a small globe and olive branch, bronze, paper ivory, blue-green highlights, no flags or text.",
    "iw058_levies_civilian_control": "Original ornate painterly emblem of civilian control of levies: upright rifle behind a civic shield tied with a plain law ribbon, no blood or fascist imagery, dark steel, bronze, muted teal.",
    "iw058_mosul_corridor": "Original ornate painterly emblem of the Mosul corridor: mountain pass and river crossing with guarded bridge gate and small convoy wheel, sandstone, blue-green river, bronze, no map borders.",
    "iw058_external_guarantee": "Original ornate painterly emblem of external guarantees: two clasped hands beneath an olive branch and small diplomatic seal, subtle starburst, no flags or text, brass, ivory, dark blue.",
    "iw058_church_civic_charter": "Original ornate painterly emblem of a church-civic charter: parchment charter secured by two equal wax seals on a shared stone plinth, abstract non-denominational architecture, bronze, ivory, teal.",
    "iw058_civic_assembly_charter": "Original ornate painterly emblem of a civic assembly charter: semicircle of empty seats around open ledger and central civic seal, bronze, wood, deep teal, no people or text.",
    "iw058_mesopotamian_autonomy": "Original ornate painterly emblem of Mesopotamian autonomy: river reeds and ancient stepped ziggurat fused with a modern civic seal and bridge, bronze, sandstone, river blue, no imperial crown or text.",
    "iw058_form18_congress": "Original ornate painterly emblem of a Mesopotamian federal congress: interlocking river-and-mountain arcs around a balanced assembly seal, joining civic pillars, brass, sandstone, deep blue-green, no flags or text.",
}

def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def run(cmd: list[str]) -> None:
    r = subprocess.run(cmd, check=False, text=True, capture_output=True)
    if r.returncode:
        raise RuntimeError(f"command failed: {' '.join(cmd)}\n{r.stdout}\n{r.stderr}")

def fit(image: Image.Image) -> Image.Image:
    rgba = image.convert("RGBA")
    box = rgba.getchannel("A").getbbox()
    if not box:
        raise ValueError("chroma removal produced a fully transparent image")
    subject = rgba.crop(box)
    scale = min(MAX_W / subject.width, MAX_H / subject.height)
    size = (max(1, round(subject.width * scale)), max(1, round(subject.height * scale)))
    subject = subject.resize(size, Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    x, y = (W - subject.width) // 2, (H - subject.height) // 2
    alpha = subject.getchannel("A")
    outline = ImageChops.subtract(alpha.filter(ImageFilter.MaxFilter(3)), alpha)
    layer = Image.new("RGBA", subject.size, (13, 15, 17, 0))
    layer.putalpha(outline.point(lambda p: min(220, p)))
    canvas.alpha_composite(layer, (x, y))
    shadow = Image.new("RGBA", subject.size, (0, 0, 0, 0))
    shadow.putalpha(alpha.filter(ImageFilter.GaussianBlur(0.55)).point(lambda p: round(p * 0.45)))
    canvas.alpha_composite(shadow, (x + 1, y + 1))
    canvas.alpha_composite(subject, (x, y))
    return canvas

def checker(size: tuple[int, int], cell: int = 8) -> Image.Image:
    board = Image.new("RGBA", size, (60, 64, 70, 255))
    d = ImageDraw.Draw(board)
    for y in range(0, size[1], cell):
        for x in range(0, size[0], cell):
            if (x // cell + y // cell) % 2:
                d.rectangle((x, y, x + cell - 1, y + cell - 1), fill=(100, 105, 112, 255))
    return board

def font(size: int):
    for path in (Path("C:/Windows/Fonts/arial.ttf"), Path("C:/Windows/Fonts/segoeui.ttf")):
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()

def sheet(files: list[Path], out: Path, scale: int, title: str) -> None:
    cols = 4
    thumb = (W * scale, H * scale)
    cell_w, cell_h = max(250, thumb[0] + 24), thumb[1] + 44
    rows = math.ceil(len(files) / cols)
    board = Image.new("RGBA", (cols * cell_w, 42 + rows * cell_h), (28, 31, 36, 255))
    d = ImageDraw.Draw(board)
    d.text((12, 10), title, fill=(240, 234, 215, 255), font=font(16))
    for i, path in enumerate(files):
        with Image.open(path) as im:
            im = im.convert("RGBA")
        col, row = i % cols, i // cols
        left, top = col * cell_w, 42 + row * cell_h
        bg = checker(thumb, max(4, scale * 2))
        bg.alpha_composite(im.resize(thumb, Image.Resampling.NEAREST))
        board.alpha_composite(bg, (left + (cell_w - thumb[0]) // 2, top))
        label = path.stem.replace("goal_independence_wave_", "").replace("_source", "").replace("_", " ")
        d.text((left + 8, top + thumb[1] + 7), label[:34], fill=(225, 226, 230, 255), font=font(11))
    board.convert("RGB").save(out, "PNG", optimize=True)

def main() -> None:
    for folder in (PROCESSED, PROMPTS, CONTACT, VALIDATION, REVIEW_NATIVE, REVIEW_3X, RUNTIME):
        folder.mkdir(parents=True, exist_ok=True)
    sources = sorted(SOURCE.glob("*_source.png"))
    if len(sources) != 20:
        raise ValueError(f"expected 20 source masters, found {len(sources)}")
    records = []
    with tempfile.TemporaryDirectory(prefix="chaosx_006_iw043_iw058_focus_") as temp:
        tmp = Path(temp)
        for source in sources:
            stem = source.stem.removesuffix("_source")
            key = tmp / f"{stem}_keyed.png"
            run([sys.executable, str(CHROMA), "--input", str(source), "--out", str(key), "--auto-key", "border", "--soft-matte", "--transparent-threshold", "12", "--opaque-threshold", "220", "--edge-contract", "1", "--despill", "--force"])
            with Image.open(key) as keyed:
                final = fit(keyed)
            processed = PROCESSED / f"{stem}.png"
            final.save(processed, "PNG", optimize=True)
            runtime = RUNTIME / f"{stem}.dds"
            run([sys.executable, str(CONVERTER), "--input", str(processed), "--output", str(runtime), "--width", str(W), "--height", str(H)])
            prompt = PROMPT_TEXT[stem.removeprefix("goal_independence_wave_")]
            prompt_file = PROMPTS / f"{stem}.txt"
            prompt_file.write_text("Use case: game icon\nAsset type: HOI4 national focus icon\nTarget size: 94x86\n\n" + prompt + "\n\nGenerate on a perfectly flat solid #00ff00 chroma-key background with no variation. Keep the subject separated with crisp edges and generous padding. Do not use #00ff00 in the subject. No shadows, reflections, watermark, UI frame, or readable text.\n", encoding="utf-8")
            native = REVIEW_NATIVE / f"{stem}_native.png"
            with Image.open(processed) as im:
                bg = checker((W, H), 8)
                bg.alpha_composite(im.convert("RGBA"))
                bg.convert("RGB").save(native, "PNG", optimize=True)
                enlarged = bg.resize((W * 3, H * 3), Image.Resampling.NEAREST)
                enlarged.save(REVIEW_3X / f"{stem}_3x.png", "PNG", optimize=True)
            data = runtime.read_bytes()
            alpha = data[128 + 3::4]
            records.append({"stem": stem, "source": source.relative_to(ROOT).as_posix(), "source_sha256": sha(source), "processed": processed.relative_to(ROOT).as_posix(), "processed_sha256": sha(processed), "runtime": runtime.relative_to(ROOT).as_posix(), "runtime_sha256": sha(runtime), "width": W, "height": H, "bytes": len(data), "alpha_min": min(alpha), "alpha_max": max(alpha), "sprite": f"GFX_{stem}"})
    processed = sorted(PROCESSED.glob("*.png"))
    sheet(processed, CONTACT / "006_iw043_iw058_focus_icons_native_contact_sheet.png", 1, "Event 006 IW-043 + IW-058 focus icons — native 94x86")
    sheet(processed, CONTACT / "006_iw043_iw058_focus_icons_3x_contact_sheet.png", 3, "Event 006 IW-043 + IW-058 focus icons — 3x review")
    sheet(sorted(SOURCE.glob("*_source.png")), CONTACT / "006_iw043_iw058_focus_icons_source_contact_sheet.png", 1, "Event 006 IW-043 + IW-058 ImageGen source masters")
    (VALIDATION / "validation.json").write_text(json.dumps({"package": "006_independence_wave/iw043_iw058_focus_icons_2026_07_18", "source_mode": "built-in ImageGen with chroma-key removal", "target_size": "94x86", "references_inspected": ".agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/national_focus/contact_sheet.png", "records": records}, indent=2) + "\n", encoding="utf-8")
    lines = []
    for r in records:
        lines += [f"{r['source_sha256']}  {r['source']}", f"{r['processed_sha256']}  {r['processed']}", f"{r['runtime_sha256']}  {r['runtime']}"]
    (VALIDATION / "hashes.sha256").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"icons": len(records), "dds": len(records), "size": [W, H]}))

if __name__ == "__main__":
    main()
