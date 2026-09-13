# Event 050: The Great Embargo

## Part 8: Achievements, system interactions, cluster behavior, and acceptance

Achievement names are working labels. Final titles and descriptions require implementation-stage localisation and asset review.

## Achievement design

The achievement set should reward distinct mastery routes. It should not grant achievements for simply being selected or waiting for the duration to expire.

## Achievement 1 working label: Nothing Gets Through, Somehow

### Challenge

As an import-dependent target, end a severe embargo through coalition collapse without accepting a major concession and without starting Resource Seizure.

### Required proof

- target dependence classified as high or critical at opening
- Pressure reaches at least seventy
- crisis ends through coalition collapse
- no major concession accepted
- no resource ultimatum or war preparation completed
- at least one functioning replacement route or self-sufficiency project contributed to survival

### Disqualifiers

- target becomes invalid
- crisis ends through expiry without coalition collapse
- major concession accepted
- Resource Seizure starts
- force-trigger or debug completion where achievements are disabled

### Icon direction

A sealed world trade ring cracked by one narrow cargo route reaching an operating factory.

## Achievement 2 working label: The Coalition of the Unwilling

### Challenge

Cause at least three important participants to leave one embargo without war against them.

### Required proof

- three separate core enforcers or high-value participants leave
- departures come from concessions, commercial fatigue, exposure, diplomacy, or intermediary pressure
- no war between the target and those three participants during the crisis
- crisis resolves successfully or reaches the porous band after the third defection

### Disqualifiers

- counting minor background members with negligible contribution
- duplicate counting after a member leaves and rejoins
- participants removed only because they were annexed or ceased to exist

### Icon direction

Three official seals breaking away from a closing ring around a central cargo emblem.

## Achievement 3 working label: An Economy Under Siege

### Challenge

Remain at near-total isolation for a full year and survive through domestic adaptation.

### Required proof

- Pressure remains at or above eighty for 365 cumulative days within one crisis
- target maintains a defined minimum fuel and production condition
- at least two meaningful self-sufficiency project families complete
- crisis ends without capitulation
- final route is endurance, collapse of the coalition, or negotiated lifting after adaptation

### Disqualifiers

- Pressure time accumulated across separate firings
- survival achieved only through Resource Seizure
- target receives a scripted resource windfall that removes the challenge before the full period

### Icon direction

A lit factory and refinery operating inside a closed ring while stockpiles remain visible.

## Achievement 4 working label: Trade Without Permission

### Challenge

Under Evolution II, cooperate with at least two other embargoed countries and help resolve all connected crises without forming a permanent faction through Event 50.

### Required proof

- Evolution II active
- at least three active targets, including the player
- sanction-breaker cooperation established with two targets
- at least two complementary resource or route exchanges complete
- all three connected crises resolve
- no Event 50-created permanent faction

### Disqualifiers

- cooperation exists only as a flavor flag
- one target becomes invalid before meaningful exchange
- network state leaks after the last crisis closes

### Icon direction

Three isolated cargo emblems connected by a triangular barter route outside a broken market ring.

## Achievement 5 working label: Neutrality Has a Price

### Challenge

As a neutral intermediary under Evolution I, profit from trade with an embargoed target, resist secondary sanctions, and remain outside the coalition until the crisis ends.

### Required proof

- player is not the embargo target
- player begins outside the coalition
- player opens a functioning intermediary route
- coalition issues a secondary-sanction demand
- player continues trade or negotiates limited compliance without joining
- target crisis reaches a valid resolution
- intermediary receives the bounded commercial outcome

### Disqualifiers

- player joins the coalition
- route never reaches first delivery
- player becomes target of the same crisis ledger
- result is obtained through a hidden debug choice

### Icon direction

A neutral merchant vessel carrying cargo between two closed customs seals while a larger warning seal fails to stop it.

## Achievement implementation principles

- Each achievement uses one-time tracking and clear disqualifiers.
- Cumulative values belong to one crisis ID unless the achievement states otherwise.
- The achievement checks real outcomes and active routes.
- Every achievement needs localisation, completed icon, grey icon, not-eligible icon, documentation, and event-specific tracking cleanup.
- Achievement conditions should remain hidden or summarized according to the project achievement surface. They must not leak future evolution surprises in ordinary event text.

## Existing event interactions

## Event 029: Riches Found

A relevant persistent resource discovery can reduce the target's dependence and improve a Self-Sufficiency route. It should not lower Pressure by itself unless the new resource removes coalition leverage through a completed project or review.

If the riches produce political conflict or criminal competition, Smuggling Networks can become easier to establish and harder to control.

## Event 033: Acid Rain

Acid rain can damage transport, industry, extraction, and exposed routes. A target suffering both crises may face higher effective embargo damage because domestic substitution and intermediary delivery become less reliable.

Air Cleanliness and acid-rain consequences remain owned by Event 33. Event 50 should not add contamination for economic disruption.

## Event 034: Industrial Boom

An industrial boom increases demand for imported inputs and can make an embargo more painful. The boom's production strength can also fund rapid self-sufficiency projects.

High Overheating can increase the risk that severe embargo damage contributes to the boom's collapse. Event 50 should use the boom's public state or owner API when one exists, not duplicate its internal values.

## Event 035: Great Depression 2.0

A target already in depression has less construction capacity and weaker commercial resilience. It should favor concessions, intermediaries, and low-cost smuggling.

The embargo should not apply a second copy of the same depression penalty. Event 50 adds isolation pressure while Event 35 owns the depression lifecycle.

## Event 042: Equipment from Heavens

A military delivery can relieve equipment shortages and help pay some covert costs. It cannot solve oil, rubber, shipping, finance, or diplomatic isolation by itself.

The delivery should not reduce Pressure unless it changes a concrete coalition or target outcome.

## Shared Condemnation system

Public Condemnation can strengthen the opening justification, coalition recruitment, and hardliner behavior.

Event 50 is not a substitute for Condemnation's tiered sanctions. Condemnation sanctions arise from public unconventional warfare, exposed atrocities, cover-ups, and related sources. The Great Embargo can arise from broader diplomatic and economic causes.

When the same target is affected by both systems:

- shared native embargo behavior must not be duplicated
- event-owned Pressure remains temporary and crisis-specific
- Condemnation remains source-accounted and persistent according to its own rules
- participant penalties should use the stronger applicable state or a clearly combined bounded effect
- removing Event 50 cannot erase Condemnation sanctions

## Famine system

An embargo does not automatically create famine.

It can contribute to famine risk only when validated food-security conditions exist, such as import dependence, route disruption, reserve failure, inadequate local supply, and no relief corridor. The famine system owns Food Security, Food Reserves, Relief Access, mortality, and relief decisions.

Event 50 can:

- raise route difficulty for an already valid famine incident
- create a diplomatic choice around humanitarian relief
- exclude food or relief cargo from enforcement when participants agree
- worsen the target's ability to fund imports

It must not debit population or log famine deaths directly.

## Migration system

Economic isolation alone does not create a migration transaction.

Migration can arise later if famine, war, occupation, or validated forced movement creates displacement. The migration system owns cohorts, routes, reception, settlement, and forced-displacement deaths.

## Deaths system

Event 50 should not create direct death ticks from ordinary economic penalties.

Deaths from famine, war, bombing, occupation, or other validated causes use their owner systems. Resource Seizure can lead to war, whose casualties enter the shared Deaths tracker through normal sources.

## Air Cleanliness

The embargo does not directly change Air Cleanliness.

Domestic substitution projects can have flavor around low-grade fuels or emergency industry, but no contamination change should be added without a real owner-supported atmospheric source.

## Event clusters

Event 50 belongs to the Negative Economy cluster with Medium member severity.

When the cluster fires:

- the cluster counts as one global pacing event
- Event 50 still applies its own repeatable weight and cap behavior
- Event 50 records its own history and actor
- member target selection should avoid unnecessary concentration on one country
- a country already suffering Great Depression 2.0 should not automatically receive The Great Embargo unless the cluster's high-chaos concentration rules deliberately allow it
- skip reasons should identify active crisis, invalid target pool, conflict with another member, or missing required economic systems

The supplied cluster export is incomplete. The implementation must inspect the authoritative workbook and live cluster registry before assigning an ID, unlock tier, cluster type, participation weight, or member ordering.

## Chaos Meter interaction

Event-owned Chaos changes are limited to concrete crisis milestones. Evolution activation gives zero Chaos.

Generic sources remain owned by their systems:

- war
- peace
- annexation
- puppeting
- faction changes
- ideology changes
- deaths
- contamination
- nuclear use

This prevents one resource war from adding generic war Chaos and a second arbitrary Event 50 war bonus for the same outcome.

## Performance acceptance

The event should process only:

- registered active crisis targets
- stored coalition members for those crises
- selected neutral and negotiation targets
- bounded review candidates

It should not use an unrestricted daily or monthly all-country scan.

Evolution II must stay within the active-crisis cap. Closing one crisis must reduce the registered active set immediately.

## Core acceptance conditions

### Targeting

- valid player countries and majors can be selected
- excluded actors never receive the crisis
- an active target cannot be selected again
- target class behavior is measured in named probability scenarios
- Evolution II chooses distinct targets and respects the cap

### Pressure

- one public value uses the zero to one hundred range
- stage thresholds change visible consequences
- coalition quality affects Pressure
- target dependence affects damage without becoming a second meter
- collapsing Pressure requires confirmation or decisive action

### Decisions

- the category shows at most five primary actions and one active mission
- every action has meaningful cost, timing, target, risk, or commitment
- selected-target decisions hide irrelevant countries
- success, partial success, and failure are distinct
- permanent gains and repeatable rewards are bounded

### Coalition

- core enforcers matter more than minor member count
- human outside countries receive meaningful choices
- neutral intermediaries require practical routes
- participant defection changes Pressure according to contribution
- coalition reviews do not create popup spam

### Evolutions

- each evolution uses proper pacing and logs once
- disabled evolutions do not set state or block baseline resolution
- Evolution I supports secondary pressure and neutral resistance
- Evolution II supports separate overlapping ledgers
- sanction-breaker cooperation dissolves cleanly

### AI

- target response changes with dependence, strength, ideology, war state, and Pressure
- participant behavior changes with rivalry, alignment, commercial capacity, and cost
- AI refuses invalid or suicidal actions
- weighted logic receives baseline and comparison evidence

### Presentation

- target, convenor, stage, urgent exposure, and response access are clear
- no raw variables or unsupported bilateral trade claims appear
- report images and icons have final runtime assets
- Event Details, history, evolution logs, docs, and workbook wording agree

### Cleanup

- every crisis-owned variable, flag, array, mission, decision, modifier, and event target clears
- durable projects and concessions remain only when intended
- one crisis cleanup cannot erase another crisis under Evolution II
- a later firing begins with fresh crisis state

## Near-completion design review

The complete design has a clear promise, one manageable value, several viable strategies, outside-country play, two meaningful evolutions, AI requirements, assets, achievements, interactions, and bounded cleanup.

A later improvement pass is justified only when implementation or audit evidence reveals a concrete gap in play, clarity, balance, or integration.
