# Fallout successor player-continuation B7 proof

Status: implemented as a dormant static pilot on 2026-07-25. This is not a release-floor credit and it does not prove live transition completion.

## Files

- `common/script_constants/fallout_consolidated_constants.txt`
- `common/scripted_triggers/fallout_consolidated_triggers.txt`
- `common/scripted_effects/fallout_consolidated_effects.txt`
- `common/decisions/fallout_consolidated_decisions.txt`
- `common/ai_strategy_plans/fallout_consolidated_ai.txt`
- `common/ideas/fallout_consolidated_ideas.txt`
- `common/national_focus/fallout_consolidated_focus.txt`
- `localisation/english/fallout_consolidated_l_english.yml`
- `docs/assets/fallout_successor_b7_usa/manifest.md`
- `docs/specs/air_cleanliness_fallout_specs/specs/53_successor_allocation_player_continuation_b7.md`
- `docs/plans/air_cleanliness_fallout_plans/subagent_handoffs/fallout_fragmentation_nzl_candidate_2026-07-25.md`
- `docs/plans/air_cleanliness_fallout_plans/subagent_handoffs/fallout_b7_usa_focus_effect_correction_2026-07-26.md`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_NZL_FRAGMENTED_TRANSFER_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_NZL_DYNAMIC_MATERIALIZATION_PROOF.md`

## Continuity evidence

The USA continuity trigger requires the snapshotted human country, surviving-tag continuation branch, current player reservation row, reserved hostable primary capital, frozen primary target equal to USA, current human control, and a current B7 transaction. The package effect writes all five current-generation package receipts, classification generation and schema, North America region, federal continuity memory, continuity archetype, a dedicated idea, and a dedicated additive focus tree. The assignment effect retains USA ownership, records player-reserved conflict output, writes source, output, cleanup, generation, assignment count, and capital state rows, and sets an explicit current-generation human-control receipt.

The focus layer has seven authored focuses with centralized 35-day, 70-day, and 105-day pacing bands. Shelter Registry adds a bunker to the surviving capital. Inland Corridors repairs infrastructure and rail. Guard Compacts changes army readiness. Regional Partners and Continental Radio Net open bilateral and communications routes. Federal Reconstruction closes the layer by replacing the temporary branch ideas with a reconstruction idea.

The focus layer now unlocks five route-locked continuity projects. Inland Depot Belt consumes rifles and trains while assigning a civilian factory, Guard Compacts consumes manpower, rifles, support stores, and Command Power, the Great Lakes Charter consumes convoys and Command Power, Radio Dead Zones consumes support stores and Command Power, and Federal Reconstruction Drive consumes trains while assigning a civilian factory. The projects change the frozen capital, write generation-bound logistics, security, diplomacy, information, or reconstruction memories, and apply a visible cancellation penalty when the package or capital becomes invalid. Each project has a distinct AI weight and the category is hidden until the USA package receipt is current.

The latest offline focus inspector parsed the tree with seven focuses, seven resolved localisation titles, no connector crossings, no node intersections, and no long connectors. Its source scan does not load all interface definitions, so its workspace-wide diagnostics are not a runtime loading proof. The two USA focus rewards use the documented `army_experience` effect. Dedicated Fallout B7 focus and idea DDS files are now present under their event-owned folders, with parent-owned registrations in `interface/fallout_consolidated.gfx`. The source-generation prompt transcript was not retained by the interrupted worker, so independent visual approval and provenance review remain open.

## Fragmentation evidence

The fragmentation source trigger requires an unresolved player successor choice. The probe walks the frozen possible-country array only after the live conflict ledger is current. It rejects every live tag and every special or already committed target. The deterministic lowest-id target and lowest-id candidate state are stored on the source with a current generation and named status. Empty pools receive a blocked status. No tag is created or transferred and no fallback is used.

The reviewed package-aware candidate is NZL, the New Zealand Lifeboat State. Its existing package has a dedicated loader, focus tree, AI, decisions, characters, ideas, exact state footprint, and capital choices. B7 now has one guarded existing-tag path. `fallout_nzl_assignment_identity_is_current` still requires a committed assignment row, while `fallout_nzl_conflict_dispositions_are_current` requires generation-bound Samoa and Aotearoa receipts. The B7 producer records `converted_existing`, appends one exact capital row, and calls the package loader only when an AI NZL tag already owns and controls states 284, 1079, 723, 1080, and 1081 while excluding state 726. It does not create a tag or transfer states. A missing or fragmented NZL tag remains blocked. The separate research handoff records the exact footprint and required allocator order.

The B7 follow-up now adds a fragmented NZL path and a separate dynamic materializer. `fallout_nzl_fragmented_transfer_can_commit` requires the same current conflict inventory plus five exact candidate states, one state per AI source owner, and matching ownership and control. `fallout_nzl_commit_fragmented_exact_footprint` records the five source scopes, uses the documented state-scope `transfer_state_to = ROOT` effect, retires each emptied source with a generation-bound `retired_landless` receipt, and exposes Wellington state 284 as the capital candidate. It then reuses the existing NZL conversion producer. When the live ledger has no NZL tag, the guarded B7 coordinator walks the frozen live conflict rows and admits only one non-player source that passes the exact five-state footprint. `fallout_successor_b7_materialize_dynamic_nzl` creates one reserved dynamic country with `original_tag = NZL` and `copy_tag = NZL`, transfers Wellington, Auckland, Canterbury, Marlborough, and Otago from five one-state AI sources, records each source retirement, commits the `created_dynamic` result, assigns Wellington as capital, and activates the reviewed Lifeboat package on the output. The source row links to the output with the current generation and cleanup owner. A failed transfer, package receipt, or output assignment raises the transition error and prevents the B7 completion flag. `fallout_successor_b7_cleanup_dynamic_nzl` restores the exact source states, reassigns their controllers, clears output receipts, retires the package runtime, makes the dynamic output landless, and releases its reserved slot because the engine documents recycling but not a destroy-country effect. The dynamic path does not set global allocation completion or scheduler activation. The exact transfer and dynamic materialization proofs are recorded in `FALLOUT_NZL_FRAGMENTED_TRANSFER_PROOF.md` and `FALLOUT_NZL_DYNAMIC_MATERIALIZATION_PROOF.md`.

## Negative proof

No B7 effect sets `fallout_successor_assignment_ledger_built`, `fallout_successor_allocation_complete`, `fallout_player_continuation_commit_complete`, `fallout_transition_complete`, or any scheduler activation flag. The helper is not referenced by an on action, decision, event, or public manual scenario. It cannot certify the global allocation ledger.

## Engine-sensitive proof boundary

Offline references support `load_focus_tree`, `set_state_flag`, scope-valued variables, array loops, and capital building effects. The exact active transition caller, host authority, save recovery, multiplayer timing, tag-switch path, state ownership mutation, focus rendering, and runtime human-control receipt remain unobserved. HOI4 was not launched.

The final art contract is explicit in `docs/assets/fallout_successor_b7_usa/manifest.md`. Seven focus sprites belong under `gfx/interface/goals/fallout_successor_b7_usa/` and four idea sprites belong under `gfx/interface/ideas/fallout_successor_b7_usa/`. All eleven are registered in `interface/fallout_consolidated.gfx` and are referenced by the B7 focus, idea, and continuity-project layers. They are dedicated Fallout art, not vanilla or Zombie placeholders. Prompt provenance and independent visual approval remain open. The shelter-registry focus and idea candidates still carry `needs_user_review` status because a visible `B7` plate remains in the generated source.

## Remaining blockers

The generic fragmentation candidate is still only named. The NZL existing-tag path and its exact five-state fragmented transfer pilot now have static assignment provenance, source retirement, conflict dispositions, exact capital-row wiring, and a dormant package caller. The dynamic path adds a guarded missing-tag materialization and a same-generation rollback surface, but it does not prove the general successor matrix, player candidate assignment, dynamic-country save persistence, or multiplayer tag delivery. Player handoff remains unproven. The B7 asset package is dedicated and wired, but its prompt provenance and independent visual approval remain open. All other survivor countries lack their final bespoke package layers. The general allocator, player tag-switch proof, complete diplomacy cleanup, scheduler activation, blackout runtime, and exact native province sweep remain release blockers.
