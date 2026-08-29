# Full Implementation Prompt for Event 22 Concentration Camps

## Goal

Implement the complete Event 22 rework in the Chaos Redux repository.

Event ID `22` becomes `Concentration Camps`, a Minor Repeatable member of the accepted `Random Chaos` cluster. A normal first firing selects one eligible country and establishes concentration camps in 20 percent of its eligible states. The affected country manages closure, restrictive review, forced labour, security expansion, concealment, evolved extermination, retreat, liberation, relief, evidence, and accountability.

Use the existing Camps and Genocide framework. Do not create a second camp, deaths, evidence, condemnation, chemical, famine, migration, or event-log system.

## Required preflight

Before editing, fully read:

- repository `AGENTS.md`
- every applicable skill file
- Event 22 index and all supporting specification files
- all existing Event 22 source, plans, and handoffs
- Camps and Genocide implementation and docs
- Deaths, Chaos Meter, Condemnation, chemical, biological, contamination, occupation, resistance, disaster, plague, civil-war, famine, migration, event-log, and event-details APIs
- German, Japanese, and Soviet camp packages
- authoritative event catalog workbook and cluster implementation
- offline Paradox wiki and installed vanilla precedents for every syntax or UI surface touched

Do not edit before the source map and dependency order are understood.

Preserve unrelated working-tree changes. Do not use destructive Git reset, checkout, clean, or broad revert commands.

## Specification package

Treat these as the accepted source design:

```text
022_concentration_camps_index.md
022_concentration_camps_spec_part_1_core.md
022_concentration_camps_spec_part_2_baseline_and_decisions.md
022_concentration_camps_spec_part_3_evolutions_and_variants.md
022_concentration_camps_spec_part_4_discovery_liberation_aftermath.md
022_concentration_camps_spec_part_5_integrations_balance_presentation.md
022_concentration_camps_event_chain_map.md
022_concentration_camps_decision_map.md
022_concentration_camps_ai_probability_matrix.md
022_concentration_camps_achievements.md
022_concentration_camps_asset_manifest.md
022_concentration_camps_research_notes.md
022_concentration_camps_catalog_handoff.md
022_concentration_camps_acceptance_criteria.md
```

Copy or install the accepted package under:

```text
docs/specs/022_concentration_camps_specs/
```

Use:

```text
docs/plans/022_concentration_camps_plans/
```

for implementation plans, audits, and handoffs.

## Initial repository exploration

If exact file locations or ownership remain unclear, spawn `chaosx_repo_explorer` once with `fork_context=false`.

Its bounded task is to map:

- old Event 22 files and keys
- event registration and weight files
- camp buildings and state registration
- current genocide decisions and country adapters
- public Deaths and exact-population helpers
- evidence and Condemnation sources
- current pulse and delayed-job patterns
- event log and detail registration
- catalog workbook and exporter
- assets and localisation families
- validation commands

The explorer is read-only. Review its handoff before coding.

## Core ownership

Event 22 owns:

- global country selection
- first-opening coverage
- repeat-incident selection
- network generation
- three player-facing values
- baseline policy and decision lifecycle
- evolution entry jobs
- Event 22 state and country adapters
- discovery, liberation, relief, and aftermath orchestration
- Event 22 history and details

Shared systems own:

- camp building definitions
- original and later responsibility attribution
- exact civilian-population removal
- Deaths ledger and Chaos conversion
- hidden atrocity and cover-up evidence
- public Condemnation thresholds and sanctions
- chemical and biological technology, stockpile, contamination, and outbreak
- natural-disaster damage
- famine state and general famine deaths
- actual migration transfers when API exists
- country-specific camp content
- shared event log and details framework

## Targeting and legal boundary

Do not create a race or ethnicity map.

Valid target-purpose order:

1. researched country-specific protected-group registry
2. occupied or non-core civilians
3. existing refugee, minority, displaced-person, or migration marker
4. resistance-linked detainees and hostages
5. political, ideological, religious, or social enemies defined by the regime
6. broad domestic purge after earlier sources are exhausted

Use `genocide` only when a qualifying protected group and specific destructive intent are both proven. Otherwise use accurate terms such as mass detention, forced labour, persecution, extermination, mass killing, or crimes against humanity.

Exclude lawful POW camps, lawful civilian internment, humane time-limited quarantine, and ordinary prisons.

## Implementation dependency order

### Phase 1: identifiers, constants, and public helpers

- remove or migrate old Spain-specific Event 22 identifiers
- register the event through the standard Minor Repeatable weight, recovery, cap-reduction, and cluster-pacing contract
- define Event 22 constants, enums, state flags, country flags, variables, and Deaths reasons
- define network generation and per-state Evolution II and III shock markers
- add event-owned registration and cleanup helpers
- add adapters to existing responsibility, evidence, Condemnation, and exact-population APIs
- centralize all important tuning values
- document every public helper contract

Use `chaosx_scripted_system_architect` for reusable helper work after the parent maps the exact scope. The subagent can patch narrow shared effects, triggers, constants, and call sites. It must write a handoff.

### Phase 2: global event and baseline setup

Implement country and state candidate pools with hard exclusions.

First ordinary firing:

- calculate eligible states
- target 20 percent, rounded upward
- count existing compatible active or quiet sites
- create only the missing concentration camps
- store responsible actor and network generation
- initialize finite detained capacity from a valid source
- batch large networks through safe delayed jobs
- open one policy event
- register Event 22 in history and details

Repeat firing:

- prefer never-fired countries
- use same-country cooldown and resolution protection
- active network receives a valid incident, not another automatic 20 percent batch
- no valid incident means no filler popup

### Phase 3: three visible values

Implement bounded:

- Network Reach
- Exposure
- Resistance Pressure

Show bands and next threshold. Keep internal evidence, mortality, workforce, transport, disease, and guard components hidden or summarized.

Do not duplicate shared Condemnation.

### Phase 4: baseline decision and mission loop

Implement both ordinary categories and every accepted decision or mission from the decision map.

Requirements:

- three to five visible primary actions in normal phases
- hard maximum six
- one to three active missions
- at most four spendable cost types per action
- dynamic cost scaling
- icon-first cost localisation
- state targeting with exact blocked reasons
- phase replacement and cleanup
- no dedicated scripted GUI

Country-specific German, Japanese, and Soviet packages replace generic duplicates through adapters.

After first complete pass, spawn `chaosx_decision_mission_auditor` with `fork_context=false`. Allow local safe patches. Review its handoff.

### Phase 5: ongoing mortality and workforce

Use finite detained capacity.

Every death:

- calculates a requested person count
- calls `apply_exact_state_civilian_population_loss` or its current public successor
- uses the actual applied amount
- logs one cause-specific Event 22 Deaths reason
- reduces detained capacity by the applied amount
- reconciles recruitable manpower only through the shared helper
- creates evidence and pressure

Release, escape, transfer, and migration reduce detained capacity without deaths.

Do not run a whole-world daily or weekly scan. Pulse only registered countries and states with distributed timing.

### Phase 6: Evolution I

Support active and pre-fire entry.

Active entry:

- count valid active concentration sites
- exclude closing, liberated, destroyed, or noncontinuing sites
- convert `floor(valid_site_count / 2)` sites, leaving the odd extra as concentration
- one moderate single-site network opens a crisis decision instead of forced conversion
- preserve responsibility, generation, evidence, workforce, and shock markers
- remove forced-labour assignment

Pre-fire entry:

- 20 percent total coverage
- roughly half concentration and half extermination sites
- concentration receives odd extra unless explicit extermination-dominant route

Implement target purpose, extermination intensity, halt operation, later selected conversion, broad domestic purge, and restricted chemical adapter.

Extermination sites do not receive the strong production assignments.

Restricted chemical site:

- requires accepted technology and project gates
- consumes real stockpile each pulse
- stops when debit fails
- causes exact deaths, contamination, accident risk, evidence, and discovery
- is explicitly alternate history in documentation and localisation
- contains no technical instructions

### Phase 7: Evolution II

For every active camp state:

- calculate 1 percent of current state civilian population
- clamp through shared protected floor
- apply exact loss
- log actual loss
- set one per-state, per-generation marker

New sites after Evolution II receive the shock once.

Conversion, control change, repeat event, save, and reload must not repeat it.

### Phase 8: Evolution III

- rebuild eligible state pool
- raise total active coverage to 50 percent
- split final target roughly evenly between concentration and extermination
- do not downgrade extermination sites
- use Soviet adapter for gulags
- active network receives additional exact 2 percent loss in every active camp state
- pre-fire Evolution III opening receives only the 2 percent shock, not the 1 percent shock
- new Evolution III sites receive only the 2 percent shock

Batch safely and revalidate every job.

### Phase 9: discovery, liberation, and aftermath

Implement state and country evidence with source families and confidence.

Discovery routes include:

- liberation or hostile occupation
- survivors and escapees
- foreign intelligence
- inspection
- resistance capture
- natural disaster
- bombing and front movement
- regime change and archives

Add one unique public Condemnation source per actor, state, source family, and generation. Add one bounded network-verification source. Do not duplicate sanctions.

On liberation by a noncontinuing controller:

- stop operation immediately
- remove former bonuses
- preserve original responsibility
- calculate survivors, disease, contamination, records, and evacuation status
- open security, relief, registration, evidence, accommodation, decontamination, and dismantlement actions
- create a new responsibility generation only if the controller reuses the site

Implement displaced-person, safe return, resettlement, tribunal, accountability, restitution, and state-recovery handoffs.

### Phase 10: cross-system adapters

Implement bounded adapters for:

- Event 5 Soviet Collapse
- Event 6 Independence Wave
- Event 13 Natural Disasters
- Event 16 experiment and Mengele content
- Event 20 Black Plague
- Event 21 Random Civil War
- Event 31 Random Terror
- chemical and biological systems
- occupation, resistance, and garrisons
- famine
- migration
- air cleanliness

Each adapter preserves cause ownership and prevents double counting.

### Phase 11: AI and probability

Implement the seven accepted AI profiles and all hard blockers.

Use the full scenario matrix.

Run `chaosx_ai_probability_auditor` after weighted surfaces exist and again after any weight patch. It is read-only. Parent applies changes.

Required MCP evidence:

- inspect
- evaluate
- sweep
- sequence
- compare
- simulate only where exact reconstruction is unavailable

No invalid extermination, assignment, transfer, expansion, chemical, or relief action may have nonzero probability.

### Phase 12: localisation

Write all event, decision, mission, category, idea, modifier, achievement, tooltip, history, detail, and evolution keys.

Use accurate site names and campaign-specific target purpose. Avoid graphic detail, invented quotations, jokes, procedural killing descriptions, and unsupported racial demographics.

Route final pass to `chaosx_localisation_auditor`. Allow local safe fixes and review the handoff.

### Phase 13: assets

Run the bounded asset prompt.

Use archival source research for real event, news, and category pictures. Use ImageGen symbolic art for icons and achievements. Do not generate victim photographs.

Produce only the assets enumerated in the accepted asset manifest.

Parent performs final GFX wiring and runtime review.

### Phase 14: achievements

Implement the accepted achievement suite from its prompt and proof contracts.

No achievement rewards perpetrator output, killing, concealment, chemical use, or network size.

### Phase 15: catalog and documentation

- replace Event 22 workbook row
- set Minor Repeatable
- resolve or register Random Chaos with a collision-free numeric ID
- set Severe member status
- populate three evolutions
- regenerate CSV exports through repository exporter
- update Camps and Genocide, Deaths, Condemnation, integration, and Event 22 docs
- do not edit CSV exports directly

Use `chaosx_spreadsheet_doc_worker` for the workbook task.

### Phase 16: completion audit and improvement pass

Run `chaosx_event_completion_auditor` read-only against the accepted specs and final source.

Resolve every missing accepted mechanic, fallback, simplification, stale document, asset gap, localisation gap, probability gap, or validation gap.

Run `chaosx_improvement_loop_planner` only after the accepted implementation is complete or when the parent explicitly places remaining work into a named addendum. Do not let the improvement loop replace missing baseline work.

## Performance and safety rules

- registered actors and states only
- no whole-world daily or weekly scan
- delayed jobs have actor, state, generation, reason, and revalidation
- invalid jobs fail closed
- no silent target substitution
- no duplicate percentage shocks
- no duplicate Condemnation source
- no free workforce generation
- no site bonus after closure or liberation
- no building deletion that clears evidence
- no annexation or puppet responsibility laundering
- no direct Chaos gain for deaths already handled by Deaths system
- no double count between camp, famine, disease, migration, disaster, bombing, or nuclear causes

## Multiplayer rules

- secret evidence only to valid observers
- public discovery to valid countries
- per-country target selection
- no global human-choice variable
- tag switch preserves network without reinitialization
- civil-war sides receive correct sites and responsibility
- save and reload works for host and client

## Validation

Run repository validation after each logical batch.

Required final tests:

- baseline small country
- baseline forced-labour country with every assignment
- active Evolution I
- Evolution II exact loss
- pre-fire Evolution III
- active Evolution III after Evolution II
- discovery and Condemnation
- liberation and relief
- retreat variants
- civil war and successor
- chemical site
- famine and disease cause accounting
- save and reload during delayed jobs
- multiplayer information and targets
- old Spain-specific key and file search
- fresh error-log delta

Use dedicated live-QA saves and the project testing folder structure. Do not use Force Trigger Mode to prove normal eligibility or probabilities.

## Completion report

Return:

- full changed-file list
- new and removed identifiers
- helper contracts
- event, decision, mission, evolution, discovery, liberation, and integration status
- population and Deaths evidence
- AI probability artifacts
- asset and GFX handoffs
- localisation audit
- achievement status
- workbook and CSV status
- validation commands and results
- live-QA saves, screenshots, logs, and findings
- subagent handoffs
- remaining blockers

Do not claim complete when an accepted system exists only in documentation, when a fallback substitutes missing content, when weighted logic lacks final evidence, when a required asset or localisation key is missing, or when live save and reload have not been tested.
