# Event 088: Mines everywhere
## Part 1. The world change

### Catalog identity

| Field | Design |
| --- | --- |
| Event ID | `088` |
| Event name | Mines everywhere |
| Type | Minor Fire-Once |
| Status | To Be Reworked |
| Minimum Chaos level | 1 |
| Primary cluster | Sudden Abundance |
| Cluster severity | Medium member |

### The incident

The world's seas acquire minefields in a single incident. The danger is immediately present in busy coastal approaches and remote ocean regions alike. Every eligible country receives a separate contribution in every valid naval strategic region. The quantity requested for each country-region pair is 1,000 additional mines, constrained by the engine's normal mine limit for that owner and region.

The central absurdity is abundance without preparation. A country can discover that it owns minefields far beyond the reach of its fleet while its own shipping faces equally extensive fields owned by opponents. Naval superiority, previous reconnaissance, possession of a coastline, and distance from the main war do not carve safe regions out of the geographical coverage. Friendly and neutral relationships still matter to the way the game resolves danger. The incident does not make every country an enemy of every other country.

The event should feel like an immediate change in what the sea means. Routes that were usable before the firing may now need clearance. Ships already at sea remain where they are and face subsequent native mine interactions. The opening does not destroy a scripted quota of ships, teleport fleets into danger, or charge countries for equipment they never ordered. The actual minefields carry the incident.

### What the player must understand immediately

The report communicates three facts together: the geographical coverage is global, mine ownership remains separate, and clearing hostile mines is still possible. A player should not mistake 1,000 mines for a combined global allowance, a single country's regional field for all hostile fields, or the event for a permanent modifier that will restore mines after they are swept.

The report arrives after the world change has been committed. Acknowledging it cannot choose which countries receive mines, delay a rival's minefield, or apply the effect a second time. The same world state must result whether a human closes the report immediately, leaves it open, or an AI handles its own notification first.

A country that cannot own mines still receives appropriate awareness through the ordinary event presentation. Its report explains the worldwide development without claiming that a nonexistent fleet has been struck or that it received a minefield contribution. Geographic completeness is independent of the identity of the country reading the report.

### The baseline experience

The first stage is recognition. The player opens the naval map and discovers that choosing a distant alternative does not automatically escape the incident. Existing friendly minefields have not been removed. Opposing ownership can coexist in the same sea region. The useful question becomes which hostile fields affect a particular operation and how that operation can be protected or delayed.

The second stage is triage through ordinary naval play. A country dependent on overseas supply may prioritize the approach to its main receiving port. A naval attacker may need to clear the approach to a planned landing while still protecting shipping elsewhere. A small fleet may preserve its valuable combat vessels and concentrate its limited clearance capability. These are different responses to the same world change, rather than scripted response branches with flat bonuses.

The third stage is uneven reopening. One country can clear a corridor relevant to its current enemies while another remains exposed elsewhere. Clearance can create a local operational advantage without pretending the entire ocean is safe. Event 088 does not erase this progress, replenish its original contribution, or trigger another worldwide deposition when a route becomes usable.

### One incident, persistent physical aftermath

The firing is global and occurs once for the campaign. The minefields then belong to normal game state. The event has no arbitrary expiration date that clears them all at once. Their survival, sweeping, hostility, decay, and ownership changes follow the verified behavior of the active engine and supported campaign setup.

The difference between a once-only incident and persistent consequences must remain clear. A country created later does not cause another event pass. A later war does not cause a refill. Loading a save, switching the viewed country, reopening event details, and receiving another notification do not repeat the incident. If normal minelaying subsequently introduces new mines into a cleared region, that is a later game action rather than Event 088 undoing the clearance.

### Scale and pacing

The user-defined 1,000-mine amount stays fixed. Higher eligible Chaos conditions do not increase the baseline above the normal cap, turn mines unsweepable, or introduce recurring saturation. The interesting escalation comes from the existing campaign: more belligerents can mean more relevant hostile owners, wider wars can expose more routes, and weakened fleets may have fewer resources available for clearance.

The event needs one strong reveal. Repeating an identical popup for every country-region pair would bury the actual strategic change. The shared event history records the global incident once. Country-facing presentation may explain personal participation without creating additional incidents or additional Chaos awards.

### Meaningful campaign situations

**A contested coastal approach.** Two enemy countries both own fields in the region. A country may benefit from the danger its own field creates for its enemy while still needing to sweep the enemy field. Owning a full field is not immunity from other ownership.

**A distant supply route.** The incident reaches sea regions that neither side would normally prioritize for minelaying. Its global geography removes the assumption that distance alone guarantees a safe alternative. Actual danger still depends on the native hostility and mission rules.

**An enclosed sea.** A valid naval region remains covered even if access is restricted. The event does not open a strait, bypass naval movement rules, or make clearance equipment appear on the other side of an access restriction.

**A peaceful world.** Countries can receive ownership without the event declaring wars. The material fields exist under the engine's peacetime behavior. The report must not claim that all neutral trade is already being attacked. Any later decay or hostility transition is native behavior that the implementation must verify and describe honestly.

**A small or landlocked participant.** Country size, importance, and whether it is the human player do not determine geographical coverage. Eligibility to own mines is handled consistently. Excluding an invalid owner does not exempt the sea beside that country or any other sea.

**A heavily modified map.** Newly introduced valid seas and changed naval regions participate on the same basis as the rest of the active map. A region's absence from the historical map is never a reason to skip it.

### Success condition

The design succeeds when a single campaign-wide firing adds the intended native mine contribution to every eligible country-region pair without removing existing mines, and normal clearance can subsequently change the operational situation. The visible result is a dangerous, unevenly recoverable maritime world. Coverage, ownership, and the permanence of real clearance are the identity of the event.
