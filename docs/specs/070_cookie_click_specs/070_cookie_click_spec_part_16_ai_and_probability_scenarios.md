# 070 Cookie Click: AI and probability scenarios

## AI responsibilities

Normal pet acquisition is human-only.
The cookie's own automatic appetite and danger use deterministic state updates plus the explicitly declared weighted selections.
A human's disconnected-country policy follows part 14.
There is no hidden normal AI clicker.

The Cookie Empire's AI must operate a country that consumes territory and also needs a functioning army.
Its governing choice, production, construction, feeding, recruitment and target priorities need one coherent policy.
Winning a war while consuming the only functioning supply hub is a meaningful possible mistake, but cannot be the default rule.

## Governing-method preference

The following are authored starting weights.
They are not measured runtime probabilities.
Invalid routes receive zero before normalization.

| World state | Rapid consumption | Long-term farming | Population conversion | Direct destruction |
| --- | ---: | ---: | ---: | ---: |
| Weak host uprising under immediate attack | 45 | 10 | 15 | 30 |
| Supplied industrial region with stable civilian rear | 15 | 50 | 25 | 10 |
| Large civilian pool and shortage of Cookie manpower | 15 | 20 | 50 | 15 |
| Ruined encircled region with little long-term industry | 30 | 5 | 15 | 50 |
| Wide region with reliable subject administrations | 15 | 50 | 25 | 10 |
| Active Final Bite against a strong remaining coalition | 35 | 15 | 20 | 30 |

The AI chooses its governing method once when the central commitment is valid.
Do not redraw that choice each day.
A method's emergency reserve policy can change without changing the method itself.
An AI with a farming commitment can use an emergency material conversion to survive.
It cannot repeatedly flip to destruction to claim several exclusive completion rewards.

## Operational policy

At 75 or more Fullness, prioritize a supplied objective, necessary equipment production and method-specific development.
At 50 to 74, maintain ordinary operations and replace expended reserves.
At 25 to 49, prioritize delivery, compatible captured equipment and low-damage feeding sources.
Below 25, pause nonessential elite recruitment, reserve fuel for critical movement and select an actual emergency input.
At zero, survival, withdrawal and restoring supply outrank offensive focus prestige.

Protect the last functioning supply hub, sole usable port, capital rail link and necessary equipment production line.
A destruction method can override one of these protections only when it has a valid replacement or is making an explicit terminal defensive choice.
A population floor is an actual validity rule, not just a low AI weight.

Construction priorities are usable supply, body-equipment production, local repair, defensive positions and then expansion institutions.
A naval island setup puts port repair, convoys and ordinary naval capability before inland heavy units.
An inland setup does not save resources for an impossible battleship program.

## Military routes

| Situation | Preferred doctrine or program | Avoid |
| --- | --- | --- |
| Low industry, wide front and many recruits | Crumb mass and basic infantry, with cheap logistics | Heavy elite commitments without replacement capacity |
| Short front, adequate durable production and dangerous enemy attacks | Disciplined core, Chocolate Guard and reserves | Excessive elite ratios |
| Strong industry and fortified objectives | Heavy shaping, Oven Artillery and later Golems | Attacking without supply or movement support |
| Open terrain and enemy supply opportunities | Wafer Riders and support institutions | Isolated deep advances without held corridors |
| Island or coastal separation | Naval institution, escorts and transport capacity | Infinite hostile-border waiting with no way to cross water |
| Strong enemy air activity | Interception and protected airfields | Fuel-consuming aircraft that cannot be supplied |

Recruitment obeys available equipment, manpower, specialty caps and shared restrictions.
Scripted mobilization decisions use the same actual payment rules for AI and humans.
Do not compensate for poor AI by granting an unbounded daily off-map army.

## Diplomacy and target priority

External-neighbor declarations are mandatory country behavior after formation.
AI target priority chooses where to fight effectively, not whether the written border-war policy applies.
The host and threats to the capital receive first military attention.
Supply-connected industrial targets outrank an unrelated distant weak country.
A reachable port can outrank a larger land target when it unlocks a necessary theater.

Cookie-domain subjects remain outside the external enemy list.
A subject leaving the domain becomes eligible after its new relationship is real.
Do not use ideology matching as a substitute for domain membership.

In The Final Bite, war declarations follow the bounded queue.
Operational planning prioritizes reachable threats and transport preparation.
Being at war with an island does not imply immediate ability to land there.

## Reward selection

Use the family weights in part 02 after removing invalid candidates.
Do not claim each individual reward has the same chance.
Within a family, choose among currently valid packets with documented weights and capacity.
The anti-repetition rule applies to family history, not an infinite reroll until a desired output appears.

The 10 percent daily bonus check occurs only on successful full feeding.
An invalid bonus has a saved supported alternative.
The player cannot reopen the window or save and reload to redraw it.
A fully capped government family should not consume the whole daily budget while producing no value.

## Revolt timing

The five-cycle warning is a deterministic warning interval.
After it expires, Evolution II has a 20 percent chance per eligible cycle, with a forced revolt at the tenth such cycle.
Evolution III has a 40 percent chance per eligible cycle, with a forced revolt at the fifth.
Recovery before the authoritative commit cancels the pending danger.

Under unchanged eligibility and independent draws, the probability of at least one success after n ordinary draws is `1 - (1 - p)^n`.
The forced final draw truncates that distribution.
This is an analytical design calculation, not a statement that the current HOI4 adapter has been verified to implement those exact independent draws.

A fully controlled Evolution II warning therefore has nine ordinary random opportunities and a final forced opportunity.
Evolution III has four ordinary opportunities and a final forced opportunity.
The warning itself is not five extra random draws.
Eligible-cycle counting pauses or resets exactly as specified by recovery and warning state, not by whether the GUI was visible.

## Active evolution timing

Active evolution uses the project's nominal 90-day MTTH behavior after the required Chaos threshold and current state are valid.
Do not replace an MTTH field with a daily probability guessed from memory.
The exact cumulative timing depends on the supported game-version adapter and actual changing conditions.
Pre-fire evolved openings are a separate initialization path.

The probability auditor must start with `hoi4.probability_inspect`.
Use `hoi4.probability_evaluate` for named fixed states, `hoi4.probability_sweep` for thresholds, `hoi4.probability_simulate` for declared uncertain inputs, and `hoi4.probability_compare` after source changes.
Use `hoi4.probability_render` where a distribution or comparison is clearer than a table.
Exact, bounded, sampled and unresolved results must remain distinct.

## Required named scenarios

| Scenario | Inputs | Expected design result |
| --- | --- | --- |
| P-01, first weak cookie | E0, Level 1, 300 target, zero prior hunger | No immediate bite or revolt during the first grace cycle |
| P-02, uninterrupted weak starvation | E0, still below Level 10, ten complete zero-click cycles | Permanent death, bounded costs and no country creation |
| P-03, evolved weak starvation | E1, Level below 5, five zero-click cycles | Earlier permanent death if maturity has not been crossed |
| P-04, maturity boundary | E0 Levels 9 and 10, E1 Levels 4 and 5 | A single clear permanent-removal threshold without reversible re-entry |
| P-05, token feeding | E2 high Level, one click each cycle | No perpetual bite or revolt immunity |
| P-06, partial recovery | Armed warning, reach 75 percent immediately before deadline | Warning canceled before commit, no full daily reward |
| P-07, late rescue | A revolt already committed | Clicks no longer restore the pet or cancel wars |
| P-08, E2 fixed starvation | Level 20, H10, Z5, unchanged eligibility | Five-cycle warning then declared truncated 20 percent distribution |
| P-09, E3 fixed starvation | Level 15, H5, Z3 | Five-cycle warning then declared truncated 40 percent distribution |
| P-10, changing Chaos | Active pet crossing 200, 400 and 600, with later decreases | Valid sequential MTTH transitions, no automatic reverse evolution |
| P-11, capped government | PP, CP, XP, Stability and War Support near supported caps | Valid material alternatives or no unsupported grant, no reroll exploit |
| P-12, no naval relevance | Landlocked host with no meaningful naval system | No useless naval-only reward or fictional convoy cost |
| P-13, no research mutation adapter | E2 or E3 hungry pet | Unsupported progress consumption excluded and reported |
| P-14, small uprising | Two-state weak host and minimum army | Viable host remainder, five light formations and no arbitrary heavy army |
| P-15, major uprising | Strong host, high lifetime value and consumed assets | Bounded equipped-strength scale without correlated-stat explosion |
| P-16, reconquest loop | Repeated loss and recovery of the same farm or workshop | No duplicate first-time food, reward or Chaos |
| P-17, subject loop | Release, tribute, annex and release again | Actual transfers only, no duplicate subject milestone |
| P-18, final islands | Global campaign with distant supplied non-Cookie islands | No false terminal victory and no teleportation |
| P-19, multiplayer input | Owner, spectator, reconnect, two clients and rapid clicks | One authoritative count and one reward per entitlement |
| P-20, DLC matrix | No DLC and each relevant capability removed separately | A coherent playable baseline, explicit unsupported optional adapters |
| P-21, manual contained | Zero prior progression with contained preset | Immediate uprising using preset strength, no ordinary prerequisites |
| P-22, manual world-end | Zero Chaos and no pet history, explicit final preset | Immediate active global campaign without fabricated historical progress |
| P-23, disconnected owner | Both configured continuity policies | No secret clicking, no reward reset, correct warning time and eligibility |
| P-24, simultaneous threats | Cookie threat plus a different active world threat | Cookie cleanup leaves the other source active |

For each scenario, record inputs, exact source revision, tool output, unresolved assumptions and the actual result.
Expected outcomes in this table are acceptance criteria.
They are not evidence that a game test has passed.

## Tuning priorities

Tune reward and appetite growth together using campaign trajectories.
A player completing every cycle, a player repeatedly stopping at 75 percent and a player starving immediately should have distinct understandable outcomes.
The strongest daily rewards should remain tempting, but reaching high Level must also make the potential enemy noticeably stronger.

Review the low-industry and high-industry tails separately.
Do not balance only against a 1936 major.
Check a minor, an island, a damaged country, an occupied country, a late major and an active world-end campaign.
Keep economy-scaled costs and force-strength targets readable.
