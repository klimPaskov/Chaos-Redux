# Decision and Mission Implementation Prompt for Event 22 Concentration Camps

## Task

Implement, audit, and validate the complete decision and mission layer for Event 22.

Use the event's existing shared camp, Deaths, evidence, Condemnation, chemical, disease, occupation, resistance, and country-package systems. Do not create a second camp framework. Do not implement the whole event solely inside decision effects.

## Required reading

Read before editing:

- repository `AGENTS.md`
- `.agents/skills/chaos-redux-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- offline Paradox wiki pages for decisions, missions, triggers, effects, modifiers, scopes, localisation, and data structures
- current vanilla decision and mission files with comparable state targeting and timed objectives
- Event 22 index and all five spec parts
- `022_concentration_camps_event_chain_map.md`
- `022_concentration_camps_decision_map.md`
- `022_concentration_camps_ai_probability_matrix.md`
- `022_concentration_camps_acceptance_criteria.md`
- current camp and genocide decisions
- current German, Japanese, and Soviet camp categories
- current public scripted effects, triggers, constants, Deaths reasons, and evidence helpers

Do not rely on remembered syntax.

## Category architecture

Working categories:

```text
chaosx_022_camp_network_management
chaosx_022_liberated_site_relief
```

The first category serves responsible, successor, and continuing operators. The second serves controllers that stop operation and manage liberated or abandoned sites.

Use ordinary decision-category presentation. The management category uses one static archival picture. Do not build a dedicated scripted GUI. Do not call `chaosx_event_ui_worker`.

The category header shows:

- current policy
- Network Reach band and percentage
- Exposure band
- Resistance Pressure band
- one current priority state or crisis

Shared Condemnation remains in the Chaos Meter and is not duplicated.

## Clutter budget

- three to five primary visible actions in normal phases
- six primary actions is the hard maximum
- one to three active missions
- actions are replaced by phase and policy
- completed rows disappear
- emergency state actions replace normal state management
- regional closure groups replace many individual state rows
- country-specific packages hide generic duplicates

Do not move an oversized list into more tabs or categories.

## Cost contract

Every action has at most four spendable cost types.

Use costs that fit the action:

- political or administrative capacity
- command power, never above the project cap
- manpower or unit commitment
- support equipment
- trucks
- trains
- convoys
- fuel
- civilian-factory burden
- stability or war support where the policy creates internal conflict

Requirements such as state control, rail access, valid target source, or active construction do not count as spendable costs.

Final cost localisation uses amount plus matching texticon. No literal resource labels or filler words.

Centralize base values and scaling in script constants. Dynamic factors include site count, state distance, network reach, site type, workforce, resistance, exposure, contamination, front distance, economy, and previous failure.

## Required policy paths

Implement:

- freeze intake and transparent closure
- restrictive review and inspection
- forced-labour administration
- security expansion
- Evolution I extermination policy
- concealment and evidence response
- retreat emergency
- successor disclosure or continuation
- liberation and relief

Every path needs visibility, costs, effects, AI, localisation direction, failure outcomes, and cleanup.

## Required management actions

Implement or adapt every accepted row in `022_concentration_camps_decision_map.md`, including:

- freeze intake
- place network under review
- resume coercive operation when route-valid
- centralize or dissolve administration
- limited confiscated-property action
- restore food and medicine
- register detainees
- open site to inspection
- reduce labour quota
- begin regional closure
- preserve records
- release or transfer survivors
- industrial, construction, extraction, and logistics assignments
- raise or lower assignment intensity
- expand into selected state
- reinforce guards
- import or transfer detainees from a valid source
- resolve resistance network
- restrict access
- falsify records
- destroy records
- stage inspection
- abandon site
- convert selected site to extermination
- set valid target purpose
- raise or halt extermination
- activate restricted chemical site
- broaden purge inward

Use working IDs from the decision map unless current namespace rules require a documented adjustment.

## Required emergency actions

For a threatened state implement:

- close and leave survivors in place
- supplied transfer
- forced evacuation on foot
- liquidation of remaining detainees for a valid extreme route
- destroy site and records
- abandonment

The category must make ordinary management unavailable while the emergency is active.

Every outcome must preserve responsibility, evidence, population accounting, and later liberation hooks.

## Required missions

### Perpetrator or operator missions

- coordinated escape crisis
- camp epidemic or famine crisis
- enemy approaching site
- regional closure
- underground local network after central closure order

### Liberator missions

- emergency survival
- trace and reunite
- document the network
- regional resettlement

Mission duration should vary by difficulty. Ordinary easy missions should normally be at least 90 days. Emergency front missions can be shorter when the campaign demands it.

Goal-style missions should complete automatically when the player does the required work. Do not require another paid click.

Success, partial success, and failure need distinct effects.

## State targeting

Use the least cluttered supported state-target pattern.

Every target decision must:

- highlight only valid states
- name the state
- explain why it qualifies
- show current site type and status
- show cost and main visible consequence
- explain the exact blocked reason
- revalidate on click

Do not expose raw state-ID lists.

When a regional group is used, build it from actual active or relief states and show the included states through dynamic localisation or tooltip.

## Forced-labour validation

- industrial assignment requires factories
- construction assignment requires active construction or repair role
- extraction requires resources or accepted extraction role
- logistics requires rail, port, depot, or supply role
- one assignment per state
- site needs workforce, guards, supply, and transport
- assignment ends on closure, conversion, liberation, exhaustion, or failed prerequisites
- output decays with workforce and pressure
- extermination conversion removes production bonuses
- no assignment creates free permanent factories or resources

## Target-purpose validation

- no ethnicity or race percentage is invented
- use registered country-specific protected groups only when present
- otherwise use occupied civilians, refugee markers, resistance detainees, political persecution, or broad domestic purge
- genocide terminology requires the accepted protected-group and intent proof
- no valid target source blocks extermination decisions and gives AI zero chance
- broad domestic purge carries severe national effects and Event 21 or Event 31 pressure

## Population and evidence calls

Decisions must call public Event 22 or shared helpers. Do not duplicate exact population-loss, responsibility, Deaths, evidence, or Condemnation logic in many decision effects.

A decision that causes deaths must provide:

- cause
- state
- responsible actor
- requested loss inputs
- current network generation
- evidence consequence
- cleanup and history consequence

A decision that moves people must use migration or transfer accounting and cannot also remove them as deaths.

## Country-specific adapters

Germany, Japan, and the Soviet Union keep their accepted categories. Add adapter calls and missing rows inside those packages. Keep the full generic category hidden beside them.

Audit:

- duplicate decisions
- mismatched costs
- incompatible responsibility helpers
- missing evolution actions
- inconsistent localisation
- generic state targeting that bypasses historical registries

## AI behavior

Every decision and mission needs valid AI logic.

Implement the profiles and scenarios from `022_concentration_camps_ai_probability_matrix.md`.

Hard zero examples:

- no target source for extermination
- no useful assignment role
- no transport for a transfer
- site already closing
- reach at cap
- relief state for perpetrator expansion
- missing technology or stockpile for chemical operation
- no safe destination for survivor transfer

AI should compare expected benefit duration with setup cost, workforce depletion, front distance, exposure, resistance, and supply.

Do not hand-tune important weights without the MCP probability pass.

## Presentation and localisation

Use concise dynamic category text and tooltips.

Player must understand:

- current policy
- current state
- what changes the three visible values
- why the current threshold matters
- which action responds to it
- visible costs and consequences

Do not expose hidden probability rolls, full evidence ledgers, internal components, future incidents, or invented demographic data.

Localisation should be grave and clear. No jokes, graphic detail, fake quotations, procedural killing descriptions, or sanitized economic framing.

## Cleanup

Every decision and mission must close when its actor, state, policy, route, war, site, target source, network generation, or relief condition becomes invalid.

Cleanup must clear:

- selected state or country target
- temporary flags
- active mission
- cost quote variables
- stale dynamic localisation target
- assignment and intensity state where operation ended
- emergency mode after resolution

Cleanup must preserve:

- responsibility
- evidence
- Deaths history
- evolution shock markers
- survivor and relief status
- event history

## Audit routing

After the first complete implementation:

1. Spawn `chaosx_decision_mission_auditor` with `fork_context=false`.
2. Give it the exact touched files, accepted decisions, and handoff path.
3. Allow local patches to decisions, missions, tooltips, AI, cleanup, costs, and visibility.
4. Route every complex weight to `chaosx_ai_probability_auditor`.
5. Route shared-helper gaps to `chaosx_scripted_system_architect`.
6. Route localisation gaps to `chaosx_localisation_auditor`.

Subagent handoffs go under:

```text
docs/plans/022_concentration_camps_plans/subagent_handoffs/
```

## Validation

Run:

- event and decision parser validation
- decision and mission duplicate audit
- cost-type audit
- visibility and cleanup audit
- AI validity audit
- probability inspect, evaluate, sweep, sequence, and compare
- save and reload tests
- country-specific adapter tests
- civil-war and tag-change tests
- multiplayer target-isolation test
- live UI review at normal resolution
- fresh error-log delta review

Use dedicated saves for baseline, each evolution, liberation, retreat, and successor paths.

## Completion report

Return:

- changed files
- category, decision, and mission IDs
- helper calls
- cost and scaling constants
- AI profiles and probability evidence
- localisation keys
- category and state presentation
- country-specific adapter changes
- cleanup behavior
- tests run and results
- screenshots and logs
- subagent handoffs
- skipped validation and reason
- remaining blockers

Do not claim completion when any accepted path exists only as a tooltip, when a state action bypasses shared population accounting, when AI can select an invalid action, or when the category exceeds its visible action budget.
