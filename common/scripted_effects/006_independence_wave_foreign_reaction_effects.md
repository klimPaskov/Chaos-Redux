# Event 006 foreign reaction effects

Source: `common/scripted_effects/006_independence_wave_foreign_reaction_effects.txt`.
Triggers: `common/scripted_triggers/006_independence_wave_foreign_reaction_triggers.txt`.
Constants: `common/script_constants/006_independence_wave_foreign_reaction_constants.txt`.
Events: `events/006_independence_wave_foreign_reaction_events.txt` (`chaosx.nr6.64` to `.72`).
Decision: `common/decisions/006_independence_wave_foreign_reaction_decisions.txt` (remnant petition).
Mechanic overview: `docs/events/006_independence_wave/foreign_reactions.md`.

## Lifecycle effects

### `independence_wave_foreign_reaction_build_queue`

- Scope: any country. Called only by `independence_wave_host_response_finish_plan` before it clears host and opening receipts.
- Guards: report barrier raised, committed plan, report plan id equals the current plan, no Join conversion for the plan, aligned plan arrays, not already built for this plan.
- Steps: freezes the committed Event 006 cohort in report row order (temporary array `independence_wave_foreign_cohort_targets`); gathers candidates from each target's registered package contacts (first), neighbors, patron entries, recognition receipt entries, the allies of its living former host, and `global.independence_wave_active_countries`; scores every actor/target pair; reserves one receipt for each actor whose best score is at least 6; schedules `.64` one day apart and `.72` on every target at the queue deadline.
- Outputs: `global.independence_wave_foreign_reaction_plan_id`, `global.independence_wave_foreign_reaction_actors`, `global.independence_wave_foreign_reactions_remaining`, global flag `independence_wave_foreign_reaction_queue_pending` (only when at least one receipt exists), `global.independence_wave_foreign_reaction_built_plan_id`.
- Side effects: the global flag keeps the report/reset barrier raised until the queue closes.

### `independence_wave_foreign_reaction_add_candidate`

- Scope: a candidate country inside the builder.
- Adds the country once when it is living, sovereign, outside the cohort, and not a host answering this wave through its host response. Bounded by `independence_wave_foreign_capacity.actor_cap`.

### `independence_wave_foreign_reaction_load_cohort_target` / `independence_wave_foreign_reaction_load_receipt_targets`

- Load the event targets `independence_wave_foreign_target`, `independence_wave_foreign_target_host` and (receipt variant) `independence_wave_foreign_actor`, and the temporary `independence_wave_foreign_target_has_host` (0 or 1).
- Input for the cohort variant: temporary `independence_wave_foreign_target_index`.

### `independence_wave_foreign_reaction_score_pair`

- Scope: the actor, with the event targets loaded.
- Outputs: temporary `independence_wave_foreign_score` (direct stake 4, recorded relationship 3, strategic fit 2, political fit 1, conflict -3, floor 0) and `independence_wave_foreign_tier_result` (earlier wave; great power only with a recorded relationship, which includes a registered package contact; regional for a package contact, strategic fit or no shared frontier; neighbor).
- No side effects.

### `independence_wave_foreign_reaction_record_reasons` / `independence_wave_foreign_reaction_clear_reasons`

- Scope: the actor. Sets or clears the `independence_wave_foreign_fact_*` and `independence_wave_foreign_family_*` country flags read by the event text and the AI policy.

### `independence_wave_foreign_reaction_reserve_actor`

- Scope: the actor, inside the builder. Writes the receipt: flag `independence_wave_foreign_reaction_pending`, variables `independence_wave_foreign_reaction_plan_id`, `_target`, `_target_generation`, `_tier`, `_score`, `_host`; appends the actor to the global array and schedules `.64`.

### `independence_wave_foreign_reaction_route_actor`

- Scope: the actor in `.64`, where ROOT is the actor.
- Re-checks the receipt and the live pair score. Humans receive `.65` to `.68` by tier; AI actors resolve through `independence_wave_foreign_reaction_resolve_ai_action` and `independence_wave_foreign_reaction_resolve_choice`. An invalid receipt or a score below 6 completes without effect.
- `.64` routes the actor only when it was not sent to answer a patron offer or a remnant petition, so an AI recipient's own reaction keeps its scheduled dispatch day.

### `independence_wave_foreign_reaction_resolve_choice`

- Scope: the actor (ROOT). Input: temporary `independence_wave_foreign_action_input` (`independence_wave_foreign_action`).
- Applies the stance and completes the receipt. A patron offer leaves the receipt waiting for the consent reply.

### `independence_wave_foreign_reaction_complete_current_actor`

- Scope: the actor. Consumes the receipt once, decrements the remaining count, and calls `independence_wave_foreign_reaction_finish_queue` at zero. Does nothing while the actor waits for a consent reply.

### `independence_wave_foreign_reaction_finish_queue`

- Scope: any. Clears every actor receipt and open offer of the current queue, clears the queue globals and flag, and calls `independence_wave_host_response_release_report_barrier` when the barrier belongs to the same plan.

### `independence_wave_foreign_reaction_check_deadline`

- Scope: a target in `.72`. Each target stores `independence_wave_foreign_deadline_plan_id` and `independence_wave_foreign_deadline_date` when the queue is raised; the date is the last dispatch plus the response and consent timeouts, converted with `chaosx_convert_days_to_date_offset`, and the event follows it by `deadline_margin_days`. The event closes the queue only once `global.date` has reached the stored date and the stored plan id is still the open queue. An earlier queue's event that arrives after the target was rescheduled finds a later date and does nothing, so it neither closes the newer queue nor clears its schedule.

### `independence_wave_foreign_reaction_release_annexed_country`

- Scope: the annexed country in `on_annex`. Closes an open offer held by the country and consumes its actor receipt.

## Stance effects

All stance effects run in actor scope with ROOT as the actor and the receipt targets loaded. `independence_wave_foreign_reaction_apply_action` re-checks each stance's availability trigger; a stance that no longer qualifies resolves as noncommittal.
The recognition and guarantee stances create caller-owned storage for `independence_wave_bilateral_receipt_new` with `constant:independence_wave_value.minimum` before calling the shared transaction helper.
The helper may modify that storage, and the stance consumes the result only after return.

| Effect | Cost | Result |
| --- | --- | --- |
| `independence_wave_foreign_reaction_apply_recognition` | Light diplomatic, or none when the target already paid for a recognition mission to this actor | Shared recognition receipt; when new, Legitimacy +minor and Recognition +standard, host hostility and pressure +minor, opinions, public history |
| `independence_wave_foreign_reaction_apply_mediation` | Standard diplomatic | Border, hostility, claim, dispute and reconquest-fear ledger toward settlement, Legitimacy +minor, Instability -minor, opinions, public history |
| `independence_wave_foreign_reaction_apply_containment` | Light diplomatic (standard for a great power) | Hostility, pressure and reconquest fear rise, Recognition -minor, Instability +minor, host opinion up, AI contain/befriend strategies, public history; no war |
| `independence_wave_foreign_reaction_apply_guarantee` | Standard diplomatic, or none when the target already paid to ask this actor | Real engine guarantee through `independence_wave_apply_bilateral_guarantee`; when new, the DM-13 award, opinion, AI protect strategy, public history |
| `independence_wave_foreign_reaction_apply_network_aid` | Light command power and equipment sent from the actor's stockpile | Security +standard (+major under war or severe threat), Instability -minor, network standing for both, public history |
| `independence_wave_foreign_reaction_apply_contest` | Light diplomatic | Legitimacy -minor, Recognition -standard, Instability +minor, opinion, AI antagonize strategy; no history |
| `independence_wave_foreign_reaction_make_offer` | Standard diplomatic | Opens the target's patron offer (`independence_wave_foreign_offer_*`) and sends `.71` to a human or `.64` to an AI target |

## Consent effects

### `independence_wave_foreign_reaction_resolve_offer`

- Scope: the released country, where ROOT is that country (`.71` or `.64`).
- Input: temporary `independence_wave_foreign_offer_reply_input` (`independence_wave_foreign_offer_reply`).
- Arms offer: acceptance delivers the full shipment from the donor and books an arms channel (standard influence, major aid) with the DM-31 values; a limited answer, or an acceptance when the donor can no longer spare the full shipment, delivers the standard infantry shipment and books a light channel.
- Corridor offer: acceptance builds one capital infrastructure level and books a trade channel (standard influence and aid); a limited answer books a light channel.
- Refusal: Legitimacy +minor and the donor's opinion falls.
- Always calls `independence_wave_foreign_reaction_close_offer`, which completes the waiting actor once.

### `independence_wave_foreign_reaction_resolve_ai_offer`

- Scope: an AI released country. Accepts below the patron dominance warning, limits below dependency, refuses beyond it.

## Remnant petition effects

### `independence_wave_remnant_petition_open_window`

- Scope: the host, called from `independence_wave_host_response_apply_current_action` when a remnant settlement sets the outside-guarantee opportunity.
- Consumes the opportunity flag. When the host has not used its petition (`independence_wave_remnant_petition_used`), stores `independence_wave_remnant_petition_plan_id`, ranks a recipient through `independence_wave_remnant_petition_select_candidate`, and opens the timed `independence_wave_remnant_petition_window` flag for `independence_wave_remnant_petition.window_days` only when a recipient qualifies.

### `independence_wave_remnant_petition_select_candidate` / `independence_wave_remnant_petition_consider_recipient`

- Scope: the host / each neighbor and ally of the host. Event targets `independence_wave_petition_host`, `independence_wave_petition_recipient`, `independence_wave_petition_best_recipient`.
- Output: host variable `independence_wave_remnant_petition_candidate`, the first highest-scoring recipient at or above the cutoff.

### `independence_wave_remnant_petition_submit`

- Scope: the host taking `independence_wave_petition_foreign_guarantee` (ROOT is the host). Sets the identity receipt, the pending flag and `independence_wave_remnant_petition_recipient`, marks the recipient (`independence_wave_remnant_petition_received`, `_from`, `_received_plan_id`) and sends it `.69` or, for AI, `.64`.

### `independence_wave_remnant_petition_resolve` / `independence_wave_remnant_petition_resolve_ai`

- Scope: the recipient (ROOT is the recipient). Input: temporary `independence_wave_remnant_petition_reply_input`.
- Acceptance pays the standard diplomatic cost, gives the real guarantee, makes the host grant military access, adds opinions and a `protect` AI strategy, and records history payload 35. Refusal adds the host's refusal opinion. An invalid petition lapses without effect.
- Always calls `independence_wave_remnant_petition_notify_host`, which stores the outcome on a waiting host and sends `.70`.

### `independence_wave_remnant_petition_end_identity`

- Scope: an annexed country (`on_annex` FROM) or a released country (`on_release_as_free` / `on_release_as_puppet` ROOT). Lapses an open received petition and clears the host's petition state and identity receipt.

## Example

```
# Inside the final host-response callback, before plan receipts clear:
independence_wave_foreign_reaction_build_queue = yes
```
