# Decision and Mission Implementation Prompt: Event 15 Utopia Manifesto

Implement the decision, mission, and scripted GUI systems mapped in the Event 15 source specs. Read `AGENTS.md`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-focus-trees`, `chaos-redux-frame-animation`, and the relevant offline wiki and vanilla documentation before editing.

## Required systems

Implement:

- Commonwealth Ledger decision category
- scripted GUI overview and tabs
- national survey
- common stores and reserves
- callings and labor methods
- property transition
- Garden City districts
- island project variants
- Doctrine of Necessary Ground selected-target system
- stewardship and integration
- league and reserve compact
- defense and auxiliary contracts
- route governance actions
- formation proof and decision

## Commonwealth Ledger values

Use four visible values:

- Need
- Plenty
- Concord
- Choice versus Assignment

Each value needs:

- centralized tuning
- readable public bands
- a dynamic breakdown
- event, focus, decision, war, territory, and AI inputs
- route-specific thresholds
- cleanup

Do not create a fifth contradiction value. Express broken promises through the four values, case integrity, conduct flags, local support, and events.

## Scripted GUI requirements

The GUI should show:

- value totals and trends
- route
- active crises
- calling shortages
- reserve band
- district project
- selected foreign target
- active Need case
- associate status

Tabs:

- overview
- Callings
- Stores and Settlements
- Necessary Ground and Associates

Every button needs:

- cost
- requirement
- blocked text
- effect
- tooltip
- AI equivalent
- cleanup

Use the animated sprites and static fallbacks from the asset package only after they exist and are wired.

## Selected-target pattern

Use a safe selected-target flow for foreign cases.

- one selected country or state context at a time for the human player
- selector and close actions
- stored selected target ID or approved event target
- target validity trigger
- only selected-target decisions visible to human
- AI evaluates all valid targets independently
- cleanup on annexation, death, route closure, war end, or invalid geography

Do not dump all potential foreign targets into the main category.

## Costs

Use varied and dynamic costs.

Possible resources:

- civilian factory burden
- military factory opportunity cost
- manpower
- infantry equipment
- support equipment
- trucks
- trains
- convoys
- fuel
- army experience
- command power within conservative limits
- stability
- war support
- reserves
- local support
- Concord
- time and active mission capacity

Political power can support a cost when the action is bureaucratic. It must not be the default main cost.

## Mission design

Implement the mapped mission families with meaningful duration, success, partial success, failure, and cleanup.

Priority missions:

- Count Houses and Hands
- Establish Capital Store
- Fill Seasonal Reserve
- Two Years Against Hunger
- Fill the Unpopular Calling
- Survey District Site
- Complete District Charter
- Secure Island Site
- Make an Island
- Wait for the Answer
- Emergency Provision
- Restore the Route
- Hold the Charter Period
- Prove the League Is Not a Mask
- Prove the Commonwealth

Use dynamic duration factors from country size, infrastructure, war, Plenty, Concord, route, transport, local support, and prior failure.

## Need cases

A Need case must include:

- a real deficit
- target relevance
- domestic alternatives
- case type
- integrity
- peaceful offer ladder
- cooldown
- expiration
- renunciation

Peaceful ladder:

1. domestic substitution
2. purchase or supply contract
3. lease or access
4. migration or settlement treaty
5. joint administration or associate charter
6. ultimatum
7. war

Routes determine when steps can be skipped. Claims should expire or create cost when Need is solved.

## Stewardship and integration

Implement:

- emergency provision
- transport restoration
- local charter
- route-specific administration
- status review or vote
- long integration
- autonomy, association, return, revolt, or core outcome

Do not grant instant cores for large or contested territory. Assigned Colony must create real resistance, Concord, condemnation, supply, and deaths-system costs where applicable.

## AI

AI must use every important system.

- prioritize severe shortages
- avoid unaffordable projects
- keep reserves before aid
- choose route-compatible calling methods
- use peaceful case steps on voluntary routes
- avoid stronger targets without reason
- close obsolete cases
- provision controlled territory
- form a league only with credible partners
- prevent auxiliary and unit loops

## Focus integration

Every decision family must be unlocked, upgraded, replaced, or closed by focus progress.

- early focuses open basic actions
- middle focuses add targets and methods
- late focuses enable league, associates, and formation
- route switches remove obsolete decisions
- post-formation decisions remain active

## Localisation

Write final in-world localisation from the source-spec direction.

- icon-first costs
- short requirement summaries
- custom tooltips for named regions and dynamic targets
- no raw trigger walls
- integer formatting for integer values
- no hidden route spoilers
- no achievement advertising in ordinary text

## Exploit checks

Prevent:

- artificial Need through one-day trade changes
- repeated reserve release and refill rewards
- assignment toggling for value farming
- district cancellation after partial reward
- invalid target or war-goal spam
- repeated status votes
- associate core farming
- infinite militia or auxiliaries
- route-switch reward collection
- formation reset of penalties

## Required handoff

After implementation, report:

- files changed
- decision and category IDs
- mission IDs
- scripted GUI entry points
- helper names
- constants
- selected-target lifecycle
- AI call sites
- localisation keys
- asset sprite references
- task-specific validation
- unresolved blockers

Then run `chaosx_decision_mission_auditor` and resolve every broad gap through the main agent or an accepted plan.
