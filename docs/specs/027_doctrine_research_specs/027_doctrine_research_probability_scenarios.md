# Event 027: Doctrine Research probability and AI audit scenarios

## Purpose

Event 027 gives every AI country direct doctrine choices, so the AI must spend them well enough that global symmetry gives human players no systematic advantage.
This file names the scenarios and their expected ordering.
It never prescribes numeric weights, which live in the Event 027 script constants.

Route weighted audits through `chaosx_ai_probability_auditor` and the `chaos-redux-subagents` skill, which own the tool workflow and the rule that a score is not a click probability unless the whole pool, every modifier, and the final selection are bound.
The auditor is read-only, and the parent chooses balance targets.

## Weighted surfaces

| Surface | Source | Evidence status |
| --- | --- | --- |
| AI domain choice | `doctrine_research_ai_score_domains` | Groups A and D evaluated after D6, D17, and D18 (`probability_domain_compare_2026-10-04.md`, `probability_domain_round2_2026-10-05.md`). |
| AI Grand Doctrine choice | `doctrine_research_ai_score_selected_grand` | Group B evaluated after D16 and D19 (`probability_native_preferences_2026-10-05.md`, `probability_track_round2_2026-10-05.md`). |
| AI track choice | `doctrine_research_ai_score_selected_track` | Group C and DR-D03, DR-D04 evaluated after D19 (`probability_track_round2_2026-10-05.md`). |
| AI subdoctrine choice | `doctrine_research_ai_score_selected_subdoctrine` | DR-C07 variants evaluated after D25 (`probability_subdoctrine_round3_2026-10-05.md`); the later change that resets only a zero native product to the base weight, so fractional factors such as 0.5 keep their effect, has scenario inputs in `probability_subdoctrine_zero_reset/` but no recorded comparison yet. |
| Multi-choice allocation | the AI loop in `027_doctrine_research_effects.txt` | Group E evaluated only as single-choice pools; no batch timeline is bound. |
| Automatic event selection | shared event picker and repeatable recovery | Group F unresolved. |
| Optional cluster participation | National Breakthroughs loader | Unconstructible until a second member exists. |

Evidence files live in `docs/plans/027_doctrine_research_plans/`, and `agent_decisions_2026-10-04.md` records each decision the evidence supports.
Real-campaign mixes remain a live check.

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

Army should have a clear lead.
Bounded randomness should not make Navy a frequent winner.

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

Navy should compete strongly with Army and normally lead when convoy losses and overseas plans are severe.
Army remains valid because it already has useful progress.

**Failure signals**

- Army wins automatically through an unconditional land preference
- Navy remains low despite fleet, coastline, and war factors
- the AI cannot select an empty Navy domain while Army is active

### DR-A03: Air-centred continental power

**State**

- large aircraft industry
- active air war
- several air wings
- air-focused strategic plan
- Army doctrine active
- Air domain empty
- moderate land war

**Expected ordering**

Air should lead or remain within the top bounded pool.
Army may win when a near-complete Army branch has immediate value.

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

Army should lead clearly.
Air may remain a secondary option.
Navy should be invalid or close to zero according to native availability and AI strategy.

**Failure signals**

- Navy receives neutral weight because every valid domain starts equal
- major-only factors leave the minor with no useful choice

### DR-A05: Future maritime plan

**State**

- currently landlocked or nearly landlocked country
- a credible plan to gain a coast
- no current fleet
- Army doctrine active
- Navy domain empty

**Expected ordering**

Navy should rise above the ordinary landlocked score.
It need not dominate unless the maritime commitment is near and credible.
The implementation reads the plan from a core or claim on a coastal state the country does not control, or a war goal, held or being justified, against a coastal owner (D17).

**Failure signals**

- current coastline is a permanent zero-weight blocker despite an explicit plan
- the plan keeps raising Navy after the claim or war goal is gone

### DR-A06: All ordinary domains complete

**State**

- Army, Navy, and Air content fully complete
- no eligible conditional or custom domain

**Expected result**

No candidate.
The batch closes without compensation.

**Failure signals**

- the AI selects a fully mastered branch
- the system grants military experience as fallback
- an invalid custom domain appears to keep the pool nonempty

## Scenario group B: Grand Doctrine selection

### DR-B01: Mobile armoured army

**State**

- empty Army domain
- high tank production
- several armoured divisions
- offensive plan across open terrain
- sufficient fuel

**Expected ordering**

A mobile or armoured Grand Doctrine should rank above infantry-mass or static-defence choices.

### DR-B02: Manpower-rich infantry state

**State**

- empty Army domain
- infantry-heavy force
- limited armour production
- large manpower reserve
- defensive or broad-front war

**Expected ordering**

Infantry, mass, defensive, or irregular approaches should rise according to the current graph and country strategy.

### DR-B03: Doctrine plan conflict

**State**

- the country's native AI preference favours one Grand Doctrine
- current force composition strongly favours another

**Expected behaviour**

The result should balance country identity against campaign evidence.
A strong native preference can lead, but a severe campaign mismatch should reduce its dominance.
The audit reports the ordering with and without the native country factor.

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
- armour branch one mastery step from completion
- country fields armoured divisions and produces tanks
- infantry branch has lower levels and moderate relevance

**Expected ordering**

Armour should lead clearly.
Completion and force fit reinforce each other.

### DR-C02: Near-complete irrelevant branch

**State**

- naval branch one step from completion
- country has almost no fleet and no naval plan
- land branch has strong current-war relevance

**Expected ordering**

The land branch should lead.
Completion value alone should not overpower a severe strategic mismatch.

### DR-C03: Empty track fills missing capability

**State**

- active Grand Doctrine
- one empty operations or logistics track
- severe supply problems
- several partially developed combat tracks

**Expected ordering**

An eligible operations or logistics branch should gain enough value to compete strongly.
The AI should be able to select a new branch and should not always stack existing branches.

### DR-C04: Four equal tracks

**State**

- four valid tracks
- similar force fit
- similar current levels
- no immediate completion
- four-choice batch

**Expected behaviour**

Seeded simulation should show bounded variation and meaningful distribution.
One fixed track should not win every choice.
Continuity can produce some stacking, but the AI should frequently develop more than one track.

### DR-C05: One dominant track

**State**

- one branch has strong force fit, route fit, active-war fit, and completion value
- other branches have weak or neutral fit
- five-choice batch

**Expected behaviour**

The AI should stack several choices in the dominant branch and finish it when possible.
After completion, it must rescore and move to the next valid target.

### DR-C06: Branch completes between choices

**State**

- first Event 027 choice advances a branch
- native faction sharing or combat completes it before the second choice resolves

**Expected behaviour**

The second choice pool excludes the completed branch.
The AI does not waste a choice or use a stale score.

### DR-C07: Banked mastery on empty track

**State**

- empty track
- enough banked mastery to unlock one or more native levels on branch selection
- several eligible subdoctrines

**Expected behaviour**

The selected branch follows AI fit, and a banked or fitting subdoctrine clearly leads.
Native banked progress remains intact.
Event attribution records at most one additional mastery step.
The banked level the AI reads for an unassigned subdoctrine is a live check.

## Scenario group D: Custom doctrine selection

### DR-D01: CBRN-ready Chaos Warfare country

**State**

- Chaos Warfare establishment prerequisites satisfied
- `land` folder empty
- chemical and biological investment
- fielded CBRN headquarters and support formations
- active unconventional-warfare plan

**Expected ordering**

Chaos Warfare should compete strongly with the Army Grand Doctrines for the empty `land` folder and may lead.
It remains an adoption and never becomes a direct downstream unlock.

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
- Hazard Assault battalions fielded
- limited armoured-delivery detachments
- limited projector batteries
- four valid tracks

**Expected ordering**

The Infantry track (Hazard Assault Formations) should lead.
The Operations track (Integrated CBRN Command) may compete when headquarters and protection systems are strong.

### DR-D04: Active Chaos Warfare, theatre command need

**State**

- strong CBRN headquarters network
- active contamination and biological threats
- several operation gates approaching

**Expected ordering**

The Operations track (Integrated CBRN Command) should lead or compete strongly.

### DR-D05: Special nonhuman country without adapter

**State**

- live special country classified as actually nonhuman
- no Kruger exception and no custom adapter

**Expected result**

No candidate and no fabricated doctrine reward.

### DR-D06: Special country with valid adapter

**State**

- live special country
- owner-defined custom doctrine adapter
- valid branch pool

**Expected result**

The country participates through that adapter.
Identity classification alone does not suppress it.
No current special country registers such an adapter, so this scenario applies to the first one that does.

## Scenario group E: Multi-choice sequence

### DR-E01: Evolution I adoption sequence

**State**

- two-choice batch
- selected domain empty
- at least one eligible Grand Doctrine and track

**Expected sequence**

Choice 1 can adopt the Grand Doctrine.
Choice 2 can assign or advance one track in the newly active doctrine.

### DR-E02: Evolution II mixed services

**State**

- three-choice batch
- Army active with one high-value branch
- Navy empty with a credible maritime plan
- Air active with moderate value

**Expected behaviour**

The AI may stack Army, adopt Navy, or split across services according to score.
Scores must be recalculated after the Navy adoption.

### DR-E03: Evolution III broad curriculum

**State**

- four-choice batch
- four tracks with close scores

**Expected behaviour**

Distribution across several tracks should occur often enough that the AI uses broad development.
The exact rate is a balance target chosen by the parent after evidence.

### DR-E04: Evolution IV branch completion

**State**

- five-choice batch
- one fresh five-level branch is the clear strategic fit

**Expected behaviour**

The AI can direct all five choices into the branch and complete it.
This should be possible, not guaranteed in every close-score case.

### DR-E05: Queue with different stages

**State**

- active baseline batch with one unresolved choice
- Event 027 fires later at Evolution II and queues a three-choice batch

**Expected sequence**

The first batch remains one choice.
The second begins with three choices after the first closes.
No merge into four choices occurs.

### DR-E06: Evolution unlock during batch

**State**

- two-choice Evolution I batch active
- Evolution II unlocks before choice 2

**Expected sequence**

The active batch remains two choices.
The next normal firing grants three.

## Scenario group F: Repeatable-event and cluster selection

The shared picker selects across every registered event, not only repeatable ones.
A firing resets Event 027's weight and halves its maximum cap, and weight recovers on the minor and major event pacing pulses rather than on a monthly hook.
Scenarios in this group must bind that real pool and cadence before they claim a probability.

### DR-F01: Initial event pool

**State**

- Event 027 enabled and unfired
- the complete current automatic-selection pool declared, with live eligibility, weights, and caps

**Expected evidence**

Event 027's normalised chance and rank, without assuming dominance from its default starting weight.

### DR-F02: After first firing

**State**

- Event 027 has fired once, its cap halved
- recovery declared per event pacing pulse

**Expected evidence**

Bounded recovery and a lower cap than unfired events.

### DR-F03: Sequence through four firings

**State**

- complete event-pool manifest
- timer cadence, pulse recovery, cap reduction, event removals, major reset behaviour, and cluster behaviour declared

**Expected evidence**

Whether Event 027 recurs at a reasonable declining frequency and whether it starves other positive events.
Sequence analysis is valid only with the complete pool.

### DR-F04: Event 027 optional cluster member

**State**

- another National Breakthroughs member selected
- Event 027 eligible
- complete member pool and participation factors declared

**Expected evidence**

Event 027's optional participation and the total cluster-size distribution, which should usually stay at two or three members.
This scenario cannot be built until a second member joins the runtime cluster.

### DR-F05: Event 027 selected cluster member

**State**

- Event 027 selected by the random event picker
- cluster roll succeeds

**Expected result**

Event 027 fires once as the guaranteed member, and no optional-member logic schedules a second fanout.
Source flow already shows the trigger row is excluded from the optional roll and dispatched first; no activation probability has been measured.

## Scenario group G: Human parity and validity

### DR-G01: Human and AI pool parity

For a fixed country state, inspect the human-visible valid pool and the AI candidate pool.

**Expected result**

Every AI candidate is a valid human action, and every valid human action can enter AI scoring.
Human navigation pages create no hidden extra doctrine options, and the general staff option (R5, pending) uses the AI pool unchanged.

### DR-G02: DLC matrix

Evaluate every supported DLC combination that changes doctrine content.

**Expected result**

Unavailable content has zero participation.
Available domains keep their current graph and order.
Conditional adapters activate only under proven rules.

### DR-G03: Invalid adapter injection

Introduce a test adapter with a missing branch identity or an unknown maximum level.

**Expected result**

The adapter fails closed.
Other domains remain valid.
No bad subdoctrine reaches a mastery trigger or effect.

## Reporting

The final audit lists, per surface, the baseline and patched scenario IDs, evidence type, pool completeness, whether the intended ordering is met, and the remaining uncertainty.
It highlights any candidate that dominates unrelated scenarios, any valid domain that is starved, any invalid candidate with positive weight, any sequence where Event 027 recurs too often, any evolved curriculum where the AI fails to rescore, any custom doctrine whose score ignores owner readiness, and any difference between human and AI pools.

Weighted logic is ready when the named scenarios show the intended ordering, invalid candidates stay at zero, bounded randomness preserves variety, multi-choice curricula rescore after every action, and the post-patch comparison shows no new dominance or starvation.
