# Event 83 probability and sequence audit plan

## Audit ownership and evidence classes

Assign the actual audit to `chaosx_ai_probability_auditor`. Begin with `hoi4.probability_inspect` on the implemented event, upgrade selector, conversion families, eligibility conditions, current cluster path, and shared picker context. The profile was read in this planning session, but no executable auditor or HOI4 probability service was available.

Use exact arithmetic only for fully specified conditional selections. Use evaluated engine scenarios for actual installed triggers and weights. Mark Monte Carlo estimates as sampled, bounds as bounds, and unresolved keys as unresolved. A random seed replay in the included Python model is not proof of game multiplayer determinism.

## Named scenarios

| Scenario | Inputs | Required question and evidence |
| --- | --- | --- |
| P01 baseline_new_agency | Chaos 0, no agency, complete valid registry | Does creation leave exactly one normal grant and one recruit entitlement? |
| P02 inclusive_thresholds | Chaos 199, 200, 399, 400, 599, 600 | Does each boundary choose the specified replacement package? |
| P03 disabled_middle_or_upper | Selectively disabled evolutions at Chaos 650 | Does the highest enabled qualifying package win independently? |
| P04 newly_opened_successor | Synthetic and real prerequisite chains | Can a grant open a successor for the next draw without granting an owned increment? |
| P05 partial_tree | Two valid increments left, III package | Are there exactly two grants and three conversions, regardless of draw order? |
| P06 full_tree_each_package | Zero remaining valid increments, each package | Does every roll convert, without removing guaranteed capacity or personnel? |
| P07 country_restricted_tree | Country-specific and feature-gated definitions | Are invalid entries absent while every valid effective entry remains represented? |
| P08 registry_drift | A supported upgrade definition added or overridden | Is incomplete coverage detected rather than called exhaustion? |
| P09 all_conversion_families | All five families and both cryptology branches usable | Are family probabilities 20% each and individual cryptology outcomes 10% each? |
| P10 restricted_conversion_families | Some families unavailable | Are remaining families renormalized equally, with the crypto split only inside its family? |
| P11 duplicate_conversions | Repeated same-family outcomes | Does every draw retain full value and its own expiration? |
| P12 evolution_II_specialty | Five, fewer, or zero usable specialties | Is there one eligible specialty or the disclosed exceptional slot conversion? |
| P13 staggered_repetition | Fires at days 0 and 60, 90/180-day rewards | Do separate deadlines and resulting totals agree with the source spec? |
| P14 snapshot_before_Chaos | Chaos 198, legitimate +5 on commit | Does the first award stay baseline while the next firing can use I? |
| P15 cluster_membership | Current Intelligence mapping and member flags | Is Event 83 Low without changing other members' fire-once rules or counting recipients as incidents? |
| P16 dense_late_campaign | Repeated III packages, many countries, varied trees | What capacity growth, temporary overlap, native limits, and performance follow? |
| P17 host_client_replay | Same saved campaign, recipients, and firing identity | Do game clients agree without local rerolls or duplicate commits? |

Use `hoi4.probability_evaluate` for named world states, `hoi4.probability_sweep` for thresholds and eligibility boundaries, `hoi4.probability_simulate` for declared uncertain long-run inputs, and `hoi4.probability_compare` for before/after behavior. Use `hoi4.probability_render` when distributions, sequences, or unresolved paths are clearer visually. Do not fabricate tool output when an adapter is missing.

## Exact design arithmetic, not engine findings

With a fixed pool of N equally eligible increments, no prerequisite changes, and R grants not exceeding N, each increment has inclusion probability R/N. In a real prerequisite tree, those assumptions may not hold across successive draws. Inspect conditional paths rather than quoting R/N universally.

With all conversion families usable, one converted roll has a 20% chance to add a permanent slot. Five converted rolls therefore add one permanent slot on average, in addition to the guaranteed five. The probability of at least one slot conversion is 1 minus 0.8 to the fifth power, or 67.232%. These figures are exact consequences of the authored selection rule, not observed HOI4 behavior.

For each legitimate firing j, permanent capacity increases by the guaranteed package size plus that firing's actual slot conversions and any exceptional Evolution II specialty conversion. There is no event-owned saturation term. Native capacity sources are additional and are not represented by that equation.

The temporary contribution to a category at time t is the sum of grants whose start time is at or before t and whose expiration is after t. A same-category repeat therefore adds a contribution rather than refreshing an old expiration. This invariant is tested in the semantic model.

## Frequency and AI limitations

Do not derive an Event 83 firing frequency from this package alone. The current global picker, cluster incidence, eligibility, history, recovery settings, and campaign state control selection. Historical simple timer or weight values must not be assumed to describe the inspected mechanics document or current code.

Native operative assignment priorities in Part 3 are design intent, not a newly invented weighted AI route tree. If implementation needs custom numerical preferences, submit the actual rules and concrete scenarios to the auditor. Do not present unimplemented descriptive priorities as measured AI probabilities.
