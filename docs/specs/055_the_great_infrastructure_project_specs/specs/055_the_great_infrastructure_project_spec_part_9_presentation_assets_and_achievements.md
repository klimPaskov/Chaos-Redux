# Event 55 Specification, Part 9

## Presentation, Writing Direction, Assets, and Achievements

## Presentation choice

Event 55 should use an ordinary decision category with:

- one category icon
- one static category picture
- one compact status header
- ordinary targeted decisions
- normal timed missions
- map highlighting for proposal routes

A dedicated scripted GUI is not justified. The player manages one public capacity value, a small proposal set, and a few active missions. The ordinary decision system can present this clearly.

The static category picture should establish scale and identity. It must not paint fake buttons, meters, route controls, or numbers into the artwork.

## Category hierarchy

The top of the category should show:

1. Event 55 program identity.
2. National Works Capacity stage and compact visual state.
3. Active project count against the current limit.
4. One short current-status sentence.
5. The static category picture.

The action area then shows only decisions relevant to the current phase.

## Visible action budget

The category should normally show three to five primary actions and never more than six in one state.

### No active project

Suggested visible set:

- three project proposals
- survey refresh when available
- one repair or maintenance action only when urgent

### One active project

Suggested visible set:

- active construction mission
- one or two stored proposals when another slot can be used
- one project intervention when a real problem exists
- survey refresh only when it can change the set

### At project limit

Suggested visible set:

- active missions
- one urgent repair, renegotiation, or scope decision
- no new authorization decisions

### Evolution III with several active projects

New proposals hide while every slot is occupied. The category shows only active missions and the most important network action.

The category should never become a list of every completed project. Completed projects belong in a concise status summary, project detail tooltip, or a selected target flow when the list becomes large.

## Active mission budget

The normal category should show one to three active missions.

A country with three active Evolution III projects can show one mission for each. Avoid separate survey, procurement, and construction missions at the same time for one project.

## Map presentation

Inspecting a proposal should identify its geography.

Preferred feedback:

- map centers on the route
- origin and destination states are highlighted
- critical route states use a distinct highlight where supported
- foreign partner states are visually distinguishable
- the tooltip names the route and purpose

A completed project can use a decision or project detail entry that highlights its current route and critical nodes.

## Event popup writing direction

The opening event should describe a national public works mobilization that has transformed roads and ordinary state infrastructure with implausible speed.

The player should see:

- survey crews, road gangs, machinery, local offices, and freight movement
- the scale of simultaneous work across the country
- the creation of a permanent authority for larger projects
- uncertainty about how such coordination and material supply became possible

The event should not explain the incident through developer language, magic variables, or update history.

The tone can use restrained administrative absurdity because this is a positive Chaos event. It should remain grounded in physical work, transport, and public reaction.

The event should avoid:

- generic cabinet reports
- staff-table framing
- claims that the map itself changed
- dramatic warnings about future danger
- final option text that sounds like a raw effect list

## Opening option direction

The main option should accept the new national works authority and direct it toward permanent megaprojects.

The reaction can draw from:

- public works slogans
- national modernization language
- engineering pride
- mild irony about every ministry suddenly owning blueprints

Final wording requires implementation writing. The spec does not supply a pasteable button line.

## Project proposal writing direction

Every proposal should name:

- real origin and destination states
- route or facility family
- the public purpose
- expected duration band
- first-stage costs
- later cost types that can arise
- main strategic benefit
- main visible risk

The title can use a dynamic route name based on geography. A working internal project label must not become final localisation without review.

## Construction incident writing direction

Incident text should focus on concrete work:

- rock, water, steel, dust, weather, machinery, labor, bridges, ports, freight, and settlements
- the specific route state or partner
- the immediate choice and consequence

Avoid generic mystery language when the cause is ordinary engineering. Use uncertainty only for a real unknown condition.

Labor, displacement, land acquisition, safety, and corruption can appear as serious issues. The event should not use cheap comedy for injury, forced movement, or severe local conflict.

## International writing direction

Partner invitations and counteroffers should sound like negotiations over visible routes, costs, access, standards, and benefits.

They should vary by:

- relations
- faction membership
- war state
- route role
- contribution burden
- embargo status
- relief priority

Do not expose AI scores or describe a country as accepting because a hidden weight is high.

## Evolution writing direction

### Evolution I

Show ministries, contractors, rail authorities, and military planners competing to begin more projects. Emphasize scale, speed, and a growing belief that any route can be built.

### Evolution II

Show engineering limits being treated as temporary obstacles. Use tunnels, viaducts, bridges, mountain cuts, desert work, and underwater construction as concrete imagery.

### Evolution III

Show several countries coordinating routes, standards, ports, and crossings into one network. Emphasize trains and freight crossing borders through a shared operating system.

Evolution text should not label itself as a warning or world-ending development.

## Event Details direction

Event Details should explain:

- the opening infrastructure transformation
- the permanent national project program
- geographic proposal generation
- long construction and maintenance commitments
- multinational cooperation and disruption

It should not list exact modifiers, hidden thresholds, raw costs, or future rare variants.

Evolution previews should explain the new class of projects each evolution allows.

## Spreadsheet wording direction

The catalog row should use concise player-facing summaries that match Event Details.

The Event 55 detail should describe one country receiving maximum infrastructure and access to a persistent megaproject program.

Evolution fields should describe:

- denser national works and difficult routes at `200+`
- extreme engineering and fixed links at `400+`
- continental multinational networks at `600+`

Cluster detail should describe Event 55 as the medium infrastructure member and explain its same-actor connection to Resources Found without exposing cluster implementation.

## Asset inventory

All working asset labels below are file and routing labels, not final player-facing localisation.

### Opening report event image

- Asset role: report event image
- Suggested final canvas: follow the verified report event reference, normally `210x176`
- Source mode: generated period-authentic documentary scene
- Subject: large public works mobilization with workers, surveyors, machinery, rail viaduct or major road cut
- Mood: ambitious, organized, physical, slightly uncanny in scale
- Avoid: maps as the main subject, modern safety clothing, modern machinery, readable generated text, generic conference rooms

### Global network news image

- Asset role: news image for the first three-country operational Evolution III network
- Suggested final canvas: follow the verified news event reference, normally `397x153`
- Source mode: generated period press photograph
- Subject: freight train or opening convoy crossing a new international bridge, border, or port interchange with several national delegations present in the background
- Avoid: modern flags when route participants are dynamic, readable generated signs, a staged modern ribbon cutting

### Decision category icon

- Asset role: small category icon
- Source mode: native transparent ImageGen
- Subject: rail, bridge, and road convergence in one strong silhouette
- Must remain readable at the exact category icon size

### Static decision category picture

- Asset role: large decision category picture
- Reference family: `icons/decision_categories/pictures`
- Expected reference canvas: `114x101`, subject to the actual consumer
- Source mode: generated full-canvas painted or documentary montage
- Subject: viaduct, highway cut, crane, port, and freight movement unified into one scene
- Avoid: fake buttons, labels, meters, borders, route diagrams, or UI controls

### National works institution idea icon

- Asset role: idea or national spirit icon
- Suggested final canvas: `64x64`
- Source mode: native transparent ImageGen
- Subject: blueprint roll, survey instrument, rail wheel, and civic engineering emblem
- Staged versions should evolve the same institution without resizing one unrelated asset

### Project family decision icons

Each family requires its own decision-specific source art, designed for the decision icon consumer and normally `32x32` after verification:

- continental railway
- continental highway
- international trade corridor
- underwater tunnel
- great bridge
- grand port
- resource corridor
- continental network

The icons can share a coordinated visual family. They must not be resized copies of the category or focus-style art.

### Mission icons

Distinct mission-specific icons are needed for:

- survey and charter
- partner negotiation
- procurement
- main construction
- repair
- rerouting
- commissioning

A smaller set can be reused across project families when the mission role is genuinely the same. Mission icons must not be simple resized decision icons.

### Status and modifier icons

Asset coverage is needed for:

- overextended works condition
- completed national works institution stage
- route disruption or maintenance state when the owning UI uses an icon
- major port or fixed-link state modifier when a visible state modifier needs art

Do not create custom icons for hidden internal markers.

### Achievement icons

Each achievement needs a completed `64x64` icon direction and the normal achievement state triplet required by the repository.

## Achievement set

All achievement names below are working labels, not final localisation.

### Achievement 1: From Sea to Sea

#### Purpose

Reward completion of a real coast-to-coast national trunk.

#### Eligible country

The player-controlled country that owns and completes the project.

#### Conditions

- receive Event 55
- complete one coast-to-coast railway or highway project
- route crosses a large minimum number of connected states
- origin and destination are on distinct distant coasts
- project reaches full completion
- route remains Operational for `365` consecutive days

#### Disqualifiers

- reduced completion
- project abandonment
- route severed during the sustain period
- a transferred project completed by another country

#### Difficulty

Hard. It requires suitable geography, long construction, and sustained route control.

#### Icon direction

A locomotive or road convoy joining two stylized coastlines, with a clear continental span and no text.

### Achievement 2: No Mountain Is High Enough

#### Purpose

Reward successful extreme engineering without outside rescue.

#### Eligible country

The host of an Evolution II mountain railway, highway, bridge, or tunnel project.

#### Conditions

- Evolution II active
- authorize an extreme mountain route
- choose the conservative or standard method
- receive no foreign financier contribution
- complete at full scope
- resolve every major engineering defect without reducing scope
- project opens Operational

#### Disqualifiers

- foreign bailout
- reduced route
- abandonment
- direct repeat-firing completion assistance after main construction begins

#### Difficulty

Very hard. It requires a large project, difficult terrain, and enough domestic capacity to survive overruns.

#### Icon direction

A rail viaduct or bridge passing through a high mountain cut, with strong height and engineering silhouette.

### Achievement 3: Steel Thread of Nations

#### Purpose

Reward durable multinational cooperation.

#### Eligible country

The host of an international trade corridor or continental network.

#### Conditions

- at least four sovereign participants
- full core route completed
- every participant retains membership
- no war among participants
- route remains Operational for `730` consecutive days
- no segment is permanently removed

#### Disqualifiers

- participant withdrawal
- corridor reduced below four participants
- host annexed before the sustain period ends
- route becomes Dormant or Severed

#### Difficulty

Very hard. It combines diplomacy, long construction, route security, and two years of stable operation.

#### Icon direction

Four rail lines or bridge spans converging into one steel junction, with distinct national terminals but no flags or text.

### Achievement 4: Master Builder

#### Purpose

Reward mastery of the complete project system.

#### Eligible country

The player-controlled country with an active Event 55 program.

#### Conditions

- complete five projects with five distinct primary families
- at least one project is international
- at least one project is unlocked by Evolution II or III
- no project has been abandoned
- every counted project remains at least Strained or better when the achievement fires
- at least one damaged project has been repaired successfully

#### Disqualifiers

- any counted project was transferred from another host
- one multimodal project counted as several families
- achievement conditions met only through repeated project duplication

#### Difficulty

Extreme. It requires a long campaign and careful use of several different systems.

#### Icon direction

A period engineer's compass over a unified rail, bridge, port, and tunnel emblem. Keep one readable central silhouette.

### Achievement 5: The Relief Artery

#### Purpose

Reward using infrastructure to solve a real humanitarian transport problem.

#### Eligible country

The host of a project with relief priority.

#### Conditions

- a genuine Famine or Migration adapter request is active
- complete a relief-priority railway, highway, port, or international corridor
- the route becomes Operational before the owning crisis reaches its worst stage
- the owning system records improved relief or movement access through the route
- sustain operation for `180` days

#### Disqualifiers

- route existed before the crisis and no new project was completed
- project was only commercial with no relief-priority commitment
- the owning humanitarian system rejects the route as unsafe
- route is abandoned or severed during the sustain period

#### Difficulty

Hard. It requires the right crisis, a feasible route, and fast construction without bypassing the owning system.

#### Icon direction

A freight train or truck convoy crossing a bridge toward a relief depot, with supply crates and no suffering as decorative imagery.

## Achievement tracking rules

- Track project identity and primary family.
- Track full versus reduced completion.
- Track host identity and transfers.
- Track continuous operational periods with interruption reset.
- Track participant count and withdrawal.
- Track foreign finance and repeat assistance where relevant.
- Track abandonment history per player country.
- Count a project once.
- Do not unlock an achievement merely because Event 55 fired.
- Do not expose hidden achievement conditions in ordinary event text.

## Asset production rules

Asset implementation must:

- inspect the exact vanilla reference family before generation
- request native transparency for alpha-backed icons
- keep source PNGs, processed previews, DDS files, prompts, and manifests
- use separate source art for category, decision, mission, idea, state modifier, and achievement roles
- preserve final event-owned folder naming
- avoid primitive local drawings and resized unrelated icons
- create the achievement triplets required by the repository
- keep the temporary event asset workspace until implementation and review are complete
- promote durable provenance and handoff facts before deleting the temporary workspace

## Presentation acceptance criteria

Presentation is acceptable only when:

- the ordinary category explains current state quickly
- National Works Capacity has a compact visual identity and clear threshold tooltip
- visible actions stay within the category budget
- active missions stay within the mission budget
- project proposals name real geography
- map highlights show the route
- no raw variables or developer wording appear
- category art contains no fake interface controls
- every visible asset has a distinct asset-family plan
- every achievement has hard conditions, disqualifiers, tracking, and icon direction
- final localisation is written from direction in implementation and is not copied from working labels without review
