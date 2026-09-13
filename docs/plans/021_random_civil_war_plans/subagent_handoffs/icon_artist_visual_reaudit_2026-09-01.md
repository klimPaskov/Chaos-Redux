# Event 021 icon artist visual re-audit handoff

Date: 2026-09-01

Scope: The bounded Event 021 Random Civil War icon package only; one decision category icon, eleven decision icons, three mission icons, three idea icons, and six achievement triplets, for 36 runtime DDS files total.

## Result

No material defect was found in the processed or runtime icon package that justifies replacing the art.

All 36 assigned runtime DDS files were decoded from their installed paths, visually reviewed through the fresh source/processed/runtime and achievement-triplet contact sheets, and checked against the exact consumer mappings.

All 36 runtime DDS files are strict one-level legacy uncompressed BGRA DDS files with valid 128-byte headers, exact dimensions, and successful decode.

Every runtime DDS decoded pixel-for-pixel equal to its mapped processed PNG.

The final package is accepted with no icon-art mutation in this audit; parent reconciliation and any live in-game review remain outside this handoff.

## Consumer and meaning audit

The installed consumer was read from `interface/021_random_civil_war.gfx`, with the decision category and decision ownership checked against `common/decisions/categories/021_random_civil_war_categories.txt` and `common/decisions/021_random_civil_war_decisions.txt`, ideas checked against `common/ideas/021_random_civil_war_ideas.txt`, and achievement ids checked against `common/achievements/chaos_redux_achievements.txt`.

The category sprite is `GFX_decision_category_021_civil_war` at `gfx/interface/decisions/021_random_civil_war/decision_category_021_civil_war.dds`, targeting the 52x40 decision-category family and representing the Event 021 civil-war crisis.

The distinct decision sprites are `secure_arsenals`, `capital_defense`, `loyalty_review`, `opposition_depot`, `relief_corridor`, `emergency_settlement`, `reconstruction`, `priority_front`, `monitor_border`, `support_government`, and `support_opposition`, all at 32x32 and all mapped to their installed Event 021 DDS paths.

The intentional decision reuse was verified: depot seizure uses `opposition_depot`; formation integration and regional-administration review use `loyalty_review`; mediation, sponsor commitment, and coalition governance use `emergency_settlement`; disarmament and communications protection use `secure_arsenals`.

The three mission sprites are `hold_capital`, `secure_rail`, and `settlement_terms`, all at 32x32 and mapped to the three Event 021 mission consumers.

The three idea sprites are `fractured_command`, `war_torn_administration`, and `unsettled_settlement`, all at 64x64 and mapped to the Event 021 national-spirit consumers; the secured-front-depot idea intentionally reuses `fractured_command`.

The six achievement ids are `021_random_civil_war_hold_the_center`, `021_random_civil_war_no_state_left_behind`, `021_random_civil_war_a_flag_of_our_own`, `021_random_civil_war_war_within_a_war`, `021_random_civil_war_the_terms_hold`, and `021_random_civil_war_fractals_of_sovereignty`.

Each achievement has the required root completed, `_grey`, and `_not_eligible` DDS files directly under `gfx/achievements/`, for 18 runtime DDS files total.

## Reference and visual evidence

The canonical contact sheets were inspected before individual references from the exact skill-local root `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference`.

The inspected canonical families were `icons/decision_categories`, `icons/decisions`, `icons/missions`, `icons/ideas`, and `icons/achievements`, including the canonical achievement template files under `icons/achievements/template`.

The matching canonical category, decision, mission, idea, and achievement references were compared for family, compact silhouette scale, transparent-canvas behavior, contrast, and state treatment.

The current Event 021 contact sheets were also inspected, including `docs/assets/021_random_civil_war/contact_sheets/021_random_civil_war_icon_package_contact_sheet.png`, `icon_artist_021_missing_icons_contact_sheet.png`, `icon_artist_021_contrast_review.png`, and `021_random_civil_war_static_art_contact_sheet.png`.

Fresh audit evidence is under `docs/assets/021_random_civil_war/validation/icon_reaudit_2026-09-01/` and includes `runtime_audit.json`, `png_stats.json`, `source_processed_runtime_contact_sheet.png`, `achievements_runtime_triplets_contact_sheet.png`, and 36 freshly decoded runtime DDS PNGs under `decoded_dds/`.

## Technical verification

The category decoded as 52x40 with alpha range 0-255.

All eleven decisions decoded as 32x32 with alpha range 0-255.

All three missions decoded as 32x32 with alpha range 0-255.

All three ideas decoded as 64x64 with alpha range 0-255.

All 18 achievement states decoded as 64x64 with alpha range 254-255 after the required framed achievement compositing.

The strict DDS checks covered magic, header size, pixel-format size and flags, zero FourCC, 32-bit BGRA masks, texture caps, one mip level, exact pitch, and exact file length.

The native source masters are larger working inputs, while the processed PNGs are the exact consumer sizes; the source-to-processed size difference is expected and is not a cross-family resize defect.

## Achievement state construction

The exact immutable templates and overlay were inspected and retained with these SHA-256 hashes: `achievement_template.png` `248DB006611EB3942550C43DF83802AA6FB24761035FC928B5D34586C0C4C5BA`, `achievement_template_grey.png` `70E073694C1A7D9FE40C63B1EB2E987A8A45B3FFD15CCF789EEAA5B843B90022`, and `overlay.png` `89BC80C6AC975BF6F1FF000FF3070B20C337BFB8B8AE966AE35A5540C004D6DD`.

`process_achievement_icons.py --audit` returned `AUDIT OK` for all six Event 021 achievement ids using the exact 64x64 triplet sources under `processed_png/achievements/triplet_sources/` and the installed root DDS outputs.

The runtime triplets show aligned completed and grey subjects, with the unchanged red-cross overlay present only on the not-eligible state.

## Defects and disposition

The inherited source master `source_png/achievements/021_random_civil_war_hold_the_center_grey.png` has an opaque near-black full-canvas backdrop instead of native transparency.

The inherited source master `source_png/achievements/021_random_civil_war_war_within_a_war_not_eligible.png` has an opaque connected fake-checkerboard backdrop.

Both defects were visually inspected and confirmed by alpha statistics; the untouched source masters were preserved as evidence.

The existing verified fallback sources under `processed_png/achievements/fallback/` remove those unwanted backdrops, and the resulting 64x64 triplet sources, processed achievement PNGs, and runtime DDS files have transparent unused canvas and pass the runtime equality checks.

These inherited source-evidence defects do not appear in the installed runtime outputs, so no new ImageGen call, source replacement, processed-art replacement, or DDS replacement was justified.

Rejected checkerboard source files under `source_png/achievements/rejected/` were treated as review evidence only and were not runtime inputs.

No placeholder, painted control, painted text, fake checkerboard in the runtime output, opaque matte, cross-family resize, or consumer-meaning mismatch was found.

## Files changed

Created the audit evidence folder `docs/assets/021_random_civil_war/validation/icon_reaudit_2026-09-01/` with the fresh decoded DDS PNGs, runtime audit JSON, PNG statistics JSON, and two contact sheets listed above.

Created this handoff at `docs/plans/021_random_civil_war_plans/subagent_handoffs/icon_artist_visual_reaudit_2026-09-01.md`.

No source art, processed art, runtime DDS, GFX, GUI, gameplay, localisation, workbook, shared reference, `docs/assets/021_random_civil_war/manifest.md`, or `docs/assets/021_random_civil_war/gfx_handoff.md` file was edited.

## Blockers and review state

There is no bounded file-audit blocker and no requested icon repair remains outstanding.

Live engine validation was not performed by this subagent and remains user-owned; this handoff does not claim live-game evidence.

Status: complete for the assigned visual re-audit with no runtime asset replacement; parent review of this handoff and existing shared reconciliation remains required.
