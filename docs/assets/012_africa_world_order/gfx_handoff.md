# Event 012 world-order icon GFX handoff

See `docs/plans/012_africa_plans/subagent_handoffs/012_africa_world_icon_package_handoff.md` for the complete machine-readable ID-to-sprite map and runtime wiring notes.

Manifest: `manifests/012_africa_world_order_icon_manifest.json`.

Generation prompts and atlas UUID provenance: `generation_provenance.md`.

Runtime DDS roots:

- `gfx/interface/goals/012_africa/world_order/` — 121 focus icons at 94x86.
- `gfx/interface/ideas/012_africa/world_order/` — 38 idea icons at 64x64.

Source atlases, source tiles, processed transparent PNGs, and contact sheets are preserved beside this file. No tile was rejected during review.

## Fictional high-chaos leader portrait handoff (v4)

The six portrait subassets below are generated fictional or supernatural identities mapped to existing Event-012 asset-matrix rows. The v4 sources push the absurdity into a different natural or impossible silhouette for every actor while keeping the vanilla HOI4 head-and-shoulders crop, single-figure composition, plain low-detail matte backgrounds, and painted finish. All six are male-presenting or explicitly nonhuman; no female character was generated. Their stable sprite registrations are present in `interface/012_africa_leaders_fictional.gfx`, and dormant character consumers are declared in `common/characters/012_africa_fictional_characters.txt`; country-leader roles, model/entity production, and runtime gates remain deferred.

| Matrix row | Final DDS | Proposed sprite | Target `.gfx` | Status |
| --- | --- | --- | --- | --- |
| `country_package_pan_high_chaos` | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_pan_v4.dds` | `GFX_portrait_012_africa_fictional_pan` | `interface/012_africa_leaders_fictional.gfx` | `v4 installed; deferred_model_required`, `deferred_runtime_gated` |
| `country_package_gorilla_kingdom` | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_gorilla_v4.dds` | `GFX_portrait_012_africa_fictional_gorilla_kingdom` | `interface/012_africa_leaders_fictional.gfx` | `v4 installed; deferred_model_required`, `deferred_runtime_gated` |
| `country_package_the_green` | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_the_green_v4.dds` | `GFX_portrait_012_africa_fictional_the_green` | `interface/012_africa_leaders_fictional.gfx` | `v4 installed; deferred_model_required`, `deferred_runtime_gated` |
| `country_package_living_rivers` | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_living_rivers_v4.dds` | `GFX_portrait_012_africa_fictional_living_rivers` | `interface/012_africa_leaders_fictional.gfx` | `v4 installed; deferred_model_required`, `deferred_runtime_gated` |
| `country_package_stoneborn` | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_stoneborn_v4.dds` | `GFX_portrait_012_africa_fictional_stoneborn` | `interface/012_africa_leaders_fictional.gfx` | `v4 installed; deferred_model_required`, `deferred_runtime_gated` |
| `country_package_ancient_hosts` | `gfx/leaders/012_africa/fictional/portrait_012_africa_fictional_ancient_hosts_v4.dds` | `GFX_portrait_012_africa_fictional_ancient_hosts` | `interface/012_africa_leaders_fictional.gfx` | `v4 installed; deferred_model_required`, `deferred_runtime_gated` |

Each final DDS is legacy BGRA 32-bit at 156x210 with an opaque matte background. The v4 source masters, processed previews, decoded review sheet, and exact-basename prompt pairs are retained under `docs/assets/portraits/012_africa/`, `docs/assets/012_africa_world_order/processed_png/`, and `docs/assets/012_africa_world_order/comparison_v4/`; the machine-readable manifest is `manifests/012_africa_world_order_fictional_portraits_v4_manifest.json`. The earlier v2 and v3 packages remain comparison evidence only.

Use these portraits only for the named fictional high-chaos actors. Do not attach them to grounded historical leaders or real African identities without a separate sourced-asset review.

## Historical male sovereign source-evidence handoff (2026-08-03)

The male-only historical audit is recorded in `manifests/012_africa_priority_male_portrait_sources_manifest.json` with rights notes in `manifests/012_africa_priority_male_portrait_sources_licence_notes.md`. The source masters, exact crop JSON, processed 156x210 evidence PNGs, evidence DDS files, and candidate contact sheet are under `source_masters/portraits/`, `source_crops/portraits/`, `processed_png/portraits/`, `final_dds/portraits/`, and `contact_sheets/portraits/` respectively.

The following stable sprite names are the parent-owned runtime contract. No `.gfx` line is changed by this package, and the evidence DDS paths below are deliberately outside `gfx/leaders/`:

| Polity | Candidate | Stable sprite | Source-evidence DDS | Status |
| --- | --- | --- | --- | --- |
| Asante | Prempeh I group crop | `GFX_portrait_012_africa_priority_asante_sovereign` | `final_dds/portraits/portrait_012_africa_priority_asante_prempeh_i_source_evidence.dds` | `blocked`: group identity uncertain; Prempeh II is Event 006-owned |
| Oyo | unnamed Alaafin office image | `GFX_portrait_012_africa_priority_oyo_sovereign` | none | `blocked`: face obscured and person unnamed |
| Sokoto | Sir Siddiq Abubakar III | `GFX_portrait_012_africa_priority_sokoto_sovereign` | `final_dds/portraits/portrait_012_africa_priority_sokoto_siddiq_abubakar_iii_source_evidence.dds` | `needs_user_review`: Smithsonian permission conflict |
| Kanem-Bornu | Shehu Sanda Kura | `GFX_portrait_012_africa_priority_kanem_bornu_sovereign` | `final_dds/portraits/portrait_012_africa_priority_kanem_bornu_sanda_kura_source_evidence.dds` | `needs_user_review`; current promoted runtime is a separate reviewed repaint |
| Manden | none | `GFX_portrait_012_africa_priority_manden_sovereign` | none | `blocked`: no defensible named male photograph |
| Kongo | Pedro VII Afonso | `GFX_portrait_012_africa_priority_kongo_sovereign` | `final_dds/portraits/portrait_012_africa_priority_kongo_pedro_vii_source_evidence.dds` | `needs_user_review`; current promoted runtime is a separate reviewed repaint |
| Buganda | Daudi Cwa II | `GFX_portrait_012_africa_priority_buganda_sovereign` | `final_dds/portraits/portrait_012_africa_priority_buganda_daudi_cwa_ii_source_evidence.dds` | `needs_user_review`: repaint and independent audit pending |
| Aksum | none | `GFX_portrait_012_africa_priority_aksum_sovereign` | none | `blocked`: ancient identity predates photography |
| Harar | Emir Abdullahi | `GFX_portrait_012_africa_priority_harar_sovereign` | `final_dds/portraits/portrait_012_africa_priority_harar_emir_abdullahi_source_evidence.dds` | `needs_user_review`; current promoted runtime is a separate reviewed repaint |
| Kilwa | none | `GFX_portrait_012_africa_priority_kilwa_sovereign` | none | `blocked`: medieval identity predates photography |
| Nubia | none | `GFX_portrait_012_africa_priority_nubia_sovereign` | none | `blocked`: ancient/medieval identity predates photography |
| Luba | Albert Kalonji | `GFX_portrait_012_africa_priority_luba_sovereign` | `final_dds/portraits/portrait_012_africa_priority_luba_albert_kalonji_source_evidence.dds` | `needs_user_review`: uploader/AP provenance and rights open |
| Lunda | Mwaantayaav Mbaku Citend | `GFX_portrait_012_africa_priority_lunda_sovereign` | `final_dds/portraits/portrait_012_africa_priority_lunda_mwaantayaav_mbaku_citend_source_evidence.dds` | `needs_user_review`: photographer permission required |
| Great Zimbabwe | none | `GFX_portrait_012_africa_priority_great_zimbabwe_sovereign` | none | `blocked`: medieval identity predates photography |
| Merina | Radama II | `GFX_portrait_012_africa_priority_merina_sovereign` | `final_dds/portraits/portrait_012_africa_priority_merina_radama_ii_source_evidence.dds` | `needs_user_review`: male identity strong; rights jurisdiction and actor gate open |
| Zulu | Dinuzulu kaCetshwayo | `GFX_portrait_012_africa_priority_zulu_sovereign` | `final_dds/portraits/portrait_012_africa_priority_zulu_dinuzulu_source_evidence.dds` | `needs_user_review`: CC0 source, but actor eligibility blocked; never Solomon kaDinuzulu |

The evidence DDS files are direct source-crop resizes. They are not final HOI4 repaints, do not grant runtime approval, and must not be attached to the six fictional high-chaos actors. The current runtime gate remains three independently reviewed male source-locked portraits (Kanem-Bornu, Harar, Kongo); six fictional high-chaos portraits remain separate dormant model-required assets.
