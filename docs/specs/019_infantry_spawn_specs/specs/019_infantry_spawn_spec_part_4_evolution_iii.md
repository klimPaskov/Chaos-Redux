# Event 19 Infantry Spawn
## Part 4: Evolution III, random divisions, and claimant generals

## Evolution III: Command Fracture

### Identity change

Evolution III ends automatic normal spawning as the default country experience. The event no longer drops another predictable generation of ordinary lots into every country. It opens a crisis system in which governments choose whether and how to call formations into existence.

Every requested division can have a completely random battalion count, combat composition, and support package. The country’s management record changes the probability distribution. A disciplined country can still receive bizarre formations, but it is more likely to receive something coherent. A badly managed country is more likely to receive divisions that are tiny, bloated, mutually incompatible, supply-heavy, or politically attached to a frightening general.

The event becomes a struggle over who controls the means of calling armies into existence.

## Entry conditions

Evolution III becomes possible through a combination of:

- global chaos reaching a high evolution range
- repeated use of the Evolution II request system
- high world totals of event formations
- several countries reaching extreme congestion
- recurring command incidents
- advanced formations operating outside normal technology systems
- unresolved claimant susceptibility created by earlier officer incidents

The world should have enough experience with the event that governments understand a formation can be requested, but still cannot control exactly what answers.

## Active-event evolution

A country with unresolved Evolution I or II generations receives the crisis layer immediately.

- ordinary automatic generation closes or pauses after current lots are registered
- existing lots become the starting pool for command ownership
- prior muster districts become potential claimant districts
- officer susceptibility records can generate the first claimant
- the random formation request system changes to full composition randomness
- existing advanced or narrow lots can become symbols of claimant authority
- the country receives the Muster Board interface and claimant tab

Existing divisions do not have their templates scrambled retroactively. The new randomness applies to future requested lots unless a specific reorganization choice deliberately subjects an old lot to random recomposition.

## Pre-fire evolved opening

A country first reached under Evolution III does not receive a normal automatic wave.

It receives:

- the crisis category and Muster Board
- a starting Muster Control value based on national context
- a starting Army Congestion value based on existing force and supply conditions
- one free but bounded initial formation draw or one emergency claimant offer, depending on war state
- a short tutorial incident direction that shows the first requested formation and its risks

A country at peace can decline the initial draw and keep the category dormant. A country in a desperate war receives strong pressure to use it.

## Full random template generator

### Design goal

The generator should create divisions that feel genuinely unpredictable while preserving engine safety, UI readability, and a minimum level of playability.

It must support all valid base vanilla land combat battalion families and support companies that the installed game version exposes, plus any explicitly registered mod additions. Examples include infantry, cavalry, bicycles, camels, marines, mountaineers, paratroopers, artillery, anti-tank, anti-air, tanks, amphibious tanks, mechanized, motorized, armored cars, flamethrower tanks, and other valid battalion families.

The examples are illustrative. Implementation must build the final pool from verified definitions and supported template syntax.

### Minimum safety rules

Every generated division must satisfy these rules:

- at least one combat battalion
- no invalid battalion or support token
- no duplicate support company in the same template when the engine forbids it
- no more support companies than valid support slots
- no template width or battalion count beyond an implementation-tested safe maximum
- no spawn-only Chaos unit in the ordinary Evolution III pool
- no equipment type whose definition is missing
- no template that crashes or becomes impossible to instantiate

Safety does not mean quality. A one-battalion formation is a valid catastrophic result.

### Combat battalion count

The intended combat battalion range is 1 to 25 for most ordinary random lots.

The distribution should have a weighted center and long tails:

- 1 to 3 battalions: rare but meaningful weak tail
- 4 to 8 battalions: common light formations
- 9 to 15 battalions: common full formations
- 16 to 20 battalions: uncommon heavy formations
- 21 to 25 battalions: rare bloated or powerful formations

Country size, request mode, control, congestion, and prior results shift the distribution.

The generator should not make every bad outcome a one-battalion unit. Poor management also creates overgrown and incompatible divisions.

### Combat family selection

Each battalion slot can draw from the eligible pool. The generator can use one of four composition logics.

#### Coherent logic

- one dominant family
- one compatible secondary family
- limited specialist additions
- sensible mobility and supply profile

#### Strained logic

- two or three families with partial compatibility
- one mismatched element
- moderate support burden

#### Absurd logic

- many unrelated families
- conflicting mobility and terrain roles
- unusual specialist concentration
- potentially high combat value with poor efficiency

#### Catastrophic logic

- extreme battalion count or extreme minimal count
- severe incompatibility
- excessive equipment families
- supply profile that is locally or nationally untenable
- strong claimant attachment chance

The chosen logic determines how slots are rolled, not the exact quality. A coherent division can still be weak. An absurd division can be frighteningly effective.

### Mobility compatibility

Mobility incompatibility is part of the event’s identity. A division may mix cavalry, bicycles, tanks, and foot infantry.

The generator should still track a mobility mismatch score. This score affects:

- movement and organization penalties through the event system
- retraining cost
- supply burden
- AI willingness to field or consolidate the lot
- whether the formation is labeled strained, absurd, or catastrophic

It should not silently prevent all strange combinations.

### Equipment family count

A template’s equipment diversity creates an integration burden.

The system records:

- number of distinct major equipment families
- technology-locked families
- fuel-dependent families
- support-equipment demand
- special or nonstandard equipment

This becomes part of the lot’s **compatibility burden** and influences costs and incidents.

### Support company randomization

A random division can receive zero to five valid support companies.

Support selection uses the same coherence logic:

- coherent lots favor support that fits the dominant combat role
- strained lots can receive one mismatched company
- absurd lots can receive an eclectic set
- catastrophic lots can receive expensive support on a tiny combat core or no support on a huge complex formation

Support companies that require unavailable equipment remain finite or understrength under the same technology-locked rules.

### Quality and absurdity are separate axes

Every generated lot receives two independent scores.

#### Material quality

Measures training, organization, equipment fill, and officer competence.

#### Structural coherence

Measures whether battalions, support, mobility, supply, and battlefield role fit together.

This creates four important experiences:

- high quality and high coherence: lucky elite result
- high quality and low coherence: powerful but bizarre result
- low quality and high coherence: sensible but understrength result
- low quality and low coherence: catastrophic result

The player should not assume that the strangest division is always the weakest.

## Outcome bands

The player-facing interface can summarize generated lots in four bands without exposing the exact random formula.

### Coherent

- clear role
- manageable equipment set
- reasonable battalion count
- low claimant attraction

### Strained

- usable with work
- one or more serious incompatibilities
- moderate integration burden

### Absurd

- unusual composition
- uncertain role
- high burden or narrow strength
- greater claimant interest

### Catastrophic

- severe weakness, bloat, incompatibility, or political danger
- immediate response required
- high revolt contribution if ignored

Final localisation should describe visible military characteristics rather than label a division as a joke.

## Management quality and probability

The distribution responds to national state.

Factors improving coherent outcomes:

- high Muster Control
- low Army Congestion
- completed training and standardization missions
- adequate equipment and supply
- no stacked muster history
- low claimant influence
- spacing requests over time

Factors worsening outcomes:

- low Muster Control
- high Army Congestion
- repeated requests in one generation
- active claimant demands
- severe war desperation
- unresolved advanced equipment debt
- failed audit or rail missions
- high Anomalous Saturation after Evolution IV

The system should use dynamic factors rather than one fixed coherent chance.

## Evolution III request families

The player chooses a request philosophy, not a template.

### Ask for Numbers

- biases toward more divisions or larger battalion count
- lower equipment quality
- higher congestion

### Ask for Discipline

- biases toward coherent structure and training
- higher army experience and officer cost
- fewer divisions

### Ask for Firepower

- biases toward artillery, armor, anti-tank, anti-air, and support
- high equipment diversity and supply burden

### Ask for Mobility

- biases toward cavalry, bicycles, motorized, mechanized, armored cars, camels, and valid air-mobile types
- fuel and terrain mismatch risk

### Ask for Anything

- widest pool and strongest tails
- lowest predictability
- strongest claimant and anomalous risk multipliers

Each request consumes resources before revealing the outcome.

## Lot disposition under full randomness

### Accept the Formation

Keeps the result and begins normal integration.

### Isolate the Lot

Prevents immediate deployment and claimant assignment. It costs supply, guards, and time.

### Break It Into Cadres

Dissolves the generated template into a smaller number of coherent training cadres. It sacrifices immediate divisions and returns only limited equipment value.

### Recombine the Battalions

Attempts a controlled reroll of composition using the same units. It is not a free reroll. It costs army experience, equipment loss, time, and control. Failure can worsen the result.

### Hand It to a Claimant

Assigns the lot to an active general for rapid readiness. It raises Claimant Influence and can create future loyalty.

### Supervised Dissolution

Removes the lot after a delay. It returns partial salvage and lowers congestion. Claimant-attached lots may resist.

## Claimant general system

### Purpose

The claimant system gives the event a political center. The generals are not cosmetic flavor. They provide military benefits, make demands, form networks, and can revolt with the units that follow them.

The design calls for 20 generic portraits that look frightening, altered, or possessed. These portraits form a reusable pool. The same campaign should normally show only a small subset in one country.

### Identity rules

Each one-person portrait must have:

- apparent gender presentation recorded in the asset manifest
- matching male or female leader metadata
- a matching regional personal-name pool
- an actual-looking era-appropriate personal name
- optional epithet, nickname, patronymic, or unsettling surname
- no generic office title as the person’s name

Recommended pool balance:

- 10 male-presenting portraits
- 10 female-presenting portraits

The implementation should use small regional name pools so the claimant’s identity fits the country while retaining Chaos Redux strangeness.

A country can also generate an institutional claimant such as a junta or committee only when the visual is a council or collective body. The requested 20 portraits are one-person portraits, so they use personal names.

### Visual direction

The portraits should be fictional HOI4-style upper-torso or bust portraits.

Shared visual traits:

- period military or improvised command clothing
- severe, uncanny, or possessed expression
- subtle supernatural disturbance rather than comedy
- distinct silhouettes and regional uniform cues
- subdued painterly treatment
- readable face at 156 by 210
- no readable text
- no gore as the primary identity

Variation can include:

- eyes reflecting an impossible light
- shadow that falls in the wrong direction
- ritual scars or strange medals
- unnaturally rigid posture
- smoke, dust, or dim barracks light
- old uniforms mixed with unexplained insignia

The package should not animate all 20 portraits. Static portraits provide better variety and keep the asset scope practical. The claimant crisis is communicated through animated UI warning assets instead.

## Claimant archetypes

The following are working design archetypes, not final localisation.

### Quartermaster Sovereign

Identity:

- controls depots, transport, and equipment distribution
- makes formations loyal by feeding and equipping them

Benefits:

- lowers equipment debt for assigned lots
- improves supply organization

Risks:

- captures depots and rail hubs during revolt
- demands a growing share of national stockpiles

### Field Prophet

Identity:

- claims supernatural insight into where formations will appear and how they should fight

Benefits:

- improves request quality or battlefield readiness
- can predict a broad result family

Risks:

- raises extremist or anomalous pressure
- demands independent recruitment and ideological authority

### Barracks Tribune

Identity:

- builds support among rank-and-file event troops
- presents the claimant as protector of soldiers against regular officers

Benefits:

- improves organization and reduces immediate mutiny
- can stabilize weak lots

Risks:

- forms soldier committees and parallel authority
- revolt can spread through many low-level formations

### Iron Saint

Identity:

- inspires fanatical discipline and sacrifice
- treats formations as a chosen host

Benefits:

- high organization and combat resilience
- rapid integration during crisis

Risks:

- demands political office, purges, or total command
- refusal can trigger a highly disciplined revolt

### Hollow Marshal

Identity:

- appears competent and calm but has no verifiable history
- builds an officer network rather than a mass following

Benefits:

- strong planning and command improvements
- better coherent-result chance

Risks:

- can take over the state through elite command capture
- may prefer a coup or one-state takeover over territorial revolt

The 20 portraits should cover these archetypes with regional variation rather than creating 20 mechanically unique systems.

## Claimant generation

A claimant can appear through:

- a random formation arriving with an unknown commander
- an existing event officer gaining prominence
- a command district being left unmanaged
- repeated use of Hand It to a Claimant
- high congestion and low control
- wartime emergency integration
- a claimant-specific flavor incident

A country normally tracks up to three active claimants. The system chooses one primary claimant and up to two rivals or subordinates.

Additional generated portraits can replace removed claimants or appear in later generations.

## Claimant demands

Claimant demands are timed choices with real consequences.

### Formal Appointment

The claimant seeks a recognized command.

Acceptance:

- improves assigned lots
- raises influence
- makes later removal harder

Refusal:

- lowers influence if the state is strong
- raises revolt risk if the claimant already controls troops

### Equipment Share

The claimant demands equipment, fuel, trains, or support stock.

Acceptance:

- improves claimant formations
- weakens national reserves

Refusal:

- can lower claimant readiness
- can trigger depot seizure attempts

### Autonomous District

The claimant seeks control of a muster district.

Acceptance:

- reduces immediate congestion
- creates a territorial revolt base

Refusal:

- requires adequate loyal forces and control

### Another Formation

The claimant demands that the country request more troops.

Acceptance:

- generates a claimant-attached lot
- raises congestion and influence

Refusal:

- can cause the claimant to make an unauthorized draw at high influence

### Political Seat

The claimant seeks a cabinet, council, military, or emergency-government role.

Acceptance:

- changes political modifiers and command efficiency
- opens takeover risk

Refusal:

- can split claimant and civilian authority

### Emergency Powers

The claimant seeks temporary national control during war or crisis.

Acceptance:

- creates a strong immediate military package
- starts a timer for restoration or permanent takeover

Refusal:

- can cause coup preparation or revolt

## Demand AI

Claimants choose demands based on archetype, country state, and current assets.

- Quartermaster Sovereigns prefer equipment and districts
- Field Prophets prefer more formations and political recognition
- Barracks Tribunes prefer formal appointment and soldier protections
- Iron Saints prefer emergency powers and political office
- Hollow Marshals prefer formal command and takeover opportunities

A claimant should not demand resources the country does not possess unless the demand is intentionally coercive and the failure outcome is meaningful.

## Claimant response strategies

### Accommodation

The state grants limited demands and uses the claimant’s military value.

Success requires clear boundaries, low congestion, and later integration.

### Co-option

The state gives a formal role while absorbing the claimant’s staff and units into regular institutions.

This is slower but can end the crisis peacefully.

### Counter-Command

The state builds loyal command networks, reassigns units, and isolates depots.

This costs army experience, equipment, and time. Failure can accelerate revolt.

### Public Discrediting

The state uses military failure, exposed fraud, or political opposition to lower influence.

It is more effective against Field Prophets and Hollow Marshals than a claimant whose troops are winning battles.

### Arrest or Removal

A high-risk action that requires loyal forces and control of the claimant’s district.

Success ends or replaces the claimant. Failure starts immediate revolt or coup.

### Surrender of Authority

The government accepts a claimant takeover.

This can avoid civil war and changes the country’s political package, leader, ideas, and AI. It should not automatically create a new tag.

## Revolt logic

### Units that revolt

A claimant revolt takes only units with a real loyalty link:

- formations assigned to the claimant
- lots created by the claimant’s demand
- units in an autonomous claimant district
- units that failed reassignment or integration
- a limited share of sympathetic event formations based on influence

The revolt must not randomly seize the entire ordinary national army.

Regular divisions can defect only through a separate, explicit effect tied to severe command collapse.

### Territorial base

The revolt seeks states where the claimant has:

- a command district
- loyal formations
- a depot or supply hub
- high local support or low central control
- an appropriate capital or headquarters location

The system should create a coherent civil-war region where possible rather than scattered isolated states.

### One-state country handling

A one-state country cannot be split safely.

Its claimant crisis resolves through one of these branches:

- takeover of the existing country
- failed coup and claimant removal
- temporary military occupation of government with a restoration mission
- exile or external seizure only when a valid foreign base exists

The system must not attempt an impossible zero-state civil war.

### Revolt strength

Revolt strength depends on:

- claimant influence
- number and quality of loyal event formations
- autonomous district size
- depot and rail control
- country stability
- war state
- Muster Control
- Army Congestion
- accepted demands
- active rival claimants

The revolt starts with the units it actually controls. It does not receive an unrelated free army.

### Revolt outcomes

- claimant defeated and crisis closed
- negotiated command settlement
- claimant military government wins
- civil war freezes into a regional breakaway
- claimant is replaced by a rival
- country collapses into several claimant zones only in a rare maximum-chaos or triggerable-scenario setup

## Rival claimant dynamics

Two or three claimants can compete.

Possible interactions:

- one claimant exposes another
- rival demands compete for the same district
- the government balances them
- one claimant joins the government against another
- rival revolts begin on different schedules
- one claimant absorbs the other’s formations after victory

The system should keep rival dynamics event-driven and readable. It should not create a permanent grand strategy minigame for every country.

## Evolution III UI transition

The decision category becomes a scripted Muster Board with four areas.

- Overview
- Formation Lots
- Command
- Request controls

The Command area appears only when a claimant exists. The Anomalous Registry area remains hidden until Evolution IV.

An animated warning border can pulse when revolt risk is critical. It requires real source frames, a static fallback, and frame-sheet wiring.

## Evolution III AI

AI chooses among five profiles.

### Professionalizer

- requests fewer formations
- spends resources on discipline and recombination
- resists autonomous claimants

### Wartime Opportunist

- requests aggressively while losing a war
- accepts a claimant temporarily
- attempts postwar co-option or removal

### Gambler

- uses Ask for Anything more often
- tolerates absurd formations
- high-chaos and unstable governments favor this profile

### Claimant Appeaser

- grants commands and resources
- avoids immediate revolt
- risks takeover

### Panic Demobilizer

- dissolves dangerous lots
- refuses most claimant demands
- can weaken itself badly during war

AI profile weights react to ideology, war, stability, military strength, supply, and claimant archetype.

## Evolution III acceptance criteria

Evolution III is satisfied when:

- normal automatic unit spawning stops by default
- the decision and scripted GUI crisis becomes the primary way to generate units
- battalion count and combat composition can be fully random within safe verified pools
- all eligible vanilla combat battalions and support companies can participate
- composition, quality, and coherence are separate concepts
- one-battalion and bloated divisions are possible but not the only bad outcomes
- the player cannot reroll freely
- poor management shifts the outcome distribution toward absurdity
- 20 fictional claimant portraits are planned with gender-matched regional name pools
- claimant demands have real military and political effects
- revolts use actual loyal event units
- one-state countries use takeover logic rather than invalid partition
- ordinary national armies are not stolen without explicit severe-collapse logic
- AI can request, manage, appease, resist, or remove claimants
