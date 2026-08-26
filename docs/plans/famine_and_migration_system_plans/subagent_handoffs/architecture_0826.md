# Famine and Migration Architecture Audit

## Scope and evidence

This is a bounded current-state architecture audit of the separate famine and migration systems as of 2026-08-26.

The audit read `AGENTS.md`, `.agents/skills/chaos-redux-state-ledgers/SKILL.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, and `.agents/skills/chaos-redux-events/SKILL.md`.

The eight design specifications read were `famine_and_migration_system_spec_part_1_core.md`, `famine_and_migration_system_spec_part_2_famine_food_security.md`, `famine_and_migration_system_spec_part_3_displacement_migration_return.md`, `famine_and_migration_system_spec_part_4_deaths_occupation_atrocity.md`, `famine_and_migration_system_spec_part_5_historical_profiles.md`, `famine_and_migration_system_spec_part_6_decisions_ai_presentation.md`, `famine_and_migration_system_spec_part_7_cross_system_connections.md`, and `famine_and_migration_system_spec_part_8_balance_acceptance.md`.

The supporting current-state records read were `completion_report.md`, `source_of_truth_map.md`, `current_owner_blocker_reaudit.md`, `handoff_dispositions.md`, `namespace_separation_validation.md`, `event_free_validation.md`, `mapmode_validation.md`, and `resume_packet.md`.

The offline wiki pages consulted were Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.

The vanilla references consulted were `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, `documentation/script_concept_documentation.md`, and `common/script_constants/documentation.md`.

The source census covered the current famine, migration, civilian-transfer, humanitarian effect and trigger files, their constants, `common/on_actions/humanitarian_runtime_on_actions.txt`, the two separate decision files and categories, both state map modes, and the existing report-header surfaces.

## Current invariant findings

| Invariant | Current evidence | Result |
| --- | --- | --- |
| Famine and migration stay separate at runtime | `source_of_truth_map.md`, `common/decisions/famine_decisions.txt`, `common/decisions/migration_decisions.txt`, and `common/map_modes/chaosx_state_map_modes.txt` define separate `famine_*` and `migration_*` categories and map modes. | Preserved. No combined namespace, category, map mode, event, or pacing row was introduced. |
| Movement is not death | `common/scripted_effects/civilian_transfer_effects.txt:369-516` performs one measured origin population loss, derives a separately clamped route-death slice, and credits only the survivor remainder. | The neutral primitive matches the required conservation model. Its Deaths write is deferred to commit accounting and is not a second population loss. |
| Exact origin debit and survivor credit | `civilian_transfer_civilians_exact` measures `state_population_k` before and after `apply_state_population_loss_without_recruitable_manpower_gain`, then calls `civilian_transfer_apply_destination_credit` only for positive survivors. | Preserved in the shared primitive. Destination credit and owner/controller manpower reconciliation are measured. |
| Fail closed on missing proof | `common/scripted_triggers/civilian_transfer_triggers.txt:8-82` requires positive request, actor, route, destination, host, role, reception, bind, and conservation proof. `civilian_transfer_rollback_transaction` quarantines failed atomicity. | Preserved in the neutral contract. Generic source adapters without proof remain API-only. |
| No whole-world recurring scan | `common/on_actions/humanitarian_runtime_on_actions.txt:29-42` limits recurring repair to `on_daily_CXT` and an initialized CXT country. Other callbacks use exact countries or owned states. | No new daily, weekly, or monthly world scan was found. The startup `every_country` baseline is one-time setup, not recurring movement processing. |
| No fake route or amount | `civilian_transfer_route_request_is_valid` requires a saved destination target and explicit route proof. The exact primitive clamps to measured debit and records residual failure. | Preserved in the neutral primitive. A caller cannot legitimately bypass route or amount proof. |
| Event-target lifetime | The transfer uses regular chain-local targets such as `civilian_transfer_route_destination` and `civilian_transfer_physical_origin`. The finalizer calls `civilian_transfer_abort`; corridor and staged-cohort owners clear their own targets and proofs. | No new global event target was added. Cleanup design is compatible with the vanilla distinction between regular and global event targets. |

## Proven source gap and patch decision

No gameplay source was patched by this subagent.

The exact neutral entry point is `civilian_transfer_execute_transaction` at `common/scripted_effects/civilian_transfer_effects.txt:992`.

The concurrent forced-movement caller invokes the undefined `civilian_transfer_execute_exact_transaction` at `common/scripted_effects/migration_forced_movement_effects.txt:218`.

The concurrent spontaneous-movement caller invokes the same undefined entry point at `common/scripted_effects/migration_spontaneous_movement_effects.txt:280`.

The concurrent corridor evacuation caller invokes the same undefined entry point at `common/scripted_effects/humanitarian_corridor_effects.txt:567`.

Those callers also reference undefined constant categories including `migration_runtime`, `migration_route_result`, `civilian_transfer_population`, `civilian_transfer_reconciliation`, `humanitarian_presentation`, `migration_modifier`, `migration_pressure_source`, and `famine_to_migration_food_stage` in the new split source files and destination-selection triggers.

The defined current categories include `humanitarian_runtime`, `humanitarian_population`, `humanitarian_pressure_source`, `migration_core_reconciliation`, `migration_state_modifier`, `migration_presentation`, and `famine_food_stage`.

This is a cross-file source migration rather than an isolated missing invariant. Adding `civilian_transfer_execute_exact_transaction` as a compatibility wrapper would violate the explicit adapter-only and no-alias boundary, while fixing only one caller would leave the other exact lanes and their constants unresolved.

The split migration files are concurrent untracked work in this worktree, so a partial rename would also risk overwriting the parent implementation. The safe decision is to leave the sources unchanged and fail closed until the parent-owned canonicalization pass is complete.

## Proposed helper map

| Helper | Scope | Inputs | Outputs | Side effects | Exact callers |
| --- | --- | --- | --- | --- | --- |
| `civilian_transfer_preflight` | Origin state | Positive people request, destination event target, route and actor proof, cohort id, role, bind mode, reception mode, obligation proof | Preflight validity and proof receipts | Saves only chain-local physical-origin context and reads aligned rows and headroom. | Forced, spontaneous, corridor, and decision adapters. |
| `civilian_transfer_civilians_exact` | Origin state | Preflight receipt and staged transfer inputs | Actual origin debit, route-death slice, survivor request, destination actual credit, conservation residual | Applies one measured origin loss and invokes destination credit for survivors only. It does not bind a cohort or commit Deaths. | Sole population mutation primitive for movement. |
| `civilian_transfer_apply_destination_credit` | Destination state | Positive survivor request and valid destination | Measured destination credit and post-credit population | Adds exact state population and corrects owner/controller manpower side effects. | Called only by `civilian_transfer_civilians_exact`. |
| `civilian_transfer_finalize` | Origin state with destination target | Pending exact debit, source and destination reception receipts, role-correct bind receipt, conservation zero | Finalize-valid receipt and projection receipt | Updates cohort host, settles proven paired obligations, records projection and presentation, commits the route-death slice once, and clears chain-local inputs. | Shared owner wrapper after every exact adapter transaction. |
| `civilian_transfer_rollback_transaction` | Origin plus destination target | Partial reception, destination credit, and measured debit receipts | Rollback-valid receipt or atomicity quarantine | Inverts reception and destination credit, restores the full measured debit, and quarantines both ends if inversion is not exact. | Shared owner wrapper after a failed post-debit finalize. |
| `migration_execute_forced_transfer_exact` | Origin state | Camp/deportation actor, fixed destination, positive amount, cause, custody, route-death proof, cohort and policy proof | Forced-transfer result and exact receipts | Stages one cohort and delegates all physical accounting to the neutral primitive. | Forced-movement owner. |
| `migration_process_spontaneous_movement_owner` | Registered origin state | Bounded flight or internal-displacement pressure, adjacent destination proof, actor, policy, and capacity proof | Spontaneous result or trapped rejection | Stages one cohort, invokes the neutral primitive, or records trapped population without a debit when no route is proven. | Registered displacement-state job. |
| `humanitarian_corridor_execute_evacuation` | Corridor origin state | Persisted front, corridor route proof, cohort, amount, actor, reception, and bind proof | Corridor transaction result | Binds the exact front and delegates evacuation population accounting to the neutral primitive. | Corridor owner only. |

## Constants and tuning plan

Keep shared transaction enums and zero/one values in `humanitarian_runtime`, `humanitarian_population`, `civilian_transfer_route_result`, and `migration_core_reconciliation`.

Keep famine stages, mortality, food reserves, and famine pressure tuning in the famine-owned `famine_*` categories.

Keep migration capacity, pressure, route, custody, presentation, and decision tuning in migration-owned `migration_*` categories.

Use `humanitarian_pressure_source` only as the narrow source enum crossing the explicit famine and migration adapters.

Resolve the stale categories by an owner-reviewed source migration to canonical categories, not by adding aliases or a combined category.

The `famine_to_migration_food_stage` read requires an explicit famine-to-migration adapter receipt before migration capacity can consume it; a new constant alias alone would not prove that boundary.

Do not alter AI, mission, random, or probability weights in this architecture pass.

## Event-target and cleanup plan

Use regular event targets for one transfer chain, including the origin, destination, corridor front, and current cohort host pointers.

Do not promote a route destination or source owner to a global event target merely to bridge a caller rename.

On rejection or zero debit, call `civilian_transfer_abort` and clear the caller's staged request variables.

On failed binding or failed exact transfer, remove the staged cohort row and destination proof through the owning forced, spontaneous, or corridor cleanup helper.

On failed post-debit finalization, require `civilian_transfer_rollback_transaction` to restore the exact debit and inverse every measured destination and reception delta before clearing the chain.

Leave durable cohort history, presentation receipts, and Deaths accounting to their current owners after a valid finalization only.

## Migration plan from duplicated or stale callers

First, the parent should freeze the concurrent split files and produce an explicit symbol mapping from each stale category to a current category or an owner-local adapter output.

Second, update all exact movement callers together so forced, spontaneous, and corridor lanes call the one canonical `civilian_transfer_execute_transaction` entry point and use the same finalize receipt.

Third, update the corresponding markdown helper contracts and scripted triggers in the same change so source and documentation do not advertise the removed exact-entry alias.

Fourth, run definition/caller and constant-category scans across all current `common` sources and reject any remaining undefined helper or category rather than creating compatibility aliases.

Fifth, run the bounded source and engine inspections for the canonical movement callers, then perform owner-level scenario validation only after the source migration has a complete proof bundle.

## Validation and artifacts

The shared primitive and caller census were checked with targeted `rg` scans and line-numbered source reads.

Vanilla documentation confirms that `state_population_k` is state-scoped, `add_manpower` supports state and country scopes, and regular and global event targets are distinct operations.

The current read-only map inspection returned `MAP_INSPECTED` for workspace `mod_chaos_redux_ea3b2d67c2c0` and produced `map-inspect.642761179b3ee6b4.json` plus overview artifacts at the following URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1b704da63c3a62e08dd6ba06367b08b8975493159d55ec983123625c7b3c93c4/1ef0a8a32fae8515171188b8d7b9f9e39188baf03af326e06aeb8023840abb85/map-inspect.642761179b3ee6b4.json`.

The map inspection aggregate remains false because unrelated `MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID` diagnostics were truncated from `map/buildings.txt`; no map source was changed.

The current report-header GUI route was attempted read-only, but the first request was rejected because `windowName` and `scenario` must be supplied together and the follow-up current-window requests did not return an artifact before the audit was stopped.

Existing split-header GUI artifacts and the GUI limitation are already recorded in `completion_report.md` and `mapmode_validation.md`; no GUI source was changed.

No live game validation was run because live consumer validation belongs to the user.

No probability baseline or compare was run because this audit changed no weighted surface and the current probability evidence remains explicitly unresolved in `completion_report.md` and `current_completion_audit.md`.

## Blockers and risks

The undefined exact-entry helper and stale constant categories block the forced, spontaneous, and corridor movement lanes from being treated as executable current source.

Generic occupation-law, strategic-bombing, war/peace, cluster, scenario, and relief-obstruction adapters remain definitions without complete owner proof or exact callers as recorded in `current_owner_blocker_reaudit.md` and `completion_report.md`.

The strategic-bombing attribution and amount, war/peace cohort and amount, and generic dispatch facts are unsupported until an owner supplies exact state, actor, amount, generation, and replay evidence.

The map aggregate diagnostics and GUI inspection timeout are engine-evidence limitations, not permission to substitute source-only acceptance.

No compatibility alias, fake route, fixed amount, combined namespace, combined decision category, whole-world recurring scan, AI-weight change, or gameplay simplification was added.

## Changed files

Only this handoff file was added by this subagent: `docs/plans/famine_and_migration_system_plans/subagent_handoffs/architecture_0826.md`.

No gameplay, constants, trigger, on-action, decision, map mode, GUI, localisation, spreadsheet, or asset file was changed by this subagent.
