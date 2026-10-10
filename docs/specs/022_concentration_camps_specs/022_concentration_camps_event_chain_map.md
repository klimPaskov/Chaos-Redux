# Event 22 Concentration Camps Event Chain Map

## Purpose

This file maps the Event 22 report, country, news, and hidden worker events. It gives implementation a complete chain without writing final localisation or locking numeric IDs before the repository collision audit.

The consolidated chain has 44 events (11 hidden, 33 player-facing), down from 64 named events in the original map (proposal P-022-B).
Variants of one situation are text and option variants of a single event, and silent transitions are history rows.

## Namespace and ID allocation

The namespace is the repository's existing `chaosx.nr22`, and the entry event is `chaosx.nr22.1`.
The legacy Spain events in that namespace (`events/022_jews_massacre.txt`) are replaced, not kept beside the new chain.

Recommended range ownership:

| Range | Owner |
| --- | --- |
| `.1` to `.49` | global dispatch, opening, and package handoff |
| `.100` to `.199` | baseline incidents |
| `.200` to `.299` | Evolution I |
| `.300` to `.399` | Evolution II |
| `.400` to `.499` | Evolution III |
| `.500` to `.599` | evidence, inspection, and public discovery, retreat |
| `.600` to `.699` | liberation and relief |
| `.700` to `.799` | succession, civil war, annexation, and reuse |
| `.800` to `.899` | accountability, displacement, closure, and aftermath |
| `.900` to `.949` | news events if the repository keeps them in the same namespace |
| `.950` to `.999` | hidden workers and bounded debug events |

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
  -> register sites and seed cohorts through the shared camp helpers
  -> player or AI selects policy (sets shared mandate and reform path)
  -> shared monthly processor owns recurring harm
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
- Routine monthly losses use the Deaths ledger, the Ledger and the category values. They do not show monthly popups.
- Final text uses dynamic country, state, policy, site type, and target-purpose localisation.

## Global and opening events (4)

### `chaosx_022_global_dispatch` (hidden)

Receives the Event 22 selection from the shared picker, builds the country candidate pool, selects one country, records the cluster source when applicable, and calls the first opening, the country-package handoff, or the repeat dispatch.
No candidate means a logged skip. An invalid selected actor after a delay fails closed; no substitute actor is selected outside the original accepted job unless the shared picker reruns the whole event selection.

### `chaosx_022_package_handoff` (hidden)

Detects established German, Japanese, or Soviet ownership and passes the opening stage, evolution stage, target coverage and generation to the country package, which hides the generic category and preserves the global Event 22 history.
Outputs: adapter success flag, created or activated site count, current policy, category owner, failure reason.
A failed handoff returns to a reviewed generic adapter only when the country package explicitly supports that fallback.
The handoff adds no date condition; the package's own gates decide.

### `chaosx_022_network_opening` (country report)

Recipient: the selected country.
Pre-effect: register or schedule the initial sites and cohorts, calculate opening coverage and the evolution split, initialize Exposure, Resistance Pressure and the network generation, and join the shared camp registry.
Text direction: several detention sites now operate across named or implied regions; trains, guards, factories, local authorities and families already feel the effect; the government must decide whether to close, review, exploit or expand; an evolved opening also says that some sites have a killing function.
Options: immediate closure, restrictive review, forced-labour administration, security expansion, and the extermination opening only when valid.
Follow-up: the policy effect (shared mandate, reform path), one event history row, and the category reveal.

### `chaosx_022_opening_setup_complete` (hidden worker)

Confirms that delayed setup finished, compares the actual count with the target, applies the pre-fire Evolution II or III shock when required, clears temporary targets and reports skipped states with reasons.
The category does not open before site registration is stable unless it can safely show setup in progress.

## Baseline incidents (10)

### `chaosx_022_repeat_incident_dispatch` (hidden)

Evaluates the valid incident families, chooses one through audited weights, and fires nothing when no threshold exists.

### Incident events

| Event | Trigger direction | Options |
| --- | --- | --- |
| `chaosx_022_coordinated_escape` | Resistance Pressure threshold, escape network and guard weakness | improve conditions, reinforce guards, targeted security operation, violent suppression for valid perpetrator routes; starts the escape mission |
| `chaosx_022_camp_epidemic` | overcrowding, famine stage, plague, global air contamination weight, contamination, destroyed infrastructure | deliver medical and food relief, isolate humanely with release conditions, abandon the site, conceal the outbreak, continue work despite disease; starts the epidemic mission |
| `chaosx_022_administrator_corruption` | seized property, high output, weak oversight | investigate and preserve records, replace local administration, tolerate theft, purge officials with a possible inward-broadening consequence |
| `chaosx_022_military_objection` | high deaths, extermination, forced evacuation or purge of core supporters; officer loyalty | halt or review orders, remove objectors, compromise, allow an independent inspection; possible coup pressure, underground network, Event 21 bridge |
| `chaosx_022_foreign_leak` | escapee, railway records, family search, foreign intelligence or administrator defection | perpetrator: restrict access, falsify records, investigate the leak, begin transparent review; observer: investigate, protect witness, share with allies, demand access |
| `chaosx_022_disaster_exposes_site` | Event 13 damage reveals records, remains, survivors or infrastructure | relief and secure evidence, conceal and repair, abandon, request foreign aid |
| `chaosx_022_underground_network_revealed` | central closure order with local continued operation | prosecute operators, negotiate surrender, expose publicly, restore coercive control; starts the underground mission |
| `chaosx_022_target_source_exhausted` | no valid intake for the current target source, regime refuses closure | close the network, reduce to dormant detention, seek another valid existing target source, broaden the purge for an extreme route; no option invents an ethnicity |
| `chaosx_022_restricted_site_accident` | restricted chemical operation, stockpile handling, bombardment or contamination failure | stop and decontaminate, conceal and continue, evacuate nearby population, abandon the site |

The cause owner is respected in every incident: the disease system owns spread, the famine system owns famine, Event 13 owns physical damage, and Event 22 and the shared camp owner own confinement, neglect and additional camp mortality.
The original quota-breakdown incident is dropped with the per-state assignments; labour exhaustion is visible in the Ledger.

## Evolution I (3)

- `chaosx_022_evolution_1_global` (hidden): marks Evolution I available, registers active countries for conversion jobs, changes the future first-opening package.
- `chaosx_022_evolution_1_country_report` (country report): counts valid concentration sites, calculates `floor(valid_count / 2)` conversions, selects states through the audited score and queues conversions.
  Text direction: part of the existing network has received a different purpose and chain of command; killing orders replace ordinary detention or labour in selected sites.
  Options: accept the national extermination route when valid, halt conversion and start the closure conflict, contain conversion through review, allow a country-specific response.
  When exactly one valid concentration site exists and no explicit extermination policy is set, the same event shows the single-site branch: convert, refuse and close, place under review, or allow local underground conversion risk.
- `chaosx_022_evolution_1_setup_complete` (hidden worker): verifies the exact conversion count, ends productive allocations, preserves markers and evidence, writes the evolution history.

## Evolution II (3)

- `chaosx_022_evolution_2_global` (hidden): marks Evolution II available, registers every active network for the 1 percent job, changes the future opening package.
- `chaosx_022_evolution_2_country_report`: deaths and disappearances rise across every camp state during a synchronized escalation. Options: continue policy, reduce intensity (return to the custody mandate), begin closure, investigate unauthorized escalation. The options affect future operation and never undo the applied loss.
- `chaosx_022_evolution_2_state_worker` (hidden, one per state, totals and the evolution history row written by the last worker): validates the active site and generation, skips a marked state, admits the sweep cohort when the parent keeps that rule (index P-022-C), requests 1 percent of current population through `camp_admin_record_deaths`, logs the actual loss, sets the marker even when the floor or cohort makes it zero, adds evidence and Resistance Pressure from the actual loss.

## Evolution III (3)

- `chaosx_022_evolution_3_global` (hidden): marks Evolution III available, registers active networks for coverage and shock jobs, changes the future first opening to the late-stage package.
- `chaosx_022_evolution_3_country_report`: calculates the 50 percent target and the minimum split, queues additions, conversions and the 2 percent shock.
  Text direction: the camp system now reaches half of eligible state administration; trains, guards, labour, killings, resistance, disease and evidence have become a national crisis.
  Options: attempt emergency national closure, keep a mixed network, intensify an explicit extremist route, allow a country-specific response.
- `chaosx_022_evolution_3_state_worker` (hidden, one per state): adds or converts the site, preserves existing extermination sites, gives the odd extra to concentration unless the route overrides, registers responsibility and generation, then requests the 2 percent shock once; a new pre-fire late-stage site sets no Evolution II marker. The last worker verifies final reach and split, totals the actual loss, records skipped states, activates the late-stage category and writes the history.

## Evidence and inspection (5)

| Event | Type and trigger | Options and effects |
| --- | --- | --- |
| `chaosx_022_first_credible_report` | observer report; first fragmentary evidence reaches a valid observer | investigate, protect witness, share evidence, dismiss, suppress for alliance or domestic reasons; a dismissal does not delete the evidence |
| `chaosx_022_inspection_requested` | responsible-country report | grant real access, grant restricted access, stage the site, reject access, begin closure before inspection |
| `chaosx_022_inspection_outcome` | responsible and inspector reports; inputs are access quality, evidence, witnesses, cover-up, foreign intelligence and state control | no verification, credible suspicion, verified state, failed cover-up with a linked-site lead |
| `chaosx_022_site_verified` | discovering-country and responsible-country reports; variants for ordinary site, cover-up confirmed by an independent source, restricted chemical or experiment site, and liquidation discovered | marks the state discovered, exposes unique state sources, adds the public Condemnation source once, reveals the foreign reaction adapters, raises linked-site discovery, records history; the cover-up variant adds the cover-up source once, the restricted variant calls the Event 16 or chemical discovery adapter with the alternate-history wording boundary, the liquidation variant carries the strongest source and tribunal priority |
| `chaosx_022_network_verified` | country reports plus a news event at the scale threshold | exposes one bounded national network source, updates the responsible country's crisis idea, activates shared sanction and tribunal gates, marks the network public, prevents a repeated network source |

Discovery steps reuse the shared discovery effects (`genocide_try_discover_state_atrocity` and the Condemnation source helpers) and add the confidence states of Part 4.

## Retreat (2)

- `chaosx_022_front_approaches_site` (responsible-country report with a selected state; trigger: enemy front, bombing, encirclement, supply collapse or projected control loss).
  Options: close in place, supplied transfer, forced evacuation on foot, liquidation for an extreme route, destroy site and records, abandon.
  Follow-up: one state mission outcome through `chaosx_022_retreat_outcome`.
- `chaosx_022_retreat_outcome` (country and observer reports): inputs are transport debit, route safety, supply, bombing, disease, resistance and destination capacity.
  Variants: supplied arrival, partial loss and escape, transport catastrophe, route discovery, forced march (severe deaths, mass escape, interruption by enemy or resistance, destination reached, witnesses and evidence), abandonment.

## Liberation and relief (2)

### `chaosx_022_site_liberated` (liberating-country report)

Pre-effect: stop operation, remove productive allocations and operator benefits, identify the site status, calculate survivors, disease, contamination, records and recent evacuation, and preserve original responsibility.
Variants of one event (the state status of Part 4): active site with survivors, abandoned site, emptied site after forced evacuation (opens route search and missing-person actions), destroyed site with evidence (opens the evidence mission), contaminated site (calls chemical or biological decontamination and blocks ordinary transfer until safe).
Options: secure and deliver urgent relief, request allied or international assistance, prioritize evidence while maintaining minimum relief, withdraw and hand responsibility to another valid controller.
No option permits silent reuse; reuse requires the separate successor event and creates responsibility.

### `chaosx_022_site_documented_and_closed` (country report)

Removes the physical camp building through the shared closure, preserves evidence and history, changes the state to a recovery status, and updates network closure progress.
Survivor registration and relief milestones complete silently or as a mission result; a large network may show one summary report.

## Succession, civil war, and reuse (4)

- `chaosx_022_successor_inherits_network`: government, ideology, tag, overlord or recognized successor changes while sites or evidence remain.
  Options: open archives and close (the archive opening is an option here, not a separate event), restrictive review, continue detention or labour, continue extermination for a valid route, conceal predecessor evidence.
  Original responsibility remains; new operation creates a new generation; the successor AI profile initializes.
- `chaosx_022_civil_war_network_split` (hidden worker plus reports to each side): partitions active states by control, preserves the pre-split actor, creates a later operation generation only after each side chooses policy, preserves evolution markers.
- `chaosx_022_new_controller_considers_reuse`: a new controller has an inactive usable site and a route that can continue operation.
  Options: keep closed and provide relief, reuse for detention, reuse for forced labour, reuse for extermination only with complete target-source proof. Any reuse creates later responsibility and removes the liberator profile.
- `chaosx_022_master_orders_continuation` (subject and overlord reports): an explicit puppet-master decision or country-package effect records contributing responsibility; the subject can comply, resist, disclose or request support. No passive overlord relation creates responsibility.

## Accountability and aftermath (5)

- `chaosx_022_displaced_person_crisis` (controller and possible receiving-country reports): survivors cannot safely return or a receiving decision is needed.
  Options: local accommodation, negotiated foreign reception, safe return when valid, delayed decision with added pressure, unsafe forced return as a negative route. Tracing, citizenship and missing-person choices (formerly a separate family-records event) are options of this event; movement uses the migration owner's proved cohorts (Part 5).
- `chaosx_022_tribunal_proposed` (investigating, successor or victorious-country report): requires verified evidence, a valid responsibility actor or institution and a valid investigating authority.
  Options: domestic public trial, international cooperation, limited operator prosecution, negotiated amnesty, obstruction.
- `chaosx_022_accountability_outcome` (participating-country reports and possible news): inputs are evidence categories, cooperation, obstruction, actor availability and survivor participation. Outcomes: comprehensive accountability, partial trials, domestic purge, amnesty, unresolved process, cover-up and later rediscovery.
- `chaosx_022_transparent_closure_complete` (affected-country report): no active operation or intake, all sites closed or in stable relief, survivors supplied and registered, records preserved or transferred, no underground site. Unregisters the network, starts the longest refire protection, updates the history and achievements, retains evidence.
- `chaosx_022_relief_and_recovery_complete` (liberating or successor-country report): survivor safety, documentation handoff, stable destinations, no disease or contamination emergency, state recovery complete. Closes the relief category and updates achievements.

Secret demolition and a dormant network are silent transitions with history rows; they stop operation, keep discovery jobs and missing-person pressure, and grant no transparent-closure protection.

## News events (3)

- `chaosx_022_news_verified_large_network`: a verified national network above the accepted reach, death, extermination, experiment or chemical threshold. No direct duplicate Condemnation; public context and an AI reaction signal.
- `chaosx_022_news_major_liberation`: liberation of a large verified or previously hidden network; scale of site and relief need, evidence, survivors, continuing displacement and medical crisis.
- `chaosx_022_news_accountability_process`: a comprehensive tribunal or major successor accountability; institutions and evidence under review, no triumphalist claim that all consequences are resolved.

## Hidden worker contract

Required workers: initial site batch, Evolution I conversion batch, Evolution II and III state batches, liberation transition, responsibility-generation transition, regional closure completion, network unregister and cleanup.
Evidence exposure and the other transitions are effects called from the events above and need no events of their own.
There is no operation-pulse worker; the shared processor owns recurring harm.

Every worker receives the expected actor, the expected state where relevant, the network generation, the action or cause, the current evolution stage, and a one-shot proof.
Every worker revalidates before applying, fails closed, records the skip reason, clears temporary targets, avoids player popups and stays idempotent over save and reload.

## Event option and AI rules

Every player-facing option needs visible direction and cost, exact availability, an AI chance or deterministic profile rule, the immediate effect, the delayed follow-up, a history effect when material, and cleanup.

No option can:

- invent a target group
- apply population loss outside `camp_admin_record_deaths` and the exact helper
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

For every event record the working semantic name, final numeric ID, title direction, description direction, viewpoint, dynamic actors and states, option directions, hidden information, image ID, sound pattern, trigger and fire path, follow-up IDs, AI profile, and history or detail registration.

Final localisation is written during implementation and audited separately.

## Disposition of the original map

| Original working event | Disposition |
| --- | --- |
| `policy_initialized` | merged into the option effects of `network_opening` |
| `labour_quota_breakdown` | dropped with the per-state assignments |
| `evolution_1_single_site_crisis` | branch of `evolution_1_country_report` |
| `evolution_2_complete`, `evolution_3_site_setup_worker`, `evolution_3_shock_worker`, `evolution_3_complete` | merged into the last state worker of each evolution |
| `coverup_discovered`, `restricted_or_experiment_site_verified`, `liquidation_discovered` | variants of `site_verified` |
| `transfer_outcome`, `forced_march_outcome` | variants of `retreat_outcome` |
| `abandoned_site_found`, `emptied_site_found`, `destroyed_site_found`, `contaminated_site_found` | variants of `site_liberated` |
| `relief_emergency_update`, `survivors_registered` | mission results and history rows |
| `archives_opened` | option of `successor_inherits_network` |
| `family_and_missing_records` | options of `displaced_person_crisis` |
| `secret_demolition_complete`, `network_dormant` | silent transitions with history rows |
