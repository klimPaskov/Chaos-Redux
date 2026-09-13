# Event 063 probability and timing scenarios

## Purpose

Event 063 contains several weighted systems:

- subject candidate selection
- release-count variation inside a pool-size band
- Evolution I cohort-host selection
- settlement posture and former-overlord response
- Evolution activation timing
- recognition and support target selection
- Pact congress invitations
- independence-war intervention level

The implementation must be audited through the Chaos Redux probability tools. The scenarios below define expected ordering, dominance limits, starvation limits, and timing bands. They do not claim exact final probabilities for campaign-dependent pools.

## Required probability tool sequence

1. `hoi4.probability_inspect` for every Event 063 `ai_chance`, `random_list`, weighted candidate pool, and evolution MTTH block.
2. `hoi4.probability_evaluate` for each named scenario in this file.
3. `hoi4.probability_sweep` across autonomy, relative strength, overlord weakness, mutual opinion, claim severity, current war load, network support, distance, access, and Liberation Cohesion.
4. `hoi4.probability_compare` after implementation changes.
5. `hoi4.probability_simulate` for the declared mixed-pool examples and any other scenario with uncertain external inputs.
6. `hoi4.probability_sequence` only when the full release pool and post-selection state transitions are declared.
7. `hoi4.probability_render` for candidate rankings, settlement matrices, timing sensitivity, and intervention ladders when a rendered view makes review easier.

The coding agent must provide the auditor with the actual scripted conditions and the declared assumptions. A source-only guess is not sufficient.

## Candidate-selection scenario family

## CS-01: Autonomy and overlord weakness matter

Pool contains two otherwise comparable subjects.

### Candidate A

- high autonomy
- credible armed forces
- weak overlord
- overlord is losing a war
- moderate relations
- no cooldown

### Candidate B

- low autonomy
- weak armed forces
- stable overlord
- strong mutual opinion
- high dependence
- no cooldown

Expected result:

- Candidate A has at least about 2.5 times Candidate B's selection weight.
- Candidate B keeps a nonzero valid floor.
- Candidate A must not become a guaranteed selection when several other strong candidates exist.

Failure signs:

- autonomy or overlord weakness has little visible effect
- the loyal integrated subject outranks Candidate A
- Candidate B has zero weight only because it is loyal
- one factor alone forces a 100 percent outcome

## CS-02: High autonomy under a strong overlord remains relevant

Candidate has high autonomy and a functional army. The overlord is stable and strong, relations are neutral, and no network state supports the subject.

Expected result:

- weight is lower than the same subject under a collapsing overlord
- weight remains above a deeply integrated loyal subject
- the candidate stays viable at low Chaos

## CS-03: Liberation-network support can compensate for small size

Candidate is a small subject with moderate autonomy, hostile relations, and strong recognition or aid pledges from liberated states. The overlord is stronger.

Expected result:

- network support raises the candidate into a competitive middle band
- network support does not make it certain
- removal of the support flags produces a clear weight decline

## CS-04: Cooldown blocks rapid recycling

A country was freed by Event 063, later became a subject again, and is inside the target cooldown.

Expected result:

- hard cooldown state blocks selection or reduces it to the defined protected state
- after expiry, the country returns to a normal low or medium weight based on live conditions
- the first-origin record does not alter cooldown behavior

## CS-05: Protected owner transaction outranks all weight

A high-autonomy subject would otherwise be the strongest candidate, but Independence Wave or Soviet Collapse currently owns a protected replacement or release transaction affecting it or its states.

Expected result:

- candidate is excluded regardless of political weight
- no fallback weight can bypass the reservation
- the event uses another frozen candidate or safely reduces the completed batch

## CS-06: Same-overlord diversity at baseline

Pool contains six subjects of Overlord A, three of Overlord B, and two of Overlord C. Several candidates under A have the highest individual weights. Evolution I is inactive.

Expected result:

- the first picks favor strong candidates
- later picks receive a meaningful diversity pressure toward B and C
- the event can still select more than one subject under A
- the whole baseline batch should not routinely come from A when valid alternatives exist

## CS-07: Coordinated cohort under Evolution I

Use the same pool as CS-06 with Evolution I active.

Expected result:

- one eligible former overlord is selected as cohort host
- two to five compatible subjects under that host are selected together
- remaining slots return to the global pool
- only one cohort is created for that former overlord
- the largest empire does not automatically win every host roll

## Provisional candidate-weight calibration

A planning-only prototype used a positive floor and normalized factors for autonomy, relative strength, overlord weakness, hostility, claims, network support, loyalty, and dependence. It was not written as final script.

Illustrative archetype weights from that prototype:

| Archetype | Prototype weight |
| --- | ---: |
| High-autonomy subject under a weak wartime overlord | 142.25 |
| Integrated loyal subject under a stable overlord | 25.00 |
| Medium-autonomy subject under a strong overlord | 70.50 |
| Small but strongly network-backed subject | 93.00 |
| High-autonomy subject under a strong overlord | 98.75 |

A 200,000-run weighted sample selected three of these five archetypes without replacement. The illustrative inclusion rates were:

| Archetype | Inclusion rate in sample | First-pick rate |
| --- | ---: | ---: |
| High-autonomy, weak wartime overlord | 82.1% | 33.2% |
| Integrated loyal, stable overlord | 23.5% | 5.9% |
| Medium autonomy, strong overlord | 56.5% | 16.3% |
| Small, network-backed | 67.8% | 21.7% |
| High autonomy, strong overlord | 70.1% | 23.0% |

Interpretation:

- the high-pressure candidate leads without becoming certain
- the loyal integrated subject remains possible
- network support can make a small subject competitive
- sampling without replacement prevents one archetype from consuming several slots

These figures are planning evidence only. The implementation must be audited from its actual scripted weights.

## Release-count scenarios

## RC-01: One valid subject

Expected result: one release.

## RC-02: Four valid subjects

Expected result: two releases in ordinary circumstances.

## RC-03: Eight valid subjects

Expected result: two or three releases, with three favored when several candidates have strong pressure.

## RC-04: Fourteen valid subjects

Expected result: three or four releases.

## RC-05: Twenty-two valid subjects

Expected result: four or five releases.

## RC-06: Thirty valid subjects

Expected result: five or six releases at baseline.

## RC-07: Evolution I large pool

With thirty valid subjects and Evolution I active, expected result is a larger batch than baseline, normally six or seven, with a hard cap of eight.

## RC-08: Late invalidation

The target count is six. Five releases complete and one reserved country disappears before its turn. No frozen fallback remains because execution has begun.

Expected result: five completed releases and one skipped row. No rollback and no dynamic pool rebuild.

## Cohort-host fairness scenarios

A planning prototype used a sublinear subject-count factor combined with pressure. This prevents a large stable empire from winning only because it has many subjects.

Illustrative host shares in one four-overlord pool:

| Host archetype | Subject count | Pressure | Prototype host share |
| --- | ---: | ---: | ---: |
| Large empire, moderate pressure | 12 | Moderate | 33.9% |
| Medium empire, severe pressure | 5 | Severe | 29.2% |
| Small subject system, high pressure | 2 | High | 17.8% |
| Large stable system | 10 | Low | 19.2% |

Acceptance requirement:

- subject count matters
- current pressure matters at least as much as raw count
- a medium collapsing system can rival a larger stable system
- no valid host becomes impossible solely because it has only two subjects

## Settlement scenarios

## ST-01: Friendly high-autonomy separation at low Chaos

Conditions:

- high autonomy
- shared ideology
- positive opinion
- no major territorial dispute
- former overlord has a heavy external war load
- subject chooses Conciliatory or Guarded

Expected ordering:

1. negotiated separation
2. unilateral recognition
3. contested separation
4. armed refusal

Dominance target:

- negotiated and recognized outcomes combined should clearly dominate
- armed refusal should remain exceptional

## ST-02: Strategic integrated subject under a strong coercive overlord

Conditions:

- low autonomy
- valuable bases or resources
- hostile relations
- strong former overlord
- no external guarantee
- safe topology

Expected ordering at baseline:

1. contested separation
2. armed refusal
3. unilateral recognition
4. negotiated separation

Dominance limit:

- armed refusal should not exceed contested separation at baseline
- immediate war should not become a default result for every low-autonomy subject

## ST-03: Same case under Evolution II with a viable cohort

Conditions match ST-02, with two or more coordinated subjects and safe war topology.

Expected ordering:

1. contested separation or armed refusal, close enough that both occur materially
2. the other high-pressure outcome
3. unilateral recognition
4. negotiated separation

Acceptance range:

- armed refusal must be meaningfully more common than in ST-02
- it must remain below certainty
- one compound war must replace separate pair wars

## ST-04: Shared external war blocks immediate conflict

Conditions:

- former subject and overlord fight the same enemy on the same side
- the engine cannot safely separate them into a direct war
- relations are hostile and the overlord chooses restoration

Expected result:

- immediate armed refusal has zero practical weight
- contested wartime separation becomes the leading result
- later ultimatum or war can occur after topology becomes safe

## ST-05: Former overlord near capitulation

Conditions:

- high surrender progress
- several external fronts
- released state has a functional army
- foreign recognition is likely

Expected ordering:

1. unilateral recognition or negotiated separation
2. the other peaceful result
3. contested separation
4. armed refusal

## ST-06: Major core conflict

Conditions:

- each country holds or claims important territory of the other
- opinion is very low
- both have military capacity
- no common-war topology block

Expected result:

- contested and armed outcomes rise sharply
- the event creates only narrow claims or restore-subject goals
- the breakaway receives no broad free claims against the former overlord

## ST-07: Human timeout

A human subject answers, but the human former overlord does not.

Expected result:

- the stored pragmatic timeout selects recognition or association
- the timeout never selects restoration war for the silent human
- the pair resolves without pausing the event system


## ST-08: Several baseline armed refusals qualify

Conditions:

- Evolution II is inactive
- several selected subject and former-overlord pairs independently pass the safe war gate
- no pair is already at war

Expected result:

- only the highest-priority pair opens a new independence-war theater
- every other hostile pair enters contested separation
- the selected theater is based on strategic pressure and viability, not processing order

## Intervention scenarios

## IV-01: Distant weak supporter

Conditions:

- low military capacity
- no access
- low or moderate network trust
- no Pact membership

Expected ordering:

1. recognition or material aid
2. the other low-risk response
3. advisers only when transport exists
4. guarantee
5. direct entry at zero or near zero

## IV-02: Regional capable supporter

Conditions:

- shared border or clear route
- positive relations
- spare equipment
- manageable war load
- no Pact membership

Expected ordering:

1. material aid
2. advisers or volunteers
3. recognition
4. guarantee
5. direct entry

Direct entry remains rare.

## IV-03: High-cohesion Pact member

Conditions:

- Liberation Cohesion at least 75
- threatened member or invited breakaway
- clear access
- capable armed forces
- no major current war

Expected ordering:

- material aid and advisers remain common
- guarantees become much more competitive
- direct entry becomes meaningful but remains below the combined non-war support share

## IV-04: High cohesion without access

Conditions match IV-03, but no land, naval, or air route can support the theater.

Expected result:

- direct entry receives zero practical weight
- material aid uses only routes that actually exist
- diplomatic recognition, mediation, and indirect support rise

## IV-05: Direct-intervener cap reached

Three Event 063 liberated-state interveners have already joined the theater.

Expected result:

- further Event 063 direct-entry decisions are hidden or weight zero
- other supporters can still provide aid, volunteers if valid under ordinary rules, recognition, or mediation

## Pact invitation scenarios

## PI-01: Compatible unfactioned country

Conditions:

- active liberation origin
- no major claim dispute
- positive trust
- not in a faction
- credible threat or useful regional link

Expected result: full membership is favored.

## PI-02: Compatible country already in another faction

Expected result:

- partner status is favored
- forced faction departure has zero weight
- observer status is a valid fallback

## PI-03: Major core conflict with a member

Expected result:

- full membership is blocked or near zero
- mediation or observer status can appear
- shared origin does not override the conflict

## PI-04: Aggressive resubjugator

Candidate has liberated provenance but recently subjected another liberated state.

Expected result:

- invitation blocked or strongly penalized
- censure state must be resolved before membership

## PI-05: Founder with weak congress support

The invitation pool has six states, but only two are likely to accept full membership.

Expected result:

- AI founder does not call the congress yet
- it uses recognition, partner, or trust-building decisions first

## Evolution timing scenarios

## ET-01: Evolution I ordinary eligibility

Expected activation band: roughly 75 to 105 days after reaching 200 Chaos.

## ET-02: Evolution I strong cohort pressure

One overlord has five high-autonomy subjects and is losing a war.

Expected result: activation is faster than ET-01, but not immediate without the pre-fire opening rule.

## ET-03: Evolution II ordinary eligibility

Expected activation band: roughly 80 to 120 days after reaching 400 Chaos.

## ET-04: Evolution II unresolved contested cohort

Several subjects have already separated and one former overlord refuses recognition.

Expected result: faster than ET-03.

## ET-05: Evolution III ordinary eligibility

Expected activation band: roughly 100 to 150 days after reaching 600 Chaos.

## ET-06: Evolution III viable network

At least six compatible liberated states exist, two origins are represented, and a recent independence war created support links.

Expected result: faster than ET-05, but the Pact still waits for a congress.

## ET-07: Pre-fire evolved opening

Chaos is already above the threshold when Event 063 fires for the first time.

Expected result:

- eligible enabled evolutions activate before the release plan is built
- the first firing uses their behavior
- evolution activation adds no Chaos by itself

## Dominance and starvation limits

- no valid subject should become impossible solely because of loyalty, small size, ideology, or distance
- owner-system conflicts and hard cooldowns can create real zero weight
- peaceful settlement should dominate strong friendly cases
- contested settlement should dominate strong unresolved strategic cases
- armed refusal should be rare at baseline and material under Evolution II
- direct intervention should never dominate ordinary network support across the full population of supporters
- a high-cohesion capable regional Pact member can have a meaningful direct-entry chance
- a no-access country should have zero direct-entry chance
- Pact full membership should have zero chance for countries that remain in another faction

## Required implementation report

The probability audit report must include:

- inspected source locations
- all resolved weights and modifiers
- scenario inputs
- outcome rankings
- timing results
- threshold sweeps
- any rank reversal
- any starved valid option
- any dominant option above its intended limit
- before and after comparison for every correction
- rendered matrices or rankings where helpful
- unresolved uncertainty and the reason it remains uncertain
