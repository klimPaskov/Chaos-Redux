# Country package, starting forces, and model planning standards

Read the relevant complete section before specifying a country package, a formable nation, starting or reinforcing forces, a new unit type, or a 3D model.

## Country package and dynamic identity standard

When an event creates, releases, transforms, or significantly modifies a country, the spec must define that country as a full package. This applies to new custom tags and to existing countries that gain event-specific political identities, focus trees, flags, leaders, cosmetic names, ideology names, starting forces, or mechanics.

Before assigning a new tag, inventory vanilla country tags and identities, Chaos Redux tags, every installed Workshop mod's country tags, and other local mods. A new tag must be unused across that complete installed set. If the country or national identity already exists in vanilla, reuse the vanilla tag and plan safe additive content. Do not create a duplicate country under a new tag. Preserve a living vanilla country and any meaningful vanilla or existing tree. When an event requires a naming family such as a suffix convention, apply that convention only after the collision audit. Record the audited source roots, conflicts, reused vanilla tags, and unresolved identity matches in the specification or coding-agent prompt.

For every new country, and every existing country that is meaningfully changed, the spec should provide a country package matrix or equivalent structured section. It must cover:

- tag or placeholder tag, with a note that final tags must avoid conflicts
- spawn, release, transformation, or takeover conditions
- core territory, claimed territory, disputed territory, and fallback territory
- history file needs for new custom tags, generated startup scientists for existing countries when characters are needed, and additive startup setup for existing countries
- public country name and cosmetic names, following the country naming rules below
- ideology-specific names
- focus-tree route names
- faction names and possible faction cosmetic names
- ruling party names, sub-ideology labels, and political movement names
- starting politics and possible ideology shifts
- starting military package, including initial divisions, template families, manpower, equipment, command structure, supply assumptions, and dynamic scaling factors
- unit growth routes through decisions, focuses, objectives, volunteers, mobilisation, depots, foreign support, faction reserves, or special mechanics
- starting leader, leader traits, portraits, and possible leader replacements
- council, junta, committee, regency, cult, military, monarchist, democratic, communist, fascist, anarchist, or factional leadership variants when relevant
- flags for the base country, ideology variants, focus-tree variants, cosmetic variants, puppet variants, and major route transformations
- national spirits, ideas, decisions, events, focus tree, achievements, mechanics, and unit systems tied to that country
- AI behavior and route preferences
- asset needs for every visible identity state
- localisation tone and naming rules
- documentation needs
- compatibility notes if the country already exists in vanilla, Chaos Redux, or common mods
- a relevance-gated detail pass for capitals and settlement names, optional intelligence and MIO identity, useful character flavour, navy and air forces when relevant, starting research, economy, stockpiles, laws, subject status, equipment identity, and DLC compatibility

Do not treat a custom country as complete because it has a tag and one flag. A serious country needs identity, politics, names, flags, leaders, starting forces, force-growth routes, mechanics, decisions, AI, localisation, assets, and route changes. If the country is only temporary and does not need a full package, the spec must explain why.

Political identity should be dynamic when the content supports it. Focus routes, ideology changes, coups, faction victories, foreign puppeting, religious transformations, high-chaos mutations, monarchist restorations, military takeovers, revolutionary councils, or world-order paths should be able to change the country name, flag, ruling party, leader, leader portrait, leader trait, cosmetic tag, national spirits, available decisions, and available recruitment systems when appropriate.

### Relevance-gated country detail pass

Small country details must be assessed deliberately, but they must not become a quota. Include a detail only when it supports the country's identity, starting position, military role, route logic, or player experience. Omit optional surfaces that would exist only to make the package look larger. Do not add an absence section for every omitted surface.

Persistent playable countries, countries with fixed historical or fictional identities, and countries expected to survive for a meaningful part of the campaign need the deepest assessment. Short-lived emergency actors and highly dynamic random countries may use shared packages when custom content would add no value. Dynamic generation does not excuse missing setup when the country still needs a valid capital, economy, army, laws, research base, or equipment package.

#### Capitals, settlements, culture, and names

Plan capital and settlement details when territory or cultural identity makes them meaningful.

For a country with fixed or bounded territory, define:

- primary capital and the states or cities that can serve as backup capitals
- relocation behavior after the capital is lost, transferred, isolated, or made invalid
- whether the capital changes through a political route, formable, conquest, restoration, evacuation, or cultural transformation
- victory-point, city, port, and regional renames caused by language, culture, religion, ideology, restoration, colonisation, decolonisation, or another real identity change
- route-specific renames and the conditions that apply or reverse them
- localisation and research direction for every culturally or historically grounded name

For a dynamic country without fixed starting territory, define how the event selects a valid controlled city or victory point after the territory is chosen. The selected city may become the capital and may receive a new name when the country's culture, ideology, mythology, or route gives a clear reason. Dynamic naming should use a researched or designed naming pool that matches the country's identity. The plan should also explain how a backup capital is selected from the country's remaining valid cities when the first capital is lost.

Do not rename cities because a government changed its cabinet or party label. City and regional renames should reflect a deeper cultural, linguistic, religious, historical, colonial, revolutionary, or high-chaos identity change.

#### Optional intelligence, MIO, and character flavour

An intelligence package is optional and should remain minimal. Plan it only when espionage, internal security, clandestine politics, resistance, infiltration, cryptology, foreign sponsorship, or a secret route is part of the country's identity or gameplay. A useful package may define a country-specific agency name and emblem, one or more meaningful upgrades, a small operative identity, or a relevant operation family. Do not create a custom agency package for a country that would play the same without it.

Custom military industrial organizations are optional. Plan them for countries with a fixed identity, a distinctive industrial institution, a meaningful equipment tradition, a route built around military production, or a country-specific manufacturer that changes equipment development. A small number of specific MIOs is better than a complete generic roster. Dynamic countries should not receive custom MIOs by default. Do not create MIOs only because the DLC system exists.

Advisors, theorists, high command, commanders, scientists, operatives, and other characters can strengthen country identity. Add them when a person, institution, faction, profession, or regional tradition gives the country useful flavour or supports a real route. Do not fill every available role. One memorable and mechanically relevant character is better than a padded roster of interchangeable bonuses.

For every optional institution or character that is included, define its role, route connection, availability, removal or replacement conditions, AI use, localisation direction, and visible identity. If a surface does not add flavour or gameplay, omit it cleanly.

#### Navy and air force relevance gate

Assess whether the country should have a navy or air force from its territory, ports, islands, airbases, inherited forces, strategic role, industrial capacity, culture, doctrine, and event premise.

When a navy matters, plan it thoroughly. Define the starting fleet or dynamic generation rule, deployment ports, ship classes and variants, naming direction, admirals, doctrine, repair and fuel needs, starting stock, production path, reinforcement path, mission priorities, route changes, and AI use. A dynamic country can scale its navy from controlled ports, dockyards, coastline, captured ships, former-owner forces, chaos tier, and foreign support.

When an air force matters, plan it thoroughly. Define the starting air wings or dynamic generation rule, deployment bases, aircraft types and variants, naming direction, air commanders or chiefs when useful, doctrine, fuel and pilot assumptions, starting stock, production path, reinforcement path, mission priorities, route changes, and AI use. A dynamic country can scale its air force from controlled airbases, military factories, inherited aircraft, chaos tier, foreign support, and available fuel.

Do not add a token navy or air force to satisfy a checklist. If naval or air power is part of the country's survival, expansion, geography, or identity, omitting its full plan is a country-package failure.

#### Starting research, economy, laws, stockpiles, and equipment identity

Every persistent playable country and every country expected to fight or develop independently needs a coherent starting setup.

Plan:

- exact starting research-slot count, including the reason for unusually low or high access
- exact starting technologies, doctrine progress, disabled or unavailable technologies, and any inherited research
- dynamic technology rules for random countries, based on origin, former owner, date, territory, industry, route, chaos tier, and event intensity
- starting civilian factories, military factories, dockyards, damaged industry, construction capacity, and production lines
- initial manpower, infantry equipment, support equipment, artillery, trucks, trains, convoys, fuel, aircraft, ships, tanks, and special stockpiles that the country actually needs
- supply position, railway access, ports, resource access, imports, production licences, foreign contracts, and dependence on a sponsor or former owner when relevant
- starting conscription, economy, trade, and occupation laws
- subject type, autonomy level, guarantees, military access, docking rights, faction status, government-in-exile status, and other starting diplomatic constraints
- equipment identity, including country-specific names, variants, module presets, improvised or inherited equipment, upgrade paths, production ownership, and visual or 3D requirements when relevant
- AI research, production, stockpile, law, trade, and equipment priorities

The setup can use exact values for a fixed country or clear generation rules for a dynamic country. Do not copy one default package across countries whose territory, culture, military role, or origin should produce different capabilities.

#### DLC and feature compatibility

Every event must remain playable and complete with every DLC combination, including no DLC. The spec must identify every planned surface that depends on DLC and define how the core event works when that DLC is absent.

Treat the no-DLC route and DLC-enhanced route as supported implementations. The no-DLC route must preserve the event premise, progression, AI behavior, balance role, cleanup, and main outcomes. DLC systems may add deeper presentation, institutions, decisions, operations, organizations, designers, markets, special projects, or other supported mechanics. They must not become a hidden requirement for the event to start or finish.

For every relevant DLC-backed surface, define:

- what the DLC version adds
- what base-game system represents the same core action when the DLC is absent
- what differences in cost, timing, visibility, AI behavior, and balance need separate tuning
- how saved flags, variables, characters, units, and country setup remain valid in both paths

If a DLC feature adds flavour only, it may be omitted in the no-DLC version without a substitute. If it carries core gameplay, the base-game implementation needs an equivalent playable action. The coding-agent prompt should require validation with no DLC, with each directly relevant DLC, and with the full supported DLC set.

### Country naming rules

Country names must be direct public country names that remain readable on the map.

Do not build public country names from internal political attachments. Avoid names that use terms such as `Military Office`, `Compact`, `Bureau`, `Authority`, `Mission`, `Board`, or similar administrative labels as the country name. These terms can exist as mechanics, focus groups, advisors, decisions, councils, ministries, internal institutions, route labels, or faction mechanics when they fit. They should not be the public name printed on the map.

Ideology-specific country names are allowed when they fit the route. Sultanate, Kingdom, Empire, Republic, Union, Commune, Federation, and similar public state forms are valid when they match the ideology, historical claim, route, or formable identity.

Prefer names built from the country, people, dynasty, region, or formable identity, then add a simple public state form only when it improves clarity. Style examples include:

- `Asante`
- `Kingdom of Asante`
- `Asante Republic`
- `Sultanate of Kilwa`
- `Kongo`
- `Kongo Commune`

Do not overload country names with political office language. The political office, emergency cabinet, military committee, colonial mission, compact council, bureau, authority, or board can be a mechanic or institution inside the country package. The map name should stay short and readable.

Names may depend on ideology, route, leader, formable status, puppet status, or high-chaos transformation. Even then, the public name should remain a country name, not an agency name.

For alternate governments, design internal bodies and party names separately from public country names. A route can have named councils, committees, directorates, juntas, congresses, restoration offices, cult offices, leagues, syndicates, ministries, synods, communes, or military commands. Those institution names should fit the country story, region, history, route, and ideological language without replacing the public country name.

### Formable nations and formation routes

When an event creates, transforms, releases, or empowers countries, check whether formable nations should be part of the design. A formable is a meaningful country identity that appears after a country satisfies territorial, political, event, focus, or hidden-route requirements. Do not treat formables as only a cosmetic rename.

Formable public names must follow the country naming rules above. The formation decision, congress, authority structure, charter, settlement, or council can have its own institutional name, but the formed map name should stay a direct country or formable name.

A formable design should define:

- formable name and tag handling
- whether it uses a new tag, an existing tag, a cosmetic tag, or a dynamic country name
- required owned and controlled states
- required cores, claims, subjects, puppets, allies, faction members, or occupied areas
- alternate state sets for different borders or reduced maps
- focus route or event route that reveals the formation
- decision that performs the formation
- hidden unlock conditions, if the formable is secret
- ideology, leader, government, legitimacy, recognition, chaos tier, crisis, patron, or achievement gates
- effects on cores, claims, compliance, resistance, subjects, puppets, factions, advisors, laws, technologies, and ideas
- visible country identity after formation, including name, adjective, flag, leader, portrait, parties, ruling ideology, advisors, and focus tree access
- post-formation ambitions, claims, diplomatic reactions, rivals, league or faction behavior, and failure states
- AI willingness to pursue the formable and AI safety checks that prevent impossible or suicidal formation attempts
- super-event, achievement, and asset implications

Do not write vague lines such as `can form a greater country`. Define the concrete formation web. If the player must control this state, this state, and this state, name those states or name the scripted state group and explain what it contains. If the exact state ids are left to implementation, describe the intended geographic set clearly enough that the implementation agent can build a scripted trigger without guessing.

Hidden formables should still be designed fully. The spec can hide player-facing names and spoilers, but the coding-agent prompt must describe the unlock route, required flags, reveal event, decision visibility, AI behavior, rewards, assets, and disqualifiers.

Formation routes should interact with focus trees and decisions. A focus can reveal or prepare the claim, while a decision performs the formation after the map requirement is met. A decision can form the country directly, while later focuses stabilize it, core it, claim further territory, or resolve internal factions. Avoid giving a formable through a focus alone when the player should prove control over named land first.

#### Formable state-puzzle presentation

When exact control of named states is the main proof for a formable, plan the reusable formable state-puzzle display from `chaos-redux-decisions-missions`.

The display should assemble the required territory from the exact in-game shapes of its states in their real geographic positions. Each state remains its own dynamic piece:

- grey when the state does not currently satisfy the formation requirement
- green when the state currently satisfies the formation requirement
- an outline, texture, label, or another non-colour cue that keeps the states readable without relying on colour alone
- a tooltip that names the state and explains its current qualification
- a summary showing qualifying states, required states, and current formation eligibility

The pieces must use exact installed-map state geometry. Do not ask the asset agent to invent borders, trace a modern map, or turn states into generic puzzle tiles. Alternate state sets, subject or ally counting rules, route locks, and ownership or control rules must be defined in the spec so the visible pieces and the formation decision use the same logic.

The interface should update from current campaign state and must not show stale qualification. Keep it compact. Do not surround the territory with unrelated values, fake buttons, or long prose.

The coding prompt should require reusable templates under:

`.claude/skills/chaos-redux-decisions-missions/templates/formable_state_puzzle/`

The template package should cover the state manifest, GUI, GFX, scripted GUI, helper triggers and effects, scripted localisation, static category-picture alternative, AI equivalent, cleanup, and validation. Skill-local templates are reference scaffolding and must be copied into system-owned files before runtime use.

A small formable whose map requirement is obvious may use a static territorial category picture instead only when the category passes the picture eligibility gate and has no interactive state-puzzle GUI. The spec should state why the static picture is clearer than a dynamic state-puzzle display.

## Starting forces and reinforcement pathway standard

When an event creates, releases, transforms, restores, or revives a country that is expected to fight, survive, defend itself, or matter militarily, the spec must define its starting forces. Newly appearing countries should not spawn as empty tags unless they are explicitly non-military administrative placeholders and the spec explains why.

### Distinct army identity and new unit-type gate

When an event introduces a new type of country with its own army, explicitly assess whether that army needs new unit types instead of only renamed vanilla division templates. Plan at least one distinct unit family when the country's biology, doctrine, recruitment source, battlefield role, equipment relationship, movement, supply behavior, or visual silhouette differs materially from an ordinary national army.

A renamed division template made entirely from ordinary vanilla battalions does not count as a new unit type. If vanilla battalions are sufficient, the spec must explain why their mechanics accurately represent the country and must still define distinct templates, recruitment rules, caps, costs, AI use, progression, and visible identity. Do not let implementation silently substitute renamed infantry for a military concept that calls for custom behavior.

For every planned new unit family, define:

- gameplay role, battlefield strengths, weaknesses, and intended counterplay
- custom sub-unit, support unit, unit category, equipment, or modifier needs
- division-template consumers and the countries, routes, evolutions, or decisions that can use them
- manpower, population, equipment, supply, fuel, training, and reinforcement rules
- availability gates, formation caps, upgrade or conversion paths, and cleanup behavior
- AI template priorities, role ratios, production needs, recruitment limits, and operational use
- localisation, bespoke vanilla-green large/map-counter consumers and tokens, icon, technology, doctrine, modifier, and script-enum implications
- 3D entity, model, material, idle, movement, attack, death, and runtime-consumer requirements when the unit should look different on the map

Every new custom unit family must also receive a voice and sound design pass. A custom unit should not inherit ordinary infantry voices, weapon sounds, vehicle sounds, or movement sounds by accident when those sounds conflict with its identity.

Every new custom unit family must also receive original counters for every counter surface it uses. The plan must name the exact installed-vanilla definition and DDS, matching skill-local counter family, runtime consumers and tokens, required states and sizes, final paths, sampled vanilla green palette, and `chaosx_icon_artist` handoff. Missing vanilla-reference inspection blocks counter production; reused counters, arbitrary green, and unreferenced imitations are not final.

For each custom unit family, define:

- spoken language, accent, cultural register, command style, or nonverbal vocal identity
- selection, acknowledgement, movement, attack, retreat, idle, damage, destruction, and death sound roles that the unit actually uses
- weapon, engine, mechanical, creature, magical, environmental, impact, and movement sounds required by its equipment and animation set
- sound variation needs so frequent actions do not repeat one clip constantly
- route, culture, ideology, equipment, or transformation conditions that change the voice or sound set
- synchronization needs for attack, movement, recoil, impact, death, destruction, and other visible actions
- source mode, rights, attribution, file format, sound identifiers, runtime consumers, looping behavior, volume, distance, and mix direction
- which vanilla sounds can be reused, with a concrete reason that they fit the unit
- which sounds require new Internet sourcing and which approved vanilla or sourced files can be reused; recording, generation, synthesis, and manual authoring are forbidden

Sound design is part of the unit identity and runtime package. A visually or mechanically custom unit with no planned voice or sound treatment is incomplete unless the spec explains why silence or an existing sound set is intentional.

All custom-unit audio must come from an identified vanilla or externally sourced file with provenance, licensing, and intended-use evidence. If a suitable source cannot be found, the sound role remains blocked instead of being filled with generated or manually created audio.

Treat the unit package as part of the country package. A new military country archetype with an army represented only by renamed vanilla formations is a planning failure unless the spec gives a concrete mechanical and visual justification for reusing those formations.

Starting units must be dynamic. Do not define one flat number of divisions for every country. The spec should explain what makes the starting force stronger, weaker, larger, smaller, better equipped, more irregular, more professional, more defensive, more foreign-backed, or stranger.

Useful scaling factors include:

- chaos tier and chaos value
- event threat, crisis pressure, evolution state, and ordinary stage state
- local population, industry, terrain, ports, rail hubs, depots, and capital control
- local legitimacy, public support, militia networks, and command obedience
- defecting army districts, security units, sailors, railway guards, border guards, police forces, or factory guards
- captured equipment, depot vulnerability, foreign aid, volunteer corridors, and faction support
- parent-country weakness, missed deadlines, lost objectives, supply failure, war state, and previous choices
- whether the tag is an ordinary republic, emergency committee, factory state, ancient restoration, partisan movement, cult, railway state, naval state, or other special actor

For every meaningful new or transformed country, map:

- starting division families or template concepts
- expected starting strength in weak, normal, severe, and high-chaos openings
- equipment and manpower source
- whether units are militia, regular defectors, border guards, mountain detachments, factory guards, railway troops, sailors, cavalry, foreign volunteers, ancient levies, or special high-chaos formations
- starting commanders, officer shortages, or leader ties when relevant
- defensive bonuses, training penalties, supply weaknesses, morale problems, or legitimacy risks
- how the package affects threat meters, foreign attention, depot pressure, old-movement resurgence, or parent-country authority
- what report, event text, or localisation direction should explain why those troops exist

The spec must also map how newly appearing countries can get more units after spawning. This should include decisions, timed objectives, focus rewards, volunteer systems, depot captures, foreign missions, local mobilization, League or faction training, factory guard mobilization, border guard formation, or special high-chaos recruitment where appropriate.

Do not make reinforcement depend only on political power or command power. Use concrete goals and resources such as holding a capital, guarding a border, controlling a depot, controlling rail lines, spending army XP, consuming equipment, committing manpower, using fuel or trains, securing local support, opening a foreign corridor, finishing a construction quota, proving legitimacy by a deadline, placing divisions in required states, or keeping a volunteer route open.

Unit-creating focuses and decisions must be specific. Avoid repeated generic rewards such as `add two infantry divisions` across many countries. A unit reward should explain the institution and story behind the unit, such as capital defense committees, local garrison defections, railway guards, factory guard shifts, mountain pass detachments, Black Banner columns, sailor battalions, Basmachi cavalry, ancient host militias, medical volunteers, foreign-trained cadres, or high-chaos special units.

Each unit-creating focus or decision should define:

- what unit or template family appears
- what unlocks it
- what non-political-power requirements it uses when appropriate
- whether it is repeatable, timed, risky, route-locked, or one-time
- what pressure or threat values it changes
- what downside it creates if repeated or failed
- what AI should do with it
- what blocked localisation direction should communicate when requirements are missing
- what icon, spirit, report event, or commander asset it needs when relevant

For focus trees, military growth should be integrated into branches. Some focuses can spawn units directly, but others should unlock decisions, improve templates, recruit commanders, create volunteer corridors, integrate militias, convert irregulars into regulars, expand special units, or change mobilisation rules. A deep tree should offer different ways to build an army depending on politics, foreign influence, economy, terrain, ideology, and chaos state.

### 3D model and skeletal animation planning standard

When a feature adds a visible unit, building, creature, vehicle, aircraft, naval object, map entity, or other 3D surface, plan the model package as a first-class feature surface rather than treating it as an optional render.

Classify the asset before writing the 3D asset section: static prop, building, humanoid unit, non-humanoid creature, vehicle, aircraft, naval object, or articulated attachment.

For a unit, define the gameplay consumer, unit category or sub-unit, entity key, `.asset` key, `.mesh` key, material and texture paths, large/map-counter consumers and tokens, idle action, movement action, attack action, death or destruction action when relevant, and the exact country, province, state, or map test that will show it.

For a building or map entity, define the building key, entity key, mesh key, state and province placement, valid state-to-province relationship, level or construction behavior, zoom visibility, rotation, runtime scale, and a test location that is inside the intended state and does not hide the model behind an existing building.

If the user does not provide a ready reference image, plan exactly one clean Meshy-ready reference image for the asset and route it through the approved image-generation workflow before the provider gate.

Meshy 7 is the generation model. The plan must forbid silent downgrade and require the exact live model identifier in provider evidence.

Select the requested model operations and required components under [Route selection and component completion](../../chaos-redux-3d-model-pipeline/SKILL.md#route-selection-and-component-completion). The specification must retain separate generated body/item inputs, one supported rig/action attempt, authorized Blender completion/fallback, calibrated component budgets, source and credit limits, contact/deformation/semantic review, and export/reimport. Existing geometry alone never mandates a rebuild.

Never plan a side-profile sheet, turnaround board, collage, or multi-view board as a Meshy input. Blender QA views and contact sheets are review evidence only and must never be sent to Meshy.

The planning spec must name the installed vanilla mesh and entity that establish axes, orientation, source geometry height, entity scale, origin, ground or water contact, and effective runtime height.

For humanoid units, the custom source geometry must match the named vanilla source mesh height and the entity scale must be applied exactly once. Record source height, entity scale, effective runtime height, coordinate axes, facing direction, origin, and the measurement evidence in the plan.

For every requested skeletal action, define the semantic role, action name, FPS, frame range, loop policy, root-motion or in-place policy, ground-contact requirement, retarget or authoring route, static fallback policy, runtime binding, and acceptance evidence.

Do not let a static render or still mesh stand in for a requested skeletal animation. If an action cannot be produced, the coding-agent prompt must mark it blocked or needs_user_review with the reason.

Plan every output in [Evidence package and handoff](../../chaos-redux-3d-model-pipeline/SKILL.md#evidence-package-and-handoff), including source/runtime separation and final hash-aware synchronization so an older copy cannot replace the approved runtime candidate. User-supplied live observations remain optional for agent delivery.

Route production to `chaosx_3d_model_pipeline` with every input and boundary required by [Bounded subagent route](../../chaos-redux-3d-model-pipeline/SKILL.md#bounded-subagent-route); the specification and coding prompt must carry that complete contract.

The coding-agent prompt must state that the main implementation agent owns `.asset`, entity, `.gfx`, unit/building/gameplay wiring, valid province and state placement, code review, useful local checks, and any game results supplied by the user. The user performs live runtime validation; agents neither request nor await it as a delivery gate.

#### 3D model planning matrix

| Surface | Minimum planned evidence |
| --- | --- |
| Humanoid unit | Vanilla source-height measurement, entity-scale crosswalk, repaired geometry, PDX material audit, idle/move/attack actions, `.mesh`/`.anim` reimport proof, unit consumer/source binding, plus any available user-supplied movement observations and screenshot |
| Building or static map entity | Vanilla building precedent, valid state/province pair, entity and `.asset` existence, mesh/material proof, scale and placement/source checks, construction or level contract, plus any user-supplied zoom/construction observations and screenshot |
| Creature, vehicle, aircraft, or naval object | Profile-specific axis and contact calibration, topology/material proof, required action list, export/reimport proof, entity/runtime wiring, plus any user-supplied domain-appropriate live observations |
