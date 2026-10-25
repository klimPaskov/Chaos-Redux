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
SCN-020 through SCN-033 are reserved for the named proposed designs below; they have not been added to gameplay or the public catalog.

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
| SCN-018 | Unregistered | None | Fracture Cascade removed by user direction on 2026-10-13 |
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
| SCN-033 | The Final Boss | Event 103 | Reserved for proposed design |

Event 068 has four independently reserved entries.
Event 069 has one reserved entry with four types; those types do not consume four scenario IDs.
The original SCN-015 proposals for Events 030, 038, 043, 044, and 067 are superseded by the allocations above.
Missile Age retains SCN-015.
The Final Boss independently reserves name-sort key `the_final_boss_name = 4.375`, after the existing Fallout key and before Global Jihad in the current name-order table.
Its four intensities share one scenario ID.
The user confirmed manual relaunch after a defeated episode on 10 October 2026, with one active or provisional Directorate at a time and ordinary terminal-conflict gates retained.

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
| 3 | Diplomatic Panic (runtime key `diplomatic_panic`) | implemented |
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
Cthulhu’s Dominion reserves world-end ID 17, The Red World reserves ID 18 for Event 091, and Chaos Always Wins reserves ID 19 for Event 103.
Global Jihad retains 15 and World of Anarchy retains 16.
The held triggerable ID SCN-017 does not conflict with this world-end reservation.
Existing world-end keys and occupied numbers are recorded in the machine-readable registry and their runtime constants.
Lower gaps are not allocated by this audit.
Chaos Always Wins uses the shared primary sort value 10 within its event, which is a reusable display category rather than another unique scenario ID.

## Super-event presentations

| Slot | Presentation | Owner | Disposition |
| --- | --- | --- | --- |
| 119 | Super-Alloy operational breakthrough | Event 098 | Reserved for proposed design |
| 120 | The World of Dust global disruption (working title) | Event 099 | Reserved for proposed design |
| 121 | The Great Revolution opening | Event 091 | Reserved for proposed design |
| 122 | The Red World terminal branch | Event 091 | Reserved for proposed design |
| 123 | The Great Revolution earned defeat | Event 091 | Reserved for proposed design |
| 124 | Chaos Always Wins | Event 103 | Reserved for proposed design |
| 125 | Durable Union of Hosts | Event 112, SE01 | Reserved for proposed design |
| 126 | Cossack Russia formation | Event 112, SE02 | Reserved for proposed design |
| 127 | Golden Horde formation | Event 112, SE03 | Reserved for proposed design |

The presentation namespace uses the value of `super_event_visible`, separately from triggerable and world-end scenario IDs.
Slot 117 belongs to Acid Rain and slot 118 belongs to the Gods of Africa global-credibility presentation; both use constant-based selectors and must be included when checking occupancy.
Slot 119 was checked against current selectors, constants, localisation keys, and planning reservations before allocation.
Slot 120 was checked against those same surfaces for Sandstorm on 8 October 2026, including the existing New Ore reservation at 119.
The reservations do not implement presentations or approve final text, images, or recordings.
Events 098 and 099 have no audio ID allocation in this ledger.
Event 091 independently reserves playback audio IDs 121, 122, and 123 for its opening, terminal branch, and earned defeat respectively.
The matching numbers are an explicit mapping between separate namespaces, not a rule for deriving audio IDs from presentation slots.
The 9 October import review checked current literal and constant selectors, source dispatch inputs, sound registrations, canonical workbook entries, and existing planning reservations before these allocations.
Event 103 independently reserves presentation 124 and playback audio 124 for Chaos Always Wins after the 10 October current-source and planning-reservation check.
Sound volume-wrapper names use playback audio ID 124, independently from the presentation mapping.
Event 112 independently reserves presentations 125, 126 and 127 and playback audio 125, 126 and 127 for SE01, SE02 and SE03 respectively.
The 10 October source check includes literal and constant selectors, sound wrappers, current reservations and 33 resolved dynamic-dispatch caller inputs.
Keep each final recording and sound registration unique, and recheck occupancy before runtime wiring.

## Imported event identity proposals

On 24 October 2026, the user explicitly instructed: “Adopt uploaded IDs and migrate the catalog.”
The catalog uses the package identities below for Events 104 through 122.
The migration carries the earlier package identities through the dependency chain so that moving IMRO, SPARTA and Cossacks does not erase Random Idea, Resistance, Lootboxes, Rule or Wrestling Tournament.
The [import and migration report](../plans/repo_cleanup/planning_package_import_2026-10-24.md) records the completed workbook checks and the [machine-readable record](../plans/repo_cleanup/planning_package_import_2026-10-24.json) preserves all original rows and displaced concepts.
Catalog identity approval does not approve every proposed mechanic, register runtime content or change availability.
All migrated events remain `Unavailable` because their event roots are absent.

| Event ID | Package | Former catalog ID | Disposition |
| --- | --- | --- | --- |
| 104 | [Rule](104_rule_specs/104_rule_reading_guide.md) | 107 | User-confirmed catalog identity, runtime unimplemented |
| 105 | [Random Idea](105_random_idea_specs/README.md) | 110 | User-confirmed catalog identity, runtime unimplemented |
| 106 | [Resistance](106_resistance_specs/README.md) | 111 | User-confirmed catalog identity, runtime unimplemented |
| 107 | [Lootboxes](107_lootboxes_specs/README.md) | 112 | User-confirmed catalog identity, runtime unimplemented |
| 108 | [Wrestling Tournament](108_wrestling_tournament_specs/00%20-%20Package%20Guide.md) | 113 | User-confirmed catalog identity, runtime unimplemented |
| 109 | [Fuel Crisis](109_fuel_crisis_specs/README.md) | 114 | User-confirmed catalog identity, runtime unimplemented |
| 110 | [IMRO](110_imro_specs/README.md) | 115 | User-confirmed catalog identity, runtime unimplemented |
| 111 | [This is SPARTA!!!](111_this_is_sparta_specs/111_this_is_sparta_index.md) | 116 | User-confirmed catalog identity, runtime unimplemented |
| 112 | [Rise of Cossacks](112_rise_of_cossacks_specs/README.md) | 122 | User-confirmed catalog identity, runtime unimplemented |
| 113 | [The Partition](113_the_partition_specs/113_the_partition_package_guide.md) | 123 | User-confirmed catalog identity, runtime unimplemented |
| 114 | [Demilitarization](114_demilitarization_specs/README.md) | 124 | User-confirmed catalog identity, runtime unimplemented |
| 115 | [Heroic Crusade](115_heroic_crusade_specs/README.md) | 126 | User-confirmed catalog identity, runtime unimplemented |
| 116 | [Warlords](116_warlords_specs/README.md) | 127 | User-confirmed catalog identity, runtime unimplemented |
| 117 | [Autonomy](117_autonomy_specs/README.md) | 128 | User-confirmed catalog identity, runtime unimplemented |
| 118 | [Shaman](118_shaman_specs/README.md) | 129 | User-confirmed catalog identity, runtime unimplemented |
| 119 | [Mistresses](119_mistresses_specs/README.md) | 130 | User-confirmed catalog identity, runtime unimplemented |
| 120 | [Widespread Mutiny](120_widespread_mutiny_specs/README.md) | 131 | User-confirmed catalog identity, runtime unimplemented |
| 121 | [Investment](121_investment_specs/README.md) | 132 | User-confirmed catalog identity, runtime unimplemented |
| 122 | [Gandhi](122_gandhi_specs/README.md) | 133 | User-confirmed catalog identity, runtime unimplemented |

The former catalog holds at 110, 113 and 122 are released by this authorized migration.
Their historical hold records remain in the JSON ledger.
Event 122 belongs to Gandhi, and Rise of Cossacks belongs to Event 112.
Presentation and playback audio identifiers remain separate namespaces and are not derived from the event number.

The displaced catalog concepts are Stability or War support (104), Anti-player ideology (105), Paranoia (106), Fury (108), Custom laws (109), 5-Way Civil War (117), Plague of locust (118), Random New Alliance (119), Massive Volcano Eruption (120) and The Pact (121).
Their full pre-migration rows are preserved separately, without inventing replacement IDs or silently treating them as aliases of another event.
Old source rows 123, 124 and 126 through 133 are retired after their concepts move to their canonical IDs.
Non-Aggressions retains 125.

Tasks 101 and Serial Killer 102 retain their existing catalog identities.
Chaos Directorate 103 remains a separate imported replacement proposal for the catalog’s Conscription entry, outside this migration.
Its original brief and previous import receipt retain the existing acceptance boundary.

## Imported identity adoptions on 25 October 2026

On 25 October 2026, the parent relayed the user’s authorization to adopt the uploaded identities for four newly imported planning packages and migrate the catalog rows.
The migration moves each row to its canonical ID with its name, Type, Chaos level, Cluster ID and Status unchanged.
The former rows 135, 136, 149 and 150 are consumed by these moves and are no longer active catalog identities.
Event 131 is restored as a repeatable migration starter owned by the existing migration system, so its former retired-row Details text is superseded.

| Event ID | Package | Former catalog ID | Disposition |
| --- | --- | --- | --- |
| 123 | [Equipment choice](123_equipment_choice_specs/README.md) | 135 | User-confirmed catalog identity, runtime unimplemented |
| 124 | [Sun moves away](124_sun_moves_away_specs/README.md) | 136 | User-confirmed catalog identity, runtime unimplemented |
| 131 | [Immigrations](131_immigrations_specs/README.md) | 149 | User-confirmed catalog identity, runtime unimplemented |
| 132 | [Secret Society Influence](132_secret_society_influence_specs/README.md) | 150 | User-confirmed catalog identity, runtime unimplemented |

Catalog identity adoption does not approve the packages’ proposed mechanics, register runtime content or change availability.
All four events remain `Unavailable` because their event roots are absent.
The Event 124 Details were corrected on the same date to the parent-supplied description of the Sun moves away event.

## Current event-design decisions

The user’s 24 October instruction makes Lootboxes a worldwide first-fire event.
Every country existing at that first firing receives access and one free box using normal random rarity and ordinary reward resolution, and each human country receives the opening window automatically.
Later purchases remain 50 PP, and the first grant has its own zero-payment receipt and once-only guard.
The Event 107 specification and catalog description carry this accepted design, with runtime implementation still queued.

The same instruction places Fuel Crisis 109 in Various Anomalies (cluster 11) as a Severe member.
The catalog membership is recorded under 109 after migration from 114.
The core event’s independent eligibility is unchanged, and runtime cluster registration remains queued with the event implementation.

## Deaths accounting reasons

Event 102 reserves `chaos_meter_deaths_reason.serial_killer = 40`, accessed as `constant:chaos_meter_deaths_reason.serial_killer` after implementation.
The current reason category in `common/script_constants/chaos_meter_constants.txt` occupies 0 through 39 plus 291 and 292.
The 10 October import checked those constants and planning references before reserving 40, without changing runtime reason registration, selectors or localisation.
Only independently caused Event 102 civilian losses use this reason. Crossovers retain the source owner's casualties and receipts.
The reservation and dedicated overlap evidence are recorded in the machine-readable registry and Event 102 import evidence.
The existing general identifier checker does not cover this additional namespace, so its dedicated constant/reservation comparison remains required.

## Event and country identities

`chaosx.nr18.33` is assigned to No Ground for a Survey, separating it from A Quarter of the Continent at `chaosx.nr18.90`.
The repair updates the survey caller and its three text keys together.
DTH, KRG, and REV are registered country identities for Death, Kruger, and the World Revolution.
CXT is the registered test-country carrier reused by the proposed Chaos Directorate role, with clean-mode admission and migration required before gameplay.
Its installed collision scan found this checkout and its matching QA copy only.
Their owner packages must reuse and inspect them instead of treating those tags as free candidates.
The REV scan also found the same identity in the installed Random Events Mod (Workshop 3199436992) and the Chaos Redux QA checkout.
Those external definitions are a compatibility consideration, not a reason to allocate a second Event 091 tag or rename its incumbent identity during documentation import.
DHC and KHC remain the Event 005 Don and Kuban carriers, reused by the proposed Event 112 admission contract.
The installed tag/cosmetic scan found this checkout and its identical QA copy only.
Living countries retain their content, and dormant admission must reconcile the current random-name history with grounded identity requirements.
Event 112 leaves generic carrier allocation to its declared geography and admission audit, so those unspecified slots are not represented as reserved tags.
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

Run `python .tools/audits/check_planning_identifiers.py` to check this ledger against live numeric constants, its declared package evidence, top-level event definitions, runtime country tags, and canonical workbook cluster identities.
The check does not infer definitions from historical prose or certify every undeclared future helper, sprite, or entity name.
