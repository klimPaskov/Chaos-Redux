from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageChops, ImageFilter, ImageOps


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[3]
HELPER = Path.home() / ".codex" / "skills" / ".system" / "imagegen" / "scripts" / "remove_chroma_key.py"
DDS = REPO / ".agents" / "skills" / "chaos-redux-event-assets" / "tools" / "convert_to_dds.py"
OVERLAY = REPO / ".agents" / "skills" / "chaos-redux-event-assets" / "assets" / "vanilla_reference" / "icons" / "achievements" / "overlay.png"


FAMILIES = {
    "decision_categories": (52, 40, 50, 38, REPO / "gfx/interface/decisions/006_independence_wave/volga_assyria"),
    "decisions": (32, 32, 30, 30, REPO / "gfx/interface/decisions/006_independence_wave/volga_assyria"),
    "ideas": (64, 64, 60, 60, REPO / "gfx/interface/ideas/006_independence_wave/volga_assyria"),
}


def run(args: list[str]) -> None:
    subprocess.run(args, check=True)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def remove_key(src: Path, dst: Path) -> None:
    run([
        "python", str(HELPER), "--input", str(src), "--out", str(dst),
        "--auto-key", "border", "--soft-matte", "--transparent-threshold", "12",
        "--opaque-threshold", "220", "--edge-contract", "1", "--despill", "--force",
    ])


def fit_transparent(keyed: Image.Image, size: tuple[int, int], max_size: tuple[int, int]) -> Image.Image:
    keyed = keyed.convert("RGBA")
    bbox = keyed.getchannel("A").getbbox()
    if not bbox:
        raise ValueError("fully transparent source")
    subject = keyed.crop(bbox)
    scale = min(max_size[0] / subject.width, max_size[1] / subject.height)
    subject = subject.resize((max(1, round(subject.width * scale)), max(1, round(subject.height * scale))), Image.Resampling.LANCZOS)
    alpha = subject.getchannel("A")
    canvas = Image.new("RGBA", size, (0, 0, 0, 0))
    x = (size[0] - subject.width) // 2
    y = (size[1] - subject.height) // 2
    outline = ImageChops.subtract(alpha.filter(ImageFilter.MaxFilter(3)), alpha)
    edge = Image.new("RGBA", subject.size, (12, 10, 8, 0))
    edge.putalpha(outline.point(lambda v: min(220, v)))
    canvas.alpha_composite(edge, (x, y))
    shadow = Image.new("RGBA", subject.size, (0, 0, 0, 0))
    shadow.putalpha(alpha.filter(ImageFilter.GaussianBlur(0.55)).point(lambda v: round(v * 0.45)))
    canvas.alpha_composite(shadow, (x + 1, y + 1))
    canvas.alpha_composite(subject, (x, y))
    return canvas


def fit_achievement(keyed: Image.Image) -> Image.Image:
    keyed = keyed.convert("RGBA")
    bbox = keyed.getchannel("A").getbbox()
    if not bbox:
        raise ValueError("fully transparent achievement source")
    subject = keyed.crop(bbox)
    scale = min(60 / subject.width, 60 / subject.height)
    subject = subject.resize((max(1, round(subject.width * scale)), max(1, round(subject.height * scale))), Image.Resampling.LANCZOS)
    # Achievement DDS uses a full opaque square behind the framed subject.
    canvas = Image.new("RGBA", (64, 64), (54, 57, 52, 255))
    x = (64 - subject.width) // 2
    y = (64 - subject.height) // 2
    canvas.alpha_composite(subject, (x, y))
    return canvas


def dds(png: Path, out: Path, size: tuple[int, int]) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    run(["python", "-B", str(DDS), "--input", str(png), "--output", str(out), "--width", str(size[0]), "--height", str(size[1])])


def main() -> None:
    if not HELPER.exists() or not DDS.exists() or not OVERLAY.exists():
        raise FileNotFoundError("imagegen helper, DDS converter, or achievement overlay missing")
    source_root = ROOT / "source_png"
    processed_root = ROOT / "processed_png"
    rows: list[dict[str, object]] = []
    runtime: list[Path] = []
    with tempfile.TemporaryDirectory(prefix="iw043_iw058_icons_") as temp:
        tmp = Path(temp)
        for family, (w, h, mw, mh, runtime_dir) in FAMILIES.items():
            for src in sorted((source_root / family).glob("*_source.png")):
                keyed = tmp / f"{src.stem}_keyed.png"
                remove_key(src, keyed)
                with Image.open(keyed) as image:
                    final = fit_transparent(image, (w, h), (mw, mh))
                out = processed_root / family / (src.name.removesuffix("_source.png") + ".png")
                out.parent.mkdir(parents=True, exist_ok=True)
                final.save(out, "PNG", optimize=True)
                rd = runtime_dir / (out.stem + ".dds")
                dds(out, rd, (w, h))
                runtime.append(rd)
                rows.append({"family": family, "source": src.relative_to(REPO).as_posix(), "source_sha256": sha(src), "processed": out.relative_to(REPO).as_posix(), "processed_sha256": sha(out), "runtime": rd.relative_to(REPO).as_posix(), "runtime_sha256": sha(rd), "width": w, "height": h})

        ach_src = source_root / "achievements" / "achievement_chaosx_006_assyria_survives_source.png"
        keyed = tmp / "achievement_keyed.png"
        remove_key(ach_src, keyed)
        with Image.open(keyed) as image:
            base = fit_achievement(image)
        ach_dir = processed_root / "achievements"
        ach_dir.mkdir(parents=True, exist_ok=True)
        base_png = ach_dir / "chaosx_006_assyria_survives.png"
        base.save(base_png, "PNG", optimize=True)
        grey_rgb = ImageOps.grayscale(base.convert("RGB")).convert("RGB")
        grey = Image.merge("RGBA", (*grey_rgb.split(), base.getchannel("A")))
        grey_png = ach_dir / "chaosx_006_assyria_survives_grey.png"
        grey.save(grey_png, "PNG", optimize=True)
        with Image.open(OVERLAY) as overlay:
            not_eligible = grey.copy()
            not_eligible.alpha_composite(overlay.convert("RGBA").resize((64, 64), Image.Resampling.LANCZOS))
        ne_png = ach_dir / "chaosx_006_assyria_survives_not_eligible.png"
        not_eligible.save(ne_png, "PNG", optimize=True)
        for p in (base_png, grey_png, ne_png):
            rd = REPO / "gfx/achievements" / f"{p.stem}.dds"
            dds(p, rd, (64, 64))
            runtime.append(rd)
            rows.append({"family": "achievement", "source": ach_src.relative_to(REPO).as_posix(), "source_sha256": sha(ach_src), "processed": p.relative_to(REPO).as_posix(), "processed_sha256": sha(p), "runtime": rd.relative_to(REPO).as_posix(), "runtime_sha256": sha(rd), "width": 64, "height": 64})
    (ROOT / "validation" / "build_rows.json").write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"assets": len(rows), "runtime": len(runtime)}))


if __name__ == "__main__":
    main()
