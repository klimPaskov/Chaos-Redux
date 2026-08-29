# Event 32 achievement implementation prompt

## Role and source files

Implement the complete Event 32 achievement set and coordinate its icons through `chaos-redux-event-assets`.

Read:

- `docs/specs/032_missiles_specs/032_missiles_spec_part_7_assets_text_and_achievements.md`
- `docs/specs/032_missiles_specs/032_missiles_asset_prompt.md`
- `docs/specs/032_missiles_specs/032_missiles_acceptance_criteria.md`
- `AGENTS.md`
- the existing Chaos Redux achievement registry and achievement documentation

The labels below are working labels. Write final player-facing localisation from the stated direction and the project writing rules.

## Shared rules

All eight achievements are visible and available to any ordinary playable country unless a row narrows eligibility.

Shared disqualifiers:

- Event 32 was launched through `SCN-015`
- force-trigger or debug bypass state remains active
- the achievement was already granted
- the country ceased to exist before the final receipt
- a required Event 32 evolution was disabled when the qualifying action occurred

Use stable event-owned receipts and the shared Deaths or incident ledgers. Do not infer achievement completion from current state when the route requires historical proof.

Centralize numeric thresholds in achievement or Event 32 script constants. The thresholds below define the intended difficulty and may be tuned only after a named balance review. Do not remove a condition merely because it is hard to track.

## Achievement 1

ID: `chaos_redux_032_exact_distance`

Working label direction: The Exact Distance.

Description direction: praise a command that proved long-range precision without widening the target set or using forbidden payloads.

Eligible countries: any ordinary country with an Event 32 program.

Unlock conditions:

- complete at least 12 conventional precision strikes
- strike 12 distinct strategic target states across at least four enemy countries
- every credited operation resolves on target or as limited success without neutral drift or self-strike
- use no command-strike or broad civilian-centered target profile in the qualifying run
- use no chemical, biological, nuclear, or thermonuclear missile payload
- Event 32 civilian deaths caused by the country remain below the centralized precision-restraint cap

Disqualifiers: any neutral accidental strike, any special payload launch, or any deliberate capital-centered strike after tracking begins.

Difficulty: very hard.

Why it is not trivial: it requires a long record of accurate operations across several wars while maintaining restraint.

Tracking: distinct target-state ledger, distinct target-country ledger, strike result receipts, target-profile receipts, special-payload history, and Event 32-attributed civilian deaths.

Icon direction: a guidance gyroscope and narrow targeting sight aligned over a railway junction, with no text.

## Achievement 2

ID: `chaos_redux_032_still_on_the_line`

Working label direction: Still on the Line.

Description direction: emphasize a dispersed launch network that remains operational after a direct attack.

Eligible countries: any ordinary country.

Unlock conditions:

- maintain three active launch states in three different strategic regions
- every site is hardened and secure
- Launch Readiness and Command Control are each at least 85
- receive a confirmed enemy missile strike that damages one launch state
- retain at least two operational sites immediately after the strike
- repair and return the damaged site to service within 180 days

Disqualifiers: losing all launch capacity, scuttling the damaged site, or using a scenario setup.

Difficulty: hard.

Tracking: site-region identities, hardening state, security state, confirmed incoming-strike receipt, post-strike operational count, repair deadline, and restored-site receipt.

Icon direction: a buried bunker under a broken incoming trail, with one intact command light represented symbolically and without readable text.

## Achievement 3

ID: `chaos_redux_032_break_the_chain`

Working label direction: Break the Chain.

Description direction: focus on stopping a widening retaliation sequence through verified command action.

Eligible countries: countries with Automatic Retaliation active.

Unlock conditions:

- become a participant in an Event 32 retaliation incident with causal depth of at least two
- the incident contains at least four distinct countries
- receive an actionable warning inside that incident
- resolve the warning through verification, delay, or network severance
- launch no retaliatory missile from the player country during the incident
- the incident closes without a later Event 32 launch attributed to the player
- survive for 90 days after incident closure

Disqualifiers: accepting automatic launch, redirecting the response into a third party, or causing a special-payload retaliation.

Difficulty: very hard.

Tracking: incident root, causal depth, unique participant ledger, warning receipt, emergency action, launch attribution, closure receipt, and survival timer.

Icon direction: a severed command cable between several incoming track marks, with a deliberate and controlled break.

## Achievement 4

ID: `chaos_redux_032_keys_returned`

Working label direction: The Keys Return.

Description direction: mark the recovery of a live rogue site before its command can launch.

Eligible countries: countries with Rogue Launch Commands active.

Unlock conditions:

- lose government control of an active launch site that contains reserve or an assigned prepared operation
- recover the site through loyal-force action or negotiated surrender
- prevent every unauthorized launch from that incident
- do not scuttle the site
- restore the site to secure status
- restore national Command Control to at least 75

Disqualifiers: site destruction, reserve duplication, an unauthorized launch, or foreign seizure before recovery.

Difficulty: hard.

Tracking: rogue-site incident identity, initial reserve or prepared-operation proof, chosen recovery route, launch-prevention receipt, restored security, and command threshold.

Icon direction: paired command keys above a reopened silo door, with one broken chain at the edge.

## Achievement 5

ID: `chaos_redux_032_no_second_sun`

Working label direction: No Second Sun.

Description direction: reward a country that survives nuclear missile use and finishes the war without answering in kind.

Eligible countries: countries with missile delivery for nuclear or thermonuclear payloads and at least one such payload in stockpile before the qualifying war ends.

Unlock conditions:

- receive a confirmed enemy nuclear or thermonuclear missile strike during a war
- remain an existing country
- finish that war through victory, enemy capitulation, or an accepted favorable peace state
- launch no nuclear or thermonuclear missile during the war
- retain an available nuclear or thermonuclear missile-delivery option until the war ends

Disqualifiers: any own nuclear or thermonuclear missile launch, loss of all qualifying stockpile before the enemy strike, or a terminal world-end state before war resolution.

Difficulty: extreme.

Tracking: prewar delivery capability, payload stockpile proof, confirmed incoming payload and attribution, own payload-use ledger, war identity, and final war result.

Icon direction: a sealed special-warhead cap beneath an unturned command key, with no mushroom cloud.

## Achievement 6

ID: `chaos_redux_032_empty_the_silos`

Working label direction: Empty the Silos.

Description direction: present a conventional counterforce campaign that removes a mature enemy missile network.

Eligible countries: any ordinary country at war with a major or another country whose Event 32 program meets the mature-program threshold.

Unlock conditions:

- the enemy begins the qualifying war with at least three active launch states
- use conventional counterforce operations to destroy, disable, capture, or force the scuttling of every enemy launch state
- use no chemical, biological, nuclear, or thermonuclear missile payload in the war
- launch no deliberate civilian-centered command strike
- win the war or force the enemy missile command to surrender through an accepted war-resolution path

Disqualifiers: an allied country removes more than half of the enemy sites without player credit, any own special payload, or the enemy rebuilding an operational site before war resolution.

Difficulty: very hard.

Tracking: frozen opening site manifest, site-resolution credit, counterforce operation receipts, payload history, target-profile history, rebuild state, and war result.

Icon direction: three dark silo silhouettes crossed by one precise targeting line, without an explosion cloud.

## Achievement 7

ID: `chaos_redux_032_sky_full_of_steel`

Working label direction: A Sky Full of Steel.

Description direction: recognize a large conventional saturation campaign that remains under national control.

Eligible countries: countries with Saturation Arsenals active.

Unlock conditions:

- complete five saturation operations in one war
- strike at least ten distinct enemy strategic states
- destroy or heavily damage the centralized required total of strategic building levels
- use only conventional payloads
- cause no neutral accidental strike
- keep Command Control at or above 35 through the final qualifying launch
- win or secure favorable peace within 365 days of the first qualifying saturation operation

Disqualifiers: special payload use, neutral drift, a rogue launch credited to the country, or loss of national command before the final operation.

Difficulty: very hard.

Tracking: war identity, operation count, distinct state ledger, strategic building damage credit, payload ledger, neutral incidents, command history, and campaign deadline.

Icon direction: five missile silhouettes in a controlled formation above an industrial horizon, with clear spacing and no text.

## Achievement 8

ID: `chaos_redux_032_long_reach`

Working label direction: The Long Reach.

Description direction: show a complete strategic command that can operate across several mission types during a major war.

Eligible countries: any ordinary country.

Unlock conditions:

- complete the full installed missile technology line through normalized Event 32 progression
- maintain at least three secure operational launch states in different strategic regions
- meet the mature-program reserve threshold
- maintain Launch Readiness and Command Control at 90 or higher for 180 consecutive days while at war with a major
- complete one conventional precision operation, one strategic barrage, and one counterforce operation during the same war
- retain at least two operational sites at the end of the 180-day period

Disqualifiers: any rogue-site loss during the timed period, a special-payload launch, or a scenario setup.

Difficulty: extreme.

Tracking: normalized technology completion, site regions, reserve threshold, continuous readiness and control timer, war identity, three operation receipts, and final site count.

Icon direction: three hardened sites connected beneath one long missile arc, rendered as a compact achievement emblem without map styling.

## Implementation and asset requirements

Implement the achievement definitions in the single Chaos Redux achievement registry. Add stable flags, variables, arrays, and receipts only where the existing Event 32 ledgers cannot prove the condition.

Keep tracking event-driven. Do not add a recurring whole-world scan. Use bounded launch, incident, site, war-resolution, and country-state hooks.

Write final localisation for title, description, eligibility, and locked state. Do not expose raw thresholds or hidden disqualifiers when the existing achievement UI does not normally reveal them.

Create the complete 64x64 achievement icon triplet for every final ID through the asset workflow. Keep filenames equal to the full achievement IDs.

Document each achievement, its tracking identifiers, reset and cleanup behavior, scenario disqualifier, and test cases. Add each achievement to the Event 32 acceptance and live-test coverage.

Do not reduce a difficult achievement to a one-time flag or current-state check. Report any condition that cannot be proved with the installed engine and propose a design-preserving solution for review.
