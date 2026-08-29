# Coding Prompt: Implement Event 021 Random Civil War

Implement the complete source specification under `docs/specs/021_random_civil_war_specs/`.

This is a large event framework. Do not reduce it to one `start_civil_war` call, a fixed territory split, a fixed half-army split, one popup, or a political-power store.

## Preflight

Before editing:

1. Read repository `AGENTS.md`.
2. Read the full Event 021 package in its documented order.
3. Read `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-focus-trees`, `chaos-redux-event-assets`, `chaos-redux-improvement-loop`, and `chaos-redux-subagents`.
4. Read the required offline Paradox wiki pages and installed vanilla documentation.
5. Inspect vanilla and Chaos Redux civil-war, country, decision, mission, AI, cluster, event-log, scenario, and asset precedents.
6. Inspect Event 006 specs, package registry, carrier collections, initialization, leaders, flags, trees, forces, reinforcement, formables, decisions, AI, assets, origin logic, and documentation.
7. Inspect Event 004, Event 007, and every specialized civil-war event named in the overlap reconciliation.
8. Verify the current authoritative XLSX workbook and live scenario registry.
9. Run the current HOI4 MCP schemas. Do not invent tool names.
10. Spawn every project subagent with `fork_context=false`.

Use the context-complete prompts in `subagent_prompts/`.

## Event identity

- Event ID `21`
- canonical entry `chaosx.nr21.1`
- Minor Repeatable
- chaos level 1
- Cluster 1, Wars
- Medium member severity

Keep the event unavailable by default until the full rework is ready.

When no valid target exists:

- remove live weight
- show `N/A`
- do not queue a nonexistent actor

## Shared framework

Build reusable Event 021 logic for:

- hidden Fracture Pressure
- visible State Authority
- valid-target pool
- opening severity
- archetype selection
- connected region planning
- viable capitals and supply
- parent remnant protection
- territory, unit, stockpile, air, and naval allocation
- ordinary claimant setup
- Event 006 package adapter
- front registry
- normal decision-category state
- active and prefire evolution paths
- neighbor exposure
- bounded global scheduling
- settlement
- successor memory
- recurrence
- theater and generation caps
- cluster and manual scenario adapters
- complete cleanup

Centralize thresholds, caps, weights, duration bands, AI tuning, and scaling in script constants or documented subsystem tuning.

Do not add an unrestricted default daily, weekly, or monthly whole-country iteration. If the design cannot be implemented without one, stop and obtain explicit approval.

## Baseline

Support:

- ideological uprising
- rival legal government
- regional secession
- Event 006 independence actor
- broad command schism
- same-tag takeover for unsafe one-state or all-island countries

Baseline normally targets minors and creates one primary opponent.

Stable countries receive a smaller crisis. Unstable, exhausted, occupied, divided, or poorly administered countries receive a larger crisis.

Plan territory before changing ownership. Regions should be connected, supplied, capital-capable, and militarily viable. Protect a playable parent remnant.

Allocate forces from actual conditions. Use unit location, territory, depots, command loyalty, ideology, local support, war state, and severity. Never blindly split half the army or stockpile.

## Decisions and missions

Use a standard decision category with:

- static category picture
- concise dynamic text
- one visible State Authority value
- phase and main pressure
- current priority front
- three to five actions
- one to three active missions

Do not create a custom GUI, selected-front window, animated seal, or animated category art.

Use concrete costs, map objectives, supply, equipment, manpower, experience, diplomacy, unit commitments, and time. An action can spend at most four resource types.

Implement government, opposition, Event 006 emergency, neighbor, settlement, and reconstruction phases. Every meaningful action needs AI and cleanup.

## Event 006 contract

Event 021 may initialize a complete human Event 006 package even when Independence Wave never fired.

Reuse:

- registered carrier
- identity
- leader and portrait
- flags
- focus tree
- politics
- ideas
- starting forces
- reinforcement
- formation and formable decisions
- recognition
- AI
- assets
- documentation

Record Event 021 origin.

Do not:

- mark Event 006 fired
- change its repeatable weight or cap
- advance its evolution history
- duplicate a living tag or character
- create an incomplete package
- create an actual nonhuman package
- auto-enroll the actor in Event 006 congress or league
- replace missing assets

Human Event 006 countries remain eligible for later Event 021 crises after their grace period.

Use `is_actual_nonhuman_country` for universal immunity. Do not use `is_special_chaos_country` as the blanket exclusion.

## Evolution I

At Gathering Storm:

- support active-war and prefire entry
- create multi-front wars when territory and actor capacity are viable
- allow majors at lower weight
- make complete Event 006 packages regular opposition actors
- plan all front regions before commitment
- give fronts distinct goals, strength, relations, and settlements
- keep remaining fronts active after one is defeated

A small country can remain two-sided when a third side would be broken.

## Evolution II

At Rising Chaos:

- create Regional Exposure for valid neighbors
- separate relief from armed support
- add border, sponsor, recognition, mediation, and containment decisions
- strengthen active sides through control, administration, depots, recruitment, and support
- allow more unusual researched Event 006 packages
- add rare uncertain strange incidents

Strange incidents must be bounded, counterable, limited to one active incident per side, and distinct from other events. Do not attach occult claims to a real religion or community.

## Evolution III

At Chaos Tier:

- activate Global Fracture
- register Event 021 as a shared world-threat source
- classify every eligible normal human country as Stable, Exposed, Fractured, or Critical
- process only due countries through a bounded scheduler
- use a Critical queue
- enforce tested theater caps
- support nested crises
- use successor grace and recurrence memory
- cap descendant generations
- keep normal event firing active
- remain nonterminal

Clear the world-threat source when the global system is no longer active.

Totalen Chaos and World Collapse scale Evolution III without creating extra evolution records.

## Cluster

Integrate with Event 004 and Event 007 in the Wars cluster.

Reserve targets before commitment.

Keep event identities separate.

At lower cluster intensity, prefer separate countries. At higher intensity, allow coherent external-war and internal-war overlap.

Log exact skip reasons.

The cluster counts as one pacing event.

## Triggerable scenario

Add the manual scenario with a verified free ID. Do not assume `SCN-014` without checking the live registry.

Working title: The Fracture Cascade.

Types:

- Political Fracture
- Independence Cascade
- Command Collapse
- Universal Fragmentation

Intensities:

- Low, about 10 percent
- Medium, about 25 percent
- High, about 50 percent
- Maximum, every eligible normal human country

Manual launch bypasses normal chaos, date, prior-fire, evolution, and cooldown gates only during setup.

Clear the bypass after setup.

Immediate setup is preferred. A deterministic launch over no more than seven in-game days is allowed only when measured one-frame setup causes a reproducible engine stall. Lock all targets and choices at confirmation.

## AI

Implement role-specific AI for:

- consolidator government
- hardliner government
- negotiator government
- revolutionary claimant
- constitutional claimant
- independence side
- command claimant
- opportunistic sponsor
- containment neighbor
- neutral mediator
- survivalist successor

AI evaluates strength, State Authority, capital, supply, equipment, manpower, ideology, territory, sponsors, external wars, settlement quality, package identity, and generation.

Invalid routes and actions receive zero weight.

Route every weighted surface through `chaosx_ai_probability_auditor` before patching, then run `hoi4.probability_compare` after the change using the same named scenarios.

## Presentation and assets

Implement the authorized static asset inventory from the asset prompt.

Do not add:

- generic claimant flags
- generic claimant portraits
- animated category art
- custom GUI
- super-event
- 3D asset

Event 006 retains ownership of its country assets.

Implement all six achievements with full tracking, disqualifiers, localisation, icon triplets, documentation, and tests.

## Logs and documentation

Complete:

- event registration
- visible and debug names
- default actor
- history row
- Event Details
- three evolution details
- evolution logs
- cluster row and reasons
- scenario row
- no-target `N/A`
- event documentation
- helper documentation
- dynamic trigger or effect documentation
- Wars cluster documentation
- scenario documentation
- source-of-truth and plan disposition
- achievement documentation
- permanent asset provenance and runtime crosswalk

After final player-facing wording exists, use `chaosx_spreadsheet_doc_worker` to edit only `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, then run `python .tools/export_event_catalog_csv.py`.

Never edit the CSV exports directly.

## MCP and audits

Use:

- event inspect, render, and compare
- probability inspect, evaluate, sweep, simulate, render, and compare as defined by the matrix
- focus inspect and render only when focus files or loading change
- GUI inspect and render only for existing category presentation that actually needs layout review
- map inspect only when state-allocation helpers touch supported map surfaces

Run the acceptance and performance scenarios in Part 10.

Near completion:

- run the decision and mission auditor
- run the country package auditor
- run the localisation auditor
- run the focus auditor only if focus files changed
- run the documentation curator
- run one improvement-loop pass
- implement, promote, queue with reason, or reject its result
- run the event completion auditor

Do not claim completion while any required event path, actor, AI behavior, settlement, cleanup, asset, achievement, log, documentation surface, workbook field, probability comparison, performance check, or accepted plan remains missing.

Report every simplification, omission, blocker, placeholder, or unapproved fallback. If none exist, say so and provide concrete completion evidence.
