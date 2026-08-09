# Event 20 Black Plague Specification, Part 7

## Evolution V, world-end path, terminal scenario, defeat, and aftermath

All labels in this file are working labels, not final localisation.

## Evolution V purpose

Evolution V unlocks the Rat King world-end path after the rat empire has become large, lethal, organized, and capable of continent-scale planning. It does not fire the terminal scenario immediately. The triggerable scenario in Part 9 can create the Rat King and Evolutions I through IV, but it never records Evolution V or sets the terminal world-end state.

The user requirement has two distinct gates.

1. The rats occupy enough states and kill enough people to begin a deliberate world takeover path.
2. The Rat King controls a continent and finishes that path, which triggers the world-end scenario.

The specification preserves both gates.

## Evolution V eligibility

Evolution V can begin rolling when all of the following are true.

- Chaos is at least 1000.
- Evolution IV is recorded.
- The Rat King exists.
- The Rat King controls a major share of eligible world states or a high absolute number appropriate to map size.
- Event-attributed Black Plague deaths pass a catastrophic global threshold.
- The Rat King has completed the necessary late government and military preparation groups.
- A permanent target has been selected from a continent that passes the live state, capital, and refuge viability gates. Its control is re-evaluated before Evolution V can resolve.

### Planning thresholds

The live implementation should use dynamic map-size aware thresholds. The following are balance targets.

- at least 15 to 25 percent of eligible world states under Rat King control
- at least five absorbed Rat Nations or equivalent dominance history
- at least 250 million event-attributed civilian deaths in a normal world population setup
- high Dominion and Sentience
- no active disputed crown crisis

The death threshold should scale when the total world population differs greatly from the normal setup. A hybrid requirement can use both an absolute minimum and a percentage of starting world population.

## Evolution V pacing

The evolution should normally take about ninety to one hundred eighty days after full eligibility.

It accelerates when:

- the Rat King wins major wars
- another capital falls
- a second continent receives rat territory
- human global countermeasure progress is weak
- Hierophancy controls government

It slows when:

- the Rat King loses territory
- human countries liberate a major plague basin
- the crown or council enters internal crisis
- a global cure and containment campaign reduces active infection sharply

The evolution roll stops if the Rat King is destroyed.

## Evolution V unlock effects

When Evolution V records:

- the event log adds the fifth evolution entry
- the world-end focus lane becomes visible in the Rat King tree
- the shared disease board reports terminal readiness, the committed continent, preparation progress, and takeover status
- human countries receive stronger world-threat cooperation actions
- the Rat King gains a final route-specific cosmetic and animated UI state
- the terminal scenario remains locked until the focus route and continent condition are complete

## World-end readiness panel

The shared board summary should show public terminal progress without revealing hidden implementation details. It remains part of the existing disease interface and does not create an additional terminal category or dedicated terminal window; the separate national-response category continues to own cure and strategic management.

### Rat King view

- selected target continent
- continent control percentage
- surviving continental capitals
- required world-end focus groups
- Dominion, Sentience, Brood Cohesion, and Hunger readiness
- global event-attributed deaths
- active human countermeasure strength
- world-end path status

### Human view

Human countries should see:

- Rat King control of the threatened continent
- remaining major continental defensive centers
- global infected and Rat-Controlled state count
- major cooperative response options
- no exact hidden Rat King focus completion unless intelligence reveals it

## Continent definition

The terminal gate needs a robust definition of continent control.

### Eligible states

Count land states assigned to the chosen continent that are not wasteland, impassable, or otherwise excluded by the existing continent system.

### Control requirement

The Rat King controls a continent when:

- it controls at least 90 percent of eligible land states on that continent
- it controls every surviving major continental capital and designated strategic refuge state
- no human major holds a connected enclave above a small threshold
- no scripted protected state blocks completion incorrectly

The 90 percent threshold prevents one tiny remote island or invalid state from blocking the scenario. Strategic capitals and refuges prevent the Rat King from triggering after ignoring the continent's real resistance.

The implementation should use existing continent and state group data rather than a hardcoded state list where possible.

## Selecting the target continent

The Rat King can select a continent after the non-continent Evolution V gates are ready and before Evolution V resolves. The choice is permanent for the reign, so the final control ledger cannot be moved to exploit a later front.

### AI selection factors

- current Rat King state share
- land connection
- existing infected states
- population and capitals
- port access
- human military strength
- distance from the Rat King capital
- government route

### Player selection

A human Rat King sees a short list of valid continents with control progress and strategic risks. The first valid choice is permanent for the reign, so the player cannot switch to exploit progress.

## World-end focus lane

The lane should be a late, deep route with several focus groups and campaign objectives. It should not be one final button.

### Group 1: Name the World Prey

**Role**: choose the target continent and transform ordinary conquest into a terminal campaign.

**Requirements**:

- Evolution V route open
- target continent selected
- sufficient Dominion and Sentience

**Unlocks**:

- continental campaign missions
- world-end readiness panel
- special map objectives

### Group 2: Break Human Coordination

**Role**: weaken coalition command, ports, radio, rail, and medical exchange.

**Mechanics**:

- intelligence operations against aid corridors
- timed objectives against communication hubs
- plague pressure on major transport centers
- no automatic free state transfer

### Group 3: Close the Harbors

**Role**: capture or neutralize ports that sustain continental relief and evacuation.

**Mechanics**:

- port-targeted campaign missions
- Sea Brood transfer
- overseas infection and blockade pressure
- strong human naval and air counterplay

### Group 4: Silence the Capitals

**Role**: capture every designated continental capital or strategic refuge.

**Mechanics**:

- timed capital objectives
- large Dominion rewards
- human emergency defense missions
- severe consequences for Rat King failure

### Group 5: Crown the Continent

**Role**: verify the 90 percent state control threshold and install royal burrow administration.

**Requirements**:

- state control threshold
- designated capitals controlled
- Brood Cohesion above crisis level
- no severed network crisis

**Unlocks**:

- final world-end focus group
- terminal super-event readiness

### Group 6: Complete the World-End Path

This group represents the Rat King's final organization of global takeover.

It should require:

- Crown the Continent completed
- high Dominion and Sentience
- global death threshold
- world_end not already active
- no incompatible terminal scenario

It should include several preparations rather than one generic focus.

- integrate continental burrow commands
- establish global port and tunnel routes
- create the final royal pulse
- suppress internal brood rivalry
- adapt plague pressure against mature human countermeasures
- prepare the terminal proclamation

The last focus sets the event-specific ready flag. It does not bypass the live continent and chaos checks.

## Human last-response package

Evolution V should create urgent but playable countermeasures for surviving human countries.

### Global countermeasure exchange

Countries can pool cure progress, medical reserve, and intelligence. Sharing is cheaper and faster because world threat is explicit.

### Continental defense objectives

- hold designated capitals
- keep at least one relief port open
- maintain a clean supply corridor
- liberate a Rat-Controlled state group
- destroy a royal burrow node
- protect the leading countermeasure country

These are timed missions with real map requirements and distinct failure effects.

### Anti-rat military coordination

Countries can coordinate air, armor, engineers, and containment through shared world-threat actions. They do not automatically form a new faction if existing diplomacy already provides a coalition.

### Emergency evacuation

A government can move selected industry, scientists, or leaders to another continent at large cost. Population evacuation carries infection risk and cannot save whole states instantly.

### Strike the crown

A high-risk objective against the Rat King capital or sovereign can reduce Dominion, interrupt the world-end path, and create a disputed crown crisis. It requires real military reach and intelligence.

## Terminal trigger

The terminal world-end scenario fires only when all of the following are true at the same time. The manual triggerable scenario does not bypass any item in this list.

- global Chaos is greater than 1000
- no other world_end flag is active
- Evolution V is recorded
- the Rat King exists
- the Rat King controls the chosen continent under the defined rule
- the final world-end focus is complete
- the event-specific ready flag is set

The trigger should be checked after relevant focus completion, state control changes, and campaign objective updates. It should not rely on a full daily world scan.

## Terminal scenario effect

The terminal scenario is a resolved campaign end in which the Rat King has taken over the world.

### Required sequence

1. set the shared world_end flag
2. set the Event 20 Rat King world-end scenario flag
3. lock incompatible future random events and terminal branches
4. stop ordinary evolution and rat-emergence processing
5. set the matching super-event visible state
6. set the unique super-event audio ID through the settings-aware helper
7. show the world-end super-event
8. begin a short terminal conquest sequence
9. transfer or annex remaining human territory to the Rat King
10. mark every remaining eligible human state as Rat-Controlled or terminal plague territory
11. resolve remaining human armies and countries consistently
12. update event log, scenario history, death totals, mapmode, and documentation state

### Terminal conquest pacing

The takeover can complete through a short staged sequence of several days or weeks so the map visibly changes. It should not require the player to fight years of ordinary wars after satisfying the terminal condition.

The sequence must be deterministic enough to finish. A world-end scenario that leaves random surviving countries indefinitely is incomplete.

### Population result

The terminal sequence can remove the ordinary surviving population floor. Remaining human population falls through final terminal death effects and transfer logic. The Deaths tracker records these losses without duplicating earlier plague deaths.

### Rat result

- Rat King remains the only rat country
- all brood units become royal units or are removed if over performance cap
- the final country identity and flag apply
- world-end focus and decision systems close into a terminal state

## World-end super-event

### Role

Terminal campaign end. The Rat King has taken over the world.

### Trigger moment

The super-event fires after world_end and scenario flags are set, immediately before or at the beginning of the terminal transfer sequence.

### Text direction

- title direction about the completed dominion of the Rat King, avoiding generic end-of-world wording
- description direction centered on emptied cities, organized burrow rule, surviving human traces, and the sovereign's global command
- no hidden mechanics, tuning values, or process notes
- main quote uses a verified public-domain candidate or new research
- button remark requires verified research and should be short, grim, and final

### Verified quote candidate

The research note includes a short King James Version excerpt from Revelation 6:8 as a candidate. It fits death, pestilence, and final judgment. Final selection remains a super-event text decision.

### Image direction

Generated fictional super-event art at 457 by 328.

- sentient Rat King in a ruined global capital or symbolic seat of power
- organized rat court or army
- evidence of a conquered human world
- strong central composition
- no map table as the main subject
- no readable text
- no comedy or mascot treatment

### Audio direction

A unique one to two minute licensed or public-domain musical track with finality, ritual, and dread. A public-domain `Dies Irae` recording is a research lead, not a wired final selection. It must be downloaded from a legitimate source, trimmed if needed, converted to a 44.1 kHz stereo WAV, documented, assigned a unique audio ID, and kept distinct from the coronation track.

## Nonterminal victory outcomes

The event needs satisfying defeat and containment outcomes even when the world-end path fails.

## Plague eradicated before Evolution III

When every state is Cured and no weaponized release remains active:

- record global eradication
- clear the Black Plague world-threat source
- retain cure progress and prevention reforms
- close emergency decisions
- open optional reconstruction and monitoring
- preserve demographic losses

A normal news event is sufficient unless deaths reached a global catastrophe threshold.

## Rat Nations defeated before Rat King

When no Rat Nation exists and no resurgence basin remains:

- record rat phase defeat
- keep disease cleanup active
- open burrow clearance and reconstruction missions
- reduce world-threat source only after severe infection also falls
- grant event and achievement tracking

If the crisis was regional, use a news or report event rather than a super-event.

## Rat King defeated

The Rat King is defeated when:

- the Rat King country no longer exists
- no successor brood controls enough territory to restore it
- no royal capital or active world-end project remains
- surviving rat units and tags are cleaned consistently

### Immediate consequences

- world-end path closes
- Evolution V cannot continue without a new valid Rat King, which should be heavily restricted
- all liberated states remain plague states until cleaned
- human coalition decisions shift from war to containment and reconstruction
- captured Rat King archives can accelerate the global countermeasure
- Dominion and Sentience values are archived for event history

The current runtime resolves the zero-controlled-state condition through an idempotent resolver. It retires `RTX`, closes active royal preparation, preserves `RTA`, former Royal Node markers, Rat Infestation, and surviving plague states, and emits `chaosx.nr20.71` once. A human response host then receives `chaosx.nr20.73`, which opens the shared `Seal Royal Burrows` state operation. Successful sealing reports `chaosx.nr20.74`, lowers infestation, raises containment, and adds countermeasure progress; a 180-day timeout reports `chaosx.nr20.75`, raises infestation and incoming exposure, and never revives the King or creates another tag.

### Possible succession

A limited Rat King restoration can occur only when:

- Evolution IV remains active
- several RTA brood markers survive
- one has high proto-sentience and dominance
- the previous Rat King was defeated before the world-end path passed a permanent failure point
- a long cooldown has elapsed

The system should not create repeated coronation super-events every few months. The first coronation remains the only global super-event. A restoration uses a normal event or news item.

The implemented route keeps these limits concrete. RTA must control more than one marked state, retain an established human basin for the new Royal Basin, meet the Sentience and Coherence gates, and spend the centralized Brood Mass cost over a 180-day decision. Evolution V flags, terminal takeover, and world end permanently block the attempt. A successful restoration reuses RTX and the existing King initializer, keeps RTA alive, emits a normal news report, and never records a second Evolution IV or coronation super-event. A failed basin selection refunds the reserve and applies a 240-day cooldown before the route can be considered again.

## Defeat aftermath package

A defeat aftermath super-event is justified only if the Rat King crisis was global or near-global, lasted long enough, and caused enormous deaths or destruction.

### Eligibility

- Rat King existed for at least a major campaign duration
- rat territory reached several regions or continents
- event deaths crossed a catastrophic threshold
- multiple major countries participated in the defeat

### Aftermath content

- reflective defeat super-event with unique image, quote, and audio if eligibility is met
- recurring reconstruction and vigilance events
- international countermeasure sharing or inspection compact through existing diplomacy systems
- long-term population recovery and ruined-state programs
- memorial and anti-biowarfare condemnation effects
- optional restrictions on future Black Plague weaponization

The reserved global defeat super-event remains intentionally gated behind the catastrophic eligibility package. The current static tranche promotes final slot-087 art, selected quote/localisation, audio ID 103, sprite registration, and shared sound/music wiring; release attribution and live consumer validation remain open.

The accepted aftermath actions now have concrete shared-category runtime surfaces. Rebuild and Keep Vigilance, International Inspection Compact, and Condemn Future Weaponization use paid timed country projects with phase, defeat, partner, findings, and material gates. Population Recovery is a 420-day ruined-state programme that applies a timed stewardship modifier, reduces tracked devastation, improves treatment, and lowers relapse risk in controlled recovering or cured states. Memorial and Biosecurity Charter is a 120-day country project that preserves a permanent memorial and anti-biowarfare record, advances countermeasure findings, and applies durable stewardship to recovered states. These projects remain ordinary disease responses; they do not create another category, cure by fiat, or open Evolution V.

A short regional rat outbreak should not create a new world order or global treaty.

## Recovery after a global crisis

### State recovery

- burrow clearance
- disease cleanup
- hospital rebuilding
- infrastructure and rail repair
- population growth recovery
- resistance and administration restoration
- refugee return when compatible systems exist

### Country recovery

- remove emergency burden gradually
- restore divisions tied to cordons
- reduce consumer goods and supply penalties
- preserve optional prevention law
- resolve war support and stability scars

### Global recovery

- clear world threat only after no rat country and no severe infection remain
- maintain global countermeasure knowledge
- record event deaths permanently
- keep condemnation for weapon users
- preserve event log and super-event history

## Event log and Event Details

### History

The history row records:

- Event 20 firing date
- origin state and owner
- event type
- actor flag when valid

### Evolution entries

Five evolution entries record:

- Evolution I strain escalation
- Evolution II overseas spread
- Evolution III first Rat Nation emergence
- Evolution IV Rat King coronation
- Evolution V world-end path unlock

Each entry should include actor context when a specific Rat Nation or Rat King owns the milestone.

### Event Details

Event Details describes the premise and visible lifecycle without listing mechanical effects or hidden conditions.

It should explain that:

- a severe Black Death strain begins in one mainland state
- countries can prepare, contain, treat, and study it through the shared disease system
- the disease can become a biological weapon
- later evolutions can carry it overseas and create nonhuman rat states

It should not reveal exact Rat King world-end thresholds, hidden mutation rolls, achievement requirements, or numeric death formulas.

## Catalog replacement direction

The obsolete catalog sentence about every country on a random continent receiving a temporary idea must be replaced.

The catalog row should reflect:

- state-based mainland origin
- persistent spread and population deaths
- shared containment and biowarfare systems
- Evolution I stronger strain
- Evolution II overseas spread
- Evolution III Rat Nations
- Evolution IV Rat King
- Evolution V world-end path
- terminal scenario where the Rat King takes over the world
- Minor Fire-Once type
- Diseases cluster
- Severe member severity

Final catalog wording must match the implemented in-game Event Details and evolution localisation. The spreadsheet worker should not copy working planning prose if implementation wording differs.

## Documentation package after implementation

Implementation should update:

- canonical event doc under `docs/events/020_black_plague/overview.md`
- biological warfare system documentation
- disease mapmode and crisis board documentation
- world-threat source documentation
- special chaos and nonhuman country classifier documentation
- Rat Nation and Rat King country package docs
- focus tree and decision route coverage
- asset manifest and GFX handoff
- super-event research and audio docs
- event catalog workbook
- any cluster documentation

## Acceptance criteria for Evolution V and end states

- Evolution V requires Chaos 1000 or more, Rat King existence, large conquest, and catastrophic deaths
- it unlocks a focus route rather than firing world end immediately
- continent control uses a robust percentage plus strategic-capital rule
- the Rat King must finish the world-end path
- terminal trigger rechecks live chaos, world_end, continent, country, and focus conditions
- the terminal scenario fully resolves the map into Rat King control
- remaining population deaths are recorded once
- incompatible future systems stop
- world-end super-event has complete unique text research, image, audio, and wiring
- human countries receive meaningful last-response missions
- plague eradication, rat defeat, and Rat King defeat have distinct recovery flows
- defeat aftermath super-event appears only for a genuinely global costly crisis
- Event Details and catalog describe the premise without exposing hidden mechanics
