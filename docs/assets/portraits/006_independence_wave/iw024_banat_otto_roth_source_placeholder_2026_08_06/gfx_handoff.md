# IW-024 Banat Otto Roth portrait GFX handoff

The source-placeholder DDS is ready at `gfx/leaders/006_independence_wave/portrait_AXX_independence_wave_otto_roth.dds`.

The portrait-specific sprite is already registered in `interface/006_independence_wave_iw024_banat_portraits.gfx`:

```text
spriteType = {
	name = "GFX_portrait_AXX_independence_wave_otto_roth"
	texturefile = "gfx/leaders/006_independence_wave/portrait_AXX_independence_wave_otto_roth.dds"
}
```

This is a full `156x210` country-leader portrait texture for character key `otto_roth`. No advisor, dossier, commander-small, mini, female, or alternate portrait surface is authorized. The complete source, crop, processing, rights, hashes, review state, and package-admission gate are in `manifest.md` and `source_provenance.json`.

The runtime DDS is a `131168`-byte, one-level, uncompressed BGRA texture with an exact decoded-pixel match to the processed PNG. Runtime consumers must use the stable `.gfx` sprite and must not point into `docs/assets/portraits/`.

The AXX package contract is now admitted conditionally through the central Event 006 dispatcher, and the parent-owned character, localisation, setup, map anchor, focus, decision, idea, party, and AI wiring is present in the package files. This handoff remains asset evidence only and does not authorize any advisor, dossier, small-portrait, or alternate portrait surface.
