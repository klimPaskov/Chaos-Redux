# Event 067 Manual Scenario and World-End Branch

## Manual scenario identity

- Scenario name: Generalissimo's Coup
- Proposed scenario ID: `SCN-015`
- Owner event: `067`
- Core purpose: place the current player or another valid major country into a mature Generalissimo crisis without waiting for normal event selection, Chaos thresholds, or evolution pacing

The supplied scenario export ends at `SCN-014`, so `SCN-015` is the required proposed ID. The implementation must verify the authoritative workbook and runtime registry before registration. A collision is a blocker and must not be resolved by silently replacing another scenario.

## Scenario launch rules

The scenario is directly launchable from the Triggerable Scenarios window when:

- no world-end state is active
- a valid host can be selected
- no Event 067 or scenario-created Generalissimo crisis is already active
- the selected setup can create a viable result

The scenario must not require:

- Event 067 to have fired naturally
- a minimum Chaos value
- Evolution I, II, or III to be enabled
- a date gate
- a prior war
- a prior event history entry
- the world-end branch to be enabled

The launch effect uses a tightly scoped scenario flag to create the requested stage and then clears it.

## Scenario target

Priority order:

1. current player country when valid
2. explicitly selected scenario target if the existing scenario framework supports a country selector without a new event-owned window
3. one weighted valid major or player country

A current player country that is too small to sustain the requested civil-war type can use a non-war crisis type, but the immediate-war type remains unavailable until a viable host exists.

The launch button and confirmation text must use the same eligibility gate.

## Scenario types

The scenario uses four type options. The names below are working labels except for the accepted scenario name.

### Favored Commander

The Generalissimo appears with Evolution I behavior active and an established service record.

The host begins with:

- visible Influence
- Theater or National Field Command
- an early demand
- a modest officer network
- no immediate final ultimatum

This type gives the player the longest crisis-management experience.

### State Within the State

The Generalissimo begins with Evolutions I and II behavior active.

The host begins with:

- medium or high Influence according to intensity
- National Field Command or Supreme Command
- officer, industry, and regional-command support
- several accepted historical concessions recorded by setup
- immediate access to counterweights and removal preparation
- no instant revolt unless the player chooses a failed coercive removal

### The Ultimatum

The Generalissimo begins as a mature Evolution III crisis.

The host begins with:

- high Influence
- strong officer support
- a visible short countdown to the final demand
- enough time for one final preparation action when the intensity permits it

The player then receives submit, refuse, or final removal choices.

### Generalissimo's War

The scenario creates the junta civil war during setup.

The host begins with:

- one canonical Generalissimo
- an immediate dynamic junta side
- forces, stockpiles, commanders, and territory scaled by intensity
- active Generalissimo focus tree on the junta
- no normal evolution wait

The confirmation screen must state that launch starts a civil war immediately.

## Scenario intensity

Intensity changes Influence, network maturity, army share, stockpile access, territorial reach, commander support, and preparation time. It does not change the identity of the event.

### Low

- Influence target near the lower boundary of the selected type
- limited officer network
- small regional footprint
- junta army target near 25 to 35 percent for the immediate-war type
- one coherent command nucleus
- government retains strong counterweights
- longer preparation window before ultimatum

### Medium

- Influence in the middle of the selected type's range
- established officer network
- junta army target near 35 to 50 percent for the immediate-war type
- one strong nucleus and possible secondary military region
- balanced government and junta stockpiles
- ordinary preparation window

### High

- high Influence
- strong officer, industry, and security reach
- junta army target near 50 to 65 percent for the immediate-war type
- multiple command regions where geography supports them
- meaningful navy and air split when relevant
- short preparation window

### Maximum

- Influence near the final threshold
- mature network across all applicable institutions
- junta army target near 65 to 80 percent for the immediate-war type
- strongest safe connected territorial package
- large real stockpile share
- several commanders and service branches
- very short final preparation window

Maximum intensity does not set the world-end flag and does not start The Generalissimos' World.

## Scenario history behavior

The scenario:

- registers its own scenario launch state
- does not count as a normal random pacing event
- does not create a false natural Event 067 history row
- consumes the unique Event 067 character opportunity so the normal event cannot create a second Generalissimo later
- can record Event 067 evolution state only where needed for the scenario setup
- does not grant Chaos for evolution activation
- applies outcome-based Chaos only after real scenario consequences occur

## Scenario repeat and cleanup

A campaign can launch Generalissimo's Coup once.

The scenario launch state must clear after setup. The active Event 067 lifecycle then uses the same owner helpers as the normal event.

A failed setup must leave no partial character, no active crisis value, no duplicate country, no scenario lock, and no consumed Event 067 state.

## Scenario validation matrix

Each type must be tested at Low, Medium, High, and Maximum intensity.

Required comparisons include:

- Influence and hidden network scale in the correct order
- army and stockpile shares increase monotonically for immediate war
- territory remains coherent at every intensity
- one-state and invalid hosts are handled without an invalid civil war
- the current player remains the target when valid
- launch bypasses normal Chaos and evolution gates
- no world-end state is set
- no second Generalissimo can appear
- save and reload preserves the setup

## Public world-end identity

- Working registry identifier: `generalissimos_world`
- Accepted public scenario name: The Generalissimos' World
- Owner event: `067`
- Visibility: public Event Details row
- Toggle: independent persistent enable state
- Minimum Chaos: 1000

The world-end branch changes the international system into a struggle over military rule. It does not create one global country or one oversized civil war.

## World-end readiness

The branch becomes eligible when:

- global Chaos is at least 1000
- no world-end state is active
- the public branch is enabled
- Event 067 has fired naturally or Generalissimo's Coup has been launched
- the canonical Generalissimo remains active, rules a country, leads an unresolved junta, or has won and established a Generalissimo state
- a valid set of ordinary human countries remains for the international struggle

Successful permanent removal before a Generalissimo regime is established blocks normal readiness. Defeating his junta also blocks readiness after the government finishes the Event 067 resolution.

This gives removal and government victory a real terminal-prevention benefit.

## World-end launch contract

The launch must:

1. guard against an existing world-end state
2. set the shared world-end state
3. set the Event 067 world-end flag
4. set the matching super-event visibility
5. set the correct unique super-event audio ID
6. use the settings-aware sound helper
7. stop ordinary automatic event firing
8. initialize the world-end actor registries
9. preserve active Event 067 country and character ownership
10. queue bounded country response packets
11. open the world-end decision and focus extensions

The event system freeze begins after the branch has committed successfully.

## World-end opening

Military establishments across the world conclude that civilian governments can no longer manage the global crisis.

The opening does not force every country into the same result. Each eligible country receives a response based on its institutions, army, war situation, stability, government form, existing commanders, and foreign alignments.

## Eligible-country roster

The launch builds a bounded roster once and then uses registered actor arrays. It must not add a recurring whole-world daily, weekly, or monthly scan.

Normal eligibility should require:

- ordinary human government
- meaningful armed forces or military administration
- controlled territory
- valid leader and commander context
- no terminal event identity that cannot use normal politics

Special handling applies to:

- one-state countries
- countries already in civil war
- capitulated governments
- governments in exile
- subjects
- countries without a valid commander
- countries already under military rule

Actual nonhuman countries and incompatible special Chaos actors are excluded.

## Country response score

A hidden military-dominance score determines the response. The score is not shown as another public world meter.

Positive factors for military takeover:

- low stability
- active or losing war
- high army size relative to population
- high military factory share
- military or authoritarian government
- weak civilian institutions
- active Event 019 claimant commanders
- recent Event 131 mutiny when implemented
- Generalissimo foreign support
- high world tension and strategic isolation

Negative factors:

- high stability
- strong civilian command reforms
- active loyal reserve
- recent defeat of the Generalissimo
- strong faction guarantees
- high legitimacy of civilian government
- small military establishment
- incompatible special-country status

The score determines one of several outcomes. The probability auditor must test every outcome pool.

## Opening country outcomes

### Existing Military Government

A country already under genuine military rule can:

- align with the original Generalissimo
- form a rival officer bloc
- remain independent
- adopt a stronger emergency structure

It does not need a redundant civil war merely to qualify as a junta.

### Peaceful Officer Coup

A commander or officer council replaces the government without a territorial civil war.

This outcome suits:

- low-stability states
- military regimes changing leadership
- one-state countries
- countries where most of the armed forces coordinate on one side

The highest valid existing commander should become the military ruler where engine ownership permits it. The country receives a world-end military-government package that is weaker than the original Generalissimo's package.

### Split Command Civil War

The armed forces divide and a dynamic military-junta side forms.

This outcome suits:

- medium military-dominance score
- divided officer corps
- several viable territorial command regions
- meaningful armed forces on both sides

The split uses Event 067's dynamic civil-war principles without creating another canonical Generalissimo.

### Controlled Emergency Government

Civilian leaders grant the military emergency authority while retaining formal rule.

This can become:

- a bridge to civilian resistance
- a later peaceful coup
- a stable military-civilian coalition
- a member of the civilian bloc with restricted army politics

### Civilian Defiance

The government refuses military rule and secures loyal commands.

The country gains access to:

- civilian command missions
- loyal reserve decisions
- support for threatened legal governments
- anti-coup intelligence
- Civil Authority Compact membership

### Existing Generalissimo State

The original Generalissimo state becomes the main potential center of the military movement. It receives the world-end focus extension and leadership tools.

## Selection of foreign military rulers

World-end military governments should reuse valid existing commanders instead of generating many portrait-bearing fictional people.

Selection priorities:

- highest-skill available field marshal
- high-skill general with political or military leadership traits
- commander with current army responsibility
- commander already connected to an Event 019 claimant path
- service council when no single commander can be selected safely

The original Event 067 Generalissimo remains uniquely stronger and keeps the complete ruler trait family.

Foreign military rulers may receive one bounded Event 067-derived military-government trait. They do not receive all four Generalissimo traits automatically.

## World-end phases

### Phase I: Commands Break with the Governments

Country response packets fire over a short bounded opening period.

Player actions include:

- secure the legal chain of command
- accept an emergency council
- recognize or reject a foreign junta
- move arsenals and loyal units
- support a threatened ally

The phase ends when the initial country roster has resolved or entered a registered delayed state.

### Phase II: The Blocs Form

Military and civilian governments begin organizing.

Potential blocs:

- International Command under the original Generalissimo
- one or more rival regional military blocs
- Civil Authority Compact
- independent neutral military states
- revolutionary and underground resistance networks

No bloc forms from one isolated member.

### Phase III: The Officer Wars

The blocs use interventions, coups, guarantees, volunteers, limited wars, and client regimes to reshape the world.

The conflict should create:

- military governments supporting each other
- civilian governments defending threatened institutions
- rival generals competing for leadership
- intervention in unresolved civil wars
- officer defections
- resistance in occupied or client states
- faction and subject realignment

### Phase IV: The Military Order or Civilian Restoration

The terminal campaign continues until one broad order becomes dominant or the world remains divided among military blocs.

The shared world-end state remains active throughout. This phase does not need a second generic world-end trigger.

## International Command

The original Generalissimo can form International Command when:

- he rules a country
- at least three independent military governments are willing to join, or two members include another major
- member governments are not at war with each other
- his state has adequate Command Cohesion
- the world-end branch is active

### Goals

- protect aligned military governments
- coordinate staff and production
- spread military rule
- defeat the main civilian coalition
- prevent rival generalissimos from replacing the original leader

### Shared decisions

- send staff missions
- transfer equipment and fuel
- guarantee a threatened junta
- intervene in an officer civil war
- coordinate doctrine and planning
- recognize a client junta
- pressure a neutral military government
- expose a rival officer conspiracy

### Membership

Positive factors:

- military government
- ideological and strategic compatibility
- dependence on the original Generalissimo
- shared enemies
- successful staff missions

Negative factors:

- rival major status
- high national ambition
- existing faction leadership
- territorial conflict
- low relations
- fear of personal domination

### Failure states

- member exits
- rival leadership bloc
- failed intervention
- internal command dispute
- client junta collapse

International Command does not receive an automatic global faction simply because the world-end branch begins.

## Rival military blocs

A major or strong regional military government can refuse the original Generalissimo's leadership and form a rival command bloc.

Rival blocs need:

- at least two meaningful members
- a leader with military-rule status
- common strategic interests
- no active war between founding members

They can:

- support their own coups
- contest neutral juntas
- fight International Command
- negotiate temporary anti-civilian cooperation
- fragment after leadership disputes

This prevents the world-end campaign from becoming one-sided automatically.

## Civil Authority Compact

The civilian bloc can form when:

- at least three independent civilian governments remain
- at least one is a major or regional power
- members are not at war with each other
- they recognize the military-rule crisis
- they have enough legal or military coordination to cooperate

### Goals

- protect legal governments
- share anti-coup intelligence
- support government sides in civil wars
- restore civilian control in defeated juntas
- resist International Command

### Shared decisions

- send loyal officer missions
- provide equipment to legal governments
- evacuate threatened officials
- coordinate sanctions
- support underground civilian networks
- guarantee command centers
- recognize restored governments

### Tradeoffs

Members must commit equipment, intelligence, political authority, and military support. A weak member can still fall to a coup if allies do not act.

## Resistance movements

Resistance should arise through normal occupation, government defeat, and military-rule pressure. Event 067 does not need to create a new universal resistance country.

Possible forms:

- state resistance modifiers
- underground civilian networks
- government-in-exile support
- loyal officer cells
- regional uprisings through existing mechanics

A resistance movement can help restore a government after a junta is defeated. It cannot erase population or create free divisions without manpower and equipment accounting.

## World-end decisions for military governments

### Support an Officer Coup

Targets a valid civilian or controlled-emergency government.

Costs can include:

- infantry and support equipment
- command power
- army experience
- intelligence exposure

Success depends on target military-dominance score, local commander support, foreign countermeasures, and distance.

Failure can expose the sponsor, strengthen civilian command, and create diplomatic consequences.

### Send a General Staff Mission

Improves a friendly junta's Cohesion, planning, and survival in exchange for equipment, officers, and political dependence.

### Guarantee the Barracks Government

Creates a military guarantee and intervention route. It cannot target an incompatible government or create a free offensive war.

### Coordinate Military Production

Creates bounded license, production, or resource support among aligned governments. It should not duplicate stockpiles.

### Remove a Rival Generalissimo

A high-risk political and intelligence action against a rival military leader. It must use the existing event or intelligence framework and cannot silently kill a grounded real leader without an authored outcome.

### Establish a Client Junta

Available after victory or intervention. The target remains a separate country and receives a military-government package. It does not receive the original Generalissimo's complete traits.

## World-end decisions for civilian governments

### Secure the Capital Command

Requires supplied loyal divisions in the capital region and improves resistance to a coup.

### Recall the Arsenals

Moves equipment and military administration away from unreliable commands at a real logistics cost.

### Form a Loyal Officer Council

Uses existing commanders who support civilian rule. It increases defense against coup coordination and may reduce army efficiency.

### Support a Legal Government

Sends equipment, volunteers, intelligence, or guarantees to a government side in an officer civil war.

### Restore Civilian Authority

Used after defeating a junta. It removes the military-government package through staged reform and does not grant instant stability.

## One-state and special geography handling

One-state countries cannot receive an invalid territorial civil war.

They can experience:

- peaceful officer coup
- controlled emergency government
- civilian defiance
- foreign-backed palace crisis

Archipelagic states use port and naval-command logic. Landlocked states use rail and headquarters logic.

## Countries already in civil war

A country already in civil war at world-end launch enters a delayed registered state.

Possible handling:

- one existing side becomes military-aligned
- a commander defects through the owner civil-war logic
- the country resolves after its current war ends

The world-end branch must not start several overlapping dynamic civil wars in the same country without a supported owner contract.

## Subjects

Subjects do not all become independent automatically.

A subject can:

- remain with its overlord
- support the overlord's legal government
- align with the overlord's junta
- use the crisis to seek greater autonomy
- join another military or civilian bloc after independence

Subject status and military dependence influence the result.

## Diplomacy and intervention limits

- No automatic annexation of friendly juntas.
- No free war goals against every civilian country.
- No instant faction membership without compatibility.
- No intervention without access, distance, or force capacity.
- No repeated coup farming against the same target.
- No automatic peace between rival military blocs.
- No guaranteed success for the original Generalissimo.

## World-end victory directions

### Generalissimo order

The original Generalissimo's order becomes dominant when it leads the strongest military bloc, controls or aligns several majors, defeats the main civilian coalition, and suppresses the strongest rival military center.

### Civilian restoration

The Civil Authority Compact succeeds when it protects or restores civilian governments across a decisive share of the world's major states and defeats the original Generalissimo's regime.

### Divided officer world

Several rival military blocs can survive without a single winner. The world-end campaign remains a fractured military order without forcing an artificial final annexation.

These are campaign-state directions and achievement or focus conditions. They do not need a second world-end flag.

## Public Event Details row

The world-end branch receives one independent Event Details row with:

- accepted scenario name
- premise direction
- terminal campaign-state direction
- enabled or disabled state
- availability status
- persistent checkbox

The row must not expose hidden readiness formulas, target scores, or future country outcomes.

Disabling this branch does not disable Event 067, the Generalissimo focus tree, the manual scenario, or another event's world-end branch.

## World-end super-event

The world-end launch uses a dedicated super-event with:

- unique slot
- unique image
- unique audio track and audio ID
- sourced quote
- researched button or cultural remark
- settings-aware playback
- Event 067 world-end flag

The accepted scenario name may serve as the super-event title if the final super-event research confirms it fits the slot and UI. Quote, remark, and audio remain blocked until researched and sourced.

## World-end Chaos handling

The branch begins at 1000 or higher Chaos, so further Chaos gains do not control readiness. Event-owned sources can still be recorded for history where they represent distinct consequences.

Potential one-time history sources include:

- first foreign peaceful officer coup caused by the world-end branch
- first split-command civil war
- formation of International Command
- formation of Civil Authority Compact as a small reversal
- defeat of the original Generalissimo as a major reversal

Generic wars, annexations, deaths, ideology changes, and faction changes remain owned by their shared Chaos sources and are not duplicated.

## World-end cleanup and persistence

Once the branch begins:

- ordinary automatic event firing remains stopped
- world-end actor registries process only registered countries
- dead or annexed actors are removed from active arrays
- invalid decisions disappear
- bloc membership and country response states survive save and reload
- the original Generalissimo character remains unique
- successful defeat of the original regime closes its focus and decision branches without clearing the shared world-end state

## World-end acceptance scenarios

Required tests include:

- branch does not trigger below 1000 Chaos
- branch does not trigger when disabled
- branch does not trigger after successful permanent removal
- branch can trigger when the Generalissimo rules after peaceful submission
- branch can trigger while an unresolved junta civil war exists when readiness permits it
- one-state countries avoid invalid civil wars
- stable civilian governments favor defiance
- unstable military-heavy states favor coup or split command
- existing military regimes can align or remain rival
- International Command requires several members
- Civil Authority Compact requires several members
- no recurring whole-world scan is added
- event system freeze occurs only after successful launch
- public Event Details toggle persists
- super-event image, text, quote, audio, and slot remain aligned
