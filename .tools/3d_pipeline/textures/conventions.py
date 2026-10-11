"""PDX normal and specular channel transforms and measured semantic gates."""

from __future__ import annotations

import math
from typing import Dict, Mapping, Optional, Tuple

from PIL import Image

from .atlas import dilate_from_occupancy, load_occupancy_mask, mask_stats


PDX_NORMAL_LAYOUT = "RRxG"
PDX_SPECULAR_LAYOUT = "rgb_specular_alpha_glossiness"

# Values follow the accepted cross-cutting unit-fix recipe. Alpha ranges are
# bounded where the plan supplies them; leather keeps provider gloss evidence.
MATERIAL_RECIPES = {
    "cloth": {"green": (40, 90), "alpha": (60, 100)},
    "skin": {"green": (110, 160), "alpha": (120, 160)},
    "leather": {"green": (120, 160), "alpha": None},
    "steel": {"green": (180, 255), "alpha": (150, 180)},
    "stone": {"green": (60, 90), "alpha": (50, 70)},
    "fur": {"green": (20, 40), "alpha": (40, 70)},
    "bone": {"green": (110, 140), "alpha": (70, 100)},
    "worn_steel": {"green": (150, 180), "alpha": (70, 100)},
    "magma": {"green": (140, 180), "alpha": (70, 100)},
    # Vanilla-calibrated low-gloss classes. The installed vanilla infantry specular alpha averages 44 (p95 76); the
    # 2026-10 footage review measured A 114-122 reading as plastic or wet chrome on dry cloth and skin, so unit
    # fabric and dry flesh stay inside the vanilla alpha band instead of the wet-skin range above.
    "matte_cloth": {"green": (40, 90), "alpha": (25, 50)},
    "dry_skin": {"green": (80, 130), "alpha": (30, 70)},
}

METAL_CLASSES = frozenset({"steel", "worn_steel"})


def resolve_material_recipes(overrides=None):
    """Resolve explicit job calibration without mutating shared defaults."""
    recipes = {name: dict(recipe) for name, recipe in MATERIAL_RECIPES.items()}
    if overrides is None:
        return recipes
    if not isinstance(overrides, Mapping):
        raise ValueError("Material recipe overrides must be a class/range mapping.")
    for name, values in overrides.items():
        if name not in recipes:
            raise ValueError(f"Unknown material class {name!r}.")
        if not isinstance(values, Mapping) or not values or set(values) - {"green", "alpha"}:
            raise ValueError("Recipe overrides accept only explicit green/alpha ranges.")
        for channel, bounds in values.items():
            if not isinstance(bounds, (list, tuple)) or len(bounds) != 2:
                raise ValueError("A calibrated channel requires two integer bounds.")
            low, high = bounds
            if type(low) is not int or type(high) is not int or not 0 <= low <= high <= 255:
                raise ValueError("Calibrated channel bounds must be ordered integers in 0..255.")
            recipes[name][channel] = (low, high)
    return recipes


def _metal_mask_values(masks, size):
    metal_masks = [values for name, values in masks.items() if name in METAL_CLASSES]
    if not metal_masks:
        raise ValueError("An explicit steel/worn_steel mask is required for metalness validation.")
    if len(metal_masks) == 1:
        return metal_masks[0]
    return bytes(255 if any(values[index] for values in metal_masks) else 0 for index in range(size))

NORMAL_FLAT_RGBA = (128, 128, 0, 128)


def _gray_image(image: Image.Image, role: str) -> Image.Image:
    if image.mode in {"1", "L", "I;16", "I"}:
        return image.convert("L")
    rgb = image.convert("RGB")
    red, green, blue = rgb.split()
    if red.tobytes() != green.tobytes() or red.tobytes() != blue.tobytes():
        raise ValueError(f"{role} input must be a grayscale provider map.")
    return red.copy()


def _image_channels(image: Image.Image, occupancy_mask: Image.Image) -> Dict[str, object]:
    rgba = image.convert("RGBA")
    mask = load_occupancy_mask(occupancy_mask, rgba.size)
    occupied = [value > 0 for value in mask.tobytes()]
    if len(occupied) != rgba.width * rgba.height:
        raise ValueError("Occupancy mask dimensions do not match the texture.")
    channels = rgba.split()
    return {
        "rgba": rgba,
        "mask": mask,
        "occupied": occupied,
        "channels": channels,
        "mask_report": mask_stats(mask),
    }


def _stats_for_values(values) -> Dict[str, float]:
    if not values:
        raise ValueError("Cannot compute material statistics over an empty occupancy mask.")
    mean = sum(values) / len(values)
    variance = sum((value - mean) ** 2 for value in values) / len(values)
    return {
        "min": int(min(values)),
        "max": int(max(values)),
        "mean": round(mean, 6),
        "std": round(math.sqrt(variance), 6),
        "count": len(values),
    }


def _stats_by_channel(image: Image.Image, occupancy_mask: Image.Image) -> Dict[str, object]:
    data = _image_channels(image, occupancy_mask)
    result = {}
    for channel_name, channel in zip(("R", "G", "B", "A"), data["channels"]):
        values = [value for value, occupied in zip(channel.tobytes(), data["occupied"]) if occupied]
        result[channel_name] = _stats_for_values(values)
    return {"channels": result, "mask": data["mask_report"]}


def repack_provider_normal(
    provider_normal: Image.Image,
    *,
    green_sign: str = "preserve",
    occupancy_mask: Optional[Image.Image] = None,
    dilation_px: int = 12,
) -> Tuple[Image.Image, Dict[str, object]]:
    """Pack a conventional provider RGB tangent normal into PDX RRxG.

    Source red is copied to PDX red and green (the mirrored X pair); provider
    green is copied to alpha by default. Inverting green is an explicit option
    that requires upstream handedness evidence in the caller's provenance.
    No detail is synthesized. Unoccupied padding is flat tangent-space normal.
    """

    if green_sign not in {"preserve", "invert"}:
        raise ValueError("green_sign must be 'preserve' or 'invert'.")
    rgba = provider_normal.convert("RGBA")
    source_red = rgba.getchannel("R")
    source_green = rgba.getchannel("G")
    if green_sign == "invert":
        from PIL import ImageOps

        source_green = ImageOps.invert(source_green)
    blue = Image.new("L", rgba.size, 0)
    packed = Image.merge("RGBA", (source_red, source_red, blue, source_green))
    report = {
        "source_layout": "provider_rgb_tangent_normal",
        "target_layout": PDX_NORMAL_LAYOUT,
        "mapping": {"R": "provider.R_x", "G": "provider.R_x", "B": "0", "A": "provider.G_y"},
        "green_sign": green_sign,
        "detail_synthesized": False,
    }
    if occupancy_mask is not None:
        packed, padding = dilate_from_occupancy(
            packed,
            occupancy_mask,
            dilation_px,
            channels=(0, 1, 2, 3),
            outside_fill=NORMAL_FLAT_RGBA,
        )
        report["padding"] = padding
    return packed, report


def packed_normal_cleanup(
    source_normal: Image.Image,
    occupancy_mask: Image.Image,
    *,
    dilation_px: int = 12,
) -> Tuple[Image.Image, Dict[str, object]]:
    """Repair safe installed PDX channel structure while preserving G and A.

    Occupied texels retain the existing green and alpha bytes exactly. Red is
    mirrored from green, blue is cleared, and non-UV padding is neutral before
    mask-driven dilation. This does not retouch or invent tangent detail.
    """

    source = source_normal.convert("RGBA")
    mask = load_occupancy_mask(occupancy_mask, source.size)
    values = list(source.getdata())
    mask_bytes = mask.tobytes()
    repaired = []
    for pixel, occupied in zip(values, mask_bytes):
        if occupied:
            repaired.append((pixel[1], pixel[1], 0, pixel[3]))
        else:
            repaired.append(NORMAL_FLAT_RGBA)
    target = Image.new("RGBA", source.size)
    target.putdata(repaired)
    dilated, padding = dilate_from_occupancy(
        target,
        mask,
        dilation_px,
        channels=(0, 1, 2, 3),
        outside_fill=NORMAL_FLAT_RGBA,
    )
    for old, new, is_occupied in zip(values, dilated.getdata(), mask_bytes):
        if is_occupied and (new[1] != old[1] or new[3] != old[3]):
            raise RuntimeError("Packed-normal cleanup changed occupied G/A source values.")
    return dilated, {
        "operation": "packed_normal_cleanup",
        "target_layout": PDX_NORMAL_LAYOUT,
        "mapping": {"R": "existing.G", "G": "existing.G_preserved", "B": "0", "A": "existing.A_preserved"},
        "occupied_green_alpha_preserved": True,
        "detail_synthesized": False,
        "padding": padding,
    }


def normal_statistics(image: Image.Image, occupancy_mask: Image.Image) -> Dict[str, object]:
    data = _image_channels(image, occupancy_mask)
    values_by_channel = {
        name: [value for value, occupied in zip(channel.tobytes(), data["occupied"]) if occupied]
        for name, channel in zip(("R", "G", "B", "A"), data["channels"])
    }
    vectors = []
    for green, alpha, occupied in zip(
        data["channels"][1].tobytes(), data["channels"][3].tobytes(), data["occupied"]
    ):
        if occupied:
            tangent_x = (green / 127.5) - 1.0
            tangent_y = (alpha / 127.5) - 1.0
            vectors.append(math.sqrt(tangent_x * tangent_x + tangent_y * tangent_y))
    r_values = values_by_channel["R"]
    g_values = values_by_channel["G"]
    return {
        "channels": {name: _stats_for_values(values) for name, values in values_by_channel.items()},
        "g_std": _stats_for_values(values_by_channel["G"])["std"],
        "a_std": _stats_for_values(values_by_channel["A"])["std"],
        "mean_tangent_tilt": round(sum(vectors) / len(vectors), 6),
        "r_g_mean_abs_error": round(sum(abs(a - b) for a, b in zip(r_values, g_values)) / len(r_values), 6),
        "b_nonzero_fraction": round(sum(value != 0 for value in values_by_channel["B"]) / len(values_by_channel["B"]), 8),
        "mask": data["mask_report"],
    }


def gate_normal(image: Image.Image, occupancy_mask: Image.Image) -> Dict[str, object]:
    stats = normal_statistics(image, occupancy_mask)
    failures = []
    for channel in ("g_std", "a_std"):
        if stats[channel] < 15 or stats[channel] > 35:
            failures.append(f"{channel}={stats[channel]} is outside 15..35.")
    if stats["mean_tangent_tilt"] > 0.35:
        failures.append(
            f"mean tangent tilt {stats['mean_tangent_tilt']} exceeds 0.35; no detail is synthesized to compensate."
        )
    if stats["r_g_mean_abs_error"] > 5:
        failures.append(f"mean R/G mirror error {stats['r_g_mean_abs_error']} exceeds 5.")
    if stats["b_nonzero_fraction"] > 0.01:
        failures.append("more than 1% of occupied normal blue values are nonzero.")
    return {"status": "passed" if not failures else "failed", "failures": failures, "statistics": stats}


def _class_membership(material_masks: Mapping[str, Image.Image], size, occupied):
    if not material_masks:
        raise ValueError("Specular recipe requires explicit material-class masks.")
    classes = [None] * len(occupied)
    masks = {}
    for class_name, mask_image in material_masks.items():
        if class_name not in MATERIAL_RECIPES:
            raise ValueError(f"Unknown material class {class_name!r}.")
        mask = load_occupancy_mask(mask_image, size, allow_empty=True)
        values = mask.tobytes()
        masks[class_name] = values
        for index, value in enumerate(values):
            if not occupied[index] or value == 0:
                continue
            if classes[index] is not None:
                raise ValueError(f"Material masks overlap at occupied texel {index}.")
            classes[index] = class_name
    uncovered = [index for index, value in enumerate(occupied) if value and classes[index] is None]
    if uncovered:
        raise ValueError(f"Material masks leave {len(uncovered)} occupied texels unclassified.")
    return classes, masks


def build_pdx_specular_from_provider(
    roughness: Image.Image,
    metalness: Optional[Image.Image],
    material_masks: Mapping[str, Image.Image],
    occupancy_mask: Image.Image,
    *,
    source_hashes: Optional[Mapping[str, object]] = None,
    recipe_overrides=None,
) -> Tuple[Image.Image, Dict[str, object]]:
    """Derive a PDX specular map from provider PBR maps and explicit masks.

    Green maps each resolved class recipe over its planned range using provider
    roughness; alpha is inverted roughness and clamped only to an explicitly
    planned class interval. Blue is zero outside the explicit metal-class union
    and is max(200, provider metalness) within steel/worn_steel. Without a
    metalness map, those masks receive 200. Provider maps remain untouched.
    """

    recipes = resolve_material_recipes(recipe_overrides)
    roughness_l = _gray_image(roughness, "roughness")
    occupancy = load_occupancy_mask(occupancy_mask, roughness_l.size)
    if metalness is not None:
        metalness_l = _gray_image(metalness, "metalness")
        if metalness_l.size != roughness_l.size:
            raise ValueError("Roughness and metalness map dimensions differ.")
        metal_values = metalness_l.tobytes()
    else:
        metal_values = None
    occupied = [value > 0 for value in occupancy.tobytes()]
    classes, masks = _class_membership(material_masks, roughness_l.size, occupied)
    rough_values = roughness_l.tobytes()
    steel_mask_values = _metal_mask_values(masks, len(occupied))
    pixels = []
    source_metal_values = []
    output_metal_values = []
    outside_steel_source_values = []
    changed_blue_pixels = 0
    for index, is_occupied in enumerate(occupied):
        if not is_occupied:
            pixels.append((0, 0, 0, 0))
            continue
        class_name = classes[index]
        recipe = recipes[class_name]
        rough = rough_values[index]
        g_min, g_max = recipe["green"]
        green = int(round(g_min + ((255 - rough) / 255.0) * (g_max - g_min)))
        gloss = 255 - rough
        alpha_range = recipe["alpha"]
        if alpha_range is not None:
            gloss = min(alpha_range[1], max(alpha_range[0], gloss))
        in_steel = steel_mask_values[index] > 0
        if metal_values is None:
            blue = 200 if in_steel else 0
        else:
            source_blue = metal_values[index]
            source_metal_values.append(source_blue)
            if in_steel:
                blue = max(200, source_blue)
            else:
                blue = 0
                outside_steel_source_values.append(source_blue)
            if blue != source_blue:
                changed_blue_pixels += 1
        output_metal_values.append(blue)
        pixels.append((0, green, blue, gloss))
    packed = Image.new("RGBA", roughness_l.size)
    packed.putdata(pixels)
    if metal_values is not None:
        source_metal_stats = _stats_for_values(source_metal_values)
        source_outside_steel_stats = (
            _stats_for_values(outside_steel_source_values)
            if outside_steel_source_values
            else None
        )
    else:
        source_metal_stats = None
        source_outside_steel_stats = None
    report = {
        "status": "packed",
        "layout": PDX_SPECULAR_LAYOUT,
        "recipes": recipes,
        "recipe_overrides": dict(recipe_overrides or {}),
        "provider_roughness_used": True,
        "provider_metalness_used": metalness is not None,
        "metal_mask": "explicit steel/worn_steel material mask union",
        "metal_classes": sorted(name for name in masks if name in METAL_CLASSES),
        "blue_channel_masking": {
            "applied": True,
            "outside_steel": 0,
            "inside_steel": "max(200, original provider metalness)" if metal_values is not None else 200,
            "steel_minimum": 200,
            "provider_metalness_original_stats": source_metal_stats,
            "provider_metalness_outside_steel_original_stats": source_outside_steel_stats,
            "derived_blue_output_stats": _stats_for_values(output_metal_values),
            "occupied_pixels_changed_from_original_provider_metalness": (
                changed_blue_pixels if metal_values is not None else None
            ),
            "provider_maps_modified": False,
        },
        "original_provider_input_hashes": dict(source_hashes or {}),
        "nonmetal_blue_channel_clamped_without_mask": False,
        "alpha_exception": "skin and steel may exceed mean A=110 only inside their explicit masks and within the listed class recipe bounds",
        "mask": mask_stats(occupancy),
        "detail_synthesized": False,
    }
    return packed, report


def specular_statistics(
    image: Image.Image,
    occupancy_mask: Image.Image,
    material_masks: Mapping[str, Image.Image],
    *,
    wet_classes=(),
    recipe_overrides=None,
) -> Dict[str, object]:
    recipes = resolve_material_recipes(recipe_overrides)
    data = _image_channels(image, occupancy_mask)
    classes, masks = _class_membership(material_masks, data["rgba"].size, data["occupied"])
    values_by_channel = {
        name: [value for value, occupied in zip(channel.tobytes(), data["occupied"]) if occupied]
        for name, channel in zip(("R", "G", "B", "A"), data["channels"])
    }
    class_stats = {}
    channel_bytes = {name: channel.tobytes() for name, channel in zip(("R", "G", "B", "A"), data["channels"])}
    for class_name in sorted(masks):
        indices = [index for index, value in enumerate(masks[class_name]) if value > 0 and data["occupied"][index]]
        if not indices:
            continue
        class_stats[class_name] = {
            channel: _stats_for_values([channel_bytes[channel][index] for index in indices])
            for channel in ("G", "A", "B")
        }
    steel_mask = _metal_mask_values(masks, len(data["occupied"]))
    outside_metal = [
        channel_bytes["B"][index]
        for index, is_occupied in enumerate(data["occupied"])
        if is_occupied and steel_mask[index] == 0
    ]
    if not outside_metal:
        outside_metal = [0]
    return {
        "channels": {name: _stats_for_values(values) for name, values in values_by_channel.items()},
        "class_stats": class_stats,
        "outside_metal_b": _stats_for_values(outside_metal),
        "wet_classes": sorted(wet_classes),
        "recipes": recipes,
        "mask": data["mask_report"],
    }


def gate_specular(
    image: Image.Image,
    occupancy_mask: Image.Image,
    material_masks: Mapping[str, Image.Image],
    *,
    wet_classes=(),
    steel_blue_tolerance: int = 0,
    recipe_overrides=None,
) -> Dict[str, object]:
    """Validate packed PDX channels against class-aware material evidence."""

    stats = specular_statistics(image, occupancy_mask, material_masks,
                               wet_classes=wet_classes, recipe_overrides=recipe_overrides)
    failures = []
    if stats["channels"]["G"]["std"] == 0:
        failures.append("specular green standard deviation is zero.")
    if stats["outside_metal_b"]["mean"] > 5:
        failures.append(
            f"mean blue/metalness outside the explicit steel mask is {stats['outside_metal_b']['mean']} (>5)."
        )
    if steel_blue_tolerance < 0 or steel_blue_tolerance > 5:
        raise ValueError("steel_blue_tolerance must be from 0 through 5 channel values.")
    for metal_class in sorted(METAL_CLASSES):
        steel_stats = stats["class_stats"].get(metal_class)
        if steel_stats is not None and steel_stats["B"]["min"] < 200 - steel_blue_tolerance:
            failures.append(
                f"{metal_class} blue/metalness has a value below the 200 minimum "
                f"(allowed compression tolerance {steel_blue_tolerance}): {steel_stats['B']['min']}."
            )
    stats["steel_blue_minimum"] = 200
    stats["steel_blue_compression_tolerance"] = steel_blue_tolerance
    for class_name, channels in stats["class_stats"].items():
        recipe = stats["recipes"][class_name]
        green_min, green_max = recipe["green"]
        green_stats = channels["G"]
        if green_stats["min"] < green_min or green_stats["max"] > green_max:
            failures.append(f"{class_name} G values are outside {green_min}..{green_max}.")
        alpha_range = recipe["alpha"]
        if alpha_range is not None:
            alpha_stats = channels["A"]
            if alpha_stats["min"] < alpha_range[0] or alpha_stats["max"] > alpha_range[1]:
                failures.append(
                    f"{class_name} A values are outside {alpha_range[0]}..{alpha_range[1]}."
                )
        is_planned_high_gloss = class_name in {"skin", "steel"} and alpha_range is not None
        is_wet = class_name in wet_classes
        if not is_planned_high_gloss and not is_wet and channels["A"]["mean"] > 110:
            failures.append(f"nonwet {class_name} mean alpha/gloss {channels['A']['mean']} exceeds 110.")
    return {"status": "passed" if not failures else "failed", "failures": failures, "statistics": stats}
