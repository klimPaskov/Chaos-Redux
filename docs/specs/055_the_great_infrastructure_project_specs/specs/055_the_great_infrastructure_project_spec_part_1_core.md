# Event 55 Specification, Part 1

## Core Event and Player Promise

## Catalog identity

- Event ID: `55`
- Event name: The Great Infrastructure Project
- Type: Minor Repeatable
- Status before implementation: To Be Reworked
- Chaos level: `1`
- Cluster: Positive Economy
- Cluster role: Medium member

## Event promise

A random ordinary country experiences an unmatched public works mobilization. Every state owned by that country at the moment of the event receives maximum constructed infrastructure. The country also establishes a permanent national project program that can plan and complete major railways, strategic highways, ports, resource corridors, international trade routes, bridges, and tunnels.

The immediate infrastructure grant is intentionally extreme. It is the event's clear positive shock and must remain visible on the map. Later play turns the gift into a long-term system with limited administrative capacity, substantial material demands, geographic restrictions, international negotiations, construction risks, and maintenance obligations.

The program should make geography matter. A continental power should receive different proposals from an island state. A resource-rich interior should see different projects from a compact trading country. A friendly regional bloc should be able to build a shared route that a diplomatically isolated state cannot sustain.

The category should create hard choices without becoming an inventory of small upgrades. A player should usually compare three meaningful proposals, commit to one or two major works, and then manage the consequences of that commitment over many months.

## Opening selection

Each firing selects one valid country from the world. The selected country can be controlled by a player or the AI.

A valid first-time recipient should normally meet all of these conditions:

- It uses ordinary civilian systems.
- It is not an actual nonhuman country.
- It is not a special system actor whose society cannot use ordinary national construction.
- It owns at least one valid state.
- It is not fully capitulated.
- It has a functioning government and normal access to state buildings.
- Its territory supports at least one useful project family after the opening grant.

A subject can qualify when it has enough autonomy, territory, and economic capacity to operate the program. A one-state country can qualify when it has a strong coastal, port, river, strait, or compact metropolitan project. It should not receive a false continental proposal.

The target selector should strongly prefer a country that has never received Event 55. A country with an existing program remains eligible for a later repeat firing, but the value of that repeat is different and smaller than the first manifestation.

Countries that have been selected recently should receive a long temporary exclusion from the target pool. This spreads the event across the world while preserving repeatability over a long campaign.

## The opening infrastructure grant

On a country's first Event 55 firing, every state owned by that country at that exact moment receives the maximum supported constructed level of infrastructure.

The grant follows these rules:

- It applies to owned states, including an owned state that is temporarily controlled by another country.
- It does not apply to states acquired later.
- It does not create a permanent rule that automatically maximizes future conquests.
- It raises the constructed building level to the current engine maximum.
- It does not erase active war damage for free. Damaged infrastructure can remain damaged and must repair through normal systems.
- It does not restore other buildings.
- It does not add railways, supply hubs, ports, resources, factories, radar, or fixed links by itself.
- It applies only once per recipient country.

This distinction matters because the later projects should still improve transport networks after every state has maximum infrastructure. Railways remain real railway projects. Ports remain real naval logistics projects. Highways use a route-specific strategic road network effect because ordinary state infrastructure is already at its maximum.

## The national works program

The selected country receives a persistent decision category for major infrastructure projects.

The category has five jobs:

1. Show the country's current ability to manage another major project.
2. Present a small set of geographically relevant proposals.
3. Show active construction missions and important project problems.
4. Let the country repair, renegotiate, reroute, suspend, or abandon damaged works.
5. Preserve completed projects as persistent map and national assets whose benefits depend on continued operation.

The category remains available after the opening project is completed. It should become quiet when no useful action exists, rather than showing obsolete or impossible decisions.

## Public mechanic value

The program uses one persistent public value with the working label `National Works Capacity`. This is a design label, not final localisation.

National Works Capacity represents the country's ability to survey routes, coordinate ministries, commit civilian industry, procure equipment, manage contractors, and supervise several large works at once. It is a readiness score, not a spendable currency.

The value should use a `0` to `100` range with four readable states:

| Range | Working status label | Meaning |
| --- | --- | --- |
| `0` to `24` | Overstretched | Existing work, war, or economic weakness prevents a new major commitment. |
| `25` to `49` | Limited | Small or moderate projects are possible. Large works need better conditions. |
| `50` to `74` | Ready | The country can begin a normal national megaproject. |
| `75` to `100` | Mobilized | Extreme or multinational works can be managed when their other requirements are met. |

The final interface should show the value through a compact visual meter or staged frame in the ordinary decision category header. The exact number can appear in the tooltip. The stage label should carry the main message.

Project progress does not become another persistent custom value. A construction mission shows its own progress and deadline through the normal mission interface. Route condition uses qualitative operational states instead of a second global meter.

## Capacity causes

National Works Capacity should be recalculated from real country conditions and the burden of active projects. It should respond to changes the player already understands.

Positive influences include:

- a strong civilian factory base
- adequate train and truck reserves
- adequate convoy capacity for maritime work
- high stability
- peace or secure home territory
- a history of completed projects
- an established engineering institution
- later event evolutions

Negative influences include:

- each active national project
- each international share the country has accepted
- war on home territory
- capitulation pressure
- severe shortages of trains, trucks, convoys, or fuel
- active embargo isolation
- suspended or failed projects
- repeated cost overruns

The internal calculation can use several hidden inputs. The player only needs the total, the current stage, the important contributors, and the next threshold that matters.

The category tooltip should list only contributors that materially change a current decision. It should not expose a full accounting ledger.

## Project slots

At baseline, a country can supervise one active major project.

A country with exceptional capacity can prepare another proposal while the first project is close to completion, but it cannot begin a second construction mission until a later evolution expands the program.

Project slots are derived from the event's current evolution and the country's National Works Capacity. They do not become a second custom resource.

Suggested limits:

| Event state | Normal active project limit |
| --- | --- |
| Baseline | `1` |
| Evolution I | `1`, or `2` for a country in the highest capacity stage |
| Evolution II | `2` |
| Evolution III | `2`, or `3` for a country in the highest capacity stage and with at least one completed project |

An international project counts against the host's limit and against each partner's accepted international commitment limit. A minor participant that contributes only transit access should not be treated as if it manages the entire project.

## Opening proposals

The first firing creates a proposal set after the infrastructure grant. The set normally contains three candidates from different project families.

A candidate is a real planned route or facility. It should identify its origin, destination, critical states, partner countries, main purpose, approximate duration, cost phases, and expected benefit before the player commits.

The first proposal set should favor projects that make the opening grant feel useful:

- a railway linking distant industrial and resource regions
- a highway connecting a capital, industrial belt, coast, or frontier
- a port or resource corridor when the country has a strong maritime or extraction need
- an international corridor when relations and geography already support it

Extreme bridges, tunnels, and continent-wide multinational systems remain locked behind their evolutions.

## First firing player choice

The opening event should have one main acceptance option. The extraordinary infrastructure build has already occurred, so the option confirms how the government will organize the permanent program rather than deciding whether the event exists.

The option tone should combine public confidence, bureaucratic ambition, and mild absurdity. It may draw on public works slogans, engineering pride, national modernization language, or a restrained joke about the map being covered in survey stakes. Final wording belongs to implementation.

The player should not choose between receiving and refusing the opening infrastructure. Refusal would undermine the event promise and create an obvious inferior option.

The country's first policy choice occurs inside the project category when it selects a proposal and construction method.

## Construction philosophy

Each project begins with one of three construction methods. These are working design roles, not final decision names.

### Accelerated schedule

The country accepts higher immediate industrial strain and a greater chance of cost overruns in exchange for faster completion.

This method suits wartime lifelines, urgent resource access, famine relief corridors, and an AI that faces a real supply emergency.

### Standard public works

The project follows the normal duration, cost, safety, and reward profile.

This is the default AI choice when no strong strategic pressure exists.

### Conservative engineering

The country spends longer on surveys, foundations, safety, and maintenance preparation. The project completes later but has a lower chance of disruption and a stronger long-term operational state.

This method suits fixed links, difficult terrain, high-value ports, and countries that can afford delay.

The method is selected once at project authorization. It should change risk, duration, and long-term maintenance. It should not create another public meter.

## Success states

Event 55 supports four broad project outcomes:

### Full completion

The project is commissioned at its planned scale. All permanent route, facility, partner, and integration effects become active.

### Reduced completion

The country finishes a shorter, cheaper, or technically simpler route after a major problem. The project remains useful, but its map scope and benefits are smaller.

### Suspended works

Construction stops with a visible incomplete project. The country can resume, redesign, transfer, or abandon it later.

### Abandonment

The project closes. Some unused equipment or committed capacity can be recovered, but sunk construction effort, diplomatic trust, and completed partial works remain lost or stranded.

Failure should usually create a recovery choice. A single bad incident should not erase years of play without warning.

## Persistent completed projects

A completed project remains a named event-owned object with:

- an owner or host
- a project family
- a route or facility footprint
- critical states or nodes
- partner countries when relevant
- an operational status
- a maintenance class
- a generation identity
- a completion date
- a record of major damage and repair

The project object is important because benefits must stop when the route is severed, a port is lost, or a multinational agreement collapses. A permanent modifier that survives every border change would not satisfy the event promise.

## Operational status

Completed projects use qualitative states:

| Status | Meaning |
| --- | --- |
| Operational | The full route or facility is controlled, connected, and politically usable. |
| Strained | The project still works but lacks equipment, fuel, convoys, maintenance, or partner support. |
| Partially disrupted | One segment or node is unavailable. Benefits are reduced to the remaining usable portion. |
| Severed | A critical segment, crossing, port, or agreement is lost. Most benefits are suspended. |
| Under repair | A repair mission is active. |
| Dormant | The project exists physically but has no current legal or diplomatic operating framework. |

The player sees the current status and its cause. Internal segment integrity can remain hidden.

## Event scope and scale

Event 55 should remain a major national program inside a Minor Repeatable event identity. It creates a long-lived system, but it does not become a separate world crisis.

The event should feel generous at first and demanding over time. It should reward a country that uses geography, supply, diplomacy, and economic timing well. It should punish careless overcommitment through delay, stranded works, and weak maintenance rather than through arbitrary destruction.

## Core non-negotiables

- Preserve the immediate maximum infrastructure grant to every state owned by the first-time recipient.
- Apply that grant once per recipient, not after every conquest or repeat firing.
- Use one persistent public mechanic value.
- Keep project progress in mission progress and route condition in qualitative states.
- Generate a small set of real geographic candidates.
- Require foreign consent for foreign territory.
- Let war, border changes, embargo, disasters, bombing, and sabotage disrupt projects.
- Allow repair, rerouting, reduced completion, suspension, and abandonment.
- Keep the ordinary decision category readable.
- Never offer a bridge, tunnel, or land connection that the map implementation cannot actually support.
