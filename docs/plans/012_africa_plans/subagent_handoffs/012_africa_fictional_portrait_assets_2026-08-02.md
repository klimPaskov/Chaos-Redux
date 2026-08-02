# Event 012 Africa fictional high-chaos portrait asset handoff

Date: 2026-08-02.

This handoff now records the v3 visual replacement for six fictional, supernatural, or nonhuman leader-portrait subassets on existing Event 012 controlled-pool rows. The v3 pass is deliberately absurd without becoming a busy council scene: every portrait has one male-presenting or nonhuman subject, one memorable impossible motif, a plain matte background, and a readable HOI4 head-and-shoulders silhouette. No female character was generated. The six dormant portrait consumers are now declared in `common/characters/012_africa_fictional_characters.txt`; they add no country tag, cosmetic tag, country-leader role, model, entity, focus, decision, or workbook row.

## v3 selected runtime set

The parent-owned sprite names remain stable, but the texture endpoints now use the v3 DDS files. The machine-readable v3 manifest is `docs/assets/012_africa_world_order/manifests/012_africa_world_order_fictional_portraits_v3_manifest.json` and the decoded review sheet is `docs/assets/012_africa_world_order/comparison_v3/portrait_012_africa_fictional_v3_decoded_contact_sheet.png`.

| Matrix row | Identity motif | Runtime DDS | Sprite | Status |
| --- | --- | --- | --- | --- |
| `country_package_pan_high_chaos` | Thunder-Skin King, storm crown and copper collar | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_pan_v3.dds` | `GFX_portrait_012_africa_fictional_pan` | `deferred_model_required`, `deferred_runtime_gated` |
| `country_package_gorilla_kingdom` | Fruit-Crown Silverback, red fruit crown and woven mantle | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_gorilla_kingdom_v3.dds` | `GFX_portrait_012_africa_fictional_gorilla_kingdom` | `deferred_model_required`, `deferred_runtime_gated` |
| `country_package_the_green` | Baobab Mirror King, living baobab crown and half mirror | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_the_green_v3.dds` | `GFX_portrait_012_africa_fictional_the_green` | `deferred_model_required`, `deferred_runtime_gated` |
| `country_package_living_rivers` | Waterfall River Sovereign, crown-fed river beard | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_living_rivers_v3.dds` | `GFX_portrait_012_africa_fictional_living_rivers` | `deferred_model_required`, `deferred_runtime_gated` |
| `country_package_stoneborn` | Salt-Glass Emperor, translucent rose salt crown and cheek | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_stoneborn_v3.dds` | `GFX_portrait_012_africa_fictional_stoneborn` | `deferred_model_required`, `deferred_runtime_gated` |
| `country_package_ancient_hosts` | Leopard Eclipse King, carved leopard hood and geometric paint | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_ancient_hosts_v3.dds` | `GFX_portrait_012_africa_fictional_ancient_hosts` | `deferred_model_required`, `deferred_runtime_gated` |

The v2 table below is retained as superseded comparison evidence. It is not the current texture endpoint.

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

The built-in ImageGen v3 source masters, processed 156x210 PNGs, DDS hashes, prompt pairs, source/decoded contact sheet, and visual review are retained under the ignored asset workspace `docs/assets/012_africa_world_order/` and the durable prompt queue `docs/assets/portraits/012_africa/`. The machine-readable manifest is `docs/assets/012_africa_world_order/manifests/012_africa_world_order_fictional_portraits_v3_manifest.json`. The earlier v2 package remains available as comparison evidence only.

The v3 visual identities are deliberately non-interchangeable: Pan is a storm-crowned sovereign; Gorilla Kingdom is a fruit-crowned silverback; The Green is a baobab-crowned mirror sovereign; Living Rivers is a copper-ringed waterfall sovereign; Stoneborn is a rose salt-glass ruler; Ancient Hosts is a leopard-hooded painted king. They contain no councils, committees, crowds, readable text, watermarks, modern props, or real historical/ethnic identity. The unused Moth-Eyed and Living Drum explorations remain outside the six-row package. The rejected photoreal/CGI Pan draft remains excluded.

Pan and Gorilla Kingdom use the two user-required untranslated Afaan Oromoo court names through the neutral localisation keys `africa_absurd_regnal_name_01` and `africa_absurd_regnal_name_02`. Their exact strings remain visible only as dormant fictional character names; no English gloss, historical attribution, or technical identifier contains them. The protocol's native-speaker and final flavour review remains open.

## Runtime boundary

The six sprite IDs remain registered in `interface/012_africa_leaders_fictional.gfx`, and only their texture endpoints moved to the v3 DDS paths. No character wiring is made in this tranche. The DDS files and sprite endpoints remain dormant until the existing country-package and model/entity gates are accepted. They must not be attached to the sixteen grounded historical African sovereign characters or used to fill a historical portrait-source gap.

## Future work

When the corresponding model and country package are accepted, the parent should add the country-leader role and validate the exact runtime gate. Historical African leaders require the separate sourced-real portrait contract documented in `docs/events/012_africa/portrait_runtime_gate.md`.
