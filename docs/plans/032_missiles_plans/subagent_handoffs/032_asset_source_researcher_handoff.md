# Event 32 Missile Asset Source Researcher Handoff

Disposition: superseded by the parent asset installation and audit pass. This handoff is retained as historical pre-wiring evidence from 2026-09-01; current consumers, final DDS files, hashes, decoded/reopened review, and the exact remaining native-raid blocker are authoritative in `docs/events/032_missiles/asset_audit.md`.

Status: bounded source, package, format, and consumer audit completed on 2026-09-01. Only this handoff file is being written by this subagent. No gameplay, localisation, interface, GFX definition, decision, event, achievement, or spreadsheet file was edited.

## Scope and inspected references

The audit followed `AGENTS.md`, the relevant sections of `chaos-redux-event-assets/SKILL.md`, and the Event 32 asset specifications.

The inspected Event 32 specification files were `docs/specs/032_missiles_specs/032_missiles_asset_prompt.md`, `docs/specs/032_missiles_specs/032_missiles_spec_part_7_assets_text_and_achievements.md`, `docs/specs/032_missiles_specs/032_missiles_package_manifest.md`, `docs/specs/032_missiles_specs/032_missiles_requirement_traceability.md`, and `docs/specs/032_missiles_specs/032_missiles_source_review.md`.

The complete existing package under `docs/assets/032_missiles` was enumerated, including its three main source/processed/DDS triplets, prompts, contact sheets, `manifest.md`, `gfx_handoff.md`, `icon_artist/review/preexisting_source_contact_sheet.png`, and 44 additional icon source PNGs.

The exact Chaos Redux consumers inspected were `events/032_missile_crisis.txt`, `common/decisions/categories/032_missiles_categories.txt`, `common/decisions/032_missiles_decisions.txt`, `common/decisions/032_missiles_missions.txt`, `common/ideas/032_missiles_ideas.txt`, and `common/dynamic_modifiers/032_missiles_state_modifiers.txt`.

The exact local registries inspected were `interface/chaosx_pictures.gfx`, `interface/chaosx_news_event_pictures.gfx`, `interface/chaosx_decision_category_pictures.gfx`, `interface/chaosx_decisions.gfx`, `interface/chaosx_ideas.gfx`, `interface/chaosx_dynamic_modifiers.gfx`, `interface/chaosx_texticons.gfx`, `interface/016_brilliant_scientist_project_icons.gfx`, `interface/023_sov_nuclear_bombs.gfx`, and `interface/031_random_terror.gfx`.

The installed vanilla consumers inspected were `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/eventpictures.gfx`, `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/decisions.gfx`, nearby vanilla decision-category definitions, and the installed DDS examples under `gfx/event_pictures` and `gfx/interface/decisions`.

The canonical review-only reference root inspected was `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference`, including its `README.md`, `CATALOG.md`, report contact sheet, news contact sheet, decision-category icon contact sheet, and decision-category picture contact sheet.

## Executive findings

The report, news, and category-picture packages contain technically valid generated source, processed preview, and final DDS evidence, but they are not installed under engine-facing `gfx/` paths and their handoff sprite names do not match the current Event 32 consumer tokens.

The current Event 32 consumers reference several sprite names that have no local `.gfx` definition, including the report, news, category icon, category picture, idea, and state-modifier names. The package `gfx_handoff.md` proposes a second naming set and nonexistent generic registry filenames such as `interface/events.gfx` and `interface/decisions.gfx`; those proposals need parent correction before wiring.

The package manifest and coverage crosswalk document only the three full-canvas images. The package also contains 44 icon source PNGs, but these have no corresponding processed previews, DDS files, prompts, per-asset provenance, license/source records, or runtime registry rows in the package.

No internet-sourced or archival image was selected for Event 32 in this audit. The three documented full-canvas source files are recorded as built-in ImageGen outputs, so they must not be described as public-domain, Creative Commons, archival, or historically sourced images.

## Exact consumer crosswalk

| Surface | Exact live consumer | Current token(s) | Installed/local precedent | Native target and format | Package evidence | Audit status |
|---|---|---|---|---|---|---|
| Country report | `events/032_missile_crisis.txt`: `chaosx.nr32.2`, `chaosx.nr32.30`, `chaosx.nr32.31`, `chaosx.nr32.32`, `chaosx.nr32.40`, `chaosx.nr32.60`, and `chaosx.nr32.80` | `GFX_chaosx_report_032_missiles_country` | `interface/chaosx_pictures.gfx`; vanilla `interface/eventpictures.gfx` | 210x176; report-card treatment with RGBA transparency at corners; final legacy one-level 32-bit BGRA DDS | Complete source, prompt, processed PNG, and DDS triplet exists | Needs parent review and runtime wiring because the token is undefined and differs from the package proposal |
| Global news | `events/032_missile_crisis.txt`: `chaosx.nr32.3` `news_event` | `GFX_chaosx_news_032_missiles_proliferation` | `interface/chaosx_pictures.gfx` and `interface/chaosx_news_event_pictures.gfx`; vanilla `interface/eventpictures.gfx` | 397x153; black-and-white documentary treatment; current processed preview and DDS are opaque; final legacy one-level 32-bit BGRA DDS | Complete source, prompt, processed PNG, and DDS triplet exists | Needs parent review and runtime wiring because the token is undefined and differs from the package proposal |
| Decision-category picture | `common/decisions/categories/032_missiles_categories.txt`: `missiles_program_management_category` `picture` field | `GFX_decision_cat_picture_032_missiles` | `interface/chaosx_decision_category_pictures.gfx`; vanilla `interface/decisions.gfx` | 114x101 opaque picture; this is the larger picture surface, not the small category icon; final legacy one-level 32-bit BGRA DDS | Complete source, prompt, processed PNG, and DDS triplet exists | Needs parent review and runtime wiring because the token is undefined and differs from the package proposal |
| Decision-category icon | `common/decisions/categories/032_missiles_categories.txt`: `missiles_program_management_category` `icon` field | `GFX_decision_category_032_missiles` | `interface/chaosx_decisions.gfx`; vanilla category sprites in `interface/decisions.gfx` | Transparent small category-icon family; canonical references are approximately 49–53x39–42, with 50x40 a normal target; final DDS must preserve alpha | No dedicated Event 32 category-icon final or defensible source package exists | Blocked for this source package; do not resize or substitute the category picture |
| Program ideas | `common/ideas/032_missiles_ideas.txt`: `missiles_program_experimental`, `missiles_program_operational`, and `missiles_program_compromised` | `GFX_idea_032_missiles_program_initial`, `GFX_idea_032_missiles_program_mature`, and `GFX_idea_032_missiles_program_compromised` | `interface/chaosx_ideas.gfx` | Conventional idea-icon family, normally 64x64 unless the exact installed consumer/reference requires otherwise; preserve alpha in final DDS | Three source-only PNGs exist under `icons/source_png/ideas`; no prompts, provenance, processed previews, DDS, or `.gfx` rows | Needs source/provenance review and completion by the asset owner; not a final handoff |
| Launch-site state modifiers | `common/dynamic_modifiers/032_missiles_state_modifiers.txt`: active, hardened, damaged, compromised, and rogue modifier definitions | `GFX_idea_032_missiles_launch_site_active`, `GFX_idea_032_missiles_launch_site_hardened`, `GFX_idea_032_missiles_launch_site_damaged`, `GFX_idea_032_missiles_launch_site_compromised`, and `GFX_idea_032_missiles_launch_site_rogue` | `interface/chaosx_dynamic_modifiers.gfx` | Conventional modifier/idea-icon family, normally 64x64 unless the exact installed consumer/reference requires otherwise; preserve alpha in final DDS | Five source-only PNGs exist under `icons/source_png/state_modifiers`; no prompts, provenance, processed previews, DDS, or `.gfx` rows | Needs source/provenance review and completion by the asset owner; not a final handoff |
| Decisions | `common/decisions/032_missiles_decisions.txt`: 43 Event 32 decision definitions | All 43 currently reuse the four existing `GFX_decision_brilliant_scientist_project_rocketry_propulsion_*` sprites defined in `interface/016_brilliant_scientist_project_icons.gfx` | Existing exact reusable 016 project-icon family | Existing reused icons are already wired; Event 32-specific icons would normally be 64x64 transparent DDS assets | 24 Event 32 decision source PNGs exist, but none is processed or runtime-registered | Current reuse is technically available, but it does not satisfy the Event 32-specific icon inventory without an explicit parent design decision |
| Missions | `common/decisions/032_missiles_missions.txt`: `missiles_launch_state_survey_mission`, `missiles_secondary_site_construction_mission`, `missiles_site_repair_mission`, `missiles_site_recovery_mission`, `missiles_precision_strike_preparation_mission`, `missiles_strategic_barrage_preparation_mission`, `missiles_saturation_barrage_preparation_mission`, `missiles_counterforce_preparation_mission`, `missiles_warning_verification_mission`, and `missiles_retaliation_network_restoration_mission` | All 10 currently reuse the same four existing Brilliant Scientist project icons | `interface/016_brilliant_scientist_project_icons.gfx` | Event-specific mission icons would normally be 64x64 transparent DDS assets | No Event 32 mission icon package exists | Missing; do not silently treat decision source PNGs or generic 016 project icons as Event 32 mission coverage |
| Texticons | No exact Event 32 consumer token was found in the inspected current events, interface, or localisation files | Candidate source names are `032_missiles_command_control`, `032_missiles_launch_readiness`, and `032_missiles_operational_reserve` | `interface/chaosx_texticons.gfx` is the relevant registry to inspect after a parent-owned consumer is exposed | Use the exact texticon consumer family; do not assume the source canvas is the runtime size; preserve alpha | Three source-only PNGs exist under `icons/source_png/texticons` with no provenance, processed PNG, DDS, or registry rows | Unscoped until a real consumer/token is confirmed; parent should not wire by inference |

The hidden dispatcher `chaosx.nr32.1` has no picture consumer and does not require an asset row.

## Main generated asset evidence

The package `manifest.md`, prompts, source files, processed previews, and DDS files consistently identify the three full-canvas assets as generated on 2026-08-29 with built-in ImageGen provenance. The package records the original generated-image paths, and the retained source copies below are the source files that should be used for any parent review.

| Asset | Source path and source hash | Processed path and hash | DDS path, dimensions, length, and hash | Source/era/license note |
|---|---|---|---|---|
| Country report | `docs/assets/032_missiles/source_png/032_missiles_country_report_source.png`; 1122x1402 RGB; SHA-256 `c6e961abaa616bc5d32315da27e57a2c50c5f43a46330dc3a9e5b528f71c0284` | `docs/assets/032_missiles/processed_png/032_missiles_country_report.png`; 210x176 RGBA; SHA-256 `56a75ddf1f47f913620dd4be2e58e7f353a95cbc8ce6a69e7ff2c3ab4115c430` | `docs/assets/032_missiles/dds/032_missiles_country_report.dds`; 210x176; 147,968 bytes; SHA-256 `6f9429f0f6d4b8743b1e554a2b3c50b6cbd51722fd6a0cc51ca8e7992a64f685` | Fictional period-authentic industrial missile scene; generated, not an archival or public-domain photograph; no external license claim |
| Global news | `docs/assets/032_missiles/source_png/032_missiles_global_proliferation_news_source.png`; 1792x878 RGB; SHA-256 `738ce640d57147fc873a07d1c6a2ab6e9c3b08a2d1bde5cfd8c2ccd8d475a4a9` | `docs/assets/032_missiles/processed_png/032_missiles_global_proliferation_news.png`; 397x153 RGBA; SHA-256 `ac92b24cf9d44a66170a5238915d7b64bace41b593e05d4cce187407988547d7` | `docs/assets/032_missiles/dds/032_missiles_global_proliferation_news.dds`; 397x153; 243,092 bytes; SHA-256 `c9da74d25c7a1d2462293d363df5c0e88928251c9f9cd216d2e5a237b1b9f444` | Fictional black-and-white documentary-style launch scene with no flags or text; generated, not an archival or public-domain photograph; no external license claim |
| Category picture | `docs/assets/032_missiles/source_png/032_missiles_program_category_source.png`; 1254x1254 RGB; SHA-256 `5045035288b0885280b9577f5494e12d440ceac91fe412060eb37281dd68efbe` | `docs/assets/032_missiles/processed_png/032_missiles_program_category.png`; 114x101 RGB; SHA-256 `a6196c6209159c6c45d363e5233c5f6738b8b1a29d28cdecefa3a17877971bb9` | `docs/assets/032_missiles/dds/032_missiles_program_category.dds`; 114x101; 46,184 bytes; SHA-256 `cd43aa6161a99cb8aad74a434e239328a2f014029ee7c0b90478ee01041e0d15` | Fictional period-authentic hardened-launch scene; generated, not an archival or public-domain photograph; no external license claim |

The processed report has an alpha range of 0–255 and retains the required transparent card corners and shadow treatment. The processed news image is opaque with alpha 255 throughout. The processed category picture is opaque RGB. All three DDS files were checked read-only as legacy one-level 32-bit BGRA textures with the expected 124-byte DDS header, BGRA masks, texture caps, exact dimensions, and exact file lengths.

The prompt files are `docs/assets/032_missiles/prompts/032_missiles_country_report_prompt.md`, `docs/assets/032_missiles/prompts/032_missiles_global_proliferation_news_prompt.md`, and `docs/assets/032_missiles/prompts/032_missiles_program_category_prompt.md`. The package manifest records the original built-in ImageGen outputs under `C:/Users/klimp/.codex/generated_images/01a04efc-747a-7530-816b-6a5ff6121572/exec-a836f221-f671-422c-a790-31143ecf1029.png`, `C:/Users/klimp/.codex/generated_images/01a04efc-747a-7530-816b-6a5ff6121572/exec-40f996cf-6429-4eff-ae6c-81a626aa3a08.png`, and `C:/Users/klimp/.codex/generated_images/01a04efc-747a-7530-816b-6a5ff6121572/exec-de19b24b-e7c7-453b-8a3c-3fbdb6b649d4.png` respectively.

The canonical report references are 210x176 sepia/black-and-white report cards with transparent corners and slight card treatment. The canonical news references are 397x153 black-and-white documentary images. The canonical decision-category picture references are 114x101 opaque images. The existing three generated assets fit those families visually and dimensionally, subject to normal parent review for style and final runtime use.

## Icon package evidence and provenance limits

The package contains 44 additional source-only PNGs: 24 files under `icons/source_png/decisions`, 5 under `icons/source_png/guidance`, 3 under `icons/source_png/ideas`, 4 under `icons/source_png/postures`, 5 under `icons/source_png/state_modifiers`, and 3 under `icons/source_png/texticons`.

The 24 decision source filenames are `decision_032_missiles_compensate_neutral_victim.png`, `decision_032_missiles_counterforce_strike.png`, `decision_032_missiles_establish_command_authority.png`, `decision_032_missiles_establish_secondary_site.png`, `decision_032_missiles_expand_capacity.png`, `decision_032_missiles_harden_site.png`, `decision_032_missiles_improve_guidance.png`, `decision_032_missiles_inspect_incident.png`, `decision_032_missiles_integrate_special_payload.png`, `decision_032_missiles_isolate_site.png`, `decision_032_missiles_negotiate_with_command.png`, `decision_032_missiles_precision_strike.png`, `decision_032_missiles_replenish_reserve.png`, `decision_032_missiles_restore_readiness.png`, `decision_032_missiles_rotate_emergency_codes.png`, `decision_032_missiles_saturation_barrage.png`, `decision_032_missiles_scuttle_site.png`, `decision_032_missiles_secure_launch_codes.png`, `decision_032_missiles_select_missile_target.png`, `decision_032_missiles_send_loyal_forces.png`, `decision_032_missiles_strategic_barrage.png`, `decision_032_missiles_survey_launch_state.png`, `decision_032_missiles_suspend_damaged_site.png`, and `decision_032_missiles_verify_warning.png`.

The accepted Event 32 decision inventory names at least three additional distinct actions for which no exact source filename exists: delay retaliation, sever the retaliation network, and restore the retaliation network. The source names also differ from some current consumers, such as `secure_launch_codes` versus `missiles_secure_launch_authority`, and shared `scuttle_site` or `isolate_site` names may only cover multiple consumers if the parent explicitly accepts that merge.

The decision source PNGs are large RGBA canvases approximately 1273–1275x1234–1236. The idea, guidance, posture, state-modifier, and texticon source PNGs are also large RGBA canvases, with the documented exceptions `idea_032_missiles_program_initial.png` at 1421x1107 and `posture_automatic.png` at 1312x1199. These are source canvases, not final runtime dimensions.

The `icon_artist/review/preexisting_source_contact_sheet.png` visibly shows distinct transparent icon candidates, but the package contains no prompt, creator record, source link, generation date, license statement, or per-file provenance for those candidates. Their appearance alone is not evidence that they were generated, sourced, public-domain, or Creative Commons. Do not promote them to final assets without a defensible provenance record and the required processed PNG/DDS evidence.

The `guidance_*` and `posture_*` files have no exact Event 32 consumer token in the inspected local events, interface, or localisation sources and are not standalone accepted visual families in the hard Event 32 asset list. They are package extras and must not be counted as coverage until a parent-owned consumer and manifest row exists.

## Reused versus generated assets

The three full-canvas report/news/category-picture assets are generated assets with retained prompts and built-in ImageGen provenance. No public-domain or Creative Commons assertion is valid for them.

The current Event 32 decisions and missions reuse the existing Brilliant Scientist project icon sprites from `interface/016_brilliant_scientist_project_icons.gfx`. Those are valid existing runtime assets, but they are generic/reused coverage rather than Event 32-specific artwork.

The canonical vanilla reference PNGs are review material only and must never be copied into runtime paths as if they were new mod assets.

The 44 additional Event 32 icon PNGs are unattributed source-only inputs. This handoff makes no claim about their source mode, producer, date, license, or generation method.

No portrait, flag, raid, payload, achievement, or super-event asset was selected or changed by this source audit. Character portraits remain outside this worker's scope and must go to `chaosx_portrait_creator`.

## Missing, blocked, and needs-review surfaces

The following current consumer tokens are not defined in the inspected local GFX registries: `GFX_chaosx_report_032_missiles_country`, `GFX_chaosx_news_032_missiles_proliferation`, `GFX_decision_category_032_missiles`, `GFX_decision_cat_picture_032_missiles`, the three `GFX_idea_032_missiles_program_*` tokens, and the five `GFX_idea_032_missiles_launch_site_*` tokens.

The three full-canvas assets are technically complete as temporary evidence packages but remain `needs_user_review` for naming, registry placement, runtime copy, and parent wiring.

The category icon is blocked because no dedicated final or defensible source asset exists. The category picture must not be reused or resized into that surface.

The idea, state-modifier, decision, mission, and texticon families are blocked or needs-review as final Event 32 packages because their current package entries are source-only and lack processing, DDS conversion, provenance, and runtime registration. The parent may retain the current 016 decision/mission reuse only if that simplification is explicit and accepted in the Event 32 design record.

The package has no Event 32-specific mission icon coverage. The seven distinct mission-art surfaces named by the asset prompt therefore remain missing even though the current mission definitions display reused 016 project icons.

There is no defensible source basis for treating the package-only icon contact sheet as an archival or licensed source. No primitive substitute should be made for the missing category icon or missing exact decision actions.

## Concrete parent wiring recommendations

Preserve the current live consumer token names unless the parent deliberately updates every corresponding gameplay consumer and documentation row. The recommended one-to-one runtime mapping is:

| Current consumer token | Recommended runtime basename/path |
|---|---|
| `GFX_chaosx_report_032_missiles_country` | `gfx/event_pictures/032_missiles/032_missiles_country_report.dds` |
| `GFX_chaosx_news_032_missiles_proliferation` | `gfx/event_pictures/032_missiles/032_missiles_global_proliferation_news.dds` |
| `GFX_decision_cat_picture_032_missiles` | `gfx/interface/decisions/032_missiles/032_missiles_program_category.dds` |

The parent should define those three current token names in a registry that is actually loaded by this mod. The local repository has `interface/chaosx_pictures.gfx`, `interface/chaosx_news_event_pictures.gfx`, and `interface/chaosx_decision_category_pictures.gfx`; it does not currently have `interface/events.gfx` or `interface/decisions.gfx`. The nearest complete event-owned precedent is `interface/023_sov_nuclear_bombs.gfx`, which co-locates category picture/icon, report/news, idea, and decision sprite definitions, while `interface/031_random_terror.gfx` demonstrates paired category icon/category-picture definitions and a news sprite.

The category icon token `GFX_decision_category_032_missiles` should receive a dedicated transparent approximately 50x40 asset in the category-icon family through the parent-selected loaded registry. It must not point at `032_missiles_program_category.dds`.

The three idea tokens should be registered under the parent-selected loaded idea registry, and the five modifier tokens should be registered under the parent-selected loaded dynamic-modifier registry. The source filenames use `initial`, `mature`, `compromised`, and `modifier_*` labels, but the current consumer token names are authoritative until the parent intentionally changes them.

For decisions and missions, the parent should either retain the exact existing 016 reuse and record it as an accepted simplification, or commission a complete Event 32 icon package with stable current-token mappings, processed previews, final DDS files, provenance, and `.gfx` rows. Do not wire source PNG filenames directly and do not silently use one decision icon as mission coverage.

The three candidate texticon source files should remain unregistered until a parent-owned localisation or script consumer is confirmed. Once a real consumer exists, the parent should add the exact token-to-DDS mapping and update the coverage crosswalk rather than inferring a use from the filenames.

The parent should copy only final DDS files into engine-facing `gfx/event_pictures/...` or `gfx/interface/decisions/...` paths and retain `docs/assets/032_missiles` as evidence. The parent should then refresh `manifest.md`, `gfx_handoff.md`, and the requirement crosswalk with exact live token, registry, runtime basename, consumer IDs, source mode, provenance, license status, era-fit note, and uncertainty.

## Handoff boundary and remaining risk

This handoff is source and consumer evidence only. It does not authorize changes to gameplay consumers, localisation, interface registries, GFX definitions, decisions, events, achievements, or spreadsheets.

The central remaining risk is that the existing package documentation presents the three main images as ready for wiring while the current code uses different token names and the local registries contain no Event 32 definitions. A parent wiring pass must resolve that mismatch explicitly.

The second remaining risk is provenance overreach for the 44 icon source PNGs. They may be useful candidates for a later asset-production pass, but they are not complete sourced assets and this audit does not invent their source or license status.

No game launch, live consumer validation, or in-game render was performed. The read-only checks were limited to package enumeration, exact consumer/registry searches, canonical and vanilla reference inspection, image dimensions/alpha inspection, and DDS header/length verification.

Files changed by this subagent: `docs/plans/032_missiles_plans/subagent_handoffs/032_asset_source_researcher_handoff.md` only.
