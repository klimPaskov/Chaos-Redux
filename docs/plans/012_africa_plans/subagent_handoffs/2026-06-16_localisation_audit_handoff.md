# Event 012 Africa Localisation Audit Handoff

Scope: Event 012 localisation and scripted localisation audit with narrow patch authority.

## Files Changed

- `localisation/english/012_african_union_l_english.yml`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-16_localisation_audit_handoff.md`

I did not edit:

- `localisation/english/chaosx_countries_l_english.yml`
- `localisation/english/chaosx_achievements_l_english.yml`
- `localisation/english/chaosx_event_names_l_english.yml`
- `common/scripted_localisation/012_africa_scripted_localisation.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`

Other Event 013/Natural Disaster changes in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` were ignored.

## Changed Keys

- Added `africa_is_one_focus_tree`
- Added `africa_is_one_focus_tree_desc`
- Updated `africa_high_chaos_bestiary_spirit_desc`
- Updated `africa_high_chaos_actor_spirit_desc`
- Updated `chaosx.events_log.window.evolution_details.africa.body.stage_4`
- Updated `AFR_high_chaos_door_desc`
- Updated `africa_unlock_bestiary_package_desc`

## Before And After

- Before: `africa_is_one_focus_tree_desc` was missing, leaving the focus-tree ID without complete player-facing localisation for load-focus-tree/tooltips.
- After: `africa_is_one_focus_tree` and `_desc` localise the focus tree as `Africa Is One` / `The Charter League focus tree.`
- Before: several high-chaos descriptions used the meta phrase `explicit fictional`, which reads like implementation/safety language in player-facing UI.
- After: those lines use in-world wording: `impossible nonhuman` and `supernatural`.

## Missing Key List

- Initial audit found `africa_is_one_focus_tree_desc` missing from the scoped localisation files.
- After patch: no missing Event 012 keys were found among event, focus, decision, idea, scripted-localisation, achievement, country, and event-name references covered by this audit.

## Duplicate Key List

- No duplicate keys found across:
  - `localisation/english/012_african_union_l_english.yml`
  - `localisation/english/chaosx_countries_l_english.yml`
  - `localisation/english/chaosx_achievements_l_english.yml`
  - `localisation/english/chaosx_event_names_l_english.yml`

## Scripted Localisation Issues

- `common/scripted_localisation/012_africa_scripted_localisation.txt` has complete localisation-key coverage for all current `africa_dossier.*` and `africa_high_chaos_package.*` branches.
- Event 012 branches in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` resolve to existing Event 012 event-log title/body/type keys.
- No Event 012 scripted-localisation brace-balance issue was found.

## Dynamic Text Opportunities

- The Authority Atlas and Bestiary counters display static thresholds `/24` and `/6`. These match `minimum_historical_dossiers = 24` and `minimum_high_chaos_packages = 6`, but they can drift if constants change. A future helper could expose threshold variables for dynamic localisation.
- Cost text now presents concrete icon-first values in `012_african_union_l_english.yml`, but those values are still localisation text rather than derived from script constants. If the owning script changes costs, these lines need a paired localisation update or a scripted helper.
- `GetAfricaSelectedDossierName` and `GetAfricaSelectedHighChaosPackageName` are useful dynamic names. Further status helpers could add selected-dossier settlement state, active cap, and package safety/blocked labels.

## Cross-Surface Mismatch Notes

- The high-chaos catalogue has 11 package names, while achievements and category threshold text require 6. This matches the current minimum threshold design and was not patched.
- Country names using `Court`, `Congress`, `Council`, or similar institutional words were left unchanged where current Event 012 specs or high-chaos package plans present them as direct polity concepts, not office placeholders.
- No final Event 012 super-event localisation was found in the scoped files. Existing super-event research handoffs remain research-only; no unsourced final super-event text was added.

## Encoding Concerns

- All scoped `.yml` files checked have UTF-8 BOM:
  - `012_african_union_l_english.yml`
  - `chaosx_countries_l_english.yml`
  - `chaosx_achievements_l_english.yml`
  - `chaosx_event_names_l_english.yml`

## Validation

- Ran Event 012 key-reference coverage over the scoped localisation files plus:
  - `events/012_african_union.txt`
  - `common/national_focus/012_africa_focus.txt`
  - `common/decisions/012_africa_decisions.txt`
  - `common/ideas/012_africa_ideas.txt`
  - `common/scripted_localisation/012_africa_scripted_localisation.txt`
  - Event 012 branches in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- Result after final check: `1814` scoped localisation keys, `352` Event 012 references checked, `0` missing, `0` duplicates.
- Checked brace balance for the two scripted-localisation files in scope; both balanced.
- Checked for remaining `explicit fictional`, update-history wording, `:0`, and leading-space key patterns in scoped files; none remained for the Event 012 audited text after patch.

## Skipped Validation

- No in-game validation was run.
- No broad all-mod localisation scan was run because the task was bounded to Event 012 scope and named files.
- No super-event quote/source validation was repeated; existing Event 012 super-event text/audio handoffs cover research status.

## Unresolved Wording Decisions

- Whether `Orisha/Vodun Nature Courts` should remain a country name is a design decision. Current specs describe a supernatural divine-court route, so I did not rename it.
- If the parent wants counters to show total catalogue size rather than threshold progress, update `/24` and `/6` text and the corresponding achievement wording together with gameplay thresholds.

## Plan Handoff

- No new plan handoff was written. The remaining items are bounded follow-up wording/dynamic-localisation decisions, not a missing mechanic discovered by this audit.
