# IW-009 Bavaria portrait refinishes — GFX handoff

Heinrich Held passed the independent likeness, HOI4 leader-style, role, and provenance gates and is promoted to the existing stable runtime DDS path.
Eugen Ritter von Schobert passes likeness and HOI4 commander style but fails the separate source-rights gate, so his evidence DDS is not wired.
No `.gfx`, gameplay, localisation, character, advisor, dossier, or `_small` source change was needed for Held's bounded promotion.

| Role | Stable sprite name | Existing target `.gfx` | Deferred runtime DDS | Trial docs-only DDS | Processed PNG | Status |
|---|---|---|---|---|---|---|
| Heinrich Held, civic country leader | `GFX_portrait_BAY_independence_wave_state_council` | `interface/006_independence_wave_region_01_portraits.gfx` | `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_state_council.dds` | `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bavaria_held_schobert_trial_01/docs_dds/BAY_heinrich_held_refinish_156x210.dds` | `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bavaria_held_schobert_trial_01/processed_png/BAY_heinrich_held_refinish_156x210.png` | `promoted`; runtime/evidence DDS SHA-256 `999857d191f7b088e11daa78fb29eadd0b514dc6da494a0102423c635e736e95` |
| Eugen Ritter von Schobert, army/corps commander | `GFX_portrait_BAY_independence_wave_mountain_commandant` | `interface/006_independence_wave_region_01_portraits.gfx` | `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_mountain_commandant.dds` | `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bavaria_held_schobert_trial_01/docs_dds/BAY_eugen_von_schobert_refinish_156x210.dds` | `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bavaria_held_schobert_trial_01/processed_png/BAY_eugen_von_schobert_refinish_156x210.png` | `blocked_provenance`; do not wire |

The existing definitions already point to the stable runtime paths:

```text
spriteType = {
	name = "GFX_portrait_BAY_independence_wave_state_council"
	texturefile = "gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_state_council.dds"
}

spriteType = {
	name = "GFX_portrait_BAY_independence_wave_mountain_commandant"
	texturefile = "gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_mountain_commandant.dds"
}
```

The engine-facing textures are full `156x210` portraits.
Event 006 has no authorized BAY advisor, dossier, commander `_small`, or flag work in this trial.
The canonical reference files under `.agents/skills/chaos-redux-event-assets/assets/` are style-only and must never be wired or copied to runtime.

See `manifest.md`, both `metadata/*.json` records, the Held exact-crop JSON, the frozen prompts, the independent audit, and the native/4x comparison sheets for provenance, crop coordinates, hashes, ownership scan, and the remaining commander blocker.
