# Event 54: Connections and Scientific Research Cluster

## Connection rule

Event 54 is the public random-discovery gateway for technologies that another Chaos Redux owner chooses to share.

A connection exists only when the owning event or system registers an individual technology. A thematic relationship is not enough.

The connection gives Event 54 permission to grant a technology. It does not give Event 54 ownership over the technology's event, project, decisions, characters, countries, facilities, equipment packages, or later consequences.

## Brilliant Scientist

Event 16 is the main early connection.

Kruger-owned technologies remain excluded by default. Event 16 may register individual technologies that can function in a country where Kruger, his laboratory, the Directorate, and the D'Rhondan systems have not appeared.

A Kruger technology granted through Event 54 must not:

- hire or create Kruger
- build his laboratory
- mark Event 16 fired
- advance a Kruger evolution
- create the Directorate
- create or advance D'Rhondan content
- consume a normal Kruger reward
- set a world-threat source merely because the technology exists

Event 16 should still fire normally later. Its route should recognize that the country already knows the granted technology and replace any duplicate reward with the owner-defined normal alternative.

## Alien Technology in Antarctica

Event 25 may register selected advanced technologies when they can exist outside the expedition and wreck race.

A grant through Event 54 does not:

- discover the Antarctic wreck
- enter a country into the expedition race
- complete an expedition stage
- consume the wreck reward
- identify the technology as coming from Antarctica in player-facing text
- prevent the normal Event 25 reward

The owner should avoid registering technologies whose entire meaning is possession of the wreck or completion of a unique expedition.

## Chemical and biological systems

Chemical and biological technologies require careful owner review because they can depend on equipment, payloads, facilities, doctrines, protection, evidence, contamination, and command structures.

A technology may enter the registered pool only when possession alone is safe and useful. The grant must not fabricate stockpiles, facilities, delivery systems, payloads, readiness, doctrine mastery, or active programs unless the technology's approved grant package requires a narrow compatibility marker.

The later production or use of an unconventional capability follows the normal CBRN consequence pipeline.

Institutional doctrine and project technologies should remain excluded when a direct grant would bypass their purpose.

## Unusual weapons and experimental technologies

Future events can register individual unusual technologies under the same rules.

The owner must decide whether the technology is:

- safe as a direct jump
- safe only after prerequisites
- safe as a bounded grant package
- safe with an owner callback
- permanently excluded

A future event specification that adds a technology should explicitly consider Event 54 registration. Silence means exclusion.

## Doctrine Research

Event 27 remains the owner of sudden doctrine progress.

Doctrine technologies do not enter Event 54's ordinary pool. This prevents conflicting doctrine branches and preserves a clear difference between the two events.

Event 27 belongs to both Scientific Research and Military Preparation at Medium severity. Its many-to-many membership must remain visible in cluster data and event details.

## Research Failure

A country with reduced research slots can still receive Event 54 grants.
The gift changes completed knowledge rather than rebuilding its institutions.
Event 60 keeps the slot loss, Scientific Capacity, Archive Recovery, reconstruction route, and independent incident cleanup.

After an authorized Event 54 grant commits, Event 60 can observe its existing recipient receipt and mark recovered only outstanding loss-ledger entries for technology identities actually delivered, including any approved required package nodes.
It recalculates only the matching legacy-family pressure and clears that pressure only when no related loss remains.
An unrelated grant supplies no restoration, and a second receipt check cannot recover or reward the same entry again.
Event 60 records direct-gift provenance for its independent-rediscovery achievement disqualifiers.
No research slots, Capacity, Archive Recovery, or new Chaos receipt accompany this matching reconciliation.

Two design choices remain unresolved before the combined behavior is implemented.

First, [Event 54's ordinary policy](054_gift_from_scientists_spec_part_1_core.md#baseline-firing) and [equal-weight policy](054_gift_from_scientists_spec_part_6_ai_multiplayer_and_balance.md#randomness-policy) keep the full safe missing pool random, while [Event 60's Gift proposal](../../060_research_failure_specs/specs/060_research_failure_spec_part_4_evolutions_connections.md#connection-gift-from-scientists) prefers a compatible lost technology.
The parent must accept either unchanged equal random selection or a defined lost-ledger priority exception.
Until that choice is accepted, the observer does not retarget Event 54, redraw a poor result, add a grant, or force-fire either event.

Second, this package proposes protection of completed gifts, while Event 60's safe regression can remove ordinary researched nodes in later incidents.
The parent must decide whether provenance protection applies and whether it is limited to a shared cluster transaction or persists into later Event 60 incidents.
The original alternatives remain recorded in [Part 4](054_gift_from_scientists_spec_part_4_evolutions_and_chaos.md#irreversibility) and Event 60's technology-regression design.

For a shared Scientific Research firing, the framework must also settle member order consistently with those choices.
Event 60's proposal fixes rollback before positive grants; Event 54 permits established member order and evaluates technology state at its own transaction start.
An actual committed gift can match a loss already recorded at that point, but the observer never manufactures a pre-existing loss or silently schedules a second gift to compensate for reversed order.
After both effects, completed grant and loss receipts must explain the resulting technology state and the research-capacity penalty remains active.

Human and AI recipients use the same accepted selection rule and exact-match reconciliation.
If Event 60 is absent, disabled, or has no matching active loss ledger, Event 54 resolves normally without a reconstruction reward.

## Video Game in Sweden

Event 24 connects through the Scientific Research cluster. Its simulation and doctrine content does not enter the technology registry.

Its military simulation and training effects remain owned by Event 24. Event 54 does not copy its national spirit or tactical benefits into the technology pool unless Event 24 later adds an actual technology and explicitly registers it.

## Scientific Research cluster identity

Scientific Research represents a broad research wave in which useful breakthroughs, military theory, singular scientists, simulations, and institutional failures can appear together.

The originating catalog export contained an unfinished placeholder row.
The distinct Scientific Research proposal uses reserved `event_cluster_id = 21`, shared with Event 089 in the [central identifier registry](../../shared_identifier_registry.md).
The old provisional ID `9` is superseded because it belongs to National Breakthroughs.
This allocation does not accept the proposed cluster behavior or membership and does not change runtime content.

The cluster should be a Minor Repeatable cluster with a 200+ Chaos unlock. Its repeated identity fits Doctrine Research, Gift from Scientists, and Research Failure, while later campaigns retain different combinations after the Fire-Once members leave the pool.

## Accepted membership

| Event | Cluster severity | Membership note |
| --- | --- | --- |
| Event 16: Brilliant Scientist | Severe | Rare high-impact member with unique event ownership |
| Event 24: Video Game in Sweden | High | Fire-once military research and training member |
| Event 27: Doctrine Research | Medium | Repeatable member that also belongs to Military Preparation at Medium severity |
| Event 54: Gift from Scientists | Medium | Global random technology member |
| Event 60: Research Failure | High | Repeatable institutional setback member |

Member severity describes the danger or campaign impact of the member inside the cluster. It does not replace the member's own event type or Chaos level.

## Cluster firing behavior

The event selected by the normal random picker is the anchor member and fires when its own eligibility passes.

Other cluster members are optional. Their participation checks use their own availability, fire-once history, repeatable state, country targets, minimum tier, and enable state.

Scientific Research should not require one permanent member to be available. A late campaign can still fire the cluster after Brilliant Scientist and Video Game in Sweden have left the normal pool.

The cluster counts as one global pacing event. Every participating event still applies its own effects, history, repeatable cap change, fire-once removal, evolution handling, and event details.

## Participation targets

The first probability pass should tune the cluster toward these outcomes:

- a normal cluster firing usually contains two or three members
- Gift from Scientists is one of the more common optional members
- Brilliant Scientist remains the rarest optional member
- Research Failure is common enough to give the cluster mixed outcomes but does not appear in most firings
- Video Game in Sweden appears often enough to matter before its Fire-Once removal
- Doctrine Research remains a meaningful repeatable member without crowding out the other repeatable events
- no optional member starves because a high-weight member always fills the combination
- the cluster still has valid combinations after every fire-once member has fired

Exact weights should be chosen only after the full candidate pool and cluster framework are inspected through the probability tools.

## Cluster co-occurrence rules

Gift from Scientists can participate with any other accepted member.

When Gift from Scientists and Doctrine Research appear together, doctrine gains remain Event 27's responsibility and Event 54 uses its non-doctrine pool.

When Gift from Scientists and Research Failure appear together, research-capacity damage remains independent; technology results follow the explicitly accepted selection, order, and protection rules above.

When Gift from Scientists and Brilliant Scientist appear together, a technology granted through Event 54 cannot count as a Kruger reward or alter which country receives the scientist.

When Gift from Scientists and Video Game in Sweden appear together, Sweden's event remains country-specific while Event 54 remains global.

## Cluster sequencing invariant

The cluster framework may use its established member order, but it must preserve these results:

- Event 54 grants are based on the recipient's technology state at its own transaction start
- a same-cluster doctrine reward cannot enter Event 54's pool
- a same-cluster custom owner event cannot mark an Event 54 grant as its normal reward
- the parent records the accepted Event 60/Event 54 order and grant-protection boundary before their combined technology result is claimed
- any actual compatible grant can reconcile only its exact outstanding loss-ledger identities once
- no observer adds, retargets, redraws, or force-fires an Event 54 grant
- Event 54 cannot restore research slots, Scientific Capacity, or Archive Recovery lost through Research Failure
- member report events do not create extra pacing transactions

## Cluster presentation direction

Cluster details should present a world in which research institutions become unstable in opposite ways. Some countries obtain whole fields of knowledge. Others reorganize doctrine, elevate unusual researchers, turn simulation into policy, or lose research capacity.

The text should avoid treating every member as a positive breakthrough. Research Failure gives the cluster a credible destructive side.

The member list should show each event's accepted severity and current availability. Event 27 should show its Scientific Research membership without hiding its separate Military Preparation membership.

## Catalog alignment

The Scientific Research cluster row and the five event rows must be updated together after implementation wording exists.

The workbook should preserve many-to-many membership. A single event-level Cluster ID cell must not erase Event 27's Military Preparation membership.

The export-only CSV files should be regenerated from the authoritative workbook and never edited directly.
