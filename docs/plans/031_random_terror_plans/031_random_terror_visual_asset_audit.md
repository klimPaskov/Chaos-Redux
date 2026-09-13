# Event 31 Random Terror Visual Asset Audit

## Scope and method

This audit traces every Event 31 visual from gameplay or interface consumer to registered sprite and runtime file, then reverses the inventory from each runtime file back to an intended consumer, source record, processed output, and DDS or TGA round trip.

The comparison baseline is the installed Hearts of Iron IV 1.19.2 asset family and the canonical Chaos Redux reference library under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference`.

Every assigned final is reviewed at native scale and enlarged scale for crop, overflow, bleed, clipping, alpha, centering, aspect ratio, subject hierarchy, normal-zoom readability, and family consistency.

Event 31 has no dedicated scripted GUI, 3D model, custom unit, bespoke counter, custom unit sound, or Event 19 provider, so those visual families have no Event 31 consumer and are intentionally absent.

## Inventory reconciliation

| Family | Runtime files before repair | Accepted runtime files | Consumer | Audit state | Disposition |
| --- | ---: | ---: | --- | --- | --- |
| Focus icons | 114 | 114 | `random_terror_actor_focus_tree` | Focus MCP raster and individual visual audit in progress | All 114 base sprites retained; 114 missing `_shine` consumers added in `interface/031_random_terror_shine.gfx`. |
| Idea icons | 29 | 29 | Event 31 national-spirit lifecycles | Individual specialist audit in progress | Pending specialist handoff. |
| Decision and mission icons | 48 | 48 | Event 31 decisions and missions | Repair in progress | The inherited detailed scene family failed at 32x32; all 48 are being regenerated as simple high-contrast native-scale icons. |
| Decision-category pictures | 3 | 3 | Government, actor, and scenario categories | Individual specialist audit complete | All three source, processed, DDS, and decoded-roundtrip views pass; their three live category sprites are consumed by `common/decisions/categories/031_random_terror_categories.txt`. |
| News pictures | 6 | 6 | `chaosx.news.310` through `chaosx.news.315` | Consumer and native visual audit complete | Retained. |
| Report pictures | 18 | 16 | `chaosx.nr31.2` through `chaosx.nr31.91` visible report callbacks | Wiring and visual repair complete | Report 04 was regenerated from an original fictional ImageGen source and passes exact DDS roundtrip validation. The two surplus runtime scenes were removed after preserving their documentation evidence and disposition. |
| Super-event pictures | 2 | 2 | Event 31 reveal and defeat super events | Native visual audit complete; specialist rights/wiring evidence retained | Retained. |
| Country-leader portraits | 45 | 45 | Eight carrier packages and entity/static consumers | Individual specialist audit in progress | Pending portrait handoff. |
| Entity animation | 2 | 2 | Shared Event Details evolution portrait with static fallback | Consumer verified; frame audit in progress | Ten real generated frames retained unless the frame audit identifies a concrete defect. |
| Faction emblems | 8 | 8 | Four large two-frame faction logos and four miniature logos | Wiring repaired; individual specialist audit in progress | Regional coordination, network confederation, Jihadist International, and Final Jihad command consumers registered. |
| Achievement states | 36 | 36 | Twelve achievements with colored, grey, and not-eligible states | Individual audit complete | All 36 retained; no crop, overlay, or readability repair required. |
| Cosmetic flags | 111 | 111 | Thirty-seven cosmetic identities at normal, medium, and small sizes | Consumer rotation and individual specialist audit complete | All 111 files pass native/enlarged inspection and exact processed-to-TGA roundtrip checks. All 37 identities now have deterministic active or dormant consumers; no weighted selection was introduced. |
| Text icon | 1 | 1 | Network Authority text-icon consumer | Individual specialist audit in progress | Pending specialist handoff. |

The accepted post-repair inventory is 421 runtime visual files.

## Report-art consumer matrix

| Accepted scene | Runtime file | Registered sprite | Live consumer or selection route | Status |
| --- | --- | --- | --- | --- |
| Damaged railway and civilian evacuation | `report_event_04_bomb_damaged_rail_bridge.dds` | `GFX_report_event_031_random_terror_bomb_damaged_rail_bridge` | Transport-disruption branch of `GetRandomTerrorIncidentReportPicture` | Regenerated from a prompt-recorded fictional ImageGen source; parent visual review and exact 210x176 DDS roundtrip passed. |
| Guarded station and emergency transport | `report_event_01_evacuation_station.dds` | `GFX_report_event_031_random_terror_evacuation_station` | Civilian-attack and copycat branches | Retained; public-domain source record verified. |
| Public-building crisis | `report_event_public_building_emergency.dds` | `GFX_report_event_031_random_terror_public_building_emergency` | Assassination, hostage, security-site, and capital-infiltration branches | Retained. |
| Burned depot | `report_event_burned_depot_captured_equipment.dds` | `GFX_report_event_031_random_terror_burned_depot_captured_equipment` | Depot-sabotage and arms-theft branches | Retained. |
| Intelligence raid and recovered documents | `report_event_intelligence_raid_recovered_documents.dds` | `GFX_report_event_031_random_terror_intelligence_raid_recovered_documents` | Intelligence, joint-operation, sponsor-evidence, sponsor-exposure, and failed-raid branches; partner-intelligence reports | Retained. |
| Relief and victims | `report_event_02_medic_civilian_aid.dds` | `GFX_report_event_031_random_terror_medic_civilian_aid` | Relief-strain branch | Retained; public-domain source record verified. |
| Border corridor | `report_event_border_corridor_military_protection.dds` | `GFX_report_event_031_random_terror_border_corridor_military_protection` | Smuggling, training-area, and port/convoy branches; corridor and intervention reports | Retained. |
| Armed enclave | `report_event_armed_enclave_captured_town.dds` | `GFX_report_event_031_random_terror_armed_enclave_captured_town` | Safe fallback for other baseline incident types | Retained. |
| Defecting soldiers or police | `report_event_defecting_soldiers_insurgency.dds` | `GFX_report_event_031_random_terror_defecting_soldiers_insurgency` | Defection and military-defection branches | Retained. |
| Capital guard | `report_event_capital_emergency_guard.dds` | `GFX_report_event_031_random_terror_capital_emergency_guard` | `chaosx.nr31.7` | Retained. |
| Rival groups | `report_event_rival_factions_border_standoff.dds` | `GFX_report_event_031_random_terror_rival_factions_border_standoff` | Rival-organization and cannibal-clash branches; `chaosx.nr31.43` | Retained. |
| Fictional Muslim religious and civic rejection | `report_event_religious_civic_rejection.dds` | `GFX_report_event_031_random_terror_religious_civic_rejection` | `chaosx.nr31.6` | Retained; no sacred hostile branding or real extremist identity. |
| Territorial proclamation | `report_event_territorial_proclamation.dds` | `GFX_report_event_031_random_terror_territorial_proclamation` | `chaosx.nr31.4` | Retained. |
| Fictional jihadist gathering | `report_event_international_network_gathering.dds` | `GFX_report_event_031_random_terror_international_network_gathering` | `chaosx.nr31.3`, `.44`, and `.90` | Retained; wholly fictional emblems. |
| Synchronized uprising | `report_event_synchronized_uprising.dds` | `GFX_report_event_031_random_terror_synchronized_uprising` | `chaosx.nr31.5` | Retained. |
| Liberation and reconstruction | `report_event_liberation_reconstruction.dds` | `GFX_report_event_031_random_terror_liberation_reconstruction` | `chaosx.nr31.8` | Retained. |

## Repairs applied by the parent implementation

| Defect | Repair | Evidence |
| --- | --- | --- |
| No Event 31 focus had the required `_shine` sprite. | Added one vanilla-contract shine sprite for each of the 114 focus icons. | Focus MCP resolves one tree with 114 focuses, 114 titles, zero connector crossings, and zero same-row spacing violations. |
| Eight accepted report sprites were missing from the GFX registry, including two sprites already referenced by events. | Registered all sixteen accepted report sprites. | Reverse registry scan and Event 31 event render. |
| Ten accepted baseline reports had no deterministic live consumer. | Preserved the selected incident type on the affected country and added `GetRandomTerrorIncidentReportPicture`. | `chaosx.nr31.2` now selects exact report art from the incident that actually occurred. |
| Four large and four miniature faction emblems were unregistered and unconsumed. | Registered vanilla-layout sprites and replaced deprecated faction creation with faction-template creation carrying the exact Event 31 icon. | Regional, transnational, jihadist, and terminal faction transactions now name their exact icon consumers. |
| Twenty-nine cosmetic flag identities were unreachable. | Added separate deterministic ordinary, transnational, and jihadist identity cycles and assigned all eight dormant carrier identities during cleanup. | Sixteen ordinary, four transnational, eight jihadist, eight dormant, and one final identity all have live routes without weighted logic. |
| The terminal actor could retain an old faction and never consume the Final Jihad command emblem. | The terminal transaction now safely leaves or dismantles the prior faction before creating the Final Command, after which recorded subordinates are re-added by the existing multiplayer-safe loop. | `random_terror_finalize_false_revelation` and its faction helper. |
| The entity animation handoff named the shared Event Details property but did not add Event 31 to its selector. | Added all five Event 31 evolution portraits to `GetEventsLogSelectedEvolutionPortrait`; Evolution V consumes the ten-frame sprite and the final character consumes the explicit static-fallback sprite. | Shared Event Details remains unchanged in layout and now resolves both final consumers. |
| Four legitimate asset paths each had one redundant alias definition. | Removed the three unconsumed category-picture aliases and the unconsumed legacy entity alias after consumer search. | The Event 31 GFX registry now has 307 sprite paths and 307 unique paths. |

## Mandatory route evidence and blockers

| Route | Result |
| --- | --- |
| Focus inspect, render, and raster | The parent repaired the isolated `random_terror_mass_defection` node by restoring its intended prerequisite on `random_terror_foreign_fighters`. Post-change inspect and structural render cover all 114 focuses at 8,752x3,136 with 104 connectors, zero crossings, zero node intersections, and zero same-row spacing violations. The post-change high-fidelity raster retry failed with the exact MCP blocker `timed out awaiting tools/call after 180s`; the earlier pre-fix raster remains visual evidence for the icon set, but it is not treated as post-fix topology proof. The six `add_army_experience` “missing helper” diagnostics are a tool classification defect because `add_army_experience` is a documented vanilla country effect. |
| Event inspect and render | Event inspect is available and ran against `chaosx.nr31.1`, returning no Event 31-specific blocker but only a partial full-workspace lint artifact. Event render accepted the exact Event 31 namespace selector but did not complete after more than six minutes and was terminated; the exact blocker is that the installed route still expanded into an unbounded full-workspace render instead of returning namespace-scoped evidence. A final retry remains pending after the two active asset repairs land. |
| GUI inspect/render/rewrite | Event 31 introduces no dedicated scripted GUI and the event UI worker remains explicitly excluded. Because Global Jihad is selected through the shared `chaosx_scenarios_window`, the parent ran the mandatory shared-window inspector and renderer with Event 31 selected, Random Pattern, and Maximum intensity. Both routes completed at 1920x1080 and UI scale 1; the inspector reported no missing fields. The render artifact is `chaosx_scenarios_window-full.svg`. No GUI rewrite was required because the shared layout did not change; inherited overlap/alignment diagnostics remain shared-window findings. |
| Technology inspect/render/compare | Inapplicable: Event 31 adds no technology or doctrine tree and uses compatible existing technologies. |
| Map inspect/rewrite | No declarative Event 31 map file or dedicated map GUI exists. Exact state presentation is provided through ordinary state-targeted decisions and missions, so there is no supported Event 31 map rewrite target. |

## Pending specialist evidence

- `subagent_handoffs/031_report_04_visual_repair_handoff.md` — reviewed, accepted, registered, and wired.
- `subagent_handoffs/031_decision_mission_icon_visual_repair_handoff.md`
- `subagent_handoffs/031_focus_idea_system_visual_audit_handoff.md`
- `subagent_handoffs/031_portrait_visual_audit_handoff.md`
- `subagent_handoffs/031_flags_categories_visual_audit_handoff.md` — reviewed and integrated; its parent wiring notes are resolved by the live category consumers and deterministic cosmetic-tag cycles.

The audit remains open until every pending handoff is reviewed, the two surplus report files are removed from runtime, all final files pass reverse-consumer reconciliation, and the post-change MCP and source audits are complete.
