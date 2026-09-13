# Event 049 Doomsday Achievement Implementation Prompt

## Role

Implement the full Event 049 achievement set, including tracking, unlock logic, disqualifiers, localisation, icon triplets, documentation, and event integration.

Read:

- `specs/049_doomsday_spec_part_12_achievements_and_acceptance.md`
- every Event 049 specification part that defines the relevant route
- `prompts/049_doomsday_asset_prompt.md`
- `quality/049_doomsday_acceptance_matrix.md`

Follow `AGENTS.md`, `chaos-redux-events`, `chaos-redux-event-assets`, and the existing project achievement pattern.

The IDs below are the proposed stable IDs. Confirm syntax and naming against the existing root achievement registry before implementation. Preserve one clear stable ID per achievement and keep icon filenames aligned with the final IDs.

## Achievement set

### `049_doomsday_a_future_worth_planning`

Working title: A Future Worth Planning

Eligible country:

Any ordinary player-controlled country affected by Event 049.

Unlock proof:

- Civic Continuity route.
- Major education, archive, transport, and evidence missions completed.
- High institutional continuity at the date.
- No Doomsday administration.
- At least one long project resumed after the failed date.

Disqualifiers:

- Violent mass suppression.
- Destructive full demobilization.
- The Final Vigil.
- Failed required public promises.

Difficulty: Hard.

Icon direction:

A school or drafting table extending past a torn calendar.

### `049_doomsday_the_last_recruit`

Working title: The Last Recruit

Eligible country:

A player-controlled country with a meaningful armed force.

Unlock proof:

- Preserve muster rolls and depots.
- Retain a defensive force to the date.
- Use conscientious or defensive service.
- Reconstitute the military after failure without mass punishment.

Disqualifiers:

- Chaotic demobilization.
- Destroyed records.
- Nothing Left to Lose.
- Event-owned atrocity.

Difficulty: Medium to hard.

Icon direction:

A military register, grounded rifle, and civil-defense armband.

### `049_doomsday_no_one_dies_for_tomorrow`

Working title: No One Dies for Tomorrow

Eligible country:

A player-controlled belligerent.

Unlock proof:

- Peace Before the End or a pacifist administration.
- Every active war ends through a valid armistice or peace before the final month.
- Conscientious service or objector release.
- No new offensive war after Event 49 fires.
- No broken Last Day truce.

Disqualifiers:

- Final-war posture.
- New offensive war.
- Truce breach.

Difficulty: Hard.

Icon direction:

Stacked rifles beneath a vigil light with civilian relief.

### `049_doomsday_the_calendar_was_wrong`

Working title: The Calendar Was Wrong

Eligible country:

Any player country that reaches the failed date.

Unlock proof:

- Experience The Last Calendar.
- Complete all required reconstruction phases.
- Restore government, education, transport, finance, and institutional function.
- Prevent revised-date hardliners from taking national power.
- Close the acute Event 049 category.

Disqualifiers:

- The Final Vigil.
- Unresolved government collapse.

Difficulty: Medium to hard.

Icon direction:

A broken calendar in morning light beside reopened institutions.

### `049_doomsday_the_final_assembly`

Working title: The Final Assembly

Eligible country:

A player-controlled Doomsday administration.

Unlock proof:

- Help satisfy a valid Final Vigil readiness path.
- Become a full member before or during terminal commitment.
- Complete the Assembly diplomacy branch.
- Fulfill one real relief, transport, demobilization, records, or shelter obligation.
- Hold meaningful influence in the dominant Assembly current.

Disqualifiers:

- Observer-only status.
- Joining after commitment with no prior contribution.
- Microstate exploit contribution.

Difficulty: Very hard.

Icon direction:

The Final Assembly emblem over a hall with relief and stored weapons.

### `049_doomsday_no_future_no_masters`

Working title: No Future, No Masters

Eligible country:

A player-controlled Doomsday administration.

Unlock proof:

- Complete Communal Devolution.
- Keep local relief functioning in all selected regions.
- Prevent exclusionary hoarding and armed settlement domination.
- Reach the date or Final Vigil with stable communal institutions.

Disqualifiers:

- Custodial Administration.
- Central military dictatorship.
- Deliberately caused severe famine or exclusion.

Difficulty: Hard.

Icon direction:

Local hands holding keys, bread, and shelter beneath one horizon.

### `049_doomsday_prepare_for_everything`

Working title: Prepare for Everything

Eligible country:

Any ordinary player country.

Unlock proof:

- Complete meaningful shelter, reserve, archive, hospital, and transport preparation.
- Use at least one preparation asset successfully against a real separate crisis.
- Reach the failed date.
- Convert preparations into useful post-date institutions.

Disqualifiers:

- Elite-only shelter exposure.
- Corrupt reserve collapse.
- The Final Vigil before cross-system protection proof.

Difficulty: Hard and campaign-dependent.

Icon direction:

A shelter with medicine, seed, records, and transport tools.

### `049_doomsday_the_state_outlived_the_prophecy`

Working title: The State Outlived the Prophecy

Eligible country:

A player country that uses Emergency Order for a substantial period.

Unlock proof:

- Prevent national government capture.
- Preserve high institutional continuity.
- Reach the failed date.
- Avoid event-owned mass death, disappearance, destroyed records, and severe Condemnation.
- Complete a legal post-date review and remedy wrongful detention.

Disqualifiers:

- Revolutionary takeover.
- Severe backlash at the date.
- Concealed atrocity or destroyed evidence.

Difficulty: Very hard.

Icon direction:

An intact archive and courthouse beyond a discarded calendar.

### `049_doomsday_still_waiting`

Working title: Still Waiting

Status: Hidden.

Eligible country:

A player country where the one bounded revised-date branch appears.

Unlock proof:

- Allow the movement to survive as a legal local minority.
- Prevent national takeover and renewed global crisis.
- Reach the defined observation date with stable institutions and no violent suppression.

Disqualifiers:

- National hardliner takeover.
- Mass repression.
- Debug-created repetition.

Difficulty: Rare and medium in direct play.

Icon direction:

A small group beside an outdated calendar under an empty sky.

### `049_doomsday_every_bell_at_midnight`

Working title: Every Bell at Midnight

Eligible country:

A player country with several significant religious, civic, regional, or cultural institutions.

Unlock proof:

- Complete the plural observance route.
- Protect final vigils in every selected region.
- Keep hospitals, communications, and relief routes open through the final night.
- Reach dawn without lethal crowd suppression or major public-order collapse.

Disqualifiers:

- Coercive exclusive observance.
- Relief routes closed for spectacle.
- Mass casualties during the final night.

Difficulty: Hard.

Icon direction:

Several distinct bell, siren, lamp, or civic symbols around one horizon.

## Tracking requirements

- Use actual event, posture, mission, focus, war, terminal, government, and recovery state.
- Use one-time flags or variables with stable save persistence.
- Avoid achievement unlocks based only on completing one focus.
- Define exact ownership across player tag switching and multiplayer.
- Follow existing rules for debug, Force Trigger Mode, mods, and campaign eligibility.
- Ensure failed missions and disqualifying actions clear eligibility permanently when required.
- Avoid whole-world daily checking. Use event-owned updates, mission completion, on-action hooks, and bounded checks.
- Document each tracking key and the event or effect that sets it.

## Asset requirements

Route icon production through `prompts/049_doomsday_asset_prompt.md`.

Every achievement needs:

- Completed `64x64` icon.
- Grey state where required.
- Not-eligible state where required.
- Native source art and manifest evidence.
- Root-level `gfx/achievements/` filenames matching the final achievement ID.
- No resized decision, idea, or focus icon substitute.

## Localisation direction

Final titles and descriptions should describe the player accomplishment and route without revealing hidden mechanics or listing internal variable checks.

The working titles can be retained only after tone and UI review.

## Validation

For every achievement, provide a test path that proves:

- Eligibility can be gained.
- Every major disqualifier blocks unlock.
- Save and reload preserves state.
- Tag switching does not duplicate or transfer credit incorrectly.
- The achievement does not unlock from debug or partial route completion.
- The final icon and text are present.

Do not mark the achievement set complete while any achievement is trivial, unreachable, missing art, missing localisation, or based on a placeholder condition.
