# Event 011 Secret Alliance Spec Part 2: Evolutions

## Evolution Model

Secret Alliance has baseline progression plus three true evolutions.

Baseline progression changes intensity inside the hidden pact. True evolutions change the available member classes, visible player agency, and reveal pressure.

Each evolution needs two entry paths:

- active-event path: Event 011 already fired and the hidden pact evolves
- pre-fire evolved opening: global evolution state has already advanced when Event 011 first fires, so the opening starts at the appropriate intensity

## Baseline Progression

Baseline starts with three minor founders and a hidden organizer.

Baseline goals:

- make the world feel slightly wrong
- keep impact small but noticeable after time
- seed suspicion and pressure without opening a full countermeasure menu
- keep the roster hidden

Baseline actions:

- rare low-grade reports
- minor opinion or diplomatic friction against the player
- small pressure on trade, press, or border posture
- hidden recruitment preparation if Evolution I is close
- light sabotage only as a narrative hint, not major building damage

Baseline should not start border wars, major industrial damage, public ultimatums, faction creation, or full war.

## Evolution I: Wider Cell Network

Design role:

Evolution I widens the compact into a minor-state network. It is still secret, but the pattern becomes harder to ignore.

Unlock direction:

- baseline pact survives long enough
- pact cohesion is healthy
- player exposure remains low while threat pressure rises
- at least one eligible minor recruit exists
- world tension, chaos tier, or regional panic makes recruitment plausible

Active-event behavior:

- invite additional minors through capped hidden pulses
- prefer factionless minors with grievances, ideological hostility, or border proximity
- introduce low-commitment associate-like members that can later be peeled away
- increase report strength without opening the full roster
- add passive evidence that can matter once Evolution II countermeasures unlock

Pre-fire evolved opening:

- start with the three founders plus extra minor network members if eligible
- keep the organizer a minor unless Evolution II is also active
- give the player higher starting suspicion and shorter time before Evolution II

Player experience:

- the player sees a network, not a single incident
- they can infer region, route, or actor type
- they still lack enough proof for direct retaliation

## Evolution II: Major Sponsor And Violent Methods

Design role:

Evolution II makes the pact dangerous. A major country can sponsor or organize the pact, and the player receives a decision category for countermeasures.

Unlock direction:

- Evolution I exists or the network is already large enough
- player is a regional hegemon, major, or high-threat country
- at least one major rival is eligible and not at war with the player
- pact pressure, exposure, or provocation heat has crossed a tuned threshold
- world tension or chaos state supports clandestine escalation

Active-event behavior:

- if no major is in the pact, try to add one major sponsor or organizer
- if no eligible major exists, promote the strongest member into a hardened organizer
- unlock the player countermeasure decision category
- enable serious sabotage and provocation reports
- allow rare killings or disappearances only through safe abstract surfaces
- let neighboring known members enable border incident and border-war routes

Pre-fire evolved opening:

- start with one major organizer plus minors where possible
- if no major is eligible, start with a strong minor organizer and higher sabotage readiness
- present the opening as a discovery of an existing pattern rather than the beginning of the conspiracy

Player experience:

- counterplay becomes active
- the player can investigate, prepare, negotiate, expose, counter-sabotage, or risk border pressure
- bad decisions can raise provocation heat and make war more likely

Evolution II must not give the player a free reveal button. Evidence, cost, risk, and cooldowns govern exposure.

## Evolution III: Public Shadow Bloc

Design role:

Evolution III makes the pact difficult to deny. The bloc can become visible before full war, but it should still preserve a final brinkmanship stage unless war already exists.

Unlock direction:

- Evolution II has fired, or Event 011 used a pre-fire Evolution II opener
- pact has enough live members or a major organizer plus live minors
- player failed, delayed, or mismanaged exposure and split-pact routes
- provocation heat or threat pressure is severe
- at least one pact member borders the player or controls a strategic route near the player

Active-event behavior:

- the pact can become a visible public faction without immediate war if no member is currently at war with the player
- the public faction receives crisis and war-preparation pressure
- public member display replaces hidden suspect display
- a second major can join if player choices increased pact cohesion or if the player is much stronger than the pact
- emergency diplomacy, public exposure, and border crisis decisions replace early investigation

Pre-fire evolved opening:

- start from the Evolution II setup first
- schedule a short delayed intensification into Evolution III after hidden state initializes
- do not start directly with a fully visible faction unless a war condition already exists

Player experience:

- the player sees the Anti-[player country] Pact on the map
- war is likely but not instant unless a reveal trigger fires
- preparation, diplomacy, and border choices still shape the war

## Reveal Paths

Reveal can happen from:

- a pact member entering war with the player
- the player attacking a pact member
- a deliberate high-risk player exposure decision at sufficient evidence
- Evolution III crisis timer reaching the declaration threshold
- failed brinkmanship or border escalation that becomes formal war

Reveal should not happen from normal low-risk investigation alone. Ordinary exposure gives the player more knowledge, leverage, and defensive options. Full faction reveal is a major crisis.

## Collapse Paths

The pact can collapse before reveal if:

- too few valid live members remain
- the organizer is invalid and no replacement exists
- the player splits enough members through negotiation and evidence
- members enter player faction or become subjects in ways that make the pact impossible
- another Chaos Redux system makes normal diplomacy impossible

Collapse should:

- clear hidden roster state
- end active missions and selected targets
- record the outcome in event details
- keep achievement flags that record completed feats
- avoid firing the reveal super-event

## Membership Caps

All caps should be constants, not hardcoded numbers in multiple files.

Design direction:

- setup has three founders
- Evolution I adds minors only
- Evolution II allows one major sponsor or organizer
- Evolution III allows a second major under strict conditions
- membership growth is capped by phase, player strength, eligible pool, and pact cohesion

The implementation should expose the caps through `common/script_constants/011_secret_alliance_constants.txt` and use MTTH entries for recruitment pulse timing.

## Rare Variants

Rare variants add replay value without changing the main arc.

### Exile Committee

Condition direction:

- player annexed or occupied countries
- exiled or released states exist nearby
- candidates have claims or cores harmed by the player

Behavior:

- more restoration language
- more exile contacts and printing-room reports
- negotiation can offer settlement or autonomy-style concessions
- sabotage focuses on logistics and propaganda

### Ideological Counterweight

Condition direction:

- player ideology is extreme or globally threatening
- several candidates are ideologically opposed

Behavior:

- public justification uses ideology
- propaganda and party-pressure decisions matter more
- final text requires historical rhetoric research before implementation

### Border Memory

Condition direction:

- player borders several candidates
- player recently took states, generated threat, or fought regional wars

Behavior:

- more border-arm roles
- border missions unlock sooner in Evolution II
- sabotage targets rail, forts, and supply hubs

### Merchant Channels

Condition direction:

- island player, overseas empire, or sea-connected pact

Behavior:

- fewer border-war routes
- more port, convoy, naval-base, and trade-route incidents
- Port Screen and Trace Arms Shipments become more important

### Double-Cross

Condition direction:

- player has high exposure and negotiation leverage
- at least one reluctant member exists

Behavior:

- a member can become an informant
- mishandling the informant accelerates reveal
- the informant does not automatically become a player ally or puppet

