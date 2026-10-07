# Treaty of Tordesillas Restoration: geography and the two spheres


## A geographic rule, not a country list

Every valid claimable land state on the current supported campaign map receives one geographic sphere or a protected exception. Ownership, ideology, faction membership, capital location, and whether a country is usually considered European or American do not determine its sphere.

Countries can straddle the division. Spain and Portugal may therefore have interests in different states of the same country. That is intentional. It creates a need for coordinated peace aims and careful subject arrangements. Annexing or releasing a country must not move the line.

The partition is generated from the installed map and validated before gameplay. Runtime ownership and control are then evaluated dynamically against that stable geography. A generated ledger is compatible with a dynamic partition requirement. A hand-written list assigning Brazil, China, or modern continents wholesale is not.

## Historical inspiration and the game convention

The 1494 treaty used a north-south line 370 leagues west of the Cape Verde Islands, with Portuguese rights to its east and Castilian rights to its west. The 1529 Saragossa agreement addressed the competing Asian claims through a further settlement. These sources provide the design's inspiration, not a scientifically exact pair of modern longitudes. [H1](093_treaty_of_tordesillas_restoration_source_and_decision_register.md) [H2](093_treaty_of_tordesillas_restoration_source_and_decision_register.md)

For this event, adopt a clearly labelled **game convention**: an Atlantic meridian at **46.5 degrees west**, with an opposite meridian at **133.5 degrees east**. Portugal receives the half reached eastward from the Atlantic line to the opposite line. Spain receives the complementary half. The two arcs are each 180 degrees. This is a deliberate, legible reinterpretation, not a claim that the historical treaties established these exact modern coordinates.

The opposite line preserves a recognizable two-half rule. The historical Asian settlement informs restitution, overlapping claims, and mutual consent. It is not falsely presented as the literal antipode of an undisputed 1494 meridian. The explanatory text must keep that distinction.

The chosen convention can be changed during pre-implementation map review only through a recorded design correction and regenerated evidence. The player cannot move it repeatedly during the campaign to turn existing conquests into a different sphere.

## Assigning land to states

Use the geographic positions and shapes of the actual land provinces. A state wholly within one half belongs to that half. A state crossing a boundary belongs to the side containing the majority of its represented land area. Sea pixels, decorative map margins, and impassable non-state space do not count as land.

For an exactly equal split, use the side containing the state's verified representative land point, such as its principal victory-point province. If that point lies exactly on a boundary, use a documented stable identifier tie-break. The same input must always produce the same result, regardless of which country opens the interface first.

The engine's map projection must be inspected and geographically calibrated. Raw horizontal pixel position is not automatically longitude, and pixel count is not automatically real land area on a distorted projection. The implementation needs a documented approximation suitable for the installed map, sample checks on both boundaries, and disclosure of any unavoidable projection limits.

The live game cannot transfer half a state. The state-level majority rule is the intended compromise. The UI should show the resulting whole-state assignment rather than drawing a precise line that implies half-state ownership. Border cases should be inspectable, not silently assigned by their owner's capital.

## Protected Iberian homelands

The two partners' protected metropolitan Iberian sets are defined from the supported map's national homeland geography before treaty expansion. This is a curated, verified adapter for the two historical participants, not the world partition itself. The exact state set must be inspected against the installed game and any supported map overhaul.

Protection does not grow with new cores, conquest, cosmetic country names, or later annexations. Otherwise a partner could core a wrong-sphere colony and turn it into an untouchable 'homeland.' Overseas colonies and island possessions outside the agreed metropolitan definition are not silently protected by this rule.

Protection means Event 093 does not give the other treaty power claims, integration rights, or automatic restitution authority over those states. It does not transfer them to a country that currently lacks ownership, delete a third party's rights, or resolve an ongoing independence war. Such disputes remain genuine political facts.

Galicia is removed from the ordinary protected-set contest and treated as the event's named exception. Its recognized settlement owner has the event's eventual integration entitlement. A later treaty partner cannot reassign it with the globe's longitude rule.

## Claims and existing possessions

At partition adoption, each partner receives new treaty claims only where eligible. Existing native claims and cores are preserved. Each new treaty grant should record whether the claim already existed and whether another known system also requires it.

Wrong-sphere possessions acquired before restoration are presented as inherited exceptions awaiting settlement. They remain legally owned by the existing owner. The partners can negotiate transfer, a limited transitional arrangement, or a delay. A transitional arrangement prevents an immediate breach accusation but does not turn the state into correct-sphere integration credit for the wrong power.

A state that is already a native core of the wrong partner receives additional protection against automatic transfer. The donor must explicitly agree to cede it. This is a consent rule, not a permanent exemption from the final partition. A player who refuses to surrender such territory can keep it, while accepting that the fully divided world may remain unattainable.

New claims never grant access, take resources, annex subjects, or create a war by themselves. Treaty AI can decline to act on a claim when the target is an ally, the route is inaccessible, or the country is recovering from war.

## Sovereignty and control are different layers

The geographic layer is stable. Legal ownership determines who can cede land and who can core it. Military control determines who can currently administer or defend it. Sphere affiliation determines which treaty power has the event's integration right. None of these can be inferred from one another.

An occupation by Spain in the Portuguese Sphere during a common war is a military fact. The intended peace aim belongs to Portugal, but Spain cannot give away an enemy-owned state with a peacetime transfer action. The partners should agree their peace objectives and use the legal settlement once available.

A Portuguese subject occupying a Spanish Sphere state does not make that state Portuguese territory forever. Its ownership and subject status require a negotiated arrangement. Faction membership alone is never enough to treat all member territory as already divided between the crowns.

## Compatibility with altered maps

The ordinary target is the actual installed Earth map. State splits, mergers, and supported map overhauls require rebuilding the geographic and regional registries from the new geometry, then rechecking the protected homeland adapter. Map changes during a save are not a normal migration route and must not silently corrupt an existing partition.

A map without a usable Earth reference cannot honestly receive a Tordesillas-style longitude partition. It needs an explicit compatibility adapter approved for that setting. Unsupported geometry should block the global stages with a clear explanation while preserving any already valid Galicia-only content. It must not quietly fall back to a modern-country list.

## What the player sees

The partition preview uses the actual state shapes and current ownership from the game. It distinguishes Spanish assignment, Portuguese assignment, protected homelands, Galicia's settlement, and disputed inherited possessions. The player can inspect any border case and see why the state is assigned as it is.

A native map mode and a bounded selected-region panel are preferred to an elaborate separate treaty GUI. A static painted world map cannot be the authoritative state-puzzle display. A static legend or archival treaty illustration is decorative only. If an exact live map presentation is unavailable, global-stage publication remains blocked until a truthful supported presentation exists.

## Design invariants

Every eligible land state has exactly one ordinary sphere. Protected states and Galicia are explicit exceptions, not unassigned errors. Ownership changes never change geographic assignment. The two half-arcs have no overlaps or gaps. Inherited possession is distinct from integration entitlement. Changes to the map or convention require a versioned migration review.

These are design-level invariants. The package's synthetic arithmetic tests exercise them on abstract coordinates. They do not certify the actual HOI4 map, whose files and projection were not available during this planning pass.
