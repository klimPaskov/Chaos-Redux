# Event 012 Focus-Family Icon GFX Handoff

## Registration target

At the time of asset production there was no Event 012 `.gfx` file under `interface/`. Register these sprites in `interface/012_africa.gfx`, or merge the block into the canonical Event 012 sprite file if one is created concurrently.

The focus tree already references each regular sprite name exactly. HOI4 also resolves the corresponding `<sprite>_shine` name for the focus-button shine state, so both definitions are required. The repository's existing focus-icon convention uses the same DDS for both definitions and applies `gfx/FX/buttonstate.lua` to the shine sprite.

## Ready-to-copy sprite block

```txt
spriteTypes = {
	# Event 012 shared focus-family icons and their standard button-state shine.
	spriteType = { name = "GFX_goal_africa_focus_family_host_proclamation" texturefile = "gfx/interface/goals/012_africa/goal_africa_focus_family_host_proclamation.dds" }
	spriteType = { name = "GFX_goal_africa_focus_family_host_proclamation_shine" texturefile = "gfx/interface/goals/012_africa/goal_africa_focus_family_host_proclamation.dds" effectFile = "gfx/FX/buttonstate.lua" }
	spriteType = { name = "GFX_goal_africa_focus_family_host_legitimacy" texturefile = "gfx/interface/goals/012_africa/goal_africa_focus_family_host_legitimacy.dds" }
	spriteType = { name = "GFX_goal_africa_focus_family_host_legitimacy_shine" texturefile = "gfx/interface/goals/012_africa/goal_africa_focus_family_host_legitimacy.dds" effectFile = "gfx/FX/buttonstate.lua" }
	spriteType = { name = "GFX_goal_africa_focus_family_charter_law" texturefile = "gfx/interface/goals/012_africa/goal_africa_focus_family_charter_law.dds" }
	spriteType = { name = "GFX_goal_africa_focus_family_charter_law_shine" texturefile = "gfx/interface/goals/012_africa/goal_africa_focus_family_charter_law.dds" effectFile = "gfx/FX/buttonstate.lua" }
	spriteType = { name = "GFX_goal_africa_focus_family_continental_representation" texturefile = "gfx/interface/goals/012_africa/goal_africa_focus_family_continental_representation.dds" }
	spriteType = { name = "GFX_goal_africa_focus_family_continental_representation_shine" texturefile = "gfx/interface/goals/012_africa/goal_africa_focus_family_continental_representation.dds" effectFile = "gfx/FX/buttonstate.lua" }
	spriteType = { name = "GFX_goal_africa_focus_family_protection_guarantee" texturefile = "gfx/interface/goals/012_africa/goal_africa_focus_family_protection_guarantee.dds" }
	spriteType = { name = "GFX_goal_africa_focus_family_protection_guarantee_shine" texturefile = "gfx/interface/goals/012_africa/goal_africa_focus_family_protection_guarantee.dds" effectFile = "gfx/FX/buttonstate.lua" }
	spriteType = { name = "GFX_goal_africa_focus_family_volunteer_intervention" texturefile = "gfx/interface/goals/012_africa/goal_africa_focus_family_volunteer_intervention.dds" }
	spriteType = { name = "GFX_goal_africa_focus_family_volunteer_intervention_shine" texturefile = "gfx/interface/goals/012_africa/goal_africa_focus_family_volunteer_intervention.dds" effectFile = "gfx/FX/buttonstate.lua" }
	spriteType = { name = "GFX_goal_africa_focus_family_aid_and_relief" texturefile = "gfx/interface/goals/012_africa/goal_africa_focus_family_aid_and_relief.dds" }
	spriteType = { name = "GFX_goal_africa_focus_family_aid_and_relief_shine" texturefile = "gfx/interface/goals/012_africa/goal_africa_focus_family_aid_and_relief.dds" effectFile = "gfx/FX/buttonstate.lua" }
	spriteType = { name = "GFX_goal_africa_focus_family_regional_congress" texturefile = "gfx/interface/goals/012_africa/goal_africa_focus_family_regional_congress.dds" }
	spriteType = { name = "GFX_goal_africa_focus_family_regional_congress_shine" texturefile = "gfx/interface/goals/012_africa/goal_africa_focus_family_regional_congress.dds" effectFile = "gfx/FX/buttonstate.lua" }
	spriteType = { name = "GFX_goal_africa_focus_family_road_corridor" texturefile = "gfx/interface/goals/012_africa/goal_africa_focus_family_road_corridor.dds" }
	spriteType = { name = "GFX_goal_africa_focus_family_road_corridor_shine" texturefile = "gfx/interface/goals/012_africa/goal_africa_focus_family_road_corridor.dds" effectFile = "gfx/FX/buttonstate.lua" }
	spriteType = { name = "GFX_goal_africa_focus_family_rail_corridor" texturefile = "gfx/interface/goals/012_africa/goal_africa_focus_family_rail_corridor.dds" }
	spriteType = { name = "GFX_goal_africa_focus_family_rail_corridor_shine" texturefile = "gfx/interface/goals/012_africa/goal_africa_focus_family_rail_corridor.dds" effectFile = "gfx/FX/buttonstate.lua" }
	spriteType = { name = "GFX_goal_africa_focus_family_army_common_reserve" texturefile = "gfx/interface/goals/012_africa/goal_africa_focus_family_army_common_reserve.dds" }
	spriteType = { name = "GFX_goal_africa_focus_family_army_common_reserve_shine" texturefile = "gfx/interface/goals/012_africa/goal_africa_focus_family_army_common_reserve.dds" effectFile = "gfx/FX/buttonstate.lua" }
	spriteType = { name = "GFX_goal_africa_focus_family_resource_sovereignty" texturefile = "gfx/interface/goals/012_africa/goal_africa_focus_family_resource_sovereignty.dds" }
	spriteType = { name = "GFX_goal_africa_focus_family_resource_sovereignty_shine" texturefile = "gfx/interface/goals/012_africa/goal_africa_focus_family_resource_sovereignty.dds" effectFile = "gfx/FX/buttonstate.lua" }
	spriteType = { name = "GFX_goal_africa_focus_family_rival_bloc" texturefile = "gfx/interface/goals/012_africa/goal_africa_focus_family_rival_bloc.dds" }
	spriteType = { name = "GFX_goal_africa_focus_family_rival_bloc_shine" texturefile = "gfx/interface/goals/012_africa/goal_africa_focus_family_rival_bloc.dds" effectFile = "gfx/FX/buttonstate.lua" }
}
```

## Integration checks

After registration, confirm that:

1. Every `GFX_goal_africa_focus_family_*` consumer in `common/national_focus/012_africa_continental_focus_tree.txt` resolves to one regular sprite definition.
2. Every regular definition has a matching `_shine` definition.
3. Every texture path resolves to one of the 13 DDS files under `gfx/interface/goals/012_africa/`.
4. No other sprite reuses these names.

No `.gui` change or animated sprite sheet is required for this static focus-family tranche.
