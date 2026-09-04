# Event 012 Gods of Africa GFX handoff

This is the GFX-only companion to `../012_africa_gods_icon_assets_handoff_2026-09-05.md`; the parent owns all `.gfx` edits and gameplay wiring.

## Proposed sprite aliases

The two compact mechanic sprites are `GFX_012_africa_gods_strength` and `GFX_012_africa_gods_wrath`, using `gfx/interface/012_africa/gods_of_africa/gods_of_africa_strength.dds` and `gfx/interface/012_africa/gods_of_africa/gods_of_africa_wrath.dds` respectively.

The five participant response sprites are `GFX_decision_012_africa_gods_fulfill_demand`, `GFX_decision_012_africa_gods_offer_substitute`, `GFX_decision_012_africa_gods_request_extension`, `GFX_decision_012_africa_gods_refuse_demand`, and `GFX_decision_012_africa_gods_defy`.

The response textures are `gfx/interface/decisions/012_africa/gods_of_africa/decision_012_africa_gods_fulfill_demand.dds`, `gfx/interface/decisions/012_africa/gods_of_africa/decision_012_africa_gods_offer_substitute.dds`, `gfx/interface/decisions/012_africa/gods_of_africa/decision_012_africa_gods_request_extension.dds`, `gfx/interface/decisions/012_africa/gods_of_africa/decision_012_africa_gods_refuse_demand.dds`, and `gfx/interface/decisions/012_africa/gods_of_africa/decision_012_africa_gods_defy.dds`.

The six Africa-side action sprites are `GFX_decision_012_africa_gods_set_priority`, `GFX_decision_012_africa_gods_grant_leniency`, `GFX_decision_012_africa_gods_mark_offender`, `GFX_decision_012_africa_gods_protect_partner`, `GFX_decision_012_africa_gods_public_pardon`, and `GFX_decision_012_africa_gods_escalate_offense`, with matching textures in `gfx/interface/decisions/012_africa/gods_of_africa/`.

The six idea aliases are `GFX_idea_gods_of_africa_idea_proclamation`, `GFX_idea_gods_of_africa_idea_voices`, `GFX_idea_gods_of_africa_idea_reciprocal_covenant`, `GFX_idea_gods_of_africa_idea_sovereign_exaction`, `GFX_idea_gods_of_africa_idea_reserve`, and `GFX_idea_gods_of_africa_idea_judgment`, with matching textures in `gfx/interface/ideas/012_africa/gods_of_africa/`.

The eight focus-family aliases are `GFX_goal_012_africa_gods_proclamation_institution`, `GFX_goal_012_africa_gods_reciprocal_doctrine`, `GFX_goal_012_africa_gods_extractive_doctrine`, `GFX_goal_012_africa_gods_provision_logistics`, `GFX_goal_012_africa_gods_oaths_diplomacy`, `GFX_goal_012_africa_gods_protection`, `GFX_goal_012_africa_gods_judgment`, and `GFX_goal_012_africa_gods_continental_settlement`, with matching textures in `gfx/interface/goals/012_africa/gods_of_africa/`.

## Wiring state

No GFX files were changed, and none of these aliases currently exists in the inspected `interface/012_africa.gfx` or another active interface file.

The current five participant decision consumers still point to the existing charter-ledger or generic sprites, the six current ideas have no matching GFX aliases, and the current focus overlay still points to the prior broad Event 012 family sprites.

The accepted priority, offender, pardon, and escalation action names are future-ready concepts without current decision ids in `common/decisions/012_africa_gods_decisions.txt`; keep them unconsumed until the parent accepts a bounded wiring change.

The Strength and Wrath sprites have no current scripted-GUI consumer in the inspected source and should be wired only when their consumer is accepted.

No custom elephant sprite is required or proposed because `common/units/012_africa_elephant_forces.txt` binds `sprite = elephantry` from vanilla.
