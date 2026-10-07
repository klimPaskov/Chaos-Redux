# World Claims: canonical proposed tuning

Status: design values, not measured balance. User-fixed entries are identified below. All other values are parent-authored expansion proposals. This file owns numbers used by the design. Implement them in event-owned constants or the shared system that already owns a value. Do not scatter tuning literals through effects, triggers, GUI, or localisation.

## User-fixed values

| Parameter | Value |
| --- | --- |
| Event identity | 086, World Claims |
| Catalog type / status | Minor Repeatable / To Be Reworked |
| Catalog Chaos level / cluster | 1 / Formables, Low, no secondary cluster |
| Evolution Chaos thresholds | I 200, II 400, III 600, IV 800, V 1000 |
| Starting-Compliance ceilings | Baseline 25, I 50, II 75, III 75, IV 100, V 100 percent |
| Immediate frontier coverage | Every valid foreign land-neighbor of any owned state |
| Core access | From III, earned through sustained control and high Compliance |
| Maximum simultaneous national spirits from this event | One staged confidence effect in this design, within the project's broader limit |

One, two, and three in structural rules are cardinalities, not percentage tuning. State IDs, native sprite dimensions, tier IDs, graph depths, and schema versions need not be multiples of five. Gameplay costs, bonuses, and durations here use five-unit increments.

## Frontier depths and allowances

Let `F` be the number of distinct valid immediate foreign land-neighbor states in the wave snapshot. Let `N` be the number of owned valid terrestrial states. `up5(x) = 5 * ceil(x / 5)`. Limits apply to newly selected optional targets, not existing marked targets. Every accepted target needs a shortest valid path through owned states or World Claims targets accepted in preceding layers of this same frozen-depth calculation.

| Profile | Owned-seed maximum depth | Ring 1 | Ring 2 new-target allowance | Ring 3 | Ring 4 | Ring 5 |
| --- | ---: | --- | --- | --- | --- | --- |
| Baseline | 1 | All | None | None | None | None |
| I | 2 | All | `min(20, max(5, up5(F / 4)))` | None | None | None |
| II | 3 | All | `min(50, max(5, up5(F / 2)))` | `min(25, max(5, up5(F / 4)))` | None | None |
| III | 3 | All | Same as II | Same as II | None | None |
| IV | 5 | All | All | `min(100, max(5, up5(F)))` | `min(50, max(5, up5(F / 2)))` | `min(25, max(5, up5(F / 4)))` |
| V | 5 plus established-network extension | All | All | Same as IV | Same as IV | Same as IV |

When `F = 0`, no territorial claim grant occurs, regardless of profile or stored network. The minimum-five formulas are never evaluated as a consolation grant.

At V, take the old World Claims network in the snapshot, retain only components connected to currently owned territory by valid land adjacency, and discover its immediate foreign boundary. This extension receives at most `min(250, 100 + 25 * floor(N / 25))` additional new targets. A new target accepted by the ordinary owned-depth pass cannot become a seed of the established-network pass in that same firing. Candidates already added by the ordinary pass are removed before counting the extension allowance.

All snapshots use the same logical firing timestamp. Geography ranking is deterministic: selected-ambition relevance, valid path continuity, appropriate regional fit, then stable state ID. The first ring has no ranking-based exclusion. Claims from unrelated providers cannot serve as old World Claims network seeds without independent World Claims provenance.

## Core requirements

| Active profile | Continuous physical control | Current Compliance | Continuous time at or above that level | Maximum connection preparation credit | Absolute physical minimum with credit |
| --- | ---: | ---: | ---: | ---: | ---: |
| III | 360 days | 80% | 60 days | 25% | 270 days |
| IV | 120 days | 90% | 30 days | 25% | 90 days |
| V | 30 days | 95% | 10 days | 25% | 25 days |

The credited required duration is `max(absolute_minimum, up5(base_days * (1 - credit_fraction)))`. The late 30-day standard with 25% credit therefore requires 25 physical days. Credit never alters the independent high-Compliance interval. Continuous control can begin only after World Claims provenance exists. A lost control interval resets its physical and high-Compliance clocks.

Maintain threshold history for 80, 90, and 95 independently, even before a core-enabled profile activates. A dip below 95 resets the 95 clock, not a still-valid 80 clock. An observed jump to a threshold starts that threshold's clock at the verified change time. Without evidence of earlier continuity, initialize it at the first reliable observation.

## Dynamic formation thresholds

`E` is the adopted, fixed ambition envelope. `P` is the subset currently owned and controlled by the claimant. `Q` is the subset of `P` meeting the scale's physical holding requirement. Anchors must belong to `Q`. Fractions use exact integers: require `100 * count >= percentage * denominator`, which is equivalent to rounding the required state count up.

The integrated subset `I` belongs to `Q`. A member is either already a native core of the claimant, or an administered noncore state with at least 90 continuous days of verified control and the scale's formation Compliance floor in its actual native occupation context. Existing noncore possessions can therefore qualify through ordinary native integration even without World Claims provenance. This does not grant them a World Claims Compliance entitlement or WC core eligibility. A native core does not bypass the physical holding requirement in `Q`. Formation integration is distinct from automatic World Claims core eligibility.

| Scale | Earliest profile | Discovery: controlled envelope / minimum held states | Required `Q / E` | Required `I / Q` | Formation Compliance floor for noncores | Holding requirement in `Q` |
| --- | --- | --- | --- | --- | --- | ---: |
| Regional | I | 40% / 5 | 80% | 50% | 50% | 90 days |
| Large regional, peninsula, major chain, subcontinent | II | 40% / 10 | 80% | 60% | 60% | 120 days |
| Continental | IV | 40% / 25, plus a completed regional-or-larger milestone | 85% | 75% | 75% | 180 days |
| Transcontinental | V | 40% in each of at least two component regions, 50 total, completed continental milestone | 85% overall and 80% in each component | 80% | 90% | 180 days |
| Hemisphere | V | 40% / 50, completed transcontinental milestone | 90% | 85% | 90% | 180 days |
| Global proclamation | V | 40% / 100, held anchor on every valid continental group, completed continental or transcontinental milestone | 90% | 90% | 95% | 180 days |
| Finished-world milestone | V, global proclamation completed | Already adopted global project | 100% of every valid currently owned terrestrial state in the full active registry | 90% | 95% | 180 days |

The global envelope covers all valid terrestrial registry states. A genuinely unowned state is dormant in the active possession denominator until it has an owner. Becoming owned activates it for every global claimant. A country being defeated does not remove its still-owned states from the denominator. The UI explicitly identifies dormant unowned entries. This is a declared world-envelope rule, not dynamic pruning by the claimant.

A component or anchor set is fixed at adoption. Changes to current qualifying ownership do not shrink it. For scales below global, no unowned-state exception is implied unless the adopted geographic record explicitly defines it. Small native formables keep their own genuine thresholds. Dynamic curated groups smaller than the table minimum require an explicit registry exception with complete formation rules, not an automatic exemption.

Thresholds for an adopted ambition remain those selected at adoption. A later Evolution does not tighten its formation floor. Automatic core eligibility always uses the currently effective core profile. Successor ambitions adopt their own scale requirements.

## Projects and payments

| Family | Cost formula | Duration | Reward / failure | Reuse gate |
| --- | --- | ---: | --- | --- |
| Select public ambition | Free | 90-day switch lock | Free selection, frozen envelope | No incompatible running project |
| Civil integration | Let `R = min(25, registered administrative-region state count)`. PP `25 + 5 * ceil(R/5)`. Support equipment `100 + 25 * ceil(R/5)` | 120 days | +10 Compliance points, capped 100, once to this claimant-state / no defeat refund | One success per claimant-state for this family |
| Heartland connection | Let `G = min(25, selected corridor state count)`. Trucks `100 + 25 * ceil(G/5)`. Trains `5 * ceil(G/5)` | 180 days | 25% preparation credit once per included claimant-state / no defeat refund | At most 25 states, fixed corridor and anchors |
| Frontier consolidation pledge | Free | 180 days | Sustained-control milestone / disappointed confidence 90 days and 90-day retry lock | Selected ambition near completion, same target envelope |
| Border assurance | 25 PP per party, atomic at mutual acceptance | 180 days | At most 5 eligible Chaos reversal / breach once | One agreement for a country-pair and frozen overlap, no parallel duplicate |
| Dynamic proclamation | PP `min(200, 50 + 5 * ceil(envelope_state_count / 5))` | Immediate after all predicates | One confidence period, optional identity, connected objectives | New territorial identity or genuine successor |
| Native proclamation | Provider-owned genuine cost only | Provider-owned | Provider effects once, compatible WC recognition once | Genuine provider route, never duplicate cost/effect |
| Post-proclamation consolidation | Free | 180 days | Durable milestone / disappointed confidence 90 days | One success per completed ambition |

Civil integration uses one selected target in a registered administrative area; its bounded area size determines the cost, not the country's overall size. If no researched administrative group exists, use the selected ambition's connected local group with `R` capped at 25 and show that group before purchase. This fallback does not change the target or effect into an area-wide reward.

No paid family can accept an empty group. Counts and prices freeze at start. No more than two simultaneous projects per country, including pledges and post-proclamation consolidation. An assurance is a diplomatic agreement rather than a project slot, but a country can maintain at most two at once.

“Near completion” for a pledge means at least 75% of `E` is owned and controlled, all anchors are held, and the selected ambition's normal formation ownership threshold is reachable without changing the envelope. Pledge success can prove a holding milestone but never waive `Q`, `I`, or anchor conditions at proclamation.

## Confidence state machine

At most one event-owned confidence effect exists. `neutral` has no modifier. `confident` supplies +10 percentage points Stability and +10 percentage points War Support for 180 days. `disappointed` supplies -5 percentage points Stability for 90 days. A new valid success replaces the state with confident and starts its duration. A public mission failure replaces it with disappointed and starts that duration. Expiry returns to neutral.

Effects are temporary native modifiers or the verified equivalent. Do not add permanent values and subtract them later, since caps and intervening changes can make that arithmetic incorrect. Repeat callbacks do not refresh a duration twice.

## Timing and shared ownership

Evolution timing input: 90 days with an eligible higher stage, 60 at Chaos 800+, 30 at 1000+. These values require the verified shared timing adapter. They are not deterministic delivery promises or proven medians.

Existing minor countdown, repeat-weight recovery, cap halving, cluster pacing, and enabled-country semantics belong to the shared event engine. Source snapshots describe a 7–30-day event countdown and repeatable recovery by 20 with diminishing caps. Do not copy those values into Event 086's private scheduler. Inspect the live owner before wiring.

The Formables catalog's existing cluster Chaos level 3 is not overwritten by this event's level 1. Low is a severity role, not a statement that the event is an optional cluster member. The shared registry owner must resolve participation separately.

## Chaos receipts

New wave: +5 for at least five countries and five new claimant-state targets. IV/V wave touching at least 100 distinct newly targeted foreign states: +10 instead. Wave contribution cap: 20 in any rolling 360 days.

Public continental-or-larger pursuit: +10, once per claimant epoch and scale, after 100 still-foreign World Claims targets across at least five other governments and a real pursuit commitment. Its separate event-wide cap is 20 in any rolling 360 days. A commitment is a World Claims pledge or a native declared war against a named overlapped owner, recorded after adoption; a war already in progress is context, not a newly repeated commitment.

Assurance: reverse at most 5 of the linked unreversed public-project contribution after 180 unbroken days. A single receipt may be settled across agreements only up to its original charge. Reversals do not reset issuance history or the rolling cap's recorded charges.
