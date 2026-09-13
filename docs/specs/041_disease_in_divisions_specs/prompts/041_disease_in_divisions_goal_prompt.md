# Event 41 implementation goal

Implement Event 41, Disease in Divisions, to the full source specification at `docs/specs/041_disease_in_divisions_specs/`. Read every file in the pack before editing.

Follow `AGENTS.md` and the event, decision, asset, improvement-loop, and subagent skills. Consult the required offline wiki and vanilla documentation. Use the HOI4 MCP event tools and the probability workflow.

Pass or fail requirements:

1. Keep Event 41 Minor Repeatable, Chaos level 1, and a Low member of Cluster 8. Root event is `chaosx.nr41.1`. Select one valid ordinary country at war with a proven active front. Exclude special Chaos countries through the shared classifier and fail closed on invalid targets.

2. Expose only Army Infection Pressure as a persistent player-managed value. Implement bounded weekly processing for active countries and affected sectors or formations, three hidden profiles, trend and cause text, map and formation status, and milestone reports. Do not add a whole-world daily scan.

3. Implement real military sickness accounting. Separate active sick, convalescent, returned, and fatal cases. Do not delete equipment for illness or count recoverable soldiers as deaths. Register fatal cases once as military casualties in the shared Deaths system and reconcile every manpower transaction. Failed management must be able to reduce the worst infected front toward half effective strength over time without routinely halving the entire army.

4. Implement the complete phased decision category and rotation mission. Show three to five relevant actions per phase and no more than one active rotation mission. Use concrete dynamic costs with no more than four spendable types per action. Fight Through the Outbreak preserves operational freedom and worsens disease without granting free combat power.

5. Implement active-event and pre-fire entry for both evolutions. Camp Fever Across the Trenches at 200+ Chaos adds proven military-network and cross-front transmission. War Plague at 600+ adds distant military routes and a proof-carrying handoff to the existing civilian outbreak owner. Evolution activation gives zero Chaos. Do not reset episodes, duplicate categories, create a second civilian ledger, or double-count civilian deaths or Air Cleanliness.

6. Implement every row in the Chaos impact map with generation guards, caps, reversals, and shared-source exclusions. Do not duplicate Chaos from war, deaths, contamination, unconventional weapon use, or cluster firing.

7. Implement the AI matrix and named probability scenarios. Run `chaosx_ai_probability_auditor` before weighted changes and after them with `hoi4.probability_compare`. Prove that AI choices change with pressure, front threat, supply, transport, medical capacity, allied exposure, civilian risk, and demobilization.

8. Produce and wire every required report, category, decision, status, aftermath, and achievement asset through the asset prompt. Use separate source art for separate UI families, native transparency for alpha-backed assets, final DDS files, manifests, and runtime crosswalks. Implement all four achievements with full tracking and disqualifiers.

9. Complete Event Logs, Event Details, evolution rows, cluster behavior, Chaos History, final localisation, permanent documentation, canonical XLSX updates, and CSV export. Keep player text aligned across all surfaces.

Use context-complete `fork_context=false` prompts for the specialists in the handoff. Near completion, spawn `chaosx_improvement_loop_planner`, resolve its result, then run `chaosx_event_completion_auditor` on the final state.

Keep iterating until every acceptance criterion is satisfied. Do not use an unapproved fallback, omit a mapped surface, or claim completion from partial work. Finish with a concrete report covering evidence, assets, audits, catalog alignment, and every blocker or simplification.
