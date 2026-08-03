# Event 012 Africa fictional high-chaos portrait asset handoff

Date: 2026-08-03.

This handoff now records the v4 visual replacement for six fictional, supernatural, or nonhuman leader-portrait subassets on existing Event 012 controlled-pool rows. The v4 pass is deliberately absurd without becoming a busy council scene: every portrait has one male-presenting or nonhuman subject, a different impossible natural silhouette, a plain matte background, and a readable HOI4 head-and-shoulders crop. No female character was generated. The six dormant portrait consumers are declared in `common/characters/012_africa_fictional_characters.txt`; they add no country tag, cosmetic tag, country-leader role, model, entity, focus, decision, or workbook row.

## v4 selected runtime set

The parent-owned sprite names remain stable, but the texture endpoints now use the v4 DDS files. The machine-readable v4 manifest is `docs/assets/012_africa_world_order/manifests/012_africa_world_order_fictional_portraits_v4_manifest.json` and the decoded review sheet is `docs/assets/012_africa_world_order/comparison_v4/portrait_012_africa_fictional_v4_decoded_contact_sheet.png`.

| Matrix row | Identity motif | Runtime DDS | Sprite | Status |
| --- | --- | --- | --- | --- |
| `country_package_pan_high_chaos` | Thundercloud Ram King, lightning cloud crown and rain-gauge eye cover | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_pan_v4.dds` | `GFX_portrait_012_africa_fictional_pan` | `deferred_model_required`, `deferred_runtime_gated` |
| `country_package_gorilla_kingdom` | Termite Citadel Silverback, red-clay citadel crown and drum-rim gorget | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_gorilla_v4.dds` | `GFX_portrait_012_africa_fictional_gorilla_kingdom` | `deferred_model_required`, `deferred_runtime_gated` |
| `country_package_the_green` | Baobab Ring-Eye King, half-wood face and firefly branch crown | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_the_green_v4.dds` | `GFX_portrait_012_africa_fictional_the_green` | `deferred_model_required`, `deferred_runtime_gated` |
| `country_package_living_rivers` | River Delta Sovereign, delta crown and waterfall beard | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_living_rivers_v4.dds` | `GFX_portrait_012_africa_fictional_living_rivers` | `deferred_model_required`, `deferred_runtime_gated` |
| `country_package_stoneborn` | Meteor Geode Sovereign, salt-glass face and constellation throat | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_stoneborn_v4.dds` | `GFX_portrait_012_africa_fictional_stoneborn` | `deferred_model_required`, `deferred_runtime_gated` |
| `country_package_ancient_hosts` | Leopard Eclipse Host, hood split into stone and feathers with eclipse paint | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_ancient_hosts_v4.dds` | `GFX_portrait_012_africa_fictional_ancient_hosts` | `deferred_model_required`, `deferred_runtime_gated` |

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

The built-in ImageGen v4 source masters, processed 156x210 PNGs, DDS hashes, exact-basename prompt pairs, source/decoded contact sheet, and visual review are retained under the ignored asset workspace `docs/assets/012_africa_world_order/` and the durable prompt queue `docs/assets/portraits/012_africa/`. The machine-readable manifest is `docs/assets/012_africa_world_order/manifests/012_africa_world_order_fictional_portraits_v4_manifest.json`. The earlier v2 and v3 packages remain available as comparison evidence only.

The v4 visual identities are deliberately non-interchangeable: Pan is a thundercloud ram sovereign; Gorilla Kingdom is a termite-citadel silverback; The Green is a half-baobab ring-eye sovereign; Living Rivers is a delta-crowned waterfall sovereign; Stoneborn is a meteor-geode ruler; Ancient Hosts is a leopard-hooded eclipse host. They contain no councils, committees, crowds, readable text, watermarks, modern props, or real historical/ethnic identity. The unused Moth-Eyed and Living Drum explorations remain outside the six-row package. The rejected photoreal/CGI Pan draft remains excluded.
The v4 manifest records per-row apparent gender and the unique absurd visual signature used for review. All six remain male-presenting or explicitly nonhuman male-coded; no female portrait or female character consumer is introduced.

Pan and Gorilla Kingdom use the two user-required untranslated Afaan Oromoo court names through the neutral localisation keys `africa_absurd_regnal_name_01` and `africa_absurd_regnal_name_02`. Their exact strings remain visible only as dormant fictional character names; no English gloss, historical attribution, or technical identifier contains them. The protocol's native-speaker and final flavour review remains open.

## Runtime boundary

The six sprite IDs remain registered in `interface/012_africa_leaders_fictional.gfx`, and only their texture endpoints moved to the v4 DDS paths. No character wiring is made in this tranche. The DDS files and sprite endpoints remain dormant until the existing country-package and model/entity gates are accepted. They must not be attached to the sixteen grounded historical African sovereign characters or used to fill a historical portrait-source gap.

## Future work

When the corresponding model and country package are accepted, the parent should add the country-leader role and validate the exact runtime gate. Historical African leaders require the separate sourced-real portrait contract documented in `docs/events/012_africa/portrait_runtime_gate.md`.
