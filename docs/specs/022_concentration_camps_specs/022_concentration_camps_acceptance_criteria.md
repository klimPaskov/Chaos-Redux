# Event 22 Concentration Camps Acceptance Criteria

## Completion meaning

Event 22 is complete only when the implemented event, shared-system adapters, decisions, population accounting, evolutions, AI, discovery, liberation, aftermath, assets, localisation, documentation, catalog, and live tests agree with this specification.

A popup plus state buildings is not a complete implementation.

## Source preflight

Before editing:

- read repository `AGENTS.md`
- read current Event 22 implementation and every related plan or handoff
- read the full Camps and Genocide system source and documentation
- read the Deaths and Condemnation public APIs
- read event, decision, localisation, asset, and spreadsheet skills
- read offline Paradox wiki pages for events, decisions, triggers, effects, modifiers, scopes, buildings, on-actions, and localisation
- inspect installed vanilla event, decision, state-building, occupation, resistance, and news patterns
- inspect current country-specific German, Japanese, and Soviet camp packages
- inspect current Event 13, Event 16, Event 20, Event 21, chemical, biological, famine, migration, and event-log integration surfaces
- inspect current event catalog workbook and Random Chaos cluster registry

Do not rely on this planning package for engine syntax.

## Source-of-truth placement

Accepted specs belong under:

```text
docs/specs/022_concentration_camps_specs/
```

Plans, improvement addenda, audit reports, and subagent handoffs belong under:

```text
docs/plans/022_concentration_camps_plans/
```

Temporary assets belong under:

```text
docs/assets/022_concentration_camps/
```

Do not create another planning-folder convention.

## Event identity

Pass conditions:

- Event ID remains `22`
- event name is `Concentration Camps`
- old Spain-specific content is removed or migrated with no orphan references
- event type is Minor Repeatable
- cluster is Random Chaos with a valid registered numeric ID
- member severity is Severe
- baseline and all three evolutions appear in the shared event details
- event respects per-country and global event enable settings
- initial weight, post-fire reset, monthly recovery, and cap reduction use the shared Minor Repeatable contract
- no private Event 22 weight loop duplicates shared pacing
- a cluster firing applies the member firing and cap change once
- manual trigger and Force Trigger Mode behave according to shared framework rules

## Global country selection

Pass conditions:

- only eligible normal countries enter the pool
- `is_special_chaos_country` actors are excluded
- countries without eligible states are excluded
- recent transparent closure protection gives zero chance
- never-fired countries are normally preferred
- active countries receive incidents instead of another automatic 20 percent opening
- country-specific packages are selected through adapters
- selection has MCP probability evidence
- no invalid country is silently replaced after selection without a logged reason

## Eligible-state selection

Pass conditions:

- eligibility uses current ownership, control, population, transport, protection, and state conditions
- state selection does not infer ethnicity
- one state cannot hold more than one primary camp type
- existing compatible active or quiet sites count correctly
- the capital is protected at baseline except for the documented small-country exception
- recently liberated relief states are excluded
- states at the protected population floor are handled safely
- state targets are unique within one setup job
- delayed jobs revalidate state and actor before execution
- no fallback state outside the accepted pool is selected silently

## Baseline opening

Pass conditions:

- first ordinary firing brings active concentration-camp coverage to 20 percent of eligible states
- count rounds upward and gives a valid small country at least one site
- baseline creates concentration camps only unless an evolution is already active
- every site receives responsibility actor and network generation
- large setup can batch safely without changing final count
- affected player receives an opening choice
- AI selects a valid opening policy
- management category initializes once
- initial detained capacity is finite and linked to a valid campaign source
- no death percentage shock occurs at pure baseline

## Repeat behavior

Pass conditions:

- event remains globally repeatable
- same active country does not receive another automatic 20 percent batch
- valid repeat incidents are context-sensitive
- no-threshold situation produces no filler incident
- cooldown scales with active network and resolution
- transparent closure gives the longest protection
- secret demolition remains eligible for later discovery
- repeat incidents do not duplicate history, decisions, buildings, or network generations

## Baseline decision loop

Pass conditions:

- opening supports closure, restrictive review, forced labour, and security expansion
- Evolution I adds extermination only when valid
- visible actions stay within the six-action hard cap
- active missions stay within one to three
- each decision has no more than four spendable cost types
- costs scale dynamically and display matching texticons
- state-targeted actions explain state, role, cost, and blocked reason
- earlier actions disappear when replaced
- country-specific packages hide generic duplicates
- all important decisions have AI behavior and cleanup
- decision category does not operate as a political-power store

## Closure path

Pass conditions:

- intake can be frozen
- labour assignments wind down
- food and medicine lower ongoing mortality
- detainees and survivors can be registered
- records can be preserved
- safe release, return, or transfer exists
- closure scales by site count and condition
- regional closure replaces state clutter for large networks
- all active death pulses stop after complete closure
- camp buildings are removed only after valid state transition
- evidence and responsibility persist
- transparent closure starts refire protection
- underground continuation is detected and resolved

## Restrictive review path

Pass conditions:

- expansion and harsh assignments pause
- inspections, registration, ration, and quota reduction work
- real access can expose evidence
- staged access is treated as concealment and can fail
- review can move toward closure or renewed exploitation
- local noncompliance can create an underground-network mission
- review does not erase deaths or responsibility

## Forced-labour path

Pass conditions:

- industrial assignment requires meaningful factories
- construction assignment requires meaningful construction or repair work
- extraction assignment requires a relevant resource role
- logistics assignment requires a rail, port, depot, or supply role
- one state runs one assignment at a time
- assignment strength depends on workforce, guards, supply, transport, and pressure
- detained workforce is finite
- deaths reduce both workforce and state population
- release, escape, transfer, and liberation reduce workforce without deaths
- depleted sites lose output
- new intake requires valid source and transfer
- national assignment cap prevents unlimited stacking
- extermination conversion removes the assignment

## Security expansion path

Pass conditions:

- expansion targets only eligible uncovered states
- generic baseline expansion respects the accepted reach ceiling
- costs include real construction, transport, guard, or equipment burden
- responsibility and generation are recorded
- detained capacity has a valid source
- Network Reach, Exposure, and Resistance Pressure rise
- a site cannot be expanded into a protected relief state
- repeated event firing cannot bypass the expansion cap

## Target-purpose system

Pass conditions:

- no generic race or ethnicity percentages are created
- target source follows the accepted hierarchy
- country-specific protected groups require researched registries
- occupied civilians, refugees, resistance detainees, political enemies, and broad domestic purge remain distinct
- genocide classification requires qualifying group and specific destructive intent
- other atrocities use accurate labels
- no valid target source means extermination policy has zero AI probability and is unavailable to the player
- broad domestic purge creates severe stability, officer, factory, and civil-war pressure

## Evolution I

Pass conditions:

- active-network entry converts `floor(valid_site_count / 2)` concentration sites, leaving the odd extra as concentration
- pre-fire entry opens with 20 percent coverage split roughly evenly
- closing, liberated, destroyed, or noncontinuing sites are excluded
- one-site moderate network uses the documented policy gate
- conversion preserves responsibility, generation, evidence, and shock markers
- forced-labour assignment is removed
- extermination sites do not grant the strong production assignments
- killing policy requires valid target purpose
- halt-extermination route exists
- further conversion obeys policy and caps
- conversion count and state choice receive probability evidence

## Restricted chemical integration

Pass conditions:

- nerve-agent route is clearly alternate history
- valid technology and project gates are required
- real stockpile is debited every operation pulse
- failed debit stops operation
- operation uses exact population loss and a distinct Deaths reason
- contamination and accident risk are applied through shared systems
- source-specific evidence is created
- state liberation and decontamination work
- no procedural chemical instructions appear in localisation
- site does not create technology or stockpile

## Evolution II

Pass conditions:

- every active camp state receives one exact 1 percent current-population loss when Evolution II reaches the network
- exact applied amount uses the public helper
- protected floor is honored
- actual applied amount is logged
- recruitable-manpower credit is reconciled once
- per-state and per-generation marker is stored
- new sites after activation receive the shock once
- conversion, controller change, repeat firing, save, and reload do not repeat it
- pre-fire evolved opening applies it after site registration

## Evolution III

Pass conditions:

- total reach becomes 50 percent of eligible states
- final network is roughly evenly split between concentration and extermination sites
- existing extermination sites are never downgraded automatically
- gulag sites use the Soviet adapter
- active-network entry adds only required sites
- every active camp state receives one exact 2 percent current-population loss
- states that earlier received Evolution II can receive the later 2 percent shock
- pre-fire Evolution III opening receives only the 2 percent opening shock
- newly added Evolution III sites do not also receive the 1 percent shock
- delayed setup survives save and reload

## Ongoing population loss

Pass conditions:

- every death removes real state population
- requested and applied loss are distinguished
- protected floor is honored
- Deaths reasons are cause-specific
- famine, disease, bombing, nuclear, disaster, migration, and camp causes do not double count
- ongoing mortality uses finite detained capacity and dynamic conditions
- pulse stops after closure or liberation
- no whole-world daily or weekly scan exists
- Chaos Meter gain comes through the shared Deaths system only

## Network Reach, Exposure, and Resistance Pressure

Pass conditions:

- all three values are bounded and centralized
- player sees current band and next threshold
- Network Reach uses current eligible and active state counts
- conversion does not change reach
- Exposure responds to evidence, leaks, access, retreat, and discovery
- concealment lowers immediate exposure only with cover-up risk
- Resistance Pressure responds to deaths, abuse, famine, disease, guards, relief, and local conditions
- violent suppression cannot permanently erase resistance
- shared Condemnation is not duplicated as a fourth Event 22 value

## Evidence and discovery

Pass conditions:

- state evidence retains source families and responsible actors
- country evidence links sites into a network
- confidence progresses from fragmentary report to verified network
- liberation checks undiscovered active, abandoned, or destroyed sites
- survivors, documents, physical evidence, foreign intelligence, and cover-up are separate contributors
- public Condemnation source is unique and added once
- one destroyed archive does not erase all proof
- network verification updates Event 22 history and foreign reactions
- no passive public condemnation occurs without discovery
- country-specific experiment and chemical sources add correct bonuses

## Liberation and relief

Pass conditions:

- noncontinuing controller stops organized operation immediately
- former operator bonuses end
- state enters a valid liberated, abandoned, destroyed, contaminated, or evacuated status
- survivor count and condition are calculated safely
- urgent security, food, medicine, disease, contamination, registration, evidence, transfer, and dismantlement actions exist
- post-liberation deaths can occur from relief failure and use a distinct reason
- liberator gains no responsibility unless it reuses the site
- reuse creates a new responsibility generation
- large relief workload uses regional missions
- relief category closes after stable aftermath

## Migration and displaced persons

Pass conditions:

- death and migration transactions are separate
- origin population is not removed twice
- safe return, family link, receiving capacity, route, war, and policy affect destination
- receiving states gain real temporary pressure
- unsafe forced return has consequences
- survivors can remain displaced after peace
- shared migration API is used when available
- no unsupported individual ethnicity or identity is invented

## Retreat and death marches

Pass conditions:

- front distance or state-loss risk creates an emergency mission
- closure in place, supplied transfer, forced evacuation, liquidation, destruction, and abandonment are distinct
- supplied transfer requires real route and capacity
- forced evacuation creates route deaths, escape, witnesses, and linked evidence
- liquidation uses exact loss and strongest evidence
- destroyed sites remain discoverable
- chemical or biological destruction can leave contamination
- emergency decisions replace ordinary management for the threatened state

## Civil war, succession, and annexation

Pass conditions:

- original pre-split responsibility persists
- each later operator receives its own generation
- state evidence and shock markers survive split
- successor chooses disclosure, closure, review, continuation, or concealment
- annexer receives relief burden, not automatic criminal responsibility
- puppet master responsibility requires explicit order or support proof
- tag switch, cosmetic tag, ideology change, annexation, release, and peace do not clear history
- Event 21 hooks use bounded context and do not create a civil war from every resistance incident

## Tribunal and accountability

Pass conditions:

- tribunal eligibility requires verified evidence and a valid actor
- evidence categories are tracked
- broad institutions can be identified without inventing characters
- named historical characters require sourced country content
- public trials, international cooperation, partial trials, amnesty, obstruction, and cover-up have distinct consequences
- accountability cannot restore deaths
- genuine relief and accountability can mitigate future pressure through the shared system
- trials are not a large reward dump

## Event integrations

Pass conditions:

- Event 5 Soviet Collapse inheritance works
- Event 6 Independence Wave inheritance works where relevant
- Event 13 disaster hook preserves cause ownership
- Event 16 experiment link uses its public contract
- Event 20 plague cause accounting is distinct
- Event 21 civil-war pressure is bounded
- Event 31 terror link is used only for independent campaigns
- chemical and biological systems own contamination
- famine owns general famine state and deaths
- migration owns actual transfers when available
- occupation and resistance use current engine and mod systems
- air cleanliness affects disease and relief where supported

## AI and probability

Pass conditions:

- all seven AI profiles are implemented or cleanly merged with documented equivalents
- hard blockers are exact zero conditions
- opening policy scenarios pass expected orderings
- state selection scenarios pass
- conversion count and target scenarios pass
- assignment and intensity scenarios pass
- concealment and retreat scenarios pass
- discovery, foreign reaction, and relief scenarios pass
- sequence tests pass
- sweeps show no abrupt invalid inversion
- never-fired countries are not starved
- no option dominates every plausible campaign
- before and after probability evidence is attached for every patched weighted surface

## Performance

Pass conditions:

- only registered countries and states receive pulses
- no whole-world daily or weekly scan
- large operations use bounded delayed jobs
- jobs have generation, actor, state, and revalidation proof
- invalid jobs fail closed
- no hidden fallback target
- pulse timing is distributed to avoid one-day spikes
- completed countries and states unregister
- save and reload does not duplicate jobs
- error log shows no repeated scope, variable, array, or target failures

## Multiplayer

Pass conditions:

- secret information is visible only to valid players
- public discovery reaches valid observers
- tag switching does not reinitialize the network
- civil-war players receive correct sites and responsibility
- selected state or country targets are scoped per player country
- simultaneous event responses do not share one global choice variable
- no repeated popup reaches every human without a valid relation
- host and client save and reload preserve state

## Presentation

Pass conditions:

- main management category uses one static archival picture at verified native size
- relief category uses a restrained icon and normal decision presentation unless a separate accepted picture is added
- category shows policy, Network Reach, Exposure, Resistance Pressure, and one current priority
- state tooltips show site type, operator, assignment, workforce condition, mortality direction, resistance direction, evidence, and closure or relief status
- no custom scripted GUI is added
- no animation is added
- map targeting highlights only valid states
- colours have icon, text, shape, or frame alternatives
- no graphic imagery or spectacle audio

## Assets

Pass conditions:

- archival sources have institution, licence, attribution, original file, checksum, and crop notes
- generated icons have ImageGen source evidence and prompt notes
- transparent backgrounds have no white matte
- native and `4x` reviews pass
- category picture fits controls and text
- report images are `210x176`
- news images are `397x153` and black and white
- decision icons are readable at `32x32`
- idea and achievement icons are readable at `64x64`
- existing building icons are audited before creating replacements
- only assets listed in the accepted asset manifest are created and wired
- runtime references do not point into `docs/assets`
- temporary asset workspace is removed only after durable evidence is promoted

## Localisation

Pass conditions:

- no raw keys appear
- all event, decision, mission, category, idea, modifier, achievement, tooltip, and log keys exist
- file encoding and BOM meet project rules
- dynamic state, country, policy, site, and target-purpose text resolves correctly
- terms distinguish concentration, forced labour, gulag, extermination, experiment, restricted chemical, liberated, and relief sites
- genocide label appears only with qualifying proof
- nerve-agent route is described as alternate history
- no invented quotations
- no graphic or procedural killing descriptions
- costs use icons
- blocked reasons are concise and exact
- hidden future outcomes remain hidden
- country-specific text replaces generic text where adapters exist
- localisation audit handoff lists all changed keys

## Event log and details

Pass conditions:

- first activation logs country, count, coverage, split, policy, and generation
- material repeat incidents log once
- every evolution logs entry path and applied count
- public discovery logs actor and evidence
- major liberation and transparent closure log
- routine pulses do not spam history
- Event 22 details show baseline and three evolutions
- shared event log and detail framework are not modified through an event-owned GUI worker

## Catalog and documentation

Pass conditions:

- authoritative XLSX Event 22 row updated
- old Spain Antisemitism row removed by replacement
- Type becomes Minor Repeatable
- Random Chaos numeric ID resolves to a real cluster row
- member severity is Severe
- Evo I through III populated
- workbook formatting and validation preserved
- CSVs regenerated through exporter
- Camps and Genocide docs updated
- Deaths reason docs updated
- Condemnation source docs updated
- integration docs and handoffs updated
- current specs, plans, and implementation agree

## Achievement acceptance

Pass conditions:

- priority achievements are implemented according to proof contracts
- no achievement rewards deaths, extermination count, output, chemical killing, or concealment
- persistent proof survives tag changes and reload
- icons have completed, grey, and not-eligible states
- achievements cannot be earned by deleting buildings, losing states, or switching tags
- multiplayer owner proof is correct

## Required subagent and audit routing

When runtime is available:

- use `chaosx_repo_explorer` only if touched-file mapping is still unclear
- use `chaosx_scripted_system_architect` for public helpers and centralized values
- use `chaosx_decision_mission_auditor` after the decision system exists
- use `chaosx_ai_probability_auditor` before and after weighted changes
- use `chaosx_localisation_auditor` after keys are written
- use `chaosx_asset_source_researcher` for archival images
- use `chaosx_icon_artist` for icons and achievements
- use `chaosx_spreadsheet_doc_worker` for workbook update
- use `chaosx_event_completion_auditor` for final read-only comparison
- use `chaosx_improvement_loop_planner` only after the current accepted design is implemented or explicitly queued
- do not use `chaosx_event_ui_worker` because Event 22 does not introduce a dedicated scripted GUI

Every patch-capable subagent writes a handoff under:

```text
docs/plans/022_concentration_camps_plans/subagent_handoffs/
```

## Required MCP evidence

At minimum:

- event-chain inspect for opening, repeat, evolution, discovery, liberation, and cleanup paths
- decision and mission inspection where supported
- probability inspect, evaluate, sweep, sequence, and compare
- map or state-target inspection if the relevant route exists
- GUI inspection only for ordinary category integration when needed, not as an event-owned scripted-GUI task

Missing required routes must be reported as blockers. Source review is not equivalent.

## Live QA scenarios

### Scenario A: baseline small country

- three to five eligible states
- first firing
- verify rounded 20 percent coverage
- choose closure
- complete regional closure
- save and reload

### Scenario B: baseline industrial authoritarian

- medium country at war
- choose forced labour
- test every valid assignment role
- exhaust one workforce
- reduce quota and close one state

### Scenario C: Evolution I active network

- at least six concentration sites
- activate Evolution I
- verify exact conversion count and selection
- halt one extermination site
- expose another

### Scenario D: Evolution II

- active mixed network
- record pre-shock population
- apply 1 percent
- verify actual exact loss and ledger
- save and reload
- add one new site and verify one shock

### Scenario E: pre-fire Evolution III

- country with no prior Event 22 network
- first firing at Evolution III
- verify 50 percent coverage and split
- verify 2 percent only

### Scenario F: active Evolution III

- baseline network already received Evolution II
- activate Evolution III
- verify expansion and additional 2 percent
- ensure new states skip 1 percent

### Scenario G: liberation

- enemy takes active, abandoned, destroyed, and chemical sites
- verify operation stops
- complete relief and evidence
- test reuse and responsibility generation in a separate save

### Scenario H: retreat

- enemy approaches several sites
- test closure in place, supplied transfer, forced evacuation, liquidation, destruction, and abandonment in separate saves

### Scenario I: civil war and successor

- split active network through Event 21
- verify responsibility and shock markers
- use one side for disclosure and one for continuation in separate saves

### Scenario J: multiplayer

- two human countries
- one perpetrator and one observer or liberator
- verify secret and public information
- save and reload

## Live test evidence

Use the project live-QA folder structure and record:

- run manifest
- dedicated save
- setup commands
- event and evolution settings
- screenshots
- fresh error-log delta
- coverage table
- repair ledger
- skipped tests and reasons

Do not use Force Trigger Mode to prove normal eligibility or probability.

## Final completion gate

The parent can claim Event 22 complete only after:

- source implementation passes repository validation
- every required handoff is reviewed
- probability evidence matches the final source
- assets are installed and reviewed
- localisation is audited
- workbook and CSVs agree
- live QA covers baseline, all evolutions, liberation, retreat, succession, and save reload
- completion auditor finds no missing accepted mechanic, fallback, silent simplification, stale document, or unhandled plan
- unresolved blockers are either fixed or explicitly prevent the completion claim
