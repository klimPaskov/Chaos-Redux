# Military Madness: Acceptance and Probability Scenarios

These are future implementation checks, not executed tests.

## User requirement coverage

| Requirement | Design location | Required evidence |
|---|---|---|
| Minor Repeatable, Chaos level 1, Military Preparation Low | Part 1 | Catalog and runtime classification agree |
| Every valid country independently affected | Parts 1 and 2 | Complete recipient trace and separate draws |
| Exactly 365 days | Parts 1 and 4 | Days-based activation and expiry |
| 1, 3, 6 and 10 rolls | Parts 1 and 2 | Exact counts at every stage |
| Broad minima 1, 1, 2 and 3 | Parts 1 and 2 | Quota trace, including duplicates |
| Thresholds 200, 400 and 600 | Part 1 | Boundary and disabled-stage cases |
| No stage after Evolution III | Part 1 | No further stage or hidden terminal grant |
| Statistic and magnitude both random | Parts 2 and 3 | Registry and per-entry magnitude trace |
| Broad statistics remain available at every stage | Part 2 | Union membership at each stage |
| Duplicates and same-statistic stacking | Parts 2 and 4 | Within-package and cross-package cases |
| No archetypes or national balancing | Parts 1 and 2 | Equal entry weights, no usefulness filters |
| Terrain, weather, mission and unit coverage from vanilla, DLC, country and Chaos Redux sources | Parts 2 and 3 | Coverage document with every candidate's disposition |
| Only technically unusable candidates excluded | Part 2 | Every exclusion has a technical reason |
| Old and new packages expire separately | Part 4 | Staggered and same-day expiry cases |

## Probability evidence

A normalized probability is exact only when the registry is complete for the country's content configuration.
Audit guaranteed broad draws separately from union draws and magnitude separately from statistic.
Aliases and entries listed in several stage pools must not gain extra weight.
Use `hoi4.probability_inspect` and named scenarios where the tool supports the draw; otherwise calculate from the script and state the assumptions.
The package lottery is separate from the event's selection weight in the global pool and the cluster.

## Probability cases

| ID | Case | Expected result |
|---|---|---|
| P01 | Baseline, complete broad pool | One broad entry and one legal magnitude |
| P02 | Evolution I | Three rolls, at least one broad |
| P03 | Evolution II | Six rolls, at least two broad |
| P04 | Evolution III | Ten rolls, at least three broad |
| P05 | Every free slot also draws broad | Accepted without substitution |
| P06 | Every slot draws the same entry | Accepted; all magnitudes recorded |
| P07 | Broad entry listed in several stage pools | One union entry, no extra weight |
| P08 | Two sources alias the same effect | One registry entry |
| P09 | Broad and unit-specific effects in one calculation family | Distinct only when their real scope differs |
| P10 | Two countries with very different forces | Same pool and weights when technical capabilities match |
| P11 | Landlocked country with no ships | Naval entries remain |
| P12 | Peacetime country with no deployed forces | Combat entries remain |
| P13 | Missing optional system | Only entries needing that system are absent |
| P14 | Country-origin effect with a national application | Origin alone does not restrict it |
| P15 | Saturated or useless result | No reroll or compensation |
| P16 | Magnitude endpoints | Both reachable with correct signs and units |
| P17 | Flat capacity statistic | No percentage conversion |
| P18 | Boolean-only candidate | Recorded type conflict, no fake magnitude |
| P19 | Empty mandatory broad pool | Occurrence fails before distribution |
| P20 | Report, row or tooltip interaction | Consumes no gameplay randomness |
| P21 | Registry entry appended | Future draws include it; saved packages unchanged |
| P22 | Global event selection | Repeat weights, caps and cluster cadence unchanged |

## Stage and lifecycle cases

| ID | Setup | Expected result |
|---|---|---|
| L01 | Chaos 199, 200, 399, 400, 599, 600 | Stages 0, I, I, II, II, III |
| L02 | Chaos 1000 or more | Still at most Evolution III |
| L03 | Evolution III disabled at 650, II enabled | New package uses Evolution II |
| L04 | Evolution I disabled, II enabled at 450 | Evolution II opens directly |
| L05 | All Evolutions disabled | Baseline package |
| L06 | Chaos rises during distribution | All recipients keep the frozen stage |
| L07 | Chaos falls while an older high-stage package is active | Old package unchanged |
| L08 | Firings at day 0 and day 100 | Expiries at days 365 and 465 |
| L09 | Two firings on the same day | Two packages with matching expiry |
| L10 | Delivery callback repeated | No extra package |
| L11 | Expiry callback repeated | No extra removal |
| L12 | Report opened, postponed or repeated | No reward, magnitude or timer change |
| L13 | Save just before or after expiry | No redraw, extension, residue or double cleanup |
| L14 | Event disabled with packages active | No new firing; cleanup continues |
| L15 | Ideology, leader or cosmetic tag change | Packages kept |
| L16 | Subject or independence change | Packages kept |
| L17 | Government in exile | Timer continues; national effects remain |
| L18 | Annexation, then release of the same tag | No inheritance or resurrection |
| L19 | Civil war copies national ideas | Packages and effects not duplicated to the new country |
| L20 | Country created after distribution | No retroactive package |
| L21 | Country vanishes before queued delivery | No award to an invalid recipient |

## Safety and composition cases

| ID | Case | Expected result |
|---|---|---|
| S01 | Two additive bonuses on one statistic | Raw sum, no multiplication |
| S02 | Two reductions beyond the valid range | Raw records kept; applied value valid |
| S03 | A saturated reduction expires | Rebuilt from surviving raw contributions |
| S04 | External reduction appears after the package | Applied value stays inside the proved domain |
| S05 | External reduction disappears | Event contribution recomputed and still beneficial |
| S06 | Dynamic modifier evaluation order changes | No drift, sign reversal or stale self-subtraction |
| S07 | Save and load changes application order | Same result as before saving |
| S08 | Very high positive stacking | Proved technical bound, no overflow |
| S09 | Percentage-point statistic | Display and engine unit agree |
| S10 | Penalty reduction | Reduces the penalty only |
| S11 | Organization capacity changes | Native current-value behavior, no healing exploit |
| S12 | Recruitment capacity falls at expiry | Native over-cap handling, no deletion |
| S13 | Experience gain expires | Earned experience remains |
| S14 | Many overlapping ten-roll packages | All records survive and each has a row |
| S15 | Statistic without a known unit or safe bound | Stays unverified, no generic percentage |
| S16 | Valid but currently ineffective statistic | Remains eligible |

## Presentation, AI and achievement cases

| ID | Case | Expected result |
|---|---|---|
| U01 | One baseline roll | Package row shows the value, unit and remaining days |
| U02 | Ten rolls with duplicates | Every roll listed in the row tooltip |
| U03 | Maximum possible overlap | Every active package has its own row |
| U04 | Next expiry removes some contributions | Spirit totals match the surviving packages |
| U05 | Saturated statistic | Spirit tooltip names the statistic and its limit |
| U06 | Last package expires | Spirit removed and category hidden |
| U07 | Foreign country | Cannot see another country's package rows |
| U08 | Event Details | Premise and progression only |
| U09 | Natural worldwide occurrence | One history record and one +5 Chaos impulse |
| U10 | Cluster delivery | No duplicate member firing or double Chaos |
| U11 | Forced or debug occurrence | No Chaos and no achievement progress |
| U12 | AI at war rolls +250% land attack | Aggressive front strategy while the contribution lasts, removed at expiry |
| U13 | AI rolls naval invasion preparation, no coastal enemy | No invasion priority change |
| U14 | A1 capital moved after opening | Frozen target remains |
| U15 | A1 ally captures the capital | Does not count as the recipient's seizure |
| U16 | A2 states ceded, released or de-cored | Frozen recovery set unchanged |
| U17 | A2 required state lost during the hold | Hold restarts within the original deadline |
| U18 | A3 new package during the 90-day hold | Attempt interrupted; package granted normally |
| U19 | A3 diplomatic transfer instead of conquest | Not a qualifying gain |
| U20 | Achievement during an invalid country lifetime | Rejected |
| U21 | Four reports, spirit icon, three achievement triplets | Fourteen runtime textures wired to their consumers |

## Scale

Test with a large country roster, the full registry, repeated same-day occurrences and many active packages.
Distribution may visit every recipient once when the event fires; expiry, cleanup, display and achievement observations stay bounded to active records, and no recurring world scan is added.
