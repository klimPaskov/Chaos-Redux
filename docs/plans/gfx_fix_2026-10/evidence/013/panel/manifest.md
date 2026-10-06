# Event 013 damaged abnormal-map panel asset manifest

Status: the parent accepted candidate 04 and the verified candidate DDS is installed at the existing runtime texture path. Matching synthetic baseline and post-change GUI renders are captured and visually compared; full GUI acceptance remains unresolved because gui_inspect timed out and the render retains one root-visibility fidelity item plus layout/state warnings.

Event: 013, natural_disasters.

Requirement: repair the damaged abnormal-map panel so the damaged state visibly differs from the clean panel through cracked glass in the main pane, a soot mark in one corner, and a torn left paper edge while preserving the layout grid.

Acceptance basis: the parent task cites the user's accepted row in C:/Users/klimp/Videos/chaos_redux_trailer/records/gfx_review/gfx_fix_plan.md:596 and explicitly accepts candidate 04 after reviewing it at 760x520 against the saved original.

| Asset | Type and consumer | Source and review | Current status |
|---|---|---|---|
| GFX_013_abnormal_disaster_panel_damaged | Opaque scripted-GUI background texture for natural_disaster_gui_damaged_panel in natural_disaster_abnormal_path_window. | Candidate 04 was created with built-in ImageGen from candidate 03, reviewed at 760x520, accepted by the parent, and rendered in a matched synthetic GUI fixture. | Installed through the preexisting sprite and GUI references; full GUI acceptance and live-game validation remain unresolved. |

Runtime path: gfx/interface/013_natural_disasters/013_abnormal_disaster_panel_damaged.dds.

Existing registration: interface/013_natural_disasters.gfx defines GFX_013_abnormal_disaster_panel_damaged with that texture path; no .gfx source edit was made.

Existing GUI element: interface/013_natural_disasters.gui defines natural_disaster_gui_damaged_panel as an iconType using GFX_013_abnormal_disaster_panel_damaged at position 0,0 and scale 1.43.

Existing normal comparison: GFX_013_abnormal_disaster_panel remains at gfx/interface/013_natural_disasters/013_abnormal_disaster_panel.dds and its runtime file hash is unchanged.

Original decoded source: docs/assets/gfx_fix_parent_2026-10/013_damaged_before.png, 760x520 RGBA, fully opaque, SHA-256 d11a64d6eb077db0cdd34172f514f4cced12b1fc9b91efe214690ae7ca08d339.

Original runtime damaged DDS archived before replacement: source_dds/013_abnormal_disaster_panel_damaged_original.dds, SHA-256 c79bd8e079371fc5e0a725c798f1682a669edb23fbcc6fdd19479e311be8489b.

ImageGen source mode: built-in ImageGen edit, not the CLI. Candidate 04's tool output is retained in source_png/013_damaged_candidate_04.png and the tool-reported original is C:/Users/klimp/.codex/generated_images/01a10fb9-ed3a-7270-ae92-27621d89b0be/exec-9bddd06f-c8b4-4b26-90c2-888e2bc282cd.png.

Selected source PNG: source_png/013_damaged_candidate_04.png, 1516x1038 RGB, SHA-256 DC09317F3C9C10A2475701986DAB6CFD1B546DCD360BF65805DBA29C999E79D4.

Processed PNG: processed_png/013_abnormal_disaster_panel_damaged_760x520.png, 760x520 RGB, SHA-256 08841104c570eae069affcfa10b47c58e477bb796bdce49be4f3a65db1384d37.

Temporary candidate DDS: processed_png/013_abnormal_disaster_panel_damaged_760x520.dds, 760x520, SHA-256 68e5b6d2b49dd87ed8491d04ac88644138773eb6a663b045c9b71ce273ec4978.

Installed runtime DDS: gfx/interface/013_natural_disasters/013_abnormal_disaster_panel_damaged.dds, 760x520, 1,580,928 bytes, SHA-256 68e5b6d2b49dd87ed8491d04ac88644138773eb6a663b045c9b71ce273ec4978.

Background mode: consumer_opaque; the saved original has alpha 255 throughout, the generated and processed PNGs are RGB, and the final BGRA DDS has alpha 255 throughout.

Conversion command: python -B .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --input docs/assets/gfx_fix_disaster_panel_resume/processed_png/013_abnormal_disaster_panel_damaged_760x520.png --output docs/assets/gfx_fix_disaster_panel_resume/processed_png/013_abnormal_disaster_panel_damaged_760x520.dds --width 760 --height 520.

DDS evidence: the final file has the 128-byte standard header, DDS_HEADER size 124, pixel-format size 32, flags 65, 32-bit BGRA masks, DDSCAPS_TEXTURE 0x1000, no mipmaps, exact dimensions 760x520, and expected length 128 + 760*520*4.

Round-trip evidence: processed_png/013_abnormal_disaster_panel_damaged_760x520_dds_roundtrip.png is pixel-identical to the processed PNG after decoding the candidate DDS.

Candidate lineage and exact prompts: prompts/candidate_01.md through prompts/candidate_04.md record each input role, prompt, tool output, retained path, dimensions, hash, review status, and selection decision.

Candidate 01 was rejected because soot covered much of the right detail pane and the left edge was over-torn.

Candidate 02 was rejected because the corner soot cue was not distinct enough.

Candidate 03 was retained as candidate 04's parent because its crack and tear were close to target, but the soot remained too faint.

Candidate 04 is selected and parent-accepted because its central crack is distinct, damage stays localized, and the five slots, dividers, pane grid, and usable regions remain aligned.

Reference and native-element mapping: reference_mapping.md.

GUI evidence: the initial narrow fixture failed, then a source-derived fixture resolved the damaged and normal panel states and visible localization values. Matching baseline and post-change artifacts are recorded in docs/plans/gfx_fix_2026-10/013_panel_handoff.md.

The clean panel, GUI source, scripted-GUI source, GFX registration, localisation, gameplay, decisions, and shared interfaces were not modified.
