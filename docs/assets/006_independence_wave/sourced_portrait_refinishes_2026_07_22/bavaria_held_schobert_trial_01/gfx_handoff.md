# IW-009 Bavaria portrait refinishes — deferred GFX handoff

Both rows are **`needs_independent_review`**. This note is a handoff only; it
does not edit `.gfx`, runtime DDS, gameplay, localisation, or character files.
Do not wire either candidate until an independent reviewer accepts the direct
source likeness, rights basis, role/era fit, and visibly painted HOI4 finish.

| Role | Stable sprite name | Existing target `.gfx` | Deferred runtime DDS | Trial docs-only DDS | Processed PNG | Status |
|---|---|---|---|---|---|---|
| Heinrich Held, civic country leader | `GFX_portrait_BAY_independence_wave_state_council` | `interface/006_independence_wave_region_01_portraits.gfx` | `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_state_council.dds` | `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bavaria_held_schobert_trial_01/docs_dds/BAY_heinrich_held_refinish_156x210.dds` | `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bavaria_held_schobert_trial_01/processed_png/BAY_heinrich_held_refinish_156x210.png` | `needs_independent_review` |
| Eugen Ritter von Schobert, army/corps commander | `GFX_portrait_BAY_independence_wave_mountain_commandant` | `interface/006_independence_wave_region_01_portraits.gfx` | `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_mountain_commandant.dds` | `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bavaria_held_schobert_trial_01/docs_dds/BAY_eugen_von_schobert_refinish_156x210.dds` | `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bavaria_held_schobert_trial_01/processed_png/BAY_eugen_von_schobert_refinish_156x210.png` | `needs_independent_review` |

If approved, the main agent should preserve the stable sprite names and point
the existing definitions to the existing runtime paths. Suggested structure
(for review only; **do not paste before approval**):

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

The engine-facing textures are full `156x210` portraits. Event 006 currently
has no authorized BAY advisor, dossier, commander `_small`, or flag work in
this trial. The canonical reference files under
`.agents/skills/chaos-redux-event-assets/assets/` are style-only and must never
be wired or copied to runtime.

See `manifest.md`, both `metadata/*.json` records, the frozen prompts, and the
native/4x comparison sheets for provenance, crop coordinates, hashes, ownership
scan, rights uncertainty, and review requirements.
