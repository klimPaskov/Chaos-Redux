# Worked campaign cases

These examples use fictional country and state labels.
They illustrate the specified rules without claiming that a particular historical map or installed engine fixture has been tested.

## A country fighting elsewhere

Country A is in a normal war against Country X.
A also shares valid land frontiers with B and C and is not in a normal war with either of them.
The allocator examines A–B and A–C normally.
Each pair can receive its baseline border battle if its selected state endpoints remain valid and free.
The war against X does not remove A from Event 078.

A must now manage its existing war and two local disputes with real military commitments.
The event does not end the war against X, give A replacement troops, or create a faction war against B and C.
If A later declares a normal war against B through some other system, only the A–B border dispute becomes invalid on that basis.
The A–C dispute continues.

## Several neighbors competing for a state

A small state owned by A borders both B and C.
The baseline allocator considers the two pairs in synchronized shuffled order.
The first admitted dispute reserves its target and staging endpoint.
If the second pair has another valid state-front candidate, it can still fight on that candidate.
If it has none, the pair has become unavailable for this wave and receives no illegal duplicate state assignment.

This is a genuine state-compatibility conflict.
It does not justify limiting A to one battle everywhere.
A can still fight on any other disjoint frontier.
The next Event 078 firing recalculates the map and may allocate the previously unavailable pair.

## Long border with increasing Chaos

A pair has ten independent valid fronts after the reservation-aware allocation set is constructed.
At baseline, it receives one root.
With Multiple Frontiers applied, its total opening allowance is three roots.
With Multiple Frontiers and Borders in Motion applied, its allowance is ten roots, subject to the final live validity of each start.

If two of the first three roots finish, the wave has still consumed three roots.
They do not generate two replacements merely because fewer battles are active.
If Borders in Motion later applies while that wave remains live, it can admit up to seven additional roots, further limited by current shared occupancy and valid endpoints.
The evolution does not replay the three earlier opportunities.

The allocator gives other pairs their baseline opportunity before filling these extra roots.
A long frontier cannot consume every available state of a small neighbor before that neighbor's other baseline relationship is considered.
Actual state collisions can still make complete coverage impossible, and the reason must remain visible in validation evidence.

## One captured state opens the next

A owns staging state A0.
B owns a line of states B1, B2, B3, and B4.
A0 borders B1, B1 borders B2, B2 borders B3, and B3 borders B4.
There are no other connections from A into B2, B3, or B4.
The root targets B1.

A wins the native battle and receives B1.
B2 becomes adjacent to A because B1 has changed hands, so B2 is a valid continuation target if its other conditions are satisfied.
When the root's seed opportunity succeeds, the next native battle uses B1 as the staging state and B2 as its single target.
An attacking victory there opens B3 under the same rule.
The already seeded chain does not make another continuation-probability roll after each win.

If B defeats the attack on B3, B retains B3 and the chain ends.
A keeps B1 and B2 under ordinary ownership rules.
B does not receive B2 automatically for defending B3.
A later independent Event 078 wave may put B2 at stake in a new root if the current frontier permits it.

## A tempting state that was already adjacent

Use the previous example, but A0 also borders B3 before B1 is captured.
B3 cannot be selected as the immediate continuation after taking B2, because it already bordered A before that step.
The chain must find a genuinely newly opened valid state from the latest capture.
It cannot jump sideways to B3 simply because B3 is valuable or poorly defended.
If no target meets the newly opened adjacency rule, the chain ends.

## A later wave arrives before the old one ends

Wave A has an unresolved A–B border battle.
Wave B fires before that battle ends.
A baseline Wave B cannot create another unresolved A–B dispute, but it can create valid disputes on A's other eligible frontiers.
An evolved Wave B can add a distinct A–B root only within its current allowance and shared occupancy limits.

When Wave A's native result arrives, it resolves Wave A's recorded target.
It cannot use Wave B's newest opponent pointer, state selection, or evolution profile.
Its capture and achievement evidence belong to Wave A.
Wave B's history and repeat accounting remain unchanged by that old result.

## Successful containment after a long advance

An advancing chain has captured five states and has already produced a qualifying sustained-advance Chaos occurrence.
The defender wins the next battle and retains its target.
The chain stops through military defeat, so the defender can begin the containment hold.

After 30 days of continuous ownership and control of that defended state, check whether the original opponent still has any advancing Event 078 chain against the defender.
If none remain and the stopped chain's wave has at least 5 of its own prior Chaos grant available, the wave pays its single −5 containment reduction.
The first five lost states are not returned by this result.
Recovering them is a separate, difficult achievement route through later genuine Event 078 captures.

## A high-value or final state

A state does not become immune merely because it contains a capital or most of a small country's industry.
Such a target is eligible only when the installed native mechanic can start and resolve it correctly with the declared participants and single-state settlement.
A last-state case needs explicit proof of callback delivery, country disappearance, ownership transfer, history, and cleanup.
If the engine cannot handle that case, the invalid target is excluded with a documented native reason.
Do not silently generalize that exception into immunity for all small countries.
