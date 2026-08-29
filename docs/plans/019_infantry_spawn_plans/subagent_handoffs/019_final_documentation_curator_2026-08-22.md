# Event 19 final documentation curator handoff — 2026-08-22

## Scope and result

This documentation-only reconciliation covers Event 19 specs, event docs, derivative-country docs, registry and classifier docs, asset manifests and GFX handoffs, achievement and scenario docs, current provider handoffs, historical prompts, and stale closure or GUI wording.

No gameplay, event, focus, decision, scripted-effect source, localisation, binary asset, spreadsheet/CSV, `.codex`, or `.qoder` file was edited by this curator.

The current source-of-truth ledger is `docs/plans/019_infantry_spawn_plans/source_of_truth_map.md`.

## Current source-of-truth facts recorded

- Event 19 is ID `19`, classification `Minor Repeatable`, unclustered, nonterminal, and has no fixed derivative tag.
- The live direct scenario is `SCN-013`, The Unbidden Muster, because proposed `SCN-008` is owned by Independence Wave.
- The accepted runtime player surface is ordinary decisions and decision categories only, with no Event 19 scripted GUI.
- The shared `infantry_spawn_ordinary_management_category_is_relevant` trigger hides the Formation Management and claimant categories after a completed takeover or achievement-marked claimant or derivative revolt even if another claimant row remains; peaceful closeout remains available until live obligations, formations, claimants, transactions, and management operations clear, and Evolution III or IV capability flags alone do not keep the ordinary categories open.
- Event 19 owns exactly `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt` for its registry code.
- The live dynamic registry contains 19 providers: `501-514`, `518`, and `520-523`, with one registration plus thirteen callbacks per provider.
- The live owner publishers expose 20 custom equipment-token identifiers across the 19 custom profile values `130-148`; providers 504 and 522 intentionally share profile `142` while retaining distinct provider identities.
- The accepted provider census is 96 land sub-units: 49 combat and 47 support, with 43 support-only definitions parent-owned unless explicitly attached by a provider.
- Provider 513 is readiness-manifest and bounded-startup wired through Event 12 but remains package-gated until `africa_strange_formation_package_ready` is set.
- Provider 523 is Event 014-owned and the accepted Event 19 coverage record counts eight cannibal combat bodies.
- A future family contributes one owner-side registration plus the complete callback contract and CXT setup registration, without an Event 19 family-list, equipment-selector, localisation-selector, picture-selector, or second registry-file edit.
- Claimant identity is male-only at runtime under `019_male_claimant_identity_correction_handoff_2026_07_16.md`; earlier female-profile and female-commander claims are rejected historical evidence.
- Derivative opening local assets are reconciled by `infantry_spawn_derivative_reconcile_starting_local_assets`, which persists transferred-state industry, population, infrastructure, rail, ports, supply, resources, standard stockpiles, private-ledger liabilities, active formations, and owner-published custom-equipment token and amount arrays.
- The derivative local-asset audit classifies fragile, strained, or viable from `constant:infantry_spawn_derivative_opening_asset`, adds only the temporary fragile-start shortfall idea, and never creates factories, infrastructure, supply assets, or a generic economy grant.
- `infantry_spawn_derivative_resolve_opening_local_asset_shortfall` is called by `infantry_spawn_derivative_inventory_the_seized_districts`, removes the temporary idea, and sets the resolved proof flag without erasing opening measurements.
- All eleven Event 19 achievements are visible in the live registry, including the four controlled-trial achievements whose obsolete `hidden = yes` entries were removed; dated handoffs that call them hidden or unawarded are archival evidence only.
- The restored `docs/assets/019_infantry_spawn/` package contains 1,434 files, including the historical source, processed, checksum, crosswalk, contact-sheet, and manifest records; its former GUI rows and 2026-07-18 completion language are archival evidence only. The three authored frame-sheet animation packages are complete archival deliverables with retained frame-000 static fallbacks and no current scripted-GUI consumer.
- The coal-golem model document is now explicitly a separate non-gating visual extension: provider 503 uses the live `sprite = infantry` unit and existing counters, while the optional custom 3D mesh/entity remains blocked by rigging failure and is not required by the Event 19 specification.

## Files changed

### Current ledgers and feature documentation

- `docs/plans/019_infantry_spawn_plans/source_of_truth_map.md` now records the current runtime boundary, male-only identity authority, local-asset contract, provider inventory, historical asset evidence, MCP limitations, plan dispositions, and superseded-document routing.
- `docs/events/019_infantry_spawn/overview.md` now records the 19-provider boundary, eight provider-523 bodies, parent-owned support-only boundary, decisions-only surface, SCN-013 identity, exact terminal-versus-peaceful category lifecycle, local-asset reconciliation, and historical asset/catalog status.
- `docs/events/019_infantry_spawn/systems/triggerable_scenario.md` now records the current scenario/provider boundary and decisions-only UI status.
- `docs/events/019_infantry_spawn/systems/unit_family_coverage.md` now records 96 land sub-units, 49 combat units, 47 support units, eight accepted provider-523 bodies, and the unresolved ninth `cannibal_bone_riders` source-template discrepancy.
- `docs/achievements/019_infantry_spawn/achievements.md` now states the current ID, scenario, decisions-only boundary, and all-eleven-visible achievement status.
- `docs/specs/019_infantry_spawn_specs/matrices/019_achievement_matrix.md` now marks all eleven achievements visible, while dated hidden/unawarded achievement handoffs are explicitly superseded.
- `docs/specs/019_infantry_spawn_specs/README.md` now routes current provider status, SCN-013, decisions-only runtime behavior, historical asset evidence, and open gates.
- `docs/specs/019_infantry_spawn_specs/specs/019_infantry_spawn_spec_part_4_evolution_iii.md` now describes decision-based Evolution III management and marks former GUI animation requirements archival.
- `docs/specs/019_infantry_spawn_specs/specs/019_infantry_spawn_spec_part_5_evolution_iv.md` now describes registry-backed decision groups instead of a runtime Muster Board.
- `docs/specs/019_infantry_spawn_specs/specs/019_infantry_spawn_spec_part_6_derivative_countries.md` now documents both derivative local-asset effects and the no-generic-grant contract.
- `docs/specs/019_infantry_spawn_specs/specs/019_infantry_spawn_spec_part_7_decisions_ui_ai_balance.md` now uses selected-lot decision terminology, records exact terminal-versus-peaceful category lifecycle, and retains its explicitly archived GUI section.
- `docs/specs/019_infantry_spawn_specs/review/decision_only_surface_addendum_2026-08-05.md` now records the shared terminal relevance stop for takeover or achievement-marked claimant/derivative revolt and the separate peaceful closeout path.
- `docs/specs/019_infantry_spawn_specs/specs/019_infantry_spawn_spec_part_8_scenario_interactions_acceptance.md` now marks former GUI assets and controls archival and makes decisions-only acceptance explicit.
- `docs/specs/019_infantry_spawn_specs/matrices/019_evolution_entry_cleanup_matrix.md` now replaces the Evolution III GUI entry with the Formation Ledger decision category and clarifies selection-cache cleanup.
- `docs/systems/cbrn_warfare/chaos_unit_family_registry.md` now records the 19-provider, eight-body provider-523, parent-owned support-only, CXT, and decisions-only boundaries and removes current-sounding Board lifecycle wording.
- `common/scripted_effects/chaosx_dynamic_effects.md` now documents both derivative local-asset effects with scope, inputs, outputs, defaults, side effects, and usage examples while identifying the actual owner source file.
- `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_dynamic_unit_provider_decision_audit_2026-08-22.md` and `019_final_catalog_alignment_2026-08-22.md` now carry the current terminal-versus-peaceful category lifecycle and the latest decision-audit disposition.

### Review, prompt, and historical-routing documentation

- `docs/specs/019_infantry_spawn_specs/review/blockers_and_uncertainty.md`, `review/spec_completion_audit.md`, `review/mandatory_improvement_loop_review.md`, `review/anti_bloat_and_scope_boundaries.md`, and `review/manual_subagent_role_reviews.md` now separate historical 2026-07-18 closure evidence from current provider-extension and documentation gates.
- The five Event 19 prompts under `docs/specs/019_infantry_spawn_specs/prompts/` now carry archival or superseded notices for the former GUI and route current work to the source-of-truth map and current provider handoffs.
- The 2026-07-18 closure/addendum documents and the historical API-referencing handoffs now point at current provider documentation instead of the removed `.tmp/event19_docs_curator_current.md` note.
- Former GUI handoffs under `docs/plans/019_infantry_spawn_plans/subagent_handoffs/` now carry archival notices, including `019_muster_board_gui_decision_audit_2026_08_05.md`, `019_muster_board_runtime_border_cleanup_2026-08-05.md`, and the seven 2026-07-28 or compact-background GUI handoffs.
- Additional dated handoffs now carry the decisions-only boundary where they referenced the former GUI: the triggerable-scenario, ordinary-category lifecycle, exact-settlement, neutral-muster asset, performance/isolation, parent-implementation, five decision/mission audit, localisation/asset, AI/balance, and army-asset handoffs.
- The three 2026-07-18 regional raw-flag handoffs now label their `Fully Functional` and no-closure statements historical for the bounded asset tranche.
- `019_final_claimant_identity_closure_2026_07_16.md` and `019_claimant_identity_specialist_reaudit_2026_07_16.md` now explicitly supersede their female-profile and female-commander claims in favor of the male-only correction handoff.
- `019_catalog_workbook_reconciliation_2026_07_18.md` now carries a historical catalog notice and routes current alignment to `019_final_catalog_alignment_2026-08-22.md`.
- Dated achievement, decision/mission, localisation, parent-audit, improvement-loop, and final-completion handoffs now state that their four-hidden or unawarded achievement wording is superseded by the current all-visible registry.

### Asset documentation

- `docs/assets/019_infantry_spawn/manifest.md` and `gfx_handoff.md` now distinguish restored historical provenance from active runtime proof and state that former GUI assets have no runtime consumer.
- The three nested former-GUI background GFX handoffs and three animation briefs now carry archival notices.
- The compact, rebuild, and richer background manifests now use archival status, and the richer `metadata.json` now identifies the former GUI asset as archival with no live consumer.
- No binary asset was deleted, regenerated, or edited.

## Plan and handoff disposition

| Plan or handoff | Disposition | Evidence or remaining work |
| --- | --- | --- |
| `019_dynamic_unit_provider_api_completion_2026-08-22.md` | implemented/current evidence | Records 19 providers, 49 combat units, eight provider-523 bodies, owner-side future-family onboarding, and 43 parent-owned support-only definitions; the whole-event gate remains open. |
| `019_dynamic_unit_provider_decision_audit_2026-08-22.md` | queued with reason | Its continuation resolves dynamic obligation visibility, four-or-fewer ordinary request rows, icon-first provider costs, and mission-slot gating. Owner approval remains required for the truthful exact standardization/settlement four-type presentation, while category-density save-state proof and the parent-owned decision/localisation integration pass remain open. |
| `019_dynamic_unit_provider_localisation_audit_2026-08-22.md` | implemented for bounded scope; integration review open | Provider presentation-token migration is complete in its scope, while decision-audit integration findings remain parent-owned. |
| `019_dynamic_unit_provider_probability_audit_2026-08-22.md` | blocked by tool limitation | The named probability-auditor route is unavailable and the provider pool has no normalized candidates. |
| `019_final_derivative_country_audit_2026-08-22.md` | open with documented blockers | Local-asset reconciliation and restored provenance supersede audit-time gaps; normalized probability evidence and strict ghost weakness proof remain unresolved. |
| `019_final_focus_tree_audit_2026-08-22.md` | implemented with non-blocking warnings | The local-asset resolver call is documented and the parent owns remaining focus-warning disposition. |
| `019_final_catalog_alignment_2026-08-22.md` | implemented, historical catalog authority only | Event 19 and SCN-013 rows are aligned, but the historical `Fully Functional` snapshot does not close current provider validation. |
| `019_decision_only_surface_2026-08-05.md` | promoted to current spec | This is the accepted runtime UI decision: ordinary decisions and categories only, with former GUI artifacts archival. |
| `019_achievement_completion_pass_handoff.md` and dated achievement audits | superseded historical visibility | Their four-hidden or unawarded wording predates the owner removal of `hidden = yes`; current all-eleven visibility is recorded in the achievement matrix and achievement documentation. |
| Old closure, GUI, and identity handoffs | superseded by named current docs | Historical evidence is preserved, but it must not be routed as an active implementation instruction. |

## Contradictions and unresolved documentation blockers

1. `docs/events/019_infantry_spawn/systems/unit_family_coverage.md` accepts eight provider-523 combat bodies, while `common/scripted_effects/014_cannibalism_effects.txt` still names `cannibal_bone_riders` in addition to those eight; the parent must reconcile the provider template, CXT inventory, and Event 014 documentation before treating the 49-combat census as final.
2. The decision audit now records dynamic custom-equipment cost presentation as resolved, while category-density save-state proof and the coordinated decision/localisation integration remain open even though the bounded localisation audit reports provider presentation-token coverage complete.
3. The named `chaosx_ai_probability_auditor` route is unavailable in this runtime, and direct MCP adapters do not normalize the 19-provider pool, so no exact provider odds or balance certification is documented.
4. The derivative ghost starting template uses the same four `death_weak_ghost_host` rows as the Death parent template, so strict weaker-than-parent proof remains unresolved even though isolation, decline, and route bounds are documented.
5. The restored asset package resolves the audit-time missing-provenance claim, but its historical PASS and catalog status remain bounded evidence and do not certify the current provider extension. The three frame-sheet packages are complete authored archival outputs with frame-000 static fallbacks, not active Event 19 GUI wiring.
6. The former GUI MCP surface is intentionally not current runtime work; a fresh read-only inspect against the historical `infantry_spawn_muster_board_window` identifier returned `GUI_INSPECTED` with zero inspected Event 19 elements, one missing and one approximated fidelity item, and global source/validation diagnostics truncated at the fixed 2,000-result ceiling. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/914ce3f03e91ed43b86b1545d73870f090c20102a5756faba685bddafddcbaf9/dc265e14c48c42b6f5f7fd71ea4ad80a70db523f9a9623406daec9dbd471c286/gui-inspect.4a7b909e843b8b82.json`. Archived GUI handoffs retain prior `SCAN_BYTE_LIMIT` evidence and must not be used to reopen a GUI implementation task.
7. Earlier female-profile and female-commander handoffs are preserved as evidence but superseded by the male-only correction and must not be used to design current claimant identity.
8. The former custom coal-golem 3D model blocker is explicitly a separate non-gating visual extension; it is not an Event 19 provider or completion blocker because the current `coal_golem` unit uses `sprite = infantry` and the Event 19 specification does not require a custom mesh/entity package.

## Duplicate or superseded documents

- Former Muster Board specifications, prompts, GUI handoffs, background manifests, animation briefs, and GUI MCP reviews are retained as archival provenance and routed by the decision-only addendum.
- The 2026-07-18 `Fully Functional` catalog, final-completion, regional-remediation, and closure handoffs remain historical tranche evidence rather than current whole-event status.
- The two claimant identity audits named above retain rejected female identity evidence and are superseded by the male-only correction handoff.
- Dated achievement completion, tracking, decision/mission, localisation, parent-audit, improvement-loop, and final-completion documents retain the former four-hidden/unawarded status as historical evidence only; the current visible registry is authoritative.
- The removed `.tmp/event19_docs_curator_current.md` reference was eliminated from the reviewed Event 19 plans and handoffs.

## Stale prompt or instruction list

- `019_infantry_spawn_goal_prompt.md`, `019_infantry_spawn_coding_prompt.md`, `019_infantry_spawn_decision_mission_prompt.md`, `019_infantry_spawn_asset_prompt.md`, and `019_infantry_spawn_achievement_prompt.md` are now visibly archival or superseded and route active work to current docs.
- Former GUI instructions inside the prompts remain only as labeled design provenance and must not be executed.
- The source spec parts and matrices now identify former GUI terms as historical where they remain for design traceability.

## Markdown hard-wrap audit

The targeted audit found pre-existing mid-sentence hard wraps in long historical or source prose in `source_of_truth_map.md`, the Event 19 overview and scenario/unit-coverage docs, the derivative spec, the source README, the review files, the registry classifier doc, the asset manifest/GFX handoff, and several dated handoffs.

New current-boundary and derivative local-asset paragraphs were written as one physical line, and no Markdown table, list, heading, quote, or code-block structure was flattened.

The remaining historical-body hard wraps were left unchanged to preserve dated audit evidence and avoid broad reformatting of concurrent work; they remain a documentation-hygiene follow-up rather than a runtime contradiction.

## Validation performed

- Read-only `hoi4.event_inspect` for `chaosx.nr19.1` returned `EVENT_INSPECTED_PARTIAL` with no blocking diagnostics and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/568dc44f09d8ed2b886eb449235559a9d2dc28541918f2dedcc2e72a7f6490f8/527beb2e1a085d1e08c72ad44022dcd4ba243f9cc11495d0e369df28db7aabf6/event-scan-23147097ed55.json`.
- A fresh read-only `hoi4.focus_inspect` call for `infantry_spawn_derivative_focus_tree` and `common/national_focus/019_infantry_spawn_derivative_focus.txt` timed out after 180 seconds; the exact limitation is recorded in the source-of-truth map.
- A fresh read-only `hoi4.gui_inspect` call for the historical `infantry_spawn_muster_board_window` returned `GUI_INSPECTED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/914ce3f03e91ed43b86b1545d73870f090c20102a5756faba685bddafddcbaf9/dc265e14c48c42b6f5f7fd71ea4ad80a70db523f9a9623406daec9dbd471c286/gui-inspect.4a7b909e843b8b82.json`; it found zero inspected Event 19 elements, one missing and one approximated fidelity item, and hit global source/validation diagnostic truncation, so it is limitation evidence rather than current GUI proof.
- All four restored background JSON manifests/metadata files parse with `ConvertFrom-Json`, and the richer background now reports `archival_superseded` status with no live consumer.
- The restored asset package path checks passed for `manifest.md`, `gfx_handoff.md`, regional raw flags, spot masters, validation JSON, and checksum records, with 1,434 files present.
- A targeted source scan of the owner-side `event19_publish_custom_equipment_tokens` callbacks found 15 publisher blocks and 20 unique custom equipment-token identifiers, confirming the live count recorded above rather than relying on an earlier tranche summary.
- A targeted `rg` check found no remaining `.tmp/event19_docs_curator_current` reference in the reviewed Event 19 docs, plans, assets, or achievement docs.
- A targeted source audit confirmed that `infantry_spawn_ordinary_management_category_is_relevant` is used by both the Formation Management and claimant categories and excludes completed takeover and achievement-marked claimant or derivative revolt.
- The 2026-08-22 decision-audit continuation was re-read after its remediation update; dynamic obligation visibility, ordinary request normalization, icon-first costs, and mission-slot gating are resolved there, while the exact standardization/settlement four-type policy remains an owner-approval blocker.
- A targeted stale-term audit found remaining `Fully Functional` and no-closure phrases only in explicitly historical or superseded contexts, with the current source map and top notices routing readers away from those claims.

## Skipped meaningful validation

- The fresh GUI inspect above was recorded only as archival limitation evidence because the accepted runtime has no Event 19 scripted GUI; no GUI render or current runtime wiring claim was made. The result includes unrelated global index collisions and truncated diagnostics, so it cannot certify the former window.
- No probability compare, sweep, simulation, or sequence pass was run because the required named probability-auditor route is unavailable and the provider pool remains unresolved.
- No in-game validation was run, as it belongs to the parent/user runtime boundary.

## Recommended parent decisions

1. Reconcile the provider-523 eighth-versus-ninth source token discrepancy before finalizing the combat census.
2. Review the decision audit's remaining exact standardization/settlement four-type policy and category-density save-state limitation; dynamic custom-equipment cost presentation and ordinary request normalization are already recorded as implemented.
3. Obtain a callable probability-auditor route or explicitly carry the normalized-odds blocker into the final report.
4. Decide whether the ghost package-level weakness interpretation is accepted or whether the starting template needs owner-side tuning and re-audit.
5. Keep the restored asset package and all former GUI material archival unless the accepted runtime surface is intentionally changed by a new parent decision.

## Completion and uncertainty

The documentation reconciliation is complete for the requested scope, and the required source-of-truth map and handoff are present.

The Event 19 gameplay/provider feature is not claimed complete by this handoff because the provider-extension, probability, decision/localisation integration, provider-523 census, ghost weakness, and final documentation gates remain open as listed above. The staged decision-auditor exact-settlement/standardization redesign remains open pending owner resolution of its truthful four-type presentation policy and currently reported hard-cost-budget blocker.

No gameplay simplification or fallback was introduced by this documentation work.

No resume packet was created because `source_of_truth_map.md` is the current ledger and the parent has the exact unresolved decisions above.
