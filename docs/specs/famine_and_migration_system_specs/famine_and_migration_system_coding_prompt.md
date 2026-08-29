# Coding Prompt: Implement the Famine and Migration Mechanics

> **Current design clarification (2026-08-25):** The user clarification and accepted split implementation supersede any shared mechanic, category, or runtime-namespace wording retained below as historical design context. The current implementation uses independent `famine_*` and `migration_*` mechanics, `famine_decision_category` and `migration_decision_category`, and `famine_state_map_mode` and `migration_state_map_mode`; no combined mechanic, category, runtime namespace, or mapmode is current. Use [source_of_truth_map.md](../../plans/famine_and_migration_system_plans/source_of_truth_map.md) and [completion_report.md](../../plans/famine_and_migration_system_plans/completion_report.md) for current status, including the incomplete blockers.

Implement the separate Chaos Redux famine and migration mechanics to the fullest extent described in `docs/specs/famine_and_migration_system_specs/`, connecting them only through explicit causal adapters and neutral conservation primitives.

This is not an event. Do not assign it a random-event ID, add it to an event category array, or make its state pulses count as random event pacing.

## Required source design

Read every file in the spec folder, including:

- the eight specification parts
- the historical profile matrix
- the integration matrix
- the death-reason ownership matrix
- the probability scenario matrix
- the decision map
- the asset matrix
- the research bibliography
- the asset prompt
- the decision and mission prompt
- the achievement prompt
- the subagent routing and context-complete subagent prompts

Treat mapped content as acceptance criteria. Do not silently replace the system with flat modifiers, fixed population losses, generic refugee variables, or event-only approximations.

## Mandatory project and engine reading

Before editing:

- read `AGENTS.md`
- read the complete `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-subagents`, and `chaos-redux-improvement-loop` skills
- read `chaos-redux-frame-animation` if any later accepted visual state needs motion
- consult the required offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, occupation, state population, scripted GUI, and interface behavior relevant to the final implementation
- read all applicable vanilla documentation under the installed Hearts of Iron IV documentation folder
- inspect vanilla precedents for state modifiers, state population changes, occupation laws, evacuations, decision categories, selected-state decisions, refugee or exile behavior, and positive state population effects
- inspect existing Chaos Redux Deaths, Air Cleanliness, Condemnation, camps and genocide, occupation, outbreak, bombing, nuclear, natural-disaster, event-log, dynamic-effect, and dynamic-trigger implementations
- use the installed HOI4 MCP routes for every supported event, weighted-logic, GUI, and map surface

If a required local reference or MCP route is unavailable, record the exact blocker. Do not treat memory or source-only inspection as equivalent proof.

## Repository exploration and architecture

Spawn `chaosx_repo_explorer` with `fork_context=false` using the supplied prompt before editing because this is a broad cross-system change.

Then spawn `chaosx_scripted_system_architect` with `fork_context=false` using the supplied prompt. The architect should design and, where allowed, implement reusable shared contracts for:

- active-state and active-country registries
- famine pressure requests
- flight-pressure requests
- exact population transfer
- route resolution
- death-reason ownership
- border policy
- reception capacity
- return and integration
- adapter validation
- script constants and tuning tables

The parent remains responsible for integration and final review.

## Performance contract

Do not add a whole-world `on_daily`, `on_weekly`, `on_monthly`, or equivalent recurring scan.

Use:

- scoped hooks
- event-driven requests
- active state and country registries
- bounded scheduled jobs
- cleanup when the state, country, route, or cohort resolves

Relevant hooks include control changes, occupation-law changes, bombing aftermath, nuclear aftermath, outbreak changes, camp and gulag actions, disaster aftermath, event adapters, war and peace transitions, relief decisions, border policy changes, and return completion.

## Famine system

Implement state food security with hidden continuous pressure and visible stages:

- supply strain
- acute shortage
- famine
- catastrophic famine

A state with no material pressure has no famine modifier.

Model named pressure components:

- local production loss
- import and transport loss
- extraction and policy harm
- population need
- environmental pressure
- vulnerability
- governance failure
- relief and protection

Use centralized script constants. Keep important tuning out of scattered magic numbers.

Famine and catastrophic famine must cause recurring, significant, population-scaled civilian deaths when unmanaged.

Use the existing exact state civilian population-loss API. Add the Deaths reason `famine` with player-facing `From famine` text. Record exactly the applied loss once.

Do not use a fixed historical death total. Do not keep killing until a target total is reached.

Implement gradual recovery. One relief action can stop worsening or reduce a stage, but it should not erase months of damage instantly.

## Island blockade and siege proof

Implement the full proof contract for island or isolated-state blockade pressure.

Require actual evidence for:

- island, archipelago, enclave, or no safe land route
- active war
- maritime dependence
- port or route disruption
- convoy, fuel, escort, or access deficit
- insufficient local production and reserves
- no functioning humanitarian corridor

A generic war or hostile ship is insufficient.

Implement siege and encirclement pressure from actual supply, control, route, population, winter, bombing, and duration conditions.

## Air Cleanliness integration

Read the existing Air Cleanliness value and thresholds.

Use it to modify active food-security pressure and recovery:

- 25 percent increases spread and slows recovery
- 50 percent enables mild nuclear-winter food pressure
- 75 percent enables severe pressure
- 100 percent requires exceptional protection, supply, technology, or evacuation to avoid continued decline

Do not apply a flat global famine-death tick.

Famine does not reduce Air Cleanliness by itself.

## Population movement

Implement movement as exact population transfer between real states.

Each cohort record must include origin, destination, cause, route, cohort type when needed, requested amount, actual origin debit, route deaths, actual arrival, responsible actor, and durable status.

Implement a reusable exact transfer adapter after local engine inspection. It must:

- validate origin and destination
- protect the origin floor
- debit origin population without logging movement as death
- reconcile recruitable-manpower side effects
- register route deaths separately
- add only surviving actual population to the destination
- reconcile destination manpower side effects
- preserve origin and destination history
- fail closed when any required proof is invalid

Do not duplicate population. Do not delete people by closing a border or decision category.

Implement:

- internal displacement
- cross-border refugee flight
- organized evacuation
- spontaneous exodus
- deportation and forced relocation
- camp and prison transfer
- voluntary return
- local integration
- third-country resettlement
- prolonged displacement

## Flight and destination logic

Build flight pressure from actual conditions:

- losing a local war or front collapse
- bombing
- nuclear blast aftermath and fallout
- camps, genocide, repression, and forced labor
- famine
- outbreaks and quarantine
- occupation
- natural disasters
- state collapse
- ideology and expected treatment

Separate desire to leave, ability to leave, and destination availability.

Ideology is one bounded factor. Direct persecution, bombing, camps, famine, occupation behavior, and route safety can override it.

Prefer a safe internal destination when valid. Then evaluate foreign destinations through route safety, border policy, capacity, relations, ties, ideology, current danger, and forced-return risk.

Use complete weighted pools with invalid candidates at zero.

## Border and reception system

Implement country border policy states:

- open humanitarian entry
- controlled entry
- transit only
- emergency quarantine entry
- closed border
- violent enforcement when compatible policy exists
- forced return as a separate action

Closed borders create trapped populations. They do not erase the cohort.

Implement reception capacity from food, shelter, infrastructure, transport, medical capacity, administration, safe states, current load, war, outbreak, and contamination.

Implement destination state modifiers for reception, overcrowding, transit, and return.

Implement origin state modifiers for exodus, evacuation, depopulation, and return readiness.

Do not grant immediate full recruitable manpower from arrivals. Recruitment requires accepted legal integration, exile formations, volunteer decisions, or another explicit route.

## Death-source expansion

Add and document exact Deaths reasons for:

- famine
- occupation repression
- forced labor
- forced displacement

Consider a separate border-closure reason only if the current Deaths UI and reason capacity benefit from it. Prefer the proximate physical cause when possible.

Use `famine_and_migration_system_death_reason_ownership.csv` as the mixed-cause contract.

One physical death has one owner.

Movement debits are not deaths. Route deaths are separate.

## Occupation, camps, gulags, and genocide

Audit all real occupation laws and map relevant ones to shared profiles such as protective administration, limited requisition, harsh extraction, forced labor, collective punishment, population transfer, and exterminatory policy.

Use scoped law and control hooks.

Connect the existing camps and genocide system through:

- food deprivation
- forced labor mortality
- deportation and transfer
- nearby flight pressure
- escapee reception
- liberation and survivor recovery
- return and family reunification
- hidden and public evidence

Integrate Soviet grain extraction, gulags, deportation, movement restriction, and concealment with Event 5.

Use the physical death reason while the occupation or camp system records responsibility, evidence, condemnation, sanctions, and tribunal pressure.

## Decision and presentation layer

Implement the separate famine and migration decision-category lifecycles from Parts 1 and 6.

`famine_register_initial_incident` and `migration_register_initial_incident` are accounting and presentation seams only and must not create event objects, event IDs, event-pool entries, event-log rows, random events, or pacing pulses. The deleted incident event files and constants are deliberate.

Implement all supported rows in `famine_and_migration_system_decision_map.csv`.

Follow the separate decision prompt for costs, clutter, state selection, missions, tooltips, and AI.

Do not create a full shared scripted GUI. Use state modifiers, report events, decision category presentation, concise dynamic localisation, and map highlights. A compact attached header is allowed only if local inspection proves it is needed and cleaner than ordinary category text.

## AI and probability

Spawn `chaosx_ai_probability_auditor` with `fork_context=false` before changing weighted surfaces. Establish named baseline scenarios from the supplied probability matrix.

Let the parent or owning patch agent implement the chosen design.

Run the auditor again with `hoi4.probability_compare` against the same scenarios.

Audit:

- famine response choices
- concealment and extraction
- destination selection
- border policy
- outbreak reception
- corridor acceptance
- return and integration
- opposition movement selection
- relief donor and requisition donor pools
- registry and flow sequence behavior where a complete sequence manifest can be declared

Distinguish exact, bounded, sampled, score-only, and unresolved evidence.

## Historical profiles

Implement the profiles in Part 5 and the historical-profile matrix as dynamic cause profiles.

Use local map, state, country, date, control, route, and ideology evidence.

Do not use fixed death totals.

Treat pre-1936 cases as memory and vulnerability unless an earlier scenario exists.

Treat later cases as policy analogues where specified.

Preserve research cautions and multi-causal framing.

## Event and scenario adapters

Implement the accepted connections in the integration matrix.

Prioritize current implemented systems and events. Do not implement unreworked catalog ideas as complete events merely to create an adapter.

Required deep connections include Event 5, Event 6, Event 13, Event 14, Event 15, Event 20, Event 21, Event 28, Event 33, Event 50, Event 95, Event 118, Event 120, and Event 149 compatibility.

Retire, disable, or convert Event 149 `Immigrations` so it no longer applies a competing flat population drain.

Cluster consequences must not count as extra pacing events.

## Special-country exclusions

Use the shared `is_special_chaos_country` and `is_actual_nonhuman_country` classifiers.

Ordinary civilian origin and destination logic should fail closed for nonhuman or special actors without a documented human civilian population transition.

Special actors can remain causes of human flight.

## Assets

Follow `famine_and_migration_system_asset_prompt.md` and the asset matrix.

Use the correct asset subagent split:

- `chaosx_icon_artist` for icons and any supported texticons
- `chaosx_asset_source_researcher` for archival images that must show real historical material
- `chaosx_generated_event_art` for generic period-authentic dynamic report images

Do not create portraits, 3D models, custom units, or super-events for this system.

Every accepted asset needs source evidence, processed PNG, DDS, path, sprite, consumer, manifest, and permanent handoff facts.

## Achievements

Implement every achievement in `famine_and_migration_system_achievement_prompt.md` unless local engine or registry evidence creates a documented blocker.

Use the single root achievement registry, complete tracking, disqualifiers, localisation, triplet icons, docs, and exploit guards.

## Localisation

Spawn `chaosx_localisation_auditor` with `fork_context=false` after broad visible text exists.

Write final text from the direction in the specs.

Keep famine and atrocity text serious. Do not use staccato writing, em dashes, semicolons, generic dramatic filler, or dialectical contrast templates.

Use dynamic state, country, route, amount, and policy names.

Do not expose hidden weights, evidence, future outcomes, or raw variables.

Do not describe refugees as inherently diseased.

## Documentation and catalog

Create or update permanent system documentation under `docs/systems/`.

Update:

- Deaths reason docs
- Air Cleanliness docs
- Condemnation docs
- camps and genocide docs
- occupation docs
- dynamic effect and trigger registries for public contracts
- affected event docs
- scenario docs where seeded behavior changes
- event catalog workbook rows after implementation facts are known

Use `chaosx_documentation_curator` for documentation reconciliation.

Use `chaosx_spreadsheet_doc_worker` only for the authoritative workbook. Then run the repository CSV exporter. Do not edit export CSVs directly.

## Audits

After implementation:

- run `chaosx_decision_mission_auditor`
- run `chaosx_localisation_auditor`
- run `chaosx_ai_probability_auditor` compare pass
- run `chaosx_event_completion_auditor` as a shared-system completion audit
- use country and focus auditors only for bounded downstream content that this implementation actually changes

Near completion, spawn `chaosx_improvement_loop_planner` with `fork_context=false` using the supplied prompt. Fold accepted design into the specs or implementation. If it returns a closure handoff, complete the remaining small tasks before final audit.

## Validation

Use the mixed-cause and acceptance scenarios in Part 8.

Validate:

- exact population conservation
- no double deaths
- save and reload
- annexation and control change
- route loss
- invalid destination
- border-policy transition
- famine recovery and relapse
- Air Cleanliness thresholds
- event adapters
- historical profiles
- AI choice ordering
- decision clutter and costs
- achievement disqualifiers
- asset consumers
- docs and catalog alignment

Do not run HOI4 through normal coding agents. Live in-game testing belongs to the user unless the user explicitly invokes the autonomous debug-playtest skill.

## Completion report

Do not claim completion until every accepted requirement is implemented and reviewed.

The completion report must list:

- files changed
- shared helpers and registries
- Deaths reasons
- famine stages and formulas
- population-transfer proof
- decision and event coverage
- AI and probability evidence
- occupation and camp connections
- event adapter coverage
- historical-profile coverage
- assets
- achievements
- localisation
- docs and workbook alignment
- task-specific validation scenarios
- every simplification, omission, fallback, blocker, or unresolved plan

If there are no simplifications, say so and support the claim with the audits and coverage records.
