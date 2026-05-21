# Event 005 Old Great Bulgaria Package

## Overview

Old Great Bulgaria is an Event 005 high-chaos Volga restoration successor. It spawns from the Soviet high-chaos successor pass when old-movement pressure is high, the Idel-Ural/Volga pressure chain has surfaced, and Soviet control still covers Kazan and Cheboksary.

The package uses two country variables:

- `ogb_volga_legitimacy`: public legitimacy from registers, charters, notables, schools, and the restored name.
- `ogb_river_authority`: practical control of ferries, toll roads, crossings, and trade movement.

## Runtime Flow

1. `can_soviet_collapse_spawn_ogb` checks high-chaos readiness, OGB nonexistence, the Volga pressure flag, old-movement pressure, and Soviet control of Kazan (`249`) and Cheboksary (`256`).
2. `soviet_collapse_spawn_ogb_if_enabled` transfers Kazan and Cheboksary to `OGB`, gives cores, and calls `soviet_collapse_setup_ogb_successor`.
3. Setup loads `OGB_soviet_collapse_focus_tree`, seeds Volga legitimacy and river authority, adds the disputed-name and restoration-council ideas, records the high-chaos evolution, and fires `chaosx.nr5_custom.36`.
4. The OGB decision category gives repeatable consolidation, ferry-line defense, and late restoration-state declaration actions.
5. The focus tree has restoration trunk, charter route choice, river trade, society, defense, Idel-Ural compact or rivalry, future-event hook, and late restoration payoff branches.

## Balance Notes

OGB increases Soviet old-movement pressure when it spawns and again on late trade-city/restoration payoffs. The pressure increases are the same small/medium constants used by other returned-name high-chaos packages, and the spawn gate requires old-movement pressure to be above the shared high-chaos gate so calm Soviet openings do not create OGB immediately.

The focus tree avoids single-reward vertical pacing. Rewards mix legitimacy variables, river authority variables, ideas, political power, stability, war support, manpower, stockpile equipment, infrastructure, factories, bunkers, anti-air, opinions, and Soviet crisis pressure.

## Icons and Assets

Current OGB wiring uses stable sprite keys in `interface/005_soviet_collapse_factory_ancient_icons.gfx`.

| Use | Sprite names | Current asset status |
| --- | --- | --- |
| Leader portrait | `GFX_portrait_OGB_volga_restoration_council` | Placeholder reuse of `gfx/leaders/005_soviet_collapse/IUL_leader.dds` |
| Decisions | `GFX_decision_ogb_consolidate_volga_registers`, `GFX_decision_ogb_guard_kazan_ferry_line`, `GFX_decision_ogb_declare_restoration_state` | Stable OGB-specific `gfx/interface/decisions/soviet_collapse/ogb_*.dds` files copied from themed Event 005 decision DDS sources |
| Ideas | `GFX_idea_ogb_disputed_restored_name`, `GFX_idea_ogb_volga_restoration_council`, `GFX_idea_ogb_volga_trade_road`, `GFX_idea_ogb_notable_workshop_compact`, `GFX_idea_ogb_heritage_guard`, `GFX_idea_ogb_old_capital_guard`, `GFX_idea_ogb_restored_volga_empire` | Stable OGB-specific `gfx/interface/ideas/soviet_collapse/ogb_*.dds` files copied from themed Event 005 and vanilla idea DDS sources |
| Focuses | `GFX_focus_OGB_*` and matching `_shine` variants | 23 per-focus `gfx/interface/goals/soviet_collapse/ogb_*.dds` files copied from Bulgaria, Volga, trade, defense, diplomacy, and restoration-themed DDS sources |

Final bespoke OGB leader art remains an asset follow-up. The focus tree, decision icons, and idea icons no longer point at shared placeholder DDS paths; later fully bespoke art can supersede the stable `ogb_*.dds` files without changing gameplay IDs.

## Future Hooks

`OGB_future_bulgaria_file` sets `ogb_future_bulgaria_event_hook`. A future event can read that flag, `ogb_volga_legitimacy`, `ogb_river_authority`, and the Idel-Ural route flags to branch between compact, rivalry, and expansion outcomes.
