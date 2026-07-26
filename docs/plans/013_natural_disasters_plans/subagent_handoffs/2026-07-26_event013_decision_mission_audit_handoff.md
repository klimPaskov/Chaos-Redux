# Event 013 decision and mission audit handoff

Audit date: 2026-07-26.

Scope: disaster-specific decision categories, aftermath missions, foreign relief, active caps, AI targeting, cleanup, cost clarity, and category-picture wiring.

## Changed file

- `common/scripted_effects/013_natural_disasters_effects.txt`

Changed identifier:

- `natural_disaster_select_priority_open_card`

## Fixed issue

High, fixed: the outbound relief decisions proved that a recipient had at least one compatible recovery card, but `natural_disaster_select_priority_open_card` only gave compatibility a score bonus.

Consequently, an unrelated high-population or high-severity card could win the selection for `natural_disaster_offer_port_lifeline_relief`, `natural_disaster_offer_engineer_relief`, or `natural_disaster_offer_medical_relief`.

The resulting recipient route could conflict with the package's advertised physical purpose, such as a port-lifeline package targeting an inland card.

The selector now requires a candidate to match the calling package before ranking it.

- Variant `neighbor_convoy` remains eligible for every live recovery card.
- Variant `port_lifeline` requires `is_coastal = yes`.
- Variant `engineer` requires `natural_disaster_state_has_strategic_transport` or `natural_disaster_state_has_industry`.
- Variant `medical` requires `natural_disaster_state_has_dense_population` or `natural_disaster_disease_pressure`.
- Generic recovery and category-display callers retain variant zero and remain unrestricted.

This is a targeting guard only.

Costs, capacity, AI weight, and relief duration are unchanged.

## Decision-category lifecycle and art

`natural_disaster_aftermath_category` is visible only for a live warning, controlled open aftermath card, or inbound relief.

`natural_disaster_foreign_relief_category` only appears when an inbound relief action is active or the donor has at least one payable, valid recipient.

`natural_disaster_refresh_category_display_family` clears stale display variables and selects a valid controlled state before the category's triggered family picture is resolved.

The aftermath category's 22 `GFX_decision_cat_picture_nd_*` references all resolve in `interface/013_natural_disasters.gfx`, and every referenced texture exists.

No decision-owned scripted GUI source was changed.

No GUI inspection or render artifact was required because this audit changed neither a decision GUI surface nor shared UI.

## Mission quality notes

| Owner and category | Region and requirement | Duration | Success, partial failure, and duplicate risk |
| --- | --- | --- | --- |
| Country / aftermath rescue slots `natural_disaster_rescue_mission_1` through `_4` | One current-controller early-rescue card per mapped slot | 35 days | Full success at three score, partial at two, otherwise failure; distinct capacity slots rather than duplicate rewards. |
| Country / aftermath stabilization slots `natural_disaster_stabilization_mission_1` through `_3` | One controlled middle-stabilization card per mapped slot | 90 days | Full success at four score, partial at three, otherwise failure; state loss or phase closure cancels and refills safely. |
| Country / aftermath reconstruction slots `natural_disaster_reconstruction_mission_1` through `_3` | One controlled late-reconstruction card per mapped slot | 210 days | Full success at five score, partial at four, otherwise failure; state loss or phase closure cancels and refills safely. |
| Country / typed chain objective | One selected unresolved chain card with prevention score | Dynamic to persisted chain due date | Seven typed missions use a one-day base plus the exact stored due-date extension, preserving family-specific 2–180 day chain windows; success, partial prevention, and failure set separate state results. |
| Recipient country / foreign relief | A routed, controlled live aftermath card | 45 days | Arrival adds the relevant phase score and package effect; timeout degrades the card; cancellation, completion, and timeout clear state, donor, route, and variant pointers. |

The active-cap helper uses base caps of rescue 3, stabilization 2, and reconstruction 2.

Weak-country, major-country, war, relief, Evolution, and barrage modifiers are clamped to four rescue and three stabilization or reconstruction slots.

The donor cap is one active outbound burden because the timed donor idea clears `natural_disaster_outbound_relief_active` on removal.

The recipient cap is one inbound relief flow through `natural_disaster_inbound_relief_active`.

## Cost, requirement, and AI notes

Warning, rescue, stabilization, reconstruction, and chain-prevention actions use physical costs including manpower, support equipment, trucks, trains or convoys, fuel, stability, and war support rather than flat political-power exchanges.

The rail actions deliberately require trains because their descriptions specify road or rail clearance and rail restoration.

Inbound relief stores a state-derived rail or convoy route before the recipient accepts its route cost, so the displayed and charged transport are deterministic.

All 29 custom cost text identifiers in `common/decisions/013_natural_disasters_decisions.txt` have both base and `_blocked` localisation keys.

All 131 decision and mission definitions have title and description localisation keys.

The four outbound donor decisions reject self-targets, non-existent targets, active war targets, targets without a live aftermath card, and a second inbound relief flow.

Their AI weights respond to faction or relationship qualification, capital, population, transport, industry, coast, government, and war where appropriate.

The selector patch makes the final selected card obey the same port, engineer, and medical conditions as the target listing.

## Cleanup and exploit-risk notes

The recovery missions cancel on a missing slot state, closed card, or phase change and call the capacity refill path.

Foreign-relief completion, cancellation, and timeout clear route flags, donor and state variables, variant flags, and the active inbound marker.

The donor's timed burden removes the outbound-active flag, preventing permanent lockout and repeated simultaneous relief grants.

The general `natural_disaster_chain_mission` definition is currently dormant: a repository-wide text search found no `activate_mission = natural_disaster_chain_mission` call, although cleanup retains a defensive removal for it.

This is low severity because it cannot appear or grant rewards in current gameplay.

Keep it only if a future generic chain needs an objective; otherwise remove the unused mission, its localisation, and the defensive removal together in a separately reviewed cleanup.

## Validation

- Compared all four outbound donor call sites against the selector's variant gates; each now has an exact compatible-state eligibility predicate.
- Confirmed the selector's other call sites use variant zero and are unaffected.
- Confirmed 22 category picture references resolve to sprite definitions and existing texture files.
- Confirmed all 131 decision and mission names and descriptions, plus all 29 custom cost and blocked-cost keys, exist in Event 013 English localisation.
- Reviewed the dynamic capacity helper, typed mission activation, inbound-relief cleanup, and donor-idea removal lifecycle against the Event 013 specification and vanilla decision/mission patterns.

No live-game validation was run, in accordance with repository policy.

## Remaining issues and simplifications

No implementation fallback or design simplification was introduced.

The dormant `natural_disaster_chain_mission` is the only remaining low-severity cleanup observation in this scope.

No broad design handoff is needed.
