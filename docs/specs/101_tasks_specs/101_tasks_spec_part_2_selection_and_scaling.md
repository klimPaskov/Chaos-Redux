# Event 101: Selection and dynamic scaling

## Prepare a credible task before drawing it

Selection has four draws after preparing the valid pool: choose a human country, choose a family, choose an archetype, then choose that archetype's target or coherent target set. Commit only after a final read-only eligibility check. If the selected country's candidates changed, draw uniformly from the remaining untried prepared eligible countries and revalidate the new selection. Try each prepared country at most once in that attempt. Never use fixed country order for this fallback. If none remain, return an unavailable result to the shared firing system.

Country selection is uniform among currently eligible human-controlled countries. The previous recipient is not removed merely to force rotation. Fairness comes from one country entry, active-task exclusion, the rest period and the same eligibility checks for every player. Any future change to recipient weights needs a new multiplayer probability review.

Candidate generation is bounded by the country's relevant fronts, owned states, declared partners and active crisis subscriptions. Build these pools when a task is being prepared. During an active task, inspect only its recorded targets. UI refresh must not scan every country or state.

## Hard eligibility

Every candidate must satisfy all of these requirements before receiving a positive weight:

| Requirement | What must be established |
| --- | --- |
| Human recipient | A current human-controlled country with no active Event 101 task |
| Authority | The recipient can carry out the necessary action under its current government, subject and diplomatic rules |
| Unfinished objective | The complete success predicate is false at assignment, and the new work is materially above the committed baseline |
| Relevant context | The war, threat, project need, partner or crisis actually exists |
| Reachable target | Verified land access, operational range or existing owner route supports a practical attempt |
| Usable capacity | The country can supply the work without assuming an unresearched technology, nonexistent resource or another player's consent |
| Measurement | The adapter can distinguish the required result with the promised timing and attribution |
| Time | The conservative feasible estimate fits the task and any owning crisis hard deadline |
| Meaningful stakes | The quoted reward is useful and the penalty can be applied within the consequence limits |

An absent measurement capability is not assigned a guessed probability. It makes that candidate unavailable and creates an explicit implementation coverage gap for the affected accepted archetype. The implementation cannot claim all six families complete while an entire family is disabled by an unresolved adapter.

## Family weights

These are initial tuning weights. They express preference among valid families and are not event firing probabilities. A family with zero valid candidates has zero weight before normalization.

Determine the country-context row before applying the family table. A country at war uses the pressured-war row when at least one physically eligible relevant candidate carries verified current front or owner pressure, otherwise the stable-war row. A country at peace uses the credible-threat row when a verified existing threat supports a real eligible protection or preparation opportunity, otherwise the no-immediate-threat row. A pressure marker needs explicit current owner or military evidence in its adapter. Global Chaos, a country name or a hypothetical future war is insufficient. With several fronts, any qualifying current pressure selects the pressured country row, while the evolution factor below still applies only to its own qualifying targets.

| Country context | Offensive | Defensive | Preparation | Industrial | Diplomatic | Crisis |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Peace, no immediate threat | 0 | 0 | 30 | 40 | 30 | 20 |
| Peace, credible existing threat | 0 | 25 | 40 | 20 | 25 | 30 |
| War, stable front and usable reserve | 40 | 30 | 20 | 15 | 10 | 30 |
| War, pressured front or strategic losses | 15 | 45 | 20 | 10 | 10 | 40 |

The crisis column is active only when a real qualifying episode exists. A high weight does not authorize a task the country cannot accomplish. A diplomatic task during war needs a practical wartime purpose. Defensive tasks during peace require a verified active threat or an owner's protection window, not an arbitrary peacetime countdown.

Trials Under Pressure gives a factor of 2 to defensive and crisis target candidates whose recorded pressure actually applies. It gives an offensive target a factor of 1.5 only for an actionable local recovery objective. It does not make an overextended country attack a distant major. Chaos Tasks gives a further factor of 2 only to verified Chaos-owner crisis targets. A target qualifying for both crisis preferences therefore has factor 4.

Apply these target-specific factors through the four-stage draw without giving extra tickets to archetypes with many targets. For each archetype, first normalize its base target-quality weights into shares. Its evolution factor is the quality-weighted mean of its targets' individual evolution factors. The family's evolution factor is the simple mean of those archetype factors. Multiply the base family weight and history factor by that family mean. Within the selected family, multiply each archetype's initial weight 100 by its own mean factor. Within the selected archetype, multiply each target's quality weight by its own evolution factor.

This hierarchy gives equal initial archetype shares before explicit contextual factors. A larger raw target count never adds archetype tickets. The weighted means ensure that boosting a qualifying target does not give the same boost to an unqualified sibling. When every candidate in a family qualifies equally, the family gets the full stated multiplier and its initial equal archetype shares remain equal. The implementation must keep all four normalizations and their units explicit.

For example, a pressured wartime country with valid defensive, preparation and crisis families has base weights 45, 20 and 40. With both pressure and Chaos preferences active, the weights become 90, 20 and 160. The resulting conditional shares are one third, about 7.4 percent and about 59.3 percent. This calculation describes the specified pool only. It is not a claim that the engine or shared event scheduler has already been measured.

## Candidate quality and recent history

Within the selected family, each eligible archetype starts at weight 100 before the explicit evolution mean above. Choose the archetype before choosing its target. An archetype with twenty eligible states therefore does not receive twenty times the share of an archetype with one eligible state. A future archetype preference beyond the declared contextual factors needs its own justification.

Within the selected archetype, start each eligible target candidate at weight 100. Apply a factor of 1.5 when it resolves a demonstrable local bottleneck, such as the front's only practical supply connection or a partner's active defense need. Apply 0.5 when it requires a longer supported route with several external dependencies. Unverified route safety is ineligibility, not a smaller weight. Apply recent-history exclusions to the prepared candidates before these draws, then renormalize each surviving level.

The two target-quality factors multiply and each applies at most once. A supported long route that also resolves a real bottleneck therefore has base quality weight 75. Its separate evolution factor is then applied through the hierarchy above. Do not count the same route's multiple dependencies as several copies of the 0.5 factor.

Keep the last three committed task signatures per country, newest first. A signature contains family, archetype, exact objective identity and the owning episode where applicable. Append once on commitment. Terminal settlement updates that entry and never appends the same generation a second time. Once an assignment commits, it remains in this recent history even if it is later cancelled neutrally.

Use these rules in order:

1. Build the physically eligible pool first. Consumed crisis outcome receipts remain permanently ineligible and are never history exceptions.
2. Apply exact-objective exclusions from all three retained signatures, then the newest signature's archetype exclusion.
3. If that leaves no candidate, remove the newest-archetype exclusion first. If the pool is still empty, remove exact-objective exclusions in signature order from oldest to newest, stopping as soon as a candidate survives.
4. On the surviving pool, apply a family factor of 0.5 for each occurrence in the newest two signatures, at most twice. If every surviving family would be penalized, use family history factors of 1 for that draw.

The family factor never excludes a candidate and does not participate in the exclusion-relaxation loop. This total order preserves a different objective in the same archetype before restoring an old exact objective. No step relaxes physical eligibility, human control, authority, time or proof requirements.

A military front with only one viable defense task may repeat after the rest period. Its new baseline, context and deadline are recalculated. A crisis outcome receipt already used by Event 101 cannot be reused, even if all other task candidates disappeared.

## Capability inputs

The implementation gathers a compact private capability record. The player does not manage these inputs as extra task statistics.

| Domain | Inputs | Direction of scaling |
| --- | --- | --- |
| Land operations | Fielded manpower, supplied usable formations, relevant enemy strength, friendly access, front distance and target importance | Larger capable forces permit larger objectives, weak supply reduces scope and lengthens time |
| Preparation | Existing usable branch, equipment deficits, recruitable manpower, training requirements and relevant production | Work follows the force the country can equip, not raw division count |
| Industry | Available usable civilian capacity, verified construction costs and modifiers, slot headroom, baseline damage, ownership and access | More usable capacity raises work, damaged or distant infrastructure adds time |
| Production | Relevant cumulative production counters, a valid observed rate or a conservative documented production estimate, existing deficits and resources | Larger real output permits larger quantities, shortages reduce feasible demand |
| Diplomacy | Current legal actions, relations, common threats, existing agreements, reachable delivery route and actual available resources | Greater distance or an existing relationship gap requires more time and work |
| Crisis | Owner epoch, phase, severity, participant role, permitted response routes and hard deadline | Scale follows the owner's attainable response, then adds a task premium within that response |

Do not use a country population as a substitute for equipment or usable industry. Do not use total military factories as proof that a particular production line is operating. Do not use state-center distance as proof of a traversable land or sea route. The implementation contract distinguishes verified getters from adapter requirements.

Pre-assignment rate history must come from an existing verified player-country sampler or a documented conservative estimate. Event 101 must not manufacture a seven-day historical rate from a single counter read. If neither exists for a production candidate, choose another valid candidate and record the missing rate adapter for implementation work.

## Workload and deadline calculation

Each archetype defines a native unit of work. Examples are a target state, a useful building level, newly qualified manpower, produced equipment or days of uninterrupted protection. Different units are never added into a fake common task currency.

Use the following mathematical contract. These symbols are specification notation, not HOI4 commands:

- `P` is conservative usable output per day in the task's actual unit at the frozen sustainable allocation. For industry and equipment, it already includes the selected share of relevant national capacity, normally 25 to 40 percent. It is not the country's full theoretical output.
- `W` is the archetype's intended work window.
- `M` is the evolution workload multiplier.
- `Q` is required new work, rounded to a valid unit and bounded by actual opportunities.
- `Twork` is the conservative time required for `Q`.
- `Taccess` covers verified travel, mobilization, setup or diplomatic delay.
- `Thold` is a required consolidation or protection interval.
- `Slack` is 25 percent of `Twork + Taccess`, increased to 50 percent for a disrupted but still feasible route.

For rate-based tasks, start with `Q = P × W × M`, then round down to a whole attainable work quantum. A building or formation quantum is indivisible. If rounding would produce zero useful work, the candidate is ineligible. For territorial tasks, select the smallest strategically coherent target set whose estimated effort fits the same budget. A major's task may be one very important defended state rather than several arbitrary provinces.

Calculate the deadline duration as `ceil5(Twork + Taccess + Thold + Slack)`. `ceil5` rounds up to the next five whole days. Whole-day engine granularity and naturally derived quantities are valid exceptions to authored round tuning. The task starts at the actual assignment time, not a later acknowledgement.

The base multiplier is 1.00. Add 0.25 when Higher Stakes is active and add 0.25 when Chaos Tasks is active. Either track alone therefore gives `M = 1.25`, both give `M = 1.50`, and neither gives `M = 1.00`. Trials Under Pressure changes context selection and compensation rather than multiplying the workload again. Increasing work requires recalculating the deadline and the feasibility check. It never means raising quantity and keeping an obsolete timer.

The following windows are starting design bands, not universal fixed timers:

| Work | Intended active work or protection window | Typical extra time |
| --- | --- | --- |
| Local capture or recovery | 20 to 45 days | Access and a 5 to 15 day consolidation period |
| Sustained defense | 30 to 90 days | Verified redeployment or protection setup |
| Equipment or branch preparation | 60 to 120 days | Training, delivery and a 10 to 20 day readiness hold |
| Ordinary development | 90 to 180 days | Actual building cost, disruption and commissioning |
| Major feasible development | 180 to 270 days | Multiple connected work packages and delivery |
| Diplomacy and support | 60 to 120 days | Relation growth, shipment and a 15 to 30 day useful duration |
| Crisis response | Owner-derived | Never later than the relevant owner hard deadline |

A justified emergency can be shorter. Its objective must be correspondingly local and achievable. The generic ninety-day mission guidance does not force an immediate military response to last three months. Conversely, a small country's slow construction must not be assigned a short timer because its absolute target is one building.

## Project size and opportunity cost

Use a sustainable allocation, not all national production. The initial tuning target for an ordinary industrial or equipment task is 25 to 40 percent of the country's relevant usable capacity during its work window. Higher Stakes can reach 50 percent only when the country has enough reserve for its existing commitments. A crisis task must respect the owner's essential defense and recovery floors.

Do not take the player's current idle capacity at face value when it can be manipulated immediately before a draw. Compare structural usable capacity with existing essential commitments and recent sampled use where available. Freeze the accepted result at assignment. Closing factories or deleting formations after assignment cannot reduce the task.

The system can offer a smaller task to a country with little spare capacity. It cannot turn a zero-capacity country into a viable construction or deployment candidate by inserting a hardcoded minimum. A country with no civilian capacity may still have a genuine diplomatic or defensive opportunity.

## Worked calibration fixtures

These are synthetic balancing cases using invented inputs. They demonstrate the formulas and must be replaced or supplemented with actual campaign fixtures during implementation.

| Fixture | Feasible input | Required work and time | Expected selection behavior |
| --- | --- | --- | --- |
| Small peaceful country | One useful infrastructure level requires 80 days at a sustainable allocation, setup takes 10 days | Base duration is `ceil5(80 + 10 + 22.5) = 115` days | It receives one useful level, not a major's programme |
| Productive medium country | Verified output at the frozen sustainable allocation is 10 units per day, work window is 60 days | Base quantity is 600, work 60 days, setup 10, readiness hold 10, duration 100 days after rounding | A 600-unit production goal is viable if the exact counter and resources support it |
| Same country with Higher Stakes | Same output, `M = 1.25` | Quantity 750, work 75, setup 10, hold 10, duration 120 days | Quantity and reward rise together with a longer deadline |
| Pressured front | Local counterattack 20 days, access 5, consolidation 10, disrupted slack 12.5 | Duration 50 days | It can receive this bounded recovery goal, while a distant capital is rejected |
| Crisis ending soon | Owner permits 25 days of work, response needs 30 days before slack | No feasible quantity fits the minimum useful objective | Reject this crisis candidate even at Chaos 600+ |

## Stability of the quotation

The final candidate is rebuilt and checked immediately before assignment. Snapshot its public terms only after that check succeeds. No reward or recent-recipient history is committed on a failed preflight.

A changed campaign can make the task harder without invalidating it. The player remains responsible for ordinary setbacks. Neutral cancellation requires a named external cause and exact evidence, as described in the implementation contract. There is no background stream of easier replacements.

All constants, multipliers, workload windows, grace rules and outcome ceilings belong in one documented Event 101 tuning group. The formulas and units must be shared by task generation, tooltips, deadline changes and tests. Display rounding must not alter the actual requirement or affordability boundary.
