# 02. The Event 001 connection and major-event selection

## Two owners of one crisis

Event 001 owns organizing, popularity pressure, local state control, human rebel countries, early containment, rituals, and whispers. Event 091 owns the return of Lenin, the single worldwide opening, the World Revolution country, its supernatural host, alignment choices, Influence, transformations, focus content, expansion, Red World, and defeat.

The user explicitly accepted the new 091 shared handoff on 10 October 2026, choosing "Use the new 091 package and align Event 001 (Recommended)". Inherited-first proportional nominations, rebel political choice and continuing targeted 001 cells are accepted and queued for gameplay implementation. The [aligned 001 integration section](../../001_communism_spread_specs/001_communism_spread_spec.md#world-revolution-state-integration) carries this same contract. The [current integration reconciliation](../implementation_handoffs/integration_contracts.md#current-checkout-reconciliation-2026-10-09) preserves the former wording as historical evidence and distinguishes accepted design from the legacy runtime.

The handoff is an adoption of existing history. It is not a reset of Event 001 followed by a replacement uprising. Event 001 remains the local cell provider after the opening, through an explicit adapter that knows whether it is operating in an ordinary defender, an independent refuser, an allied local base, or territory administered directly by the World Revolution.

| Connected stage | Owner and availability | New experience | Persistent result |
| --- | --- | --- | --- |
| I. Unstable Revolutionary Activity | 001, Gathering Storm and at least one active communist-controlled state | Rare human breakaways, railway seizures, armed strikes, local councils, and mutinies | Real rebel entities and local control history |
| II. Dark Worker Rituals | 001, Rising Chaos and at least one Level 2 stronghold | Missing organizers, industrial rituals, altered shifts, tools used in unexplained attacks, uncertain physical evidence | Prepared sites, ritual history, and local pressure |
| III. Whispers of the World Revolution | 001, Chaos Tier and at least one Level 3 lockdown | The same voice in different languages, impossible coordination, portraits changing, third-eye marks, silent workers without a heartbeat | Permanent whisper-unlocked history and normal Major-pool eligibility once all current gates hold |
| IV. The Great Revolution | 091 selected as a separate Major event | Lenin, a public nonhuman army, simultaneous territorial shock, and global war | 091 fire-once history, its actual country actor, and the opening super-event |

These are thematic stages, not four technology unlocks. Apotheosis, later powers, army specialization, transformed leaders, and commands are baseline 091 progression. The event log records the first three as 001 evolutions, then records 091 as its own Major event. It does not add a duplicate fourth 001 evolution row.

## Active spread and historical unlock are different facts

The pinned planning repository exposed the global marker `communism_spread`, the unlock marker `communism_spread_world_revolution_unlocked`, and the historical evolution marker `communism_global_evolution_world_revolution_whispers`. The pinned cleanup could clear these and reset 091 weight. Current source must be inspected before deciding which repairs remain necessary. The rework must separate the enduring fact that Whispers happened from the current fact that a qualifying insurgency remains active.

Containment can therefore make 091 temporarily ineligible without undoing the player's campaign history or deleting accumulated weight. If the actual 001 spread system is fully contained, the active marker becomes false. The historical unlock stays true. Renewed eligible 001 activity can reactivate the present-state gate without replaying the original evolution or awarding its history twice.

New 001 rebel creation must preserve its host pointer, episode identity, exact state list, pre-transfer state level, ritual and whisper evidence, real unit identities, and stock receipts before any old clear helper runs. Existing campaigns can contain rebels whose exact former level was already erased by older scripts. Those rebels retain their observed territory, units, leaders, and stocks. The migration records an unknown legacy level and uses conservative quality for any additional muster. It never invents a Level 3 history or destroys an army to make the record easier to reconstruct.

## Weight and selection

Actual entry into Evolution 3 unlocks the historical prerequisite, through either active-event progression or a pre-fire evolved opening. The evolved opening establishes the entry receipt. Baseline Event 001 firing and the Chaos threshold alone grant no unlock. This agrees with [the current 001 Major-event hook](../../001_communism_spread_specs/001_communism_spread_spec.md#world-revolution-major-event-hook). Every actual later whisper incident adds exactly 200 to stored 091 Major weight. The usual Major-weight gains from the central event system continue. A report that uses the same eerie imagery is not automatically a weight-bearing whisper.

The pinned 001 source called the whisper-weight helper from the evolution activation as well as later incidents. The rework must distinguish those cases. The design follows the user's sequence: milestone unlock first, designated later whisper receipts grant the additional 200. If retained initial weight is needed for ordinary Major competition, it belongs to the normal event-weight policy, not an undocumented extra whisper award.

The pinned existing dedicated later-whisper entries are `chaosx.nr1.16`, `chaosx.nr1.30`, `chaosx.nr1.31` and `chaosx.nr1.32`. All four award the required addition once per distinct later occurrence. Their current helper uses a twenty-five weight for each. Part 8 preserves that explicit pool, distinguishes the broader incident directions, and requires any added later whisper to enter the same receipt-bearing registry. The implementation must not drop an existing later whisper from the award merely because its presentation is rewritten.

Every special addition has an incident receipt. Reopening a report, changing controller, loading a save, completing an unrelated focus, or replaying a helper cannot award it twice. Whispers never directly fire 091. They make selection more likely within the full eligible Major pool.

The selector revalidates all of the following together immediately before reserving the event:

| Gate | Required interpretation |
| --- | --- |
| Historical prerequisite | Evolution 3 has actually entered at least once, active or pre-fire, with its historical receipt |
| Chaos | Event level 5, meaning the first Total Chaos tier at 800 or above in the current six-tier numeric model |
| Average communist support | Strictly greater than 5 percent, using the ordinary-country denominator defined below |
| Active crisis | The actual 001 active spread marker is currently valid |
| Origin | A valid physical origin and a viable country setup can be reserved |
| Lifetime | 091 has never fired in this campaign and is not already reserved or committing |
| Terminal state | No incompatible terminal world state blocks the ordinary event system |
| Shared settings | The event and its normal automatic-selection path are enabled under the shared settings contract |

The term Chaos level 5 is a catalog level, not a raw `chaos_tier = 5` equality. The installed scripts must be inspected for their zero-based tier convention. The threshold requirement is Total Chaos beginning at 800. Red World's separate condition is Chaos strictly above 1000.

When any gate fails, the visible weight is N/A. The stored number remains intact. Selection probability must be evaluated against the entire eligible Major pool during implementation. A ratio computed from 091 alone is not a meaningful probability claim.

## Average world communism

Use the arithmetic mean of current communist popularity across existing ordinary countries that own or control at least one eligible inhabited state. Every qualifying country contributes once. Special Chaos actors, dormant tags, dead governments with no territorial participation, and duplicated owner/controller entries do not enlarge the denominator. A government in exile with no current eligible ownership or control does not create an extra weight in this mean.

This is an explicit design choice for the previously unspecified word average. It treats the brief's world-state gate as a country-level political condition. It is independent of the population-weighted inhabited-world rule measure used by Red World. The implementation should name both quantities clearly and must not substitute one for the other.

At exactly 5 percent, selection fails. At a representable value above 5 percent, it can pass if the other gates hold. A highly communist world still cannot bypass the Chaos gate. A high Chaos world still cannot bypass active spread or the historical unlock.

## Incident families before the opening

| Incident | What the player observes | Mechanical consequence and restraint |
| --- | --- | --- |
| Synchronized stoppage | Rail and factory crews stop at the same minute in distant states | Bounded sabotage or an existing 001 escalation opportunity, with one incident cooldown |
| The altered portrait | A familiar wall portrait is found with a physical-looking third eye | A whisper receipt only when this is a designated later whisper, with no free territorial spawn |
| Missing organizers | The surviving cell insists that absent colleagues still attend meetings | A finite organizer investigation and a local cell change, with missing people not automatically counted as dead |
| The common voice | Workers answer in different languages with the same cadence and content | Cross-border preparation links and intelligence evidence, without revealing a guaranteed origin |
| Tools against armed men | A strike becomes an attack with unnaturally effective tools | A real local violent outcome, with the actual casualties sent once to the shared Deaths owner |
| The impossible night shift | A mill reports production despite an empty floor and locked entrances | A temporary industrial anomaly and later preparation evidence, not indefinite free factories |
| No heartbeat | A wounded worker is alive and responsive without normal physiology | A narrow precursor to nonhuman revelation, with confirmed conversion reserved for its actual outcome |

Each family supports multiple grounded state contexts such as a mine, mill, depot, shipyard, factory quarter, or agricultural supply district. Reports stay occasional. The 001 owner keeps the progression and incident cooldowns, and the 091 planner does not introduce a second periodic world scan to produce more flavor.

## The handoff moment

Reservation freezes the ordinary-country snapshot, inherited state and rebel inventory, support values, actor candidates, selections, and random outcomes. The next steps validate every required origin and country operation before the destructive part begins. Only actual successful firing records the immutable firing date and month. A failed preflight ends that selection attempt without consuming the fire-once event or deleting its stored weight, while retaining the proposal's selections and draws until a relevant input change permits a new review.

After the opening commits, later cell operations remain targeted. Neither a new focus nor a higher Momentum stage repeats the worldwide proportional allocation. New countries formed afterward receive role and diplomacy handling through bounded creation and transfer callbacks. They do not retroactively join a second opening lottery.

### Source basis

The user brief controls the three 001 evolutions, the separate 091 Major event, retained weight, the 200-point additions, active spread, and strict support gate. The pinned repository's 001 overview, effects, triggers, and central logic provide the existing identifiers and destructive cleanup findings. Exact migration responsibilities appear in the technical handoffs.
