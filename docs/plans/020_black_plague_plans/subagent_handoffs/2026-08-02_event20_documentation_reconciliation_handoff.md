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

## Pass-3 reconciliation addendum (2026-08-02)

### Scope and boundary

This addendum reconciles the active Event 020 README, manifest, limitations, completion audit, source-of-truth disposition, Part 9 scenario spec and matrix, core-readiness report, runtime event docs, selected prompts, and stale historical handoffs against the parent-provided live facts.

No gameplay, localisation, GUI, GFX, audio, image, model, asset, spreadsheet, or export-only CSV file was edited.

The parent retains final runtime wiring, live-consumer validation, balance claims, workbook ownership, and the whole-spec completion claim.

### Current source-of-truth map

| Surface | Current authority and evidence | Disposition |
| --- | --- | --- |
| Rat identity | `docs/specs/020_black_plague_specs/corrections/2026-07-29_two_rat_tags.md`, `README.md`, and `docs/events/020_black_plague/overview.md` | Accepted invariant: exactly `RTA` reusable carrier and `RTX` Rat King; internal broods are RTA state markers, not country tags. |
| Focus counts | `docs/events/020_black_plague/overview.md`, core-readiness report, `rat_king_depth.md`, and the two focus source files | Current documented runtime counts are 51 RTA and 71 RTX nodes. The focus source files contain one tree-level `id` plus 50/70 focus blocks; the accepted count convention is retained without changing gameplay. |
| SCN-012 launch and repeat behavior | Part 9 spec, `matrices/triggerable_scenario_matrix.md`, `docs/events/020_black_plague/overview.md`, and the scenario content/runtime handoffs | Repeat-blocked planning rows are superseded. Successful repeats are reconciliation-only and idempotent; terminal or unavailable worlds remain blocked. The intensity postcondition reconciles live RTA/RTX division counters and verifies configured floors before success. |
| Last-response missions | `docs/events/020_black_plague/last_response_missions.md`, `shared_response.md`, and `common/decisions/020_black_plague_shared_response_decisions.txt` | Hold the Line and Secure the Refuge are native `activate_mission`/`days_mission_timeout` missions; live progress, timeout, and teardown checks remain open. |
| Weapon delivery icon | `docs/events/020_black_plague/overview.md`, `interface/020_black_plague_weaponization.gfx`, and `common/decisions/020_black_plague_weaponization_decisions.txt` | `GFX_decision_black_plague_weapon_delivery` is dedicated and wired; old Military Acceleration alias wording is historical only. |
| Source-frame presentation | `docs/assets/020_black_plague/rat_king_animation/manifest.md`, `royal_burrows_seal_animation/manifest.md`, and Event 020 GFX references | Rat King portrait and Royal Burrows seal packages are promoted with documented static fallbacks. Broader crisis, Doctor Wu, route, and aftermath presentation remains queued. |
| Audio | Readiness/limitations docs and `sound/020_black_plague/super_event_087_rat_king_defeat_aftermath.wav`, `super_event_101_rat_king_coronation.wav`, and `super_event_102_rat_king_world_end.wav` | Three Event 020 WAVs are 44.1 kHz stereo. Rights attribution and live playback remain open. |
| Model boundary | README, limitations, readiness, and runtime overview | No bespoke 3D models are required or planned; the registered infantry entity is the accepted Rat visual consumer. |

### Unresolved plan and handoff disposition

| Item | Disposition | Remaining owner or reason |
| --- | --- | --- |
| Two-tag correction | Accepted and promoted | Parent must preserve RTA/RTX and never revive RTB-RTM runtime tags. |
| SCN-012 repeat reconciliation and intensity postcondition | Implemented statically and promoted | Parent/user owns fresh launch, repeat, save/reload, and failure-retry validation; complete inverse rollback is not claimed. |
| Hold the Line and Secure the Refuge | Implemented statically as native missions | Parent/user owns live outcome, timeout, and teardown validation. |
| Crown Strike and Seal Royal Burrows mission API | Queued decision | They remain shared timed state actions until the parent decides whether native mission fields are required. |
| RTA/RTX focus routes | Implemented statically at documented 51/71 counts | Parent/user owns live timing, AI order, layout, and balance validation. |
| Weapon icon, Rat King portrait, Royal Burrows seal, and three WAVs | Promoted static evidence | Rights attribution and live playback/consumer validation remain open. |
| Broader crisis/Doctor Wu/route/aftermath art and narrative | Queued | Existing readiness and addendum plans remain the working queue. |
| Black fog | Optional engine-dependent enhancement with blocker rule | Black mapmode base remains mandatory; no safe clipping proof is documented. |
| Workbook/catalog and full balance validation | Left unchanged | Parent and spreadsheet worker own workbook/export and live balance evidence. |

### Contradictions reconciled

- The manifest's blanket no-implementation status now separates static runtime evidence from unrun live validation, with the historical integrity table explicitly marked as archival.
- README and limitations no longer say the source-frame Rat King/seal packages are unresolved; they now record those packages as promoted while retaining broader presentation blockers.
- The readiness report, event overview, Rat King route doc, and source-of-truth disposition now use 51 RTA and 71 RTX focus counts.
- The readiness report no longer lists the dedicated weapon-delivery icon as absent or treats a final rat model package as pending.
- Last-response docs now state the native mission API; Crown Strike and Seal Royal Burrows remain explicitly separate shared timed actions pending a parent decision.
- Part 9 and the triggerable-scenario matrix carry superseded notices for the old repeat-blocked wording and document accepted reconciliation-only idempotence plus the configured-intensity brood-target postcondition.
- Historical 2026-08-01 content, consequence, focus-audit, Rat King-depth, and live-wiring handoffs now carry explicit superseded notices where their old counts or asset absence claims remain for provenance.

### Contradictions still open

- The accepted 51/71 focus count convention is one tree-level identifier plus 50/70 focus blocks in the source text; no gameplay change was made to resolve that counting convention.
- Crown Strike and Seal Royal Burrows still intentionally use the shared timed state-action API rather than native mission fields.
- SCN-012 post-failure cleanup is retryable but does not prove atomic inverse rollback of every earlier disease or transfer mutation.
- Live scenario, mission, focus, balance, audio playback, rights, and mapmode validation remain unrun.

### Duplicate or superseded document list

- `2026-08-01_event20_content_tranche_handoff.md`, `2026-08-01_event20_consequence_and_aftermath_addendum.md`, `2026-08-01_event20_rat_focus_audit_handoff.md`, `2026-08-01_event20_rat_king_depth_handoff.md`, and `2026-08-01_event20_live_wiring_completion_audit_handoff.md` remain historical records with explicit superseded notices.
- The 2026-07-24 multi-tag country, scenario, and flag handoffs remain archival and are governed by the accepted 2026-07-29 two-tag correction.
- No document was deleted or merged; no duplicate current SCN-012 or cluster contract was introduced.

### Stale prompt or instruction list

- `black_plague_coding_prompt.md`, `black_plague_goal_prompt.md`, and `black_plague_decision_mission_prompt.md` retain historical bodies beneath explicit notices; follow the notices for two-tag, repeat-reconciliation, native last-response, no-model, and Crown/Seal API boundaries.
- Older prompt bodies still contain finite-tag, independent-brood, or repeat-blocked language for provenance. Do not use those lines as current production instructions.
- Older source ledgers and 2024 handoffs retain unavailable-environment and retired-tag claims with their historical notices; no deletion was authorized.

### Files changed in pass 3

- `docs/specs/020_black_plague_specs/README.md`
- `docs/specs/020_black_plague_specs/manifest.md`
- `docs/specs/020_black_plague_specs/review/limitations_and_blockers.md`
- `docs/specs/020_black_plague_specs/review/completion_audit.md`
- `docs/specs/020_black_plague_specs/review/source_of_truth_and_plan_disposition.md`
- `docs/specs/020_black_plague_specs/matrices/triggerable_scenario_matrix.md`
- `docs/specs/020_black_plague_specs/specs/020_black_plague_spec_part_9_triggerable_scenario.md`
- `docs/specs/020_black_plague_specs/prompts/black_plague_coding_prompt.md`
- `docs/specs/020_black_plague_specs/prompts/black_plague_goal_prompt.md`
- `docs/specs/020_black_plague_specs/prompts/black_plague_decision_mission_prompt.md`
- `docs/plans/020_black_plague_plans/2026-07-29_event20_core_readiness_report.md`
- `docs/plans/020_black_plague_plans/2026-08-01_event20_consequence_and_aftermath_addendum.md`
- `docs/plans/020_black_plague_plans/2026-08-01_event20_content_tranche_handoff.md`
- `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-01_event20_live_wiring_completion_audit_handoff.md`
- `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-01_event20_rat_focus_audit_handoff.md`
- `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-01_event20_rat_king_depth_handoff.md`
- `docs/events/020_black_plague/overview.md`
- `docs/events/020_black_plague/last_response_missions.md`
- `docs/events/020_black_plague/rat_route_depth.md`
- `docs/events/020_black_plague/rat_king_depth.md`

### Validation performed

- Read-only `rg` checks verified that active docs no longer present 50/70 counts, a missing dedicated weapon-delivery icon, unresolved Rat King/seal packages, or pending model production as current requirements.
- Read-only `rg` checks verified the old repeat-blocked language is confined to historical prompt/audit bodies beneath superseded notices, while the Part 9 spec, active matrix, overview, and handoff use reconciliation-only wording.
- Native mission declarations, icon wiring, and source-frame manifest/GFX references were inspected at their named runtime paths.
- Python `wave` inspection confirmed all three Event 020 WAVs are 44,100 Hz stereo.
- The changed-path review was restricted to Markdown documentation surfaces; no gameplay, localisation, GUI, GFX, audio, image, model, asset, spreadsheet, or CSV path was edited by this pass.

### Skipped meaningful validation

- No HOI4 process, save, scenario launch, focus render, mission outcome, or live audio playback was run because repository instructions assign those checks to the parent/user.
- No workbook read/export or binary texture/model validation was run because spreadsheet and asset production are outside this documentation scope.

### Recommended parent decisions

1. Treat this handoff plus `README.md`, the two-tag correction, Part 9, and the triggerable-scenario matrix as the current Event 020 documentation state.
2. Preserve SCN-012 reconciliation-only repeat behavior and the configured-intensity brood-target postcondition; do not restore repeat blocking from historical prompt or matrix bodies.
3. Keep Hold the Line and Secure the Refuge native missions, while deciding separately whether Crown Strike and Seal Royal Burrows should remain shared timed actions.
4. Keep the no-model boundary permanent for this event unless the user explicitly reopens it.
5. Carry live scenario/mission/focus/balance/audio/rights/mapmode validation and broader narrative/presentation gaps into the owning parent passes.

### Simplifications, omissions, and blockers

This pass made no gameplay simplifications and did not claim Event 020 full completion. Remaining blockers are the explicitly listed live-validation, rights-attribution, Crown/Seal mission-API, black-fog, broader narrative/presentation, and workbook-owner surfaces.
