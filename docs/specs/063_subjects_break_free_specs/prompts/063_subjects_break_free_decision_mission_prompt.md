# Decision and mission prompt: Event 063 Subjects Break Free

Use `chaos-redux-decisions-missions` to implement the complete Event 063 decision and mission system. Follow `AGENTS.md`, `chaos-redux-events`, the shared system prompt, and all Event 063 spec files.

Read first:

- `docs/specs/063_subjects_break_free_specs/specs/063_subjects_break_free_spec_part_2_settlements.md`
- `docs/specs/063_subjects_break_free_specs/specs/063_subjects_break_free_spec_part_3_network_and_pact.md`
- `docs/specs/063_subjects_break_free_specs/specs/063_subjects_break_free_spec_part_5_decisions_missions_and_ai.md`
- `docs/specs/063_subjects_break_free_specs/quality/063_subjects_break_free_probability_scenarios.md`
- `docs/specs/063_subjects_break_free_specs/prompts/063_subjects_break_free_asset_prompt.md`

## Presentation choice

Use one ordinary decision category with:

- one small category icon
- one static category picture
- phase-specific category text
- Liberation Cohesion and its current band only after the Pact forms
- no separate scripted GUI window

Keep the category readable:

- normally show three to five decisions
- never show more than six decisions at once
- keep no more than three active missions
- rank and cap dynamic targets
- hide obsolete, impossible, dead, hostile, resolved, or cooldown targets
- replace opening actions with stronger later versions when the phase changes

Working labels in the spec identify roles. Write final decision and mission localisation from the defined viewpoint and purpose.

## Required phase families

### Phase 1: Independence settlement

For newly independent countries, implement the mapped actions for:

- wider recognition
- separation negotiation
- national command cleanup
- frontier preparation
- guarantee requests

For former overlords, implement the mapped actions for:

- formal recognition
- association terms
- suspension of strategic access
- restoration ultimatum
- mediation

Do not let a decision cancel independence. Recognition, access, claims, readiness, and war risk are the available levers.

### Phase 2: Liberation network

Implement bounded actions for:

- recognizing a fellow breakaway
- real equipment or logistics aid
- military advisers
- guarantee of a threatened state
- mediation of a former-overlord dispute
- support for a valid remaining subject

Supporting a subject can affect autonomy pressure, Event 063 candidate weight, recognition readiness, or a conditional future aid pledge. It must not release the country directly.

### Phase 3: Independence war

For breakaway participants, implement:

- support requests
- supply corridor
- front coordination
- mediation request

For supporters, implement:

- fulfillment of aid pledges
- volunteers
- guarantees
- direct intervention
- ceasefire pressure

Honor the support ladder. Material aid should be more common than direct entry. Direct Event 063 intervention is capped at three liberated-state interveners per theater. Hide direct-entry actions after the cap is reached or when access, capacity, or topology is invalid.

### Phase 4: Liberation Pact

Implement phased actions for:

- founding congress
- full-member invitation
- partner and observer offers
- membership objection
- leadership transfer
- coordinated defense
- pooled aid
- supply corridor
- volunteers
- collective guarantee
- member mediation
- recognition of new breakaways
- support for one remaining subject
- former-overlord recognition pressure
- censure, suspension, restoration of status, and dissolution where valid

Do not list every network state or every subject. Build a bounded priority pool for each action family.

## Required missions

Implement the five mapped mission families:

1. Secure Recognition, around 180 days with dynamic adjustment
2. Keep the Separation Peaceful, around 120 days
3. Prepare for Reconquest, around 90 days
4. Hold the Independence Front, tied to the opening war phase
5. Draft the Pact Charter, around 120 days

Mission success and failure must create the consequences defined in Part 5. Failure must not silently restore subject status, annex a country, or create a war that fails the safety gate.

A later phase replaces obsolete missions. Independence war replaces the peaceful-settlement mission. Recognition removes recognition preparation. Pact dissolution removes Pact missions.

## Cost rules

Use real costs from the spec:

- equipment
- support equipment
- artillery
- trucks and trains
- fuel
- convoys
- temporary civilian-factory use
- command power or military experience where command work is real
- stability or war support for divisive policies
- temporary division commitment
- relations, access, and Liberation Cohesion
- time and active mission capacity

Political power can support diplomacy. Do not price every action only in political power or command power. Use no more than four cost types for one action. Scale aid and logistics by target need, donor surplus, distance, and transport route.

Aid must transfer real donor capacity. No decision should create an unlimited stockpile. Repeated support to the same target requires cooldowns, target need, and diminishing value.

## Public value rule

Liberation Cohesion is the only persistent Event 063 number shown to the player. Keep candidate scores, settlement tension, invitation weights, intervention willingness, and internal trust hidden.

The Pact category and charter spirit must show:

- numeric cohesion
- current band
- causes of recent material gains or losses
- actions unlocked by the current band

Do not expose a ledger of hidden components.

## AI

Implement the actor behavior and ordering from Part 5 and the probability scenarios.

- newly independent AI chooses posture from relations, dependence, strength, threats, and support
- former-overlord AI recognizes, negotiates, contests, or seeks restoration from practical conditions
- network AI recognizes and aids relevant countries
- Pact AI protects cohesion and viable members
- factioned liberated states choose partner status
- no-access countries do not enter distant wars
- donors with severe shortages do not send large aid
- direct intervention remains less common than non-war support across ordinary cases

Run the full `hoi4.probability_inspect`, `evaluate`, `sweep`, `compare`, and declared simulation workflow. Resolve starved valid actions, dominant invalid actions, and rank reversals before completion.

## Ideas and cleanup

Implement the lifecycle of:

- Contested Sovereignty
- Former Authority Disputed
- Independence War Mobilization
- the four Pact Charter cohesion states

Use staged upgrades or replacements, not stacked duplicate copies. Every idea, mission, target row, promise, and cooldown needs a clear owner and exit condition.

## Required evidence

Provide:

- decision inventory by phase and actor
- mission inventory and concurrency proof
- cost table with real resource paths
- visibility and target-cap proof
- AI and probability audit
- save and reload tests
- multiplayer human-human settlement test
- cleanup test after recognition, war, re-subjugation, country loss, Pact exit, and Pact dissolution
- screenshots of the category in settlement, war, low-cohesion Pact, and high-cohesion Pact states
- asset crosswalk for category, decision, mission, and charter icons

Keep iterating until every accepted decision and mission row is implemented and the category remains clear in real campaign states.
