# Event 032 SCN-015 Triggerable Scenario Registry Handoff

Disposition: implemented and superseded by the parent core integration pass. The source-absence statements in the original handoff describe the 2026-08-30 snapshot and are retained only as historical evidence; current Event 032 core files, atomic setup/cleanup, and workbook/export alignment are authoritative in the current worktree and test ledger.

Date: 2026-08-30

## Scope

This bounded handoff covers only the shared Triggerable Scenarios registry surface for Event 032 SCN-015, Missile Age. It does not edit `events/032_missile_crisis.txt`, Event 032 core effects or triggers, decisions, achievements, spreadsheets, generated CSV files, or unrelated settings.

## Files changed by this handoff

- `common/script_constants/032_missiles_scenario_constants.txt`
- `common/scripted_triggers/032_missiles_scenario_triggers.txt`
- `common/scripted_effects/032_missiles_scenario_effects.txt`
- `common/script_constants/chaosx_triggerable_scenarios_constants.txt`
- `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt`
- `common/scripted_triggers/chaosx_triggerable_scenarios_triggers.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt`
- `localisation/english/032_missile_crisis_l_english.yml`
- `docs/systems/event_system/triggerable_scenarios.md`
- `docs/events/032_missiles/systems/triggerable_scenario.md`
- `docs/specs/032_missiles_specs/032_missiles_test_matrix.md`

## Implemented surface

SCN-015 is registered as raw ID `15` with name sort value `5.625`. The shared window now initializes and cycles five Event 032 profiles: Global Proliferation, Saturation War, Command Breakdown, Special Payload Crisis, and Retaliation Network. All four shared intensity values are handled by Event 032 package scale constants.

The four list-sort views, row name, `#015` entry label, profile descriptions, intensity impacts, eligibility bridge, confirmation dispatch, setup receipt, duplicate guard, bounded package flags, and cleanup are wired. The dispatcher calls `missiles_scenario_launch_unregistered`. No Event 032 GUI, world-end branch, recurring world scan, or terminal flag was added.

The setup wrapper freezes profile and intensity runtime values, calls the documented Event 032 core program and technology adapters once per valid recipient, marks only the selected profile tracks, and clears country/global bypass flags. Country setup is guarded by `missiles_scenario_country_setup_complete`; the global launch receipt is guarded by `missiles_scenario_launched`; package failure is surfaced through `missiles_scenario_setup_failed` without a false successful launch marker.

Special Payload Crisis uses the Event 032-owned `missiles_special_payload_supported` country flag as the existing technology-and-stockpile proof and never grants payloads. Saturation War requires a valid war between valid recipients. Retaliation Network requires two valid recipients and marks only High and Maximum for bounded warning pressure.

## Collision evidence

The shared triggerable registry contains Fallout at raw ID `14`, Missile Age at raw ID `15`, and an existing Global Jihad row at raw ID `16` in this worktree. Event 031's current untracked constants already use `triggerable_scenario_id = 16` for that Global Jihad row; its `world_end_scenario_id = 15` belongs to the separate world-end registry namespace and was not overwritten. Fallout remains unchanged at `14`.

The current Event 031 constants file is user-owned untracked work and was deliberately not staged by this bounded worker. Its observed triggerable selector is already past the stale private `15` reservation and does not collide with SCN-015.

## Validation

- Consulted the required Chaos Redux event skill, offline Paradox wiki core pages, and vanilla script-constant/effect/trigger documentation before editing.
- Confirmed every Event32 localization key introduced by this surface exists in the Event32 UTF-8 BOM localization file.
- Counted braces in all new and touched Clausewitz script surfaces; each file is balanced.
- Audited the shared registry, four sort branches, selector, type cycling, dispatcher, eligibility trigger, and scripted-localisation references for raw ID `15`.
- Confirmed the new effect contains one bounded launch-time `every_country` pass plus one cleanup pass and no on-action world scan.
- Did not launch Hearts of Iron IV or claim live save/game evidence.
- An isolated `chaosx_event_completion_auditor` was requested with `fork_context=false`, but it did not return within the bounded wait window and was closed without edits.

## Blockers and handoff boundary

The original snapshot lacked `common/scripted_effects/032_missiles_effects.txt` and `common/scripted_triggers/032_missiles_triggers.txt`. The parent has since supplied the core APIs, atomic mutation, result/failure reporting, evolution implementation, site/reserve mutation, and bounded launch-time setup; the current implementation and remaining MCP/live-consumer limits are recorded in the test ledger.

No spreadsheet or generated CSV update was made because it was explicitly outside this worker's scope.

Git staging and commit were blocked by the pre-existing `.git/index.lock` from 2026-08-29T23:32:17+03:00. No Git process was visible, but the lock was left untouched to protect the user's existing index and staged work.
