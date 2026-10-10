# Event 037: Mysterious People

## Part 1: Core event design

Status markers: **Pending** means design that is not in source yet, **Legacy** means current source that this design retires, and **Proposed** means a change that waits for acceptance.
The mechanics in this package are implemented (2026-10-10); `docs/events/037_mysterious_people/overview.md` is the implementation record.

## Catalog identity

| Field | Value |
| --- | --- |
| Event ID | `37` |
| Event name | Mysterious People |
| Event type | Minor Repeatable |
| Chaos level | `1` |
| Cluster | Sudden Abundance (catalog cluster `15`), Medium member |
| Catalog status | To Be Reworked |

The authoritative workbook row and the cluster rules are in [the catalog handoff](../handoffs/037_mysterious_people_catalog_and_cluster_alignment.md).

## Legacy runtime

**Legacy.** `events/037_mysterious_population.txt` holds a two-event stub.
`chaosx.nr37.1` is hidden and sends `chaosx.nr37.2` to one random country, which gains `2,500,000` recruitable manpower and triggers `chaosx.news.42`.
The stub's text calls the newcomers "green", offers to enslave them, and the news title asks whether they are aliens.

This design retires the whole stub.
Recruitable manpower given to one country, the enslavement option, and the alien headline all contradict the premise below and the mystery firewall.
The implementation keeps the existing file stem `037_mysterious_population` for the event file, localisation file, and picture folder, and rewrites their contents.

## Playable promise

Mysterious People is a global demographic anomaly.
Each firing adds real civilian population to every inhabited state in the world.
The newcomers arrive with homes, possessions, family ties, local speech, and enough apparent history to enter ordinary life.

The first manifestation feels useful and unsettling.
Factories find workers, farms gain families, and recruitment grows as the newcomers settle.

Repeated manifestations change the meaning of the event.
Each wave arrives before the last one has found homes and work, so unsettled newcomers pile up.
Countries that build housing and roads turn the anomaly into lasting strength.
Countries that ignore it slide into overcrowding, then hunger and flight through the existing Famine and Migration systems.
At the highest evolution, governments under severe pressure start asking who the newcomers really are, and some of them start registering people by origin.

The event never establishes where the newcomers came from.

## The core loop

1. A manifestation adds people to every valid state.
2. Each state's new arrivals start as **unsettled newcomers**.
3. Every state settles a share of its unsettled newcomers each month, at a rate set by its size, infrastructure, condition, and the country's choices.
4. Unsettled newcomers relative to population produce **Overpopulation Pressure**.
5. Low pressure lets settled newcomers strengthen the country, and high pressure costs stability, feeds Famine, and pushes people into Migration.
6. The player lowers pressure by settling people faster: housing, roads and water, a registration drive, requisitioned property, and at the highest evolution new cities.

The player manages one national value, Overpopulation Pressure, and one count, the newcomers living in the country.
Part 2 owns the population ledger, Part 3 owns pressure and its consequences, and Part 4 owns the decisions.

## Global firing rule

Every firing runs one bounded world transaction from the hidden entry event.
It visits each state once, creates population in every valid state, updates the newcomer ledger, and records country and world counts.

The firing is global even when the report is shown through one player country.
It does not choose a recipient country, a major power, or a region.
It does not move population from anywhere.

This single pass at firing is the only world-wide iteration in the design.
Recurring work is bounded and described in [Part 2](037_mysterious_people_spec_part_2_population_and_ledger.md#runtime-cadence).

## Valid state definition

A state qualifies when all of these hold at the moment of firing:

- `humanitarian_state_is_valid = yes`, so its owner and controller run ordinary civilian systems and are not special Chaos countries
- its real population is at least the inhabited-state threshold, planned at `5,000`

The threshold keeps empty map fragments and wasteland remnants out while keeping small islands and rural states with a real community.
Implementation may move it after checking the installed state-population distribution.

A populated occupied state qualifies.
The population appears in the state itself and the owner's national pressure carries it (Part 3).
A state below the threshold is skipped for that firing and can qualify later.

Event 037 adds no tag list of its own.
The shared `uses_normal_civilian_systems` and `is_special_chaos_country` classifiers decide special and nonhuman countries.

## Firing sequence

1. Event 037 is selected through the normal Minor Repeatable pool, or once through a cluster when Sudden Abundance becomes live.
2. The transaction resolves the manifestation stage (baseline or the highest enabled evolution, Part 3).
3. For each valid state it reads pre-fire population, applies one grant, updates the state ledger, and adds to country and world counts.
4. It recomputes each affected country's hotspot list and pressure.
5. It checks the one-shot Chaos milestones below.
6. It records one Event 037 history entry with the applied totals.
7. It sends the manifestation report to human players.

The transaction finishes before any report reads totals, so every number shown comes from applied results.

## First manifestation

The first firing introduces the anomaly through the people and places that cannot be reconciled with memory.
A village stands where the county map shows open fields, and its fruit trees are mature.
Children walk to a school that the town does not remember building, and their teacher knows every family by name.
Neighbours are greeted at the market by people who remember attending their weddings.

The opening is curious and uneasy rather than panicked.
At baseline the newcomers settle quickly, and many governments treat the arrival as a windfall.

The first manifestation also fires the rewritten world news event `chaosx.news.42`, once per campaign.

## Mystery firewall

These explanations may appear as theories, accusations, propaganda, sermons, or scientific speculation, and none of them is confirmed:

- falsified records on an impossible scale
- a miracle or a judgement
- a census error that somehow produced living people
- a hidden migration operation
- shared memory failure
- a correction of history by an unknown force

The event never confirms that the newcomers are aliens, time travellers, clones, returned dead, people from another world, products of a government project, a known supernatural species, or linked by origin to another Chaos Redux event.

Other events may create suggestive coincidences, such as an Event 019 soldier recognizing a village name or an Event 030 traveller's records contradicting a family history.
These links deepen uncertainty and never solve Event 037.
The [research boundary](../research/037_mysterious_people_research_boundary.md) applies the same rule to research and art.

## Event-log role

The entry event is `chaosx.nr37.1`.
Each firing produces one Event 037 history entry, never one per state or country.
The entry's detail view shows the people created worldwide, the number of states affected, and the manifestation stage (Part 7).

Evolution milestones use the shared evolution log.
Pressure stages and state crises are runtime status and never become evolution entries.

## Cluster role

The workbook lists Event 037 as a Medium member of Sudden Abundance, catalog cluster `15`.
The cluster is registered in the runtime as cluster `15`, and Event 037 is its only runtime member until the other catalogue members register theirs.
One cluster activation calls Event 037 once and produces one world transaction, one history entry, one repeatable-weight update, and one set of milestone checks.

## Direct Chaos

Event 037 adds direct Chaos only at concrete demographic milestones, checked at the end of each firing.
Evolution activation adds no Chaos.

| Milestone | Direct Chaos | Repeat rule |
| --- | ---: | --- |
| First manifestation | `+2` | Once per campaign |
| Living newcomers first reach `5%` of world population | `+3` | Once per campaign |
| Living newcomers first reach `10%` of world population | `+5` | Once per campaign |
| Living newcomers first reach `25%` of world population | `+10` | Once per campaign |

Deaths from famine, flight, war, disasters, camps, and any other cause reach Chaos through the shared Deaths ledger of the owner that caused them.
Event 037 never adds a second Chaos source for them.

## Success and failure shape

A well-managed country gains a larger workforce, more recruits over time, and faster construction while pressure stays low.
A poorly managed country loses stability, sees Famine stages in its most crowded states, and watches people leave through Migration.
Mixed outcomes are normal: a country can prosper while one crowded region fails.

## Core acceptance statement

The event succeeds when every grant changes real state population exactly once, the newcomer ledger stays inside real population through every later loss and move, Famine and Migration keep their ownership, and the player manages the crisis through one readable pressure value and a short list of real actions.
