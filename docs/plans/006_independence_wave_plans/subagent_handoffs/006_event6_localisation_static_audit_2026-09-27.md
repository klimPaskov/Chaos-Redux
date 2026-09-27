# Event 006 repository-wide static localisation audit (2026-09-27)

## Evidence and disposition

The authoritative audit result supplied for this documentation update was executed after the Statehood Ledger network-band source change: `python .tools/audit_localisation_static.py`.
The scan covered 336 localization files and 72,505 definitions, with 0 parse errors, 0 duplicate keys, 0 missing BOMs, 0 missing `l_english` headers, 0 encoding artifacts, 0 undefined event roots, and 0 missing event title/description keys.
The machine-readable findings were filtered for sources or keys containing `006_independence_wave`, `independence_wave`, or `chaosx.nr6`; there were 0 Event 006-specific entries in `missing_prefixed`, `missing_event_roots`, `missing_event_content`, or `exposed_flags`.

The complete repository scan reported 262 undefined key bindings in `missing_prefixed` and one displayed requirement flag in `exposed_flags`: `camp_admin_rows_initialized` at `common/scripted_triggers/camp_administration_triggers.txt:51`.
Those findings are outside Event 006 paths; this audit does not establish when they arose or authorize a Camp Administration change.
The scan also reported 22,920 dead-key candidates; this conservative repository-wide result is not an Event 006 deletion instruction.

Disposition: the Event 006-specific static localisation findings are clear for the named filters, while the repository-wide findings above remain recorded without attribution to Event 006.
This is evidence about current source only and does not establish runtime behavior, package admission, or whole-event completion.
Event 006 remains **HOLD / PARTIAL** at 32 content-attested selectable packages, 29 compatible reservation groups, 41 runtime adapters, and 161 unattested selectable non-overlay rows.
No localisation source was changed.

## Documentation reconciliation

- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`: the current authority and IW-039 continuation text distinguish the Event 006 filter from repository-wide findings; dated historical snapshots remain unchanged.
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`: the current continuation text makes the same distinction; dated historical check summaries remain unchanged.
- This handoff records the supplied audit command, counts, scope, and remaining repository-wide findings.
