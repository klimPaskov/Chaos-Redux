# Fallout successor B7 USA asset manifest

Status: dedicated final art is required before the USA continuity package can pass its asset gate. The dormant pilot uses installed vanilla sprites only for structural review and does not present them as final Fallout art.

## Focus sprites

| Runtime sprite | Target source path | Use |
| --- | --- | --- |
| `GFX_goal_fallout_usa_federal_continuity_ledger` | `gfx/interface/goals/fallout_successor_b7_usa/federal_continuity_ledger.dds` | Federal ledger opening |
| `GFX_goal_fallout_usa_shelter_registry` | `gfx/interface/goals/fallout_successor_b7_usa/shelter_registry.dds` | Shelter registry |
| `GFX_goal_fallout_usa_supply_corridors` | `gfx/interface/goals/fallout_successor_b7_usa/supply_corridors.dds` | Inland corridors |
| `GFX_goal_fallout_usa_guard_compacts` | `gfx/interface/goals/fallout_successor_b7_usa/guard_compacts.dds` | Guard compacts |
| `GFX_goal_fallout_usa_bilateral_reconstruction` | `gfx/interface/goals/fallout_successor_b7_usa/bilateral_reconstruction.dds` | Regional partner charters |
| `GFX_goal_fallout_usa_continental_radio_net` | `gfx/interface/goals/fallout_successor_b7_usa/continental_radio_net.dds` | Radio network |
| `GFX_goal_fallout_usa_federal_reconstruction` | `gfx/interface/goals/fallout_successor_b7_usa/federal_reconstruction.dds` | Reconstruction capstone |

## Idea sprites

| Runtime sprite | Target source path | Use |
| --- | --- | --- |
| `GFX_idea_fallout_usa_federal_continuity_ledger` | `gfx/interface/ideas/fallout_successor_b7_usa/federal_continuity_ledger.dds` | Opening ledger |
| `GFX_idea_fallout_usa_shelter_registry` | `gfx/interface/ideas/fallout_successor_b7_usa/shelter_registry.dds` | Shelter institution |
| `GFX_idea_fallout_usa_guard_compact` | `gfx/interface/ideas/fallout_successor_b7_usa/guard_compact.dds` | Guard institution |
| `GFX_idea_fallout_usa_federal_reconstruction` | `gfx/interface/ideas/fallout_successor_b7_usa/federal_reconstruction.dds` | Reconstruction institution |

## Wiring gate

The main agent must register the focus sprites in `interface/fallout_successor_b7_usa.gfx` and the idea sprites in the same GFX handoff after reviewed DDS files exist. The gameplay pilot keeps the vanilla references until that registration can be made without missing files. No Zombie Apocalypse asset, audio, sprite, or path is reused.

## Review requirements

Each final image needs a source record, generated or sourced provenance, DDS conversion evidence, dimensions, alpha validation, and a runtime sprite handoff. Fictional USA continuity imagery must use the approved event-asset workflow and remain distinct from real-person portraits and attested flags.
