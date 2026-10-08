# Chaos impact and cross-event relationships

## Shared accounting

The supplied mechanics guide assigns shared Chaos to war, peace, annexation, puppet creation, liberation, country freedom, faction membership, ideology changes, military growth, deaths, pollution, nuclear use, and world-tension increases.
Event 072 must use those established paths and must not add the same consequence again under an event-specific label.
The displayed guide values are reference behavior, not permission to hardcode a second copy of the shared constants.

| Shared consequence | Supplied guide value | Event 072 treatment |
| --- | --- | --- |
| War begins | +1 or +5 for a major change | Ordinary reclamation and later wars use the shared source |
| Peace | -1 or -3 for a major change | Successful or failed limited settlement uses the shared source once |
| Annexation | +2 or +10 for a major change | Apply shared ownership/annexation policy where applicable, not an assumed annexation for every state transfer |
| Puppet creation | +1 or +3 for a major change | Use the real accepted subject relationship, if any |
| Liberation | -2 or -5 for democratic liberation | Shared source for actual released Celtic states |
| Country freed | -3 | Shared source for actual freedom, not a renamed client |
| Faction join | +1 or +3 for a major change | League and federation membership use existing membership handling |
| Faction leave | -1 or -3 for a major change | Real departures use the shared source |
| Monthly natural decline | -1 | No additional Irish monthly decline |
| World-tension increase | +1 per percentage point | Do not duplicate with a matching custom Irish increase |
| Military buildup | +1 per 100 military factories or 100 divisions | Opening force and later growth remain part of shared ordinary-country accounting |
| Deaths | +1 per million recorded deaths | No extra casualty Chaos from the same soldiers |

Ireland and the Celtic partner states are normal human countries.
Their ordinary growth is not routed through a special nonhuman-country power system.
The initial war and force are the event's meaningful manifestation, and the existing shared war and buildup sources already cover their destabilizing effect.
This is the reason for zero additional activation Chaos.

## Event-owned sources

| Source | Concrete consequence | Proposed amount | Guard and reversal |
| --- | --- | ---: | --- |
| CX01 | Ireland explicitly breaks a signed Scottish independence or regional self-government guarantee while imposing a different sovereign settlement | +5 | Once per affected Scottish settlement provenance, maximum one campaign charge. Not charged for merely selecting an imperial focus. |
| CX02 | A federal government attempts coercive enforcement that actually suspends agreed common institutions and causes a member's documented withdrawal or charter rupture | +3 | Once per affected member and concrete dispute, maximum two charges and +6 in the campaign. Ordinary faction-leave Chaos remains separate. |
| CR01 | A completed constitutional repair restores the specific guarantee broken under CX01 and ends its actual political consequence | -2 | Only after the corresponding paid +5 source, once. No reduction for a fresh unrelated treaty. |
| CR02 | Accepted arbitration repairs a CX02 institution rupture and the relevant member restores the charter | -2 | Only against that recorded rupture, once per charged member. Maximum total reversal cannot exceed that source's previous positive charge. |

CX01 represents the additional political breach, not the ordinary war, annexation, or ideology effect.
CX02 represents a collapsed common institution following coercion, not merely a faction departure.
If implementation reveals that another shared system already charges these exact non-war consequences, remove the duplicate custom source and record the overlap resolution.
Do not preserve both solely to match a target Chaos total.

Settlement increases, Strain threshold checks, map changes in the GUI, Evolution eligibility, Evolution activation, tree loading, formation labels, news, super-events, logging, and achievement awards add zero custom Chaos.
A formation that produces a real shared diplomatic change still receives that shared source through its normal handler.
Do not create Chaos just for reaching a branch or clicking a declaration button.

## Anti-farming

Record the original positive source, affected counterpart, event provenance, and whether a reversal has been paid.
Repeatedly breaking and restoring the same promise cannot generate new charges and reductions indefinitely.
Save reload, country cosmetic changes, federation demotion, and reconstitution do not reset these guards.
A reversal cannot be claimed when its original consequence was never charged or was prevented by a rejected action.
No custom periodic Chaos loop is added.

## Event relationships

| Existing event or system | Meaningful relationship | Required boundary |
| --- | --- | --- |
| 006 Independence Wave | An existing or newly released Scottish, Welsh or Breton government can answer the corresponding Irish offer | Reuse its live identity and origin. Existing forces and content replace any proposed new-release grant, while Irish aid remains paid and its charter requires fresh acceptance. |
| 009 White Peace | An automatic peace could interrupt the defined northern attempt | Use narrowly owned protection on the reclamation actor/context where supported. The inspected generic event excludes factions and is not a proof of the required British settlement. |
| 060 Research Failure | Irish or partner technology can regress during military development | Re-evaluate template and training feasibility. Do not restore all lost technology as an incidental focus bypass. |
| 061 Industrial conversion | Military and civilian capacity can change during paid projects | Pause or revise future capacity commitments without duplicating buildings or inventing negative available factories. |
| 062 Allies Backstab | A real faction rupture can separate Celtic partners or end a military route used by an Atlantic agreement | Suspend only clauses and offers that depend on the lost membership, access or safe war side. Other accepted obligations keep their own terms, and no partner receives blanket immunity. |
| 063 Subjects Break Free | A Scottish, Welsh or Breton subject can become a sovereign counterpart in place | End subject-only authority and aid conditions. Reassess the existing bilateral or federal offer against its new sovereignty, with consent and no second release, army or formation reward. |
| 064 Border fortifications | The northern front may have unusually strong forts | Include the case in force and AI testing. Do not delete the forts or auto-win because the ordinary opening is harder. |
| Shared scenarios and global crisis systems | Government survival, territory, supply, and ordinary population systems may change | Update only the affected event-owned work. Do not override the shared scenario lifecycle to preserve an Irish mission. |

The [Event 063 settlement owner](../../../063_subjects_break_free_specs/specs/063_subjects_break_free_spec_part_2_settlements.md) decides recognition, contested independence and any safe restoration war.
Ireland cannot undo that result through a pending union or dominion acceptance, and gaining sovereignty alone does not accept a Celtic federal charter.
The same government may keep a voluntary procurement or port agreement whose terms remain valid.
The 90-day federal constitutional proof counts only after its own required sovereign members, homelands and accepted charters are valid together.
An Event 063 release or an [Event 062 faction rupture](../../../062_allies_backstab_specs/specs/062_allies_backstab_spec_part_6_outcomes_connections.md) is not itself an Irish guarantee breach under CX01 or an Irish coercive rupture under CX02.
Those consequences require the Irish conduct defined above.
AI Ireland reassesses whether it can still provide the offered protection, and the independent partner evaluates the revised offer under its normal sovereignty and capacity rules.
Ordinary Celtic diplomacy remains complete when those events are absent.

These interactions are contracts against the supplied catalog and mechanics, not claims that every listed rework is already implemented.
The reviewed catalog snapshot statuses are retained in the research ledger.
Inspect the authoritative workbook before asserting current status.
The event does not add chemical, biological, or supernatural military content solely because those systems exist in Chaos Redux.
Their ordinary global effects continue through the shared systems.
