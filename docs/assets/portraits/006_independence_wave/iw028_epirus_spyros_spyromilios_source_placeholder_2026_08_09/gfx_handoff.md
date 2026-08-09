# IW-028 Epirus commander portrait GFX handoff

- Character token: `BBX_independence_wave_spyros_spyromilios`.
- Role: male historical army corps commander.
- Sprite: `GFX_portrait_BBX_independence_wave_spyros_spyromilios`.
- Target `.gfx`: `interface/006_independence_wave_iw028_epirus_portraits.gfx`.
- Runtime texture: `gfx/leaders/006_independence_wave/portrait_BBX_independence_wave_spyros_spyromilios.dds`.
- Runtime size and format: full `156x210` legacy one-level uncompressed BGRA32 DDS.
- Ready definition:

```text
spriteType = {
	name = "GFX_portrait_BBX_independence_wave_spyros_spyromilios"
	texturefile = "gfx/leaders/006_independence_wave/portrait_BBX_independence_wave_spyros_spyromilios.dds"
}
```

- Character definition uses `army = { large = GFX_portrait_BBX_independence_wave_spyros_spyromilios }` only.
- No advisor, high-command, dossier, or small portrait is authorized for this requirement.
- Georgios Christakis-Zografos remains the political leader on `BBX_independence_wave_epirus_council`; the old corps-commander role was split out to this token.
- The runtime DDS is a sourced `source_placeholder`, not a generated or styled replacement. The user may supply a HOI4-style final later at the same runtime path if explicitly requested.
- Independent parent visual review: PASS. The parent confirmed identity preservation, a clear male military subject, and readable head-and-shoulders framing; the producer did not self-approve the identity gate.
