# Event 32 specification, part 4: Evolutions

## Evolution structure

Event 32 uses five parallel mutation tracks.

The catalog numbers remain stable. Their unlock order follows campaign conditions and chaos tiers, so a later-numbered evolution may activate before an earlier-numbered one. This is intentional. The evolution number identifies the catalog track, not a mandatory sequence.

| Catalog evolution | Working track label | Minimum chaos tier | Main prerequisite |
| --- | --- | --- | --- |
| Evolution IV | Rogue Launch Commands | Gathering Storm | Event 32 fired once and at least one country has a vulnerable program |
| Evolution II | Unreliable Guidance | Rising Chaos | Event 32 fired once and global program strain exists |
| Evolution I | Saturation Arsenals | Chaos Tier | Event 32 fired at least once and a meaningful share of programs is operational |
| Evolution III | Special Warheads | Totalen Chaos | Event 32 fired once and at least one eligible payload owner exists |
| Evolution V | Automatic Retaliation | Late Totalen Chaos, at least `900` chaos | Event 32 fired once and at least two countries can support retaliation |

Each track has one global evolution unlock entry. Country-level adoption and incidents are ordinary progression inside that track.

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

No global daily or weekly scan is required. The implementation can evaluate pending tracks through:

- the Event 32 firing transaction
- chaos-tier change hooks
- bounded delayed evolution jobs created when a threshold is first met
- exact shared-system events that make a prerequisite true

Suggested base MTTH targets:

| Track | Base MTTH after eligibility |
| --- | --- |
| Rogue Launch Commands | about `120` days |
| Unreliable Guidance | about `105` days |
| Saturation Arsenals | about `90` days |
| Special Warheads | about `120` days |
| Automatic Retaliation | about `150` days |

The MTTH should shorten when the corresponding global pressure rises and lengthen when few programs can use the track.

When the first Event 32 firing occurs above an evolution threshold, the event may create a short delayed unlock job instead of waiting the full ordinary MTTH. The delay should still give the baseline setup time to finish and should avoid firing five evolution popups on the same day.

## Evolution logging

Use one distinct `type` value per track.

Recommended mapping:

| Track | Evolution type | Stage |
| --- | --- | --- |
| Saturation Arsenals | `missiles_evolution.saturation` | `1` |
| Unreliable Guidance | `missiles_evolution.unreliable_guidance` | `1` |
| Special Warheads | `missiles_evolution.special_warheads` | `1` |
| Rogue Launch Commands | `missiles_evolution.rogue_commands` | `1` |
| Automatic Retaliation | `missiles_evolution.automatic_retaliation` | `1` |

Each unlock is actorless because it changes the global Event 32 rules.

The evolution row direction should explain the visible change in missile warfare. It should not list hidden incident probabilities or reveal every rare outcome.

---

# Evolution I: Saturation Arsenals

## Design role

Saturation Arsenals turns limited missile programs into strategic stockpiles capable of sustained barrages.

The evolution changes reserve scale, site capacity, replenishment, range, cooldown, defense saturation, and AI aggression. It should feel like a genuine change in war planning.

## Global unlock conditions

Suggested conditions:

- current chaos tier is Chaos Tier or above
- Event 32 has fired at least once
- the evolution is enabled
- at least a meaningful share of valid program countries has normalized stage `2` or higher
- at least two countries are at war or one global conflict contains several program countries
- the evolution has not already been recorded

The share threshold should be dynamic and based on the current valid program pool. A fixed country count can be used as a floor.

## Immediate global effects

On unlock:

- increase the mature-program reserve multiplier
- raise the ordinary reserve cap
- unlock saturation barrage preparation
- permit one extra launch-site cap slot for countries that meet territory and industry requirements
- shorten replenishment cooldowns
- shorten launch cooldowns after readiness recovery
- extend reach at later technology stages
- increase defense-saturation effects
- activate saturation AI profiles
- create one global news item if the presentation review supports it
- record the evolution row

The unlock must not grant every country a maximum arsenal immediately. Countries receive an initial saturation package scaled by their current program and then build further reserves through Event 32 repeats and decisions.

## Country adoption

A country can adopt saturation doctrine when it has:

- normalized stage `2` or higher
- at least one active launch site
- sufficient industry
- minimum Command Control
- no active total program collapse

Adoption provides:

- saturation barrage action
- larger replenishment batches
- higher site capacity ceiling
- reserve-dispersal or rapid-reload decisions
- AI willingness to conduct repeated strikes
- a visible saturation-program status

A country can decline or delay adoption. It still receives larger repeat-event packages, but does not gain the most aggressive operation set until it commits.

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

Use no more than four spendable cost types.

A country with strong industry can replenish faster, but every replenishment must have a cap and cooldown. Event 32 repeat firings remain valuable.

## Range

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

Suggested conditions:

- current chaos tier is Rising Chaos or above
- Event 32 has fired at least once
- the evolution is enabled
- at least one of these global pressures is true:
  - several countries have low readiness
  - missile reserves have grown faster than site capacity
  - a meaningful number of launches has occurred
  - a large share of programs has advanced technology without maintenance investment
- the evolution has not already been recorded

## Immediate global effects

On unlock:

- activate the expanded guidance outcome table
- unlock guidance and maintenance actions
- add preparation risk breakdowns
- allow accidental neutral and self-target incidents
- allow mistaken-retaliation bridges
- add maintenance-backlog state to missile programs
- adjust AI to consider failure risk
- record one evolution row

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

Each action should change a visible risk statement or readiness result. Tiny generic modifiers are insufficient.

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

Suggested conditions:

- current chaos tier is Totalen Chaos or above
- Event 32 has fired at least once
- the evolution is enabled
- at least one valid missile country owns a supported unconventional payload technology and stockpile
- the evolution has not already been recorded

The global unlock can occur when only one country qualifies. Other countries gain delivery access later when they acquire a supported payload.

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

Each payload family has its own country-level integration state:

- unavailable
- eligible
- integrating
- operational
- suspended
- compromised

A country can integrate several payloads, but each has its own stockpile and consequence adapter.

Integration should require:

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

Countries should have a policy or posture that affects AI and command risk:

- prohibited
- retaliatory only
- military targets only
- unrestricted under war conditions
- emergency delegation
- rogue control

Final labels require localisation work.

The policy does not override stockpile, technology, target, or shared-system gates.

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

Suggested conditions:

- current chaos tier is Gathering Storm or above
- Event 32 has fired at least once
- the evolution is enabled
- at least one missile country has a vulnerable program
- the evolution has not already been recorded

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

Suggested conditions:

- global chaos is at least `900`
- no terminal `world_end` state is active
- Event 32 has fired at least once
- the evolution is enabled
- at least two countries have operational missile programs
- at least one pair is hostile, at war, or under severe strategic tension
- at least one country has enough reserve and surviving sites to retaliate
- the evolution has not already been recorded

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

The unlock does not force every country into automatic posture.

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

Suggested response windows:

| Posture | Response window |
| --- | --- |
| Off | no automatic countdown |
| Supervised | `7` days |
| Delegated | `4` to `5` days |
| Automatic | `2` to `3` days |

The exact duration can depend on readiness, warning quality, damage, and payload estimate.

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

- allowed only when new attribution evidence exists
- uses the exact selected-target flow
- cannot silently redirect to a random country

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

Suggested hard caps:

- generation cap `3`
- country cap `6`
- linked-incident cap `12`
- one response per country per root
- one active warning per country per root
- automatic missile cap per root derived from constants
- thermonuclear automatic response cap much lower than conventional

The implementation must prove that false warnings, wrong-state hits, and special payloads use the same root record.

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
