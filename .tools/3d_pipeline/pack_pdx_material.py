"""Build the packed material textures expected by ``PdxMeshAdvanced``.

Meshy exports glTF metallic-roughness data as separate grayscale maps and as a
glTF packed map. HOI4 uses a different packed layout for the PDX ``spec``
and ``n`` slots. Keeping these conversions in the pilot runner makes the
material route repeatable and leaves the provider files untouched.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Dict

from PIL import Image


PDX_SPECULAR_LEVEL = 32


def _record(path: Path, root: Path) -> Dict[str, Any]:
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    return {
        "path": str(path.relative_to(root)).replace("\\", "/"),
        "bytes": path.stat().st_size,
        "sha256": digest,
    }


def _replace_file(path: Path) -> None:
    """Remove an existing generated image before a Windows overwrite."""

    if path.exists():
        if not path.is_file():
            raise RuntimeError(f"Generated texture target is not a file: {path}")
        path.unlink()


def pack_pdx_specular_map(job: Path, specular_source_rel: str) -> Dict[str, Any]:
    """Pack Meshy metallic and roughness maps into the HOI4 PDX layout.

    The source must be the provider's ``metallic_roughness.png``. The sibling
    grayscale maps are authoritative because the glTF packed alpha channel is
    not the HOI4 roughness channel. The resulting channels are R=0,
    G=specular level, B=metallic, and A=roughness.
    """

    source = (job / specular_source_rel).resolve()
    if source.name.casefold() != "metallic_roughness.png":
        return {
            "status": "not_required",
            "source": str(source.relative_to(job)).replace("\\", "/"),
        }
    metal = source.with_name("metallic.png")
    rough = source.with_name("roughness.png")
    if not source.is_file() and not (metal.is_file() and rough.is_file()):
        raise FileNotFoundError(
            f"PDX material packing requires the provider packed map or its "
            f"metallic/roughness siblings: {source}"
        )
    for path in (metal, rough):
        if not path.is_file():
            raise FileNotFoundError(
                f"PDX material packing requires the provider sibling map: {path}"
            )

    with Image.open(metal) as metal_image, Image.open(rough) as rough_image:
        metal_l = metal_image.convert("L")
        rough_l = rough_image.convert("L")
        if metal_l.size != rough_l.size:
            raise ValueError(
                f"Metallic and roughness maps must have the same dimensions: "
                f"{metal_l.size} != {rough_l.size}"
            )
        zero = Image.new("L", metal_l.size, 0)
        specular = Image.new("L", metal_l.size, PDX_SPECULAR_LEVEL)
        packed = Image.merge("RGBA", (zero, specular, metal_l, rough_l))

    output = source.with_name("pdx_specular.png")
    _replace_file(output)
    packed.save(output, format="PNG", optimize=True)
    report = {
        "status": "packed",
        "layout": {
            "red": "unused_mask_zero",
            "green": f"specular_level_{PDX_SPECULAR_LEVEL}",
            "blue": "metallic",
            "alpha": "roughness",
        },
        "source": {
            "glTF_packed_map": _record(source, job) if source.is_file() else None,
            "metallic": _record(metal, job),
            "roughness": _record(rough, job),
        },
        "output": _record(output, job),
        "dimensions": list(packed.size),
    }
    report_path = job / "blender" / "reports" / "pdx_material_pack.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def pack_pdx_normal_map(job: Path, normal_source_rel: str) -> Dict[str, Any]:
    """Pack a conventional RGB tangent normal into HOI4's PDX ``n`` layout.

    The pinned ``io_pdx_mesh`` route reconstructs the tangent normal from the
    PDX texture's red and alpha channels and forces blue to one on import. The
    provider's standard RGB normal therefore needs R=source.R, A=source.G,
    with the unused green and blue channels zeroed. Passing the provider RGB
    image through unchanged makes the game read an opaque alpha channel as the
    normal Y component, producing the bright, broken surfaces seen in the
    pilot's map render.
    """

    source = (job / normal_source_rel).resolve()
    if source.name.casefold() == "pdx_normal.png":
        return {
            "status": "already_packed",
            "output": _record(source, job),
        }
    if not source.is_file():
        raise FileNotFoundError(f"PDX normal packing requires the provider normal map: {source}")

    with Image.open(source) as source_image:
        rgba = source_image.convert("RGBA")
        red = rgba.getchannel("R")
        green = rgba.getchannel("G")
        zero = Image.new("L", rgba.size, 0)
        packed = Image.merge("RGBA", (red, zero, zero, green))

    output = source.with_name("pdx_normal.png")
    _replace_file(output)
    packed.save(output, format="PNG", optimize=True)
    report = {
        "status": "packed",
        "layout": {
            "red": "source_normal_red",
            "green": "unused_zero",
            "blue": "unused_zero",
            "alpha": "source_normal_green",
        },
        "source": _record(source, job),
        "output": _record(output, job),
        "dimensions": list(packed.size),
    }
    report_path = job / "blender" / "reports" / "pdx_normal_pack.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def prepare_texture_source_rels(job: Path, source_rels: Dict[str, str]) -> Dict[str, str]:
    """Return Blender-friendly source paths while preparing runtime packs."""

    result = dict(source_rels)
    specular = result.get("specular")
    if not specular:
        return result
    report = pack_pdx_specular_map(job, specular)
    if report.get("status") == "packed":
        # The PDX packed map is for the final DDS only. Blender's Principled
        # roughness input must receive the provider roughness channel, or the
        # PDX mask/specular channels make the working preview appear chrome
        # black and exaggerate every normal-map defect.
        result["specular"] = str(
            Path(specular).with_name("roughness.png")
        ).replace("\\", "/")
    normal = result.get("normal")
    if normal:
        # Keep the conventional RGB normal in the Blender working scene so
        # previews and deformation review remain visually meaningful. The PDX
        # packed companion is selected only for the runtime DDS in the pilot
        # runner after Blender has extracted the working textures.
        pack_pdx_normal_map(job, normal)
    return result
