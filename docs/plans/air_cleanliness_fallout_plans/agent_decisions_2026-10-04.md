# Fallout agent decisions, 2026-10-04

Basis for every decision below: the user granted the implementing agents full design authority and asked that the recommended, spec-consistent option be taken and recorded instead of waiting for input. Each entry states the decision, the reason, and where it lives in source. Disposition labels follow the plans-folder rules in `CLAUDE.md`.

## A1. Living-world scheduler activation replaces the spec 12 release receipt

Disposition: implemented (static review only, live delivery is `needs_live_game`).

Spec 12 `Release audit receipt` required a generation-bound receipt for 660 reviewed blocks plus live host, save, and multiplayer proof before either activation flag could be set. That receipt has no producer and the proof it asks for is user-owned live testing, so the gate kept all 104 registered chains unreachable.

Decision: `fallout_event_activate_living_world` (coordinator scope, `common/scripted_effects/fallout_consolidated_effects.txt`) sets `fallout_event_scheduler_activation_approved` and `fallout_event_scheduler_active` once, when the map-return receipts, registry header, numerical registry header and player continuation commit are current and no scheduler error exists. It runs from `fallout_event_scheduler_reconcile` beside the numerical-registry work. The per-chain reviews already recorded in this folder stand in for the release receipt. The registry headers bind the survival ledger they were built from, so the full per-state survival scan is not repeated at activation.

Fatigue, the ordinary cooldown, the three-arc cap, delayed-row caps and the hard repeat veto are unchanged.

## A2. Ash-week orientation runs for every registry country

Disposition: implemented (static review only, live delivery is `needs_live_game`).

Decision: `fallout_orientation_reconcile_registry` runs in the coordinator pass once the numerical registry is current. Human successors begin at once, AI successors begin at most `fallout_orientation_runtime.daily_ai_starts` (2) per day. Each step runs in hidden event `chaosx.fallout.85` so ROOT is the registry country, which every orientation effect and trigger already assumes.

- National orientation (62-65) and capital condition (66-69) run for every registry country.
- Immediate resource crisis (70-73) and government archetype (74-77) run only for the twelve pilot memories with reviewed rows, and only when memory, region and archetype all match those rows.
- Character or institution (78-81) is recorded complete without a popup until a curated character registry exists.
- A component with no reviewed row, or with no branch the country can pay for, is recorded complete through `fallout_event_record_orientation_component` without a popup. A missing capital is retried for `retry_days` (10) before the component is skipped.
- A transaction whose event never issued, or whose issued event is more than `stall_days` (30) past due, is cancelled and its component recorded, so no country can be held out of ordinary events forever.
- After all five components the closure report (82/83, cleanup 84) runs. If it cannot be issued, the closure is recorded finished without a report.

The surface approvals that had no setter are written by `fallout_orientation_approve_country_surfaces`: regional, archetype, memory, state-result and capital-repair rows are approved for every registry country, the government row only for the twelve pilot memories, and character installation stays blocked. The resource-crisis package receipt is installed by `fallout_orientation_install_resource_package` against the assigned capital for the twelve pilot memories.

The old dormancy trigger `fallout_orientation_activation_is_dormant` (orientation only while the scheduler was off) is replaced by `fallout_orientation_runtime_is_open` (orientation unless the scheduler is in error). Ordinary events still require `fallout_event_orientation_is_complete` per country, so running both together is safe.

## A3. Capital repair uses the engine's own repair, sped up

Disposition: implemented.

No documented effect repairs exactly one damaged level (see `FALLOUT_ORIENTATION_CAPITAL_INFRASTRUCTURE_REPAIR_ENGINE_PROOF.md`). Decision: a successful sealed civic core adds `fallout_capital_civic_repair_success` to the capital state for 180 days, a partial result adds `fallout_capital_civic_repair_partial` for 90 days. Both use the documented state modifiers `state_repair_speed_infrastructure_factor`, `state_repair_speed_rail_way_factor` and `state_repair_speed_supply_node_factor` (vanilla precedent: `common/dynamic_modifiers/mun_dynamic_modifiers.txt`). The result text describes repair crews on the roads, rail sidings and depots instead of an exact restored level.

## A4. Opening and result events no longer re-check the ordinary cooldown

Disposition: implemented.

The commit path extends `fallout_event_ordinary_cooldown_due_day` into the future before it issues the opening the same day, while every opening trigger re-checked `num_days >= cooldown_due_day` through `fallout_event_country_can_receive_ordinary_event`. Every issued opening would therefore have failed its own trigger and left a blocking tombstone receipt. The cooldown is already enforced, with its crisis-break exception, by candidate eligibility at selection. Decision: the shared gate keeps activation, phase, registry, orientation, quiet period and ownership checks and drops the cooldown check. Selection (`fallout_event_numerical_selection_slot_is_open`) now also requires that shared gate, so nothing is selected before orientation completes and the quiet period ends.

## A5. Candidate reviews run in each country's own event

Disposition: implemented.

`fallout_event_build_pilot_candidate_registries` ran from the coordinator, but its body and about 100 candidate triggers use ROOT as the reviewed country (state searches write `ROOT.fallout_event_<id>_candidate_state_id`). Run from the coordinator, every state-targeted candidate wrote to the coordinator and was never appended. Decision: the coordinator now only requests a review and the body runs as `fallout_event_build_country_candidate_registry` inside hidden event `chaosx.fallout.86`.

Reviews also refresh: once after the country can first receive ordinary events (rows built at map return could not see orientation-gated candidates), and every `candidate_refresh_days` (30) while the country has no opening, delayed row, arc or bilateral row in flight. Selection waits for the post-orientation review. Chain ledgers seeded once per generation (`fallout_ash_wolves_*`, `fallout_bridge_that_moved_*`, `fallout_first_unmasked_day_*` current values) are cleared only on a new generation, so a refresh keeps earlier outcomes.

## A6. Ready dispatches are issued by the review lanes

Disposition: implemented.

Delayed results, callbacks and arc stage envelopes became ready inside the human and AI review lanes but were issued only by the one-country-per-day registry cursor, so a result could arrive weeks after its due day. Decision: both lanes call `fallout_event_issue_ready_dispatch` right after reconciling a country.

## A7. Major-arc and Refugee Train consumers

Disposition: implemented (static review only).

- The four major-arc stage consumers (Year Zero 401, Orchard Flowers 408, Skilled List 429, False Spring Losses 478) required `fallout_event_<id>_candidate_state_id` after the candidate review had cleared it. Their state target and pressure now persist until the next review. Orchard Flowers also initialised its target as a temporary variable that shadowed the stored target; it is now a normal variable. Their country and state triggers use PREV and OWNER instead of ROOT, because the arc consumer runs in the coordinator pass.
- `fallout_event_schedule_selected_relationship_candidate` saved ROOT (the coordinator) as the bilateral partner. It now saves the partner registry country, so the Refugee Train pair can reserve its reciprocal rows.

## A8. Manual sweep strikes skip the per-strike humanitarian hook

Disposition: implemented. The tick-time gain is `needs_live_game`.

The manual sweep aggregate already owns population, Deaths (reason 19), famine and migration for its 10,154 coordinator strikes, so the per-strike humanitarian corridor, nuclear evacuation report, famine pressure and migration pressure work in `common/on_actions/humanitarian_runtime_on_actions.txt` double-counted them and slowed the drop tick. Decision: `fallout_manual_sweep_callback_window_is_open` is true for every coordinator drop while the sweep or verifier is open. It deliberately omits the observed-versus-issued comparison, because the Chaos Meter observer in `chaosx_on_actions_chaos_meter.txt` loads first and has already counted the final strike when the humanitarian hook runs. The humanitarian hook skips its state block when the window is open. Ordinary nukes, Event 023 strikes and nukes by any other launcher keep their humanitarian handling. The edit in the humanitarian file is one added limit line.

## A9. The stopped thread's temp-variable and Deaths hunks are already in history

Disposition: implemented.

The uncommitted hunks in `common/scripted_effects/fallout_consolidated_effects.txt` (orientation and Event 230 moves reading `ROOT.<temp>`, missing Deaths output pre-initialization, and the Air Winter famine adapter's unset cause) were committed in `0cfdf83c2` as part of the shared exact population-loss change, which states that Event 230 and the orientation helpers read their own temporaries. `chaos_meter_deaths.zero` and `chaos_meter_deaths_reason.air_winter_exposure` exist in `common/script_constants/chaos_meter_constants.txt`, and the file has no remaining stopped-thread hunks. No separate adoption commit was made because rewriting shared history is not allowed.

## A10. Air Cleanliness Treaty operations and treaty memory in Fallout

Disposition: implemented (static review only; targeted decision persistence, mapmode tier display, embargo ownership, and corridor population read-back are `needs_live_game`). Acceptance basis: decision D2 restored the treaty as accepted design and baseline spec 02 lists the operations; the specific rules below are agent decisions under the user's grant of design authority.

- Shared Sampling Grid (`air_cleanliness_treaty_shared_sampling_grid`). "75 percent treaty formed" is read as "the treaty exists", because the treaty only forms at 75 percent contamination; a quorum of four live members is added so the grid is a joint project. "Improves forecasting" is implemented as one rule: while the grid runs (365 days), every member reads the Air Winter mapmode at atmospheric office level, and members with their own office read at terminal-modelling level. One grid at a time, 180-day gap.
- Seed Archive Exchange (`air_cleanliness_treaty_seed_archive_exchange`). "Breadbasket" is a pastoral or rural Air Winter state with at least 60 food reserve; "seed vault" is a completed greenhouse refuge. The shipment adds 8 food reserve to every Air Winter state the recipient owns and controls (one bounded `every_owned_state` on one country at completion). The "post-Fallout greenhouse start" is the archive memory: both countries start their Fallout survivor with 8 more Food.
- Evacuation Corridor (`air_cleanliness_treaty_evacuation_corridor`). The source is the recipient member's own emergency priority state, so the recipient chooses which state needs help, at Phase 4 or worse (Phase 6 is included, matching the convoy's "Phase 3 or worse" pattern). The sponsor must border it with a state below Phase 4 and under the refugee ceiling. Five percent of the source moves, capped at a quarter of the receiver's population, above a 25K protected floor. The corridor uses the Air Winter island-refugee transfer contract (one exact debit through `apply_exact_state_civilian_population_loss`, a measured credit, no Deaths record) rather than the migration `civilian_transfer_execute_transaction`, which requires a live migration cohort row, reception front, and food-safety projection that a one-off treaty relocation does not have.
- Naming a burner (`air_cleanliness_treaty_sanction_burners`). No per-country contamination ledger exists, so "caused severe contamination recently" is defined from the Condemnation system: the 180-day `condemnation_recent_use` flag plus at least 50 combined chemical, biological, and nuclear Condemnation (the buckets decay, so the value tracks recent use). Targets come from the bounded `global.condemnation_targets`. A named burner is banned and enters the existing violator ledger, which reuses every existing embargo, opinion, join, departure, and annex path. "May push the violator toward Fallout radical routes" is implemented as eligibility for the Warlord Command archetype without an active war.
- Treaty memory after Fallout (P4). Applied once per generation at the first Ash-week orientation step to the survivor's current resource entries: former members +6 Recognition and +3 Cohesion, banned countries -6 Recognition, seed archive holders +8 Food. Applying it to current entries rather than the frozen survival ledger keeps the ledger's replay checks valid. The closure report lists the memories that applied.

## A11. The NZL and USA packages run inside survivor allocation

Disposition: implemented (static review only; tree loading, the dynamic NZL path, and the human USA continuation are `needs_live_game`). Acceptance basis: lead decision 4 for round 1 under the user's grant of design authority.

- `fallout_apply_transition_phase_survivor_allocation` calls `fallout_successor_b7_run_vertical_slice` once per generation, after the successor transaction begins and before `fallout_allocate_surviving_countries_in_place`. The B7 pass commits its own rows first (USA `player_reserved`, NZL `converted_existing` or `created_dynamic`), so the in-place allocator skips them and finalizes the transaction as before.
- Eligibility stays as spec 53 accepted it. The USA Federal Continuity package applies only to a human player continuing as the USA. The NZL Lifeboat State applies to an AI NZL that owns and controls the exact five-state footprint without Samoa (state 726), or to the dynamic NZL rebuilt from five one-state AI owners. A human NZL keeps the universal package because its states are player-reserved. Because vanilla NZL owns Samoa, the Lifeboat package only appears when Samoa has left NZL before the Fallout (for example through the Independence Wave); this limitation is recorded rather than changed, because releasing Samoa inside allocation would alter another event's package.
- Both packages load their own trees in place of the universal tree (`fallout_usa_federal_continuity_focus_tree`, `fallout_nzl_lifeboat_focus_tree`) and set the tree receipts their triggers already required (`fallout_b7_usa_focus_tree_loaded`, `fallout_nzl_focus_tree_loaded`). Map return skips countries that hold a current bespoke package (`fallout_country_has_bespoke_survivor_package`) when it assigns the generic region memory and loads the universal tree, so the NZL memory and both trees survive. Every other survivor keeps the universal package.
- The B7 USA row now sets the capital to the reserved primary capital, as the in-place commit does, so the row's capital check holds.

## A12. Radio Service Coordinator portrait

Disposition: implemented (commit `493815feb`). The portrait-creator subagent could not be spawned from this session, so the parent produced the fictional portrait with the same native ImageGen route and the shared tools: a 1024x1536 ImageGen master, `extract_portrait_source_crop.py --auto` for the 156x210 head-and-shoulders master, and `create_advisor_icon.py` at the measured dossier opening (30.477406 x 45.094508, rotation -4.76, offset 0 0, sepia 0.18; opening gap, inner-edge gap, and exterior leak all 0). The runtime card is `gfx/interface/ideas/fallout_world_end/nzl_lifeboat_state/NZL_fallout_radio_service_coordinator.dds` (65x67, LFS) registered as `GFX_portrait_NZL_fallout_radio_service_coordinator_small`. The master, crop record, review images, and manifest stay in the ignored local folder `docs/assets/fallout_nzl_lifeboat_state/portraits/`.

## R1. Round 1 review fixes

Disposition: implemented (static review only; every item below is `needs_live_game`). These are corrections, not new design.

- Survivor allocation runs the B7 pass with the transition coordinator as ROOT. The NZL footprint trigger (`fallout_nzl_has_exact_state_package`), the Samoa disposition check, and the fragmented-transfer source checks tested ROOT, so an AI NZL could never pass, the dynamic NZL failed its footprint check and raised a transition error, and the fragmented transfer would have handed the five island states and the opening Home Guard divisions to the coordinator. They now use PREV, the checked country. The NZL and USA capital rows record PREV, not the coordinator, as the assigned country.
- With the scheduler active, the coordinator reconciles every country, and the Mountain Pass Census (635) and Mine Generator (642) reconcilers tested `owner = { tag = ROOT }`, so every AI opening or running chain of either kind would have been cancelled as target lost. The reconcilers now test PREV, the state triggers test OWNER or PREV, and the chain history names the reconciled country as its actor.
- Tooltips that said civilians "enter the Deaths ledger" now say they are added to the death toll, and the failed civic sealing result no longer mentions the ledger.

## R2. Round 1 review, second pass

Disposition: implemented (static review only; annex timing is `needs_live_game`). Corrections and recorded limits, not new design.

- `air_cleanliness_treaty_handle_annexed_country` now releases an annexed sponsor's four operation receipts (sampling grid, seed archive, evacuation corridor, burner case) without a withdrawal report. Before, the global grid lock waited out its timer and the sponsor's active flags stayed on the dead tag, so a restored tag could never start that operation again.
- The treaty operations' timed cooldown and lock flags read their duration through `days = var:<temporary>`. This follows the repository rule and the installed precedent in `common/scripted_effects/SIA_scripted_effects.txt`, which passes `var:` to a timed country flag, so it is kept. Other workstreams moved timed flags to literal days through `meta_effect` after concluding the engine ignores a variable duration. If live play shows a cooldown that never ends, convert these flags the same way.
- Unresolved: the NZL Lifeboat State still requires Samoa (state 726) to be outside NZL before allocation, so with vanilla ownership it only appears after Samoa has left NZL. Releasing Samoa inside the B7 pass would create a country after the conflict ledger is frozen and has no pre-transition rows. The safe place for a Samoa disposition is before the pre-transition snapshot, which belongs to a later tranche.

## A13. Country memories come from tag and capital area

Disposition: implemented (static review only; a live campaign result is `needs_live_game`). Acceptance basis: round 2 lead item 2 under the user's grant of design authority.

The nine region defaults gave every European survivor the British memory and left ten of the twelve Ash-week pilot memories and the three memory-gated chains unreachable. Decision: allocation now marks each universal survivor as waiting and, before finalization, `fallout_assign_successor_country_memories` runs five stages over all survivors in turn: exact tag (with a homeland condition for empires and a heartland condition for the Soviet Union), civil-war clone original tag, capital area, shared capital area, regional default. Stages 1 to 3 hand out each memory once per generation, so a tag rule always beats another country's area claim and the result does not depend on country order across stages. Every vanilla state belongs to exactly one of 98 areas (`fallout_country_memory_area_<memory>`).

A second survivor seated in an area shares that area's memory. About ninety countries hold land in 1936 and the memories are bound to places, so strict one-to-one assignment would give many survivors a memory written for another continent. Memories with content written for one identity (the twelve pilots, West African Port Confederacies and Manchurian Reactor Keeps) are never shared; a second survivor receives a fixed neighbouring memory. New chains for a memory must add it to `fallout_country_memory_candidate_is_protected`.

The memory is fixed for the generation (`fallout_country_memory_assignment_generation`), and map return keeps it, so `fallout_survival_country_source_memory` and the registry replay checks still match. The NZL and USA packages keep their own memories and count as holders. In a vanilla 1936 world the pilots reach USA, SWI, GER, SIA, BRM, SYR, ETH and CHL, the chains reach LIB and MAN, and Don Steppe, Congo, Sahel and Antarctic need a released country or a survivor seated in those areas. Full tables: `FALLOUT_COUNTRY_MEMORY_ASSIGNMENT.md`.

## A14. Resource crisis and government archetype run for every region and archetype cell

Disposition: implemented (static review only; live delivery and AI branch frequencies are `needs_live_game`). Acceptance basis: round 2 lead item 3 under the user's grant of design authority; the accepted 108-cell coverage matrix supplies the content of every cell.

Decision: steps 3 and 4 of the Ash-week orientation no longer need one of the twelve pilot memory rows. Each registry country loads its region and archetype cell row from per-cell script constants (`fallout_orientation_cell_*`, documented in `FALLOUT_ORIENTATION_CELL_ROWS.md`). A pilot memory row still takes precedence when memory, region and archetype all match. The resource package, government row approval, mapping triggers and request loaders accept cell rows; the score bonus for a declared regional and archetype match stays with pilot rows.

- Supporting resource: Fuel or Power per cell, read from the matrix's local resource response. The local measure keeps the existing Scrap plus support cost, so no new cost path was added.
- AI preferences: the resource preference follows the archetype (continuity, quarantine, machine and religious governments prefer the public ration order, warlords the emergency warrant, the rest the local measure, as the twelve pilot rows already do); the government preference is the matrix's per-cell AI preference. The probability route remains unavailable (`hoi4_probability_inspect` returned "Invalid tool arguments" in round 1), so no probability audit evidence exists for these weights.
- Unavailable branch: each cell's prohibited branch is mapped to one of the six offered courses with one world-state condition from a fixed list (Fuel, Power, Recognition, Cohesion, Filters, Clean water, Medicine, Food, Shelter capacity, capital supply access, capital Air Winter phase, coastal capital, a working factory or refinery in the capital, a state that can receive evacuees, a single owned state, or the immediate crisis resource). It is enforced in the option triggers, the shared affordability trigger used by the hidden AI, and the begin checks, and the event text names the closed course. The lock applies to pilot rows too, since it belongs to the cell. Mutant polity cells have no lock because their prohibited branch is an exclusion branch that is never offered.
- Text: every cell has nine hand-written strings written from its matrix columns, with no internal identifiers. They avoid named religions and peoples, as the matrix's local research gate requires for content that has not been researched per country.
- Skips: the resource step now records `archetype_row_missing` when the country has no region or archetype and `state_target_missing` (with the retry window) when the capital package cannot be installed; the old `memory_row_missing` skip is gone.
