# Event 061: Return to Peacetime

## Part 6: Presentation, writing direction, assets, and achievements

## Presentation role

Return to Peacetime should look like a worldwide administrative and industrial conversion that ordinary people can see.

The visual and written center should be:

- factory lines being retooled
- military depots being inventoried
- trains and ports carrying returning personnel
- procurement offices cancelling contracts
- barracks emptying
- civilian construction absorbing labour and materials
- governments deciding whether to preserve a defence skeleton

Avoid making the event feel like a map change or a generic diplomatic announcement.

## Player-facing writing direction

This specification does not include final localisation.

Implementation should write complete in-world text for every visible surface.

### General tone

Use a weary, practical, bureaucratic tone.

The baseline is sudden. The prose should focus on concrete work and public expectation while avoiding dramatic claims.

Useful details:

- machine tools being reset
- munitions contracts being cancelled
- uniformed men receiving release papers
- warehouses sorting vehicles and rifles
- railway schedules filling with returning soldiers
- building ministries taking over materials
- officers preserving plans and records
- factories discovering that civilian retooling is harder than an order on paper

Avoid:

- generic statements that the world has changed forever
- abstract map language
- short dramatic fragments
- administrative text copied from the planning documents
- final prose that lists every modifier
- claims that all countries welcome the transition
- cheap humour about veterans, mass unemployment, or countries under attack

### Dynamic national variation

The national report should adapt to visible country state.

#### Country at peace

Emphasize civilian demand, cancelled orders, returning personnel, and the expectation of reconstruction.

#### Country at war

Emphasize contradictory orders, factories changing work while fighting continues, emergency exemptions, and pressure to reopen contracts.

Do not frame the country as voluntarily surrendering.

#### Major industrial country

Mention many factories, broad procurement networks, and the scale of contract settlement.

#### Small industrial country

Mention the concentration of the change in a few plants and the risk that one conversion alters the whole defence base.

#### Country with no factory conversion

Do not claim that plants changed when the exact quota was zero.

Focus on law, public support, and military administration.

#### Country already at low laws

Do not claim a law changed when it was already at the ordinary floor.

Explain the broader demobilization and later vulnerability.

### Humour and irony

The baseline can use restrained administrative irony in its acknowledgement option.

The irony should come from governments discovering that a signed cancellation does not instantly turn an arsenal into a civilian factory.

Evolution I can use a dry disposal-office tone.

Evolution II should remain serious and humane.

Evolution III should be sober. Voluntary pacifist options can use confident civic language. Forced disarmament should not use a joke.

Any cultural reference requires separate research and exact sourcing before use.

No cultural reference is required for this event.

## Event surface map

## Baseline national report

### Viewpoint

The affected country's government and public institutions.

### Visible information

- number of factories converted
- War Support and Stability shift
- economy law change
- conscription law change
- reconversion penalty
- Return to Rearmament availability

### Information to keep out of the opening report

- exact future evolution effects
- hidden AI stance
- hidden Readiness pillar points
- anti-exploit variables
- future extreme-law settlement conditions

### Option direction

An acknowledgement that the transition is already underway.

The tooltip gives the exact result and points to the decision category.

## Swords into Ploughshares warning

### Viewpoint

Civilian reconstruction authorities and military quartermasters.

### Visible information

- stockpiles are being reviewed
- surplus equipment may be dismantled or sold
- protection decisions are available
- a deadline is active
- the recovered value will support civilian reconstruction

### Uncertain information

The exact final quantities can remain estimated until the resolution because stockpiles and war conditions can change.

### Option direction

A practical instruction to review the stores.

## Swords into Ploughshares result

### Viewpoint

The national disposal and reconstruction program.

### Visible information

- broad equipment families removed
- protected families
- civilian disposition
- Reconstruction Materials tier

The report should not claim every individual rifle or vehicle was physically melted down. Disposal can include dismantling, conversion, sale, and parts recovery.

## The Great Demobilization warning

### Viewpoint

Military command and demobilization offices.

### Visible information

- an approximate number or share of eligible divisions is at risk
- cadre and border-protection actions are available
- current war state changes the target
- manpower and equipment will return through safe disband

### Tone

Serious and specific.

Avoid treating soldiers as an abstract resource dump.

## The Great Demobilization result

### Viewpoint

Returning service personnel, transport systems, employers, and military administration.

### Visible information

- divisions mustered out
- manpower returned when measurable
- broad equipment return
- Veteran Reintegration tier

Do not imply that every returning soldier immediately finds work.

## Permanent Peace settlement

### Viewpoint

A government deciding whether national defence institutions still have a legal place.

### Visible information

- current Readiness band
- whether immediate exemption exists
- the last-chance conditions
- the 90-day deadline
- active-war deferral when applicable
- the two extreme laws and broad visible consequences

### Information to keep hidden

- exact AI probability
- achievement disqualifier logic
- future event connections
- raw structural-action flags

### Option direction

The report should direct the player to the settlement decisions.

It should not present forced abolition as an ordinary neutral law adjustment.

## Return to Rearmament category text

### Category header

Show:

- Rearmament Readiness total and band
- qualitative status of industry, economy law, conscription, institutions, and public reserves
- unresolved converted factory capacity
- current economy and conscription law restoration targets
- current mission and deadline
- current reconversion phase

The category header should remain concise enough that the actions are visible without excessive scrolling.

### Decision descriptions

Every decision description should answer:

- what institution or physical work is being undertaken
- what the country must commit
- how long it takes
- which visible Event 61 state it changes
- why it is unavailable when blocked

Do not repeat the full category premise in every action.

### Tooltips

Nonstandard tooltips should show:

- exact factory batch and target state
- current and target law
- civilian factory commitment
- Stability or War Support transaction
- structural-action credit when relevant
- Readiness band effect
- irreversible ledger loss for permanent conversion
- emergency aftermath

## Idea and law text direction

### Industrial Reconversion Shock

Describe cancelled contracts, retooling, labour transfers, and broken supplier rhythm.

The stage description should explain why the penalty changes over time.

### Reconstruction Materials

Describe recovered machine tools, metals, vehicles, and industrial parts entering civilian rebuilding.

Do not imply that the country gained free new factories.

### Veteran Reintegration

Describe returning technicians, drivers, engineers, and workers alongside housing and employment pressure.

### Peace Dividend

Describe civilian resources released by the absence of a standing military.

The text should make clear that the benefit exists only while the country maintains the extreme peace structure.

### Improvised Rearmament

Describe rushed contracts, weak training, competing orders, and production disorder.

### Peacetime Economy

Describe a legal economy tier that dismantles most routine arms production and favors civilian recovery.

### No Army

Describe the legal abolition of the conventional standing army and the difficulty of restoring recruitment institutions.

## Event Logs and Event Details direction

### Event name

Use the fixed event name:

`Return to Peacetime`

### Event Details premise

Explain that governments across the world convert military production, lower mobilisation laws, and release wartime institutions into civilian life.

Do not list exact percentages, hidden thresholds, or future evolution conditions in the premise paragraph.

### Evolution catalog entries

Each evolution entry should explain its public premise:

- stockpile disposal for reconstruction
- standing-army demobilization
- extreme peace laws for countries that fail to rearm

The catalog surface should not display fake firing dates or history sequence numbers.

### History row

Show the event name, date, repeat count, and concise global result.

### Related evolution history

Use real activation records with tier, stage, and actor only when an actor exists.

## Visual style direction

Use static generated artwork with a grounded 1930s to 1940s documentary and painted strategy-game presentation.

The event is global and anonymous.

Do not depict a named historical leader, a specific identifiable government, or a real political symbol as the main subject.

Avoid modern factory equipment, modern tactical gear, readable generated text, national flags, glowing fantasy effects, and celebratory parade imagery.

## Report image family

Target consumer size: `210x176` for each report image, subject to exact local precedent confirmation.

### Baseline report image

Composition direction:

- broad factory interior
- artillery or military vehicle production line being dismantled or retooled
- civilian machinery or transport equipment beginning to replace it
- workers and returning soldiers as secondary figures
- no readable signage
- no dominant flag
- clear visual split between wartime machinery and civilian production

### Evolution I report image

Composition direction:

- large military depot or warehouse
- rifles, crates, vehicle parts, and machine tools being sorted and dismantled
- civilian reconstruction materials leaving the depot
- practical industrial activity, not a bonfire of weapons
- no gore or triumphal symbolism

### Evolution II report image

Composition direction:

- demobilization center or railway platform
- soldiers returning equipment and receiving papers
- trains, baggage, families, and civilian clothing
- broad human scale without a famous person
- serious but hopeful tone

### Evolution III report image

Composition direction:

- closed arsenal gates and quiet barracks
- civilian building work visible beyond them
- remaining military machinery covered or removed
- a restrained sense of vulnerability
- no apocalypse imagery

## Decision category picture

Use a static full-canvas category picture based on the exact installed vanilla reference dimensions.

Composition direction:

- factory floor divided by use, with military tooling on one side and civilian production on the other
- procurement files, machine tools, and railway freight as supporting details
- no painted buttons, counters, meters, or fake interface controls
- readable at the category picture's small size

## Icon family

Every distinct consumer receives a distinct icon unless local vanilla reuse is explicitly accepted for a generic law or cost surface.

### Category icon

Visual direction:

- factory gear divided between a rifle silhouette and civilian tool
- clear at small size
- neutral global identity

### Rearmament decision icons

Required concepts:

- arms contracts
- state arsenal reopening
- general staff
- public defence campaign
- economy-law restoration
- conscription restoration
- emergency rearmament
- permanent civilian conversion
- Defence Ministry
- National Arsenal
- Service Registry
- emergency national defence

### Evolution I decision icons

Required concepts:

- army stores protection
- mobile and armoured reserve protection
- air reserve protection
- logistics reserve protection
- central reconstruction
- civilian auctions

### Evolution II decision icons

Required concepts:

- essential cadres
- threatened-border formations
- accelerated mustering out

### Evolution III decision icons

Required concepts:

- national defence settlement
- voluntary permanent peace
- extreme-law recovery

### Idea icons

Required concepts:

- Industrial Reconversion Shock
- Reconstruction Materials
- Veteran Reintegration
- Peace Dividend
- Improvised Rearmament

### Law icons

Required concepts:

- Peacetime Economy
- No Army

The two law icons should belong to the same visual family and remain distinct from national-spirit icons.

## Asset ownership

Use:

- `chaosx_generated_event_art` for the four report images and category picture
- `chaosx_icon_artist` for the category, decision, idea, law, and achievement icons
- `chaos-redux-event-assets` for source mode, reference inspection, processing, DDS conversion, GFX handoff, manifest, and final placement

Final runtime wiring remains with the main implementation agent.

The asset package needs exact local vanilla-reference inspection before dimensions and sprite paths are locked.

## Achievement set

The event supports three demanding achievements.

Names below are working localisation labels. Internal keys are stable planning identifiers.

## Achievement 1: The Arsenal Returns

### Internal key

`chaosx_achievement_061_arsenal_reborn`

### Difficulty

Very hard.

### Player challenge

Recover from the deepest Event 61 demobilization without an external shortcut.

### Entry conditions

- player-controlled ordinary country
- non-major when the relevant Event 61 cycle begins
- forced into Peacetime Economy and No Army through Evolution III
- independent at the moment the challenge starts

### Completion conditions

Within a tuned hard period after forced adoption, the same country must:

- restore at least Partial Mobilization
- restore at least Limited Conscription
- reopen every Event 61 ledger unit currently owned from the qualifying cycle, or prove that a lost state no longer belongs to the country
- field at least 24 ordinary conventional divisions
- remain independent
- avoid capitulation after the recovery challenge begins

Suggested time target: 1,095 days.

The final period requires balance testing for small countries and different start dates.

### Disqualifiers

- Event 82 restoring either qualifying law step
- Emergency Rearmament
- Emergency National Defence
- Black Market shortcut supplying the qualifying recovery
- becoming a subject
- using annexed factory gains to satisfy the ledger requirement
- tag switching away from the qualifying country
- scripted debug setup

### Tracking rules

Record:

- qualifying cycle ID
- forced-law date
- initial qualifying ledger total by owned state
- external shortcut flags
- law milestones
- final division count
- independence state

A state lost through war should be removed from the owned-ledger completion denominator. Annexing replacement factories does not reduce the original owned ledger.

### Icon direction

Closed arsenal doors being forced open around a growing gear and rifle silhouette.

Use a strong central silhouette and no text.

## Achievement 2: Swords, Ploughshares, Swords

### Internal key

`chaosx_achievement_061_swords_ploughshares_swords`

### Difficulty

Very hard.

### Player challenge

Accept meaningful civilian reconstruction, rebuild without an emergency shortcut, then survive a defensive war against a major.

### Entry conditions

- player-controlled ordinary country
- Swords into Ploughshares removes a meaningful equipment value from the country
- the country receives and uses a nontrivial Reconstruction Materials tier

### Middle conditions

Before the next Event 61 baseline cycle, the same country must:

- restart arms contracts
- reopen at least a tuned share of its current owned factory ledger
- restore at least one economy-law step
- reach Readiness 60

Suggested ledger share target: 75 percent of qualifying owned capacity.

### Completion condition

The country wins a defensive war against a major power after completing the middle conditions.

Victory must be defined through a robust result such as:

- enemy major capitulates
- signed peace leaves the player's country independent and in control of every prewar core
- another existing war-result helper proves a defensive victory

### Disqualifiers

- player declares the qualifying war
- Emergency Rearmament
- Emergency National Defence
- Event 82 supplies the qualifying law restoration
- Black Market shortcut supplies qualifying recovery
- becoming a subject
- changing tag outside an approved cosmetic continuation
- debug setup

### Tracking rules

Record:

- qualifying Event 61 cycle
- equipment value removed
- Reconstruction Materials tier
- reconstruction benefit used for a minimum duration or until expiry
- ledger restoration share
- law restoration milestone
- Readiness milestone
- war initiator and enemy-major status
- victory result

### Icon direction

A plough blade reshaped into a bayonet around a factory gear.

The two uses should form one readable object at achievement size.

## Achievement 3: The Arsenal Sleeps

### Internal key

`chaosx_achievement_061_arsenal_sleeps`

### Difficulty

Hard or secret, subject to project achievement policy.

### Player challenge

Maintain an exposed state without a conventional army through a long high-Chaos period.

### Entry conditions

- player-controlled continental major at challenge start
- at least one foreign land border
- independent
- Peacetime Economy active
- No Army active
- zero eligible conventional divisions
- not in a faction

### Sustained conditions

Maintain for five continuous years:

- Peacetime Economy
- No Army
- zero eligible conventional divisions
- independence
- no faction membership
- high Stability
- global Chaos at 800 or higher

Suggested Stability floor: 70 percent.

### Protection exclusions

The country cannot rely on:

- subject armies acting as its normal defence shield
- joining a faction temporarily
- becoming a subject
- a puppet ring created after the challenge begins
- special event-owned conventional substitutes that violate the spirit of No Army
- Emergency National Defence

Ordinary nonhuman or owner-excluded special units need explicit achievement classification so a hidden exception does not invalidate or trivialize the challenge.

### Failure and reset

The continuous timer resets when any sustained condition fails.

A defensive war does not automatically fail the achievement if the country remains independent and keeps the laws. Using emergency rearmament does fail it.

### Icon direction

A padlocked arsenal beneath a laurel, with idle smokestacks and a distant border marker.

Keep the symbol readable and avoid text.

## Achievement visibility and localisation direction

Achievement descriptions should state the visible challenge clearly.

They should not expose every anti-exploit flag.

Disqualifying shortcuts that a reasonable player might use should appear in the achievement requirement tooltip.

Rare implementation-only checks remain hidden.

## Asset requirement count

Minimum planned custom visible assets:

| Asset family | Count |
| --- | ---: |
| Report images | 4 |
| Decision category picture | 1 |
| Category icon | 1 |
| Rearmament and exit decision icons | 13 |
| Evolution I decision icons | 6 |
| Evolution II decision icons | 3 |
| Evolution III decision icons | 3 |
| Idea icons | 5 |
| Law icons | 2 |
| Achievement icons | 3 |
| Minimum total | 41 |

The final count can rise when one decision needs separate active, locked, or route-specific icon treatment. It should not fall through generic duplication without an explicit visual audit decision.

## Presentation acceptance conditions

Presentation is complete only when:

- every visible surface has final in-world text
- dynamic text shows actual country results
- no planning labels or developer notes appear in localisation
- report images use the correct local event-image precedent and dimensions
- the category picture contains no fake controls
- every distinct decision, idea, law, and achievement has an intentional icon or an approved exact vanilla reuse
- final assets are processed and wired through the event-asset workflow
- no placeholder, wrong crop, halo, raw key, or missing sprite remains
- Event Details and history surfaces use the correct metadata model
- the three achievements have persistent tracking, disqualifiers, icons, and documentation
- cultural references are omitted unless separately researched and sourced
