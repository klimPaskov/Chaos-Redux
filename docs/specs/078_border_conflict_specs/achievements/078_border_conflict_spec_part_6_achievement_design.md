# Event 078 achievements

## Shared rules

These are three difficult, multi-condition achievements built around genuine territorial outcomes.
They use the existing Chaos Redux achievement system and remain subject to its ordinary campaign eligibility rules.
An achievement cannot be earned from a debug-forced result, duplicated callback, technical cancellation, or an ownership change made by another system.
Normal scripted Event 078 allocation is allowed.

A capture receipt records the wave, conflict, original opponent identity, target, winning country identity, and whether the capture belonged to the advancing chain.
The receipt is a gameplay evidence requirement, not a proposed native storage API.
Holding a state requires continuous ownership and control for the full stated duration.
Losing either condition invalidates that hold attempt.
A later reacquisition does not silently restart the same hold.

Display progress through the existing achievement surface and the informational category where useful.
Do not create a new event currency or national spirit for achievement progress.
The names below are internal design handles.
Final visible names and descriptions belong to the implementation writing pass.

## cr_078_many_fronts

### Purpose

Reward a country that manages several neighboring border crises in the same worldwide outbreak without giving up any of its own Event 078 stakes.
This requires both taking and holding territory and defending existing territory.

### Conditions

The country must win genuine Event 078 battles against at least five distinct neighboring country identities in one wave.
At least one of those victories must be an attacking capture and at least one must be a defensive retention.
Repeated victories against the same opponent count once toward the opponent condition.
The country must lose no state through an Event 078 settlement in that wave.
A cancelled dispute does not count as a win and does not repair a failed no-loss condition.

After the wave closes, the country must continuously own and control every state it captured in that wave for 30 days.
All five qualifying opponents must have been distinct current country identities when their victories occurred.
Their later annexation by an unrelated system does not erase a valid victory, but their identity cannot be recreated to multiply the count.

### Failure and restart

A state lost through an Event 078 settlement in the wave permanently disqualifies that wave for this achievement.
A captured state lost during the hold also disqualifies the attempt.
A later independent wave may qualify normally.
Do not merge opponents or captures from separate waves.

### Visual subject

Several border markers arranged around one intact central shield, readable as one simple symbol.
The subject should suggest attention to several directions without putting five tiny flags into a 64 by 64 icon.

## cr_078_unbroken_frontier

### Purpose

Reward a sustained advance whose gains remain useful after the immediate battles finish.
The target is one genuine chain, not a collection of isolated captures.

### Conditions

The country must make at least five valid captures in one Event 078 chain against the same original opponent identity.
The root's initial capture counts as the first capture.
Every later qualifying capture must follow the newly opened adjacency rule.
Captures from another root or another wave do not add to this chain's progress.

After the chain ends, the country must continuously own and control all states captured by that chain for 90 days.
The hold begins after the last battle and chain closure, not after the fifth capture while additional battles are still running.
A sixth or later capture extends the set that must be held.
A legitimate loss ending the advance does not itself invalidate the achievement if the country still meets the five-capture and hold requirements.

### Failure and restart

A cancellation caused by a broken conflict identity invalidates that chain's achievement evidence.
Ordinary exhaustion of the frontier is a valid chain conclusion.
A state lost during the hold invalidates that attempt.
A separate later chain can qualify.

### Visual subject

A single advancing boot and a continuous line of moved boundary stones.
Keep the line broad enough to read at native size and avoid miniature map labels.

## cr_078_recovered_frontier

### Purpose

Reward a country that first stops a serious territorial advance and later recovers the same lost frontier through the event's own border fighting.
The recovery may take several later firings.

### Conditions

An opposing Event 078 chain must have taken at least five states from the country.
The country must end that chain through a genuine defensive victory.
Capture the identities of the first five states lost to that chain and the original opposing country.
The country must subsequently recover each of those five states through valid attacking Event 078 victories against that same opposing country identity.
Normal-war conquest, a peace conference, annexation by another country, scripted grants, and diplomatic transfers do not satisfy the recovery condition.

After the fifth required state has been recovered, the country must continuously own and control all five for 90 days.
A required state already recovered earlier must still be held when the five-state hold begins.
The recovery does not require a single later wave or a single recovery chain.
It does require real Event 078 capture receipts for all five states.

### Attempt selection and failure

Track the earliest qualifying stopped chain that has not already failed and do not allow a player to switch between unfinished attempts.
Only one recovery attempt per country needs to be active at a time.
If the original opponent ceases to exist before all five qualifying recaptures have occurred, close the attempt as failed.
A recreated country using the same tag cannot complete it.
If all five qualifying recaptures already occurred, later disappearance of the opponent does not invalidate a hold that still satisfies its conditions.

A required state leaving the opponent before its qualifying recovery does not count as recovered.
The attempt may remain open while the original opponent still exists, because a later legitimate Event 078 recovery may again become possible.
The achievement interface must show that the exact historical states remain the objectives.
Loss of a required state during the final 90-day hold fails the attempt.
A later qualifying stopped chain can begin a new attempt.

### Visual subject

A boundary stone being returned to its original socket, with a broken forward arrow behind it.
Use one clear return motion and avoid small text or numbered stones.

## Fairness and farming boundaries

The event does not forbid legitimate campaigns merely because countries share an ideology or faction, unless the native mechanic makes that battle invalid.
Achievement eligibility still follows the shared system's established anti-debug and campaign rules.
Do not invent an untestable claim that the event can detect all cooperative multiplayer farming.
Record genuine participants and results so the shared achievement rules can operate on truthful evidence.

No achievement awards extra land, starts a border war, changes the event's repeat weight, or changes the battle result.
They recognize outcomes without steering the allocator toward easily farmed states.

## Asset and registry handoff

Each achievement uses the project's canonical 64 by 64 icon pipeline.
Prepare one subject source per achievement and derive its normal, grey, and unavailable states through the existing templates and processing script.
The runtime achievement definition belongs in the shared achievement registry with the existing root-level unique identifier structure.
The achievement image filenames and IDs must agree exactly with the registry.
Do not create a separate Event 078 achievement registry or hand-painted substitutes for the canonical state treatments.
