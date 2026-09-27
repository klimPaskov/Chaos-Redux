"""Convert Meshy PBR texture downloads into HOI4 PdxMeshAdvanced DDS maps.

Inputs are the provider files saved beside a download (base_color.png, metallic.png,
roughness.png, normal.png). The asset profile in config/asset_profiles.json supplies the
texture size, the runtime diffuse gamma, and the specular packing; nothing is hardcoded.

Outputs in --out-dir:
  <stem>_diffuse.dds   RGB graded by the profile gamma (lifts provider-dark cloth), alpha kept
  <stem>_specular.dds  R=0, G=profile specular level, B=metallic, A=255-roughness (glossiness)
  <stem>_normal.dds    PDX "RRxG" layout: R=0, G=normal.R (tangent X), B=0, A=normal.G (tangent Y)
  <stem>_textures_manifest.json with source/output hashes and the transforms applied

DDS files are uncompressed BGRA with one mip, produced by the event-asset converter
(.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py), matching the project's
other unit models.

Usage:
  python .tools/3d_pipeline/review/pdx_textures.py --textures <dir> --out-dir <dir> --stem chaosx_zombies [--profile humanoid_unit]
"""
import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageOps

HERE = Path(__file__).resolve().parent
PIPE = HERE.parent
MOD = PIPE.parent.parent
CONVERTER = MOD / ".agents" / "skills" / "chaos-redux-event-assets" / "tools" / "convert_to_dds.py"


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest().upper()


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--textures", required=True)
    p.add_argument("--out-dir", required=True)
    p.add_argument("--stem", required=True)
    p.add_argument("--profile", default="humanoid_unit")
    p.add_argument("--gamma", type=float, help="override the profile runtime_diffuse_gamma")
    a = p.parse_args()

    profile = json.loads((PIPE / "config" / "asset_profiles.json").read_text(encoding="utf-8"))["profiles"][a.profile]
    size = int(profile.get("texture_max_dimension", 1024))
    gamma = a.gamma if a.gamma is not None else float(profile.get("runtime_diffuse_gamma", 1.0))
    spec_level = int(profile["materials"]["specular_packing"]["green"])
    src = Path(a.textures)
    out = Path(a.out_dir)
    work = out / "png"
    work.mkdir(parents=True, exist_ok=True)

    def load(name, mode):
        img = Image.open(src / name).convert(mode)
        return img.resize((size, size), Image.Resampling.LANCZOS) if img.size != (size, size) else img

    base = load("base_color.png", "RGBA")
    lut = [int(round(255.0 * ((v / 255.0) ** gamma))) for v in range(256)]
    r, g, b, alpha = base.split()
    diffuse = Image.merge("RGBA", (r.point(lut), g.point(lut), b.point(lut), alpha))
    metal = load("metallic.png", "L")
    rough = load("roughness.png", "L")
    zero = Image.new("L", (size, size), 0)
    specular = Image.merge("RGBA", (zero, Image.new("L", (size, size), spec_level), metal, ImageOps.invert(rough)))
    normal_src = load("normal.png", "RGBA")
    normal = Image.merge("RGBA", (zero, normal_src.getchannel("R"), zero, normal_src.getchannel("G")))

    record = {"profile": a.profile, "size": size, "diffuse_gamma": gamma, "specular_level": spec_level,
              "sources": {n: digest(src / n) for n in ("base_color.png", "metallic.png", "roughness.png", "normal.png")},
              "outputs": {}}
    for role, img in (("diffuse", diffuse), ("specular", specular), ("normal", normal)):
        png = work / f"{a.stem}_{role}.png"
        img.save(png)
        dds = out / f"{a.stem}_{role}.dds"
        subprocess.run([sys.executable, str(CONVERTER), "--input", str(png), "--output", str(dds), "--width", str(size), "--height", str(size)],
                       check=True, capture_output=True)
        record["outputs"][role] = {"dds": dds.name, "sha256": digest(dds), "bytes": dds.stat().st_size}
    (out / f"{a.stem}_textures_manifest.json").write_text(json.dumps(record, indent=1), encoding="utf-8")
    print(json.dumps(record["outputs"]))


if __name__ == "__main__":
    main()
