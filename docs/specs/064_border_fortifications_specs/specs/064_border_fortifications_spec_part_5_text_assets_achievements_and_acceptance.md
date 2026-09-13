# Event 064 Border Fortifications

## Part 5: Text direction, assets, achievements, and acceptance

## Player-facing tone

Event 064 should feel strange, material, and militarily serious. The fortifications are useful, but their worldwide and simultaneous appearance should remain unsettling.

The writing should show physical evidence:

- completed concrete positions where no construction existed
- fresh earth, obstacles, firing ports, access paths, and sealed rooms
- engineers discovering coherent layouts without plans or work records
- armies taking possession before governments understand the cause
- allied and neutral borders receiving the same treatment as hostile fronts
- deeper positions and state systems appearing at higher evolution stages

Avoid these frames:

- a normal government announcing a successful planned building program
- a generic map changing on a staff table
- a failed radio message or stock communications breakdown
- empty end-of-world language
- technical implementation vocabulary
- jokes about mass death or civilians trapped by war
- raw values presented as if they were public military reports

Dry military or bureaucratic irony can appear in report options and decision text. It should come from governments trying to classify an impossible gift, not from meme language.

## Localisation handoff

The implementation agent writes final text. This specification gives direction and required dynamic content.

### Accepted names

The following names come directly from the user brief and can remain as final English labels unless later localisation review finds a clear fit problem:

- Border Fortifications
- Defense in Depth
- Fortress States
- Fortress World

All other names in this package are working labels, not final localisation.

### Event title direction

Keep the title concise and centered on the physical frontier phenomenon. Avoid a title that claims a government ordered or completed the work.

### Local report description direction

Write from the receiving country's viewpoint after the global wave has already occurred.

The description should reveal:

- the structures appeared across current foreign land borders
- the same reports are arriving from other countries
- the country's own local result
- the highest visible evolved package that changed local territory
- the need to choose a practical response

The text should preserve uncertainty about origin. It should not claim supernatural, alien, divine, or scientific causation without a later accepted design change.

### Report option direction

Each option represents one posture.

- Integrate the Line direction: controlled professional acceptance, defensive practicality, or dry acknowledgment that the structures now exist and must be used.
- Keep the Roads Open direction: engineers and logisticians taking control of an inherited network problem.
- Study the Breach direction: restrained offensive resolve focused on crossing foreign lines.
- Observation-only direction: a land-borderless government recognizes that every continental plan has changed.

Options should be short enough for the event window. Do not write hidden mechanical details into the button label.

### Evolution text direction

- Defense in Depth: layered belts and strongpoints appearing behind the frontier, with uncertain origin and visible strategic intent.
- Fortress States: border regions becoming integrated military systems with air warning, supply work, and selective coastal defenses.
- Fortress World: capitals and internal hubs receiving permanent fallback positions far from ordinary borders.

Evolution history text should describe what changed on the materialization date. Evolution catalog text should describe the premise without fake history.

### Decision category direction

The category title and description should communicate a temporary national response to the most recent wave. Mention current posture, remaining time, and active project through dynamic text.

Do not create a fake control-room interface in the category picture or prose.

### Decision and mission direction

Every decision needs:

- clear target type
- visible cost bundle
- duration
- public result
- reason it is unavailable
- failure conditions when a mission is active

The writing should name the target state or target country. It should avoid raw hidden strategic scores and internal variable names.

### Modifier direction

Each posture modifier should explain the public military policy and its visible effect. It should not imply that the modifier created the original forts.

### Event Details direction

Event Details should explain:

- the global frontier rule
- that relations do not prevent a boundary from receiving defenses
- that completed works persist after borders change
- that later evolutions deepen selected areas

Do not reveal exact caps, quotas, Chaos values, AI weights, achievement logic, or hidden target scores.

### History direction

The global History row should describe one synchronized wave and provide world result counts. It should avoid a misleading actor country.

The local detail can provide the receiving country's result when the interface supports scoped detail safely.

### Cluster text direction

Sudden Abundance text should frame Event 064 as a worldwide arrival of constructed defensive capacity.

Military Preparation text should frame Event 064 as a shift in defensive readiness and breach planning.

Cluster details can reveal member severity and readiness. They should not reveal the exact result of a future member before it fires.

### Achievement text direction

Achievement names in this package are working labels. Final titles and descriptions should be concise, readable, and focused on the challenge. Do not hide essential disqualifiers from the achievement tooltip.

### Spreadsheet-facing text direction

The authoritative Event 064 row should describe the global border-fort wave and summarize each evolution in one clear sentence. It must replace the unrelated leader-trait detail currently present in the export.

The primary cluster field should identify Sudden Abundance. The additional Military Preparation membership must be recorded through the workbook's accepted multi-cluster structure or the cluster membership table. Do not invent an unverified comma format in a single-value field.

## Dynamic localisation inputs

Use dynamic placeholders where the current interface supports them safely.

Recommended report inputs:

- receiving country
- wave sequence or repeat status
- direct frontier provinces improved
- frontier provinces already at cap
- frontier anchors improved
- depth positions created
- Fortress States changed
- internal redoubts created
- highest concrete evolution package
- response-window duration

Recommended decision inputs:

- target state
- target country for breach work
- project duration
- civilian factory commitment
- equipment, transport, fuel, experience, manpower, or command cost
- expected physical result
- current cap reason
- current invalidation reason

Recommended history inputs:

- global countries changed
- global direct frontier provinces changed
- global evolved positions changed
- world regions represented
- cluster context when publicly appropriate

Fallback localisation must remain grammatical when a count is zero, one, or many.

## Asset strategy

The event uses a focused static asset package. Existing HOI4 building models remain the map presentation, while Event 064 adds report, category, posture, decision, and achievement art.

The asset agent must inspect the exact current consumer, vanilla references, current Event 064 art, and existing Chaos Redux style before producing replacements.

### Source mode

Use generated non-portrait art for the report image, decision category picture, decision icons, posture icons, and achievement art. Historical photographs can be used as private style references only when their rights and repository reference rules permit it.

Do not present an unverified archival photograph as a final sourced asset. The event depicts a fictional synchronized worldwide phenomenon, so generated original art is the safer default.

## Report event image

### Existing identity

Preserve the current sprite identity when compatible:

- sprite: `GFX_report_event_border_fortifications`
- current family path: `gfx/event_pictures/064_border_forts/`

The implementation and asset agents must inspect the current DDS and source evidence. Replace it when it fails the current report-event format, composition, quality, provenance, or visual consistency rules.

### Required final format

- final DDS for the event window
- PNG preview
- `210x176` report-event composition
- black and white with restrained sepia treatment
- transparent report-card corners through the standard report-event processor
- no readable text in the generated art
- no flags or faction symbols that imply one country caused the event
- no modern equipment

### Composition direction

Show a 1930s or 1940s military frontier where reinforced-concrete positions, wire, anti-tank obstacles, access trenches, and inspection parties extend across a landscape. The scene should suggest that the structures are already complete. Workers or soldiers can be present, but they should inspect or occupy the completed line. Normal building activity should not appear.

Use a clear foreground bunker or firing position, a middle-distance line, and a distant route or settlement that shows strategic depth. Keep the image readable at event-window scale.

## Decision category picture

Use the canonical decision-category picture reference family and inspect the active consumer before locking dimensions. The current planning reference canvas is `114x101`, but the asset agent must verify the exact repository surface.

Composition direction:

- fortified frontier in the foreground
- railway or road feeding the line
- observation or signal position
- distant city, port, or terrain objective
- no painted buttons, meters, text, or fake controls
- enough empty structure for category overlay readability

Use a static picture. Animation adds no useful information for this event.

## Decision category icon

Create one `32x32` transparent icon for the Event 064 response category.

Direction:

- simple concrete bunker silhouette
- one border line or barrier motif
- strong outer shape
- minimal small detail
- readable against the standard decision background

## Posture icons

Create three coordinated `64x64` transparent idea or timed-modifier icons. Each needs a distinct silhouette while sharing the same visual family.

| Working posture | Icon direction |
| --- | --- |
| Integrate the Line | bunker cross-section with linked firing positions or command arrows contained inside the defensive line |
| Keep the Roads Open | rail or road entering a fortified sector, with a supply crate or transport marker |
| Study the Breach | cracked bunker plan, engineer tool, and concentrated assault arrow without gore |

Do not resize the category icon into posture icons. Generate or draw each posture concept for its own consumer.

## Decision icons

Create five `32x32` transparent decision icons.

| Working decision family | Icon direction |
| --- | --- |
| Reinforce a Priority Sector | bunker and reinforcing concrete layer or sandbag band |
| Connect the New Line | rail or road link joining a fortified point |
| Conduct Breach Exercises | cracked fort target with engineer wedge or obstacle-clearing tool |
| Harden the Air and Coastal Flank | compact combined warning motif with anti-air gun, radar arc, and coastal emplacement, simplified for readability |
| Prepare a National Redoubt | capital or star-shaped central citadel within an inner defensive ring |

The air and coastal icon must remain readable at 32 pixels. If the combined concept cannot pass a native-size review, use a shared fortified-flank symbol and let target-specific localisation distinguish the branch.

## Achievement icons

Create one original completed `64x64` icon for each achievement, then use the standard achievement processor to create completed, grey, and not-eligible variants.

The four completed icons need different compositions. Do not recolor one base image and call them separate achievements.

Detailed direction appears in the achievement sections below.

## Asset naming direction

Use lowercase snake_case for files and stable `GFX_` sprite names. The asset prompt contains the proposed family names and final handoff requirements.

Every final asset package needs:

- source files
- processed PNG previews
- final DDS files
- provenance notes
- exact dimensions
- alpha validation where relevant
- sprite-name proposal
- target `.gfx` file
- final path
- SHA-256 hash
- manifest status
- `gfx_handoff.md`

No runtime file may point into temporary `docs/assets/` workspaces after completion.

## Achievement framework

All achievement labels below are working labels, not final localisation. They must be implemented through the Chaos Redux achievement system and must suppress debug, console, and manual-event shortcuts.

Each achievement needs stable challenge flags or variables, explicit start and failure conditions, cleanup, save-load persistence, final icons, localisation, documentation, and targeted tests.

## Achievement A: Continent of Concrete

### Working key

`chaosx_achievement_064_continent_of_concrete`

### Visibility and difficulty

- visible
- very hard

### Challenge purpose

Reward a large land country that turns a complex multi-neighbor frontier into a mature fort network and then proves it under simultaneous pressure.

### Eligibility start

The challenge can arm after a natural Event 064 wave when the player country:

- is independent or has an autonomy level that permits normal independent war leadership
- has at least five distinct current land neighbors
- has at least eight controlled core border states
- has at least twelve qualifying direct frontier provinces
- is not using debug or manual Event 064 context
- has not already completed the achievement

Store the eligible core border-state challenge set at challenge start. Later peaceful border changes do not add easy new states to the set. A state lost before the war phase fails or pauses the challenge according to the accepted implementation model.

### Construction requirement

Before the defense phase begins:

- at least eighty percent of the stored qualifying frontier provinces must have total land-fort level five or higher
- at least four stored border states must contain state anti-air or radar
- the player must have selected Integrate the Line during the current or immediately prior valid response window

The implementation must prove a bounded way to evaluate the stored frontier set. It must not add a recurring world scan.

### Defense requirement

The player must:

- be at war with at least two stored land-neighbor countries at the same time
- hold every stored core border state for `180` consecutive days during that multi-front war
- remain independent
- avoid joining a new faction after the challenge war phase begins
- avoid transferring stored states to subjects or allies

A white peace or victory after the full hold period can complete the achievement. The challenge need not require annexing the attackers.

### Disqualifiers

- manual or debug Event 064 firing used for the challenge wave
- console or debug context
- state-transfer shortcut
- becoming a subject
- joining a faction after the war phase begins
- losing control of a stored core border state during the hold period
- challenge set reduced through release or ownership transfer

### Why it is not trivial

The player needs a large exposed frontier, several evolved state defenses, a deliberate defensive posture, and a sustained multi-neighbor war without surrendering any marked border state.

### Icon direction

A national land silhouette or broad frontier arc surrounded by a ring of linked concrete bunkers. Show several outward threat arrows stopped at the line. Keep the shape clear at 64 pixels.

## Achievement B: The Line Held

### Working key

`chaosx_achievement_064_the_line_held`

### Visibility and difficulty

- visible
- hard

### Challenge purpose

Reward a smaller country that survives a stronger neighbor through the new line without escaping through alliance or subordination.

### Eligibility start

Arm the challenge when:

- the player is a non-major
- a natural Event 064 wave has affected at least one controlled core border state
- the player enters a defensive war against a land neighbor
- the attacker's industry or fielded military strength is at least twice the player's accepted comparison value
- the player is independent and factionless at the challenge start
- the capital and one or more threatened core border states are marked

Use the complete current AI and military context to choose a stable strength comparison. Document the selected metric.

### Completion requirement

The player must achieve one of these after holding the challenge state:

- win the defensive war
- force a peace that preserves the capital and every marked core border state
- survive `365` days and reduce the attacker to a non-threatening peace state through accepted war resolution

Throughout the challenge the player must:

- keep control of the capital
- keep control of every marked core border state
- remain independent
- remain outside factions
- avoid transferring the marked states

### Disqualifiers

- manual or debug Event 064 wave
- becoming a subject
- joining a faction
- losing the capital
- losing a marked core border state
- winning through an ownership-transfer or tag-switch shortcut
- attacker ceasing to be the relevant opponent through a third-party scripted deletion before the hold condition is satisfied

### Why it is not trivial

The player begins weaker, cannot call a faction to solve the war, and must preserve every marked defensive state.

### Icon direction

An intact bunker or short fort line under several broken assault arrows, with a small national center or capital light behind it.

## Achievement C: Breach the Unbreachable

### Working key

`chaosx_achievement_064_breach_the_unbreachable`

### Visibility and difficulty

- visible
- very hard

### Challenge purpose

Reward offensive mastery of the event's counterplay. The player must prepare for a real high-fort target, cross the line, and reach the enemy capital quickly.

### Eligibility start

Arm the challenge when:

- the player selects Study the Breach
- a valid target country is stored through Conduct Breach Exercises
- the target owns or controls a connected fortified frontier containing at least three relevant border states or an equivalent bounded province threshold
- the target's qualifying direct frontier positions average or meet total fort level five or higher under the accepted test
- the target capital is reachable through a continuous land route from the stored frontier after entering target territory
- the context is natural and non-debug

### Completion requirement

Within `180` days of the challenge offensive beginning, the player must:

- take control of the stored fortified frontier objective
- establish a continuous controlled land path from the breached frontier toward the target capital
- capture the stored target capital
- remain the main country responsible for the capture

The implementation should track a sequence of controlled objective states because the engine may not expose division orders safely.

### Disqualifiers

- target capital acquired through peace conference, subject transfer, scripted ownership transfer, or civil-war tag replacement
- target capital captured first by another country
- target ceases to exist before the player's land objective sequence completes
- nuclear strike used on the stored target during the challenge when a reliable event flag can detect it
- manual or debug Event 064 firing
- console or debug context

Do not promise detection of paratrooper or naval-invasion orders unless the engine exposes reliable hooks. The continuous land-objective sequence is the required proof that the player crossed and exploited the fortified front.

### Why it is not trivial

The target line must already be strong, the player must spend on breach preparation, and the capital must fall through a stored land campaign within a short window.

### Icon direction

A cracked concrete bunker split by an engineer wedge or concentrated assault arrow, with a clear route continuing toward a small capital symbol.

## Achievement D: Last Redoubt

### Working key

`chaosx_achievement_064_last_redoubt`

### Visibility and difficulty

- hidden or rare
- extreme

### Challenge purpose

Reward a player who survives near national collapse through a Fortress World redoubt and then recovers.

### Eligibility start

Arm the challenge when:

- global Chaos is at least `600`
- Fortress World has concretely materialized for the player country
- the player owns at least ten core states or another accepted minimum that prevents a one-state exploit
- the player controls a valid capital redoubt and a linked supply-hub or major supply-route redoubt
- the player is at war
- controlled core victory-point share falls below forty percent while the capital and linked supply position remain held
- the context is natural and non-debug

### Hold requirement

The player must hold the stored capital redoubt and linked supply position for `180` consecutive days without capitulating.

### Recovery requirement

After the hold period, the player must recover to at least eighty percent of owned core victory-point value and end the immediate capital threat.

### Disqualifiers

- capitulation
- moving the capital through a manual or scripted shortcut after the challenge begins
- transferring the capital or supply state
- becoming a subject
- tag switching away from the challenged country
- manual or debug Event 064 wave
- console or debug context

### Why it is not trivial

The country must first suffer a severe territorial collapse, preserve two linked strategic positions for a long period, and then reconquer most of its core victory points.

### Icon direction

A central capital citadel linked to a supply node inside a broken encirclement ring. A small outward recovery arrow can show the later counterattack.

## Achievement tracking principles

- Use country-scoped challenge state and bounded state or target ledgers.
- Arm challenges only after all entry conditions are confirmed.
- Store the relevant target country, capital, states, date, and context.
- Revalidate ownership and control at meaningful event, war, decision, state-transfer, or periodic player-only checkpoints.
- Avoid recurring whole-world scans.
- Clear failed challenges and stale targets.
- Preserve valid challenge progress through save and reload.
- Suppress completion under debug, manual-event, console, observer, or test contexts.
- Do not grant an achievement merely because Event 064 fired.
- Document every metric whose engine meaning could be ambiguous, including military strength and victory-point share.

## Documentation requirements

Create or update a permanent Event 064 overview under the repository's current event-documentation convention.

The documentation should cover:

- event identity and type
- baseline global transaction
- valid frontier definition
- repeat behavior
- evolution packages
- response postures and projects
- AI behavior
- Chaos impact map
- both cluster memberships
- achievements
- asset paths and sprite identities
- event log and Event Details integration
- catalog update
- validation status
- known blockers

Do not write only that the event was reworked. The document should let a maintainer understand the implemented behavior without reading every script file.

## Catalog update direction

Update the authoritative XLSX, then run:

```text
python .tools/export_event_catalog_csv.py
```

Do not edit the exported CSV files directly.

Required Event 064 fields:

| Field | Direction |
| --- | --- |
| ID | `064` |
| Event Name | Border Fortifications |
| Details | Global synchronized fortification of every valid current foreign land frontier, followed by country responses |
| Evo I | Defense in Depth adds selected strategic anchors and bounded secondary positions |
| Evo II | Fortress States adds integrated border-state sectors with stronger forts, anti-air, radar, supply work, and selective coastal defenses |
| Evo III | Fortress World adds bounded internal redoubts around capitals and major strategic positions |
| Type | Minor Repeatable |
| Chaos level | `1` |
| Primary cluster | Sudden Abundance |
| Additional cluster | Military Preparation |
| Member severity in each | Medium |
| Status after implementation but before full live acceptance | Needs Testing |

The workbook's actual field structure decides how the two cluster memberships are stored. The final exports and cluster member lists must express both without losing the primary assignment.

## Validation layers

### Static validation

- syntax and encoding
- event namespace and id uniqueness
- registration and type arrays
- scripted effect and trigger references
- localisation keys and duplicates
- decision and mission targets
- building type and modifier validity
- event-log and Event Details mappings
- cluster member mappings
- achievement registrations
- asset paths, sprite names, dimensions, DDS format, and hashes
- workbook and CSV export alignment

### Deterministic scenario validation

- normal two-country border
- province touching two foreign countries
- ally border
- subject and overlord border
- active war front
- civil-war frontier
- occupied territory
- enclave
- strait-only neighbor
- island country
- tiny one-state country
- large continental country
- high existing fort levels
- mixed valid and capped provinces
- each evolution alone
- all evolutions together
- lower evolution disabled with higher evolution enabled
- repeated wave after border changes
- cluster root and queued-member routes
- multi-cluster arbitration
- save and reload during response project
- annexation or target loss during project
- achievement start, fail, cleanup, and completion

### Large-world and performance validation

Use a representative late-game map with many countries, occupations, civil wars, high forts, and several continents.

Prove:

- one wave token
- one country pass per valid country
- no province duplicate grant
- bounded evolved candidate selection
- no recurring background world scan
- cleanup of all temporary arrays and flags
- acceptable event execution and save impact

### Balance validation

Test at:

- early Chaos Level 1 campaign
- first Defense in Depth wave
- first Fortress States wave
- first Fortress World wave
- repeated high-tier wave
- major offensive war
- minor defensive war
- AI supply crisis
- island offensive planning

Review:

- war duration
- attack success against ordinary and anchor forts
- AI use of engineers, air support, supply, and breach posture
- fort cap saturation speed
- project affordability
- train, truck, fuel, equipment, and manpower impact
- cluster frequency
- direct Chaos generation

## Completion report requirements

The final implementation report must list:

- files changed
- event registration state
- baseline result
- evolution coverage
- response and project coverage
- AI scenario results
- probability-audit evidence
- Chaos-source evidence and shared-source audit
- cluster membership and multi-cluster behavior
- achievement tracking and tests
- asset manifest and sprite handoff
- localisation coverage
- Event Details and history coverage
- workbook and export result
- static validation result
- task-specific scenario result
- save-load result
- performance result
- improvement-loop addendum or closure handoff
- every remaining blocker, omission, fallback, or skipped test

Do not claim Event 064 complete while a mapped surface remains unresolved.
