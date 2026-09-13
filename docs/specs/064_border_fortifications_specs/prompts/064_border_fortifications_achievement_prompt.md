# Achievement Prompt: Event 064 Border Fortifications

Implement the complete Event 064 achievement package defined under `docs/specs/064_border_fortifications_specs/`.

Read the full package, especially:

- `specs/064_border_fortifications_spec_part_5_text_assets_achievements_and_acceptance.md`
- `matrices/acceptance_criteria.md`
- `matrices/tuning_and_balance_framework.md`
- `prompts/064_border_fortifications_asset_prompt.md`

Follow `AGENTS.md`, current Chaos Redux achievement conventions, current event and debug-context conventions, the icon asset rules, and the completion-auditor definition. Use `fork_context=false` for spawned specialists.

All achievement titles below are working labels, not final localisation. Write final titles and descriptions from the direction in the spec. Do not expose internal variables or omit important disqualifiers from tooltips.

## Shared achievement rules

- Use natural Event 064 context for challenge arming.
- Suppress manual event, manual cluster, debug, console, observer, and test shortcuts.
- Use player-country scoped tracking.
- Store target countries, states, capitals, supply positions, dates, and challenge phase when required.
- Persist valid progress through save and reload.
- Clear failed, invalid, completed, annexed, and stale challenge state.
- Avoid recurring whole-world scans.
- Evaluate stored player targets at meaningful war, state-control, decision, event, or bounded player-only checkpoints.
- Prevent state release, ownership transfer, subject creation, faction joining, tag switching, and third-party capture shortcuts where mapped.
- Register every achievement in the current Chaos Redux achievement system.
- Wire final localisation, icons, detail text, eligibility state, completion state, and documentation.
- Produce deterministic test setup and evidence for arm, progress, fail, cleanup, save-load, and completion routes.
- Do not grant an achievement merely because Event 064 fired.

## Achievement 1: Continent of Concrete

### Working key

`chaosx_achievement_064_continent_of_concrete`

### Status

Visible, very hard.

### Eligible country state

Arm after a natural Event 064 wave when the player:

- is independent or has the accepted independent-war autonomy state
- has at least five distinct current land neighbors
- has at least eight controlled core border states
- has at least twelve qualifying direct frontier provinces
- has not used a manual or debug Event 064 route for the challenge wave
- has not completed the achievement

Store the eligible core border-state set and the relevant frontier coverage source at challenge start. The implementation must use a bounded and save-safe representation.

### Preparation phase

Before the war hold begins, require:

- at least eighty percent of the stored qualifying frontier provinces at total land-fort level five or higher
- at least four stored border states with state anti-air or radar
- Integrate the Line selected during the current or immediately prior valid response window

If exact province storage is unsafe, create a documented state-scoped equivalent that preserves the challenge. Do not quietly reduce the requirement to owning a few fortified states.

### War phase

Require:

- war with at least two stored land-neighbor countries at the same time
- uninterrupted control of every stored core border state for 180 days during the multi-front condition
- continued independence
- no new faction membership after war-phase start
- no release or transfer of stored states

After the hold, allow completion through victory, valid white peace, or another accepted peace that preserves the full stored line.

### Failures and disqualifiers

- any stored core border state lost during the hold
- stored state released or transferred
- player becomes a subject
- player joins a faction after the war phase begins
- manual or debug Event 064 challenge wave
- console or test context
- tag switch away from the challenged country
- target-neighbor requirement removed through an ownership manipulation before the hold is complete

### Tracking notes

Use explicit phases:

1. eligible and preparing
2. prepared and waiting for valid war
3. multi-front hold active
4. hold complete and awaiting valid peace if needed
5. completed or failed

The hold timer resets or fails according to the exact lost-state rule. Do not let the timer continue while fewer than two stored neighboring enemies remain at war.

### Icon direction

Use the completed icon described in the asset prompt, then create grey and not-eligible variants through the standard processor.

## Achievement 2: The Line Held

### Working key

`chaosx_achievement_064_the_line_held`

### Status

Visible, hard.

### Eligible country state

Arm when:

- player is a non-major
- a natural Event 064 wave affected at least one controlled core border state
- player begins a defensive war against a land neighbor
- attacker is at least twice as strong under one documented metric
- player is independent and factionless
- capital and threatened core border states can be stored safely

### Strength metric

Inspect current project AI and achievement helpers. Select one stable comparison, such as a bounded composite of fielded divisions, deployed manpower, total industry, and equipment, or an existing shared country-strength helper.

Document:

- exact metric
- comparison date
- whether allies or subjects count
- how civil wars are handled
- how missing data is handled

Do not change the metric during the challenge merely because the player begins winning.

### Completion routes

Complete after one of these valid outcomes:

- player wins the defensive war
- player reaches a peace that preserves the capital and every marked core border state
- player survives 365 days and reaches the accepted safe war-resolution state

Throughout the challenge require:

- capital held
- every marked core border state held
- player remains independent
- player remains outside factions
- no marked state is transferred or released

### Failures and disqualifiers

- capital lost
- marked core border state lost
- player becomes a subject
- player joins a faction
- player releases or transfers a marked state
- attacker disappears through an invalid third-party or scripted shortcut before the condition is met
- manual or debug Event 064 wave
- console, observer, or test context
- tag switch away from the player country

### Tracking notes

Store the attacker, comparison value, challenge start date, capital, marked states, and war id or accepted war identity. Handle white peace, attacker faction changes, and third-party intervention explicitly.

The player may receive incidental foreign help through normal war behavior, but faction joining remains disqualifying. Do not add an unprovable no-foreign-unit condition.

### Icon direction

Use the intact short line and broken assault-arrow composition from the asset prompt.

## Achievement 3: Breach the Unbreachable

### Working key

`chaosx_achievement_064_breach_the_unbreachable`

### Status

Visible, very hard.

### Eligible country state

Arm when:

- player selects Study the Breach
- player completes or validly starts Conduct Breach Exercises against one stored target
- target has a meaningful level-five-or-higher fortified frontier
- target line covers at least three relevant border states or an equivalent bounded province threshold
- target capital is stored
- a continuous land objective route from the frontier toward the capital can be defined
- context is natural and non-debug

### Fort-line proof

Inspect the current building query surface and choose a bounded proof. Preferred order:

1. verify qualifying fort levels in stored frontier states at challenge start
2. store a bounded frontier-state set and required average or minimum coverage
3. use an existing shared fort-density helper if one already has correct semantics

Do not arm against a target whose fortification comes only from one unrelated isolated province.

### Land-campaign sequence

The engine may not expose division order type reliably. Prove the breach through stored geographic objectives:

1. player takes the stored frontier objective
2. player controls a continuous land-connected chain of accepted objective states from that frontier
3. player captures the stored target capital within 180 days of offensive phase start
4. player is the country that captures and controls the capital

Build the objective chain from current map geography before the offensive phase. Keep it bounded and handle invalid map changes.

### Failures and disqualifiers

- target capital obtained through peace conference, release, subject transfer, scripted ownership transfer, or civil-war tag replacement
- another country captures the capital first
- target ceases to exist before the player's sequence completes
- stored land route becomes invalid and cannot be repaired under the accepted rule
- player uses a nuclear strike on the stored target when reliable detection exists
- manual or debug Event 064 context
- console, observer, or test context
- player tag switch

Do not claim detection of paratrooper or naval-invasion orders without reliable hooks. The stored continuous land sequence is the required proof.

### Tracking notes

Store target, target capital, fortified frontier set, route objectives, offensive start date, current route phase, nuclear-use disqualifier when available, and third-party control state.

The timer begins when the player enters the accepted offensive phase. Event 064 firing alone does not start it.

### Icon direction

Use the cracked bunker, engineer wedge, and capital-route composition from the asset prompt.

## Achievement 4: Last Redoubt

### Working key

`chaosx_achievement_064_last_redoubt`

### Status

Hidden or rare, extreme.

### Eligible country state

Arm when:

- global Chaos is at least 600
- Fortress World has concretely materialized for the player
- player owns at least ten core states or the final accepted anti-small-country minimum
- player controls a valid capital redoubt
- player controls a linked supply hub or major supply-route redoubt
- player is at war
- controlled core victory-point share falls below forty percent
- capital and supply redoubt remain held
- context is natural and non-debug

### Hold phase

Require uninterrupted control of the stored capital redoubt and linked supply position for 180 days without capitulation.

### Recovery phase

After the hold, require:

- at least eighty percent of owned core victory-point value controlled again
- immediate capital threat ended under a documented condition
- player never capitulated
- player remained independent

### Failures and disqualifiers

- capitulation
- capital lost
- linked supply redoubt lost during hold
- capital moved through a player or scripted shortcut after challenge start
- capital or supply state transferred or released
- player becomes a subject
- player tag switch
- manual or debug Event 064 context
- console, observer, or test context

### Victory-point metric

Use a documented current helper or a bounded sum over the player's stored core-state set. Define:

- numerator
- denominator
- treatment of occupied enemy cores
- treatment of newly gained cores
- treatment of released states
- check cadence

Avoid a world scan.

### Icon direction

Use the capital citadel, linked supply node, broken encirclement, and recovery cue from the asset prompt.

## Final localisation

Write final achievement text after tracking semantics are fixed.

Each tooltip should state:

- player eligibility
- natural Event 064 requirement
- main challenge
- time limit or hold duration
- major visible disqualifiers
- hidden status where appropriate

Do not expose debug-only implementation language. Do not use the working labels as final copy without localisation review.

## Documentation

Add every achievement to the permanent Event 064 overview and current achievement documentation. Record:

- final key
- final title
- visible or hidden status
- exact conditions
- disqualifiers
- tracking variables or flags
- icon paths and sprites
- test scenarios
- known engine limitation and accepted equivalent proof

## Required tests

For each achievement, prove:

- eligibility arms once
- ineligible country does not arm
- manual and debug context do not arm
- save and reload preserves progress
- every major disqualifier fails or clears the challenge
- state release and transfer cannot simplify the target set
- tag switching does not preserve an invalid challenge
- annexation cleans all state
- successful route completes once
- completed achievement does not rearm
- icons show correct completed, grey, and not-eligible states
- localisation is complete

Run specific edge tests:

- Continent of Concrete with border changes after preparation
- Continent of Concrete with one enemy leaving war before 180 days
- The Line Held with attacker joining a larger faction
- The Line Held with third-party intervention
- Breach the Unbreachable with target capital moved
- Breach the Unbreachable with third-party capital capture
- Last Redoubt with changing owned core set
- Last Redoubt with capital threatened but supply redoubt safe

## Completion rule

Do not claim the achievement package complete until all four achievements are registered, tracked, localised, documented, illustrated, tested, save-safe, exploit-resistant, and included in the final Event 064 completion audit. Report every unavailable hook, equivalent proof, simplification, or blocker directly.
