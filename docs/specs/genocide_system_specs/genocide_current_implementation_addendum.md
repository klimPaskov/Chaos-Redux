# Camps and Genocide System Rework: Current Implementation Connection Addendum v2

## Verdict

Implement this as a patch and expansion of the existing `genocide_crisis` system, not as a new random event and not as a new parallel file family. The current system already has named script files, building IDs, state responsibility tracking, an active camp-state registry, a monthly pulse, Deaths integration, discovery-based condemnation, AI strategy, and Germany-Mengele integration. Preserve that spine and extend it.

This addendum supersedes all earlier package wording that suggested parallel `chaosx_genocide_*` files, a new standalone `docs/systems/genocide_system.md`, Soviet document-exposure wording, or a vague chemical placeholder.

## Hard corrections from the user

### Soviet Collapse has no leak or record reveal content

The Soviet Union must never receive leaked-report style genocide events. Do not add or keep:

- leaked Soviet files
- archive reveal events
- record reveal events
- journalist leak events
- stolen document events
- exposed folder events
- random internal report popups
- any Soviet Collapse event that exists mainly to expose documents or reports

The Soviet Collapse connection is internal and mechanical only. Gulag repression can change collapse opening values, but it must not expose records. Public discovery still belongs to the existing physical discovery model, such as enemy occupation or liberation of a state with discoverable atrocity infrastructure.

### Nerve-agent integration must be grounded in HOI4 systems

Do not write a vague abstract button. Do not write real-world operational method text. Implement the feature as a believable HOI4 decision bridge from existing chemical warfare and special-project mechanics into existing camp-site mechanics.

A country that has the required nerve-agent research, chemical special project, or existing chemical-warfare flag may unlock state-targeted camp escalation decisions. Those decisions must require eligible controlled camp infrastructure, consume game stockpile or production capacity, raise Deaths-system output, increase hidden evidence severity, add contamination or accident pressure through existing chemical helpers, and worsen future discovery condemnation.

## Keep the current implementation spine

Use these current file surfaces as the implementation base:

- `common/script_constants/genocide_crisis_constants.txt`
- `common/buildings/chaosx_buildings.txt`
- `common/decisions/categories/genocide_crisis_categories.txt`
- `common/decisions/genocide_crisis_decisions.txt`
- `common/scripted_effects/genocide_crisis_effects.txt`
- `common/scripted_triggers/genocide_crisis_triggers.txt`
- `common/on_actions/genocide_crisis_on_actions.txt`
- `common/on_actions/chaosx_on_actions_chaos_meter.txt`
- `events/genocide_crisis_events.txt`
- `common/ai_strategy/genocide_crisis_ai_strategy.txt`
- `common/dynamic_modifiers/genocide_crisis_dynamic_modifiers.txt`
- `common/ideas/genocide_crisis_ideas.txt`
- `common/opinion_modifiers/genocide_crisis_opinion_modifiers.txt`
- `interface/chaosx_buildings.gfx`
- `gfx/entities/chaosx_buildings.asset`
- existing localisation files named by the current genocide crisis documentation

Do not create replacement files such as `chaosx_genocide_effects.txt`, `chaosx_genocide_triggers.txt`, `chaosx_genocide_decisions.txt`, or `chaosx_genocide_l_english.yml` if the current files exist. Patch the existing files.

## Preserve the current state model

Keep the current building IDs:

- `concentration_camp`
- `extermination_camp`
- `gulag_labor_camp_network`

Keep the current responsible-authority variable:

- `genocide_responsible_country`

Use `genocide_responsible_country` for discovery, Deaths ownership context, condemnation, tribunal severity, and any later responsibility logic. Do not replace it with `camp_responsible_country` or another parallel variable.

Keep the current active-state processing model:

- active states are registered into `global.genocide_active_camp_states`
- monthly processing runs from `genocide_monthly_global_pulse`
- the pulse is reached through the existing host-only Chaos Meter monthly on-action

Do not add a separate all-country monthly scan. If a new feature needs ticking, register only the affected states and process them through the existing active-state array.

## Required implementation work

The requested work is an expansion of the current system. It should focus on missing country-specific decisions, stronger ticking-death behavior, cleanup of nuisance events, and real cross-system integration.

Required work:

1. Verify that active concentration camps, extermination camps, Gulag networks, and experiment-linked sites really call the shared Deaths pipeline and reduce real state population. If docs claim this but script does not, wire it through `genocide_monthly_global_pulse` and `global.genocide_active_camp_states`.
2. Add or finish German Holocaust decisions inside the existing genocide decision files. These should unlock in the 1940s under eligible fascist, Nazi-equivalent, historical, or radicalized conditions, with territorial and war-state gates.
3. Add or finish Japanese occupation atrocity, forced-labor, and experimentation decisions. These should require war with China or a configured Chinese target bloc and valid occupied Chinese, Manchurian, or occupation-specific target states.
4. Add or finish Soviet Gulag decisions. These should represent Gulag expansion, deportations, forced labor, purges, famine pressure, and repression, not a German-style extermination path by default.
5. Connect Soviet Gulag repression to Soviet Collapse opening values. Heavy repression can weaken early opposition, reduce initial republic momentum, delay first resistance escalation, or reduce starting force packages, but it must create long-term grievances and must never prevent full collapse when collapse threat reaches max.
6. Remove leaked-file, stolen-document, journalist-leak, exposed-folder, and similar nuisance events from the camp flow entirely. Preserve useful effects only by calling them from concrete discovery, liberation, capitulation, tribunal, state-control, or aftermath logic.
7. Add the grounded HOI4 nerve-agent or restricted-chemical bridge through existing chemical research, special-project, doctrine, stockpile, and contamination systems. It must be state-targeted, costed, gated, and tied to existing camp sites.
8. Update documentation and localisation so player-facing text describes visible actions and consequences without update-history language, real-world procedural detail, or hidden future spoilers.

## Leaks, reports, and discovery cleanup

The current system should keep hidden pressure and physical discovery. It should remove random nuisance leak events.

Keep:

- `genocide_visibility`
- `hidden_atrocity_score`
- `genocide_discovered_sites`
- concrete discovery from state occupation or liberation
- capitulation and tribunal preparation hooks
- discovery condemnation that targets `genocide_responsible_country`
- internal decision consequences when they create meaningful player choices

Remove or disable from the active camp flow:

- leaked files events
- stolen folder events
- journalist leak events
- exposed document events
- repeated camp report popups
- random minor leaks that only interrupt the player

For the Soviet Union, do not replace removed leak events with any Soviet Collapse document reveal. Soviet repression should affect collapse mechanics through variables, state memories, modifiers, and starting setup, not through leaked reports.

If a removed event contains useful gameplay effects, keep the helper effect and call it from a concrete trigger. Do not leave the event as a random or nuisance popup.

## German decision integration

Do not create a separate Holocaust subsystem. Add Germany-specific decisions and helpers to the existing `genocide_crisis` system.

Use the existing Auschwitz and Mengele integration where it exists:

- state `88`
- province `9412`
- `genocide_auschwitz_experiment_site`
- `genocide_ss_laboratory_site`
- `mengele_autonomy`
- `mengele_permission_level`
- Auschwitz Directorate condemnation handling when that faction exists

Required German decision families:

- activate or expand wartime camp administration
- escalate occupied Poland and Auschwitz-area infrastructure
- centralize deportation logistics through abstract train, rail, and supply costs
- expand extermination sites from eligible concentration camp states
- intensify extermination policy at high cost and high future discovery risk
- transfer prisoners to experimental facilities only when the Mengele or Auschwitz chain allows it
- destroy camp or laboratory evidence only when state loss is plausible
- enable nerve-agent or restricted-chemical camp escalation only when the chemical warfare system supports it and eligible sites exist

Unlock logic:

- limited preparatory actions may appear from 1940 if fascist Germany is at war or controls eligible occupied territory
- stronger Holocaust decisions usually require 1941 or later, occupied Poland or Auschwitz-area control, major-war context, radical route flags, or high genocide escalation
- high-chaos or radicalized flags may accelerate the opening, but do not silently create full 1936 Holocaust decisions
- democratic, liberal, or non-radical Germany must not see these decisions

## Japanese decision integration

Japan needs a separate occupation and experimentation identity. Do not copy the German camp path.

Use the current system's biological integration where available. Prisoner experimentation should connect to existing anthrax, tularemia, plague, outbreak, contamination, biological special-project, and Deaths helpers where those exist.

Required Japanese decision families:

- expand forced labor sites in occupied Chinese or Manchurian target states
- conduct occupation reprisals as an anti-resistance action with later blowback
- intensify forced-labor extraction at population, resistance, and discovery cost
- transfer prisoners to experimental facilities
- escalate biological research through game-level experimentation if relevant biological research or special-project progress exists
- destroy experimental evidence only when state loss is plausible

Targeting must be dynamic and bounded. Japan should not receive a wall of state decisions. Use a selected-target flow, capped target list, priority target pool, or an existing dynamic target pattern.

Eligibility must require war with China or the configured Chinese target bloc plus controlled eligible Chinese, Manchurian, or occupation-specific target states. Korea and Manchuria can have starting occupation repression markers, but active China escalation should require war or occupied Chinese territory.

## Soviet Gulag and Soviet Collapse integration

The Soviet system should remain Gulag, deportation, forced labor, purge, famine pressure, and mass repression first. It should not become a German-style extermination system by default.

Required Soviet decision families:

- expand `gulag_labor_camp_network` in selected remote, borderland, or hostile regions
- deport suspected opposition groups
- purge regional administrators
- suppress nationalist or republic organizers
- intensify forced labor quotas
- mobilize Gulag labor for limited construction or extraction gains
- apply famine pressure only through existing safe game abstractions and state effects
- destroy camp or NKVD evidence only when invasion, collapse, or state loss is plausible, without leaked-report events

Soviet Collapse bridge:

- Store suppression memories by state, region, republic target, or collapse-relevant group when Soviet decisions hit republic regions.
- During Soviet Collapse release setup, read those memories to reduce initial republic momentum, reduce first resistance pressure, delay early MTTH escalation, lower local organization, or weaken initial unit packages.
- Store grievances separately. Heavy repression should increase hatred, refusal to negotiate, local instability, foreign sympathy for released republics, later discovery condemnation if physical sites are captured, and post-collapse radicalization risk.
- At max Soviet Collapse threat, all possible releasables must still break away. Gulag suppression can change opening strength and timing, not the mandatory release outcome.
- Do not add leaked records, archive reveal, report reveal, or document exposure events to make this bridge visible. The player should see the mechanical result in collapse difficulty and republic opening conditions.

Use names that match the current Soviet Collapse implementation if it already has republic momentum, threat, resistance, release, or starting-force helper variables. If those names do not exist, add a small adapter helper in the Soviet Collapse scripted effects and document it.

## Grounded HOI4 nerve-agent and restricted-chemical bridge

This bridge belongs in the existing genocide and chemical warfare systems. It must not include real-world procedures, technical handling, production descriptions, or method text.

Unlock requirements should inspect existing chemical warfare code and use real repo flags, technologies, doctrines, special projects, stockpile variables, or scripted triggers. Possible anchors may include:

- nerve-agent research or special-project completion flags
- advanced chemical stockpile variables
- chemical raid or chemical air-delivery unlocks
- Chaos Warfare chemical suppression or contaminant-firebases unlocks
- relevant safety, logistics, or doctrine gates

The final implementation must use the actual repo identifiers found during inspection, not invented placeholder flags.

Decision shape:

- visible only to countries with eligible ideology, extreme route, or country-specific atrocity chain
- requires an existing eligible active camp, extermination camp, Gulag escalation site, or experimental site
- requires controlled target state and valid `genocide_responsible_country`
- costs chemical stockpile, production capacity, command capacity, security/logistics burden, or other existing chemical-system resources
- applies a temporary state flag or modifier to the selected site
- increases Deaths-system ticks for that site for a limited period
- adds contamination or air-cleanliness pressure through existing helpers
- increases hidden `genocide_visibility` and evidence severity
- increases future discovery condemnation
- increases accident or exposure risk when safety, stability, or logistics are weak

Player-facing wording should use existing in-game tech names if they exist. Otherwise use broad names such as restricted chemical stockpile, nerve-agent stockpile, chemical extermination escalation, or chemical site escalation. Do not describe how the weapon is made, stored, handled, or used.

This is not a global magic button. It is a decision bridge that uses existing HOI4-style research, stockpile, site, state, cost, and consequence systems.

## Documentation updates

Update:

- `docs/systems/genocide_crisis_system.md`
- `genocide_mechanics_spec.md` only if it still exists in the repo as a source spec, plan, or legacy doc that agents read
- `CHAOS_REDUX_MECHANICS.md`
- any touched Deaths, Condemnation, Chemical Warfare, Biological Warfare, Soviet Collapse, or Mengele docs
- localisation for all new and removed visible decisions, events, ideas, modifiers, and tooltips

The docs should say the system is `genocide_crisis`, not a new `chaosx_genocide` system. They should also state that Soviet Collapse integration has no leaked-report or archive-reveal events.

## Validation contract

Validation should prove the meaningful behavior, not restate generic syntax rules.

Required checks:

- active states are the only monthly camp-death loop
- active camp sites reduce real state population through the shared Deaths system
- Deaths tab reasons work for concentration camps, extermination camps, Gulag repression, and experiment-linked deaths where implemented
- discovery condemnation uses `genocide_responsible_country`
- Germany decisions unlock only for eligible Germany routes, dates, war states, and territories
- Japan decisions unlock only during war with China or the configured Chinese target bloc and only for valid occupied targets
- Soviet Gulag decisions feed Soviet Collapse opening values without blocking mandatory max-threat release
- no Soviet leak, report reveal, archive reveal, or record reveal content exists in the Soviet Collapse bridge
- removed leak events no longer fire from the camp system
- nerve-agent or restricted-chemical decisions use existing chemical flags, research, special projects, and stockpile variables
- chemical bridge decisions are state-targeted, site-gated, costed, and consequence-bearing
- AI weights are bounded and cannot use invalid targets
- localisation is complete and does not expose hidden future outcomes
- docs match the final implementation

## Acceptance standard

The work is complete only if the existing `genocide_crisis` system is extended cleanly. A parallel new system, renamed file family, fake hidden death substitute, random leak-event workaround, Soviet document reveal, vague chemical placeholder, missing Soviet Collapse bridge, missing country-specific decisions, or unresolved AI and localisation gap is incomplete.
