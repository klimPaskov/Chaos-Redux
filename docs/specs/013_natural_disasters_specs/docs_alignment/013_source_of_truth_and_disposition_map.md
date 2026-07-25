# Event 013 Natural Disasters, source-of-truth and disposition map

> Implementation disposition, 2026-07-10: the accepted package mapped below has been implemented as the fresh Event 013 system. The original completion stance at the end of this planning document describes the pre-implementation snapshot. Current live-file, audit, asset, and validation evidence is indexed by `docs/events/013_natural_disasters.md` and `docs/plans/013_natural_disasters_plans/013_implementation_validation_notes.md`.

This file is a closure follow-up for the expanded second-pass package. It does not add new disaster mechanics. It tells the implementation agent which files now own the accepted design, which files are support material, and which working prompts are superseded.

## Current source-of-truth set

| Surface | Accepted source file or files | Implementation use |
| --- | --- | --- |
| Core event identity | `specs/013_natural_disasters_spec_part_1_core.md` | Treat Event 013 as a fresh Minor Repeatable disaster container. Preserve one Event 013 history row per Event 013 firing even when many delayed impacts occur. |
| Reusable dynamic disaster system | `specs/013_natural_disasters_spec_part_2_reusable_system.md`, `matrices/013_disaster_call_contract.md` | Build the public call contract first. Other events must be able to call families, targets, severity, reports, news, aftermath, chains, and scaling overrides without copying disaster logic. |
| Disaster families | `specs/013_natural_disasters_spec_part_3_disaster_family_playbooks.md`, `specs/013_natural_disasters_spec_part_8_deep_family_minispecs.md` | Use the deep family mini-spec as the stronger source when a family appears in both files. Part 3 remains the compact catalogue. |
| Aftermath and normal recovery | `specs/013_natural_disasters_spec_part_4_aftermath_decisions_ui.md`, `specs/013_natural_disasters_spec_part_10_recovery_decision_mission_map.md`, `matrices/013_aftershock_and_aftermath_matrix.md` | Build visible aftermath notifications, compact cards, recovery decisions, active mission caps, partial success, chain prevention, and foreign relief from these files. |
| Evolutions and cluster behavior | `specs/013_natural_disasters_spec_part_5_evolutions_clusters_scenarios.md` | Preserve baseline, Evolution I, Evolution II, and Evolution III design. Keep the Natural Disasters cluster as Event 013 only at this stage. |
| Abnormal disaster GUI | `specs/013_natural_disasters_spec_part_9_abnormal_scripted_gui_map.md`, `diagrams/013_abnormal_gui_state_flow.mmd`, `diagrams/013_abnormal_gui_player_flow.mmd` | Use the scripted GUI only for Evolution III abnormal and manual barrage variants. Use state-driven cards, path previews, frame-sheet animations, and static fallbacks. |
| Presentation and assets | `specs/013_natural_disasters_spec_part_6_presentation_assets_super_events.md`, `prompts/natural_disasters_asset_prompt.md` | Use these as asset direction. Actual visual production belongs to the asset subagents and frame-animation workflow. |
| Super-event research | `matrices/013_super_event_research_handoff_matrix.md`, `prompts/natural_disasters_super_event_prompt.md`, `docs/super_events/013_natural_disasters_super_event_text_research.md`, `docs/super_events/013_natural_disasters_super_event_audio_production.md` | The six researched presentations are documented and registered through the shared general super-event system. They are not direct Event 013 disaster-window UI; do not wire them into the Event 013 scripted GUI. |
| AI, balance, and acceptance | `specs/013_natural_disasters_spec_part_7_ai_balance_acceptance.md`, `matrices/013_implementation_readiness_ledger.md` | Use both as completion gates. The readiness ledger is a traceability aid, not a replacement for Part 7. |
| Docs and catalog alignment | `docs_alignment/013_catalog_and_docs_alignment.md`, this file | Use only after implementation creates final in-game wording. Do not write final spreadsheet text from working labels. |
| Closure and anti-bloat | `research/004_final_improvement_loop_anti_bloat_closure.md`, `research/008_closure_followup_final_readiness_pass.md` | Do not add broad new design unless the user explicitly asks for a specific surface. Treat rejected bloat items as constraints. |

## Superseded or support material

| File | Disposition | How to use it |
| --- | --- | --- |
| `research/003_manual_improvement_loop_pass.md` | Superseded by second-pass expansion and final closure. | Keep for history only. Do not use its remaining-depth notes as open tasks. |
| `prompts/natural_disasters_continuation_prompt.md` | Superseded and removed from the package manifest. | Use the closure and resume prompts instead; no continuation prompt is required for the accepted implementation. |
| `research/000_source_reading_log.md` | Support evidence from first pass. | Use with the second and third-pass reading notes to understand what was available. |
| `research/006_second_pass_source_reading_log.md` | Support evidence from second pass. | Use with this file and the closure follow-up when checking source coverage. |
| Public research notes | Support evidence only. | They ground hazard grouping, warnings, vulnerability, and recovery. They do not provide final localisation or final super-event quote choices. |

## Accepted negative boundaries

These boundaries are part of the source design and should not be relaxed during implementation.

| Boundary | Required handling |
| --- | --- |
| Old Natural Disasters logic | Do not preserve or patch it. Build the Event 013 system from scratch. |
| Old Earth Earthquake logic | Do not reuse it. Event 046 remains an inactive unknown placeholder. Whole-earth rupture belongs inside Event 013 Evolution III. |
| Event 099 Sandstorm | Convert to a placeholder or a narrow bridge into the Event 013 dust and sandstorm family. Do not keep a second sandstorm system. |
| Event 051 Heat Wave | Keep separate. Event 013 local heat calls must skip, bridge, or non-stack when Event 051 heat logic is active. |
| Generic institution framing | Do not make Event 013 look like an official disaster office, bureau, agency, or similar generic announcer. The player sees specific disasters in specific places. |
| Final localisation in planning files | Do not paste working labels or direction notes as final player-facing text. |
| Super-event wording and audio | Do not invent final titles, remarks, quotes, slogans, lyric fragments, cultural references, or audio choices without the research workflow. |
| Normal disaster GUI sprawl | Do not create a separate custom map GUI for every normal disaster family. Compact aftermath cards are enough outside abnormal cases. |
| Focus trees and new relief tags | Do not add broad disaster-recovery focus trees or relief countries unless the user explicitly asks for a new event beyond Event 013. |

## Read order for the coding pass

1. Read `README.md` and `manifest.md` to understand package layout.
2. Read `research/004_final_improvement_loop_anti_bloat_closure.md` and `research/008_closure_followup_final_readiness_pass.md` to avoid restarting broad planning.
3. Read `specs/013_natural_disasters_spec_part_1_core.md` and `specs/013_natural_disasters_spec_part_2_reusable_system.md` before any code design.
4. Read `matrices/013_disaster_call_contract.md` before writing helpers.
5. Read Parts 3 and 8 together for every family implementation tranche.
6. Read Parts 4 and 10 before writing decisions, missions, aftermath cards, and notifications.
7. Read Part 9 and both abnormal GUI diagrams before touching scripted GUI or animated map paths.
8. Read Part 6, the super-event matrix, and prompt files before asset, quote, remark, or audio work.
9. Read Part 7 and `matrices/013_implementation_readiness_ledger.md` before claiming any implementation surface is complete.
10. Use `docs_alignment/013_catalog_and_docs_alignment.md` only after final in-game text exists.

## Historical completion stance

This was the pre-implementation planning stance. The accepted package has since been implemented and statically audited; use `docs/plans/013_natural_disasters_plans/013_event_completion_final_audit.md` and `docs/plans/013_natural_disasters_plans/013_implementation_validation_notes.md` for current evidence. The remaining live-engine scenario matrix is an external validation gate, not an instruction to restart the implementation plan.
