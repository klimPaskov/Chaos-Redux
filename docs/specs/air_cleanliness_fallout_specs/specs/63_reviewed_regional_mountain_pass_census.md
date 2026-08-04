# Spec 63: The Mountain Pass Census

## Scope

The Mountain Pass Census is a dormant Fallout-owned Middle East and North Africa chain about a highland refuge that must decide who can claim shelter, return home, serve the garrison, or keep the pass open. It is an ordinary Fallout country event chain. It is not the Fallout blackout and it is not an ordinary super-event.

The chain uses events `chaosx.fallout.635` through `.641` under `add_namespace = chaosx.fallout`. Candidate `635` uses transaction `710062`, route `7162`, and Event Log history `9168`.

## Admission and target

The country must have a current Fallout identity, durable survival resources, the exact `fallout_region.middle_east_north_africa` region, campaign day `300` through `2599`, enough Food, Clean Water, Fuel, Medicine, Shelter Capacity, Recognition, and Cohesion for at least one branch, and no committed or closed census memory.

The candidate producer chooses the lowest owned and controlled state that passes the current Fallout state identity and durable resource rows, has a produced Air Winter snapshot from the current generation, retains surviving population, and exposes the current Air Winter `mountain_highland` presentation receipt. The state must carry shelter capacity, Refugee Pressure, Supply Access, Reclamation, Exposure, and Disease Pressure within the reviewed bands. It must have a non-damaged native infrastructure level. Rural, pastoral, town, and large-town pretransition categories are accepted because a mountain pass may serve a village, camp, or refuge town.

The chain records a pass census from the existing highland presentation and state ledgers. It does not claim that the engine exposes a generic mountain-pass building, route, or topology. Specific historic pass names require a later country-memory receipt.

## Four branches

1. Local citizenship registers residents and refugees together. It spends Food, Shelter Capacity, and Recognition and raises census trust while lowering disease and refugee pressure.
2. Return plan issues escorted travel permits. It spends Food, Fuel, and Recognition and lowers refugee pressure while increasing exposure if the pass is closed too quickly.
3. Military colony places the pass under a permanent garrison. It spends Fuel, support equipment, and Command Power and raises military control while reducing Cohesion and increasing war support.
4. Open-pass community keeps the road available to displaced families and trade caravans. It spends Food, Clean Water, and Medicine and raises local authority while increasing disease risk unless the clinic ledger is strong.

Human and hidden-AI lanes use the same affordability, frozen ledgers, deterministic branch grading, delayed result, callback, Event Log payloads, and cleanup receipts. Unaffordable branches are unavailable and receive no hidden-AI weight.

## Numerical contract

The opening freezes country Food, Clean Water, Fuel, Medicine, Recognition, Cohesion, War Support, and the state Shelter Capacity, Supply Access, Reclamation, Exposure, Disease Pressure, Refugee Pressure, population, and infrastructure values. A branch cost is paid only after the exact ordinary receipt, current target, generation, and affordability checks pass. A rejected delayed result refunds a paid branch before commitment.

The result arrives exactly `35` days after the accepted branch. It resolves to success, partial, or failure from the frozen snapshot and branch ledgers. Result effects update Food, Clean Water, Fuel, Medicine, Recognition, Cohesion, Stability, War Support, Shelter Capacity, Supply Access, Reclamation, Exposure, Disease Pressure, Refugee Pressure, and native infrastructure when failure requires damage. Failure requests bounded civilian loss through the Deaths system with the Fallout aftermath cause.

The callback arrives exactly `210` days after result settlement. It regrades the frozen census against current highland shelter, supply, disease, refugee, and exposure values. It writes a branch-aware late memory, applies bounded resource and state changes, and can request a smaller Deaths-system loss on failure. Cleanup releases the result and callback rows exactly once, clears transaction-only state, preserves durable census ledgers, and blocks repeat admission for the same country and state memory.

## AI and cleanup

Continuity and Food Compact governments favor local citizenship when Medicine and Recognition are available. Bunker Authority, Quarantine State, Maritime Remnant, Scavenger Syndicate, Technate, and Machine Protocol favor Return Plan when shelter and infrastructure are repairable. Nomad Convoy and Religious Refuge governments favor Open-pass Community when Food, Clean Water, and refugee pressure support an open route. Warlord Command favors Military Colony during war or high War Support. Ties use a fixed branch order.

Generation change, owner change, control loss, stale target, duplicate ticket, or failed row authentication cancels only this census. A paid but uncommitted branch is refunded. A committed result is allowed to finish or is terminalized by its exact cleanup ticket. No global scheduler flag, on-action caller, recurring loop, new tag, focus tree, decision category, bilateral partner, or map rewrite is added.

## Text and asset contract

Player-facing text names the highland shelter register, mule tracks, pass clinics, winter permits, garrison stores, refugee families, and the first thaw road. It uses MENA regional and government-aware wording. The dedicated fictional report card is `GFX_report_event_fallout_mountain_pass_census`. It contains no readable text, real people, flags, or attested symbols and is not copied from Canal Schedule, Rail Spine Vote, Metro Republic Below, Tunnel Ward Committees, or zombie assets.

## Proof boundary

The tranche remains dormant and outside release-floor credit until scheduler activation and delayed-delivery receipts are approved. Static proof must cover the native infrastructure read and damage effect, the Air Winter highland receipt, Deaths-system request, exact `35` and `210` day offsets, branch affordability recheck, hidden-AI parity, Event Log history `9168`, dedicated asset hashes, and generation-safe cleanup. Candidate `FALLOUT-635` is an internal identity with no workbook or catalog row. The exact sweep, blackout, normal-map cold route, wasteland conversion, successor allocation, and universal focus package belong to the completed core.
