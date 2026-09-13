# Event 40 Probability and AI Scenario Contract

## Evidence rule

Every probability-bearing Event 40 surface must be audited through the HOI4 MCP probability workflow.

Start with `hoi4.probability_inspect`. Use the smallest tool that answers the declared question. Use `hoi4.probability_compare` after any source change, with the same named scenarios used for the baseline.

The audit must distinguish:

- exact normalized probabilities
- bounded probabilities
- sampled simulation results
- score-only comparisons
- unresolved results caused by an incomplete candidate pool or external state

The source design defines intended ordering and refusal behavior. It does not invent exact percentages before the complete implementation pool exists.

## Surfaces requiring audit

- initial target selection
- later regional target selection
- British decision AI
- target decision AI
- incident selection
- Evolution I cell-family selection
- coup and revolt route selection
- Evolution II client contribution and refusal
- counter-bloc invitation and acceptance
- federation core selection
- federation outcome selection
- Lawrence-defection route
- Lawrence's Kingdom route
- focus-tree AI
- mission prioritization

## Initial target scenarios

### `PROB-L40-TARGET-CALM-BASELINE`

World state:

- Chaos below 200
- Britain stable and at peace
- three valid Arabian targets
- Target A has British access and moderate instability
- Target B has no access and high stability
- Target C has a strategic port but strong counterintelligence

Expected ordering:

1. Target A
2. Target C
3. Target B

The result can remain score-only if the complete picker contains undeclared external candidates.

### `PROB-L40-TARGET-PLAYER-VALID`

World state:

- one player Arabian target and two AI targets
- equal declared strategic conditions

Expected:

- the player target receives a normal nonzero score
- player control does not force selection
- no hidden major-country requirement removes the player minor

### `PROB-L40-TARGET-PREVIOUS-FAILURE`

World state:

- two otherwise similar targets
- Target A borders a country that dismantled the network
- Target B borders a British client

Expected:

- Target B has the higher British intervention score
- Target A receives preparedness that lowers its score or raises expected cost

### `PROB-L40-TARGET-BRITISH-OVEREXTENSION`

World state:

- Britain at major war
- severe convoy and equipment pressure
- several valid targets

Expected:

- all intervention scores fall
- remote targets fall more than accessible targets
- Britain can produce a valid no-action or pause result
- the model must not normalize an impossible pool into a forced intervention

## British decision scenarios

### `PROB-L40-BRIT-CALM-SECURE-ROUTE`

World state:

- Britain has equipment surplus, fuel, convoys, and secure access
- active target has strategic value
- Influence is contested

Expected ordering:

1. Authorize Gold and Arms
2. Secure the relevant route
3. Send Officer Cadres
4. High-exposure political penetration
5. Disavow mission

### `PROB-L40-BRIT-OVEREXTENDED-WORLD-WAR`

World state:

- Britain fights a major war
- low convoys and support equipment
- active target has moderate strategic value

Expected ordering:

1. Limited political or intelligence support
2. Pause or preserve network
3. Negotiate a narrow settlement
4. Large material commitment
5. Recovery operation without a plausible route

Large commitments should reach zero or near-zero validity when Britain cannot pay.

### `PROB-L40-BRIT-CAPTURED-LAWRENCE`

World state:

- Lawrence detained
- target controls routes
- Britain has moderate intelligence access

Expected ordering depends on capability:

- negotiation dominates when rescue odds are poor
- recovery operation rises with strong local contacts and a secure exit route
- disavowal rises when exposure is severe and Lawrence has low strategic value
- ordinary aid and officer decisions receive zero validity

## Target AI scenarios

### `PROB-L40-TARGET-WEAK-NO-AGENCY`

Profile:

- Fractured government
- low stability
- weak security
- foreign military threat
- no La Résistance agency

Expected ordering:

1. accept controlled or broad British aid
2. seek guarantees
3. improve loyal officer capacity
4. sponsor balance when another real patron exists
5. immediate detention or expulsion

The target should not choose a reckless confrontation merely because the decision has a high visible reward.

### `PROB-L40-TARGET-STRONG-AGENCY-NATIONALIST`

Profile:

- Counterintelligence state or anti-imperial challenger
- high stability
- strong agency or fallback security score
- secure routes

Expected ordering:

1. build counterintelligence file
2. audit the gold ledger
3. place mission under escort
4. turn a contact
5. broad access or client settlement

### `PROB-L40-TARGET-SOVEREIGN-PRAGMATIST`

Profile:

- moderate stability
- real foreign threat
- enough state capacity
- wants British aid without subordination

Expected ordering:

1. accept arms under national custody
2. open a liaison office
3. seek an independent treaty
4. balance sponsors if a real alternative exists
5. broad unrestricted access

### `PROB-L40-TARGET-DOUBLE-GAMER`

Profile:

- high intelligence capacity
- contested Influence
- turned contact available

Expected ordering:

1. feed controlled intelligence
2. secure national custody
3. collect further evidence
4. expose the network only when leverage is mature
5. become a voluntary client

### `PROB-L40-TARGET-DOMINANT-INFLUENCE`

Profile:

- Influence above 95
- divided officer corps
- target lacks loyal route control

Expected:

- safe negotiated settlement outranks reckless expulsion for most profiles
- anti-imperial AI can still confront Britain when it has a real resistance coalition
- invalid clean-dismantlement decisions receive zero score

## Evolution I scenarios

### `PROB-L40-E1-RESISTANT-FRAGMENTED`

World state:

- Evolution I active
- resistant target with divided officers
- British arms route open
- moderate cell strength

Expected incident ordering:

1. officer pressure or arms-cache incident
2. route sabotage
3. political demonstrations
4. full civil war

A civil war remains invalid until the territorial and military split is complete.

### `PROB-L40-E1-STRONG-SECURITY`

World state:

- strong target counterintelligence
- controlled ports and railways
- low Influence

Expected:

- detection and failed-cell incidents dominate
- coup weight approaches zero
- Britain prefers lower-exposure actions or withdrawal

### `PROB-L40-E1-EXPEL-HIGH-INFLUENCE`

World state:

- high Influence
- target expels Lawrence
- mature officer and smuggling cells

Expected ordering:

1. coordinated refusal or limited revolt
2. depot or route seizure
3. coup attempt when a valid coalition exists
4. no consequence

The result must still allow target suppression and partial outcomes.

## Evolution II scenarios

### `PROB-L40-E2-CLIENT-CORE`

World state:

- two loyal clients and one independent ally
- secure regional routes
- active target adjacent to a client

Expected:

- client contribution scores are positive
- the nearest capable client contributes more than a distant weak client
- independent ally can refuse without breaking its settlement
- active target faces stronger system pressure than in the baseline scenario

### `PROB-L40-E2-CLIENT-AUTONOMY`

World state:

- client has high autonomy pressure and low British promise credibility

Expected ordering:

1. demand compensation or autonomy
2. limited contribution
3. coordinate with other clients
4. unconditional support

### `PROB-L40-E2-COUNTER-BLOC`

World state:

- three independent governments
- shared concern over British encirclement
- no war among them

Expected:

- founding invitation and acceptance are positive
- a government dependent on Britain has lower acceptance
- a government at war with another invitee receives zero acceptance until conflict resolution

## Evolution III scenarios

### `PROB-L40-E3-FEDERATION-READY`

World state:

- at least three participants
- connected territory or valid transport
- functioning congress
- legitimate core
- no unresolved member war

Expected:

- federation action has a high positive score
- looser league remains a valid alternative for low authority or high mistrust
- immediate war against a refusing major neighbor is not the default

### `PROB-L40-E3-BRITISH-ARABIA`

World state:

- clients dominate
- Britain strong and reliable
- independent bloc weak

Expected ordering:

1. British Arabia
2. looser British-aligned compact
3. Independent Arab Federation
4. Lawrence's Kingdom

### `PROB-L40-E3-INDEPENDENT-FEDERATION`

World state:

- sovereign congress strong
- Britain overextended or accepts autonomy
- several independent participants

Expected ordering:

1. Independent Arab Federation
2. looser sovereign league
3. British Arabia
4. Lawrence's Kingdom unless personal conditions are also complete

### `PROB-L40-LAWRENCE-DEFECT-CANDIDATE`

World state:

- high trust
- independent charter
- British overreach
- target military and political success

Expected:

- defection becomes possible but remains less common than staying British or retiring
- without any one critical proof, defection returns to zero validity
- a source change to this route requires probability compare under the same scenario

### `PROB-L40-LAWRENCE-KINGDOM-RARE`

World state A:

- Chaos above 600
- federation ready
- personal conditions incomplete

Expected:

- kingdom route invalid

World state B:

- every accepted personal condition complete
- no stronger uncontested claimant
- rare AI strategy active

Expected:

- kingdom route becomes valid
- British and independent ordinary routes remain available when their conditions hold
- kingdom AI score remains much lower than ordinary valid federation routes

## Malta disruption scenario

### `PROB-L40-MALTA-ROUTE-DISRUPTED`

World state:

- Malta Crusaders controls key eastern Mediterranean access
- Britain retains a longer Red Sea route

Expected:

- Mediterranean supply actions become invalid or much weaker
- Red Sea route actions rise when physically valid
- Britain can abandon a low-value target
- Malta itself remains outside the target pool

## Focus-tree AI scenarios

### `PROB-L40-FOCUS-BRITISH-ORIGIN`

Origin:

- British Arabia
- strong Britain
- low Federal Authority

Expected:

- administration and command repair before expansion
- British compact route favored
- sovereign break route remains possible after broken promises or British weakness

### `PROB-L40-FOCUS-SOVEREIGN-ORIGIN`

Origin:

- Independent Arab Federation
- moderate Federal Authority
- several unintegrated members

Expected:

- congress, recognition, and integration favored
- British protectorate focuses invalid
- Lawrence personal focuses hidden unless the kingdom origin applies

### `PROB-L40-FOCUS-LAWRENCE-ORIGIN`

Origin:

- Lawrence's Kingdom
- Lawrence alive
- succession unresolved

Expected:

- succession and constitutional settlement outrank aggressive expansion
- after succession is solved, ordinary economy, command, diplomacy, and integration routes gain weight

## Required comparison report

The final probability audit should include a table with:

| Scenario | Surface | Baseline result type | Intended ordering | Source change | Comparison result | Unresolved external factors |
| --- | --- | --- | --- | --- | --- | --- |

No implementation should claim an exact chance when the complete candidate pool, cooldown state, external modifiers, and route validity were not supplied.
