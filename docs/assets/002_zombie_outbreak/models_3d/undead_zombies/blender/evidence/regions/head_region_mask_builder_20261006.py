"""Build a review-only head-region draft from manual source-view annotations.

This script resolves explicitly traced image polygons through hash-bound raycast
face-ID maps, then projects the selected source triangles through the exact UV
loop data exported from the reviewed Blender checkpoint. It does not edit a
mesh, UV layer, rig, weight, action, material, or runtime file.
"""

from collections import Counter, defaultdict
import hashlib
import json
import os
from pathlib import Path
import struct
import zlib

from PIL import Image, ImageDraw, ImageFont


HERE = Path(__file__).resolve().parent
MODEL_ROOT = HERE.parents[2]
REGION_DIR = HERE
EXPECTED_SOURCE_SHA = "c7439c1af44891d480082fa85efee73f848f0a8a086bbc05e9e0676878f269bf"
EXPECTED_RUNTIME_SHA = "de3f5f66b6d724221200a883941ebcda649d880a07780f71d1820c7a2c301052"
EXPECTED_UV_SHA = "ffc52fc345baf26d8aff6f89f2f3907bf7f7a0063b47e829715ace401c564401"
EXPECTED_CORRESPONDENCE_SHA = "7dbd42bdde00a0d2c90674bc09b80a35214eddfa7b04c8de36f6583efbf81158"
EXPECTED_HISTORY_SHA = "7b34719788dc9ebe39ca5b02143a574fe7df2aad4991ce5a406b849d120cb5b2"
WIDTH = HEIGHT = 512

REGIONS = {
    "pale_gray_skin_headneck": {"label": "Pale exposed skin: face, ears, neck", "rgb": (35, 210, 255)},
    "black_hair": {"label": "Dark scalp hair", "rgb": (255, 148, 26)},
    "eyes_socket_margins": {"label": "Eyes and socket margins", "rgb": (235, 40, 220)},
    "teeth_mouth": {"label": "Mouth and teeth candidate", "rgb": (80, 235, 70)},
}
VIEWS = ("head_front", "head_left", "head_right", "head_rear")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_json(path):
    with open(path, "r", encoding="utf-8") as stream:
        return json.load(stream)


def atomic_json_new(path, obj):
    tmp = path.with_name(path.name + ".tmp-" + str(os.getpid()))
    with open(tmp, "x", encoding="utf-8", newline="\n") as stream:
        json.dump(obj, stream, sort_keys=True, indent=2, ensure_ascii=False)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())
    if read_json(tmp) != obj:
        raise RuntimeError("JSON sibling validation failed: " + str(tmp))
    os.replace(tmp, path)


def save_png_new(path, image):
    tmp = path.with_name(path.name + ".tmp-" + str(os.getpid()))
    image.save(tmp, format="PNG", optimize=False)
    with Image.open(tmp) as check:
        check.load()
        if check.size != image.size:
            raise RuntimeError("PNG sibling dimension check failed: " + str(tmp))
    os.replace(tmp, path)


def map_path_and_ids(preflight, view):
    entry = preflight["face_id_maps"][view]
    path = MODEL_ROOT / entry["path"]
    compressed = path.read_bytes()
    if hashlib.sha256(compressed).hexdigest() != entry["compressed_sha256"]:
        raise RuntimeError("compressed face-ID map hash mismatch: " + view)
    raw = zlib.decompress(compressed)
    if hashlib.sha256(raw).hexdigest() != entry["raw_sha256"]:
        raise RuntimeError("raw face-ID map hash mismatch: " + view)
    if len(raw) != WIDTH * HEIGHT * 2:
        raise RuntimeError("face-ID map has unexpected dimensions: " + view)
    ids = struct.unpack("<" + str(WIDTH * HEIGHT) + "H", raw)
    return path, raw, ids, entry


def expand_polygons(entry, view):
    result = []
    for polygon in entry["polygons"]:
        points = polygon
        if view == "head_right":
            points = [[WIDTH - 1 - int(point[0]), int(point[1])] for point in polygon]
        result.append(points)
    return result


def uv_triangle_area(points):
    return abs(
        points[0][0] * (points[1][1] - points[2][1])
        + points[1][0] * (points[2][1] - points[0][1])
        + points[2][0] * (points[0][1] - points[1][1])
    ) * 0.5


def main():
    root = MODEL_ROOT.parents[1]
    history_path = MODEL_ROOT / "history.jsonl"
    preflight_path = REGION_DIR / "source_uv_faceid_preflight.json"
    annotation_path = REGION_DIR / "head_region_annotations_draft_20261006.json"
    uv_bin_path = REGION_DIR / "source_face_uv_loops_20261006.bin"
    uv_meta_path = REGION_DIR / "source_face_uv_loops_20261006.json"
    correspondence_path = REGION_DIR / "source_to_runtime_triangle_uv_correspondence_20261006.json"
    source_path = MODEL_ROOT / "blender" / "checkpoints" / "06_exported.blend"
    uv_outline_path = REGION_DIR / "uv_outline_source_512.png"
    output_names = [
        "head_front_regions_draft_512.png",
        "head_left_regions_draft_512.png",
        "head_right_regions_draft_512.png",
        "head_rear_regions_draft_512.png",
        "head_uv_regions_draft_512.png",
        "head_mask_pale_gray_skin_headneck_512.png",
        "head_mask_black_hair_512.png",
        "head_mask_eyes_socket_margins_512.png",
        "head_mask_teeth_mouth_512.png",
        "head_region_faces_draft_20261006.json",
    ]
    outputs = [REGION_DIR / name for name in output_names]
    if any(path.exists() for path in outputs):
        raise RuntimeError("refusing to overwrite a pre-existing draft output")

    if sha256(source_path) != EXPECTED_SOURCE_SHA:
        raise RuntimeError("source checkpoint hash mismatch")
    if sha256(uv_bin_path) != read_json(uv_meta_path)["binary"]["sha256"]:
        raise RuntimeError("extracted UV loop binary hash mismatch")
    uv_receipt = read_json(uv_meta_path)
    if uv_receipt["uv"]["sha256_float32_xy_loop_order"] != EXPECTED_UV_SHA:
        raise RuntimeError("UV loop hash mismatch")
    if sha256(correspondence_path) != EXPECTED_CORRESPONDENCE_SHA:
        raise RuntimeError("source-to-runtime correspondence hash mismatch")
    if sha256(history_path) != EXPECTED_HISTORY_SHA:
        raise RuntimeError("parent correspondence review history hash mismatch")

    preflight = read_json(preflight_path)
    annotation = read_json(annotation_path)
    correspondence = read_json(correspondence_path)
    if preflight["source_checkpoint_sha256"] != EXPECTED_SOURCE_SHA:
        raise RuntimeError("preflight source hash mismatch")
    if preflight["runtime_mesh_sha256"] != EXPECTED_RUNTIME_SHA:
        raise RuntimeError("preflight runtime mesh hash mismatch")
    if preflight["uv_loop_coordinate_sha256"] != EXPECTED_UV_SHA:
        raise RuntimeError("preflight UV hash mismatch")
    if annotation["source_checkpoint"]["sha256"] != EXPECTED_SOURCE_SHA:
        raise RuntimeError("annotation source hash mismatch")
    if annotation["runtime_mesh"]["sha256"] != EXPECTED_RUNTIME_SHA:
        raise RuntimeError("annotation runtime hash mismatch")
    if annotation["uv"]["sha256"] != EXPECTED_UV_SHA:
        raise RuntimeError("annotation UV hash mismatch")
    if correspondence["comparison"]["matched_one_to_one_faces"] != 30474:
        raise RuntimeError("approved correspondence does not cover all source triangles")
    if correspondence["comparison"]["unmatched_source_face_ids"] or correspondence["comparison"]["ambiguous_source_faces"]:
        raise RuntimeError("source-to-runtime correspondence contains unmatched or ambiguous faces")
    face_map = {row["source_face_id"]: row["runtime_face_id"] for row in correspondence["source_to_runtime_face_id_map"]}
    if len(face_map) != 30474 or any(k != v for k, v in face_map.items()):
        raise RuntimeError("source-to-runtime face mapping is not one-to-one identity")

    vote_counts = defaultdict(Counter)
    vote_views = defaultdict(set)
    trace_pixel_counts = Counter()
    overlap_pixel_counts = Counter()
    view_records = {}
    selected_pixels_by_view = {}

    for view in VIEWS:
        view_annotations = annotation["views"].get(view)
        if view == "head_right":
            view_annotations = annotation["views"]["head_left"]
        if not view_annotations:
            raise RuntimeError("missing reviewed manual annotation for " + view)
        map_file, raw_map, face_ids, map_info = map_path_and_ids(preflight, view)
        source_path_view = MODEL_ROOT / preflight["source_views"][view]
        if not source_path_view.is_file():
            raise RuntimeError("source view missing: " + view)

        masks = {}
        for region in REGIONS:
            image = Image.new("L", (WIDTH, HEIGHT), 0)
            draw = ImageDraw.Draw(image)
            for annotation_entry in view_annotations:
                if annotation_entry["region_id"] == region:
                    for polygon in expand_polygons(annotation_entry, view):
                        draw.polygon(polygon, fill=255)
            masks[region] = image.tobytes()
        active = [0] * (WIDTH * HEIGHT)
        active_region = [None] * (WIDTH * HEIGHT)
        for region, mask_bytes in masks.items():
            for index, pixel in enumerate(mask_bytes):
                if pixel:
                    active[index] += 1
                    active_region[index] = region
                    trace_pixel_counts[(view, region)] += 1

        for index, val in enumerate(face_ids):
            if not val:
                continue
            active_count = active[index]
            if not active_count:
                continue
            if active_count > 1:
                overlap_pixel_counts[view] += 1
                continue
            face = val - 1
            region = active_region[index]
            vote_counts[face][region] += 1
            vote_views[(face, region)].add(view)
        view_records[view] = {
            "source_image": str(source_path_view.relative_to(MODEL_ROOT)).replace("\\", "/"),
            "source_image_sha256": sha256(source_path_view),
            "face_id_map": str(map_file.relative_to(MODEL_ROOT)).replace("\\", "/"),
            "face_id_map_raw_sha256": map_info["raw_sha256"],
            "face_id_map_compressed_sha256": map_info["compressed_sha256"],
            "manual_annotation_view": "head_left mirrored horizontally" if view == "head_right" else view,
            "overlapping_manual_region_pixels_excluded_from_face_votes": overlap_pixel_counts[view],
            "traced_region_pixels": {region: trace_pixel_counts[(view, region)] for region in REGIONS},
        }

    face_region = {}
    ambiguous_faces = {}
    for face, counts in vote_counts.items():
        if len(counts) == 1:
            face_region[face] = next(iter(counts))
        else:
            ambiguous_faces[face] = dict(sorted(counts.items()))

    face_sets = {region: sorted(face for face, value in face_region.items() if value == region) for region in REGIONS}
    runtime_sets = {region: sorted(face_map[face] for face in face_sets[region]) for region in REGIONS}

    with open(uv_bin_path, "rb") as stream:
        uv_records = stream.read()
    if len(uv_records) != 30474 * 28:
        raise RuntimeError("source face UV record length mismatch")
    uv_triangles = {}
    out_of_range_loop_count = 0
    for face, u0, v0, u1, v1, u2, v2 in struct.iter_unpack("<I6f", uv_records):
        if face in uv_triangles:
            raise RuntimeError("duplicate face in source UV records")
        uv_triangles[face] = ((u0, v0), (u1, v1), (u2, v2))
        out_of_range_loop_count += sum(not (0.0 <= u <= 1.0 and 0.0 <= v <= 1.0) for u, v in uv_triangles[face])
    if len(uv_triangles) != 30474:
        raise RuntimeError("source UV record face count mismatch")

    uv_masks = {}
    uv_area = {}
    zero_uv_area_faces = {}
    for region in REGIONS:
        mask = Image.new("L", (WIDTH, HEIGHT), 0)
        draw = ImageDraw.Draw(mask)
        area = 0.0
        zero = []
        for face in face_sets[region]:
            points_uv = uv_triangles[face]
            current_area = uv_triangle_area(points_uv)
            area += current_area
            if current_area == 0.0:
                zero.append(face)
            points_px = [(round(u * (WIDTH - 1)), round((1.0 - v) * (HEIGHT - 1))) for u, v in points_uv]
            draw.polygon(points_px, fill=255)
        uv_masks[region] = mask
        uv_area[region] = area
        zero_uv_area_faces[region] = zero

    mask_bytes = {region: uv_masks[region].tobytes() for region in REGIONS}
    uv_coverage_texels = {region: mask_bytes[region].count(255) for region in REGIONS}
    overlap_pixels = 0
    overlap_pairs = Counter()
    for index in range(WIDTH * HEIGHT):
        hit = [region for region in REGIONS if mask_bytes[region][index]]
        if len(hit) > 1:
            overlap_pixels += 1
            for i, first in enumerate(hit):
                for second in hit[i + 1:]:
                    overlap_pairs[tuple(sorted((first, second)))] += 1

    # Build 512x512 grayscale class masks and 512-wide labelled evidence canvases.
    for region, image in uv_masks.items():
        save_png_new(REGION_DIR / ("head_mask_" + region + "_512.png"), image)

    font = ImageFont.load_default()
    for view in VIEWS:
        _, _, face_ids, _ = map_path_and_ids(preflight, view)
        source_image_path = MODEL_ROOT / preflight["source_views"][view]
        with Image.open(source_image_path) as src:
            base = src.convert("RGBA")
        layer = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
        pixels = layer.load()
        for index, val in enumerate(face_ids):
            if val:
                region = face_region.get(val - 1)
                if region:
                    x, y = index % WIDTH, index // WIDTH
                    pixels[x, y] = (*REGIONS[region]["rgb"], 128)
        display = Image.alpha_composite(base, layer).convert("RGB")
        canvas = Image.new("RGB", (WIDTH, HEIGHT + 78), (18, 21, 25))
        canvas.paste(display, (0, 30))
        d = ImageDraw.Draw(canvas)
        d.text((8, 8), view.upper() + " | EXACT FACE-ID REGION DRAFT", fill=(245, 245, 245), font=font)
        for i, region in enumerate(REGIONS):
            x = 8 + (i % 2) * 252
            y = HEIGHT + 37 + (i // 2) * 18
            rgb = REGIONS[region]["rgb"]
            count = len(face_sets[region])
            d.rectangle((x, y + 2, x + 10, y + 12), fill=rgb)
            d.text((x + 15, y), REGIONS[region]["label"] + " | " + str(count) + " faces", fill=(235, 235, 235), font=font)
        save_png_new(REGION_DIR / (view + "_regions_draft_512.png"), canvas)

    with Image.open(uv_outline_path) as src:
        atlas = src.convert("RGBA")
    layer = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    layer_pixels = layer.load()
    for index in range(WIDTH * HEIGHT):
        hit = [region for region in REGIONS if mask_bytes[region][index]]
        if len(hit) > 1:
            layer_pixels[index % WIDTH, index // WIDTH] = (255, 255, 0, 220)
        elif hit:
            layer_pixels[index % WIDTH, index // WIDTH] = (*REGIONS[hit[0]]["rgb"], 150)
    atlas = Image.alpha_composite(atlas, layer).convert("RGB")
    canvas = Image.new("RGB", (WIDTH, HEIGHT + 86), (15, 17, 20))
    canvas.paste(atlas, (0, 28))
    d = ImageDraw.Draw(canvas)
    d.text((8, 8), "UV ATLAS | IDENTITY UV | DRAFT | YELLOW = CROSS-CLASS UV OVERLAP", fill=(245, 245, 245), font=font)
    for i, region in enumerate(REGIONS):
        x = 8 + (i % 2) * 252
        y = HEIGHT + 35 + (i // 2) * 18
        rgb = REGIONS[region]["rgb"]
        d.rectangle((x, y + 2, x + 10, y + 12), fill=rgb)
        d.text((x + 15, y), REGIONS[region]["label"] + " | " + str(uv_coverage_texels[region]) + " texels", fill=(235, 235, 235), font=font)
    save_png_new(REGION_DIR / "head_uv_regions_draft_512.png", canvas)

    face_records = {}
    for region in REGIONS:
        ids = face_sets[region]
        view_counts = Counter()
        selected_view_pixels = Counter()
        for face in ids:
            for view in vote_views[(face, region)]:
                view_counts[view] += 1
        for view in VIEWS:
            _, _, face_ids, _ = map_path_and_ids(preflight, view)
            selected_view_pixels[view] = sum(1 for val in face_ids if val and face_region.get(val - 1) == region)
        mask_path = REGION_DIR / ("head_mask_" + region + "_512.png")
        face_records[region] = {
            "label": REGIONS[region]["label"],
            "source_face_ids": ids,
            "runtime_face_ids": runtime_sets[region],
            "source_face_count": len(ids),
            "source_views_with_votes": dict(sorted(view_counts.items())),
            "projected_source_view_pixels": dict(sorted(selected_view_pixels.items())),
            "uv_pixel_coverage": uv_coverage_texels[region],
            "uv_pixel_coverage_fraction": uv_coverage_texels[region] / (WIDTH * HEIGHT),
            "uv_triangle_area_sum_in_uv_square_units": uv_area[region],
            "uv_degenerate_face_ids": zero_uv_area_faces[region],
            "mask_path": str(mask_path.relative_to(MODEL_ROOT)).replace("\\", "/"),
            "mask_sha256": sha256(mask_path),
        }

    evidence = {
        "schema_version": 1,
        "status": "draft_parent_visual_review_required",
        "scope": "head slice only; no topology, geometry, rig, weights, UVs, actions, material recipe, or runtime files modified",
        "source_checkpoint": {"path": "blender/checkpoints/06_exported.blend", "sha256": EXPECTED_SOURCE_SHA},
        "runtime_mesh": {"path": "export/v2/chaosx_undead_zombies.mesh", "sha256": EXPECTED_RUNTIME_SHA},
        "uv": {"layer": "UVMap", "sha256": EXPECTED_UV_SHA, "runtime_layer": "map1", "transform": "identity"},
        "correspondence": {
            "report_path": "blender/evidence/regions/source_to_runtime_triangle_uv_correspondence_20261006.json",
            "report_sha256": EXPECTED_CORRESPONDENCE_SHA,
            "parent_review_record": "history.jsonl",
            "parent_review_record_sha256": EXPECTED_HISTORY_SHA,
            "review_scope": "all 30474 source faces map one-to-one to runtime triangles with identity UV; no unmatched or ambiguous IDs",
            "review_does_not_approve": ["semantic masks", "AO", "winding or normals", "weights", "actions", "runtime appearance or installation"],
        },
        "annotation": {
            "path": "blender/evidence/regions/head_region_annotations_draft_20261006.json",
            "sha256": sha256(annotation_path),
            "method": "manually traced polygons on reviewed 512 source renders, resolved only through matching raycast face-ID maps",
            "right_profile": "horizontal mirror of the manually traced left profile; face-ID map independently captured from the right source view",
            "deferred_geometry_review": annotation["deferred_geometry_review_note"],
        },
        "uv_loop_data": {
            "path": "blender/evidence/regions/source_face_uv_loops_20261006.bin",
            "sha256": sha256(uv_bin_path),
            "receipt_path": "blender/evidence/regions/source_face_uv_loops_20261006.json",
            "receipt_sha256": sha256(uv_meta_path),
            "face_records": len(uv_triangles),
            "out_of_range_loop_count": out_of_range_loop_count,
        },
        "views": view_records,
        "manual_trace_overlap_pixels_excluded": dict(sorted(overlap_pixel_counts.items())),
        "ambiguous_source_face_ids_excluded": {str(face): counts for face, counts in sorted(ambiguous_faces.items())},
        "regions": face_records,
        "cross_class_uv_overlap": {
            "texel_count": overlap_pixels,
            "class_pair_texel_counts": {"|".join(pair): count for pair, count in sorted(overlap_pairs.items())},
            "highlighted_yellow_in_overlay": True,
        },
        "special_review": {
            "teeth_mouth": "conditional candidate only; exact semantic separability and boundary remain for parent review",
            "ear_scalp_shards": "deferred and unclassified",
            "accepted_semantic_masks": False,
            "runtime_installation": False,
        },
        "visual_outputs": {},
    }
    for name in output_names[:-1]:
        path = REGION_DIR / name
        with Image.open(path) as image:
            evidence["visual_outputs"][name] = {"path": str(path.relative_to(MODEL_ROOT)).replace("\\", "/"), "sha256": sha256(path), "dimensions": list(image.size), "mode": image.mode}
    manifest_path = REGION_DIR / output_names[-1]
    atomic_json_new(manifest_path, evidence)
    print(json.dumps({"status": evidence["status"], "regions": {key: {"faces": value["source_face_count"], "uv_texels": value["uv_pixel_coverage"]} for key, value in face_records.items()}, "ambiguous_face_count": len(ambiguous_faces), "manual_trace_overlap_pixels": dict(overlap_pixel_counts), "cross_class_uv_overlap_texels": overlap_pixels, "manifest": str(manifest_path.relative_to(MODEL_ROOT)).replace("\\", "/"), "manifest_sha256": sha256(manifest_path)}, sort_keys=True))


if __name__ == "__main__":
    main()
