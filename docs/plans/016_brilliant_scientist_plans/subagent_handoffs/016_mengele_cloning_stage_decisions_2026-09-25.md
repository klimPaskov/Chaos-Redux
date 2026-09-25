# Event 016 Mengele Cloning private stage decisions — 2026-09-25

## Scope and disposition

This is one bounded Cloning family decision slice under `docs/plans/016_brilliant_scientist_plans/016_final_mengele_portfolio_closure_plan_2026-09-02.md` and `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md`.
The four assigned files contain the decisions, family-only gates, localisation, and this handoff.
The slice does not establish complete Event 016 or native project acceptance.

## Owned files and exact identifiers

| File | Owned identifiers |
| --- | --- |
| `common/decisions/016_mengele_cloning_stage_decisions.txt` | `mengele_event016_cloning_theory`, `mengele_event016_cloning_prototype`, `mengele_event016_cloning_deployment`, and `mengele_event016_cloning_weaponization` under existing `mengele_clone_army_category`. |
| `common/scripted_triggers/016_mengele_cloning_stage_decision_triggers.txt` | The 25 `brilliant_scientist_mengele_cloning_` receipt, visibility, requirement, affordability, cancellation, and stage-specific factory-margin triggers. |
| `localisation/english/016_mengele_cloning_stage_l_english.yml` | 27 names, descriptions, compact costs, full-cost and requirement tooltips, lifecycle messages, and stage outcomes; UTF-8 BOM. |
| This handoff | Source crosswalk, native boundary, AI evidence, and open acceptance. |

The literal family selector is `constant:brilliant_scientist_project_family.cloning` (ID 8) and the private aligned receipt is `mengele_event016_active_project_stage_entries^7`.
Each begin, cancel, and finish callback sets literal Cloning and stage selectors before calling `brilliant_scientist_mengele_begin_project_stage`, `brilliant_scientist_mengele_cancel_project_stage`, or `brilliant_scientist_mengele_finish_project_stage`.
Theory, Deployment, and Weaponization remain paid in both DLC states.
The paid Prototype row appears only without `Gotterdammerung`; with the DLC, `sp_brilliant_scientist_cloning` retains its native clock, breakthrough and resource payment, and completion callback.
No decision calls the Kruger stage or capacity helpers.

## Prototype output and correction

The shared private stage core records the Cloning Prototype receipt and its modifier but does not grant the full clone programme output on that stage.
The no-DLC decision runs its extra output only after `mengele_event016_stage_finished` and `mengele_event016_project_output_applied` both equal one and `mengele_event016_cloning_prototype_completed` exists.
It invokes `germany_mengele_complete_cloning_project` only when `germany_mengele_cloning_project_completed` is absent, then calls `chaosx_grant_custom_operational_technology` with `chaosx_custom_technology_family.clone` and fixed Mengele provenance.
When `germany_master_race_claim_established` exists and the Aryan refinement technology is absent, it calls `clone_select_mengele_aryan_refinement`.
The wrapper clears its neutral API selectors and never calls `clone_select_kruger_refinement`.

This mirrors the existing `sp_mengele_cloning` output in `common/special_projects/projects/mengele_cloning_projects.txt`: its output calls `germany_mengele_complete_cloning_project` and the neutral clone API.
The completion helper in `common/scripted_effects/germany_mengele_effects.txt` records the dedicated cloning completion, enables `clone_equipment_1` production through controlled biowarfare facilities, selects the Mengele refinement, and schedules `germany_mengele.24` if the active German programme is revolt-ready.
The neutral API in `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt` grants shared clone access and, for `is_mengele_clone_directorate_country`, selects Mengele rather than Kruger refinement.
The separate Aryan helper in `common/scripted_effects/clone_system_effects.txt` enables its distinct battalion and template only when the established German claim applies.
All three paths are receipt-guarded or technology-guarded, and their existing effects are idempotent; the output remains subject to native runtime acceptance.

## Quotes, durations, and icons

| Stage | Duration | Civilian factories reserved | Direct Political Power | Direct Support Equipment | Direct fuel | Existing icon |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Theory | 210 days | 1 | 65 | 130 | 0 | `GFX_decision_brilliant_scientist_project_cloning_theory` |
| No-DLC Prototype | 330 days | 2 | 98 | 325 | 150 | `GFX_decision_brilliant_scientist_project_cloning_prototype` |
| Deployment | 480 days | 4 | 130 | 975 | 750 | `GFX_decision_brilliant_scientist_project_cloning_deployment` |
| Weaponization | 660 days | 7 | 195 | 1,950 | 2,250 | `GFX_decision_brilliant_scientist_project_cloning_weaponization` |

The duration constants are in `common/script_constants/016_brilliant_scientist_constants.txt`; payment quotes are in `common/script_constants/016_brilliant_scientist_project_constants.txt`.
Only the native `civilian_factory_use` and `ai_hint_pp_cost` fields have file-scoped aliases, because they reject the shared `constant:` tokens here.
Actual affordability, three direct debits and refunds, and the decision timer remain backed by shared constants and private receipt effects.
The four icon definitions are in `interface/016_brilliant_scientist_project_icons.gfx`; their DDS files exist under `gfx/interface/decisions/016_brilliant_scientist/projects/`.

## AI source crosswalk and MCP evidence

| Private stage | Kruger source decision | Base | War factor | Cautious factor | Private no-spare trigger and exact CIC quote |
| --- | --- | --- | --- | --- | --- |
| Theory | `brilliant_scientist_advance_cloning_theory` | `brilliant_scientist_project_board.ai_medium` | `brilliant_scientist_project_ai.preferred_factor` | `brilliant_scientist_project_ai.cautious_factor` | `brilliant_scientist_mengele_cloning_theory_decision_no_spare_factories`; 1 |
| No-DLC Prototype | `brilliant_scientist_fallback_cloning_prototype` | `brilliant_scientist_project_board.ai_high` | same | same | `brilliant_scientist_mengele_cloning_prototype_decision_no_spare_factories`; 2 |
| Deployment | `brilliant_scientist_advance_cloning_deployment` | `brilliant_scientist_project_board.ai_medium` | same | same | `brilliant_scientist_mengele_cloning_deployment_decision_no_spare_factories`; 4 |
| Weaponization | `brilliant_scientist_advance_cloning_weaponization` | `brilliant_scientist_project_board.ai_medium` | same | same | `brilliant_scientist_mengele_cloning_weaponization_decision_no_spare_factories`; 7 |

Kruger applies the cautious factor through `brilliant_scientist_has_low_project_capacity`.
Each private cautious trigger instead checks `NOT = { num_of_civilian_factories_available_for_projects > quote }` against its own stage constant, so the cautious factor applies when available project CIC equals or falls below the exact quote.
The private base and factor constants match each corresponding Kruger Cloning row; only the low-capacity predicate is provider-specific.
The native timed rows were discovered by the connected `mission_ai_will_do` adapter: both Kruger and private `hoi4.probability_inspect` calls returned `PROBABILITY_SOURCE_INSPECTED`, four candidates, and a complete declared pool.
The Kruger inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0164bd4bef72241225c53ad6c19d87d6ec72f878b0d62e0cdcaadf4fe6ccf1fe/02758c41ac5aa901fb87f82acf41935a81a146d2e0d8ce82b67b8fb8a69fbfc0/probability-inspect-62f2b563c5e7.json`.
The private inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aa652760c95d1588db3c6bf6090c2f42d826b5578ff33651deafc4cc08cd1988/b41f2c478fe6b26f24b876a7a0d8f39f185dbd204e508643b7e745ccbdf709d1/probability-inspect-fc9981ddbce0.json`.

The named scenarios were `peace_factory_margin`, `war_factory_margin`, and `war_low_factory_margin`, all actor `MCL`, with available civilian factories 10, 10, and 4.
Separate `hoi4.probability_evaluate` runs returned `PROBABILITY_ANALYZED_PARTIAL` and eight unresolved or bounded items each: Kruger artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/610577d646648bdcb3e78fd31880769265e2860b0a611f5365fa6341824f4187/9214b979070a82e9ff78ca96d6a82014c9491d56093181992323d054edc6c9f7/probability-4618ca83ddc550dedbb781c0.json`, private artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8febf01370c1515288e853d45d808c5cc1636aa364003c4b86655fa97b275869/a8ef2e850879524551e4f4661b3c4348456203e0ce714aef2eca7e63682722f1/probability-a1db4e79884ef4058d7d8df0.json`.
The same-scenario `hoi4.probability_compare` returned `PROBABILITY_ANALYZED_PARTIAL`, 24 unresolved or bounded items, and 24 comparison changes in `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5ea0523357a9fc6712189b0e9c203d3c53b45b1c886b5c3dcda77d048a1ac8a9/a095aac96608d409e62e148627e8280d2e8b50c3863d4849f7764874a8784083/probability-e2badff51fb0613e480c82ce.json`.
The before and after candidate IDs differ, and the flat scenarios cannot bind the provider and project receipt variables, so these partial outputs are discovery and uncertainty evidence rather than demonstrated probability parity.
The parent probability auditor must review full candidate and external-factor coverage and obtain acceptance-grade comparison under matched playable states.

After the stage-specific caution refinement, `hoi4.probability_inspect` discovered all four private candidates with complete declared pool and zero discovery unresolved items at source revision `29eb8640b60096bdaf57d3ac75bfa0406dcf6e626aa6657850df964556f89dab` (`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9bae09370c4dbd455afa652126198c80c6f8e02754bb9a5b1142671311152d9b/f5c806dccfe29e63771ee25ddfdb0ec4fc035679f1d63fa12169bf9d7e82b205/probability-inspect-386fc0382e8b.json`).
An equality-boundary `hoi4.probability_evaluate` used five MCL peace scenarios with available CIC 1, 2, 4, 7, and 8; it returned `PROBABILITY_ANALYZED_PARTIAL` with eight unresolved or bounded items (`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/15b30f577d73541de23fbf98053c2a6ce95ac4b9f40e56f2631191439d535664/0ae76ecdd95b0c41093a51e323a6f000306a1f393c816a60e275934b1dae420b/probability-2c6e455f5fcf85751c577089.json`).
A same-scenario cross-source `hoi4.probability_compare` against the Kruger board returned `PROBABILITY_ANALYZED_PARTIAL` with 184 unresolved or bounded items and 625 reported changes because the broad Kruger board and private candidate sets differ (`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/11478eb13bb26fff63207204131632d90dec22638a7378c01f462d65e5886da3/8aaa51174686c0eb1a398a1fc6c705452d9b02e23851cc501cc64b46b3ae7418/probability-45329556e7130777e4d6fa29.json`).
These new MCP results establish source discovery and disclose the scenario limit; the exact equality behavior is proven by the four source predicates and quotes, not by a complete engine probability evaluation.

## Open integration and acceptance

The mapped DLC native project is `sp_brilliant_scientist_cloning` in `common/special_projects/projects/016_brilliant_scientist_projects.txt`.
Parent integration in `common/scripted_effects/016_mengele_project_bridge_effects.txt` invokes the dedicated `germany_mengele_complete_cloning_project` after a successful authenticated native clone grant, guarded by its completion flag; the established German claim can then select the Aryan refinement if its technology is absent.
The no-DLC decision and DLC callback therefore both route through the existing dedicated clone programme, with private Theory and Prototype receipts controlling the DLC grant.
Native callback order and live clone consumer results remain unaccepted.
Parent read-only `hoi4.event_inspect` lint on `germany_mengele.24` after the bridge patch returned `EVENT_INSPECTED_PARTIAL`, source revision `f38750d657aae964fc445b75e7bd6dc5ca78a5f72ff6779d08ba080a8eaded7e`, zero blocking diagnostics, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d9a57fa195726164883d39711be26b068a392cba896dcb70fad3f6a3f8166cda/1d77c83e7f092e80eca5517cef6006b872301c53f80dfdf4e38ce78ad727347d/event-lint-f38750d657aa.json`.
The inspector deferred workspace-wide helper and lifecycle passes, so this focused event result does not prove the native project callback or its output order.
Native timed-decision callback ordering, cost display and factory reservation, clone equipment production, possible German revolt, and both DLC-state consumers have not been accepted in a live game.
No HOI4 process was launched, no shared or Xenobiological file was edited, and no Git staging or commit was performed.

## Source review

Read the eleven offline core wiki pages, the Decision and Idea Modding pages, and the Special Projects sections of the offline Trigger and Effect pages; the installed vanilla decision documentation, script-constant, effect, trigger, modifier, and localisation documentation; and the vanilla `GER.txt` timed-decision precedent.
Read `chaos-redux-decisions-missions`, `chaos-redux-events`, and `chaos-redux-subagents`, the accepted plan and spec, Kruger Cloning wrappers, the private stage core, native project and bridge, custom clone API, and existing Mengele clone programme.
Checked for existing Cloning decision IDs before writing, then checked all new decision, trigger, and localisation declarations against the existing namespaces.
