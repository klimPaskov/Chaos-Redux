# Event 017 Random Faction localisation audit handoff

## Scope

Audit target: Event 017 `Random faction` localisation after the current implementation.

Read sources:

- `AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `.agents/skills/xlsx/SKILL.md` for the read-only workbook check
- Event 017 spec package under `docs/specs/017_random_faction_specs/`
- Current Event 017 implementation files named by the parent
- Offline Paradox wiki pages and relevant vanilla documentation for localisation, decisions, events, scopes, effects, triggers, modifiers, ideas, AI, and on actions

No separate project subagent was spawned from this pass.

## Changed files

- `localisation/english/017_join_faction_l_english.yml`
- This handoff file

## Changed keys

- `chaosx.nr17.10.d`
- `chaosx.nr17.30.a`
- `chaosx.nr17.30.b`
- `random_faction_bloc_pressure_status_aligned`
- `random_faction_bloc_pressure_status_leader`
- `chaosx.events_log.window.event_details.random_faction`
- `chaosx.events_log.window.evolution_details.random_faction.body.stage_3`
- `chaosx.events_log.window.evolution_details.random_faction.body.event_detail`

## Dynamic localisation added or fixed

- `chaosx.nr17.10.d` now names the selected country with `[ROOT.GetName]`.
- `chaosx.nr17.30.a` now names option 1's actual faction with `[random_faction_option_1_leader.GetFactionName]`.
- `chaosx.nr17.30.b` now names option 2's actual faction with `[random_faction_option_2_leader.GetFactionName]`.
- `random_faction_bloc_pressure_status_aligned` now names the current faction with `[ROOT.GetFactionName]`.
- `random_faction_bloc_pressure_status_leader` now names the leader's faction with `[ROOT.GetFactionName]`.

## Behavior or display before and after

- Before: the selected-player event described the pressure as happening to "us" without naming the selected country.
- After: the event opens with `In [ROOT.GetName]`, making the selected country visible in the event text.

- Before: the neighbor pressure follow-up options said "Follow the pressure" and "Look for a counterweight" without identifying which faction the saved options represented.
- After: both options print the actual saved faction names.

- Before: aligned-minor and faction-leader category status lines showed values but did not name the current faction.
- After: both status lines show the current faction dynamically.

- Before: Event Details and one evolution-detail body used implementation-facing phrases such as saved option targets, alignment shock, records the faction leader, and capped cascades.
- After: those strings describe the visible diplomatic pressure premise and avoid exposing internal storage or tuning language.

## Missing key list

None found for Event 017 keys referenced by:

- `events/017_join_faction.txt`
- `common/decisions/017_random_faction_decisions.txt`
- `common/decisions/categories/017_random_faction_categories.txt`
- `common/scripted_localisation/017_random_faction_scripted_localisation.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `common/ideas/017_random_faction_ideas.txt`
- `common/achievements/chaos_redux_achievements.txt`

## Duplicate key list

None found for Event 017 localisation definitions across `localisation/english/*.yml`.

## Scripted localisation issue list

- `GetRandomFactionBlocPressureStatus` resolves all four branches to existing keys.
- Event-log scripted localisation selectors for event ID 17 and Random Faction evolution type/stages resolve to existing keys.
- No direct `§` or `£` format characters were found inside the two scripted localisation files checked.
- No scripted localisation patch was needed.

## Dynamic text opportunities

- Decision cost text is currently static and mirrors constants. If the parent expects future tuning without text edits, route a follow-up to add scripted localisation cost helpers or another dynamic cost-display pattern.
- Pressured neutral status could be stronger if gameplay stores and exposes the pressure source faction or current leading faction pull.
- `chaosx.nr17.40.d` still says "A small country's accession" because the leader reaction event is fired in faction-leader scope without a saved visible target for localisation. If the parent wants the minor named there, gameplay must carry a target into that event safely.

## Cross-surface mismatch notes

- `docs/spreadsheets/chaos_redux_events_catalog.xlsx` row 17 still mirrors the old Event Details and Evolution III wording:
  - old Event Details mentions saved option targets, alignment shock, and Bloc Pressure decision opening
  - old Evolution III text mentions a capped cascade and instant map repaint
- I did not edit the workbook because the parent explicitly scoped it as read/check only if practical. The spreadsheet worker should update row 17 to mirror the final in-game Event Details and evolution wording.
- `docs/events/017_random_faction.md` remains implementation documentation. It contains technical descriptions by design and does not need to mirror the in-game Event Details string exactly.

## File encoding concerns

- `localisation/english/017_join_faction_l_english.yml`: UTF-8 BOM present after patch.
- `localisation/english/chaosx_achievements_l_english.yml`: UTF-8 BOM present.
- `localisation/english/chaosx_event_names_l_english.yml`: UTF-8 BOM present.
- Checked script `.txt` files are not BOM files, which is normal for the current repo script files.

## Recommended fixes

- Update `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, `Events` row ID 17, to match the patched in-game Event Details and Evolution III wording.
- Consider a later scripted localisation helper for dynamic cost text if Event 17 decision cost constants are expected to keep changing.
- Consider saving a visible accession actor target for `chaosx.nr17.40` if faction-leader reaction text should name the newly aligned minor.

## Meaningful validation run

- Verified Event 017 referenced localisation keys are present.
- Verified no duplicate Event 017 keys across English localisation.
- Verified named `.yml` files keep UTF-8 BOM after the patch.
- Read `docs/spreadsheets/chaos_redux_events_catalog.xlsx` and confirmed row 17 exists and currently mirrors the old in-game detail wording.

## Skipped meaningful validation and why

- Did not edit or save the workbook because the parent requested it as read/check only if practical.
- Did not run in-game UI validation. This pass was limited to file-level localisation coverage and text consistency.

## Unresolved wording decisions

- Whether Event 17 spreadsheet text should be updated by the parent or a spreadsheet worker.
- Whether faction-leader reaction event `chaosx.nr17.40` should receive a gameplay target handoff so its text can name the newly aligned minor.

## Plan handoff path

No separate improvement plan was written.
