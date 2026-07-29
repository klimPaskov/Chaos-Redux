# Chaos Redux: Complete Mechanics and Systems Guide

Last reconciled with the repository source on 2026-07-29.

This document is the top-level map of Chaos Redux gameplay systems. It explains how the shared systems fit together, points to the canonical subsystem documents, and records important implementation boundaries. Live script remains authoritative for exact values and runtime behavior. Accepted specifications describe intended design. Dated plans and handoffs are evidence snapshots rather than automatic proof that a feature is active.

The event catalog workbook at `docs/spreadsheets/chaos_redux_events_catalog.xlsx` is the source of truth for the complete player-facing event, cluster, and scenario catalog. The documents under `docs/events/` are the canonical mechanic references for numbered event chains.

## Contents

1. [System status and authority](#system-status-and-authority)
2. [Random event framework](#random-event-framework)
3. [Chaos Meter and global consequence systems](#chaos-meter-and-global-consequence-systems)
4. [World-end and terminal systems](#world-end-and-terminal-systems)
5. [Triggerable scenarios](#triggerable-scenarios)
6. [Chaos Warfare and CBRN systems](#chaos-warfare-and-cbrn-systems)
7. [Camps, repression, and genocide crisis](#camps-repression-and-genocide-crisis)
8. [Major event-owned mechanic packages](#major-event-owned-mechanic-packages)
9. [Cross-event country, UI, and support systems](#cross-event-country-ui-and-support-systems)
10. [Multiplayer, AI, and performance model](#multiplayer-ai-and-performance-model)
11. [Inspection and manual controls](#inspection-and-manual-controls)
12. [Canonical documentation map](#canonical-documentation-map)

---

## System status and authority

The guide uses the following status language.

| Status | Meaning |
| --- | --- |
| Active | The gameplay surface is wired in the current source. |
| Partial | A substantial runtime package exists, but its own source documentation records unresolved content or acceptance work. |
| Fail-closed | Code and presentation may exist, but the action remains unavailable because the engine cannot provide a required verified input. No proxy or fallback is used. |
| Reserved | The identity is visible for compatibility or future work, but it is not a complete gameplay route. |

Important current boundaries:

- Reaching 1000 Chaos enters the final Chaos tier. It does not call a generic random world-end selector.
- Terminal routes are owned by exact events or consequence systems and must pass their own readiness, enable, and conflict gates.
- Fallout is the active contamination-driven terminal consequence. The natural Final Silence registry route is retired, although the explicit manual Final Silence scenario remains available.
- Event 005 Soviet Collapse, Event 006 Independence Wave, Event 012 Africa, and Event 016 Brilliant Scientist have large active packages with documented remaining work. Their event documents define the exact current boundary.
- Event 017 Random Faction is implemented in source and remains marked `Needs Testing` in the catalog.
- The Africa Is One manual scenario is a reserved placeholder and does not represent a complete Event 012 scenario.
- Exact-state chemical battlefield operations and nerve-agent occupation suppression are fail-closed until the installed engine exposes the required verified state-condition and target-loss receipts.

---

## Random event framework

### Shared event pool

Chaos Redux uses one registered event framework for automatic incidents, manual event firing, Event Details, clusters, and event-owned actor selection.

Every registered event has:

- a stable numeric ID and player-facing name.
- a classification of fire-once, repeatable, or major.
- a current weight and availability state.
- an enable or disable state.
- optional actor-selection and valid-target logic.
- optional evolution tracks, cluster membership, super-events, world-end branches, achievements, decisions, countries, focus trees, or custom interfaces.
- history and Event Details content where applicable.

Country-specific events must prove that a valid target exists before selection. If no target exists, the event is unavailable and displays `N/A` rather than firing against an invalid country.

### Timer and pacing

The event timer uses the current values in `common/script_constants/event_system_constants.txt`.

| Setting | Current default |
| --- | ---: |
| Initial timer | 7 to 30 days |
| Normal timer range | 45 to 60 days |
| Absolute minimum timer | 2 days |
| Minor-event decrement step | 1 day |
| Compression interval | every 3 minor pacing events |
| Minimum-side decrement cap | 15 days |
| Maximum-side decrement cap | 5 days |

Each minor pacing event increases pressure on the next roll. The minimum side can lose up to 15 days and the maximum side can lose up to 5 days. A major event resets the accumulated minor-event pacing pressure.

The Chaos tier multiplier is applied after the timer range is calculated.

| Chaos tier | Range | Timer multiplier |
| --- | ---: | ---: |
| Calm World | 0 to 199 | 1.0 |
| Gathering Storm | 200 to 399 | 0.8 |
| Rising Chaos | 400 to 599 | 0.7 |
| Chaos | 600 to 799 | 0.6 |
| Totalen Chaos | 800 to 999 | 0.5 |
| World Collapse | 1000 and above | 0.5 |

### Event classifications and weights

#### Fire-once events

Fire-once events begin at the default event weight of 1000 unless their own registration changes that value. Once accepted, they are removed from normal future selection for that campaign.

#### Repeatable events

Repeatable events begin at the default weight of 1000. After firing, their cap is multiplied by the configured reduction factor, currently 0.5. Their weight then recovers at the configured rate, currently 20 per month, up to the current cap.

The default cap sequence is 1000, 500, 250, 125, and progressively lower values until the event becomes extremely rare.

#### Major events

Major events begin inactive and gain weight from minor pacing events. The configured baseline gain is 150 when the active pool contains 90 non-major events and 10 major events. The dynamic major-weight system scales that gain against the live registered pool so adding or disabling events does not silently distort the intended major-event cadence.

When a major event fires, the fired major is removed, other unfired major weights are reset, and minor-event timer pressure is cleared.

Canonical reference: [Dynamic Major Event Weights](docs/systems/dynamic_major_event_weights.md).

### Evolutions

Evolutions are mutation tracks inside an event identity. They are separate from ordinary stage progression.

An evolution can:

- change future event behavior.
- add a new country, crisis, route, decision set, or focus branch.
- increase the scale or danger of future firings.
- unlock a terminal branch.
- add a separate Event Log milestone.

Each evolution has an independent enable state. Disabled evolutions must not write their recorded flags or leak their gated content into the baseline route.

### Event clusters

Clusters group compatible normal events into larger incidents. The random picker still selects one event first. If that event belongs to a cluster, the cluster rolls its configured chance and may execute several member events.

A cluster counts as one global pacing event. Each member still applies its own effects, history, fire-once removal, repeatable cap changes, actor mapping, and Event Details state. Member events do not each advance the shared timer or major-weight gain.

The current cluster UI shows availability, roll chance, enabled state, fired count, member danger, and fired or skipped reasons.

Canonical references:

- [Event Clusters](docs/systems/event_clusters.md)
- [Events Log Evolutions and Clusters](docs/systems/events_log_evolutions_and_clusters.md)

### Event Log and Event Details

The Event Log is the shared observation surface for the random-event framework and selected system records.

Its main tabs are:

- Status.
- History.
- Evolutions.
- Events.
- Clusters.

The Events tab exposes live event weight, fired count, type, repeatability, availability, and individual enable state. The History and Evolution tabs preserve actor context where the owning system provides one. Event Details can open separate movable windows and can show an event's evolutions and public terminal branches.

The logger also supports dedicated record types for Fallout country memories and unified CBRN action records. Fallout itself does not create an ordinary random-event history entry.

Canonical references:

- [Event Logs Window](docs/systems/events_log_window.md)
- [Events Log Evolutions and Clusters](docs/systems/events_log_evolutions_and_clusters.md)
- [Event Logging Controls](docs/systems/chaosx_event_logging_controls.md)

### Settings

The settings interface controls:

- global and per-country event-system enable state.
- event selection, filtering, sorting, and direct firing.
- force-trigger testing.
- timer minimum and maximum values.
- repeatable recovery and cap reduction.
- baseline major-event gain.
- per-tier timer multipliers.
- event and evolution enable states.
- cluster selection and manual firing.
- triggerable scenarios.
- super-event audio and presentation preferences.
- Chaos Meter, Deaths, Air Cleanliness, and related subsystem preferences.
- settings export.

Numeric manual entry uses the dedicated settings input buffer rather than an unsupported free-form text widget.

Canonical references:

- [Miscellaneous Settings Menu](docs/systems/settings_miscellaneous_menu.md)
- [Settings Numeric Manual Inputs](docs/systems/settings_numeric_manual_inputs.md)
- [Settings Export](docs/systems/chaosx_settings_export.md)

---

## Chaos Meter and global consequence systems

### Chaos Meter

The Chaos Meter is a global instability value. It drives timer speed, evolution gates, event-owned high-chaos routes, UI status, and some terminal readiness checks.

Chaos changes come from exact recorded causes. The shared source set includes:

- wars, peace settlements, annexations, puppeting, liberation, release, and subject changes.
- coups, ideology changes, mobilization, guarantees, faction formation, faction membership, and faction dissolution.
- world-tension movement, military-factory growth, division growth, tracked deaths, and air-contamination movement.
- nuclear use through the shared 10, 5, 3, 2, then 1 direct-chaos ladder.
- event-owned changes and special system outcomes.
- monthly world decay of 1 Chaos while the meter is active.

The Chaos Meter window contains Status, History, Air Cleanliness, Condemnation, and Deaths views.

Canonical references:

- [Chaos Meter Popup Window](docs/systems/chaos_meter_popup_window.md)
- [War Declaration Counting](docs/systems/chaos_meter_war_declaration_counting.md)
- [Nuclear Chaos Ladder](docs/systems/nuclear_chaos_ladder.md)

### Deaths

The Deaths system is the shared population and casualty ledger.

It records:

- civilian and military totals.
- exact cause families.
- affected country and state context where supplied.
- recent history for the Deaths tab.
- population loss applied through shared bounded effects.
- Chaos gain at one point per one million accumulated tracked deaths.

Connected sources include strategic bombing, nuclear strikes, chemical attacks, biological outbreaks, contamination, disaster impacts, camp processing, event-country consumption, and military casualty receipts.

The system changes real state population when a mechanic supplies an accepted civilian-loss request. It is not limited to recruitable-manpower penalties.

Canonical references:

- [Deaths Mechanic](docs/systems/chaos_meter_deaths_mechanic.md)
- [Deaths and Event Log UI](docs/systems/chaos_meter_deaths_and_events_log_ui.md)
- [Combat, Contamination, and Occupation Deaths](docs/systems/chaos_meter_combat_contamination_occupation_deaths.md)

### Air Cleanliness

Air Cleanliness stores global atmospheric contamination in basis points.

| Source | Current contribution |
| --- | ---: |
| Chemical contamination in one state | 1 basis point |
| Low-intensity outbreak state | 1 basis point |
| Standard outbreak state | 2 basis points |
| High-intensity outbreak state | 3 basis points |
| Normal nuclear strike | 20 basis points |
| Thermonuclear strike | 150 basis points |
| Wildfire smoke or volcanic ash reservoir | up to 4 basis points per month for each source |

The normal monthly recovery bands are:

| Contamination | Recovery |
| --- | ---: |
| Below 25 percent | 3 basis points |
| 25 percent and above | 2 basis points |
| 50 percent and above | 1 basis point |
| 75 percent and above | 0.5 basis points |

At 25 percent, spread pressure becomes easier. At 50 percent, mild winter conditions can begin. At 75 percent, stronger global effects become possible. At 100 percent, the irreversible contamination route and Fallout request gate become eligible.

Every net 1 percent rise adds 1 Chaos. Every net 1 percent recovery removes 1 Chaos.

The system also owns state contamination refresh, winter modifiers, natural smoke and ash sources, and the shared monthly Air Cleanliness Treaty host.

Canonical references:

- [Air Cleanliness Mechanic](docs/systems/air_contamination_mechanic.md)
- [Air Cleanliness Treaty](docs/systems/air_cleanliness_treaty.md)

The broader treaty design is partial. The current tranche includes implemented treaty actions and shared host logic. Pooled decontamination, seed archive exchange, evacuation corridors, relief votes, major-burner sanctions, and improved forecast precision remain outside the implemented tranche.

### Condemnation and sanctions

Condemnation is the shared public responsibility system for unconventional warfare, exposed atrocities, evidence destruction, blocked inspections, and repeated use.

Public source families are:

- Chemical.
- Biological.
- Nuclear.
- Atrocity.
- Coverup.
- Repeat Use.

Hidden evidence stays outside the public total until an accepted discovery, observer, inspection, occupation, forensic publication, or disclosure path reveals it.

| Tier | Public score |
| --- | ---: |
| Normal | below 25 |
| International Concern | 25 to 49 |
| Formal Censure | 50 to 99 |
| Arms Embargo | 100 to 174 |
| Strategic Embargo | 175 to 299 |
| Total Embargo | 300 to 499 |
| Pariah State | 500 and above |

The Condemnation tab shows the public score, source breakdown, current and peak tier, recent public sources, next threshold, sanction participants, practical penalties, decay, and compliance state.

Sanction participants can impose bilateral penalties, recall volunteers or attaches, block new lend-lease, and respond through inspections, aid, retaliation, or stockpile destruction. The native embargo action depends on By Blood Alone. The scripted enforcement record and its penalties remain active without that DLC.

Canonical references:

- [Condemnation and Sanctions](docs/systems/condemnation_sanctions.md)
- [CBRN Diplomacy Actions](docs/systems/cbrn_diplomacy_actions.md)

### World threat

The world-threat framework consolidates existential external dangers under `world_in_threat` and a counted set of source flags. Event systems add or remove their own source only when their real gameplay conditions justify it.

Current consumers use the shared state for cooperation, AI posture, emergency responses, and event interactions. Event-specific threat flags do not replace the shared aggregate.

Canonical reference: [World Threat Mechanic](docs/systems/world_threat_mechanic.md).

---

## World-end and terminal systems

World-end routes are explicit consequences owned by events or global systems. They do not begin merely because Chaos reached the final tier.

Every accepted automatic terminal branch must prove:

- its owner-specific route and world-state conditions.
- the required Chaos gate where applicable.
- that its branch is enabled.
- that no conflicting terminal state is active.
- its own actor, target, and presentation requirements.

When a terminal route commits, it sets the shared `world_end` state and its own scenario flag. Systems that must stop after a terminal transition read those flags directly.

### Current public registry

| Owner | Public terminal route | Presentation |
| --- | --- | --- |
| Event 2 Zombie Outbreak | Zombie Apocalypse | Zombie Apocalypse super-event |
| Fallout consequence system | Fallout | Dedicated blackout UI and audio |
| Event 7 Fury | The World in Fury | The World in Fury super-event |
| Event 10 Death | Last Shores | The Census of Zol super-event |
| Event 14 Cannibalism | The World Is the Larder | Matching super-event |
| Event 14 Cannibalism | No Thaw Will Come | Matching super-event |
| Event 18 Resources Found | The World Opens Below | The Deep War Crosses the Seas super-event |
| Event 16 Brilliant Scientist | Laboratory World | Matching super-event |
| Event 16 Brilliant Scientist | Strategic Singularity | Matching super-event |

Public rows have independent persistent enable state. Disabling one branch does not disable its owner event or a sibling branch. A terminal branch that has already begun cannot be undone through the checkbox.

The weaponized Wendigo ascendancy retains an internal registry identity and remains absent from public Event Details.

The old save-facing Final Silence scenario ID remains reserved. Its automatic public registry entry has been replaced by Fallout. The manual `SCN-004` Final Silence launcher still exists as an explicit sandbox route.

Fallout can be requested by the Air Cleanliness terminal gate, an owning terminal event, or its manual route. It uses a dedicated blackout transition and does not create an ordinary random-event history row or ordinary super-event popup.

Canonical references:

- [Event Details World-End Catalog](docs/systems/events_log_world_end_scenarios.md)
- [Air Cleanliness Mechanic](docs/systems/air_contamination_mechanic.md)
- Fallout specifications and runtime documents under `docs/specs/air_cleanliness_fallout_specs/` and `docs/plans/air_cleanliness_fallout_plans/`

---

## Triggerable scenarios

Triggerable scenarios are explicit sandbox or challenge setups launched from the settings UI. The window is data-driven, sortable by ID or name, and stores a scenario-specific type plus one of four intensity levels before confirmation.

Manual scenarios intentionally bypass the normal random-event timing and selected source-event prerequisites that the scenario is designed to replace. They retain their own host, target, conflict, idempotency, and setup-validity gates.

| ID | Scenario | Current role |
| --- | --- | --- |
| SCN-001 | Zombie Apocalypse | Seeds standard or special zombie outbreaks with intensity-scaled coverage. |
| SCN-002 | Army of Clones | Creates a hostile clone army with standard or Aryan configuration. |
| SCN-003 | Soviet Collapse | Forces the Event 005 terminal collapse with ordinary or chaos republic settings. |
| SCN-004 | Final Silence | Runs the explicit nuclear or thermonuclear Final Silence sequence. |
| SCN-005 | The World in Fury | Seeds pact-based or hostile Fury actors. |
| SCN-006 | Death | Starts Death with an intensity-scaled initial footprint without starting its terminal route. |
| SCN-007 | Disaster Barrage | Starts one Event 013 disaster season by selected family and intensity. |
| SCN-008 | Every Banner Rises | Launches the Event 006 frozen release transaction with selected political and war rules. |
| SCN-009 | Coalition Unmasked | Builds and reveals an Event 011 coalition around the current player. |
| SCN-010 | The Hunger Lines | Launches selected Event 014 crisis profiles without exposing hidden branches in its public text. |
| SCN-011 | Africa Is One | Reserved placeholder. It launches only a neutral placeholder event. |
| SCN-012 | Black Plague Unbound | Seeds established plague outbreaks, Rat Nations, and the Rat King without granting the terminal evolution. |
| SCN-013 | The Unbidden Muster | Launches the Event 019 formation crisis with conventional, specialist, claimant, or nonhuman profiles. |

Canonical references:

- [Triggerable Scenarios](docs/systems/triggerable_scenarios.md)
- [Independence Wave Scenario](docs/systems/independence_wave_triggerable_scenario.md)
- [Infantry Spawn Scenario](docs/systems/019_infantry_spawn_triggerable_scenario.md)

---

## Chaos Warfare and CBRN systems

Chaos Warfare is an equipment-backed chemical, biological, radiological, and nuclear command package. Its systems are connected through shared readiness, protection, payload, exposure, consequence, evidence, Condemnation, Deaths, Air Cleanliness, and action-record contracts.

Owning technology, equipment, a doctrine, or a delivery platform never creates an attack by itself. An accepted release must identify an exact route and target, prove authorization, consume the required payload, resolve protection, and write the shared consequences.

### Chaos Warfare doctrine

Chaos Warfare is a conditional grand doctrine that costs 100 Army Experience to adopt. Adoption starts a 90-day institutional establishment mission and initializes Chemical Readiness.

Establishment requires:

- 500 gas masks.
- 50 decontamination equipment.
- 100 support equipment.
- a fielded CBRN Operations HQ Section.
- a fielded Gas Mask and Decontamination Detachment.

The four player-facing mastery tracks are:

| Compatibility ID | Player-facing track | Main role |
| --- | --- | --- |
| `extermination_columns` | Hazard Assault Formations | Protected infantry, contaminated-terrain operations, Hazard Pioneers, and Chaos Assault Battalions. |
| `chemical_suppression` | Toxic Armored Warfare | Sealed crews, armored delivery, protected breakthrough logistics, and bounded suppression eligibility. |
| `contaminant_firebases` | Contaminant Fire Support | Projectors, chemical artillery, persistent shells, and deep-contamination preparation. |
| `integrated_chemical_operations` | Integrated CBRN Command | Intelligence, weather, logistics, decontamination, biosecurity, and Theater CBRN Headquarters. |

Four cross-track institutions raise readiness caps and unlock stronger authorization:

1. Protective Foundation.
2. Delivery Integration.
3. Theater Exploitation.
4. Terminal CBRN Command.

The five use policies progress from Defensive Preparation through Retaliation Authority, Limited Battlefield Authority, Strategic Release Authority, and Unrestricted Chaos Warfare. A policy authorizes later adapters. It does not consume payload or create exposure.

The officer corps adds mutually exclusive army-command and division-command postures, institutional high-command roles, and the Chemical Operations Commander trait.

Canonical references:

- [Chaos Warfare Doctrine](docs/systems/chaos_warfare_doctrine.md)
- [Grand Doctrine Update](docs/chemical_warfare/chaos_warfare_grand_doctrine_update.md)
- [Officer Corps Spirits](docs/chemical_warfare/chaos_warfare_officer_corps_spirits.md)
- [Division Command Spirit](docs/chemical_warfare/chaos_warfare_division_command_spirit.md)

### Chemical Readiness and native operations surface

The native CBRN decision categories expose:

- doctrine establishment and use policy.
- Chemical Readiness.
- national protection and procurement.
- civilian protection.
- headquarters preparation.
- chemical and biological release routes.
- occupation measures.
- international response.

The existing Chaos Meter tabs remain the global consequence readout. The CBRN system does not use an undisclosed custom-GUI replacement for these decision categories.

Canonical reference: [CBRN Operations Surface](docs/systems/cbrn_operations_surface.md).

### Army Headquarters and regimental support

Six Army-HQ-only support companies provide command preparation for chemical planning, protection, decontamination, cordons, medical response, biological containment, and the doctrine capstone.

An HQ order:

1. checks the deployed Army HQ and exact company composition.
2. checks readiness, policy, Command Power, and real equipment.
3. records a force band and operation identity.
4. applies a bounded preparation period.
5. pays weekly sustainment while active.
6. ends through scheduled targeted events.

HQ preparation does not select a state or release a payload. Exact delivery remains the responsibility of a selected-state raid, decision, camp adapter, occupation adapter, biological route, or other verified action.

Regimental CBRN companies are the division layer. They provide protection, reconnaissance, decontamination, medical, or route eligibility and have real reinforcement needs.

Canonical references:

- [CBRN Army Headquarters](docs/systems/cbrn_hq_command.md)
- [CBRN Regimental Support](docs/chemical_warfare/cbrn_regimental_support.md)

### Protective equipment and civil defence

The protection package includes:

- military and civilian gas-mask models.
- filters and protective clothing.
- decontamination equipment.
- CBRN instruments.
- medical and warning capacity.
- national reserve, issue, maintenance, and replacement decisions.
- civilian registration, fitting, alarm, shelter, and response decisions.
- equipment-aware MIOs and AI production targets.

Protection reduces accepted exposure according to the exact agent and route. It does not erase evidence, responsibility, historical deaths, or confirmed-use history.

### Chemical payload and delivery

The chemical system uses exact equipment models for chlorine, phosgene, mustard, lewisite, tabun, sarin, soman, and supported special-agent packages.

The shared delivery pipeline requires:

- an unlocked exact agent.
- a valid exact target state.
- an authorized delivery route.
- sufficient matching payload.
- a protection receipt.
- a condition receipt where the route requires one.
- evidence, attribution, Deaths, contamination, medical, and Condemnation processing.

Active delivery routes include selected-state chemical air and strategic rocket raids, chemical doomsday release, restricted-site camp escalation, and other route-specific adapters that can prove their inputs.

Chemical aircraft modules affect only designs that install the exact rack. Idle aircraft and ordinary air missions do not create contamination.

The timed exact-state ground-operation family is fail-closed because the current engine surface does not expose the required selected-state weather and terrain receipt. The decisions, assets, costs, and resolution code remain gated and unavailable. No capital proxy, random state, or neutral-condition estimate is used.

Canonical references:

- [Chemical Warfare System](docs/chemical_warfare/chemical_warfare_documentation.md)
- [Chemical Payload and Consequence Core](docs/systems/cbrn_chemical_delivery.md)
- [CBRN Battlefield Operations](docs/systems/cbrn_battlefield_operations.md)
- [Chemical First-Use Surprise](docs/chemical_warfare/chemical_first_use_surprise.md)

### Chemical and protective MIOs

The Military Industrial Organization layer includes chemical munitions, air delivery, protective equipment, decontamination, detection, and biological protection families.

Exact chemical-rack weight, range, and agility behavior uses grant-only module technologies because current MIO filters cannot prove that a variant carries one specific chemical rack. This prevents a chemical designer from granting its bonuses to ordinary aircraft.

Canonical reference: [CBRN Designers](docs/systems/cbrn_designers.md).

### Biological warfare

The biological package includes:

- ordinary-agent special projects for Tularemia, Anthrax, Plague, and Smallpox.
- strategic biological raids.
- battlefield dissemination routes.
- covert operative release.
- supply-chain sabotage.
- captured-facility recovery.
- Japan's China biological campaign.
- stockpile safety and accidents.
- doomsday release.
- countermeasures, quarantine, medical response, vaccination, and disease containment.
- weaponized-zombie projects and delivery routes.
- biological Air Cleanliness and Deaths integration.

Repeated seeds can merge into one state disease episode, but every deliberate action receives its own immutable action identity. The current merged episode owns later civilian-death updates when the engine cannot separate deaths by individual seed.

The biological AI selects projects and production from actual posture, industry, conventional reserve health, protection, containment, arsenal risk, completed projects, and an explicit use route. Country tags do not grant free authorization or bypass safety gates.

Canonical references:

- [Biowarfare System](docs/biological_warfare/biowarfare_system.md)
- [Strategic Biological Raids](docs/biological_warfare/strategic_biological_raids.md)
- [Battlefield Biological Dissemination](docs/biological_warfare/battlefield_biological_dissemination.md)
- [Biological Countermeasures](docs/biological_warfare/biological_countermeasures.md)
- [Biological Stockpile Safety](docs/biological_warfare/biological_stockpile_safety.md)
- [Biological Sabotage](docs/systems/biological_sabotage.md)
- [Captured Facility Recovery](docs/systems/captured_biological_facility_recovery.md)
- [CBRN Biological AI](docs/systems/cbrn_biological_ai.md)

### Unified CBRN action records

Every accepted deliberate chemical release and ordinary biological seed creates one durable aligned action record.

The record stores:

- attacker and affected country.
- exact target state and date.
- weapon class, agent, delivery method, and severity.
- civilian deaths and the available military casualty receipt.
- contamination or outbreak change.
- evidence and attribution.
- retaliation state.
- first-use and repeat-use state.

Each record also writes a dedicated Event Log system-history row. The action ledger remains separate from the Deaths, Air Cleanliness, outbreak, Condemnation, and diplomacy ledgers.

Canonical reference: [CBRN Unified Action Records](docs/systems/cbrn_action_records.md).

### CBRN diplomacy

The international-response layer includes:

- inspection demands.
- exact-state forensic publication.
- foreign decontamination aid.
- sanctions participation.
- retaliation and stockpile-destruction routes.
- compliance and refusal records.

Every action uses a stored country or state target and consumes real equipment, factory capacity, or political resources. Forensic publication advances the exact stored action row and does not assign hidden liability to a guessed incident.

Canonical reference: [CBRN Diplomacy Actions](docs/systems/cbrn_diplomacy_actions.md).

### Occupation policies

Two supported occupation policies are active:

- CBRN Coercive Security.
- Protected Occupation Administration.

The legacy `concentration` occupation-law ID remains hidden and modifier-free for save migration.

The Nerve Agent Suppression Detachment and exact-state suppression transaction are retained as fail-closed compatibility code. The current engine does not provide the required verified state-condition and target-loss receipts. The commissioning and operation controls remain hidden, and no estimator or fallback is used.

Canonical reference: [CBRN Occupation and Nerve Suppression](docs/systems/cbrn_occupation_and_nerve_suppression.md).

---

## Camps, repression, and genocide crisis

The camp-repression system models detention, forced labor, extermination, gulag networks, experiment-linked sites, restricted chemical sites, evidence destruction, discovery, occupation exposure, foreign pressure, and tribunal risk.

### Core state

The system separates hidden internal harm from public Condemnation.

Countries and states track:

- escalation.
- visibility.
- deaths.
- resistance pressure.
- foreign pressure.
- coverup effort.
- discovered sites.
- responsible-country pointers.
- hidden atrocity and coverup evidence.

Internal operation and concealment do not automatically create public Condemnation. Discovery, occupation, inspection, observers, failed coverup, or another accepted disclosure path exposes the stored responsibility.

### Buildings and sites

The main building identities are:

- concentration camp.
- extermination camp.
- gulag labor camp network.

Experiment-linked and restricted chemical sites attach additional evidence and consequence state to an exact physical site.

### Monthly processing and Deaths

Active sites are held in bounded registries and processed through the camp system's existing monthly coordinator. Site method, supply, protection, accident pressure, evidence, resistance, and responsible-country state affect the resolved harm.

Population loss is written through the shared Deaths system. Discovery converts hidden evidence into public atrocity or coverup sources without rewriting the original site history.

### Country routes and AI

Country-specific packages cover:

- German camp administration, occupied Poland escalation, extermination sites, Mengele-linked experiments, deportation logistics, and retreat coverups.
- Japanese forced labor, reprisals, prisoner experimentation, occupation evidence destruction, and biological links during the China war.
- Soviet gulag expansion, deportations, famine pressure, purges, labor quotas, evidence destruction, and the Soviet Collapse bridge.

Restricted chemical-site escalation uses the shared CBRN payload and consequence pipeline for its one-time release. The camp system retains ownership of site existence, monthly harm, evidence, resistance, and discovery.

Canonical references:

- [Camp Repression Network and Ledger](docs/systems/genocide_crisis_system.md)
- [Original Genocide Mechanics Concept](docs/systems/genocide_mechanics_spec.md)
- [CBRN Camp Integration](docs/systems/cbrn_camp_integration.md)

---

## Major event-owned mechanic packages

The workbook contains the complete event catalog, including ordinary events and Fallout country memories. The table below maps the event chains that own substantial persistent mechanics.

| ID | Event | Main persistent systems | Current source status |
| ---: | --- | --- | --- |
| 1 | Communist Insurgency | State control, insurgency levels, sabotage, intervention, revolutionary escalation, World Revolution unlock. | Active |
| 2 | Zombie Outbreak | State outbreaks, zombie countries, evolution, Anti-Zombie League, cure, weaponization, horde succession, island evacuation, terminal branches. | Active |
| 3 | The Holy Realm | Himalayan host selection, focus tree, Buddhahood progression, Dhyana, Sangha Compact, Buddha powers, Final Silence ritual content. | Active. Automatic public Final Silence terminal registration is retired in favor of Fallout. |
| 4 | Random War | Safe country-pair selection, repeatable declarations, War Contagion escalation, special-country participation. | Active |
| 5 | Soviet Collapse | Union Collapse Threat, republic release, leagues, command and corridor systems, successor focus packages, joint liberation coordination. | Partial. The event document records unresolved successor, focus, presentation, and completion work. |
| 6 | Independence Wave | Frozen release transaction, host survival, package registry, founding-state simulation, Networks, Leagues, rival blocs, formables, evolutions, country packages. | Partial. Shared core is source-closed, while package capacity, routes, formables, assets, and some source proofs remain open. |
| 7 | Fury | Repeatable aggressive minor transformation, finite reinforcements, target selection, expansion pressure, Fury focus and decisions, terminal route. | Active |
| 8 | Tensions Rising | World-tension shocks, diplomatic fever stages, relation damage, AI posture, follow-up incidents, border-war escalation. | Active |
| 9 | White Peace | Safe status-quo war selection, dynamic repeatable cap, single or multi-pair peace branches, settlement memory. | Active |
| 10 | Death | Hidden island consumption, maritime evidence, coastal reveal, wasteland spread, ghost hosts, Death country, continent consumption, Last Shores. | Active |
| 11 | Secret Alliance | Fixed player target, concealed coalition, investigation and counterplay, reveal, coalition war, settlement, achievements, manual scenario. | Active |
| 12 | Africa | Pan-African formation, charter autonomy, continental focus AI, world-order responses, evolutions, priority-member content. | Partial release candidate. Its source document does not claim the whole gameplay and presentation package is complete. |
| 13 | Natural Disasters | Exact-state disasters, warnings, delayed impacts, Deaths, building damage, aftermath cards, recovery missions, disaster seasons. | Active |
| 14 | Cannibalism | War-exposure selection, Hunger, Command Integrity, cults, network spread, finite Larder, warlords, convergence, terminal routes. | Active |
| 15 | Utopia Manifesto | Country transformation, planned society routes, island lease, replacement focus tree, decisions, missions, characters, identities, achievements. | Complete against its frozen accepted event package |
| 16 | Brilliant Scientist | Doctor Kruger, Directorate, project portfolio, foreign operations, containment, Kruger State, terminal routes, achievements, aftermath. | Active core package. Additional report, flavor, model, and consumer-validation work remains open. |
| 17 | Random Faction | Dynamic minor selection, live faction discovery, forced alignment, regional pressure, cascades, leader reactions, achievements. | Implemented in source and cataloged as Needs Testing |
| 18 | Resources Found | Persistent resource fields, enrichment, exploitation, contracts, incidents, cave breach, Oth-Kesh Host, Deep War terminal route. | Active |
| 19 | Infantry Spawn | Weighted formation lots, origin and obligation ledgers, claimant pressure, derivative countries, focus and decision systems, manual scenario. | Fully functional in its completion records |
| 20 | Black Plague | State disease lifecycle, shared response, countermeasures, Rat Nations, Rat King, weaponization, terminal progression, manual scenario. | Active. Additional narrative and bespoke 3D asset work remains a later tranche. |
| 163 | Doctor Wu | Weighted clinical host, persistent host-transfer API, Black Plague response integration. | Active |

Canonical event documents:

- [Event 001 Communist Insurgency](docs/events/001_communism_spread.md)
- [Event 002 Zombie Outbreak](docs/events/002_zombie_outbreak.md)
- [Event 003 The Holy Realm](docs/events/003_holy_realm.md)
- [Event 004 Random War](docs/events/004_random_war.md)
- [Event 005 Soviet Collapse](docs/events/005_soviet_collapse.md)
- [Event 006 Independence Wave](docs/events/006_independence_wave.md)
- [Event 007 Fury](docs/events/007_fury.md)
- [Event 008 Tensions Rising](docs/events/008_tensions_rising.md)
- [Event 009 White Peace](docs/events/009_white_peace.md)
- [Event 010 Death](docs/events/010_death.md)
- [Event 011 Secret Alliance](docs/events/011_secret_alliance.md)
- [Event 012 Africa](docs/events/012_africa.md)
- [Event 013 Natural Disasters](docs/events/013_natural_disasters.md)
- [Event 014 Cannibalism](docs/events/014_cannibalism.md)
- [Event 015 Utopia Manifesto](docs/events/015_utopia_manifesto.md)
- [Event 016 Brilliant Scientist](docs/events/016_brilliant_scientist.md)
- [Event 017 Random Faction](docs/events/017_random_faction.md)
- [Event 018 Resources Found](docs/events/018_resources_found.md)
- [Event 019 Infantry Spawn](docs/events/019_infantry_spawn.md)
- [Event 020 Black Plague](docs/events/020_black_plague.md)
- [Event 163 Doctor Wu](docs/events/163_doctor_wu.md)

### Germany, Mengele, and the Tibet Expedition

The Germany Mengele chain is a normal HOI4-triggered country mechanic rather than a random-event-pool entry. It connects Auschwitz experiments, Mengele autonomy, an Angel of Death civil-war route, Final Solution decisions, a Tibet expedition, cloning projects, camps, Condemnation, Deaths, world threat, Holy Realm reactions, and later terminal consequences.

Canonical reference: [Mengele and Tibet Expedition](docs/events/germany_mengele.md).

### Fallout living-world memories

Fallout owns a separate scheduled country-memory ecosystem. These incidents use `chaosx.fallout` identities, country and state registries, survival resources, cause memory, successor packages, delayed callbacks, and the dedicated Fallout Event Log type.

The Fallout rows in the event catalog are not normal random events and do not enter the standard event-weight pool.

---

## Cross-event country, UI, and support systems

### Liberation release coordinator

The release coordinator synchronizes country-release systems that can collide, especially Soviet Collapse and Independence Wave. It protects host survival, state reservations, transaction ownership, rollback, and joint presentation.

Canonical reference: [Liberation Release Coordinator](docs/systems/liberation_release_coordinator.md).

### Country and formable registries

Event-created countries use shared carrier collections, provenance, package identity, active-generation state, and collision-safe formable contracts.

Event 006 adds a dedicated country registry, formable registry, package admission rules, regional package overlays, rival blocs, and fail-closed formable readiness.

Canonical references:

- [Independence Wave Country Registry](docs/systems/006_independence_wave_country_registry.md)
- [Independence Wave Formable Registry](docs/systems/006_independence_wave_formable_registry.md)
- [Chaos Unit Family Registry](docs/systems/chaos_unit_family_registry.md)

### Startup history compatibility

Additive technologies, equipment, facilities, and character grants for existing countries are applied through the startup compatibility layer rather than copied vanilla history files.

Canonical reference: [Startup History Compatibility Grants](docs/systems/startup_history_compatibility.md).

### Custom achievements

Chaos Redux uses a shared achievement registry and event-owned achievement packages. Achievement logic records real route, survival, origin, scenario, and forced-run disqualifiers. Event-owned documents remain authoritative for exact conditions.

Canonical references:

- [Custom Achievements](docs/systems/custom_achievements.md)
- [Independence Wave Achievements](docs/systems/006_independence_wave_achievements.md)
- [Brilliant Scientist Achievements](docs/systems/016_brilliant_scientist_achievements.md)

### State map modes

Custom map modes expose state-level system data such as disease, contamination, camp or repression state, and event-owned map overlays. Rebuilds are system-owned and should occur after a transaction commits rather than during every intermediate mutation.

Canonical reference: [State Map Modes](docs/systems/state_map_modes.md).

### Main menu, welcome, and help

The mod includes a custom main menu, welcome surface, settings interface, Event Log, Chaos Meter, super-event presentation, scenario window, and a dedicated help window.

Canonical references:

- [Main Menu Redesign](docs/systems/main_menu_redesign.md)
- [Chaos Redux Help Window](docs/systems/chaosx_help_window.md)
- [GFX, Icon, Flag, and Map Mode Registry](docs/systems/gfx_icon_flag_mapmode_cleanup.md)

### 3D runtime assets

Chaos Redux has a registered 3D unit and facility asset pipeline with explicit model, material, animation, scale, entity, and runtime-consumer contracts. A model package is not a gameplay mechanic until its unit, building, entity, action, and map consumer are wired.

Canonical references:

- [Chaos Warfare Facility Models](docs/systems/chaos_warfare_facility_models.md)
- `docs/specs/chaos_redux_3d_model_workflow_planning_package/`
- `docs/assets/chaos_redux_3d_model_pilots/`

---

## Multiplayer, AI, and performance model

### Multiplayer state

The random-event registry, Chaos Meter, world-end state, event histories, clusters, and global consequence ledgers are shared campaign state.

Player-country UI state, selected rows, open windows, sorting, and manual input buffers are stored on the relevant player country. The event framework preserves actor context and does not assume that the current player is the target unless the event or scenario explicitly defines that contract.

Settings that change shared simulation values affect the campaign. Presentation preferences and local window state remain player-facing controls.

### AI

Persistent event packages provide route-aware AI for their decisions, focus paths, diplomacy, production, research, country transformation, response systems, and terminal readiness.

The CBRN AI:

- requires real technology, industry, stock, protection, policy, and route state.
- receives no free readiness or payload.
- avoids unsupported delivery surfaces.
- uses differentiated country profiles.
- treats nonhuman countries as ineligible for ordinary institutional CBRN behavior.

### Performance

The main performance rules are:

- automatic event firing uses the registered pool rather than scanning unrelated content.
- event-owned systems use bounded arrays, active-state registries, delayed callbacks, and tag-scoped on-actions.
- clusters count once for pacing.
- target-heavy decisions use narrowed eligibility.
- custom systems avoid general daily, weekly, or monthly world iterations.
- exact-state systems rebuild map or UI views after committed changes rather than at every calculation step.

---

## Inspection and manual controls

### Live inspection

The main inspection surfaces are:

- Event Log Status for current timer, weights, counts, and tuning.
- Event Log History and Evolutions for recorded incidents.
- Events for live availability, type, weight, fired count, and enable state.
- Clusters for cluster chance and member state.
- Event Details for event-specific prose, evolutions, and public terminal routes.
- Chaos Meter History for exact Chaos causes.
- Air Cleanliness for atmospheric sources and thresholds.
- Condemnation for public responsibility and sanctions.
- Deaths for civilian and military totals and recent causes.
- CBRN action records through their dedicated Event Log entries.
- optional event-system log output.

### Manual controls

The settings UI can:

1. select and fire an event.
2. select a random valid event by type.
3. force an event for bounded testing.
4. enable or disable events and evolutions.
5. enable, disable, inspect, or manually fire clusters.
6. inspect and toggle public world-end branches.
7. launch a triggerable scenario after confirmation.
8. change timer, weight, Chaos, and presentation settings.
9. export the current settings state.

Automatic event-fire log output is disabled by default. It can be enabled from the settings surface when a source-level behavior needs inspection.

---

## Canonical documentation map

### Shared framework

- `docs/systems/dynamic_major_event_weights.md`
- `docs/systems/event_clusters.md`
- `docs/systems/events_log_window.md`
- `docs/systems/events_log_evolutions_and_clusters.md`
- `docs/systems/events_log_world_end_scenarios.md`
- `docs/systems/triggerable_scenarios.md`
- `docs/systems/settings_miscellaneous_menu.md`
- `docs/systems/settings_numeric_manual_inputs.md`
- `docs/systems/chaosx_settings_export.md`

### Chaos and global consequences

- `docs/systems/chaos_meter_popup_window.md`
- `docs/systems/chaos_meter_deaths_mechanic.md`
- `docs/systems/air_contamination_mechanic.md`
- `docs/systems/air_cleanliness_treaty.md`
- `docs/systems/condemnation_sanctions.md`
- `docs/systems/world_threat_mechanic.md`
- `docs/systems/nuclear_chaos_ladder.md`

### CBRN and Chaos Warfare

- `docs/systems/chaos_warfare_doctrine.md`
- `docs/systems/cbrn_operations_surface.md`
- `docs/systems/cbrn_hq_command.md`
- `docs/systems/cbrn_chemical_delivery.md`
- `docs/systems/cbrn_action_records.md`
- `docs/systems/cbrn_diplomacy_actions.md`
- `docs/systems/cbrn_designers.md`
- `docs/systems/cbrn_biological_ai.md`
- `docs/systems/cbrn_battlefield_operations.md`
- `docs/systems/cbrn_occupation_and_nerve_suppression.md`
- `docs/chemical_warfare/`
- `docs/biological_warfare/`

### Camps and repression

- `docs/systems/genocide_crisis_system.md`
- `docs/systems/genocide_mechanics_spec.md`
- `docs/systems/cbrn_camp_integration.md`

### Events and countries

- `docs/events/`
- `docs/systems/006_independence_wave_country_registry.md`
- `docs/systems/006_independence_wave_formable_registry.md`
- `docs/systems/liberation_release_coordinator.md`
- `docs/systems/startup_history_compatibility.md`

### UI, assets, and catalogs

- `docs/systems/state_map_modes.md`
- `docs/systems/custom_achievements.md`
- `docs/systems/main_menu_redesign.md`
- `docs/systems/chaosx_help_window.md`
- `docs/systems/gfx_icon_flag_mapmode_cleanup.md`
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`

## Future maintenance

Update this guide whenever one of the following changes:

- event classification, timer, weight, or cluster behavior.
- Chaos tiers or global consequence thresholds.
- a public world-end registry entry.
- the triggerable-scenario registry.
- the active or fail-closed status of a CBRN delivery surface.
- the completion boundary of a major event package.
- a shared country, formable, achievement, map-mode, or UI system.

Do not copy detailed tuning from a subsystem into this guide unless the value is central to understanding the shared model. Keep detailed mechanics in the canonical subsystem document and keep this file as the current map of the whole mod.
