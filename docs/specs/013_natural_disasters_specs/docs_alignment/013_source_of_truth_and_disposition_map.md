# Event 013 Natural Disasters, source-of-truth and disposition map

> Implementation disposition, 2026-07-10: the accepted package mapped below has been implemented as the fresh Event 013 system.
> Current live-file, audit, asset, and validation evidence is indexed by `docs/events/013_natural_disasters/overview.md` and `docs/plans/013_natural_disasters_plans/`.
> The spec audit of 2026-10-10 merged the superseded build prompts into `prompts/natural_disasters_implementation_resume_prompt.md` and updated this map; see the README changelog.

This map says which files own the accepted design, which files are historical build contracts, and which boundaries stay binding.

## Current source-of-truth set

| Surface | Accepted source file or files | Use |
| --- | --- | --- |
| Core event identity | `specs/013_natural_disasters_spec_part_1_core.md` | Fresh Minor Repeatable disaster container with one Event 013 history row per accepted call. |
| Reusable dynamic disaster system | `specs/013_natural_disasters_spec_part_2_reusable_system.md`, `matrices/013_disaster_call_contract.md` | Call contract intent and the dated acceptances for reports, news and the recovery bill, which supersede older prose in every part. |
| Disaster families | `specs/013_natural_disasters_spec_part_3_disaster_family_playbooks.md`, `specs/013_natural_disasters_spec_part_8_deep_family_minispecs.md` | Part 8 is the stronger source when a family appears in both files; Part 3 is the compact catalogue. |
| Aftermath and normal recovery | `specs/013_natural_disasters_spec_part_4_aftermath_decisions_ui.md`, `specs/013_natural_disasters_spec_part_10_recovery_decision_mission_map.md`, `matrices/013_aftershock_and_aftermath_matrix.md` | Aftermath cards, staged recovery, caps, partial success, chain prevention and foreign relief. |
| Evolutions, cluster and scenario | `specs/013_natural_disasters_spec_part_5_evolutions_clusters_scenarios.md` | Baseline and the three evolutions, Event 013's role in cluster 5, and Disaster Barrage. Cluster membership itself belongs to the shared cluster system in `docs/systems/event_system/event_clusters.md`. |
| Abnormal disaster GUI | `specs/013_natural_disasters_spec_part_9_abnormal_scripted_gui_map.md`, `diagrams/013_abnormal_gui_state_flow.mmd`, `diagrams/013_abnormal_gui_player_flow.mmd` | Only for Evolution III and Maximum Disaster Barrage abnormal paths. |
| Presentation and assets | `specs/013_natural_disasters_spec_part_6_presentation_assets_super_events.md` | Asset and super-event direction; live registrations are authoritative for delivered files. |
| Super-event research | `matrices/013_super_event_research_handoff_matrix.md`, `docs/super_events/013_natural_disasters/` | The six researched presentations use the shared general super-event system and are not Event 013 GUI surfaces. |
| AI, balance, and acceptance | `specs/013_natural_disasters_spec_part_7_ai_balance_acceptance.md`, `implementation_readiness/013_validation_scenario_matrix.md` | Acceptance criteria and live acceptance scenarios. |
| Docs and catalog alignment | `docs_alignment/013_catalog_and_docs_alignment.md`, this file | Edit the workbook only from final in-game wording. |
| Shared-system hooks and open proposals | `README.md` | Verified Deaths, Famine, Air Cleanliness and cross-event hooks, plus the proposals awaiting an owner decision. |

## Historical build contracts and support material

| File | Disposition | How to use it |
| --- | --- | --- |
| `prompts/natural_disasters_implementation_resume_prompt.md` | Current resume brief. | Read before any continuation; it carries the binding rules once. |
| `prompts/natural_disasters_asset_prompt.md`, `prompts/natural_disasters_super_event_prompt.md`, `prompts/natural_disasters_achievement_prompt.md`, `prompts/natural_disasters_decision_mission_prompt.md` | Historical build contracts, executed. | Use only to understand original intent for a bounded repair. |
| `implementation_readiness/013_acceptance_gate_matrix.md`, `implementation_readiness/013_source_to_file_surface_map.md`, `matrices/013_implementation_readiness_ledger.md` | Historical build contracts. | Traceability only; Part 7 and the event overview replace them. |
| Coding, goal, subagent-routing and continuation prompts; closure resume packet; final next-agent prompt; dependency-order plan; simplification blocklist | Superseded and removed (continuation prompt earlier, the rest on 2026-10-10). | Their rules live in the resume brief, this map, Part 7 and CLAUDE.md; git history keeps the originals. |
| `research/003_manual_improvement_loop_pass.md`, `research/004_final_improvement_loop_anti_bloat_closure.md`, `research/008_closure_followup_final_readiness_pass.md` | Historical closure records. | The rejected-expansion list in 004 remains a binding constraint and is restated below. |
| `research/000_source_reading_log.md`, `research/006_second_pass_source_reading_log.md`, `research/008_third_pass_closure_alignment_log.md`, `research/007_second_pass_validation_notes.md`, `research/009_third_pass_validation_notes.md` | Provenance of the original planning environment. | Unchanged evidence; their file inventories describe the package as it was then. |
| Public research notes (`research/002`, `research/005`) | Support evidence only. | They ground hazard grouping, warnings, vulnerability and recovery; they are not localisation. |

## Accepted negative boundaries

These boundaries are part of the source design and should not be relaxed.

| Boundary | Required handling |
| --- | --- |
| Old Natural Disasters logic | Do not restore or patch it. |
| Old Earth Earthquake logic | Do not reuse it. Event 046 remains an inactive placeholder. Whole-earth rupture belongs inside Event 013 Evolution III. |
| Event 099 | A narrow bridge into the Event 013 dust and sandstorm family through `call_natural_disaster`. No second sandstorm system. |
| Event 051 Heat Wave | Keep separate. Event 013 heat must not stack with Event 051. |
| Generic institution framing | Event 013 never reads as an official disaster office, bureau, agency, or generic announcer. |
| Planning labels in localisation | Working labels and direction notes are never pasted as player-facing text. |
| Super-event wording and audio | Final titles, remarks, quotes, slogans, lyric fragments, cultural references, and audio come only from the research workflow. |
| Normal disaster GUI sprawl | No separate custom map GUI for normal families; compact aftermath cards are enough outside abnormal cases. |
| Focus trees and new relief tags | No disaster-recovery focus trees or relief countries unless the user asks for a new event beyond Event 013. |
| Family-level super-events and world end | Super-events stay reserved for the six abnormal milestones, and Event 013 stays non-terminal. |
