# Camp, Repression, and Atrocity Consequences Rework Planning Package

This package is a planning handoff for a large Chaos Redux rework of the existing camp, forced-labor, gulag, atrocity, discovery, Deaths, condemnation, and Mengele-linked systems.

The package is written as a system rework rather than a single random-event spec because the requested scope crosses buildings, decisions, country AI, Germany's Mengele chain, Japan's biowarfare chain, Soviet paranoia and collapse mechanics, colonial country packages, the Chaos Meter Deaths tab, condemnation, discovery, assets, localisation direction, and implementation prompts.

## Safety and design boundary

The rework does not include player-operated target selectors by protected class and does not include mechanics that optimize chemical or biological killing. Mechanical target pools are territorial, legal, and political gameplay pools: occupied states, non-core states, colonial subjects, state repression pools, prison-labor pools, opposition-pressure pools, and borderland or periphery state groups. Historical persecution can be represented through route context, evidence, condemnation, and aftermath, but the player should not receive a target menu for a protected group.

The rework treats radicalized extermination-site escalation as an atrocity liability and collapse driver. It can raise extremist hardliner pressure and racial-policy radicalization for regimes that already pursue those routes, but its main consequences are population loss, stability damage, resistance, supply strain, institutional corruption, discovery catastrophe, tribunal severity, internal revolt risk, and world-threat escalation.

Restricted contaminated-site escalation is designed as contaminated evidence and consequence pressure. It consumes stockpiles, creates immediate and monthly harm, raises evidence depth, and worsens discovery and postwar consequences. It is not an efficiency upgrade.

## Package contents

- `source_review/read_files_manifest.md` records uploaded source files and package files read during planning.
- `research/historical_anchor_notes.md` records initial historical anchors and how they should be used as design inspiration.
- `research/continuation_historical_sources.md` records continuation-pass source anchors for U.K./Raj, U.S.A., France/Vichy/North Africa, Italy/Libya, Belgium/Congo, and generic routes.
- `specs/system_camp_repression_rework_spec_part_1_core_loop.md` defines the shared loop.
- `specs/system_camp_repression_rework_spec_part_2_country_systems_major_powers.md` maps the country systems.
- `specs/system_camp_repression_rework_spec_part_3_germany_japan_soviet_deepening.md` expands the deep Germany, Japan, and Soviet packages.
- `specs/system_camp_repression_rework_spec_part_4_ui_ai_assets_acceptance.md` maps UI, AI, assets, achievements, and acceptance criteria.
- `specs/system_camp_repression_rework_spec_part_5_country_decision_kits_focus_hooks.md` details U.K./Raj, U.S.A., France/Vichy/North Africa, Italy/Libya, Belgium/Congo, and generic decision kits with focus hooks.
- `specs/system_camp_repression_rework_spec_part_6_scripted_gui_wireframe_value_display.md` defines the Repression Ledger wireframe and exact value display plan.
- `specs/system_camp_repression_rework_spec_part_7_implementation_checklist_validation.md` lists implementation surfaces, touched files, validation commands, and scenario checks.
- `matrices/country_ai_matrix.md` gives an AI behavior matrix.
- `matrices/decision_mission_matrix.md` gives a decision and mission family matrix.
- `matrices/values_and_pressure_model.md` gives values, pressure models, and state pools.
- `matrices/country_decision_kits_matrix.md` summarizes the Part 5 country kits, decision families, mission bands, and discovery routes.
- `prompts/` contains goal, implementation, decision, GUI, validation, asset, super-event, and achievement prompts.
- `continuation/continuation_prompt.md` preserves the final planning handoff and next implementation entry point.

## Current source baseline

The uploaded `genocide_crisis_system.md` describes a system with concentration camps, extermination camps, and gulag labor camp networks, internal harm before discovery, state population loss through the Deaths pipeline, and discovery-based condemnation. This package builds on that implementation rather than replacing it with a new isolated event.

The uploaded `germany_mengele.md` describes a Germany-specific Auschwitz and Mengele chain with `mengele_autonomy`, `mengele_permission_level`, Auschwitz state `88`, biowarfare facilities, cloning project unlocks, and the Angel of Death Directorate coup path. This package uses those variables and hooks as the Germany integration spine.

The uploaded `chaos_meter_deaths_mechanic.md` describes the global Deaths tab and real state-population loss pipeline. This package routes all population damage through that existing system.

## Continuation status

The requested continuation sections are complete. Part 5 now provides detailed country decision kits and focus hooks. Part 6 provides the scripted GUI wireframe and exact value display plan. Part 7 provides the implementation checklist, touched files, validation commands, and scenario checks.

No required planning section remains from the continuation prompt. The next clean step is implementation against the live Chaos Redux repository, followed by targeted decision, focus, localisation, country package, GUI, asset, and completion audits.
