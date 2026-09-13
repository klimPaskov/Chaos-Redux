# Event 059: The Offensive

## Part 5: Presentation, localisation direction, assets, and documentation

## Presentation choice

The event should use the ordinary global report and existing Event Logs surfaces. Its mechanic is hidden AI decision-making, so a custom window would expose internal formulas without giving the player a meaningful action.

The presentation package consists of:

- one activation report sent to every human player
- one concise report for each active-event evolution
- one combined activation report when the event first fires with one or more eligible evolutions
- normal History, Evolutions, Events, Event Details, and Clusters coverage
- one event report image reused across the event chain
- one difficult achievement with its own achievement icon family

The event should not create a new persistent meter. Material conditions remain visible through ordinary country, war, supply, equipment, air, and naval interfaces.

## Activation report direction

### Viewpoint

The report should describe a worldwide military planning shift from the viewpoint of observers comparing mobilization orders, field exercises, front activity, production contracts, and naval preparations across many states.

### Information visible to the player

The player should learn that:

- AI-run governments have adopted a more offensive strategic posture
- armies will place greater weight on attacks, concentration, and exploitation
- production and operational support will follow offensive priorities
- human-controlled countries are not directed by this system
- the posture persists after the report

### Information kept internal

Do not reveal:

- raw AI strategy weights
- hidden safety thresholds
- exact production ratios
- exact target rankings
- MTTH factors
- internal country archetype scores
- the next evolution before it becomes visible

### Tone

The tone should be serious, concrete, and global. It should focus on shortened timetables, reserves moving toward active fronts, attack exercises replacing static defense drills, transport schedules changing, and ports filling with invasion preparations.

Avoid abstract claims that every government has become irrational. The behavior is aggressive, not mindless.

### Option direction

The activation option is an acknowledgment. Its tone should be restrained and practical. It can sound like a commander or government accepting that future wars will be harder to contain. It should not use a joke, slogan, invented quotation, or broad moral statement.

## Evolution I report direction

The report should show that offensives now continue through reinforcement, resupply, and follow-up phases. Useful visible details include reserve trains moving forward, damaged routes being repaired under pressure, fresh formations entering sectors that were expected to quiet down, and landings receiving immediate reinforcements.

The option should communicate recognition that a pause can no longer be assumed after the first attack.

## Evolution II report direction

The report should show governments studying exposed rivals, unresolved claims, existing war goals, calls to arms, and conflicts that can be entered for gain. It should focus on timetables and diplomatic opportunities becoming operational plans.

The text must not name a hidden future target or imply that every AI country will declare war immediately.

The option should carry guarded concern about governments treating weakness as usable policy.

## Evolution III report direction

The report should show greater scale through crowded staging areas, several active axes, packed airfields, full ports, and reserve formations committed farther forward. It should communicate higher accepted risk without claiming that the AI receives stronger combat statistics.

The option should recognize that the world has entered a period of larger and more frequent operations.

## Pre-fire evolved opening direction

When the first firing starts with eligible evolutions, the activation report should describe the current strongest visible posture without separately reciting all earlier stages.

- with Evolution I, the opening should already show sustained pressure and prepared follow-up
- with Evolution II, it should also show exposed rivals and claims being converted into plans
- with Evolution III, it should show broad theater commitments and ambitious invasion preparation

The Event Logs retain the stage-by-stage record. The popup remains one coherent report.

## Event Details direction

Event Details should explain the public premise and persistent campaign role.

The details should cover:

- the worldwide adoption of aggressive AI strategy
- the distinction between AI behavior and direct country bonuses
- current-control behavior for human takeover and AI handback
- the broad themes of front activity, force concentration, offensive production, air support, naval invasion, and strategic opportunity
- the three evolution directions

It should not read like an implementation guide. It should not list script keys, exact weights, hidden formulas, or a country-by-country exception list.

## Event Logs coverage

### Events tab

The row should show:

- Event ID 59
- The Offensive
- Minor Fire-Once
- minimum Chaos level 1
- Diplomacy cluster membership
- High member severity
- current weight before firing
- fired count after activation
- enabled state

After implementation is accepted for testing, the event should be enabled by default with the other reworked events.

### History

The history entry should use a global presentation without a misleading country actor. It records the activation date and event identity once.

### Evolutions

Each evolution row should show:

- source event
- evolution name
- tier and stage
- activation date
- enabled state
- no country actor unless the shared UI requires a neutral global presentation

A pre-fire evolved opening can produce several evolution rows on the same date. Their order must follow stage order.

### Clusters

When the event participates in the Diplomacy cluster, the cluster history should identify it as fired or skipped with the correct reason. Its High severity must appear consistently in the member display. Diplomatic Panic must not appear as a separate alias cluster.

## Localisation coverage inventory

Final wording belongs to implementation. The following surfaces need finished localisation written from the direction above:

| Surface | Required content |
| --- | --- |
| Event name | Final public event name |
| Activation title | Worldwide doctrinal shift |
| Activation description | Concrete signs, persistent AI behavior, human exemption |
| Activation option | Restrained acknowledgment |
| Evolution I name and description | Persistence, reinforcement, follow-up pressure |
| Evolution II name and description | Claims, opportunities, intervention, weak rivals |
| Evolution III name and description | Scale, theater ambition, accepted risk |
| Evolution report titles | Current escalation without raw mechanics |
| Evolution report descriptions | Visible military and diplomatic evidence |
| Evolution options | Brief practical reactions |
| Events row and Event Details | Premise, type, Chaos level, active state |
| Cluster member text | Diplomacy membership, High severity, and authoritative role metadata |
| AI-only tooltip | Current human control suspends the behavior |
| Achievement title and description | Final wording from the achievement direction |
| Achievement eligibility tooltip | Clear challenge conditions and disqualifiers |

The implementation should use established project key patterns after inspecting the existing Event 059 and Event Logs localisation. Working file labels in this package are not final player-facing text.

## Localisation quality rules

Final text should:

- use concrete military activity
- distinguish current wars from new opportunity wars
- explain the human-control exemption once in clear language
- keep the AI capable and dangerous without describing it as insane
- avoid claims that the event grants combat bonuses
- avoid generic crisis filler
- avoid invented quotations, slogans, lyric fragments, and cultural references
- use complete sentences
- avoid em dashes and semicolons
- avoid short chains of dramatic fragments

## Event report image

### Asset role

One report image establishes the identity of the activation and can be reused by evolution reports. Reuse is intentional because the evolutions change the meaning of the same global doctrine rather than introducing new actors or visual identities.

### Source mode

Generated period-authentic documentary scene.

### Composition direction

Show a nationality-neutral combined-arms offensive during the late 1930s or 1940s. A column of period tanks and infantry should move through a breached defensive line while artillery smoke and aircraft establish the scale of the operation. Forward movement, concentration, and logistical preparation should be visible. The scene should feel like a wartime press photograph rather than modern cinematic concept art.

### Required visual qualities

- clear central subject at report-event size
- period-correct uniforms, weapons, vehicles, aircraft, and field equipment
- no readable text
- no identifiable national flag or political symbol
- no modern optics, electronics, vehicles, body armour, or street furniture
- no graphic gore
- no map-only composition
- no generic conference room
- no large empty sky or foreground that wastes the crop

### Target and handling

The final report image should follow the current Chaos Redux report-event reference and processor contract. The planning target is 210 by 176 pixels with the established black-and-white and sepia-card treatment. Exact runtime path and sprite registration must be confirmed against the repository before implementation.

Proposed stable basename:

`chaosx_event_059_the_offensive`

Proposed event-scoped runtime folder:

`gfx/event_pictures/059_the_offensive/`

The asset package must preserve the generated source, processed PNG preview, final DDS, prompt, source mode, review evidence, manifest, and GFX handoff.

## Achievement visual

The achievement uses separate source artwork designed for a 64 by 64 achievement surface. It must not be a resized crop of the report image.

### Motif direction

Show a small fortified shield or defensive line breaking and turning back a large offensive arrow. The visual should communicate a weaker defender reversing a major assault. Keep the silhouette readable at native size. Use a period map or military-symbol texture only as secondary detail.

### Required states

Follow the current achievement registry and asset precedent. Prepare the completed, grey, and not-eligible states if the repository uses the standard triplet.

### Source and processing

Use generated icon art through the icon workflow. Inspect the achievement reference family first. Preserve native transparency when required by the current consumer. Keep the achievement art independent from the event report image.

## Achievement player-facing direction

The achievement should be presented as a difficult reversal by a non-major country under the highest event evolution. The description must clearly communicate the qualifying defensive war, stronger AI major opponent, survival period, absence of a major ally, and victory condition.

The final title should be researched or written during implementation from this direction. The working label in the prompt is not final localisation.

## Documentation alignment

Implementation should update:

- the permanent Event 059 documentation
- the authoritative event catalog workbook
- the generated catalog CSV snapshots
- any AI-system documentation created for the event
- the event asset manifest and permanent provenance record
- the achievement registry documentation
- the Event Logs and cluster documentation when new generic behavior is required

The catalog row should use The Offensive, the full public premise, the three evolution summaries, Minor Fire-Once, Chaos level 1, Diplomacy cluster, High severity, and the implementation status reached after validation.

## Presentation acceptance

The presentation passes when:

- every human player receives the correct report once
- active-event evolutions produce one clear report each
- a pre-fire evolved opening produces one combined report
- History records the event once without a false actor
- Evolutions records each activated stage
- the Events row and Event Details show current information
- the Diplomacy cluster display shows High severity and correct fired or skipped state
- no raw localisation keys appear
- no text claims direct combat bonuses
- the report image is correct at native size
- the achievement icon states are complete and readable
