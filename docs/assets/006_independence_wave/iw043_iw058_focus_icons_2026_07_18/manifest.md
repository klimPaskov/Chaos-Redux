# Event 006 IW-043 / IW-058 focus-icon package

Status: complete and handed off for parent-owned `.gfx`/focus integration.

## Scope

Exactly twenty original national-focus icons were generated with the built-in ImageGen workflow. Each source master is retained, chroma-keyed to a real alpha channel, finished on a transparent 94x86 canvas, converted to a legacy uncompressed BGRA DDS, and reviewed at native and 3x scale against the canonical national-focus reference contact sheet at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/national_focus/contact_sheet.png`.

Source mode: generated fictional/alternate-history symbolic art; no historical photograph or real-person likeness is used.

Package root: `docs/assets/006_independence_wave/iw043_iw058_focus_icons_2026_07_18/`

Runtime folder: `gfx/interface/goals/006_independence_wave/volga_assyria/`

Suggested `.gfx`: `interface/006_independence_wave_iw043_iw058_focus_icons.gfx` (already frozen by the parent).

## Asset inventory

All rows use the naming stem shown below. For each row, the source is `source_png/focuses/<stem>_source.png`, the processed preview is `processed_png/focuses/<stem>.png`, and the runtime file is `gfx/interface/goals/006_independence_wave/volga_assyria/<stem>.dds`.

| Stem | Sprite IDs | Related focus consumers | Size | State |
| --- | --- | --- | --- | --- |
| `goal_independence_wave_iw043_congress` | `GFX_goal_independence_wave_iw043_congress`, `_shine` | `independence_wave_iw043_open_middle_volga_congress`; `independence_wave_iw043_confirm_kazan_mandate`; `independence_wave_iw043_seat_the_delegations` | 94x86 RGBA | complete |
| `goal_independence_wave_iw043_navigation` | `GFX_goal_independence_wave_iw043_navigation`, `_shine` | `independence_wave_iw043_secure_volga_navigation`; `independence_wave_iw043_reopen_kazan_river_customs`; `independence_wave_iw043_repair_cheboksary_workshops`; `independence_wave_iw043_survey_rail_and_ferry_network`; `independence_wave_iw043_trade_beyond_the_middle_volga` | 94x86 RGBA | complete |
| `goal_independence_wave_iw043_rights_charter` | `GFX_goal_independence_wave_iw043_rights_charter`, `_shine` | `independence_wave_iw043_guarantee_language_and_municipal_rights` | 94x86 RGBA | complete |
| `goal_independence_wave_iw043_muftiate_civic_courts` | `GFX_goal_independence_wave_iw043_muftiate_civic_courts`, `_shine` | `independence_wave_iw043_settle_muftiate_and_civic_jurisdiction` | 94x86 RGBA | complete |
| `goal_independence_wave_iw043_river_guard` | `GFX_goal_independence_wave_iw043_river_guard`, `_shine` | `independence_wave_iw043_organize_the_river_guard`; `independence_wave_iw043_authorize_emergency_navigation_council`; `independence_wave_iw043_return_guard_to_civilian_law` | 94x86 RGBA | complete |
| `goal_independence_wave_iw043_bolgar_constitution` | `GFX_goal_independence_wave_iw043_bolgar_constitution`, `_shine` | `independence_wave_iw043_recover_bolgar_civic_memory`; `independence_wave_iw043_bind_crescent_to_congress`; `independence_wave_iw043_proclaim_modern_volga_bulgaria` | 94x86 RGBA | complete |
| `goal_independence_wave_iw043_federal_chamber` | `GFX_goal_independence_wave_iw043_federal_chamber`, `_shine` | `independence_wave_iw043_charter_chamber_of_peoples`; `independence_wave_iw043_federalize_river_cities`; `independence_wave_iw043_ratify_modern_volga_federation` | 94x86 RGBA | complete |
| `goal_independence_wave_iw043_form12_congress` | `GFX_goal_independence_wave_iw043_form12_congress`, `_shine` | `independence_wave_iw043_negotiate_volga_ural_accessions`; `independence_wave_iw043_convene_volga_ural_federal_congress` | 94x86 RGBA | complete |
| `goal_independence_wave_iw043_form13_compact` | `GFX_goal_independence_wave_iw043_form13_compact`, `_shine` | `independence_wave_iw043_invite_idel_ural_delegations`; `independence_wave_iw043_convene_idel_ural_compact` | 94x86 RGBA | complete |
| `goal_independence_wave_iw058_provisional_council` | `GFX_goal_independence_wave_iw058_provisional_council`, `_shine` | `independence_wave_iw058_assemble_provisional_national_council`; `independence_wave_iw058_seat_church_civic_and_village_delegates` | 94x86 RGBA | complete |
| `goal_independence_wave_iw058_four_guarantees` | `GFX_goal_independence_wave_iw058_four_guarantees`, `_shine` | `independence_wave_iw058_write_four_community_guarantees` | 94x86 RGBA | complete |
| `goal_independence_wave_iw058_church_civil_jurisdiction` | `GFX_goal_independence_wave_iw058_church_civil_jurisdiction`, `_shine` | `independence_wave_iw058_settle_church_and_civil_jurisdiction` | 94x86 RGBA | complete |
| `goal_independence_wave_iw058_diaspora_liaison` | `GFX_goal_independence_wave_iw058_diaspora_liaison`, `_shine` | `independence_wave_iw058_open_diaspora_liaison_bureau`; `independence_wave_iw058_link_synods_villages_and_diaspora`; `independence_wave_iw058_bind_diaspora_experts_to_public_service` | 94x86 RGBA | complete |
| `goal_independence_wave_iw058_levies_civilian_control` | `GFX_goal_independence_wave_iw058_levies_civilian_control`, `_shine` | `independence_wave_iw058_discipline_the_levies_board`; `independence_wave_iw058_authorize_levies_guardianship`; `independence_wave_iw058_restore_civilian_command` | 94x86 RGBA | complete |
| `goal_independence_wave_iw058_mosul_corridor` | `GFX_goal_independence_wave_iw058_mosul_corridor`, `_shine` | `independence_wave_iw058_hold_mosul_council_quarter`; `independence_wave_iw058_secure_nineveh_approaches`; `independence_wave_iw058_fortify_mountain_river_corridor` | 94x86 RGBA | complete |
| `goal_independence_wave_iw058_external_guarantee` | `GFX_goal_independence_wave_iw058_external_guarantee`, `_shine` | `independence_wave_iw058_request_external_guarantees`; `independence_wave_iw058_entrench_mosul_recognition`; `independence_wave_iw058_negotiate_former_host_settlement` | 94x86 RGBA | complete |
| `goal_independence_wave_iw058_church_civic_charter` | `GFX_goal_independence_wave_iw058_church_civic_charter`, `_shine` | `independence_wave_iw058_convene_concordat_council`; `independence_wave_iw058_charter_church_civic_compact`; `independence_wave_iw058_ratify_concordat_state` | 94x86 RGBA | complete |
| `goal_independence_wave_iw058_civic_assembly_charter` | `GFX_goal_independence_wave_iw058_civic_assembly_charter`, `_shine` | `independence_wave_iw058_convene_civic_national_assembly`; `independence_wave_iw058_charter_municipal_and_community_chambers`; `independence_wave_iw058_ratify_civic_national_state` | 94x86 RGBA | complete |
| `goal_independence_wave_iw058_mesopotamian_autonomy` | `GFX_goal_independence_wave_iw058_mesopotamian_autonomy`, `_shine` | `independence_wave_iw058_offer_mesopotamian_autonomy_charter`; `independence_wave_iw058_ratify_mesopotamian_settlement` | 94x86 RGBA | complete |
| `goal_independence_wave_iw058_form18_congress` | `GFX_goal_independence_wave_iw058_form18_congress`, `_shine` | `independence_wave_iw058_convene_mesopotamian_federal_congress` | 94x86 RGBA | complete |

## Retained evidence

- One prompt text file per source master under `prompts/`.
- `contact_sheets/006_iw043_iw058_focus_icons_source_contact_sheet.png`.
- `contact_sheets/006_iw043_iw058_focus_icons_native_contact_sheet.png`.
- `contact_sheets/006_iw043_iw058_focus_icons_3x_contact_sheet.png`.
- Native checkerboard reviews under `review_native/` and nearest-neighbour 3x reviews under `review_3x/`.
- `validation/validation.json` and `validation/hashes.sha256`.
- `_tooling/build_focus_icons.py` records the deterministic chroma removal, transparent canvas fitting, contact-sheet, and DDS conversion workflow.

## Status notes

All twenty icons are complete. No visual rejection or fallback was used. No blockers remain inside this bounded focus-icon package. The parent owns final runtime review and exact `.gfx`/focus loading attestation.
