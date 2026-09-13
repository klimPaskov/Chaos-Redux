# Event 037: Mysterious People

## Part 1: Core event design

## Catalog identity

| Field | Value |
| --- | --- |
| Event ID | `37` |
| Event name | Mysterious People |
| Event type | Minor Repeatable |
| Chaos level | `1` |
| Cluster | Various Anomalies |
| Member severity | Low |

## Playable promise

Mysterious People is a global demographic anomaly. Each firing adds real civilian population to every valid inhabited state in the world. The newcomers arrive with homes, possessions, memories, family ties, local-language knowledge, and enough apparent history to enter ordinary life with little immediate friction.

The first manifestation should feel useful and unsettling. Factories find workers. Farms gain families. Empty streets fill. Recruitment pools grow after integration. Tax bases expand. Local authorities discover complete household records for people whom nobody remembers meeting.

Repeated manifestations change the meaning of the event. Housing, services, food distribution, transport, and settlement capacity begin to fail under the growing population. Countries that invest early can turn the anomaly into sustained economic and military strength. Countries that ignore it face overcrowding, famine, displacement, unrest, and political collapse. At the highest evolution, governments under severe pressure may begin persecuting the population they once welcomed.

The event never establishes where the newcomers came from. Every explanation remains an interpretation, rumour, doctrine, accusation, or failed theory.

## Global firing rule

Every firing runs one bounded world transaction. It evaluates each state once, creates the appropriate population in every valid state, updates the Event 037 provenance ledger, records country and world totals, and registers states that need later pressure processing.

The firing is global even when the entry popup is shown through one player country. It does not choose one recipient country, one major power, or one region.

The event does not move population from another state. Every applied grant raises world population by the same amount.

## Valid state definition

A state qualifies when all of these conditions are true at the moment of firing:

- it has a valid state scope and a living civilian population
- its current real population meets the event's minimum inhabited-state threshold
- it is not a wasteland or another state type that cannot support ordinary civilian life
- it belongs to an ordinary human civilian society, or its current controller can safely receive ordinary civilian population
- it is not owned and controlled only by an actual nonhuman country
- it is not excluded by a stronger owner system because adding civilians would corrupt that system's population contract

A populated occupied state remains eligible. The population appears in the state itself. The controller handles immediate order, relief, and movement decisions while control lasts. The state ledger survives control and ownership changes.

A state below the inhabited-state threshold is skipped for that firing. It can qualify later if ordinary population rises above the threshold.

The recommended design threshold is `5,000` real inhabitants. This avoids adding settlements to empty map fragments while retaining small islands and rural states with a real community. Final implementation tuning may move the threshold if installed state data shows that `5,000` excludes meaningful inhabited states or includes invalid remnants.

## Firing sequence

The intended sequence is:

1. Event 037 is selected through the normal Minor Repeatable system.
2. The global transaction snapshots each qualifying state's pre-fire population.
3. Every qualifying state receives one stage-scaled population grant.
4. Each state's mysterious-population ledger increases by the amount actually created.
5. Country and world totals update from applied grants.
6. Newly relevant states and countries enter sparse Event 037 processing.
7. The global manifestation report appears to human players.
8. Human-controlled countries with meaningful local impact receive a concise national follow-up when needed.
9. Pressure, integration, Famine, Migration, and other consequences continue through their normal owners.
10. Repeatable weight and event-log handling follow the shared event system.

The transaction must finish before reports describe totals. Every number shown to the player should come from applied results, not a forecast.

## First manifestation

The first firing introduces the anomaly through observations that cannot be reconciled with memory:

- villages stand on land that local maps showed as open fields
- schools contain enrolled children with several years of records
- municipal rolls include households with paid taxes and old addresses
- families possess photographs of local weddings attended by people who deny being there
- roads connect new settlements to existing routes with weathering that suggests long use
- employers remember workers whose personnel files appeared that morning
- graves, family trees, property deeds, and medical histories reach backward beyond the event date

The event should present the scale clearly. The world has gained population. The records support the newcomers. The social fabric accommodates them with unusual ease. No authority can identify a departure point, transport route, migration wave, military operation, or administrative process that brought them into being.

The opening should avoid panic as the default. Baseline integration is smooth enough that many governments see the arrival as a demographic windfall.

## Baseline demographic gift

At baseline, each qualifying state receives a moderate population increase based mainly on its pre-fire population. Small states receive a bounded local addition. Large urban and industrial states can gain hundreds of thousands or more. The grant is real state population and enters all ordinary population systems.

Baseline effects should create visible benefits without granting free strategic infrastructure:

- the future workforce expands
- the future recruitable population expands as integration completes
- consumer demand and the tax base rise
- underused land and industry gain inhabitants
- countries with spare capacity can gain a temporary demographic-dividend effect
- populated frontier and rural states may become more viable

The new houses, villages, roads, and records are part of the anomaly's narrative reality. They do not automatically grant infrastructure levels, factories, supply hubs, railways, or building slots. Strategic capacity still requires state development and country investment.

## Integration at baseline

Newcomers arrive with the practical knowledge needed to function in their apparent home society. They speak relevant local languages, know local customs, recognize nearby institutions, and possess plausible qualifications. Their integration is not instant in every administrative sense, but it is unusually fast.

Baseline integration should normally produce:

- low resistance from the newcomers
- no automatic crime or insurgency wave
- no automatic ideological conversion
- no automatic epidemic
- no automatic foreign allegiance
- a short administrative delay before the full military benefit becomes available
- faster integration in stable, well-served states
- slower integration in occupied, damaged, starving, or heavily displaced states

The integration delay prevents an immediate manpower exploit and represents registration, age verification, medical processing, employment, and military administration. It must not turn the population grant into a fake manpower modifier. The people already exist in real state population while integration catches up.

## Repeated firings

Every firing uses current real state population as its starting point. Previous mysterious arrivals therefore contribute to the next grant. This makes the event compound naturally without a separate exponential multiplier.

Repeated manifestations add to the same per-state ledger. A state can contain several waves without a separate player-facing cohort list. Internal history may retain a compact firing reference for audits or flavour, but the public mechanic uses one living mysterious-population total.

The event remains repeatable under the shared diminishing-weight rules. Repeated firings become less common through the normal cap reduction. A short presentation cooldown may prevent flavour popup repetition without changing event selection eligibility.

## Player information

The player should be able to learn:

- how many mysterious people currently live in the country
- the current national Overpopulation Pressure stage
- which owned or controlled states have the most severe Event 037 pressure
- which public policy is active
- which responses can reduce support pressure
- when Famine, Migration, or atrocity systems have taken ownership of a consequence

The player should not receive a permanent component ledger for every hidden input. Housing, food projection, service capacity, infrastructure stress, integration, refugee burden, occupation damage, and mysterious share feed the public result through short causal tooltips and state status text.

## Mystery firewall

These explanations may appear as theories, accusations, propaganda, cult beliefs, intelligence hypotheses, or scientific speculation:

- falsified records on an impossible scale
- a religious miracle
- a census error that somehow created living people
- a hidden migration operation
- mass shared memory failure
- a demographic correction by an unknown force
- spontaneous settlement formation
- a reality or history anomaly described without a confirmed mechanism

The event must never confirm any of these identities:

- aliens
- time travellers
- clones
- returned dead
- people from an alternate universe
- a secret government population project
- a known supernatural species
- a shared origin with another Chaos Redux event

Later systems may create suggestive coincidences. A mysterious surname may match another anomaly. An officer from Event 019 may recognize a village name. A time-travel event may produce a contradictory theory. These links must deepen uncertainty and must never solve Event 037.

## Event-log role

The entry event uses the canonical `chaosx.nr37.1` identity during implementation.

Each normal firing produces one Event 037 history entry even though every valid state receives population. The history row should record the global incident once, with applied world population growth available in the detail view. It must not create one history row per state or one pacing event per country.

Evolution milestones use the shared evolution log. Ordinary pressure stages, local policy changes, and state crises are baseline runtime states and do not become evolution entries.

## Cluster role

Mysterious People remains a Low member of Various Anomalies. Its baseline is beneficial, its origin is unexplained, and its destructive potential arrives through later evolutions and poor management.

Cluster participation must preserve the event's one-firing global transaction. A cluster call cannot apply Event 037 once for every cluster actor or report. The cluster provides one Event 037 firing, one event-history entry, and one repeatable-weight transaction.

## Concrete Chaos contribution

Event 037 contributes modest direct Chaos only when the anomaly reaches concrete demographic milestones. Evolution eligibility and activation add no Chaos.

| Concrete outcome | Direct Chaos | Repeat rule |
| --- | ---: | --- |
| First confirmed global manifestation | `+2` | Once per campaign |
| Living mysterious population first reaches `1%` of world population | `+2` | Once per campaign |
| Living mysterious population first reaches `5%` of world population | `+3` | Once per campaign |
| Living mysterious population first reaches `10%` of world population | `+5` | Once per campaign |
| Living mysterious population first reaches `25%` of world population | `+10` | Once per campaign |
| One firing creates at least `5%` of pre-fire world population | `+5` | Once per campaign |

These gains represent a real global anomaly with lasting demographic consequences. Routine pressure, famine deaths, forced-displacement deaths, atrocities, wars, annexations, and other consequences use their existing shared Chaos sources. Event 037 must not duplicate them.

A managed world can earn a small, tightly guarded recovery milestone. After the world has crossed the `5%` mysterious-population threshold, a full year with no Event 037-linked Famine state, no Event 037 state at Emergency or Breakdown, and no ongoing Event 037 atrocity campaign may remove `2` Chaos. This recovery can occur once for each distinct global crisis cycle and requires a prior crisis threshold.

## Success and failure shape

A well-managed country can receive:

- a larger integrated workforce
- higher long-term recruitment potential
- stronger use of underpopulated states
- faster recovery from prior population loss
- a durable demographic advantage after repeated firings

A poorly managed country can suffer:

- urban and rural overcrowding
- service and transport failure
- Famine pressure
- internal and cross-border displacement
- political radicalization
- repression and atrocities
- shrinking real population after preventable deaths
- state collapse when demographic pressure combines with war or existing humanitarian crises

The event supports mixed outcomes. A country can prosper nationally while one damaged region fails. A state can absorb the newcomers after an early crisis. A regime can reduce pressure through forced movement while creating severe diplomatic and moral consequences.

## Core acceptance statement

The implemented event succeeds only when every applied grant changes real state population, every mysterious cohort remains traceable through the Event 037 ledger, ordinary population losses reconcile that ledger, Famine and Migration retain their existing ownership, systematic killing enters the existing atrocity pipeline, and the player can manage the crisis through one readable pressure system.
