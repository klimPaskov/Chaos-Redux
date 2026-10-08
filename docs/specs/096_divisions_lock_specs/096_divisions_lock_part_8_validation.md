# Event 096: requirement coverage and acceptance evidence

Proposed design: [README](README.md#authority-and-current-workflow) records current authority, owner workflows and historical receipt limits.

## 1. What this package can prove

The planning work can establish source coverage, an internally explicit design, arithmetic properties of the chosen formulas, complete handoff coverage, and reviewed dispositions. It cannot establish native engine behavior without the installed references and execution tools.

Use these evidence classes throughout implementation:

| Class | Meaning |
| --- | --- |
| Design review | The proposed rule is complete and consistent on paper |
| Reference evidence | A retained source documents a primitive or existing mod pattern |
| Arithmetic evidence | A separate deterministic reference calculation checks the proposed equations |
| Native tool evidence | Installed-version inspection, schema validation, evaluation, render, or comparison produced a retained artifact |
| Live evidence | The user observed the behavior in the running game or supplied a relevant native save |

One class does not substitute for another. The reference-model results generated for this package are not HOI4 tests. No current probability, GUI, native refund, or runtime result may be inferred from them.

## 2. User-brief traceability

| Supplied requirement | Canonical design location | Completion condition |
| --- | --- | --- |
| Correct catalog identity and Peace High membership | README, Part 7 | Metadata aligned without an unsupported status promotion |
| Simultaneous worldwide native lock | Part 1 Sections 1 and 5 | Every real existing actor affected in one firing, no tag list |
| Country-specific live capacity | Part 2 Sections 3 and 4 | Actual territorial, population, infrastructure, civilian and military inputs drive A |
| Template size matters, no giant-division bypass | Part 2 Sections 1 and 2 | Additive structural count including support and special formations |
| Existing units unchanged at firing | Part 1 Section 1 | No entry mutation of units, orders, fronts, or organization |
| Roughly one-week minimum | Parts 1 and 7 | Verified seven elapsed game days, including repeats and midday entry |
| Dynamic extension and release | Part 1 Section 2 | Condition-based persistence, explicit unchanged-excess interpretation |
| Optional random single and stronger actions | Part 3 | Exact current eligible pool, human confirmation, bounded batch |
| Capacity growth can end the lock | Part 2 | Conquest before peace, population and industry gains alter the same live A |
| Repeats use current world state | Parts 1 and 4 | Recompute, renew floor, coalesce jobs and credits without duplicate effects |
| Four exact evolutions | Part 4 | Both active and pre-fire paths, thresholds, multiplier, reviews, safe settings |
| Military Madness connection | Part 4 Section 8 | Combat-stat changes do not create artificial capacity |
| The Offensive connection | Parts 4 and 5 | Aggressive strategy can coexist with a retained force and frozen templates |
| Other capacity-changing events interact naturally | Parts 2 and 7 | General live inputs and local reconciliation, provider refresh where useful |
| Understandable identity | Part 6 | Two persistent values, one contextual time, one confirmation bound |
| Full supplied-source processing and honesty | Reading audit and research record | Complete supplied reading, targeted external limits disclosed |

## 3. Measurement and capacity fixtures

All fixtures in this and the following sections require native evidence before implementation completion. Their presence in this document means they are specified, not executed.

| ID | Fixture | Required result |
| --- | --- | --- |
| M01 | Four six-battalion formations and one twenty-four-battalion formation with the same sub-unit multiset | Identical F |
| M02 | Add and remove an unused template, then put the same template into the deployment queue | No fielded-force change before deployment |
| M03 | Add actual support attachments without changing line battalions | F increases by their exact weights, no missing or double-counted support |
| M04 | Damage and reorganize an existing formation without changing its structure | F remains unchanged |
| M05 | Autonomous robots and equipment-independent rats | Positive correct F despite zero human manpower, and despite zero equipment where applicable |
| M06 | A sub-unit with several categories and an unclassified installed type | Exactly one final known profile, positive unknown baseline |
| M07 | Sent and received expeditionaries, volunteers, exiles, colonial manpower, allied units on friendly land | Correct owner attribution and global structural conservation |
| M08 | Intelligence decoys, garrisons, ships, aircraft, and standalone railway guns | No accidental inclusion in the division-structure measure |
| M09 | Actual formation loss or provider army grant during a hold | Fresh actual F, no inferred casualties or ignored new unit |
| C01 | Core control gained and lost | Correct live population and territorial contribution |
| C02 | Non-core conquest before ownership transfer, then compliance change | Immediate access floor, later access improvement, no need for peace conference |
| C03 | A defeated power retains legal ownership but loses control | Lost footprint leaves P and T |
| C04 | Change consumer-goods allocation, construction assignment, production line, and trade | No allowance manipulation through idle or imported factories |
| C05 | Build, permanently remove, convert, capture, and lose factories, including offsite grants | Correct selected C/M policy and no overlord double count |
| C06 | Bomb and repair factories without permanent removal | Completed-base policy remains consistent |
| C07 | Huge state population and a zero-population or offmap actor | Safe scaling, positive allowance floor, no overflow or invented upper cap |
| C08 | Military Madness or another combat-stat modifier changes strength | No circular increase in allowance and no stat-driven force change |
| C09 | Quarter-point boundary near equality | Display and predicate agree exactly |

## 4. Lifecycle and transaction fixtures

| ID | Fixture | Required result |
| --- | --- | --- |
| L01 | Within allowance at entry and throughout the week | Hold lasts the verified minimum, then releases automatically |
| L02 | Within allowance at entry, oversized before minimum ends | Floor expiry does not release it |
| L03 | Slight positive unchanged excess for a long observation window | No finite expiry, no automatic disband, no false release countdown |
| L04 | Large excess becomes compliant through growth or exact voluntary removal | Immediate action refresh or next authoritative daily refresh releases after the floor |
| L05 | Midday application, then a later same-day repeat | Native floor is properly renewed and never matures early from an older callback |
| L06 | Repeated entry while held, duplicate dispatch delivery, and two genuine same-day firings | Live recalculation, one logical job chain, correct idempotence and floor policy |
| L07 | Legacy `.3` callback and an old already-open release popup | Neither blindly unlocks a current or another-owner hold |
| L08 | Save and load during floor, oversize, watch, pending request, and terminal receipt | No lost state, duplicate action, free credits, or request reuse |
| L09 | Annexation, exiled continuation, cosmetic change, held and watched political succession, unrelated new country | Correct cohort, fresh held floor versus preserved watch due day, no stale consent or achievement transfer |
| L10 | Future-event disable, evolution disable, re-enable, and explicit clear | Distinct documented effects, no false success reward |
| D01 | Open and cancel a confirmation repeatedly | No unit selected in advance, no removal, no refund, no RNG preview loop |
| D02 | Timeout or invalid controller while popup remains open | Cancelling path only, old receipt cannot authorize a newer request |
| D03 | Gain capacity between popup opening and confirmation | Refresh first, no removal if already compliant |
| D04 | Batch bound falls before commit, or eligible population shrinks | Reject a stale advertised bound, preserve documented partial-stop behavior after a valid commit |
| D05 | Valid batch reaches compliance on its first removal | Stop after one, report one, never force the full advertised bound |
| D06 | Source-owned protected formation shares an ordinary visual identity | Exact provider exclusion, no ledger damage from a guessed filter |
| D07 | Active combat, foreign authority, quiet front, human final formation, new final-formation risk after confirmation, AI final formation | Correct pool, frozen explicit possible zero-owned-army permission, safe stop or invalidation for newly undisclosed risk, absolute AI exclusion |
| D08 | Exact native removal with equipment variants, depleted strength, and zero-human units | Correct surviving returns, no duplicate paper establishment or unrelated deletion |
| D09 | Double confirmation delivery and repeated completion callback | Receipt consumed exactly once |
| D10 | Two actions on one game day and a cancelled or zero-result action | Shared successful-execution guard, no fee or guard consumption on cancellation |

## 5. Evolutions, AI, and Chaos fixtures

| ID | Fixture | Required result |
| --- | --- | --- |
| E01 | Pre-fire openings below 200 and at 200, 400, 600, 800, with closed historical stages or a still-active stricter grant | Current-Chaos opening, retained stricter active regime on coalescing repeat, no closed-grant threshold bypass or compounded multipliers |
| E02 | Active next-stage eligibility, Chaos drop, and a large Chaos jump | Actual MTTH route, no invented guaranteed date or same-callback stage cascade |
| E03 | Active evolution when some participants are held and others already released | Refresh held countries, give released countries a real new watch when applicable |
| E04 | Evolution II growth above both thresholds, only one threshold, and capacity loss without force growth | Reacquire only when both selected conditions pass |
| E05 | Evolution III or IV capacity loss after release | Current relative threshold governs reacquisition |
| E06 | Equality at each relock threshold and equality at A while held | Strict reacquisition inequality, inclusive held-state release, no confused tolerance |
| E07 | Passed and failed reviews, new peak, upgrade, repeat, held or watched split, and merger of different grants | Once-only consumed receipts, bounded targets, inherited spent history, maximum rather than additive obligation, one resulting chain |
| E08 | Watch due day after many daily refreshes | Appointment stays anchored to watch start rather than sliding forward |
| A01 | Peaceful small and large countries at identical e | Same ratio-based preference structure, different live capacities and possible batch bounds |
| A02 | War, threat, capitulation, another owner, and growth hold at, above, and below the thirty-day projection boundary | Both actions vetoed exactly when required, eight valid observations, reset or missing history cannot fabricate G |
| A03 | Sticky retain with unchanged state, then accumulated ten-percent change | No timer-only reroll, inclusive material-change trigger against stored baseline |
| A04 | T/G/O or pool-empty transition without a ten-percent change | Reconsideration occurs at the legal boundary |
| A05 | Successful action, failed action, no-op, and a pending human request | Exactly one bounded attempt per choice, correct next review or sticky retain |
| A06 | e near 0.5, 0.75, 2 and every k step for several N_owned values | Score rankings, severe gate, capped E, raw-e batch quantization, and action bound all distinguish their roles |
| A07 | Complete eligible unit pool with protected and unprotected records | Native uniform selection and removal without replacement, fresh membership each step |
| Q01 | Initial actual global deprivation at several entry-force shares | Correct quartile consequence and one dispatch receipt |
| Q02 | Repeated relocks, broader first relapses, and credited or uncredited lineage splits and mergers | No duplicate contribution, conserved active plus retired weight, inherited credited bit, correct ten- and twenty-five-percent thresholds |
| Q03 | Rapid refirings and settings toggles | Family positive budget survives, no farming or negative clear reward |
| Q04 | Normal construction, wars, deaths, and evolution status alone | No duplicated generic or status-only Chaos |
| Q05 | Compliance versus disappearance, manual clear, repeat supersession, zero-force succession, overdue transfer, or incomplete transfer snapshot | Only legitimate attributable restoration earns the once-only negative consequence, retired and superseded grants cannot cash later rewards |

The probability owner begins with the actual implemented surface and `hoi4.probability_inspect`. It must then evaluate complete named pools, sweep relevant thresholds, and compare the changed implementation with an immutable real baseline using the same fixtures. A seeded simulation or sequence analysis is additional evidence only when its pool, transitions, and horizon are explicitly defined.

Do not normalize the abstract scores by hand and call the result a native probability audit. Record source revision, scenario identity, candidate completeness, unresolved external inputs, tool artifact, and evidence class for each result.

## 6. Ownership, assets, and achievement fixtures

| ID | Fixture | Required result |
| --- | --- | --- |
| O01 | Each known native owner alone and paired with Event 096 | Release removes only the Event 096 hold |
| O02 | Special recruitment exceptions and individual template locks | Preserve actual owner behavior before, during, and after overlap |
| O03 | Event 019 management and provider-owned units | Start and completion barriers remain, optional removal cannot bypass ledger ownership |
| O04 | Supported new game and migrated old save | Every native owner reconstructed through a proven contract |
| U01 | Every core country state at supported resolutions and long localisation | Four-value budget, correct status, no clipping or misleading countdown |
| U02 | Opening, release, relapse, and overlapping notices | Accurate current state and no release delayed by acknowledgement |
| U03 | Report card and all small icons at native size | Canonical treatment, correct transparency, distinct single/batch silhouettes |
| U04 | All achievement triplets | Correct source lineage, unchanged templates and overlay, strict DDS and root-only path checks |
| H01 | Qualifying and nonqualifying industrial-growth release | Counterfactual capacity and daily observation contracts are exact |
| H02 | Severe voluntary reduction with final force inside and outside the broad band | Actual transaction contribution, no automatic reward for a click |
| H03 | Three or more fully compliant rolling reviews with army growth | Complete grant, strict review compliance, no skipped or mixed-episode credit |
| H04 | Genuine repeat and duplicate delivery separately for all three objectives, clear, disable, annexation, successor, missing observations | Genuine repeat retires unfinished attempt and starts a separately qualifying one from zero, duplicate does not reset, same-grant evolution alone does not reset, existing awards survive |

## 7. Performance and final acceptance

Profile a normal early campaign, a late large-army campaign, and a supported maximum controlled-state footprint, including the ordinary category held open during a local refresh. Confirm that frame-driven predicates use complete snapshots, the force measure uses aggregates, inactive countries have no needless callback chain, and active capacity calculation completes within one game day. Stress duplicate firing, bounded succession partitioning, and maximum ten-removal transactions. Preserve every unvisited state or participant when batching is necessary.

Use installed vanilla documentation as syntax authority. Inspect and render the relevant event chain, evaluate its weighted surfaces, and compare actual changed source. The user performs live-game validation. Do not launch the game, invent screenshots, or request logs as a substitute for the required workflow in this planning task.

Implementation completion requires the three native gates in Part 7, all material rows above, matching localisation and asset coverage, catalog alignment, accepted review dispositions, and no undisclosed design reductions. If a gate fails, identify the exact failed capability and its effect on the design. The planning package can be complete while implementation remains gated, but the event cannot be called implemented or Playable on that basis.
