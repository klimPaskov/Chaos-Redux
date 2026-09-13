# Gods of Africa decisions, missions, and UI specification

## Presentation choice

The default player-facing surface is an ordinary decision category with one compact attached display.

This choice keeps the system readable and follows the project hierarchy for decision presentation. Two public values, one active demand, and a small response set do not require a full separate mechanic window.

A dedicated scripted GUI remains a conditional implementation route for the African unifier's target-management surface. It should be accepted only after the normal category and selected-target pattern are tested against the live layout.

## Participant category

### Visibility

The category becomes visible after the country is registered as a participant.

It remains visible while:

- Gods of Africa is active
- the participant exists
- final settlement has not completed

A defiant participant keeps the category because it needs Wrath, Strength, punishment risk, and defensive actions. The ordinary demand area changes into a defiance status area.

### Header hierarchy

The category header should communicate four things in this order:

1. Gods of Africa Strength
2. Wrath of the Gods
3. current demand or relationship state
4. next useful action

The header should avoid paragraphs. Each meter receives a distinct icon, fill, band label, trend marker, and tooltip.

### Strength meter

Display requirements:

- `0 to 100` range
- current qualitative band
- upward, stable, or downward trend
- next threshold marker
- concise tooltip naming the most important current contributors
- practical consequence of current ceiling

The tooltip should explain what current Strength permits in broad terms. It should not list exact hidden punishment rolls.

### Wrath meter

Display requirements:

- `0 to 100` range
- current qualitative band
- upward, stable, or downward trend
- next threshold marker
- concise tooltip naming current visible reasons
- active floor if war, occupation, or defiance prevents further reduction

The tooltip can list recent visible actions such as a failed demand or returned territory. It should not expose hidden relationship weights.

### Relationship note

One short derived status line may appear below the meters. It is not a third value.

Examples of content direction:

- Africa remembers recent compliance
- occupation prevents reconciliation
- a prior agreement remains broken
- the current relationship is calm
- defiance has ended ordinary tribute

This line should use natural prose and should never become a numeric loyalty display.

## Active demand mission

### One mission rule

Only one ordinary demand mission can be active for a participant.

The mission title and description should dynamically identify:

- demand family
- requested resource, action, country, or state group
- amount
- deadline
- current payment progress if partial payment is supported
- whether substitution and extension are available

### Mission durations

Use varied durations based on action difficulty.

| Demand type | Normal duration direction |
| --- | --- |
| ceremonial or political recognition | `45 to 90` days |
| normal equipment or fuel shipment | `60 to 120` days |
| trains, convoys, aircraft, armor, industrial support | `90 to 180` days |
| emergency wartime aid | `30 to 60` days |
| territorial withdrawal or faction change | `60 to 180` days |

The implementation should centralize duration bands in script constants.

### Auto-completion

A goal that can be verified automatically should complete without a second player click.

Examples:

- required states transferred
- war ended
- access granted
- target alliance left
- a timed industrial commitment completed

Material stockpile payments can remain explicit clickable decisions because the player must choose when to debit the resource.

### Mission failure

Failure should:

- show the exact unmet public condition
- raise Wrath once
- close the current response actions
- begin one punishment review
- set the next demand cooldown

The failure effect must not rerun every day after expiry.

## Participant response phase

The normal phase exposes at most five primary actions.

### Action 1: fulfill

Purpose:

- pay or complete the demand

Possible costs:

- requested material
- one supporting cost if the transfer method requires it, such as convoys or political effort

The action should normally use one or two cost types. It must never exceed four.

Blocked tooltip:

- states the missing amount with the correct texticon
- states any non-cost requirement, such as route access
- names the protected-floor issue when the country cannot safely pay

### Action 2: propose substitute

Purpose:

- open a small offer selection from up to three valid alternatives

The parent category should not show every substitute at once. After clicking, replace the normal response set with a temporary substitute phase.

Substitute phase actions:

- offer candidate A
- offer candidate B
- offer candidate C
- return to demand

Only valid candidates appear. The action should show the full alternative amount before confirmation.

The candidate set is frozen for the demand contract so save and reload cannot reroll a better offer.

### Action 3: request extension

Purpose:

- gain more time for a difficult transfer

Possible cost packages:

- political effort
- partial upfront material
- small increase in final amount
- temporary diplomatic concession

No package may exceed four spendable costs.

The extension action should state:

- new deadline
- extra burden
- acceptance uncertainty if Africa can reject
- whether another extension will be blocked

### Action 4: refuse

Purpose:

- reject this demand while remaining in the recurring system

The confirmation should show:

- expected Wrath increase
- current Strength band
- current broad punishment ceiling
- that future demands remain possible

It should not reveal the exact punishment family or hidden probability.

### Action 5: defy

Purpose:

- permanently stop ordinary demand calls and enter open hostility

The action needs a confirmation window that states:

- ordinary demands stop
- Wrath gains a high floor
- normal friendship route closes
- punishments and African hostility can continue
- reconciliation is rare and costly

The action should not be placed next to fulfill with the same visual weight. It needs a distinct warning frame and a deliberate confirmation step.

## Phased visibility

### No active demand

Visible primary actions should normally be:

- review relationship details
- voluntary offering when a real African need is active
- prepare for likely demands if the participant is not defiant
- declare defiance when eligible

A phase should not show four empty or disabled response decisions when no demand exists.

### Active demand

Show the five response actions defined above, with invalid actions hidden or clearly disabled.

### Negotiation phase

Show up to three substitute choices and one return action.

### Defiance phase

Replace demand actions with a threat-response set chosen from the current risk.

Possible actions:

- harden transport nodes
- protect strategic stockpiles
- expand counterintelligence
- organize disaster reserves
- seek foreign guarantees

Only three to five actions should be visible. The exact set should react to current Strength, Wrath, recent punishment family, war, and country capacity.

### Reconciliation phase

Show:

- public prerequisites
- reparations or aid package
- territorial and war requirements
- timed reconciliation mission
- withdrawal action if the player abandons the attempt

## Defensive decisions for defiant countries

### Harden transport nodes

Story role:

- guard rail hubs, ports, supply hubs, and infrastructure against sabotage or disaster

Requirements:

- named strategic states chosen from current supply and industrial importance

Costs may include:

- civilian factory commitment
- trains
- support equipment
- command power within project limits

Effects:

- reduce valid rail and supply punishment impact
- create a timed protection state
- tie up real capacity

### Secure strategic stockpiles

Story role:

- disperse equipment and fuel reserves

Costs may include:

- trucks
- trains
- civilian factory burden
- temporary production penalty

Effects:

- reduce stockpile-loss punishment
- reduce substitute flexibility while stores are dispersed

### Expand counterintelligence

Story role:

- target African networks and false divine claims

Costs may include:

- political power
- command power
- intelligence resources where valid
- temporary diplomatic exposure

Effects:

- reduce sabotage chance
- raise discovery chance for attributable action
- risk increasing Wrath if exposed

### Organize disaster reserves

Story role:

- prepare emergency transport, relief, and repair capacity

Costs may include:

- convoys
- trains
- fuel
- civilian factories

Effects:

- improve Event 013 mitigation or aftermath when the owner API supports it
- reduce famine and migration pressure after a disaster

### Seek foreign guarantees

Story role:

- build an anti-African diplomatic shield

Requirements:

- valid foreign partners
- no direct contradiction with current faction status

Effects:

- improve external support
- make direct military retaliation costlier for Africa
- possibly provoke Africa if the partner is a current enemy

## Voluntary aid

### Visibility

Voluntary aid appears only when Africa has a registered major need.

Valid incidents:

- major war
- severe disaster
- famine
- migration crisis
- transport collapse
- final continental offensive

### Offer set

Show no more than three valid offers based on participant capacity and African need.

Examples:

- land equipment shipment
- fuel and transport package
- industrial reconstruction commitment
- military assistance
- diplomatic support

Each offer requires a meaningful capacity-scaled contribution. Token payments are excluded.

### Cooldown

A participant receives hidden relationship credit once per incident family or threshold. Repeating the same small offer cannot farm standing.

## Africa-side category

### Audience

Visible only to the African unifier.

### Header

Show:

- Gods of Africa Strength
- current doctrine route
- current continental priority
- number of active participant demands
- one concise summary of compliance and defiance

The category should not show a full numeric ledger for every participant.

### Target selector

Use one selected-target flow.

Default phase:

- select participant
- change continental priority
- view grouped tribute report
- review urgent offenders
- review reliable partners

After selecting a participant, show only valid target actions.

### Selected participant summary

Show:

- country name and flag
- Wrath band
- active demand state
- current visible offenses
- broad cooperation history
- defiance state
- valid Africa-side actions

Do not show the hidden final friendship score.

### Africa-side actions

#### Grant leniency

Use when:

- demand is active
- target has a valid hardship or cooperative record
- no irreversible punishment has committed

Effects:

- reduce amount, extend time, or accept a substitute
- lower immediate material gain
- improve hidden long-term standing

#### Mark priority offender

Use when:

- target has a proven offense
- priority-offender cap is not reached

Effects:

- raises target selection weight
- unlocks route-specific pressure
- never raises punishment ceiling above Strength

#### Protect partner

Use when:

- target qualifies through hidden cooperation history
- Africa has real capacity

Effects:

- opens a bounded aid package
- consumes African resources
- improves alliance and final settlement potential

#### Public pardon

Use when:

- war or occupation floor has ended
- reconciliation or settlement conditions are complete

Effects:

- clears temporary Wrath floor
- reduces Wrath
- preserves permanent history marks

#### Escalate proven offense

Use when:

- current offense qualifies
- no punishment job is already committed

Effects:

- triggers immediate evaluation
- obeys all normal tier and cooldown gates

### Africa AI access

AI Africa evaluates every valid participant without using the human target selector. The selector is presentation only.

## Costs and texticons

Every spendable cost uses compact icon-first localisation.

The implementation should use the project's normal texticons and add a custom texticon only when a real custom spendable value is accepted.

Requirements such as state control, war status, route access, and target validity remain separate from costs.

No action may hide a fifth cost in its effect or confirmation.

## Tooltips

### Meter tooltip

Target length:

- two to four short lines for normal state
- one additional line for a current floor or extreme threshold

### Demand tooltip

It should explain:

- requested amount or action
- deadline
- capacity basis in broad terms
- visible consequence of compliance
- visible risk of refusal

### Blocked tooltip

It should name the exact blocker:

- missing material amount
- unavailable transfer route
- active war replacing ordinary demands
- extension already used
- substitute set unavailable
- invalid African unifier
- system ending

Raw triggers should not appear.

## Category picture

The category picture is presentation only.

It should contain:

- one coherent fictional continental institution
- a central object or chamber that can plausibly issue demands
- visual change between calm and hostile state only if the consumer supports variants

It should not contain:

- fake buttons
- fake meters
- readable generated text
- a map used as the entire subject
- a collage of unrelated sacred objects
- real religious symbols merged into a single emblem

## Optional compact attached display

A compact attached display may provide:

- two meter bars
- two band labels
- one active-demand status icon
- one warning frame at extreme Wrath

It should not become a second action panel.

## Dedicated GUI acceptance gate

A full Event 012 window is justified only when all of these are proven:

- the Africa-side selected-target category cannot remain readable
- the window gives functional target management
- the two public values remain clear
- no extra public meter is introduced
- AI has equivalent actions
- every click has an owner effect and trigger
- the event UI worker receives exact files, states, resolutions, assets, and handoff path
- pre-change and post-change MCP GUI evidence is available

A full GUI should have no more than:

- one participant list
- one selected-participant card
- the two public meters
- one active demand card
- up to five current actions

## Decision and mission cleanup

Cleanup triggers include:

- African unifier invalid
- participant annexed
- system final settlement
- active demand resolved
- war replaces ordinary demand
- permanent defiance
- reconciliation abandoned
- selected target invalid
- demand generation changed

Cleanup must clear mission, decisions, selected-target flags, stored IDs, temporary offers, and stale event targets.

## AI and exploit review

The decision audit must test:

- exact cost debit once
- no click after mission resolution
- no repeated extension
- no substitute reroll
- no voluntary-aid farming
- no defiance reversal without reconciliation
- no stale selected target
- no AI choice with invalid cost or target
- no participant demand while ordinary calls are paused by war
- no Africa action above current capability
- no more than five visible primary actions in any phase
- no more than three active missions

## Localisation direction

Participant text should react to:

- demand family
- Wrath band
- Strength band
- doctrine route
- current war or peace
- occupation of African territory
- prior compliance or failure
- African emergency

Low Wrath can sound ceremonial, formal, or almost friendly. High Wrath should become specific and accusatory. It should name public offenses when known.

The tone should avoid generic administration language, false mystery through sealed reports, and direct claims that the text is a warning. The situation and consequence should communicate the threat.
