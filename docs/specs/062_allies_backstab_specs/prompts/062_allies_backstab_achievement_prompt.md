# Event 062 achievement implementation prompt

Implement the four accepted achievements for Chaos Redux Event 62.

Read:

- `docs/specs/062_allies_backstab_specs/specs/062_allies_backstab_spec_part_7_ai_achievements_presentation.md`
- `docs/specs/062_allies_backstab_specs/quality/062_allies_backstab_acceptance_scenarios.md`
- `AGENTS.md`
- `chaos-redux-events`
- `chaos-redux-event-assets`

Use the single Chaos Redux achievement registry. Do not create a new achievement file with another unique ID unless the current repository structure explicitly requires it.

Working names are not final localisation. Write final player-facing text in the project style.

## Achievements

### The Weak Link Holds

Track the player as an expelled country that belonged to the highest-vulnerability candidate tier. Require the country to remain uncapitulated, retain the original capital, and obtain recognized separation or defensive victory.

Store the vulnerability-tier proof at selection. Do not recalculate it after the faction changes.

### Council of the Cast Out

Track at least three original victims from one purge. Require liaison creation, unified cohesion, successor compact formation, independent survival of every counted member, and peace with the original faction.

The player must remain part of the victim coalition through the settlement.

### No Second Betrayal

Track a player faction leader during Evolution II. After the first actual split, require success in `Prevent a Second Defection`, at least five original political units still loyal, and no additional defection before resolution.

A neutral withdrawal after the first split counts as another loss unless the accepted mission terms explicitly exempt it.

### A Seat of Our Own

Track a player in the qualifying Evolution III generation. Require the player to become leader of a valid faction containing members from at least two different shattered original factions and keep that faction intact for one year.

Require at least three independent political units.

## Tracking rules

Use persistent receipts for:

- Event 62 generation ID
- original faction identity
- original victim array
- vulnerability tier
- original capital
- capitulation state
- liaison creation
- cohesion threshold
- first split
- later defection count
- successor faction origin
- member original-faction provenance
- settlement outcome
- one-year holding period

Every achievement must have explicit disqualifiers and must survive save and reload.

Do not award from approximate current state when historical proof is required.

## Assets

Use the accepted asset handoff. Each achievement requires:

- completed DDS
- grey DDS
- not-eligible DDS
- filename matching the full achievement ID
- root placement under `gfx/achievements/`
- sprite or engine registration according to current precedent

Do not resize decision or idea icons into achievement art.

## Localisation

Write:

- final achievement name
- clear visible requirement
- concise description
- hidden progress text only when the existing UI supports it safely

Do not reveal hidden target formulas. `Highest-vulnerability candidate tier` should become understandable player text such as being selected among the faction's weakest members, while the implementation keeps the exact receipt.

## Validation

Test each achievement's success, near miss, disqualifier, save and reload, player tag switch rule, and one-time award behavior.

Verify that debug or force-trigger achievement disqualification follows the existing project policy.

Document tracking keys, asset paths, localisation keys, and acceptance results in the Event 62 implementation report.
