# `docs/assets/` Cleanup Inventory — 2026-08-22

## Scope and method

This began as a read-only inventory of every top-level directory present under `docs/assets/` on 2026-08-22. The current-state refresh below supersedes its directory count and Git-state totals while preserving the package-by-package evidence from that snapshot.

I read `AGENTS.md` and the complete `.agents/skills/chaos-redux-event-assets/SKILL.md` before inspecting the workspaces.

The asset-skill contract treats `docs/assets/<event_id>_<event_slug>/` as temporary event-scoped evidence that remains while work is active, blocked, awaiting review, or under acceptance, and requires durable provenance, licensing, attribution, requirement-to-runtime crosswalks, review results, accepted handoff facts, and blocker notes to be promoted before deletion (`.agents/skills/chaos-redux-event-assets/SKILL.md:134-145`, `:147-163`, `:524-528`).

The separate `docs/assets/portraits/` tree is a durable grounded-portrait archive and must never be deleted as part of temporary-workspace cleanup (`.agents/skills/chaos-redux-event-assets/SKILL.md:147-163`, `:524-528`).

Events 21+ were not audited as standalone content; they were considered only when a shared runtime or archive reference was necessary to classify a workspace.

No asset, gameplay, localisation, workbook, GUI, GFX, sound, or interface file was changed.

## Current-state refresh — 2026-08-24

The refreshed physical tree contained 23 top-level directories, 28,427 files, and 56,979,143,899 bytes before empty-directory cleanup. Git reported 4,090 tracked paths, 2,568 modified tracked paths, and 24,341 ignored paths under `docs/assets/`; the very large ignored count remains evidence that normal `git status` is not a safe deletion inventory.

Three active workspaces were not present in the original table:

- `docs/assets/014_cannibalism/` contained 3,489 files and 8,409,639,013 bytes, with files modified on 2026-08-24. Its root manifest remains `needs_user_review`, and its model evidence includes provider, source, runtime-review, and blocked-package states. It is `retain_active_recent`.
- `docs/assets/019_infantry_spawn/` contained 1,434 ignored files and 577,198,292 bytes. Its manifest classifies former GUI rows as archival provenance but explicitly does not close the current provider-extension or whole-event documentation gate. Because the event package remains active and the workspace contains the durable evidence needed to disposition those rows, it is `retain_blocked_or_uncertain`; no partial evidence deletion was approved.
- `docs/assets/famine_and_migration_system/` contained 188 files and 99,222,937 bytes. Its asset rows are substantially produced, but parent consumer wiring, probability/MCP proof, runtime review, and system completion remain open. It is `retain_active_recent`.

The refreshed runtime-facing search across `common/`, `events/`, `interface/`, `gfx/`, `localisation/`, `sound/`, `music/`, and `history/` found no executable path into `docs/assets/`. The only matches were source-evidence comments in `sound/012_africa_strange_forces_sound.asset` and `interface/012_africa_animations.gfx`.

No complete event or shared-system workspace satisfied the skill requirement that all accepted runtime assets, provenance, licensing, crosswalks, review results, handoff facts, and unresolved dispositions be promoted before deletion. Recent modification time alone was never used as approval, and ignored status was never treated as deadness.

`docs/assets/chaos_warfare_system_audit/` contained only four empty subdirectories, zero files, zero bytes, zero Git paths, and no runtime references. After resolving the absolute path inside `docs/assets/` and verifying the zero-file condition, the four empty leaves and their empty parent were removed non-recursively. This removed no asset or recoverable content and reduced the current top-level directory count from 23 to 22.

The current filesystem still contains 95 `README.md` files under `docs/`. A refreshed local-link resolution pass found zero missing local targets. No central `docs/assets/README.md` was added because the package manifests and permanent plan/spec/event documents own status; a central asset index would duplicate volatile acceptance state.

## Verdict

Safe-delete-approved top-level directories: **none**.

The only `already_absent` entry is `docs/assets/chaos_warfare_system_audit/`: it has four empty physical subdirectories, zero files, zero bytes, and no tracked, non-ignored, or ignored file content. No deletion action is necessary or authorized.

`docs/assets/portraits/` is classified `retain_portrait_archive` regardless of current modification state.

The current tree contains 3,939 tracked `docs/assets` paths, 0 non-ignored untracked paths, 16,774 ignored untracked paths, and 2,544 modified tracked paths. Ignored files are still present workspaces and are not disposable merely because normal `git status` does not list them.

The runtime search across `gfx/`, `interface/`, `sound/`, `common/`, `events/`, and `localisation/` found no actual runtime path pointing into `docs/assets/`. The only four matches are comments documenting source evidence:

- `interface/chaosx_texticons.gfx:426` points to the CBRN request list.
- `sound/012_africa_strange_forces_sound.asset:2` points to preserved Event 012 model sources.
- `interface/006_independence_wave_macedonia_portraits.gfx:3` points to retained source evidence.
- `interface/012_africa_animations.gfx:2` points to retained animation frames and review GIFs.

No runtime path into `docs/assets/portraits/` was found, which is required by the portrait-archive contract.

## Top-level inventory and Git state

The size column includes ignored evidence files and binaries physically present in each workspace. `status` is the count of modified tracked paths under that exact top-level prefix at the time of this audit.

| Workspace | Files / directories / bytes | Newest file | Git state | Classification |
| --- | --- | --- | --- | --- |
| `docs/assets/002_zombie_outbreak/` | 3,270 / 416 / 16,373,512,493 bytes | `models_3d/demonic_zombies/manifest.md` — 2026-08-21 22:38:33 | 35 tracked; 3,235 ignored; 0 non-ignored untracked; status 0 | `retain_blocked_or_uncertain` |
| `docs/assets/006_independence_wave/` | 5,220 / 1,495 / 2,978,466,577 bytes | `source_placeholder_2026_08_03_iw043_iw058/review/source_placeholder_contact_sheet.png` — 2026-08-21 14:40:03 | 1,156 tracked; 4,064 ignored; 0 non-ignored untracked; status 608 | `retain_blocked_or_uncertain` |
| `docs/assets/006_independence_wave_california_civic_source_clearance/` | 5 / 3 / 399,637 bytes | `manifest.md` — 2026-07-24 21:39:10 | 0 tracked; 5 ignored; 0 non-ignored untracked; status 0 | `retain_blocked_or_uncertain` |
| `docs/assets/012_africa/` | 2,668 / 588 / 5,783,640,970 bytes | `tier_a_identity_icons/sources/tier_a_source_sheet.png` — 2026-08-21 14:40:09 | 1,016 tracked; 1,652 ignored; 0 non-ignored untracked; status 865 | `retain_blocked_or_uncertain` |
| `docs/assets/012_africa_priority_portraits_real_sources/` | 1 / 0 / 28,241 bytes | `manifest.md` — 2026-08-10 10:12:05 | 1 tracked; 0 ignored; 0 non-ignored untracked; status 0 | `retain_blocked_or_uncertain` |
| `docs/assets/012_africa_tiera_visual_packages/` | 89 / 9 / 46,390,131 bytes | `source_flags/stoneborn_dfx_relic_oath_route_master.png` — 2026-08-21 14:40:10 | 89 tracked; 0 ignored; 0 non-ignored untracked; status 63 | `retain_blocked_or_uncertain` |
| `docs/assets/012_africa_world_order/` | 425 / 13 / 167,794,842 bytes | `source_png/portrait_012_africa_fictional_the_green_v4_source.png` — 2026-08-21 14:40:12 | 425 tracked; 0 ignored; 0 non-ignored untracked; status 397 | `retain_blocked_or_uncertain` |
| `docs/assets/012_africa_world_order_flags/` | 159 / 4 / 52,303,835 bytes | `source_png/SOUTH_AMERICAN_SUN_COVENANT.png` — 2026-08-21 14:40:13 | 159 tracked; 0 ignored; 0 non-ignored untracked; status 157 | `retain_blocked_or_uncertain` |
| `docs/assets/016_brilliant_scientist/` | 2,862 / 296 / 2,775,589,645 bytes | `models_3d/alien_infantry/manifest.md` — 2026-08-22 12:34:38 | 60 tracked; 2,802 ignored; 0 non-ignored untracked; status 0 | `retain_blocked_or_uncertain` |
| `docs/assets/016_brilliant_scientist_dhrondan_event_art/` | 55 / 16 / 38,209,403 bytes | `contact_sheets/identity_art.png` — 2026-08-21 18:08:31 | 3 tracked; 52 ignored; 0 non-ignored untracked; status 0 | `retain_active_recent` |
| `docs/assets/020_black_plague/` | 97 / 30 / 72,484,729 bytes | `source_png/decisions/decision_weapon_delivery_imagegen_source.png` — 2026-08-21 14:40:13 | 64 tracked; 33 ignored; 0 non-ignored untracked; status 44 | `retain_blocked_or_uncertain` |
| `docs/assets/chaos_warfare_cbrn/` | 8 / 6 / 3,458,232 bytes | `cbrn_unit_texticon_requests.md` — 2026-08-15 22:12:37 | 0 tracked; 8 ignored; 0 non-ignored untracked; status 0 | `retain_blocked_or_uncertain` |
| `docs/assets/chaos_warfare_system/` | 2,539 / 372 / 6,393,916,218 bytes | `models_3d/cw_facility/runtime/handoff.md` — 2026-08-21 15:17:17 | 168 tracked; 2,371 ignored; 0 non-ignored untracked; status 131 | `retain_blocked_or_uncertain` |
| `docs/assets/chaos_warfare_system_audit/` | 0 / 4 / 0 bytes | none | 0 tracked; 0 ignored; 0 non-ignored untracked; status 0 | `already_absent` |
| `docs/assets/country_flags/` | 7 / 3 / 2,831,965 bytes | `cxt_test_country/gfx_handoff.md` — 2026-08-21 17:49:14 | 7 tracked; 0 ignored; 0 non-ignored untracked; status 0 | `retain_active_recent` |
| `docs/assets/portraits/` | 1,131 / 144 / 385,346,532 bytes | `012_africa/comfyui_source_inputs/README.md` — 2026-08-21 15:03:30 | 752 tracked; 379 ignored; 0 non-ignored untracked; status 279 | `retain_portrait_archive` |
| `docs/assets/shared_clone_system/` | 1,039 / 68 / 1,246,051,435 bytes | `models_3d/clone_infantry/counter_art/aryan_clone_infantry/gfx_handoff.md` — 2026-08-06 18:33:46 | 0 tracked; 1,039 ignored; 0 non-ignored untracked; status 0 | `retain_blocked_or_uncertain` |
| `docs/assets/shared_portal_raider_system/` | 137 / 42 / 684,420,951 bytes | `models_3d/portal_raider/evidence/counter/manifest.json` — 2026-08-09 23:44:18 | 0 tracked; 137 ignored; 0 non-ignored untracked; status 0 | `retain_blocked_or_uncertain` |
| `docs/assets/shared_robot_system/` | 781 / 50 / 2,529,573,450 bytes | `models_3d/autonomous_robot/runtime/handoff.md` — 2026-08-20 21:42:08 | 4 tracked; 777 ignored; 0 non-ignored untracked; status 0 | `retain_active_recent` |
| `docs/assets/system_camp_repression_rework/` | 220 / 70 / 1,715,301,813 bytes | `models_3d/extermination_camp_building/manifest.md` — 2026-08-03 15:42:48 | 0 tracked; 220 ignored; 0 non-ignored untracked; status 0 | `retain_blocked_or_uncertain` |

Git quotes two ignored Event 006 evidence paths because their filenames contain non-ASCII bytes; those two files are included in the corrected Event 006 ignored count and were not treated as disposable.

## Retention register, consumers, and promotion evidence

### `002_zombie_outbreak` — `retain_blocked_or_uncertain`

The demonic and infected model manifests say `ready_for_user_live_validation` and record runtime model promotion, but the same workspace contains the Event 002 counter handoff marked `needs_user_review` with runtime promotion intentionally withheld.

The infected provider evidence also contains `provider/credits/final_batch_blocker.json` with `status: blocked_insufficient_balance` and `promotion_status: blocked_before_rig_export`, which conflicts with the more optimistic package manifest and must not be silently resolved by deletion.

The Event 001–010 cleanup audit identifies seven specialized non-armored zombie packages as incomplete and explicitly says to preserve their provider and counter evidence (`docs/plans/repo_cleanup/subagent_handoffs/events_001_010_cleanup_audit_2026-08-22.md:30`, `:146-152`).

Live runtime consumers exist for the promoted model packages under `gfx/models/units/chaosx_demonic_zombies/` and `gfx/models/units/chaosx_infected_zombies/`, with the existing unit/entity path and counter registration owned by `interface/chaosx_subuniticons.gfx`; the seven pending counter destinations are only proposed in `models_3d/gfx_handoff.md`.

### `006_independence_wave` — `retain_blocked_or_uncertain`

The root manifest records final and handed-off icon families but explicitly says the asset manifest does not promote a package and that source-placeholder work does not clear rights, package, attestation, runtime, or reachability gates.

The current Event 006 cleanup audit classifies the event `HOLD/PARTIAL` across package admission, portraits/rights, probability, focus, runtime, super-event audio rights, and GUI evidence (`docs/plans/repo_cleanup/subagent_handoffs/events_001_010_cleanup_audit_2026-08-22.md:34`, `:154-158`).

The 608 modified tracked files and 4,062 ignored files show active/recent work, including source-placeholder, animation, formable, flag, portrait, and GUI evidence packages.

Live consumers include `gfx/interface/goals/006_independence_wave/`, `gfx/interface/ideas/006_independence_wave/`, `gfx/interface/decisions/006_independence_wave/`, `gfx/achievements/`, `interface/006_independence_wave.gfx`, the Event 006 focus/decision/event surfaces, and the shared scripted-GUI ledger; the workspace remains evidence for many of those consumers.

### `006_independence_wave_california_civic_source_clearance` — `retain_blocked_or_uncertain`

The source-clearance result is `PASS`, but both `manifest.md:3,91-99` and `gfx_handoff.md:1-3,17-21` state that runtime promotion was intentionally withheld, no final DDS exists, no `.gfx` edit is authorized, and the package is `not_promoted` / `pending_full_portrait_pipeline`.

The durable plan handoff confirms the candidate is source-only and instructs the parent to preserve it until source-locked processing, independent review, DDS conversion, and runtime wiring are separately completed (`docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw184_california_civic_source_clearance_2026_07_24.md:1-3,26-44`).

There is no live `gfx`, `interface`, `common`, `events`, `sound`, or `localisation` consumer for this package; that absence is not deletion approval because the source and rights evidence are still the pending input to a future portrait pipeline.

### `012_africa` — `retain_blocked_or_uncertain`

This broad event workspace has no root manifest and contains 865 modified tracked files plus 1,652 ignored files, so there is no single completed/approved package boundary that would make whole-directory deletion safe.

The Event 012 asset reconciliation records a release-candidate matrix with 84 installed-runtime rows, 28 installed-dormant rows, 117 deferred controlled-pool rows, and 10 deferred runtime-gated rows, while explicitly preserving the animation, Tier A, portrait, strange-force, and model packages as current evidence (`docs/plans/012_africa_plans/subagent_handoffs/012_africa_asset_matrix_runtime_reconciliation_2026-08-09.md:5-7,58-74`).

Live consumers include `interface/012_africa_animations.gfx`, `common/scripted_guis/012_africa_charter_scripted_gui.txt`, `common/decisions/012_africa_decisions.txt`, Event 012 focus/decision/event surfaces, and runtime DDS roots under `gfx/interface/012_africa/`; the workspace contains source frames, manifests, and review artifacts for those consumers.

### `012_africa_priority_portraits_real_sources` — `retain_blocked_or_uncertain`

The sole `manifest.md` is a source-of-truth portrait evidence ledger whose rows include `blocked_ownership`, `blocked_source_gap`, `needs_user_review_rights`, `needs_user_review_identity`, `source_ready_repaint_pending_audit`, and `source_ready_actor_gate_pending`; it explicitly says a row is not runtime-complete until source-locked repaint and independent audit are recorded.

The associated handoff says only four reviewed replacements were installed and that twelve remaining held rows retain the existing dormant treatment until source, rights, identity, and actor gates are cleared (`docs/plans/012_africa_plans/subagent_handoffs/012_africa_real_sourced_portrait_runtime_2026-08-02.md:42-46`).

The four promoted runtime consumers are `common/characters/012_africa_priority_member_characters.txt` and `interface/012_africa_priority_member_characters.gfx`, with runtime DDS under `gfx/leaders/012_africa/priority_members/`; unresolved rows have no approved consumer. The evidence workspace cannot be deleted while those source and blocked-row decisions remain active.

### `012_africa_tiera_visual_packages` — `retain_blocked_or_uncertain`

`manifest.json` reports `status: complete_and_wired` and `no_unwired_assets: true`, but it also records five retained generated masters as `generated_imagegen_partial` because original prompt metadata is unavailable and normalized acceptance prompts were substituted as evidence.

The durable handoff confirms the six flag/emblem packages are installed, but it points back to the workspace for source hashes, evidence contact sheets, and the retained-source uncertainty (`docs/plans/012_africa_plans/subagent_handoffs/012_africa_tiera_visuals_final_2026-08-09.md:5,17-41`). The package also has 63 current tracked modifications, so it is not an inactive archive.

Live consumers include `common/countries/012_africa_cosmetic.txt`, `interface/012_africa_tier_a_identity_icons.gfx`, `common/ideas/012_africa_promoted_tiera_ideas.txt`, `gfx/flags/`, and `gfx/interface/012_africa/tier_a/emblems/`. Deletion would discard unresolved provenance and active review evidence even though final runtime files exist.

### `012_africa_world_order` — `retain_blocked_or_uncertain`

The world-order handoff records 121 focus icons and 38 idea icons under runtime roots, but the six fictional leader packages are explicitly `deferred_model_required` and `deferred_runtime_gated`, and the historical source-evidence rows retain blocked/needs-review states.

The handoff also says the source atlases, source tiles, processed PNGs, comparison sheets, and portrait evidence remain in the workspace, with runtime country-leader roles and model/entity production deferred (`docs/assets/012_africa_world_order/gfx_handoff.md:30-76`). The directory has 397 modified tracked paths and a newest file on 2026-08-21.

Live consumers include `gfx/interface/goals/012_africa/world_order/`, `gfx/interface/ideas/012_africa/world_order/`, `interface/012_africa_leaders_fictional.gfx`, dormant `common/characters/012_africa_fictional_characters.txt`, and Event 012 world-order focus roots. The deferred model/runtime gates and retained source provenance rule out deletion.

### `012_africa_world_order_flags` — `retain_blocked_or_uncertain`

The manifest and package handoff mark all 39 cosmetic flag ladders and 117 TGAs `complete`, but the handoff explicitly leaves the final runtime audit and the decision to promote permanent provenance to the parent after Event 012 acceptance (`docs/plans/012_africa_plans/subagent_handoffs/012_world_order_flag_assets_handoff.md:1-5,59`).

The directory has 157 modified tracked paths and current source/processed/contact-sheet evidence; it is therefore recent and not a completed, promoted temporary workspace.

The live consumer is the existing `common/countries/012_africa_world_order_cosmetic.txt` identity set resolved through `gfx/flags/<TAG>.tga`, `gfx/flags/medium/<TAG>.tga`, and `gfx/flags/small/<TAG>.tga`; no `.gfx` registration is required. The absence of a `.gfx` consumer does not remove the unresolved promotion and acceptance dependency.

### `016_brilliant_scientist` — `retain_blocked_or_uncertain`

The root manifest describes a largely wired core runtime, but its open-gates section retains a queued CBRN stockpile design, a rejected/blocked Alien Infantry 3D package, unresolved durable portrait-source queue ownership, and unresolved external redistribution rights (`docs/assets/016_brilliant_scientist/manifest.md:166-173`).

The Event 011–020 cleanup audit calls Event 016 explicitly partial and says targeted transfer, cleanup, probability, balance, Event 019 isolation, and presentation validation remain open (`docs/plans/repo_cleanup/subagent_handoffs/events_011_020_cleanup_audit_2026-08-22.md:52`).

Live consumers span `gfx/leaders/KRG/`, `gfx/event_pictures/016_brilliant_scientist/`, `gfx/interface/016_brilliant_scientist/`, `gfx/flags/`, `sound/016_brilliant_scientist/`, and the corresponding Event 016 `interface`, `common`, and event files. The workspace contains ignored model and evidence trees and cannot be deleted while these blockers and rights facts remain unresolved.

### `016_brilliant_scientist_dhrondan_event_art` — `retain_active_recent`

The manifest marks the generated non-portrait flags, report/news scenes, faction emblem, and country panel complete, but the separate special-project icon and achievement triplet remain blocked under `chaosx_icon_artist`.

The dated handoff explicitly says parent `.gfx` registration is still required and instructs the team to keep `docs/assets/016_brilliant_scientist_dhrondan_event_art/` while Event 016 remains active and under review, promoting durable facts before cleanup (`docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_dhrondan_flags_event_art_handoff_2026-08-21.md:1-16,62-69`).

Proposed/runtime destinations include `gfx/flags/DHR*`, `gfx/event_pictures/016_brilliant_scientist/`, and `gfx/interface/016_brilliant_scientist/`, but this package has no completed parent `.gfx` wiring authority yet. Its newest evidence is 2026-08-21 and the blocked icon surfaces make deletion unsafe.

### `020_black_plague` — `retain_blocked_or_uncertain`

The root asset manifest says `complete` and records several wired decisions, focus, crisis-seal, terminal-readiness, report, and news assets, but one terminal-readiness panel is explicitly reserved for a future scripted-GUI panel and the broader Event 020 completion audit remains partial.

The Event 011–020 cleanup audit lists open Event 020 sound-definition wiring, counter review, model/audio acceptance, broader presentation, attribution, balance, live/runtime validation, and missing portrait-worker handoff (`docs/plans/repo_cleanup/subagent_handoffs/events_011_020_cleanup_audit_2026-08-22.md:56,220-224`). The workspace has 44 modified tracked paths.

Live consumers include `interface/020_black_plague_response.gfx`, `interface/020_black_plague_rat_identity.gfx`, `interface/020_black_plague_event_pictures.gfx`, `gfx/interface/goals/020_black_plague/`, `gfx/interface/animated/020_black_plague/`, and Event 020 focus/decision/scripted-GUI/event consumers. Keep the evidence until the partial completion and attribution gates are resolved.

### `chaos_warfare_cbrn` — `retain_blocked_or_uncertain`

This is a request/backlog workspace, not a completed asset package. `cbrn_unit_texticon_requests.md` states that all CBRN texticons currently use placeholder aliases in `interface/chaosx_texticons.gfx` and lists distinct future pictograms that should replace them.

There is no final bespoke CBRN texticon manifest, source-to-runtime package, independent review, or accepted handoff in this directory. Its only live relationship is the placeholder alias set in `interface/chaosx_texticons.gfx:426`; deletion would erase the request and replacement contract.

### `chaos_warfare_system` — `retain_blocked_or_uncertain`

This shared workspace contains multiple stage packages with mixed dispositions, including complete-and-wired stages, user-review counter packages, `needs_user_review` unit/model packages, and runtime candidates pending user-owned live HOI4 validation.

Examples include `models_3d/chaos_assault_battalion/manifest.md` and `runtime/handoff.md` marked `needs_user_review`, `stage_10_cbrn_counter_icons/v3_counters/manifest.md` marked `needs_user_review`, and facility/model manifests that are complete only through export/reimport proof with live validation outstanding. It has 131 modified tracked paths and 2,371 ignored files.

Live consumers are distributed across shared CBRN surfaces, including `common/buildings/chaosx_buildings.txt`, `common/units/cbrn_regimental_support.txt`, `interface/cbrn_protection.gfx`, `interface/cbrn_designers.gfx`, `interface/chaosx_subuniticons.gfx`, `sound/chaos_warfare/`, and stage-specific runtime DDS roots. The mixed acceptance states and shared-system ownership make whole-directory deletion unsafe.

### `chaos_warfare_system_audit` — `already_absent`

The directory has only four empty physical subdirectories (`contact_sheets`, `processed_png`, `prompts`, and `source_png`). It contains no files, no manifest, no handoff, no Git paths, and no runtime references, so there is no content to delete or promote.

### `country_flags` — `retain_active_recent`

The nested `cxt_test_country` package is marked `complete` for its source, processed preview, review DDS, and three runtime TGAs, but its handoff explicitly says no in-game validation is claimed and the package was generated/reviewed on 2026-08-21.

Its live runtime surface is `gfx/flags/CXT.tga`, `gfx/flags/medium/CXT.tga`, and `gfx/flags/small/CXT.tga`, consumed by the `CXT` country registered in `common/country_tags/chaosx_test_country.txt` and its country definition. Recent test-country work and the uncompleted runtime validation gate require retention.

### `portraits` — `retain_portrait_archive`

This is the durable portrait archive required by the asset skill, not a deletable temporary event workspace. It contains source/crop/processed/provenance packages for Events 002, 005, 006, 010, 012, 014, 016, 020, 038, and scientist/shared portrait work.

The archive has 279 modified tracked paths and 379 ignored files, but its dirty state does not weaken the mandatory retention rule. Runtime GFX and character files consume copied DDS files under engine-facing `gfx/leaders/` or `gfx/interface/` paths, never paths inside `docs/assets/portraits/`.

### `shared_clone_system` — `retain_blocked_or_uncertain`

The clone manifest is `needs_user_review` and says runtime registration is parent-owned while the locked adapter cannot attach/reorient the rifle or prove attack, support-attack, and training contact alignment.

`models_3d/clone_infantry/evidence/recovery_rifle_attachment_adapter_blocker.md` is explicitly `blocked_by_locked_adapter_capability`, and `runtime/handoff.md` says the body is parent-integrated while combined rifle acceptance remains blocked. The package has no tracked files but 1,039 ignored files, so Git visibility is not deletion evidence.

Live consumers include the parent clone unit/entity path, `clone_infantry_mesh`, `clone_infantry_entity`, and the parent-owned `.gfx`, `.asset`, equipment, sound, and formation consumers; accepted roles are limited while rifle-dependent actions remain pending. Preserve all recovery and rejection evidence.

### `shared_portal_raider_system` — `retain_blocked_or_uncertain`

The model manifest says `blocked; rejected Meshy geometry preserved; no runtime model outputs`, and the runtime handoff says the generated task omitted the required ray rifle, with no final mesh, animation, PDX textures, export, or reimport proof.

The crosswalk marks the model, rig, all ten actions, export, and runtime binding blocked/not synchronized. The counter handoff is only a parent-owned proposal; the package must not be deleted because it preserves the rejected geometry, sourced audio candidates, and failure/recovery evidence.

There is no live portal-raider model/entity consumer. Proposed counter destinations are `gfx/interface/counters/divisions_large/unit_portal_raider_icon.dds` and `gfx/interface/counters/divisions_small/onmap_unit_portal_raider_icon.dds`, but the handoff says no `.gfx` file was edited and no final art was produced.

### `shared_robot_system` — `retain_active_recent`

The robot manifest says production-complete and runtime-wired, but live consumer and combat presentation validation remain user-owned, and the newest evidence is 2026-08-20.

The permanent runtime handoff records the installed mesh, entity, eight actions, textures, counters, technology/equipment icons, five positional action-sound consumers, and the unconsumed selection cue caused by the lack of a provider-neutral per-subunit callback (`docs/assets/shared_robot_system/models_3d/autonomous_robot/runtime/handoff.md:14-18`).

Live consumers span `gfx/models/units/autonomous_robot/`, the robot entity and unit definitions, interface counters/icons, technology/equipment surfaces, and `sound` action consumers. Keep the recent package until user-owned live validation and the registered-but-unconsumed selection-cue disposition are closed.

### `system_camp_repression_rework` — `retain_blocked_or_uncertain`

The asset manifest marks the two visible emblems wired, and the system completion tracker says the static Ledger presentation is complete, but the durable plan still records optional Ledger animation as queued and the plan/spec surfaces continue to rely on source and prompt paths under this workspace.

The current completion report promotes coverage and live consumers but still records the engine-runtime scenario execution gap (`docs/plans/system_camp_repression_rework_plans/completion_report.md:84-92,128-134`). Exact source, prompt, processed, and review evidence has not been consolidated out of `docs/assets/system_camp_repression_rework/`, so whole-directory deletion would break reproducibility.

Live consumers include `interface/camp_repression_rework.gfx`, `common/decisions/categories/camp_repression_rework_categories.txt`, the generic site-inspection decision, and the shared Repression Ledger GUI/scripted-GUI system. The workspace is ignored rather than tracked, but it remains active evidence and must be retained.

## Event 005 runtime portrait-copy finding is a separate `gfx` candidate

The Event 001–010 cleanup audit identifies exactly four installed-but-unreferenced Event 005 runtime portrait DDS files:

- `gfx/leaders/005_soviet_collapse/LID_leader.dds`
- `gfx/leaders/005_soviet_collapse/RCD_leader.dds`
- `gfx/leaders/005_soviet_collapse/RLD_leader.dds`
- `gfx/leaders/005_soviet_collapse/TRS_leader.dds`

The audit says exact filename/tag searches found no current consumer, while the user-supplied source archive and checksums under `docs/assets/portraits/005_soviet_collapse/user_supplied_runtime_2026-08-21/` must be preserved (`docs/plans/repo_cleanup/subagent_handoffs/events_001_010_cleanup_audit_2026-08-22.md:69-80`).

This is a separate engine-facing `gfx` cleanup candidate and is not evidence for deleting any `docs/assets/` directory. `docs/assets/portraits/` remains `retain_portrait_archive`.

## MCP evidence boundary

This follow-up was a docs/assets retention audit and did not invoke a new event, focus, GUI, map, technology, or probability route; no source runtime surface was edited.

The existing bounded audits retain the following read-only artifacts that support the recorded incomplete/blocked states but do not authorize deletion:

- Event 005 event trace: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1ac8d48eb4e76c52c97fa4631468860c5f215964815296fc372b92b41b6f7922/4b965f2e5401f4fa4b2182f89d87e02d674fa4a9578e933a4d21119b4da21f1a/event-trace-bc0062fc8506.json`.
- Event 016 evolution probability inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d3e25351e895f681d6a208920bc62f4a74ef3c05dfd7900c13fe7da06fec03b2/ab5717220786646b49f121daf60c12226b973e2791ff02f56c72517d1cc33797/probability-inspect-991079c10600.json`.
- Event 020 complete two-option probability inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9c287c5002b964c0072f23b1d010e246b0202459808514e3b3c21a5e97ad7b7f/4a0d107d906c692ceff25b22d30176be50d5b293e707b43d42bbd8a55893cf12/probability-inspect-a04ba2efd8da.json`.
- Event 020 weaponization inspection with one unresolved dynamic construct: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cbc8056b63aa5d04954ffb5abf0594b889361a82a822cde0b89007d9d8cb1f53/213f139e1be100659d08fa6618db31f7b72eb0d52b64733a32a45cc309f4de1e/probability-inspect-362254a8e39a.json`.

The Events 011–020 audit records root event inspect/render timeouts and incomplete probability pools, and the Events 001–010 audit records partial event traces and unavailable fresh focus/render evidence. Those limitations reinforce retention and are not engine proof that any asset workspace is dead.

## Worktree collision and dynamic-reference risks

- The 16,774 ignored files are not represented by ordinary `git status`; any future cleanup must inventory ignored paths before proposing deletion or moving a workspace.
- The large Event 006, Event 012, Event 016, Event 020, and shared warfare workspaces have active tracked modifications from other work, so deleting a top-level directory would destroy unrelated in-progress evidence.
- A manifest that says `complete` is insufficient where a handoff says `parent wiring pending`, `needs_user_review`, `runtime not promoted`, `deferred_runtime_gated`, or `blocked`.
- Dynamic engine consumers can be constructed through character definitions, cosmetic tags, shared registries, scripted localisation, meta effects, event targets, and generated runtime basenames; source-only filename counts are not sufficient proof of deadness.
- The four comment-only `docs/assets` matches in runtime-facing files are documentation references, not runtime paths, but they confirm that source evidence is still expected by maintainers.
- Existing Event 012 and Event 016 handoffs explicitly preserve dormant/deferred packages; dormant is not the same as stale.
- The Event 002 specialized package contains contradictory optimistic and blocking status files; keep both until an owner reconciles the status.

## Recommended next action

Do not delete any top-level `docs/assets/` directory in this cleanup tranche.

If deletion is revisited, require an owner-approved per-workspace closure record that names the promoted durable provenance/crosswalk/handoff paths, proves no unresolved asset or rights gate remains, confirms no recent or active work, and records a final runtime consumer scan. Handle the four Event 005 DDS copies separately under the `gfx` cleanup owner, preserving the portrait archive.
