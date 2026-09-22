# Event 074: Japan Lands in USA

## A Japanese army on the American mainland

Japan suddenly controls a usable Pacific landing zone and has a substantial, supplied army inside the continental United States.
The landing has already happened when the American warning appears.
The opening creates a front that Japan can expand through normal combat and that the United States must actively contain.
A Japanese defeat at sea, an exhausted national stockpile, or a collapsing position in Asia does not prevent this opening.

The campaign turns on three connected tasks: defend the unloading ports, join the coastal positions, and move through western transport corridors before the opponent can concentrate.
Japan receives enough prepared force to attempt those tasks immediately.
Its exceptional support is finite, so preserving transport access and capturing additional working infrastructure matter after the first fighting.
The United States can mobilize local formations and prepare a counterattack, but it must pay real costs and choose where to concentrate.

## Catalog identity

| Field | Design |
| --- | --- |
| ID | `074` in filenames and documentation, numeric `74` in registries |
| Canonical event name | Japan Lands in USA |
| Type | Minor Fire-Once |
| Catalog status | To Be Reworked until an implementation review supports a change |
| Chaos level | 1 |
| Cluster | Wars |
| Cluster role | Medium member |
| Existing root to preserve | `chaosx.nr74.1` |
| Main actors | Existing Japan and United States country identities |

The user's current brief supplies this identity and supersedes the sparse catalog export for this event.
The large military effect does not change its Minor classification or its cluster severity.

## The first playable moment

The world map shows Japanese control over the selected coastal footprint, Japanese divisions stand in legal deployment positions, usable unloading capacity exists, and both countries receive the appropriate notice.
The Japanese player can issue orders without waiting for a second event, a purchase, a declaration of war, a naval supremacy check, or a mission reward.
The American player sees the actual landing region and can open the emergency decision category immediately.

The first report has no acceptance option that cancels the landing, grants the army a second time, or delays the American warning until Japan acknowledges its own message.
Material effects belong to the committed landing.
Any acknowledgement only closes the report.

A normal-strength baseline opening contains 30 divisions, with a mixture of line infantry, stronger assault infantry, and a smaller mobile component.
Evolution III opens with 150 divisions before the bounded late-campaign adjustment.
These are proposed tuning anchors, not tested balance results.
Part 3 defines the entire force and reserve budget.

## Availability

The only political and strategic requirements are that Japan exists, the United States exists, and the two are at war with each other.
Do not add requirements for Japanese strength, naval supremacy, ship count, a particular ideology, a historical date, a living named leader, American weakness, or control of Pacific islands.
Existing event settings and the already-consumed fire-once state continue to apply as shared framework rules.

A placement preflight is still necessary because a real map location must exist.
For example, a separate neutral country might own every eligible Pacific mainland state.
That situation must leave the event unconsumed and eligible for a later placement attempt.
It must never annex the neutral country, begin another war, report a landing that did not happen, or replace the missing coast with Hawaii, Alaska, Mexico, Canada, or an inland state.
This is an explicit map-feasibility limit, not an additional requirement that Japan be winning.

The same rule applies when the engine cannot safely place the promised force around existing defenders.
A failed preflight does not become a hidden failure roll after the event is counted as fired.
The implementation must prove its defended-coast behavior before release.

## One landing episode

Event 074 commits once for the campaign.
Its initial landing bundle can contain several simultaneous entry points at higher tiers.
Those points are all part of the same landing episode.
Later reinforcement deliveries and active evolutions enlarge this episode through retained Japanese access.
They do not repeat the original surprise landing or seize new enemy ports by script.

The episode remembers its landing date, selected tier, actual occupied footprint, issued force and material totals, original port targets, and whether special support has ended.
That record survives save reloads and country-player changes.
The absence of a current national spirit or decision category cannot make the event available again.

## What remains normal

Japan keeps its government, ideology, existing focus tree, armed forces, territorial claims, diplomacy, and obligations in other wars.
The United States keeps the same systems.
The event grants wartime control over the landing footprint, not permanent Japanese ownership or cores.
Ordinary occupation, resistance, combat, capitulation, peace conferences, and territorial settlements decide what follows.

There is no separate peace objective, forced American surrender, automatic white peace, protected expeditionary state, or agreement that saves Japan from its other enemies.
A surviving Japanese country may continue to fight from America after losing much of its home territory.
If ordinary game rules eliminate Japan entirely, Event 074 does not secretly resurrect it or create a successor tag to preserve the expedition.

## Campaign phases

| Phase | Japan's immediate problem | United States response | Exit |
| --- | --- | --- | --- |
| Landing established | Deploy along a coherent front and protect unloading access | Locate the actual footprint and move regular forces west | First transport objectives are active |
| Coastal expansion | Capture another port or transport junction and connect pockets | Hold routes to the interior and avoid isolated city garrisons | Japan gains a connected coast or the front stabilizes |
| Inland campaign | Extend supply behind the advancing army | Cut vulnerable corridors and concentrate counterattacks | Ordinary territorial gains or Japanese containment |
| Isolated expedition | Fight toward a working port while support runs down | Keep the coast closed and finish disconnected pockets | Access restored, special support ends, or coastal control disappears |
| Ordinary supported or unsupported war | Use surviving troops and normal supply | Continue the national war | Normal war ending or disappearance of an actor |

A missed mission changes available support and opportunities, not the rules of war.
The game never destroys an army because a progress bar expired.

## Player information

Use the normal map, army interface, and two actor-specific decision categories.
Each category shows two event-specific operational readings: usable registered access points and remaining special-support time.
Actual division strength, fuel, stockpiles, supply, and airfield capacity remain visible through their normal interfaces.
Do not invent a second equipment wallet or claim that national fuel is physically stored in California.

Detailed tooltips explain which ports qualify, when support expires, which delivery is available, and why a decision is blocked.
Internal issue totals, milestone guards, selection scores, and transaction receipts stay out of the main category description.

## Design acceptance

A successful baseline test has a visible, controllable Japanese army on the mainland immediately after the event.
With Japan's original navy removed and its original stockpiles exhausted, the new army can begin a credible land operation and survive ordinary opening logistics.
A competent American response can still contain it.
A successful high-tier test creates several useful entry points and a large western theater without causing every formation to pile into one undersupplied province.

The army is allowed to lose through combat, encirclement, lost infrastructure, and later supply failure.
It must not arrive already defeated by empty equipment, missing manpower, zero organization, invalid aircraft, or a broken supply setup.
