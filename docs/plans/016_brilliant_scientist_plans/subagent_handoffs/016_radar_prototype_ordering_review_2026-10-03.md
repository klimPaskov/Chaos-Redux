# Event016 radar Prototype ordering source review

Date: 2026-10-03.
Role: chaosx_scripted_system_architect, explicitly read-only except this handoff.
Disposition: source review completed, engine and final integration evidence unresolved and parent-owned.

## Finding and acceptance basis

No concrete source defect was found in the added Electronics retry at effects lines 1525-1531.
It closes the stated ordering gap when the exact radar output marker and radio_detection precede a newly applied private Electronics Prototype.
This conclusion is conditional source reasoning, not an executed scenario or engine validation.

The delegation records accepted user decisions: exact output markers on existing IDs, preserve matching active paid timers, add no projects, technologies, or models, and retain three native categories.
The review does not establish additional design approval.
Native Prototype ownership beyond this ordering patch remains separate queued work and was not redesigned.

## Source identities and reviewed evidence

Root: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
All spans below refer to the current local files inspected during this review.

| File | SHA-256 | Relevant spans |
| --- | --- | --- |
| `common/scripted_effects/016_mengele_project_stage_effects.txt` | `8161A88971EEA2989126634AA41E433E652934D76D906414A048BD3498A12C40` | 11-42 receipt initialization, 64-69 selector clearing, 781-790 Electronics package dispatch, 895-956 output gate and Electronics output, 1313-1320 output epilogue, 1324-1387 exact settlement and radar callbacks, 1464-1553 adoption/sync/record adapters, 1559-1570 family reconciliation, 1666-1688 availability |
| `common/scripted_triggers/016_mengele_project_stage_triggers.txt` | `5AB7041CE22F13FBFECF641F4CA9E6FC7D693DDF366DA14E631A3DFA498E537C` | 16-35 provider lifecycle excerpt, 88-94 exact Electronics Deployment request, 183-199 Electronics predecessors, 1282-1293 receipt emptiness, 1427-1435 Electronics native authenticity, 1600-1617 aggregate authenticity |

Read current `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, and `.agents/skills/chaos-redux-events/SKILL.md`.
No broad repository scan or MCP call was made.
No reference artifacts or engine revisions are claimed.

## Manual source scenario traces

| Scenario | Source outcome and evidence |
| --- | --- |
| Marker and radio_detection both precede private Prototype reconciliation | Earlier pair attempts fail the Deployment predecessor at triggers 189-194. Sync authenticates the native completion at effects 1518, applies the private Prototype through 1521, records synced = one at 1524, and retries the exact pair at 1530. With a valid provider and empty Electronics receipt, Deployment reaches the existing package/output path and records its native source if that path reports success. |
| Private Prototype precedes the marker and technology | The new retry initially lacks at least one pair input and does nothing. Marker arrival checks has_tech at 1363 and attempts settlement if technology is already present. If the marker arrives first, the radio_detection callback at 1383-1387 supplies the later attempt. Thus either marker/technology order has a source path to settlement after Prototype, subject to the same guards. |
| Missing exact output marker, even with completed sp_air_radar and radio_detection | Prototype authenticity can succeed through triggers 1427-1435, but the pair helper fails its exact marker requirement at effects 1373. The retry neither fabricates the marker nor infers it from technology or project completion. Missing radio_detection analogously blocks at 1374. |
| Active matching Electronics paid stage receipt | Exact settlement initializes arrays append-only, then fails the family receipt-empty check at 1335 and triggers 1291-1292. It never calls the stage output at 1339. Existing receipt entries and timer flags are not cleared, restarted, refunded, or consumed by this retry. This paid-timer conclusion concerns the Deployment retry, not the separate queued Prototype ownership policy. |
| Replay after private Prototype has already been applied | apply_family_stage_output resets project_output_applied, then its predecessor rejects the completed Prototype. Sync leaves native_prototype_synced = zero and never reaches the new retry. A direct pair callback after completed Deployment fails the repeated-stage guard at triggers 193 and cannot grant again or overwrite recorded provenance. |
| Result markers with successful new Prototype and blocked pair | Sync sets native_prototype_synced = one before attempting Deployment. A marker/technology gate failure does not reset it. A receipt/predecessor failure inside exact settlement also does not reset it. record_native_project_prototype can therefore publish native_prototype_recorded = one at 1545. The dedicated native_later_stage_settled result resets to zero when exact settlement is entered and only becomes one after its output succeeds. |
| Result markers with successful new Prototype and attempted package application | The nested stage dispatcher may reset or replace generic project_output_applied, computation_output_applied, and stage_output_gap, since those describe the latest output attempt. The dedicated native_prototype_synced remains one independently, so Prototype recording is preserved even if the Deployment package fails to report success. adopt_completed_native_after_theory explicitly restores its saved outer generic outputs and selectors at 1503-1511. No guarantee is made that the generic project_output_applied remains a Prototype-specific result after nested Deployment. |
| Selector clearing | Exact settlement clears family, requested stage, native source, and index through effects 1355 and 64-69. Sync unconditionally repeats that clearing at 1534 and resets authorization at 1535. Even a pair gate failure takes the sync epilogue. The outer Theory adoption adapter intentionally restores its own saved selectors after sync, preserving that enclosing transaction. |
| Other-family isolation | The new retry requires Electronics at 1529 before the pair helper selects Electronics Deployment. Other families cannot enter that call through sync. Exact provenance writes use the prepared Electronics index, and the receipt-empty check reads Electronics slot 1. Existing sequential family reconciliation explicitly selects each later family at 1564, 1566, and 1568. Receipt schema initialization and existing availability restoration can touch shared maintenance state, so isolation means no added other-family stage grants or receipt settlement. |

## Helper contract and lifecycle impact

No helper was created or changed by this subagent.
The parent's single added call reuses `brilliant_scientist_mengele_settle_native_electronics_deployment_from_radar` from `brilliant_scientist_mengele_sync_native_project_prototypes`.
Both operate in country scope.
Inputs are a valid provider, newly applied Electronics private Prototype for the new call site, exact output-seen country flag, radio_detection, strict predecessor flags, and an empty Electronics paid receipt.
Successful output is the existing Electronics Deployment package/completion plus `electronics_radar_pair` provenance in the existing Deployment source array.
Side effects remain those of the existing output dispatcher and availability reconciliation.
Dedicated Prototype success markers remain separate from Deployment success.

Constants and tuning: no additions or changes.
Event targets: no additions or changes.
Cleanup: existing selector clearing is reused, with no new persistent lifecycle state.
Migration: one additional retry call, without moving or duplicating the settlement logic.
Call sites, localisation, model, visual, gameplay documentation, and skills were not edited by this subagent.

## Simplifications, omissions, and blockers

No implementation simplification or fallback was introduced.
This assignment deliberately permits only source review and this handoff.
Parent owns actual offline wiki and installed reference reads, live MCP retry, final integration, review, and commit.
MCP service health and route availability were not tested, so no route outage is asserted.
The exact evidence gap is that this delegation prohibits MCP calls and provides no executed callback-order artifacts.

The source traces assume country-scoped callback delivery, visibility of completed sp_air_radar to the native authenticity predicate when reconciliation runs, and expected has_tech visibility for radio_detection.
Actual callback timing, synchronous research callback reentry, downstream conventional-package grant behavior, and marker installation on the exact project output were not executed or independently inspected outside the two named source files.
Parent must retain those limitations in final completion claims.

The retry only follows a newly applied private Prototype.
It is not a general deferred retry queue for an already-completed Prototype whose earlier Deployment attempt was blocked by a paid receipt or provider lifecycle condition.
That behavior preserves the accepted paid-timer gate and does not authorize bypassing it.
An output marker absent when the original hook runs is not reconstructed by this patch.
Broader native Prototype ownership remains separate queued work.

## Delivery

Only file written: this handoff.
Meaningful validation performed: manual control-flow traces for all scenarios in the table against the named local source blocks and their direct adapters.
Meaningful validation skipped: engine execution, MCP inspect/compare, callback timing, external package consumer behavior, and reference validation, all retained by the parent under the explicit source-only boundary.
No game launch, model creation/edit, other file edit, index mutation, or commit.
Skills used: chaos-redux-subagents and chaos-redux-events.
No skills created or updated.

## Parent review and service retry

Parent acceptance is bounded to the added exact Electronics handoff under the approved native marker mapping and unchanged paid-timer decision.
The direct source review preserves the dedicated native_prototype_synced success marker, while generic output markers may describe the subsequent Deployment attempt.
The desktop MCP routes disappeared after the app connection reset.
The installed service initialized and answered ping and tools/list as version3.6.0 under a one-workspace configuration.
A narrower source_lookup for this exact helper disabled references, selected one definition, and limited the body to36 lines, but timed out after120 seconds.
The accompanying event reference context request also timed out after120 seconds.
The current live schemas do not expose source_lookup view/keyPath or script_validate.
The parent retains direct local wiki and installed reference evidence in native_stage_completion_hooks.md and the existing provider mechanic documentation.
No runtime or technology rendering acceptance is claimed from this source-only fix.
