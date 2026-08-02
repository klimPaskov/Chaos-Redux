# Event 020 documentation reconciliation handoff

Date: 2026-08-02

## Scope

This documentation-only pass reconciles the accepted `2026-07-29_two_rat_tags.md` correction with current Event 020 specs, matrices, reviews, prompts, event-system documentation, and the live registry evidence.

No gameplay, localisation, GUI, GFX, audio, image, model, asset, spreadsheet, or export-only CSV file was edited.

No Git commit was created because the parent explicitly requested no commit.

## Source-of-truth map

| Surface | Current source | Disposition |
| --- | --- | --- |
| Rat country identity | `docs/specs/020_black_plague_specs/corrections/2026-07-29_two_rat_tags.md` and `docs/specs/020_black_plague_specs/README.md` | Accepted source. Exactly two tags are allowed: reusable `RTA` carrier and separate `RTX` Rat King. Additional broods are internal RTA state markers, basin variables, strength pools, and army allocations. |
| Triggerable scenario contract | `docs/specs/020_black_plague_specs/specs/020_black_plague_spec_part_9_triggerable_scenario.md` and `docs/specs/020_black_plague_specs/matrices/triggerable_scenario_matrix.md` | Accepted source. `SCN-012` directly seeds the disease, forces Evolutions I through IV, creates or reuses RTA internal broods, creates or preserves RTX, and never scales country-tag count. |
| Current scenario-system summary | `docs/systems/triggerable_scenarios.md` | Updated to describe the reusable RTA carrier, internal brood markers, and separate RTX. |
| Event and cluster IDs | `common/script_constants/020_black_plague_constants.txt`, `common/script_constants/event_cluster_constants.txt`, and `docs/specs/020_black_plague_specs/matrices/event_chain_map.md` | Static evidence resolves the Diseases cluster to `8`, the scenario to `SCN-012`, and the launch report to `chaosx.nr20.90`. The matrix no longer instructs implementers to allocate new IDs. |
| Catalog wording contract | `docs/specs/020_black_plague_specs/matrices/catalog_update_draft.md` | Updated from proposed rows to live Event 20, Diseases cluster `8`, and SCN-012 wording with user-owned `Needs Testing` status. |
| Runtime-facing event overview | `docs/events/020_black_plague/overview.md` | Left unchanged in this pass because it already records cluster `8`, SCN-012, and the RTA/RTX two-tag contract. Parent worktree edits were preserved. |

## Files changed

- `docs/systems/triggerable_scenarios.md`
- `docs/specs/020_black_plague_specs/matrices/catalog_update_draft.md`
- `docs/specs/020_black_plague_specs/matrices/country_package_matrix.md`
- `docs/specs/020_black_plague_specs/matrices/event_chain_map.md`
- `docs/specs/020_black_plague_specs/matrices/evolution_matrix.md`
- `docs/specs/020_black_plague_specs/matrices/implementation_acceptance_checklist.md`
- `docs/specs/020_black_plague_specs/prompts/black_plague_asset_prompt.md`
- `docs/specs/020_black_plague_specs/research/source_read_ledger.md`
- `docs/specs/020_black_plague_specs/review/improvement_loop_review.md`
- `docs/specs/020_black_plague_specs/review/package_validation.md`
- `docs/specs/020_black_plague_specs/specs/020_black_plague_spec_part_1_core_crisis.md`
- `docs/specs/020_black_plague_specs/specs/020_black_plague_spec_part_5_rat_nations.md`
- `docs/specs/020_black_plague_specs/specs/020_black_plague_spec_part_9_triggerable_scenario.md`
- `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-02_event20_documentation_reconciliation_handoff.md`

## Disposition table

| Document group | Disposition |
| --- | --- |
| Event 020 accepted specs and matrices listed above | Promoted current two-tag and live-ID wording in place. |
| `docs/specs/020_black_plague_specs/prompts/black_plague_asset_prompt.md` | Updated the flag section from a 12-tag pool to the reusable RTA carrier family plus the existing RTX section. |
| `docs/specs/020_black_plague_specs/review/improvement_loop_review.md` | Retained as historical review provenance with an explicit superseded notice and corrected summary language. |
| `docs/specs/020_black_plague_specs/review/package_validation.md` | Retained as historical archive validation with an explicit notice and current static-ID wording. |
| `docs/specs/020_black_plague_specs/research/source_read_ledger.md` | Retained unchanged in substance as provenance, with an explicit notice that its proposed IDs are pre-live and superseded. |
| 2024-07-24 country-package and asset handoffs | Left unchanged because they already carry explicit superseded notices and preserve retired RTB-RTM evidence. |
| `docs/events/020_black_plague/overview.md` | Left unchanged because it already matches the two-tag, cluster-8, and SCN-012 contract and contains parent worktree edits. |
| Workbook and CSV exports | Left unchanged. Spreadsheet ownership remains with the parent and `chaosx_spreadsheet_doc_worker`. |

## Contradictions resolved

- `docs/systems/triggerable_scenarios.md` no longer says SCN-012 creates independent Rat Nation countries. It now describes one reusable RTA carrier with internal brood markers plus RTX.
- `country_package_matrix.md` and `implementation_acceptance_checklist.md` no longer define a finite multi-tag pool or several independent Rat Nation tags. They require exactly RTA and RTX.
- `event_chain_map.md` no longer describes `.40` and `.41` as allocating a new rat tag, and its namespace preamble no longer tells implementers to assign unresolved event IDs.
- `evolution_matrix.md` now names the RTA carrier and internal brood markers for Evolution III and the RTX tag for Evolution IV.
- `catalog_update_draft.md` now records live cluster and scenario rows rather than proposed rows and describes RTA/RTX identity accurately.
- Part 1 now records the live Diseases cluster ID `8` instead of the obsolete planning candidate `5`.
- Part 5 and Part 9 distinguish internal RTA broods from additional country tags while preserving coexistence with RTX.
- The asset prompt no longer requests twelve base Rat Nation flag designs.
- Historical review, archive-validation, and source-ledger docs now carry explicit notices where their old multi-tag or unresolved-ID wording remains for provenance.

## Unresolved plan and handoff disposition

| Item | Disposition | Reason or next owner |
| --- | --- | --- |
| 2026-07-24 RTB-RTM country and flag drafts | Superseded and archival | Existing handoffs now carry notices. Do not revive their tags or assets as runtime requirements. |
| 2026-07-29 two-tag correction | Accepted source | Parent implementation and all current docs should preserve RTA/RTX. |
| SCN-012 scenario package | Implemented static documentation evidence, live validation queued | Parent/user owns fresh-launch, active-crisis, save/reload, and rollback validation. |
| Diseases cluster `8` and SCN-012 registry IDs | Resolved statically | Do not allocate replacement IDs. |
| Current RTA internal brood count and state-marker behavior | Implemented in current runtime evidence | Parent owns gameplay completion and balance claims. |
| Remaining asset, focus, route-depth, native-mission, rights, and live-validation gaps | Queued in existing audits | This pass did not alter those implementation dispositions. |

## Stale prompt and instruction list

- `docs/specs/020_black_plague_specs/prompts/black_plague_coding_prompt.md` and `black_plague_goal_prompt.md` retain historical bodies with explicit 2026-08-01 superseded notices. Read the notice before using either prompt and do not follow their finite-pool or independent-Rat-Nation sentences.
- Older 2024 country-package and asset handoffs retain retired RTB-RTM identifiers for audit provenance and are explicitly superseded. They are not current production instructions.
- `docs/specs/020_black_plague_specs/research/source_read_ledger.md` still contains its original unavailable-environment and proposed-ID statements, but its new top notice makes that status explicit.

## Duplicate or superseded documents

- No document was deleted.
- The 2024 multi-carrier country and flag handoffs remain archival superseded records.
- No duplicate current Event 020 scenario or cluster contract was found after the targeted reconciliation.
- The catalog, event-chain, country-package, evolution, and acceptance matrices remain separate surfaces because each serves a distinct implementation or audit purpose.

## Contradictions still open

- The current implementation still has user-owned live validation and an explicitly documented SCN-012 late-failure rollback limitation. This pass does not claim atomic inverse rollback.
- Existing audit handoffs retain partial asset, focus-icon, route-depth, native-mission, rights, and live-consumer gaps. Those are gameplay or asset-owner decisions, not documentation conflicts resolved here.
- Some historical prompt bodies still mention obsolete pool language beneath their superseded notices. Rewriting those bodies would destroy audit provenance, so the parent should rely on the current source map and notices.

## Validation performed

- Read-only searches confirmed current Event 020 docs now reference `RTA`, `RTX`, cluster `8`, and `SCN-012` in the reconciled surfaces.
- Targeted searches confirmed `docs/systems/triggerable_scenarios.md` no longer contains the stale SCN-012 phrase `creates independent Rat Nations`.
- Targeted searches confirmed the current matrices no longer contain `finite tag pool`, `finite dormant pool`, `new rat tag`, or `planning allocations` in their active contract lines.
- Targeted searches verified the historical source ledger, review, and 2024 handoffs carry explicit historical or superseded labels where old claims remain.
- `git diff --stat` was reviewed for only the documentation surfaces listed above. No gameplay, asset, model, spreadsheet, or CSV path was touched by this pass.

## Skipped meaningful validation

- No HOI4 process, save, or live scenario launch was run because repository instructions assign live consumer validation to the parent and user.
- No workbook read or export was run because the event catalog workbook is owned by `chaosx_spreadsheet_doc_worker` and was outside this documentation scope.
- No binary asset inspection or model validation was run because this pass only reconciles text documentation.

## Recommended parent decisions

1. Treat `docs/specs/020_black_plague_specs/corrections/2026-07-29_two_rat_tags.md` and `README.md` as the only current identity authority, with this handoff as the reconciliation record.
2. Do not revive RTB-RTM tags, finite Rat Nation pools, or independent Rat Nation country language from historical prompts or audits.
3. Keep SCN-012 and cluster `8` stable while the parent completes live scenario and workbook validation.
4. Resolve the documented SCN-012 rollback limitation and remaining gameplay or asset audit gaps in their owning implementation passes, not by changing the two-tag documentation contract.

No resume packet was created because this handoff is the current Event 020 documentation state and the parent did not request a separate packet.
