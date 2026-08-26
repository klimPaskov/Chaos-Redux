# IW-045 Bashkiria corridor guard repair

Date: 2026-08-26

## Finding

The IW-045 `independence_wave_bsk_open_ural_network_corridor` decision checked the nonexistent flag `independence_wave_bsk_volga_river_corridor_open`. Its completion helper and cleanup use the actual package receipt `independence_wave_bsk_volga_ural_corridor_open`, written by `independence_wave_bsk_focus_open_volga_ural_corridor` and cleared at setup and cleanup. The decision could therefore remain visible after completion and be started again whenever its other gates were still satisfied.

## Patch

`common/decisions/006_independence_wave_bashkiria_mari_decisions.txt:509` now checks `independence_wave_bsk_volga_ural_corridor_open`, matching the package effect writer, setup reset, and cleanup reset. No new flag or alias was introduced.

## Boundary

This is a package-local visibility guard repair. It does not alter the IW-045 admission gate, package identity, state-651 anchor, host ledger, force mapping, focus graph, costs, AI weights, localisation wording, assets, or the 32/161 whole-event boundary. The existing user-requested source-layout consolidations remain independent of this gameplay fix.

## Validation

The focused source scan now finds no `independence_wave_bsk_volga_river_corridor_open` reference and finds the same `independence_wave_bsk_volga_ural_corridor_open` receipt in the decision guard, focus helper, setup reset, and cleanup reset. The six scoped static validators all passed after the patch. A bounded `hoi4.event_inspect` lint returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics at revision `43388d6b2737a1c8e2409f324449210941414fee69c903a1c69d441ca9d33b97`; its linked artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d00ed37074f450ff0c615f47f8a5bdc5a3a8b0cfbc19381abd75d1dcadc965fc/28451f50122bce9216e4f27257e36bb444517baccebac3ea004fccb591f5de78/event-lint-43388d6b2737.json`. The matching overview render returned `EVENT_RENDERED_PARTIAL` with zero blocking diagnostics and manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2c28202d93ce6f7451ee4d9241837cd5c2beeaf68966cd0bdc496b7ef786ea1e/5a1c33b1ec44a54bf547b7f53497c5903ebf477eff135ac0f3de2ef919fbd505/event-overview-43388d6b2737-manifest.json`. The workspace deferred large helper/lifecycle projections, so no live parser or runtime receipt is claimed.
