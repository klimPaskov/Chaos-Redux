# Event 012 elephant model documentation cleanup handoff — 2026-09-06

Status: `implemented documentation reconciliation`; parent review and user-owned live validation remain pending.

This pass is documentation-only and makes no gameplay, model, asset, or achievement completion claim.

## Scope and acceptance basis

The parent task limited this pass to stale Event 012 elephant model documents that could still be read as describing a current custom entity, model, or skeletal-action runtime path, with priority on the 2026-08-05 shared-model handoff and the 2026-08-22 custom-model animation audit.

The acceptance basis is the explicit user direction recorded in `docs/plans/012_africa_plans/subagent_handoffs/012_africa_elephant_vanilla_elephantry_reuse_2026-08-27.md`: retain the custom `chaosx_elephant` gameplay identity while reusing the installed vanilla `elephantry` visual and animation family.

Current source documentation records `sprite = elephantry`, no custom `override_model`, retired custom elephant registrations, an archival/non-promoted custom evidence package, and parent/user live-validation limits.

No gameplay, localisation, GUI, GFX, entity, audio, binary asset, spreadsheet, or unrelated Event 012 documentation file was edited.

## Source-of-truth map

| Surface | Current authority | Evidence and boundary |
| --- | --- | --- |
| Event-level elephant contract | `docs/events/012_africa/elephant_warfare.md` | The custom unit, equipment, armour, technology bridge, host/Action 102 consumers, and vanilla `elephantry` visual are documented together; the custom model package is archival/non-promoted and live gameplay proofs remain open. |
| Active visual runtime disposition | `docs/systems/3d_model_pipeline/chaosx_africa_elephant_model.md` | `chaosx_elephant` uses `sprite = elephantry`, mixed templates leave `override_model` unset, the vanilla infantry entity supplies the active visual, and former custom registrations are retired. |
| User decision and source wiring | `docs/plans/012_africa_plans/subagent_handoffs/012_africa_elephant_vanilla_elephantry_reuse_2026-08-27.md` | The user direction is explicit, active-source evidence is recorded, the custom workspace is archival/non-promoted, and parent/user live consumer validation remains pending. |
| Historical custom package record | `docs/plans/012_africa_plans/subagent_handoffs/012_africa_elephant_shared_model_2026-08-05.md` | The package measurements, exports, action names, provenance, sound, counter, and former registration claims are retained with a `superseded` disposition and direct pointers to the three current sources above. |
| Historical mixed animation audit | `docs/plans/012_africa_plans/subagent_handoffs/012_custom_model_animation_quality_audit_2026-08-22.md` | The elephant rows and recovery instructions are explicitly historical and superseded; the eight strange-force findings remain historical audit material outside this elephant disposition. |

## Plan and handoff disposition

| Document | Disposition | Acceptance basis, evidence, and limit |
| --- | --- | --- |
| `docs/plans/012_africa_plans/subagent_handoffs/012_africa_elephant_shared_model_2026-08-05.md` | `superseded` | The 2026-08-27 explicit user direction replaces the custom model/entity/action path with vanilla `elephantry`; all package and former-runtime claims remain historical provenance, and the current event, visual, and reuse documents are linked at the top. |
| `docs/plans/012_africa_plans/subagent_handoffs/012_custom_model_animation_quality_audit_2026-08-22.md` | `superseded` for the elephant portion | The 2026-08-27 user direction removes the custom elephant from the current animation target; the eight strange-force audit remains historical material and is not reclassified by this pass. |
| `docs/plans/012_africa_plans/subagent_handoffs/012_africa_elephant_vanilla_elephantry_reuse_2026-08-27.md` | `implemented` source reuse, pending live validation | It records explicit user direction, current source wiring, retired custom registrations, and the remaining parent/user live-consumer and gameplay-proof boundary; it was read but left unchanged in this pass. |
| `docs/events/012_africa/elephant_warfare.md` | `implemented` documentation authority | It records the current custom gameplay identity plus vanilla visual boundary and remains the event-level source; it was read but left unchanged in this pass. |
| `docs/systems/3d_model_pipeline/chaosx_africa_elephant_model.md` | `implemented` documentation authority | It records the active vanilla visual consumer and archival custom package boundary; it was read but left unchanged in this pass. |

## Files changed

- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_elephant_shared_model_2026-08-05.md` — strengthened the superseded notice with direct current-source links, scoped all package/runtime claims as historical, and rewrote former active-status bullets as historical provenance.
- `docs/plans/012_africa_plans/subagent_handoffs/012_custom_model_animation_quality_audit_2026-08-22.md` — strengthened the elephant-only superseded notice, marked the elephant inventory and 46-action count historical, removed elephant recovery/regeneration instructions, and excluded the superseded path from current strange-force validation steps.
- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_elephant_model_docs_cleanup_2026-09-06.md` — this scoped audit and parent handoff.

Both named stale handoffs already had pre-existing superseded notices in the shared worktree, and this pass retained those changes while adding direct links and eliminating current-sounding elephant runtime instructions.

## Documents left unchanged

No documents were merged or deleted.

The current event document, visual-disposition document, and vanilla-reuse handoff were left unchanged because they already express the accepted source-reuse boundary and its validation limits.

The broader `docs/plans/012_africa_plans/documentation_cleanup_handoff_2026-09-05.md` was left unchanged because it already records these documents as current or superseded and is outside this narrow patch.

The related `012_africa_elephant_animation_recovery_2026-08-22.md`, `012_africa_elephant_meshy7_redo.md`, `012_africa_elephant_unit_wiring_2026-08-05.md`, and `012_africa_elephant_shared_reference_2026-08-05.md` were left unchanged because their existing top-level statuses already route the custom path to historical provenance or vanilla reuse; the shared-reference note remains transitively historical through its superseded target.

## Contradictions resolved

1. The shared-model handoff said parent-owned custom runtime copies and registrations “now exist” and described the custom unit as parent-wired, while current sources retire those registrations and use vanilla `elephantry`; the wording now explicitly anchors those claims to the 2026-08-05 historical state.
2. The animation audit treated six custom elephant actions as part of a current 46-action runtime gate and instructed recovery or regeneration of the missing package; the elephant counts, row, recovery step, validation commands, blocker text, and final recommendation now identify that material as historical and superseded.
3. The two stale handoffs lacked direct navigation to the current event, visual-disposition, and user-decision documents; both now link all three at the top.

## Contradictions still open

1. Parent/user live visual validation of the vanilla infantry entity and the separate elephant gameplay achievement witnesses remains open; this pass does not claim either proof.
2. Retention or deletion of the approximately 340 MB archival evidence package remains an explicit owner decision; this pass neither deletes nor promotes it.
3. The existing technology artifact linked by `docs/events/012_africa/elephant_warfare.md` reports aggregate validation false with blocking diagnostics, and standalone Technology Tree Viewer availability remains unverified; this model-document cleanup does not change or resolve that technology boundary.

## Duplicate or superseded documents

| Document or group | Current treatment |
| --- | --- |
| `012_africa_elephant_shared_model_2026-08-05.md` | Retained as historical custom-package provenance with an explicit `superseded` disposition and current-source links. |
| `012_custom_model_animation_quality_audit_2026-08-22.md` | Retained as historical mixed animation audit; only its elephant portion is explicitly superseded by vanilla reuse, while the strange-force findings remain historical. |
| `012_africa_elephant_animation_recovery_2026-08-22.md`, `012_africa_elephant_meshy7_redo.md`, `012_africa_elephant_unit_wiring_2026-08-05.md`, and `012_africa_elephant_shared_reference_2026-08-05.md` | Retained historical records with existing superseded or transitively superseded status; no duplicate merge or deletion was authorized. |

## Stale prompts or instructions

- The shared-model handoff no longer presents custom entity/action registration or future runtime synchronization as active; those statements are explicitly historical.
- The mixed animation audit no longer instructs an owner to recover or regenerate the elephant package, count its six actions in a current gate, or validate the retired elephant entity files as active consumers.
- Related historical model notes may still contain custom-package terminology inside provenance sections, but their top-level statuses route them away from current implementation and the current source-of-truth links above govern Event 012 elephant runtime decisions.

## Markdown hard-wrap issue list

The two patched handoffs and this handoff were reviewed for accidental physical line breaks inside prose sentences or clauses, and no hard-wrap issue was found.

Intentional Markdown headings, block quotes, list items, table rows, and blank paragraph boundaries were preserved.

This was a targeted audit, not a repository-wide Markdown line-wrap audit.

## Recommended parent decisions

1. Keep the three current source documents above as the only active documentation authority for the Event 012 elephant visual path.
2. Decide separately whether to retain or delete the approximately 340 MB archival package, preserving these superseded records if it is removed.
3. Perform the parent/user live validation of the vanilla `elephantry` consumer and the separate gameplay achievement witnesses before any completion claim.
4. Treat any future custom elephant model or action work as a new explicitly accepted design decision rather than a continuation of these superseded handoffs.

## MCP and validation record

The required read-only `hoi4_tech_inspect` trace for `chaosx_africa_elephant_warfare_tech` was attempted with `mode = trace`, `direction = both`, and `maxDepth = 2`, but the call failed after a 180-second service timeout; no new MCP artifact was produced.

The existing technology artifact remains linked in `docs/events/012_africa/elephant_warfare.md` and was not rewritten or treated as clean acceptance.

No event, focus, weighted-logic, GUI, or map MCP route was applicable because this pass reconciled only 3D model documentation, and the event document was read as a current source and left unchanged.

Targeted validation searched the two patched handoffs for custom-elephant runtime and recovery language, confirmed that all remaining elephant references are explicitly historical, superseded, archival, or vanilla-reuse statements, and checked that the three current source paths exist.

No binary assets, generated images, spreadsheets, or gameplay files were inspected or changed.

## Remaining risks

- The shared worktree contains many concurrent changes outside this documentation scope, so no broad status or unrelated diff is attributed to this pass.
- Retained historical documents and evidence will continue to appear in broad searches for `chaosx_elephants` or `elephant_shared_base`; their explicit dispositions must remain visible.
- The technology MCP timeout and existing aggregate diagnostics remain unresolved outside this documentation pass.
- Parent review and user live validation remain required before any Event 012 completion claim.
