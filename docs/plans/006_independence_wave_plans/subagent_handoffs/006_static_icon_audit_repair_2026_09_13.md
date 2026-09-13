# Event 006 static icon audit and repair handoff

Date: 2026-09-13.

Owner: bounded static gameplay/icon asset auditor for Event 006.

Status: complete with no repairs.

## Scope

This audit covered ASSET-007 through ASSET-038, ASSET-049, all 16 delivered ASSET-047 achievement triplets including the separately reviewed Assyria triplet, and the already-authorized FORM-05 and FORM-48 emblems.

No gameplay, localisation, spreadsheet, or broad `.gfx` wiring file was edited.

No source, processed, or final asset was changed because the reviewed packages met their registered dimensions, alpha, visual, DDS, and path requirements.

## Reviewed focus assets

All focus source masters were individually opened from `docs/assets/006_independence_wave/source_png/focuses/`, all processed PNGs were reviewed in `docs/assets/006_independence_wave/contact_sheets/006_icon_focuses_contact_sheet.png`, and all final DDS decodes were reviewed in `docs/assets/006_independence_wave/contact_sheets/006_icon_dds_decoded_contact_sheet.png`.

| Registry row | Exact stem | Source | Processed | Final DDS | Result |
| --- | --- | --- | --- | --- | --- |
| ASSET-007 | `goal_independence_wave_founding_administration` | `goal_independence_wave_founding_administration_source.png` | `goal_independence_wave_founding_administration.png` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_founding_administration.dds` | complete |
| ASSET-008 | `goal_independence_wave_constitutional_state` | `goal_independence_wave_constitutional_state_source.png` | `goal_independence_wave_constitutional_state.png` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_constitutional_state.dds` | complete |
| ASSET-009 | `goal_independence_wave_popular_councils` | `goal_independence_wave_popular_councils_source.png` | `goal_independence_wave_popular_councils.png` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_popular_councils.dds` | complete |
| ASSET-010 | `goal_independence_wave_traditional_restoration` | `goal_independence_wave_traditional_restoration_source.png` | `goal_independence_wave_traditional_restoration.png` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_traditional_restoration.dds` | complete |
| ASSET-011 | `goal_independence_wave_military_emergency` | `goal_independence_wave_military_emergency_source.png` | `goal_independence_wave_military_emergency.png` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_military_emergency.dds` | complete |
| ASSET-012 | `goal_independence_wave_patron_client` | `goal_independence_wave_patron_client_source.png` | `goal_independence_wave_patron_client.png` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_patron_client.dds` | complete |
| ASSET-013 | `goal_independence_wave_recognition_diplomacy` | `goal_independence_wave_recognition_diplomacy_source.png` | `goal_independence_wave_recognition_diplomacy.png` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_recognition_diplomacy.dds` | complete |
| ASSET-014 | `goal_independence_wave_army_integration` | `goal_independence_wave_army_integration_source.png` | `goal_independence_wave_army_integration.png` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_army_integration.dds` | complete |
| ASSET-015 | `goal_independence_wave_infrastructure_authority` | `goal_independence_wave_infrastructure_authority_source.png` | `goal_independence_wave_infrastructure_authority.png` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_infrastructure_authority.dds` | complete |
| ASSET-016 | `goal_independence_wave_former_host_settlement` | `goal_independence_wave_former_host_settlement_source.png` | `goal_independence_wave_former_host_settlement.png` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_former_host_settlement.dds` | complete |
| ASSET-017 | `goal_independence_wave_league_congress` | `goal_independence_wave_league_congress_source.png` | `goal_independence_wave_league_congress.png` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_league_congress.dds` | complete |
| ASSET-018 | `goal_independence_wave_regional_formable` | `goal_independence_wave_regional_formable_source.png` | `goal_independence_wave_regional_formable.png` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_regional_formable.dds` | complete |
| ASSET-019 | `goal_independence_wave_high_chaos_sovereignty` | `goal_independence_wave_high_chaos_sovereignty_source.png` | `goal_independence_wave_high_chaos_sovereignty.png` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_high_chaos_sovereignty.dds` | complete |

The 13 processed focus files are exactly 94x86 RGBA with alpha extrema 0 and 255.

Each decoded focus DDS is exactly 94x86 with the expected legacy 32-bit BGRA DDS header and is pixel-equal to its processed PNG after decode.

The source art is visually distinct by focus role and contains no malformed subject, clipped subject, or unintended duplicate family art.

## Reviewed idea assets

All idea source masters were individually opened from `docs/assets/006_independence_wave/source_png/ideas/`, all processed PNGs were reviewed in `docs/assets/006_independence_wave/contact_sheets/006_icon_ideas_contact_sheet.png`, and all final DDS decodes were reviewed in `docs/assets/006_independence_wave/contact_sheets/006_icon_dds_decoded_contact_sheet.png`.

| Registry row | Exact stem | Source | Processed | Final DDS | Result |
| --- | --- | --- | --- | --- | --- |
| ASSET-020 | `idea_independence_wave_improvised_government` | `idea_independence_wave_improvised_government_source.png` | `idea_independence_wave_improvised_government.png` | `gfx/interface/ideas/006_independence_wave/idea_independence_wave_improvised_government.dds` | complete |
| ASSET-021 | `idea_independence_wave_unrecognized_state` | `idea_independence_wave_unrecognized_state_source.png` | `idea_independence_wave_unrecognized_state.png` | `gfx/interface/ideas/006_independence_wave/idea_independence_wave_unrecognized_state.dds` | complete |
| ASSET-022 | `idea_independence_wave_fragmented_command` | `idea_independence_wave_fragmented_command_source.png` | `idea_independence_wave_fragmented_command.png` | `gfx/interface/ideas/006_independence_wave/idea_independence_wave_fragmented_command.dds` | complete |
| ASSET-023 | `idea_independence_wave_unsettled_borders` | `idea_independence_wave_unsettled_borders_source.png` | `idea_independence_wave_unsettled_borders.png` | `gfx/interface/ideas/006_independence_wave/idea_independence_wave_unsettled_borders.dds` | complete |
| ASSET-024 | `idea_independence_wave_patron_pressure` | `idea_independence_wave_patron_pressure_source.png` | `idea_independence_wave_patron_pressure.png` | `gfx/interface/ideas/006_independence_wave/idea_independence_wave_patron_pressure.dds` | complete |
| ASSET-025 | `idea_independence_wave_league_membership` | `idea_independence_wave_league_membership_source.png` | `idea_independence_wave_league_membership.png` | `gfx/interface/ideas/006_independence_wave/idea_independence_wave_league_membership.dds` | complete |
| ASSET-026 | `idea_independence_wave_founding_identity` | `idea_independence_wave_founding_identity_source.png` | `idea_independence_wave_founding_identity.png` | `gfx/interface/ideas/006_independence_wave/idea_independence_wave_founding_identity.dds` | complete |
| ASSET-049 | `idea_independence_wave_post_release_instability` | `idea_independence_wave_post_release_instability_source.png` | `idea_independence_wave_post_release_instability.png` | `gfx/interface/ideas/006_independence_wave/idea_independence_wave_post_release_instability.dds` | complete |

The eight processed idea files are exactly 64x64 RGBA with alpha extrema 0 and 255.

Each decoded idea DDS is exactly 64x64 with the expected legacy 32-bit BGRA DDS header and is pixel-equal to its processed PNG after decode.

The source art is visually distinct by state and pressure role, with no malformed subject, clipped subject, or cross-family substitution.

## Reviewed decision and mission assets

All decision and mission source masters were individually opened from `docs/assets/006_independence_wave/source_png/decisions/`, all processed PNGs were reviewed in `docs/assets/006_independence_wave/contact_sheets/006_icon_decisions_contact_sheet.png`, and all final DDS decodes were reviewed in `docs/assets/006_independence_wave/contact_sheets/006_icon_dds_decoded_contact_sheet.png`.

The exact 12 stems are `decision_independence_wave_recognition_actions`, `decision_independence_wave_government_actions`, `decision_independence_wave_army_integration_actions`, `decision_independence_wave_depot_border_actions`, `decision_independence_wave_former_host_negotiations`, `decision_independence_wave_patron_aid`, `decision_independence_wave_patron_balancing`, `decision_independence_wave_network_aid`, `decision_independence_wave_league_votes`, `decision_independence_wave_border_arbitration`, `decision_independence_wave_formable_proclamation`, and `decision_independence_wave_integration_missions`.

These correspond to ASSET-027 through ASSET-038 in order.

Every source, processed, and final path follows the same stem with `_source.png`, `.png`, and `.dds` suffixes under `source_png/decisions/`, `processed_png/decisions/`, and `gfx/interface/decisions/006_independence_wave/` respectively.

The 12 processed decision files are exactly 32x32 RGBA with alpha extrema 0 and 255.

Each decoded decision DDS is exactly 32x32 with the expected legacy 32-bit BGRA DDS header and is pixel-equal to its processed PNG after decode.

The source art is visually distinct and legible at native size, with no malformed subject, clipped subject, or cross-family substitution.

## Reviewed achievement triplets

The 15 primary ASSET-047 IDs are `chaosx_006_one_state_to_statehood`, `chaosx_006_no_master`, `chaosx_006_peace_with_host`, `chaosx_006_break_reconquest`, `chaosx_006_found_league`, `chaosx_006_cross_regional_league`, `chaosx_006_rescue_member`, `chaosx_006_regional_formable`, `chaosx_006_volga_bulgaria`, `chaosx_006_small_to_major`, `chaosx_006_radical_bloc`, `chaosx_006_every_flag_survival`, `chaosx_006_balanced_patrons`, `chaosx_006_league_arbitrator`, and `chaosx_006_host_remnant`.

The separately reviewed 16th triplet is `chaosx_006_assyria_survives` from `docs/assets/006_independence_wave/iw043_iw058_static_icons_2026_07_18/`.

All 15 primary source masters were individually opened from `docs/assets/006_independence_wave/source_png/achievements/` using the exact `<id>_source.png` names.

All 15 primary color, grey, and not-eligible processed states were reviewed in `docs/assets/006_independence_wave/processed_png/achievements/` and in the native-size `docs/assets/006_independence_wave/contact_sheets/006_icon_achievements_contact_sheet.png`.

The Assyria source and all three processed states were individually opened, and the package review sheet `docs/assets/006_independence_wave/iw043_iw058_static_icons_2026_07_18/validation/review/native/achievements_native.png` was reviewed.

Every final triplet is directly under `gfx/achievements/` as `<id>.dds`, `<id>_grey.dds`, and `<id>_not_eligible.dds`.

The prescribed audit command passed for the primary triplets:

```text
python -B .agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py --audit --input docs/assets/006_independence_wave/processed_png/achievements --output-dir gfx/achievements
AUDIT OK for all 15 primary achievement triplets.
```

The prescribed audit command also passed for Assyria:

```text
python -B .agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py --audit --input docs/assets/006_independence_wave/iw043_iw058_static_icons_2026_07_18/processed_png/achievements --output-dir gfx/achievements
AUDIT OK chaosx_006_assyria_survives.
```

All final achievement DDS files are strict 64x64 legacy BGRA triplets with source-layer equality verified by the prescribed processor audit.

The decoded final achievement alpha range of 254 through 255 is expected because the immutable completed or grey template is composited beneath the subject layer.

Direct final-DDS-to-subject pixel inequality is expected for the same template-underlay reason and is not a defect.

The immutable template and overlay inputs were not edited or replaced.

## Reviewed authorized formable emblems

FORM-05 was reviewed from `docs/assets/006_independence_wave/form05_mediterranean_assets_2026_07_16/source_png/emblems/independence_wave_formable_form_05_alpha_master.png`, `docs/assets/006_independence_wave/form05_mediterranean_assets_2026_07_16/processed_png/emblems/independence_wave_formable_form_05.png`, and `gfx/interface/006_independence_wave/emblems/independence_wave_formable_form_05.dds`.

FORM-48 was reviewed from `docs/assets/006_independence_wave/form48_pacific_assets_2026_07_17/source_png/emblems/independence_wave_formable_form_48_alpha_master.png`, `docs/assets/006_independence_wave/form48_pacific_assets_2026_07_17/processed_png/emblems/independence_wave_formable_form_48.png`, and `gfx/interface/006_independence_wave/emblems/independence_wave_formable_form_48.dds`.

The FORM-05 and FORM-48 package contact sheets `006_form05_ui_icons_contact_sheet.png` and `006_form48_emblem_source_and_runtime.png` were reviewed.

Both processed and decoded final emblems are exact 128x128 RGBA assets with alpha extrema 0 and 255, and processed-to-DDS decoded pixel equality passed.

The source alpha masters retain the recorded fallback lineage and show no clipped edges, coloured spill, halo, fake checkerboard, or unintended transparent hole in the processed or final outputs.

No other formable emblem family was promoted or substituted.

## Source alpha and fallback evidence

The primary Event 006 icon prompt file `docs/assets/006_independence_wave/prompts/006_icon_prompts.md` records that the untouched generated masters use uniform `#ff00ff` chroma backgrounds.

The owned processor `.tools/process_independence_wave_icons.py` records the approved fallback helper and exact settings: `C:/Users/klimp/.codex/skills/.system/imagegen/scripts/remove_chroma_key.py --auto-key border --soft-matte --transparent-threshold 12 --opaque-threshold 220 --edge-contract 1 --despill --force`.

The FORM-05 and FORM-48 package prompt and validation files record their respective untouched raw sources, alpha-master outputs, fallback helper settings, and visual checks.

The opaque source masters are therefore documented processing inputs rather than evidence of a final runtime defect.

All processed and decoded runtime visuals were checked for key-colour spill, matte edges, halos, fake checkerboards, and unintended holes, and none were found.

No native ImageGen replacement was justified.

## Canonical references and runtime path audit

The canonical reference contact sheets and matching references were inspected only under `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/`.

The inspected families were `icons/national_focus`, `icons/ideas`, `icons/decisions`, `icons/missions`, and `icons/achievements`, including the achievement template inputs.

The close vanilla runtime definitions `interface/goals.gfx`, `interface/goals_shine.gfx`, `interface/ideas.gfx`, and `interface/decisions.gfx` were reviewed for sprite family, texture path, alpha behavior, and focus-shine conventions.

The project file `interface/006_independence_wave.gfx` contains all 13 expected focus base sprites, all 13 expected focus shine sprites, all eight expected idea sprites, and all 12 expected decision or mission sprites pointing to the reviewed DDS paths.

The project file `interface/006_independence_wave_small_assets.gfx` contains the exact FORM-05 and FORM-48 emblem texture paths.

No missing runtime path, stale target path, duplicate exact sprite definition, cross-family texture substitution, or unauthorized extra family was found in the reviewed wiring.

No `.gfx` file was edited because wiring ownership remains with the parent.

## Final status and blockers

Complete deliverables are 13 focus icons, eight idea icons, 12 decision or mission icons, 16 achievement triplets, and two authorized formable emblems.

No concrete repair was found, so no asset file changed.

There are no in-scope static-asset blockers or needs-user-review rows.

Live game consumer validation remains the parent and user acceptance gate and is not claimed by this source/DDS audit.

No unauthorized extra family, blocked formable emblem, portrait, flag, gameplay file, localisation file, spreadsheet, or broad wiring edit was created.

This handoff is the only file created by this subagent for the audit, and no changes were staged or committed.
