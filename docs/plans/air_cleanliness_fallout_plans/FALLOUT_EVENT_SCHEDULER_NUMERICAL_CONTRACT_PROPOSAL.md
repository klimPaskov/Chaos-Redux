# Fallout living-world scheduler numerical contract proposal

## Status

Proposed for explicit user approval. None of the values in this document are authorized for gameplay implementation until the user accepts the contract.

This proposal fills the numerical gaps deliberately left out of the dormant schema-2 scheduler substrate. It defines ordinary candidate scoring, fatigue, cadence, visible-budget reservation, queue caps, deterministic selection, and coordinator batch limits. It does not define event prose, event choices, branch results, successor packages, or scheduler activation.

## Existing accepted substrate

This proposal does not reopen these implemented and accepted facts:

- the Fallout timeline has Ash week, First season, First winter year, Consolidation, Rival orders, New states, Soot retreat, Second world, and Open continuation phases
- Ash week ends after day 7 and the ordinary scheduler remains quiet through that interval
- the primary event families and nineteen nonzero cooldown families keep their current stable identities
- every country has twenty fatigue array entries including the permanent zero entry at index 0
- one country may hold no more than three unresolved major arcs
- a global broadcast normally requires a thirty-day global gap
- ordinary, arc, delayed-result, bilateral, cancellation, cleanup, and dispatch receipts keep their current exact transaction identities
- an issued receipt remains a blocking tombstone until its exact event-owned terminalizer consumes it
- the stable post-allocation registry remains the only country pool
- the survival ledger, region, government archetype, country memory, cause memory, Air Winter values, crisis resources, characters, and bilateral partners remain inputs rather than substitutes for event content
- human and hidden AI routes use the same costs, outcomes, memory, delayed results, and cleanup
- both scheduler activation flags remain unset
- suffixes `100` through `126` remain reservations with zero defined blocks and zero release-floor credit

The dormant 10 through 14 day ordinary cooldown constants are not an accepted pacing contract. Several are shorter than the accepted normal fourteen-day popup floor. They also count only the opening and would overshoot the ten-year visible target when delayed results are included. Approval of this proposal supersedes those unused values with the table below.

## Proposed decisions

Approval accepts all decisions in this document as one numerical contract.

1. Country size uses the frozen successor assignment state count.
2. Human successors receive a bounded daily review lane. AI successors use a bounded registry batch.
3. Ordinary cadence depends on timeline phase and frozen country size.
4. Every opening reserves visible budget for its complete scheduled envelope.
5. A major crisis may break cadence once under an exact seven-day and 180-day rule.
6. Family fatigue ranges from 0 through 100, rises by 60 at an accepted opening, and decays by one point per elapsed day.
7. Candidate scores use the exact additive formula in this document.
8. Deterministic ties use stable numeric identities and never randomness.
9. Major arcs, delayed rows, bilateral rows, characters, repeated states, and repeatable events have exact caps and recurrence rules.
10. Save recovery preserves committed selection and issued envelopes without rescoring or reissuing them.
11. Hidden AI uses the same selection inputs except for the explicitly human-only player-relevance input.
12. Numerical implementation remains dormant and contributes no event blocks to the release floor.

## Frozen country size

Country size is calculated once from the exact states committed to the successor assignment row.

| Size | Frozen assigned states |
| --- | ---: |
| Small | 1 through 3 |
| Medium | 4 through 9 |
| Large | 10 or more |

Later conquest, annexation, state transfer, or fragmentation does not rewrite this pacing identity. A country with no frozen assigned state cannot receive a scheduler row and fails closed.

## Host-owned review lanes

The existing Fallout coordinator remains the only request owner. The numerical implementation may extend its bounded registry work but may not add a daily or monthly all-country on-action.

Once per engine date, the coordinator performs these lanes in order:

1. reconcile one current receipt row from each compact transaction family using the existing cursors
2. process every current human successor in the frozen player-continuation array once
3. process a bounded number of nonhuman registry countries from the existing stable cursor

The AI batch is determined without division or rounding:

| Frozen scheduler registry count | AI countries reviewed per date |
| --- | ---: |
| 1 through 30 | 1 |
| 31 through 60 | 2 |
| 61 through 90 | 3 |
| 91 or more | 4 |

Human countries are skipped when encountered by the AI cursor. The cursor advances through the frozen registry order and wraps to index 0. A country may commit at most one new selected envelope on one engine date. Due results, callbacks, cancellations, and cleanup take priority over a new opening. This is bounded registry work, not a new world-country iterator.

Literal multiplayer lobby-host authority remains an engine blocker. This contract does not treat the deterministic coordinator as proof of lobby-host identity and does not authorize activation while that blocker remains.

## Ordinary cadence

The base cooldown is selected from the current Fallout phase and frozen country size.

| Phase | Small | Medium | Large |
| --- | ---: | ---: | ---: |
| First season, days 8 through 90 | 24 | 18 | 14 |
| First winter year, days 91 through 365 | 28 | 24 | 20 |
| Consolidation, days 366 through 730 | 32 | 28 | 24 |
| Rival orders, days 731 through 1460 | 34 | 30 | 26 |
| New states, days 1461 through 2190 | 36 | 32 | 28 |
| Soot retreat, days 2191 through 2920 | 38 | 34 | 30 |
| Second world, days 2921 through 3650 | 40 | 36 | 32 |
| Open continuation, day 3651 onward | 46 | 42 | 38 |

Ash week has no ordinary cooldown value because ordinary selection is disabled. Orientation owns its fixed sequence and the seven-day quiet period.

### Visible-budget cost

Every candidate declares an integer `visible_budget_cost` from 1 through 4. The value counts the visible opening and every visible result or callback already promised by that reservation before the next independent opening.

Examples:

- one self-contained visible incident costs 1
- a visible opening and one visible delayed result cost 2
- an opening, a visible conflict beat, and a visible result cost 3
- four already scheduled visible beats cost 4

The opening reservation calculates:

```text
reserved_cooldown_days = phase_size_base_cooldown * visible_budget_cost
requested_due_day = current_day + reserved_cooldown_days
ordinary_cooldown_due_day = maximum(existing_due_day, requested_due_day)
```

Every later visible result in that envelope also requests `current_day + phase_size_base_cooldown`. It may extend the existing due day but can never shorten the opening reservation. Hidden AI results, mechanical callbacks, and cleanup events have zero visible-budget cost. An AI opening still reserves the same narrative envelope against that AI country's local cooldown so AI simulation does not race through chains.

The declared cost is part of the immutable ordinary, delayed, arc, or bilateral request payload. A retry with a different cost is not the same transaction.

### Ten-year pacing arithmetic

If a country always has eligible content and every visible beat consumes its reserved share, the phase table produces these approximate day-8-through-day-3650 totals:

| Frozen size | Ordinary visible beats | Eleven visible Ash-week beats | Ten-year baseline |
| --- | ---: | ---: | ---: |
| Small | 103.9 | 11 | 114.9 |
| Medium | 118.0 | 11 | 129.0 |
| Large | 136.2 | 11 | 147.2 |

Candidate droughts, war, loss of valid targets, route locks, and player choices can lower those totals. Rare crisis breaks can raise them. The baseline sits inside the accepted 90 through 180 meaningful visible event target without treating every event block as campaign content.

## Crisis and broadcast cadence

A candidate may use the crisis break only when all of these are true:

- it is classed as a crisis incident
- its normalized unresolved mechanic pressure is at least 80
- no crisis break was committed for that country in the previous 180 days
- at least seven days have elapsed since the country's last visible Fallout popup
- the exact crisis target and crisis resource remain current

An accepted crisis break sets its own last-break day and reserves `42 * visible_budget_cost` days. It cannot be used to bypass a pending issued receipt, due delayed result, or unresolved same-crisis transaction. A crisis with lower pressure waits for ordinary cadence.

A broadcast keeps the accepted thirty-day global minimum. It also consumes visible budget cost 1 for every human country that receives it. A broadcast does not clear or shorten an existing local cooldown. World-rewrite presentation and the Fallout blackout are outside the broadcast class.

## Family fatigue

Fatigue entries are integer values from 0 through 100. Index 0 is always zero.

Each country stores `fallout_event_fatigue_last_update_day`. Before candidate scoring:

```text
elapsed_days = maximum(current_day - fatigue_last_update_day, 0)
fatigue[i] = maximum(fatigue[i] - elapsed_days, 0) for indexes 1 through 19
fatigue_last_update_day = current_day
```

The decay transaction writes all nineteen values before it writes the update day. Repeating the transaction on the same day changes nothing.

When an opening dispatch receipt is committed, its cooldown family gains 60 fatigue and clamps at 100. The last cooldown-family identity is written in the same commit. Results, callbacks, cleanup, cancellation before issue, and a failed issue attempt do not add fatigue. An issued opening that later resolves as failure, partial success, or aborted after choice still adds fatigue because the narrative family was presented.

The last cooldown family is a hard veto for the next independent opening. If every otherwise valid candidate belongs to that family, no event is selected. The scheduler does not weaken the veto or invent a fallback.

## Primary-family base weights

Transition and orientation do not enter ordinary candidate selection. The other families use these base weights:

| Primary family | Base weight |
| --- | ---: |
| Global survival and society | 40 |
| Regional and biome | 42 |
| Government archetype | 42 |
| Successor country memory | 48 |
| Character and leader | 44 |
| Diplomacy, trade, war, and settlement | 40 |
| Cause memory and altered fiction | 38 |
| Recovery and late world order | 42 |

Every manually reviewed candidate may add an authored adjustment from minus 10 through plus 10. A value outside that band invalidates the candidate row. The adjustment may not be used to bypass a missing region, archetype, memory, character, target, or phase gate.

## Candidate scoring

All normalized input values are clamped to 0 through 100 before use. Fixed-point contributions are added without intermediate rounding. The complete score is rounded once after every addition and deduction.

```text
score = primary_family_base
      + authored_adjustment
      + phase_suitability
      + 0.30 * severity
      + 0.25 * unresolved_mechanic_pressure
      + 0.10 * player_relevance
      + 0.10 * state_value
      + region_match
      + government_match
      + country_memory_match
      + cause_memory_match
      + winter_match
      + crisis_resource_match
      + character_match
      + bilateral_opportunity
      + route_match
      + previous_choice_match
      + recent_war_or_crisis
      + arc_capacity_adjustment
      - family_fatigue
      - repeated_state_penalty
      - repeatable_event_penalty
```

The exact fixed contributions are:

| Input | Contribution |
| --- | ---: |
| Preferred phase | 30 |
| Supported secondary phase | 15 |
| Exact region match | 20 |
| Exact government-archetype match | 20 |
| Exact country-memory match | 20 |
| Exact terminal-cause memory match | 15 |
| Exact Air Winter condition match | 15 |
| Exact survival-resource crisis match | 25 |
| Required recurring character available | 15 |
| Valid bilateral partner and relationship opportunity | 15 |
| Exact focus, decision, or government route match | 15 |
| Supporting previous choice memory | 12 |
| Recent war or crisis explicitly relevant to the event | 20 |

An event can mark a dimension neutral. A neutral dimension gives zero. If the event marks a dimension required, mismatch makes the candidate ineligible instead of applying a penalty.

### Normalized pressure inputs

The candidate row must name the exact live or durable source for every nonzero normalized input.

- Resource pressure is `2 * clamp(50 - current_resource, 0, 50)`.
- Air Winter pressure uses phase values 0, 15, 30, 45, 65, 85, and 100 for phases 0 through 6.
- Severity is event-owned evidence such as disease, exposure, damage, war loss, active siege, displacement, or a bilateral dispute. Its formula belongs in the reviewed event contract.
- State value is event-owned evidence of why the exact target matters. It can use survival value, capital identity, infrastructure, population, institution, route, or resource evidence named by that event.
- Player relevance is 100 when the recipient country is human, 50 when an AI recipient's exact bilateral partner is human, 25 when an AI event contract names a current war or mission target owned by a human, and 0 otherwise. Use only the highest applicable value. Human lane priority therefore does not depend on an invented state-selection interface.

An event cannot assign a nonzero severity, state value, or player-relevance input without a named script receipt. Working labels and prose are not evidence.

### Arc capacity adjustment

Only candidates that open a new major arc use this adjustment:

| Active major arcs | Adjustment |
| --- | ---: |
| 0 | 10 |
| 1 | 0 |
| 2 | -20 |
| 3 | ineligible |

Continuation events for an already reserved arc do not use this adjustment. They authenticate their parent ticket and use the delayed or callback lane.

### Positive eligibility

After the single final rounding, a candidate must have a score greater than 0. Zero or a negative score is not eligible. No minimum-score fallback exists.

## Repetition and target memory

Each country stores the two most recent visible state targets and their issue days.

- Targeting the same state once within 90 days applies a 35-point penalty.
- A third visible incident about that state within 120 days is ineligible.
- A current capital or active siege may bypass the third-incident veto, but it still takes the 35-point penalty.
- A nonrepeatable event with a completed memory is ineligible forever for that country.
- A repeatable event is ineligible for 90 days after its last opening and takes a 50-point penalty through day 365.
- A repeatable event has no event-recency penalty after day 365.

The exact event token and target identity are stored before the visible-history commit marker. State history is updated only after an opening dispatch receipt is current.

## Characters and bilateral partners

A recurring character or institution actor already owned by an unresolved arc, delayed row, or bilateral row cannot open another arc. The actor identity must pass the existing cross-family uniqueness proof.

A bilateral candidate is eligible only when:

- both countries have current scheduler and survival rows
- the partner is not the source country
- both directions pass the exact relationship and target gates
- neither side has a conflicting issued bilateral receipt
- the exact pair has not opened the same bilateral family in the previous 90 days
- both sides remain within the bilateral row cap

When several partners qualify, compare the complete candidate score with the partner-specific opportunity input. An exact tie uses the lower frozen partner registry index. The reservation still writes both reciprocal rows before either side can receive an event.

## Transaction caps

| Surface | Cap per country |
| --- | ---: |
| Outstanding ordinary opening receipt | 1 fixed receipt |
| Active major arcs | 3 |
| Delayed and callback rows | 8 |
| Bilateral rows including cleanup-pending rows | 6 |
| Independent arcs for one character or institution | 1 |
| Newly selected envelope per engine date | 1 |

Cleanup-pending and issued tombstone rows count against their cap until exact release. A cap failure makes the candidate ineligible. It does not discard an older row, allocate a larger array, or substitute a simpler event.

A delayed or callback reservation must use a due day from 1 through 730 days after its parent transaction. Longer stories advance through reviewed arc stages and create a new bounded reservation only after the previous stage terminalizes.

## Deterministic selection

The scheduler evaluates only candidates whose manually registered phase and identity pool can match the country. It does not build a random global pool.

The winner is selected by this stable order:

1. higher final candidate score
2. crisis incident before major-arc opening, relationship, routine incident, and broadcast when scores tie
3. lower stable candidate identity
4. lower stable target state or country identity
5. lower bilateral partner registry index

Due result, callback, cancellation, and cleanup envelopes do not compete with new candidates. They use their committed ticket and take transaction priority. No `random`, `random_list`, or MTTH roll resolves an exact tie.

The selected row freezes generation, registry index, phase, mode, candidate identity, event tokens, primary family, cooldown family, visible-budget cost, final score, target, partner, parent arc, character, issue day, due day, and every candidate-specific branch token before its pending marker. A retry must match that immutable payload exactly.

## Hidden AI parity

The scheduler selects AI candidates from the same eligibility gates and numerical score. Player relevance follows the exact recipient, partner, war, and mission rules above. It can raise an AI event that directly affects a human campaign, but it cannot change costs or outcomes.

The selected control mode is frozen in the dispatch envelope. A control change while an envelope or result is pending does not convert the existing route. The next independent candidate uses current control state.

Hidden AI roots use event-owned branch weights based on archetype, resources, war, route, characters, and previous memory. They pay the same costs, reserve the same arc and delayed rows, use the same deterministic result partitions, mutate the same fatigue, and run the same cleanup. Hidden AI cannot receive a free branch, reduced cost, guaranteed success, or invisible reward loop.

## Save recovery and cleanup

Numerical implementation must follow these commit rules:

1. decay fatigue idempotently to the current day
2. calculate and freeze every candidate input
3. choose one winner by stable comparison
4. reserve required ordinary, arc, delayed, character, or bilateral rows
5. reserve the complete visible-budget due day
6. write the selected payload
7. write the pending selection marker last
8. create the dispatch envelope
9. write the dispatch-issued receipt before running the event command
10. add fatigue and visible history exactly once against that issued opening

A save before issue may retry the exact frozen selection. It does not rescore live inputs or allocate a second ticket. A save after issue sees the issued tombstone and may not emit the command again. A stale generation cancels an unissued selection with a typed reason. An issued selection remains owned by its exact event terminalizer.

If a target or partner becomes invalid before issue, the transaction cancels without fatigue or visible-history mutation. If it becomes invalid after issue, the exact event-owned cancellation path consumes the envelope, records the cancellation memory, and performs cleanup. Generic reconciliation may not erase an issued row.

Schema promotion may add these numerical receipts only to a completely dormant current-generation row while both activation flags are absent. It may not fabricate fatigue history, event recency, country size, player targets, or an issued payload for an active or legacy Fallout campaign.

## Release and activation boundary

Approval of this document authorizes a dormant numerical implementation only. It does not authorize either scheduler activation setter.

Activation remains blocked until all of these are true:

- the complete Ash-week orientation chain has callers, logs, details, assets, runtime rows, and audits
- successor allocation and player continuation are proven
- the candidate registry and every selected event pool are manually reviewed
- at least 660 unique Fallout event blocks pass content, AI, memory, delayed-result, cleanup, localisation, asset, log, detail, and documentation review
- ordinary, arc, delayed, character, bilateral, crisis, broadcast, save-recovery, and cleanup scenarios pass static audit
- literal host authority or an explicitly accepted engine-supported authority contract is proven
- scheduler debug presentation exposes phase, cooldown, fatigue, score, selected candidate, target, partner, ticket, and cleanup state during development
- the activation setter receives a separate final review

Expansion toward 910 blocks begins only after the 660-block floor passes review. No reservation, generated draft, or hidden helper counts as an event block.

## Proposed implementation order after approval

1. Promote this accepted numerical design into the living-world source specs.
2. Replace the dormant cooldown constants with typed phase-and-size values.
3. Promote the scheduler schema with frozen size, fatigue day, visible history, crisis break, repeatable event, selection, and queue-cap receipts.
4. Add pure candidate-input and score triggers plus clamp-owning calculation effects.
5. Add idempotent fatigue decay and opening-commit mutation.
6. Add bounded human and AI review lanes to the existing coordinator.
7. Add visible-budget reservation to ordinary, delayed, bilateral, and broadcast wrappers.
8. Add deterministic candidate and partner comparison.
9. Add development-only score and receipt presentation.
10. Validate with a small manually reviewed candidate registry while both activation flags remain unset.

No living-world event block should be added merely to test the selector. The first content pilot requires its own accepted event contract and manual review.

## Static acceptance scenarios

The numerical implementation must prove at least these cases without launching HOI4:

1. A one-state human successor with continuous eligible content remains near 115 visible beats over ten years before rare crisis variation.
2. A medium successor remains near 129 visible beats under the same assumption.
3. A large successor remains near 147 visible beats and never uses an ordinary cooldown shorter than fourteen days.
4. A two-popup envelope reserves twice the base budget and its result cannot shorten that reservation.
5. A family opened at fatigue 0 commits fatigue 60 once, decays by exact elapsed days, and cannot immediately repeat.
6. Two equal candidates choose the lower stable candidate identity regardless of registry iteration order.
7. A country with three active major arcs cannot open a fourth but can receive an authenticated continuation.
8. A third recent event about one noncapital nonsiege state is rejected.
9. A character reserved by one arc cannot open a second arc.
10. A bilateral reservation either commits both reciprocal rows or commits neither.
11. A full delayed or bilateral queue rejects a new candidate without deleting existing content.
12. A save before issue retries one frozen selection and a save after issue emits no second command.
13. Human and hidden AI routes expose the same branch costs and result partitions and reserve the same fatigue, delayed rows, and cleanup for the same selected candidate.
14. No activation setter, ordinary event caller, or block in suffixes `100` through `126` appears in the numerical tranche.

## Engine evidence and limitations

The proposal is based on the offline Data structures, Triggers, Effects, Scopes, On actions, Event modding, Localisation, AI modding, Decision modding, Idea modding, and Modifiers pages. Installed documentation was reviewed for variables, arrays, `for_loop_effect`, `for_each_scope_loop`, `check_variable`, scope variables, event commands, script constants, and sequential fixed-point arithmetic.

Repository precedents are the current Fallout scheduler transaction substrate, `006_independence_wave_effects.txt` and its triggers for aligned stable registries, `020_black_plague_effects.txt` for delayed scheduler state, and the Air Winter event scheduler for bounded candidate ownership and stable tie-breaking.

HOI4 was not run. Runtime cost, save interruption, multiplayer observation, popup cadence, and literal host behavior remain unobserved. Those are release gates and not reasons to invent a fallback.

## Approval record

No approval is recorded yet. If accepted, record the user's approval here and promote the complete contract into the source specifications before implementing its values.
