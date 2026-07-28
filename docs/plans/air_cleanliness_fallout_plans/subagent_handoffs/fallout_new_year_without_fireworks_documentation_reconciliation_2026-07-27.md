# The New Year Without Fireworks documentation reconciliation handoff

Status: current-reconciliation patch complete for the dormant The New Year Without Fireworks tranche. Gameplay completion and runtime acceptance are not claimed by this handoff.

## Scope

The reconciliation covers candidate `649`, events `649` through `655`, transaction `710064`, callback transaction `710164`, route `7164`, route upper bound `7165`, Event Log history `9170`, `64` ordinary rows, and `530` defined event blocks.

The reconciliation preserves the accepted dormant spec, both unset scheduler activation flags, the asset handoff state, the workbook ownership boundary, the read-only event-inspector limitation, and the explicit host-authority, save-recovery, delayed-delivery, multiplayer, Event Log, and player-visible runtime blockers.

## Source-of-truth map

| Surface | Path | Disposition | Evidence or boundary |
| --- | --- | --- | --- |
| Accepted design | `docs/specs/air_cleanliness_fallout_specs/specs/65_reviewed_regional_new_year_without_fireworks.md` | Accepted source design, unchanged | Defines the East Asia country-only identity, four branches, ledgers, receipts, asset contract, workbook source, and dormant runtime boundary. |
| Static implementation proof | `docs/plans/air_cleanliness_fallout_plans/FALLOUT_NEW_YEAR_WITHOUT_FIREWORKS_PROOF.md` | Updated with read-only tooling evidence | Records ids, branch grading, Event Log history `9170`, asset hashes, workbook and export references, and the unresolved `EVENT_INSPECTED_PARTIAL` result. |
| Current event id ledger | `docs/plans/air_cleanliness_fallout_plans/FALLOUT_EVENT_ID_LEDGER.md` | Current summary and New Year tranche reconciled | The header and latest tranche now report `64` rows, `530` blocks, candidate `649`, events `649` through `655`, transaction `710064`, route `7164`, and history `9170`. |
| Current scheduler proof | `docs/plans/air_cleanliness_fallout_plans/FALLOUT_EVENT_SCHEDULER_PROOF.md` | Current summary and New Year tranche reconciled | The current header, status, range, latest tranche, asset evidence, workbook evidence, and runtime blockers now include candidate `649`. |
| Implementation status README | `docs/plans/air_cleanliness_fallout_plans/README_IMPLEMENTATION_STATUS.md` | Current summary and New Year tranche reconciled | The latest tranche, scheduler foundation, current count, proof links, asset boundary, workbook row, and dormant blocker wording now include The New Year Without Fireworks. |
| Candidate pilot proof | `docs/plans/air_cleanliness_fallout_plans/FALLOUT_REVIEWED_CANDIDATE_PILOT_PROOF.md` | Current header, upper bound, constants count, and New Year tranche reconciled | The current header reports candidate `649`, route upper bound `7165`, `64` rows, and `530` blocks. The static evidence bullet reports `64` candidate ids, transaction keys, and route ids. |
| Source-of-truth map | `docs/plans/air_cleanliness_fallout_plans/source_of_truth_map.md` | New Year row added | The map now links Spec 65, the tranche proof, gameplay surfaces, constants, localisation, Event Log, asset manifest, `.gfx`, DDS, workbook, and exported row. |
| Asset manifest | `docs/assets/649_new_year_without_fireworks/manifest.md` | Parent registration reconciled | The manifest records source and runtime hashes and now records the static `.gfx` registration while keeping live presentation unproven. |
| Workbook source | `docs/spreadsheets/chaos_redux_events_catalog.xlsx` | Unchanged, spreadsheet-owned | The workbook remains the authoritative editable catalog source. Its exported row is checked without editing the workbook. |
| Workbook export evidence | `docs/spreadsheets/chaos_redux_events_catalog.csv:612` | Existing evidence checked | The `FALLOUT-649` row contains events `649` through `655`, transaction `710064`, route `7164`, history `9170`, dormant and runtime-blocker wording, and `Needs Testing` status. |

## Plan and handoff disposition

| Document or surface | Disposition | Reason |
| --- | --- | --- |
| Spec 65 | Accepted source design remains open | The spec deliberately does not claim gameplay or runtime acceptance. |
| `FALLOUT_NEW_YEAR_WITHOUT_FIREWORKS_PROOF.md` | Evidence retained and linked | Static evidence is complete enough for documentation reconciliation, while live validation and the event-inspector result remain unresolved. |
| `FALLOUT_EVENT_ID_LEDGER.md` | Current reconciliation implemented | The current header and latest tranche now carry the New Year identity and count. |
| `FALLOUT_EVENT_SCHEDULER_PROOF.md` | Current reconciliation implemented | The current scheduler summary and latest tranche now carry the New Year identity, asset and workbook evidence, and activation blockers. |
| `README_IMPLEMENTATION_STATUS.md` | Current reconciliation implemented | The status summary and scheduler foundation now carry the New Year identity, count, proof links, asset boundary, workbook row, and runtime blockers. |
| `FALLOUT_REVIEWED_CANDIDATE_PILOT_PROOF.md` | Current reconciliation implemented | The current candidate proof now carries candidate `649`, route upper bound `7165`, the `64`-row count, the `530`-block count, and the New Year tranche. |
| `source_of_truth_map.md` | Current map row added | The New Year sources are now navigable from the shared map. |
| Asset manifest and handoff | Left unchanged | The asset surface is outside this patch and remains `handed_off` pending parent-owned runtime review. |
| Workbook and export | Left unchanged | The workbook is owned by the spreadsheet worker. The existing export row is evidence only and no workbook update or export was performed. |
| New Year-specific addendum or prompt | Not found, no disposition needed | No separate tranche addendum or stale event-specific prompt exists under the targeted docs paths. |

## Contradictions resolved

- The current status, id ledger, scheduler proof, and candidate proof previously stopped at Mine Generator with `63` rows, `523` blocks, candidate `642`, route upper bound `7164`, and history `9169`. They now report The New Year Without Fireworks with `64` rows, `530` blocks, candidate `649`, route upper bound `7165`, and history `9170`.
- The current proof indexes previously omitted the New Year source, proof, asset, and workbook crosswalk. The four ledgers and shared source map now link those surfaces.
- The static proof lacked the supplied event-inspector limitation. It now records the partial artifact and the failed workspace-wide validation state without presenting it as a pass.

## Contradictions still open

- The asset manifest and `.gfx` registration now agree on static registration. Live presentation remains unproven.
- The workbook row now uses covered ceremonial banners and distinguishes branch and callback Event Log payloads from authenticated cleanup. The exporter was rerun from the workbook source.
- The read-only event-inspector response is workspace-wide rather than tranche-specific. It returned `EVENT_INSPECTED_PARTIAL`, `validation.passed=false`, `8939` events, `22905` issues, `6616` blocking diagnostics, and `MCP_INLINE_FILES_TRUNCATED` as the only listed diagnostic. This remains unresolved tooling evidence.

## Duplicate, superseded, and stale-document audit

- No duplicate New Year spec, proof, addendum, or prompt was found in the targeted docs paths.
- `FALLOUT_NEW_YEAR_WITHOUT_FIREWORKS_PROOF.md` is tranche evidence and does not supersede Spec 65.
- Historical Mine Generator and earlier count sections remain prior snapshots. They are not duplicate New Year documents and were not deleted.
- The temporary asset workspace remains active because the tranche is dormant and runtime acceptance is open. It must not be deleted until durable provenance and runtime wiring are reconciled by the parent.
- No New Year-specific prompt file was found. Generic source-index instructions remain unchanged.

## Recommended parent decisions

1. Ask the spreadsheet worker to reconcile the Military Ceremony workbook wording with Spec 65 and the player-facing localisation, then run the exporter if the workbook changes.
2. Decide whether the asset manifest should move from `handed_off` to a static-registration status while preserving the runtime presentation blocker.
3. Keep `fallout_event_scheduler_activation_approved` and `fallout_event_scheduler_active` unset until user-owned checks cover dispatch, delayed queue delivery, host authority, save recovery, multiplayer behavior, Event Log rendering, and player-visible art.
4. Treat the read-only event-inspector result as unresolved until the truncation condition is understood. Do not convert its artifact into a validation or completion claim.
5. Retain Spec 65 as the accepted source design unless the parent explicitly changes the design or runtime boundary.

## Files changed

- `docs/plans/air_cleanliness_fallout_plans/README_IMPLEMENTATION_STATUS.md` current header, scheduler foundation count, proof index, current count paragraph, and New Year tranche section.
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_EVENT_ID_LEDGER.md` current header and New Year tranche section.
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_EVENT_SCHEDULER_PROOF.md` current header, status, range, and New Year scheduler tranche section.
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_REVIEWED_CANDIDATE_PILOT_PROOF.md` current header, current candidate count, constants count, and New Year correction section.
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_NEW_YEAR_WITHOUT_FIREWORKS_PROOF.md` read-only event-inspector evidence section.
- `docs/plans/air_cleanliness_fallout_plans/source_of_truth_map.md` New Year source map row.
- `docs/plans/air_cleanliness_fallout_plans/subagent_handoffs/fallout_new_year_without_fireworks_documentation_reconciliation_2026-07-27.md` created as this handoff.

No spec, gameplay, localisation, interface, asset, or workbook source file was edited.

## Validation

- Targeted `rg` checks confirm the four current summaries carry candidate `649`, event range `649` through `655`, transaction `710064`, route `7164`, history `9170`, `64` rows, `530` blocks, and route upper bound `7165` where applicable.
- The candidate pilot constants block contains `64` candidate ids, `64` transaction keys, and `64` route ids.
- `interface/fallout_world_end.gfx:665-666` contains the static New Year sprite registration and points to the expected runtime DDS path.
- `docs/spreadsheets/chaos_redux_events_catalog.csv:612` contains `FALLOUT-649` and the requested ids, dormant wording, runtime blocker wording, and `Needs Testing` status.
- The tranche proof records the supplied `EVENT_INSPECTED_PARTIAL` artifact and `validation.passed=false` limitation.
- `git diff --check` was run on the documentation files changed by this reconciliation.

HOI4 was not launched. Workbook editing and exporter execution were skipped because the workbook is spreadsheet-worker-owned and this task forbids spreadsheet changes. Live dispatch, delayed delivery, save recovery, multiplayer behavior, Event Log rendering, and player-visible art remain unobserved.

## Resume packet

No separate resume packet was created. This handoff is the current resume state for candidate `649`.

## Remaining risks

The New Year Without Fireworks remains dormant and contributes zero release-floor credit. A later parent repair statically wired a generation-reset abort route from country runtime cleanup. Runtime execution, save recovery, the wider scheduler boundary, and the partial event-inspector result must remain explicit in any completion report.
