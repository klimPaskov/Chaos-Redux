# Camp repression rework final handoff

Resume the Chaos Redux `system_camp_repression_rework` package in the live repository.

## Read first

- `AGENTS.md`
- `docs/plans/system_camp_repression_rework_plans/source_of_truth_and_completion_tracker.md`
- `docs/plans/system_camp_repression_rework_plans/completion_report.md`
- `docs/plans/system_camp_repression_rework_plans/scenario_contract_validation_report.md`
- `docs/plans/system_camp_repression_rework_plans/subagent_handoffs/decision_mission_final_audit_2026-07-11.md`
- `docs/specs/system_camp_repression_rework_specs/README.md`
- `docs/specs/system_camp_repression_rework_specs/specs/system_camp_repression_rework_spec_part_7_implementation_checklist_validation.md`
- the relevant validation skill if engine-runtime scenario execution becomes available

## Current live state

- The shared lifecycle, registered-state monthly processing, Deaths integration, responsibility, discovery, cleanup, and Ledger display cache are implemented.
- Player actions route through `camp_rework_route_country_specific_action` and use `camp_rework_action_state_id` for state targets.
- The final decision inventory is 29 major-country actions, 43 colonial-country actions, and 12 generic actions, for 84 total player actions. The three closing IDs are `fr_support_refugee_and_rescue_networks`, `bel_negotiate_colonial_strike_settlement`, and `generic_inspect_active_site`.
- The decision files also contain 41 missions. Ledger show, hide, open, and close are four separate controls. The final decision-and-mission re-audit passed after the bounded cooldown-parity correction; all 32 Ledger country action slots now use their native decision cooldown gates.
- Italy includes `ita_authorize_homeland_emergency_detention` and `ita_expand_desert_transport_guard`.
- France uses `is_france_camp_legacy_pool_state`, `is_france_north_africa_labor_pool_state`, `is_france_vichy_internment_pool_state`, `is_france_other_colonial_labor_pool_state`, and `is_france_core_fallback_pool_state`.
- Italy uses `is_italy_libya_repression_pool_state`, `is_italy_east_africa_repression_pool_state`, `is_italy_balkan_occupation_pool_state`, `is_italy_colonial_project_pool_state`, and `is_italy_core_fallback_pool_state`.
- Fixed country packages cannot inherit the generic restricted-method route. Germany, Japan, the Soviet Union, and the colonial packages use their explicit live gates and matching stockpile checks.
- The restricted-method tiers are abstract: chlorine, phosgene, mustard, lewisite, tabun, sarin, and soman for chemical capacity; anthrax, tularemia, plague, and smallpox for biological capacity.
- The connected monthly arrays reduce real state population through the Deaths pipeline. Stored responsibility and accumulated evidence control discovery and condemnation.
- The Repression Ledger has five tabs: Overview, State Pools, Active Sites, Country System, and Discovery & Reform. Its header displays `[ROOT.GetName]: [GetCampCountryPanelName]` plus phase and discovery state.
- The maintained Ledger presentation is built from 24 derived DDS sprites sourced from frozen ImageGen files in `docs/assets/system_camp_repression_rework/source/ui_imagegen/`. All 24 have live consumers, including scripted visibility for evidence and reform seals. Prompts are in `docs/assets/system_camp_repression_rework/prompts/repression_ledger_imagegen_prompts.md`; `docs/assets/system_camp_repression_rework/tools/build_ledger_ui_assets.py` is the processor. It is not a fallback or simple-shape substitute.
- Super-event slots `12`, `74`, `75`, `76`, and `77` are wired with final art and unique audio IDs `45`, `44`, `46`, `47`, and `48`.
- Achievements `60` through `69` are wired with localisation and icon variants.
- Germany's focus reward lifecycle uses at most three stable lane spirits before convergence and exactly one final capstone spirit. The core variant preserves exact science-and-force totals; stage-specific variants preserve the exact highest completed optional territorial stage through reclamation, continental dominance, the command spine, or full world dominance. No new command prerequisite exists.
- Required static assets are live. Optional Ledger frame animation remains queued.
- The event catalog workbook is aligned through the existing Soviet Collapse row. This system rework does not create a standalone ChaosX event identity.
- All 15 Part 7 and cross-cutting scenario contracts passed static trace with zero failures. No engine-runtime scenario execution occurred in this environment.

## Remaining handoff gates

1. If an engine-runtime environment becomes available, execute the 15 recorded scenarios and append runtime results to `scenario_contract_validation_report.md`. Until then, preserve the explicit gap and do not relabel static trace as in-game execution.
2. The parent reviews the final combined repository state, including the decision/mission PASS handoff, then decides whether the documented runtime-validation gap permits the final completion claim.
3. Create the required scoped commit only after that parent review.

No accepted gameplay, localisation, asset, workbook, country-kit, mission, achievement, or super-event implementation remains queued in this handoff. Optional Ledger frame animation remains an enhancement, not a missing runtime dependency. Do not replace the live static Ledger assets with an animation fallback, fabricate engine-runtime evidence, or add a new random-event identity for this system rework.
