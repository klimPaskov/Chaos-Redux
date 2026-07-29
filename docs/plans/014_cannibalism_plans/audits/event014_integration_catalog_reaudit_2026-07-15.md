# Event 014 Integration and Catalog Re-audit

Date: 2026-07-15

Scope: bounded source-level re-audit of Event 014 integration, registry, terminal, scenario, achievement, shared-system, media, cleanup, and authoritative catalog surfaces. This report does not replace the separate country-package, decision/mission, focus-tree, localisation/asset, documentation, spreadsheet, or super-event visual audits.

## Result

Event 014 is consistently registered as `chaosx.nr14.1`, Minor Fire-Once, outside every event cluster. Its ordinary, Wendigo, terminal, defeat-aftermath, Event Details, SCN-010, achievement, shared-threat, cross-event, super-event, cleanup, and workbook integrations are present and mutually consistent.

| Severity | Residual findings |
| --- | ---: |
| P0 | 0 |
| P1 | 0 |
| P2 | 0 |
| P3 | 0 |

One narrow catalog-helper maintenance defect was found and closed during the audit. It was not a gameplay or workbook defect: the helper still emitted the retired `Implemented` vocabulary, truncated the Manual Scenarios table and status validation to row 10, and assumed an existing calculation-properties object. The repaired helper now emits `Fully Functional`, preserves the current row count including concurrent SCN-013, normalizes the current validation vocabulary, and creates calculation properties when absent. The final residual count above is therefore zero at every severity.

## Required references and method

The audit used the repository instructions plus the `chaos-redux-events`, `chaos-redux-subagents`, `xlsx`, and `chaos-redux-super-events` skills. The required offline wiki pages were consulted for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, AI, achievements, interface modding, and scripted GUI. Relevant vanilla documentation and precedents were also checked for on-actions, scripted GUIs, decisions, script constants, achievements, music, and sound assets.

No Paradox wiki web page was used. No gameplay source, localisation, media asset, or authoritative workbook cell was changed by this audit.

## Integration evidence

### Identity, classification, dispatcher, and auto-fire

- `events/014_cannibalism.txt` defines exactly one entry root, `chaosx.nr14.1`. It is hidden and triggered-only; its immediate block enters through `cannibalism_begin_from_prefire_context`.
- `common/scripted_effects/chaosx_logic_effects.txt` registers Event 014 exactly once in `global.fire_once_events`, maps it to the fire-once type, evaluates its availability, and records its fired/history state. It has no major-event or repeatable-event registration.
- `common/scripted_effects/chaosx_event_cluster_effects.txt` contains no Event 014 registration or Cannibalism cluster reference. The catalog cluster cell is correspondingly empty.
- `common/scripted_effects/chaosx_settings_effects.txt` prepares Event 014 through `cannibalism_prepare_random_event_fire`, dispatches the standard `chaosx.nr[EVENT_ID].1` root, and then applies the shared fire-once handler.
- Event 014 uses the existing daily event timer. It adds no Event 014 daily, weekly, or monthly all-country on-action. Its host-selection country scan is a one-shot pre-fire selection, not recurring global work.

### Name mapping, actors, and evolutions

- `chaosx.event_name.14` resolves to `Cannibalism`, and the debug/event-name selector maps numeric Event ID 14 to that key.
- The opening history entry first selects the regular `cannibalism_first_host` event target and falls back to `cannibalism_latest_actor` only if necessary.
- Live actor ownership is refreshed at initial activation, external spread, warlord creation, ordinary Hannibal unification, and the existing-ZZZ Wendigo merge. Ordinary unification stores its CBL host as `cannibalism_latest_actor`; the Wendigo merge stores the surviving ZZZ host.
- Shared Event Log and evolution-history arrays snapshot actor scopes when entries are recorded. Clearing the live latest-actor target during final cleanup therefore does not erase recorded history.
- Defeat attribution uses the scoped `global.cannibalism_defeat_contributors` roster. Reconstruction eligibility and achievement participation iterate that same roster before final cleanup.
- Evolution I, II, and III use constants for their type, stage, and tier identities. Active runtime and pre-fire paths both record the same milestones. Pre-fire Evolution III enters through the real convergence transaction rather than synthetic marker assignment.
- Event Details exposes exactly three evolution previews. Evolution III remains gated behind `cannibalism_reveal_complete`.

### Event Details and terminal rows

- Neutral and revealed detail selectors are separate. The neutral detail contains none of the Hannibal, Lecter, Wendigo, world-end, or unification spoilers checked by this audit.
- Terminal registry ID 6 is `world_is_the_larder`, owner Event 14, default enabled, and points to super-event 50.
- Terminal registry ID 7 is `no_thaw_will_come`, owner Event 14, default enabled, and points to super-event 53.
- Both terminal rows remain hidden until reveal, have distinct active flags, and use independent toggle IDs in `global.disabled_world_end_scenarios`.
- Shared terminal triggers check registry IDs 6 and 7 independently. The ordinary route cannot substitute for or disable the Wendigo route, and vice versa.

### SCN-010 and achievements

- SCN-010 registers exactly five types: Discipline Collapse, Ritual Cells, Silent Islands, Warlord States, and Convergence.
- It uses the four shared intensities Low, Medium, High, and Maximum. The selector wraps across exactly those five type IDs.
- Scenario launch performs an atomic preflight before runtime mutation, dispatches one of exactly five setup branches, and removes reservation, temporary-array, pending-prefire, and launch state on exit.
- Event 014 has exactly 18 achievement definitions. Five are public and 13 are hidden.
- Each achievement definition delegates to its matching completion trigger. The Event Details tracker has exactly 18 read-only tracker decisions and uses those same completion triggers with staged visibility.
- Manual scenario starts disqualify campaign achievement eligibility as specified.

### Shared threat and declared cross-event behavior

- `cannibalism_refresh_world_threat_source` owns `world_threat_source_cannibalism` and immediately refreshes the shared world-threat state after setting or clearing it.
- The shared dynamic threat aggregator consumes that source. Final Cannibalism cleanup clears the source and refreshes the aggregate again.
- Sixteen focused cross-event assertions passed: actual nonhuman origins and spread targets are excluded; Fury keeps its explicit human exception; Death-consumed, nuclear-fallout, severe-chemical, severe-biological, and nonhuman-owned states cannot become Larder states; civilian loss uses the shared exact-population effect; the Deaths-disabled path still removes population without recruitable-manpower gain; prisoner feeding splits civilian and military deaths once; Wendigo merging reuses the live original ZZZ and blocks Event 002's legacy terminal while pending or merged; Fallout's final-silence handoff excludes both Event 014 world ends; famine, locust, disease, and disaster supply ingress remains connected; relief writes shared disaster/famine state; camp linking requires a prison/camp plus an active cell; and nuclear, biological, and chemical contamination damages cells.
- Event 014 has no Random War or Fury cluster registration. It reads canonical CBRN and disaster state rather than duplicating those systems.

### Super-events, music, sound, and rights

- Public super-event IDs are 49 for the reveal, 50 for The World Is the Larder, 52 for defeat aftermath, and 53 for No Thaw Will Come. Event 014 does not use ID 51.
- All four IDs have scripted image, title, quote, button, and description mappings plus registered GFX sprites and DDS paths.
- Each ID has six volume-specific sound variants and six volume-specific sound-effect variants. The shared audio helper resolves the variant dynamically from the super-event ID and volume suffix.
- The four OGG files and four WAV files are unique and match the hashes recorded in `docs/super_events/014_cannibalism/audio_research.md`.
- `ffprobe` identified all eight files as stereo 44.1 kHz audio. WAV durations were 114.0/114.0 seconds for ID 49, 120.0/120.0 for ID 50, 116.1/116.001 for ID 52, and 118.0/118.0 for ID 53.
- The music attribution page includes all four IDs, source and rights data, including the required CC BY-SA 2.0 attribution for ID 52. Preserved rights evidence is present.

### Cleanup and registry retirement

- Country and state retirement paths remove actors and nodes from their live registries.
- Global completion only runs after victory and absence of Cannibalism residue. It clears system, convergence, unification, evolution, terminal, threat, and live-target state; performs owner-safe terminal-hunt cleanup; and refreshes shared world threat.
- Final cleanup resizes all 15 audited runtime arrays: six live registries and nine spread-queue columns. It also resets aggregate network/larder counters.
- Scenario cleanup removes reservations, launch state, temporary arrays, and pre-fire variables. The system-started flag is cleared so a later clean scenario start is possible.
- Shared Event Log history and evolution actor snapshots are intentionally retained; they are history records rather than live Cannibalism registries.

## Catalog workbook evidence

Authoritative workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`

Audited SHA-256: `6aa758d699d814599a1011d5f9acc1089bbf42baf053be7a4dbabadd525091a2`

- `Events!A15:M15` matches all 13 current Event 014 source/localisation fields exactly. The row reads Minor Fire-Once, has an empty cluster field, and records `Fully Functional`.
- `Scenarios!A10:F10` matches all six current SCN-010 source/localisation fields exactly and records `Fully Functional`.
- The pre-reveal catalog description contains none of the audited hidden-identity spoilers.
- The Events table covers `A1:M1015`. The Manual Scenarios table covers `A1:F11`, including concurrent SCN-013.
- Event status validation covers `M2:M1015`. Scenario status validation covers `F2:F11` and uses the current `Fully Functional` vocabulary.
- Conditional formatting covers Event 014 and SCN-010 status cells.
- The workbook contains no formulas, formula-error cells, or formula-error tokens.
- Current Event 014 authority documents and the current spreadsheet audit agree with both `Fully Functional` cells. Historical `Implemented` evidence is explicitly bannered as a superseded 2026-07-12 checkpoint.

The repaired `docs/plans/014_cannibalism_plans/tooling/update_event014_catalog.py` was run twice against a temporary workbook copy. Both target rows matched the helper, the second run was idempotent, the Manual Scenarios table and validation remained at row 11, and SCN-013 remained intact. The authoritative workbook hash did not change during this test.

## Task-specific validation

- 22 of 22 static integration assertions passed for the root, classification, cluster absence, name/actor mapping, evolutions, Event Details, terminal registry, SCN-010, achievements, shared threat, cleanup arrays, and public super-event assets.
- 16 of 16 declared cross-event assertions passed across Zombies/Wendigo, Deaths, Fallout, CBRN, disasters, camps, relief, and population-loss integration.
- 19 of 19 authoritative catalog target cells matched live localisation and source identity exactly.
- All eight Event 014 audio files passed codec/channel/rate/duration inspection, hash reconciliation, and registry lookup.
- Catalog authority documents, the current spreadsheet audit, the workbook, and the update helper all use the same `Fully Functional` vocabulary.

## Files changed by this audit

- `docs/plans/014_cannibalism_plans/tooling/update_event014_catalog.py`
- `docs/plans/014_cannibalism_plans/audits/event014_integration_catalog_reaudit_2026-07-15.md`

No gameplay file, localisation file, visual/audio asset, or workbook file was edited by this audit. No commit was created.

## Simplifications, omissions, and blockers

None. No fallback, placeholder, skipped declared route, missing catalog field, missing AI/achievement/terminal integration, or unresolved blocker remains in this audit scope.

This was a source, asset-registry, media-metadata, and workbook audit. It did not launch a live HOI4 runtime session and does not claim that such a session was performed.
