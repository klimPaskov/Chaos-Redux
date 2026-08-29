# Event 028: Asteroid Incoming

## Specification package index

This folder is the source design package for Event 028, Asteroid Incoming.

The event is a global fire-once major event. A player-controlled chooser receives three dynamically selected country and state targets plus a genuine miss option. A selected impact resolves after a two-day trajectory lock, destroys the chosen state, damages three land-adjacency rings, records civilian deaths, creates a permanent asteroid crater, produces a global dust aftermath, and presents a dynamic super-event. At higher Chaos, fragments strike additional regions and crater controllers gain transferable armour bonuses from extraordinary material.

The package treats the supplied Event 028 brief as authoritative. The current catalog export still describes an older minor repeatable prediction event. The implementation must replace that stale row in the authoritative workbook and regenerate the CSV exports.

## Files

| File | Purpose |
| --- | --- |
| `028_asteroid_incoming_spec_part_1_core.md` | Event identity, campaign role, full player flow, eligibility, and fixed design rules |
| `028_asteroid_incoming_spec_part_2_targeting_and_trajectory.md` | Dynamic target construction, impact-state choice, multiplayer ownership, trajectory lock, emergency response, and adjacency geometry |
| `028_asteroid_incoming_spec_part_3_impact_damage_and_aftermath.md` | Population loss, building destruction, crater state, Deaths integration, capital handling, country reports, and nuclear separation |
| `028_asteroid_incoming_spec_part_4_dust_and_global_recovery.md` | Atmospheric dust load, global stages, Air Cleanliness, Event 013 connections, mitigation, and decay |
| `028_asteroid_incoming_spec_part_5_evolutions.md` | Global Fragmentation and Extraordinary Minerals, fragment distribution, transfer rules, strategic value, and evolution logging |
| `028_asteroid_incoming_spec_part_6_decisions_and_missions.md` | Pre-impact response, rescue, reconstruction, dust mitigation, crater security, costs, AI use, and clutter control |
| `028_asteroid_incoming_spec_part_7_ai_multiplayer_and_balance.md` | Option logic, target preferences, probability scenarios, multiplayer behavior, anti-exploit rules, and tuning expectations |
| `028_asteroid_incoming_spec_part_8_events_logs_and_text_direction.md` | Event-chain surfaces, reports, news, Event Details, evolution views, super-event context, and writing direction |
| `028_asteroid_incoming_spec_part_9_visual_and_audio_direction.md` | Visual identity, map effects, report and news art, category presentation, icons, and audio role |
| `028_asteroid_incoming_spec_part_10_achievements_and_acceptance.md` | Achievement set, end-to-end acceptance criteria, validation scenarios, and completion proof |
| `028_asteroid_incoming_tuning_matrix.md` | Central design ranges for damage, fragments, dust stages, recovery, targeting, and mineral stacking |
| `028_asteroid_incoming_research_basis.md` | Scientific and historical research used as design support, with abstraction limits and bibliography |
| `028_asteroid_incoming_catalog_reconciliation.md` | Required authoritative workbook corrections and export alignment |
| `028_asteroid_incoming_source_crosswalk.md` | Traceability from the supplied brief to the completed specification files |
| `028_asteroid_incoming_design_review.md` | Manual multi-role review, accepted improvements, rejected bloat, and unresolved tooling limits |
| `028_asteroid_incoming_asset_prompt.md` | Bounded visual-asset production prompt |
| `028_asteroid_incoming_super_event_prompt.md` | Bounded quote, cultural remark, image, and licensed audio research prompt |
| `028_asteroid_incoming_achievement_prompt.md` | Achievement scripting, text, tracking, and icon prompt |
| `028_asteroid_incoming_decision_mission_prompt.md` | Decision and mission implementation and audit prompt |
| `028_asteroid_incoming_ai_probability_prompt.md` | Required probability and AI weighting audit scenarios |
| `028_asteroid_incoming_coding_prompt.md` | Full implementation handoff for the parent coding agent |
| `028_asteroid_incoming_goal_prompt.md` | Compact final goal prompt that points to this package |

## Design authority

The supplied Event 028 brief controls the event identity and all stated percentages, evolution effects, and presentation requirements. Research in this package supports the structure and atmosphere. It does not replace the user's values with a physical impact simulation.

All working labels in this package are structural labels. The implementation agent must research and write final player-facing localisation under the Chaos Redux writing rules.
