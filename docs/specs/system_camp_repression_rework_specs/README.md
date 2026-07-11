# Camp, Repression, and Atrocity Consequences Rework Package

This package is the accepted design source for the implemented Chaos Redux rework of the existing camp, forced-labor, gulag, atrocity, discovery, Deaths, condemnation, and Mengele-linked systems.

The package is written as a system rework rather than a single random-event spec because the requested scope crosses buildings, decisions, country AI, Germany's Mengele chain, Japan's biowarfare chain, Soviet paranoia and collapse mechanics, colonial country packages, the Chaos Meter Deaths tab, condemnation, discovery, assets, localisation direction, and implementation prompts.

## Safety and design boundary

The rework does not include player-operated target selectors by protected class. Mechanical target pools are territorial, legal, and political gameplay pools: occupied states, non-core states, colonial subjects, state repression pools, prison-labor pools, opposition-pressure pools, and borderland or periphery state groups. Historical persecution can be represented through route context, evidence, condemnation, and aftermath, but the player does not receive a target menu for a protected group.

The rework treats radicalized extermination-site escalation as an atrocity liability and collapse driver. It can raise extremist hardliner pressure and racial-policy radicalization for regimes that already pursue those routes, but its main consequences are population loss, stability damage, resistance, supply strain, institutional corruption, discovery catastrophe, tribunal severity, internal revolt risk, and world-threat escalation.

Restricted contaminated-site escalation is implemented through abstract capability and stockpile tiers. The internal resolver retains the accepted `camp_chemical_killing_efficiency` and `camp_biological_killing_efficiency` variable names, but the playable contract is restricted-method severity, recurring stockpile and logistics cost, a single Deaths path, contamination or outbreak risk, evidence, instability, discovery, and tribunal pressure. The implementation contains no recipes, dosage, delivery procedure, protected-class selector, or operational targeting guidance.

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

## Current implementation baseline

The live system keeps the existing `concentration_camp`, `extermination_camp`, and `gulag_labor_camp_network` buildings. It adds the shared lifecycle in `common/scripted_effects/camp_repression_rework_effects.txt`, the unified player action bus in `common/scripted_effects/camp_repression_action_dispatcher_effects.txt`, and the country packages in the major and colonial decision, effect, and idea files.

The reconciled implementation contains **84 player actions**: 29 major-country actions, 43 colonial-country actions, and 12 generic actions. It also contains **41 missions** and four separate Repression Ledger controls for show, hide, open, and close. France refugee aid is live as `fr_support_refugee_and_rescue_networks`, Belgium strike negotiation as `bel_negotiate_colonial_strike_settlement`, and generic site inspection as `generic_inspect_active_site`. Italy includes both `ita_authorize_homeland_emergency_detention` and `ita_expand_desert_transport_guard`.

The monthly lifecycle runs through the connected active-country and active-state arrays. Population harm reduces real state population and enters the Chaos Meter Deaths pipeline. Each active site stores the responsible country, and discovery or condemnation follows the stored authority and accumulated evidence rather than blaming the discoverer or current controller. Germany, Japan, the Soviet Union, the U.K./Raj, the U.S.A., France/Vichy, Italy, Belgium/Congo, and generic users have live country packages.

Restricted methods remain abstract strategic tiers. Chemical capacity covers chlorine, phosgene, mustard, lewisite, tabun, sarin, and soman; biological capacity covers anthrax, tularemia, plague, and smallpox. These tiers use capability, stockpile, Deaths, contamination or outbreak, evidence, discovery, instability, and tribunal outcomes without operational recipes or protected-class targeting.

The Repression Ledger has five live tabs: Overview, State Pools, Active Sites, Country System, and Discovery & Reform. Its header shows `[ROOT.GetName]: [GetCampCountryPanelName]` plus phase and discovery state. Direct and subject-controlled state actions use the same `camp_rework_action_state_id` pointer and country dispatcher; all 32 Ledger country action slots mirror their normal decision cooldown gates.

The Ledger's maintained presentation is a static ImageGen-based package with **24 derived DDS sprites**, all with live consumers. The evidence and reform seals use scripted visibility. Its frozen generated sources live in `docs/assets/system_camp_repression_rework/source/ui_imagegen/`, prompts live in `docs/assets/system_camp_repression_rework/prompts/repression_ledger_imagegen_prompts.md`, and the deterministic processor is `docs/assets/system_camp_repression_rework/tools/build_ledger_ui_assets.py`. The live Ledger is not a fallback or simple-shape substitute. Optional authored frame animation remains queued as an enhancement.

Super-event slots `12`, `74`, `75`, `76`, and `77` have final text, unique images, unique audio IDs `45`, `44`, `46`, `47`, and `48`, and live settings-aware playback. The required static UI, icon, report, news, super-event, project, and achievement assets are wired. Optional Ledger animation remains queued behind the maintained live static presentation.

Achievements `60` through `69` are live with localisation and their required icon variants. Germany's focus reward lifecycle is consolidated into at most three stable lane spirits before the capstone and exactly one final world-order spirit after convergence. The core final variant preserves the exact science-and-force totals; stage-specific variants preserve the exact additions from reclamation, continental dominance, the command spine, or full world dominance according to the highest completed optional territorial stage. No new command prerequisite was added.

The event catalog workbook remains `docs/spreadsheets/chaos_redux_events_catalog.xlsx`. This is a system rework rather than a new isolated random-event identity. The existing Soviet Collapse `Events!C6` Details cell matches the live Event Details text.

## Completion status

The shared runtime, all 84 player actions, 41 missions, four Ledger controls, country packages, Ledger, presentation assets, achievements, super-events, audio, localisation, and workbook alignment are implemented. The final decision-and-mission audit passed; its evidence is in `docs/plans/system_camp_repression_rework_plans/subagent_handoffs/decision_mission_final_audit_2026-07-11.md`. `docs/plans/system_camp_repression_rework_plans/source_of_truth_and_completion_tracker.md` records the final live identifiers and `completion_report.md` records the remaining validation boundary.

All 15 Part 7 and cross-cutting static scenario contracts were traced with zero failures. This was code-and-asset readback, not engine-runtime scenario execution. No in-game scenario run occurred in this environment, so runtime timing, rendered GUI behavior, AI choice, and numeric deltas remain an explicit validation gap for the parent completion review. The evidence and limitation are recorded in `docs/plans/system_camp_repression_rework_plans/scenario_contract_validation_report.md`.

No fallback or unapproved simplification was used. Optional Ledger frame animation remains explicitly queued and is not a blocker for the maintained static presentation.
