# Event 016 remaining private conventional Prototype decisions handoff

Disposition: implemented source wrappers under parent review. The parent subsequently reconciled the no-DLC later-stage requirements; native later-stage settlement and engine acceptance remain open.

## Owned files and identifiers

- `common/decisions/016_mengele_remaining_conventional_prototype_decisions.txt` adds `mengele_event016_electronics_prototype`, `mengele_event016_rocketry_prototype`, and `mengele_event016_high_energy_prototype` to the existing `mengele_clone_army_category`.
- `common/scripted_triggers/016_mengele_remaining_conventional_prototype_decision_triggers.txt` adds country-scope visibility, requirements, affordability, exact receipt, cancellation, and AI factory-margin predicates for those three decisions.
- `localisation/english/016_mengele_remaining_conventional_prototype_l_english.yml` adds titles, descriptions, cost displays, requirements, and effect descriptions with UTF-8 BOM.
- This handoff is the fourth owned file. No existing decision, trigger, stage core, category, spreadsheet, or project file was edited, staged, or committed.

## Private stage contract

The accepted `016_final_mengele_portfolio_closure_plan_2026-09-02.md` maps Electronics to family 2 and receipt index 1, Rocketry to family 4 and index 3, and High Energy to family 5 and index 4. The shared private stage core already quotes their fallback Prototype costs and durations, settles direct political power, support equipment, and fuel, and records the private Prototype flag and dynamic modifier. It does not award the operational package at Prototype; the later Deployment branch owns that package. The new decisions use literal family and Prototype selectors for each `brilliant_scientist_mengele_begin_project_stage`, `brilliant_scientist_mengele_cancel_project_stage`, and `brilliant_scientist_mengele_finish_project_stage` callback. An invalid or failed finish cannot call a separate output effect from these wrappers.

| Family | Native Prototype mapping with Götterdämmerung | Paid fallback quote without DLC | Duration | Existing sprite |
| --- | --- | --- | --- | --- |
| Electronics | `sp_air_radar` | 2 civilian factories, 68 political power, 250 support equipment, 250 fuel | 210 days | `GFX_decision_brilliant_scientist_project_electronics_guidance_prototype` |
| Rocketry | `sp_rockets_flying_bomb` or `sp_air_jet_engine` | 3 civilian factories, 75 political power, 275 support equipment, 750 fuel | 270 days | `GFX_decision_brilliant_scientist_project_rocketry_propulsion_prototype` |
| High Energy | `sp_nuclear_reactor` | 3 civilian factories, 90 political power, 250 support equipment, 400 fuel | 360 days | `GFX_decision_brilliant_scientist_project_high_energy_physics_prototype` |

The local `@` mirrors exist only for `civilian_factory_use` and `ai_hint_pp_cost`, whose decision fields do not accept the shared `constant:` tokens in the existing pattern. The payment predicates and localisation read the shared fallback constants. The three direct payment axes are owned by the private begin/cancel/finish core; timed decision modifiers reserve and release civilian factories. Visibility requires provider authority, empty family receipt, private Theory completion, unfinished Prototype, and no Götterdämmerung. The mapped native completion is also excluded. Each cancellation checks only provider authority and the exact active private Prototype receipt, so later resource depletion does not cancel paid work.

The AI weights match the accepted Kruger parity values: `brilliant_scientist_project_board.ai_high`, the preferred war factor, and `brilliant_scientist_project_ai.cautious_factor` when the private provider has only the quoted civilian factory margin. No Kruger capacity or receipt is read.

## Source and MCP evidence

Read the eleven required offline wiki pages, installed vanilla decision and script-constant documentation, and a vanilla decision precedent in `common/decisions/GER.txt`. Consulted `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`, the Materials and Biomedical no-DLC Prototype rows, the private stage core, family and quote constants, and the existing sprite definitions. Source validation checked three unique IDs absent from the existing conventional decision file, family IDs and receipt indices, exact native project tokens, four quote axes, duration keys, icons, callback counts, localisation coverage and BOM, and balanced script blocks.

Read-only HOI4 MCP `hoi4.probability_inspect` found all three weighted rows at source revision `31110ddfa07bf482d51f98e856406092b08658e2918f4ac2406201e765eec789`. The installed inspector classified these timed decisions under `mission_ai_will_do`; `decision_ai_will_do` reported no candidates. An explicit two-scenario evaluation returned `PROBABILITY_ANALYZED_PARTIAL`, analysis ID `probability-fbda83d83930b625f21d515a`, scenario hash `9397bd5d9e76cfc191a8d6aa16b8ae4c9143686878320a570537de60c287b4df`, and six unresolved candidate-scenario results. This does not establish numerical balance. The parent owns scenario completion, baseline and compare under the same named scenarios, and final MCP review. No live engine or HOI4 process was used.

MCP continuation resources: inspection `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c207afce76f84b3bd27e72c498b2c59e4d842aa3a994fe7d58cb748ba4acf15e/083b639298a963fceb5d281fbdf13d5983a32816fdf9712ba7bbfad19c1f3176/probability-inspect-424773a79edd.json`; partial evaluation `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d4b308dfa842ede3b383fab5176d89c55ee672e6c796426ff9b036452fad51b5/80d854cadf7822cf6c64991a37dc14e42d3a450fdbfbc4b201374f271a761275/probability-fbda83d83930b625f21d515a.json`.

## Blockers and parent follow-up

The worker identified that the existing Deployment requirements still required native special-project completion in the no-DLC route. Parent review added explicit no-DLC alternatives to the Electronics, Rocketry, and High Energy Deployment requirements in `common/scripted_triggers/016_mengele_conventional_stage_decision_triggers.txt`, plus the Electronics Weaponization radar requirement, and aligned the four requirement tooltips in `localisation/english/016_mengele_conventional_stage_decisions_l_english.yml`. With the DLC, the native requirements remain in force; without it, the paid provider stage follows the private predecessor, military-factory and resource gates, and direct cost. Native later-stage settlement in the DLC route remains a separate unresolved acceptance surface.

The parent should also verify native timer/factory reservation ordering, same-family cleanup timing, and the private Prototype receipt and modifier in its engine review. No substitute native completion, duplicate Deployment decision, or early operational package was introduced.

Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`. No skill was created or updated.
