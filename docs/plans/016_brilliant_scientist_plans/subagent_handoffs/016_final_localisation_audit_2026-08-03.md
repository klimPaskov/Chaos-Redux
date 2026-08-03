# Event 016 final localisation audit - 2026-08-03

## Scope and evidence

This read-only pass covers the high-speed materials trial tranche, the ten-country settlement tranche, Event 016 event/localisation surfaces, scripted localisation, event-log/detail mappings, and referenced report/decision assets.

Evidence was checked in `events/016_brilliant_scientist_*.txt`, `common/decisions/016_brilliant_scientist_*.txt`, the 17 `localisation/english/016_brilliant_scientist*_l_english.yml` files, the six `common/scripted_localisation/016_brilliant_scientist_*.txt` files, the shared Event Log scripted localisation, and the linked plans/specs/docs.

## Missing key list

- No missing localisation keys were found in the 259 Event 016 event/title/description/option references.
- No missing localisation keys were found in the 680 bounded Event 016 UI references across events, decisions, focuses, ideas, modifiers, characters, country files, special projects, technologies, and units.
- The high-speed action has all required decision, cost, effect, event (`chaosx.nr16.195`), outcome, and dynamic-modifier keys.
- All six new settlement options (`chaosx.nr16.5.h_ger` through `.5.m_cze`) and their tooltip keys are present.
- All ten settlement facility/custody scripted-localisation outputs have corresponding keys.
- Event name 16, Event Log evolution/detail entries, and world-end title/detail outputs are present.

## Duplicate key list

- No duplicate case-sensitive localisation keys were found across 2,780 Event 016 English keys.
- No duplicate `defined_text` names were found across 92 Event 016 scripted-localisation definitions.
- A case-insensitive comparison surfaced `KRG_XENOBIOLOGICAL_ASCENDANCY` and a lower-case focus key as a near-collision, but the keys are case-sensitive and are not duplicates.

## Scripted localisation issue list

- No undefined `GetBrilliant...` scripted-localisation calls were found in Event 016 localisation values.
- No missing `localization_key` targets were found in the six Event 016 scripted-localisation files.
- No undefined scripted-localisation references were found in the audited Event 016 event, decision, focus, and country surfaces.
- Event Log mappings resolve Event 016 to `chaosx.event_name.16`, `chaosx.events_log.window.event_details.brilliant_scientist`, all four evolution title/description pairs, and both world-end title/detail branches.
- No forbidden section-sign or pound-sign format characters were found in the six Event 016 scripted-localisation files.

## Dynamic text opportunities

- The high-speed event description already resolves the saved test-corridor state name with `[brilliant_scientist_high_speed_test_corridor.GetName]` and appends the host-specific facility clause through `GetBrilliantScientistCountrySettlementFacilityClause`.
- Settlement option tooltips already use host-specific facility/custody clause selectors for all ten receipts.
- The only bounded wording opportunity is consistency: ten settlement/context tooltip strings use "Capacity rises/falls," while the Directorate UI and high-speed tooltips call the same variable "Project Capacity."

## Cross-surface mismatch notes

- High-speed source constants, decision cost text, event text, effect tooltip, dynamic modifier text, and implementation docs agree on PP 100, Air XP 25, Support Equipment 150, Motorized 200, fuel 5,000, manpower 3,000, three civilian factories, and 180 days.
- The `.195` result is intentionally absent from the Event Log/catalog row; the high-speed addendum, event docs, and catalog all describe it as a child action rather than a standalone evolution entry.
- The ten settlement receipts are represented in event options, resolver effects, AI factors, host-flavor clauses, and localisation without an unwired text surface.
- Report and decision icon registrations resolve to existing DDS files; no localisation-facing asset name is missing.
- No hidden route text or premature secret-reveal wording was found in the audited high-speed or settlement strings.

## File encoding concerns

- All 17 Event 016 English YAML files are UTF-8 with BOM.
- The six Event 016 scripted-localisation TXT files are BOM-free, matching their script-file role; this is not a localisation YAML encoding defect.
- No Event 016 localisation key uses the deprecated `:0` form, leading whitespace, or malformed multi-line value syntax.

## Recommended fixes

- No blocking localisation patch is required.
- Optional future wording pass: normalize the ten settlement/context tooltip phrases from "Capacity rises/falls" to "Project Capacity rises/falls" in `localisation/english/016_brilliant_scientist_directorate_outcomes_l_english.yml` and any matching context strings, if the owning gameplay/UI pass prefers the longer label.
- Leave `.195` out of Event Log/catalog child-event listings unless the event design explicitly changes; adding a row would contradict the accepted high-speed addendum.

## Changed files and validation

- Changed file: this handoff only; no gameplay or localisation source file was patched.
- Validation included BOM/format checks, case-sensitive duplicate-key scans, scripted-localisation definition/reference scans, bounded cross-surface key coverage scans, focused `.195` reference search, and Event Log mapping inspection.
- In-game loading and live UI validation were not run because repository instructions reserve those checks for the user.

## Unresolved wording decisions

The owner should decide whether "Capacity" is acceptable shorthand in settlement receipts or whether all ten strings should use the Directorate UI label "Project Capacity."

## Handoff path

`docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_final_localisation_audit_2026-08-03.md`
