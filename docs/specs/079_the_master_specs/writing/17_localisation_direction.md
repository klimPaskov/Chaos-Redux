# 17. Writing and localisation direction

## General approach

Finished localisation is written during implementation. This document defines viewpoint, content, dynamic fields, and tone. Except for the event name and action/evolution names already supplied by the user, the labels here are working labels, not final localisation.

Use clear diplomatic language with a restrained satirical edge in selected options. The humor should arise from a sponsor's claim to be helping while seeking control. Avoid generic declarations about maps changing, history being rewritten, grand chessboards, destiny, puppet strings, or an omniscient narrator announcing that a threat exists.

The target remains a political society with a government, army, institutions, and economic needs. Text should not treat it as empty land. Neither the name The Master nor the puppet outcome requires dehumanizing the target population.

## Text surfaces

| Surface | Viewpoint and required facts | Tone and variation | Required dynamic inputs |
| --- | --- | --- | --- |
| Opening report | Sponsor learns that a specific minor has become a contest target | Practical opportunity mixed with concern over rivals | Target name, ruling group, sponsor seed, strongest rival, strongest initial advantage |
| Propaganda action | Sponsor directs a public campaign toward a specific ideology | Confident official explanation. Avoid fabricated slogans | Target, pledged ideology, duration, popularity change, estimated Influence |
| Investment action | Sponsor funds a named output in a named state | Concrete economic commitment, including what donor industry gives up | State, output, reserved factories, funded days, actual quote |
| Military aid action | Sponsor sends real material or advisers | Material assistance and political intent are both explicit | Equipment components, recipient, delivery time, training output |
| Government support | Sponsor backs the actual incumbent or supplied institution | Explain why that recipient is friendly and what can invalidate support | Incumbent group or valid bloc, opinion condition, costs |
| Opposition support | Sponsor builds a different political movement | Explain intended domestic change without inventing a historical party | Pledged group, current popularity, projected change, diplomatic exposure |
| Interference | Sponsor tries to reduce one rival's position in one country | Specific operation and its limited effect, not generic sabotage | Target, selected rival, anchor, remaining loss budget, refund rule |
| Leadership operation | A real domestic transition is attempted | Match parliamentary, executive, royal, or military context | Existing recipient, institution, political threshold, stability cost |
| Evolution record | Contest methods or geographic breadth changes | Describe newly available practices without claiming an immediate conquest | Actual stage, affected races, newly available tools |
| Winner report | Sponsor establishes an actual puppet relationship | State the concrete outcome, with route-specific political detail | Winner, target, final alignment, largest real contributions |
| Target report | Target government faces its new dependence | Domestic consequence and continuity of administration | New overlord, government state, retained investments |
| Rival report | Sponsor lost the race after its own commitments | Explain the result and remaining material consequences | Winner, target, final score, sunk deliveries, refunds |
| International news | Observers learn which country has become a subject | Diplomatic significance and method, not a generic world-map summary | Target, winner, stage, political/economic/military route |
| Achievement text | Player understands a specific demanding result | Accurate condition description without unexplained hidden clauses | Fixed achievement requirements and needed shared eligibility terms |

## Naming and country context

Use the game's current localized country names and actual political labels. A country changing its cosmetic name must be reflected in current UI without rewriting the archived factual identity of an earlier race. Do not hardcode a parliamentary label into a one-party committee or a royal council.

For leadership reports, use existing character localization only when that character is actually selected. If the operation is an institutional alignment without a named appointment, describe the institution. Never generate a plausible-sounding historical minister's name.

## Tooltips and errors

The opening score tooltip lists capped evidence families and the final cap. Positive-action tooltips explain compatibility and repeated-family returns. Payment tooltips distinguish cost discounts from physical shipments. Invalidation tooltips name the reason the action is unavailable instead of presenting a broken button.

Raw IDs, variable names, source-audit commentary, coding instructions, test labels, and placeholder research notes must not appear in the live UI. A blocked engine feature is a developer release gate, not a humorous in-game error message.

## Research-dependent wording

Historical quotations, real slogans, speeches, newspaper headlines, and literary allusions require verified sources and exact attribution. This package approves no invented quotation. Most Event 79 text can be original country-neutral diplomatic writing and does not need a famous line.

If later writers use a source-dependent cultural reference, record the original source, date, language, translation basis, and the exact small fragment being reused before adding it to localisation.
