# Event 81 achievement implementation and asset prompt

Read the full Event 81 source specification, especially Part 9, and the current achievement registry and existing implementation patterns. Use the relevant event, asset, localisation, and auditing skills. Every proposed name is a working label, not final localisation.

Implement all eight achievements exactly from Part 9. The source part contains each proposed ID, eligible country, route, outcome conditions, disqualifiers, difficulty, visibility, historical tracking requirements, and completed icon direction. Do not replace those conditions with a generic event-fired or current-stage check.

## Registry and route map

| Proposed ID | Route to prove | Distinct tracking |
|---|---|---|
| `chaosx_081_revenue_order` | ENG sustains the mature Evolution II network for an additional 180 days | Actual 360-day maturity, breadth, relief, successor identities |
| `chaosx_081_minor_settlement` | A qualifying small independent human country completes the full peaceful chain | Original economy and status, twelve projects, four consolidations, final Evolution II transition |
| `chaosx_081_former_subject_settlement` | An initially British-dependent country becomes independent and finishes peaceful reform | Initial dependency, genuine independence, at least one complete evolved stage |
| `chaosx_081_enforcement_defeated` | A human major's refusal leads to a defeated British enforcement war and worldwide abolition | Refusal identity, correct special entitlement, linked war, victorious settlement actor |
| `chaosx_081_allied_exit` | A British-led ally experiences the Nominal ceiling, then completes lawful final reform | Initial faction relationship, 180-day ceiling interval, valid later relationship change |
| `chaosx_081_external_recovery` | Remove real expanded external claims before peaceful independence | Actual prior British trade and two distinct collected expanded claims |
| `chaosx_081_partner_settlements` | Two sovereign countries complete an assistance project and both reach evolved peaceful independence | Both identities, paid assistance, both final transitions under Evolution II |
| `chaosx_081_network_recovery` | ENG rebuilds a severely damaged Evolution II collection network | Initial breadth and real receipts, genuine exit-driven loss, legitimate 180-day recovery |

Inspect `common/achievements/chaos_redux_achievements.txt` and all shared ID sources for collisions. Keep all tracking event-owned and avoid an additional global heartbeat for achievement checks. Subscribe to the same substantive outcomes and country review schedule that already maintain the mechanic.

Track eligibility when the source says it begins. The current major flag cannot reconstruct whether a country was a small minor several years earlier. The current puppet flag cannot prove it was an initial British dependent. A current Tax Independence stage cannot prove that twelve projects were completed peacefully.

## Required disqualifier tests

Cover console-only activation, repeat event delivery, multiple humans, save reload, tag restoration, merged or split successors, puppet-release loops, faction-entry tricks, a project finishing after a relationship lock appears, zero recorded levies, and a super-event triggered without real economic maturity.

Do not award a bilateral-war achievement to every allied country when one country negotiates a settlement. Do not infer a qualifying enforcement war from any conflict with Britain. Do not retax previously peaceful exemptions to make Britain's recovery achievement easier.

## Art and localisation

Coordinate with the asset prompt for eight original completed subjects and the required three-state achievement pipeline. Use the current immutable templates and `process_achievement_icons.py`. Final output belongs directly in `gfx/achievements/` with the proposed ID or the final collision-free equivalent and the `_grey` and `_not_eligible` suffixes.

Write final titles and descriptions from the directions after checking any cultural references. The source labels are not finished achievement names. Ensure description text accurately discloses all meaningful requirements without suggesting an easy trigger that the code does not use.

## Acceptance

For each achievement, provide its final ID, trigger ownership, initial eligibility record, success path, disqualifier coverage, asset consumers, localisation keys, and validation evidence. State which mandatory tools were actually run. Missing icon variants, incomplete history tracking, registry conflicts, and untested successor logic are blockers. Do not report complete coverage from a single current-state screenshot.
