# Event 016 Directorate current GUI evidence — 2026-09-25

## Scope and source

This is a read-only refresh of the existing `kruger_directorate_container` in `interface/016_brilliant_scientist_directorate.gui` and `common/scripted_guis/016_brilliant_scientist_directorate_scripted_gui.txt`.
No geometry, script, art, or localisation was changed for this review.
The earlier actual-text and severe-state review remains in `016_final_directorate_gui_closure_2026-09-02.md`; its older source revision is not substituted for current evidence.

## Explicit current fixtures

Both fixtures disabled generated scenarios, rendered the normal state at 1366×768, 1920×1080, and 2560×1440 with UI scale 1, and supplied explicit element visibility because the offline inspector does not evaluate nested scripted-GUI country-flag visibility reliably.

| Scenario | Compact panel | Full panel | Open control | Close control | MCP source revision |
| --- | --- | --- | --- | --- | --- |
| `event016_directorate_current_collapsed` | visible | hidden | visible | hidden | `72df8ccbe31b6e27a7b07ad1f41ab59bac0852180b25d98197447dc43f98ea38` |
| `event016_directorate_current_expanded` | hidden | visible | hidden | visible | `72b5d3058c2feb8e8b57a658c1fd81fa69d9b53d59e44976661e84dfbeee506a` |

The collapsed `hoi4.gui_inspect` returned `GUI_INSPECTED`, passed validation, inspected 22 elements, and reported no blocking click-region conflict.
Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5e360b43fd0b8fb90a626e0950aadc3042860c7fec70ff56abd6ac96139b3d4f/ee476ebde038e29ec60d76e9992161f1e8613f0de28ab3d568bf35173b67402d/gui-inspect.6536ab67af3ec0e4.json` with shared revision `6536ab67af3ec0e486e16ddc83fad61b90a954365c52aca9f96392aaaea04511`.

## Visual review

The current collapsed full-window image shows the 500×58 title bar, `Kruger Directorate` title, and open control, with no expanded content or visible clipping.
Its click-region image shows only `kruger_directorate_open_button` at the control.
The current expanded image shows the portrait, four meters, title, and close control inside the 500×360 frame; its click-region image shows only `kruger_directorate_close_button`.
The three-resolution expanded matrix shows the same composition without a newly visible overlap or off-canvas element.
Both render calls returned `GUI_RENDERED` with validation passed and no blockers.

| Artifact | MCP URI |
| --- | --- |
| Collapsed full PNG | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4be3c43ca18b2c4f63b930e1a93b6e10e00c4d4ca41bf8d43a8903eee4f0a6e9/0243ddc5e120fa67194b6802f20d462a07a847cb4be8e6ea7ad3aeae463adc9a/kruger_directorate_container-full.png` |
| Collapsed click regions | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/93d5fc3f7d08fad63b749e46aec81a09bc6539c91e8daadb0b01c1c1cbdca1f1/2c1fb3d2c37a83092f71720332a5ff95617565d8e7f09572b0bd43f7e791d61d/kruger_directorate_container-click-regions.png` |
| Expanded full PNG | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/24d665afd5adf6cd5a583d7dae9f9eb9b5a940c6b9d8ba237f84369cc59e3dd0/cf9a3fe826474fdf4ee614c57fd00e4054fa33c8fe4ddd6e7e5c00449798fbcc/kruger_directorate_container-full.png` |
| Expanded click regions | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/474cfa20cab8a12d182bef6fbcdbac097bd7766c9554215b54b0aa6f8f629bbf/ce0f34a8849b6780d1d3f39039d7b2f6bf3564a5da2cf8fbecd9c9b09070c0fc/kruger_directorate_container-click-regions.png` |
| Expanded resolution matrix | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/97b70aa086994f87991028a5a29c82832ac974dd65918f7094d97d2f98725dba/b0b65ab5ec43adf71a609173d72a3ecc8b0ed81d39f7a0ee9d1b496df8dfb9c8/kruger_directorate_container-resolution-scale.png` |
| Expanded fidelity | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8a50e6872610ef5983c16e4dc6fcc52011e4e3e533e2cf76b30e8f1a76770e07/e43804161044e43a9378bb5c87518fb2139b39990f47c0febfc1d081fd8506de/kruger_directorate_container-fidelity.json` |

## Limits and disposition

This fixture establishes current layout and visible click-region behavior for the explicit compact/full states, not runtime evaluation of the country flag or actual in-game text.
The generic expanded fixture leaves four numeric values and three dynamic-localisation text fields unresolved, so it displays `[X]` and `[dynamic_loc]` placeholders; those placeholders are fixture limits, not accepted player-facing copy.
The fidelity report also says the offline renderer does not execute `Effect gfx/FX/buttonstate.lua`.
Actual-text and severe-state evidence from the 2026-09-02 handoff must be refreshed against current source if those surfaces change or before an unqualified current visual completion claim.
No implementation change or live-game acceptance is claimed here.
