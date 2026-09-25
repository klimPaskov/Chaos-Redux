# Event 016 Mengele Temporal private stage decision handoff — 2026-09-25

## Scope and disposition

This bounded slice implements the accepted Temporal Mechanics family decision route from the [Mengele portfolio closure plan](../016_final_mengele_portfolio_closure_plan_2026-09-02.md) and [final completion contract](../../../specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md).
It does not establish Event 016 completion or live acceptance.
The four worker files listed here are the outputs of this assignment; parent integration also added `docs/events/016_brilliant_scientist/systems/mengele_temporal_stages.md` to document the mechanic, assets, and acceptance limits.

## Files and exact identifiers

| File | Owned content |
| --- | --- |
| `common/decisions/016_mengele_temporal_stage_decisions.txt` | `mengele_event016_temporal_theory`, `mengele_event016_temporal_prototype`, `mengele_event016_temporal_deployment`, `mengele_event016_temporal_weaponization` in `mengele_clone_army_category`. |
| `common/scripted_triggers/016_mengele_temporal_stage_decision_triggers.txt` | Visibility, inclusive payment, exact receipt, cancellation, and factory-margin predicates under the `brilliant_scientist_mengele_temporal_` prefix. |
| `localisation/english/016_mengele_temporal_stage_l_english.yml` | Four names and descriptions, compact icon costs, full affordability text, requirements, cancellation, and outcomes; UTF-8 BOM. |
| This handoff | Quote, callback, source, MCP, and integration evidence. |

The existing family selector is `constant:brilliant_scientist_project_family.temporal` (ID 14); its private aligned active-stage receipt is index 13.
Each decision writes its literal family and stage selectors independently in `complete_effect`, `cancel_effect`, and `remove_effect`.
Each row requires the existing provider/registry validity gate, the exact private predecessor flag, and an empty Temporal active-stage receipt.
Theory, Deployment, and Weaponization are available with or without `Gotterdammerung`; the paid Prototype is available only without it and only before exact native `sp:sp_brilliant_scientist_temporal_mechanics` completion.

## Native project and callback ownership

`common/special_projects/projects/016_brilliant_scientist_projects.txt` defines `sp_brilliant_scientist_temporal_mechanics` at line 782 with its own breakthrough, resource, prototype-time, and output contract.
`common/scripted_triggers/016_mengele_project_bridge_triggers.txt` uses that exact native ID in `brilliant_scientist_can_research_mengele_temporal_prototype`.
`common/scripted_effects/016_mengele_project_bridge_effects.txt` requires exact native completion and private Theory/Prototype receipts before granting `chaosx_custom_technology_family.temporal` on the native path.
The shared private stage core records the Temporal Prototype receipt but grants the operational package normally at Deployment and the `temporal_weaponization` upgrade at Weaponization.
On the no-DLC paid route, this decision's Prototype `remove_effect` calls `brilliant_scientist_mengele_finish_project_stage` first; it calls `chaosx_grant_custom_operational_technology` only when the private finish reports both `mengele_event016_stage_finished = one` and `mengele_event016_project_output_applied = one`, the private Prototype flag exists, and the DLC is absent.
The public API avoids duplicate static technology and deduplicates source provenance; the wrapper clears its family and source selectors after the call.
A failed or rejected private finish cannot grant the output through this wrapper.
No new row invokes Kruger board payment, Capacity, or native integration effects.

## Stage quote and icon evidence

| Stage | Duration | Civilian-factory reservation | Political Power | Support Equipment | Fuel | Existing icon suffix |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Theory | 360 days | 2 | 75 | 120 | 0 | `temporal_mechanics_theory` |
| No-DLC Prototype | 540 days | 3 | 113 | 300 | 500 | `temporal_mechanics_prototype` |
| Deployment | 720 days | 6 | 150 | 900 | 2,500 | `temporal_mechanics_deployment` |
| Weaponization | 900 days | 10 | 225 | 1,800 | 7,500 | `temporal_mechanics_weaponization` |

The duration and payment sources are `common/script_constants/016_brilliant_scientist_constants.txt` and `common/script_constants/016_brilliant_scientist_project_constants.txt`.
The four `GFX_decision_brilliant_scientist_project_temporal_mechanics_*` sprites and DDS references already exist in `interface/016_brilliant_scientist_project_icons.gfx` lines 62–65.
The file-local civilian-factory and Political Power hints mirror the shared values because these native decision fields use literal tokens in this repository pattern.
The private begin/cancel/finish core owns the three direct payment axes and any refund; the decision lifecycle owns `civilian_factory_use` reservation and release.

## Kruger AI comparison

| Stage | Kruger source ID | Kruger base | Private base | Wartime factor | Cautious factor |
| --- | --- | --- | --- | --- | --- |
| Theory | `brilliant_scientist_advance_temporal_theory` | `brilliant_scientist_project_board.ai_low` | same | `brilliant_scientist_project_ai.preferred_factor` with `has_war = yes` | `brilliant_scientist_project_ai.cautious_factor` on low capacity |
| No-DLC Prototype | `brilliant_scientist_fallback_temporal_prototype` | `brilliant_scientist_project_board.ai_high` | same | same | same |
| Deployment | `brilliant_scientist_advance_temporal_deployment` | `brilliant_scientist_project_board.ai_low` | same | same | same |
| Weaponization | `brilliant_scientist_advance_temporal_weaponization` | `brilliant_scientist_project_board.ai_low` | same | same | same |

The source is `common/decisions/016_brilliant_scientist_directorate_project_board.txt` lines 3224–3385 and 5711–5757.
The private cautious predicates compare available civilian factories with each decision's exact quote: Theory two, no-DLC Prototype three, Deployment six, and Weaponization ten.
Each `brilliant_scientist_mengele_temporal_<stage>_decision_no_spare_factories` trigger uses `NOT = { available CIC > stage quote }`, so equality activates the cautious factor while any spare factory suppresses it.
Kruger's source uses `brilliant_scientist_has_low_project_capacity` in all four rows; the private route preserves each exact base, wartime factor, and cautious factor but uses this family/stage-specific factory proxy without reading or writing Kruger Capacity.
Source parity of factor values does not prove identical trigger frequency or AI selection.

## MCP evidence and open limits

`hoi4.probability_inspect` reached workspace `mod_chaos_redux_ea3b2d67c2c0` and identified `mission_ai_will_do` as the adapter for these timed decisions.
The exact four Kruger candidates were discovered with `PROBABILITY_SOURCE_INSPECTED` (source revision `aa89ad566f4937f339dc42692fdebd6642a21bcd22284d820c6fbd6725d333ee`): `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b9d2a8fd07c3d9592e631df273b342f139d5748cf7e7acd40cd523a3e0adeca8/d9f258450799d2f99994b83d749543dce8561ee0ddfd98bb452b0bffff0a34f3/probability-inspect-62f2b563c5e7.json`.
Before the parent caution refinement, the four new candidates were discovered with `PROBABILITY_SOURCE_INSPECTED` (source revision `33c2969efc5823ec9de75c3e90a2384c0b9c54a9e43e444fcf5be491c9b527ed`): `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6d465153ec85ebae39da1fabc70876d66a8489a8c71ec9dc087d95572218cb71/a0517103c9b7716dbb1bc62aed63024ca3f39392490c37f46cb7199d29f9a7af/probability-inspect-df8ab5658e0f.json`.
The earlier three-scenario private evaluation (`peace_factory_margin`, `wartime_factory_margin`, `wartime_tight_factories`) returned `PROBABILITY_ANALYZED_PARTIAL`, scenario hash `50dbc6474d5d97e1972ccfcd22c1ae5d0c35b4ef3df3eebe56b4e4472eeea932`, with eight explicit unresolved items: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b9c1a90075658ccabf3254f08bf076425f8c4e92453b2f0d0afc0ccde4a0d924/bca5bd92be1b322f16241f2ad9782f25fb096d48fc9d3fa0aa65efdec9d08f47/probability-9586770057613c4f891659fb.json`.
Those artifacts precede the stage-specific caution edit and cannot validate its post-change behavior.
Post-edit `hoi4.probability_inspect` found all four private Temporal candidates with `PROBABILITY_SOURCE_INSPECTED`, source revision `c9c79f50b7d6af76efdbf772cb48d791b5b8e78943b7c17f1bcd67aaf89e1e47`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/715ec826c9110790c2c0727495a1730f65ea35489470ef6efd42c604223f88f6/3bd4a35eea16c650f7ca71d13d66cf1bd0d9e7f05f5601d646a3acf1d2aca5d6/probability-inspect-e46cc652d368.json`.
The parent baseline audit prompted this correction, but no historical pre-edit source file exists for a valid same-path MCP comparison; post-edit discovery is not a `hoi4.probability_compare` result.
The earlier analysis reports willingness scores with unresolved scripted trigger and campaign state inputs, not click probabilities or balance acceptance; the required full auditor comparison remains parent-owned and unresolved.

Static review checked the four exact decision IDs, three literal callbacks per stage, private slot 13, native ID, existing icon definitions, localisation references, UTF-8 BOM, and source quote values.
The caution boundary was checked against all four shared factory quotes: equality activates the cautious factor and one spare factory does not.
The parent still needs its decision/mission audit, the complete probability scenario comparison, and integration review of native versus paid Prototype payment.
Native timed-decision ordering, real cost presentation, and the operational consumer remain subject to engine evidence and user live acceptance.
No HOI4 process was launched, no shared file or spreadsheet was edited, and no files were staged or committed.
