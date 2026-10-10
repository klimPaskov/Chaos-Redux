# Event 079: The Master

## Catalog identity

| Field | Required value |
| --- | --- |
| Event ID | 79 |
| Event name | The Master |
| Type | Minor Repeatable |
| Catalog status | To Be Reworked |
| Chaos level | 1 |
| Cluster | Diplomacy |
| Member severity | Medium |
| Root event | `chaosx.nr79.1` |

## The contest

An independent AI-controlled minor becomes the subject of a public competition for foreign control. Each major power and each player-controlled country receives its own Influence score in that country. Diplomats, investors, military missions, government supporters, and opposition sponsors compete to make their country indispensable. The first participant to reach **100 Influence** becomes the target's actual overlord immediately.

The player sees the country being contested, its political alignment, their own Influence, and the strongest rival. The important choice is how to build a position that survives interference. Supporting an already friendly government produces influence efficiently. Supporting an opposition party can be slower initially but can improve later campaign efficiency. Investment leaves useful infrastructure or industry behind, including when another sponsor wins. Military aid can bring the army closer to a sponsor without automatically changing the civilian government.

Country size is not a score multiplier. Majors can afford more sustained commitments, but cannot buy unlimited actions at once. A player minor can concentrate political power and a modest military or economic commitment in one target while majors divide their attention. Countries sharing an ideology still have separate scores, separate costs, and separate claims to victory.

## Campaign rhythm

The opening provides a breakdown of each country's initial position. Starting Influence is capped at 45, so nobody wins merely because of existing relations. A participant can undertake one political campaign and one material campaign in the same target, subject to a limit of three active campaigns across all targets. An interference operation uses the political slot. The player therefore has to give up a positive political action to attack a rival.

Most campaigns take several weeks. Effects occur when the action or a stated delivery milestone completes. They do not depend on answering a report popup. Completed actions can change real party popularity, provide actual equipment, deliver a building, improve target military training, or change an eligible government appointment. Influence remains the only new headline measure.

A lead is vulnerable but cannot be erased by an unlimited pile of simultaneous attacks. Rival losses have a visible rolling limit. Repeating the same positive action family has diminishing returns. A varied campaign is usually stronger than repeatedly paying for the same speech or funding the same minister.

## Evolution

At Chaos 200+, Influence Campaigns permits stronger operations, support for domestic institutions, and direct attempts to alter the government. At Chaos 400+, The Great Game permits up to five independent target races at the same time and adds stronger attempts to realign governments and obstruct a leading sponsor. Every ordinary firing still selects one new target.

The global evolution record controls which campaign tools are available. Existing races can evolve after the project's maturity checks. An eligible high-Chaos opening can begin at an evolved stage. Crossing a Chaos threshold alone does not instantly upgrade an active contest.

## End state

Victory establishes a real puppet relationship. A faction invitation, guarantee, military access agreement, or opinion modifier is not a substitute. The target keeps its territory, national content, armed forces, and completed investments. Normal subject mechanics govern its later development. The winner does not receive free annexation, a copied army, or a permanent Event 79 exemption from independence mechanics.

The ending announces the winner and the political means that mattered most. Losing participants retain their own countries and resources that were never spent. Delivered weapons and completed works remain with the target. Open financial and industrial commitments are reconciled using their actual delivery history.

## Reading the specification

Read Parts 01 through 08 for the full game rules. Part 09 contains worked campaign examples. The specialist folders define AI, interface, assets, achievements, integration, writing direction, and research. Implementation contracts, source coverage, unverified engine requirements, test cases, and ready handoff prompts live in the [implementation working records](../../plans/079_the_master_plans/).

The five action-family names and two evolution names supplied in the user brief are preserved. Other action, incident, achievement, and interface names in these documents are **working labels, not final localisation**. Numeric values introduced here are initial design tuning. They are not claimed to be playtested or separately approved by the user.

## Revision log

### 2026-10-10 spec audit

Basis: 10 Oct 2026 spec audit under the user's planning-package brief.

- Influence is a whole number: gains round down once at completion, replacing quarter-point precision and fractional displays (Parts 02 and 09).
- Removed fairy-dust opinion bonuses from propaganda and incumbent support; the opposition opinion penalty is kept and explained as the real cost of that route (Part 03).
- Cut three incidents whose alternatives were empty or cosmetic (funding disclosure, officer objection, budget review), leaving three reactions with genuine choices (Part 06).
- Added a famine connection: Public works can become a relief shipment delivered through the famine owner when a target state is starving (Parts 04 and 16).
- Shortened the blocking-coalition timing rules, consolidated discount and Chaos rules into their Part 15 homes, and replaced tool and workflow narration in Parts 10 to 12 with outcome requirements and skill links.
