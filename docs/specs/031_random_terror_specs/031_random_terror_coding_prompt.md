# Event 31 Random Terror full implementation prompt

## Goal

Implement Event 31 Random Terror to the fullest extent defined by:

`docs/specs/031_random_terror_specs/`

Treat every specification part, matrix, research note, and prompt in that folder as accepted source design.

Do not replace mapped content with a smaller prototype, generic fallback, placeholder, or partial chain.

Do not claim completion until the final repository satisfies the complete package.

## Required project reading

Before editing, read:

- `AGENTS.md`
- `chaos-redux-events`
- `chaos-redux-decisions-missions`
- `chaos-redux-focus-trees`
- `chaos-redux-event-assets`
- `.agents/skills/chaos-redux-event-assets/references/portrait-production.md`
- `chaos-redux-frame-animation`
- `chaos-redux-super-events`
- `chaos-redux-improvement-loop`
- `chaos-redux-subagents`
- `CHAOS_REDUX_MECHANICS`
- the dynamic trigger and effect registries
- the authoritative event catalog workbook
- every file in `docs/specs/031_random_terror_specs/`

Read the required offline Paradox wiki core pages and the pages for events, decisions, ideas, AI, characters, focuses, countries, interface, scripted GUI where relevant, graphical assets, achievements, sound, technology, and map presentation.

Read relevant current vanilla documentation from the installed game and inspect at least one vanilla precedent for every engine-facing surface.

Inspect current Chaos Redux precedents before choosing new patterns.

Do not rely on memory when local documentation exists.

## Repository and tool preflight

Use `chaosx_repo_explorer` with `fork_context=false` because this is a large cross-surface event and the live file map is not included in the planning package.

Map:

- existing Event 31 files and placeholder content
- random-event category registration and default-enable allowlist
- pre-fire actor and history pipeline
- event log and Event Details selectors
- evolution registry and UI
- public world-end registry and toggles
- triggerable scenario registry
- country-carrier collections and protected tag audit
- special Chaos and actual-nonhuman classifiers
- world-threat aggregate
- Deaths and Condemnation APIs
- decision categories and selected-target patterns
- state map-mode or highlight precedents
- focus-tree loading, filters, Focus Navigation, and carrier trees
- achievement registry
- portrait, flag, icon, report, news, super-event, sound, and animation consumers
- documentation and authoritative workbook rows

Use the mandatory HOI4 MCP routes for supported event, focus, probability, technology, GUI, and map surfaces.

If a required route is unavailable, record the exact blocker. Do not treat source-only review as equivalent evidence.

Agents must not launch or play Hearts of Iron IV unless the user explicitly invokes the autonomous debug-playtest skill. Normal implementation ends with source, MCP, audit, and user-owned in-game handoff evidence.

## Stable identity

Preserve:

- Event ID `31`
- event name `Random Terror`
- type `Minor Repeatable`
- Chaos level `1`
- entry event `chaosx.nr31.1`
- evolution names from the specification
- manual scenario name `Global Jihad`
- public world-end name `The False Revelation`

Verify proposed scenario ID `SCN-014` and proposed future cluster ID `9` against the authoritative workbook and live registries before reservation.

Do not register Internal Fracture until enough member events are reworked and the cluster is accepted.

Event 31 must work without that cluster.

## Core event system

Implement one global repeatable firing that selects several valid countries and exact states.

One firing counts as one global pacing event.

National follow-ups and incidents must not advance the random-event timer again.

Register Event 31 in the repeatable category, type selectors, name selectors, debug selectors, history, Event Details, and default-enable allowlist only when the full rework is ready.

A country with no valid state makes the event unavailable for that target.

The global event shows `N/A` when no valid target exists.

Use the ordinary repeatable weight, recovery, and cap behavior from the shared system.

## Representation rules

Every Event 31 organization, leader, flag, emblem, faction, country identity, and slogan is fictional.

Religion, ethnicity, nationality, civilization, refugee population, immigrant population, and ordinary ideology never add to baseline target or recruitment weight.

Evolution IV introduces one fictional jihadist branch.

Muslim governments, communities, clerics, soldiers, and fictional religious authorities can be its main opponents.

Use an event-local Muslim-majority registry only for the later actor-specific reaction and enemy-priority system.

Never use it for ordinary vulnerability, recruitment, or cell formation.

The game never confirms that the False Revelation entity is Allah.

No asset or audio may depict Allah, use sacred calligraphy as hostile branding, use Quran recitation, the call to prayer, Islamic sacred chant, or a real extremist symbol.

Do not reproduce real attack planning, evasion, financing, recruitment, or propaganda methods.

## Values and state progression

Implement centralized tuning and visible stages for:

### Government

- Terror Pressure, `0` to `100`
- Response Legitimacy, `0` to `100`

### State activity

- Clear
- Dormant
- Active
- Entrenched
- Armed Insurgency
- Lost Local Control

### Later global values

- Network Reach after Evolution II
- International Unity after Evolution IV

### Territorial actors

- Territorial Control
- Network Authority
- External Supply

### Hidden

- Apocalyptic Readiness

Show only current relevant values.

Keep hidden formulas hidden.

The decision category, state map presentation, events, focuses, AI, and tooltips must read the same source values.

## Targeting and incidents

Implement country and state eligibility, weighted opportunity, geographic diversity, recent-target cooldowns, active-crisis reinforcement, and invalid-state exclusion from Part 2.

Use exact state targets.

Do not substitute a capital proxy when the incident belongs elsewhere.

Implement the accepted incident families and their stage and geography validity.

At minimum include civilian attacks, transport disruption, depot sabotage, port and convoy attacks, fictional official assassination attempts, hostage crises, security-site attacks, propaganda surges, arms theft, sponsor evidence, corridors, training areas, copycats, failed raids, intelligence breakthroughs, defections, relief strain, military defection, capital infiltration, rival organizations, community rejection, joint operations, sponsor exposure, and cannibal clashes.

Keep incident content tactically abstract.

Use event-owned scheduled pulses only for affected countries and actors.

Do not add a recurring whole-world daily, weekly, or monthly scan without explicit user permission.

Implement cross-state and cross-border spread with causal evidence and cooldowns.

Implement complete invalid-target, annexation, state-transfer, actor-death, and crisis-clear cleanup.

## Deaths, damage, Chaos, and Condemnation

Use the shared exact state population-loss and Deaths routes.

Create stable Event 31 death reasons that distinguish extremist attacks, territorial atrocities, government counterterror casualties, and world-end consequences.

Do not apply the same deaths twice.

Damage real buildings only when they exist and the incident supports them.

Use state population, incident severity, protection, state activity, and outcome quality for dynamic losses.

Reserve direct Chaos changes for public strategic shocks and avoid double counting deaths and wars.

Use Condemnation for exposed sponsorship, public atrocities, collective punishment, cover-ups, forced rule, and repeated public abuse.

Do not treat ordinary lawful response as condemnation.

## Government decisions and missions

Implement the full decision and mission matrix through `chaos-redux-decisions-missions`.

Use the accepted ordinary category presentation and event-owned state map mode.

Do not create a permanent dedicated GUI.

Keep three to five visible primary actions, six as the hard maximum, and no more than three active missions.

Use no more than four spendable cost types per action.

Use action-appropriate equipment, fuel, trains, convoys, manpower, divisions, XP, conservative command power, civilian capacity, legitimacy risk, and foreign obligations.

Do not turn the category into a political-power store.

Implement clean success, costly success, partial success, failure, and abusive failure for operations.

Implement consent for every foreign resource or unit commitment.

Write compact icon-first costs and exact blocked tooltips.

Spawn `chaosx_scripted_system_architect` with `fork_context=false` for repeated Event 31 helpers, selected-target contracts, constants, targets, and cleanup.

Keep subsystem-private helpers in Event 31 files.

## Baseline territorial escalation

Baseline can already create coups, capital seizures, civil wars, government takeover, partition, negotiated enclaves, and temporary territorial countries.

Do not gate all territorial creation behind Evolution III.

Coordinate with Event 21 so one country does not receive duplicate civil wars.

Choose the outcome that fits geography, pressure, military defection, capital state, and parent viability.

A stable country cannot lose territory from the first ordinary attack.

## Evolutions

Implement the five accepted evolutions as true global event changes.

- Organized Cells
- Transnational Terror Network
- Territorial Insurgency
- The Jihadist International
- The Final Jihad

Use delayed active-event pacing and dynamic factors from Part 4 and Part 9.

When Event 31 has never fired, begin its first firing at the active evolution level without replaying all lower stages as immediate popups.

Every evolution has an independent enable state and full event-log coverage.

A disabled evolution must not set recorded flags, expose hidden routes, or block baseline resolution.

Evolution IV alone introduces the fictional jihadist current.

It does not convert every Event 31 organization.

Evolution V makes The False Revelation eligible but never fires it automatically.

## Territorial country packages

Implement the complete country-package matrix.

Use shared protected carriers, origin-aware package state, and full collision audits across vanilla, Chaos Redux, installed Workshop references, and local mods.

Do not duplicate Event 006 or Soviet Collapse carriers.

Every durable actor needs:

- valid territory
- viable capital
- parent survival or valid takeover
- fictional identity
- leader or council
- parties and politics
- flags
- three starting idea lifecycles
- actor values
- starting research slots
- compatible technology
- real starting forces and equipment
- reinforcement pathways
- economy and supply
- route-appropriate air and naval access only from real sources
- decisions
- focus loading
- diplomacy and AI
- merger, split, takeover, defeat, and cleanup

Use existing combat battalions and support companies.

Do not add a custom Event 31 unit, equipment archetype, 3D model, custom unit sound, or bespoke unit counter.

No Event 19 provider is required under the accepted design.

Territorial Event 31 actors are special Chaos countries and remain outside the actual-nonhuman classifier.

The False Revelation state remains human-populated and also stays outside actual nonhuman.

## Focus tree

Implement the shared actor-specific focus framework from Part 6.

Required route families:

- opening survival
- Shadow Council
- War Directorate
- Ideological Secretariat
- Captured Economy
- Armed Movement
- Network and Diplomacy
- Expansion and State Capture
- Crisis and Failure
- Jihadist International
- Final Jihad
- False Revelation terminal replacement

The implementation agent owns exact focus count, IDs, coordinates, prerequisites, and clean layout.

Preserve the accepted architecture, tradeoffs, idea lifecycles, decision links, route payoffs, and hidden-route conditions.

Use varied rewards, proper icons, search filters, Focus Navigation, route-specific localisation, and route-specific AI.

Do not create filler branches, repeated spirit stacks, fake nonlinearity, crossing connectors, or unrelated regional formables.

Use `hoi4.focus_inspect`, `hoi4.focus_render`, and bounded `hoi4.focus_rewrite` passes until first-glance branch clarity passes.

Run `chaosx_focus_tree_auditor` after the tree is complete.

When technology grants or research bonuses change the graph, use `hoi4.tech_inspect`, `hoi4.tech_render`, and `hoi4.tech_compare`.

## Global Jihad scenario

Verify and register the stable scenario ID.

Implement all five deployment types:

- Dispersed Networks
- Border Corridors
- Capital Uprisings
- Territorial Fronts
- Random Pattern

Implement Low, Medium, High, and Maximum intensities.

The launch must validate the complete transaction before state changes.

Create viable actors, parent governments, cells, wars, network values, faction structure, response tools, and AI.

Use a tightly scoped setup bypass and clear it after launch.

The scenario does not advance random-event pacing or spend Event 31 repeatable weight.

Cancel changes nothing.

A failed setup leaves no partial state.

Maximum activates the Final Jihad and never bypasses the `1000+` Chaos and territorial readiness gates for The False Revelation.

## The False Revelation

Implement one public world-end branch with its own registry row and persistent independent toggle.

Require:

- `1000+` Chaos
- Evolution V enabled and recorded
- no existing world end
- branch enabled
- viable jihadist actor
- substantial territorial success
- widespread crises
- high International Unity
- major strategic victory
- hidden readiness
- delayed transition

Select or safely create the dominant host.

Reconcile existing actors through merger, subordinate command, rival claim, or fragmentation.

Preserve player control through explicit multiplayer-safe rules.

Set the shared and scenario-specific terminal state only after the full transaction validates.

Freeze ordinary random-event firing and keep terminal content active.

Implement pressure-grounded uprisings, terminal values, extreme staged abilities, command capitals, supply corridors, coalition objectives, defeat outcomes, and structured aftermath.

Do not create rebel armies in countries with no cells or pressure.

## Cross-event and shared-system integration

Implement Part 10.

Mandatory integrations include:

- absolute hostility and no alliance with Event 14 cannibal actors
- Event 21 duplicate-civil-war prevention
- Event 006 carrier protection
- Natural Disaster relief and state context without blaming refugees
- exclusion of Death, Rat Nations, zombies, and incompatible special actors from ordinary targeting
- optional guarded Event 16 connections
- no Event 19 custom-unit integration under current design
- guarded nuclear and missile seizure only through actual owning-system state
- shared Deaths, Condemnation, Chaos, Air Cleanliness, country carriers, classifiers, world threat, logs, and scenario systems

Register and maintain an Event 31 world-threat source only when the event becomes a genuine existential threat.

Clear it from real surviving world state.

## AI and probability

Implement government, cell, actor, route, jihadist, final-command, coalition, and scenario AI from Part 9.

Use every named scenario in `031_random_terror_ai_scenario_matrix.md`.

Any weighted patch requires:

1. baseline `chaosx_ai_probability_auditor` pass
2. parent or owning-agent patch
3. final auditor pass with `hoi4.probability_compare` against the same scenarios

Distinguish exact, bounded, sampled, score-only, and unresolved results.

Do not claim normalized probability from an incomplete pool.

Include paired identity-fairness cases proving Muslim-majority status, refugee population, ethnicity, nationality, and ordinary ideology do not raise ordinary target scores.

## Assets

Execute `031_random_terror_asset_prompt.md` through the correct asset workers.

Every flag uses the flat ImageGen workflow.

Every portrait is fictional or institutional and belongs to `chaosx_portrait_creator`.

Create final report, news, category, focus, idea, decision, mission, state, faction, achievement, and super-event assets.

Create the authorized entity portrait animation only after verifying the exact consumer and static fallback.

Do not use placeholders, primitive art, resized cross-family icons, real extremist symbols, sacred hostile branding, or modern props.

The parent owns final non-portrait `.gfx` and gameplay wiring.

## Super-events

Execute `031_random_terror_super_event_prompt.md`.

Research and verify the reveal and defeat packages.

Each needs a final title, description, button, sourced quote, generated image, unique licensed or public-domain musical recording, final WAV, unique audio ID, source and rights record, settings-aware playback, permanent docs, and canonical audio-catalog entry.

Treat unresearched text, quote, image, audio, or slot as a blocker.

Do not use default or placeholder audio.

## Achievements

Implement all `12` achievements from `031_random_terror_achievement_prompt.md`.

Use the single root achievement registry.

Implement tracking, disqualifiers, hidden states, localisation, original icon triplets, docs, and valid and invalid test cases.

Force-trigger, debug, tag-switch, scenario, and contribution protections must work exactly as specified.

## Event logs and Event Details

Complete all name, type, actor, history, evolution, Event Details, world-end, and scenario surfaces.

Prepare the primary actor before generic history recording when needed.

History and evolution log surfaces show real dates and sequence metadata.

Event Details catalog surfaces do not show fake history metadata.

The False Revelation row has an independent persistent toggle.

Do not expose hidden readiness, probability, entity identity, or future surprises.

## Localisation

Write finished player-facing text from the direction in the specs.

Do not paste prompts, working labels, instruction language, debug names, hidden formulas, or implementation history.

Use exact dynamic actors, countries, states, corridors, values, and routes where the player needs them.

Keep every route voice distinct.

Follow all project prose rules.

Run `chaosx_localisation_auditor` after broad text exists and resolve its handoff.

## Documentation and workbook

Write complete Event 31 docs and update every affected system document.

Update only:

`docs/spreadsheets/chaos_redux_events_catalog.xlsx`

Then run:

`python .tools/export_event_catalog_csv.py`

Never edit the three CSV exports directly.

Use `chaosx_spreadsheet_doc_worker` only after final in-game-facing wording and implementation facts are stable.

Use `chaosx_documentation_curator` during the long implementation when specs, plans, handoffs, manifests, or reports need reconciliation.

## Required subagent routing

All project subagents use `fork_context=false` and context-complete prompts.

Use the routing file in this package.

At minimum, route appropriate work to:

- repo explorer
- scripted-system architect
- decision and mission auditor
- focus-tree auditor
- country-package auditor
- localisation auditor
- portrait creator
- generated event art
- icon artist
- super-event text researcher
- super-event audio researcher
- AI probability auditor
- spreadsheet worker
- documentation curator when needed
- event completion auditor
- improvement-loop planner near completion

Do not invoke the event UI worker because the accepted design has no event-owned dedicated GUI.

Do not invoke the 3D model pipeline because the accepted design has no custom 3D asset or custom unit.

## Improvement loop

The planning package already contains a closure review.

After a meaningful implementation tranche, inspect whether implementation exposed a new broad design gap not covered by the specs.

Near completion, spawn `chaosx_improvement_loop_planner` with `fork_context=false`.

It should return a closure handoff unless implementation created a new material gap.

Resolve, promote, queue with a reason, or reject every addendum before completion.

Do not stack another plan while a previous Event 31 addendum is unresolved.

## Final audits

Before completion run:

- event MCP inspect, render, compare
- probability baseline and compare passes
- focus inspect, render, rewrite review, and audit
- technology inspect, render, compare where affected
- decision and mission audit
- country-package audit
- localisation audit
- asset and super-event reconciliation
- documentation and workbook reconciliation
- event completion audit

Resolve every blocker or report the goal incomplete.

## Completion report

The final report must list:

- files changed
- event registration and chain
- decisions and missions
- values and state stages
- evolutions
- country packages
- focus routes
- AI and probability evidence
- Global Jihad types and intensities
- False Revelation and aftermath
- cross-event systems
- assets and animation
- super-event text, image, audio, and rights
- achievements
- event logs and Event Details
- docs and workbook
- commits
- meaningful validation findings
- unresolved blockers
- every simplification, fallback, merge, omission, or replacement

If no simplifications exist, state that and support it with route, matrix, asset, audit, and documentation coverage.

Keep iterating until the implemented files satisfy the entire specification. Do not claim completion because the event popup works, the game parses, or the most visible surfaces exist.
