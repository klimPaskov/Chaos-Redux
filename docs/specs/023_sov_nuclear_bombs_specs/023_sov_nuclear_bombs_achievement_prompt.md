# Event 023 achievement implementation prompt

Implement the full Event 23 achievement set from Part 10.

## Required achievements

1. `023_sov_nuclear_bombs_a_hundred_suns`.
2. `023_sov_nuclear_bombs_the_bomb_never_fell`.
3. `023_sov_nuclear_bombs_ultimatum_without_ash`.
4. `023_sov_nuclear_bombs_scattered_arsenal`.
5. `023_sov_nuclear_bombs_firebreak`.
6. `023_sov_nuclear_bombs_first_and_last`.
7. `023_sov_nuclear_bombs_the_last_telephone`.

Working names may change during final localisation. Stable implementation IDs should remain once registered.

## Eligibility, visibility, and difficulty

| Achievement | Eligible country and player | Visibility | Difficulty | Why it is not trivial |
| --- | --- | --- | --- | --- |
| A Hundred Suns | Human player controlling the Event 23 Soviet host | Visible | Medium | Requires a large fully accounted arsenal and high Readiness without Missing devices |
| The Bomb Never Fell | Human player controlling the Event 23 Soviet host | Visible | Hard | Requires public deterrence, a serious crisis, zero Soviet combat use, full accounting, and a verified moratorium |
| Ultimatum Without Ash | Human player controlling the Event 23 Soviet host | Visible | Medium to hard | Requires credible coercion against a real independent target and a durable settlement without combat detonation |
| Scattered Arsenal | Human player controlling the Event 23 Soviet host during Event 5 | Visible | Very hard | Requires several custody crises, negotiated resolution, complete recovery or dismantlement, and restored command |
| Firebreak | Human player controlling the Event 23 Soviet host during a multi-major exchange | Visible | Very hard | Requires a confirmed exchange and successful stand-down before General Exchange or Fallout |
| First and Last | Human player controlling the Event 23 Soviet host | Visible | Very hard | Requires exactly one combat use, then total verified removal of the remaining arsenal and lasting moratorium |
| The Last Telephone | Human player controlling the Event 23 Soviet host at Evolution IV | Visible | Extreme | Requires the complete severe first-use emergency gate, final strike preparation, and reciprocal stand-down at 1000 or more Chaos |

All seven are public mastery achievements. None is a hidden surprise route. Their tooltips may avoid exposing internal variable names while still describing the visible objective.

## Description and icon direction

| Achievement | Description direction | Icon direction |
| --- | --- | --- |
| A Hundred Suns | Emphasize a large usable arsenal, high readiness, and complete accounting | Rows of sealed Soviet bomb casings or storage doors under controlled industrial light |
| The Bomb Never Fell | Emphasize demonstrated deterrence, a serious crisis, zero combat use, and verified moratorium | A locked bomb cradle or sealed keys beside dismantlement tools and a distant test cloud |
| Ultimatum Without Ash | Emphasize a real target accepting a durable settlement without a combat detonation | An armistice or transfer document beside unused launch keys and a sealed device, with no readable generated text |
| Scattered Arsenal | Emphasize recovery or dismantlement across several breakaways and restored command | Guarded rail lines converging on a secure central depot with distinct sealed crates |
| Firebreak | Emphasize stopping a confirmed major exchange before General Exchange or Fallout | Two damaged communication lines joined across a burned horizon |
| First and Last | Emphasize exactly one combat use followed by complete verified removal and moratorium | One distant cloud reflected on dismantlement tools and an empty storage rack |
| The Last Telephone | Emphasize final authorization pressure at Evolution IV and a successful reciprocal stand-down | A period command telephone held above a sealed order or launch key under blackout conditions |

## Required reading

Read:

- `AGENTS.md`.
- `chaos-redux-events`.
- `chaos-redux-event-assets`.
- `chaos-redux-subagents`.
- Event 23 Part 10.
- Current root achievement registry and vanilla achievement precedents.

## Gameplay implementation

For every achievement, implement:

- Exact tracking flags and variables.
- Unlock trigger.
- Actor and player control checks.
- Disqualifiers.
- Verification period where specified.
- Save and reload persistence.
- Debug and force-trigger handling consistent with the project achievement system.
- Event, decision, collapse, custody, moratorium, exchange, strike, or shared-system hooks.
- Player-facing localisation.
- Documentation.

Do not convert a hard achievement into an opening-event unlock.

## Specific proof requirements

### A Hundred Suns

Prove at least 100 accounted operational Soviet bombs, Readiness at least 90, and no Missing devices.

### The Bomb Never Fell

Prove public demonstration, Evolution II or later, one qualifying crisis, Atomic Moratorium, zero Soviet combat detonations, and complete accounting.

### Ultimatum Without Ash

Prove a real valid independent target, recorded response, full or partial compliance, no Soviet combat detonation against the target, and settlement verification.

### Scattered Arsenal

Prove Event 5 custody crises across at least two breakaways, complete recovery or dismantlement, one negotiated or monitored resolution, no operational breakaway nuclear actor, and Integrity at least 80.

### Firebreak

Prove a confirmed major-to-major detonation, at least two nuclear majors, successful reciprocal stand-down before General Exchange and before Fallout, and a verification period without violation.

### First and Last

Prove exactly one Soviet combat detonation, complete reconciliation and removal of every remaining Soviet operational device, Atomic Moratorium, and no second Soviet combat detonation.

### The Last Telephone

Prove Evolution IV, 1000 or more Chaos, valid nuclear-major opponent, full severe-loss first-use conditions, strike preparation reaching final authorization, then reciprocal hotline stand-down without Soviet first use.

## Asset implementation

Route the complete seven achievement triplets to `chaosx_icon_artist` with `fork_context=false`.

For each achievement create:

- Base eligible or unlocked DDS.
- Grey DDS.
- Not-eligible DDS.
- Source PNG and prompt.
- Processed PNG.
- Contact-sheet review.
- Manifest row.

Use the exact root achievement path and full IDs. Do not put achievement DDS files in an event subfolder.

Do not derive every achievement from one resized icon. Each needs a distinct composition matching its goal.

## Localisation direction

Names can use restrained allusion, technical language, or bitter irony. Descriptions should explain the visible objective and avoid internal variable names.

Do not reveal hidden probability weights, false-warning routes, or future event surprises.

## Audit

Check:

- No automatic opening unlock.
- No duplicate completion on save and reload.
- No completion through missing or duplicated devices.
- No target that was already a subject or capitulated for Ultimatum Without Ash.
- No immediate Soviet settlement violation.
- No Firebreak completion after General Exchange or Fallout.
- No First and Last completion with one hidden operational device.
- No Last Telephone completion without the full emergency gate.
- Correct actor and player ownership.
- Correct achievement asset paths and localisation.

Write a handoff under:

`docs/plans/023_sov_nuclear_bombs_plans/subagent_handoffs/`

List changed IDs, files, hooks, tracking state, asset files, validation cases, and remaining blockers.
