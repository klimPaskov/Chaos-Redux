# FORM-03 icon `.gfx` handoff

## Ownership note

This asset tranche did not edit `.gfx`, focus, idea, decision, localisation,
GUI, or gameplay files.  During final path review,
`interface/006_independence_wave_form03.gfx` already contained the exact base,
shine, idea, and decision sprite registrations listed below.  Those existing
entries were created outside this tranche and already point to the delivered
runtime DDS paths.

Suggested/observed target file:
`interface/006_independence_wave_form03.gfx`.

## Focus sprites

Each shine sprite should continue to use the same DDS as its base sprite with
`effectFile = "gfx/FX/buttonstate.lua"`.

| Runtime DDS | Base sprite | Shine sprite | Gameplay focus |
|---|---|---|---|
| `gfx/interface/goals/006_independence_wave/form03/goal_independence_wave_form03_open_charter_convention.dds` | `GFX_goal_independence_wave_form03_open_charter_convention` | `GFX_goal_independence_wave_form03_open_charter_convention_shine` | `independence_wave_form03_open_charter_convention` |
| `gfx/interface/goals/006_independence_wave/form03/goal_independence_wave_form03_define_public_service_guarantees.dds` | `GFX_goal_independence_wave_form03_define_public_service_guarantees` | `GFX_goal_independence_wave_form03_define_public_service_guarantees_shine` | `independence_wave_form03_define_public_service_guarantees` |
| `gfx/interface/goals/006_independence_wave/form03/goal_independence_wave_form03_establish_delta_works_board.dds` | `GFX_goal_independence_wave_form03_establish_delta_works_board` | `GFX_goal_independence_wave_form03_establish_delta_works_board_shine` | `independence_wave_form03_establish_delta_works_board` |
| `gfx/interface/goals/006_independence_wave/form03/goal_independence_wave_form03_build_federal_appeals_and_examinations.dds` | `GFX_goal_independence_wave_form03_build_federal_appeals_and_examinations` | `GFX_goal_independence_wave_form03_build_federal_appeals_and_examinations_shine` | `independence_wave_form03_build_federal_appeals_and_examinations` |
| `gfx/interface/goals/006_independence_wave/form03/goal_independence_wave_form03_harmonize_corridor_standards.dds` | `GFX_goal_independence_wave_form03_harmonize_corridor_standards` | `GFX_goal_independence_wave_form03_harmonize_corridor_standards_shine` | `independence_wave_form03_harmonize_corridor_standards` |
| `gfx/interface/goals/006_independence_wave/form03/goal_independence_wave_form03_submit_low_countries_compact.dds` | `GFX_goal_independence_wave_form03_submit_low_countries_compact` | `GFX_goal_independence_wave_form03_submit_low_countries_compact_shine` | `independence_wave_form03_submit_low_countries_compact` |

## Idea / national-spirit sprites

| Runtime DDS | Sprite | Gameplay idea / `picture` token |
|---|---|---|
| `gfx/interface/ideas/006_independence_wave/form03/idea_independence_wave_form03_provisional_charter.dds` | `GFX_idea_independence_wave_form03_provisional_charter` | `independence_wave_form03_provisional_charter` |
| `gfx/interface/ideas/006_independence_wave/form03/idea_independence_wave_form03_charter_without_works.dds` | `GFX_idea_independence_wave_form03_charter_without_works` | `independence_wave_form03_charter_without_works` |
| `gfx/interface/ideas/006_independence_wave/form03/idea_independence_wave_form03_industrial_directorate.dds` | `GFX_idea_independence_wave_form03_industrial_directorate` | `independence_wave_form03_industrial_directorate` |
| `gfx/interface/ideas/006_independence_wave/form03/idea_independence_wave_form03_dual_compromise.dds` | `GFX_idea_independence_wave_form03_dual_compromise` | `independence_wave_form03_dual_compromise` |
| `gfx/interface/ideas/006_independence_wave/form03/idea_independence_wave_form03_ratified_confederation.dds` | `GFX_idea_independence_wave_form03_ratified_confederation` | `independence_wave_form03_ratified_confederation` |
| `gfx/interface/ideas/006_independence_wave/form03/idea_independence_wave_form03_charter_rupture.dds` | `GFX_idea_independence_wave_form03_charter_rupture` | `independence_wave_form03_charter_rupture` |

## Decision-family sprites

| Runtime DDS | Sprite | Current gameplay family |
|---|---|---|
| `gfx/interface/decisions/006_independence_wave/form03/decision_independence_wave_form03_language.dds` | `GFX_decision_independence_wave_form03_language` | convention, examinations, language codes, appeals, and protected local services |
| `gfx/interface/decisions/006_independence_wave/form03/decision_independence_wave_form03_works.dds` | `GFX_decision_independence_wave_form03_works` | carrier and associate corridor/works actions |
| `gfx/interface/decisions/006_independence_wave/form03/decision_independence_wave_form03_member_vote.dds` | `GFX_decision_independence_wave_form03_member_vote` | founding delegations, autonomous membership, invitations, and member guarantees |
| `gfx/interface/decisions/006_independence_wave/form03/decision_independence_wave_form03_ratification.dds` | `GFX_decision_independence_wave_form03_ratification` | ratification mission and resubmission |
| `gfx/interface/decisions/006_independence_wave/form03/decision_independence_wave_form03_repair.dds` | `GFX_decision_independence_wave_form03_repair` | reopening and both repair actions |
| `gfx/interface/decisions/006_independence_wave/form03/decision_independence_wave_form03_withdrawal.dds` | `GFX_decision_independence_wave_form03_withdrawal` | autonomous-membership withdrawal |

## Parent review points

- Preserve the filenames and sprite names exactly; runtime DDS checksums are in
  `manifest.md`.
- Do not wire the retained package copies under `docs/assets/.../dds/`; those
  are provenance copies only.  Runtime sprites must continue to use the `gfx/`
  paths above.
- No report image, flag, animation, or alternate state is part of this handoff.
- Native and enlarged transparency/alignment sheets are under
  `contact_sheets/`.
- No blocker remains for these 18 icon sprites.
