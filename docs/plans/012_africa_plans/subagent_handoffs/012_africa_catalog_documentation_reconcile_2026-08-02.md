# Event 012 catalog documentation reconciliation handoff

Date: 2026-08-02.

Status: The bounded Event 012 catalog documentation cleanup is complete. The workbook and three export snapshots are clean and reconciled. This state does not prove Event 012 gameplay completion.

## Scope

This pass reconciled the named catalog merge handoff and the directly linked Event 012 release overview and completion audit. It did not edit the workbook, export CSVs, gameplay, localisation, assets, GFX, GUI, or unrelated Event 012 documents.

## Source-of-truth map

| Surface | Current authority | Evidence and boundary |
| --- | --- | --- |
| Accepted Event 012 design | `docs/specs/012_africa_specs/` | Defines intended mechanics and acceptance requirements. |
| Release-candidate status | `docs/events/012_africa/overview.md` | Records current implementation evidence and open gameplay, presentation, and live-consumer gates. |
| Catalog source | `docs/spreadsheets/chaos_redux_events_catalog.xlsx` | Editable source owned by `chaosx_spreadsheet_doc_worker`; current SHA256 is `4b6489d5582ed8be32e10db1d842b2449c49025e06544d386a6d42f1f72c9481`. |
| Catalog exports | `docs/spreadsheets/chaos_redux_events_catalog.csv`, `chaos_redux_clusters_catalog.csv`, and `chaos_redux_scenarios_catalog.csv` | Export-only snapshots with current SHA256 values recorded in the catalog merge handoff. |
| Catalog reconciliation evidence | `docs/plans/012_africa_plans/subagent_handoffs/012_africa_event_catalog_merge_2026-08-02.md` | Records Event 012 row identity, accepted gated World-End wording, `Needs Testing`, and current hashes. |
| Gameplay completion evidence | Current implementation files and dated audits | Evidence only. The catalog and clean worktree do not authorize a gameplay completion claim. |

## Plan and handoff disposition

| Document | Disposition | Result |
| --- | --- | --- |
| `subagent_handoffs/012_africa_event_catalog_merge_2026-08-02.md` | Updated | Replaced stale workbook and export hashes, removed the stale dirty-worktree statement, and clarified that catalog status does not prove gameplay completion. |
| `docs/events/012_africa/overview.md` | Updated | Records the clean workbook/export state and points to the current hash handoff while preserving the incomplete release boundary. |
| `subagent_handoffs/012_africa_final_completion_audit_2026-08-01.md` | Updated | Replaced catalog-specific promotion-pending wording with current clean-snapshot evidence while preserving the audit's incomplete verdict. |
| Other Event 012 specs, plans, manifests, prompts, and handoffs | Left unchanged | They remain dated evidence or accepted design material outside this narrow catalog cleanup. |

No document was deleted, merged destructively, promoted into a new source spec, rejected, or silently redesigned in this pass.

## Contradictions resolved

1. The catalog merge handoff now uses the current workbook SHA256 and all three current export SHA256 values instead of the stale snapshots.
2. The catalog merge handoff and linked completion audit no longer describe the `docs/spreadsheets` worktree as dirty or catalog promotion as pending.
3. The accepted Event 012 identity is stated consistently as Africa Is One, Minor Fire-Once, Severe member severity, cluster 6, with `Needs Testing` and the gated `The World Is One` World-End wording.
4. The overview, catalog handoff, and completion audit now state that clean workbook/export evidence is not gameplay completion evidence.

## Open contradictions and historical documents

Several older Event 012 completion and world-package audits retain their dated pre-reconciliation catalog claims. They were not directly linked to this catalog handoff and remain historical evidence rather than current status. The parent should not reuse their old `In progress`, blank World-End, dirty-worktree, or promotion-pending wording as the current catalog state.

The clean catalog still coexists with unresolved gameplay and presentation gates. No contradiction is implied between a clean catalog row and an incomplete Event 012 release candidate.

## Duplicate or superseded documents

The release overview remains the single current Event 012 status index. The three subsystem event documents remain separate authorities for mechanics and are not duplicates. The prior catalog merge wording is superseded in place by the updated handoff. No duplicate catalog source was created.

## Stale prompt or instruction list

No prompt file was in the direct cleanup scope. Older dated audit prose outside the changed files may still describe the former catalog state and should be treated as historical evidence.

## Parent decisions and remaining blockers

- Keep Event 012 status at `Needs Testing` until live gameplay and acceptance work closes the documented gates.
- Obtain authoritative W5 pre-install receipts before any world-package readiness claim.
- Complete terminal presentation and audio, unique model and external-package work, native-language review, and live-consumer acceptance before any completion claim.
- Preserve the clean workbook/export pair when future implementation facts change, then rerun the exporter through the spreadsheet owner workflow.

## Validation

- Reused the parent-provided successful `python -B .tools/export_event_catalog_csv.py` result and current hashes without opening or editing the workbook or CSVs in this documentation pass.
- Confirmed `git status -- docs/spreadsheets` is clean.
- Ran targeted searches over the changed Event 012 surfaces for the superseded workbook and export hashes and for the former catalog-state wording.
- Reviewed the final diff to confirm changes are documentation-only and limited to the three direct Event 012 surfaces plus this handoff.

Skipped meaningful validation: no gameplay parser, live-save, in-game, binary-art, or workbook round-trip test was run because those surfaces are outside this documentation scope and the parent supplied authoritative catalog/export evidence.

## Files changed

- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_event_catalog_merge_2026-08-02.md`
- `docs/events/012_africa/overview.md`
- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_final_completion_audit_2026-08-01.md`
- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_catalog_documentation_reconcile_2026-08-02.md`

No gameplay completion claim is made by this handoff.
