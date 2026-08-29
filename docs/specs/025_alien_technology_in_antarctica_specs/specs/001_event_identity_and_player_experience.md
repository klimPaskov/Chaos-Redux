# Event identity and player experience

## Event role

Alien Technology in Antarctica is a major event about logistics, uncertainty, scientific competition, covert pressure, and the cost of pursuing a prize that no country understands.

The event begins with a global discovery and becomes a medium-length international race. A participant commits real material, selects a route, builds an outpost, narrows the crash area, protects its expedition, reads rival behavior, and chooses when to risk a final recovery attempt. The winner gains a major custom technology. Losing countries can still earn useful fragment rewards when they made real progress.

The event should feel playable from the first month. The player should not wait through several passive reports before making a meaningful choice.

## Catalog identity

| Field | Specification |
| --- | --- |
| Event ID | `25` |
| Canonical entry event | `chaosx.nr25.1` |
| Event name | Alien Technology in Antarctica |
| Type | Major |
| Default event state before rework | Disabled and unavailable |
| Target state after implementation and audit | Enabled by default and listed as playable or needs testing according to project status policy |
| Minimum chaos level | Tier 1, Calm World |
| Evolutions | Five |
| Super-event | Opening discovery |
| Cluster | No active runtime membership |
| Event-log actor | None for the global opening history row |
| Winner actor | Stored separately for outcome reports and detail state |

## Why the event starts at Calm World

The baseline incident is strange but bounded. Governments can treat it as a remote scientific and strategic prize. The race has a clear ordinary ending, and no evolution is required for completion. Locking the event behind a high chaos tier would reduce replay value and make the five evolutions less meaningful.

The event still uses normal major-event weight accumulation. It never bypasses major-event selection through a cluster.

## Runtime cluster decision

The Scientific Research cluster is a useful catalog category for Event 016, Event 024, Event 027, and other future scientific incidents. Event 025 remains outside its active runtime membership.

A normal cluster member can be fired when another member is selected. Applying that behavior to Event 025 could allow a minor scientific event to launch a major event without the accumulated major weight and reset contract. The specification therefore leaves Event 025 standalone. A future cluster-framework change may add an affinity-only catalog relationship or an explicit major-member gate, but that future work must not alter the accepted Event 025 pacing.

## Opening presentation

The opening super-event occurs immediately when the major event fires.

The public information should establish these facts:

- an object entered the atmosphere over Antarctica
- several observation stations, ships, or listening posts detected related anomalies
- the impact area is broad and uncertain
- fragments or signals suggest material worth recovering
- governments are moving before the site can be confirmed

The public information should leave these points uncertain:

- whether the object was crewed
- whether it was alien, experimental, temporal, or something else
- whether it remains active
- whether any occupant survived
- which exact region contains the main wreck
- whether the first reports are reliable

The opening super-event is followed by an invitation event for each current human-controlled country and a hidden participant-selection pass for AI major countries.

## Human participation

Every valid human-controlled country receives an entry choice.

Human eligibility does not require major status, a coastline, a specific ideology, or a nearby Antarctic gateway. A landlocked or weak player may enter through a chartered route with higher cost, longer travel time, and more dependence on foreign staging.

A human country is blocked only when participation is impossible or incompatible with an active terminal state. Examples include a country that no longer exists, a country that is no longer human-controlled when invitations are resolved, or a country already under an incompatible global end-state. Insufficient resources may disable the commitment action, but they do not erase the invitation.

All human entrants are accepted. AI slots are reduced when many human countries enter. No human player is silently denied because an AI roster was filled first.

## AI participation

AI participation is restricted to valid major countries selected during event initialization.

The system creates a bounded roster drawn from valid AI majors. Selection considers:

- current major status
- available convoys and fuel
- civilian industrial capacity
- usable coastline or a plausible gateway agreement
- active wars and supply burden
- research position and technology need
- current Event 016 and Event 036 alien-technology ownership
- current stability and risk tolerance
- relations with likely rivals
- special exclusions

The normal target is enough AI expeditions to create competition without filling the board with weak or doomed participants. Human entrants count toward the active participant set.

The Kruger State may receive a narrow AI exception when it exists, is not in a terminal state, can support the expedition, and its Event 016 route makes scientific competition coherent. Other AI-controlled special chaos and actual nonhuman countries remain excluded unless a later accepted spec adds a dedicated route. This AI restriction does not remove the entry choice from a human-controlled country.

## Player opt-out

A human country may decline the race.

Declining does not hide the event. The country becomes an observer and receives major public reports, the winner announcement, and any global diplomatic consequences. It does not receive the Expedition Board or participant actions.

A player may not join after the entry window closes unless a participant withdraws during the first mobilization phase and the replacement route is still open. Late replacement is a rare explicit event, not a permanent join button.

## Expected campaign length

The race should usually last between 10 and 24 months after the entry window.

Fast, well-prepared expeditions with direct southern access can complete sooner. Distant, underfunded, sabotaged, or high-risk expeditions may take longer. The event should not commonly remain unresolved for several years without a clear reason.

The event uses phase gates and timed objectives so a stockpile-rich country cannot win through one instant purchase.

## Baseline completion promise

The baseline winner must complete all of these public steps:

1. enter the race
2. organize a staging route
3. establish a functioning Antarctic outpost
4. narrow the crash zone through survey work
5. reach final recovery readiness
6. complete the primary recovery operation before another participant

The first valid participant to complete the primary recovery operation secures the recovery core and becomes the winner.

Evolutions may change the route, add danger, scatter fragments, or extend the aftermath. They may not remove the possibility of a prepared expedition winning through the ordinary phases.

## Global and national consequences

The event affects more than the winner.

- participants consume material and tie up civilian capacity
- rival operations create opinion and tension effects
- expedition casualties can enter the shared Deaths ledger when actual deaths occur
- public clashes can affect world tension
- fragment recovery creates smaller research rewards
- the winner receives a custom technology and a visible alien-research aftermath
- Event 036 later reads the shared recovery ledger

The baseline event does not set the global world-threat state. The expedition is a dangerous competition, not an existential actor.

## Major-event reset behavior

Event 025 follows the ordinary major-event contract.

- it begins at zero weight
- minor pacing events add the current dynamic major gain
- it competes with other eligible major events
- firing resets major-event weights according to the shared system
- firing resets minor timer pressure according to the shared system
- its opening is recorded once in History
- its five evolution milestones are recorded separately

## Event completion states

| State | Meaning |
| --- | --- |
| Observer | Country declined or was not selected |
| Active participant | Country has an expedition in the race |
| Withdrawn | Country left before final recovery |
| Eliminated | Expedition became nonviable and failed cleanup gates |
| Fragment claimant | Country recovered material but did not win |
| Winner | Country secured the primary recovery core |
| Post-recovery holder | Country retains alien-derived material during aftermath |
| Contained | Holder limited further use under Evolution V |
| Destroyed | Holder destroyed recoverable material after learning the initial technology |
| Transferred | Holder gave control to another valid country or consortium |
| Concealed | Holder continues secret study with elevated accident risk |
| Integrated | Holder committed to continued alien-system use |

## Deliberate scope limits

Event 025 does not create a country, focus tree, custom unit, national leader, faction, or permanent Antarctic state ownership system.

The crash site is represented through the expedition board and event assets. A map entity would depend on a verified Antarctic province consumer and would duplicate future Event 036 spacecraft ownership. Event 036 should own any eventual reusable spacecraft model package. Event 025 may consume that model later only through a separately accepted shared-asset handoff.
