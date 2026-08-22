# Event 016 D'Rhondan icon asset completion handoff

Status: complete for the parent-authorized binary and GFX tranche. This handoff covers 88 purpose-built D'Rhondan focus icons, 11 distinct lifecycle idea icons, the exact missing contact/country/project sprite registrations, and the scoped supporting-binary audit. Per the parent correction, no All Roads Lead Home achievement DDS, achievement definition, trigger, localisation, or GFX entry was created. No 3D model completion is claimed.

## Files and counts

- Runtime focus DDS: `gfx/interface/goals/016_dhrondan_focus/` contains exactly 88 files at the registered branch paths. Every file is 94x86, one-level uncompressed BGRA DDS, and retains transparent unused canvas.
- Runtime lifecycle DDS: `gfx/interface/ideas/016_dhrondan_focus/` contains exactly 11 files at the registered paths. Every file is 64x64, one-level uncompressed BGRA DDS, and retains transparent unused canvas.
- Focus registration: `interface/016_dhrondan_focus_icons.gfx` contains 88 base focus sprites, 88 matching `_shine` sprites, and 11 lifecycle idea sprites. Its 99 unique texture paths now all exist.
- Missing-token registration: `interface/016_dhrondan_assets.gfx` adds exactly 21 previously unresolved names: 14 contact tokens, 7 country event/decision tokens, and the requested `GFX_sp_dhrondan_envoy_craft` project token as part of the same exact asset registry.
- Staging and evidence: `docs/assets/016_brilliant_scientist/dhrondan_icon_asset_completion/` contains source PNGs, processed PNGs, decoded DDS previews, focus/idea/supporting contact sheets, `metadata/manifest.json`, `metadata/focus_dds_validation.json`, `metadata/ideas_dds_validation.json`, `metadata/supporting_dds_validation.json`, `metadata/prompt_log.md`, and `gfx_handoff.md`.

The full focus branch-to-file and lifecycle sprite lists are in `docs/assets/016_brilliant_scientist/dhrondan_icon_asset_completion/gfx_handoff.md`. The registered runtime patterns are exact: `goal_DHR_<name>.dds` under the branch named in `interface/016_dhrondan_focus_icons.gfx`, and `dhrondan_<lifecycle>.dds` under `gfx/interface/ideas/016_dhrondan_focus/`.

## GFX audit evidence

The scoped source audit covered `events/016_brilliant_scientist_dhrondan_contact_events.txt` events `.40-.47`, `events/016_dhrondan_country_events.txt` events `.48-.52`, both D'Rhondan decision categories, contact and country decisions, alien-infantry landing decisions, the Envoy special project, `interface/alien_infantry_system.gfx`, and `interface/016_brilliant_scientist_hidden_technologies.gfx`. A source-token census reports zero unresolved `GFX_` tokens after adding `interface/016_dhrondan_assets.gfx`.

The 21 added registrations are:

| Consumer family | Sprite names |
| --- | --- |
| Contact reports | `GFX_report_event_016_dhrondan_craft_authorized`, `GFX_report_event_016_dhrondan_envoy_departure`, `GFX_report_event_016_dhrondan_planetary_audience`, `GFX_report_event_016_dhrondan_pact_return`, `GFX_report_event_016_dhrondan_ufo_landing`, `GFX_report_event_016_dhrondan_expedition_failure`, `GFX_report_event_016_dhrondan_revolt_warning`, `GFX_report_event_016_dhrondan_rebellion` |
| Contact decisions | `GFX_decision_category_dhrondan_contact`, `GFX_decision_honor_dhrondan_accord`, `GFX_decision_send_kruger_to_dhronda`, `GFX_decision_send_mengele_to_dhronda`, `GFX_decision_dhrondan_ufo_landing` |
| Country event/decision | `GFX_news_event_016_dhrondan_sovereignty`, `GFX_report_event_016_dhrondan_diplomatic_compact`, `GFX_decision_category_dhrondan_sovereignty`, `GFX_decision_dhrondan_reclamation`, `GFX_decision_dhrondan_enclave_supply`, `GFX_decision_dhrondan_state_integration`, `GFX_decision_dhrondan_two_world_compact` |
| Special project | `GFX_sp_dhrondan_envoy_craft` |

Existing shared GFX definitions were inspected and retained for the two-frame alien counters, alien laser equipment, two alien tactics, and two hidden technology icons. Every consumed DHR/contact/landing/project/counter/equipment/tactic/hidden-tech token has a definition and an existing DDS path.

## Binary and visual review

Canonical references were read only from `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference`. National-focus and idea contact sheets were inspected before individual references. Runtime DDS headers were parsed and decoded to PNG. The focus validation reports 88 files, 94x86 dimensions, alpha range 0-255, and 88 unique DDS hashes after replacing the duplicate laboratory icon. The idea validation reports 11 files, 64x64 dimensions, alpha range 0-255, and distinct lifecycle art. Supporting validation covers 35 installed DHR/contact binaries: 13 event/news pictures, 14 decision/event-detail binaries, one 161x98 project icon, one 152x42 large counter, one 60x12 map counter, two 90x48 tactics, two 132x52 hidden technologies, and one 132x52 laser equipment icon.

The supporting contact sheets show readable opaque scene art for event/news consumers, transparent readable decision/project/technology/tactic art, and vanilla-compatible two-frame counter behavior. The counter review matched the canonical large/map counter canvas, frame dimensions, frame order, alpha behavior, and selected-state marker convention. Existing support DDS binaries were not rewritten because the inspected headers and visuals are valid. Of the 35 inspected supporting binaries, 28 remain installed at registered runtime paths and seven unconsumed candidates are archived outside runtime under `docs/assets/016_brilliant_scientist/dhrondan_icon_asset_completion/unconsumed_dds/`.

## ImageGen provenance and alpha

All new source art used official native-alpha ImageGen calls with transparent unused canvas requested in the initial prompt. The existing 40 focus masters were retained from the prior native-alpha DHR package. Native-alpha transparent atlases supplied the remaining focus and all 11 lifecycle sources. The replacement `goal_DHR_join_the_scattered_laboratories` was generated as a single native-alpha icon showing three distributed alien field laboratories connected to a central relay; its source is preserved at `source_png/focus/goal_DHR_join_the_scattered_laboratories.png`, with the original shared duplicate removed from the staged output. It is visually distinct from `goal_DHR_the_exoplanetary_materials_board`, and the DDS hash audit now reports 88/88 unique focus hashes.

The generation prompts and cache provenance are recorded in `metadata/prompt_log.md`, including the atlas outputs `exec-da584c59-b799-4ba9-b861-43bf82122b56.png`, `exec-0b506059-a99d-40b1-8288-4f6ab49fd16f.png`, `exec-e7c7390b-a22c-4e94-85e0-f9ff7b15d8bd.png`, and the replacement output `exec-a1254f68-816e-40e7-8fe8-61aa9ff1d5d6.png`. A fake-checkerboard edit output was discarded. No background-removal fallback was used, and no unapproved fallback art was introduced.

## Remaining blockers and boundaries

Four decision-folder event-detail binaries (`event_dhrondan_accord.dds`, `event_dhrondan_contact.dds`, `event_dhrondan_landing.dds`, and `event_dhrondan_rebellion.dds`) and three unconsumed event-picture binaries (`event016_dhrondan_news_envoy.dds`, `event016_dhrondan_news_rebellion.dds`, and `event016_dhrondan_special_project_envoy_craft.dds`) were inspected but have no authoritative sprite token in the scoped event/decision/project sources. No guessed registrations were added. The parent moved these seven candidates out of runtime and preserved them under `docs/assets/016_brilliant_scientist/dhrondan_icon_asset_completion/unconsumed_dds/` for a future gameplay owner that introduces exact consumers. This does not block the current `.40-.52` and DHR decision/project consumer audit.

The handoff does not cover portraits, gameplay, localisation, spreadsheets, country/focus/decision logic, achievement production, or any 3D model/entity/audio package.
