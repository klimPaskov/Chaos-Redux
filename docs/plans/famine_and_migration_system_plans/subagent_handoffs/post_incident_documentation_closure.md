# Post-Incident Documentation Closure Handoff

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

> **Superseded incident-layer banner (2026-08-25):** Any incident-event, event-option, `famine_incident.1`, or `migration_incident.1` wording in this historical handoff is superseded. Current register helpers are accounting/presentation seams only, and the incident event files and constants were deliberately deleted.

Date: 2026-08-25.

Status: bounded documentation closure applied for the post-incident consistency findings. This handoff does not claim gameplay completion and no gameplay, localisation, asset, GUI, map, event, decision, focus, country, or spreadsheet file was edited.

## Current authority

The accepted implementation is split into independent famine and migration mechanics with `famine_*` and `migration_*` runtime namespaces, separate `famine_decision_category` and `migration_decision_category` categories, and separate `famine_state_map_mode` and `migration_state_map_mode` mapmodes.

The incident notifications are triggered-only `famine_incident.1` and `migration_incident.1` transitions, not random-pool events or replacement Event149 identities.

The current status authorities are [source_of_truth_map.md](../source_of_truth_map.md), [completion_report.md](../completion_report.md), [famine_system.md](../../../systems/famine_system.md), [migration_system.md](../../../systems/migration_system.md), [ai_probability_current.md](../ai_probability_current.md), and [handoff_dispositions.md](../handoff_dispositions.md).

The current asset ledger retains 58 declared DDS outputs as 47 root assets, 7 report images, and 4 mapmode buttons, while the physical inventory is 61 because three wired category DDS files remain outside the declared manifests.

Event149 remains retired and unavailable with no replacement source ID, pool row, event-log identity, evolution, or pacing entry.

The feature remains incomplete because exact owner facts, weighted-logic dynamic-pool evidence, GUI/map runtime evidence, specialist reruns, and asset provenance/edge blockers remain open in the current authorities.

## Files changed

- `docs/specs/famine_and_migration_system_specs/README.md` now states that the accepted split design supersedes shared runtime wording while preserving the original package text below the notice.
- The five implementation prompts and eight specification parts under `docs/specs/famine_and_migration_system_specs/` now carry the same current-design clarification and current-authority links.
- `docs/plans/famine_and_migration_system_plans/resume_packet.md`, `improvement_review_addendum.md`, `repo_exploration.md`, and `ai_probability_baseline.md` now carry superseded historical-snapshot notices and current-authority links.
- `docs/plans/famine_and_migration_system_plans/subagent_handoffs/final_asset_audit.md`, `generated_event_art.md`, `icon_artist.md`, `decision_mission_final_audit.md`, `documentation_curator.md`, and `ai_probability_final_audit.md` now carry standalone superseded historical-snapshot notices and current-authority links.
- `docs/plans/famine_and_migration_system_plans/handoff_dispositions.md` now explicitly records the six stale standalone handoffs as superseded historical snapshots or as superseded by this closure, with current replacement authorities.
- `docs/plans/famine_and_migration_system_plans/subagent_handoffs/post_incident_documentation_closure.md` is this handoff.

## Dispositions

No historical specification text was merged, deleted, promoted, or silently rewritten.

The original shared-system design remains available as historical context, but the new notices make the accepted split implementation authoritative for current work.

The named resume, review, exploration, probability-baseline, and standalone handoff documents are retained as superseded historical evidence and must not be used to reopen shared identifiers, categories, counts, or implementation order.

No current blocker was closed by documentation wording.

## Contradictions resolved

- Direct reads of the spec package now encounter an explicit split-namespace, split-category, and split-mapmode boundary before the historical shared wording.
- The stale resume and planning documents now point to the current source map and completion report instead of acting as active continuation instructions.
- The stale standalone handoffs now identify their old combined paths, names, counts, and claims as historical snapshots.
- The handoff ledger no longer presents the six stale standalone handoffs as current namespace-updated evidence without an explicit superseded status.

## Contradictions still open

- The binding specification package still contains the original shared design text by deliberate preservation; a later parent-approved spec promotion or rewrite may be needed if the historical text remains too easy to misread.
- `ai_probability_current.md:24` and `completion_report.md:106` cite migration source hash `d1f041...`, while fresh inspection of `common/decisions/migration_decisions.txt` returned `9a5080...`; the current probability record needs a parent-owned artifact refresh after source freeze.
- The old asset matrix and historical asset handoff retain the former 58-file breakdown, while current authority records 58 declared outputs, 61 physical files, three files outside manifests, and provenance/edge blockers.

## Validation

- Targeted source and documentation scans confirmed that current runtime evidence contains no `famine_migration_*` or `fm_*` identifiers outside historical documentation references.
- The handoff directory contains 70 Markdown handoffs and the disposition ledger contains 70 handoff rows.
- The current authority documents retain separate categories/mapmodes, triggered-only incident events, Event149 retirement, the 58-versus-61 asset caveat, partial probability status, and GUI/map limitations.
- The new notices preserve paragraph structure and keep each inserted prose sentence on one physical line.

A comprehensive repository-wide Markdown hard-wrap scan and fresh MCP rerun were skipped because this was a bounded notice-only documentation patch and the parent supplied the current MCP evidence; existing historical formatting was not reflowed.

## Parent decisions and risks

The parent should refresh the migration probability artifact reference, decide whether to promote split wording into a new accepted spec revision, and reconcile the old asset matrix and historical asset handoff against the current 58-declared/61-physical inventory.

No gameplay completion, audit completion, asset closure, GUI/map runtime proof, or owner-fact resolution is claimed by this handoff.
