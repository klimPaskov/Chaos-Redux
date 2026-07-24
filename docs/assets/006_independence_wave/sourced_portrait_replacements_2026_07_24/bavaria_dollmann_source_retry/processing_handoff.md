# IW-009 Bavaria commander source processing handoff

This handoff covers the source-only Friedrich Dollmann retry for grounded male commander token `BAY_independence_wave_mountain_commandant`.

The selected identity source is `source_masters/BAY_friedrich_dollmann_bundesarchiv_1940_original_533x800.jpg` and the exact identity crop is `source_crops/BAY_friedrich_dollmann_head_shoulders_300_120_500_450.png` with crop `(300,120)-(500,450)`.

The unchanged master is the original 533x800 Bundesarchiv image uploaded to Commons in 2008, not the current 511x800 horizontally cropped derivative.

The source master SHA-256 is `15D387707C22E7B73B513961AAE7EB42F40E3E296FF4A68E8AAB6B5DA6E82E12`.

The crop is a direct no-resample 200x330 grayscale PNG with SHA-256 `C19C7D634EE585CB32853ED1A0F28BC4D37724AEAC2F58FF2509E20DE6C9B071`.

The source comparison evidence is `evidence/BAY_friedrich_dollmann_source_master_crop_comparison.png` with SHA-256 `58B36189021E1D5F83D3A5A627B92CB7747EF79FE6DACE694DCBB10812E8CD18`.

The source attribution to retain is `Bundesarchiv, Bild 101I-052-1435-20 / CC-BY-SA 3.0` under <https://creativecommons.org/licenses/by-sa/3.0/de/deed.en>.

The source page is <https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_101I-052-1435-20,_Oberrhein,_Befestigung_am_Isteiner_Klotz.jpg> and the exact unchanged archived original is <https://upload.wikimedia.org/wikipedia/commons/archive/1/11/20220702180551%21Bundesarchiv_Bild_101I-052-1435-20%2C_Oberrhein%2C_Befestigung_am_Isteiner_Klotz.jpg>.

The official archive record is <https://www.bild.bundesarchiv.de/dba/de/search/?query=Bild+101I-052-1435-20>.

The stable sprite is `GFX_portrait_BAY_independence_wave_mountain_commandant`.

The parent-owned `.gfx` consumer remains `interface/006_independence_wave_region_01_portraits.gfx`.

The reserved runtime texture remains `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_mountain_commandant.dds`.

No DDS is present or proposed in this source-only retry.

No ImageGen output, processed `156x210` candidate, final portrait PNG, `.gfx` edit, gameplay edit, localisation edit, workbook edit, skill edit, or fallback is present.

The next processing pass must use the exact crop as the sole identity input, use the canonical commander references under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/` for style only, preserve Dollmann's face geometry and source-supported pose, avoid inventing hidden uniform detail, and stop for an independent likeness/style/provenance audit before conversion or runtime wiring.

The exact alternate-role wording is: `Friedrich Dollmann is used here as Bavaria's emergency passes-and-depots commandant; this is a territorial-command abstraction, not a claim of historical Gebirgstruppe service.`

The package status is `source_ready_needs_user_review` and is not runtime-ready.
