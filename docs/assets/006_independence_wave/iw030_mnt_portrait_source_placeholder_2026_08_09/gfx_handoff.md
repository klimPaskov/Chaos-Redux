# IW-030 Montenegro portrait GFX handoff

Runtime sprites are registered in `interface/006_independence_wave_iw030_montenegro_portraits.gfx`.

- `GFX_portrait_MNT_independence_wave_kristo_popovic` -> `gfx/leaders/006_independence_wave/portrait_MNT_kristo_popovic.dds`
- `GFX_portrait_MNT_independence_wave_blazo_jovanovic` -> `gfx/leaders/006_independence_wave/portrait_MNT_blazo_jovanovic.dds`
- `GFX_portrait_MNT_independence_wave_mitar_martinovic` -> `gfx/leaders/006_independence_wave/portrait_MNT_independence_wave_mitar_martinovic.dds`

`MNT_kristo_popovic` and `MNT_blazo_jovanovic` are vanilla characters. Event 006 changes their portraits only inside the IW-030 roster checkpoint through character-scoped `set_portraits`. `MNT_independence_wave_mitar_martinovic` is defined in `common/characters/006_independence_wave_montenegro_characters.txt`, recruited exactly once by `chaosx.nr6.350`, and owns civilian-large plus army-large consumers. There are no advisor, high-command, dossier, or small portrait consumers.
