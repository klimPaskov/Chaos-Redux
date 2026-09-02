# Event016 conventional technology API documentation reconciliation

Date: 2026-09-02

Status: Documentation-only reconciliation completed for the named API documents and registry row; this handoff records current source evidence and open gates, and does not claim gameplay, MCP, engine, model, or final acceptance.

## Scope and authority

The closure contract is `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md`.

The reconciled custom API documentation is `docs/events/016_brilliant_scientist/systems/custom_technology_api.md` and `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.md`.

The separate conventional API is implemented in `common/scripted_effects/016_conventional_technology_api_effects.txt`, documented in `common/scripted_effects/016_conventional_technology_api_effects.md`, and guarded by `common/scripted_triggers/016_conventional_technology_api_triggers.txt`.

The ordinary category and paid action consumers are `common/decisions/categories/016_conventional_technology_categories.txt`, `common/decisions/016_brilliant_scientist_technology_actions.txt`, and `common/scripted_triggers/016_brilliant_scientist_technology_action_triggers.txt`.

Static technology evidence is in `common/technologies/016_brilliant_scientist_project_technologies.txt` and `common/technologies/016_brilliant_scientist_project_force_technologies.txt`.

Unit and chassis evidence is in `common/units/016_brilliant_scientist_project_forces.txt` and `common/script_constants/016_brilliant_scientist_project_force_constants.txt`.

Portal reservation and outcome ownership remains in `common/raids/016_brilliant_scientist_portal_raids.txt` and `common/scripted_effects/016_brilliant_scientist_raid_effects.txt`.

The cross-subsystem registry now includes `conventional_technology_packages` in `common/scripted_effects/chaosx_dynamic_effects.md`.

## Current implementation disposition

| Surface | Current source fact | Documentation disposition |
| --- | --- | --- |
| Custom technology API | The existing API retains 18 custom technology IDs: seven operational packages, seven weaponization packages, and four xeno-control technologies. | Kept as the custom API surface without adding conventional families or vanilla technology/history grants. |
| Conventional package API | Six existing families are Computation, Electronics, Materials, Rocketry, High Energy, and Biomedical, with Deployment and Weaponization tiers. | Documented as a separate API with durable neutral flags, separate provenance arrays, full-strength existing stage modifiers, and one shared computation-slot owner. |
| Runtime bridge | `chaosx_reconcile_custom_technology_runtime` now calls `chaosx_reconcile_conventional_technology_runtime` after the custom xeno and project-force reconciliation. | Documented as reconciliation of already-held conventional flags; it does not fabricate missing conventional grants. |
| Strategic actions | Eight existing actions use neutral weaponized-family flags through the ordinary `conventional_technology_operations` category. | Documented as an existing consumer boundary; payment, targets, timers, cancellation/refund, cooldown, and AI ownership remain separate from package reconciliation. |
| Random selector | The custom random helper remains exactly seven families: Portal, Clone, Robot, Paleogenetic, Xenobiological, Alien Infantry, and Temporal. | Explicitly kept separate from the six-family conventional API; no extra random branch, technology, or family was added. |

## Contradictions corrected

- The custom API power table was replaced with values read directly from the current operational and weaponization technology blocks, including the positive Paleogenetic supply burden, Alien landing-only/tactic behavior, and the four xeno-control values.
- The unit context now cites the current reusable robot chassis constants rather than the stale power summary, including hardness 0.88, armor 70, breakthrough 60, defense 50, soft attack 36, hard attack 30, piercing 75, and speed 7.
- Revocation advice was removed: durable learned flags and external knowledge/source provenance are permanent historical state, and callers must not clear them; the documented xeno stale-alternate cleanup is the narrow exception.
- Trainability wording now describes ordinary recruitment as constrained by package equipment, manpower, fuel, production, and normal trainability, with no API-wide artificial division cap; free or event-spawned formation caps remain separate, and Alien Infantry remains landing-only.
- The model note now records the approved geometry-preserving/manual-recovery path and does not describe paid regeneration as the current requirement; seven model runtime packages remain unaccepted.
- Portal documentation describes the current native delete/recreate path: successful landing destroys the assigned origin formation and creates a full-readiness target formation with 0.50 experience, while the source does not establish carried equipment/manpower conservation. Conservation remains unresolved pending explicit user approval and is not represented as accepted unit teleportation.
- Native raids continue to own reservation, collection, cancellation, expiry, outcome, and history; the Portal documentation does not move that ownership into the conventional API.

## Open dispositions and blockers

| Item | Disposition | Remaining limitation |
| --- | --- | --- |
| Conventional package source and docs | Source-backed and documented for parent review. | Parent still owns final integration and completion claims. |
| Technology MCP inspection | Read-only structural scan and narrow explanation were run. | Scan returned `validation=false` with 1,427 blocking technology diagnostics, so it is not engine acceptance. |
| Random-family probability evidence | The earlier exact seven-candidate artifact remains recorded in `016_final_conventional_api_probability_baseline_2026-09-02.md`. | The fresh broad source inspect found 18 candidates, `poolComplete=false`, and one unresolved item; dynamic weights/effective probabilities remain partial or unsupported, with no comparison acceptance. |
| Portal conservation | Current source behavior is documented without an invented conservation rule. | User approval is still required before any delete/recreate conservation design can be treated as accepted. |
| Model packages | Geometry-preserving manual recovery is authorized. | Seven production runtime packages, final wiring, and runtime acceptance remain open. |
| Other closure gates | Focus/reward and AI review, GUI state/resolution evidence, final MCP/auditor comparisons, engine/live user acceptance, and catalog/presentation synchronization remain open under the contract. | This handoff does not close or waive any of those gates. |

One source-comment inconsistency remains outside this documentation scope: the header of `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt` still describes a “matching capped locked template,” while current runtime comments and implementation describe ordinary recruitment without an API-wide division cap; the parent should reconcile that source comment separately.

## Evidence and validation

The required offline Paradox wiki pages and applicable vanilla documentation were consulted before editing; the vanilla technology-specific documentation filename requested by convention was not present in the installed documentation directory.

The technology scan artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7483eec1a361e063d7ea773118f58f84e9f68df16f0ea1992ff2f1744c6334fd/60807a7beb3f996c70022ba7491da6e33b20e3f2e35ce8a62630631e0b9a30ff/technology-scan-02712a52b0ad.json` and reports 679 technologies, 18 folders, 1,427 blocking diagnostics, and failed validation.

The narrow technology explanation artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/227b746d60ab67dc726cf9d3d759ca14e445bd1609fdd88474c19b83e3236878/edad4abdafb7e04d8a24bcc04d3b9b821f4c1646b634231c47d3edd48db47c87/technology-explain-0d63df11607d.json`.

The fresh broad probability artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c4e08b019785dd3154052d14134d4a09d21846d439b3a6b2092f35dfd92d40d9/7f623bb5df1e90294a36fadbe4d41eaaaba2af92a6b82444ebdf317d71dbed97/probability-inspect-b094a3b333e6.json` and reports 18 candidates, zero available under its required inputs, one unresolved item, and `poolComplete=false`.

The prior corrected seven-candidate probability artifact is retained by `016_final_conventional_api_probability_baseline_2026-09-02.md`; its inspection was complete for the seven branches, but dynamic temporary weights and effective probability acceptance remain unresolved.

Targeted source checks confirmed the six conventional family flags, eight action IDs, seven random branches, conventional reconcile call, category path, and absence of stale positive revocation/model wording in the reconciled docs.

No game was launched, no logs were requested, no gameplay/config/assets/spreadsheet/provider files were changed, and no commit or staging operation was performed.

## Files changed

- `docs/events/016_brilliant_scientist/systems/custom_technology_api.md`
- `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.md`
- `common/scripted_effects/chaosx_dynamic_effects.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_final_conventional_api_docs_2026-09-02.md`

The source implementation, workbook, unrelated documentation, and final acceptance evidence were intentionally left unchanged.

## Parent follow-up

The parent should review the remaining source-comment cap wording, obtain the unresolved MCP and probability comparisons, finish model/focus/AI/GUI/catalog gates, and retain the explicit Portal conservation approval question before making any final closure claim.
