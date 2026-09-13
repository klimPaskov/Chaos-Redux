# Event 033 Acid Rain improvement-loop review

## Review scope

This review applies the project improvement-loop questions to the accepted planning package. It checks premise, player control, performance, probability, costs, edge cases, presentation, shared-system ownership, and completion proof.

## Finding 1, mortality could be mistaken for a manpower modifier

Problem:

The prototype applies `local_manpower` penalties and its localisation claims deaths, but it does not remove real civilian population. A future implementation could reproduce that mismatch by calculating casualties, changing a modifier, and updating counters without killing population in the affected state.

Revision:

Every positive mortality pulse is now an exact state-population transaction through `apply_exact_state_civilian_population_loss`. The helper's applied value must equal the observed state-population reduction and is the only value allowed in Deaths, Event 33 totals, reports, and achievements. `local_manpower`, recruitable-population penalties, generic manpower loss, unit attrition, and counter-only changes are explicitly rejected as substitutes. The event remains fictional and may be supernatural. Environmental research informs corrosion and runoff without limiting lethality.

Status:

Resolved in Parts 1, 2, 4, 9, 11, and 12, plus the population-loss contract matrix.

## Finding 2, the prototype runtime violates the performance contract

Problem:

The current implementation runs a daily country scan and then scans every owned state. It also rebuilds effects through broad continent loops.

Revision:

The new design builds eligibility once, tracks sparse front and country registries, uses three-day exposure pulses, six-day drift, seven-day contamination, and scheduled movement. Only the global phase intentionally processes all frozen eligible states.

Status:

Resolved in architecture. Implementation inspection remains mandatory.

## Finding 3, the first coverage model was too slow

Problem:

A 45 to 70 percent regional visit quota with 24 to 70 day dwell produced a one-front median above two years in the first abstract test.

Revision:

The accepted quota is 60 to 85 percent. The second visit must clear all untouched states in that region. Dwell is 18 to 50 days with bounded corrections.

Result:

In 10,000 abstract runs, the one-front median became 514 days, 95th percentile 581, and maximum observed 661. Two fronts produced median 315, and three fronts 248. No run retained untouched states after the safety limit.

Status:

Resolved for planning. Repeat against real map counts and scripted weights.

## Finding 4, complete coverage could still fail on islands

Problem:

A connected-neighbor drift can stall on detached islands or disconnected state groups.

Revision:

Each front can perform a bounded same-region atmospheric jump when connected growth stalls. The jump targets untouched states and does not count as cross-region movement.

Status:

Resolved in Part 3. Needs island map test.

## Finding 5, Air Contamination needed event-specific source accounting

Problem:

Using the existing natural aerosol source would hide the Event 33 lifetime total and make the 1500 bp cap difficult to verify.

Revision:

Add a dedicated Acid Rain source, track lifetime actual additions, and clamp against both lifetime remaining and the distance to 5000 bp before the central mutation. Increment lifetime only by the actual returned delta.

Result:

A 10,000-sequence randomized planning test produced no lifetime or ceiling violation.

Status:

Resolved in design. Shared ledger layout and source ID require implementation audit.

## Finding 6, the first interpretation of the cluster rows was wrong

Problem:

The repeated Event 13 entries looked like empty placeholders. The accepted Event 33 goal establishes five logical slots with distinct danger and tier behavior.

Revision:

Event 33 follows all five Event 13 rows as the sixth optional Severe member, and Event 51 follows as the seventh optional High member. Neither replaces an Event 13 slot.

Status:

Resolved in Part 7 and catalog alignment.

## Finding 7, a Major event inside a repeatable cluster could double pace the event system

Problem:

Using Event 33's normal Major dispatch inside the cluster could apply cluster pacing and Major pacing separately.

Revision:

A prepared queue computes an effective pacing type. A queue containing Event 33 commits Major pacing once, reserves Event 33, and suppresses a second Major reset when its member dispatch occurs.

Status:

Resolved at specification level. Cluster framework implementation is a critical test area.

## Finding 8, preparation risked becoming too many buttons and values

Problem:

Four components, four tiers, urgent actions, recovery, counters, and three fronts could create interface overload.

Revision:

The category shows four repeatable permanent project buttons, at most five urgent actions, and a compact recovery state view. World Coverage and Preparedness are the only active managed values. Casualties and contamination are read-only.

Status:

Resolved in Parts 1, 5, and 6.

## Finding 9, cost scaling could make poor large countries unable to participate

Problem:

Scaling only by population or state count punishes large weak countries beyond their industrial capacity.

Revision:

Geographic scale sets the desired band, then final cost is capped at no more than one band above industrial capacity. Fragile countries always retain a payable project and urgent route when stockpiles allow.

Result:

The abstract AI test produced median Preparedness from 13.75 to 25 after 30 days, 18.75 to 63.75 after 90 days, and a broader 18.75 to 100 after 180 days. This preserves real inequality without removing agency.

Status:

Resolved in design. Exact in-game stockpile tests remain.

## Finding 10, preparation should not change weather formation

Problem:

Letting shelters lower severe-cell probability would make civil defense alter atmospheric physics. Letting preparation raise probability would punish successful play.

Revision:

Severe-cell formation depends on Chaos, intensity, dwell, and cooldown. Preparation can modestly affect target weighting after a cell forms and strongly affects consequences.

Status:

Resolved in Part 7.

## Finding 11, deaths and contamination could add Chaos twice

Problem:

Event-specific milestone effects could duplicate the shared Deaths and Air Cleanliness Chaos conversions.

Revision:

Only discrete atmospheric outcomes receive direct Event 33 Chaos. Death totals and contamination deltas use their shared systems without a second event addition.

Status:

Resolved in Parts 1 and 11.

## Finding 12, global phase could become an endless whole-world penalty

Problem:

A dynamic duration without a guarantee can trap the campaign in permanent global exposure.

Revision:

The global phase has a 45-day minimum and an eight-check rising ladder whose final check is guaranteed. Environmental state can change early chances but not the guarantee.

Status:

Resolved in Parts 3 and 7.

## Finding 13, old-save migration could falsely count clouded continents as touched

Problem:

The prototype applied `acid_clouds_state` across a region but acute `acid_rain_state` to a small area. Counting all cloud states as touched would invent exposure.

Revision:

Only old acute rain states migrate as touched and active. Cloud states contribute visited-region evidence. Completed prototype saves remain completed without retroactive reactivation.

Status:

Resolved in Part 11.

## Finding 14, the audio candidate is not ready for implementation

Problem:

The candidate recording has verified public-domain markings, but no excerpt was auditioned in this planning pass.

Revision:

The package identifies it only as a candidate and requires audio specialist listening, timestamp selection, uniqueness review, conversion, and in-game volume testing.

Status:

Open implementation gate, not a design blocker.

## Finding 15, exact helper names and fixed shared layouts need live repository proof

Problem:

Air source IDs, Deaths cause rows, Humanitarian source records, achievement registration, and super-event IDs can have fixed arrays or layout limits.

Revision:

The specification defines required contracts and leaves final identifiers to collision and layout inspection. The coding prompt requires repository search and specialist audits before shared edits.

Status:

Open implementation gate.

## Final quality position

The design now has:

- a coherent fictional premise
- bounded regional runtime
- exact state coverage
- a softlock-resistant movement path
- exact state-population mortality with safety caps and one authoritative applied-loss ledger
- real resource commitments
- compact player choices
- distinct cumulative evolutions
- separate Air source accounting
- no duplicate Chaos ownership
- a guaranteed global endpoint
- old-save migration
- complete presentation, asset, achievement, AI, and validation handoffs

The remaining open items require engine access, live probability tools, GUI inspection, audio audition, asset generation, implementation, and playtesting. They do not require another conceptual rewrite unless those tests expose a failed engine assumption.
