# Event 54 Probability and Random-Selection Scenarios

These scenarios define the evidence expected from the AI Probability Auditor and HOI4 probability tools. They do not claim results before the implementation and live candidate pool exist.

## Evidence rules

Every scenario begins with `hoi4.probability_inspect` on the exact Event 54 candidate or cluster surface.

Use:

- `hoi4.probability_evaluate` for exact recipient draws and cluster member traces
- `hoi4.probability_sweep` for pool-size, provider-count, and participation sensitivity
- `hoi4.probability_compare` after any weight, candidate, or member change
- `hoi4.probability_simulate` only when a declared uncertain pool or campaign sample requires sampling
- `hoi4.probability_sequence` only when the complete repeatable-event and cluster cadence contract is supplied
- `hoi4.probability_render` for matrices, comparisons, sensitivity, and unresolved views

Every conclusion must be labeled exact, bounded, sampled, score-only, or unresolved.

## Technology-draw scenarios

### `E54-TECH-001`: Baseline ordinary minor

**World state:** 1936 start, small independent country, three or fewer research slots, no branch commitments, no custom pool.

**Grant target:** 1.

**Questions:**

- Is every eligible ordinary candidate equally weighted?
- Are doctrines and hidden technologies absent?
- Can future-year technologies participate?
- Does one selected technology appear exactly once?

**Required result:** Exact trace over the complete candidate pool.

### `E54-TECH-002`: Baseline ordinary major

**World state:** 1936 start, major country with a different starting technology set.

**Grant target:** 1.

**Questions:**

- Does the country use its own pool independently from the minor country's pool?
- Does major status change no candidate weight?
- Are already researched technologies absent?

**Required result:** Exact trace and candidate-pool comparison with `E54-TECH-001`.

### `E54-TECH-003`: Evolution I without replacement

**World state:** 250 Chaos, Evolution I enabled, ordinary pool only.

**Grant target:** 3.

**Questions:**

- Are three draws made without replacement?
- Is the pool revalidated after every grant?
- Can a first branch choice remove opposing candidates from draws two and three?

**Required result:** Exact multi-draw trace under at least two deterministic seeds.

### `E54-TECH-004`: Existing concentrated industry route

**World state:** Recipient already owns concentrated industry and related descendants.

**Grant target:** 3 or 5.

**Questions:**

- Are every dispersed industry candidate and alias removed?
- Can later concentrated nodes remain when safe?

**Required result:** Exact exclusion proof.

### `E54-TECH-005`: Uncommitted exclusive branch

**World state:** Recipient owns neither side of a mutually exclusive family.

**Grant target:** 10.

**Questions:**

- Can one side enter the draw?
- Does the opposite side disappear immediately after selection?
- Can no later slot grant the opposing branch?

**Required result:** Exact sequence proof and seeded sweep.

### `E54-TECH-006`: Evolution II expanded pool

**World state:** 450 Chaos, Evolution II enabled, at least three registered providers.

**Grant target:** 5.

**Questions:**

- Are ordinary and registered candidates in one eligible pool?
- Does every candidate have equal weight?
- Does one provider occupy an excessive share of the complete pool?
- Does a registered grant leave its owner lifecycle unchanged?

**Required result:** Exact pool share, candidate trace, and provider-count sensitivity.

### `E54-TECH-007`: Scientific Deluge

**World state:** 650 Chaos, Evolution III enabled, representative 1940 recipient.

**Grant target:** 10.

**Questions:**

- Does the transaction remain bounded?
- Are all ten grants distinct?
- Are branch conflicts impossible across all ten slots?
- Is the final report list complete?

**Required result:** Exact sequence trace plus runtime measurement from the implemented event chain.

### `E54-TECH-008`: Pool smaller than target

**World state:** Late-game country with four safe missing technologies.

**Grant target:** 10.

**Questions:**

- Does the country receive exactly four?
- Does processing stop after exhaustion?
- Is no excluded fallback selected?

**Required result:** Exact proof.

### `E54-TECH-009`: Zero eligible pool

**World state:** Country owns every safe candidate or has only excluded candidates missing.

**Grant target:** 5.

**Questions:**

- Does the country receive zero grants?
- Does the transaction continue for other countries?
- Does a human report explain exhaustion without exposing internal exclusions?

**Required result:** Exact proof.

### `E54-TECH-010`: Rejected owner callback

**World state:** One registered candidate enters the initial pool but fails its final owner eligibility check.

**Grant target:** 5.

**Questions:**

- Is the candidate removed for the current attempt?
- Does the country reroll without losing a slot?
- Can the candidate never create an infinite rejection loop?
- Does the owner state remain unchanged?

**Required result:** Exact trace.

### `E54-TECH-011`: Grant package overlap

**World state:** A registered candidate grants one selected technology and two required setup technologies.

**Grant target:** 5.

**Questions:**

- Does the package count as one Event 54 slot?
- Are all three researched nodes removed from later draws?
- Does the package contain only declared dependencies?

**Required result:** Exact trace and package inventory proof.

### `E54-TECH-012`: No-DLC graph

**World state:** Relevant DLC disabled.

**Grant target:** 5.

**Questions:**

- Are missing or replaced DLC nodes absent?
- Does the event use the active graph without substitution?
- Do reports show only valid localized technology names?

**Required result:** Exact candidate comparison with the corresponding DLC-enabled state.

### `E54-TECH-013`: Special research actor

**World state:** One special or nonhuman country uses ordinary research, while one system actor has no safe technology state.

**Grant target:** 3.

**Questions:**

- Is the research-capable special country included?
- Is the system actor excluded?
- Does the event avoid a blanket special-country exclusion?

**Required result:** Exact recipient proof.

### `E54-TECH-014`: Repeat firing

**World state:** Same recipient after one previous Event 54 firing.

**Grant target:** Current stage amount.

**Questions:**

- Are prior grants absent from the new pool?
- Is no receipt reused?
- Does repeat count change no candidate weight?

**Required result:** Exact before-and-after pool comparison.

### `E54-TECH-015`: Save and reload

**World state:** Save after grant commitment and before report acknowledgement.

**Questions:**

- Does reload preserve committed results?
- Can the report be reopened without regranting or rerolling?
- Is the firing sequence consumed once?

**Required result:** Event-chain and save-state evidence. Probability remains exact because the draw was already committed.

## Scientific Research cluster scenarios

### `E54-CLUSTER-001`: Full early roster

**World state:** 250 Chaos, all five members enabled and eligible, none fired.

**Questions:**

- Does the selected anchor fire?
- Is the expected optional-member count usually two or three in the declared model?
- Is Brilliant Scientist the rarest optional member?
- Is Gift from Scientists among the most common optional members?

**Required result:** Exact or bounded member probabilities with a complete candidate pool.

### `E54-CLUSTER-002`: Fire-once members exhausted

**World state:** Events 16 and 24 have fired, while Events 27, 54, and 60 remain eligible.

**Questions:**

- Can the cluster still fire?
- Do repeatable members retain valid participation?
- Does one missing fire-once member block nothing else?

**Required result:** Exact availability and member trace.

### `E54-CLUSTER-003`: Event 27 dual membership

**World state:** Event 27 is eligible in both Scientific Research and Military Preparation.

**Questions:**

- Is each membership represented independently?
- Does one cluster firing apply Event 27's repeatable weight and cap change once?
- Does Event 27 remain represented in both clusters after the firing under its normal repeatable state?
- Are severity and member data correct in each cluster?

**Required result:** Exact many-to-many membership proof.

### `E54-CLUSTER-004`: Gift and Research Failure co-occurrence

**World state:** Events 54 and 60 both participate and Event 60 selects the human country.

**Questions:**

- Do direct grants persist?
- Does reduced research capacity persist?
- Does neither event overwrite the other?
- Is the cluster counted once for pacing?

**Required result:** Exact event-chain trace.

### `E54-CLUSTER-005`: Disabled member

**World state:** Gift from Scientists disabled, other members available.

**Questions:**

- Is Event 54 skipped with the correct reason?
- Can the cluster still fire through another anchor?
- Are no Event 54 grants or reports created?

**Required result:** Exact skip proof.

### `E54-CLUSTER-006`: High-chaos evolved gift

**World state:** 650 Chaos, Event 54 participates through the cluster, Evolution III enabled.

**Questions:**

- Does Event 54 use Scientific Deluge inside the cluster?
- Does it still create one event history row and no extra pacing transaction?
- Do the cluster and evolution histories remain distinct?

**Required result:** Exact chain trace and rendered history evidence.

## Change-control scenario

Any later change to candidate eligibility, registered providers, grant count, candidate weight, cluster membership, participation logic, or member severity requires:

1. a baseline audit using the same scenario identifiers
2. the owner-applied change
3. `hoi4.probability_compare` against the prior scenario artifacts
4. a report of dominance, starvation, rank reversal, and unresolved external factors

No exact probability should be reported when the complete pool is unavailable.
