# Final event-free famine and migration localisation audit

> **Superseded historical identifier banner (2026-08-25):** Any `famine_incident.1`, `migration_incident.1`, or incident-option identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities document accounting/presentation seams only and the deliberate deletion of the incident event files and constants.

Date: 2026-08-25

Status: the bounded localisation audit and safe tooltip patch are complete. Current MCP visual evidence remains blocked by tool timeouts and by the installed map route's lack of scripted-mapmode tooltip rendering.

## Scope and binding design

The audit covered the current English famine and migration localisation, decision and mission consumers, category visibility, scripted-localisation branches, the two scripted state mapmodes, report headers, achievements, and the shared Deaths reason labels.

No event, gameplay, asset, GUI, documentation source, workbook, or spreadsheet file was edited. The system remains event-free. No `famine_incident.1` or `migration_incident.1` event object or localisation key exists in the inspected runtime source.

The categories remain separate and independently gated by their own problem triggers. The famine category presents exactly Food Security, Food Reserves, and Relief Access as its three values. The migration category presents exactly Displacement Load, Reception Capacity, and Border Policy as its three values. The phase and current-priority lines are prose guidance rather than additional values.

The source defines exactly `famine_state_map_mode` and `migration_state_map_mode`. Neither definition has a problem-state visibility gate, and all four selected and deselected button sprites are wired, so the source supports start-of-game availability. Runtime button visibility remains part of the MCP blocker below.

## Changed files

- `localisation/english/chaosx_map_modes_l_english.yml`
- `docs/plans/famine_and_migration_system_plans/subagent_handoffs/final_event_free_localisation_audit.md`

The localisation file already contained concurrent work. This patch preserved it and changed only the keys listed below.

## Changed keys

Famine mapmode, 7 keys:

- `MAPMODE_FAMINE_STATE_MAP_MODE_DESCRIPTION`
- `famine_state_map_mode_detail_authorized`
- `famine_state_map_mode_blockade_not_proven`
- `famine_state_map_mode_relief_delivery_proven`
- `famine_state_map_mode_relief_route_proven`
- `famine_state_map_mode_relief_none`
- `famine_state_map_mode_stage_untracked`

Migration mapmode, 21 keys:

- `MAPMODE_MIGRATION_STATE_MAP_MODE_DESCRIPTION`
- `migration_state_map_mode_detail_authorized`
- `migration_state_map_mode_origin_recorded`
- `migration_state_map_mode_origin_unproven`
- `migration_state_map_mode_host_recorded`
- `migration_state_map_mode_host_unproven`
- `migration_state_map_mode_destination_recorded`
- `migration_state_map_mode_destination_unproven`
- `migration_state_map_mode_flight_share_recorded`
- `migration_state_map_mode_flight_share_none`
- `migration_state_map_mode_reception_share_recorded`
- `migration_state_map_mode_reception_share_none`
- `migration_state_map_mode_capacity_invalid`
- `migration_state_map_mode_identity_return_ambiguous`
- `migration_state_map_mode_identity_integration_owner`
- `migration_state_map_mode_identity_unresolved`
- `migration_state_map_mode_source_unknown`
- `migration_state_map_mode_corridor_generation_recorded`
- `migration_state_map_mode_corridor_generation_none`
- `migration_state_map_mode_cohort_exact`
- `migration_state_map_mode_cohort_none`

Total changed localisation keys: 28.

## Audit findings

### Missing key list

None.

- All 34 decision and mission entries have title and description keys.
- All 169 distinct famine and migration scripted-localisation branch keys resolve in English localisation.
- All eight famine and migration achievements have `_NAME`, `_DESC`, and `_tooltip` keys.
- Both required Deaths reasons resolve: `chaos_meter.deaths.cause.famine` and `chaos_meter.deaths.cause.forced_displacement`.

### Duplicate key list

None among the 381 English keys beginning with `famine_` or `migration_`, or the two relevant `MAPMODE_` families.

### Scripted localisation issue list

None found. Existing selector calls, variables, constants, state and country scope calls, formatting codes, and fallback branches remain intact.

### Dynamic text opportunities

No new selector was needed. The authorized tooltips already expose the relevant dynamic food stage, reserves, pressure components, deaths, movement roles, cause, route and corridor state, cohort state, state population, displacement, reception, border policy, integration, resettlement, and return values.

The patch grouped those existing values into readable sections. Every dynamic token present in the pre-patch values was preserved, including the corridor operation number.

### Cross-surface mismatch notes

No current English-localisation mismatch remains among category value names, mapmode summaries, achievements, or Deaths reasons.

The famine and migration categories use separate terminology throughout the assigned surface. No united category or combined mapmode localisation remains.

### File encoding concerns

None. All six inspected localisation files retain UTF-8 BOM: the two main system files, the two mission files, the mapmode file, and the shared Chaos Meter file. No `:0` key version appears in the assigned files.

### Prose-quality issues found and fixed

- Vagueness: `Conditions incomplete`, `No resolved driver`, and ledger-style unknown states were replaced with direct statements about blockade, cause, movement type, and cohort availability.
- Bloat: the famine authorized tooltip fell from 19 displayed source lines to 9, and the migration tooltip fell from 25 to 13, without removing causal values.
- Obvious explanation: repeated `recorded`, `proven`, and internal-state wording was removed where the visible status already conveys the fact.
- Repetition: origin, host, destination, route, corridor, population, and national values are grouped rather than introduced by a separate sentence on every line.
- Overcomplication: mapmode descriptions now explain fill and border meaning directly without narrating the full implementation taxonomy.
- Style-rule repair: no em dash, sentence semicolon, prompt fragment, event ID, implementation history, or tuning-history wording remains in the assigned files.

### Sourced-quotation preservation

No sourced or attributed quotation appears in the inspected famine, migration, mission, mapmode, achievement, report-header, or Deaths-reason localisation. No quotation was changed.

## Display before and after

Before, the authorized famine tooltip presented each value on its own line and used 19 lines. After, it uses compact Food Security and Pressure Sources sections across 9 source lines while retaining the score, pressure, exposure, reserves, need, delivery efficiency, blockade, relief, eight causal components, and deaths.

Before, the authorized migration tooltip used 25 lines and repeatedly described values as recorded projections. After, it groups movement identity, cause, route, corridor, cohort, state population movement, reception, return, and the three national category values across 13 source lines.

Before, several fallback labels described internal evidence state. After, they tell the player that the blockade, endpoint, share, capacity, movement type, cause, corridor operation, or single cohort is unavailable or unknown.

## Meaningful validation

- A source census found 34 decision and mission entries with zero missing title or description keys.
- A scripted-localisation census found 169 distinct famine and migration branch keys with zero missing English definitions.
- An English-localisation census found 381 relevant keys and zero duplicates.
- All eight achievement text triplets resolve.
- Repository searches found zero `famine_incident.1` or `migration_incident.1` localisation keys or event objects.
- The category descriptions contain exactly the three required value labels for their own mechanic.
- The two authorized mapmode tooltips retain all prior dynamic tokens. Their explicit line counts fell to 9 and 13.
- The inspected Deaths labels remain `From famine` and `From forced displacement`.

## MCP evidence and exact blockers

The current `hoi4.map_inspect` queries for `famine_state_map_mode` and `migration_state_map_mode` produced no result after more than 90 seconds and were terminated. No current artifact URI was returned.

The current `hoi4.gui_inspect` calls for `famine_report_header_window` and `migration_report_header_window` produced no result after more than 90 seconds and were terminated. The corresponding `hoi4.gui_render` calls for normal, long-text, and missing-localisation states at 1920x1080 and 1280x720 also produced no result after more than 60 seconds and were terminated. No current GUI artifact URI was returned.

The installed map route renders geographic substrate, not dynamic scripted-mapmode colours or delayed tooltip layout. Source review therefore does not prove mapmode tooltip wrapping, runtime colours, or button visibility. This is retained as an unresolved presentation-evidence blocker.

## Skipped meaningful validation

No live game test was run because live consumer validation belongs to the user. Current overflow, wrapping, mapmode button visibility, dynamic colour evaluation, and report-header rendering remain unproven because the required MCP calls timed out and the map renderer lacks scripted-mapmode tooltip execution.

## Unresolved wording decisions

None. The remaining uncertainty concerns visual execution, not the intended English wording.

## Simplifications, omissions, and blockers

No gameplay meaning, causal component, requirement, achievement condition, dynamic token, or sourced quotation was removed. No fallback category, shared GUI, combined terminology, or event surface was introduced.

The only blocker is the missing current MCP visual evidence described above. No commit was created because the parent owns final integration and the shared worktree contains concurrent changes.
