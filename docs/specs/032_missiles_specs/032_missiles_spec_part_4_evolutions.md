# Event 32 specification, part 4: Evolutions

## Evolution structure

Event 32 uses five parallel mutation tracks.
Implementation status: all five tracks, their gates, native pacing, logging, adoption and disabled-safe behaviour are `implemented` in source; runtime detail lives in `docs/events/032_missiles/systems/evolution_pacing.md`.

The catalog numbers remain stable.
Unlock order follows campaign conditions and chaos tiers, so a later-numbered evolution may activate before an earlier-numbered one.
The evolution number identifies the catalog track, not a sequence.

| Catalog evolution | Track | Minimum chaos | Implemented prerequisite |
| --- | --- | ---: | --- |
| Evolution IV | Rogue Launch Commands | `200` (Gathering Storm) | At least one vulnerable program: weak command, compromise, civil war, stability below `0.30`, or a damaged, captured or occupied site |
| Evolution II | Unreliable Guidance | `400` (Rising Chaos) | An operational program and real strain: two low-readiness programs, overstock beyond site capacity, three committed launches worldwide, or half the advanced programs without guidance investment |
| Evolution I | Saturation Arsenals | `600` (Chaos Tier) | At least two operational programs forming at least 40% of the live pool, and two programs at war |
| Evolution III | Special Warheads | `800` (Totalen Chaos) | One program owning both the technology and the physical stock of a supported payload |
| Evolution V | Automatic Retaliation | `900` | No world end, two operational programs, one hostile pair, and one response-capable program (advanced stage, a secure site, Command Control `75`, and the response reserve); the responder can be a third country |

Each track has one global evolution unlock entry.
An unlock grants access only; country adoption and incidents are ordinary progression inside the track.

An evolution disabled in Event Details:

- cannot set its global unlock flag
- cannot record an evolution row
- cannot expose its decisions
- cannot modify AI
- cannot create incidents belonging to that track
- cannot become a hidden prerequisite for baseline progression
- must leave conventional baseline play fully functional

## Evolution pacing

The normal evolution process is:

1. Event 32 has fired and initialized at least one valid program.
2. The current chaos tier meets the track threshold.
3. The track's world-state prerequisite is true.
4. The track is enabled.
5. A bounded evolution pulse evaluates the track.
6. The track uses its MTTH model.
7. The global unlock event fires.
8. Evolution context is set and recorded once.
9. Country adoption and incident logic become available.

No global daily or weekly scan is used.
Pressure is observed at finite boundaries: the firing transaction, program transactions, war and peace, state control, chaos-threshold crossings, and settled payload-stock transactions, coalesced into one `chaosx.nr32.192` delivery.

Implemented pacing (superseding the 2026-10-04 delayed-job model):

| Track | Native MTTH event | Base day scale |
| --- | --- | ---: |
| Rogue Launch Commands | `chaosx.nr32.201` | `120` |
| Unreliable Guidance | `chaosx.nr32.202` | `105` |
| Saturation Arsenals | `chaosx.nr32.203` | `90` |
| Special Warheads | `chaosx.nr32.204` | `120` |
| Automatic Retaliation | `chaosx.nr32.205` | `150` |

`common/mtth/032_missiles_evolution_mtth.txt` shortens a track by `0.5` under its corresponding pressure, lengthens it by `1.5` when few programs can use it, and applies `0.8` in the final chaos tier.
Each attempt rechecks the real prerequisites before recording; a rejected attempt does not consume the track.

When the first firing happens above several thresholds, those tracks use a short exception instead: `21` days plus `14` per eligible track in order, with at least seven days between commits, so five popups never land on one day.

## Evolution logging

Every track uses the canonical Event Logs identity: event `32`, type `constant:missiles_event.evolution_type` (`32`), and stage equal to the catalog number (I Saturation `1`, II Guidance `2`, III Special Warheads `3`, IV Rogue `4`, V Automatic Retaliation `5`).
The shared toggle flag is `events_log_disabled_evolution_32_32_<stage>`.
The logged tier is each track's minimum chaos tier.

Each unlock is actorless because it changes the global Event 32 rules.
The evolution row explains the visible change in missile warfare without listing hidden probabilities or rare outcomes.

---

# Evolution I: Saturation Arsenals

## Design role

Saturation Arsenals turns limited missile programs into strategic stockpiles capable of sustained barrages.

The evolution changes reserve scale, site capacity, replenishment, range, cooldown, defense saturation, and AI aggression. It should feel like a genuine change in war planning.

## Global unlock conditions

See the Evolution structure table: Chaos Tier, an operational share of at least 40% of the live pool with a two-program floor, and two programs at war.

## Immediate global effects

On unlock the track becomes available and the evolution row is recorded.
Nothing is granted to any country by the unlock itself; every saturation effect below reads the live enabled-and-adopted state.

## Country adoption

Adopt Saturation Doctrine is an explicit country decision (agent decisions, item 6).
It requires stage Guided or higher, an active site, more than `15` factories, Command Control at the operation minimum, Launch Readiness at the floor, and no rogue command.
It costs `25` command power, `140` support equipment and `700` fuel.

Adoption provides:

- the saturation barrage action
- the saturation reserve ceiling of `40`
- larger replenishment and shorter launch cooldowns
- AI willingness to conduct repeated strikes

A country can decline or delay adoption indefinitely.
Disabling the track suspends every saturation bonus without removing stock.

## Saturation barrage mechanics

A saturation barrage:

- reserves missiles from one or several sites
- uses a minimum barrage size
- can target one exact state or a bounded set of exact states
- reduces target defense effectiveness as barrage size rises
- increases the chance that at least one missile malfunctions under Unreliable Guidance
- causes high readiness loss
- increases detection and attribution confidence
- creates a long cooldown
- raises retaliation pressure

The operation should remain finite. It cannot automatically launch every missile in the country.

## Replenishment

Saturation replenishment should use stronger commitments.

Possible cost package:

- military factory output burden
- fuel
- support equipment
- manpower or civilian factory burden

The part 5 cost rules apply.
A country with strong industry can replenish faster, but every replenishment has a cap and cooldown, and repeat firings remain valuable.

## Range

Saturation range bonuses only matter once reach compares against real target distance (part 3, Reach, pending).

The evolution may increase reach through:

- temporary extended-range preparation
- later-stage missile systems
- larger fuel commitment
- reduced payload mass
- additional guidance penalty

Range increase should not allow every site to reach every state without checking the installed engine route.

## AI behavior

Saturation AI should:

- prefer logistics, industry, ports, airfields, capitals, and launch sites
- spend reserves when a strike supports an active offensive or defensive crisis
- keep a deterrent floor when facing another missile power
- avoid exhausting the entire reserve on low-value targets
- use larger barrages against heavily defended targets
- reduce barrage size when readiness is low
- avoid special payloads unless the Special Warheads track and payload policy allow them

## Failure and counterplay

Saturation creates risks:

- readiness collapse
- maintenance backlog
- more visible sites
- larger accident probability under Unreliable Guidance
- stronger retaliation
- higher fuel and equipment burden
- captured reserve value
- command-control pressure from several launch chains

The player can counter these risks through hardening, reserve dispersion, maintenance, command reform, and smaller strike packages.

## Track interactions

### With Unreliable Guidance

Large barrages increase the probability that at least one missile fails. The event should calculate barrage-level risk without rolling an unbounded random block for every missile.

### With Special Warheads

Special payload saturation is allowed only when the country owns enough physical payload and the shared CBRN systems can process the exact targets. Nuclear and thermonuclear saturation must be heavily constrained.

### With Rogue Launch Commands

A rogue site with a large local stockpile becomes more dangerous. Reserve dispersion reduces one-site seizure but creates more sites to secure.

### With Automatic Retaliation

Saturation retaliatory waves can exhaust reserve and generate several linked incidents. Chain caps still apply.

---

# Evolution II: Unreliable Guidance

## Design role

Missile production and deployment outpace guidance, maintenance, training, and command reliability.

The evolution expands the failure model. It creates wrong-state impacts, neutral incidents, self-strikes, launch-site accidents, breakups, and disputed attribution.

## Global unlock conditions

See the Evolution structure table: Rising Chaos, an operational program, and one of the four strain signals.

## Immediate global effects

On unlock:

- activate the expanded guidance outcome table
- unlock the aftermath actions (recalibration, debris investigation, site suspension)
- show the guidance grade's one-line risk statement before launch
- allow accidental neutral and self-target incidents
- allow mistaken-retaliation bridges
- adjust AI to consider failure risk
- record one evolution row

Maintenance backlog stays an internal input to the guidance grade, not a separate visible state.

The evolution does not make every launch unreliable. A well-maintained high-readiness program should remain dependable.

## Guidance pressure

Internal guidance pressure should rise from:

- low Launch Readiness
- damaged launch sites
- large barrage size
- extended range
- recent launch activity
- special payload integration
- obsolete normalized stage
- low Command Control
- maintenance backlog
- civil war
- captured or improvised sites

It should fall from:

- guidance program investment
- crew training
- maintenance
- later technology
- recent verified test data
- high readiness
- secure command
- shorter range
- smaller strike package

## Outcome families

### Failure before launch

- engine or fuel-system failure
- guidance package rejection
- command abort
- launch door or site failure
- payload integration failure

Result:

- launch does not occur
- some reserve or payload may be returned
- readiness falls
- site may be damaged
- public evidence depends on visibility

### Breakup after launch

- missile is destroyed or disintegrates
- debris may fall into a bounded state pool
- target receives little or no strategic damage
- attribution may remain uncertain

### Wrong object in target state

- intended state is hit
- target profile changes
- collateral damage rises
- intended strategic objective may survive

### Wrong state

- missile enters a bounded nearby state
- the state may belong to the victim, a belligerent partner, a neutral, or the actor
- the incident uses the actual state for all damage and consequence calls

### Neutral drift

- neutral country receives an accidental strike
- diplomatic incident and possible retaliation follow
- the launching country can admit, compensate, conceal, or blame another actor where supported

### Self-strike

- the actor's own state is hit
- launch site, nearby infrastructure, or another state in the verified return pool may suffer damage
- Command Control and readiness fall sharply

### Launch-site accident

- participating site is damaged
- local reserve can be destroyed
- crews and civilians may die
- special payload may create contamination or outbreak only through the owning shared system

## Barrage-level risk

Large barrages should use a bounded aggregate model.

Recommended approach:

1. calculate per-operation failure pressure
2. calculate a minimum number of successful launches from readiness and site capacity
3. roll a bounded number of failure events based on barrage bands
4. assign each failure to one outcome family
5. clamp failures so they cannot exceed missiles launched
6. resolve all damage through exact states

This avoids one expensive random chain per missile while preserving the danger of large barrages.

## Guidance investment

Country actions should include:

- recalibrate guidance packages
- replace maintenance components
- retrain launch crews
- inspect fuel and launch systems
- conduct a controlled test
- reduce extended-range strain
- suspend one damaged site

Each action must change the visible guidance grade, its risk statement, or readiness.
Tiny generic modifiers are insufficient.
Implemented actions: Improve Guidance and Maintenance, Emergency Guidance Recalibration, Investigate Debris and Suspend a Damaged Site (part 5).

## AI behavior

AI should reduce launch willingness when:

- failure risk is high
- the target is close to neutral states
- the country has low reserve
- Command Control is fragmented
- the selected payload is special
- the country cannot absorb a diplomatic incident

AI may still launch when:

- capital or supply collapse is imminent
- the enemy is close to victory
- a high-value target is exposed
- retaliation doctrine demands a response
- the AI profile accepts risk
- a rogue command incident bypasses normal government restraint

## Track interactions

### With Saturation Arsenals

Saturation adds aggregate failure pressure. Maintenance becomes a real strategic cost.

### With Special Warheads

A failed payload launch can create a site accident, dud, wrong-state release, or public evidence. The shared payload system decides whether release occurred.

### With Rogue Launch Commands

Rogue crews may have poor maintenance, false target data, or deliberately altered guidance.

### With Automatic Retaliation

Debris, wrong-state hits, and false tracks can trigger mistaken warnings. Verification becomes more valuable.

---

# Evolution III: Special Warheads

## Design role

Countries adapt missile systems to deliver unconventional payloads they already possess.

The evolution joins Event 32 to the existing chemical, biological, nuclear, thermonuclear, contamination, condemnation, and Deaths systems.

## Global unlock conditions

See the Evolution structure table: Totalen Chaos and one program that owns both the technology and physical stock of a supported payload.
The unlock can occur when only one country qualifies.
Other countries gain delivery access later when they acquire a supported payload.

## Immediate global effects

On unlock:

- enable payload-integration decisions for qualifying countries
- enable special-payload strike profiles
- enable special-payload targeting AI
- enable missile-specific CBRN incident records
- add special-payload readiness and command costs
- record one evolution row
- create a restrained global report or news item if the public evidence is sufficient

No payload is granted by the evolution.

## Payload integration record

Each payload family has one player-facing integration state: fitted or not fitted.
A fitted family is stored at a secure site; a family held for a prepared operation is shown on that operation, not as a separate state.
Loss of custody (capture, isolation, destruction) is resolved through the site and receipt records rather than a visible "suspended" or "compromised" label.

A country can integrate several payloads, but each has its own stockpile and consequence adapter.
Implemented as three decisions: Integrate Special Payload (`chaosx.nr32.30`), Select Special Payload (`.31`, conventional always available) and Set Special-Payload Policy (`.32`).

Integration requires:

- supported technology
- physical stockpile
- minimum missile technology stage
- active launch site
- minimum readiness
- minimum command control
- training or project commitment
- time

## Conventional high explosive

Conventional payload remains available from baseline. The evolution may unlock heavier conventional packages for mature missiles.

## Chemical

Chemical missile delivery uses:

- exact agent selection
- exact target state
- matching physical payload
- shared CBRN policy and protection checks
- shared exposure and contamination pipeline
- shared evidence, Condemnation, Air Cleanliness, and Deaths

The player should see the agent and expected broad effect before launch without seeing hidden outcome rolls.

## Biological

Biological delivery uses:

- exact weaponized agent or supported stockpile
- exact target state
- shared outbreak creation
- containment and spread rules
- shared evidence, Condemnation, Air Cleanliness, and Deaths

Event 32 does not own outbreak mutation or cure progression.

## Nuclear

Nuclear delivery uses:

- owned nuclear technology
- owned nuclear bomb stockpile
- exact target state or province accepted by the shared route
- nuclear effect, visual, fallout, contamination, condemnation, and deaths from the shared system

The delivery route should make Event 23 more strategically useful without changing Event 23's Soviet ownership and arsenal logic.

## Thermonuclear

Thermonuclear delivery requires the exact supported weapon and shared route. It uses the stronger thermonuclear consequence package.

## Special-payload policy

Countries have a policy that affects AI use, ordinary preparation and command risk:

- prohibited
- retaliation only
- military targets only
- unrestricted in war
- emergency delegation

Rogue control is not a selectable policy; it is the state a rogue incident forces onto a captured payload.
The policy does not override stockpile, technology, target, or shared-system gates.
README open question 3 proposes showing the policy to humans only once a Delegated or Automatic posture exists.

## Command burden

Special payloads reduce Command Control more than conventional launches because they require:

- additional custody
- more personnel
- separate authorization
- physical payload transfer
- heightened foreign intelligence pressure
- stronger retaliation readiness

Strong security can reduce the burden, but cannot remove the diplomatic consequences of actual use.

## AI behavior

AI special-payload use should consider:

- payload policy
- war state
- enemy special-payload use
- target value
- condemnation tier
- sanction exposure
- own survival
- faction commitments
- civilian death risk
- retaliation risk
- command control
- reliability
- stockpile scarcity
- ideology and strategy profile

AI must not use a special payload merely because it is available.

## Track interactions

### With Saturation Arsenals

Large special-payload salvos require enough physical payload and severe readiness cost. Thermonuclear saturation should be rare and heavily constrained.

### With Unreliable Guidance

Wrong-state and site-accident outcomes become much more dangerous. Release is recorded only if the shared system confirms it.

### With Rogue Launch Commands

Captured payloads and unauthorized integration can create severe incidents. A rogue site cannot invent a payload it does not physically possess.

### With Automatic Retaliation

A detected special-payload strike increases retaliation urgency and may shorten verification windows. Attribution uncertainty remains relevant.

---

# Evolution IV: Rogue Launch Commands

## Design role

Missile forces become institutions that governments can lose control over.

The evolution creates internal political and military incidents around sites, crews, codes, local commanders, civil-war sides, coups, occupation, and foreign intelligence.

## Global unlock conditions

See the Evolution structure table: Gathering Storm and at least one vulnerable program.

Vulnerability can include:

- low stability
- civil war
- capitulation pressure
- low Command Control
- occupied launch state
- damaged site
- several sites under emergency delegation
- foreign intelligence penetration
- recent coup or government replacement
- site inherited by a new country

## Immediate global effects

On unlock:

- activate command-pressure incidents
- unlock security, code rotation, inspection, scuttling, and recovery actions
- allow launch-site mutiny
- allow unauthorized launch
- allow site defection or local seizure
- allow foreign bribery and forged orders
- allow captured arsenals to create political leverage
- increase the strategic value of launch states
- record one evolution row

## Command-pressure model

Command pressure is an internal derived score.

Sources:

- low Command Control
- low stability
- civil war
- occupied or isolated site
- recent government change
- several launch sites
- large reserve
- special payload stockpile
- damaged communications
- emergency delegation
- foreign intelligence
- unpaid or neglected maintenance
- ideology conflict between government and military

Protective factors:

- secure codes
- high site security
- high Command Control
- stable government
- recent inspection
- loyal garrison
- dispersed custody
- allied monitoring where accepted
- scuttling readiness
- low local reserve

## Incident families

### Unauthorized launch preparation

A crew or commander begins a launch without national approval.

Player responses:

- isolate the site
- send loyal forces
- negotiate
- rotate or invalidate codes
- cut communications
- allow the launch under emergency doctrine
- scuttle the site when necessary

The incident should use a timed mission or short crisis window.

### Launch-site mutiny

The site stops accepting orders and controls a bounded local reserve.

Possible outcomes:

- peaceful surrender
- assault and recapture
- local commander defection
- launch during the confrontation
- site destruction
- foreign intervention
- civil-war side transfer

### Crew defection

Missile crews attempt to move codes, guidance data, or physical missiles to another country or civil-war side.

The transfer must prove an exact recipient and debit the original reserve once.

### Regional authority seizure

A governor, warlord, military district, or civil-war administration claims authority over the local site.

The incident is more likely when the central government lacks control of the state.

### Foreign bribery or intelligence penetration

A foreign country attempts to obtain:

- launch codes
- target data
- guidance sabotage
- false warning access
- site location
- crew loyalty
- payload custody

The foreign actor must have a valid intelligence or diplomatic route. Event 32 should not select a random unrelated country.

### Captured arsenal threat

A new controller threatens the former owner or nearby countries with a captured site.

The threat can be real, bluffing, or technically impossible depending on technology and command access.

### Rogue special-payload custody

A rogue command controls a real chemical, biological, nuclear, or thermonuclear payload.

This incident calls the owning CBRN system only if the payload is actually released.

## Incident frequency

The track should not create constant popup spam.

Use:

- one active rogue crisis per country by default
- incident cooldowns
- severity scoring
- hidden candidate queues
- a global active-incident cap
- human priority over minor AI flavor incidents
- AI silent resolution for low-severity cases
- reports for public consequences

The event should favor countries where the incident can change play.

## Civil-war bridge

When a civil war splits a missile country:

- both sides receive lower Command Control
- site records follow state control
- reserve divides by capacity and central command
- one or more sites may become contested
- Rogue Launch Commands receives a major pressure increase
- emergency decisions appear immediately
- no evolution is recorded again

Event 21 and other civil-war systems call this bridge.

## Occupation bridge

When an enemy captures a site:

- the site becomes compromised
- the new controller gains a resolution action
- the former owner loses capacity
- a local reserve share may be captured
- a rogue or foreign-control incident can start
- automatic retaliation ignores the site until control is restored or integrated

## AI behavior

AI should prioritize:

- securing a site that holds special payloads
- preventing an unauthorized launch
- scuttling an indefensible site
- recapturing a site near its capital
- negotiating when assault risks a special payload
- integrating a captured site only when it can support the cost
- avoiding aggressive launch posture at very low control

AI personality and government form may affect whether it purges, negotiates, centralizes, delegates, or scuttles.

## Track interactions

### With Saturation Arsenals

Larger reserves and more sites raise command pressure. Dispersion reduces one-site losses while creating more security obligations.

### With Unreliable Guidance

Rogue sites are more likely to use damaged systems, false target data, or poor maintenance.

### With Special Warheads

Physical custody becomes central. A rogue command cannot access a payload located elsewhere.

### With Automatic Retaliation

A rogue site may generate a false signal, ignore a stand-down order, or exploit delegated authority. High automation can turn a local command crisis into a wider exchange.

---

# Evolution V: Automatic Retaliation

## Design role

Countries build automated or semi-automated retaliation networks that can respond before attribution is fully confirmed.

The evolution creates warning events, retaliation postures, verification windows, false signals, chain reactions, emergency shutdown actions, and bounded broad exchanges.

## Global unlock conditions

See the Evolution structure table.
Outside actual war, a held war goal or active justification in either direction counts as a hostile pair; faction and subject ties never do, and negative opinion alone does not.

## Immediate global effects

On unlock:

- enable retaliation posture decisions
- enable shared warning processing
- enable verified, uncertain, false, and forged warning incidents
- enable retaliation chain records and caps
- enable emergency network actions
- enable AI posture selection
- connect qualifying missile and special-payload strikes to the warning helper
- record one evolution row

The unlock gives every program access to the warning network with posture Off.
Set Retaliation Posture is an explicit decision (`15` command power and `5` Launch Readiness, `70`-day cooldown), blocked during a warning, a committed retaliation, or a severed network; it opens `chaosx.nr32.40`.

## Retaliation postures

### Off

- no automatic preparation
- ordinary government decision required
- lowest false-response risk
- slowest response
- may reduce deterrence or AI confidence

### Supervised

- warning creates a player or AI response event
- launch requires confirmation
- longest verification window
- good balance between control and response

### Delegated

- command network prepares retaliation automatically
- player or AI can stop or redirect it during a shorter window
- higher survivability
- higher rogue and false-signal risk

### Automatic

- qualifying warning begins a short countdown
- network launches unless disabled, delayed, or invalidated
- fastest response
- highest false-warning and chain risk
- requires minimum readiness and command control to adopt
- can remain active after government disruption if the network survives

A country with fragmented Command Control cannot safely activate the strongest posture through ordinary policy. A rogue route may still force it.

## Warning classification

A warning record stores:

- source incident
- detected launch count
- predicted target
- likely actor
- attribution confidence
- payload estimate
- time to impact or response window
- corroborating channels
- conflicting channels
- false-signal indicators
- victim posture
- available response sites
- causal root and generation

Player-facing classifications can be:

- verified
- probable
- uncertain
- conflicting
- false

Final wording should avoid exposing exact hidden probabilities.

## Response window

Implemented response windows (`missiles_resolution`):

| Posture | Response window |
| --- | --- |
| Off | no automatic countdown |
| Supervised | `7` days |
| Delegated | `5` days |
| Automatic | `3` days |

Delay Retaliation adds `3` days once per warning, and a warning expires after `14` days.

The player should have enough time to understand the incident. A one-day surprise that can launch thermonuclear weapons would create poor gameplay.

## Emergency actions

### Verify the warning

- uses intelligence, radar, and command channels
- can raise or lower attribution confidence
- can expose a forged signal
- costs time and command capacity

### Delay retaliation

- extends the countdown once
- reduces readiness
- may weaken deterrence
- unavailable when the network is already past commitment

### Sever the network

- stops automatic launch
- sharply lowers readiness
- may disable several sites
- creates a repair or restoration mission

### Isolate one site

- removes a compromised site from the response
- preserves the rest of the network
- risks losing that site's reserve or command link

### Change target

`rejected` for this round (agent decisions, lead decision 5).
A response always targets the warning's attacker; verification that names a different actor resolves the warning instead of redirecting it.

### Restore control

- ends an emergency after the incident
- requires secure codes, repaired communication, and minimum Command Control

### Accept the retaliation

- allows the current prepared response to launch
- player sees broad expected consequence and attribution state
- hidden malfunction rolls remain hidden

## Retaliation package

A retaliatory launch should scale with:

- detected severity
- incoming missile count
- payload estimate
- posture
- reserve
- surviving site capacity
- command control
- doctrine
- causal generation
- chain cap

The package must leave a bounded reserve floor unless the country's survival is judged critical or the posture explicitly allows full release.

## False signals

False signals may originate from:

- warning-system failure
- incompatible or damaged systems
- forged foreign data
- rogue command
- debris
- guidance error
- simultaneous exercise or test
- communication loss
- captured site transmission
- third-party framing attempt

A false signal can produce:

- stand-down after verification
- diplomatic accusation
- readiness loss
- network shutdown
- mistaken retaliation
- attack on the wrong country
- entry of a neutral country into war

## Third-party interference

A foreign intelligence service may attempt to:

- forge launch evidence
- redirect attribution
- hide the real actor
- trigger a rival's automatic network
- delay verification
- alter target data

The actor must meet intelligence, access, and motive requirements. This cannot be a random global flavor roll.

The operation should carry severe discovery consequences.

## Chain reaction

When retaliation launches:

1. create a new linked incident
2. increment retaliation generation
3. mark the responding country as processed for the root
4. apply the strike through the ordinary operation pipeline
5. notify affected countries through the warning helper
6. stop when caps or invalid conditions are reached
7. close the root chain and write one summary

The chain cannot recurse directly inside one effect block.

## Chain caps

Part 3, Causal chain controls, owns the hard caps.
In addition, an automatic response never raises its payload above conventional unless the payload policy allows it, and thermonuclear automatic responses stay rarer than conventional ones.
False warnings, wrong-state hits, and special payloads use the same root record.

## AI behavior

AI posture selection should consider:

- current war
- enemy missile capability
- government stability
- Command Control
- readiness
- number of secure sites
- reserve
- recent attacks
- ideology and strategy
- condemnation
- special-payload policy
- faction commitments
- risk of decapitation
- intelligence quality

AI response behavior should:

- verify uncertain warnings when time permits
- launch against confirmed attackers
- avoid a full response to weak or conflicting evidence
- sever the network when control is lost
- preserve a reserve floor
- use special payloads only under its policy
- stop when the root chain cap is reached
- never select a dead or allied target

## Track interactions

### With Saturation Arsenals

Retaliation packages can be larger and faster. Reserve-floor logic and chain caps remain mandatory.

### With Unreliable Guidance

False warning and wrong-country risk rise. Verification and maintenance have more value.

### With Special Warheads

Payload estimate changes response urgency. A nuclear or thermonuclear warning can shorten the countdown, but does not guarantee a matching payload response.

### With Rogue Launch Commands

A compromised site may resist stand-down orders, generate forged signals, or launch under delegated authority.

## Shared terminal consequence connection

A broad nuclear or thermonuclear exchange may increase Air Contamination enough to satisfy the existing Fallout consequence route.

Event 32 does not set `world_end`, register a separate terminal branch, or bypass the Fallout owner's readiness gates. It only creates real strikes and calls the shared consequences.

---

# Cross-track behavior

## Combined pressure examples

### Saturation plus Unreliable Guidance

- large reserve
- frequent barrages
- aggregate malfunction risk
- maintenance becomes central
- neutral incidents become plausible

### Saturation plus Rogue Commands

- several sites
- dispersed reserve
- more seizure targets
- one mutiny cannot seize everything
- security cost rises

### Special Warheads plus Rogue Commands

- payload custody incidents
- captured weapons
- emergency scuttling
- high condemnation after release

### Unreliable Guidance plus Automatic Retaliation

- wrong-state strikes
- false tracks
- disputed attribution
- mistaken retaliation

### All five tracks

The system becomes a global strategic crisis with large arsenals, unreliable operations, unconventional delivery, contested command, and rapid retaliation.

The design must remain playable through:

- bounded incidents
- clear status
- emergency actions
- finite chain caps
- AI restraint conditions
- one active crisis per country by default
- phased decision visibility
- exact cleanup

## Evolution news and reports

A track should receive a global news item only when the change is visible enough to justify one.

Suggested presentation:

| Track | Presentation |
| --- | --- |
| Rogue Launch Commands | Global news only after a public unauthorized launch or several visible mutinies |
| Unreliable Guidance | One news item after debris or accidental cross-border strikes become public |
| Saturation Arsenals | Global news at unlock |
| Special Warheads | Global news after the first confirmed missile-delivered unconventional payload, not at secret integration |
| Automatic Retaliation | Global news at first public network activation or first chain incident |

The evolution log records the global unlock even when the public news is delayed.

## Evolution completion criteria

Every evolution is complete only when it has:

- eligibility and MTTH
- enable and disable behavior
- one global log entry
- country adoption or incident rules
- decisions and AI
- shared-system integration
- cleanup
- assets or reused assets
- player-facing text direction
- test scenarios
- no dependency on an unimplemented hidden shortcut
