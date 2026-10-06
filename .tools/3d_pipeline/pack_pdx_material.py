"""Build the packed material textures expected by ``PdxMeshAdvanced``.

Meshy exports glTF metallic-roughness data as separate grayscale maps and as a
glTF packed map. HOI4 uses a different packed layout for the PDX ``spec``
and ``n`` slots. Keeping these conversions in the pilot runner makes the
material route repeatable and leaves the provider files untouched.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Dict

from PIL import Image, ImageOps
if str(Path(__file__).resolve().parent) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
from textures.conventions import build_pdx_specular_from_provider, repack_provider_normal, gate_specular


def _material_class_inputs(job: Path, source: Path):
    """Read explicit, source-adjacent class/UV masks; never infer from colour."""
    path = source.parent / "material_classes.json"
    if not path.is_file():
        raise ValueError("PDX specular packing needs explicit material_classes.json masks beside " + str(source))
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    def load_mask(value):
        target = (source.parent / value).resolve()
        target.relative_to(job.resolve())
        with Image.open(target) as image:
            return image.convert("L").copy()
    masks = {name: load_mask(value) for name, value in data["classes"].items()}
    occupancy = load_mask(data["occupancy"])
    return masks, occupancy, {"manifest": _record(path, job),
                              "masks": {name: _record((source.parent / value).resolve(), job) for name, value in data["classes"].items()},
                              "occupancy": _record((source.parent / data["occupancy"]).resolve(), job)}


def _channel_stats(image: Image.Image) -> Dict[str, Dict[str, float]]:
    """Return compact channel evidence for runtime texture QA."""

    rgba = image.convert("RGBA")
    result: Dict[str, Dict[str, float]] = {}
    for name, channel in zip(("R", "G", "B", "A"), rgba.split()):
        values = list(channel.getdata())
        result[name] = {
            "min": int(min(values)),
            "max": int(max(values)),
            "mean": round(sum(values) / len(values), 4),
        }
    return result


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
    not the HOI4 glossiness channel. Explicit source-adjacent material masks
    control G strength, B metal coverage and class-bounded inverted-roughness A.
    PdxMeshAdvanced uses spec.A as Glossiness in the installed vanilla shader.
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

    masks, occupancy, mask_evidence = _material_class_inputs(job, rough)
    with Image.open(metal) as metal_image, Image.open(rough) as rough_image:
        packed, recipe = build_pdx_specular_from_provider(rough_image, metal_image, masks, occupancy)
    semantic_gate = gate_specular(packed, occupancy, masks)
    if semantic_gate["status"] != "passed":
        raise ValueError("PDX specular material gate refused provider pack: " + str(semantic_gate["failures"]))

    output = source.with_name("pdx_specular.png")
    _replace_file(output)
    packed.save(output, format="PNG", optimize=True)
    report = {
        "status": "packed",
        "layout": {
            "red": "unused_mask_zero",
            "green": "provider_roughness_mapped_to_explicit_material_class_recipe",
            "blue": "metallic",
            "alpha": "glossiness_255_minus_roughness",
        },
        "source": {
            "glTF_packed_map": _record(source, job) if source.is_file() else None,
            "metallic": _record(metal, job),
            "roughness": _record(rough, job),
        },
        "output": _record(output, job),
        "dimensions": list(packed.size),
        "channel_stats": _channel_stats(packed),
        "material_masks": mask_evidence,
        "recipe": recipe,
        "semantic_gate": semantic_gate,
    }
    report_path = job / "blender" / "reports" / "pdx_material_pack.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def pack_pdx_specular_channels(
    job: Path,
    metallic_source_rel: str,
    roughness_source_rel: str,
    output_rel: str,
) -> Dict[str, Any]:
    """Pack separate metallic and roughness maps into a PDX specular texture."""

    metallic = (job / metallic_source_rel).resolve()
    roughness = (job / roughness_source_rel).resolve()
    output = (job / output_rel).resolve()
    for path in (metallic, roughness):
        if not path.is_file():
            raise FileNotFoundError(path)
    masks, occupancy, mask_evidence = _material_class_inputs(job, roughness)
    with Image.open(metallic) as metallic_image, Image.open(roughness) as roughness_image:
        packed, recipe = build_pdx_specular_from_provider(roughness_image, metallic_image, masks, occupancy)
    semantic_gate = gate_specular(packed, occupancy, masks)
    if semantic_gate["status"] != "passed":
        raise ValueError("PDX specular material gate refused provider pack: " + str(semantic_gate["failures"]))
    output.parent.mkdir(parents=True, exist_ok=True)
    _replace_file(output)
    packed.save(output, format="PNG", optimize=True)
    report = {
        "status": "packed",
        "layout": {
            "red": "unused_mask_zero",
            "green": "provider_roughness_mapped_to_explicit_material_class_recipe",
            "blue": "metallic",
            "alpha": "glossiness_255_minus_roughness",
        },
        "source": {
            "metallic": _record(metallic, job),
            "roughness": _record(roughness, job),
        },
        "output": _record(output, job),
        "dimensions": list(packed.size),
        "channel_stats": _channel_stats(packed),
        "material_masks": mask_evidence,
        "recipe": recipe,
        "semantic_gate": semantic_gate,
    }
    report_path = job / "blender" / "reports" / "pdx_generation_specular_pack.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def ensure_gltf_metallic_roughness_map(job: Path, source_rel: str) -> Dict[str, Any]:
    """Create a glTF-convention packed map when a provider only supplies sibling channels."""

    source = (job / source_rel).resolve()
    if source.is_file():
        return {"status": "present", "output": _record(source, job)}
    metallic = source.with_name("metallic.png")
    roughness = source.with_name("roughness.png")
    for path in (metallic, roughness):
        if not path.is_file():
            raise FileNotFoundError(path)
    with Image.open(metallic) as metallic_image, Image.open(roughness) as roughness_image:
        metallic_l = metallic_image.convert("L")
        roughness_l = roughness_image.convert("L")
        if metallic_l.size != roughness_l.size:
            raise ValueError(
                f"Metallic and roughness maps must have the same dimensions: "
                f"{metallic_l.size} != {roughness_l.size}"
            )
        zero = Image.new("L", metallic_l.size, 0)
        opaque = Image.new("L", metallic_l.size, 255)
        packed = Image.merge("RGBA", (zero, roughness_l, metallic_l, opaque))
    source.parent.mkdir(parents=True, exist_ok=True)
    _replace_file(source)
    packed.save(source, format="PNG", optimize=True)
    report = {
        "status": "created_from_siblings",
        "source": {
            "metallic": _record(metallic, job),
            "roughness": _record(roughness, job),
        },
        "output": _record(source, job),
        "dimensions": list(packed.size),
    }
    report_path = job / "blender" / "reports" / "gltf_metallic_roughness_source.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def pack_pdx_normal_map(job: Path, normal_source_rel: str) -> Dict[str, Any]:
    """Pack a conventional RGB tangent normal into HOI4's PDX ``n`` layout.

    The pinned ``io_pdx_mesh`` material route reads the PDX normal texture's
    green channel as tangent X and alpha as tangent Y. The runtime shader
    reconstructs tangent Z. R mirrors source.R/G, B is zero, and A retains
    source.G unless explicit provider handedness evidence requests inversion.
    """

    source = (job / normal_source_rel).resolve()
    if source.name.casefold() == "pdx_normal.png":
        with Image.open(source) as packed_source:
            stats = _channel_stats(packed_source)
        with Image.open(source) as checked:
            mirrored = checked.getchannel('R').tobytes() == checked.getchannel('G').tobytes()
        if not mirrored or stats["B"]["max"] != 0:
            raise ValueError(
                f"Existing PDX normal requires R/G mirror and B-zero cleanup through the shared delivery step: {source}"
            )
        return {
            "status": "already_packed",
            "output": _record(source, job),
            "channel_stats": stats,
        }
    if not source.is_file():
        raise FileNotFoundError(f"PDX normal packing requires the provider normal map: {source}")

    with Image.open(source) as source_image:
        packed, normal_recipe = repack_provider_normal(source_image, green_sign="preserve")

    output = source.with_name("pdx_normal.png")
    _replace_file(output)
    packed.save(output, format="PNG", optimize=True)
    report = {
        "status": "packed",
        "layout": {
            "red": "source_normal_red_mirrored_tangent_x",
            "green": "source_normal_red_tangent_x",
            "blue": "unused_zero",
            "alpha": "source_normal_green_tangent_y",
        },
        "source": _record(source, job),
        "output": _record(output, job),
        "dimensions": list(packed.size),
        "channel_stats": _channel_stats(packed),
        "recipe": normal_recipe,
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
    if Path(specular).name.casefold() == "metallic_roughness.png":
        ensure_gltf_metallic_roughness_map(job, specular)
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
