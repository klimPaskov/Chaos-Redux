# IW-002 Wales sourced portrait GFX handoff

This is a source-only handoff. No `.gfx` file was edited and no DDS was created.

| Consumer | Stable identifier | Future runtime path |
| --- | --- | --- |
| Wales corps commander, full army/civilian large portrait | `WLS_independence_wave_mountain_commandant` / `GFX_portrait_WLS_independence_wave_mountain_commandant` | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds` |

The parent-owned consumer declaration is `interface/006_independence_wave_region_01_portraits.gfx:67-68`.

The future processor must create and audit the full `156x210` commander-family texture from the unchanged source master and explicit crop before the parent wires this stable sprite. No advisor, dossier, `_small`, alternate, generic, or fallback sprite is implied.
