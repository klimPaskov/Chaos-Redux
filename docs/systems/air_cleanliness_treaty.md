# Air Cleanliness Treaty

## Current implementation boundary

The Air Cleanliness Treaty is a persistent severe-contamination diplomacy and Air Winter mitigation system. It forms at 75 percent Air Contamination when at least one eligible founder has been observed by the existing Air Winter state pass.

The implemented tranche contains:

- deterministic founder selection
- generation-bound invitations
- idempotent membership registration and removal
- treaty-owned opinion and embargo cleanup
- permanent violation memory
- non-periodic annex cleanup
- an atomic Global Cleaning Day project
- a country-targeted Joint Filter Convoy project
- a state relief route lasting up to six months that feeds the existing Air Winter pressure formula
- a Fallout pause receipt that ends operational projects while preserving treaty memory
- AI weights for joining and both projects

The broader accepted treaty package is not complete. Pooled decontamination, seed archive exchange, evacuation corridors, inspections, votes, sanctioning of major burners, and improved forecast precision beyond shared basic sampling remain unimplemented.

## Runtime owner

`air_contamination_monthly_update` remains the only global monthly Air Cleanliness coordinator. It calls `air_cleanliness_treaty_pre_winter_pulse` before the existing state pass and `air_cleanliness_treaty_host_pulse` afterward. The pre-pass removes invalid routes before winter pressure is calculated. The post-pass records `global.date`, reconciles current membership, and uses only bounded arrays.

The treaty does not add an `on_monthly`, `on_daily`, or other periodic on action. `common/on_actions/air_cleanliness_treaty_on_actions.txt` contains only `on_annex`, where ROOT is the annexer and FROM is the annexed country. Annex cleanup is disabled during Fallout transition and Fallout so the world rewrite cannot fire treaty reports or elect transient founders.

## Persistent ledgers

The principal scope arrays are:

- `global.air_cleanliness_treaty_members`
- `global.air_cleanliness_treaty_violators`
- `global.air_cleanliness_treaty_relief_states`
- `global.air_cleanliness_treaty_filter_convoy_donors`

Mutation queues are separate from the arrays they repair:

- `global.air_cleanliness_treaty_member_removals`
- `global.air_cleanliness_treaty_violation_queue`
- `global.air_cleanliness_treaty_route_removals`
- `global.air_cleanliness_treaty_filter_convoy_cancellations`

The code never removes a member or state while iterating the same registry. It first records the scope in the appropriate work queue and mutates the source registry during a second loop.

## Formation and invitations

At or above `constant:air_contamination_threshold_bp.winter_75`, the host examines `global.air_winter_registered_countries`. It chooses the eligible founder with the lowest live country id. No random country selector or world-country scan is used.

Formation increments `global.air_cleanliness_treaty_generation`, registers the founder, stores `air_cleanliness_treaty_founder`, fires `chaosx_contamination.7` and `.10`, and issues the first invitation set.

Each observed country stores `air_cleanliness_treaty_invitation_attempt_generation` before the delayed event command is emitted. The invitation has a thirty-day pending window and a two-day delivery delay. The terminal generation receipt is written only when the event opens. A decline or completed invitation prevents another offer during the same treaty generation. A delivery that fails because the founder or recipient is temporarily invalid can be tried again on a later ninety-day bounded scan.

Event `chaosx_contamination.9` validates the current generation and persistent founder before opening. Acceptance calls `air_cleanliness_treaty_register_member`. It does not set a membership flag directly.

## Membership and sanctions

Registration sets the current and historical membership flags, adds one country-scope array entry, applies mutual cooperation only against current members, and clears treaty-owned embargo residue between members. Opinion edges remove the treaty-owned modifier before adding its one current instance. Schema reconstruction routes through the same edge helpers, so restored member and violator arrays restore their permanent opinions and native embargo ownership without stacking duplicate treaty modifiers.

A new member also joins the active sanctions ledger against existing treaty violators. The native embargo helper records the Air Cleanliness Treaty as a separate relation owner. Removing treaty ownership breaks an engine embargo only when no condemnation, Great Embargo, external, or other tracked owner remains.

An unconventional-weapon hook calls the compatibility effect `air_cleanliness_treaty_on_unconventional_use`. The wrapper delegates to the idempotent violation transaction. A current member is removed once, added to the violator registry once, marked with `air_cleanliness_treaty_betrayal_memory`, stripped of active relief routes, and sanctioned only by current members. The violation news report can fire only once for that country.

Opinion modifiers are permanent while their lifecycle edge exists. Member departure removes mutual cooperation and the departing country's treaty sanctions. Annexation removes the absent country from live registries while preserving its betrayal flag for a later return.

## Global Cleaning Day

`air_cleanliness_global_cleaning_day` is a forty-five-day atomic project. Air Contamination must be above the project floor and below the irreversible boundary when work begins. The sponsor and at least one other signatory must remain live members through completion, and the sponsor must possess the required support equipment, convoys, and available civilian factories at the start. Crossing the irreversible boundary or falling below the full one-hundred-basis-point result cancels the project before it can enter a clamped reduction path.

Equipment is removed at project start. A global transaction number, a sponsor receipt, a generation receipt, a global lock, and a persistent sponsor target prevent concurrent starts and duplicate completion. Successful completion reduces Air Contamination by one hundred basis points, starts a one-hundred-eighty-day cooldown, and fires `chaosx_contamination.11`.

Cancellation releases every lock and receipt. Equipment already issued from depots is not refunded.

## Joint Filter Convoy

`air_cleanliness_joint_filter_convoy` is a targeted country decision backed by `target_array = global.air_cleanliness_treaty_members`. The decision contract is ROOT as donor and FROM as recipient.

The recipient must retain a designated priority state that is:

- a valid Air Winter state
- at Phase 3 or worse
- owned and controlled by the recipient
- still marked as the recipient's priority state
- free of another active or reserved treaty route

The donor and recipient must be distinct live members and cannot be at war. The donor pays support equipment and convoys at dispatch and reserves civilian factories for twenty-one days. The donor enters a dedicated active-project registry. The selected state stores the donor, recipient, treaty generation, and reservation flag. Ownership, control, membership, generation, and war status are checked again before arrival.

Arrival applies existing Air Winter response values for filters and clinic sheltering. It reduces exposure and disease pressure, improves adaptation, shelter, and recovery, normalizes the state ledger, and recalculates `air_winter_survival_value`. It also sets `air_winter_relief_route` for one hundred eighty days. The existing Air Winter pressure calculator subtracts `constant:air_winter_pressure.relief_route` while that flag remains active.

Active route states are held in a bounded registry. A route is removed before monthly winter pressure if its timed flag expires, the owner or controller changes, either country leaves the treaty, either country violates the treaty, the treaty generation changes, or the two countries enter a war. Membership removal, dissolution, annexation, and Fallout also cancel active donor projects and release exact state reservations through the dedicated donor registry.

All three Air Winter map modes display whether the selected state currently has a treaty filter route.

## AI behavior

Invitation AI weighs government, major status, unconventional stockpiles, prior weapon use, and war with the founder.

Cleaning Day AI weighs government, war strain, and very high Air Contamination. Filter Convoy AI has a zero-validity gate through the decision availability trigger. It then weighs donor capacity, war strain, target phase, and critical target survival value. Every AI value is stored in `common/script_constants/air_cleanliness_treaty_constants.txt`.

## Files

- `common/script_constants/air_cleanliness_treaty_constants.txt`
- `common/scripted_triggers/air_cleanliness_treaty_triggers.txt`
- `common/scripted_effects/air_cleanliness_treaty_effects.txt`
- `common/scripted_effects/chaos_meter_effects.txt`
- `common/scripted_effects/air_cleanliness_winter_effects.txt`
- `common/scripted_effects/fallout_world_end_effects.txt`
- `common/scripted_effects/chaosx_welcome_effects.txt`
- `common/decisions/air_cleanliness_treaty_decisions.txt`
- `common/decisions/categories/air_cleanliness_treaty_categories.txt`
- `common/on_actions/air_cleanliness_treaty_on_actions.txt`
- `events/air_cleanliness_treaty_events.txt`
- `events/chemical_warfare_events.txt`
- `common/opinion_modifiers/air_contamination_opinion_modifiers.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_map_modes.txt`
- `localisation/english/_chaosx_events_l_english.yml`
- `localisation/english/chaosx_decisions_l_english.yml`
- `localisation/english/chaosx_map_modes_l_english.yml`
- `localisation/english/chaosx_modifiers_l_english.yml`

## Icons and event images

No new visual asset is required by this tranche.

- Treaty category: `GFX_decision_category_contamination_defense`, defined in `interface/chaosx_decisions.gfx`, with texture `gfx/interface/decisions/decision_category_contamination_defense.dds`
- Both projects: `GFX_decision_generic_operation`, defined by vanilla `interface/decisions.gfx`, with texture `gfx/interface/decisions/decision_generic_operation.dds`
- Formation, invitation, and succession reports: vanilla `GFX_report_event_generic_sign_treaty2`
- Cleaning Day report: vanilla `GFX_report_event_generic_sign_treaty1`
- Violation report: Fallout-independent Chaos Redux sprite `GFX_news_event_chaosx_cbw_doom`
- Convoy reports: vanilla `GFX_report_event_generic_factory`

A future dedicated treaty icon package should use a treaty-owned directory and stable sprite ids before art is commissioned. That package is not required for the implemented decisions to render.

## Proof and runtime boundary

Static engine proof is recorded in `docs/plans/air_cleanliness_fallout_plans/AIR_CLEANLINESS_TREATY_LIFECYCLE_PROOF.md`.

Hearts of Iron IV was not launched. Targeted decision persistence, delayed invitation delivery, mapmode text rendering, native embargo behavior, Fallout pause timing, and save reconstruction remain runtime observation gates. No runtime pass is claimed.

## Future plans

1. Add pooled state decontamination through the existing Air Winter decontamination project and formula.
2. Add seed archive exchange with food, adaptation, and memory effects.
3. Add bounded evacuation-corridor projects using the existing reception-state ledger.
4. Add inspection and vote transactions with explicit member receipts.
5. Add sanctions against major atmospheric burners only after an exact target ledger is defined.
6. Carry membership and betrayal memories into Fallout successors only after the pending post-Fallout treaty policy is approved.
