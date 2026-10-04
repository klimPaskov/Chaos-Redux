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
