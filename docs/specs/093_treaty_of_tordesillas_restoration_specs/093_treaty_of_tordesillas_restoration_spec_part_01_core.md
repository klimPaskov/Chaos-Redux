# Treaty of Tordesillas Restoration: core design


## Catalog identity

Event 093 is **Treaty of Tordesillas Restoration**, formerly **Portugal wants land**.
It is a **Minor Fire-Once** event with **Chaos level 1**, in the **Formables** cluster as its **Medium member**.
Its implementation status remains **To Be Reworked**.
The initiating event is one firing.
Its diplomatic aftermath, four evolutions, integration projects, and possible world-end are continuations of that firing, not repeat selections from the event pool.

The user's current brief is authoritative for these design choices.
The supplied catalog still contains the earlier Galicia-only idea and no Event 093 cluster assignment.
That difference is a pending catalog migration, not permission to silently change the export or label the event implemented.

## The experience

Portugal begins with a demand that a government can plausibly bargain over: Galicia.
Spain might pay that price to secure a quiet border, extract compensation, or obtain Portuguese assistance during a civil war.
It might also refuse.
A player who only experiences the baseline should receive a complete Iberian story with a settlement, a failed bargain, or a real confrontation.

The absurdity arrives through escalation.
Two governments discover that an old agreement about dividing distant possessions is useful for ending their own arguments.
Later, they declare that its logic applies to every country on Earth.
The eventual partnership is dangerous because the countries help one another turn claims into organized empires, not because a popup supplies limitless divisions or annexes the map.

The player should remember what was promised over Galicia when the same governments negotiate ownership of continents.
An honored bargain makes cooperation easier.
A victory purchased with Portuguese aid and followed by betrayal leaves a specific debt.
A Portuguese invasion can produce a settlement, but it cannot retroactively become an act of friendship.

## Three valid campaign outcomes

The baseline can end without a restored treaty.
This is a successful completion of the opening design, not a failed attempt to reach the 'real' content.
A modest Portugal might take Galicia and stop.
A stable Spain might prevent the transfer.
A Portuguese player might abandon an expensive intervention.

A second campaign can produce a limited, durable Iberian alliance.
The partners resolve their dispute and use the treaty to coordinate overseas interests, yet decline the later universal partition.
That route should retain its diplomatic benefits without being dragged into world conquest by a hidden timer.

The full escalation produces complementary imperial expansion, regional integration, and eventually **Two Crowns, One World**.
Neither this route nor its ending is guaranteed by the initial selection, a compatible ideology, or crossing a Chaos threshold.

## Countries and legitimacy

Portugal means the living Portuguese state, resolved through the current country identity and its legitimate continuity.
Spain means the living national Spanish authority, or the competing national Spanish authorities during a civil war.
A tag name, cosmetic name, or original-tag test alone does not establish that a country is the proper participant.

The scenario adds no new historical leader, dynasty, ideology, or country tag.
It does not require either government to be a monarchy.
'Two Crowns' is the user's established imperial metaphor and world-end name.
A republic can revive the treaty as a state doctrine, while an anarchist or strongly anti-imperial government can consistently refuse it.

Regional independence movements are not automatically treated as national Spanish governments.
A Galician state owns its own territory and must be involved in any agreement that would transfer it.
Spain cannot sell another sovereign country's land by selecting an option.

## Preparation before the opening

Before the global event is accepted as a valid firing, resolve Portugal, Galicia on the current map, the relevant Spanish authorities, and the owner and controller of the disputed territory.
A missing Portuguese state or an unresolvable geography definition makes the event ineligible, rather than consuming its only firing on a broken target.

An existing Portugal that owns Galicia is a valid special case.
The opening becomes a request for Spanish recognition of the existing settlement, not another transfer or free core.
A temporarily occupied Galicia can support negotiations, but no government may transfer legal ownership it does not possess.
An unresolved Spanish succession is a reason to use the civil-war or disputed-authority route, not to assume the historical Nationalists have won.

The participant summary must identify the actual countries and what each can promise.
Portugal can decline to press its claim.
This closes the immediate crisis without a punishing, obligatory political-power loss and without barring a later, genuinely mutual treaty discussion.

## Persistent memory with a small public interface

The design has four public custom values at most: **Iberian Confidence**, **Aid Fulfillment** while a contract is active, **Spanish Consolidation**, and **Portuguese Consolidation** after regional integration becomes available.
The last two are readiness indicators for the two-sided imperial project, not claims that that percentage of the globe is owned.

Confidence describes how credible ongoing cooperation is.
It cannot remove an unresolved territorial dispute, replace an explicit treaty vote, or prove that a civil-war promise was fulfilled.
Aid Fulfillment is calculated from actual credited deliveries under the signed contract.
Consolidation is derived from correct-sphere reach and integrated territory, as specified in Part 09.

Everything else is an outcome, a native country statistic, a project status, or a supporting record.
A named breach, an agreed Galician settlement, and the identity of an aid recipient are facts, not additional currencies.
The player should manage a dispute, an alliance, and regions, rather than twenty parallel meters.

Each value's tooltip answers one question: what the value is now, which gate it opens next, and what is holding it back.
Confidence names its next gate (50, 60 or 65) and the one unresolved obligation that blocks it, if any.
Aid Fulfillment shows the delivered share and the component furthest behind.
Consolidation shows whether reach or integration is the limiting component.
Internal ledgers, receipts, cooldowns and frozen weights never appear as extra lines.

## The lifecycle

The ordinary sequence is preparation, Galicia crisis, settlement or lasting dispute, possible treaty restoration, geographic partition, regional integration, universal conquest doctrine, and possible world-end.
There are deliberate exits between these stages.
A treaty may be suspended or dissolved.
Defeat can interrupt an integration project.
A former partner can survive as an ordinary country after the imperial system collapses.

Evolution thresholds are 200, 400, 600, and 800 Chaos in that order.
World-end eligibility is strictly above 1000.
An event selected at 1100 Chaos still opens with Galicia.
It does not begin with world claims, free cores, or a completed faction.
Stage requirements remain meaningful at high Chaos.

## What the design does not add

There is no unconditional Iberian union, replacement focus tree, free historical expeditionary army, magical transport across hostile seas, new resource economy, or custom technology tree.
There is no requirement for unique 3D units, animated portraits, or native raid content.
Existing national identities and meaningful vanilla or modded systems remain in place.

Numerical choices in Part 14 are proposed tuning, not observed balance results.
