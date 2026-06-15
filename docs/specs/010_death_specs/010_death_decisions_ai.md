# Event 010 Death - Decisions, Missions, Coalition, And AI Spec

## Decision Surface

Death uses normal decision categories first. Add a scripted GUI only if the implemented decision surface becomes too dense.

Categories:

| Category | Visibility |
| --- | --- |
| `death_missing_islands_category` | pre-reveal observers |
| `death_black_shore_category` | revealed threat, coastal/neighbor/frontline countries |
| `living_compact_category` | eligible compact leaders and members |
| `death_forbidden_files_category` | rare desperate/occult/high-chaos countries |
| `death_war_logistics_category` | countries at war with Death or compact members |

Do not show every decision to every country. Use visibility gates and state-targeted decisions.

## Missing Islands File

Visible before reveal only to countries with a plausible reason to notice:

- former owner
- current island owner
- nearby naval-base owner
- naval major
- country with intelligence agency
- country whose faction/subject owned the missing state
- player country if directly connected to the incident

| Decision | Cost direction | Duration | Effect |
| --- | --- | --- | --- |
| `send_lighthouse_tender` | convoys, small command power or navy XP | 30-45 days | Raises discovery chance and may reveal one consumed island to the country. |
| `compare_admiralty_charts` | political power, command power | 20-30 days | Raises `death_notice`; may identify a threatened sea region. |
| `bury_the_report` | grants short-term stability or avoids panic | instant/cooldown | Raises `death_silence` and worsens later reveal penalties. |
| `publish_the_empty_harbor_story` | stability or war support cost | instant/cooldown | Raises global notice and can unlock early compact preparation. |

Mission:

| Mission | Duration | Success | Failure |
| --- | --- | --- | --- |
| `restore_contact_with_missing_island` | 90 days | Owner places supplied division, patrol, or investigation marker before Death consumes the target. | Raises `death_silence` and may accelerate consumption. |

Early text must not name Death unless public reveal has occurred.

## Black Shore Containment

Visible after reveal to countries with threatened coasts, neighboring states, faction responsibilities, or compact membership.

State-targeted decisions:

| Decision | Target | Cost direction | Effect |
| --- | --- | --- | --- |
| `establish_black_cordon` | watched/withering coastal or adjacent state | infantry equipment, support equipment, command power | Adds defense score and slows withering if supplied units exist. |
| `evacuate_the_shore` | withering depth 1-3 | trains, convoys, trucks, stability | Saves part of population before consumption; creates refugee pressure. |
| `salt_the_railheads` | threatened rail/supply state | rail damage, support equipment, command power | Slows Death if state falls; harms friendly logistics. |
| `hold_the_lighthouses` | threatened sea-region coast | fuel, convoys, naval XP | Reduces coastal jump chance in sea region. |
| `burn_the_records` | desperate state | stability/legitimacy cost | Reduces Death yield if state is consumed; worsens recovery. |

Timed missions:

| Mission | Duration | Requirement | Result |
| --- | --- | --- | --- |
| `guard_the_cordon_line` | 120-180 days | supplied divisions in target states | success regresses or stalls withering; failure advances it |
| `keep_the_port_lit` | 90-120 days | port controlled, convoys/fuel available | locks state out of coastal jump pool for cooldown |
| `last_train_out` | 90 days | trains/trucks/convoys and no active combat | saves population; failure records civilian deaths and dread |

The player should see why a mission succeeds or fails through tooltips and event details.

## Living Compact

The Living Compact can be a crisis compact layered on top of existing factions, or a template-backed faction if implementation decides that is cleaner. The source behavior is the same either way.

Formation conditions:

- Death revealed.
- At least one mainland state consumed or consumed-population threshold reached.
- Candidate leader is not Death, not nonhuman, not capitulated, and not blocked by subject rules.
- Candidate leader is a major, faction leader, threatened regional country, or proven containment actor.
- Minimum threatened membership or major sponsor threshold is met.

Shared values:

- `living_compact_cohesion`
- `living_compact_command`
- `death_public_dread`

Shared decisions:

| Decision | Cost | Requirement | Result |
| --- | --- | --- | --- |
| `convene_black_shore_conference` | PP, command power, 30 days | reveal plus enough threat | starts compact formation |
| `pool_cordon_equipment` | member equipment contributions | compact exists | reduces containment costs for front members |
| `assign_coalition_fronts` | command power, army XP | members bordering Death | raises guard mission success chance |
| `standardize_evacuation_orders` | trains, convoys, PP | high dread | improves evacuation efficiency, costs stability |
| `declare_the_dead_coast` | leader action | high coastal threat | creates shared naval patrol mission |

Leadership transfer:

- if leader capitulates, is consumed, or leaves eligibility, transfer to highest-valid member
- if no valid member exists, compact enters emergency mode and shared decisions degrade

Failure states:

- low cohesion blocks joint actions
- high dread without cohesion creates panic events
- members under unrelated war pressure may contribute equipment instead of joining wars

## Forbidden Files

This route is not a power fantasy. It is a costly way to fight Death, delay it, or betray the living.

Unlock inputs:

- Death revealed
- high chaos
- severe casualties or territorial losses
- low stability
- occult/high-chaos flags from other systems
- extremist/desperate government
- compact failure or no viable coalition path

Decision family:

| Decision | Role |
| --- | --- |
| `listen_to_the_last_clerk` | Opens study route and raises temptation. |
| `open_the_black_register` | Uses forbidden knowledge to identify target states. |
| `petition_zol` | Starts betrayal/client route. |
| `offer_the_unburied` | Sacrificial containment; slows Death locally at a moral cost. |

Outcomes:

1. Study Death to fight it: stronger containment, internal dread, intelligence exposure.
2. Forbidden containment: sacrifices manpower, stability, war support, or state population; disqualifies clean achievements.
3. Join Death: terminal or challenge path. Country becomes a marked client, not a normal ally, and may still be consumed.

AI rules:

- AI should almost never petition Death.
- AI may study Death under severe threat if it lacks compact support.
- AI forbidden containment requires high threat, high chaos, low stability, and no better option.
- AI should not use this path if doing so would ruin a nearby human player's core defense without clear warning.

## Anti-Death War Logistics

Available to countries at war with Death or compact members.

| Decision | Cost direction | Effect |
| --- | --- | --- |
| `issue_white_map_orders` | command power, army XP | limited movement/attrition mitigation in Death states |
| `supply_the_living_columns` | trucks, trains, fuel, support equipment | lowers withering strength loss in selected front states |
| `mark_the_return_paths` | recon/engineers or army XP | lowers attrition and retreat risk |
| `silence_the_empty_broadcasts` | intel/agency, PP | reduces dread and local ghost spawn chance |
| `count_the_missing` | PP, command power | records casualties, improves cohesion, reveals consumed-population estimates |

Offensive missions:

| Mission | Trigger | Success |
| --- | --- | --- |
| `occupy_every_tile_in_death_state_group` | country/faction fighting Death | clears a target state group |
| `hold_the_black_capital` | origin occupied | if all footholds are cleared during timer, Death defeat fires |
| `clear_the_footholds` | world-end | continent-specific emergency progress and partial rewards |

## AI Weights

Use MTTH variables or scripted scoring helpers for decision weights.

Ordinary country AI:

- investigates early if naval, nearby, former owner, player ally, or intelligence-heavy
- does not bankrupt itself chasing rumors before reveal
- prioritizes cordon and evacuation for owned high-population coasts
- uses patrol decisions only with enough fuel/convoys/naval XP
- joins compact based on proximity, threat, ideology, faction obligations, and current war load
- contributes equipment if distant or already in a major war
- avoids forbidden route unless desperate

Compact leader AI:

- forms compact when Death is public and enough members are at risk
- funds shared equipment first
- assigns coalition fronts second
- supports frontline members before distant symbolic actions
- handles leadership transfer cleanly

Death AI:

- hidden stage: no normal wars, target low-population islands
- reveal stage: declare through scripted effects on valid neighbors
- containment stage: wither weak states and use bounded jumps
- world-end: aggressive plans and continent footholds

## Exploit Guards

Implementation must prevent:

- repeated evacuation of the same population
- cordon re-click loops without cooldown or cost
- equipment pool duplication when compact members join or leave
- player joining Death while keeping a normal industry/economy
- hidden consumption of major/player capitals before reveal
- forced compact leaving/joining breaking existing factions
- missions continuing on consumed or recovered states
- Death target arrays retaining invalid states

## Decision Audit Checklist

Before completion:

- every decision and mission has trigger tooltips and effect descriptions
- costs are dynamic and centralized
- AI weights are meaningful
- decision categories do not flood irrelevant countries
- compact and forbidden routes have clear disqualifiers and achievement effects
- state-targeted decisions clean themselves up on state consumption, liberation, defeat, and world-end
