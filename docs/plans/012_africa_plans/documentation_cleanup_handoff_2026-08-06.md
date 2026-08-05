# Event 012 Africa documentation cleanup handoff

Date: 2026-08-06.

## Scope and disposition

This pass reconciles the Event 012 release overview, elephant model and runtime handoffs, visual matrix notes, acceptance-ledger evidence, achievement handoffs, dated completion audits, and the catalog workbook note after the shared armoured elephant tranche.

Gameplay, localisation, GFX, GUI, binary asset, spreadsheet, and workbook files were not edited by this documentation pass.

The current source still does not claim gameplay completion, live-save validation, or achievement completion.

## Current source-of-truth map

| Surface | Current source of truth | Evidence and boundary |
| --- | --- | --- |
| Accepted Event 012 design | `docs/specs/012_africa_specs/` | The accepted specifications define intended mechanics, route gates, identities, and required asset rows. |
| Release-candidate status | `docs/events/012_africa/overview.md` | The overview is the current status index and now records the elephant exception, current matrix counts, and remaining model-gated families. |
| Elephant mechanics contract | `docs/events/012_africa/elephant_warfare.md` | The event document records the `chaosx_elephant` unit, equipment, technology bridge, host consumer, Action 102 consumers, counters, sounds, and non-completion boundary. |
| Elephant runtime handoff | `docs/plans/012_africa_plans/subagent_handoffs/012_africa_elephant_unit_wiring_2026-08-05.md` | Static unit/entity/technology/equipment bindings and host/member formation consumers are recorded; live campaign proof remains open. |
| Shared model package | `docs/assets/012_africa/models_3d/elephant_shared_base/manifest.md` and `docs/plans/012_africa_plans/subagent_handoffs/012_africa_elephant_shared_model_2026-08-05.md` | Mesh, six actions, packed maps, sound provenance, counter hashes, scale, and parent-owned runtime copies are documented; the package does not claim in-game completion. |
| Visual row status | `docs/specs/012_africa_specs/matrices/012_africa_asset_animation_matrix.csv` and `012_africa_asset_animation_matrix_notes.md` | The 239-row matrix is authoritative and now records rows 203-204 as `installed_runtime`. |
| Shared acceptance ledger | `docs/plans/012_africa_plans/012_africa_acceptance_ledger.csv` | All 239 `asset_item` rows match the matrix key order and status values; non-asset dispositions remain separate. |
| Achievement route status | `docs/plans/012_africa_plans/012_africa_achievements_handoff.md`, `subagent_handoffs/012_africa_achievement_callsite_audit_2026-07-29.md`, and `subagent_handoffs/012_africa_a1_achievement_acceptance_2026-07-30.md` | Row 36 is runtime-evidence-gated after model/entity wiring; achievement owners, disqualifiers, and live witnesses remain open. |
| Catalog workbook boundary | `docs/plans/012_africa_plans/subagent_handoffs/012_africa_event_catalog_workbook_2026-08-03.md` | The workbook remains owned by `chaosx_spreadsheet_doc_worker`; this note records the elephant exception without editing workbook or export files. |

## Evidence snapshot

- The current visual matrix has 239 rows with 52 `installed_runtime`, 28 `installed_dormant`, 12 `deferred_runtime_gated`, 133 `deferred_controlled_pool`, 14 `deferred_model_required`, and 0 `deferred_unique_package_required` rows.
- Matrix and ledger reconciliation imported 239 matrix rows and 239 `asset_item` ledger rows, with exact key order and exact status-to-disposition equality.
- Matrix rows 203 and 204 are `unit_identity_elephant_logistics` and `unit_identity_elephant_shock`, both `installed_runtime`, both using `chaosx_elephant_equipment.dds` and the shared `GFX_chaosx_elephant_equipment_medium` token family.
- The static runtime consumer set exists at `common/units/012_africa_elephant_forces.txt`, `common/units/equipment/012_africa_elephant_equipment.txt`, `common/technologies/012_africa_elephant_technologies.txt`, `common/scripted_effects/012_africa_elephant_effects.txt`, `gfx/entities/chaosx_elephants.asset`, `gfx/entities/chaosx_elephants.gfx`, `sound/chaosx_elephants_sound.asset`, and `interface/012_africa_elephant.gfx`.
- Host wiring calls `africa_elephant_prepare_host_guard`; Action 102 member wiring calls `africa_elephant_prepare_member_guard` before the existing package force initializer, and all five structural package templates contain one `chaosx_elephant` regiment.
- Shared counter aliases are registered in `interface/chaosx_subuniticons.gfx` for the shared-body and `chaosx_elephant` large and on-map tokens.
- Achievement row 36 remains blocked with `RUNTIME-EVIDENCE-GATED` documentation because its formation, terrain, supply, protection-victory, and three failure-disqualifier helpers do not yet have accepted achievement callers or live movement, supply, destruction, and war-purpose witnesses.
- Rows 197-202 and 205-212 remain model-required, and Actions 74-76 remain gated by `africa_strange_formation_package_ready`.

## Plan and handoff disposition

| Document | Disposition | Current interpretation |
| --- | --- | --- |
| `docs/events/012_africa/overview.md` | Current status authority | The elephant consumer is a separate live runtime exception; the other strange formations remain gated and no model-dependent completion is claimed. |
| `docs/events/012_africa/elephant_warfare.md` | Current mechanics document | This is the narrow elephant runtime contract and is complementary to the unit wiring handoff, not a duplicate. |
| `012_africa_elephant_unit_wiring_2026-08-05.md` | Current static runtime evidence | Parent wiring is recorded; live movement, supply, destruction, war-purpose, and save validation remain open. |
| `012_africa_elephant_shared_model_2026-08-05.md` | Current source package handoff | Its former dormant boundary is superseded by parent unit wiring, while the package remains the model provenance authority. |
| `012_africa_elephant_shared_reference_2026-08-05.md` | Superseded | The immutable one-image reference remains provenance only; the shared model handoff is the active package record. |
| `012_africa_model_requirements_2026-08-01.md` | Historical baseline with superseding note | Rows 203-204 are promoted through one shared body; rows 197-202 and 205-212 remain deferred. |
| `012_africa_asset_animation_matrix.csv` | Current authoritative matrix | Rows 203-204 are installed runtime; no unique-package status remains. |
| `012_africa_asset_animation_matrix_notes.md` | Reconciled | The old 50/21/16/7 snapshot was replaced with the current 52/28/14/0 counts and shared-body exception. |
| `012_africa_acceptance_ledger.csv` | Current ledger evidence | Asset rows match matrix order and statuses; achievement row 36 remains blocked and runtime-evidence-gated. |
| `012_africa_achievements_handoff.md` | Reconciled | Row 36 is separated from the three remaining model-gated achievement rows, with live proof still open. |
| `012_africa_achievement_callsite_audit_2026-07-29.md` | Reconciled dated audit | Row 36 cleared the model-package barrier but remains dormant behind exact achievement owners and live witnesses. |
| `012_africa_a1_achievement_acceptance_2026-07-30.md` | Reconciled dated handoff | Row 36 is runtime-evidence-gated; rows 18, 35, and 40 remain model-gated. |
| `012_africa_achievement_owner_kernel_consolidation_2026-08-01.md` | Reconciled blocker note | Elephant proof owners remain caller-pending even though the static package now exists. |
| `012_africa_event_catalog_workbook_2026-08-03.md` | Historical catalog evidence with superseding note | The catalog remains broad and intentionally incomplete; the workbook/export pair was not edited here. |
| `documentation_cleanup_handoff.md` | Historical cleanup baseline with superseding note | Its old counts and no-model statement are provenance, not current status. |
| `012_africa_final_improvement_loop_addendum_2026-08-01.md` | Historical working plan with superseding note | Current matrix counts and elephant exception are recorded; remaining model gates stay queued. |
| `012_africa_final_completion_audit_2026-08-01.md` | Historical completion audit with superseding note | The old 16-row model deficit is reduced to 14 remaining rows; the incomplete verdict is unchanged. |
| `012_africa_priority_member_acceptance_pass_2026-07-30.md` | Historical package audit with superseding note | Its package-force model boundary remains valid for the sixteen package identities; the elephant consumer is a separate exception. |
| `docs/assets/012_africa/models_3d/elephant_shared_base/runtime/crosswalk.md` | Reconciled | Runtime geometry, actions, maps, sounds, and shared-body roles now distinguish static wiring from live review. |
| `docs/assets/012_africa/models_3d/elephant_shared_base/evidence/counter/manifest.md` and `gfx_handoff.md` | Reconciled | Counter files and aliases are statically wired; live validation remains open. |
| `docs/assets/012_africa/models_3d/elephant_shared_base/evidence/equipment/gfx_handoff.md` | Reconciled | The runtime `.gfx` owner and parent-reviewed status replace the former proposed/needs-review language. |

## Contradictions and unresolved stale claims

1. The overview's dated runtime-core row was narrowed to Stone, Gorilla, and Pan and now links the separate elephant document; no contradiction remains on that row.
2. Older completion and model audits outside the patched 2026-08-01 files still list all sixteen model-required rows or say no model package exists; they remain historical evidence and should not be used as current release status.
3. The workbook itself still carries the broad catalog model-boundary wording from the 2026-08-03 snapshot; the workbook handoff now explains that the elephant exception is documented in the matrix and overview, but a spreadsheet-owner update would be required if player-facing catalog detail must change.
4. `docs/assets/012_africa/focus_icons_imagegen/coverage_crosswalk.md` and `manifest.md` retain older registration-pending wording even though current `.gfx` registrations exist; this is outside the elephant scope and remains a separate asset-doc cleanup target.
5. The current static consumer evidence does not prove a live campaign witness, so “live custom unit consumer” means source/runtime wiring and not in-game validation.

## Duplicate and superseded documents

- `012_africa_elephant_shared_reference_2026-08-05.md` is explicitly superseded by `012_africa_elephant_shared_model_2026-08-05.md`.
- `documentation_cleanup_handoff.md` is superseded for current status by this handoff and `docs/events/012_africa/overview.md`.
- The model requirements handoff, final improvement addendum, and final completion audit remain useful dated evidence but are superseded where their old counts or blanket no-model claims conflict with the elephant exception.
- `elephant_warfare.md` and `012_africa_elephant_unit_wiring_2026-08-05.md` are complementary and should not be merged because one describes mechanics and the other records runtime bindings.

## Stale prompt or instruction list

- The original no-model status in `012_africa_model_requirements_2026-08-01.md` is now explicitly historical and partitioned by row range.
- The old achievement callsite and A1 handoffs formerly grouped row 36 with model-gated rows; both now use runtime-evidence-gated wording.
- The event-catalog workbook handoff formerly described only the non-model boundary; its superseding note records the elephant exception without changing catalog files.
- Focus-icon asset manifests still describe registration as pending and should be routed to the asset owner separately.

## Markdown hard-wrap audit

No accidental mid-sentence or mid-clause hard wraps were found in the Markdown files changed or reviewed in this pass.

The long table rows and block quotes remain intentional Markdown structures, and each added prose sentence is kept on one physical line.

## Recommended parent decisions

1. Preserve the overview's narrowed runtime-core wording when future dated handoffs are promoted.
2. Keep achievement 36 blocked until exact formation, terrain, supply, protection-victory, and failure-disqualifier owners plus live movement, supply, destruction, and war-purpose witnesses are accepted.
3. Decide whether the spreadsheet owner should update the player-facing workbook row to mention the shared elephant exception, then regenerate exports through the required workbook workflow if so.
4. Route the stale focus-icon registration wording to the asset owner without reopening the elephant or matrix decisions.
5. Keep rows 197-202 and 205-212, Stone/Gorilla/Pan Actions 74-76, and the three remaining model-gated achievements deferred until their own packages and evidence exist.

## Files changed in this documentation pass

- `docs/events/012_africa/overview.md` received a wording clarification for its current strange-formation row.
- `docs/specs/012_africa_specs/matrices/012_africa_asset_animation_matrix_notes.md` now records current status counts and the elephant shared-body exception.
- `docs/plans/012_africa_plans/012_africa_achievements_handoff.md`, `subagent_handoffs/012_africa_achievement_callsite_audit_2026-07-29.md`, and `subagent_handoffs/012_africa_a1_achievement_acceptance_2026-07-30.md` now separate row 36 from model-gated achievements.
- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_model_requirements_2026-08-01.md`, `012_africa_achievement_owner_kernel_consolidation_2026-08-01.md`, `012_africa_priority_member_acceptance_pass_2026-07-30.md`, and `012_africa_elephant_equipment_icon_2026-08-05.md` now carry current elephant-boundary or runtime-owner notes.
- `docs/plans/012_africa_plans/documentation_cleanup_handoff.md`, `012_africa_final_improvement_loop_addendum_2026-08-01.md`, `subagent_handoffs/012_africa_event_catalog_workbook_2026-08-03.md`, and `subagent_handoffs/012_africa_final_completion_audit_2026-08-01.md` now carry superseding current-status notes or counts.
- `docs/assets/012_africa/models_3d/elephant_shared_base/manifest.md`, `runtime/handoff.md`, `runtime/crosswalk.md`, `evidence/counter/manifest.md`, `evidence/counter/gfx_handoff.md`, and `evidence/equipment/gfx_handoff.md` now distinguish static wiring from live validation.
- This handoff is new at `docs/plans/012_africa_plans/documentation_cleanup_handoff_2026-08-06.md`.

## Validation and skipped checks

- Imported the visual matrix and acceptance ledger and confirmed 239 rows each, exact asset key order, and exact matrix-status to ledger-disposition equality.
- Recounted current matrix statuses as 52/28/12/133/14/0 for installed runtime, installed dormant, runtime-gated, controlled-pool, model-required, and unique-package-required respectively.
- Confirmed the static elephant runtime paths, host and Action 102 helper references, and shared counter aliases exist in the current filesystem.
- Searched current achievement docs for stale row-36 `MODEL-GATED` wording and found no remaining hit in the audited files.
- Searched current counter and equipment handoffs for `parent wiring pending`, `wiring pending`, `needs_user_review`, and proposed-owner wording and found no remaining hit in the audited files.
- No in-game launch, live-save scenario, HOI4 consumer test, MCP event/focus/technology render, workbook round-trip, or binary visual review was run by this documentation pass because those surfaces remain parent- or owner-scoped.

## Remaining risks

- Static unit/entity wiring may still expose parser, equipment, supply, formation, or animation issues that require the parent-owned live scenario.
- Achievement 36 still lacks exact positive and negative runtime owners and all requested live witnesses.
- The shared model package reports 4,998 semantic boundary edges, so topology review remains an explicit asset risk even though no degenerate or non-manifold faces were reported.
- The workbook and generated exports remain historical catalog evidence until the spreadsheet owner decides whether the new elephant exception changes player-facing wording.
- Remaining model-required unit rows and the gated Stone/Gorilla/Pan formations remain intentionally deferred.

No gameplay completion claim is made by this handoff.
