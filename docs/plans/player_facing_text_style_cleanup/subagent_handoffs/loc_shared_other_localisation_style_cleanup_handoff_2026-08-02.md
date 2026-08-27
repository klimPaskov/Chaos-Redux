# Shared and Other Localisation Style Cleanup Handoff

Scope: assigned `localisation/english/*.yml` files excluding the 001 through 020 event files and the cbrn, cbw, bio, chemical, condemnation, camp, fallout, germany, and japan file families.

The pass follows the player-facing copy rules supplied by the parent. Revised text removes em dashes, semicolons, vague dramatic filler, implementation-history wording, staccato reactions, and dialectical hedging while preserving localisation keys, dynamic tokens, formatting colours, and gameplay meaning.

## Changed files


Shared files: `_chaosx_events_l_english.yml`, `chaosx_achievements_l_english.yml`, `chaosx_decisions_l_english.yml`, `chaosx_doctrines_l_english.yml`, `chaosx_equipment_l_english.yml`, `chaosx_event_names_l_english.yml`, `chaosx_factions_l_english.yml`, `chaosx_gui_l_english.yml`, `chaosx_ideas_l_english.yml`, `chaosx_modifiers_l_english.yml`, `chaosx_operations_l_english.yml`, `chaosx_raids_l_english.yml`, `chaosx_special_projects_l_english.yml`, `chaosx_technologies_l_english.yml`, and `chaosx_units_l_english.yml`.

`loading_tips_l_english.yml` was audited but has no remaining diff. The parent restored the Henry Adams quotation before this handoff.

## Key-level changes

- Numeric event descriptions and news descriptions from 022 through 099 were rewritten to name the actor, action, target, consequence, or current state directly. Existing `[ROOT...]`, `[FROM...]`, `[?global...]`, and colour tokens were preserved.
- Numeric event option and news reaction keys with vague filler were clarified, including `chaosx.nr22.2.a`, `chaosx.nr22.3.b`, `chaosx.news.22.a`, `chaosx.nr23.2.a`, `chaosx.news.23.a`, `chaosx.nr24.2.a`, `chaosx.news.24.a`, `chaosx.nr26.2.b`, `chaosx.news.27.a`, `chaosx.news.31.a`, `chaosx.nr30.7.a`, `chaosx.news.34.a`, `chaosx.news.35.a`, `chaosx.nr31.2.a`, `chaosx.news.36.a`, `chaosx.nr32.2.a`, `chaosx.news.37.a`, `chaosx.news.38.a`, `chaosx.nr34.2.a`, `chaosx.nr35.2.a`, `chaosx.news.40.a`, `chaosx.nr36.2.a`, `chaosx.news.41.a`, `chaosx.news.42.a`, `chaosx.nr39.2.a`, `chaosx.news.45.a`, `chaosx.nr41.2.a`, `chaosx.nr42.2.a`, `chaosx.news.47.a`, `chaosx.nr43.2.a`, `chaosx.news.48.a`, `chaosx.news.49.a`, `chaosx.nr47.2.a`, and `chaosx.news.50.a`.
- `063_subject_independence_l_english.yml` now includes the missing `chaosx.nr63.2.b` key with the player-facing response `Accept the declaration.`
- `082_law_upgrade_l_english.yml` had control-character mojibake removed from `chaosx.nr82.2.d` and now uses readable mobilisation prose.
- `046_great_earthquake_l_english.yml` and `099_desert_storm_l_english.yml` no longer expose internal reserved-report wording. Their report descriptions state the neutral current world condition.
- `chaosx_event_names_l_english.yml` expands `chaosx.event_name.77`, `.84`, `.85`, and `.87` from abbreviations to `Equipment Aid`, `Political Power`, `Experience`, and `The First World War`.
- `_chaosx_events_l_english.yml` received direct wording for classification, timers, chaos sources, chaos timing, world-end, evolution, configuration, contamination, the Chamberlain event, and genocide register text. No gameplay tokens were removed.
- Shared decision, GUI, idea, equipment, doctrine, operation, raid, special-project, modifier, faction, technology, unit, and achievement descriptions received narrow copy edits where they exposed implementation process, generic AI filler, or unclear tradeoffs. Dynamic values and scripted localisation calls remain intact.

## Missing key list

The scoped event-reference scan found one missing key that was fixed: `chaosx.nr63.2.b` in `063_subject_independence_l_english.yml`.

The remaining unresolved event-reference candidates are orphan or unknown definitions with no direct caller and no approved lore source: `chaosx.news.79.a`, `chaosx.news.80.t`, `chaosx.news.80.d`, `chaosx.news.80.a`, and `chaosx.nr100.1.t`, `.d`, `.a`, `chaosx.nr100.2.t`, `.d`, `.a`. They are listed for the parent rather than filled with invented fallback lore.

The common-file scan found no missing `chaosx.*` localisation references. Scripted-localisation scans contain intentionally generated `chaosx.event_name.*` ranges for IDs that have no event source, so those generated ranges were not bulk-filled.

## Duplicate key list

Exact-case duplicate scan of the assigned files found no duplicate keys.

There is one case-insensitive collision that predates this pass and remains unresolved because renaming either side would alter gameplay references: `ZIN` in `chaosx_countries_l_english.yml:29` and `zin` in `chaosx_ideas_l_english.yml:101`.

## Scripted localisation issue list

No broken scripted-localisation reference was identified in the assigned surface after the scoped common-file and event-file scans.

The generated `chaosx.event_name.*` references in `common/scripted_localisation/chaosx_scripted_localisation_debug.txt` and `chaosx_scripted_localisation_settings.txt` intentionally cover IDs without corresponding source events. This remains a dynamic-range design issue for the owner of those helpers, not a safe localisation-only patch.

## Dynamic text opportunities

- The UFO decision category description in `chaosx_decisions_l_english.yml` still embeds the target threshold as a direct dynamic variable. It is readable, but a shared scripted localisation helper could expose the threshold name and current target more clearly.
- The event-log and scenario surfaces in `chaosx_gui_l_english.yml` contain several fixed labels for event classes and evolution stages. They are functional, but a future GUI pass could centralise route names and stage names through scripted localisation.
- The event-name range has explicit names through 99 and selected later IDs. Unknown event IDs continue to use generated or generic labels. The owner of the debug/settings helper should decide whether those IDs are deliberately hidden or need a registry expansion.

## Cross-surface mismatch notes

- Event descriptions now use direct state and consequence wording, while event scripts and dynamic tokens are unchanged.
- The new `chaosx.nr63.2.b` option label matches the existing acceptance branch, which only reduces stability and fires the independence news event.
- The neutral report text for 046 and 099 keeps the reserved event slots displayable without exposing internal slot or effect terminology.
- Event-name labels are clearer in the event log, but the corresponding source filenames and event IDs remain unchanged.
- Existing blank descriptions in older numeric event files remain visible as blank descriptions. Filling them safely requires event-specific design input and was not invented in this copy pass.

## Encoding concerns

All assigned English localisation files were rechecked after edits and retain UTF-8 with BOM. The scoped scan found no control characters after the 082 mojibake repair.

## Quotation immutability audit

No actual sourced quotation was changed in this subagent diff. `LOADING_TIP_17` is restored to the Henry Adams source wording by the parent, and the file has no remaining diff. Other attributed loading-tip quotations were left untouched. The changed event and GUI strings contain no attributed or source-quoted wording.

## Validation

Meaningful checks completed: scoped event and common-file localisation reference scans, exact-case and case-insensitive duplicate scans, BOM and control-character checks, and a final search showing zero em dash, ellipsis, and mojibake matches in the assigned files. The only remaining semicolon is the immutable semicolon in the Henry Adams source quotation at `LOADING_TIP_17`.

Skipped: Hearts of Iron IV was not launched, and no live GUI or in-game localisation rendering was performed, in accordance with repository instructions.

## Unresolved wording decisions

- Historical and fictional event content with sensitive themes was kept semantically tied to its existing event mechanics. The parent should review tone before release.
- The `ZIN` and `zin` collision remains unresolved.
- Orphan event 79, event 80, and unknown event 100 keys remain unfilled because no caller or lore source was available.
- Existing blank description keys remain queued for event-owner review.

No plan handoff beyond this localisation handoff was written.
