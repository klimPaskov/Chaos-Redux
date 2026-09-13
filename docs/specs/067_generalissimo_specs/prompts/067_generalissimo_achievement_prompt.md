# Event 067 Generalissimo Achievement Prompt

Implement the complete Event `067` achievement set and create the required icon triplets.

## Required sources

Read:

- `docs/specs/067_generalissimo_specs/specs/067_generalissimo_spec_part_8_presentation_assets_localisation.md`
- `docs/specs/067_generalissimo_specs/specs/067_generalissimo_spec_part_9_acceptance_and_limits.md`
- every Event 067 specification part needed to verify route, civil-war, world-end, scenario, and actor conditions
- `AGENTS.md`
- `chaos-redux-events`
- `chaos-redux-event-assets`
- current vanilla and Chaos Redux achievement definitions

Final titles and descriptions must follow the direction below. The working identifiers and title directions are not final localisation.

## Shared rules

- Use the single root Chaos Redux achievement registry and current project pattern.
- Create stable tracking flags or variables only where existing state cannot prove the condition.
- Track the canonical Generalissimo and original host safely across civil war and reunification.
- Prevent debug, console, incomplete scenario, or invalid bypass states from granting achievements.
- Record every disqualifier explicitly.
- Do not grant an achievement merely because a focus is completed if the challenge also requires a war, route, member count, duration, or restoration outcome.
- Create one completed, grey, and not-eligible icon for every achievement.
- Use exact achievement IDs as filenames after inspecting project convention.
- Achievement art is a separate icon family. Do not resize focus or idea icons.

## Achievement definitions

### `067_generalissimo_civilian_command`

Title direction:

A legal government proves that the armed forces remain subordinate.

Eligible country:

Original Event 067 host.

Unlock:

- Evolution II active
- Influence reached at least 65
- Generalissimo permanently removed without revolt
- peaceful submission never used

Disqualifiers:

- junta victory
- immediate-war scenario setup
- debug completion markers

Difficulty:

Hard.

Icon direction:

A command baton placed beneath a civilian seal or secured command chain.

Tracking:

Store the peak Influence before removal and the peaceful resolution method.

### `067_generalissimo_refuse_the_ultimatum`

Title direction:

The legal government refuses the final demand and defeats the military revolt.

Eligible country:

Original host government.

Unlock:

- Evolution III ultimatum at Influence 85 or higher
- refuse the ultimatum
- win the civil war as the original government
- Generalissimo permanently removed

Disqualifiers:

- submission
- another country annexes the junta before the host meaningfully wins
- debug or forced-victory marker

Difficulty:

Very hard.

Icon direction:

A government seal standing against crossed marshal batons.

Tracking:

Record ultimatum Influence, refusal, government-side identity, and victory contribution.

### `067_generalissimo_barracks_to_capital`

Title direction:

The Generalissimo converts maximum military backing into national rule.

Eligible country:

Generalissimo junta.

Unlock:

- revolt begins at Influence 90 or higher
- junta wins and reunifies the host
- junta receives no foreign volunteers or expeditionary forces

Disqualifiers:

- peaceful submission
- foreign intervention exceeds the accepted no-help definition
- debug force-grant state

Difficulty:

Very hard.

Icon direction:

A field headquarters becoming a national capital silhouette.

Tracking:

Record opening Influence, foreign volunteers, expeditionaries, direct foreign unit support, and junta victory.

### `067_generalissimo_total_command`

Title direction:

Personal military rule, decisive warfare, and a regional sphere reach their complete form.

Eligible country:

Generalissimo-led country.

Unlock:

- Generalissimo becomes ruler
- Personal Command political route completed
- Decisive Command military route completed
- Supreme Strategic Sphere route completed
- two valid major enemies capitulated after takeover

Disqualifiers:

- political route changed
- target major counted twice
- pre-takeover capitulation counted
- debug or scenario completion override

Difficulty:

Very hard.

Icon direction:

One baton over a command globe with a clear offensive symbol.

Tracking:

Use a unique set of defeated post-takeover major identities.

### `067_generalissimo_first_among_generals`

Title direction:

A stable officer order accepts the original Generalissimo's leadership.

Eligible country:

Generalissimo-led Officer Directorate.

Unlock:

- Officer Directorate route completed
- Command Cohesion at least 90
- lead International Command
- at least five independent members
- at least two members are majors
- no member leaves for 365 days

Disqualifiers:

- Personal Command or National Emergency Council final route
- faction created outside the Event 067 route
- member count includes subjects when the design requires independence

Difficulty:

Very hard.

Icon direction:

One senior star surrounded by several officer stars in a council ring.

Tracking:

Track member identities, independence, major status, continuous membership, leadership, and Cohesion.

### `067_generalissimo_guardian_state`

Title direction:

The Generalissimo preserves a military guardian state without launching conquest.

Eligible country:

Generalissimo-led National Emergency Council.

Unlock:

- National Emergency Council completed
- Fortress Command completed
- no offensive war for five years after permanent government proclamation
- Command Cohesion at least 70 at the end
- country remains independent

Disqualifiers:

- Event 067 offensive expansion decision used
- player declares an offensive war
- country becomes a subject

Difficulty:

Hard.

Icon direction:

A shielded civic building beneath a military star.

Tracking:

Record proclamation date, offensive-war state, route state, independence, and Cohesion.

### `067_generalissimo_world_against_the_barracks`

Title direction:

Civilian governments defeat the original Generalissimo during the world-end struggle.

Eligible country:

Original legal host or qualifying civilian major in Civil Authority Compact.

Unlock:

- The Generalissimos' World active
- country leads the Compact or is its principal military contributor under a defined rule
- original Generalissimo state defeated
- civilian government restored in at least three countries
- at least one restored country is a major

Disqualifiers:

- country previously submitted to the Generalissimo
- country becomes a military government
- same restored country counted twice

Difficulty:

Extreme.

Icon direction:

Several civilian seals breaking a ring of marshal batons.

Tracking:

Track original Generalissimo defeat, restored country identities, major status, Compact role, and player regime.

### `067_generalissimo_no_second_shot`

Title direction:

A prepared final removal succeeds when the military takeover is nearly complete.

Eligible country:

Original host.

Unlock:

- Evolution III ultimatum active
- Influence at least 90
- choose final removal
- operation succeeds
- no earlier failed ordinary dismissal

Disqualifiers:

- immediate-war scenario type
- debug chance override
- Generalissimo already removed through another route

Difficulty:

Extreme and preparation-sensitive.

Icon direction:

A stopped clock beside a broken command insignia, without graphic violence.

Tracking:

Record Influence at operation, final removal state, success, prior dismissal failure, and scenario type.

## Asset production

Route all achievement icons to `chaosx_icon_artist` with a complete context-free prompt.

Requirements:

- inspect achievement references and triplet rules
- native transparent source where required by the consumer
- one independent composition per achievement
- readable at 64 by 64
- completed, grey, and not-eligible states
- exact filenames
- source ImageGen evidence
- contact sheet
- manifest
- runtime path handoff

## Validation

For every achievement, build at least one positive and one negative scenario.

Verify:

- route and actor identity
- timing
- civil-war side
- unique country sets
- member counts
- no duplicate target counting
- no pre-event progress counted where prohibited
- save and reload
- disqualifiers
- scenario and debug blocking
- icon and localisation

Report every achievement that cannot be proven reliably as incomplete. Do not weaken a condition to make tracking easier.
