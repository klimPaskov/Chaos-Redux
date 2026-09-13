# Event 40 Achievement Implementation Prompt

Implement the accepted achievement set for Chaos Redux Event 40.

## Required reading

Read:

- `AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- every Event 40 specification file
- installed vanilla achievement definitions and runtime asset precedents

Use the single Chaos Redux achievement registry at:

`common/achievements/chaos_redux_achievements.txt`

Do not create a separate achievement database with another `unique_id`.

## Achievement set

### `chaos_redux_040_uncrowned_kingdom`

Working title: The Uncrowned Kingdom

Unlock:

- Lawrence's Kingdom has formed
- Lawrence is alive at formation
- the new state is not a British subject
- the country followed the accepted personal route, not a cosmetic rename of British Arabia

Track the exact Event 40 formation origin.

### `chaos_redux_040_promises_kept`

Working title: Promises Kept

Unlock as Britain when:

- the British Arabian System is formally established
- at least three durable partners exist
- Britain completes the regional campaign
- no registered constitutional or autonomy guarantee was broken

Define what counts as a guarantee and what exact outcome breaks it. Do not rely on flavour text.

### `chaos_redux_040_better_bargain`

Working title: A Better Bargain

Unlock as an Arabian target when:

- the country received a major British material package
- Lawrence's Influence never completed a dominant client settlement
- the country resolves as a sovereign armed partner or independent British ally

The aid receipt must be one-shot and value-bearing. A token opening gift is insufficient.

### `chaos_redux_040_every_ledger_has_a_name`

Working title: Every Ledger Has a Name

Unlock when the target:

- completes the gold-ledger investigation
- turns a valid contact
- exposes or uses the network evidence
- dismantles the active network
- avoids a civil war during that intervention

### `chaos_redux_040_gold_without_chains`

Working title: Gold Without Chains

Unlock when a country:

- receives British financial or military support in at least two distinct validated stages
- never becomes a British subject
- later joins or forms the Independent Arab Federation

Track receipts by generation and stage. Do not count the same shipment twice.

### `chaos_redux_040_desert_conference`

Working title: The Desert Conference

Unlock when the player:

- founds a counter-bloc or Arab congress
- secures at least three independent participating governments
- ends the Event 40 regional campaign through a negotiated settlement
- avoids forced annexation of the founding participants

### `chaos_redux_040_rails_ports_promises`

Working title: Rails, Ports, and Promises

Unlock as Britain or British Arabia when:

- one active later intervention uses a connected route containing at least one valid port component, one railway or supply connection, and one air-route component
- the route remains functional through the intervention settlement
- the later intervention completes successfully

Use actual map and access proof. Do not unlock from three abstract flags that can exist without a connected route.

## General rules

For every achievement implement:

- stable tracking flags or variables
- clear starting eligibility
- exact unlock trigger
- disqualifiers
- one-time award state
- player-facing name and description
- hidden debug text when needed
- full icon triplet
- documentation
- route or event hooks
- save and reload persistence

Respect the project's force-trigger, custom-game-rule, and achievement eligibility policy.

## Icon direction

Request these visual concepts from `chaosx_icon_artist`:

- The Uncrowned Kingdom: Lawrence identity motif, restrained crown, federal charter
- Promises Kept: two sealed agreements over a route network
- A Better Bargain: secured rifle crate under national custody
- Every Ledger Has a Name: ledger, payment marks, investigative lens
- Gold Without Chains: gold purse and broken chain around a federal seal
- The Desert Conference: three delegations around a charter seal
- Rails, Ports, and Promises: locomotive, ship, and aircraft around one route marker

Achievement files remain under `gfx/achievements/` with filenames matching the full achievement IDs and state suffixes.

## Validation

Test every achievement through a dedicated acceptance path. Verify that near-miss states do not unlock it.

Report:

- exact files changed
- tracking IDs
- localisation keys
- icon filenames
- tested unlock route
- tested disqualifier or near miss
- unresolved blockers
