# Event 22 Concentration Camps Event Chain Map

## Purpose

This file maps the Event 22 report, country, news, and hidden worker events. It gives implementation a complete chain without writing final localisation or locking numeric IDs before the repository collision audit.

## Namespace and ID allocation

Recommended namespace:

```text
chaosx_event_022
```

Recommended range ownership:

| Range | Owner |
| --- | --- |
| `.1` to `.49` | global dispatch, opening, and package handoff |
| `.50` to `.99` | policy transition and category initialization |
| `.100` to `.199` | baseline incidents |
| `.200` to `.299` | Evolution I |
| `.300` to `.399` | Evolution II |
| `.400` to `.499` | Evolution III |
| `.500` to `.599` | evidence, inspection, and public discovery |
| `.600` to `.699` | liberation and relief |
| `.700` to `.799` | succession, civil war, annexation, and reuse |
| `.800` to `.899` | accountability, displacement, closure, and aftermath |
| `.900` to `.949` | news events if the repository keeps them in the same namespace |
| `.950` to `.999` | hidden worker and bounded debug events |

The implementation must inspect current namespace usage and lock collision-free numeric IDs. Semantic working names below remain the design reference.

## Event-chain diagram

```text
Shared random-event picker
  -> Event 22 global dispatch
      -> choose eligible country
          -> country-specific package handoff, when valid
          -> generic first opening, when never fired
          -> repeat incident dispatch, when active or dormant

First opening
  -> calculate and register network
  -> player or AI selects policy
  -> category and pulse registration
  -> baseline incidents and missions

Evolution activation
  -> active-country evolution worker
  -> evolved first opening for untouched countries
  -> evolution report and history

Evidence route
  -> credible report
  -> investigation or inspection
  -> verified site
  -> verified network
  -> shared Condemnation and foreign reaction

Control-loss route
  -> retreat emergency
  -> liberation state transition
  -> relief and evidence work
  -> displacement and accountability
  -> transparent closure, unresolved aftermath, or successor reuse
```

## Event surface rules

- Hidden worker events never show player text.
- One player-facing report should normally summarize one setup batch.
- Large networks should not generate one popup per state.
- State incidents can show a named priority state and apply bounded regional effects.
- News events are reserved for a verified large network, major liberation, or major accountability threshold.
- Routine operation pulses use the Deaths ledger, state status, and category values. They do not show monthly popups.
- Final text uses dynamic country, state, policy, site type, and target-purpose localisation.

## Global and opening events

### `chaosx_022_global_dispatch`

Type: hidden country or global dispatch event, according to shared random-event framework.

Purpose:

- receive Event 22 selection from the shared picker
- build complete country candidate pool
- select one country
- record cluster source when applicable
- call first opening, country-package handoff, or repeat dispatch

Failure behavior:

- no candidate means a logged skip
- invalid selected actor after delay means fail closed
- no substitute actor is selected outside the original accepted job unless the shared picker explicitly reruns the entire event selection

### `chaosx_022_package_handoff`

Type: hidden country event.

Purpose:

- detect established German, Japanese, or Soviet ownership
- pass Event 22 opening stage, evolution stage, target coverage, and generation to the country package
- hide generic category
- preserve global Event 22 history

Required outputs:

- adapter success flag
- created or activated site count
- current policy
- category owner
- failure reason when package cannot accept the call

A failed handoff returns to a reviewed generic adapter only when the country package explicitly supports that fallback.

### `chaosx_022_network_opening`

Type: player-facing country report.

Recipients:

- selected country

Pre-effect:

- complete or schedule initial site registration
- calculate opening coverage and evolution split
- initialize Network Reach, Exposure, Resistance Pressure, and network generation

Text direction:

- several detention sites now operate across named or implied regions
- trains, guards, factories, local authorities, and families already feel the effect
- government must decide whether to close, review, exploit, or expand
- evolved opening also identifies that some sites have a killing function

Options:

- immediate closure
- restrictive review
- forced-labour administration
- security expansion
- extermination opening only when valid

Follow-up:

- policy initialization event or effect
- event history row
- category reveal

### `chaosx_022_opening_setup_complete`

Type: hidden country worker.

Purpose:

- confirm delayed setup finished
- compare actual count with target count
- apply pre-fire Evolution II or III shock when required
- initialize operation pulse
- clear temporary setup targets
- report skipped states and reasons

Do not open the category before required site registration is stable, unless the category can safely show setup in progress.

### `chaosx_022_policy_initialized`

Type: hidden country event or effect.

Purpose:

- store national policy
- add or update staged national idea
- activate correct decision mode
- set AI profile
- schedule first bounded incident window

## Repeat dispatch and baseline incidents

### `chaosx_022_repeat_incident_dispatch`

Type: hidden country event.

Purpose:

- evaluate valid incident families
- choose one through audited weights
- avoid filler when no threshold exists

Candidate incident events follow.

### `chaosx_022_labour_quota_breakdown`

Type: country report with selected state.

Trigger direction:

- one or more forced-labour assignments near workforce, supply, disease, or sabotage collapse

Text direction:

- output orders continue while work gangs, guards, and railway managers report that the system cannot meet another quota

Options:

- reduce intensity and lose output
- transfer or import detainees from a valid source
- restore food and medicine
- force the quota, causing deaths and collapse risk
- close the assignment

Follow-up:

- state mission or immediate assignment transition

### `chaosx_022_coordinated_escape`

Type: country report with selected state.

Trigger direction:

- Resistance Pressure threshold
- escape network and guard weakness

Options:

- improve conditions and negotiate surrender of the crisis
- reinforce guards
- conduct a targeted security operation
- use violent suppression for valid perpetrator routes

Outcomes:

- release or escape population transfer
- testimony and exposure
- deaths and evidence
- state resistance shift

### `chaosx_022_camp_epidemic`

Type: country report with selected state.

Trigger direction:

- overcrowding, famine, plague, low air cleanliness, contamination, or destroyed infrastructure

Options:

- deliver medical and food relief
- isolate humanely with release conditions
- abandon the site
- conceal the outbreak
- continue work despite disease

Cause ownership:

- disease system owns disease spread
- Event 22 owns confinement, deliberate neglect, and additional camp mortality

### `chaosx_022_administrator_corruption`

Type: country report.

Trigger direction:

- confiscated property, centralized administration, high output, weak oversight

Options:

- investigate and preserve records
- replace local administration
- tolerate theft to keep output
- purge officials, with possible inward-broadening consequence

### `chaosx_022_military_objection`

Type: country report.

Trigger direction:

- high deaths, extermination, forced evacuation, or purge of core supporters
- officer loyalty or civil-service resistance

Options:

- halt or review orders
- remove objectors
- compromise on intensity
- allow an independent inspection

Possible follow-up:

- hardliner coup pressure
- underground network
- Event 21 civil-war bridge

### `chaosx_022_foreign_leak`

Type: perpetrator-side report and observer-side report.

Trigger direction:

- escapee, railway records, family search, foreign intelligence, or administrator defection

Perpetrator options:

- restrict access
- falsify records
- investigate the leak
- begin transparent review

Observer options:

- investigate
- protect witness
- share with allies
- demand access

### `chaosx_022_disaster_exposes_site`

Type: affected controller report and observer report when access exists.

Trigger direction:

- Event 13 damage reveals records, remains, survivors, or site infrastructure

Options:

- relief and secure evidence
- conceal and repair
- abandon
- request foreign aid

### `chaosx_022_underground_network_revealed`

Type: successor or closing-government report.

Trigger direction:

- central closure order and local continued operation

Options:

- prosecute operators
- negotiate surrender
- expose the network publicly
- restore coercive central control

Follow-up:

- underground-network mission
- responsibility for national and local actors

### `chaosx_022_target_source_exhausted`

Type: perpetrator-side country report.

Trigger direction:

- no valid intake remains for current target purpose
- regime refuses automatic closure

Options:

- close the network
- reduce to dormant detention
- seek another valid existing campaign target source
- broaden purge into core population for an extreme route

No option can invent an ethnicity.

### `chaosx_022_restricted_site_accident`

Type: country and state report.

Trigger direction:

- restricted chemical operation, stockpile handling, bombardment, or contamination failure

Options:

- stop and decontaminate
- conceal and continue
- evacuate nearby population
- abandon the site

System calls:

- stockpile
- contamination
- exact deaths
- evidence
- discovery

## Evolution I events

### `chaosx_022_evolution_1_global`

Type: hidden global evolution event plus shared evolution log.

Purpose:

- mark Evolution I available
- register active countries for conversion jobs
- change future first-opening package

### `chaosx_022_evolution_1_country_report`

Type: player-facing affected-country report.

Pre-effect:

- count valid concentration sites
- calculate `floor(valid_count / 2)` conversions
- select states through audited score
- queue conversions

Text direction:

- part of the existing network has received a different purpose and chain of command
- transport and killing orders replace ordinary detention or labour policy in selected sites

Options:

- accept national extermination policy when valid
- halt conversion and start closure conflict
- contain conversion through review
- allow country-specific response

The event option does not change the required automatic conversion count for an explicit evolved opening unless the accepted one-site policy gate applies.

### `chaosx_022_evolution_1_single_site_crisis`

Type: country report.

Trigger:

- one valid concentration site
- no explicit extermination policy

Options:

- convert
- refuse and close
- place under review
- allow local underground conversion risk

### `chaosx_022_evolution_1_setup_complete`

Type: hidden worker.

Purpose:

- verify exact conversion count
- remove incompatible assignments
- preserve markers and evidence
- start extermination pulses
- write evolution history

## Evolution II events

### `chaosx_022_evolution_2_global`

Type: hidden global evolution event plus shared evolution log.

Purpose:

- mark Evolution II available
- register every active network for the 1 percent job
- change future opening package

### `chaosx_022_evolution_2_country_report`

Type: player-facing country report after or during the batched effect.

Text direction:

- deaths and disappearances rise across every camp state during a synchronized escalation
- state reports show a shared policy, supply collapse, or deprivation pattern

Options:

- continue policy
- reduce intensity
- begin closure
- investigate unauthorized escalation

The options affect future operation. They do not undo the exact applied loss.

### `chaosx_022_evolution_2_state_worker`

Type: hidden state worker.

Contract:

- validate active site and generation
- skip marked state
- request 1 percent current population
- call exact helper
- log actual loss
- set marker even when protected floor produces zero
- add evidence and resistance based on actual loss

### `chaosx_022_evolution_2_complete`

Type: hidden country worker.

Purpose:

- total actual loss
- skipped-state ledger
- clear batch state
- write evolution history

## Evolution III events

### `chaosx_022_evolution_3_global`

Type: hidden global evolution event plus shared evolution log.

Purpose:

- mark Evolution III available
- register active networks for coverage and shock jobs
- change future first opening to the late-stage package

### `chaosx_022_evolution_3_country_report`

Type: player-facing affected-country report.

Pre-effect:

- calculate 50 percent coverage target
- calculate final concentration and extermination minimum split
- queue additions and conversions
- queue 2 percent shock

Text direction:

- the camp system now reaches half of eligible state administration
- trains, guards, labour, killings, resistance, disease, and evidence have become a national crisis

Options:

- attempt emergency national closure
- keep a mixed detention and extermination network
- intensify an explicit extremist route
- allow country-specific response

### `chaosx_022_evolution_3_site_setup_worker`

Type: hidden state worker.

Purpose:

- add or convert site
- preserve existing extermination sites
- use concentration extra for odd split unless route overrides
- register responsibility and generation
- set pre-fire Evolution III rule so no Evolution II shock follows

### `chaosx_022_evolution_3_shock_worker`

Type: hidden state worker.

Contract:

- request 2 percent current population
- call exact helper
- log actual loss
- set Evolution III marker
- do not set or apply Evolution II shock for a new pre-fire late-stage site

### `chaosx_022_evolution_3_complete`

Type: hidden country worker.

Purpose:

- verify final reach and split
- total actual loss
- record skipped states
- activate late-stage category
- write history

## Evidence and inspection events

### `chaosx_022_first_credible_report`

Type: observer report.

Trigger:

- first fragmentary evidence source reaches a valid observer

Options:

- investigate
- protect witness
- share evidence
- dismiss
- suppress for alliance or domestic reasons

A dismissal does not delete the evidence.

### `chaosx_022_inspection_requested`

Type: responsible-country report.

Options:

- grant real access
- grant restricted access
- stage the site
- reject access
- begin closure before inspection

Follow-up:

- inspection outcome event

### `chaosx_022_inspection_outcome`

Type: responsible and inspector reports.

Outcome inputs:

- access quality
- evidence
- witnesses
- cover-up
- foreign intelligence
- state control

Results:

- no verification
- credible suspicion
- verified state
- failed cover-up and linked-site lead

### `chaosx_022_site_verified`

Type: discovering-country report and responsible-country report.

Effects:

- mark state discovered
- expose unique state sources
- add public Condemnation source
- reveal foreign reaction adapters
- raise linked-site discovery chance
- record history

### `chaosx_022_network_verified`

Type: country reports plus news event when scale threshold is met.

Effects:

- expose bounded national network source
- update responsible-country crisis idea
- activate shared sanction and tribunal gates
- mark network public
- prevent repeated network source

### `chaosx_022_coverup_discovered`

Type: observer and responsible-country reports.

Trigger:

- destroyed or falsified evidence confirmed by independent source

Effects:

- add cover-up source once
- increase accountability severity
- reveal administrator or institution link

### `chaosx_022_restricted_or_experiment_site_verified`

Type: observer report and possible news event.

Effects:

- add source-specific evidence
- call Event 16 or chemical-system discovery adapter
- preserve historical and alternate-history wording boundary

## Retreat events

### `chaosx_022_front_approaches_site`

Type: responsible-country report with selected state.

Trigger:

- enemy front, bombing, encirclement, supply collapse, or projected control loss

Options:

- close in place
- supplied transfer
- forced evacuation on foot
- liquidation for an extreme route
- destroy site and records
- abandon

Follow-up:

- one state mission and one outcome event

### `chaosx_022_transfer_outcome`

Type: country report.

Inputs:

- transport debit
- route safety
- supply
- bombing
- disease
- resistance
- destination capacity

Results:

- supplied arrival
- partial loss and escape
- transport catastrophe
- route discovery
- abandonment

### `chaosx_022_forced_march_outcome`

Type: country and observer reports when discovered.

Results:

- severe deaths
- mass escape
- route interrupted by enemy or resistance
- destination reached
- evidence and witness creation

### `chaosx_022_liquidation_discovered`

Type: liberator or observer report.

Effects:

- strongest state atrocity and cover-up source
- exact responsible actor
- possible military-objection evidence
- tribunal priority

## Liberation and relief events

### `chaosx_022_site_liberated`

Type: liberating-country report.

Pre-effect:

- stop operation
- remove assignment and operator benefits
- identify site status
- calculate survivors, disease, contamination, records, and recent evacuation
- preserve original responsibility

Options:

- secure and deliver urgent relief
- request allied or international assistance
- prioritize evidence while maintaining minimum relief
- withdraw and hand responsibility to another valid controller

No option permits silent reuse. Reuse requires a separate successor event and creates responsibility.

### `chaosx_022_abandoned_site_found`

Type: liberator report.

Text direction:

- guards and administrators are gone or scattered
- survivors, records, disease, and supplies remain unresolved

Options:

- secure
- emergency relief
- pursue fleeing administrators
- preserve evidence

### `chaosx_022_emptied_site_found`

Type: liberator report.

Purpose:

- reveal forced evacuation route
- open route search, witness, and missing-person actions

### `chaosx_022_destroyed_site_found`

Type: liberator report.

Purpose:

- expose physical or documentary remnants
- start evidence-preservation mission
- assess survivors and contamination

### `chaosx_022_contaminated_site_found`

Type: liberator report.

Purpose:

- call chemical or biological decontamination
- block ordinary transfer until safe
- preserve source-specific evidence

### `chaosx_022_relief_emergency_update`

Type: bounded report used only at a major relief threshold.

Possible directions:

- mortality falling
- epidemic worsening
- housing exhausted
- records and families identified
- foreign aid arrives

Routine progress remains in missions and category values.

### `chaosx_022_survivors_registered`

Type: country report or silent completion with optional report for large network.

Effects:

- unlock return and resettlement
- improve evidence confidence
- update achievement proof

### `chaosx_022_site_documented_and_closed`

Type: country report.

Effects:

- remove physical camp building through closure helper
- preserve evidence and history
- change state to recovery status
- update network closure progress

## Succession, civil war, and reuse events

### `chaosx_022_successor_inherits_network`

Type: successor-country report.

Trigger:

- government, ideology, tag, overlord, or recognized successor changes while sites or evidence remain

Options:

- open archives and close
- restrictive review
- continue detention or labour
- continue extermination for a valid route
- conceal predecessor evidence

Effects:

- original responsibility remains
- new operation creates new generation
- successor AI profile initializes

### `chaosx_022_civil_war_network_split`

Type: hidden worker plus reports to each relevant side.

Purpose:

- partition active states by control
- preserve pre-split actor
- create later operation generation only after each side chooses policy
- preserve evolution markers

### `chaosx_022_new_controller_considers_reuse`

Type: controller report.

Trigger:

- new controller has an inactive but usable site and a route that can continue operation

Options:

- keep closed and provide relief
- reuse for detention
- reuse for forced labour
- reuse for extermination only with complete target-purpose proof

Any reuse creates later responsibility and removes liberator profile.

### `chaosx_022_master_orders_continuation`

Type: subject and overlord reports.

Trigger:

- explicit puppet-master decision or country-package effect

Purpose:

- record contributing responsibility
- let subject comply, resist, disclose, or request support

No passive overlord relation creates responsibility.

### `chaosx_022_archives_opened`

Type: successor and observer reports.

Effects:

- expose predecessor evidence
- improve legitimacy or foreign support according to shared systems
- create hardliner and collaborator conflict
- support accountability achievements

## Accountability and aftermath events

### `chaosx_022_displaced_person_crisis`

Type: controller and possible receiving-country reports.

Trigger:

- survivors cannot safely return
- receiving capacity or border decision required

Options:

- local accommodation
- negotiated foreign reception
- safe return when valid
- delayed decision with added pressure
- unsafe forced return as a negative route

### `chaosx_022_family_and_missing_records`

Type: aftermath report.

Purpose:

- create tracing, citizenship, and missing-person choice
- use preserved records and testimony

### `chaosx_022_tribunal_proposed`

Type: investigating, successor, or victorious-country report.

Requirements:

- verified evidence
- valid responsibility actor or institution
- valid investigating authority

Options:

- domestic public trial
- international cooperation
- limited operator prosecution
- negotiated amnesty
- obstruction

### `chaosx_022_accountability_outcome`

Type: participating-country reports and possible news event.

Inputs:

- evidence categories
- cooperation
- obstruction
- actor availability
- survivor participation

Outcomes:

- comprehensive accountability
- partial trials
- domestic purge
- amnesty
- unresolved process
- cover-up and later rediscovery

### `chaosx_022_transparent_closure_complete`

Type: affected-country report.

Requirements:

- no active operation or intake
- all sites closed or in stable relief
- survivors supplied and registered
- records preserved or transferred
- no underground site

Effects:

- unregister active network
- start longest refire protection
- update event history and achievements
- retain evidence and aftermath records

### `chaosx_022_secret_demolition_complete`

Type: responsible-country report.

Requirements:

- no active buildings
- unresolved survivors, records, or cover-up evidence

Effects:

- stop operation pulse
- keep discovery jobs and missing-person pressure
- no transparent-closure protection

### `chaosx_022_network_dormant`

Type: country report or silent transition.

Purpose:

- mark suspended intake and assignment
- retain low-level repression, evidence, and refire incident eligibility

### `chaosx_022_relief_and_recovery_complete`

Type: liberating or successor-country report.

Requirements:

- survivor safety
- evidence and documentation handoff
- stable destinations
- no disease or contamination emergency
- state recovery complete

Effects:

- close relief category
- update achievements
- retain historical state record

## News events

### `chaosx_022_news_verified_large_network`

Trigger direction:

- verified national network above accepted reach, death, extermination, experiment, or chemical severity threshold

Recipients:

- countries with normal news visibility

Effects:

- no direct duplicate Condemnation
- public context and AI reaction signal

### `chaosx_022_news_major_liberation`

Trigger direction:

- liberation of a large verified or previously hidden network

Text direction:

- scale of site and relief need
- evidence and survivors
- continuing displacement and medical crisis

### `chaosx_022_news_accountability_process`

Trigger direction:

- comprehensive tribunal or major successor accountability

Text direction:

- institutions and evidence under review
- no triumphalist claim that all consequences are resolved

## Hidden worker events

Required workers include:

- initial site batch
- Evolution I conversion batch
- Evolution II shock batch
- Evolution III site and shock batches
- operation pulse
- evidence exposure transaction
- liberation transition
- responsibility-generation transition
- regional closure completion
- network unregister and cleanup

Every worker receives:

- expected actor
- expected state where relevant
- network generation
- action or cause
- current evolution stage
- one-shot proof

Every worker:

- revalidates before applying
- fails closed
- records skip reason
- clears temporary targets
- avoids player popup
- remains idempotent over save and reload

## Event option and AI rules

Every player-facing option needs:

- visible direction and cost
- exact availability
- AI chance or deterministic profile rule
- immediate effect
- delayed follow-up
- history effect when material
- cleanup

No option can:

- invent a target group
- apply population loss outside the exact helper
- clear evidence through building deletion
- transfer people without source and destination accounting
- activate chemical operation without stockpile
- restore a closed network through a repeat popup without a new generation

## Event spam controls

- one opening report per country and generation
- one evolution report per country and evolution entry
- one report per selected baseline incident
- one report per major discovery confidence transition
- one report per liberation state only when the state has a materially distinct emergency, otherwise summarize a region
- one transparent-closure report per network
- one major news event per public threshold
- no pulse reports
- no repeated observer report for the same evidence source

## Localisation handoff fields

For every event record:

- working semantic name
- final numeric ID
- title direction
- description direction
- viewpoint
- dynamic actors and states
- option directions
- hidden information
- image ID
- sound pattern
- trigger and fire path
- follow-up IDs
- AI profile
- history or detail registration

Final localisation is written during implementation and audited separately.
