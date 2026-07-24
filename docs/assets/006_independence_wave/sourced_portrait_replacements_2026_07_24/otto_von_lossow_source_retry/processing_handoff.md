# Otto von Lossow processing handoff

Status: `blocked_imagegen_safety_no_runtime_asset`.

The unchanged archival master is `source_masters/OTTO_von_lossow_bain_1923_original.jpg`.

The original crop `source_crops/OTTO_von_lossow_bain_1923_head_shoulders_2000_400_8000_7000.png` was rejected because it is a face close-up rather than an explicit head-and-shoulders crop.

The corrected crop is `source_crops/OTTO_von_lossow_bain_1923_head_shoulders_1300_0_7763_8700.png`, using source coordinates `(1300,0)-(7763,8700)`.

It visibly contains Lossow's full head, face, neck, and both shoulders, but necessarily retains parts of the military collar and shoulder decoration.

The corrected crop was submitted to ImageGen with a source-locked identity-preserving HOI4 commander prompt that explicitly removed all insignia and unsupported symbols.

The safety system rejected the request and returned no output.

Do not retry this photograph, bypass the safety block, overwrite the source files, or use a filtered/resized photograph as final runtime art.

A different rights-clear, symbol-safe archival photograph of Lossow or a separately researched non-owned Bavarian male commander is required before this consumer can proceed.

Proposed target from the Bavaria retry package: stable token `BAY_independence_wave_mountain_commandant`, sprite `GFX_portrait_BAY_independence_wave_mountain_commandant`, runtime path `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_mountain_commandant.dds`. Treat this as a parent confirmation point, not an automatic wiring instruction.

No ImageGen output, processed `156x210` PNG, DDS, `.gfx` edit, gameplay edit, localisation edit, advisor/dossier/`_small` derivative, or fallback exists in this handoff.

Open review item: Commons clearly records `PD-US`, but the 1923 file page gives Bain News Service as source agency without an LOC catalog/LCCN or worldwide rights statement. Keep the provenance caveat attached through independent review.
