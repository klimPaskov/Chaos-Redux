# Fallout The Last Inventory implementation handoff

## Scope

This tranche defines the dormant global-survival food-security chain reserved by
Fallout event suffixes `100` through `106` and `123` through `126`.

- `100` is the human opening with three concrete choices.
- `101` is the deterministic hidden-AI opening.
- `102`, `103`, and `104` are branch-specific delayed results.
- `123`, `124`, and `125` are hidden-AI delayed results using the same effect path.
- `105` and `126` are the visible and hidden-AI first winter callbacks.
- `106` releases the authenticated cleanup row.

The chain remains dormant. No effect in this tranche sets
`fallout_event_scheduler_activation_approved` or
`fallout_event_scheduler_active`, and no ordinary candidate caller was added.
The release-floor count remains unchanged.

## Engine surfaces and contracts

The opening uses `fallout_event_country_can_receive_ordinary_event` and
`fallout_event_issued_ordinary_receipt_is_current`. The single coordinator in
`common/scripted_effects/fallout_world_end_food_event_effects.txt` captures the
issued mode, target, token, and ticket, reserves a delayed row, then consumes
the exact ordinary receipt. If the receipt cannot be consumed, the newly
reserved row is cancelled with `caller_cancelled`.

Result and callback events authenticate the issued delayed token, mode, and
branch before applying effects. Results are terminalized, their row is marked
for cleanup, and a callback row is reserved with a distinct transaction-key
offset. Callback resolution marks its own row for cleanup. Event `106` uses the
hidden cleanup token and the native delayed-row release wrapper.

The human and hidden-AI routes share the same branch effects, outcome bands,
survival-ledger mutation, Deaths call, event-log payload, callback, and cleanup.
The AI branch is deterministic. Very low food selects requisition. Democratic
or communist governments publish the ledger. Low recognition selects household
caches. The remaining case publishes the ledger.

## Gameplay effects

The result writes only through the Fallout survival ledger for food,
recognition, and cohesion. Stability and war support use the normal country
effects. Requisition failure applies a one percent state population loss in
every owned state through `apply_exact_state_civilian_population_loss` with the
`fallout_aftermath` Deaths reason. No direct state-population mutation is used.

The callback opens two authored decision surfaces in
`common/decisions/fallout_food_security_decisions.txt`:

- `fallout_event_100_ration_law` spends food and filters during a three-week
  review, then restores food, recognition, and cohesion if the review closes.
- `fallout_event_100_first_hunger_mission` spends food and medicine during a
  two-week mission, then records food, recognition, and cohesion recovery.

Failure or cancellation applies the dedicated
`fallout_food_grievance_aftershock` modifier. Result branches use dedicated
country modifiers for public ration law, household caches, and requisition
authority. The event picture is the reviewed Fallout asset
`GFX_report_event_fallout_last_inventory`.

The two callback decisions use the existing Fallout icon
`GFX_idea_fallout_state_grade`, registered in
`interface/fallout_world_end.gfx` and sourced from
`gfx/interface/ideas/fallout_world_end/idea_fallout_state_grade.dds`. No zombie
asset, sprite, or path is referenced. A future food-security asset tranche may
replace this shared Fallout idea icon after the decision family is expanded.

## Event Log surfaces

Result and callback commits append the dedicated Fallout history id `9105` with
branch and outcome payloads. `GetEventsLogHistoryEventName` and
`GetEventsLogEventDetailDescription` now resolve the name and payload-specific
detail text through `GetFalloutEvent100EventLogDetail`. This is a history row,
not a new ordinary event-log registry candidate.

## Review status and limits

Static checks for this handoff include duplicate event-id scan, brace-count
balance on touched Clausewitz files, localisation-key duplicate scan, BOM
presence, and unsupported operator scan. HOI4 was not launched.

The chain is not counted toward the 660-block release floor until the exact
Fallout caller, orientation completion, scheduler activation review, runtime
save and multiplayer behavior, and manual human and AI event-log detail review
are completed. The callback flags are durable opening receipts for the two
decision surfaces, not a claim that the wider ration-law or hunger-mission
families are complete.

## Future expansion

The next reviewed tranche should add a water-security companion that reads the
same state grade and current Supply Access receipt, then a shelter chain that
can alter the exposure and disease rows without bypassing the Deaths system.
The food family should eventually gain a regional harvest branch, a military
convoy branch, and a successor-specific memory branch. Each addition needs its
own delayed tokens, branch bounds, event-log payloads, AI resolution, and
cleanup receipt before it can be counted in the release floor.
