# Event 012 world-order icon GFX handoff

See `docs/plans/012_africa_plans/subagent_handoffs/012_africa_world_icon_package_handoff.md` for the complete machine-readable ID-to-sprite map and runtime wiring notes.

Manifest: `manifests/012_africa_world_order_icon_manifest.json`.

Generation prompts and atlas UUID provenance: `generation_provenance.md`.

Runtime DDS roots:

- `gfx/interface/goals/012_africa/world_order/` — 121 focus icons at 94x86.
- `gfx/interface/ideas/012_africa/world_order/` — 38 idea icons at 64x64.

Source atlases, source tiles, processed transparent PNGs, and contact sheets are preserved beside this file. No tile was rejected during review.

## Fictional high-chaos leader portrait handoff (v2)

The six portrait subassets below are generated fictional or supernatural identities mapped to existing Event-012 asset-matrix rows. The v2 sources are intentionally absurd but still use the vanilla HOI4 head-and-shoulders crop, single-figure composition, plain low-detail matte backgrounds, and painted finish. All six are male-presenting or explicitly nonhuman; no female character was generated in this revision. Their sprite registrations are present in `interface/012_africa_leaders_fictional.gfx`; character definitions, model/entity production, and runtime gates remain deferred.

| Matrix row | Final DDS | Proposed sprite | Target `.gfx` | Status |
| --- | --- | --- | --- | --- |
| `country_package_pan_high_chaos` | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_pan.dds` | `GFX_portrait_012_africa_fictional_pan` | `interface/012_africa_leaders_fictional.gfx` | `v2 installed; deferred_model_required`, `deferred_runtime_gated` |
| `country_package_gorilla_kingdom` | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_gorilla_kingdom.dds` | `GFX_portrait_012_africa_fictional_gorilla_kingdom` | `interface/012_africa_leaders_fictional.gfx` | `v2 installed; deferred_model_required`, `deferred_runtime_gated` |
| `country_package_the_green` | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_the_green.dds` | `GFX_portrait_012_africa_fictional_the_green` | `interface/012_africa_leaders_fictional.gfx` | `v2 installed; deferred_model_required`, `deferred_runtime_gated` |
| `country_package_living_rivers` | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_living_rivers.dds` | `GFX_portrait_012_africa_fictional_living_rivers` | `interface/012_africa_leaders_fictional.gfx` | `v2 installed; deferred_model_required`, `deferred_runtime_gated` |
| `country_package_stoneborn` | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_stoneborn.dds` | `GFX_portrait_012_africa_fictional_stoneborn` | `interface/012_africa_leaders_fictional.gfx` | `v2 installed; deferred_model_required`, `deferred_runtime_gated` |
| `country_package_ancient_hosts` | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_ancient_hosts.dds` | `GFX_portrait_012_africa_fictional_ancient_hosts` | `interface/012_africa_leaders_fictional.gfx` | `v2 installed; deferred_model_required`, `deferred_runtime_gated` |

Each final DDS is legacy BGRA 32-bit at 156x210 with an opaque matte background. The v2 source masters, processed previews, decoded review sheet, and replacement-ready ComfyUI source/prompt pairs are retained under `docs/assets/012_africa_world_order/source_png/`, `docs/assets/012_africa_world_order/processed_png/`, `docs/assets/012_africa_world_order/comparison_v2/`, and `docs/assets/portraits/012_africa_world_order/`; the machine-readable manifest is `manifests/012_africa_world_order_fictional_portraits_manifest.json`.

Use these portraits only for the named fictional high-chaos actors. Do not attach them to grounded historical leaders or real African identities without a separate sourced-asset review.
