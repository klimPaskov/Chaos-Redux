# Event 006 Pacific focus-icon GFX handoff

Parent-owned wiring only: this package did not edit `.gfx` files. The parent-owned `interface/006_independence_wave_pacific_focus_icons.gfx` now registers the 14 base sprites and their 14 `_shine` partners below, and the current Pacific focus implementation resolves to the exact base IDs. All textures are installed under `gfx/interface/goals/006_independence_wave/`.

The `_shine` entries follow the existing Event 006 focus convention: same texturefile as the base icon and `effectFile = "gfx/FX/buttonstate.lua"`.

```text
spriteTypes = {
	# HBX — California
	spriteType = { name = "GFX_goal_independence_wave_hbx_screen_federal_arsenals" texturefile = "gfx/interface/goals/006_independence_wave/goal_independence_wave_hbx_screen_federal_arsenals.dds" }
	spriteType = { name = "GFX_goal_independence_wave_hbx_screen_federal_arsenals_shine" texturefile = "gfx/interface/goals/006_independence_wave/goal_independence_wave_hbx_screen_federal_arsenals.dds" effectFile = "gfx/FX/buttonstate.lua" }
	spriteType = { name = "GFX_goal_independence_wave_hbx_reopen_coastal_supply_bureaus" texturefile = "gfx/interface/goals/006_independence_wave/goal_independence_wave_hbx_reopen_coastal_supply_bureaus.dds" }
	spriteType = { name = "GFX_goal_independence_wave_hbx_reopen_coastal_supply_bureaus_shine" texturefile = "gfx/interface/goals/006_independence_wave/goal_independence_wave_hbx_reopen_coastal_supply_bureaus.dds" effectFile = "gfx/FX/buttonstate.lua" }
	spriteType = { name = "GFX_goal_independence_wave_hbx_seat_sacramento_civic_convention" texturefile = "gfx/interface/goals/006_independence_wave/goal_independence_wave_hbx_seat_sacramento_civic_convention.dds" }
	spriteType = { name = "GFX_goal_independence_wave_hbx_seat_sacramento_civic_convention_shine" texturefile = "gfx/interface/goals/006_independence_wave/goal_independence_wave_hbx_seat_sacramento_civic_convention.dds" effectFile = "gfx/FX/buttonstate.lua" }
	spriteType = { name = "GFX_goal_independence_wave_hbx_bind_ports_factories_and_guard" texturefile = "gfx/interface/goals/006_independence_wave/goal_independence_wave_hbx_bind_ports_factories_and_guard.dds" }
	spriteType = { name = "GFX_goal_independence_wave_hbx_bind_ports_factories_and_guard_shine" texturefile = "gfx/interface/goals/006_independence_wave/goal_independence_wave_hbx_bind_ports_factories_and_guard.dds" effectFile = "gfx/FX/buttonstate.lua" }
	spriteType = { name = "GFX_goal_independence_wave_hbx_settle_federal_asset_ledger" texturefile = "gfx/interface/goals/006_independence_wave/goal_independence_wave_hbx_settle_federal_asset_ledger.dds" }
	spriteType = { name = "GFX_goal_independence_wave_hbx_settle_federal_asset_ledger_shine" texturefile = "gfx/interface/goals/006_independence_wave/goal_independence_wave_hbx_settle_federal_asset_ledger.dds" effectFile = "gfx/FX/buttonstate.lua" }
	spriteType = { name = "GFX_goal_independence_wave_hbx_charter_pacific_procurement_board" texturefile = "gfx/interface/goals/006_independence_wave/goal_independence_wave_hbx_charter_pacific_procurement_board.dds" }
	spriteType = { name = "GFX_goal_independence_wave_hbx_charter_pacific_procurement_board_shine" texturefile = "gfx/interface/goals/006_independence_wave/goal_independence_wave_hbx_charter_pacific_procurement_board.dds" effectFile = "gfx/FX/buttonstate.lua" }
	spriteType = { name = "GFX_goal_independence_wave_hbx_convene_pacific_maritime_congress" texturefile = "gfx/interface/goals/006_independence_wave/goal_independence_wave_hbx_convene_pacific_maritime_congress.dds" }
	spriteType = { name = "GFX_goal_independence_wave_hbx_convene_pacific_maritime_congress_shine" texturefile = "gfx/interface/goals/006_independence_wave/goal_independence_wave_hbx_convene_pacific_maritime_congress.dds" effectFile = "gfx/FX/buttonstate.lua" }

	# HAW — Hawaiʻi
	spriteType = { name = "GFX_goal_independence_wave_haw_reconcile_shipping_registers" texturefile = "gfx/interface/goals/006_independence_wave/goal_independence_wave_haw_reconcile_shipping_registers.dds" }
	spriteType = { name = "GFX_goal_independence_wave_haw_reconcile_shipping_registers_shine" texturefile = "gfx/interface/goals/006_independence_wave/goal_independence_wave_haw_reconcile_shipping_registers.dds" effectFile = "gfx/FX/buttonstate.lua" }
	spriteType = { name = "GFX_goal_independence_wave_haw_organize_island_coastwatch" texturefile = "gfx/interface/goals/006_independence_wave/goal_independence_wave_haw_organize_island_coastwatch.dds" }
	spriteType = { name = "GFX_goal_independence_wave_haw_organize_island_coastwatch_shine" texturefile = "gfx/interface/goals/006_independence_wave/goal_independence_wave_haw_organize_island_coastwatch.dds" effectFile = "gfx/FX/buttonstate.lua" }
	spriteType = { name = "GFX_goal_independence_wave_haw_seat_island_government_compact" texturefile = "gfx/interface/goals/006_independence_wave/goal_independence_wave_haw_seat_island_government_compact.dds" }
	spriteType = { name = "GFX_goal_independence_wave_haw_seat_island_government_compact_shine" texturefile = "gfx/interface/goals/006_independence_wave/goal_independence_wave_haw_seat_island_government_compact.dds" effectFile = "gfx/FX/buttonstate.lua" }
	spriteType = { name = "GFX_goal_independence_wave_haw_bind_shipping_supply_and_coastwatch" texturefile = "gfx/interface/goals/006_independence_wave/goal_independence_wave_haw_bind_shipping_supply_and_coastwatch.dds" }
	spriteType = { name = "GFX_goal_independence_wave_haw_bind_shipping_supply_and_coastwatch_shine" texturefile = "gfx/interface/goals/006_independence_wave/goal_independence_wave_haw_bind_shipping_supply_and_coastwatch.dds" effectFile = "gfx/FX/buttonstate.lua" }
	spriteType = { name = "GFX_goal_independence_wave_haw_settle_base_and_property_accounts" texturefile = "gfx/interface/goals/006_independence_wave/goal_independence_wave_haw_settle_base_and_property_accounts.dds" }
	spriteType = { name = "GFX_goal_independence_wave_haw_settle_base_and_property_accounts_shine" texturefile = "gfx/interface/goals/006_independence_wave/goal_independence_wave_haw_settle_base_and_property_accounts.dds" effectFile = "gfx/FX/buttonstate.lua" }
	spriteType = { name = "GFX_goal_independence_wave_haw_ratify_autonomous_pacific_mandate" texturefile = "gfx/interface/goals/006_independence_wave/goal_independence_wave_haw_ratify_autonomous_pacific_mandate.dds" }
	spriteType = { name = "GFX_goal_independence_wave_haw_ratify_autonomous_pacific_mandate_shine" texturefile = "gfx/interface/goals/006_independence_wave/goal_independence_wave_haw_ratify_autonomous_pacific_mandate.dds" effectFile = "gfx/FX/buttonstate.lua" }
	spriteType = { name = "GFX_goal_independence_wave_haw_dispatch_pacific_delegation" texturefile = "gfx/interface/goals/006_independence_wave/goal_independence_wave_haw_dispatch_pacific_delegation.dds" }
	spriteType = { name = "GFX_goal_independence_wave_haw_dispatch_pacific_delegation_shine" texturefile = "gfx/interface/goals/006_independence_wave/goal_independence_wave_haw_dispatch_pacific_delegation.dds" effectFile = "gfx/FX/buttonstate.lua" }
}
```

### Wiring notes

- Base and `_shine` names intentionally omit any trailing `_focus`; they exactly match the parent-provided identifiers.
- All 14 textures are native 94x86 focus canvases with transparent corners. Do not resize or substitute the shared Event 006 focus icons.
- `GFX_goal_independence_wave_hbx_convene_pacific_maritime_congress` is the distinct HBX maritime-congress/formable focus icon required by the Pacific branch.
- No advisor, leader, commander, portrait, flag, idea, decision, localisation, or GUI sprite is part of this handoff.
