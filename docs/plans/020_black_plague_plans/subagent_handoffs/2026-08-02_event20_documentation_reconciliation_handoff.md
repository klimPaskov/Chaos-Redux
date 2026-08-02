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
| Crown Strike and Seal Royal Burrows mission API | Implemented statically as native mission bridges | State-selected zero-day launchers store explicit target markers; native country missions own the timeout, cancellation, factory reservation, and shared-action resolution. Live outcome validation remains open. |
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
- Last-response docs now state the native mission API; Crown Strike and Seal Royal Burrows follow the same bridge with explicit state markers and cleanup.
- Part 9 and the triggerable-scenario matrix carry superseded notices for the old repeat-blocked wording and document accepted reconciliation-only idempotence plus the configured-intensity brood-target postcondition.
- Historical 2026-08-01 content, consequence, focus-audit, Rat King-depth, and live-wiring handoffs now carry explicit superseded notices where their old counts or asset absence claims remain for provenance.

### Contradictions still open

- The accepted 51/71 focus count convention is one tree-level identifier plus 50/70 focus blocks in the source text; no gameplay change was made to resolve that counting convention.
- Crown Strike and Seal Royal Burrows now use native mission fields while retaining the shared state-action resolver for outcomes.
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
3. Keep Hold the Line, Secure the Refuge, Crown Strike, and Seal Royal Burrows on the native mission surface; validate their live timeout, cancellation, and teardown behavior.
4. Keep the no-model boundary permanent for this event unless the user explicitly reopens it.
5. Carry live scenario/mission/focus/balance/audio/rights/mapmode validation and broader narrative/presentation gaps into the owning parent passes.

### Simplifications, omissions, and blockers

This pass made no gameplay simplifications and did not claim Event 020 full completion. Remaining blockers are the explicitly listed live-validation, rights-attribution, black-fog, broader narrative/presentation, and workbook-owner surfaces.

## Pass-4 current-tranche seal and SCN-012 contract addendum (2026-08-02)

### Scope and evidence boundary

This narrow follow-up reconciles the completed Event 020 crisis-seal and Rat King terminal-readiness seal packages, their exact runtime names and paths, the shared-board trigger and tooltip contract, and the current SCN-012/idempotent scenario wording. Current gameplay, GUI, GFX, and localisation files were read as evidence only; no gameplay, localisation, scripted GUI, GFX, asset binary, spreadsheet, or CSV file was edited.

### Current source-of-truth map

| Surface | Current authority and evidence | Disposition |
| --- | --- | --- |
| Severe/Collapsed crisis seal package | `docs/assets/020_black_plague/animations/black_plague_crisis_seal/manifest.md` and `gfx_handoff.md`, `docs/assets/020_black_plague/manifest.md`, and `interface/020_black_plague_rat_identity.gfx` | Promoted. `GFX_black_plague_crisis_seal_static` points to `gfx/interface/animated/020_black_plague/crisis_seal/black_plague_crisis_seal_static.dds`; `GFX_black_plague_crisis_seal_animated` points to `gfx/interface/animated/020_black_plague/crisis_seal/black_plague_crisis_seal_sheet.dds`; both are eight-frame, 6 FPS siblings. |
| Shared-board crisis gate and tooltip | `interface/biowarfare_disease_containment.gui`, `common/scripted_guis/biowarfare_disease_containment_scripted_gui.txt`, `common/scripted_triggers/biowarfare_disease_containment_triggers.txt`, and `localisation/english/biowarfare_disease_containment_l_english.yml` | Promoted. `disease_containment_board_selected_card` mounts the static and animated icons; `disease_containment_board_black_plague_crisis_seal_visible` and `_animated_visible` share `disease_containment_board_view_state_is_black_plague_crisis`, which requires `black_plague_state_is_severe` or `black_plague_state_is_collapsed`; both use `disease_containment.gui.selected.black_plague_crisis_seal.tt`. |
| Rat King terminal-readiness seal package | `docs/assets/020_black_plague/animations/rat_king_world_end_readiness_seal/manifest.md` and `gfx_handoff.md`, `docs/assets/020_black_plague/manifest.md`, and `interface/020_black_plague_rat_identity.gfx` | Promoted. `GFX_black_plague_rat_king_terminal_readiness_static` points to `gfx/interface/animated/020_black_plague/world_end_readiness_seal/black_plague_rat_king_terminal_readiness_static.dds` and `_animated` points to `gfx/interface/animated/020_black_plague/world_end_readiness_seal/black_plague_rat_king_terminal_readiness_sheet.dds`; the pair is eight frames at 6 FPS. |
| Terminal decision consumer | `common/decisions/020_black_plague_rat_decisions.txt` and `localisation/english/020_black_plague_rat_decisions_l_english.yml` | Promoted decision wiring. `black_plague_rat_king_execute_terminal_takeover` consumes the animated readiness sprite and resolves through the existing Evolution V gate; its name, description, and cost keys resolve. No separate scripted-GUI terminal-readiness rectangle exists in the current tree. |
| SCN-012 repeat and intensity contract | Part 9 spec, triggerable-scenario matrix, `docs/events/020_black_plague/overview.md`, `common/scripted_effects/020_black_plague_scenario_effects.txt`, and `common/scripted_triggers/020_black_plague_scenario_triggers.txt` | Accepted current contract. Successful repeat signals are idempotent and reconciliation-only; they preserve history and existing identity, reconcile the configured-intensity brood target and RTA/RTX division floors, refresh board/mapmode/threat state, and do not replay Evolutions I-IV or duplicate reports. A failed downstream postcondition clears temporary state and remains retryable; atomic inverse rollback of every prior mutation is not claimed. |
| SCN-012 status localisation | `localisation/english/chaosx_gui_l_english.yml` and `localisation/english/020_black_plague_scenario_l_english.yml` | Current. `chaosx.scenarios.launch_status.black_plague.terminal_lock` has one authoritative definition in `chaosx_gui_l_english.yml`; the Event 020 scenario file does not redeclare it. The repeat-ready, already-launched, setup-failed, and unavailable strings describe the accepted idempotent/retryable contract. |

### Unresolved plan and handoff disposition

| Item | Disposition | Remaining owner or reason |
| --- | --- | --- |
| Crisis seal source-frame package and shared-board wiring | Promoted and documented | Parent owns live GUI visibility, scale, and tooltip validation. |
| Rat King terminal-readiness source-frame package and final-order decision icon | Promoted and documented | Parent owns live decision visibility and should decide whether a separate scripted-GUI readiness panel is still required. |
| SCN-012 repeat reconciliation and configured-intensity postcondition | Implemented statically and promoted | Parent/user owns fresh launch, repeat, save/reload, and failure-retry validation; no full inverse rollback claim is made. |
| Duplicate `terminal_lock` localisation key | Resolved in this tranche | The divergent Event 020 scenario-file definition was removed; `chaosx_gui_l_english.yml` is the sole current owner and preserves the accepted terminal-lock meaning. |

### Contradictions and stale surfaces

- The two seal asset manifests previously described parent-owned or absent consumers; the current manifests now distinguish promoted GFX/decision wiring from the still-absent dedicated terminal-readiness panel.
- The root asset manifest previously ended with a blanket “No GFX, GUI, gameplay, localisation, or model files were changed” statement; it now records the promoted runtime registration and the remaining panel boundary.
- The previously divergent `chaosx.scenarios.launch_status.black_plague.terminal_lock` definition was removed from `localisation/english/020_black_plague_scenario_l_english.yml`; the key now has one owner in `localisation/english/chaosx_gui_l_english.yml`.
- Historical content and audit handoffs may still call broader crisis report art queued. That wording refers to report/presentation depth, not the now-promoted shared-board crisis seal; their historical notices remain intact.

### Duplicate or superseded document list

- No Event 020 document was deleted or merged in this follow-up.
- The two animation package manifests and GFX handoffs are current runtime evidence after this addendum; older parent-owned/no-consumer sentences were replaced in place rather than preserved as active instructions.
- Historical 2026-08-01 handoffs remain archival and are governed by the current reconciliation handoff; no stale prompt was promoted.

### Stale prompt or instruction list

- Older asset and completion handoffs retain historical “source-frame crisis” or “readiness” absence claims beneath superseded notices. Use the package manifests, `docs/events/020_black_plague/overview.md`, and this addendum for the promoted seal status.
- No prompt currently authorizes a separate terminal-readiness scripted GUI; the absence is documented as a remaining parent decision rather than silently filled with a fallback.

### Files changed in this follow-up

- `docs/assets/020_black_plague/animations/black_plague_crisis_seal/manifest.md`
- `docs/assets/020_black_plague/animations/black_plague_crisis_seal/gfx_handoff.md`
- `docs/assets/020_black_plague/animations/rat_king_world_end_readiness_seal/manifest.md`
- `docs/assets/020_black_plague/animations/rat_king_world_end_readiness_seal/gfx_handoff.md`
- `docs/assets/020_black_plague/manifest.md`
- `docs/events/020_black_plague/overview.md`
- `docs/events/020_black_plague/shared_response.md`
- `docs/specs/020_black_plague_specs/README.md`
- `docs/specs/020_black_plague_specs/manifest.md`
- `docs/specs/020_black_plague_specs/review/completion_audit.md`
- `docs/specs/020_black_plague_specs/review/limitations_and_blockers.md`
- `docs/specs/020_black_plague_specs/review/source_of_truth_and_plan_disposition.md`
- `docs/plans/020_black_plague_plans/2026-07-29_event20_core_readiness_report.md`
- `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-02_event20_documentation_reconciliation_handoff.md`

### Validation performed

- Targeted `rg` checks matched every crisis and terminal sprite name to `interface/020_black_plague_rat_identity.gfx` and matched both DDS directory families to the package manifests and current event docs.
- Targeted `rg` checks matched the shared-board icon types, the Severe/Collapsed state trigger, and `disease_containment.gui.selected.black_plague_crisis_seal.tt` across GUI, scripted GUI, scripted trigger, and localisation evidence.
- Targeted `rg` checks matched the RTX final-order decision icon and its name, description, and cost localisation keys.
- Targeted `rg` checks verified SCN-012 repeat-ready, setup-failed, terminal-lock, and configured-intensity/idempotent wording in the active overview and scenario implementation evidence.
- A duplicate-key check across the Event 020/shared disease localisation surfaces found no duplicate keys after the terminal-lock owner was consolidated.
- No HOI4 process, save, scenario launch, GUI render, or live consumer validation was run.

### Recommended parent decisions

1. Preserve the promoted crisis seal contract and use `disease_containment_board_view_state_is_black_plague_crisis` as the single Severe/Collapsed gate for both icon siblings.
2. Decide whether the terminal-readiness asset remains decision-only or receives a dedicated scripted-GUI panel; do not claim that panel until a consumer rectangle and trigger exist.
3. Keep `chaosx.scenarios.launch_status.black_plague.terminal_lock` owned only by `localisation/english/chaosx_gui_l_english.yml` while preserving the accepted terminal/unavailable distinction.
4. Run the user-owned live checks for crisis-card visibility, terminal decision visibility, SCN-012 repeat reconciliation, configured-intensity floors, failure retry, and save/reload persistence.

### Simplifications, omissions, and blockers

No gameplay simplification was introduced. The remaining documentation-visible boundary in this tranche is the absence of a dedicated scripted-GUI terminal-readiness panel; live validation remains unrun and no Event 020 full-completion claim is made.

## Pass-5 native Crown and Royal Burrow mission bridge (2026-08-02)

The parent implementation converted Crown Strike and Seal Royal Burrows from shared `days_remove` state actions into native mission-backed operations without changing their shared action ids, costs, reports, or the two-tag boundary. Each visible state-targeted decision is now a zero-day launcher that marks the selected state and activates a country mission. The mission owns the existing duration, civilian-factory reservation, invalidation cancellation, and timeout resolver; the resolver calls the original shared state-action effect exactly once and clears the marker, owner, mission flag, and mission instance.

The active sources are `common/decisions/020_black_plague_shared_response_decisions.txt`, `common/scripted_triggers/020_black_plague_shared_response_triggers.txt`, `common/scripted_effects/020_black_plague_shared_response_effects.txt`, and `localisation/english/020_black_plague_response_l_english.yml`. Terminal country cleanup now removes both mission instances and clears their state markers. Live mission outcomes, GUI rendering, and factory reservation remain user-owned validation surfaces; the former native-mission API gap is superseded by this addendum.
