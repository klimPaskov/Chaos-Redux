# Fallout NZL allocator bridge blocker

Date: 2026-07-26  
Scope: dormant NZL Lifeboat State candidate selection and allocator-owned conflict receipts for Samoa state `726` and the Aotearoa overlap states `284` and `723`  
Owner: `chaosx_scripted_system_architect`  
Status: **blocked; documentation-only handoff; no gameplay edits**

## Verdict

The requested package-aware NZL allocator bridge is not safe to implement against the current schemas. The repository has generation-authenticated conflict rows for countries and generation-authenticated inventory rows for states, but it has no state-level conflict-disposition receipt that can carry a typed result, source package or country, output country, cleanup owner, and transition generation for `726`, `284`, and `723`.

The current NZL helper is also not a safe substitute. `fallout_nzl_record_conflict_dispositions` in `common/scripted_effects/fallout_nzl_lifeboat_effects.txt` writes `fallout_nzl_samoa_disposition` and `fallout_nzl_aotearoa_overlap_disposition` from a NZL country scope, uses the locally invented enum `fallout_nzl_conflict_disposition`, and is called by the B7 NZL assignment producer. It cannot prove which allocator-owned semantic result occurred for either state group.

Because the semantic result and the owner-side receipt API are unproven, this tranche makes no gameplay edits. The dormant package, scheduler, public scenario, player handoff, and general allocator remain unchanged.

## Exact surfaces inspected

### NZL package

- `common/scripted_triggers/fallout_nzl_lifeboat_triggers.txt`
  - `fallout_nzl_has_exact_state_package` requires ownership and control of `284`, `1079`, `723`, `1080`, and `1081` and excludes NZL ownership of `726`.
  - `fallout_nzl_assignment_identity_is_current` requires tag `NZL`, the current assignment row, country memory `constant:fallout_country_memory.new_zealand_lifeboat_state`, region `constant:fallout_region.oceania_remote_islands`, and archetype `constant:fallout_government_archetype.maritime_remnant`.
  - `fallout_nzl_conflict_dispositions_are_current` consumes two NZL-local flags, two NZL-local enum variables, and two generation variables.
  - `fallout_nzl_conflict_disposition_inputs_are_current` checks the global phase, conflict ledger, NZL footprint, the current owner and controller of `726`, the `SAM` country row, and every live country row. It does not identify a state-level source, package id, output tag, cleanup owner, or typed semantic result for either overlap.
  - `fallout_nzl_existing_tag_conversion_can_commit` and `fallout_nzl_lifeboat_package_can_activate` consume the local receipt pair.
- `common/scripted_effects/fallout_nzl_lifeboat_effects.txt`
  - `fallout_nzl_record_conflict_dispositions` is the only writer for the local pair and is called from `fallout_nzl_commit_existing_tag_assignment`.
  - `fallout_nzl_clear_conflict_dispositions` is called from the global allocation reset and clears the local pair.
  - `fallout_nzl_activate_lifeboat_package` remains a dormant package loader, not an allocator.
- `common/script_constants/fallout_nzl_lifeboat_constants.txt`
  - `fallout_nzl_conflict_disposition` defines `samoa_state_excluded = 1` and `aotearoa_overlap_inactive = 2`. No source contract proves either value as a real allocator disposition, so these values cannot be promoted into the global resolution vocabulary.
- `common/scripted_effects/fallout_nzl_lifeboat_effects.md`
  - Documents the package as dormant and dependent on allocator receipts, but has no supported state-level receipt contract.

### B7 allocator pilot

- `common/scripted_triggers/fallout_successor_b7_triggers.txt`
  - `fallout_successor_b7_transaction_is_current` requires the survivor-allocation transaction, preallocation consumption, current generation, current conflict ledger, and current player reservation ledger.
  - `fallout_successor_b7_fragmentation_candidate_is_available` is a generic possible-country predicate. It excludes live rows, assignments, materialization receipts, release receipts, and landholding, but it has no NZL package identity or package-footprint contract.
- `common/scripted_effects/fallout_successor_b7_effects.txt`
  - `fallout_successor_b7_probe_fragmentation_candidate` selects the lowest-id generic possible country and lowest-id candidate state. It does not select a reviewed package or NZL.
  - `fallout_successor_b7_run_vertical_slice` is the dormant coordinator and the only path that reaches `NZL` assignment logic.
  - `fallout_nzl_commit_existing_tag_assignment` is called through the NZL effect file and writes the country-level `converted_existing` row. It does not publish a per-state Samoa or Aotearoa bridge receipt.

### Global Fallout allocator schema

- `common/scripted_triggers/fallout_world_end_triggers.txt`
  - `fallout_live_tag_conflict_row_is_current` and `fallout_live_tag_conflict_resolution_is_current` are country-scope contracts.
  - `fallout_live_tag_conflict_resolution_provenance_is_current` accepts the shared enum `constant:fallout_tag_conflict_resolution.*` and validates source/output/cleanup relationships for a country row.
  - `fallout_successor_state_inventory_row_is_current` is a state-scope contract, but stores only owner, controller, hostability, player reservation, event-package markers, candidate membership, and generation. It has no disposition enum or source/output/cleanup receipt.
  - `fallout_successor_conflict_ledger_is_current` validates aligned country and state arrays, not state-level conflict outcomes.
  - `fallout_successor_assignment_country_row_is_current` and `fallout_successor_assignment_capital_row_is_current` validate post-allocation country and capital rows, not overlap-resolution rows.
- `common/scripted_effects/fallout_world_end_effects.txt`
  - `fallout_record_live_tag_conflict_row` records a country as `allocation_pending`.
  - `fallout_record_successor_state_inventory_row` records generation-bound state ownership and controller facts.
  - `fallout_reset_successor_conflict_inventory` and `fallout_reset_successor_allocation_ledger` clear these existing country and state rows. No effect commits a state-level disposition.
  - `fallout_begin_successor_allocation_transaction` and `fallout_finalize_successor_allocation_transaction` manage the general transaction. They do not expose an NZL-specific bridge API.
- `common/script_constants/fallout_world_end_constants.txt`
  - `fallout_successor_inventory_schema.version = 1` is the current state/country inventory schema.
  - `fallout_tag_conflict_resolution` contains `continued_in_place`, `converted_existing`, `released_releasable`, `created_dynamic`, `retired_landless`, `preserved_event_package`, and `player_reserved`. The enum is defined for country conflict rows and does not establish the semantic result for any of the three requested state surfaces.

### Independence Wave overlap evidence

- `common/scripted_triggers/006_independence_wave_packages_region_13_triggers.txt`
  - `can_plan_independence_wave_package_iw_175` checks plan-slot, reservation-group, `SAM` tag availability, and anchor `726` availability.
  - No `IW-174` runtime planner predicate is present in this file.
- `common/scripted_effects/006_independence_wave_packages_region_13_effects.txt`
  - `independence_wave_load_package_iw_175` identifies package `constant:independence_wave_package_id.iw_175`, country `SAM`, and anchor `726`.
  - `independence_wave_reserve_package_iw_175` reserves anchor `726` and tries extended state `1072`.
  - No effect publishes a Fallout conflict-resolution receipt for `726`.
- `common/country_tags/006_independence_wave_countries.txt`
  - `GRX` is registered for IW-174.
- `common/scripted_effects/006_independence_wave_scenario_effects.txt`
  - IW-174 and `GRX` are in the scenario blocked arrays.
  - A static blocked entry is not a current allocator resolution and cannot be interpreted as `retired_landless`, `preserved_event_package`, or any other shared enum.
- `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv`
  - IW-174 is described as an Aotearoa Māori package using tag `GRX`, while IW-175 is the Samoa package using `SAM`.
- `docs/plans/air_cleanliness_fallout_plans/subagent_handoffs/fallout_nzl_conflict_disposition_api_blocker_2026-07-22.md`
  - The earlier audit records the same absence of a supported state-level producer and correctly leaves the package dormant.

## Unsupported schema gap

The existing state inventory can answer who owns or controls a state in the current transition generation. It cannot answer how an allocator resolved a state conflict. The country conflict row can answer that question only for its country scope, and its provenance validator requires a matching output and cleanup relationship.

There is no supported representation for a receipt with this shape:

```text
state set = {726} or {284, 723}
source package/tag = SAM/IW-175 or GRX/IW-174 when genuinely live
typed resolution = one proven fallout_tag_conflict_resolution value
output country = optional, but required for result types that use it
cleanup owner = allocator-owned scope
transition generation = global.fallout_transition_generation
```

The current NZL-local enum would hide this gap. Generation stamps alone prove freshness, not semantic ownership, source identity, reservation status, or reciprocal cleanup. A state-owner absence check also cannot distinguish an unplanned state, an active Independence Wave reservation, a player reservation, a blocked package, and an explicitly retired source.

## Safe next-step contract

No helper should be added until the parent accepts a schema owner and semantic result source. The next implementation tranche should be allocator-owned and should make the state receipt explicit rather than copying country rows into NZL.

1. Define a shared, versioned state-conflict receipt schema under `common/script_constants/` and the global Fallout allocator surfaces. The schema must name the state set, source country or package id, proven shared resolution enum, optional output country, cleanup owner, and generation.
2. Add allocator-owned writers in the general allocation effect file, after the relevant country or package transaction commits. The writer must reject stale inventory, player reservations, live event-package ownership, blocked packages, duplicate state rows, and already-current receipts.
3. Make Samoa receipt production read an actual committed IW-175/SAM result. `SAM` plan eligibility or anchor reservation alone is insufficient.
4. Make Aotearoa receipt production read an actual committed IW-174/GRX result. The blocked IW-174 registration is not a retirement result. If IW-174 remains disabled, the allocator must publish a separately designed non-overlap result rather than infer one.
5. Add one package-aware NZL predicate and selector in the allocator. It should require the locked tag `NZL`, the reviewed package identity, exact hostable footprint, current assignment transaction, current state receipts, and no unresolved player or event-package overlap. It should store one generation-bound selected-country/package row and must not reuse the generic lowest-id candidate selector.
6. Move the NZL activation gate to consume the allocator-owned bridge only after reciprocal validation succeeds. The NZL package effect must remain a consumer and must not decide conflict outcomes.
7. Extend cleanup and save-recovery paths together. Reset must clear the bridge rows by generation and owner without erasing unrelated country conflict rows. Rebuild must reject partial receipt sets.

## Validation performed

- Read `AGENTS.md`, `chaos-redux-events`, and `chaos-redux-subagents` before inspection.
- Consulted the offline Paradox wiki pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.
- Consulted the installed vanilla documentation for script constants, effects, and triggers, including `save_event_target_as`, `save_global_event_target_as`, `clear_global_event_target`, `has_event_target`, `check_variable`, `meta_effect`, and scope support.
- Inspected every gameplay file and handoff listed above.
- Searched gameplay sources for NZL disposition writers, generic global resolution writers, allocator candidate selectors, IW-175 reservation calls, IW-174/GRX registration and blocked markers, and any activation caller.
- Confirmed balanced braces in the inspected NZL, B7, and global Fallout script files.

Skipped meaningful validation:

- No gameplay file, constant, trigger, effect, event, decision, on-action, scenario, map, localisation, or spreadsheet was changed.
- No HOI4 launch, save test, MCP gameplay render, scheduler test, player handoff, or map mutation was run. The requested bridge is blocked before runtime testing can be meaningful.

## Files changed

- `docs/plans/air_cleanliness_fallout_plans/subagent_handoffs/fallout_nzl_allocator_bridge_blocker_2026-07-26.md`

No gameplay identifiers, constants, tags, states, event targets, flags, variables, localisation keys, or call sites were changed.

## Remaining risks and parent follow-up

- The existing committed `fallout_nzl_conflict_disposition` enum and NZL-local writer remain semantically unsupported. The parent should not treat them as allocator proof and should decide whether to supersede or remove them when the shared bridge schema is accepted.
- The B7 generic selector remains package-agnostic and must not be promoted to NZL materialization.
- IW-175/SAM has a planning and reservation surface but no Fallout resolution receipt.
- IW-174/GRX is blocked and has no runtime disposition.
- No general allocator, scheduler, public scenario, or player handoff is authorized by this tranche.

No fallback or simplification was used. The requested gameplay implementation remains incomplete because the current repository cannot prove the required state-level semantics.
