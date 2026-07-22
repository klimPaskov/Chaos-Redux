# Event 006 BRI regionalist portrait - parent wiring handoff

This package does not edit `.gfx`, gameplay, localisation, country history, or
the runtime texture folder. It supplies a source-preserving portrait candidate
for the existing BRI civic-delegate leader.

## Existing sprite to preserve

```text
spriteType = {
	name = "GFX_portrait_BRI_independence_wave_civic_commission"
	texturefile = "gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_civic_commission.dds"
}
```

Definition: `interface/006_independence_wave_brittany_portraits.gfx`  
Character token: `BRI_independence_wave_civic_delegate`  
Role branches: traditional regionalist compact; protected-ports patron  
Subject: Régis de l'Estourbeillon, grounded male Breton regionalist civic figure

## Current revision 3 art

- unchanged source master: `source_png/leader_bri_regionalist_regis_de_l_estourbeillon_john_wickens_1904_source_master.jpg` (`1145x1707`, RGB, SHA-256 `C310F1D916A578FD4E3C5B9ADAC4D4737DA6D841D02D5EA59F66C4589AE9230D`)
- prior v2 raw/processed evidence remains in `source_png/leader_bri_regionalist_regis_de_l_estourbeillon_imagegen_master.png` and `processed_png/leader_bri_regionalist_regis_de_l_estourbeillon.png`
- v3 raw ImageGen master: `source_png/leader_bri_regionalist_regis_de_l_estourbeillon_imagegen_master_v3.png` (`1082x1454`, RGB, SHA-256 `660E954102CC6DF902792E84D0B0F97F178351476485A008362E64A1610E8120`)
- v3 processed review PNG: `processed_png/leader_bri_regionalist_regis_de_l_estourbeillon_v3.png` (`156x210`, opaque RGB, SHA-256 `5426E39BC1622E7ECD32A41CC0A1C05D6596446A40FA0B7BA2047EF350BBAE80`)
- v3 visual comparison: `contact_sheets/bri_regionalist_v3_comparison.png` (source/v2/v3 plus male vanilla HOI4 refs)
- final runtime DDS: deferred to parent; expected path `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_civic_commission.dds`

The v3 candidate is visibly full-color with a restrained 1930s HOI4-painted
finish rather than sepia or photographic treatment. The parent should still
independently review the face, gaze, age appearance, hat, silhouette, and
visible costume against the unchanged John Wickens source before conversion.
If identity drift or invented costume detail is judged material, fail closed:
reject v3 and keep the civic slot blocked. Do not wire v2/v1 without review,
the Dulac illustration, a generated or generic face, a female identity, an
advisor, or an operative.

## Suggested parent actions

1. Review `contact_sheets/bri_regionalist_v3_comparison.png` and the unchanged
   source master against the v3 processed portrait.
2. If likeness, costume, and full-color HOI4 finish are accepted, convert the
   v3 processed RGB PNG with
   `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` to the
   existing runtime texture path.
3. Preserve the existing sprite name and `.gfx` declaration; no duplicate
   declaration is needed.
