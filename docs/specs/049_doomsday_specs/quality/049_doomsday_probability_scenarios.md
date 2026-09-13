# Event 049 Probability and Weighted-Logic Scenarios

## Audit contract

Every weighted or random surface begins with `hoi4.probability_inspect`.

Use exact evaluation when the complete candidate pool and all external factors are known. Use bounded or score-only evidence when the pool is incomplete. Use seeded simulation for incident variety and sequence behavior. Use `hoi4.probability_compare` after any source change to a weight, modifier, random list, MTTH, AI score, or target weight.

The probability auditor remains read-only and does not choose the balance target.

## Date-generation scenarios

| ID | Surface | Setup | Expected result | Evidence |
| --- | --- | --- | --- | --- |
| `DATE-01` | Predicted-date distribution | Baseline Event 49 at Chaos 600 with no pre-fire evolution. | All dates fall within the accepted two-to-four-year window. Middle dates are more common than either edge. | Inspect, sweep, seeded simulation, distribution render. |
| `DATE-02` | Predicted-date distribution | Pre-fire Evolution I at Chaos 850. | Date remains in the accepted window and does not become automatically shorter only because the evolution is active. | Compare against `DATE-01`. |
| `DATE-03` | Predicted-date distribution | Pre-fire Evolution II at Chaos 1100 with high world crisis. | The opening is stronger, while the date distribution still leaves enough time for advanced content or applies an explicit accelerated-phase rule. | Evaluate and sequence. |

## Opening Conviction scenarios

| ID | Surface | Setup | Expected result | Evidence |
| --- | --- | --- | --- | --- |
| `OPEN-01` | Opening Conviction | Chaos 600, limited wars, strong institutions. | Opening lands in the lower baseline band. | Evaluate. |
| `OPEN-02` | Opening Conviction | Chaos 750, global war, high deaths, severe disaster pressure. | Opening is higher than `OPEN-01` but remains within the baseline band unless a pre-fire evolution applies. | Compare. |
| `OPEN-03` | Opening Conviction | Evolution I pre-fire. | Opening falls within the accepted evolved band and exceeds comparable baseline cases. | Sweep and compare. |
| `OPEN-04` | Opening Conviction | Evolution II pre-fire. | Opening falls within the advanced band without automatically satisfying Final Vigil readiness. | Evaluate and inspect terminal state. |

## Country-weight aggregation scenarios

| ID | Surface | Setup | Expected result | Evidence |
| --- | --- | --- | --- | --- |
| `AGG-01` | Global aggregation | One very populous major at high local conviction, most countries low. | The major moves the global value materially but cannot dominate it alone. | Evaluate with complete country pool. |
| `AGG-02` | Global aggregation | Many small and medium countries at high conviction, skeptical majors. | Geographic breadth and country count can move the global value into a high stage. | Compare with `AGG-01`. |
| `AGG-03` | Microstate exploit | Release many tiny countries after Event 49 and set moderate local conviction. | Aggregate and terminal progress remain bounded. | Simulate sequence and compare. |
| `AGG-04` | Country removal | Annex a high-contribution country. | Its contribution is removed or transferred once with no ghost weight. | Sequence. |
| `AGG-05` | Civil-war split | Split one major into two civil-war sides. | Combined contribution does not double the original population weight. | Compare before and after split. |

## Society-current initialization scenarios

| ID | Surface | Setup | Expected ordering | Evidence |
| --- | --- | --- | --- | --- |
| `CUR-01` | Current mix | Stable democracy at peace with strong schools and civic groups. | Skeptical continuity and cooperative civic currents outrank revolutionary and state-loyalist currents. | Score inspection and sweep. |
| `CUR-02` | Current mix | Losing authoritarian belligerent with severe repression. | Pacifist, revolutionary, and avenging currents rise. Coercive state-loyalism remains possible. | Compare with `CUR-01`. |
| `CUR-03` | Current mix | Disaster-exposed island state with transport risk. | Survivalist, custodial, and relief currents rise without forcing one route. | Evaluate. |
| `CUR-04` | Current mix | Occupied colony with local councils and harsh occupation. | Communal and anti-authority currents rise through campaign conditions. No religion or culture receives a fixed automatic current. | Inspect factors. |
| `CUR-05` | Current mix | Same country under different war and institutional states. | The current ordering changes with campaign state. Static national stereotyping is absent. | Compare. |

## AI posture scenarios

| ID | Setup | Expected primary posture | Expected refusal |
| --- | --- | --- | --- |
| `POST-01` | Stable high-continuity democracy, low local conviction, at peace. | Civic Continuity. | Emergency Order and Nothing Left to Lose. |
| `POST-02` | High-conviction state with strong trusted civic and religious networks. | Concordat of Vigil. | Broad repression without violent movement evidence. |
| `POST-03` | Authoritarian state with strong police, moderate continuity, immediate capture risk. | Emergency Order. | Voluntary transfer at low organization. |
| `POST-04` | Industrial state under bombing, famine risk, or severe disaster exposure. | National Preparation. | Pure denial when public harm is obvious. |
| `POST-05` | Losing war, low War Support, strong pacifist organization, enemy open to contact. | Peace Before the End. | Final offensive without a plausible objective. |
| `POST-06` | Militarized regime under existential defeat with strong state-loyalist current. | Nothing Left to Lose. | Early demobilization. |
| `POST-07` | Same country one month later with no major shock. | Current posture remains stable. | Monthly oscillation. |
| `POST-08` | Major war reversal or evolution activation. | Emergency posture change becomes possible. | Free repeated switching. |

Evidence for all posture scenarios:

- Inspect the full candidate pool.
- Evaluate named scenarios.
- Sweep Conviction, stability, War Support, organization, and remaining time.
- Compare after any weight patch.
- Render the score matrix when it improves review.

## Evolution timing scenarios

| ID | Evolution | Setup | Expected result | Evidence |
| --- | --- | --- | --- | --- |
| `EVO-01` | The Last Calendar | Chaos 800, low Conviction, strong global continuity. | Eligible but relatively slow, with no instant activation. | MTTH inspect and sweep. |
| `EVO-02` | The Last Calendar | Chaos 900, high Conviction, several major confirmations. | Faster than `EVO-01`, still paced unless pre-fire. | Compare and timing render. |
| `EVO-03` | Nothing After Tomorrow | Chaos 1000, high Conviction, low organization. | Eligible but slow because societies lack governing capacity. | Evaluate. |
| `EVO-04` | Nothing After Tomorrow | Chaos 1100, high Conviction, high organization, parallel councils. | Faster than `EVO-03`. | Compare. |
| `EVO-05` | Disabled evolution | Evolution toggle off. | Zero activation chance and no recorded flags. | Inspect and sequence. |

## Incident-selection scenarios

| ID | Setup | Expected behavior | Evidence |
| --- | --- | --- | --- |
| `INC-01` | Peaceful stable country with strong education. | School, public evidence, finance, and civic incidents dominate. War-only incidents are absent. | Candidate-pool inspect and seeded simulation. |
| `INC-02` | Losing belligerent with pacifist organization. | Refusal, prisoner, armistice, family, and depot incidents dominate. | Compare with `INC-01`. |
| `INC-03` | National Preparation with disaster pressure. | Shelter, reserve, rail, hospital, and hoarding incidents dominate. | Evaluate. |
| `INC-04` | Emergency Order with severe backlash. | Raid, prisoner, martyr, underground, and revolutionary incidents rise. | Sweep backlash. |
| `INC-05` | Final month. | Early emergence incidents are replaced by vigils, final transport, hospitals, archives, and standing orders. | Sequence and candidate-pool proof. |
| `INC-06` | Repeated identical source state. | One-shot confirmation incident does not repeat for farming. | Long seeded simulation. |

## Peace-acceptance scenarios

| ID | Setup | Expected ordering | Evidence |
| --- | --- | --- | --- |
| `PEACE-01` | Long losing offensive war, low War Support, enemy also exhausted. | Armistice acceptance is high. | Evaluate complete option pool. |
| `PEACE-02` | Defensive war with occupied homeland and active enemy advance. | Continued defense outranks full demobilization. Humanitarian truce remains possible. | Compare. |
| `PEACE-03` | Aggressive enemy sees a demobilized target and expects quick victory. | Enemy rejection is high. | Evaluate both belligerents. |
| `PEACE-04` | Civil war with balanced fronts and high shared Conviction. | Local truce and congress options rise. Automatic national white peace remains absent. | Simulate sequence. |
| `PEACE-05` | Last Day truce already offered and rejected. | Cooldown blocks immediate repeated offers. | Sequence. |
| `PEACE-06` | Truce breach. | Future trust and acceptance fall sharply. | Compare pre-breach and post-breach. |

## Government-takeover scenarios

| ID | Setup | Expected route | Evidence |
| --- | --- | --- | --- |
| `TAKE-01` | High continuity, recognized councils, voluntary posture. | Voluntary custodial transfer leads. | Evaluate route pool. |
| `TAKE-02` | Functioning parliament, high movement representation. | Constitutional transfer leads. | Compare. |
| `TAKE-03` | Weak center, strong municipal services, communal current. | Municipal cascade leads. | Evaluate. |
| `TAKE-04` | High military refusal, preserved defensive command. | Military-refusal transfer leads. | Evaluate. |
| `TAKE-05` | Severe backlash, deaths, destroyed records, collapsing government. | Revolutionary collapse rises strongly. | Sweep backlash and continuity. |
| `TAKE-06` | Strong functioning state and low organization. | Existing-government survival leads even at high Conviction. | Compare with `TAKE-05`. |
| `TAKE-07` | Player country. | No AI-only silent voluntary transfer. Player receives the valid decision or crisis path. | Structural inspection. |

## Focus-route scenarios

| ID | Setup | Expected route priority | Evidence |
| --- | --- | --- | --- |
| `FOCUS-01` | Voluntary major-power custodial administration. | Custodial, relief, records, and Assembly routes. | Focus weight inspect and compare. |
| `FOCUS-02` | Municipal cascade with communal current. | Communal Devolution and relief. | Evaluate. |
| `FOCUS-03` | Losing war and military-refusal takeover. | Peace, demobilization, defensive service. | Evaluate. |
| `FOCUS-04` | Strong devotional and civic concordat. | Observance, reconciliation, hospitals. | Evaluate. |
| `FOCUS-05` | Severe repression and revolutionary takeover. | Avenging Witnesses reveals and receives weight. | Inspect hidden route gate. |
| `FOCUS-06` | No suppression evidence. | Avenging Witnesses remains hidden and weight zero. | Compare. |

## Terminal-readiness scenarios

| ID | Setup | Expected result | Evidence |
| --- | --- | --- | --- |
| `TERM-01` | High Conviction for one day, few administrations. | No terminal commitment. | Sequence. |
| `TERM-02` | Sustained highest Conviction plus widespread institutional withdrawal. | Path B can mature. | Sequence with declared cadence. |
| `TERM-03` | Broad voluntary administrations across regions. | Path A can mature. | Evaluate country pool. |
| `TERM-04` | One major power demobilizes alone. | Path C remains incomplete. | Evaluate. |
| `TERM-05` | Several major powers demobilize and join with relief obligations. | Path C can mature. | Compare. |
| `TERM-06` | Strong pacifist refusal and common compact across regions. | Path D can mature. | Sequence. |
| `TERM-07` | Severe suppression-driven takeovers across regions. | Path E can mature. | Sequence. |
| `TERM-08` | Many released microstates join, no major spread. | Terminal remains blocked. | Simulate exploit. |
| `TERM-09` | Mixed partial progress across A, C, and D. | Mixed path can mature only after equivalent sustained proof. | Evaluate declared mixed model. |
| `TERM-10` | Final Vigil toggle disabled. | Zero terminal selection chance. Event and evolutions continue. | Inspect. |
| `TERM-11` | Another world end already active. | Final Vigil chance zero. | Inspect. |

## Failed-date response scenarios

| ID | Setup | Expected result | Evidence |
| --- | --- | --- | --- |
| `FAIL-01` | Centralized prophetic group, exposed leaders, open public evidence. | Collapse or fraud response dominates. | Evaluate. |
| `FAIL-02` | Strong devotional relief network. | Mercy or institutional persistence rises. | Compare. |
| `FAIL-03` | Communal councils delivering services. | Symbolic fulfillment and communal persistence rise. | Evaluate. |
| `FAIL-04` | Severe suppression and revolutionary government. | Rage, revolutionary consolidation, and counterrevolution risks rise. | Sweep. |
| `FAIL-05` | Strong skeptical continuity and fulfilled public promises. | Government legitimacy and rapid recovery lead. | Evaluate. |
| `FAIL-06` | Real major disaster overlaps the date. | Conviction falls less and reinterpretation rises. Damage remains owner-controlled. | Compare. |
| `FAIL-07` | Revised-date branch already used. | Future revised-date chance is zero. | Sequence. |

## Sequence-level acceptance

Use `hoi4.probability_sequence` only after the complete custom-pool manifest declares:

- Evaluation cadence.
- Conviction gain and loss sources.
- Incident cooldowns.
- One-shot guards.
- Evolution eligibility and MTTH.
- Posture persistence.
- Country addition and removal.
- Government-transfer state.
- Terminal readiness accumulation and reset.
- Failed-date transition.
- Revised-date terminal state.

If the sequence manifest is incomplete, report unresolved evidence instead of claiming exact long-run probability.
