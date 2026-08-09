# Event 012 Africa super-event image GFX handoff

This package owns exactly four generated super-event images and keeps the existing runtime sprite names, texture paths, and 457x328 consumer size unchanged.

| Slot | Sprite name | Final DDS | Target `.gfx` | Use note |
| --- | --- | --- | --- | --- |
| 101 | `GFX_super_event_012_africa_africa_is_one` | `gfx/super_events/012_africa/super_event_012_africa_africa_is_one.dds` | `interface/012_africa_event_pictures.gfx` | Africa-wide congress, rail and harbor continuity, dignified political completion. |
| 102 | `GFX_super_event_012_africa_scramble_response` | `gfx/super_events/012_africa/super_event_012_africa_scramble_response.dds` | `interface/012_africa_event_pictures.gfx` | Fortified African harbor command facing distant outside fleets, sanctions and expedition pressure. |
| 103 | `GFX_super_event_012_africa_continental_wars` | `gfx/super_events/012_africa/super_event_012_africa_continental_wars.dds` | `interface/012_africa_event_pictures.gfx` | Shattered railway crossing between two continent-scale forces, period equipment and human scale. |
| 104 | `GFX_super_event_012_africa_the_world` | `gfx/super_events/012_africa/super_event_012_africa_the_world.dds` | `interface/012_africa_event_pictures.gfx` | Diverse exhausted council around an empty final seat, six-part seal and postwar finality. |

The parent should preserve the existing sprite definitions and only verify that the texture files resolve to the final DDS paths above. No `.gfx` file was edited in this handoff.

Source masters, processed PNGs, decoded DDS round-trips, prompts, hashes, and the contact sheet are under `docs/assets/012_africa/super_events/images_final/`.

## Ignored or superseded material

- `docs/assets/012_africa/super_events/current_runtime_previews/` contains inspection-only PNG decodes of the old runtime DDS files and is not a source or final asset.
- The first generated The World candidate `exec-31479ca9-8254-4fa3-9edf-4da620a4a581.png` was not promoted because its council read too narrowly as a Western-only body; the selected `exec-d8884dbc-93d4-4689-854e-e6216e06c3d1.png` is the diverse final source.
- No fifth role, host variant, route variant, icon, portrait, news image, or animation is included in this package.

