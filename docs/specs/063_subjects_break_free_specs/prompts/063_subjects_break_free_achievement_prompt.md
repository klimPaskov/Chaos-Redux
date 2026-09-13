# Achievement prompt: Event 063 Subjects Break Free

Implement and document the four Event 063 achievements below. Follow `AGENTS.md`, `chaos-redux-events`, `chaos-redux-event-assets`, the shared achievement patterns already in the repository, and the Event 063 specification files.

Read:

- `docs/specs/063_subjects_break_free_specs/specs/063_subjects_break_free_spec_part_6_presentation_assets_achievements_and_acceptance.md`
- `docs/specs/063_subjects_break_free_specs/specs/063_subjects_break_free_spec_part_2_settlements.md`
- `docs/specs/063_subjects_break_free_specs/specs/063_subjects_break_free_spec_part_3_network_and_pact.md`
- `docs/specs/063_subjects_break_free_specs/prompts/063_subjects_break_free_asset_prompt.md`

Working labels below are identifiers and title directions. Write final achievement localisation from the described feat. Do not copy working labels automatically.

## Achievement 1

ID: `chaosx_achievement_063_independence_secured`

Title direction: durable independence followed by solidarity with another breakaway.

Description direction: make clear that the country must survive independently, gain recognition from its former overlord, and materially assist another liberated state.

Eligible countries:

- a country successfully freed by Event 063 in the current campaign

Unlock conditions:

- remain continuously independent for 730 days after the tracked Event 063 release
- remain existent and not a subject at completion
- former overlord has formally recognized independence
- materially support another active liberated state after the tracked release

Qualifying support:

- transferred equipment or logistics aid that left the donor's real stockpile
- a valid guarantee
- volunteers or direct defense
- successful mediation that ended another country's former-overlord dispute

Non-qualifying support:

- recognition alone
- a duplicate aid hook
- an action with no real target effect

Disqualifiers:

- force-run, debug, or scenario setup when the shared achievement framework marks the run ineligible
- re-subjugation during the 730-day continuity period
- country ceases to exist

Difficulty: Medium.

Visible status: visible.

Tracking:

- tracked release transaction generation
- release date
- former overlord
- recognition state and date
- continuous independence timer
- qualifying support recipient and support type
- one-shot completion guard

Icon direction: recognized seal, open chain, and a small aid crate. Use a distinct compact silhouette.

## Achievement 2

ID: `chaosx_achievement_063_pact_founder`

Title direction: a durable cross-origin liberation alliance.

Description direction: found or lead the Event 063 Liberation Pact, expand it across liberation origins, and hold high cohesion for a full year.

Eligible countries:

- the original Pact founder
- a valid later Pact leader only when the repository's achievement design permits inherited leadership attempts

Unlock conditions:

- Liberation Pact exists
- player country is the eligible tracked founder or leader
- at least six full members
- at least two distinct first liberation origins among full members
- Liberation Cohesion at least 75
- cohesion remains at or above 75 for 365 continuous days
- no full member is currently a subject at completion

Disqualifiers:

- partners or observers counted as full members
- force-run, debug, or ineligible scenario setup
- timer interrupted by cohesion falling below 75
- Pact dissolves
- player country leaves, becomes subject, or ceases to exist

Difficulty: Hard.

Visible status: visible.

Tracking:

- founder and current leader identity
- full-member roster
- each member's first liberation origin
- live distinct-origin count
- high-cohesion timer start and reset
- subject-state validation for every full member
- one-shot completion guard

Icon direction: complete charter ring with six linked emblems. It should read as a functioning institution, not a globe or one ideology.

## Achievement 3

ID: `chaosx_achievement_063_independence_war_victory`

Title direction: a coordinated breakaway defeating a stronger former overlord.

Description direction: lead an Evolution II compound independence war, begin weaker, fight with another subject from the same cohort, receive external liberated-state support, and preserve independence.

Eligible countries:

- breakaway war leader in an Event 063 Evolution II compound independence war

Unlock conditions:

- former overlord was stronger at the frozen war-opening snapshot under the accepted combined-strength comparison
- at least one additional same-overlord cohort member joined the breakaway side
- at least one active liberated state outside the original cohort delivered qualifying material or military support
- peace leaves the tracked war leader independent
- former overlord recognizes the settlement or no longer has a valid restoration claim

Qualifying external support:

- real equipment or logistics transfer
- volunteers
- direct war entry
- a guarantee that became relevant to the conflict

Disqualifiers:

- ordinary one-country baseline war
- former overlord was not stronger at war opening
- supporter was part of the original cohort
- duplicate support event counted twice
- peace restored subject status
- ineligible force or scenario state

Difficulty: Hard.

Visible status: visible.

Tracking:

- war and transaction identity
- breakaway leader
- former overlord
- frozen combined-strength comparison
- cohort roster
- external supporter identity and support type
- peace result
- one-shot completion guard

Icon direction: a defensive shield holding against a restored chain or authority mark. Avoid a specific national symbol.

## Achievement 4

ID: `chaosx_achievement_063_peaceful_release`

Title direction: former authority preserved through recognition and no reconquest.

Description direction: recognize a large release batch, avoid restoration for two years, and retain positive relations with several former subjects.

Eligible countries:

- a former overlord that lost at least four completed subjects in one Event 063 firing

Unlock conditions:

- at least four subjects from one tracked firing received recognition without first defeating the former overlord in an Event 063 independence war
- no tracked released country is re-subjugated by the player or an attributed player-controlled proxy during the next 730 days
- no restoration war is begun against a tracked country during that period
- at least three tracked released countries have positive relations with the player at completion

Disqualifiers:

- recognition occurs only after military defeat in the relevant independence war
- fewer than four completed releases in the tracked batch
- any prohibited restoration or proxy re-subjugation
- force-run, debug, or ineligible scenario state

Difficulty: Medium to Hard.

Visible status: visible.

Tracking:

- transaction generation
- former-overlord identity
- completed released-country roster
- recognition method for each country
- 730-day non-restoration timer
- player and attributed proxy war or puppet actions
- live relation count at completion
- one-shot completion guard

Icon direction: several open chain links beside a signed settlement document.

## Implementation requirements

- inspect existing Chaos Redux achievement definitions, scripted triggers, localisation, icon registration, and eligibility rules before adding content
- use stable event-owned tracking that survives save and reload
- do not overwrite one active attempt with an unrelated later Event 063 firing
- define how simultaneous qualifying firings are tracked with a bounded set and no unbounded global scan
- reset or fail timers only for the conditions stated above
- ensure AI or other players cannot accidentally grant a player credit through an unrelated duplicate hook
- make every achievement one-shot
- wire final localisation and the completed, grey, and not-eligible icon triplets
- document every trigger, tracker, reset condition, and disqualifier
- test every achievement through a positive case, each major failure case, save and reload, tag switching, and multiplayer attribution

## Asset requirements

Coordinate with the asset prompt. Each achievement needs:

- completed `64x64` icon
- grey `64x64` icon
- not-eligible `64x64` icon
- unchanged repository red not-eligible overlay
- manifest row, source hash, processed hash, final DDS hash, sprite registration, and live consumer evidence

Do not claim an achievement complete while its icon triplet, localisation, eligibility, or tracking remains placeholder or missing.
