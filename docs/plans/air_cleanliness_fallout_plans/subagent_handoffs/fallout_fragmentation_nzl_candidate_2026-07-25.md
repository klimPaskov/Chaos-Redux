# Repo Explorer Handoff

## Scope read
- Parent task: identify one existing possible-country candidate for the next Fallout fragmentation materialization tranche after the committed B7 USA continuity pilot.
- Explicit constraints: read-only gameplay inspection; no Hearts of Iron IV launch; inspect one existing tag, its history/focus/package, and Fallout materialization precedents; state whether a safe candidate is proven or blocked.
- Candidate inspected: `NZL` (New Zealand Lifeboat State).
- Skills/docs read: `AGENTS.md`, `chaos-redux-subagents`, `chaos-redux-events`, `hoi4-focus-trees`; required offline Paradox wiki pages; vanilla collections/effects documentation and relevant vanilla files.

## Primary findings
- `NZL` is the only existing Fallout successor package found with a dedicated package loader, focus tree, decisions, characters, AI plans, ideas, constants, cosmetics, on-actions, localisation, and asset surfaces.
- The package is dormant and cannot be safely materialized from the current allocator. `fallout_nzl_activate_lifeboat_package` has no Fallout caller, and its activation trigger requires allocator receipts plus two conflict-disposition receipts that have no producer.
- The B7 fragmentation probe is package-agnostic: it selects the lowest-id member of `global.fallout_all_possible_country_scopes` and the lowest candidate state. It does not select `NZL`, transfer ownership, release/create a tag, load a focus tree, or record materialization provenance.
- Recommendation: reserve `NZL` as the reviewed candidate, but mark the materialization slice blocked. Do not activate a live slice until the allocator has a package-aware NZL selector and authenticated conflict/assignment/materialization receipts.

## Relevant files
| Path | Why it matters | Evidence |
| --- | --- | --- |
| `common/scripted_effects/fallout_nzl_lifeboat_effects.txt` | Dormant package activation and runtime initialization. | `fallout_nzl_activate_lifeboat_package` at line 522; sets politics/ideas/cosmetic tag, chooses capital 284 or 1079, loads `fallout_nzl_lifeboat_focus_tree`, creates starting forces, and marks the package active. |
| `common/scripted_triggers/fallout_nzl_lifeboat_triggers.txt` | Exact activation and post-activation gates. | `fallout_nzl_has_exact_state_package` lines 9-15; `fallout_nzl_assignment_identity_is_current` lines 18-40; `fallout_nzl_conflict_dispositions_are_current` lines 42-56; activation gate lines 59-64; current-package gate lines 66-81. |
| `common/national_focus/fallout_nzl_lifeboat_focus.txt` | Authored Fallout focus tree consumed by the loader. | Tree id `fallout_nzl_lifeboat_focus_tree` at lines 8-9; focus availability is gated by `fallout_nzl_lifeboat_package_is_current`; state-specific gates reference 284, 1079, and 723. |
| `common/ideas/fallout_nzl_lifeboat_ideas.txt` | Fallout package ideas referenced by activation and routes. | Contains `fallout_nzl_empty_harbors`, `fallout_nzl_lifeboat_morality`, and subsequent lifecycle ideas. |
| `common/characters/fallout_nzl_lifeboat_characters.txt` | Runtime package character roster recruited during activation. | Package file is present; activation calls `fallout_nzl_recruit_package_characters`. |
| `common/ai_strategy_plans/fallout_nzl_lifeboat_ai.txt` | AI route plans gated by the current package receipt. | Humanitarian/isolation plans require `original_tag = NZL`, `fallout_nzl_lifeboat_package_is_current`, and `fallout_nzl_ai_override`. |
| `common/decisions/fallout_nzl_lifeboat_decisions.txt` | Package decision surface. | Decision visibility/cancel triggers require `fallout_nzl_lifeboat_package_is_current`; category is in `common/decisions/categories/fallout_nzl_lifeboat_categories.txt`. |
| `common/on_actions/fallout_nzl_lifeboat_on_actions.txt` | Post-activation callbacks. | All relevant callbacks are gated by `fallout_nzl_lifeboat_package_is_current`; this file does not call package activation. |
| `common/countries/fallout_nzl_lifeboat_cosmetics.txt` | Fallout cosmetic tag consumed by activation. | Loader sets `NZL_FALLOUT_LIFEBOAT_STATE`. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/NZL - New Zealand.txt` | Vanilla tag baseline and capital. | `capital = 284` at line 1. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/284-New Zealand.txt` | Wellington state baseline. | Owner/core `NZL`; package uses 284 as Wellington capital option. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/1079-Auckland.txt` | Auckland state baseline. | Owner/core `NZL`; package uses 1079 as alternate capital option. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/723-Southern Island.txt` | Southern Island state baseline. | Owner/core `NZL`; package requires it. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/1080 - Marlborough.txt` | Marlborough state baseline. | Owner/core `NZL`; package requires it. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/1081 - Otago.txt` | Otago state baseline. | Owner/core `NZL`; package requires it. |
| `common/scripted_effects/fallout_successor_b7_effects.txt` | Current B7 candidate probe and dormant coordinator. | `fallout_successor_b7_probe_fragmentation_candidate` at line 131 picks lowest country/state ids; `fallout_successor_b7_run_vertical_slice` at line 211 is explicitly not connected to a public caller. |
| `common/scripted_triggers/fallout_successor_b7_triggers.txt` | Current generic fragmentation candidate predicate. | `fallout_successor_b7_fragmentation_candidate_is_available` at line 190 only excludes live/owned/committed/special rows; no package or tag check. |
| `common/scripted_effects/fallout_world_end_effects.txt` | Allocation transaction and receipt reset/finalization. | Reset clears materialization/release/assignment receipts around lines 2870-2930; transaction begins only after current conflict ledger around 2934; finalizer at 2960 only sets completion after strict postconditions. No materialization producer exists in Fallout files. |
| `common/scripted_triggers/fallout_world_end_triggers.txt` | Conflict-ledger and allocation proof gates. | `fallout_successor_conflict_ledger_is_current` at line 2179 validates all live/possible-country/state inventory; postcondition trigger at line 2905 requires the complete assignment structure. |
| `docs/plans/air_cleanliness_fallout_plans/FALLOUT_NZL_LIFEBOAT_ENGINE_PROOF.md` | Existing package audit and blockers. | Records dormant status, exact footprint, missing allocator dispositions, no caller, and no runtime proof. |
| `docs/plans/air_cleanliness_fallout_plans/subagent_handoffs/fallout_nzl_conflict_disposition_api_blocker_2026-07-22.md` | Confirmed conflict API blocker. | No producer sets `fallout_nzl_samoa_disposition_resolved` or `fallout_nzl_aotearoa_overlap_resolved`; local flags would be unauthenticated. |

## Existing patterns
- The NZL loader is an existing-tag package pattern, not a dynamic-country pattern. It requires `tag = NZL`, current assignment identity, current generation, exact owner/controller footprint, and explicit bilateral conflict dispositions before activation.
- `fallout_successor_b7_fragmentation_candidate_is_available` is not safe to reuse for NZL materialization because its pool is generic and its deterministic rule is lowest database id, not package readiness. A next tranche needs an explicit package-aware NZL predicate/selector or a reviewed registry mapping tag to package.
- `fallout_world_end_effects.txt` currently records and clears provenance fields such as `fallout_releasable_release_committed` and `fallout_dynamic_country_materialization_committed`, but no Fallout effect writes those receipts. The current implementation therefore proves inventory and postcondition schemas, not a materialization operation.

## Vanilla or reference precedents
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`: `release` does nothing if the target country already exists; `create_dynamic_country` runs child initialization effects; `transfer_state_to` sets both owner and controller; `set_state_owner_to` only changes owner; `set_capital` requires an explicit state.
- Vanilla materialization examples inspected include `events/BBA_Ethiopia.txt`, `events/France.txt`, `events/GOE_Afghanistan.txt`, `common/decisions/YUG.txt`, and `common/scripted_effects/002_zombie_outbreak_effects.txt`. They demonstrate release/dynamic-country/transfer syntax, but do not prove this mod's NZL conflict, player-handoff, save-recovery, or focus-load behavior.
- The offline wiki and vanilla `common/collections/_documentation.md` confirm `game:all_possible_countries`, `every_collection_element`, and collection-size checks. Membership in that collection alone does not prove an existing tag is materializable without conflict.

## Likely edit order for the parent
1. Add a package-aware candidate contract for `NZL` that requires current conflict inventory, absence from live conflict/player/event-package rows, exact candidate states, and a reviewed package id; do not silently change the generic B7 lowest-id rule.
2. Add an allocator-owned conflict-resolution producer for Samoa (state 726) and the Aotearoa/GRX overlap, with generation, cleanup owner, output, and resolution enum receipts. Existing IW/GRX flags are not substitutes.
3. Add one NZL assignment/materialization effect that writes source/result/cleanup/provenance rows before state mutation. Use `transfer_state_to` for owner+controller, then `set_capital`; do not rely on owner-only mutation.
4. Validate NZL's exact footprint (284, 1079, 723, 1080, 1081; 726 excluded), capital choice (284 or 1079), current generation, assignment identity, and package receipts before calling `fallout_nzl_activate_lifeboat_package`.
5. Rebuild/check the conflict ledger after mutation and call the existing finalizer only if `fallout_successor_allocation_ledger_postconditions_are_met` passes. Keep the route dormant until runtime proof covers tag existence/release semantics, ownership/control transfer, focus loading, and player handoff.

## Validation checks
- Static: confirm `NZL` is in the possible-country inventory and not in `global.fallout_live_tag_conflict_countries`; verify package-aware selector cannot choose an arbitrary un-packaged tag.
- Assignment: `fallout_successor_conflict_ledger_is_current`, `fallout_successor_assignment_country_row_is_current`, and the live-tag conflict resolution/provenance triggers must all be current for the transition generation.
- Footprint: `fallout_nzl_has_exact_state_package`; state 726 must remain unowned by NZL; state owner and controller must both equal NZL after mutation.
- Package: `fallout_nzl_assignment_identity_is_current`, `fallout_nzl_conflict_dispositions_are_current`, `fallout_nzl_lifeboat_package_can_activate`, then `fallout_nzl_lifeboat_package_is_current` after activation.
- Completion: `fallout_successor_allocation_ledger_postconditions_are_met` must pass before `fallout_finalize_successor_allocation_transaction`; recheck `game:all_possible_countries` collection alignment after any tag mutation.
- Runtime-only proof still required: existing/landless NZL behavior, release no-op semantics when a tag exists, state transfer persistence, focus-tree load, scope-valued receipt persistence, and player-control/change-tag handoff. No HOI4 run was performed.

## Risks and blockers
Confirmed blockers:
- No Fallout caller currently invokes `fallout_nzl_activate_lifeboat_package`.
- No producer writes `fallout_nzl_samoa_disposition_resolved` or `fallout_nzl_aotearoa_overlap_resolved` and their generation receipts.
- No Fallout materializer writes `fallout_releasable_release_committed` or `fallout_dynamic_country_materialization_committed` provenance.
- The B7 probe is generic and may name an un-packaged tag; it cannot be promoted directly into NZL materialization.
- Runtime behavior for tag existence/landless release, state mutation, focus loading, and player assignment is unobserved; therefore a live/safe materialization slice is not proven without runtime proof.

Ordinary downstream risks:
- Existing NZL audit notes a missing radio-coordinator portrait and unresolved vanilla NZL alternate-AI retirement. These do not identify a new candidate, but they prevent claiming the package is fully release-ready.

## Recommended next action
Treat `NZL` as the single reviewed candidate for the next design tranche, not as a safe activation target. First implement and audit the package-aware selector plus authenticated conflict/assignment receipts; then perform a separate runtime-proof pass before enabling any player-facing materialization or final allocation completion.
