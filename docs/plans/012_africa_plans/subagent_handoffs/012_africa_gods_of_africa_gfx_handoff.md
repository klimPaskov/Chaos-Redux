# Event 012 Gods of Africa GFX handoff

This is the GFX-only companion to `../012_africa_gods_icon_assets_handoff_2026-09-05.md`; the parent owns all `.gfx` edits and gameplay wiring.

Reconciliation note, 2026-09-05: the asset package changed no GFX files, but the current parent working tree now contains the proposed aliases in `interface/012_africa.gfx` and the Event 012 category picture consumers. This source evidence supersedes the narrower pending-wiring wording below without constituting parent or user approval.

## Proposed sprite aliases

The two compact mechanic sprites are `GFX_012_africa_gods_strength` and `GFX_012_africa_gods_wrath`, using `gfx/interface/012_africa/gods_of_africa/gods_of_africa_strength.dds` and `gfx/interface/012_africa/gods_of_africa/gods_of_africa_wrath.dds` respectively.

The five participant response sprites are `GFX_decision_012_africa_gods_fulfill_demand`, `GFX_decision_012_africa_gods_offer_substitute`, `GFX_decision_012_africa_gods_request_extension`, `GFX_decision_012_africa_gods_refuse_demand`, and `GFX_decision_012_africa_gods_defy`.

The response textures are `gfx/interface/decisions/012_africa/gods_of_africa/decision_012_africa_gods_fulfill_demand.dds`, `gfx/interface/decisions/012_africa/gods_of_africa/decision_012_africa_gods_offer_substitute.dds`, `gfx/interface/decisions/012_africa/gods_of_africa/decision_012_africa_gods_request_extension.dds`, `gfx/interface/decisions/012_africa/gods_of_africa/decision_012_africa_gods_refuse_demand.dds`, and `gfx/interface/decisions/012_africa/gods_of_africa/decision_012_africa_gods_defy.dds`.

The six Africa-side action sprites are `GFX_decision_012_africa_gods_set_priority`, `GFX_decision_012_africa_gods_grant_leniency`, `GFX_decision_012_africa_gods_mark_offender`, `GFX_decision_012_africa_gods_protect_partner`, `GFX_decision_012_africa_gods_public_pardon`, and `GFX_decision_012_africa_gods_escalate_offense`, with matching textures in `gfx/interface/decisions/012_africa/gods_of_africa/`.

The six idea aliases are `GFX_idea_gods_of_africa_idea_proclamation`, `GFX_idea_gods_of_africa_idea_voices`, `GFX_idea_gods_of_africa_idea_reciprocal_covenant`, `GFX_idea_gods_of_africa_idea_sovereign_exaction`, `GFX_idea_gods_of_africa_idea_reserve`, and `GFX_idea_gods_of_africa_idea_judgment`, with matching textures in `gfx/interface/ideas/012_africa/gods_of_africa/`.

The eight focus-family aliases are `GFX_goal_012_africa_gods_proclamation_institution`, `GFX_goal_012_africa_gods_reciprocal_doctrine`, `GFX_goal_012_africa_gods_extractive_doctrine`, `GFX_goal_012_africa_gods_provision_logistics`, `GFX_goal_012_africa_gods_oaths_diplomacy`, `GFX_goal_012_africa_gods_protection`, `GFX_goal_012_africa_gods_judgment`, and `GFX_goal_012_africa_gods_continental_settlement`, with matching textures in `gfx/interface/goals/012_africa/gods_of_africa/`.

## Wiring state

No GFX files were changed by this handoff. The current working tree contains the listed mechanic, decision, idea, and focus aliases in `interface/012_africa.gfx`; report-event aliases are tracked by the companion event-art handoff and `interface/012_africa_event_pictures.gfx`.

The current five participant decision consumers, the Africa-side priority/leniency/offender/protection/pardon/escalation consumers, the six ideas, and the Gods focus overlay now have source references to the generated aliases described above; parent/user visual review and live playback remain open.

The current decision file contains consumers for the listed priority, offender, pardon, and escalation aliases, while any future action concept without a current decision id remains unconsumed until a bounded owner change is accepted.

The Strength and Wrath sprites have no current scripted-GUI consumer in the inspected source and should be wired only when their consumer is accepted.

No custom elephant sprite is required or proposed because `common/units/012_africa_elephant_forces.txt` binds `sprite = elephantry` from vanilla.
