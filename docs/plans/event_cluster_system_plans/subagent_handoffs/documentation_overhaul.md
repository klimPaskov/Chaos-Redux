# Dynamic Severity-Aware Cluster Overhaul Documentation Handoff

## Scope and status

This handoff records the documentation reconciliation for the user-approved Dynamic Severity-Aware Cluster Overhaul.

The documentation pass was limited to the event-system Markdown files named by the parent and this handoff file.

No gameplay, UI, localisation, spreadsheet, CSV, skill, generated-agent, binary, or asset file was edited.

No Git commit was created, as requested.

The documentation now describes the accepted system contract rather than an implementation-history prompt.

The documentation does not claim gameplay completion or engine validation.

## Source-of-truth map

| Surface | Current documentation authority | Boundary |
| --- | --- | --- |
| Accepted cluster design | `docs/systems/event_system/event_clusters_spec.md` | Exact eligibility, severity, formulas, ordering, state, history, UI, acceptance, and external-validation contract. |
| Runtime-facing cluster reference | `docs/systems/event_system/event_clusters.md` | Registry rows, runtime flow, formulas, dispatch, pacing, history, and presentation summary. |
| Event Chaos Levels | `docs/systems/event_system/event_chaos_levels.md` | Independent six-tier event property and its relationship to cluster member severity. |
| Shared Event Logs window | `docs/systems/event_system/events_log_window.md` | Tabs, catalogue/history behavior, current and historical cluster details, arrays, and data ownership. |
| Evolutions and cluster details | `docs/systems/event_system/events_log_evolutions_and_clusters.md` | Cross-tab cluster detail, filtering, sorting, snapshot behavior, and evolution/world-end boundaries. |
| Pacing and major-event weights | `docs/systems/event_system/dynamic_major_event_weights.md` | One pacing/cooldown update per successful cluster and automatic-memory boundaries. |
| Event-system navigation | `docs/systems/event_system/README.md` | Links and document roles for the event-system documentation set. |
| Runtime source evidence | `common/script_constants/event_cluster_constants.txt` and `common/scripted_effects/chaosx_event_cluster_effects.txt` | Parent-owned implementation evidence only; these files were read but not edited by this subagent. |
| Workbook contract | `docs/spreadsheets/chaos_redux_events_catalog.xlsx` | Workbook schema and formula prose remain unchanged and are outside this subagent's scope. |

The accepted contract is authoritative for intended behavior, while current gameplay source remains evidence that the parent must reconcile before claiming implementation completion.

## Required contract coverage

The reconciled documents cover ordinary event-system eligibility as the authority for automatic triggers, manual triggers, required rows, optional rows, and delayed dispatch.

They state that cluster logic can only narrow eligibility, that required means 100 percent after eligibility, and that required status never bypasses event fireability.

They state that a selected trigger rejected by the event system does not roll its cluster and continues through ordinary standalone handling.

They state that manual cluster forcing may bypass only cluster-specific gates and cannot dispatch a trigger or member rejected by the equivalent event-system force context.

They preserve Event Chaos Levels as independent and unchanged, while adding the separate Low T0, Medium T1, High T2, and Severe T3 cluster-member floors.

They state effective minimum as the maximum of the severity floor and declared member minimum.

They state the High and Severe two-pass support rule, including trigger and sole-configured-member exemptions.

They include the activation bases, severity factors, eligible-count factors, fatigue factor, previous-participation factor, 1 through 90 clamp, and exact activation formula.

They define the previous optional ratio from actually dispatched eligible optional rows in the last completed automatic batch and exclude trigger and required rows.

They include the full optional participation matrix, 0.95 accepted-row decay, 1 through 100 clamp, guaranteed trigger/required ordering, and Low-to-Severe optional ordering with random order within severity.

They document stable logical row IDs, explicit primary trigger rows for duplicate Events 6, 9, and 13, batch identity, queued context, delayed fireability rechecks, skipped invalidation, overlap isolation, and versioned non-destructive state.

They document one pacing/cooldown update per successful cluster, automatic fatigue and participation-memory boundaries, manual automatic-memory isolation, and successful-history-only recording.

They document activation and member history snapshots, including chance, roll, role, severity, effective minimum, status, canonical reason, trigger, batch, and valid context fields.

They document Guaranteed, N/A, Manual, and no-roll representations and prohibit recomputation of historical values.

They document the Event Logs and Settings copy Varies by member, duplicate staged-ID copy Varies by row, current unique trigger-specific chance, By Roll automatic-pool-weighted mean, By Unlock Tier, By Member Count, and N/A behavior.

They record the severity corrections Fury as Medium, Tensions Rising as Low, and Black Plague as Severe.

They state that workbook schema and formula prose remain unchanged and that no new visual assets are required.

They record the exact HOI4 MCP limitation: the probability, event, and GUI routes fail with `ARTIFACT_MANIFEST_INTEGRITY_FAILED` because `Artifact provenance manifest does not match its immutable address`.

## Unresolved plan and handoff disposition

| Item | Disposition | Evidence or reason |
| --- | --- | --- |
| `docs/systems/event_system/event_clusters_spec.md` | Promoted to accepted source contract | The former imperative specification was replaced with the current contract, formulas, state rules, UI rules, acceptance scenarios, and validation limitation. |
| Existing scoped plans under `docs/plans/event_cluster_system_plans/` | None found before this pass | No pre-existing scoped plan or addendum was available to mark implemented, queued, rejected, or superseded. |
| This documentation handoff | Created | Records the documentation state, contradictions, validation, and parent-owned risks. |
| Parent-owned gameplay implementation | Queued for parent reconciliation | Documentation describes the approved contract, but this subagent did not edit gameplay files or claim implementation completion. |
| Event catalog workbook update | Unchanged and out of scope | The approved contract explicitly leaves workbook schema and formula prose unchanged. |
| New visual assets | Not required | Existing Event Logs and Settings surfaces are sufficient for the documented contract. |
| External MCP evidence | Blocked | The required routes fail with the exact artifact-manifest integrity error recorded above. |

No scoped plan was silently marked implemented, rejected, or superseded without a named source file.

## Contradictions found and resolved

| Previous claim or omission | Documentation surface | Resolution |
| --- | --- | --- |
| The cluster layer was described as a post-selection fixed-roll layer with broad bypass behavior. | `event_clusters_spec.md`, `event_clusters.md`, `event_chaos_levels.md` | Rewritten to make ordinary event-system eligibility authoritative, cluster narrowing explicit, trigger rejection standalone, and manual forcing limited to cluster-only gates. |
| Cluster member severity and Event Chaos Level were not separated. | `event_clusters_spec.md`, `event_clusters.md`, `event_chaos_levels.md` | Added the independent severity floor, effective minimum, two-pass support rule, and corrected member severities. |
| Fixed cluster/member participation behavior lacked the approved activation and decay formulas. | `event_clusters_spec.md`, `event_clusters.md`, `events_log_window.md`, `events_log_evolutions_and_clusters.md` | Replaced the fixed behavior with the exact tier bases, factors, clamps, matrix, ordering, and accepted-row decay. |
| Duplicate event IDs did not have a stable row identity or explicit opening trigger semantics. | `event_clusters_spec.md`, `event_clusters.md`, `events_log_window.md`, `events_log_evolutions_and_clusters.md` | Added stable logical row IDs, explicit primary trigger rows for Events 6, 9, and 13, and batch-bound queued context. |
| Pacing text did not distinguish successful activation, failed roll, gated attempt, preflight failure, and manual memory. | `dynamic_major_event_weights.md`, `event_clusters_spec.md`, `event_clusters.md` | Added one-update success behavior and unchanged-memory boundaries. |
| Event Logs text omitted row-level chance, severity, role, effective minimum, availability, status, reason, batch, and live/history distinctions. | `events_log_window.md`, `events_log_evolutions_and_clusters.md`, `event_clusters.md` | Added the complete current and historical detail contract, including N/A, Guaranteed, Manual, Varies by member, and Varies by row. |
| Cluster catalogue sorting omitted By Unlock Tier and By Member Count and did not define By Roll. | `event_clusters_spec.md`, `event_clusters.md`, `events_log_window.md`, `events_log_evolutions_and_clusters.md` | Added the two modes and the live automatic-pool-weighted mean over distinct eligible trigger events. |
| Event Chaos documentation treated manual cluster forcing as a separate broad bypass. | `event_chaos_levels.md` | Replaced the wording with the equivalent event-system force-context constraint. |

## Open contradictions and source gaps for the parent

These are implementation evidence items, not documentation decisions.

At the time of this pass, `record_events_log_cluster_entry` in `common/scripted_effects/chaosx_event_cluster_effects.txt` visibly appended the legacy member snapshot arrays while newer cluster-detail arrays for row, role, severity, effective-minimum, chance, roll, and trigger were being cleared but not appended by that recorder.

The parent should verify that every successful history row appends all required snapshot fields and that the detail view reads aligned arrays without reconstructing historical values.

At the time of this pass, `try_fire_event_cluster_for_selected_event` still visibly called the legacy `get_event_cluster_roll_chance` path in the inspected source region.

The parent should verify that the approved activation formula and automatic-memory updates are the path used by automatic cluster activation, while manual forcing remains roll-free and memory-isolated.

At the time of this pass, the inspected source bounded `cycle_events_log_cluster_sort_mode_prev` and `cycle_events_log_cluster_sort_mode_next` to sort modes 0 through 3, and the catalogue rebuild likewise validated a maximum of 3.

The parent should verify that By Unlock Tier and By Member Count are wired through constants, cycling, bounds, metric selection, stable tie handling, localisation, and GUI display.

The current source snapshot did contain the corrected member severities for Fury, Tensions Rising, and Black Plague when inspected after the documentation edits.

The source snapshot also contained the new probability-memory and pending-context array declarations, but declaration or clearing alone is not evidence that all append, migration, delayed-recheck, and historical-display paths are complete.

The external MCP limitation remains open and prevents engine-backed probability, event, or GUI evidence.

## Duplicate, superseded, or historical documents

No file was deleted.

The former prompt-like role of `event_clusters_spec.md` was superseded in place by the accepted contract so existing links remain valid.

`event_clusters_spec.md` and `event_clusters.md` intentionally retain overlapping terminology but have distinct authority boundaries, with the former holding exact acceptance rules and the latter holding the implementation-facing summary.

No accidental duplicate current-state cluster document remained in `docs/systems/event_system/` after the README and cross-document references were aligned.

Historical subagent handoffs outside the allowed scope were not edited and are not current source-of-truth documents.

In particular, `docs/plans/player_facing_text_style_cleanup/subagent_handoffs/systems_player_facing_copyedit_handoff.md` may still mention an earlier source-role conflict, but it was outside the permitted documentation scope and remains historical evidence only.

## Stale prompts and instructions

The stale imperative cluster prompt previously occupying `event_clusters_spec.md` was removed by promotion to the current contract.

Targeted event-system documents no longer retain the old fixed cluster roll, fixed participation, broad manual bypass, or per-member pacing wording.

The outside-scope player-facing-copyedit handoff named above was left unchanged and must not be treated as current cluster guidance.

Implementation comments or source-side legacy helper names remain parent-owned source evidence and were not changed by this documentation pass.

## Markdown hard-wrap audit

The seven modified event-system documents were rewritten or patched so prose sentences remain on one physical line.

The same parser was also run over every Markdown file in docs/systems/event_system, and it found no accidental mid-sentence or mid-clause hard wrap.

Headings, list items, table rows, indented formulas, and deliberate structure were preserved.

No accidental mid-sentence or mid-clause hard-wrap issue was found in the modified documentation surfaces after the rewrite.

The new handoff likewise keeps each prose sentence on one physical line.

## Documentation completion checklist

- [x] Accepted source contract records ordinary event-system authority and cluster-only narrowing.
- [x] Required, optional, trigger, delayed, manual, and standalone behavior is documented.
- [x] Event Chaos independence, severity floors, effective minimum, corrections, and two-pass support are documented.
- [x] Activation bases, factors, fatigue, previous participation, rounding, and clamps are documented.
- [x] Optional matrix, accepted-row decay, dispatch ordering, and guaranteed rows are documented.
- [x] Stable row IDs, duplicate primary triggers, batch state, delayed invalidation, overlap isolation, and versioning are documented.
- [x] Pacing, cooldown, automatic memory, manual isolation, and successful-history-only behavior are documented.
- [x] Current and historical snapshot fields and canonical status/reason behavior are documented.
- [x] Event Logs, Settings, catalogue, sort modes, By Roll, N/A, and existing-asset behavior are documented.
- [x] Workbook schema and formula prose are explicitly unchanged.
- [x] The MCP artifact-manifest limitation is recorded without claiming engine evidence.
- [ ] Parent verifies gameplay implementation against the accepted contract.
- [ ] Parent completes the required source and in-game validation owned outside this documentation scope.

## Changed documentation files

- `docs/systems/event_system/README.md`
- `docs/systems/event_system/dynamic_major_event_weights.md`
- `docs/systems/event_system/event_chaos_levels.md`
- `docs/systems/event_system/event_clusters.md`
- `docs/systems/event_system/event_clusters_spec.md`
- `docs/systems/event_system/events_log_evolutions_and_clusters.md`
- `docs/systems/event_system/events_log_window.md`
- `docs/plans/event_cluster_system_plans/subagent_handoffs/documentation_overhaul.md`

## Files deliberately left unchanged

The following same-folder documents were inspected through targeted cluster searches and did not contain fixed cluster behavior requiring reconciliation:

- `docs/systems/event_system/crisis_rescue.md`
- `docs/systems/event_system/events_log_world_end_scenarios.md`
- `docs/systems/event_system/triggerable_scenarios.md`

The event catalog workbook, CSV exports, gameplay files, UI files, localisation files, skills, and generated agent definitions were not touched.

## Validation performed

Targeted `rg` searches confirmed that the only same-folder documents containing cluster behavior after the pass are the seven reconciled event-system documents listed above.

Targeted searches confirmed the required phrases and values for Varies by member, Varies by row, By Unlock Tier, By Member Count, Fury Medium, Tensions Rising Low, Black Plague Severe, the activation/participation tables, and the MCP failure string.

Targeted searches found no remaining same-folder wording for the old fixed cluster/member participation model, broad event-system bypass, or per-member cooldown update.

The source review confirmed the currently declared stable row IDs, severity floors, participation matrix, activation factors, probability bounds, result statuses, and pending/history array names without changing those source files.

The offline Paradox wiki core pages and relevant vanilla documentation pages were consulted before reconciliation as required by the repository instructions.

The baseline `hoi4.probability_inspect` adapter-list call returned `PROBABILITY_ADAPTERS_LISTED` with 11 adapters but no candidate-specific artifacts or source analysis.

The surface-specific `hoi4.probability_inspect` call for `common/scripted_effects/chaosx_event_cluster_effects.txt` with the `custom_weighted_pool` adapter failed with `ARTIFACT_MANIFEST_INTEGRITY_FAILED` and the immutable-address provenance message.

The read-only `hoi4.event_inspect` scan failed with the same artifact-manifest error.

The read-only `hoi4.gui_inspect` call for `events_log_popup_window` under scenario `event_log_shared_architecture_baseline` failed with the same artifact-manifest error.

No surface-specific HOI4 MCP probability, event, or GUI evidence was therefore accepted.

No resume packet was created because this handoff is the only additional file permitted by the parent and already contains the current-state ledger needed for continuation.

## Recommended parent decisions

1. Confirm that the source activation path has replaced the legacy roll helper with the approved severity-aware formula and automatic-memory transitions.

2. Confirm that successful history insertion appends every documented immutable activation and member snapshot field, including logical row ID, role, severity, effective minimum, starting/final chance, roll, status, canonical reason, trigger, batch, and history sequence.

3. Confirm that catalogue rebuild, sort cycling, scripted localisation, and GUI labels implement By Unlock Tier, By Member Count, and the live distinct-trigger weighted By Roll mean.

4. Resolve any source/spec mismatch before marking the cluster overhaul complete, and retain the exact MCP limitation in the final report.

## Proposed cleanup if patching is not allowed

If a later integration boundary prevents source-side fixes, retain this handoff and add a parent-owned implementation blocker under the open contradictions section rather than weakening the accepted contract or deleting historical documents.

If a later source review changes an accepted behavior, update `event_clusters_spec.md` first, then reconcile the implementation-facing and Event Logs documents, and record the decision in a new parent-owned handoff.

## Parent handoff

Documentation reconciliation is complete within the granted scope.

The parent may use `docs/systems/event_system/event_clusters_spec.md` as the accepted contract and this file as the current documentation ledger.

Gameplay implementation, engine validation, source-side wiring, and completion claims remain parent-owned and unresolved where listed above.
