# Event 067 Generalissimo Full Implementation Prompt

Implement Event `067` Generalissimo to the fullest extent described by the accepted specification pack.

## Source of truth

Read every file under:

`docs/specs/067_generalissimo_specs/`

Treat the nine specification parts as acceptance criteria. Use the diagrams, research, probability matrix, surface map, catalog handoff, and specialist prompts as supporting implementation contracts.

Also read all required repository skills and references named by those files, including:

- `AGENTS.md`
- `chaos-redux-events`
- `chaos-redux-decisions-missions`
- `chaos-redux-focus-trees`
- `chaos-redux-event-assets`
- `chaos-redux-frame-animation`
- `chaos-redux-super-events`
- `chaos-redux-subagents`
- `chaos-redux-improvement-loop`
- current offline Paradox wiki pages
- current vanilla documentation and direct precedents
- current Event 019, Event 065, Event Logs, Event Details, cluster, scenario, world-end, civil-war, character, and country-provider implementations

Do not implement from this prompt alone. The full pack defines the event.

## Required result

Deliver one complete Minor Fire-Once event with:

- entry event `chaosx.nr067.1`
- Chaos level 1
- Military Preparation cluster membership as a High member
- one valid major or player-controlled host
- one canonical fictional male Generalissimo
- maximum safe commander level and attributes
- every safe positive applicable general and field marshal trait
- maximum useful command capacity
- direct military use after he becomes ruler
- hidden service record before Evolution I
- Generalissimo Influence from 0 to 100 as the only public pre-coup value
- paced evolutions at 200, 400, and 600 or higher Chaos
- demands, concessions, counterweights, missions, and removal methods
- immediate revolt after failed arrest, capture, assassination, or final removal
- dynamic revolt strength and a viable host-derived civil war
- peaceful submission
- full military-government country package
- Command Cohesion from 0 to 100 as the only public post-takeover value
- full host-adaptive focus tree
- route-specific decisions, missions, AI, and postwar integration
- manual scenario Generalissimo's Coup
- public world-end branch The Generalissimos' World
- two complete super-events
- complete static visual asset package
- eight achievements
- full Event Logs, Event Details, evolution, scenario, cluster, docs, and catalog alignment

## Core identity rules

Create one character token. Never create separate commander, field marshal, ruler, scenario, or world-end clones.

Prefer a dynamic civil-war side. Do not reserve a fixed junta tag unless current engine and MCP inspection proves that a required surface cannot function dynamically. A fixed tag remains blocked until a fresh collision scan covers vanilla, Chaos Redux, installed Workshop mods, and sibling local mods.

The junta remains human and uses normal civilian systems. Do not classify it as actual nonhuman. Do not classify it as a special Chaos country without a concrete cross-system exclusion need.

No custom unit, equipment family, technology tree, doctrine tree, 3D model, unit counter, or unit audio package belongs to this event.

No full-screen event mechanic window belongs to this event. Use the accepted ordinary decision category, compact attached display, static phase pictures, and small read-only focus inlay.

## Implementation order

### 1. Preflight and mapping

- inspect the current Event 067 placeholders and registrations
- confirm current commander, character, civil-war, focus-loading, scenario, world-end, cluster, Event Logs, and Event Details patterns
- confirm whether `SCN-015` is free in the authoritative workbook and runtime registry
- confirm the current Military Preparation cluster identity or resolve its missing registry row
- inspect Event 019 claimant commander integration
- inspect Event 065 trait-provider integration
- map exact touched files before editing
- preserve unrelated user changes

Use `chaosx_repo_explorer` only if this mapping remains unclear after direct inspection.

### 2. Scripted owner layer

Use `067_generalissimo_scripted_system_prompt.md` and `chaosx_scripted_system_architect`.

Implement:

- constants
- valid-host trigger
- one-character creation and transfer
- trait package audit
- hidden service record
- Influence calculation
- command authority
- evolution pacing
- demands
- removal calculations
- revolt-strength allocation
- dynamic country setup
- peaceful takeover
- Command Cohesion
- scenario setup
- world-end actor registry
- cleanup and repair

Keep event-owned lifecycle in event-owned files. Do not pollute shared dynamic registries with owner logic.

### 3. Event chain and registration

Implement the full event family, including:

- appearance
- evolution transitions
- demands
- concessions and refusals
- removal results
- ultimatum
- revolt
- peaceful submission
- government victory
- junta victory
- foreign reactions
- world-end launch and world-end reactions

Register the event as Minor Fire-Once with Chaos level 1. Add it to the reworked default-enabled allowlist only when the complete event is ready for normal selection.

Use `hoi4.event_inspect`, `hoi4.event_render`, and `hoi4.event_compare` before and after the event-chain change.

### 4. Decisions and missions

Use `067_generalissimo_decision_mission_prompt.md` and `chaosx_decision_mission_auditor`.

Implement the crisis category, military-government category, postwar integration, and world-end actions. Keep each phase readable. Use real military, equipment, intelligence, political, and unit-commitment costs. Do not turn the category into a political-power store.

Every visible chance must match the executed chance. Failed arrest, capture, assassination, and final removal start the revolt immediately.

### 5. Dynamic country and civil war

Create a viable split based on Influence and hidden support.

The junta receives:

- useful territory
- a valid capital
- forces and templates
- manpower and equipment
- appropriate commanders
- stockpiles
- military factories and bases
- navy and air assets only where relevant
- three starting ideas
- the canonical Generalissimo
- the dedicated focus tree

The legal government retains a viable capital, forces, supply, and a real route to victory. Avoid total transfer, empty sides, isolated capitals, fixed-state assumptions, and broken one-state cases.

Resolve subjects, factions, guarantees, wars, and third-party annexation explicitly.

### 6. Focus tree and inlay

Use `067_generalissimo_focus_tree_prompt.md`, `chaosx_focus_tree_auditor`, and the required MCP focus workflow.

Implement every political, military, economic, internal-rule, foreign-policy, integration, conditional service, and hidden world-end route. Include search filters, Focus Navigation, route AI, idea lifecycles, and the accepted focus inlay.

Use `chaosx_event_ui_worker` only for the Event 067 inlay and compact display. Require the complete GUI inspect, render, rewrite, and comparison sequence over relevant states and resolutions.

### 7. AI and probability

Use all relevant scenarios from `067_generalissimo_probability_scenario_matrix.md`.

Before changing any AI or random weight:

1. run `chaosx_ai_probability_auditor`
2. begin with `hoi4.probability_inspect`
3. establish named baseline results
4. apply the intended patch through the owning agent or parent
5. run the auditor again
6. require `hoi4.probability_compare` over the same scenarios

Cover host targeting, evolution pacing, demand choice, concession and removal AI, revolt allocation, focus routes, scenario intensity, world-end outcomes, and bloc behavior.

### 8. Assets and portrait

Use `067_generalissimo_asset_prompt.md`.

Route:

- the one fictional portrait to `chaosx_portrait_creator`
- generated non-icon art to `chaosx_generated_event_art`
- icons and achievement triplets to `chaosx_icon_artist`

Create every accepted asset family. Keep separate source art for portraits, focus icons, ideas, decisions, category pictures, traits, flags, achievements, and super-events. Do not satisfy one icon family by resizing another.

Keep `docs/assets/067_generalissimo/` while work is active or blocked. Before full completion, promote durable evidence, verify runtime wiring, and delete the temporary event workspace according to the asset skill.

### 9. Super-events

Use `067_generalissimo_super_event_prompt.md`.

Complete:

- ruler super-event after peaceful submission or junta reunification
- world-end super-event at The Generalissimos' World launch

Use separate sourced quote and audio research. Each super-event needs a unique licensed musical recording, complete sound wrappers, settings-aware playback, final image, final text, source documentation, and music-catalog row.

Do not invent quotes, use uncertain audio, reuse default tracks, or leave placeholders.

### 10. Achievements

Use `067_generalissimo_achievement_prompt.md`.

Implement all eight achievements with exact eligibility, disqualifiers, tracking, localisation, and completed, grey, and not-eligible icon triplets.

### 11. Scenario and world-end

Confirm the stable scenario ID before writing the authoritative workbook or registry. Implement all four scenario types and four intensity stops. The launch must bypass normal timing and evolution prerequisites without counting as a normal event firing or pacing transaction.

Implement the public world-end branch with its independent Event Details toggle, 1000 or higher Chaos gate, active canonical Generalissimo requirement, bounded actor registry, military-government outcomes, rival blocs, International Command, Civil Authority Compact, and normal world-end event freeze.

### 12. Localisation, docs, and catalog

Use `chaosx_localisation_auditor` after broad text exists.

Write final in-world localisation for:

- events and news
- options
- decisions and missions
- tooltips
- ideas and traits
- focus tree and inlay
- dynamic country names and parties
- scenario UI
- achievements
- super-events
- Event Logs and Event Details

Do not paste planning directions or working labels as final text. Do not expose hidden values, future branches, debug state, rework history, tuning notes, or implementation language.

Update permanent Event 067 documentation. Update only `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, then run `python .tools/export_event_catalog_csv.py`. Never edit catalog CSV exports directly.

## Required specialist routing

Use context-complete prompts with no inherited parent context.

Required near-final routes:

- `chaosx_focus_tree_auditor`
- `chaosx_decision_mission_auditor`
- `chaosx_country_package_auditor`
- `chaosx_localisation_auditor`
- `chaosx_ai_probability_auditor`
- `chaosx_event_completion_auditor`
- `chaosx_spreadsheet_doc_worker`
- `chaosx_improvement_loop_planner`

Use `chaosx_documentation_curator` when handoffs and docs become difficult to reconcile.

Do not spawn another improvement-loop pass until the previous addendum has been implemented, folded into specs, queued with a reason, or rejected with a reason.

## Improvement-loop gate

After the first complete implementation tranche, run the improvement loop against the actual implementation.

The planner must inspect:

- event lifecycle
- decisions and missions
- focus tree
- dynamic country package
- AI
- assets
- super-events
- scenario
- world-end campaign
- integrations
- current plans and handoffs

Implement or formally disposition every accepted addendum. Run a final closure review. Do not claim completion while an accepted expansion remains unresolved.

## Meaningful validation

Required evidence includes:

- event-chain inspect, render, and compare
- focus inspect, normal-zoom render, rewrite, and compare
- GUI inspect and render across relevant states and resolutions
- probability baseline and post-patch comparisons
- trait allowlist and exclusion audit
- character uniqueness and ownership scenarios
- dynamic civil-war split matrix
- peaceful-submission path
- government victory and junta victory
- save-state idempotence through source-level and MCP evidence
- manual scenario type and intensity matrix
- world-end outcome and actor-registry scenarios
- Event Logs, Event Details, cluster, and catalog crosswalk
- final asset and audio runtime crosswalk
- route coverage table
- decision and mission audit
- country package audit
- localisation audit
- completion audit

Do not invoke the autonomous live debug-playtest skill unless the user explicitly requests it. Normal source, MCP, and repository validation remain required.

## Completion report

Create a permanent Event 067 completion report with:

- files changed
- systems implemented
- event state coverage
- character and trait audit
- Influence and Command Cohesion behavior
- demand and removal coverage
- civil-war allocation cases
- peaceful takeover and victory outcomes
- focus route coverage
- AI and probability evidence
- scenario coverage
- world-end coverage
- assets, portrait, flags, icons, super-events, audio, and achievements
- Event Logs and Event Details alignment
- docs and workbook alignment
- specialist handoffs and dispositions
- improvement-loop addenda and dispositions
- task-specific validation
- every unresolved blocker
- every simplification, merger, omission, fallback, or replacement

If no simplifications were made, state that explicitly and support it with the route, asset, audit, and scenario evidence. Do not claim completion because the event compiles, the popup appears, or the commander exists.
