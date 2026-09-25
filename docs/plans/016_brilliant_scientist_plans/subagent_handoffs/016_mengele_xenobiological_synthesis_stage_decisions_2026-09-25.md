# Event 016 Mengele Xenobiological Synthesis private stage decision handoff — 2026-09-25

## Scope and disposition

This is one bounded family slice under `docs/plans/016_brilliant_scientist_plans/016_final_mengele_portfolio_closure_plan_2026-09-02.md` and `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md`.
The four assigned files contain private decision wrappers, family-specific gates, player-facing localisation, and this handoff.
Parent review added `docs/events/016_brilliant_scientist/systems/mengele_xenobiological_synthesis_stages.md` to document the lifecycle, interactions, existing sprites, and remaining acceptance work.
This handoff makes no Event 016 completion or native acceptance claim.

## Owned files and exact identifiers

| File | Identifiers |
| --- | --- |
| `common/decisions/016_mengele_xenobiological_synthesis_stage_decisions.txt` | `mengele_event016_xenobiological_synthesis_theory`, `mengele_event016_xenobiological_synthesis_prototype`, `mengele_event016_xenobiological_synthesis_deployment`, `mengele_event016_xenobiological_synthesis_weaponization` under the existing `mengele_clone_army_category`. |
| `common/scripted_triggers/016_mengele_xenobiological_synthesis_stage_decision_triggers.txt` | The `brilliant_scientist_mengele_xenobiological_synthesis_` receipt, visibility, requirements, affordability, cancellation, and private factory-margin gates. |
| `localisation/english/016_mengele_xenobiological_synthesis_stage_l_english.yml` | Four names, descriptions, compact cost strings, requirement and full-cost tooltips, common lifecycle tooltips, and four stage outcomes; UTF-8 BOM. |
| This handoff | Source checks, prices, AI crosswalk, and unresolved acceptance. |

Family selector is `constant:brilliant_scientist_project_family.xenobiological_synthesis` (ID 11); the private aligned receipt is `mengele_event016_active_project_stage_entries^10`.
All begin, cancel, and finish wrappers pass literal family and requested-stage selectors to `brilliant_scientist_mengele_begin_project_stage`, `brilliant_scientist_mengele_cancel_project_stage`, and `brilliant_scientist_mengele_finish_project_stage`.
The existing provider-validity gate and exact private predecessor receipt control the rows; no wrapper reads or writes the Kruger Capacity or board ledger.
Theory, Deployment, and Weaponization remain paid provider decisions in both DLC states.
The paid Prototype row is visible only without `Gotterdammerung`; with the DLC, native `sp_brilliant_scientist_xenobiological_synthesis` owns the Prototype clock, breakthrough and resource payment, and native completion callback.

## Native project and output boundary

`common/special_projects/projects/016_brilliant_scientist_projects.txt` defines `sp_brilliant_scientist_xenobiological_synthesis`; its project visibility points to `brilliant_scientist_can_research_mengele_xenobiological_synthesis_prototype` in `common/scripted_triggers/016_mengele_project_bridge_triggers.txt`.
`common/scripted_effects/016_mengele_project_bridge_effects.txt` grants the xenobiological operational API from an authentic native completion with private Theory and Prototype receipts.
`common/scripted_effects/016_mengele_project_stage_effects.txt` records a private Prototype receipt without granting that operational API, while its Deployment and Weaponization paths call the custom operational and weaponization upgrade APIs.
For the no-DLC Prototype, this decision wrapper grants `chaosx_custom_technology_family.xenobiological` with Mengele provenance only after private finish reports both `mengele_event016_stage_finished = one` and `mengele_event016_project_output_applied = one`, and the private Prototype flag exists.
A failed private finish cannot reach this extra grant; the wrapper clears its API selectors after use.
The public grant API is idempotent, so the later Deployment call does not duplicate an already learned operational package.

## Quote, duration, and icon crosswalk

| Stage | Duration | Native civilian-factory reservation | Direct Political Power | Direct Support Equipment | Direct fuel | Existing icon |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Theory | 240 days | 1 | 70 | 140 | 0 | `GFX_decision_brilliant_scientist_project_xenobiological_synthesis_theory` |
| No-DLC Prototype | 390 days | 2 | 105 | 350 | 250 | `GFX_decision_brilliant_scientist_project_xenobiological_synthesis_prototype` |
| Deployment | 570 days | 5 | 140 | 1,050 | 1,250 | `GFX_decision_brilliant_scientist_project_xenobiological_synthesis_deployment` |
| Weaponization | 750 days | 7 | 210 | 2,100 | 3,750 | `GFX_decision_brilliant_scientist_project_xenobiological_synthesis_weaponization` |

Durations come from `common/script_constants/016_brilliant_scientist_constants.txt`; direct costs and factory quotes come from `common/script_constants/016_brilliant_scientist_project_constants.txt`.
File-scoped civilian-factory and AI Political Power aliases only mirror shared values for native decision fields that reject `constant:` tokens; actual affordability and private debits use shared constants.
The existing icon definitions in `interface/016_brilliant_scientist_project_icons.gfx` resolve to four existing DDS files in `gfx/interface/decisions/016_brilliant_scientist/projects/`.
The decision modifier reserves and releases civilian factories through the native lifecycle; only the three direct cost axes are debited and refunded by the private API.

## AI parity and evidence limit

| Stage | Exact Kruger decision | Base | Wartime multiplier | Cautious multiplier |
| --- | --- | --- | --- | --- |
| Theory | `brilliant_scientist_advance_xenobiological_synthesis_theory` | `brilliant_scientist_project_board.ai_low` | `brilliant_scientist_project_ai.preferred_factor` | `brilliant_scientist_project_ai.cautious_factor` |
| No-DLC Prototype | `brilliant_scientist_fallback_xenobiological_synthesis_prototype` | `brilliant_scientist_project_board.ai_high` | same | same |
| Deployment | `brilliant_scientist_advance_xenobiological_synthesis_deployment` | `brilliant_scientist_project_board.ai_low` | same | same |
| Weaponization | `brilliant_scientist_advance_xenobiological_synthesis_weaponization` | `brilliant_scientist_project_board.ai_low` | same | same |

Kruger uses `brilliant_scientist_has_low_project_capacity` for the cautious multiplier.
The parent replaced the single Weaponization-based cautious predicate after the read-only baseline audit found it applied at every stage.
Four private no-spare-factory triggers now compare available project factories against the exact stage quotes 1/2/5/7 with equality included, without consulting Kruger Capacity.
The same-scenario post-patch probability audit is pending; source hashes at this patch are decision `38D5232F6099985BF1710EE372554E7A79648A333974F613D6C90D65B8EF899B` and trigger `5FC76BEC30F2A2FCACF80A5643083725FD1EE7322D8F1D5A8AFFCCC84384C1E3`.
The source crosswalk is `common/decisions/016_brilliant_scientist_directorate_project_board.txt` at the three Xenobiological Synthesis stage decisions and its no-DLC Prototype fallback.
Source parity is not MCP probability evidence.

## Source checks and remaining acceptance

Consulted the eleven offline core wiki pages plus Decision and Idea Modding, including the offline special-project trigger and effect sections; consulted installed vanilla decision documentation and engine documentation for constants, effects, triggers, modifiers, and localisation, and the vanilla `GER.txt` timed-decision precedent.
Read the required decisions, events, and subagents skills, the accepted plan/spec, the native project and bridge, shared stage core and quote constants, Kruger decisions, and the neighboring private-family wrapper pattern.
Checked the proposed decision and trigger namespace before writing; the completed files were then checked against existing decision, trigger, and localisation declarations for exact ID collisions.
Static review must still be followed by the parent decision audit, `hoi4.probability_inspect` baseline and same-scenario `hoi4.probability_compare` through `chaosx_ai_probability_auditor`, and native callback/payment acceptance for both DLC states.
No HOI4 process was launched, no shared file or spreadsheet was edited, and no Git staging or commit was performed.
