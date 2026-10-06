# 3D model texture tools

This package prepares and validates PDX model DDS textures without starting Blender or contacting a provider.

`delivery.py` captures source, occupancy-mask, provenance, and target-preimage SHA-256 values in a compare-and-swap manifest, stages immutable inputs and encoded outputs separately, writes decoded-pixel evidence, and installs only after the manifest and current files still match their recorded hashes.

`bc_codec.py` writes deterministic legacy DXT1/BC1 diffuse maps and DXT5/BC3 diffuse-alpha, normal, and specular maps, with every mip through 1x1; it uses NumPy endpoint fitting and records encoder and NumPy versions.

`dds.py` validates the complete DDS header, FourCC, caps, dimensions, mip count, payload length, and every compressed mip, and decodes BC1, BC3, and input-only single-level BGRA pixels for QA.

`atlas.py` requires an explicit grayscale occupancy mask and copies existing occupied texel values into gutters by bounded eight-neighbour propagation; it never detects islands from image brightness or invents texture values.

`conventions.py` implements the PDX `RRxG` normal layout, safe cleanup of existing packed normals, provider normal repacking, provider-PBR specular recipes, masked channel measurements, and class-aware material gates.

The offline wiki's `Graphical asset modding` page documents sprite image paths and frame fields, and its `Entity modding` page documents the `pdxmesh` file and entity scale references; the installed vanilla shader and exact installed model textures supply the model-material semantics and compression precedents used here.

## Image and material contract

Diffuse maps use BC1 when alpha is unused and BC3 when source pixels or the declared runtime consumer use alpha; normal and specular maps use BC3 because their alpha channel carries material data.

The maximum output dimension defaults to 512 pixels and never exceeds the source dimensions; a 1024-pixel request needs a written justification of at least 30 characters.

Each map requires an occupancy mask whose file SHA, mesh SHA, registration SHA, coverage, and dimensions can be verified against the runtime UV-mask manifest.

Island dilation defaults to 12 pixels and accepts 8 through 16 pixels; `dilation_px: 0` requires a concrete `skip_dilation_reason`, which supports UV-wrap cases where the mask does not represent tiled addressing.

The provider-normal recipe maps source R to PDX R and G, maps source G to PDX A by default, and writes PDX B as zero; source-green inversion requires a hash-verified handedness-evidence file.

For an existing PDX normal, `packed_normal_cleanup` copies occupied G into R, preserves occupied G and A, clears B, sets unused map pixels to `(128, 128, 0, 128)`, and applies mask-based dilation without synthesizing tangent detail.

Specular maps use R=0, G=specular strength, and A=255 minus provider roughness; the explicit steel mask sets B to zero outside steel and to `max(200, provider metalness)` inside steel, or 200 inside steel when no metalness map exists.

The class recipe ranges are cloth G 40–90/A 60–100, skin G 110–160/A 120–160, leather G 120–160 with provider-derived alpha, steel G 180–255/A 150–180, stone G 60–90/A 50–70, and fur G 20–40/A 40–70.

The specular gate rejects constant G, mean B above 5 outside the explicit steel mask, steel B below 200, and mean A above 110 on nonwet classes; the decoded BC3 check allows up to five values of blue-channel quantization error, and skin and steel may exceed 110 only inside their explicit masks and within their listed alpha ranges.

The specular report retains the original provider roughness, metalness, and class-mask path/SHA rows, provider blue-channel statistics, derived blue statistics, the count of occupied pixels changed by the mask, and confirmation that provider inputs remain unchanged.

The normal gate measures only occupied pixels and requires G and A standard deviations from 15 through 35, mean tangent tilt no greater than 0.35, an R/G mirror error no greater than 5 values, and zero-valued B apart from the declared compression tolerance.

Compression-only batches preserve occupied source channels and may report old semantic defects as unresolved; their install gate checks format, full mips, decoded fidelity, alpha bounds, source hashes, and CAS preimages.

Provider repacks and material recipes require verified provenance and a passing material gate; compression-only conversion requires no material provenance.

## Request format

The request is a UTF-8 JSON object with a unique batch id and one or more texture items.

```json
{
  "batch_id": "unit-fix-body-textures",
  "items": [
    {
      "id": "body_diffuse",
      "role": "diffuse",
      "source_rel": "docs/assets/owner/models_3d/unit/textures/source/body_diffuse.png",
      "target_rel": "gfx/models/units/unit/body_diffuse.dds",
      "occupancy_mask_rel": "docs/plans/unit_fix_2026-10/pipeline_evidence/uv_masks/unit_body_diffuse_occupancy.png",
      "conversion_scope": "compression_only",
      "size": 512,
      "dilation_px": 12,
      "alpha_used": "auto"
    }
  ]
}
```

`source_rel` may identify a PNG or a supported input DDS; `target_rel` may equal `source_rel` for a protected in-place CAS update because the original bytes are archived in the staging root first.

An optional `expected_target_sha256` must match the target when planning; otherwise the planner captures the current target SHA or records that the target is absent.

`minimum_coverage` is optional and applies only when a family-specific coverage floor is justified by its atlas layout.

## Material provenance

Provider-normal repacking uses a JSON object with `kind: provider_rgb_normal`, an exact `source` path and SHA, and `green_sign: preserve` or `invert`; `invert` also requires a separately hashed `green_sign_evidence` file.

Provider-specular generation uses `kind: provider_pbr_specular`, exact `roughness` and optional `metalness` path/SHA rows, and an explicit path/SHA row for every class mask.

Compression-only semantic review of an existing PDX normal uses `kind: pdx_packed_normal_evidence` with the exact source path and SHA.

Compression-only semantic review of an existing PDX specular map uses `kind: pdx_material_mask_evidence`, the exact source path and SHA, and explicit class-mask path/SHA rows.

Every provenance row is resolved inside the repository root and rehashed before conversion and installation; provenance that claims generated detail is rejected.

## Commands

Run these commands from the repository root with the same Python environment that supplies Pillow and NumPy.

```powershell
python -B .tools/3d_pipeline/textures/cli.py prepare `
  --root . `
  --request docs/plans/unit_fix_2026-10/texture_batch_request.json `
  --staging-root docs/plans/unit_fix_2026-10/texture_staging `
  --manifest docs/plans/unit_fix_2026-10/texture_install_manifest.json

python -B .tools/3d_pipeline/textures/cli.py convert `
  --root . `
  --manifest docs/plans/unit_fix_2026-10/texture_install_manifest.json

python -B .tools/3d_pipeline/textures/cli.py convert `
  --root . `
  --manifest docs/plans/unit_fix_2026-10/texture_install_manifest.json `
  --execute

python -B .tools/3d_pipeline/textures/cli.py install `
  --root . `
  --manifest docs/plans/unit_fix_2026-10/texture_install_manifest.json

python -B .tools/3d_pipeline/textures/cli.py install `
  --root . `
  --manifest docs/plans/unit_fix_2026-10/texture_install_manifest.json `
  --execute
```

Conversion and installation are dry-run operations unless `--execute` is supplied; the parent owns runtime batch execution and adapter integration.

The Python integration API is `textures.delivery.prepare_batch(repo_root, request_json, staging_root, manifest_path)`, `textures.delivery.convert_batch(repo_root, manifest_path, execute=False)`, `textures.delivery.install_batch(repo_root, manifest_path, execute=False)`, and `textures.delivery.resolve_uv_mask(repo_root, mask_manifest_path, pdxmesh, texture_name, expected_mesh_sha256=None, expected_registration_sha256=None)`.

Before conversion, the planner stores the source and target hashes; conversion archives the original source, prepares each mip from an explicit occupancy mask, writes a DDS and QA report to staging, and records the decoded pixel measurements.

Before installation, the gate verifies the request/provenance/input/mask/archive/output hashes, rechecks every target preimage, writes verified backups and temporary sibling files, then atomically replaces targets with rollback on a partial batch failure.

## Decoded-image gate

The gate uses Pillow's DDS decoder for base-level pixel evidence and the repository parser for every lower mip; both decoders must agree within one channel value on the base level.

Mips at least 8x8 pixels require RGB PSNR of at least 25 dB and per-channel MAE at most 16; smaller block levels retain their measurements with a 15 dB PSNR and 32 MAE floor to account for one-block endpoint quantization.

Packed alpha requires MAE at most 10; diffuse alpha minimum and maximum must each stay within four values, and BC1 diffuse output must decode fully opaque.

Every mip report retains dimensions, per-channel MAE, p95 and maximum error, per-channel PSNR, RGB PSNR, and alpha bounds where alpha represents opacity.
