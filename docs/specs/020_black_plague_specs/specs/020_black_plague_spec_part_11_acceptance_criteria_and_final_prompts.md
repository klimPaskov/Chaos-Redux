# 020 Black Plague spec Part 11 - Acceptance criteria and final prompt alignment

This part defines the acceptance standard for Event 020 Black Plague as a full rework package. It is a planning and implementation handoff. It does not provide final player-facing localisation, super-event title text, option text, focus text, decision text, achievement text, quotes, slogans, cultural remarks, or audio selections.

All names in this file are working labels only where they refer to internal route or package structure.

## Package completion standard

Event 020 is complete only when the implemented mod behaves as a state-based Black Death system that connects to the existing Chaos Redux disease, biowarfare, death, chaos, mapmode, country, focus, super-event, and documentation layers. A small event popup, a temporary modifier, a single country idea, a continent-wide disease effect, or a static disease button set is not an acceptable implementation.

The implementation must preserve the playable promise from the user brief:

- the outbreak begins in one weighted mainland state
- the disease spreads state by state
- the same shared disease board handles preparation, threat response, infection response, containment, recovery, weapon exposure, and rat-threat response
- deaths reduce real state population and feed the shared Deaths and Chaos systems
- cure progress weakens the disease before it permits cleanup
- weaponization exists only at gameplay abstraction level through the existing biowarfare and special-project systems
- Evolutions I through V change the disease and unlock the rat-state escalation
- rat countries are actual nonhuman chaos countries
- the King of Rats is a separate country with a deeper focus tree and a terminal world-end route
- assets, super-events, achievements, AI, docs, and spreadsheet surfaces align with the finished implementation

Any smaller version must be reported as incomplete. The implementation agent must not call a fallback complete because the first popup works or because the disease appears somewhere on the map.

## Source-of-truth files

The accepted design package is the set of spec, matrix, prompt, research, and handoff files in this package.

Core spec parts:

- `specs/020_black_plague_spec_part_1_core_outbreak.md`
- `specs/020_black_plague_spec_part_2_dynamic_disease_board_and_decisions.md`
- `specs/020_black_plague_spec_part_3_spread_deaths_cure_weaponization.md`
- `specs/020_black_plague_spec_part_4_evolutions_i_ii_and_overseas.md`
- `specs/020_black_plague_spec_part_5_rat_nations_country_package.md`
- `specs/020_black_plague_spec_part_6_king_of_rats_world_end.md`
- `specs/020_black_plague_spec_part_7_focus_tree_blueprints_and_country_package_deepening.md`
- `specs/020_black_plague_spec_part_8_decision_mission_and_ui_blueprint.md`
- `specs/020_black_plague_spec_part_9_rat_warfare_units_and_counterplay.md`
- `specs/020_black_plague_spec_part_10_super_events_assets_achievements.md`
- `specs/020_black_plague_spec_part_11_acceptance_criteria_and_final_prompts.md`

Matrices and prompts:

- `matrices/020_black_plague_state_status_matrix.md`
- `matrices/020_black_plague_ai_behavior_matrix.md`
- `matrices/020_black_plague_asset_matrix.md`
- `matrices/020_black_plague_country_package_matrix.md`
- `matrices/020_black_plague_focus_route_matrix.md`
- `matrices/020_black_plague_decision_mission_matrix.md`
- `prompts/020_black_plague_asset_prompt.md`
- `prompts/020_black_plague_super_event_prompt.md`
- `prompts/020_black_plague_achievement_prompt.md`
- `prompts/020_black_plague_decision_mission_prompt.md`
- `prompts/020_black_plague_subagent_routing_prompt.md`
- `prompts/020_black_plague_coding_prompt.md`
- `prompts/020_black_plague_goal_prompt.md`

The old catalog row that describes a continent-wide temporary idea is not design authority. It is stale source history and should be replaced after implementation wording is final.

## No-simplification rules

The following substitutions are not acceptable unless the user explicitly approves a reduced scope before implementation:

| Required design | Unacceptable simplification |
| --- | --- |
| state-based disease statuses | one national spirit or one continent-wide modifier |
| shared disease board | separate duplicate Black Plague category |
| dynamic spread and death ticks | one event that applies a fixed penalty |
| real state population loss | only reducing recruitable manpower or adding generic attrition |
| cure progress over time | instant cure button or instant modifier removal |
| biowarfare integration | one event option that unlocks a payload without projects, risks, and condemnation |
| dynamic mapmode and black fog direction | a static icon that never updates by state status |
| rat countries | rebels with ordinary human manpower and infantry equipment |
| King country | cosmetic rename of a base rat tag |
| rat focus trees | thin vertical chains with repeated small modifiers |
| world-end path | a normal conquest reward or ordinary super-event |
| achievements | automatic unlocks from event fire or obvious first click |
| assets | placeholders, reused unrelated sprites, or missing manifests |
| AI behavior | flat weights that ignore war, borders, infection, cure state, rat pressure, and route validity |

Every missing surface must appear in the completion report. A placeholder can be useful during development, but it cannot be counted as a finished Event 020 surface.

## State-based disease requirements

The disease layer must treat states as the main objects. Every infected, threatened, contained, recovering, cured, weaponized, and rat-held state must carry enough script state for the shared disease board, mapmode, AI, death ticks, spread checks, cure logic, recovery logic, and cleanup logic to read it.

Minimum state data expected by the design:

- disease identity for Black Death
- current state status
- severity or disease load
- containment level
- medical support or treatment level
- cure protection applied to the state
- relapse or recovery residue where relevant
- weaponized exposure marker where relevant
- rat warren pressure where relevant
- recent death pressure or cumulative deaths where implementation needs it
- spread source strength
- cooldowns or flags that prevent duplicate target decisions or duplicate mission rows

The first outbreak selection must be weighted toward mainland states that combine high population with low development, poor infrastructure, weak prevention, poor state capacity, and crowding. Islands should not be selected for the initial baseline outbreak unless a manual scenario or later evolution explicitly changes the opening package.

The outbreak should start with limited deaths, then become more dangerous through local severity, missed response, weak cure progress, Evolution I, uncontrolled spread, and rat pressure. The early state must be survivable if the player reacts quickly. Ignoring it must be able to cause very large population loss.

## Shared disease-board requirements

The player must interact with Black Death through the shared disease and biowarfare decision surface. A duplicate Black Plague-only decision category would break the design. The shared board should show different available actions depending on state status and country exposure.

The board must support these state groups:

- clean and prepared states
- threatened states
- infected states
- contained states
- recovering or cured states with relapse risk
- weaponized exposure states
- rat-held states or rat-border states

The decision board must feel like a changing crisis board, not a flat checklist. It should hide obsolete actions, show current target states, use dynamic status summaries, and use AI-equivalent actions where the human UI has click choices.

Acceptance requires:

- state-target decisions or target-selection flow that does not flood the player with every possible state at once
- clear costs beyond only political power or command power
- state named or region named requirements instead of raw state id clutter
- available and blocked tooltips that explain supply, equipment, port, border, hospital, unit, cure, or cleanup requirements
- cleanup of stale target flags, missions, and event targets when a state changes status
- AI paths for preparation, quarantine, cure support, port inspection, containment, cleanup, and rat-border operations

## Deaths, population, and Chaos integration

Black Death deaths must reduce real state population and pass through the shared Deaths system. This includes ordinary outbreak deaths, severe stage deaths, weaponized exposure deaths, rat occupation deaths, uncontrolled relapse deaths, and cleanup failure deaths where applicable.

Deaths should also feed Chaos through the existing death-to-chaos relationship, with any event-specific chaos changes kept aligned with the shared system. The implementation should avoid double counting the same death event. If the shared Deaths system already applies Chaos changes, Event 020 should not add a parallel chaos bump for the same population loss unless the spec defines a separate public panic, global threat, or condemnation effect.

Death scaling should consider:

- current state population
- disease severity
- containment level
- treatment and cure progress
- infrastructure and state capacity
- war, occupation, resistance, and refugee pressure
- rat-held or warren pressure
- evolution state
- weaponized exposure markers
- active medical missions and cleanup missions

Ignored high-population states should be able to suffer devastating losses. This does not mean every state dies instantly. The system should create worsening ticks over time, with clear opportunities for prevention, treatment, containment, and cleanup.

## Cure and countermeasure requirements

Cure progress is a global, country, or shared disease value according to the existing biowarfare system pattern. The exact storage belongs to implementation, but the behavior must match the spec:

- early progress reduces death pressure slightly
- middle progress reduces spread and severity more strongly
- high progress unlocks better treatment and cleanup
- full or near-full progress permits state recovery actions
- cure progress should not instantly erase all infected states
- cure progress should be harder after Evolution I
- cure progress should interact with sample access, medical programs, study decisions, international sharing, accidents, and weaponization risk

Countries with infected states should be able to contribute to cure research. Countries without infection but with strong medical or biowarfare capacity can participate through prevention or shared countermeasure work if the existing system supports it. AI countries should not sit idle when the disease threatens them or their borders.

Cure-related localisation should describe broad visible medical progress and response capacity. It should not expose hidden formulas or future rat evolutions too early.

## Weaponization boundary

Weaponization must stay at a high-level gameplay abstraction. The special-project path may represent sample study, safety systems, delivery integration, stockpile handling, accident risk, condemnation, retaliation, and deployment unlocks. It must not include real-world wet-lab steps, culturing instructions, protocols, genetic manipulation details, dosage guidance, delivery engineering, or actionable biological weapon procedure.

Acceptance requires:

- use of the existing biowarfare and special-project structure where possible
- long project pacing and unique iteration direction
- defensive study and weaponization kept distinct enough that achievement disqualifiers and accident logic can read them
- lab leak, stockpile accident, domestic blowback, runaway spread, condemnation, and retaliation risks represented as gameplay outcomes
- deployment into enemy states handled through existing biowarfare delivery systems or their safe abstractions
- clear player warning that weaponization is dangerous in gameplay terms

If implementation cannot safely integrate with existing special projects, this surface should be blocked and reported. It should not become a one-off event button.

## Evolution acceptance criteria

The evolution chain must preserve the split between baseline disease stages and actual evolutions.

Evolution I:

- makes the strain harder to cure
- increases lethality and crisis speed
- modestly increases spread pressure
- updates disease board, AI urgency, and evolution log content

Evolution II:

- unlocks overseas and port-connected spread
- uses ports, convoys, troop routes, naval access, and island exposure as factors
- adds port inspection and maritime prevention importance
- does not turn the disease into instant global teleportation

Evolution III:

- unlocks rat nation emergence from worst diseased states
- requires uncontrolled connected infection, high severity, or collapse pressure
- creates actual nonhuman chaos countries that remain plague sources
- keeps Black Death state modifiers in rat-held states

Evolution IV:

- creates a separate King of Rats country from the strongest rat nation
- transfers or unifies rat holdings and forces
- unlocks the deeper King focus tree and King super-event package
- updates world-threat logic and AI behavior

Evolution V:

- unlocks the King world-end route
- requires focus progress plus continent or state-set control and death or rat-held pressure
- triggers the terminal world-end scenario only after world-end rules are satisfied

Each evolution must support active-event entry where relevant. If the event has not fired yet and the campaign state supports a stronger opening, the implementation may use a pre-fire evolved opening only if it follows the spec and logs the evolution properly.

## Rat country package requirements

Base rat nations are not ordinary rebels. They are actual nonhuman chaos countries with their own country setup and AI.

Acceptance requires:

- registered tags or tag pool for rat nations
- shared special chaos country and actual nonhuman classification
- starting ownership and control setup for infected states that break away
- plague state retention after spawn
- leader portrait or institutional portrait direction, with generated nonhuman or symbolic source mode
- base flag and possible variant flags in normal, medium, and small sizes
- country names, adjectives, parties, and ideology direction that read as public country names, not internal offices
- starting unit templates or unit families using nonhuman rat logic
- no human manpower or ordinary equipment dependence
- automatic reinforcement tick based on state severity, population consumed, warren strength, terrain, ports, and focus progress
- hostile behavior toward all human countries
- rat-to-rat absorption where stronger adjacent rat countries can annex weaker ones and inherit units or warren strength
- base rat focus tree routes for warren growth, swarm warfare, plague ecology, defense, absorption, and King preparation
- AI behavior that expands, defends warrens, absorbs weaker rats, targets vulnerable human states, and avoids nonsensical diplomacy

If multiple rat tags are used, every tag must have safe cleanup, country setup, flag coverage, localisation coverage, AI behavior, and no conflict with existing tags.

## King of Rats requirements

The King of Rats must be a separate country package, not a renamed base rat nation. It should feel like organized nonhuman statehood with route choices and a terminal ambition.

Acceptance requires:

- separate tag or well-defined country identity
- King formation logic from the strongest rat nation
- transfer or absorption of rat states and forces
- King reveal super-event after research and asset work
- King leader portrait and possible animated portrait package
- King flag and route variant direction where route changes justify visible identity shifts
- deeper focus tree with coronation, sentience, government routes, swarm command, warren economy, plague mastery, human terror, rat unity, continental conquest, and world-end route
- government route differences such as Royal Command, Brood Council, and Hunger Mind or their accepted equivalents
- idea lifecycle that changes King command, warren organization, plague ecology, and route identity
- King-specific unit growth and elite units
- AI that pursues growth, continent control, plague pressure, and world-end route only when route and campaign state support it
- defeat and cleanup behavior that leaves meaningful aftermath if the King was a large threat

The King should be much stronger than base rats once its route matures. It can become deliberately overpowered if it earns the terminal path, but it still needs readable thresholds, counterplay windows, and route commitments.

## Focus tree acceptance criteria

Base rat and King focus trees must follow the route-family design from Part 7 and the focus route matrix. They should be real focus trees, not a generated list of repeated stat rewards.

Base rat tree acceptance:

- opening survival and warren consolidation
- swarm growth and automatic unit tick hooks
- plague ecology branch that changes disease pressure
- human war branch for attacks, supply sabotage, and state conversion
- defense branch for burrow survival and border pressure
- absorption branch for rat-to-rat annexation behavior
- King preparation branch that can feed King formation
- AI route weights for defensive, aggressive, absorption, and King-preparation behavior

King tree acceptance:

- coronation trunk that establishes sentience and command
- government route family with meaningful locks and payoffs
- swarm command and elite rat unit path
- warren economy and nonhuman production or growth path
- plague mastery path that changes disease behavior and cure resistance
- human terror and resistance-shattering path
- rat unity and absorption consolidation path
- continental conquest path
- terminal world-end path gated by territory, deaths, focus progress, and world-end rules
- route-specific ideas, decisions, AI behavior, flags, portraits, and assets where relevant

Focus rewards should unlock systems, decisions, units, missions, map changes, AI behavior, ideas, or route states. Small passive modifiers can support a focus, but they must not form the main branch design.

## Decision, mission, and UI acceptance criteria

The disease board and anti-rat layer must implement the decision and mission families from Part 8, Part 9, and the decision mission matrix.

Decision family acceptance:

- preparedness and surveillance for clean or prepared states
- threatened-state border, port, troop-route, and refugee controls
- infected-state quarantine, lockdown, hospitals, treatment, army cordon, cleanup, and vector control
- contained-state monitoring and controlled reopening
- recovery-state cleanup and relapse prevention
- weaponized exposure containment and investigation
- cure research and countermeasure contribution
- anti-rat cordon, evacuation, fortification, nest assault, cleanup, and border containment
- international coordination where the shared system supports it

Mission acceptance:

- use timed missions for holding borders, guarding ports, protecting cleanup crews, retaking rat states, maintaining cordons, and sustaining cure work
- include success, failure, and partial success where the outcome supports it
- give the player enough time to act
- hide or cancel stale missions when targets change status or ownership
- prevent duplicate mission spam from the same state and category

UI acceptance:

- show state status, severity, containment, cure effect, spread risk, and available action type clearly
- update mapmode and selected state display whenever status changes
- support black fog or an engine-supported equivalent disease presentation
- use static fallbacks for any animated UI assets
- keep hidden rat and King content out of early disease text and UI until public reveal conditions are met

## Rat warfare and counterplay acceptance criteria

Rat warfare must feel different from human warfare. Rats do not use human manpower or normal equipment. They grow from plague ecology, warren strength, controlled infected states, terrain, focus progress, and King command.

Rat unit acceptance:

- baseline swarm units for ordinary expansion
- fast urban or infrastructure attack units where the design uses them
- plague gnawer or disease-spreading units where evolution and focus state allow them
- burrow guard or defensive units for warren states
- brood mass or late swarm units for high growth states
- King guard or elite units for King routes

Human counterplay acceptance:

- cordon missions that require units and supply in border states
- port and rail controls where rat spread or disease spread uses movement routes
- anti-warren operations that need equipment, time, and controlled states
- cleanup operations after retaking rat-held plague states
- cure and treatment support that reduces disease deaths during military operations
- emergency evacuation or scorched cleanup only where the spec permits harsh tradeoffs
- AI cooperation and world-threat behavior when the King becomes a large threat

The player must be able to defeat rats through effort, timing, and investment. The design should not make them impossible before the world-end route is earned.

## World-end acceptance criteria

The rat world-end scenario is terminal. It should not fire from ordinary spread or a strong rat country alone.

Required conditions:

- King of Rats exists
- King has progressed through the world-end focus path
- world-end global rules are satisfied
- King controls the required continent, state set, or accepted equivalent
- death pressure, rat-held territory pressure, or plague-state pressure is high enough
- no incompatible world-end scenario is already active

World-end implementation must:

- set the generic world-end flag
- set the rat-specific world-end flag
- show the rat world-end super-event with researched text, image, and audio
- gate incompatible future random event behavior where world-end rules require it
- document the scenario in event docs and spreadsheet after implementation wording is final
- make the terminal state clear through gameplay and UI

## Super-event acceptance criteria

Required super-events:

- King reveal
- rat world-end

Conditional super-event candidates:

- continental rat threat escalation if implementation accepts it as campaign-defining
- rat defeat aftermath if the King became global or near-global before defeat

Every implemented super-event requires:

- role and trigger alignment with the spec
- researched title direction converted into final title only after research
- researched quote with exact wording and attribution confidence
- researched cultural remark or button direction with copyright-safe wording
- generated or sourced image with manifest and DDS handoff
- unique real audio track with source, license, duration, conversion notes, and sound id handoff
- settings-aware playback wiring in implementation
- docs and spreadsheet alignment after final text exists

Unresearched titles, button text, quotes, cultural remarks, allusions, slogans, lyric fragments, and audio choices are blockers. They must not become final localisation.

## Asset acceptance criteria

All visible surfaces need asset coverage or a documented blocker.

Required asset families:

- disease icons and state status visuals
- black fog or approved state disease presentation
- shared disease board UI assets
- decision and mission icons
- idea and national spirit icons
- focus icons for base rats and King route families
- rat country flags and King route flags where used
- base rat leader or institutional portrait
- King portrait and optional animated overlay
- mutated rat unit icons
- anti-rat counterplay icons
- report and news images for key disease and rat thresholds
- super-event images for required packages
- achievement icons for the full suite

Every final asset must have source mode, processed preview, final game file, target size, sprite name where relevant, target surface, manifest entry, and handoff note. Animated assets require source frames, processed frames, sheet PNG, sheet DDS, static fallback, contact sheet, preview GIF for review, and frame metadata.

No asset should be marked complete if it is a resized icon from another asset type, a placeholder, a primitive local drawing, an unlicensed sourced image, or a generated artifact without manifest notes.

## Achievement acceptance criteria

Achievements should reward mastery and rare routes. They must not unlock automatically when the event fires.

The suite should cover:

- clean containment
- severe outbreak recovery without weaponization
- port and overseas prevention
- defensive study without weaponization
- dangerous weaponization survival
- first warren destruction
- preventing the King
- defeating the King
- continent cleanup
- base rat play
- King formation
- King government route mastery
- King continent control
- rat world-end
- human recovery after near-terminal King threat

Each achievement needs:

- working id converted into a final registered achievement id
- final title and description written from direction only after implementation context is stable
- visibility or hidden status
- unlock conditions
- disqualifiers
- tracking flags or variables
- icon direction and final icon variants
- docs and spreadsheet alignment where applicable

Achievement text can reveal hidden content only if the achievement is hidden or if the route is already public according to the final achievement design.

## AI acceptance criteria

The AI layer must cover all important actor groups:

- outbreak owner
- countries with threatened states
- countries with infected states
- countries with ports after Evolution II
- countries with biowarfare capability
- neighbors of infected states
- neighbors of rat-held states
- great powers and faction leaders
- base rat nations
- King of Rats
- human coalition or containment leaders

AI must consider disease severity, population at risk, state status, war state, stability, industry, supply, manpower, equipment, ports, borders, cure progress, containment level, rat pressure, ideology, condemnation, and route validity.

Dangerous choices such as weaponization, harsh lockdowns, evacuation, extreme cleanup, or risky rat assaults should not be flat random clicks. They should depend on desperation, ideology, capability, war situation, and threat level.

Rat AI must not behave like a normal human country. It should expand from warren logic, plague states, vulnerable borders, supply weaknesses, and King command route state. Diplomacy should be minimal or hostile unless the spec later accepts a strange high-chaos exception.

## Documentation and spreadsheet acceptance criteria

Implementation must update the Chaos Redux documentation and event catalog after final gameplay and localisation exist.

Docs should cover:

- what Event 020 is
- state-based outbreak flow
- disease board and decision flow
- death and cure model
- weaponization at gameplay abstraction level
- evolutions
- rat nations
- King of Rats
- world-end scenario
- super-events
- assets and known blockers
- AI behavior
- limitations and accepted future work if any

Spreadsheet alignment should happen after final in-game event-detail and evolution-detail wording exists. The spreadsheet worker should mirror player-facing text from localisation where required. It should not invent implementation status or copy planning labels as final wording.

## Validation and audit acceptance criteria

Before completion claims, the implementation environment should run the relevant project audits:

- scripted-system review for repeated disease, spread, death, cure, mapmode, rat tick, and cleanup helpers
- decision and mission audit for shared disease board choices
- focus tree audit for base rat and King trees
- country package audit for rat tags and King tag
- localisation audit for all player-facing text and dynamic strings
- asset manifest and sprite handoff review
- super-event research and audio validation
- event completion audit against the accepted spec package
- spreadsheet update after final wording exists

Validation should focus on Event 020 surfaces that can realistically fail:

- status changes update mapmode and disease board
- first outbreak state is weighted and mainland
- death ticks reduce population and feed shared Deaths
- cure progress reduces harm before cleanup
- overseas spread waits for Evolution II
- rat emergence waits for Evolution III
- King formation waits for Evolution IV
- world-end waits for Evolution V, focus progress, territory, death pressure, and world-end rules
- rat countries do not use human manpower or normal equipment
- stale decisions and missions clean up when states change status
- AI has a valid path for disease response and rat warfare

Passing boilerplate checks should not replace meaningful validation.

## Final prompt alignment

The prompt files in this package have been revised to reflect Part 8 through Part 11. The coding prompt should be treated as the implementation overview. The goal prompt remains a condensed 3500 to 4000 character version for starting the implementation goal. Asset, super-event, achievement, decision and mission, and subagent prompts should be handed to the appropriate implementation or subagent worker when the live repository environment is available.

The implementation agent should not assume the planning spec contains final localisation. It contains design direction and research gates. Final text belongs to implementation after source checks where needed.

## Near-completion improvement-loop status

The current environment cannot actually spawn project Codex subagents. A manual anti-bloat and depth review using the uploaded improvement-loop skill was recorded in the handoff folder, and this Part 11 incorporates the resulting closure-style requirements. This does not replace the required project subagent pass in a live implementation environment. The next agent with access to project subagent spawning should run `chaosx_improvement_loop_planner` with `fork_context=false`, then record whether it produces a closure handoff or an expansion addendum.

Until that live subagent pass is run or explicitly waived by the project owner, the planning package should be treated as a complete candidate spec package with a process blocker, not as a fully process-final canonical package.
