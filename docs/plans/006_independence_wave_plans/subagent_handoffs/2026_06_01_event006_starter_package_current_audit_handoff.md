# Event 006 Starter Package Current Audit Handoff

Date: 2026-06-01

## Scope

Audited the currently implemented Event 006 starter country-package surfaces for:

- `OGB` Volga / Old Great Bulgaria
- `ASY` Assyria
- `DNZ` Danzig
- `UGA` Buganda carrier
- `SOK` Sokoto
- `GAR` Guarani
- `CHR` Charrua
- `KUR` Kurdistan Mountain Assembly
- Railway / Timetable Authority package

Audit stayed inside Event 006 surfaces and did not edit Event 005 files, create tags, create flag artwork, or add new package families.

## Files Changed

- `common/decisions/006_independence_wave_decisions.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `docs/events/006_independence_wave.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_01_event006_starter_package_current_audit_handoff.md`

## Changed Identifiers

- `independence_wave_integrate_charrua_assembly`
- `independence_wave_integrate_kurdish_mountain_assembly`
- `can_independence_wave_show_first_impossible_state_super_event`
- `can_independence_wave_show_first_old_name_super_event`
- `independence_wave_update_achievement_tracking`
- `soviet_collapse_breakaway` guard references
- `independence_wave_package_kurdistan`
- `GFX_idea_independence_wave_kurdish_mountain_assembly` documentation entry

## Patch Summary

- Fixed Charrua/Kurdistan integration mission timeout wiring. Charrua now uses `@independence_wave_charrua_integration_days`; Kurdistan now uses `@independence_wave_kurdish_integration_days`.
- Replaced stale Event 005 guard references to nonexistent `soviet_collapse_breakaway_state` with the implemented Event 005 flag `soviet_collapse_breakaway` in Event 006 collision checks.
- Added `independence_wave_package_kurdistan` to the local-polity package achievement marker path so Kurdistan is tracked with Buganda, Guarani, and Charrua.
- Added the already-produced Kurdish Mountain Assembly idea sprite name to the Event 006 icon ledger in `docs/events/006_independence_wave.md`. The intended DDS asset already exists at `gfx/interface/ideas/independence_wave/idea_independence_wave_kurdish_mountain_assembly.dds`.

## Before And After

- Before: `independence_wave_integrate_charrua_assembly` and `independence_wave_integrate_kurdish_mountain_assembly` each referenced the other package's timeout constant.
- After: each mission references its own package timeout constant.
- Before: first-old-name and first-impossible-state paths had stale `soviet_collapse_breakaway_state` guards that did not match the actual Event 005 flag surface.
- After: the guards use `soviet_collapse_breakaway`, matching Event 005 usage and the main `is_independence_wave_release` trigger.
- Before: KUR received the package flag and local-polity overlay, but was not included in the `chaosx_iw_local_polity_package` achievement/package marker update.
- After: KUR is included in the same local-polity marker path as UGA, GAR, and CHR.

## Country Package Coverage Checklist

- `OGB`: registered in Chaos Redux tag files, has repo country/history/localisation/flags, Event 006 package flags and variables, Volga reduced-release anchors `249` and `256`, Event 006-only decisions/focus overlay, and explicit Event 005 separation.
- `ASY`: vanilla tag/country/history/characters/localisation/flags; Event 006 package marker `independence_wave_package_assyria`; Mosul state `676` control requirements; decisions, focus unlocks, idea, AI strategy, and event-log hooks present.
- `DNZ`: vanilla tag/country/history/localisation/base flags; Event 006 package marker `independence_wave_package_danzig_free_city`; Danzig state `85` control requirements; decisions, focus unlocks, idea, AI strategy, and event-log hooks present.
- `UGA`: vanilla tag/country/history/localisation/flags; Event 006 package marker `independence_wave_package_buganda`; Uganda state `548` start and control requirements; decisions, focus unlocks, idea, AI strategy, and event-log hooks present.
- `SOK`: vanilla tag/country/history/localisation/flags; Event 006 package marker `independence_wave_package_sokoto`; Sokoto state `902` start/control; Borno `901` and Niger `781` temporarily masked during release and restored as claim/proof targets; decisions, focus unlocks, idea, AI strategy, and event-log hooks present.
- `GAR`: vanilla tag/country/history/localisation/flags; Event 006 package marker `independence_wave_package_guarani`; reduced anchors `510`, `502`, `688`; seeded core set includes `301`, `688`, `957`, `510`, `504`, `944`, `503`, `502`; decisions, focus unlocks, idea, AI strategy, and event-log hooks present.
- `CHR`: vanilla tag/country/history/localisation/flags; Event 006 package marker `independence_wave_package_charrua`; anchors/control seats `945` and `946`; seeded core set includes `300`, `945`, `946`; decisions, focus unlocks, idea, AI strategy, and event-log hooks present.
- `KUR`: vanilla tag/country/history/characters/localisation/flags; Event 006 package marker `independence_wave_package_kurdistan`; mountain control states `350`, `352`, `800`, `421`, `676`; decisions, focus unlocks, idea, AI strategy, and event-log hooks present after marker patch.
- Railway / Timetable Authority: generic railway package marker uses `independence_wave_package_railway_candidate` plus `independence_wave_package_type = railway_package`; focus and decision path requires owned controlled high-infrastructure state, junction committee, bridge guard, independence, legitimacy, and militia strength.

## File Surface Checklist

- `docs/events/006_independence_wave.md`: package documentation and icon ledger checked; Kurdish idea sprite ledger entry added.
- `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md`: origin-separation rules and starter-package scope checked; no edit made.
- `common/script_constants/006_independence_wave_constants.txt`: package constants and integration days referenced by decisions checked; no edit made.
- `common/scripted_effects/006_independence_wave_effects.txt`: package setup, achievement markers, claims, event-log recording, and Event 005 collision checks audited; KUR local-polity marker and stale guard patched.
- `common/scripted_triggers/006_independence_wave_triggers.txt`: package gates, state-control requirements, railway hub control, and Event 005 collision checks audited; stale guards patched.
- `common/decisions/006_independence_wave_decisions.txt`: package decisions and timed integration missions audited; Charrua/Kurdistan timeout constants patched.
- `common/national_focus/006_independence_wave_focus.txt`: provisional tree loading and package overlays checked; no edit made.
- `common/ideas/006_independence_wave_ideas.txt`: package ideas checked; current file points KUR at `independence_wave_kurdish_mountain_assembly`.
- `common/ai_strategy/006_independence_wave.txt`: package AI markers checked for historical, city/port, local-polity, and strange package posture; no edit made.
- `common/scripted_localisation/006_independence_wave_scripted_localisation.txt`: package label resolver checked; no edit made.
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`: event-log package type surfacing checked at current scope; no edit made.
- `interface/006_independence_wave_icons.gfx`: package icon references checked; current file registers `GFX_idea_independence_wave_kurdish_mountain_assembly`.
- `localisation/english/006_independence_wave_l_english.yml`: package decision, focus, idea, and tooltip keys checked; no edit made.

## Missing Or Stale Country Package Surfaces

- No broken decision/focus/idea/localisation/GFX references were found in the focused starter-package surface after the patch.
- No Event 006 code path was found loading an Event 005 OGB focus tree or Event 005 OGB helper.
- KUR currently relies on vanilla country history and characters plus Event 006 overlay mechanics; no bespoke Event 006 leader or party package exists. This is acceptable for the bounded starter overlay, but should remain a later identity-depth item if Kurdistan becomes a full package.
- Railway packages are still generic rather than tag-specific; current Timetable Authority linkage is enough for the starter package but not a full railway country family.

## Map And State Setup Issues

- No immediate host-survival or state-scope bug found in the Timetable Authority path. The gate uses `any_owned_state = { is_controlled_by = ROOT infrastructure > constant:independence_wave_startup.railway_infrastructure_gate }`, so it requires an owned, controlled rail hub before junction/authority decisions can succeed.
- OGB, SOK, GAR, CHR, and KUR reduced-release anchors are explicitly state-scoped. ASY, DNZ, and KUR also have vanilla cores in their target states, so the generic candidate pool can surface them when inactive and safe.
- SOK temporary core masking on `901` and `781` is restored through `independence_wave_restore_temporary_package_cores`; no stale masked-core path found in the audited surface.

## Politics, Leader, Portrait, Flag, Advisor, And Party Issues

- No new flag artwork is introduced by the current Event 006 package code.
- Flag coverage found:
  - `OGB`: repo base and ideology flags in large/medium/small.
  - `ASY`, `UGA`, `SOK`, `GAR`, `CHR`: vanilla ideology flags in large/medium/small.
  - `DNZ`: vanilla base Danzig flags in large/medium/small.
  - `KUR`: vanilla base/ideology/cosmetic flags in large/medium/small.
- No flag asset subagent follow-up is required from this audit.
- No generated one-person leader/portrait gender-pool issue found in the audited Event 006 starter surfaces. Most listed packages rely on vanilla leaders or institutional overlays.

## Focus, Decision, Idea, And Asset Issues

- Fixed two package mission timeout mismatches in the decision surface.
- Confirmed package decisions have matching localisation keys, scripted triggers/effects, and registered GFX icons in the audited starter package set.
- Confirmed package focus overlays unlock matching package decisions and use registered focus icons.
- Confirmed the Kurdish Mountain Assembly idea DDS exists and the current `.gfx`/idea references are wired to `GFX_idea_independence_wave_kurdish_mountain_assembly` / `picture = independence_wave_kurdish_mountain_assembly`.

## Starting Military, Technology, Industry, Supply, And Production Issues

- Event 006 released-country setup applies shared startup manpower/equipment and loads the provisional focus tree after setting `chaosx_release_origin_independence_wave`.
- Listed vanilla tags retain vanilla history technology/characters where applicable.
- No large military, industry, or balance expansion was made. This pass did not audit all vanilla OOB quality beyond verifying the package paths do not introduce an obvious broken Event 006 reference.

## AI And Playability Issues

- AI strategy overlays exist for Event 006 releases and package families.
- KUR local-polity tracking was missing from the achievement/package marker update and is now patched.
- Starter packages are playable as overlays through the shared provisional tree and package decisions. They are not full bespoke country packages; deeper trees, advisors, bespoke party packages, and route-specific leaders remain outside this bounded pass.

## Validation Run

- Brace balance on `common/decisions/006_independence_wave_decisions.txt`, `common/scripted_effects/006_independence_wave_effects.txt`, `common/scripted_triggers/006_independence_wave_triggers.txt`, `interface/006_independence_wave_icons.gfx`, and `localisation/english/006_independence_wave_l_english.yml`: all `brace_balance=0`.
- Trailing whitespace on the same files: none found.
- `rg -n '<=|>='` on touched Event 006 script files: no matches.
- BOM check for `localisation/english/006_independence_wave_l_english.yml`: `ef bb bf`.
- Localisation `:0` key check for `localisation/english/006_independence_wave_l_english.yml`: no matches.
- Focused Event 005 leakage search found only documented separation text and explicit negative guards in Event 006 code; no `soviet_collapse_breakaway_state` references remain in the audited Event 006 surfaces.
- Mechanical reference checks:
  - Used package decision/focus icons minus registered `interface/006_independence_wave_icons.gfx` sprites: no missing entries.
  - Used package idea pictures minus registered idea sprites: no missing entries.
  - Package decision/focus tooltip keys minus `006_independence_wave_l_english.yml`: no missing entries.

## Skipped Validation

- No in-game launch validation was run.
- No full HOI4 parser validation was run.
- No commit was created from this subagent pass because the repository already contains a large pre-existing dirty worktree with many untracked Event 006 gameplay/assets files and unrelated Event 005 modifications; staging these untracked package files would risk committing prior work outside this narrow audit.

## Remaining Package Gaps

- Starter packages are coherent overlays, not full country-package completions. Further identity work should be a parent-level design task or improvement-loop addendum, not a small audit patch.
- Railway/Timetable Authority needs deeper tag-specific route design and final railway-family identity before it can be treated as a complete country family.
- KUR uses vanilla leaders/history and a local-polity overlay; deeper Kurdistan-specific party, advisor, and route identity remain follow-up scope if desired.
- No flag follow-up is needed from this pass.
