# Asteroid Incoming, Part 2: Targeting and Trajectory

Status: implemented, except the suitability-weighted country draw marked as proposed.
Exact helper names and constants are in the [Event 028 overview](../../events/028_asteroid_incoming/overview.md).

## Chooser

The country whose event pool selects Event 028 becomes the chooser and stays the chooser until the outcome finishes, even if a human switches tag.
One global transaction blocks every other copy, so multiplayer never produces several boards or several impacts.
The history row names the chooser as the actor; the outcome separately records the chosen target.
At the lock the chooser is saved permanently (`asteroid_incoming_impact_chooser`), so Event Details can say who chose the trajectory after the transaction ends.

## Building the board

The board holds exactly three distinct country and state pairs: no country and no state appears twice.

### Valid target country

A country can take a slot only when all of the following hold:

- it exists, is not the chooser, is not an actually nonhuman country and is not the CXT test country;
- it owns and controls at least two usable states (`asteroid_incoming_runtime.target_country_minimum_usable_states`);
- at least one usable state is fully controlled, so a surviving government seat exists after the centre is destroyed.

Special Chaos countries that represent ordinary human societies stay eligible.
Relationships with the chooser do not filter the human board; enemies, allies, subjects and strangers all create part of the choice, and the AI handles protected relationships through its weights (Part 7).

### Valid impact state

A state can be a centre when it is land, passable, not wasteland, not an existing crater or fragment site, owned and controlled by the candidate, and has a meaningful settlement: a city category, any factory, dockyard, infrastructure, railway, supply node, air base, naval base or strategic value.
The candidate must keep another usable owned, controlled state.
A capital can be chosen.

### State suitability

Within each drawn country the board picks its best state by a point score in `asteroid_incoming_runtime` (`target_score_*`).
The score rewards capital status, victory points, population bands, industry, supply, railway, infrastructure, air and naval bases, direct land neighbours and states reachable within three rings, and penalizes frontline states and isolated states below the reachable-state threshold.
An island or empty appendage wins only when the country has nothing better.

### Country draw and diversity

The implemented board draws each country uniformly at random from the valid pool, then picks that country's best state.
The second draw prefers a country with a valid centre on a different continent from the first; the third draw is unrestricted.

**Proposed (2026-10-10 audit, not implemented): suitability-weighted draw.**
Because most countries are small, a uniform draw often produces three minor targets whose rings barely matter, which weakens the choice the brief asks for.
The draw should prefer countries whose best state reaches a preferred suitability score (a new `asteroid_incoming_runtime` threshold), falling back to the full valid pool when fewer than three such countries exist.
The board stays random and relation-blind; only the chance of a meaningful footprint rises.
This needs parent acceptance and a probability check of how often majors and minors appear.

## What the options show

Each strike option shows the target flag, state name, country name, continent and a capital marker.
The board description states that each strike erases its centre and damages three surrounding land rings, and adds the fragmentation or minerals warning when those evolutions are eligible.
The near-miss option says plainly that there will be no impact or dust.

Example of the implemented option text: "Strike [flag] Ile de France, France (Europe), current capital".
The near miss reads: "Choose the near miss: no impact or dust".

Options never show hidden scores, fragment locations, random rolls or AI logic.

## Board validity

The board's validity is stored once in the global flag `asteroid_incoming_board_ready`, which the description and every option read, so a popup restored from a save cannot describe one board and offer another.
The dispatcher sets it on success, the opening event re-validates once, the reopened board re-validates without rerolling, and every reset, lock, miss, fail-closed and cleanup path clears it.
Forced firing while a course is locked or after the passage explains that state and preserves the original opening date and outcome.

## Confirmation and lock

A strike option opens a confirmation that repeats the target and the global consequences.
Cancelling returns to the same board through `chaosx.nr28.8`, keeping the pairs, chooser, opening date and evolution snapshot.

Confirmation stores the locked country and state, the original state id, its capital status, the chooser, the lock day and the expected impact date (`lock_duration_days` after the lock).
The resolver is queued on both the chooser and the target with the same constant delay; whichever fires first resolves the impact and the other is a no-op.
If both callbacks are lost, a monthly watchdog finds the overdue lock and resolves it on the global host.
A board or confirmation whose chooser is annexed closes through the fail-closed outcome without picking a new chooser or coordinate.

### Target identity

Accepted decision F06 (basis: user-granted design authority, 2026-10-04 agent decisions): history, Event Details, news and the super-event name the target through the persistent country and state pointers saved at the lock.
No separate name or flag snapshot is stored, because no supported effect stores a name string; an annexed target still resolves to its former name and flag, while a cosmetic rename during the two days shows the new name.
Open question 6 in the README asks the parent to confirm this as final.

## Two-day lock

The locked state is a geographic coordinate.
Peace deals, annexation, civil war, state transfers and tag changes during the lock never move the impact.
The current owner and controller at impact receive the losses and reports for the territory they actually hold; the original target stays named as the intended target.

A course whose state became invalid through another permanent map transformation fails closed: a global bulletin reports that the trajectory broke apart (`chaosx.news.97`), with no dust, fragments, craters or deaths, and the impact is never redirected.

## Target preparedness

The locked target chooses one stance in `chaosx.nr28.3`, whose description says whether the locked state is its capital.
No stance saves the centre or changes the fixed ring population losses.

| Stance | Implemented effect |
| --- | --- |
| Preserve command continuity | A shorter, milder government dislocation after the impact |
| Disperse transport and reserves | At impact the target loses `transport_loss_per_state` of its trains, trucks and fuel for each main-footprint state it holds (capped at `transport_loss_cap`); this stance keeps `transport_dispersion_preserved_share` of that loss |
| Mobilize medical command | Shorter local damage in its states, fewer rescue-period deaths and a cheaper first mobile-hospital deployment |

The impact report lists destroyed and preserved transport only for the original target.
The target AI weighs capital status, stability, transport exposure and outer-ring population rather than ideology (Part 7).

## Capital relocation

When the locked centre is the current capital, the transaction moves the capital before destroying the state.
Backup selection prefers controlled cores and safer, populated, connected states outside the first ring, then surviving ring states when nothing safer exists.

Accepted decision F02 (basis: user-granted design authority): when no settled, fully controlled backup exists, relocation tries any controlled owned state, then any owned state even if occupied, then any controlled state.
If none qualifies, the impact still proceeds, the capital stays at the crater, the country takes the full government dislocation, Government Beyond the Crater stays closed, and the report and Event Details say the government could not move.

Relocation keeps the same government, leader, flag and focus tree.

## Ring construction

The footprint uses shortest land-state adjacency from the locked centre.

- Ring 0 is the centre.
- Ring 1 is every eligible land state directly adjacent to Ring 0.
- Ring 2 and Ring 3 continue outward, each excluding states already in an earlier ring.

A state reachable by several paths belongs to its smallest ring and is processed once.
Rings cross national borders; sea zones do not create links.
Impassable states can carry the ring outward but receive no population or building transaction when they hold nothing to damage.

## Fragment separation

Fragments use the same shortest-path rings, with two rings each.

- A fragment centre is never inside the main three-ring footprint or another fragment's first ring.
- The planner prefers one centre per country, several continents and a centre with at least one land neighbour, with a bounded fallback for genuinely isolated candidates.
- Overlapping fragment rings, and fragment rings overlapping main rings, apply only the strongest profile once.

The planner reduces the fragment count when the world cannot provide enough separated centres; it never forces an overlap or an invalid state.

## Unavailable board

With fewer than three valid pairs, Event Details shows `N/A` with the reason and automatic selection skips the event.
A forced firing in such a world shows the explicit `N/A` option instead of broken choices.
