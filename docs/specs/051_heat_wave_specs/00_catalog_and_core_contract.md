# Catalog and Core Contract

## Accepted catalog entry

| Field | Value |
| --- | --- |
| Event ID | `051` |
| Event name | Heat Wave |
| Event class | Minor Repeatable |
| Chaos level | `1` |
| Chaos tier name | Calm World |
| Cluster | Natural Disasters |
| Cluster severity | High |
| Design status | To Be Reworked |
| Entry namespace | `chaosx.nr51.1` |

## Source conflict ruling

The supplied exported event catalog contains an older row that labels Event 51 as Minor Fire-Once and gives only a one-sentence description. The attached rough brief defines a repeatable crisis with a complete cleanup gate and explicit inheritance of permanent damage between episodes. These concepts cannot coexist with Fire-Once classification.

The current design ruling is therefore:

- Event 51 is Minor Repeatable.
- Its weight and cap follow the shared repeatable-event system.
- It cannot be selected while one Heat Wave episode, its recovery phase, or its cleanup transaction is still active.
- A later firing creates a fresh episode generation and does not reactivate stale temporary state from the previous generation.
- Permanent consequences remain because they belong to the world, not because the old episode remains active.

The event catalog workbook is authoritative for implementation. The CSV exports are evidence snapshots and must not be edited directly.

## Playable promise

Heat Wave should feel like a world-spanning emergency that changes ordinary strategy for several months. The event is about choosing which systems continue to function when every system needs water, transport, labor, maintenance, and relief at the same time.

The crisis should force visible choices:

- cities or farms
- the front or the home front
- factory output or infrastructure preservation
- immediate rationing or reserve protection
- evacuation or shelter in place
- continued offensive operations or unit rotation
- emergency imports or convoy conservation
- temporary shutdowns or long-term damage

The event fails its design promise if it becomes a flat national modifier, a uniform global debuff, a row of political-power purchases, or a hidden monthly population drain.

## Event ownership

Event 51 owns:

- global Heat Wave episode lifecycle
- global Heat Wave Intensity
- state Heat Stress calculation and presentation
- heat-specific temporary state, country, and unit consequences
- heat mitigation choices
- heat-specific accumulated exposure
- heat-specific recovery and cleanup
- environmental degradation eligibility and its event ledger
- heat-specific report events and world reactions
- the decision category and event-owned missions
- evolution pacing and evolution behavior
- the Evolution III escalation super-event trigger request

Event 51 does not take ownership away from shared systems. The following boundaries are mandatory:

| Consequence | Owning system | Event 51 role |
| --- | --- | --- |
| Wildfire incident | Event 013 Natural Disasters | Submit a validated wildfire request after heat and drought conditions make one plausible |
| Wildfire smoke and ash | Air Cleanliness through Event 013 | Do not add a second heat-owned contamination amount |
| Civilian population loss | Shared population transaction and Deaths | Request exact heat loss and record it once under a heat reason |
| Military casualties | Shared military casualty and Deaths path | Submit or apply the supported heat-casualty transaction once |
| Famine stages and famine mortality | Famine | Publish heat pressure and submit proven incident requests |
| Displacement cohorts and movement | Migration | Submit proven heat-displacement requests and hazard projections |
| Event pacing | Shared event system | Fire as one Minor Repeatable event and respect normal pacing ownership |
| Cluster pacing | Shared cluster system | When fired as a cluster member, do not create a second pacing transaction |

## State and country eligibility

Normal civilian processing should use the shared country classifier `uses_normal_civilian_systems`. The full special-country and nonhuman classifiers stay hidden from generated tooltips.

A state is valid for ordinary Heat Stress when it has a valid map identity and belongs to or is controlled by a country that can use the relevant civilian, military, or economic systems. State selection should fail closed when owner, controller, population, target proof, or ledger generation is incomplete.

An excluded country may still occupy or fight in a hot state. Its military units can receive engine-supported environmental penalties if the unit system applies them generically. It should not receive ordinary civilian water queues, cooling centers, food-rationing reports, or migration decisions when its owning classifier says those systems make no sense.

## Evolution identity

Event 51 contains one evolution track with three sequential stages:

| Stage | Name | Minimum Chaos | Main change |
| --- | --- | --- | --- |
| I | The Killing Heat | `200+` | Systematic recurring civilian and military mortality becomes possible |
| II | The Drying Earth | `600+` | Sustained exposure can create permanent environmental degradation |
| III | The Scorched World | `1000+` | Large areas can become close to uninhabitable and rare wasteland conversion becomes possible |

Evolution activation changes behavior but adds no Chaos by itself. Concrete outcomes caused by evolved behavior may add Chaos through one-shot milestones or through the shared Deaths and Air Cleanliness sources.

## Completion definition

The rework is not complete until all of these are aligned:

- event registration and repeatable classification
- entry and follow-up event chain
- lifecycle and cleanup
- global and state calculations
- state and country effects
- military effects
- decisions and missions
- AI use and AI refusal logic
- evolution pacing and logs
- Deaths integration
- Famine integration
- Migration integration
- Event 013 wildfire integration
- Air Cleanliness non-duplication
- event logs and Event Details
- Natural Disasters cluster membership
- presentation and localisation
- required static and animated assets
- Evolution III super-event package
- achievements
- event documentation
- authoritative catalog workbook and regenerated CSVs
- task-specific validation evidence

No smaller visible subset should be called the Event 51 rework.
