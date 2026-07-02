# Event 014 Cannibalism Final Localisation Audit

Subagent role: localisation audit and narrow text patch.

Scope reviewed:

- `localisation/english/014_cannibalism_l_english.yml`
- `localisation/english/chaosx_event_names_l_english.yml`
- `localisation/english/chaosx_music_l_english.yml`
- `common/decisions/014_cannibalism_decisions.txt`
- `common/national_focus/014_cannibalism_focus_tree.txt`
- `common/ideas/014_cannibalism_ideas.txt`
- `common/dynamic_modifiers/014_cannibalism_state_modifiers.txt`
- `common/characters/CBL.txt`
- `common/achievements/chaos_redux_achievements.txt`
- `interface/014_cannibalism.gfx`
- `docs/events/014_cannibalism.md`

## Audit Results

Missing key list: none found in the scoped surfaces. The audit checked 344 unique required keys derived from Event 014 decisions, missions, focus ids, idea ids, dynamic modifier ids, CBL character name tokens, Event 014 achievement ids and tooltips, `chaosx.event_name.14`, and super-event music/title/description/quote/button keys for IDs 141 through 144.

Duplicate key list: none found inside the three scoped localisation files. No cross-file duplicates were found between `014_cannibalism_l_english.yml`, `chaosx_event_names_l_english.yml`, and `chaosx_music_l_english.yml`.

Scripted localisation issue list: no broken scripted-localisation references were found in the scoped files. The scoped audit did not edit global scripted localisation files because they were outside the prompt scope.

Dynamic text opportunities:

- `cannibalism_cbl_last_table_map_mission_desc` and `cbl_map_the_final_larder_desc` described the map mission in generic terms. They now spell out the implemented visible requirements: at least four controlled states, coast or rail projection, and at least one completed hunting-ground project.
- Cost strings remain static text that matches the current scripted costs. If parent retunes Event 014 constants, these cost keys should be updated in the same change or converted to a scripted localisation pattern if the cost values become variable at runtime.

Cross-surface mismatch notes:

- Fixed: the CBL focus text and mission text now match the map mission helper requirement in `cannibalism_cbl_last_table_map_control`.
- Fixed: `docs/events/014_cannibalism.md` used update-history phrasing around the 36-focus tree and cleanup. The doc now describes the feature as current implementation.
- Remaining non-localisation note: `GFX_goal_cannibalism_port_harvests` is registered in `interface/014_cannibalism.gfx` and listed in `docs/events/014_cannibalism.md`, but is not referenced by the scoped CBL focus tree.
- Remaining non-localisation note: `GFX_portrait_CBL_hannibal` is registered in `interface/014_cannibalism.gfx` and listed in `docs/events/014_cannibalism.md`, but no scoped CBL character currently references it.

File encoding concerns:

- `014_cannibalism_l_english.yml`, `chaosx_event_names_l_english.yml`, and `chaosx_music_l_english.yml` all retain UTF-8 with BOM.
- No `:0` localisation key style violations were found in scoped localisation.
- No leading-space localisation key definitions were found in scoped localisation.

Recommended fixes with file paths and keys:

- Completed: `localisation/english/014_cannibalism_l_english.yml`
  - `cannibalism_cbl_last_table_map_mission_desc`
  - `cbl_map_the_final_larder_desc`
- Completed: `docs/events/014_cannibalism.md`
  - Removed update-history wording from the CBL focus tree and cleanup descriptions.
- Parent follow-up optional: decide whether `GFX_goal_cannibalism_port_harvests` and `GFX_portrait_CBL_hannibal` are intentional reserved assets or stale asset/documentation entries.

## Patch Details

Changed files:

- `localisation/english/014_cannibalism_l_english.yml`
- `docs/events/014_cannibalism.md`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/2026-07-01_event014_final_localisation_audit.md`

Changed keys:

- `cannibalism_cbl_last_table_map_mission_desc`
- `cbl_map_the_final_larder_desc`

Dynamic localisation added or fixed:

- No scripted dynamic localisation was added.
- Existing player-facing text was made more explicit for an existing dynamic mission requirement.

Behavior or display before and after:

- Before: the Last Table map mission description said to hold enough states, map projection, and hunting-ground projects.
- After: the mission description says to control at least four states, keep coast or rail projection, and maintain at least one completed hunting-ground project.
- Before: the CBL focus description said the commune needed enough territory and prepared hunting grounds.
- After: the focus description states the same four-state, coast-or-rail, and hunting-ground project requirements.
- Before: the event doc contained "now has" and "now clears" update-history phrasing.
- After: the event doc describes those systems as current implementation.

Meaningful validation run:

- Rechecked BOM and key style for the three scoped localisation files. All three retain BOM, contain no `:0` entries, and contain no leading-space key definitions.
- Rechecked key coverage across scoped decisions, missions, focuses, ideas, state modifiers, CBL character names, Event 014 achievements, event name, and super-event music/text entries. Result: 344 unique required keys, 0 missing.
- Rechecked duplicate localisation keys inside and across scoped localisation files. Result: 0 duplicate keys.
- Verified the patched map mission wording against `cannibalism_cbl_last_table_map_control`, which requires `cannibalism_cbl_has_map_projection`, `cannibalism_cbl_has_hunting_ground_project`, and `controlled_states = 4` through `constant:cannibalism_last_table_requirement.controlled_states`.
- Rechecked update-history wording in `docs/events/014_cannibalism.md`. No `now`, `newly`, `reworked`, `changed because`, or `this update` matches remain there.

Skipped meaningful validation and why:

- No in-game UI validation was run. This was a text/key audit with no GUI layout change.
- No global scripted-localisation audit was performed because the prompt scope was limited to the named files.

Unresolved wording decisions:

- None for Event 014 localisation in the scoped files.

Plan handoff path:

- No broader plan handoff was written. The two remaining notes are asset/reference cleanup decisions for the parent, not localisation blockers.
