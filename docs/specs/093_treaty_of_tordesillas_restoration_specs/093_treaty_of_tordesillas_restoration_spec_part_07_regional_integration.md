# Treaty of Tordesillas Restoration: regional integration


## Integration as a campaign choice

At Evolution III each treaty power receives a regional route to integrate owned territory inside its assigned sphere.
The inspiration is Anarchist Spain's ability to turn conquered territory into cores, while the intended experience is substantially less repetitive: choose a coherent region, meet its conditions, fund one project, and integrate the eligible group together.

The purpose is not instant cultural transformation.
A core is the game's representation of a functioning political and administrative settlement.
Populations are not moved, erased, replaced, or counted as recruits simply because a project finishes.
Existing physical population and civilian loss systems remain authoritative.

Integration is available to both partners regardless of their government names.
The narration changes with their political character, but the substantive ownership and security requirements remain the same.
An ideological conversion does not grant a second set of free cores.

## Defining a region

Regions are generated from geography and the installed map's meaningful geographic groupings, then reviewed for coherence.
Prefer connected groups of approximately 5 to 12 states.
Small islands may form a compact maritime group when their actual sea adjacency and administrative connection justify it.
A long string of unrelated overseas islands is not one region merely because Portugal owns all of them.

A region never crosses the Spanish-Portuguese sphere boundary.
A larger geographic region that crosses the line is divided into sphere-specific portions.
The generator may split an excessively large or disconnected unit, but it must not produce a custom region for every player's current ownership pattern.

The project enrolls the currently eligible, connected portion of a registered region.
It must include either the whole region or a substantial coherent portion identified by the region definition.
The player cannot select one easy state in each continent and call the selection a region.
Isolated territories use a small-region route with the same consent and security rules.

Region boundaries stay stable during a campaign.
Capturing another state can make a new project possible, but does not retroactively add that state to a project which is about to finish.
This closes the last-day conquest shortcut.

## Admission conditions

The integrating country must legally own and currently control every enrolled state.
States already cored by that country are excluded before enrollment.
If another valid system cores an enrolled state before completion, it receives no duplicate Event 093 completion credit, and a project left with no non-core work closes without a project reward under the ordinary actual-paid cancellation accounting.
Military occupation, faction access, puppet ownership, a claim, and an ally's promise are insufficient.
The country must be the correct sphere partner, except for the recognized owner of Galicia under its special settlement.

The enrolled area must have a workable administrative and supply connection.
This may be a land route or a functioning overseas connection.
A recently encircled region cut off from all support should not finish a national integration project while its government cannot reach it.

Security conditions combine a minimum holding period, a per-state compliance floor, a per-state resistance ceiling, and the absence of an unresolved treaty ownership dispute.
Every enrolled state must pass them individually, so one uncontrolled or extremely resistant state cannot hide behind a calm neighbour.
Large regions require stronger preparation.
The thresholds and project lengths are centralized in Part 14.

## Two choices at confirmation

Each project makes two choices when it is confirmed: how the region is settled and how fast the administration works.
They are separate, so the player is never asked to compare four bundled packages.

**Settlement.**
A negotiated settlement works with local institutions and is the default.
It needs the tier's full compliance floor in every enrolled state.
A coercive settlement lowers that floor by 10 points and therefore lets a crown integrate a restless recent conquest sooner, but it adds the 60-day preparation period from Part 14 and submits one persecution displacement request for the enrolled states to the migration owner when the project starts.
The people who flee become Displacement Load in the receiving neighbours and use migration's ordinary reception and border decisions; Event 093 moves nobody itself and charges no deaths.
Targets of later subordination offers remember coercive settlements from the previous 365 days, as described in Part 13.

Negotiation is impossible, and only a coercive settlement remains, while the integrating crown is at Condemnation Tier 3 (Arms embargo) or higher, or while it runs an active camp in any enrolled state.
Local institutions do not sign accession papers with a government under arms embargo or beside a camp.
The camp and its discovery stay with the camp and condemnation owners.

**Pace.**
The ordinary pace uses the tier's base duration and cost.
The concentrated pace spends half again as much support equipment for a shorter project, as set in Part 14.
If a concentrated project pauses for any reason, it loses its speed advantage for the rest of the project and keeps none of the extra equipment.
Concentration is therefore a bet on holding a quiet region, not a universal best button.

Neither choice lowers the ownership, control, supply or resistance gates.
A coercive settlement is not a permanent 'remove resistance' purchase; resistance and compliance remain native values that the crown must actually manage.

## Hunger in an enrolled region

Famine owns food security in enrolled states.
A project pauses while any enrolled state is at famine or catastrophic famine Food Security, and resumes when the state recovers through the famine owner's ordinary relief, import and evacuation actions.
Taking Requisition Food from an enrolled state, or choosing Continue Requisitions there, turns a negotiated project into a coercive one at once, with the displacement request above and no extra preparation time.
The crown thus decides whether to feed a region it wants to keep or squeeze it and accept the flight that follows.

## Progress and disruption

A project advances while its legal basis, control, and essential supply conditions remain valid.
A temporary supply interruption pauses progress without resetting completed work.
Persistent loss of control or a treaty suspension freezes the project and states why.

A loss lasting 60 consecutive days cancels the affected enrollment unless the region can be reduced to a still coherent, originally enrolled group.
Reduction must never substitute new states or preserve the original full reward.
The result is a smaller declared project, with its cost and remaining time reviewed through the cancellation rules.

Changing state ownership to the other treaty partner ends the donor's project for those states.
The recipient does not inherit free completed progress without accepting a documented project handover and its remaining obligations.
A transfer cannot be used to multiply project slots or completion benefits.

Cancellation returns only the unspent refundable portion of the actual payment.
Administrative costs and equipment already committed to completed work are not magically recovered.
The proposed cancellation profile in Part 14 is a design target for an explicit receipt-based implementation, not an assumption that the engine offers atomic transactions.

## Completion

Completion rechecks every enrolled state.
Eligible states become cores of the integrating country in one regional settlement.
Ineligible states do not receive a core because their neighbors succeeded.
The result screen identifies the completed region and any states held out for a concrete reason.

A project is not allowed to complete as an empty shell.
If no enrolled states remain eligible, it resolves as cancelled or blocked, releases its slot, and grants no prestige, Confidence, achievement credit, or core-related reward.

Finished cores remain if the treaty is later suspended or dissolved.
They represent a completed settlement, not a temporary faction modifier.
Event 093 never removes another country's cores as a routine consequence of its own completion.
Other systems may independently change cores under their own rules.

The country does not receive a new permanent national spirit for every region.
Regional records and native cores carry the result.
Country-level administrative effects are consolidated within the spirit budget in Part 12.

## Galicia's special route

Galicia can be integrated by the country recognized in the opening settlement, even when the ordinary hemisphere rule would say otherwise.
This eligibility begins at Evolution III.
The baseline transfer itself remains non-core.

An honored peaceful settlement supports the easier small-region path once local conditions permit it.
A war settlement or a repudiated bargain repaired by force requires the longer recent-conquest preparation.
The original dispute therefore affects play long after the border changes.

Spain retaining Galicia does not need to re-core a state that is already its legitimate native core.
Such an existing core supplies no new Event 093 integration achievement credit.
Portugal cannot transfer Galicia away and buy it back to farm special-region completion.

## Why the system is faster without becoming empty

The main speed advantage is batch processing.
A single project can integrate a coherent group and completes automatically when its conditions are met.
The player does not visit every state, wait for separate cooldowns, or spend the same cost through dozens of identical decision rows.

The proposed durations are months rather than a multi-year wait for every province.
The final implementation must compare the actual installed Anarchist Spain route against this design on equivalent test conquests.
Until that benchmark exists, the numerical speed advantage is a target to validate, not a measured claim.

The remaining difficulty comes from choosing what to integrate, maintaining control, paying real costs, and helping the weaker treaty partner.
Large, hostile, and newly captured areas consume more time and resources than settled small possessions.
That distinction is central to the event's identity.
