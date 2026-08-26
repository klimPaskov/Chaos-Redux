# Event 016 documentation registry reconciliation handoff

Date: 2026-08-26.

Status: Documentation-only reconciliation after `d77afae7e` and the current shared MCP evidence; Event 016 remains incomplete.

## Scope

This pass reconciles the country-scoped Alien Infantry landing-registry finding, the current D’Rhondan and Portal residual issues, the current GUI/Event MCP limits, and the active Event 016 completion audits.

No gameplay, localisation, GUI, GFX, asset, model, sound, spreadsheet, or skill file was changed.

The source-of-truth correction is `d77afae7e` (`fix: preserve alien landing registry ownership`), with `fbd5f6703` retained as the preceding country-isolation change.

## Current source-of-truth map

| Surface | Current authority | Reconciled status |
| --- | --- | --- |
| Registry writer | `common/scripted_effects/016_alien_infantry_api_effects.txt:301-327` | `alien_infantry_register_landing_state` saves the invoking COUNTRY and selected STATE as event targets, then mutates the registry from the saved COUNTRY scope. |
| Registry contract | `common/scripted_effects/016_alien_infantry_api_effects.md:24,43` and `common/scripted_effects/chaosx_dynamic_effects.md:459-463` | The registry is caller-country-owned, idempotent, and not a global cross-provider array. |
| Owner-target implementation handoff | `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_alien_dhrondan_country_scoped_registry_2026-08-26.md:21-35` | The nested-scope correction and its partial Event MCP evidence are current. |
| Superseded global registry handoff | `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_alien_landing_state_registry_2026-08-26.md:3-18` | Historical global-array evidence only; the top notice points to the country-scoped implementation. |
| Event `.47` MCP evidence | `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_current_mcp_audit_2026-08-26.md:7-13` and the current `hoi4.event_inspect` artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4bb00f3a4ad4419e9e8bfaa344ce6aecadc33e485ade34078e2b979357f24169/6c946983334778a1a37960e11109f73e65d532ee2bc0de1dfe0a4b68e6072e14/event-state_flow-f588a2607444.json` | `EVENT_INSPECTED_PARTIAL`, status `ok`, zero blocking diagnostics, large-workspace helper projection deferred. |
| Directorate GUI MCP evidence | `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_current_mcp_audit_2026-08-26.md:27-31` and current inspect artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ac982a59753151c4e08404fce5807fb7bbae7a1b628eeb6ba8a15b00860b8cbc/126cd885185d595e3aea7f6be9679b4403aef0c8097e94faad34716dfc7c539d/gui-inspect.b4279d9e180ba8bb.json` | Current inspect returns `GUI_INSPECTED` with 22 Event 016 elements, but global graph diagnostics are truncated and a narrow current render returned `INTERNAL_ERROR` with no artifact. |
| D’Rhondan route consumers | `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_dhr_route_consumers_2026-08-26.md:45-53` | Five focus support markers remain reserved hooks without accepted consumers; no duplicate decisions were added. |
| Portal beachhead lifecycle | `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_portal_lifecycle_patch_2026-08-26.md:136-152` | Active-beachhead and extraction-marker cleanup remain queued for a named containment/spread owner. |
| Custom-unit model gate | `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_asset_workspace_cleanup_2026-08-26.md:35-39`, `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/attempts/v13_firearm_preset/final_manifest.md`, and the current Alien Infantry model handoffs | Alien Infantry V13 model, rig, seven actions, PDX exports, actual-byte reimport evidence, and static entity/GFX/animation/sound registrations are promoted for parent review; the supported effect point, particle/light binding, strict audio-role coverage, positional playback, and live acceptance remain blocked, and Portal Raider remains blocked at the model/entity/action gate. |
| Asset workspace | Cleanup commit `31a66c4f4` and `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_asset_workspace_cleanup_2026-08-26.md:5-39` | The cleanup handoff recorded 2,014,398,979 bytes across 4,022 files, while the current working tree measures 3,723,212,401 bytes across 4,073 files; the delta is retained as concurrent workspace evidence, not treated as a cleanup revert. |

## Plan and handoff disposition

| Document or issue | Disposition | Parent-facing meaning |
| --- | --- | --- |
| Former S1/P1 country-scoped registry writer finding in `016_final_decision_audit_2026-08-26.md` | Resolved at source by `d77afae7e`; audit wording patched | Do not reapply the registry patch; run the two-provider transfer acceptance matrix. |
| E016-01 in `016_final_event_completion_audit_2026-08-26.md` | Resolved at source; historical analysis retained and patched | The overall completion audit remains incomplete for other blockers and evidence gaps. |
| `016_alien_dhrondan_post_tranche_ownership_addendum_2026-08-26.md` registry tranche | Implemented; verification queued | The addendum now points to owner-target verification instead of another source patch. |
| `016_alien_landing_state_registry_2026-08-26.md` global-array design | Superseded | Keep as historical evidence only. |
| Portal beachhead active/extraction markers | Queued with reason | A future containment/spread owner must define transient versus permanent markers, expiry, controller changes, and cleanup. |
| Five D’Rhondan support flags | Queued with reason | Keep as reserved hooks or assign accepted consumers; do not invent duplicate decisions. |
| Directorate GUI inspect/render | Partial and MCP-limited | Inspect is current and successful for the exact window, but global graph diagnostics and current render failure prevent GUI-fidelity closure. |
| Event `.47` inspect/render/compare | Partial and MCP-limited | Current state-flow inspect is partial with zero blocking diagnostics; helper projection, render/compare baseline, and live transfer proof remain open. |
| Alien Infantry V13 model package | Accepted export and static runtime promotion; live integration blocked | Preserve the final manifest and V13 handoff as current source-of-truth evidence, while keeping supported effect-point binding, strict audio-role coverage, positional playback, and live acceptance open. |
| Portal Raider model package | Blocked | Preserve model, action, sound, entity, and reimport blockers; no runtime completion claim. |
| Asset workspace cleanup | Implemented as a compacting pass, workspace retained | The current larger folder measurement is evidence for parent review, not permission to delete active provenance. |

## Contradictions resolved

1. `016_final_decision_audit_2026-08-26.md` previously called the registry writer an S1/P1 blocker and instructed a new scope patch; its section now records the finding as resolved at source and retains only dynamic acceptance work.

2. `016_final_event_completion_audit_2026-08-26.md` previously treated E016-01 as a critical source defect; its table, finding, plan ledger, validation notes, closure order, and final classification now identify `d77afae7e` as the correction and retain the two-provider matrix as open.

3. `016_alien_dhrondan_post_tranche_ownership_addendum_2026-08-26.md` previously required replacing the global registry; its current notice and action list now require verification of the owner-target implementation.

4. The final decision audit’s GUI-timeout wording conflicted with the later current MCP audit; the reconciled status is current GUI inspect success with 22 Event 016 elements, truncated global diagnostics, and a narrow current render `INTERNAL_ERROR` with no artifact.

5. The asset cleanup handoff’s post-cleanup size is smaller than the current working-tree measurement; both values are retained with explicit provenance and no inference that the cleanup was reverted.

## Duplicate or superseded documents

- `016_alien_landing_state_registry_2026-08-26.md` is superseded by `016_alien_dhrondan_country_scoped_registry_2026-08-26.md` for runtime ownership, while its original global-array evidence remains historical.

- The pre-correction registry sections of `016_final_decision_audit_2026-08-26.md`, `016_final_event_completion_audit_2026-08-26.md`, and `016_alien_dhrondan_post_tranche_ownership_addendum_2026-08-26.md` are retained as dated audit history but no longer control implementation order.

- `016_current_mcp_audit_2026-08-26.md` is the current shared MCP receipt for Event, focus, technology, GUI, and map evidence; older timeout-only GUI or Event receipts remain historical and do not override it.

## Stale prompt or instruction audit

No named Event 016 prompt was found that still instructs the parent to apply the registry-writer scope patch.

The stale actionable instructions were in audit and addendum prose rather than a prompt file, and those instructions were corrected in this pass.

The remaining model handoff approval language, GUI worker attestation requirement, probability-auditor route limitation, Portal lifecycle ownership gap, and five support-marker ownership gap remain active instructions or risks and were not silently downgraded.

## Markdown hard-wrap audit

No accidental mid-sentence hard wrap was introduced in the four changed documentation files, and each new prose sentence is kept on one physical line.

The existing long audit files retain their deliberate heading, table, block-quote, and one-sentence-per-line structure; no unrelated prose reflow was performed.

Affected paths: none beyond the changed paragraphs in `016_final_decision_audit_2026-08-26.md`, `016_final_event_completion_audit_2026-08-26.md`, and `016_alien_dhrondan_post_tranche_ownership_addendum_2026-08-26.md`.

## Validation performed

- Read the current registry writer and confirmed the owner-target sequence at `common/scripted_effects/016_alien_infantry_api_effects.txt:301-327`.

- Read the API and dynamic-effect documentation and confirmed the current country-scoped wording at `common/scripted_effects/016_alien_infantry_api_effects.md:24,43` and `common/scripted_effects/chaosx_dynamic_effects.md:459-463`.

- Ran `rg` across Event 016 plans and specs for global registry references, P1 registry wording, E016-01, Portal beachhead lifecycle, five support flags, GUI/MCP limits, and model blockers.

- Ran current read-only `hoi4.event_inspect` for `chaosx.nr16.47` and recorded `EVENT_INSPECTED_PARTIAL`, status `ok`, zero blocking diagnostics, and the linked artifact above.

- Ran current read-only `hoi4.gui_inspect` for `kruger_directorate_container` under `event016_directorate_compact_current` and recorded `GUI_INSPECTED`, 22 Event 016 elements, and the linked artifact above.

- Ran a narrow current read-only `hoi4.gui_render` retry for the same window and scenario, which returned `INTERNAL_ERROR` with no artifact and remains recorded as a GUI/MCP limit.

- Measured the current `docs/assets/016_brilliant_scientist` folder without opening binary contents and found 4,073 files totaling 3,723,212,401 bytes.

## Skipped meaningful validation

No Hearts of Iron IV process, savegame, live campaign, or in-game consumer test was run.

No `hoi4.event_compare` baseline, named `chaosx_ai_probability_auditor` route, or same-scenario `hoi4.probability_compare` pass was available for this documentation-only reconciliation.

No binary asset or spreadsheet was opened or changed, because those surfaces are outside this curator scope.

## Recommended parent decisions

1. Accept the `d77afae7e` owner-target source correction as the current registry implementation and schedule the two-provider ordinary/deferred DHR transfer acceptance matrix.

2. Keep Portal active-beachhead lifecycle work queued until a named containment/spread owner supplies an accepted lifecycle contract.

3. Keep the five D’Rhondan support flags as reserved hooks or assign explicit owners before adding consumers.

4. Treat current GUI inspect success as scoped evidence only and preserve the global-diagnostics and current-render limitations.

5. Keep Alien Infantry V13 supported effect-point, particle/light, strict audio-role, positional-playback, and live-acceptance blockers and Portal Raider model/entity/action blockers open, and retain the active asset workspace while provenance and acceptance remain incomplete.

## Remaining risks

The owner-target registry correction has no current two-provider live transfer proof.

Portal beachhead active-state cleanup and extraction-marker policy remain unowned.

The five D’Rhondan support flags remain without accepted downstream consumers.

Current Event and GUI MCP routes are partial or error-limited, and no accepted comparison baseline exists.

Probability audit and compare coverage remain incomplete because the custom auditor route is unavailable.

Alien Infantry V13 model/action export acceptance and static entity/GFX/animation/sound registration are complete, but supported effect-point binding, strict audio-role coverage, positional playback, and live acceptance remain blocked; Portal Raider model/entity/action/audio/muzzle/runtime acceptance remains blocked.

This handoff does not claim whole-event completion.
