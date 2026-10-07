# 15. AI Strategy, Balance, and Acceptance

## Intended campaign outcomes

Preparation must produce a much better survival result while imposing a genuine early opportunity cost.
Hardening must preserve enough immediate military function to tempt a government under pressure.
It must also make later losses noticeably worse.

A well-run small country can survive through local organization and selective aid.
A wealthy country cannot buy universal immunity with one capital action.
A large empire must protect several real populations and routes.
An occupied country retains meaningful responsibility through whichever authority can act.

The event remains a major mortality crisis.
Well-prepared countries are not necessarily untouched.
Unprepared high-Wrath countries can suffer devastating demographic losses without violating population floors or duplicating casualties.

## Modifier combination

State effects project to national outcomes using the relevant exposed population, productive capacity, or actual formations.
Overlapping water, insects, Boils, Darkness, and mourning do not each add an unrestricted national version of the same penalty.

Initial event-owned ceilings are an 85% reduction in output or construction, a 75% reduction in relevant recovery, movement, or planning, and a 95% reduction in air effectiveness or detection.
These ceilings bound Event 085's consolidated contribution, not unrelated systems' total effects.
The appropriate supported modifier field and its units must be inspected before implementation.

Harden Our Hearts removes half of the event-owned active production interruption before the relevant ceiling, without reversing destroyed buildings or Famine-owned loss.
It does not create positive output when the country has no Event 085 production interruption.

The event owns at most three simultaneous national spirits.
A state aftermath modifier is not an excuse to hide a fourth national spirit.
The system may use more internal records without making the player manage more values.

## Mortality anchor table

All entries below are episode allowances for the stated phase or impact, applied to actually exposed living people and settled by the listed owner.
They are not daily rates.
They are fictional balancing parameters.

| Plague | Initial allowance before Wrath and intensity | Important limitation |
| --- | ---: | --- |
| Blood | 5 basis points | Direct unsafe-water/service loss only; infectious consequences separately proven |
| Frogs | Normally zero direct; up to 5 basis points for proven secondary disease | No automatic death debit when frogs disappear |
| Lice and Gnats | 10 basis points for proven disease exposure | Disease owner and actual affected people |
| Flies | 25 basis points for proven disease exposure | Excludes Famine's separate hunger mortality |
| Livestock | Zero direct human mortality | Food collapse and famine belong to Famine |
| Boils | 125 basis points | Full disease episode allowance, not per tick |
| Hail and Fire | 250 basis points | One combined impact budget; preparation and remaining people matter |
| Locusts | Zero direct human mortality | Famine owns resulting hunger deaths |
| Darkness | 10 basis points | Entire 72-hour phase, excluding previously settled causes |
| Firstborn | The cohort formula in Part 8 | Actual surviving firstborn people, current protection, 0.95 hazard ceiling |

A basis point here is 0.01%.
One hundred basis points is 1%.
The values are deliberately distinguishable from the food owner's exposure stages.

For a selected representative state, an overlap allowance remains the original phase's allowance unless a genuinely new accepted episode or impact provides another budget.
More processing ticks cannot create more total mortality.
Any disease owner mapping must preserve this limit or report why its accepted native contract requires a revised tuning proposal.

## AI policy matrix

| Situation | Expected strategic tendency | Must not do |
| --- | --- | --- |
| Peace, adequate services and resources | Prepare early and preserve the response network | Harden randomly at the same rate as a desperate frontline country |
| Critical offensive, low Wrath, early plague | Consider a bounded military continuity choice | Ignore all later civilian consequences |
| Wrath at least 75 or severe proven civilian exposure | Strong preference for meaningful protection | Continue hardening solely because of ideology |
| Small country with no road stockpile | Select a valid local commitment or seek reachable aid | Wait forever for 25 trucks when a local route exists |
| Country with a functioning network near Darkness | Start valid Passover promptly | Delay until completion is no longer possible |
| Country with only 24 hours remaining | Consider the valid local emergency route | Start a 48-hour national operation |
| Potential refugee host with unsafe food or no capacity | Seek support, transit, or bounded reception | Treat low Wrath as proof of unlimited safety |
| Enemy facing a mutual humanitarian collapse | Consider a limited proven corridor | Grant universal military access as a relief shortcut |
| World-end qualifying cycle in progress | Preserve collective low Wrath unless an exceptional need is proven | Break the cycle for a negligible temporary bonus |
| Missing route, target, or owner proof | Reject the action and pursue a valid alternative | Keep a positive weight on an impossible action |

These are intended tendencies, not accepted numeric probabilities.
War urgency, civilian exposure, current resources, protected capacity, failed promises, and terminal progress provide the main weight inputs.
Religion never provides a protection advantage or an automatic refusal rule.

Equivalent valid random plague targets use equal weights.
Priority relief selection can legitimately prefer greater need after validity.
The two selection purposes must not be conflated.

## Probability evidence

The implementation must route weighted target and AI behavior through `chaosx_ai_probability_auditor`.
Begin with `hoi4.probability_inspect` for the actual entries and helpers.
Use named world-state evaluation, threshold sweeps, comparisons after changes, and simulations only for declared uncertain inputs.
Use the verified game-version adapter for MTTH timing conclusions.

The shared Evolution base timing is not proven by hand arithmetic.
Provide scheduled state changes where a country's resources, Wrath, or deadline change during the horizon.
Distinguish exact, bounded, sampled, and unresolved findings.

No MCP probability audit was run for this planning package.
The following cases are acceptance requirements, not reported test passes.

## Required comparison cases

| Case | Fixture and expected result |
| --- | --- |
| A01 — Global opening | All valid countries join one episode; no extra random-event pacing per recipient |
| A02 — One-state country | It receives a valid footprint and a feasible local route |
| A03 — Large country | Representative phase coverage rounds upward and does not target only the capital |
| A04 — Equal target draw | Equivalent physically valid states have equal opening probability |
| A05 — Invalid terrain | An invalid agricultural or physical target is rejected before weighting |
| A06 — Country release | Current stage, population cohort, damage, and remaining deadlines transfer without reset |
| A07 — Annexation | Responsibility weight and Wrath history conserve rather than disappearing |
| A08 — Exile | The government does not receive a second civilian population debit |
| A09 — Non-human case | Physical exposure and human firstborn eligibility remain separate |
| A10 — Dead target | No character or civilian cohort is killed twice |
| A11 — Duplicate coordinator | Repeated processing produces one accepted stage and one settled receipt |
| A12 — Save/load | Deadline, cycle, preparations, firstborn survivors, and mission reservations persist |
| A13 — Exact stockpile | Holding exactly the displayed cost is sufficient |
| A14 — Insufficient stockpile | No partial hidden debit or negative stockpile occurs |
| A15 — Cost isolation | A helper's temporary negation cannot contaminate the next resource debit |
| A16 — Local capacity | Work occupies real capacity without a factory-count gate or population deletion |
| A17 — Partial completion | Actual reached people receive partial protection; credit cannot exceed the full total |
| A18 — Late completion | Aid can help survivors but cannot reverse settled earlier deaths |
| A19 — Objective lost to war | Valid work transfers or closes without falsely granting success or moral blame |
| A20 — Donation loop | Returning the same shipment does not generate repeated Wrath reductions |
| A21 — Food owner | Crop loss affects proven remaining capacity; no private famine stage is set |
| A22 — Famine timing | Sustained severe exposure produces owner mortality within its actual schedule |
| A23 — Disease owner | Boils uses a peaceful accepted episode; no weapon unlock or duplicate flat death effect |
| A24 — Composite storm | Hail plus causal fire share the accepted budget and coherent protection |
| A25 — Repeated storm | A new valid strike affects surviving people and remaining structures only |
| A26 — Locust front | It traverses valid adjacent states and protects already moved surviving food |
| A27 — Disconnected map | Valid separate seeds provide coverage without a front teleporting arbitrarily |
| A28 — Global Darkness | Actual presentation begins and ends with the common phase, with readable controls |
| A29 — Passover timing | 48-, 36-, and 24-hour variants enforce deadlines; valid completion exactly at the deadline settles before the tenth-plague freeze |
| A30 — Passover scope | Prepared capital and unprepared outer district remain distinct |
| A31 — Incoming refugees | Arrival does not grant automatic full protection or duplicate firstborn records |
| A32 — Population floor | Applied deaths, population debit, and cohort decrement match exactly |
| A33 — Route conservation | Origin debit equals destination survivors plus route deaths |
| A34 — Second tenth | Firstborn survivors are not reinitialized to 25% of remaining population |
| A35 — Named succession | Proven eligible characters resolve through valid owner roles and replacements |
| A36 — Evolution mid-warning | A warning's accepted deadline is not shortened retroactively |
| A37 — Exactly 1000 Chaos | Evolution III can be active; the endless branch cannot newly activate |
| A38 — Branches disabled | The proposed bounded renewal does not become indefinite recurrence |
| A39 — Maximum at low Chaos | Strong opening profile does not forge completed cycles or raise Chaos to 1001 |
| A40 — Fixed global weight | Depopulation does not itself lower global Wrath |
| A41 — Late repentance | Endpoint improvement does not count as a full qualifying escape cycle |
| A42 — Broad recovery | A small holdout cannot block a genuinely qualifying 80%-weight recovery |
| A43 — Other terminal threat | Ending 085 does not clear another source or the shared terminal-history latch |
| A44 — Chaos attribution | Deaths and physical consequences cannot be counted twice through anomaly entries |
| A45 — Modifier cap | Overlap respects consolidated ceilings and the three-spirit maximum |
| A46 — UI budget | No more than six primary actions or three urgent event missions are visible |
| A47 — Owner cleanup | Ending 085 leaves genuine famine, displacement, outbreaks, and disaster aftermath alive |
| A48 — Achievement integrity | Debug reset, duplicate receipts, and tag farming cannot earn survival unlocks |
| A49 — Later legitimate episode | A new root episode reuses campaign firstborn survivors; it cannot reclassify surviving non-firstborn people |
| A50 — Major fire-once | Natural and cluster openings share consumed member eligibility; manual replay and internal cycles do not rearm it or duplicate Major pacing |

## Completion evidence

Source inspection proves only what the inspected source contains.
Arithmetic checks prove only the declared calculations.
MCP inspection and rendering prove the supported source or consumer properties they actually evaluate.
A screenshot supplied by the user proves only the observed live state.

Before completion, specialist passes must address systems, decisions, AI probabilities, localization, visuals, documentation, and final coverage.
The improvement-loop planner must review the implemented package near completion and its accepted findings must be resolved.
Unavailable roles and tools remain explicit open gates.
No parent self-review is described as a completed specialist pass.

Live gameplay validation remains user-owned.
Do not launch the game automatically or claim that a playable campaign has been tested from this specification alone.
