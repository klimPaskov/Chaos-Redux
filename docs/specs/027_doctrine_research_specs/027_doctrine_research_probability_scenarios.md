# Event 027: Doctrine Research probability and AI audit scenarios

## Purpose

Event 027 gives every AI country direct doctrine choices. The AI must use those choices well enough that a human player does not receive a systematic advantage from global symmetry.

This file defines named scenarios and expected ordering. It does not prescribe final numeric weights.

The probability auditor must distinguish score evidence from normalized probability evidence. A branch score is not a click probability unless the complete candidate pool, every modifier, and the final selection operation are present.

## Mandatory audit route

For each weighted surface:

1. Use `hoi4.probability_inspect` to identify the exact source, candidates, modifiers, external factors, and normalization model.
2. Record whether the pool is complete.
3. Use `hoi4.probability_evaluate` for fixed named scenarios.
4. Use `hoi4.probability_sweep` for important changing inputs.
5. Use `hoi4.probability_simulate` only when seeded sampling helps test bounded randomness.
6. Use `hoi4.probability_compare` after any source change, using the same scenarios.
7. Use `hoi4.probability_render` when a ranking, sensitivity, timing, or comparison view improves review.
8. Use `hoi4.probability_sequence` only when the complete repeatable-event pool and sequence contract are declared.

The auditor remains read-only. The parent agent chooses the intended balance target and applies changes.

## Weighted surfaces

The implementation should expose separate auditable surfaces for:

- Event 027 automatic selection from the repeatable-event pool
- National Breakthroughs cluster participation when Event 027 is optional
- AI doctrine-domain choice
- AI Grand Doctrine choice inside an empty domain
- AI track choice inside an active Grand Doctrine
- AI subdoctrine choice inside an empty track
- AI choice allocation across a two-to-five-choice batch

## Scenario group A: Domain selection

### DR-A01: Doctrine-less land major

**State**

- major country
- large field army
- active land war
- several military factories producing land equipment
- no Grand Doctrine selected in Army, Navy, or Air
- modest coastline and small fleet
- limited aircraft production

**Expected ordering**

1. Army
2. Air
3. Navy

Army should have a clear lead. Bounded randomness should not make Navy a frequent winner.

**Failure signals**

- every domain has equal score
- major status alone gives Navy or Air a dominant score
- missing doctrine state creates zero scores for all domains

### DR-A02: Island naval power

**State**

- island or archipelago country
- significant navy and dockyards
- active convoy war
- overseas strategic plan
- smaller land army
- no Navy Grand Doctrine
- Army Grand Doctrine already active with incomplete tracks

**Expected ordering**

Navy should compete strongly with Army and normally lead when convoy losses and overseas plans are severe. Army remains valid because it already has useful progress.

**Failure signals**

- Army wins automatically due an unconditional land preference
- Navy remains low despite fleet, coastline, and war factors
- the AI cannot select an empty Navy domain while Army is active

### DR-A03: Air-centered continental power

**State**

- large aircraft industry
- active air war
- several air wings
- air-focused strategic plan
- Army doctrine active
- Air domain empty
- moderate land war

**Expected ordering**

Air should lead or remain within the top bounded pool. Army may win when a near-complete Army branch has immediate value.

**Failure signals**

- Air production and air war do not affect the score
- active Army doctrine blocks Air adoption

### DR-A04: Landlocked small minor

**State**

- no coastline
- no fleet or dockyards
- small field army
- little aircraft production
- no doctrines selected
- defensive land threat

**Expected ordering**

Army should lead clearly. Air may remain a secondary option. Navy should be invalid or close to zero according to native availability and AI strategy.

**Failure signals**

- Navy receives neutral weight because every valid domain starts equal
- major-only factors leave the minor with no useful choice

### DR-A05: Future maritime plan

**State**

- currently landlocked or nearly landlocked country
- focus route and AI strategy target a coastal expansion
- planned dockyard construction and naval invasion
- no current fleet
- Army doctrine active
- Navy domain empty

**Expected ordering**

Navy should rise above the ordinary landlocked score. It need not dominate unless the planned maritime commitment is near and credible.

**Failure signals**

- current coastline is a permanent zero-weight blocker despite an explicit route plan
- scripted route preference forces Navy after the route becomes invalid

### DR-A06: All ordinary domains complete

**State**

- Army, Navy, and Air content fully complete
- no eligible conditional or custom domain

**Expected result**

No candidate. The batch closes without compensation.

**Failure signals**

- the AI selects a fully mastered branch
- the system grants military experience as fallback
- an invalid custom domain appears to keep the pool nonempty

## Scenario group B: Grand Doctrine selection

### DR-B01: Mobile armored army

**State**

- empty Army domain
- high tank production
- several armored divisions
- offensive plan across open terrain
- sufficient fuel

**Expected ordering**

A mobile or armored Grand Doctrine should rank above infantry-mass or static-defense choices when those are the current graph alternatives.

The exact doctrine names depend on the installed graph.

### DR-B02: Manpower-rich infantry state

**State**

- empty Army domain
- infantry-heavy force
- limited armor production
- large manpower reserve
- defensive or broad-front war

**Expected ordering**

Infantry, mass, defensive, or irregular approaches should rise according to the current graph and country strategy.

### DR-B03: Doctrine plan conflict

**State**

- historical AI plan prefers one Grand Doctrine
- current force composition strongly favors another
- the historical plan remains active

**Expected behavior**

The result should reflect the intended balance between country identity and campaign evidence. A strong historical preference can lead, but severe campaign mismatch should reduce its dominance.

The audit must report ordering under both historical and alternate AI plans.

### DR-B04: Invalid doctrine candidate

**State**

- one Grand Doctrine is missing a DLC, country gate, or valid selection action
- several other doctrines are valid

**Expected result**

The invalid candidate has zero participation and cannot be selected.

## Scenario group C: Track and branch selection

### DR-C01: Near-complete relevant branch

**State**

- active Army Grand Doctrine
- armor branch one event mastery step from completion
- country fields armored divisions and produces tanks
- infantry branch has lower levels and moderate relevance

**Expected ordering**

Armor should lead clearly. Completion and force fit reinforce each other.

### DR-C02: Near-complete irrelevant branch

**State**

- naval branch one step from completion
- country has almost no fleet and no naval plan
- land branch has strong current-war relevance

**Expected ordering**

The land branch should lead. Completion value alone should not overpower a severe strategic mismatch.

### DR-C03: Empty track fills missing capability

**State**

- active Grand Doctrine
- one empty operations or logistics track
- severe supply problems
- several partially developed combat tracks

**Expected ordering**

An eligible operations or logistics branch should gain enough value to compete strongly. The AI should be able to select a new branch and should not always stack existing branches.

### DR-C04: Four equal tracks

**State**

- four valid tracks
- similar force fit
- similar current levels
- no immediate completion
- four-choice batch

**Expected behavior**

Seeded simulation should show bounded variation and meaningful distribution. One fixed track should not win every choice. Continuity can produce some stacking, but the AI should frequently develop more than one track.

### DR-C05: One dominant track

**State**

- one branch has strong force fit, route fit, active-war fit, and completion value
- other branches have weak or neutral fit
- five-choice batch

**Expected behavior**

The AI should stack several choices in the dominant branch and finish it when possible. After completion, it must recalculate and move to the next valid target.

### DR-C06: Branch completes between choices

**State**

- first Event 027 choice advances a branch
- native faction sharing or combat completes it before the second choice resolves

**Expected behavior**

The second choice pool excludes the completed branch. The AI does not waste a choice or use a stale score.

### DR-C07: Banked mastery on empty track

**State**

- empty track
- enough banked mastery to unlock one or more native levels on branch selection
- several eligible subdoctrines

**Expected behavior**

The selected branch follows AI fit. Native banked progress remains intact. Event attribution records at most one additional event mastery step.

The scenario remains unresolved until the local engine sequence is proven.

## Scenario group D: Custom doctrine selection

### DR-D01: CBRN-ready Chaos Warfare country

**State**

- Chaos Warfare establishment prerequisites satisfied
- doctrine not yet selected
- chemical and biological investment
- fielded CBRN headquarters and support formations
- active unconventional-warfare plan
- ordinary Army domain also valid

**Expected ordering**

Chaos Warfare should compete strongly and may lead. It must remain a valid domain adoption. It cannot become a direct downstream unlock.

### DR-D02: CBRN-unready ordinary country

**State**

- missing Chaos Warfare establishment requirements
- no CBRN route or equipment
- ordinary Army, Navy, and Air domains valid

**Expected result**

Chaos Warfare is absent from the candidate pool.

### DR-D03: Active Chaos Warfare, infantry-heavy formations

**State**

- Chaos Warfare active
- Hazard Assault formations fielded
- limited armored-delivery equipment
- limited projector batteries
- four valid tracks

**Expected ordering**

Hazard Assault Formations should lead. Integrated CBRN Command may compete when headquarters and protection systems are strong.

### DR-D04: Active Chaos Warfare, theater command need

**State**

- strong CBRN headquarters network
- active contamination and biological threats
- air and surface coordination need
- several operations gates approaching

**Expected ordering**

Integrated CBRN Command should lead or compete strongly.

### DR-D05: Special nonhuman country without adapter

**State**

- live special country
- no coherent ordinary or custom doctrine adapter

**Expected result**

No candidate and no fabricated doctrine reward.

### DR-D06: Special country with valid adapter

**State**

- live special country
- owner-defined custom doctrine adapter
- valid branch pool

**Expected result**

The country participates through that adapter. Identity classification alone does not suppress it.

## Scenario group E: Multi-choice sequence

### DR-E01: Evolution I adoption sequence

**State**

- two-choice batch
- selected domain empty
- at least one eligible Grand Doctrine and track

**Expected sequence**

Choice 1 can adopt the Grand Doctrine. Choice 2 can select or advance one track in the newly active doctrine.

### DR-E02: Evolution II mixed services

**State**

- three-choice batch
- Army active with one high-value branch
- Navy empty with credible maritime plan
- Air active with moderate value

**Expected behavior**

The AI may stack Army, adopt Navy, or split across services according to score. Scores must recalculate after Navy adoption.

### DR-E03: Evolution III broad curriculum

**State**

- four-choice batch
- four tracks with close scores

**Expected behavior**

Distribution across several tracks should occur often enough that the AI can use broad-development play. The exact rate is a balance target chosen by the parent after evidence.

### DR-E04: Evolution IV branch completion

**State**

- five-choice batch
- one fresh five-level branch is the clear strategic fit

**Expected behavior**

The AI can direct all five choices into the branch and complete it. This should be possible, not guaranteed in every close-score case.

### DR-E05: Queue with different stages

**State**

- active baseline batch with one unresolved choice
- Event 027 fires later at Evolution II and queues a three-choice batch

**Expected sequence**

The first batch remains one choice. The second begins with three choices after the first closes. No merge into four choices occurs.

### DR-E06: Evolution unlock during batch

**State**

- two-choice Evolution I batch active
- Evolution II unlocks before choice 2

**Expected sequence**

The active batch remains two choices. The next normal firing grants three.

## Scenario group F: Repeatable-event and cluster selection

### DR-F01: Initial event pool

**State**

- Event 027 enabled and unfired
- complete current repeatable-event pool declared
- baseline recovery and cap settings

**Expected evidence**

Report Event 027's normalized chance and ranking without assuming it dominates because it has default starting weight.

### DR-F02: After first firing

**State**

- Event 027 has fired once
- its cap has been reduced through the shared repeatable system
- scheduled monthly recovery declared

**Expected evidence**

Show the event's bounded recovery and lower cap relative to unfired repeatable events.

### DR-F03: Sequence through four firings

**State**

- complete event-pool manifest
- timer cadence, monthly recovery, cap reduction, event removals, major reset behavior, and cluster behavior declared

**Expected evidence**

Use sequence analysis only when the complete pool is available. Determine whether Event 027 can recur at a reasonable declining frequency and whether it starves other positive events.

### DR-F04: Event 027 optional cluster member

**State**

- another National Breakthroughs member selected
- Event 027 eligible
- complete cluster member pool and participation factors declared

**Expected evidence**

Evaluate Event 027's optional participation and total cluster-size distribution. The cluster should usually produce a limited group, not every member.

### DR-F05: Event 027 selected cluster member

**State**

- Event 027 selected by the random event picker
- cluster roll succeeds

**Expected result**

Event 027 fires once as the guaranteed selected member. No optional-member logic can schedule a second fanout.

## Scenario group G: Human parity and validity

### DR-G01: Human and AI pool parity

For a fixed country state, inspect the human-visible valid pool and AI candidate pool.

**Expected result**

Every AI candidate is a valid human action, and every valid human action can enter AI scoring. Human navigation pages do not create hidden extra doctrine options.

### DR-G02: DLC matrix

Evaluate all supported DLC combinations that change doctrine content.

**Expected result**

Unavailable content has zero participation. Available domains preserve their current graph and order. Conditional adapters activate only under proven rules.

### DR-G03: Invalid adapter injection

Introduce a test adapter with a missing branch identity or unknown maximum mastery.

**Expected result**

The adapter fails closed. Other domains remain valid. No bad subdoctrine reaches a mastery trigger or effect.

## Required comparison report

The final probability audit should include:

| Surface | Baseline scenario IDs | Patched scenario IDs | Evidence type | Pool completeness | Intended ordering met | Remaining uncertainty |
| --- | --- | --- | --- | --- | --- | --- |

The report should highlight:

- any candidate that dominates across unrelated scenarios
- any valid domain that is consistently starved
- any invalid candidate with positive weight
- any sequence where Event 027 recurs too frequently
- any evolved batch where AI fails to recalculate
- any custom doctrine whose score ignores owner-system readiness
- any difference between human and AI candidate pools

## Acceptance standard

Weighted logic is ready when the named scenarios demonstrate the intended ordering, invalid candidates remain at zero, bounded randomness preserves variety, multi-choice batches recalculate after every action, and post-patch comparison shows no new dominance or starvation problem.
