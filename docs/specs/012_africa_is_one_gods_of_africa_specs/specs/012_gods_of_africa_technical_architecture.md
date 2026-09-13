# Gods of Africa technical architecture specification

## Purpose

This document converts the accepted gameplay design into an implementation map. It does not replace required repository inspection, offline wiki reading, vanilla documentation, vanilla precedents, MCP evidence, or source validation.

All identifiers below are proposed working names. The implementation agent should preserve the Event 012 namespace and adapt names to established local patterns where a stronger existing convention is found.

## Ownership boundary

Gods of Africa belongs to Event `012`, Africa Is One.

The implementation should use:

- Event 012's authoritative African unifier scope or event target
- Event 012's continent-control and victory proof
- Event 012's evolution state
- Event 012's country and claimant registry
- Event 012's existing diplomacy, base, aid, guarantee, liberation, and settlement state where available

It should not create:

- a new Event 070 entry event
- a second African unifier selector
- a second continent-control ledger
- a second Africa Is One victory trigger
- a separate normal-event registration
- a separate cluster member
- an unrestricted world scan in a daily, weekly, or monthly on-action

## Proposed file map

Exact files must follow the live repository layout. A likely owner-local structure is:

```text
events/012_africa_is_one_events.txt
common/script_constants/012_africa_is_one_gods_constants.txt
common/scripted_effects/012_africa_is_one_gods_effects.txt
common/scripted_triggers/012_africa_is_one_gods_triggers.txt
common/scripted_localisation/012_africa_is_one_gods_scripted_localisation.txt
common/on_actions/012_africa_is_one_on_actions.txt
common/decisions/012_africa_is_one_decisions.txt
common/decisions/categories/012_africa_is_one_categories.txt
common/ideas/012_africa_is_one_ideas.txt
common/opinion_modifiers/012_africa_is_one_opinion_modifiers.txt
common/dynamic_modifiers/012_africa_is_one_dynamic_modifiers.txt
common/ai_strategy/012_africa_is_one_ai_strategy.txt
localisation/english/012_africa_is_one_l_english.yml
interface/012_africa_is_one.gfx
```

A dedicated GUI file should be added only if the implementation accepts the full GUI gate from the design specification.

## Runtime model

### African owner record

The African unifier owns the global system state.

Suggested persistent owner state:

| Working identifier | Type | Role |
| --- | --- | --- |
| `gods_of_africa_active` | country flag on unifier plus global proof if required | system activation |
| `gods_of_africa_activation_committed` | flag | prevents duplicate activation |
| `gods_of_africa_activation_date` | variable or date proof | activation history |
| `gods_of_africa_strength` | variable | global public Strength value |
| `gods_of_africa_strength_band` | variable | cached display and ceiling band |
| `gods_of_africa_doctrine` | variable or flags | reciprocal or extractive route |
| `gods_of_africa_priority_family` | variable | current African need priority |
| `gods_of_africa_dispatch_cursor` | variable | bounded participant scheduling |
| `gods_of_africa_active_demand_count` | variable | global clutter and dispatch control |
| `gods_of_africa_super_event_fired` | flag | one-time presentation proof |
| `gods_of_africa_final_settlement_committed` | flag | ending lock |
| `gods_of_africa_restoration_generation` | variable | prevents stale records after a valid restoration |

If the repository already has a global Event 012 owner or runtime carrier, use that carrier. Do not store the same fact in several places without a clear ownership reason.

### Participant record

Each participant owns its relationship state.

Suggested persistent participant state:

| Working identifier | Type | Public | Role |
| --- | --- | --- | --- |
| `gods_of_africa_participant` | flag | no | active registry membership |
| `gods_of_africa_participant_generation` | variable | no | joins record to current owner generation |
| `gods_of_africa_wrath` | variable | yes | personal Wrath value |
| `gods_of_africa_wrath_band` | variable | derived | display and decision gating |
| `gods_of_africa_active_demand` | flag | visible through mission | one-demand lock |
| `gods_of_africa_demand_id` | variable | no | current contract identity |
| `gods_of_africa_demand_family` | variable | visible through text | current demand family |
| `gods_of_africa_demand_amount` | variable | yes during demand | requested amount |
| `gods_of_africa_demand_deadline` | date or mission | yes | current deadline |
| `gods_of_africa_demand_band` | variable | no | burden band |
| `gods_of_africa_demand_status` | variable | no | open, extended, partial, resolved, failed |
| `gods_of_africa_next_demand_date` | date proof or variable | no | participant cooldown |
| `gods_of_africa_defiant` | flag | visible state | permanent opt-out under normal rules |
| `gods_of_africa_war_floor` | flag or derived trigger | no | active war Wrath floor |
| `gods_of_africa_territory_floor` | flag or derived trigger | no | occupation Wrath floor |
| `gods_of_africa_reconciliation_pending` | flag | visible through mission | rare restoration route |
| `gods_of_africa_recent_extreme_punishment` | timed flag | no | target cooldown |
| `gods_of_africa_recent_punishment_family_*` | timed flags | no | variety and repetition control |

### Hidden relationship record

Hidden history may use counters and flags because it is not a third public mechanic.

Suggested facts:

- total demands issued
- total full compliance
- total accepted substitutes
- total failed demands
- total direct refusals
- longest compliance streak
- current compliance streak
- voluntary aid incidents
- emergency aid incidents
- African territory returned
- wars against Africa
- days at war with Africa
- African core states occupied
- African allies attacked
- agreements broken
- public pardons received
- prior permanent defiance
- reconciliation completed
- Tier IV punishments suffered
- Tier V punishments suffered
- support during final continental campaign
- permanent favored disqualifiers
- exceptional positive marks

Use flags for true or false facts and variables for counts or scores. Avoid numeric variables that only hold zero or one.

## Participant registry

### Initial registration

The activation effect should build the initial registry from valid majors and player-controlled countries in one bounded pass.

This one-time activation pass is different from an unrestricted recurring world on-action. It is acceptable only if the repository's current Event 012 pattern and user permission allow the bounded initialization.

Each country is registered idempotently. The effect should:

1. validate the African unifier
2. exclude the unifier
3. exclude invalid and special countries according to the Event 012 design
4. set participant proof
5. set generation proof
6. initialize Wrath from current conduct
7. assign a stable dispatch order
8. set the first demand date with a deterministic stagger
9. queue the introduction once

### Later registration

Later majors and player-controlled countries require a low-frequency bounded onboarding route.

Preferred order:

1. direct registration from an existing player-control or tag-switch hook
2. direct registration from an existing Event 012 major-status or diplomatic milestone
3. owner-local quarterly review if no direct hook exists

A quarterly review should run from the African unifier's owner scope and stop when the system ends. It should not add a generic all-country quarterly action if Event 012 can own the iteration.

### Participant removal

A participant leaves the active registry when:

- it no longer exists
- it becomes the African unifier through a valid Event 012 transformation
- its generation is stale after an authorized system restoration
- the system reaches final settlement

The participant's history can be archived if Event 012 needs it for restored countries or final summaries.

## Activation sequence

Proposed effect flow:

```text
Event 012 Evolution I active
    -> African unifier establishment proof exists
    -> start consolidation timer once
    -> delayed activation validation
    -> save authoritative unifier scope
    -> set active state and generation
    -> calculate initial Strength
    -> register participants
    -> stagger introductions and first-demand dates
    -> open Africa-side category
    -> record Event 012 milestone
    -> issue proclamation and world report
```

The activation validation must fail closed if the unifier disappeared, Event 012 ended, Evolution I was disabled, or the establishment proof is stale.

## Strength calculation

### Range

The public value is clamped between `0` and `100`.

Use a weighted composite. The exact weights should be centralized in script constants and tuned after repository inspection.

Recommended factor groups:

| Factor group | Suggested share | Notes |
| --- | --- | --- |
| military readiness and relative power | about `25` | divisions alone are insufficient |
| industry and logistics | about `20` | factories, fuel, rail, trains, convoys, supply |
| continental control | about `20` | Event 012 authoritative state groups and institutions |
| strategic reach | about `15` | air, navy, technology, intelligence, global access |
| internal condition | about `10` | stability, surrender, capital, cohesion |
| Chaos and evolution amplification | about `10` | bounded amplifier |

These shares are design anchors. The implementation should avoid expensive exact world-rank calculations when a stable bounded comparison can produce the same band ordering.

### Recalculation cadence

Recalculate Strength:

- at activation
- after major Event 012 territorial milestones
- after African capital loss or recovery
- after large war-state changes
- after doctrine and evolution changes
- after severe African disaster or recovery
- on a low-frequency owner-local refresh, likely monthly

One monthly calculation in the African unifier scope is acceptable if it does not iterate every country. Do not run a per-country world recalculation.

### Smoothing

Ordinary changes should move through a smoothing rule or confirmation window. Major proofs such as capitulation risk, capital loss, or continent-control threshold can bypass smoothing.

Suggested behavior:

- ordinary recalculation can move by a bounded amount per refresh
- a major defeat can drop one or more bands immediately
- a major victory can raise a band after a short confirmation period

### Band cache

Cache the current band after recalculation so punishment and UI triggers do not repeat the full calculation.

Proposed bands:

- `0 to 19` limited
- `20 to 39` regional
- `40 to 59` continental
- `60 to 79` global
- `80 to 100` extreme

## Wrath transactions

### Central helper

All Wrath changes should call one participant-scope owner helper.

Inputs should include:

- signed amount through a positive value plus direction proof
- reason constant
- minimum floor after change
- maximum cap
- whether to add a history entry
- authoritative African unifier proof

Outputs should include:

- amount applied
- old band
- new band
- threshold crossed

Use positive input values and separate add or subtract behavior. Do not rely on a unary negative variable token.

### Suggested transaction anchors

| Incident | Suggested base movement |
| --- | --- |
| ceremonial compliance | `-5` to `-10` |
| standard compliance | `-10` |
| severe or emergency compliance | `-15` to `-20` |
| accepted substitute | `-5` to `-10` |
| meaningful voluntary aid | `-10` to `-20` |
| direct refusal | `+15` |
| deadline failure | `+20` |
| broken transfer | `+20` to `+30` |
| occupation of African core territory | floor plus one-shot increments |
| active war with Africa | high floor |
| permanent defiance | set at least `70` plus permanent flag |
| completed reconciliation | reduce to a high manageable band |

All final values should use round increments and dynamic modifiers. These are tuning anchors, not unconditional literals at every call site.

### Floors

Wrath floors should be derived from active conditions. A helper should reapply the highest valid floor after every reduction.

Potential floors:

- active hostile war
- current African core occupation
- unresolved broken treaty
- permanent defiance
- recent extreme offense

## African need profile

### Purpose

The need profile keeps tribute useful and stops repeated requests for surplus stockpiles.

### Internal categories

Use a small internal family list:

- land equipment
- mobile and artillery equipment
- armor
- aircraft
- fuel
- transport
- industry and repair
- strategic resources
- manpower and formations
- diplomatic recognition
- territorial liberation
- alliance and access
- emergency relief

Each category receives a hidden need score.

### Inputs

Need scores may read:

- stockpile and production deficits
- reinforcement demand
- fuel days and current consumption
- convoy and train reserve
- current wars and fronts
- damaged Event 012 infrastructure
- air and naval balance
- occupied African territory
- active disaster and humanitarian pressure
- diplomacy and recognition state
- Event 012 doctrine and priority

### Need output

The selector should return:

- valid family mask
- family weights
- emergency family proof
- current priority bonus
- families blocked by surplus or invalid mechanics

The need profile is hidden. The Africa-side UI may show one qualitative priority chosen by the player.

## Target capacity profile

### Protected floors

Each material family needs a protected operating floor.

Examples:

- infantry equipment required for deployed and training units
- support equipment required for current templates
- fuel required for a minimum period of current operation
- convoys required for supply and trade
- trains required for current logistics
- aircraft required for current wings and reinforcement
- tanks required for active armored formations

The floor may be lowered by punitive demand bands, but normal requests should use only capacity above the floor.

### Capacity outputs

The capacity helper should return:

- valid family mask
- usable amount per family
- burden bands per family
- maximum readable demand amount
- substitute candidates
- hardship proof
- current war reserve proof

### Missing stockpile access

Where the engine cannot read or debit a stockpile reliably, the family should fail closed or use a documented owner contract. Do not infer a transfer from a modifier that does not give Africa the material.

## Demand creation contract

### Inputs

- valid African unifier
- valid participant
- no active demand
- participant not permanently defiant
- no active war route replacing ordinary demands
- current Strength band
- current Wrath and floor
- Africa need profile
- participant capacity profile
- current Event 012 evolution and doctrine
- global active-demand budget

### Selector stages

1. remove invalid demand families
2. apply African need weights
3. apply participant capacity weights
4. apply conduct and Wrath weights
5. apply doctrine and evolution access
6. apply recent-family repetition penalties
7. choose family
8. choose burden band inside valid ceiling
9. calculate amount or diplomatic condition
10. calculate duration
11. calculate valid substitute set
12. persist contract proof
13. create one mission and response actions
14. send participant and Africa reports

### Contract identity

Every demand receives a monotonically increasing owner-side sequence ID or a collision-safe participant-local ID joined to the system generation.

Every debit, completion, extension, substitute, and failure effect must verify the same contract identity. This prevents stale decisions from resolving a later demand.

### Amount rounding

Use family-specific readable steps, such as:

- rifles and support equipment in hundreds or thousands
- trucks and artillery in tens or hundreds
- tanks and aircraft in whole readable groups
- convoys and trains in whole units
- fuel in large round quantities
- factory burden in whole factories and whole days

Do not display fractional equipment or long decimal values.

## Demand resolution contracts

### Full compliance

The compliance effect should:

1. verify current contract and capacity
2. debit participant once
3. credit Africa once
4. record exact transferred amount
5. reduce Wrath through central helper
6. update hidden compliance history
7. extend participant cooldown
8. clear mission and response decisions
9. clear temporary contract state
10. queue grouped Africa report

### Equipment transfers

Use existing stockpile debit helpers where supported:

- infantry equipment
- support equipment
- motorized equipment
- convoys
- trains
- fuel

The receiving side needs an owner-local grant helper that resolves the same equipment token and exact amount. If a compatible shared helper already exists, reuse it. A new shared helper belongs in the dynamic registry only if several unrelated systems will call it.

### Partial payment

Partial payment should persist:

- amount requested
- amount paid
- amount remaining
- revised deadline
- partial status

The second payment must debit only the remaining amount.

### Substitute

The offer creator should persist up to three substitute family and amount pairs. Africa's response should read the frozen offer, not recalculate a different offer after the player clicks.

### Extension

An accepted extension should:

- update the mission deadline once
- add any agreed burden or upfront transfer
- set an extension-used flag for the contract
- block repeated extension unless a specific route authorizes it

### Failure

A failed demand should:

- lock resolution
- raise Wrath
- update hidden failure history
- call punishment evaluation once
- set the next demand date after punishment review
- clear active demand state

## Punishment evaluation contract

### Inputs

- participant and unifier proof
- current Strength band
- current Wrath
- failed demand band
- offense history
- failure count and recent streak
- global Chaos tier
- Event 012 evolution access
- target condition
- recent target and global punishment cooldowns
- recent punishment families

### Desired tier

Build a desired tier from Wrath, offense, failure history, and current hostility.

### Capability tier

Build a maximum tier from Strength, African capability, evolution, and Chaos channel access.

Suggested ceiling:

| Strength band | Maximum normal tier |
| --- | --- |
| Limited | I |
| Regional | II |
| Continental | III |
| Global | IV |
| Extreme | V after full gate |

### First-failure gate

A first ordinary refusal should cap at Tier I or Tier II depending on Strength and demand severity. A first refusal cannot reach Tier IV or Tier V.

### Tier V gate

Tier V requires separate explicit trigger proof for:

- extreme Strength
- very high Wrath
- high Chaos
- serious repeated failure or major offense
- evolution access
- no active target or global extreme cooldown
- Africa not collapsing
- valid emergency ultimatum route

### Family selection

Build a complete valid family pool for the chosen tier. Apply weights from offense relevance, target vulnerability, recent-family penalty, doctrine, and attribution risk.

Candidate families:

- diplomatic pressure
- unrest
- stockpile loss
- production disruption
- supply and rail damage
- port and convoy disruption
- military readiness loss
- building damage
- natural disaster gateway
- migration or famine consequence request
- sanctions
- direct African intervention
- exact population-loss sequence

### Disaster gateway

The owner should set documented `natural_disaster_call_*` inputs, call `call_natural_disaster = yes`, then inspect the result and proof outputs.

A rejected call should not be treated as success. It can produce a failed manifestation report or route to another valid family.

### Population-loss sequence

The extreme sequence should:

- select valid affected states through a bounded target set
- calculate requested loss per state from current civilian population
- preserve a minimum remaining population
- call `apply_exact_state_civilian_population_loss`
- inspect applied result
- record Deaths once
- stop when target and global caps are reached
- retain wave and contract proof across delayed events

## Protection contract

Protection uses the same capacity discipline in the opposite direction.

Inputs:

- hidden cooperation record
- low Wrath and no disqualifier
- African real capacity
- participant current need
- doctrine route
- protection cooldown

Outputs may include:

- equipment or fuel transfer
- expeditionary force path
- guarantee or alliance action
- reconstruction support
- Event 013 mitigation request
- famine or migration owner request
- demand leniency

A weak Africa should not grant a large army it does not possess.

## Africa-side selected-target pattern

Use the project selected-target decision pattern if target-specific actions are needed.

The owner category should have:

- participant array
- one visible target selector
- one close or clear selection action
- a selected participant flag
- a stored selected participant ID or event target
- selected-target visibility triggers
- cleanup when target becomes invalid
- AI access that does not depend on human selection

Only actions valid for the selected target should appear.

## Event ID allocation

The implementation should inspect Event 012's live namespace before reserving IDs.

Recommended role groups inside `chaosx.nr12.*`:

- activation and introduction
- demand issue and reports
- negotiation results
- punishment reports
- defiance and reconciliation
- Africa defeat
- continental settlement
- credibility super-event trigger

Do not reserve exact numeric suffixes from this planning document without checking collisions.

## Localisation data

Scripted localisation should resolve:

- current Strength value and band
- current Wrath value and band
- current trend
- current demand family
- amount and texticon
- deadline
- selected states or countries
- substitute offers
- African priority
- broad punishment risk
- qualitative relationship memory cues
- final settlement outcome

Player-facing text should never expose raw variable names, candidate weights, debug reasons, or internal family IDs.

## Event Log contract

Gods of Africa is not a new random event identity.

Major milestones should log under Event 012 with a system-specific detail subtype where the existing logger supports it.

Routine demand transactions belong to an owner ledger, not the main Events History list.

A transaction ledger may store recent entries for the player-facing category or reports. It should remain bounded.

## AI implementation contracts

Weighted surfaces include:

- participant response choice
- substitute acceptance
- extension acceptance
- permanent defiance decision
- African priority choice
- African participant target choice
- demand family choice
- punishment family choice
- protection target choice
- focus route choice

Every weighted surface needs:

1. complete candidate pool
2. named scenarios
3. baseline `hoi4.probability_inspect`
4. evaluation or sweep matching the question
5. source patch by the owning agent
6. `hoi4.probability_compare` using the same scenarios
7. unresolved classification when external factors remain incomplete

## DLC adapters

Core demand families need base-game behavior.

DLC may add:

- more precise market or equipment transfer methods
- improved aircraft or tank family resolution
- diplomatic embargo variants
- subject or autonomy interactions
- intelligence routes

Every adapter should:

- have an explicit DLC gate
- produce the same broad gameplay purpose
- leave a base-game route active
- fail closed without stale decisions

## Save and reload

Persist:

- system generation
- active status
- Strength
- participant registry
- Wrath
- active demand contract
- deadline
- payment progress
- defiance
- hidden history
- recent extreme cooldowns
- Africa priority and doctrine
- final settlement state

Rebuild only presentation and temporary decision activation after reload. Do not reroll the demand family, amount, punishment, or substitute set.

## Cleanup order

### System ending

1. set ending lock
2. stop dispatch
3. cancel active demand missions
4. cancel pending negotiations
5. cancel delayed punishment work that has not committed impact
6. clear selected-target state
7. issue participant-specific ending events
8. archive or clear active registry
9. remove categories and transient ideas
10. preserve final history proofs needed by Event 012

### Participant invalidation

1. remove from active array
2. clear active decisions and mission
3. clear target selection
4. cancel uncommitted punishment job
5. archive relevant history if a successor route uses it

## Validation requirements

Implementation evidence should include:

- event-chain inspect and compare
- decision and mission audit
- AI probability audit and compare
- Event 012 focus render and focus audit if the overlay branch is added
- GUI inspect and render only if a dedicated GUI is accepted
- task-specific population and disaster API tests
- multiplayer isolation scenarios
- save and reload contract tests
- Event 012 completion audit
- localisation audit
- authoritative XLSX update and CSV export

Live game validation belongs to the user unless the autonomous debug skill is explicitly invoked.
