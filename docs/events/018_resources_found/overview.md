# Event 018 - Resources Found

Event 018 is a Minor Repeatable Economy (pos) event with Medium cluster severity. Its canonical entry is `chaosx.nr18.1`. Each accepted firing selects one valid state owned and controlled by the firing country, then either creates a persistent field or enriches an existing eligible field. The baseline is complete with all evolutions disabled.

The system uses the six standard HOI4 resources only: oil, aluminium, rubber, tungsten, steel, and chromium. A baseline discovery chooses one of them with equal probability and adds 80 to 120 units, centered on 100. Resource legality is never terrain-gated. Terrain, infrastructure, coast, population, and existing development affect state weighting and presentation only.

## Discovery and enrichment

The generic random-event dispatcher calls `resources_found_prepare_random_event_fire` before firing Event 018. The preparation effect stores one exact country and one exact state as regular event targets. It weighs a new field against an enrichment without rerolling after the visible event begins.

A fresh field receives one stable record and enters `.1`. An enrichment enters `.2`, uses follow-up text, and retains the same record. Duplicate resource rolls add to the existing resource ledger, so repeated oil rolls in one state stack. Different rolls create a compound field. The practical 1,200-unit Event 018 concentration cap prevents an unbounded single-state number while preserving repeated enrichment below that explicit design ceiling.

Invalid discovery owners include terminal actors, special chaos countries, and actual nonhuman countries. Valid states must be owned and controlled, non-impassable, sufficiently populated, compatible with Event 018, and neither permanently closed nor already represented by a second field record.

## Persistent field record

The state is the authoritative physical record. It stores:

- field sequence, discoverer, current owner, current controller, discovery date, discovery count, stage, posture, and status;
- separate Event 018 additions for oil, aluminium, rubber, tungsten, steel, and chromium;
- total Event 018 addition, current total state resources, distinct-resource count, and largest Event 018 resource;
- Developed Yield, Excavation Depth, Workforce Safety, Foreign Pressure, Subsurface Disturbance, Breach Pressure, and exploitation history;
- contract partner, contract term and stage, concession partner, commission sponsor and stage, border claimant and stage;
- suspension, occupation, closure, incident, evacuation, hunt, sealing, cave-entry, and achievement evidence.

The owning country keeps a bounded array of its fields and a selected-field pointer. State ownership transfer migrates the pointer and physical record, then reviews diplomatic rights separately. Temporary occupation suspends vulnerable delivery and development behavior without transferring the resource ledger. Annexation, actor removal, peace-conference ownership, and selected-field loss use one-shot reconciliation hooks rather than a world-wide periodic country loop.

## Selected-field interface

The `Selected Resource Field` category owns a compact scripted GUI. It displays the state, current owner and controller, discovery count, all six Event 018 ledgers, their added total, and the state's full strategic-resource total. A compact legal and lifecycle block shows posture, development stage, operating/closure/suspension status, contract status, and commission status. The core values appear as integers with named bands:

- Developed Yield records usable output and industrial maturity;
- Excavation Depth records the physical commitment and later risk burden;
- Workforce Safety records training, engineering, evacuation, and labor protection;
- Foreign Pressure records material demand, contracts, claims, smuggling, and strategic competition.

Subsurface Disturbance is hidden until Evolution II evidence reveals it. Breach Pressure is hidden until the Evolution III public crisis. Every value tooltip explains the actions that raise or lower it. Previous and next controls cycle valid owned fields. Human selection changes only presentation and the chosen player project. AI field evaluation uses the underlying owned-field set and stable scheduler targets.

Five field identities have real source-frame animation packages and registered static fallbacks: ordinary seal, unsafe workings, revealed disturbance, public breach, and sealing operation. Suspended uses a static identity. Exact closure stores the six reversed ledgers and a bounded `last closed field` pointer, removes the state from active selection, and opens a separate history view with the Closed sprite. The parent category remains visible through that history record even when the seal removed the country's last active field. The History control never moves the gameplay selection onto that state, so a closed record cannot receive projects, cycle among active fields, or become eligible for discovery again. The category includes an animation toggle that swaps every animated active identity to its fallback.

Every priced decision displays its exact rounded payment, required available civilian and military factory capacity, and either its computed project duration or its immediate-execution status before selection. A shared ledger stores 13 cost profiles and 16 duration rows. The same calculator rebuilds those rows and rechecks the selected row immediately before payment; political power, command power, army experience, manpower, infantry equipment, support equipment, anti-tank equipment, trucks, trains, convoys, and fuel all use the displayed rounded values. Changes to national scale, war status, the selected field, excavation, breach, disturbance, safety, infrastructure band, or contract validity hide priced actions until the appropriate category's visible refresh control rebuilds the ledger. Discovery, enrichment, cave setup, cave-war registration, foreign-actor selection, and field cycling also initialize or refresh it directly so AI countries do not depend on a player click.

The ten player-facing missions keep immutable field, partner, border-pair, state, or country targets for their lifetime. The eight MTTH evolution clocks and their one-day reschedule mission remain engine missions for their existing cancel and timeout behavior, but live only under `resources_found_hidden_clock_category`; that category is permanently invisible because mission-level `visible` does not hide missions.

## Administration and development

Field posture is a real transition project rather than a free instant switch. Available postures are:

- National Resource Authority;
- Domestic Commercial Charter;
- Foreign Concession;
- International Commission when negotiated;
- Strategic Reserve and suspension.

Development includes geological appraisal, deeper testing, basin mapping, primary works, a rail and road corridor, heavy machinery, local processing, worker settlement, regional labor, crew rotation, ventilation and medical facilities, guarded access, and integrated compound processing. Projects calculate country scale, field scale, danger, infrastructure, war, occupation, and contract context before setting cost and duration. Payments draw from political power, command power, army experience, manpower, equipment, convoys, and fuel according to the project's physical identity; civilian and military factory values are exact availability gates.

Project outcomes update the state map, field values, posture, AI weights, and later incident profile. Mature fields use a small number of meaningful state-output identities instead of accumulating tiny permanent national modifiers.

## Trade, foreign pressure, and concessions

Completing Invite Strategic Bids runs one country scan for the selected field. It does not add a periodic or on-action world loop. Each valid country is scored only for resources recorded in that field. Current deficit, imported amount, industrial consumption, and abundant domestic extraction are evaluated separately for oil, aluminium, rubber, tungsten, steel, and chromium. Field total, resource diversity, Developed Yield, global significance, suspension, and commission constraints form a shared field score. Candidate scoring then adds the strongest available land-neighbor, faction, military-access, same-continent, or valid maritime route, current opinion of the owner, a core or claim on the field, rivalry with the existing partner, war demand, major status, factory capacity, and the owner's weakness. Overextension and lack of access reduce the score.

A field that is closing, cave-converted, or transaction-locked does not run the scan. Invalid, capitulated, and war-enemy countries cannot be selected. The highest country at or above the centralized minimum becomes the sole foreign-interest actor. Equal scores keep deterministic country iteration order. If no country qualifies, no actor pointer is created. The actor receives the existing owner and field pointers and immediately refreshes its decision-cost previews.

The owner can invite bids, reserve output, balance buyers, accept machinery and transport, open a concession, or sign a persistent export contract. A contract records the buyer, access, term, stage, route state, interruption history, and settlement. Delivery uses normal strategic-resource rights. Route loss, occupation, suspension, closure, partner disappearance, and state transfer review or remove those rights through the same lifecycle helpers.

Exclusive access increases rival pressure. Nationalization is a timed preparation with compensation and dispute outcomes. Fair settlement can close the dispute. Smuggling and sabotage derive from borders, route exposure, pressure, and material stake, and have patrol, customs, intelligence, and diplomatic counterplay. Event 018 does not create a parallel trade currency.

## International commission and border conflict

A severe multi-country competition can produce a negotiated international commission. The commission records sponsor and parties, sets quotas and inspection rules, places the state under engine demilitarization, removes forts, and permits fewer than three guard divisions. Compliance requires the engine DMZ, the troop limit, and zero land or coastal forts. Restoration reinstates those conditions. Violation raises diplomatic stakes. Dissolution clears the engine DMZ, commission rights, targets, and state identity.

A border claimant must possess a real claim or mapped dispute. Adjacency alone is insufficient. High field value and Foreign Pressure open a staged crisis: competing surveys, road or customs confrontation, armed patrol incident, a timed frontier objective, and a limited border war when military conditions permit. The objective names the disputed state and checks troop, supply, transport, and route commitments. Owner victory, claimant victory, negotiated settlement, stalemate, ceasefire, and commission mediation have separate outcomes. Claimant victory transfers the state and its physical field ledger, then reviews contracts and concessions under the new owner.

## Suspension and exact closure

Suspension is reversible. It suppresses extraction and risk growth, preserves all six resource ledgers, retains maintenance and containment access, records its duration, and pauses or reviews contracts. Entering suspension finalizes any live maximum-extraction interval before the suspension clock begins. If Maximum Shifts remains the field's operating posture, resumption starts a new interval, so no suspended day enters the exploitation ledger.

Ordinary closure is a multi-step engineering and settlement project. Its cost and duration scale with field total, resource diversity, depth, development, contracts, danger, occupation, and country capacity. Exact closure acquires the field transaction lock, removes each of the six Event 018 ledger amounts from the matching state resource, and never removes more than the recorded addition. Preexisting resources and additions from other systems remain. It then settles or terminates contracts, removes resource rights and DMZ state, clears modifiers and targets, removes the field from its owner's array, closes Event Details history, and permanently excludes that state from future Event 018 discovery.

Partial closure leaves the ledger intact and restricts the workings. It is never presented as permanent prevention.

## Evolution I - Compound Fields

Evolution I has separate pre-fire and active-field paths. A pre-fire opening makes 2 to 4 independent large 80 to 120 rolls in one state. The active path adds 1 to 3 independent rolls to an existing field. Duplicate resources stack in both paths.

Compound fields unlock integrated processing, unified administration, split concessions, stronger transport, and deeper foreign competition. Several materially interested countries can negotiate the commission and demilitarized route. A stable non-supernatural compound field can remain productive, suspend, settle its foreign arrangements, or close exactly. Evolution I records one shared evolution row for its field opening.

## Evolution II - The Sick Workings

Evolution II also has distinct pre-fire and active paths. The pre-fire economic package makes 3 to 5 independent 90 to 140 rolls, while an active enrichment makes 1 to 3. The visible incident chain remains gradual even when the game begins at a higher enabled evolution.

The chain starts with worker sickness and ordinary physical explanations, then machinery corrosion, disappearances, recorded knocking, failed ordinary tests, physical evidence, and an underground attack. Investigation can use medical inspection, scientific testing, military survey, controlled isolation, rescue, or restricted workings. Concealment and coercive extraction remain possible but increase later deaths, breach, exploitation score, and achievement disqualification.

All worker and field deaths remove actual state population through `apply_exact_state_civilian_population_loss` and register shared Deaths cause 16 when that presentation system is enabled. The same population change occurs when Deaths presentation is disabled. Safety, restricted access, rescue, and investigation change the applied risk and timing. Evolution II can stabilize with Evolution III disabled.

## Evolution III - The Public Breach

Evolution III's opening adds one independent 120 to 200 roll of every standard resource. A game that enters at this evolution still begins the Evolution II incident sequence before surface attacks.

After physical evidence, underground attack, and stabilization, Breach Pressure becomes visible and the crisis reaches public life. The sequence includes a perimeter breach, settlement attack, transport disruption, city intrusion, foreign aid, supplied monster hunts, evacuation, partial closure, full sealing, failure, and a protected final window.

Monster hunts require suitable armed forces and real anti-armor preparation. Evacuation commits trucks, trains, route capacity, receiving capacity, and time. Success and failure have distinct state-population, safety, transport, contract, and breach consequences. Continuing extraction increases the visible exploitation score and the strength of a later emergence.

Full sealing requires suspension, workforce evacuation or control, engineering preparation, surface containment, and completion of the timed seal. Success subtracts every Event 018 resource addition, closes the field exactly, and permanently blocks Evolution IV for that field. It has no hidden retaliation. Partial sealing delays danger but does not make that claim. Evolution III remains containable when Evolution IV is disabled.

Every event option that physically starts a partial or emergency seal uses the same calculated payment and containment-mission launcher as the matching decision. Options presented from inside a mission completion callback record closure intent instead of overwriting that live mission; after demobilization, the separately priced full-seal decision remains reachable. Cancellation, occupation, or transfer clears every partial/full/emergency closing flag on the locked state before project runtime is released, so no field can remain closing without a mission.

## Evolution IV - The Oth-Kesh Host

Evolution IV uses separate protected pre-fire and active windows. It cannot occur on the first discovery day. A field must complete the public sequence, reach the configured visible breach and exploitation gates, remain unsealed, and pass its dynamic release date.

The first emergence creates the playable DHO country in the field state. Starting strength derives from recorded exploitation, resource scale, development, deaths, failed sealing, safety, suspension, hunts, and evacuation, with a hard range of 6 to 30 divisions. The former owner can continue as the Oth-Kesh Host. Later cave breaches reinforce the same country.

The complete tag, capacity, unit, focus, decision, AI, counterplay, world-end, and cleanup contract is documented in `docs/events/018_resources_found/cave_country.md`.

Reusable scope, input, output, and side-effect contracts are documented in `docs/events/018_resources_found/helper_contracts.md`.

## Captured-resource deployment

For every controlled non-origin state, DHO sums current oil, aluminium, rubber, tungsten, steel, and chromium. Capacity is `floor(total / 10)`, capped at 10. The origin always contributes zero future capacity. A state must remain continuously controlled for 30 days. Its activation is visible and can be interrupted by recapture or resource denial. A prepared denial adds 30 days to each interrupted activation attempt and subtracts three capacity, clamped at zero, exactly once when an activation succeeds; the preparation is not consumed merely because an attempt began. Active anchors spawn divisions sequentially at the configured interval.

Losing an anchor starts a 21-day grace period. Expired excess units receive Unfed Broods rather than vanishing. Recapture can restore support. Liberation opens exact anchor cleanup and resource restoration with an explicit scar.

Burrow War preparation can begin only when a defended enemy capital, supply hub, or level-3 fortified state borders an active nondisrupted anchor. Project completion snapshots the exact state, its defending formation, and its qualifying objective type, then opens one visible 90-day mission. Only DHO control of that stored state during the live mission and before World End records the route achievement; retargeting, timeout, cancellation, cave defeat, and terminal transition clear every live marker and pointer.

Scree Tide uses the deployed Oth-Kesh Scree Pack battalion identity rather than a generic division total. Release Raiding Broods always creates its paid formation, but it opens a qualifying 180-day surge only with at least three active Scree Packs and total divisions within live brood capacity. Five different state captures and two different country capitulations must enter the same window; per-attempt marks prevent repeat credit. The final qualifying hook rechecks the three formations, capacity, and pre-World-End state before latching success.

## World end and defeat

The cave world end requires the enabled setting, no active world end, chaos strictly above 1,000, a valid origin-continent registry, DHO ownership and control of every eligible state, a continuous 60-day verification, valid resource-weighted foothold candidates beyond that continent, and completion of the final `The World Opens Below` focus. Verification unlocks that capstone but cannot execute the terminal transition by itself.

Success sets the shared terminal state and Event 018 terminal identity, blocks incompatible automatic event progression, suspends ordinary fields, transforms DHO into the World Below, and creates a stronger local foothold on every valid non-origin continent. Foothold weighting uses resources, diversity, industry, transport, and Event 018 field value. Each foothold opens a playable local war and the neighbor-war resolver runs again.

Regional defeat clears the live cave threat and creates cleanup without requiring a global aftermath. The global defeat super-event and reconstruction compact appear only after world-end or near-global evidence. No surviving field or residual incident secretly recreates the cave threat.

The reconstruction choice is offered only after global-defeat eligibility, a three-state personal cleanup contribution, no remaining cave cleanup state, and no live cave threat. Event `.99` sets its presented flag immediately and is never reopened by completing the chosen reconstruction project.

## Super-events, news, and audio

Event 018 reserves three super-event displays:

- display 82, cave emergence, audio 54, *Pictures at an Exhibition: IV. Bydło*;
- display 83, world end, audio 55, Brahms's *Symphony No. 1 in C minor: I. Un poco sostenuto - Allegro*;
- display 84, global defeat, audio 56, Chopin's Prelude in E minor, Op. 28 No. 4.

All three use unique 44.1 kHz stereo WAV packages lasting 115, 110, and 109 seconds. IDs 54 and 55 have worldwide public-domain/CC0 recording grants; ID 56 is CC BY 3.0 with complete attribution and change notice. The reconciled text, quote, image, trigger, audio, rights, and rejection authority is `docs/super_events/018_resources_found/overview.md`; the detailed audio manifest and split research notes retain the underlying evidence.

News events 84 to 89 cover the global field, border crisis, public attack, cave emergence, regional containment, and global defeat. Their images are true grayscale. Regional and global defeat news are mutually gated by the scale of the threat.

## Achievements

Fifteen achievements cover ordinary economic mastery, all-resource discovery, safe closure, exact Evolution III sealing, contract completion, negotiated commission, maximum emergence survival, regional defeat contribution, maximum anchor capacity, equipment-free cave armies, all three warfare doctrines, continent control, and global reconstruction. Their predicates use recorded action evidence, disqualifiers, field sequences, anchor states, and contribution ledgers rather than event-fire flags. Thirty From Below snapshots both the legal owner and physical controller before breach transfer. The Last Shaft Closed counts three distinct completed pre-World-End, non-origin anchor activations and excludes footholds. The two mobile-doctrine achievements use their exact mission and live-formation evidence.

Definitions, visible requirements, and icon triplets are documented in `docs/achievements/018_resources_found/achievements.md`.

## Gameplay files

- event chain: `events/018_random_resource.txt`;
- tuning: `common/script_constants/018_resources_found_constants.txt`, `common/script_constants/018_resources_found_decision_constants.txt`, `common/script_constants/018_resources_found_foreign_interest_constants.txt`, and `common/script_constants/018_resources_found_cave_constants.txt`;
- MTTH: `common/mtth/018_resources_found_mtth.txt`;
- field, incident, decision, cave, UI, log, news, and achievement effects: `common/scripted_effects/018_resources_found_*.txt`;
- field, decision, cave, and achievement triggers: `common/scripted_triggers/018_resources_found_*.txt`;
- decisions and categories: `common/decisions/018_resources_found_decisions.txt` and `common/decisions/categories/018_resources_found_categories.txt`;
- field and cave modifiers: `common/dynamic_modifiers/018_resources_found_state_modifiers.txt`, `common/ideas/018_resources_found_cave_ideas.txt`, and `common/opinion_modifiers/018_resources_found_opinion_modifiers.txt`;
- narrow hooks: `common/on_actions/018_resources_found_on_actions.txt`;
- scripted GUI: `common/scripted_guis/018_resources_found_scripted_gui.txt`, `interface/018_resources_found.gui`, and `interface/018_resources_found.gfx`;
- English text: `localisation/english/018_random_resource_l_english.yml` and `localisation/english/018_resources_found_system_l_english.yml`;
- scripted text: `common/scripted_localisation/018_resources_found_scripted_localisation.txt` plus the shared Event Details, settings, and super-event selectors;
- shared integrations: event dispatcher, cluster 7, Event Details/log, the clickable World Opens Below world-end row and independent automatic-selection checkbox, Deaths cause 16, world threat, terminal progression, news, achievements, music, and sound registries;
- catalog: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.

## Asset wiring

Event art:

- reports: `gfx/event_pictures/018_resources_found/`, registered in `interface/018_resources_found.gfx`;
- news: `gfx/event_pictures/news/018_resources_found/`, registered in the same GFX file;
- super-events: `gfx/super_events/018_resources_found/`, registered in `interface/chaosx_super_events.gfx`;
- portraits: `gfx/leaders/018_resources_found/`, registered in `interface/chaosx_characters.gfx`;
- flags: `gfx/flags/DHO*.tga` and matching medium/small files.

Icons and UI:

- 65 focus icons: `gfx/interface/goals/018_resources_found/`;
- cave and countermeasure ideas: `gfx/interface/ideas/018_resources_found/`;
- decision, category, and category-picture art: `gfx/interface/decisions/018_resources_found/`;
- selected-field static and animated assets: `gfx/interface/018_resources_found/` and `gfx/interface/animated/018_resources_found/`;
- 15 achievement complete, grey, and not-eligible triplets: `gfx/achievements/`.

All static sources, generated prompts, processed PNGs, DDS/TGA files, dimensions, animation frame plans, fallbacks, contact sheets, provenance, and sprite identifiers are recorded under `docs/assets/018_resources_found/`.

The exact-estimate refresh controls reuse `GFX_decision_generic_research`. The internal clock category and its nine non-rendered missions require no category art, mission icons, or localisation.

## Balance notes

The baseline discovery is economically valuable immediately but requires 90 to 240-day development projects and real industrial, transport, equipment, fuel, labor, stability, or political commitments to reach mature output. Foreign Pressure rises with material value rather than elapsed time alone. Safety lowers accident and incident risk but competes with extraction time and production commitments.

The cave opening is bounded at 30 divisions. Later growth is map-based and delayed: 10 resources per capacity, 10 capacity maximum per state, zero from the origin, 30 days of uninterrupted control, and sequential spawning. Counterplay therefore has three distinct windows: prevent emergence by full sealing, recapture an activating state, or break a mature anchor with hard-attack capable forces.

## Future plans

- Add more post-closure flavor only when it uses the closed-field history without reopening the resource ledger.
- Extend foreign contract identities when new route or trade APIs provide stronger material distinctions.
- Add Oth-Kesh leadership variants only with a mapped focus outcome, authored identity, generated portrait, and full animation fallback package.
- Add cave doctrine content through templates, objectives, anchors, and coalition responses rather than small passive modifiers.
