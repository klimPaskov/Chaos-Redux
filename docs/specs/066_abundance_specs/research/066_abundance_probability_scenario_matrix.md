# Event 066 Probability Scenario Matrix

## Evidence workflow

Every weighted surface starts with `hoi4.probability_inspect`.
The audit then selects `hoi4.probability_evaluate`, `hoi4.probability_sweep`, `hoi4.probability_simulate`, `hoi4.probability_compare`, or `hoi4.probability_render` according to the question.
Use `hoi4.probability_sequence` only when the manifest fully declares repeat cadence, weight recovery, cap reduction, cooldowns, removals, resets, and terminal states.

The first audit establishes baseline scenarios before tuning.
The implementation owner applies any changes.
The second audit uses `hoi4.probability_compare` against the same scenario identities.

Results must be labeled exact, bounded, sampled, score-only, or unresolved.

## Generation scenarios

| ID | Setup | Question | Expected evidence |
| --- | --- | --- | --- |
| GEN-01 | Ordinary major, no special mechanic, 24 equally weighted core candidates, Chaos below 200 | Is baseline generation broad and free of option-index bias | No family dominates outside sampling tolerance, each option position has the same marginal distribution |
| GEN-02 | Ordinary minor with exactly four valid candidates | Does the generator produce four distinct single cards | Every wave contains all four candidates in randomized order |
| GEN-03 | Special country with three atomic candidates at baseline | Does pool failure fail closed | Country is excluded with a recorded reason, no dummy card appears |
| GEN-04 | DLC absent | Are DLC providers truly dormant | No DLC candidate enters the pool and no missing-DLC branch error occurs |
| GEN-05 | DLC present, country lacks the mechanic | Does mechanic ownership still gate the provider | Candidate remains absent |
| GEN-06 | DLC present, country owns the mechanic | Does the candidate join without changing Event 66 core | Candidate appears at declared weight and can be selected |
| GEN-07 | Country-specific mechanic active | Does its owner provider compete with generic values | Candidate appears without tag-only false positives |
| GEN-08 | Active harmful crisis | Is the harmful value eligible before Evolution I | Candidate has baseline eligibility and its harm class does not zero its weight |
| GEN-09 | Same controlled pool at Chaos below 200 and at 200+ with Evolution I enabled | Does Strange Abundance shift the same pool | Rare, owner-specific, active-crisis, and harmful odds rise by the declared ordering while ordinary candidates remain material |
| GEN-10 | Evolution I disabled at 200+ | Does disabling remove the shift | Distribution matches baseline weighting within sampling tolerance |
| GEN-11 | Evolution II enabled, Low, Standard, Medium, and High profiles | Does pair frequency follow severity | Pair share rises in the order Low, Standard or Medium, High, while every profile retains singles |
| GEN-12 | Evolution II disabled at 400+ | Are pairs fully suppressed | Pair count is zero |
| GEN-13 | Evolution III enabled with Evolution II enabled, all four profiles | Do triples define the stage | Triple share rises by severity, Standard and Medium have triples as the largest cardinality group, High is triple-dominant, Low retains strong pair presence |
| GEN-14 | Evolution III enabled while Evolution II disabled | Is cardinality safely suppressed | No pairs or triples, Evolution III cardinality effect is inactive |
| GEN-15 | Large pool with 120 candidates across 20 providers | Are low-weight providers starved | Every positive-weight family appears across a sufficiently large sample, dominance matches declared weights |
| GEN-16 | Recent candidate and family memory active | Does novelty dampen without banning | Recent items appear less often for the bounded memory period and remain possible |
| GEN-17 | Pair and triple pool with exact duplicates and hard storage conflicts | Are safety rerolls narrow | Duplicates and hard conflicts never survive, thematic contradictions remain allowed |
| GEN-18 | Four cards with the same candidates in different orders | Is signature normalization correct | Reversed ordering cannot create a duplicate card |
| GEN-19 | One provider returns malformed weight or display data | Is provider failure isolated | Faulty candidates are removed, other providers still generate four cards where possible |
| GEN-20 | Repeated save and load before selection | Is the roll persistent | Card identities and option order remain byte-equivalent or logically identical |

## Provisional cardinality target bands

These are tuning bands for controlled test pools, not final universal probabilities.
The complete provider pool can require adjustment while preserving the ordering.

| Stage and profile | Singles | Pairs | Triples |
| --- | ---: | ---: | ---: |
| Baseline or Evolution I | 100% | 0% | 0% |
| Evolution II Low | 65% to 80% | 20% to 35% | 0% |
| Evolution II Standard | 50% to 65% | 35% to 50% | 0% |
| Evolution II Medium | 45% to 60% | 40% to 55% | 0% |
| Evolution II High | 30% to 45% | 55% to 70% | 0% |
| Evolution III Low | 15% to 30% | 35% to 50% | 25% to 40% |
| Evolution III Standard | 5% to 20% | 25% to 40% | 45% to 60% |
| Evolution III Medium | 5% to 15% | 25% to 35% | 50% to 65% |
| Evolution III High | 5% to 10% | 15% to 30% | 65% to 80% |

Every stage keeps a nonzero single-card path when its row permits singles.
No exact percentage is accepted without complete-pool evidence.

## AI choice scenarios

| ID | Setup | Expected card ordering |
| --- | --- | --- |
| AI-01 | Stable peacetime major, four useful core singles | Card with real headroom and strategic fit leads, saturated or irrelevant card trails |
| AI-02 | Major at war with near-empty fuel and active air and armor forces | Fuel abundance leads comparable Political Power, Stability, and Navy Experience choices |
| AI-03 | Minor at war with severe manpower shortage | manpower leads a safe administrative value when both can apply fully |
| AI-04 | Stable country with one clearly harmful crisis card and three useful safe cards | Harmful card has the lowest score but remains selectable |
| AI-05 | Desperate country near capitulation, mixed pair gives manpower plus harmful pressure | Mixed pair can lead a safe low-impact single when immediate survival value is large |
| AI-06 | Four harmful cards with different severity and reversibility | AI chooses the least destructive or most reversible card probabilistically, no generic fallback appears |
| AI-07 | Special Chaos country whose owner treats panic or contamination as strategically useful | Owner route preference can reverse ordinary harm penalty without altering generation |
| AI-08 | High-profile triple with three saturated values versus useful single | Useful single can lead despite lower cardinality |
| AI-09 | Pair with two strong values versus pair with one strong and one severe harmful value | Safe strong pair leads for a stable ordinary AI |
| AI-10 | Unknown or contextual owner value | Unknown value receives neutral bounded treatment, not automatic zero or maximum |
| AI-11 | Same four card scores in four option orders | Final choice distribution is invariant to option position |
| AI-12 | One card invalidates before resolution | Invalid card leaves the choice set, remaining scores renormalize |

## Cluster scenarios

| ID | Setup | Expected result |
| --- | --- | --- |
| CLU-01 | Low Event 66 slot selected alone | One Low-profile world wave |
| CLU-02 | Medium slot selected alone | One Medium-profile world wave |
| CLU-03 | High slot selected alone | One High-profile world wave |
| CLU-04 | Low and Medium slots selected together | One Medium-profile wave with bounded slot-count pressure |
| CLU-05 | All three Event 66 slots selected | One High-profile wave, one history row, one cap change, one pacing result |
| CLU-06 | Three Event 66 slots in cluster candidate pool with other members | Effective Abundance incidence matches intended cluster balance after coalescing |
| CLU-07 | High slot selected below 400 Chaos | Four single cards, no pair gate bypass |
| CLU-08 | High slot selected at 400+ with Evolution II disabled | Four single cards |
| CLU-09 | High slot selected at 600+ with Evolutions II and III enabled | Triple-dominant profile within target band |

## Sequence and repeat scenarios

Run these only when the full repeatable-event manifest is declared.

| ID | Setup | Expected result |
| --- | --- | --- |
| SEQ-01 | Event 66 repeated under default weight recovery and cap reduction | Firing cadence matches shared Minor Repeatable rules |
| SEQ-02 | Same country across four Event 66 waves with novelty memory | Candidate repetition is reduced but remains possible |
| SEQ-03 | Human country leaves one choice pending across a later wave | Pending country is skipped and old cards are unchanged |
| SEQ-04 | First manifestation followed by several repeats | Direct Event 66 Chaos is `+5` once and zero thereafter |
| SEQ-05 | Evolution thresholds crossed between waves | Next wave records eligible enabled stages in order and uses their generation rules |

## Rendering and report

Use probability render views when they improve review of:

- cardinality by evolution and profile
- candidate-family frequency
- Evolution I before and after comparison
- option-index symmetry
- AI score and choice comparison
- cluster effective incidence after coalescing
- repeat diversity over sequence samples

The final audit report must name the scenario IDs, complete candidate pools, external factors, random seeds when sampled, sample sizes, confidence limits, unresolved assumptions, and exact source revision.
