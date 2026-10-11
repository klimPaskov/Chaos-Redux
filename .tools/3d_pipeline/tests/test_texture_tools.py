"""Focused tests for texture encoding, PDX conventions, and CAS delivery."""

from __future__ import annotations

import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest

from PIL import Image

PIPELINE = Path(__file__).resolve().parents[1]
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

from textures import bc_codec
from textures.atlas import dilate_from_occupancy, load_occupancy_mask
from textures.conventions import (
    gate_normal,
    gate_specular,
    packed_normal_cleanup,
    repack_provider_normal,
    build_pdx_specular_from_provider,
    resolve_material_recipes,
)
from textures.dds import DdsError, decode_mip_rgba, parse_dds_header
from textures.delivery import (
    TextureDeliveryError,
    convert_batch,
    install_batch,
    prepare_batch,
    resolve_uv_mask,
    sha256_file,
)


def _make_request(root, *, source_rel, target_rel, mask_rel, batch_id="unit_texture_test", **item_options):
    request = {
        "batch_id": batch_id,
        "items": [
            {
                "id": "body_diffuse",
                "role": "diffuse",
                "source_rel": source_rel,
                "target_rel": target_rel,
                "occupancy_mask_rel": mask_rel,
                "dilation_px": 8,
                "conversion_scope": "compression_only",
                **item_options,
            }
        ],
    }
    path = root / "request.json"
    path.write_text(json.dumps(request, indent=2), encoding="utf-8")
    return path


def _occupancy(size, bounds=None):
    mask = Image.new("L", size, 0)
    if bounds is None:
        mask.paste(255, (0, 0, size[0], size[1]))
    else:
        mask.paste(255, bounds)
    return mask


class TextureDdsTests(unittest.TestCase):
    def test_t062_four_by_four_bc1_mip_uses_channel_balanced_endpoint_search(self):
        # These four source colors repeat across the exact prepared t062 mip 7.
        image = Image.new("RGBA", (4, 4))
        colors = [
            (68, 76, 74, 255),
            (138, 117, 70, 255),
            (38, 55, 48, 255),
            (41, 208, 222, 255),
        ]
        image.putdata(colors * 4)
        encoded, mips = bc_codec.build_dds(image, "BC1_UNORM")
        header = parse_dds_header(encoded, min_dimension=4, max_dimension=1024)
        decoded = decode_mip_rgba(encoded, header, 0)
        metrics = bc_codec.encode_metrics(image, decoded)
        self.assertEqual(len(mips), 3)
        self.assertLessEqual(metrics["channels"]["R"]["mae"], 32.0)
        self.assertLessEqual(max(metrics["channels"][channel]["mae"] for channel in "RGB"), 32.0)
        self.assertGreaterEqual(metrics["rgb_psnr_db"], 15.0)

    def test_native_bc_encoders_write_complete_legacy_mips_and_pillow_pixels(self):
        source = Image.new("RGBA", (16, 16))
        pixels = []
        for y in range(16):
            for x in range(16):
                pixels.append((x * 16, y * 16, (x + y) * 8, 255 if (x + y) % 2 else 176))
        source.putdata(pixels)
        for format_name in ("BC1_UNORM", "BC3_UNORM"):
            image = source if format_name == "BC3_UNORM" else Image.new("RGBA", (16, 16), (50, 90, 120, 255))
            first, chain = bc_codec.build_dds(image, format_name)
            second, _ = bc_codec.build_dds(image, format_name)
            self.assertEqual(first, second)
            header = parse_dds_header(first, min_dimension=4, max_dimension=1024)
            self.assertEqual(header.format_name, format_name)
            self.assertEqual(header.mip_count, 5)
            self.assertEqual(len(chain), header.mip_count)
            self.assertEqual(decode_mip_rgba(first, header, 4).size, (1, 1))
            with Image.open(io.BytesIO(first)) as decoded:
                decoded.load()
                self.assertEqual(decoded.size, (16, 16))
                self.assertEqual(decoded.convert("RGBA").tobytes(), decode_mip_rgba(first, header).tobytes())

    def test_header_gate_rejects_wrong_fourcc_short_payload_and_missing_mips(self):
        image = Image.new("RGBA", (16, 16), (80, 110, 130, 255))
        data, _ = bc_codec.build_dds(image, "BC1_UNORM")
        broken_format = bytearray(data)
        broken_format[84:88] = b"DXT5"
        with self.assertRaises(DdsError):
            parse_dds_header(bytes(broken_format), min_dimension=4, max_dimension=1024)
        with self.assertRaises(DdsError):
            parse_dds_header(data[:-1], min_dimension=4, max_dimension=1024)
        broken_mips = bytearray(data)
        broken_mips[28:32] = (1).to_bytes(4, "little")
        with self.assertRaises(DdsError):
            parse_dds_header(bytes(broken_mips), min_dimension=4, max_dimension=1024)
        missing_texture_caps = bytearray(data)
        missing_texture_caps[108:112] = (0).to_bytes(4, "little")
        with self.assertRaises(DdsError):
            parse_dds_header(bytes(missing_texture_caps), min_dimension=4, max_dimension=1024)

    def test_diffuse_bc1_rejects_nonopaque_alpha(self):
        image = Image.new("RGBA", (4, 4), (20, 40, 60, 254))
        with self.assertRaises(ValueError):
            bc_codec.encode_bc_level(image, "BC1_UNORM")

    def test_legacy_bgra_input_decodes_to_rgba(self):
        width = height = 128
        header = bytearray(128)
        header[:4] = b"DDS "
        for offset, value in ((4, 124), (8, 0x100F), (12, height), (16, width), (20, width * 4), (76, 32), (80, 65), (108, 0x1000)):
            header[offset:offset + 4] = value.to_bytes(4, "little")
        for offset, value in ((88, 32), (92, 0x00FF0000), (96, 0x0000FF00), (100, 0x000000FF), (104, 0xFF000000)):
            header[offset:offset + 4] = value.to_bytes(4, "little")
        pixels = bytes((11, 22, 33, 44)) * (width * height)
        data = bytes(header) + pixels
        parsed = parse_dds_header(
            data,
            require_full_mips=False,
            min_dimension=128,
            max_dimension=1024,
            allow_uncompressed_bgra=True,
        )
        decoded = decode_mip_rgba(data, parsed)
        self.assertEqual(parsed.format_name, "BGRA8")
        self.assertEqual(decoded.getpixel((0, 0)), (33, 22, 11, 44))


class AtlasAndConventionTests(unittest.TestCase):
    def test_dilation_uses_explicit_occupancy_even_when_valid_art_is_black(self):
        image = Image.new("RGBA", (9, 5), (0, 0, 0, 255))
        image.putpixel((4, 2), (10, 40, 90, 255))
        mask = Image.new("L", (9, 5), 0)
        mask.putpixel((4, 2), 255)
        output, report = dilate_from_occupancy(image, mask, 2, channels=(0, 1, 2))
        self.assertEqual(output.getpixel((2, 2)), (10, 40, 90, 255))
        self.assertEqual(output.getpixel((0, 0)), (0, 0, 0, 255))
        self.assertEqual(report["filled_pixels"], 24)
        with self.assertRaises(ValueError):
            load_occupancy_mask(Image.new("RGB", (2, 2), (10, 0, 0)))

    def test_provider_normal_repack_preserves_green_by_default_and_can_only_flip_explicitly(self):
        source = Image.new("RGBA", (2, 1))
        source.putdata([(16, 64, 99, 255), (210, 128, 30, 255)])
        packed, report = repack_provider_normal(source)
        self.assertEqual(list(packed.getdata()), [(16, 16, 0, 64), (210, 210, 0, 128)])
        self.assertEqual(report["detail_synthesized"], False)
        flipped, _ = repack_provider_normal(source, green_sign="invert")
        self.assertEqual(flipped.getpixel((0, 0)), (16, 16, 0, 191))

    def test_existing_normal_cleanup_preserves_occupied_ga_and_neutralizes_padding(self):
        source = Image.new("RGBA", (5, 3))
        source.putdata([(9, 100 + index, 77, 130 + index) for index in range(15)])
        mask = Image.new("L", source.size, 0)
        mask.putpixel((2, 1), 255)
        repaired, report = packed_normal_cleanup(source, mask, dilation_px=1)
        self.assertEqual(repaired.getpixel((2, 1)), (source.getpixel((2, 1))[1], source.getpixel((2, 1))[1], 0, source.getpixel((2, 1))[3]))
        self.assertEqual(repaired.getpixel((0, 0)), (128, 128, 0, 128))
        self.assertTrue(report["occupied_green_alpha_preserved"])

    def test_normal_gate_requires_variation_and_bounded_tangent_tilt(self):
        image = Image.new("RGBA", (4, 4))
        values = []
        for index in range(16):
            x = 105 if index % 2 else 151
            y = 112 if index % 3 else 145
            values.append((x, x, 0, y))
        image.putdata(values)
        mask = Image.new("L", image.size, 255)
        self.assertEqual(gate_normal(image, mask)["status"], "passed")
        self.assertEqual(gate_normal(Image.new("RGBA", image.size, (128, 128, 0, 128)), mask)["status"], "failed")

    def test_class_recipes_use_masks_and_provider_maps_with_skin_gloss_exception(self):
        size = (6, 1)
        roughness = Image.new("L", size)
        roughness.putdata([230, 170, 125, 30, 75, 220])
        metalness = Image.new("L", size, 0)
        class_masks = {}
        classes = {"cloth": (0, 1), "skin": (2,), "steel": (3,), "stone": (4,), "fur": (5,)}
        for class_name, indices in classes.items():
            mask = Image.new("L", size, 0)
            data = [255 if index in indices else 0 for index in range(6)]
            mask.putdata(data)
            class_masks[class_name] = mask
        occupancy = Image.new("L", size, 255)
        packed, report = build_pdx_specular_from_provider(roughness, metalness, class_masks, occupancy)
        self.assertEqual(report["nonmetal_blue_channel_clamped_without_mask"], False)
        self.assertEqual(packed.getpixel((3, 0))[1] >= 180, True)
        gate = gate_specular(packed, occupancy, class_masks)
        self.assertEqual(gate["status"], "passed", gate["failures"])
        self.assertGreater(packed.getpixel((2, 0))[3], 110)  # explicit skin class recipe

    def test_specular_blue_is_masked_outside_steel_and_steel_keeps_provider_variation_above_200(self):
        size = (6, 1)
        roughness = Image.new("L", size)
        roughness.putdata([230, 180, 140, 100, 50, 25])
        metalness = Image.new("L", size)
        metalness.putdata([230, 128, 40, 0, 180, 255])
        original_metalness = metalness.tobytes()
        cloth_mask = Image.new("L", size, 0)
        cloth_mask.putdata([255, 255, 255, 255, 0, 0])
        steel_mask = Image.new("L", size, 0)
        steel_mask.putdata([0, 0, 0, 0, 255, 255])
        occupancy = Image.new("L", size, 255)
        source_hashes = {
            "roughness": {"path_rel": "source/roughness.png", "sha256": "a" * 64},
            "metalness": {"path_rel": "source/metalness.png", "sha256": "b" * 64},
            "material_masks": {
                "cloth": {"path_rel": "masks/cloth.png", "sha256": "c" * 64},
                "steel": {"path_rel": "masks/steel.png", "sha256": "d" * 64},
            },
        }
        packed, report = build_pdx_specular_from_provider(
            roughness,
            metalness,
            {"cloth": cloth_mask, "steel": steel_mask},
            occupancy,
            source_hashes=source_hashes,
        )
        self.assertEqual([packed.getpixel((x, 0))[2] for x in range(6)], [0, 0, 0, 0, 200, 255])
        self.assertEqual(metalness.tobytes(), original_metalness)
        blue_report = report["blue_channel_masking"]
        self.assertEqual(blue_report["occupied_pixels_changed_from_original_provider_metalness"], 4)
        self.assertFalse(blue_report["provider_maps_modified"])
        self.assertEqual(report["original_provider_input_hashes"], source_hashes)
        self.assertEqual(gate_specular(packed, occupancy, {"cloth": cloth_mask, "steel": steel_mask})["status"], "passed")

        below_band = packed.copy()
        pixels = list(below_band.getdata())
        pixels[4] = (pixels[4][0], pixels[4][1], 199, pixels[4][3])
        below_band.putdata(pixels)
        self.assertTrue(any("steel blue/metalness has a value below the 200 minimum" in failure
                            for failure in gate_specular(below_band, occupancy, {"cloth": cloth_mask, "steel": steel_mask})["failures"]))
        self.assertEqual(
            gate_specular(
                below_band,
                occupancy,
                {"cloth": cloth_mask, "steel": steel_mask},
                steel_blue_tolerance=5,
            )["status"],
            "passed",
        )

    def test_specular_gate_rejects_flat_green_and_blue_leak_outside_steel(self):
        size = (4, 1)
        occupancy = Image.new("L", size, 255)
        cloth = Image.new("L", size, 255)
        steel = Image.new("L", size, 0)
        masks = {"cloth": cloth, "steel": steel}
        flat = Image.new("RGBA", size, (0, 50, 0, 80))
        self.assertTrue(any("standard deviation is zero" in x for x in gate_specular(flat, occupancy, masks)["failures"]))
        leaked = Image.new("RGBA", size, (0, 50, 40, 80))
        self.assertTrue(any("outside the explicit steel mask" in x for x in gate_specular(leaked, occupancy, masks)["failures"]))

    def test_bone_magma_and_worn_steel_keep_physical_ranges_and_metal_union(self):
        size = (5, 1)
        roughness = Image.new("L", size)
        roughness.putdata([0, 100, 150, 200, 255])
        metalness = Image.new("L", size)
        metalness.putdata([255, 255, 255, 230, 255])
        originals = (roughness.tobytes(), metalness.tobytes())
        masks = {}
        for name, indices in {"bone": (0, 1), "steel": (2,), "worn_steel": (3,), "magma": (4,)}.items():
            mask = Image.new("L", size)
            mask.putdata([255 if index in indices else 0 for index in range(5)])
            masks[name] = mask
        occupancy = Image.new("L", size, 255)
        packed, report = build_pdx_specular_from_provider(roughness, metalness, masks, occupancy)
        self.assertEqual(list(packed.getdata()), [(0, 140, 0, 100), (0, 128, 0, 100),
                                               (0, 211, 255, 150), (0, 156, 230, 70), (0, 140, 0, 70)])
        self.assertEqual(report["metal_classes"], ["steel", "worn_steel"])
        self.assertEqual(gate_specular(packed, occupancy, masks)["status"], "passed")
        self.assertEqual((roughness.tobytes(), metalness.tobytes()), originals)
        leaked = packed.copy()
        leaked.putpixel((0, 0), (0, 140, 30, 100))
        self.assertEqual(gate_specular(leaked, occupancy, masks)["status"], "failed")

    def test_explicit_calibration_preserves_defaults_and_rejects_invalid_ranges(self):
        before = resolve_material_recipes()
        calibrated = resolve_material_recipes({"stone": {"alpha": [70, 100]}})
        self.assertEqual(calibrated["stone"]["alpha"], (70, 100))
        self.assertEqual(resolve_material_recipes(), before)
        for override in ({"unknown": {"green": [1, 2]}}, {"bone": {"alpha": [100, 70]}},
                         {"bone": {"alpha": [0.0, 100]}}, {"bone": {"blue": [0, 255]}}):
            with self.assertRaises(ValueError):
                resolve_material_recipes(override)


class TextureDeliveryTests(unittest.TestCase):
    def _make_root(self):
        temp_root = tempfile.TemporaryDirectory(prefix="chaosx_texture_test_")
        self.addCleanup(temp_root.cleanup)
        root = Path(temp_root.name)
        (root / "source").mkdir()
        (root / "runtime").mkdir()
        (root / "evidence").mkdir()
        return root

    def test_plan_and_convert_are_staging_only_and_manifest_binds_hashes(self):
        root = self._make_root()
        source = Image.new("RGBA", (128, 128))
        source.putdata([(x % 256, y % 256, (x + y) % 256, 255) for y in range(128) for x in range(128)])
        source_path = root / "source" / "diffuse.png"
        source.save(source_path)
        mask_path = root / "evidence" / "occupancy.png"
        _occupancy(source.size, (16, 16, 112, 112)).save(mask_path)
        target_path = root / "runtime" / "diffuse.dds"
        request = _make_request(
            root,
            source_rel="source/diffuse.png",
            target_rel="runtime/diffuse.dds",
            mask_rel="evidence/occupancy.png",
        )
        manifest_path = root / "evidence" / "cas.json"
        before_source = sha256_file(source_path)
        plan = prepare_batch(root, request, "staging", manifest_path)
        self.assertEqual(plan["state"], "prepared")
        self.assertEqual(plan["items"][0]["planned_format"], "BC1_UNORM")
        dry_run = convert_batch(root, manifest_path, execute=False)
        self.assertEqual(dry_run["status"], "dry_run")
        self.assertFalse((root / "staging").exists())
        self.assertEqual(sha256_file(source_path), before_source)
        converted = convert_batch(root, manifest_path, execute=True)
        self.assertEqual(converted["state"], "staged", converted["conversion"])
        item = converted["items"][0]
        self.assertTrue(item["converted"]["qa"]["install_eligible"])
        self.assertEqual(item["converted"]["source_archive_sha256"], before_source)
        self.assertEqual(sha256_file(source_path), before_source)
        self.assertEqual(item["converted"]["qa"]["dds"]["format"], "BC1_UNORM")
        self.assertEqual(item["converted"]["qa"]["dds"]["mip_count"], 8)

    def test_install_cas_rejects_changed_target_without_overwriting_it(self):
        root = self._make_root()
        pixels = Image.new("RGBA", (128, 128), (60, 90, 125, 255))
        source_path = root / "source" / "body.dds"
        source_path.write_bytes(bc_codec.build_dds(pixels, "BC1_UNORM")[0])
        mask_path = root / "evidence" / "occupancy.png"
        _occupancy((128, 128), (8, 8, 120, 120)).save(mask_path)
        request = _make_request(
            root,
            source_rel="source/body.dds",
            target_rel="source/body.dds",
            mask_rel="evidence/occupancy.png",
            batch_id="cas_conflict",
            alpha_used=False,
        )
        manifest_path = root / "evidence" / "cas_conflict.json"
        original_sha = sha256_file(source_path)
        prepare_batch(root, request, "staging", manifest_path)
        staged = convert_batch(root, manifest_path, execute=True)
        self.assertEqual(staged["state"], "staged", staged["conversion"])
        dry = install_batch(root, manifest_path, execute=False)
        self.assertEqual(dry["status"], "dry_run")
        self.assertEqual(sha256_file(source_path), original_sha)
        source_path.write_bytes(b"concurrent edit")
        changed_sha = sha256_file(source_path)
        with self.assertRaises(TextureDeliveryError):
            install_batch(root, manifest_path, execute=True)
        self.assertEqual(sha256_file(source_path), changed_sha)

    def test_pdx_normal_evidence_runs_masked_semantic_gate_during_compression_only(self):
        root = self._make_root()
        source = Image.new("RGBA", (128, 128))
        source.putdata([
            (
                108 if x % 2 else 148,
                108 if x % 2 else 148,
                0,
                108 if y % 2 else 148,
            )
            for y in range(128)
            for x in range(128)
        ])
        source_path = root / "source" / "body_normal.png"
        source.save(source_path)
        mask_path = root / "evidence" / "normal_occupancy.png"
        _occupancy(source.size).save(mask_path)
        provenance = {
            "kind": "pdx_packed_normal_evidence",
            "source": {"path_rel": "source/body_normal.png", "sha256": sha256_file(source_path)},
        }
        provenance_path = root / "evidence" / "normal_provenance.json"
        provenance_path.write_text(json.dumps(provenance), encoding="utf-8")
        request = _make_request(
            root,
            source_rel="source/body_normal.png",
            target_rel="runtime/body_normal.dds",
            mask_rel="evidence/normal_occupancy.png",
            batch_id="pdx_normal_evidence",
            role="normal",
            provenance_rel="evidence/normal_provenance.json",
        )
        # _make_request's fixed role is diffuse; specialize the item for this contract.
        request_data = json.loads(request.read_text(encoding="utf-8"))
        request_data["items"][0]["role"] = "normal"
        request.write_text(json.dumps(request_data), encoding="utf-8")
        manifest_path = root / "evidence" / "normal_cas.json"
        prepare_batch(root, request, "staging", manifest_path)
        converted = convert_batch(root, manifest_path, execute=True)
        self.assertEqual(converted["state"], "staged", converted.get("conversion"))
        qa = converted["items"][0]["converted"]["qa"]
        self.assertEqual(qa["material_semantic_gate"]["status"], "passed")
        self.assertTrue(qa["install_eligible"])

    def test_provider_specular_batch_report_binds_inputs_and_masks_nonmetal_blue(self):
        root = self._make_root()
        size = (128, 128)
        roughness = Image.new("L", size)
        metalness = Image.new("L", size)
        cloth = Image.new("L", size, 0)
        steel = Image.new("L", size, 0)
        rough_values = []
        metal_values = []
        cloth_values = []
        steel_values = []
        for y in range(128):
            for x in range(128):
                if x < 64:
                    rough_values.append(50 + (x % 64) * 2)
                    metal_values.append(80 if x % 3 == 0 else 0)
                    cloth_values.append(255)
                    steel_values.append(0)
                else:
                    rough_values.append(20 + (x - 64) * 2)
                    metal_values.append(160 + ((x - 64) % 96))
                    cloth_values.append(0)
                    steel_values.append(255)
        roughness.putdata(rough_values)
        metalness.putdata(metal_values)
        cloth.putdata(cloth_values)
        steel.putdata(steel_values)
        inputs = {
            "roughness": ("source/roughness.png", roughness),
            "metalness": ("source/metalness.png", metalness),
            "cloth": ("evidence/cloth.png", cloth),
            "steel": ("evidence/steel.png", steel),
        }
        input_rows = {}
        original_hashes = {}
        for name, (rel, image) in inputs.items():
            path = root / rel
            image.save(path)
            digest = sha256_file(path)
            original_hashes[rel] = digest
            input_rows[name] = {"path_rel": rel, "sha256": digest}
        occupancy_path = root / "evidence" / "occupancy.png"
        _occupancy(size).save(occupancy_path)
        provenance = {
            "kind": "provider_pbr_specular",
            "roughness": input_rows["roughness"],
            "metalness": input_rows["metalness"],
            "material_masks": {
                "cloth": input_rows["cloth"],
                "steel": input_rows["steel"],
            },
            "material_recipe_overrides": {
                "cloth": {"green": [45, 80], "alpha": [70, 95]},
                "steel": {"green": [150, 180], "alpha": [70, 100]},
            },
        }
        provenance_path = root / "evidence" / "provider_materials.json"
        provenance_path.write_text(json.dumps(provenance), encoding="utf-8")
        request = _make_request(
            root,
            source_rel="source/roughness.png",
            target_rel="runtime/body_spec.dds",
            mask_rel="evidence/occupancy.png",
            batch_id="provider_specular_masked",
            role="specular",
            conversion_scope="provider_specular_recipe",
            provenance_rel="evidence/provider_materials.json",
        )
        manifest_path = root / "evidence" / "provider_specular_cas.json"
        prepare_batch(root, request, "staging", manifest_path)
        converted = convert_batch(root, manifest_path, execute=True)
        self.assertEqual(converted["state"], "staged", converted.get("conversion"))
        item = converted["items"][0]
        self.assertEqual(item["converted"]["qa"]["material_semantic_gate"]["status"], "passed")
        self.assertEqual(item["converted"]["processing"]["recipe_overrides"],
                         provenance["material_recipe_overrides"])
        blue_report = item["converted"]["processing"]["blue_channel_masking"]
        self.assertEqual(blue_report["outside_steel"], 0)
        self.assertTrue(blue_report["inside_steel"].startswith("max(200"))
        self.assertGreater(blue_report["occupied_pixels_changed_from_original_provider_metalness"], 0)
        recorded_hashes = item["converted"]["processing"]["original_provider_input_hashes"]
        self.assertEqual(recorded_hashes["roughness"]["sha256"], original_hashes["source/roughness.png"])
        self.assertEqual(recorded_hashes["metalness"]["sha256"], original_hashes["source/metalness.png"])
        for rel, digest in original_hashes.items():
            self.assertEqual(sha256_file(root / rel), digest)

    def test_in_place_cas_install_keeps_original_sha_in_archive(self):
        root = self._make_root()
        source = Image.new("RGBA", (128, 128))
        source.putdata([(x, y, (x + y) // 2, 255) for y in range(128) for x in range(128)])
        source_path = root / "source" / "inplace.dds"
        source_path.write_bytes(bc_codec.build_dds(source, "BC1_UNORM")[0])
        mask_path = root / "evidence" / "occupancy.png"
        _occupancy((128, 128), (16, 16, 112, 112)).save(mask_path)
        request = _make_request(
            root,
            source_rel="source/inplace.dds",
            target_rel="source/inplace.dds",
            mask_rel="evidence/occupancy.png",
            batch_id="inplace_cas",
            alpha_used=False,
        )
        manifest_path = root / "evidence" / "inplace.json"
        original_sha = sha256_file(source_path)
        prepare_batch(root, request, "staging", manifest_path)
        staged = convert_batch(root, manifest_path, execute=True)
        self.assertEqual(staged["state"], "staged", staged["conversion"])
        installed = install_batch(root, manifest_path, execute=True)
        self.assertEqual(installed["state"], "installed")
        self.assertEqual(sha256_file(source_path), installed["items"][0]["converted"]["stage_dds_sha256"])
        archive = root / installed["items"][0]["source_archive_rel"]
        self.assertEqual(sha256_file(archive), original_sha)

    def test_1024_requires_justification_and_no_upscale_is_enforced(self):
        root = self._make_root()
        image = Image.new("RGBA", (128, 128), (40, 50, 60, 255))
        source_path = root / "source" / "small.png"
        image.save(source_path)
        mask_path = root / "evidence" / "mask.png"
        _occupancy(image.size).save(mask_path)
        request = _make_request(
            root,
            source_rel="source/small.png",
            target_rel="runtime/small.dds",
            mask_rel="evidence/mask.png",
            batch_id="no_upscale",
            size=1024,
            size_justification="A documented comparison shows the original atlas is already 128px and must not be enlarged.",
        )
        plan = prepare_batch(root, request, "staging", root / "evidence" / "no_upscale.json")
        self.assertEqual(plan["items"][0]["output_size"], 128)

    def test_diffuse_auto_alpha_selects_bc3_only_when_pixels_use_alpha(self):
        root = self._make_root()
        image = Image.new("RGBA", (128, 128), (40, 50, 60, 255))
        image.putpixel((64, 64), (40, 50, 60, 128))
        source_path = root / "source" / "alpha_diffuse.png"
        image.save(source_path)
        mask_path = root / "evidence" / "alpha_mask.png"
        _occupancy(image.size).save(mask_path)
        request = _make_request(
            root,
            source_rel="source/alpha_diffuse.png",
            target_rel="runtime/alpha_diffuse.dds",
            mask_rel="evidence/alpha_mask.png",
            batch_id="alpha_diffuse",
        )
        plan = prepare_batch(root, request, "staging", root / "evidence" / "alpha_cas.json")
        self.assertEqual(plan["items"][0]["planned_format"], "BC3_UNORM")
        self.assertTrue(plan["items"][0]["alpha_used"])

    def test_uv_mask_manifest_resolver_verifies_mesh_registration_and_file_sha(self):
        root = self._make_root()
        mask_path = root / "evidence" / "uv.png"
        _occupancy((128, 128), (10, 10, 100, 100)).save(mask_path)
        row = {
            "texture": "unit_diffuse.dds",
            "mask": "evidence/uv.png",
            "sha256": sha256_file(mask_path),
            "mesh_sha256": "a" * 64,
            "registration_sha256": "b" * 64,
            "coverage": 8100 / 16384,
            "size": 128,
        }
        path = root / "evidence" / "masks.json"
        path.write_text(json.dumps([{"pdxmesh": "unit_mesh", "masks": [row], "issues": []}]), encoding="utf-8")
        resolved = resolve_uv_mask(
            root,
            path,
            "unit_mesh",
            "unit_diffuse.dds",
            expected_mesh_sha256="a" * 64,
            expected_registration_sha256="b" * 64,
        )
        self.assertEqual(resolved["mask_rel"], "evidence/uv.png")
        self.assertEqual(resolved["sha256"], row["sha256"])
        with self.assertRaises(TextureDeliveryError):
            resolve_uv_mask(root, path, "unit_mesh", "unit_diffuse.dds", expected_mesh_sha256="c" * 64)


if __name__ == "__main__":
    unittest.main()
