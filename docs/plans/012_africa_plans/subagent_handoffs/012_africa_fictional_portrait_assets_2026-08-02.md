# Event 012 Africa fictional high-chaos portrait asset handoff

Date: 2026-08-02.

This asset tranche creates six fictional, supernatural, or nonhuman leader-portrait subassets for existing Event 012 controlled-pool rows. It adds only the dormant `.gfx` sprite registration; it does not add a country tag, cosmetic tag, character, model, entity, focus, decision, localisation key, or workbook row.

## Asset map

| Matrix row | Identity | Runtime DDS | Proposed sprite | Status |
| --- | --- | --- | --- | --- |
| `country_package_pan_high_chaos` | Pan | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_pan.dds` | `GFX_portrait_012_africa_fictional_pan` | `deferred_model_required`, `deferred_runtime_gated` |
| `country_package_gorilla_kingdom` | Gorilla Kingdom | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_gorilla_kingdom.dds` | `GFX_portrait_012_africa_fictional_gorilla_kingdom` | `deferred_model_required`, `deferred_runtime_gated` |
| `country_package_the_green` | The Green | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_the_green.dds` | `GFX_portrait_012_africa_fictional_the_green` | `deferred_model_required`, `deferred_runtime_gated` |
| `country_package_living_rivers` | Living Rivers | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_living_rivers.dds` | `GFX_portrait_012_africa_fictional_living_rivers` | `deferred_model_required`, `deferred_runtime_gated` |
| `country_package_stoneborn` | Stoneborn | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_stoneborn.dds` | `GFX_portrait_012_africa_fictional_stoneborn` | `deferred_model_required`, `deferred_runtime_gated` |
| `country_package_ancient_hosts` | Ancient Hosts | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_ancient_hosts.dds` | `GFX_portrait_012_africa_fictional_ancient_hosts` | `deferred_model_required`, `deferred_runtime_gated` |

## Production and review evidence

The built-in ImageGen source masters, processed 156x210 PNGs, DDS hashes, prompt pairs, contact sheet, and visual review are retained under the ignored asset workspace `docs/assets/012_africa_world_order/` and `docs/assets/portraits/012_africa_world_order/`. The machine-readable manifest is `docs/assets/012_africa_world_order/manifests/012_africa_world_order_fictional_portraits_manifest.json`.

All six images are one centered figure on a plain matte background in a restrained HOI4 painted treatment. They contain no councils, committees, crowds, readable text, watermarks, modern props, or real historical/ethnic identity. Pan's rejected photoreal/CGI draft remains excluded from the package.

## Runtime boundary

The six sprite IDs are registered in `interface/012_africa_leaders_fictional.gfx`, but no character wiring is made in this tranche. The DDS files and sprite endpoints remain dormant until the existing country-package and model/entity gates are accepted. They must not be attached to the sixteen grounded historical African sovereign characters or used to fill a historical portrait-source gap.

## Future work

When the corresponding model and country package are accepted, the parent should add one dedicated fictional character definition per row, then validate the exact runtime gate and localisation. Historical African leaders require the separate sourced-real portrait contract documented in `docs/events/012_africa/portrait_runtime_gate.md`.
