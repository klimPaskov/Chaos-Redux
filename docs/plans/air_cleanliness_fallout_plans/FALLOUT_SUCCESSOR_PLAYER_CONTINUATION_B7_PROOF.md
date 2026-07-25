# Fallout successor player-continuation B7 proof

Status: implemented as a dormant static pilot on 2026-07-25. This is not a release-floor credit and it does not prove live transition completion.

## Files

- `common/script_constants/fallout_successor_b7_constants.txt`
- `common/scripted_triggers/fallout_successor_b7_triggers.txt`
- `common/scripted_effects/fallout_successor_b7_effects.txt`
- `common/ideas/fallout_successor_b7_usa_ideas.txt`
- `common/national_focus/fallout_successor_b7_usa_focus.txt`
- `localisation/english/fallout_successor_b7_usa_l_english.yml`
- `docs/assets/fallout_successor_b7_usa/manifest.md`
- `docs/specs/air_cleanliness_fallout_specs/specs/53_successor_allocation_player_continuation_b7.md`
- `docs/plans/air_cleanliness_fallout_plans/subagent_handoffs/fallout_fragmentation_nzl_candidate_2026-07-25.md`

## Continuity evidence

The USA continuity trigger requires the snapshotted human country, surviving-tag continuation branch, current player reservation row, reserved hostable primary capital, frozen primary target equal to USA, current human control, and a current B7 transaction. The package effect writes all five current-generation package receipts, classification generation and schema, North America region, federal continuity memory, continuity archetype, a dedicated idea, and a dedicated additive focus tree. The assignment effect retains USA ownership, records player-reserved conflict output, writes source, output, cleanup, generation, assignment count, and capital state rows, and sets an explicit current-generation human-control receipt.

The focus layer has seven authored focuses with centralized 35-day, 70-day, and 105-day pacing bands. Shelter Registry adds a bunker to the surviving capital. Inland Corridors repairs infrastructure and rail. Guard Compacts changes army readiness. Regional Partners and Continental Radio Net open bilateral and communications routes. Federal Reconstruction closes the layer by replacing the temporary branch ideas with a reconstruction idea.

The latest offline focus inspector parsed the tree with seven focuses, seven resolved localisation titles, no connector crossings, no node intersections, and no long connectors. It returned 29 total blocking diagnostics, of which nine belong to this tree. Its source scan does not load vanilla interface sprite definitions and therefore reports the seven vanilla `GFX_goal_generic_*` references as missing. A direct vanilla scan confirms the six focus sprites used here and both idea sprites in the installed interface files. The inspector also reports the two `add_army_experience` uses as unresolved helpers even though the repository and vanilla precedents use that effect. These are inspector-scope diagnostics, not a runtime claim. Dedicated B7 focus and idea art remains a final asset gate.

## Fragmentation evidence

The fragmentation source trigger requires an unresolved player successor choice. The probe walks the frozen possible-country array only after the live conflict ledger is current. It rejects every live tag and every special or already committed target. The deterministic lowest-id target and lowest-id candidate state are stored on the source with a current generation and named status. Empty pools receive a blocked status. No tag is created or transferred and no fallback is used.

The reviewed package-aware candidate is NZL, the New Zealand Lifeboat State. Its existing package has a dedicated loader, focus tree, AI, decisions, characters, ideas, exact state footprint, and capital choices. It cannot be materialized by B7. `fallout_nzl_assignment_identity_is_current` requires a committed assignment row, while `fallout_nzl_conflict_dispositions_are_current` requires generation-bound Samoa and Aotearoa receipts that currently have no producer. B7 therefore keeps the generic probe dormant and does not label NZL as ready. The separate research handoff records the exact footprint and the required allocator order.

## Negative proof

No B7 effect sets `fallout_successor_assignment_ledger_built`, `fallout_successor_allocation_complete`, `fallout_player_continuation_commit_complete`, `fallout_transition_complete`, or any scheduler activation flag. The helper is not referenced by an on action, decision, event, or public manual scenario. It cannot certify the global allocation ledger.

## Engine-sensitive proof boundary

Offline references support `load_focus_tree`, `set_state_flag`, scope-valued variables, array loops, and capital building effects. The exact active transition caller, host authority, save recovery, multiplayer timing, tag-switch path, state ownership mutation, focus rendering, and runtime human-control receipt remain unobserved. HOI4 was not launched.

The final art contract is explicit in `docs/assets/fallout_successor_b7_usa/manifest.md`. Seven focus sprites belong under `gfx/interface/goals/fallout_successor_b7_usa/` and require `interface/fallout_successor_b7_usa.gfx` registrations. Four idea sprites require matching `GFX_idea_fallout_usa_*` registrations. The current package uses vanilla icon names only as a temporary pilot and does not claim those assets are final.

## Remaining blockers

The fragmentation candidate is named but not materialized. NZL package-aware selection, conflict dispositions, assignment provenance, state transfer, focus activation, and player handoff remain unproven. The pilot still uses vanilla focus and idea icons. All other survivor countries lack their final bespoke package layers. The general allocator, player tag-switch proof, complete diplomacy cleanup, scheduler activation, blackout runtime, and exact native province sweep remain release blockers.
