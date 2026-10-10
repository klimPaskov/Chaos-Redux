# Decisions, missions, costs, and visibility

Follow [the decisions and missions skill](../../../.claude/skills/chaos-redux-decisions-missions/SKILL.md) for structure, tooltips, and audits.

## Presentation

Event 036 uses one ordinary decision category with a static category picture and a compact status header.
A scripted GUI is out of scope, because the three header values and a short decision list carry every choice.

## Status header

| Line | Shows |
| --- | --- |
| National Posture | The posture and the permission line (retaliation only, chemical first use, chemical and biological first use, or unrestricted use) |
| Convention Standing | Provisional, Divided, Established, or Dominant |
| Current Agenda | The agenda name, ratifications against the quorum, and the deadline, or the active project's name, stage, percentage, and whether the country has contributed |

Each line has one tooltip that names what changes it and the next deadline that matters to the country.

Never shown: multipliers, weights, internal progress units, contribution shares, candidate lists, sponsor scores, or other countries' covert programs.

## Visibility budget

At most five primary decisions are visible at once, and at most three Event 036 missions run at once.
A decision disappears as soon as its posture, agenda, treaty, project, or target becomes invalid.

Actions that already exist elsewhere are not duplicated here:

| Need | Existing action |
| --- | --- |
| Publish evidence of an attack | `cbrn_share_forensic_evidence` |
| Demand an inspection | `cbrn_demand_inspections`, with Protocol ratification as an extra eligibility basis |
| Send decontamination aid | `cbrn_sponsor_decontamination_mission`, with Compact ratification as valid access |
| Set the national use policy | `cbrn_choose_retaliation_only`, `cbrn_choose_battlefield_authorization`, `cbrn_choose_unrestricted_authorization` |

## Posture actions

Shown when no agenda response or contribution needs attention.

| Decision | Who sees it | Cost | Effect |
| --- | --- | --- | --- |
| Seek Accession | Public Rejection countries 180 days after their last change | Political power scaled by Standing | Starts Accession Review |
| Revise Posture | Members past the 365-day lock | Political power and a temporary stability penalty | Opens a follow-up event listing only the allowed revisions |
| Begin Withdrawal | Members without an open Assistance Guarantee | Political power | Starts Withdrawal Notice |
| Begin Covert Program | Public Rejection countries with a chemical or biological research route and no program | Political power and one civilian factory for 180 days | Starts the program and its hidden evidence |
| Expand Covert Program | Countries running a program | Civilian factory time | Raises AI research and production priority for the chosen family and adds hidden evidence |
| End Covert Program | Countries running an unexposed program | None | Closes the program |

## Conference actions

Shown while an agenda is in negotiation, filtered to the agenda.

| Decision | Who sees it | Cost | Effect |
| --- | --- | --- | --- |
| Sponsor the Current Agenda | Eligible members while sponsorship is open | Political power and one civilian factory for 60 days | Becomes sponsor ([04](04_recurring_conventions_and_treaty_families.md#sponsor)) |
| Lobby for Ratification | Members who can ratify | Political power | Raises AI ratification weight among eligible members for the rest of negotiation |
| Organize Opposition | Opponents and members who will decline | Political power and opinion with the sponsor | Lowers AI ratification weight, doubled for the Opposition Leader |

Each country can use each conference action once per agenda.

## Treaty obligations

Shown only to ratifiers with an open obligation, as missions rather than decisions:

- Declaration Deadline, for the Chemical Production Articles and the Biological Laboratory Registry
- Assistance Guarantee, for the Protection and Assistance Compact
- Doctrine Integration, for the Strategic WMD Doctrine Charter

## Project contributions

While a project is active, the conference actions are replaced by the four contribution decisions in [08](08_international_chaos_weapons_program.md#contributions).
They are hidden while the program is Paused, Dormant, completing, or cancelled, and while the country is in cooldown.

## Mission catalog

| Mission | Duration | Success | Failure |
| --- | ---: | --- | --- |
| Accession Review | 90 days | Choose a member posture | Stay in Public Rejection with a 180-day retry lock |
| Withdrawal Notice | 90 days | Leave the convention | Cancelled if the country becomes invalid |
| Declaration Deadline | 120 days | Keep treaty benefits | Suspension |
| Assistance Guarantee | 60 to 120 days by distance | Trust kept and the guarantee fulfilled | Suspension |
| Doctrine Integration | 150 days | Integrated doctrine | Prior state kept, 180-day retry lock |
| Project Contribution | 90 or 120 days | Receipt applied once | No progress and no refund |

Mission durations within a band are script constants.

## Cost rules

No action uses more than four cost types.
Political power fits public diplomacy, civilian factories fit industrial and facility work, equipment fits protection and specialist contributions, manpower fits facility security, and command power stays on the existing CBRN operations.
Costs scale with economy size and Standing where the formula is visible in the tooltip, and stay flat otherwise.

Blocked tooltips name the exact missing requirement through `custom_trigger_tooltip`, never a raw flag.

## Targets

Country-targeted actions reuse the existing CBRN target selection.
Event 036 adds no target list of its own.

## Exploit controls

The implementation must prevent:

- posture changes timed around a single attack, through the 365-day lock and day-of-action relief
- repeated opening normalization
- duplicate contribution receipts or progress after cancellation
- grants for non-contributors or repeated grants for one project
- sponsorship stacking, through the 365-day sponsorship cooldown
- withdrawal during an open Assistance Guarantee
- repeated treaty Chaos through repeal and re-ratification

## AI equivalence

Every decision has an AI path with hard validity gates that no positive factor overrides, as [10](10_ai_behavior_and_probability_contract.md) defines.
