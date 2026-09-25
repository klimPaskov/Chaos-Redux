# Event 016 Mengele Paleogenetics private stage decision handoff — 2026-09-25

## Scope and disposition

This is one bounded family slice under the accepted [Mengele portfolio closure plan](../016_final_mengele_portfolio_closure_plan_2026-09-02.md) and [final completion contract](../../../specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md).
The four new files implement private Paleogenetics decision wrappers, gates, localisation, and this handoff only.
This handoff does not claim Event 016 completion or live acceptance.

## Changed files and identifiers

| File | Owned content |
| --- | --- |
| `common/decisions/016_mengele_paleogenetics_stage_decisions.txt` | `mengele_event016_paleogenetics_theory`, `_prototype`, `_deployment`, and `_weaponization` in `mengele_clone_army_category`. |
| `common/scripted_triggers/016_mengele_paleogenetics_stage_decision_triggers.txt` | Family-specific visibility, affordability, exact receipt match, cancellation, and factory-margin triggers with the `brilliant_scientist_mengele_paleogenetics_` prefix. |
| `localisation/english/016_mengele_paleogenetics_stage_l_english.yml` | Names, descriptions, costs, requirements, cancellation text, and outcomes for the four rows. UTF-8 BOM. |
| This file | Source evidence, implementation boundary, and parent validation handoff. |

Family selector is `constant:brilliant_scientist_project_family.paleogenetics` (ID 10), and the private aligned receipt slot is `mengele_event016_active_project_stage_entries^9`.
The literal requested stage is set separately in every begin, cancel, and finish wrapper.
The provider gate is the existing `brilliant_scientist_mengele_project_stage_provider_is_valid`; each next row requires its exact private predecessor receipt and no active private receipt in this family.
The Prototype row is offered only without `Gotterdammerung`, while Theory, Deployment, and Weaponization use the same provider path in both DLC states.

## Native project, output, and ownership evidence

`common/special_projects/projects/016_brilliant_scientist_projects.txt` defines `sp_brilliant_scientist_paleogenetics` at line 548, with its own breakthrough, resource, time, and output contract.
`common/scripted_triggers/016_mengele_project_bridge_triggers.txt` names this exact project in `brilliant_scientist_can_research_mengele_paleogenetics_prototype`.
`common/scripted_effects/016_mengele_project_bridge_effects.txt` requires completed native `sp:sp_brilliant_scientist_paleogenetics` plus private Theory and Prototype receipts before granting `chaosx_custom_technology_family.paleogenetic` at native Prototype.
The shared stage output core records the private Paleogenetics Prototype flag, but its normal custom operational grant is attached to Deployment and Weaponization.
Consequently the no-DLC Prototype `remove_effect` calls `brilliant_scientist_mengele_finish_project_stage`, then calls the public paleogenetic operational API only when `mengele_event016_stage_finished` and `mengele_event016_project_output_applied` both equal one, the private Prototype flag exists, and `Gotterdammerung` is absent.
The API is idempotent, and the wrapper clears its temporary family and source selectors after the call.
A rejected or failed private finish cannot grant the output through this wrapper.
No decision calls the Kruger board ledger, Capacity, or native integration helper.

## Quote, duration, and icon evidence

| Stage | Duration | Native civilian-factory reservation | Direct Political Power | Direct Support Equipment | Direct fuel | Icon |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Theory | 210 days | 1 | 65 | 130 | 0 | `GFX_decision_brilliant_scientist_project_paleogenetics_theory` |
| No-DLC Prototype | 330 days | 2 | 98 | 325 | 300 | `GFX_decision_brilliant_scientist_project_paleogenetics_prototype` |
| Deployment | 480 days | 4 | 130 | 975 | 1,500 | `GFX_decision_brilliant_scientist_project_paleogenetics_deployment` |
| Weaponization | 660 days | 6 | 195 | 1,950 | 4,500 | `GFX_decision_brilliant_scientist_project_paleogenetics_weaponization` |

Duration and payment sources are `common/script_constants/016_brilliant_scientist_constants.txt` and `common/script_constants/016_brilliant_scientist_project_constants.txt`.
The civilian-factory and Political Power file-local hints mirror those shared values only because the native decision modifier and AI hint use literal tokens here.
The three direct debits and refunds remain in `brilliant_scientist_mengele_begin_project_stage`, `brilliant_scientist_mengele_cancel_project_stage`, and `brilliant_scientist_mengele_finish_project_stage`; the decision's native `civilian_factory_use` lifecycle releases the reservation.
The four icon definitions and DDS paths already exist in `interface/016_brilliant_scientist_project_icons.gfx` and `gfx/interface/decisions/016_brilliant_scientist/projects/`.
No new art is requested.

## Exact Kruger AI comparison and parent probability pass

| Stage | Kruger decision source | Kruger base | Private base | Wartime factor | Cautious factor |
| --- | --- | --- | --- | --- | --- |
| Theory | `brilliant_scientist_advance_paleogenetics_theory` | `brilliant_scientist_project_board.ai_medium` | same | `brilliant_scientist_project_ai.preferred_factor` on `has_war = yes` | `brilliant_scientist_project_ai.cautious_factor` on low capacity |
| No-DLC Prototype | `brilliant_scientist_fallback_paleogenetics_prototype` | `brilliant_scientist_project_board.ai_high` | same | same | same |
| Deployment | `brilliant_scientist_advance_paleogenetics_deployment` | `brilliant_scientist_project_board.ai_medium` | same | same | same |
| Weaponization | `brilliant_scientist_advance_paleogenetics_weaponization` | `brilliant_scientist_project_board.ai_medium` | same | same | same |

The source is `common/decisions/016_brilliant_scientist_directorate_project_board.txt` at lines 2564–2726 and 5515–5561.
The Kruger predicate is `brilliant_scientist_has_low_project_capacity` in all four rows; private decisions use one `brilliant_scientist_mengele_paleogenetics_<stage>_decision_no_spare_factories` trigger per stage.
The private factory quotes are Theory one, no-DLC Prototype two, Deployment four, and Weaponization six; each trigger applies the cautious factor when available factories do not exceed that stage's quote, including equality.
The base, wartime, and cautious factor constants remain source-parallel with Kruger, while the private condition is a stage-specific factory-margin proxy rather than a Kruger Capacity receipt.
The parent owns the mandatory `hoi4.probability_inspect` baseline and same-scenario `hoi4.probability_compare` pass through `chaosx_ai_probability_auditor`; source equality of factors is not MCP probability evidence.
After the parent caution refinement, `hoi4.probability_inspect` found all four private Paleogenetics candidates with `PROBABILITY_SOURCE_INSPECTED`, source revision `9d2410a786b8e6694cdf59d79fc3d019f47ad3f2fac1950a51bb2ff91135c4f2`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2d0ccc1ed3d94fa6c4fe8b736829a21d01dad9ef9c7b905863f185c8ae0329a9/bb3fd42d620c16c7e87908873c5f4910ec474ef7642d892f82998bf5acc71c72/probability-inspect-ebf20562c0d2.json`.
There is no historical pre-edit source file for a valid same-path MCP comparison; the post-edit discovery does not replace the parent-owned scenario comparison.

## Validation limits and integration handoff

Static review verified four matching decision and trigger IDs, four existing icon definitions, all referenced localisations, a UTF-8 BOM, the family/index mapping, the exact native project token, and direct-cost constants against the shared quote tables.
The caution boundary was checked against each shared factory quote: equality activates the cautious factor and one spare factory does not.
No HOI4 process was launched, no shared file or spreadsheet was edited, and no Git staging or commit was performed.
The parent must perform the required decision audit and probability MCP pass, inspect the complete cross-family bridge and callback state, and retain the existing native-versus-provider payment boundary when integrating this slice.
Native timed-decision callback ordering, in-engine cost display and factory reservation, and the no-DLC reward consumer remain subject to the parent's evidence and the user's live acceptance.

## Parent review

The parent confirmed that all four new decision IDs are unique in `common/decisions`, the family array index is nine, the no-DLC Prototype post-finish guard precedes the neutral operational grant, and the four icon DDS files and localisation BOM exist.
The parent added `docs/events/016_brilliant_scientist/systems/mengele_paleogenetics_stages.md` for the lifecycle, runtime consumers, assets, and acceptance boundary.
The probability MCP pass, current decision-list presentation, and native callback behavior remain open.
