# 15. AI, Balance, and Acceptance

## Intended outcomes

Preparation costs real output early and produces a much better survival result.
Hardening keeps enough military function to tempt a government under pressure and makes later losses noticeably worse.
A well-run small country survives through local organization and selective aid; a wealthy country cannot buy universal immunity with one action; a large empire must protect many states.
The event remains a major mortality crisis: prepared countries are hurt, and unprepared high-Wrath countries can suffer devastating losses without breaking population floors or counting deaths twice.

## Modifier combination

State effects project to the crisis spirit through the exposed share of population or industry.
Overlapping plagues, Darkness and mourning share these ceilings on Event 085's combined contribution:

| Statistic group | Ceiling |
| --- | ---: |
| Factory output, construction speed | −85% |
| Recovery, training, movement, planning | −75% |
| Air mission efficiency, air and naval detection | −95% |

Harden Our Hearts halves Event 085's active production interruption before the ceiling.
Event 085 holds at most three national spirits (Part 1).

## Mortality budgets

Each budget is a whole-phase or whole-impact allowance applied to the exposed population and settled once by the listed owner, before the Wrath multiplier, intensity and protection.
One basis point is 0.01%.

| Plague | Budget | Owner and limit |
| --- | ---: | --- |
| Blood | 5 bp | Event 085 direct; outbreak deaths separate |
| Frogs | 0 direct; up to 5 bp | Outbreak owner, only for uncleared states at the die-off |
| Lice and Gnats | 10 bp | Outbreak owner |
| Flies | 25 bp | Outbreak owner; hunger deaths are Famine's |
| Livestock | 0 | Famine owns resulting hunger deaths |
| Boils | 125 bp | Outbreak owner, whole episode |
| Hail and Fire | 250 bp | Natural Disasters, one combined impact budget |
| Locusts | 0 | Famine owns resulting hunger deaths |
| Darkness | 10 bp | Event 085 direct, whole 72 hours |
| Firstborn | Part 8 formula | Event 085 direct |

More processing ticks or overlap never create more total mortality than the budget.

### Representative cases

These rough cases check that the tradeoff is felt; they exclude famine deaths, which depend on Famine's own timing.

| Country (first cycle, baseline) | Wrath at the final night | Passover | Pre-tenth direct, outbreak and storm deaths (share of exposed population) | Tenth-plague deaths (share of total population) |
| --- | ---: | --- | ---: | ---: |
| Prepared every phase | 0 to 10 | Prepared | About 1% | About 0.13% |
| Hardened three times, then heeded | 40 to 50 | Prepared | About 2% | About 0.3% |
| Hardened every phase | 100 | Unprepared | About 8% | About 24% |

The last row is the brief's devastating outcome: a quarter of the population can die in one night.
If implementation tuning moves these figures far apart from each other or far from these orders of magnitude, record the change and reason in the plans folder.

## AI behavior

The AI uses the same costs, windows and requirements as the player.
Religion and ideology never decide protection.
The anchors below go to `chaosx_ai_probability_auditor` for verification.

| Action | Base weight | Modifiers |
| --- | ---: | --- |
| Harden Our Hearts | 0 at peace, 5 at war | ×3 when surrender progress is at least 30%; ×0.5 at Wrath 50 or more; ×0 at Wrath 75 or more; during Darkness ×0 unless surrender progress is at least 50% |
| Heed actions (2–4, 6–11) | 10 | ×1.5 at peace; ×2 at Wrath 50 or more; prefer the local variant when the transport cost exceeds a quarter of the country's stockpile; target the footprint state with the most exposed people |
| Military Stand-Down | 5 at peace, 0 at war | ×1 at war only when Wrath is 50 or more and surrender progress is below 10% |
| Observe the Passover | 100 at Darkness onset | National program when affordable; otherwise local preparations in the most populous states, up to three at once |
| Foreign Relief Pledge | 0 | 5 when Wrath is at least 25 and the stockpile holds twice the cost; ×2 for faction members and neighbors; ×0 for enemies unless a Migration corridor between them is open |
| Reconstruction Coordination | 5 | ×2 for states in famine or catastrophic famine |

An impossible action keeps zero weight.
Equivalent random plague targets use equal weights; relief targeting may prefer need, and the two selection purposes stay separate.
Use `hoi4.probability_inspect` and named scenarios for this review where the tool supports it; otherwise calculate representative cases from the script.

## Acceptance cases

These are future implementation checks, not executed tests.

| Case | Expected result |
| --- | --- |
| A01 Global opening | All valid countries join one episode; no per-recipient pacing |
| A02 One-state country | It has a footprint and a feasible local route |
| A03 Large country | Footprint rounds up and does not target only the capital |
| A04 Equal target draw | Equivalent valid states have equal opening probability |
| A05 Invalid terrain | Invalid agricultural or physical targets are rejected before weighting |
| A06 Country release | Phase, damage, Passover status, firstborn share and remaining deadlines transfer without reset |
| A07 Annexation | Weight joins the annexer and Wrath becomes the weighted average |
| A08 Exile | No second civilian population debit |
| A09 Nonhuman country | Physical damage only; no firstborn deaths |
| A10 Dead target | No character or state settled twice |
| A11 Duplicate coordinator | Repeated processing produces one phase and one settlement |
| A12 Save and load | Deadlines, cycle, objectives, Passover status and firstborn shares persist |
| A13 Exact stockpile | Holding exactly the shown cost is enough |
| A14 Insufficient stockpile | No partial debit or negative stockpile |
| A15 Cost isolation | A helper's in-place negation cannot contaminate the next debit |
| A16 Local organization | Applies the state penalty without a factory gate, population loss or manpower |
| A17 Partial completion | Half protection and −5 Wrath; later full completion adds only −5 |
| A18 Late completion | Helps survivors, cannot reverse settled deaths |
| A19 Objective lost to war | Closes as partial or failed without false credit or blame |
| A20 Donation loop | A pledge pays only an active recipient objective; returned or idle aid earns nothing |
| A21 Famine input | Food shock reflects only the remaining harvest; no stage is set directly |
| A22 Famine timing | Sustained shocks reach famine on Famine's own schedule |
| A23 Disease owner | Boils uses a non-weapon outbreak without weapon unlocks or duplicate deaths; compare ordinary care, delivered matching Wu treatment and research due after the phase; only reached patients change the care result; one clinical settlement and one protective credit; no Passover or firstborn protection |
| A24 Composite storm | Hail and fire share one budget and one warning |
| A25 Repeated storm | A new strike hits only surviving people and remaining buildings |
| A26 Locust front | Moves through adjacent valid states and spares food already protected |
| A27 Disconnected map | Separate seeds cover islands without teleporting fronts |
| A28 Global Darkness | The visual starts and ends with the phase and keeps controls readable |
| A29 Passover timing | 48-, 36- and 24-hour variants respect the deadline; completion exactly at the deadline counts |
| A30 Passover scope | A prepared capital and an unprepared outer state stay distinct |
| A31 Late arrivals | A Prepared state whose population grows more than 10% after completion becomes Partly prepared |
| A32 Population floor | Applied deaths, population debit and firstborn share reduction match |
| A33 Route conservation | Origin debit equals arrivals plus route deaths |
| A34 Second tenth plague | Uses the reduced firstborn share, never a fresh 25% |
| A35 Named succession | Only proven eligible characters die; succession follows the character owner |
| A36 Evolution mid-warning | A warning's deadline is not shortened |
| A37 Exactly 1000 Chaos | Evolution III may be active; the endless branch cannot activate |
| A38 Branches disabled | At most one renewed sequence |
| A39 Maximum at low Chaos | No forged cycles, no Chaos raised to 1001 |
| A40 Fixed global weight | Depopulation does not lower global Wrath |
| A41 Late repentance | A last-minute drop does not qualify an escape cycle |
| A42 Broad recovery | A small holdout cannot block an 80%-weight recovery |
| A43 Other terminal threat | Ending Event 085 clears only its own world-threat source and threat |
| A44 Chaos attribution | Deaths and physical consequences are not counted twice |
| A45 Modifier ceilings | Overlap respects ceilings and the three-spirit maximum |
| A46 Category budget | No more than six actions or three urgent missions visible |
| A47 Owner cleanup | Ending Event 085 leaves famine, displacement, outbreaks and disaster aftermath alive |
| A48 Achievement integrity | Debug resets, duplicate results and tag farming cannot unlock survival achievements |
| A49 Later legitimate episode | Reuses remaining firstborn shares |
| A50 Major fire-once | Natural and cluster entries share eligibility; manual launches and internal cycles do not rearm it or duplicate Major pacing |

## Completion

Implementation completion follows the repository rules: available specialist audits and MCP checks are used where they answer a concrete question, unavailable ones are recorded as limits, and live gameplay validation belongs to the user.
