# Shared identifier registry

This ledger reserves identifiers across current planning packages and records occupied runtime identities.
The allocation basis is the user’s 7 October 2026 instruction to assign unoccupied scenario IDs and prevent overlaps.
An identifier reservation does not approve the surrounding design, register runtime content, or establish playability.
Implemented IDs remain stable; proposals use unused slots and retain their separate acceptance requirements.

The [machine-readable registry](shared_identifier_registry.json) carries the same assignments and source locators.
The [scenario occupancy audit](../plans/repo_cleanup/specification_package_audit_2026-10-07/handoffs/scenario_occupancy.md) records the runtime and canonical workbook checks that preceded allocation.

## Triggerable scenarios

The `SCN-` label corresponds to the raw integer in `triggerable_scenario_id`.
Public workbook rows, internal registrations, retired compatibility identities, and explicit holds all occupy their slots.
The absence of a workbook row is not permission to reuse an ID.
SCN-014 belongs to Fallout; SCN-004 remains a compatibility identity; SCN-017 remains held because its owner has not been established.
SCN-020 through SCN-032 are reserved for the named proposed designs below; they have not been added to gameplay or the public catalog.

| ID | Scenario | Owner | Disposition |
| --- | --- | --- | --- |
| SCN-001 | Zombie Apocalypse | Event 002, Zombie Outbreak | implemented |
| SCN-002 | Army of Clones | legacy shared clone scenario; original owner not identified in current docs; Event 016 only has a connection hook | implemented owner unresolved |
| SCN-003 | Soviet Collapse | Event 005, Union Unmade | implemented |
| SCN-004 | retired Final Silence compatibility alias | legacy dispatcher redirects to Fallout | retired alias do not reuse |
| SCN-005 | World in Fury | Event 007 | implemented |
| SCN-006 | Death | Event 010 | implemented |
| SCN-007 | Disaster Barrage | Event 013 | implemented |
| SCN-008 | Every Banner Rises | Event 006 | implemented |
| SCN-009 | Coalition Unmasked | Event 011 | implemented |
| SCN-010 | The Hunger Lines | Event 014 | implemented alias |
| SCN-011 | Africa Is One | Event 012 | implemented |
| SCN-012 | Black Plague Unbound | Event 020 | implemented |
| SCN-013 | The Unbidden Muster | Event 019 | implemented alias |
| SCN-014 | Fallout manual consequence sandbox | Air Cleanliness/Fallout system | implemented runtime catalog gap |
| SCN-015 | Missile Age | Event 032 | implemented collision incumbent |
| SCN-016 | Global Jihad | Event 031 | implemented |
| SCN-017 | None | None | reserved by comment owner undocumented |
| SCN-018 | The Fracture Cascade | Event 021 | implemented alias |
| SCN-019 | Assassin Network | Event 039 | implemented |
| SCN-020 | All Times at Once | Event 030 | Reserved for proposed design |
| SCN-021 | Believers vs Nonbelievers | Event 038 | Reserved for proposed design |
| SCN-022 | Monsters from the Deep | Event 043 | Reserved for proposed design |
| SCN-023 | Yakubite Uprising | Event 044 | Reserved for proposed design |
| SCN-024 | Generalissimo's Coup | Event 067 | Reserved for proposed design |
| SCN-025 | First Colonies | Event 068 | Reserved for proposed design |
| SCN-026 | The Empty Throne | Event 068 | Reserved for proposed design |
| SCN-027 | Open Crossings | Event 068 | Reserved for proposed design |
| SCN-028 | The Reckoning of ZIN | Event 068 | Reserved for proposed design |
| SCN-029 | Boxer challenge (four types) | Event 069 | Reserved for proposed design |
| SCN-030 | Cookie Monster Uprising | Event 070 | Reserved for proposed design |
| SCN-031 | War for the Soul | Event 084 | Reserved for proposed design |
| SCN-032 | The Ten Plagues | Event 085 | Reserved for proposed design |

Event 068 has four independently reserved entries.
Event 069 has one reserved entry with four types; those types do not consume four scenario IDs.
The original SCN-015 proposals for Events 030, 038, 043, 044, and 067 are superseded by the allocations above.
Missile Age retains SCN-015.

## Event clusters

The live `event_cluster_id` constants retain their meanings.
The canonical workbook uses Diseases 8, Random Stuff 12, and Pacts 13 under the same identifier-cleanup authorization.
The former Random Stuff catalog ID 19 stays held; it is not offered for reuse.
The historical v2 mapping in `docs/systems/event_system/event_clusters.md` is a competing migration proposal, not permission to reuse live identities.
Scientific Research 21 and Internal Fracture 22 reserve distinct proposed identities only.
Event 031 remains cataloged under Domestic Unrest 16; reserving Internal Fracture does not add or replace membership.
Event 043/046 Alien Invasions membership remains a separate design conflict.

| ID | Cluster | Disposition |
| --- | --- | --- |
| 1 | Wars | implemented |
| 2 | Liberations | implemented |
| 3 | Diplomacy (runtime key `diplomatic_panic`) | implemented |
| 4 | Peace | implemented |
| 5 | Natural Disasters | implemented |
| 6 | Formables | implemented |
| 7 | Positive Economy | implemented |
| 8 | Diseases | implemented |
| 9 | National Breakthroughs | implemented |
| 10 | Negative Economy | implemented |
| 11 | Various Anomalies | implemented |
| 12 | Random Stuff | implemented |
| 13 | Pacts | reserved proposed design |
| 14 | Randomizations | reserved proposed design |
| 15 | Sudden Abundance | reserved proposed design |
| 16 | Domestic Unrest | reserved proposed design |
| 17 | Alien Invasions | reserved proposed design |
| 18 | Military Preparation | reserved proposed design |
| 19 | Former Random Stuff catalog identity | retired catalog alias held |
| 20 | Intelligence | implemented |
| 21 | Scientific Research | reserved proposed design |
| 22 | Internal Fracture | reserved proposed design |

## World-end scenarios

`world_end_scenario_id` is separate from the `SCN-` triggerable namespace.
Cthulhu’s Dominion reserves world-end ID 17; Global Jihad retains 15 and World of Anarchy retains 16.
The held triggerable ID SCN-017 does not conflict with this world-end reservation.
Existing world-end keys and occupied numbers are recorded in the machine-readable registry and their runtime constants.
Lower gaps are not allocated by this audit.

## Super-event presentations

| Slot | Presentation | Owner | Disposition |
| --- | --- | --- | --- |
| 119 | Super-Alloy operational breakthrough | Event 098 | Reserved for proposed design |
| 120 | The World of Dust global disruption (working title) | Event 099 | Reserved for proposed design |

The presentation namespace uses the value of `super_event_visible`, separately from triggerable and world-end scenario IDs.
Slot 117 belongs to Acid Rain and slot 118 belongs to the Gods of Africa global-credibility presentation; both use constant-based selectors and must be included when checking occupancy.
Slot 119 was checked against current selectors, constants, localisation keys, and planning reservations before allocation.
Slot 120 was checked against those same surfaces for Sandstorm on 8 October 2026, including the existing New Ore reservation at 119.
The reservation does not implement the presentation or approve final text, image, audio, or an audio ID.
Allocate the final audio ID independently and keep its unique recording and sound-registration requirements.

## Event and country identities

`chaosx.nr18.33` is assigned to No Ground for a Survey, separating it from A Quarter of the Continent at `chaosx.nr18.90`.
The repair updates the survey caller and its three text keys together.
DTH and KRG are registered country identities for Death and Kruger; their owner packages must reuse and inspect them instead of treating those tags as free candidates.
The duplicate Event 012 package is historical provenance, and the two Event 097 design variants share the existing `chaosx.nr97.1` root.
Their presence does not allocate another runtime namespace.

## Namespace and maintenance rules

Triggerable scenarios, world-end scenarios, event-cluster IDs, event namespaces, country tags, and cosmetic identities are separate namespaces.
Equal numeric values in separate registries are not collisions.
A shared reference to an existing owner is not a second definition.
Before allocating any identifier, check the runtime source, this ledger, the canonical XLSX where applicable, and current package reservations.
Update the owner package and this ledger together; preserve original archive receipts as dated evidence.
A retired or unresolved held ID must be explicitly released before reuse.
Country tags additionally require the installed vanilla, local-mod and Workshop collision check required by the event-planning skill.

Run `python .tools/check_planning_identifiers.py` to check this ledger against live numeric constants, its declared package evidence, top-level event definitions, runtime country tags, and canonical workbook cluster identities.
The check does not infer definitions from historical prose or certify every undeclared future helper, sprite, or entity name.
