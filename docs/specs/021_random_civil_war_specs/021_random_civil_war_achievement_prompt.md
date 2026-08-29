# Achievement Prompt: Event 021 Random Civil War

Implement the complete Event 021 achievement set defined in `021_random_civil_war_spec_part_9_presentation_assets_achievements.md`.

Read the current achievement registry, existing Chaos Redux achievement patterns, `AGENTS.md`, `chaos-redux-events`, `chaos-redux-event-assets`, and the Event 021 specification.

Keep all Event 021 achievements inside the existing root achievement registry. Do not create a second achievement `unique_id`.

## Global rules

Every achievement needs:

- stable ID
- final title and description
- exact tracking flags, variables, arrays, or event targets
- eligibility
- disqualifiers
- completed icon
- grey icon
- not-eligible icon
- GFX wiring
- documentation
- event, settlement, country-origin, and cleanup hooks
- a test case
- no automatic or trivial unlock

Force-trigger, debug setup, and triggerable scenario launch normally disqualify all six achievements.

Use `chaosx_icon_artist` with `fork_context=false` for the icon triplets.

## Achievement set

### Hold the Center

ID: `021_random_civil_war_hold_the_center`

Eligible: player-controlled original affected government.

Unlock:

- win the Event 021 civil war
- retain the original or validated replacement capital through the decisive war
- State Authority never reaches Collapse after the opening
- no disqualifier

Track:

- opening capital
- valid replacement
- minimum authority
- government victory

### No State Left Behind

ID: `021_random_civil_war_no_state_left_behind`

Eligible: player-controlled original government or legitimate successor.

Unlock:

- resolve an Evolution I multi-front crisis
- recover or peacefully reintegrate every opening core state
- use no harsh settlement
- leave no partition
- no disqualifier

Track the opening core-state set, front count, settlement path, partition state, and final integration.

### A Flag of Our Own

ID: `021_random_civil_war_a_flag_of_our_own`

Eligible: player-controlled human Event 006 country created through Event 021.

Unlock:

- win recognized independence from the former host
- survive the immediate postwar period
- complete one valid Event 006 consolidation, recognition, formation, or formable milestone
- remain independent
- no disqualifier

Track Event 021 origin, former host, recognition, survival, package milestone, and independence.

### War Within a War

ID: `021_random_civil_war_war_within_a_war`

Eligible: player-controlled original government or legitimate successor.

Unlock:

- Event 021 begins while the country is fighting a qualifying major external war
- every Event 021 front is defeated or settled
- the country remains in existence
- the country does not capitulate to the external enemy during the civil war
- no disqualifier

Track external war at opening, internal fronts, external capitulation, final survival, and full internal resolution.

### The Terms Hold

ID: `021_random_civil_war_the_terms_hold`

Eligible: player-controlled signatory to a negotiated Event 021 settlement.

Unlock:

- conclude coalition, autonomy, recognition, or armistice terms
- keep the settlement intact for the defined long period
- fulfill public disarmament or constitutional obligations
- prevent Event 021 recurrence among the signatories
- no disqualifier

Track settlement type, signatories, obligations, violations, recurrence, and duration.

### Fractals of Sovereignty

ID: `021_random_civil_war_fractals_of_sovereignty`

Eligible: player-controlled human Event 006 country that existed before the nested crisis.

Unlock:

- suffer a nested Event 021 crisis
- preserve independent statehood
- resolve every nested front
- retain or recover the package homeland
- remain outside `is_actual_nonhuman_country`
- no disqualifier

Track Event 006 identity, Event 021 generation, nested fronts, homeland, final independence, and nonhuman exclusion.

## Acceptance

The achievement work is incomplete when:

- any route unlocks from a scenario or debug bypass
- tracking starts after the relevant opening state was lost
- a harsh settlement can satisfy No State Left Behind
- an Event 006 country formed by another origin satisfies A Flag of Our Own
- The Terms Hold ignores later violations
- nested generation is not proven for Fractals of Sovereignty
- icons are missing or reused as simple recolors from unrelated achievements
- localisation, docs, and tracking disagree
