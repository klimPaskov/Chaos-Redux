# Event 059 acceptance matrix

## Status language

Each row must end as `pass`, `blocked`, `needs_user_review`, or `not_applicable`. A source-only assumption is not a pass for engine behavior.

| Area | Acceptance requirement | Required evidence |
| --- | --- | --- |
| Event identity | Stable entry remains Event 59 and is registered as Minor Fire-Once at Chaos level 1 | Event inspection, registration check, catalog alignment |
| Fire-Once behavior | Event can fire once, then leaves ordinary and cluster selection | Weight and fired-state inspection, forced duplicate test |
| Global activation | One permanent global active state is created | Source inspection, save and reload test |
| Player reports | Every human player receives one activation report | Multiplayer or controlled fan-out test, history de-duplication check |
| Human exemption | Current human-controlled countries receive no Event 059 AI behavior or direct modifier | Player takeover test, modifier inspection |
| AI handback | Returning a country to AI restores every active layer after reassessment | Control transition test |
| New countries | AI countries created after firing receive current layers | Release or civil-war test |
| No global scan | No new unbounded daily, weekly, or monthly whole-world loop is used | Source review, on-action inventory, performance review |
| Direct bonuses | Event grants no attack, breakthrough, organisation, planning, supply, production, research, or equipment-stat bonus | Idea, modifier, event-effect, and scripted-effect search |
| Baseline fronts | Supplied favorable fronts become more active and concentrated | AI scenarios 01, 02, 08, 09 |
| Baseline restraint | Critical supply, equipment, manpower, and fuel failures suppress attacks | AI scenarios 04, 05, 06, 07 |
| Concentration | Main fronts gain priority without emptying capital, ports, or critical secondary fronts | Front observation and unit distribution evidence |
| Production adaptation | Offensive-enabling production rises only within country capacity and replacement floors | Minor and major production scenarios, stockpile trend evidence |
| Air support | Aircraft move toward useful active fronts when range, fuel, and airfields permit | Air assignment test |
| Naval invasion | Viable invasions become more likely and unsupported invasions remain blocked | AI scenarios 11, 12, 13 |
| Existing objectives | Existing war goals and useful calls gain timely action at baseline | AI scenarios 17, 23 |
| Baseline war boundary | Baseline does not create arbitrary new wars | AI scenarios 19, 29 |
| Evolution I timing | Active-event Evolution I follows enabled state, 200+ gate, and dynamic MTTH | Timed test at several Chaos values |
| Evolution I behavior | Persistence, reinforcement, follow-up, and recovery change without adding predatory war logic | AI scenarios 01, 08, 10, 40 |
| Evolution II timing | Active-event Evolution II follows enabled state, 400+ gate, and dynamic MTTH | Timed test at several Chaos values |
| Evolution II behavior | Claims, war goals, intervention, and valid weak-target opportunities gain weight | AI scenarios 18, 20, 21, 23 |
| Evolution II legal limit | Weak unrelated targets and forbidden subject actions remain invalid | AI scenarios 19, 26, 41 |
| Evolution III timing | Active-event Evolution III follows enabled state, 600+ gate, and dynamic MTTH | Timed test at several Chaos values |
| Evolution III behavior | Scale, theater count, invasion ambition, and accepted risk rise | AI scenarios 02, 03, 11, 21, 22 |
| Evolution III safety | Critical supply, fuel, manpower, reserve, and legal-path vetoes remain | AI scenarios 04, 06, 07, 12, 19 |
| Evolution independence | Disabling one stage removes only its own future channel | AI scenarios 40, 41, 42, 44 |
| Pre-fire opening | First firing above thresholds activates each enabled eligible layer with one popup and ordered logs | AI scenarios 43 and 44 |
| Evolution Chaos | Evolution eligibility, activation, and logging add zero Chaos | Before and after Chaos evidence |
| Initial Chaos | Activation adds one bounded 15 to 25 gain and never repeats | Low and high coverage tests, reload and cluster tests |
| Shared-source overlap | Wars, deaths, annexations, faction changes, and tension receive no Event 059 duplicate | Chaos history comparison |
| Cluster assignment | Event appears in Diplomacy with High severity, and Diplomatic Panic is not retained as a separate alias cluster | Cluster catalog, membership export, and UI evidence |
| Cluster metadata | Required or optional role, participation chance when relevant, and minimum tier match the authoritative Diplomacy defaults | Registry inspection, probability audit for any weighted value, and manual cluster tests |
| Cluster pacing | A cluster containing Event 059 counts as one global pacing event | Timer and major-gain evidence |
| Special actors | Owner-specific hard strategy remains dominant | AI scenario 28 and special actor tests |
| Subjects | Subjects fight more actively only inside legal participation | AI scenarios 25 and 26 |
| Peace interaction | White Peace and scripted settlements work and are not instantly undone | Peace test with later time advance |
| Save migration | Legacy fired state maps once without duplicate report, history, weight, or Chaos | Migration fixture or controlled old-save test |
| DLC compatibility | Baseline remains functional without optional DLC and unsupported channels skip safely | No-DLC or DLC-disabled validation |
| Event Logs | Events, History, Evolutions, Event Details, and Clusters show complete and aligned information | UI inspection and screenshots |
| Actor mapping | Global event and evolutions do not show a misleading country flag | History and evolution detail screenshots |
| Localisation | No raw keys, hidden formulas, final working labels, em dashes, semicolons, or claims of direct bonuses | Localisation audit |
| Report art | Final 210 by 176 report image is period-correct, readable, processed, converted, wired, and documented | Asset manifest, PNG, DDS, in-game screenshot |
| Achievement logic | Qualifying defensive challenge is difficult, tracked, guarded, and not automatically unlocked | Unit tests or scripted checks, live achievement test |
| Achievement art | Completed achievement icon family is readable and wired | Asset manifest and UI screenshot |
| Probability audit | Complete pools, scenarios, sweeps, comparisons, and renders are reviewed | Auditor handoff and tool evidence |
| AI outcome quality | No plan dominates every scenario and no essential recovery or defense plan starves | Probability report and bounded time pass |
| Performance | No event-owned log spam, repeated reapplication, or material time-step regression | Fresh logs, profiler or bounded comparative observation |
| Documentation | Event docs, authoritative workbook, CSV exports, AI notes, asset records, and achievement docs agree | Diff and export validation |
| Final audit | Event completion auditor maps every spec requirement to implementation evidence | Completion table with unresolved blockers |

## Achievement acceptance

The planned achievement passes only when all of these are true:

- qualification starts while Total Offensive is active
- the player is an independent non-major at qualification
- the player is defending against an AI major that began the qualifying war as an attacker
- the enemy major is materially stronger at qualification and is not already close to capitulation
- no major ally protects the player's side during the qualifying period
- the player remains uncapitulated and independent for at least 180 continuous days
- the qualifying AI major is capitulated or removed in defeat while the player still controls its capital and at least 75 percent of the core states held at qualification
- late joining, subject protection, human takeover of the target, and duplicate qualification cannot unlock it

The implementation can refine auditable strength thresholds after inspecting available scripted values, but it cannot reduce the achievement to participation or survival alone.

## Live observation minimum

A full completion claim needs more than parser success. At minimum, live observation should cover:

1. one strong major attacking a weaker supplied opponent
2. one weak minor with limited industry
3. one severe supply or fuel failure
4. one viable and one inviable naval invasion
5. one Evolution II opportunity target and one unrelated weak target
6. one high-risk Evolution III peer front
7. one player takeover and AI handback
8. one country created after activation
9. one pre-fire evolved opening
10. one Diplomacy cluster firing
11. save and reload
12. the Event Logs and achievement surfaces
