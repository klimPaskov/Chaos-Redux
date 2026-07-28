# Event 006 post-9199b465b localisation and catalog re-audit

Date: 2026-07-28

Scope: Read-only re-audit of Event 006 after commit `9199b465b`, `event6 align catalog and event details wording`. The audit covers the crisis category, crisis mission title, crisis mission description, crisis cost text, expanded Independence Wave Event Details, Event 006 scripted-localisation references, the Event 006 workbook row, the Liberations cluster row, and `SCN-008` catalog text. Random Events, CBB, and CBD surfaces were excluded. The current working tree contains unrelated uncommitted additions in shared GUI and events-log files, which were not evaluated as gameplay changes. The parent closure patch subsequently changed only the Event 006 decision description and Event Details localisation keys documented below; no workbook or CSV row was changed.

## Result

PASS for the commit-specific punctuation, crisis wording, catalog synchronization, and failure-consequence disclosure repairs.

The crisis category now names both accepted resistance routes: an enemy-controlled owned state and a foreign-owned state under the host's control. The crisis mission description no longer exposes `shared allocator`, no longer uses a semicolon, and uses a dynamic 120-day duration. The cost text now says stability `changes by` the signed negative constant, so it no longer produces `falls by -5%`. The Event Details paragraph has sentence punctuation, lists the current 6, 8, 10, 14, and 20 automatic-wave counts, and names stability below 35%, enemy-controlled owned-state resistance above 50, and controlled foreign-owned-state resistance above 50.

The workbook and exports are synchronized. `Events!C7` matches the static Event Details paragraph, `Scenarios!C9` matches the current `Sovereign Scatter` source localisation without the implementation label `Event 6`, and the Event 006, cluster, and scenario CSV rows match their workbook rows exactly.

The parent closure patch now discloses the concrete cancellation and blocked-resolution consequences in the crisis mission description and Event Details string. Cancellation exposes the stability loss and cooldown; invalid or exhausted planning exposes the stability, war-support, resistance, cooldown, and ownership-preservation consequences through the centralized constants.

## Missing key list

None found.

The direct crisis decision references `independence_wave_open_host_crisis`, `independence_wave_open_host_crisis_desc`, and `independence_wave_cost_pre_wave_crisis`, and all three resolve. The category key `independence_wave_crisis_category`, Event Details key `chaosx.events_log.window.event_details.independence_wave`, crisis history description, and all five crisis cause keys resolve.

## Duplicate key list

None found across the 42 Event 006 English localisation files after excluding their shared `l_english` header. The scoped parser found 6,106 player-facing keys and no duplicate key.

No duplicate Event 006 `defined_text` name was present in the final audit snapshot. The Event 006-owned `GetIndependenceWaveCrisisHistoryCause` resolver in `common/scripted_localisation/006_independence_wave_crisis_localisation.txt:10` is the single definition and includes occupation, stability, combined, requester-lost, and unknown branches. A transient duplicate block appeared in an intermediate working-tree snapshot while the shared events-log file was being edited and disappeared before the final scan. Recheck that file before committing concurrent edits.

## Scripted localisation issue list

No broken scoped scripted-localisation reference was found. `GetIndependenceWaveCrisisHistoryCause` resolves all five cause keys. The shared events-log resolver maps the Event 006 crisis history description and Event Details key, and both rival-bloc Event Details functions referenced by the dynamic suffix are defined.

No scripted-localisation issue remains in the committed Event Details or catalog tranche. The transient duplicate `GetIndependenceWaveCrisisHistoryCause` observation is recorded above as a concurrent-edit risk.

## Dynamic text opportunities

The crisis mission duration is already dynamic through `independence_wave_crisis_timing.mission_days`. The cost resources and signed stability change are dynamic through the decision constants.

The phrase `bounded retry` is static even though the retry limit is a constant. A future wording pass could expose the retry limit dynamically, such as a limited number of daily retries, if the player-facing contract requires that precision.

The automatic-wave counts and crisis thresholds in Event Details are static and currently match the constants exactly. They remain a future synchronization risk if the ladder or thresholds change. Moving them to scripted localisation would require an explicit workbook contract update and is not required for this tranche.

## Cross-surface mismatch notes

1. `common/scripted_effects/006_independence_wave_crisis_effects.txt:156-163` cancels the mission when pressure disappears and applies the failure stability change of -10% plus cooldown. The parent closure patch discloses that consequence in `independence_wave_open_host_crisis_desc` and the Event Details string.

2. `common/scripted_effects/006_independence_wave_crisis_effects.txt:48-80` applies the blocked consequence after an invalid plan or exhausted retry. It changes stability by -10%, war support by +5%, and resistance by +5 in a qualifying pressure state, then applies cooldown without changing ownership. The parent closure patch discloses those outcomes through dynamic constant tokens in both player-facing surfaces.

3. The category, Event Details, and mission description now use explicit wording for enemy-controlled owned states and controlled foreign-owned states, so the accepted crisis routes are consistent across the player-facing surfaces.

4. No remaining Event Details punctuation issue was found. The target key contains no semicolon and no implementation label. The unrelated shared GUI file still contains semicolons in excluded Random Event text, which are outside this audit.

5. No Event 006 workbook or export mismatch remains. `Events!C7`, `Scenarios!C9`, and the corresponding CSV cells match their current localisation sources. The Event 006 cluster row and its CSV export also match.

## File encoding concerns

All 42 `localisation/english/006*.yml` files are UTF-8 with BOM. The directly audited decision, scenario, and shared GUI localisation files are also UTF-8 with BOM. No encoding concern was found.

The workbook contains no formulas. The workbook and exported CSV rows were read without recalculation or write operations.

## Follow-up notes

1. The connected mission and Event Details surfaces now describe cancellation and blocked-resolution consequences with dynamic constants; a future pass could expose the bounded retry limit itself if the player-facing contract requires that precision.
2. The mission description now names enemy-controlled owned states and controlled foreign-owned states explicitly.
3. Keep only the Event 006-owned `GetIndependenceWaveCrisisHistoryCause` definition and ensure concurrent edits to `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` do not reintroduce a duplicate name.
4. Preserve the current workbook source of truth and rerun `.tools/export_event_catalog_csv.py` after any future workbook wording change.

## Patch and validation record

Changed files in the parent closure patch: `localisation/english/006_independence_wave_decisions_l_english.yml` and the Event 006 line in `localisation/english/chaosx_gui_l_english.yml`. This handoff records the audit and its closure evidence; the workbook and CSV remain unchanged because their rows already matched.

Changed keys: `independence_wave_open_host_crisis_desc` and `chaosx.events_log.window.event_details.independence_wave`.

Dynamic localisation added or fixed: the two player-facing surfaces now expose the centralized crisis stability, cooldown, war-support, and resistance constants.

Meaningful validation run: BOM checks for all 42 Event 006 localisation files and directly audited shared GUI files, scoped duplicate-key parsing, direct crisis-decision reference coverage, five-branch crisis scripted-localisation coverage, Event Details dynamic-function reference coverage, punctuation and implementation-label checks, exact source-to-workbook comparison for Event Details and SCN-008, and exact workbook-to-CSV comparison for the Event 006, Liberations cluster, and SCN-008 rows.

Skipped meaningful validation: no workbook write or CSV export was run because the audit was read-only and the rows already matched. No live game or GUI render was run because runtime validation belongs to the parent and user. The shared events-log file was concurrently modified, so its final duplicate-definition check should be repeated immediately before the parent commit.

Unresolved wording decision: decide in a future pass whether the bounded retry limit itself belongs in the mission tooltip or Event Details surface; cancellation and blocked-resolution values are now disclosed.

Plan handoff path: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event_details_catalog_post_9199b465b_reaudit_2026_07_28.md`.
