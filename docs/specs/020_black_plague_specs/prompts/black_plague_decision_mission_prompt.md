# Black Plague Decision and Mission Implementation Prompt

> Historical accepted-design prompt, reconciled 2026-08-09: the dedicated-response-category correction supersedes the single-category instructions below. National cure, logistics, cooperation, knowledge, and recovery use `black_plague_response_category`; selected-state containment and anti-rat actions remain in `chaosx_disease_containment_category`. Crown Strike and Seal Royal Burrows use state-selected zero-day launchers backed by native `activate_mission`/`days_mission_timeout` owners with explicit state markers and shared-action resolvers. Hold the Line and Secure the Refuge remain native `activate_mission`/`days_mission_timeout` missions. SCN-012 repeat signals are reconciliation-only and its live intensity postcondition verifies RTA/RTX floors. The current two-tag boundary and separately promoted shared rat ground-unit model/entity package are recorded in the source-of-truth map and model handoff; no per-subtype or Rat King-specific model is authorized, and sound-definition wiring, counter review, and live model validation remain open. The promoted weapon-delivery icon/source-frame Rat King-seal packages and implemented `.57-.59`, `.64-.65`, and `.71-.75` surfaces are recorded in the consequence/aftermath addendum.

Implement the full Event 20 decision and mission system from the accepted spec and `matrices/decision_mission_matrix.md`. Read `AGENTS.md`, `chaos-redux-events`, and `hoi4-decisions-missions` first. Inspect the live shared biological warfare and disease category before editing.

## Core ownership rule

Register Event 20 in both the dedicated Black Plague response category and the existing disease-containment UI. National cure, medical logistics, cooperation, knowledge policy, and recovery belong to the dedicated category. Generic disease actions and Black Plague state containment remain shared and selected-state gated. Both surfaces read the appropriate country phase, local status, exposure routes, countermeasure progress, Rat Infestation, and evolution stage without duplicating cure progress or payment effects.

## Required phase behavior

Implement dynamic action families for:

- Prepared country
- Exposed country
- Infected country and selected state
- Containment
- Recovery and Cured monitoring
- anti-rat response after Evolution III
- Rat Nation country mechanics
- Rat King country mechanics

Hide obsolete actions and replace weaker versions as the crisis progresses. The category should show a curated current action set, not a debug wall.

## Human-country actions

Implement every generic action family in the decision matrix, including surveillance, reserves, inspections, targeted border and port controls, troop restrictions, field hospitals, quarantine, army cordons, emergency hospitals, relief corridors, burial and sanitation crews, vector control, treatment distribution, evacuation, controlled reopening, residual tracing, recovery, foreign medical aid, countermeasure exchange, and anti-rat clearance.

Also implement the separate Black Plague-specific state entries inside the shared containment category:

- Clean the City of Rats
- Seal Granaries, Markets, and Warehouses
- Clear Sewers and Burrow Shafts
- Flea, Shelter, and Bedding Control
- Purge Vermin from Rail Yards and Docks
- Demolish Infested Blocks
- Purge the Warrens after Liberation

These actions must change visible Rat Infestation and related spread, mortality, emergence, burrow, or resurgence pressure. They need distinct costs, cooldowns, target rules, AI use, and failure states. They must not be compressed back into one generic vector-control button.

### Cost rules

Use fitting dynamic costs:

- support equipment
- trucks
- trains
- convoys
- fuel
- civilian factory burden
- consumer goods
- tied divisions
- command power at conservative levels
- stability
- war support
- compliance and resistance pressure
- supply and reinforcement penalties
- medical reserve
- intelligence exposure

Political power may support a bureaucratic action. It must not be the only meaningful cost for emergency, military, medical, or logistical actions.

### Key tradeoffs

- quarantine without relief can raise deaths
- army cordons tie down real military capacity
- port closure protects health while damaging overseas supply
- troop restrictions reduce spread while weakening fronts
- evacuation can move infection to receiving states
- controlled reopening restores output while raising relapse risk
- broad response creates national emergency burden
- city rat clearing can scatter infected vermin when transport, food stores, shelters, and adjacent states are not controlled
- demolishing infested blocks can reduce local disease while causing displacement, resistance, and regional spread

## Missions

Use timed missions for actions that require holding or protecting real geography.

Required mission families include:

- maintain a border cordon
- protect a relief corridor
- keep a port open and inspected
- hold a capital against Rat Nations
- clear a burrow node
- liberate and quarantine a rat state
- strike a royal burrow node
- protect a countermeasure research center
- hold designated continental capitals and relief ports
- complete Crown the Continent objectives

Name real dynamic states, ports, capitals, corridors, or selected regions in tooltips. Do not expose raw state ID lists.

## Countermeasure actions

Implement beginning, sharing, hoarding, stealing, and international cooperation through the dedicated Black Plague category while reusing the shared disease effects and progress producer. Full progress reduces mortality and spread and allows cleanup. It never removes active disease instantly.

## Rat Nation mechanics

Rat players use decisions to alter brood pulses, establish burrow nodes, exploit or preserve controlled populations, and challenge or resist rival absorption. They cannot buy ordinary units.

## Rat King mechanics

Implement royal pulse doctrine, regional brood administration, population policy, intelligence operations, continent selection, capital objectives, Crown the Continent, and world-end readiness. The player cannot switch target continent freely after committing to the path.

## Triggerable scenario initialization

After the Black Plague triggerable scenario launches, every affected human country must immediately see the dedicated national-response category and the correct Prepared, Exposed, Infected, or anti-rat set in the shared containment category. The scenario can seed many states and actors in one bootstrap, so decision activation must batch safely and avoid duplicate targets or missions. The full disease mapmode rebuild and decision refresh must complete before ordinary weekly processing resumes.

## AI

Every meaningful human GUI action needs an AI equivalent that evaluates all valid targets without using the human selector. Use the AI strategy matrix. Block invalid countries, dead targets, disabled evolutions, missing routes, absent ports, and impossible state objectives.

## Cleanup and exploits

- cancel missions when target or owner becomes invalid
- clear selected target flags and variables
- prevent repeated reward farming
- prevent free unit, equipment, cure, and aid loops
- prevent multiple cordons or hospitals from stacking beyond designed caps
- prevent Rat Nation pulse decisions from bypassing the timed reinforcement system
- prevent world-end missions from completing after continent control is lost
- hide Black Plague-specific decisions when another disease is selected or no valid Black Plague target remains
- clear scenario-only selected targets and activation flags after bootstrap

## Localisation

Use icon-first costs and dynamic state or country names. Long requirements need custom trigger tooltips. Final text must describe public actions and visible consequences without hidden evolution or achievement spoilers.

## Completion audit

After implementation, run the decision and mission auditor. Report both category lifecycles, every Black Plague-specific action ID and its owning category, mission owners and targets, durations, success and failure behavior, Rat Infestation changes, scenario initialization, AI validity, cleanup, exploit findings, and every simplification.
