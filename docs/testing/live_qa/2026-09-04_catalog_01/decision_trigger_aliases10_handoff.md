# Decision trigger alias audit handoff

Status: audited no-op. The requested alias repair has no eligible decision-source cases in the fresh launch log or the current source tree, so no gameplay file was changed and no commit was created.

## Scope and exclusions

The audit used `docs/testing/live_qa/2026-09-04_catalog_01/logs/launch_09/logs/error.log` with SHA-256 `9467A687F36B02E5F7E74DE8D0D2426A5F1D766FF278043C12120F7A57AEB87F`.

The eligible source surface was `common/decisions/**/*.txt`, excluding Event 029 files. Event 032 decision and mission files were included in the scan; the separate Event 032 operations-effects sources are parent-owned and were excluded from this decision tranche. The protected Event 006, 012, 016, and 023 surfaces were also left untouched. AI weights and all other weighted logic were not inspected for patching and were not changed.

The requested mappings were checked against the installed trigger documentation and the offline wiki: `political_power` to `has_political_power`, `has_command_power` to `command_power`, `is_capitulated` to `has_capitulated`, `is_at_war` to `has_war`, and `is_player` to `is_ai = no` only where the surrounding scope and negation would be equivalent.

## Fresh native errors

The log contains 63 `Invalid trigger` rows using one of the five requested alias names across all loaded surfaces, representing 42 unique file-and-line locations because some diagnostics repeat during the later load pass.

| Alias | Native rows | Unique locations | Loaded surfaces | Eligible decision rows |
| --- | ---: | ---: | --- | ---: |
| `political_power` | 15 | 11 | `common/scripted_triggers`, `common/scripted_effects`, and `events` | 0 |
| `has_command_power` | 6 | 6 | `common/scripted_triggers` and `events` | 0 |
| `is_capitulated` | 34 | 19 | `common/scripted_triggers` and `common/scripted_effects` | 0 |
| `is_at_war` | 5 | 3 | `common/scripted_triggers` and `common/scripted_effects` | 0 |
| `is_player` | 3 | 3 | `common/scripted_triggers` | 0 |

The only `Invalid trigger` row whose path is under `common/decisions` is the excluded Event 029 `modifier` trigger at line 3748; it is not one of the requested aliases and remains parent-owned.

The alias rows are outside this decision tranche at these locations:

- `political_power`: `common/scripted_triggers/023_sov_nuclear_bombs_cost_triggers.txt` lines 10, 15, 27, and 33; `common/scripted_triggers/026_black_friday_triggers.txt` line 339; `common/scripted_triggers/chaosx_universal_cost_triggers.txt` line 142; `common/scripted_effects/021_random_civil_war_parent_effects.txt` lines 822, 873, and 1003, each repeated once; `common/scripted_effects/031_random_terror_effects.txt` line 3181, repeated once; and `events/031_terrorist_attack.txt` line 314.
- `has_command_power`: `common/scripted_triggers/028_asteroid_incoming_triggers.txt` lines 510 and 518; and `events/032_missile_crisis.txt` lines 265, 271, 277, and 283.
- `is_capitulated`: `common/scripted_triggers/025_alien_technology_in_antarctica_triggers.txt` lines 24, 216, 245, and 256; `common/scripted_effects/025_alien_technology_in_antarctica_ledger_effects.txt` lines 652, 666, 680, 695, 710, 725, 740, 755, 950, 995, 1040, 1085, 1130, and 1175, each repeated once; and `common/scripted_effects/025_alien_technology_in_antarctica_runtime_effects.txt` line 910, repeated once.
- `is_at_war`: `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt` line 316; `common/scripted_effects/032_missiles_scenario_effects.txt` line 283, repeated once; and `common/scripted_effects/035_great_depression_effects.txt` line 6247, repeated once.
- `is_player`: `common/scripted_triggers/039_murder_mystery_integration_triggers.txt` lines 16 and 77; and `common/scripted_triggers/039_murder_mystery_runtime_triggers.txt` line 108.

Those non-decision files were not edited because this task is limited to exact aliases in decision sources. The Event 032 operations-effects source remains parent-owned.

## Eligible decision-source scan

A word-boundary scan over all decision `.txt` files except Event 029 found 37 exact `political_power` tokens, zero exact `has_command_power`, zero exact `is_capitulated`, zero exact `is_at_war`, and zero exact `is_player` tokens.

The 37 `political_power` matches are valid context-bearing names rather than invalid trigger keys: 17 are `check_variable = { var = political_power ... }` in `common/decisions/012_africa_decisions.txt`, five are the same variable form in `common/decisions/016_brilliant_scientist_directorate_project_board.txt`, three are constant field names in `common/decisions/016_brilliant_scientist_directorate_synthesis.txt`, and twelve are constant field names in `common/decisions/biological_sabotage_decisions.txt`.

No line matching the requested alias pattern `alias =`, `alias >`, or `alias <` exists in any decision file except the excluded Event 029 files. The Event 032 decision and mission files also contain zero exact requested alias keys. The apparently similar `political_power` variable and constant field names were therefore preserved byte-for-byte.

## Backup inventory

The requested archive directory is [`pre_patch_decision_trigger_aliases10`](pre_patch_decision_trigger_aliases10). Its inventory is empty because the eligible source scan produced no candidate file. The inventory decision is recorded in [`pre_patch_decision_trigger_aliases10/README.md`](pre_patch_decision_trigger_aliases10/README.md).

## Before and after behavior

Before this audit, the fresh native log showed no requested alias error in an eligible decision source. After this audit, the decision source tree is unchanged, so all decision costs, requirements, comparators, values, scopes, AI blocks, mission lifecycles, and cleanup behavior are unchanged.

No replacement was applied to the valid `check_variable` variable name `political_power`, and no replacement was applied to the valid `constant:...political_power` field names. Replacing either would change variable or constant references rather than repair a trigger keyword.

## Documentation and precedent consulted

The required offline pages were opened before source inspection: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding in `paradox_wiki/`.

The installed vanilla documentation `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md` documents `command_power`, `has_capitulated`, `has_political_power`, `has_war`, and `is_ai` as valid country triggers and does not document `is_player`.

Vanilla decision precedents use `command_power > ...`, `has_capitulated = yes`, `has_war = yes/no`, `has_political_power < ...`, and `is_ai = no` in the installed `common/decisions/AFG.txt`, `BEL.txt`, `CZE.txt`, and `categories/00_decision_categories.txt` files. This confirms the requested replacement forms without requiring a semantic guess.

## Validation and limits

The fresh-log parser was rerun with exact alias matching and grouped by alias, source path, and line. It reported 63 native alias rows, 42 unique locations, and zero rows under eligible `common/decisions` paths.

The current source scan was rerun with exact word boundaries and a structural trigger-key check. It reported zero eligible invalid alias keys and preserved the 37 valid context-bearing `political_power` references described above.

No `hoi4.gui_inspect` or `hoi4.gui_render` evidence was required because no decision-owned GUI surface was touched. No `chaosx_ai_probability_auditor` pass was required because no AI weight, probability-bearing modifier, or weighted target changed. No game launch or live gameplay validation was run.

## Remaining issues and parent routing

The 63 alias diagnostics remain in out-of-scope scripted trigger, scripted effect, and event files listed above. Event 029's separate `modifier` trigger remains excluded by the parent boundary, and the Event 032 operations-effects source remains parent-owned. No semantics ambiguity was found in the eligible decision surface, and no plan handoff was written.
