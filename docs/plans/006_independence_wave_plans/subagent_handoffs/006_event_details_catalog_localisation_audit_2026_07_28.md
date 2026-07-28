# Event 006 latest tranche localisation and catalog audit

Date: 2026-07-28

Scope: Read-only audit of the latest Independence Wave crisis decision localisation, the expanded Event Details string, and Event 006 catalog wording. The audited source surfaces are `localisation/english/006_independence_wave_decisions_l_english.yml`, `localisation/english/chaosx_gui_l_english.yml`, `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, and their related scripted-localisation and exported catalog references. No gameplay, localisation source, workbook, or CSV file was edited.

## Result

HOLD for three small wording repairs and one catalog synchronization repair.

The crisis category, crisis decision title, crisis decision description, and custom-cost key all exist and resolve. The expanded Event Details key exists and its automatic-wave counts and crisis thresholds match the current constants and triggers. The Event 006 event row, cluster row, and evolution wording are aligned between the workbook and the GUI source.

The hold is caused by player-facing wording and catalog drift. The crisis description exposes the implementation term `shared allocator` and contains a semicolon. The crisis cost text says stability falls by `-5%` because it formats a signed negative constant after the phrase `falls by`. The expanded Event Details paragraph contains a semicolon. The workbook and exported CSV still say `Every researched Event 6 independence movement` in `SCN-008` scenario description cell `Scenarios!C9`, while the current source localisation already says `Every researched independence movement`.

## Missing key list

None found in the scoped crisis decision, decision category, Event Details, scripted-localisation, event-log, and catalog surfaces.

Direct crisis decision references resolve as follows: `independence_wave_open_host_crisis`, `independence_wave_open_host_crisis_desc`, and `independence_wave_cost_pre_wave_crisis` are present. The category key `independence_wave_crisis_category` and Event Details key `chaosx.events_log.window.event_details.independence_wave` are also present.

## Duplicate key list

None found in `localisation/english/006_independence_wave_decisions_l_english.yml` or `localisation/english/chaosx_gui_l_english.yml`.

The all-Event-006 scan covered 42 English localisation files, 6,094 keys, and found no duplicate keys or `:0` keys. The scoped shared-prefix collision scan also found no duplicate crisis or Event Details key.

## Scripted localisation issue list

No broken scripted-localisation reference was found. `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` references `chaosx.events_log.window.event_details.independence_wave`, and that key resolves.

The static Event Details paragraph is currently correct for the constants in `common/script_constants/006_independence_wave_constants.txt`: Calm World 6, Gathering Storm 8, Rising Chaos 10, Chaos Tier 14, Totalen Chaos 20, and World Collapse 20. The crisis thresholds are also accurate for the current triggers: resistance above 50 in a controlled state not owned by the host, or stability below 35 percent.

## Dynamic text opportunities

The Event Details counts and thresholds are hardcoded in one static paragraph. They are accurate now, but future tuning of the wave ladder or crisis thresholds could make this text stale. A dynamic scripted-localisation replacement is a non-blocking future opportunity and would require an explicit workbook contract update. It is not required for this tranche.

The crisis cost key should either format a positive display-magnitude constant or change its wording to `Stability changes by [?constant:independence_wave_crisis.stability_open_loss|%0].` The current signed value must not remain after `falls by`.

## Cross-surface mismatch notes

1. `localisation/english/006_independence_wave_decisions_l_english.yml:233`, key `independence_wave_open_host_crisis_desc`, says `the shared allocator may call a synchronized Independence Wave`. `shared allocator` is an implementation term that should not be shown to players. The same sentence uses a semicolon. Recommended wording is: `Occupied resistance and failing stability are making the old authority impossible to maintain. Commit the security service to a [?constant:independence_wave_crisis_timing.mission_days|0]-day emergency. If the country still cannot hold its ground when the mission ends, the synchronized Independence Wave may be called. An invalid or unavailable plan leaves the release blocked and preserves the host's last state.`

2. `localisation/english/006_independence_wave_decisions_l_english.yml:234`, key `independence_wave_cost_pre_wave_crisis`, says `Stability also falls by [?constant:independence_wave_crisis.stability_open_loss|%0].` The effect applies the negative constant `-0.05`, so the current tooltip can read `falls by -5%`. Correct the display value or use signed wording as described above.

3. `localisation/english/chaosx_gui_l_english.yml:953`, key `chaosx.events_log.window.event_details.independence_wave`, uses a semicolon after `20 in Totalen Chaos`. Replace it with a period so the sentence reads `20 in Totalen Chaos. World Collapse also releases 20 ...`.

4. `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, `Scenarios!C9`, and the export `docs/spreadsheets/chaos_redux_events_catalog.csv` still contain `Every researched Event 6 independence movement with a safe homeland ...`. The current source key `chaosx.scenarios.independence_wave.desc.sovereign_scatter` in `localisation/english/006_independence_wave_scenario_l_english.yml:14` already omits the implementation label. Update the workbook source cell to the exact current localisation wording, then run `python .tools/export_event_catalog_csv.py` from the mod root so both export CSVs are refreshed. The exporter was intentionally not run during this read-only audit.

5. The audited workbook Event 006 row and cluster row match the GUI and cluster localisation wording. Evolution title and body pairs in `Events!D7:H7` also match their source keys. No other audited content mismatch was found.

## File encoding concerns

All 42 `localisation/english/006*.yml` files are UTF-8 with BOM. The two directly audited localisation files are UTF-8 with BOM. No encoding concern was found.

The workbook contains no formulas, so no recalculation issue was found. The CSVs mirror the workbook as exported, including the stale `SCN-008` wording.

## Recommended fixes

1. In `localisation/english/006_independence_wave_decisions_l_english.yml`, revise `independence_wave_open_host_crisis_desc` to remove `shared allocator`, replace the semicolon, and use `unavailable plan` wording that describes the player-facing outcome.
2. In the same file, revise `independence_wave_cost_pre_wave_crisis` so the stability loss is displayed as a positive magnitude or described with signed `changes by` wording.
3. In `localisation/english/chaosx_gui_l_english.yml`, replace the Event Details semicolon after `Totalen Chaos` with a period.
4. Update workbook source cell `docs/spreadsheets/chaos_redux_events_catalog.xlsx:Scenarios!C9` to match `chaosx.scenarios.independence_wave.desc.sovereign_scatter`, then run `.tools/export_event_catalog_csv.py` to refresh `chaos_redux_events_catalog.csv` and the other export files.

## Patch and validation record

Changed files: this handoff only. No source localisation, gameplay, workbook, or CSV file was patched.

Changed keys: none.

Dynamic localisation added or fixed: none. The signed stability display issue is reported for the owning implementation pass.

Meaningful validation run: UTF-8 BOM and duplicate-key checks across all 42 Event 006 English localisation files, direct-reference coverage for the crisis decision and category, Event Details reference coverage through scripted localisation, exact Event Details count and threshold comparison against current constants and triggers, and read-only workbook-to-source comparison for the Event 006 row, cluster row, evolution fields, and SCN-008 scenario fields. The comparison found one mismatch in `Scenarios!C9`.

Skipped meaningful validation: no workbook write or CSV export was performed because this audit was explicitly read-only. No live game or GUI render was run because runtime validation belongs to the parent and user.

Unresolved wording decisions: choose whether to add a positive display-magnitude constant or use signed `changes by` wording for the stability cost. Decide whether the static Event Details counts should remain a catalog contract or move to dynamic scripted localisation in a later tranche.

Plan handoff path: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event_details_catalog_localisation_audit_2026_07_28.md`.

## Parent integration note - 2026-07-29

The three player-facing wording findings are resolved in the current source. The crisis description no longer exposes implementation terminology, the cost text uses signed `changes by` wording, and the Event Details paragraph uses sentence punctuation instead of a semicolon. The workbook `Scenarios!C9` and both exported catalog rows now use `Every researched independence movement with a safe homeland...`; `python .tools/export_event_catalog_csv.py` was run after the workbook source check. The remaining dynamic Event Details opportunity is non-blocking and remains a future tuning-synchronization improvement.
