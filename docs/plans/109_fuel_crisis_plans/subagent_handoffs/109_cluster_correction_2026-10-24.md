# Event 109 Fuel Crisis identity and cluster correction

Disposition: Accepted and queued for implementation, based on the user's direct instruction of 24 October 2026. This correction documents cluster placement only and claims no runtime activation or gameplay completion.

## Accepted decision and source of truth

The user directed that Fuel Crisis “belong in the various anomalies cluster as severe member.” The accepted design assignment is Various Anomalies, cluster 11, Severe member. The user also directed that existing event eligibility remain unchanged. Cluster placement must not silently alter triggers, fire-once admission, event weights, or any other current eligibility rules.

The user also directed on 24 October 2026: “Adopt uploaded IDs and migrate the catalog.” Fuel Crisis uses accepted canonical Event 109; former catalog identity 114 is historical only. The identity decision is settled, while parent-owned workbook and shared-registry migration remains in progress. No catalog status is asserted. The supplied workspace status is design documents only, with no runtime definitions identified by the parent.

## Documents and dispositions

- `docs/specs/109_fuel_crisis_specs/README.md` now states the accepted cluster, basis, unresolved parent-owned identity migration, and absence of a runtime claim.
- `109_fuel_crisis_spec_part_1_core.md` carries cluster 11 Severe in its design identity table, with event eligibility unchanged.
- `109_fuel_crisis_spec_part_5_acceptance.md` adds an explicit cluster acceptance case.
- Coding and goal prompts carry the cluster assignment and instruct implementers to preserve existing eligibility without inferring catalog status.
- `109_fuel_crisis_implementation_handoff.md` replaces the unassigned-cluster and stale status narrative with the accepted assignment and parent-owned migration limits.
- `109_fuel_crisis_evidence_and_decisions.md` preserves the historical source/catalog observations as historical evidence and no longer presents them as current design/status authority.
- `109_fuel_crisis_review_and_validation.md` reflects the accepted cluster decision without claiming implementation.
- The remaining specification parts preserve existing mechanics and their prior acceptance basis. The current correction does not invent or deepen mechanics.

The ID decision is accepted; only the parent-owned migration operation remains to be completed. Fuel Crisis remains unimplemented according to the task input. The parent will update workbook membership and the shared registry; no workbook, registry, or runtime file changed here.

## Implementation acceptance cases

| Scenario | Required result |
| --- | --- |
| Shared Various Anomalies membership is registered | Fuel Crisis is a Severe member of cluster 11. |
| Existing event trigger and ordinary selection conditions are evaluated | Conditions remain as before the cluster change; no added eligibility gate, reroll, or event-weight change is introduced. |
| Event is activated through the accepted normal route | Existing admission and occurrence behavior remains authoritative; cluster membership does not itself constitute runtime activation. |
| Design identity is migrated from 109 against catalog identity 114 | Parent resolves all occupied IDs and references before workbook/registry/runtime writes; this handoff makes no migration choice. |

## Changed files and limits

Changed documentation: README, Part 1, Part 5, coding and goal prompts, evidence/decisions, review/validation, implementation handoff, and this current handoff under `docs/plans/109_fuel_crisis_plans/subagent_handoffs/`. Historical source observations were retained with their scope clarified. No gameplay, localization, workbook, registry, assets, or event runtime files changed.

No engine reference or runtime inspection was needed for this pure wording correction. Current implementation status comes from the parent task context, not a fresh repository scan. Parent integration, workbook migration, and runtime validation remain outside this subtask.

## Parent integration after catalog migration

The parent completed the authorized catalog and shared-registry migration on 24 October 2026.
The catalog has 155 unique event IDs and uses the canonical package identities 104 through 122, with all migrated events remaining Unavailable.
The final migration evidence supersedes this handoff’s earlier pending-migration observations, while preserving those observations as subtask history.
See the [current task report](../../repo_cleanup/planning_package_import_2026-10-24.md) for the original-row preservation, completed mappings and verification limits.
Runtime implementation remains outside this import task.
