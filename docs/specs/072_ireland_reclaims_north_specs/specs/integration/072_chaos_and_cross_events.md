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
| 006 Independence Wave | A Celtic government may already exist or become independent during the Irish campaign | Reuse it, retain its content, and require its consent. Do not release or duplicate it again. |
| 009 White Peace | An automatic peace could interrupt the defined northern attempt | Use narrowly owned protection on the reclamation actor/context where supported. The inspected generic event excludes factions and is not a proof of the required British settlement. |
| 060 Research Failure | Irish or partner technology can regress during military development | Re-evaluate template and training feasibility. Do not restore all lost technology as an incidental focus bypass. |
| 061 Industrial conversion | Military and civilian capacity can change during paid projects | Pause or revise future capacity commitments without duplicating buildings or inventing negative available factories. |
| 062 Allies Backstab | A Celtic or Atlantic alignment can be affected by the broader faction system | Respect the actual faction change and invalidate affected charters or offers. Do not grant permanent blanket immunity. |
| 063 End Subject Status | A client or dominion may become independent | Update sovereignty and accepted obligations. It does not automatically become an Irish-owned state or remain a loyal subject through stale flags. |
| 064 Border fortifications | The northern front may have unusually strong forts | Include the case in force and AI testing. Do not delete the forts or auto-win because the ordinary opening is harder. |
| 071 Persia and 073 Mongols | Other formables and territorial projects can change current holders | Read actual country identity and ownership, with no global exclusion merely because another formable exists. |
| Shared scenarios and global crisis systems | Government survival, territory, supply, and ordinary population systems may change | Update only the affected event-owned work. Do not override the shared scenario lifecycle to preserve an Irish mission. |

These interactions are contracts against the supplied catalog and mechanics, not claims that every listed rework is already implemented.
Current catalog statuses are retained in the research ledger.
The event does not add chemical, biological, or supernatural military content solely because those systems exist in Chaos Redux.
Their ordinary global effects continue through the shared systems.
