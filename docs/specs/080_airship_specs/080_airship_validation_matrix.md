# Event 080: Validation and probability scenario plan

These are required implementation checks, not completed tests.

## Functional acceptance matrix

| ID | Scenario | Required observation |
|---|---|---|
| V01 | Uninterrupted baseline departure | Position 0 at launch and position 1 after two days |
| V02 | Full healthy clock-only fixture | Position 120 at day 240 and final arrival at day 242 |
| V03 | A two-day additional repair | Completion shifts to day 244 without an added or skipped route step |
| V04 | Pause partway through a travel window | The remaining travel time is preserved through the pause |
| V05 | Save and load before a due transition | Exactly one transition and one persisted exposure outcome |
| V06 | Two human countries open the map | No duplicate scheduler, decision payment, or route advancement |
| V07 | United States is an AI country | The voyage progresses without a human-only mission owner |
| V08 | Final arrival suffers a fatal incident | Crash only, with no success rewards or homecoming news |
| V09 | Position 121 map rendering | A valid final state is shown, with no missing sprite or stale 120 route |
| V10 | Original stop registry comparison | Every original stop remains at its original route position |
| V11 | A legacy no-land-predicate position | Actual geography proves land or open water, without guessing from `always = no` |
| V12 | Index-1 movement discrepancy | Trigger, actual route location, and final region data agree after a documented correction |
| V13 | Occupied land beneath the route | The controller receives host content and costs, not the displaced owner |
| V14 | Controller changes during a repair | Only valid undelivered work moves to the new responsible host |
| V15 | Controller changes after impact | Retaliation target remains the impact snapshot, rescue uses the new controller |
| V16 | Valid ocean position | No territorial host, no fabricated local deaths, and no last-host declaration |
| V17 | Emergency diversion | Actual branch location changes, canonical route order and remaining steps do not |
| V18 | Denied or invalid diversion destination | No random owned-state fallback and a clear remaining valid response |
| V19 | Condition reaches zero in flight | A single physical crash at the actual position |
| V20 | Evacuated grounded ship becomes unserviceable | A write-off or abort, without manufacturing a flight crash |
| V21 | Several countries share one legacy region | One operational exposure, with no probability multiplication by country count |
| V22 | Many aircraft and anti-aircraft units nearby | A bounded local hazard category, not an uncapped sum |
| V23 | Host is fighting far away | No local combat modifier without actual local exposure |
| V24 | Repair at Condition 90 | Tooltip shows a maximum 10 restored Condition and the real cost |
| V25 | Exact resource affordability boundary | A country holding exactly the cost can pay, and one below cannot |
| V26 | Repeated cancellation and reopening | No free repair, duplicated refund, repeated reward, or rerolled incident |
| V27 | A response window expires in multiplayer | The displayed standing-order default resolves once |
| V28 | Trial suspended by emergency | No ground-time exposure credit or successful unfinished result |
| V29 | Four trial families inspected | Each uses valid graph targets or the documented bounded XP conversion |
| V30 | Third and fourth successful trials | The research and XP caps hold across the whole voyage |
| V31 | Chaos crosses an evolution threshold | Eligibility occurs without an instant unsupported midair refit |
| V32 | Grand Tour refit completes | Physical capacity changes once and only real boarded people appear |
| V33 | Flying City refit at a poor field | No false technical capability, no completed conversion |
| V34 | Late Flying City installation | Visual form can change, unearned thirty-step completion reward remains locked |
| V35 | Chaos falls after a physical refit | Existing form persists without repeat activation or duplicate rewards |
| V36 | Boarding and normal disembarkation | No state population changes and Deaths is unchanged; boarding-group counts match the manifest |
| V37 | Onboard deaths across several boarding groups | Deaths are split by group and debited once from each origin state, with one Deaths registration each |
| V38 | An origin state changes controller or is nearly empty | The group keeps its boarding attribution, and a capped debit is reported at its applied amount |
| V39 | Birth and stowaway discovery | The relevant group count rises by one with no population transaction |
| V40 | Missing visitor returns | Missing status closes and the person is excluded from any later presumed-loss registration |
| V41 | Rescue crosses a controller transfer | Work credit and survivor counts persist without double counting |
| V42 | Crash with partially empty hull | Structural profile uses the actual form and onboard casualties use actual occupants |
| V43 | Population-limited local impact | Reported deaths equal the shared helper's actual applied loss |
| V44 | Immediate foreign crash | War exists before a report option is clicked and no war goal is created, including a Peace Movement-led USA; Event 84 observes the same war without veto, duplicate declaration, or forced white peace |
| V45 | Friendly or same-faction impact controller | Minimal supported separation permits the exact required war, without unrelated faction destruction |
| V46 | Subject, overlord, truce, pact, or democratic restriction | Each blocking relationship is tested and resolved explicitly, with no silent skip or retarget |
| V47 | Existing American war with the controller | No duplicate declaration or generic war Chaos |
| V48 | Domestic crash | No self-declaration or false foreign responsibility |
| V49 | USA disappears while voyage is active | Flight terminates safely into civilian recovery accounting, with no resurrected state |
| V50 | Local military impact | Only eligible nearby units suffer bounded native losses, without stockpile or Deaths duplication |
| V51 | Valid wildfire handoff | One accepted public-owner sequence, future fire impact, separate impact and fire losses |
| V52 | Existing compatible fire card | Merge under the fire owner's rules, with no missing accepted impact |
| V53 | Urban or industrial fire at a forest-ineligible site | A verified compatible owner handles it, or the branch remains an explicit release blocker |
| V54 | Fire continues after Airship ends | Airship cleanup does not erase the shared fire or its recovery tasks |
| V55 | Crash and later rescue meet the super-event gate | One verified presentation after confirmed qualifying facts, with no use of unconfirmed missing people |
| V56 | Routine peaceful full voyage | Local flavour is substantial and global news remains within its ordinary budget |
| V57 | Host repeatedly opens a stop event | One visit reward and no extra passenger exchanges or payouts |
| V58 | Success with earned evolution exposure | Only qualified extra rewards are paid once |
| V59 | Clean-voyage achievement after a presumed loss | Achievement remains locked |
| V60 | Rescue achievement after deliberate attack | Instigator cannot farm rescue credit for its own manufactured crash |
| V61 | Nonhuman controller with actual territory | Civilian tourist flavour is adapted or excluded while physical routing remains valid |
| V62 | Long names and large casualty values in GUI | No clipped values, incorrect owner names, or unclickable controls |
| V63 | Reduced-motion display | Every route, Condition, and emergency state remains readable |
| V64 | Whole source-to-runtime review | No guessed final copy, missing active assets, unresolved release blockers, or unperformed checks labelled passed |

## Probability questions

The probability auditor must evaluate the actual composed decision and incident sequences, not a hand-written duplicate that omits cancellations, repairs, terminal locks, or controller changes. Use the project's probability workflow through `chaosx_ai_probability_auditor`.

| ID | Sweep or fixture | What must be measured |
|---|---|---|
| P01 | Fixed Condition at sound, worn, damaged, and critical | Incident and fatal exposure per leg, with conditional weights distinguished |
| P02 | 121 steps with all normal wear and original service stops | Survival, completion, delays, repairs, and Condition distribution |
| P03 | Three American standing orders with identical initial world | Risk, time, expense, and whether one policy strictly dominates |
| P04 | Quiet, moderate-war, and heavy-local-war maps | Actual local exposure sensitivity without global country-count inflation |
| P05 | Zero, one, and many foreign controllers inside a legacy region | Exactly one ship exposure and correct actual host selection |
| P06 | Baseline, Grand Tour, experimental, and Flying City starts | Completion, actual casualty ranges, cost affordability, and earned rewards |
| P07 | Evolution eligibility at launch, middle, and final quarter | Activation timing, physical refit feasibility, and no late reward farming |
| P08 | Poor and wealthy US and host economies | Solvable service choices, safe-abort frequency, and unpaid work rejection |
| P09 | No experiments, one experiment, four commitments | Risk and useful-data rates, interruption behaviour, XP and research caps |
| P10 | Ordinary and prepared rescue across all crash profiles | Death conservation, rescue cost, survivor rates, and threshold sensitivity |
| P11 | Repeated save/load, choices opened in different orders | No resampling or duplicated events and identical causal results |
| P12 | Routine flavour across complete peaceful voyages | Passenger and social share, host popup cadence, thread congestion, news volume |
| P13 | Faction and subject crash targets | Exact immediate war outcomes, not a numerical simulation substitute for engine tests |
| P14 | Fire acceptance, rejection, and existing-card merge | No missing loss ownership or duplicate casualty contribution |
| P15 | Achievement fixtures with near-miss conditions | Difficult objectives, no empty-ship or deliberate-crash exploits |
| P16 | Country count and elapsed-time performance sweep | Bounded active work, independent of irrelevant world-country growth |

Use a published reproducible seed set and enough independent full-voyage runs to report uncertainty. A proposed initial batch is 10,000 voyages for each principal policy and world fixture, expanded where rare outcomes or confidence intervals remain unresolved.

### Fixed-Condition reference arithmetic

This table checks only the proposed fixed-Condition model for P01. It ignores repairs, wear, delays, changing hazards, and Condition reaching zero, so it bounds intuition rather than predicting a voyage. The chance of at least one direct fatal branch in 121 identical exposures is `1 - (1 - p)^121`.

| Fixed band | Incident probability | Fatal given incident | Direct fatal per exposure | At least one in 121 identical exposures |
|---|---:|---:|---:|---:|
| Sound | 5% | 0.5% | 0.025% | 2.98% |
| Worn | 10% | 2.5% | 0.250% | 26.13% |
| Damaged | 20% | 10% | 2.000% | 91.32% |
| Critical | 35% | 30% | 10.500% | 99.99% |

The worn, damaged, and critical rows show why deterioration must create a credible reason to repair.

## Design acceptance targets

A peaceful competent baseline AI should normally complete the voyage. An initial calibration target is 70% to 90% completion after normal wear, actual service opportunities, occasional incidents, and sensible repairs. This is deliberately a range pending the recovered original stop registry. Do not claim it is achieved from the fixed-Condition formula alone.

A critical ship that repeatedly refuses repair should be unsafe within a handful of subsequent exposed legs. A competent safety-first policy should reduce deaths while costing additional time and resources. A full programme should create useful opportunities but should not become an obviously superior free reward setting. Host costs must scale without making every minor host's only feasible response refusal.

Routine passenger and host content should remain visible enough to define the experience. Aim for roughly 15 to 30 interactive routine stories during a peaceful voyage, with additional short non-interactive observations as useful. This target is subject to the actual stop count, host cooldowns, and the three-thread limit. Ordinary global news should remain around five to seven items, with genuine separate crises handled by the exceptional rules.
