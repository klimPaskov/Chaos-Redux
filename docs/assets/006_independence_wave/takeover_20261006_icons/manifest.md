# Event 006 generated icon and animation package

This package contains the approved Event 006 icon replacements, five exact-geometry formable-state pairs, one decorative eight-frame status overlay, and the installed recognition-strip state-0 replacement.

The parent authorized the visual repair tranche and later accepted the G5/G6 correction for a state-neutral bronze ornament loop. Built-in ImageGen was used for every new subject and animation frame with native transparency requested; the available tool exposes no model selector, so no backend model is claimed.

## Generated static icons

| Asset | Sprite and owning GFX | Canvas | Source and prompt | Processed preview | Runtime DDS |
| --- | --- | ---: | --- | --- | --- |
| Recognition idle seal | GFX_independence_wave_recognition_seal_static in interface/006_independence_wave.gfx | 64x64 | source/imagegen/recognition_seal_static_v1.png; prompts/recognition_seal_static.json | processed/independence_wave_recognition_seal_static.png | gfx/interface/006_independence_wave/animations/independence_wave_recognition_seal_static.dds |
| League Reserve texticon | GFX_independence_wave_form03_league_reserve_texticon in interface/006_independence_wave_small_assets.gfx | 18x18 | source/imagegen/league_reserve_texticon_v2.png; prompts/league_reserve_texticon_v2.json | processed/independence_wave_form03_league_reserve_texticon.png | gfx/texticons/006_independence_wave/independence_wave_form03_league_reserve_texticon.dds |
| Network category icon | GFX_decision_category_independence_wave_network in interface/visual_consistency_repair.gfx | 52x40 | source/imagegen/decision_category_network_v1.png; prompts/decision_category_network.json | processed/decision_category_independence_wave_network_subject.png plus processed/decision_category_independence_wave_network.png | gfx/interface/decisions/visual_consistency_repair/categories/decision_category_independence_wave_network.dds |
| Borders category icon | GFX_decision_category_independence_wave_borders in interface/visual_consistency_repair.gfx | 52x40 | source/imagegen/decision_category_borders_v2.png; prompts/decision_category_borders_v2.json | processed/decision_category_independence_wave_borders_subject.png plus processed/decision_category_independence_wave_borders.png | gfx/interface/decisions/visual_consistency_repair/categories/decision_category_independence_wave_borders.dds |

The network and borders ImageGen sources are separate from their processed subject layers and final composites. Both composites use the cataloged visual component .agents/skills/chaos-redux-event-assets/assets/visual_components/national_spirit_backgrounds/decision_category_background_blue_roundel.png as a background_template beneath original ImageGen subject art; its catalog SHA-256 is 6c8643599351cae78f569642b3d0d21f2ca01d3a7ef4891dfe8b7a1922b70713.

The network subject occupies 46x34 pixels on a 52x40 transparent subject layer with a 3px margin. The border subject occupies 44x34 pixels with 4px side margins and 3px top/bottom margins.

The reserve texticon source uses the installed vanilla GFX texticon gfx/texticons/civ_factory.dds, decoded from its original 18x18 DDS for prompt input. The v1 source was rejected because its charcoal face and green accent were too dark at native size; its source, prompt, preview, and DDS are retained under source/imagegen/, prompts/, and review/. The selected v2 has a mid-tone pewter cover, near-black outline, and one muted emerald accent.

The border v1 was rejected because its visible checkpoint silhouette was too wide for the category slot; v2 brings the posts closer and makes the symbol taller. Eighty-two alpha-1 pixels outside a 2px expansion of its inset alpha>=2 subject bounds were removed during normalization; the untouched source is retained.

The recognition seal source was a focused edit of the approved transparent hidden-state seal, with the strong frame used only as a material/relief style reference. Seven alpha-1 residue pixels on the outer source border were removed during normalization; the untouched ImageGen source and exact request remain retained.

No background removal or opaque/chroma-key source route was used.

## Formable state pieces

These pieces use the exact existing Event 006 geometry masks and the established palette helper .tools/repair_event6_state_puzzle_assets.py. The shared map revision is 5070618991ee5bd9f3076ed92beecfc6a0788c12333e35fc0b648631e800002d, the installed map hash is e131d30e5dcb13d9c2a8598f820a2de0ae9828f3a24f2bddc1bcfff40f71660a, and the state-registry hash is 9777af66b45f2539296e2cc1efaf5b0a8d6146b087f31b2bc1a4c646cc0cc6c5.

| Formable and state | Source geometry | Processed variants | Runtime DDS variants |
| --- | --- | --- | --- |
| FORM11 state 234 | source/puzzle_geometry/form11_state_234_geometry_source.png | processed/puzzles/independence_wave_form11_state_234_unresolved.png; processed/puzzles/independence_wave_form11_state_234_qualifying.png | gfx/interface/formables/state_puzzles/006_form11_state_puzzle/states/independence_wave_form11_state_234_unresolved.dds; corresponding _qualifying.dds |
| FORM11 state 245 | source/puzzle_geometry/form11_state_245_geometry_source.png | processed/puzzles/independence_wave_form11_state_245_unresolved.png; processed/puzzles/independence_wave_form11_state_245_qualifying.png | gfx/interface/formables/state_puzzles/006_form11_state_puzzle/states/independence_wave_form11_state_245_unresolved.dds; corresponding _qualifying.dds |
| FORM18 state 413 | source/puzzle_geometry/form18_state_413_geometry_source.png | processed/puzzles/independence_wave_form18_state_413_unresolved.png; processed/puzzles/independence_wave_form18_state_413_qualifying.png | gfx/interface/formables/state_puzzles/006_form18_state_puzzle/states/independence_wave_form18_state_413_unresolved.dds; corresponding _qualifying.dds |
| FORM18 state 676 | source/puzzle_geometry/form18_state_676_geometry_source.png | processed/puzzles/independence_wave_form18_state_676_unresolved.png; processed/puzzles/independence_wave_form18_state_676_qualifying.png | gfx/interface/formables/state_puzzles/006_form18_state_puzzle/states/independence_wave_form18_state_676_unresolved.dds; corresponding _qualifying.dds |
| FORM18 state 1001 | source/puzzle_geometry/form18_state_1001_geometry_source.png | processed/puzzles/independence_wave_form18_state_1001_unresolved.png; processed/puzzles/independence_wave_form18_state_1001_qualifying.png | gfx/interface/formables/state_puzzles/006_form18_state_puzzle/states/independence_wave_form18_state_1001_unresolved.dds; corresponding _qualifying.dds |

For each state, the unresolved and qualifying source alphas have the same binary geometry mask; the source alpha values differ because the prior unresolved edge was antialiased while the prior qualifying edge was opaque. Both output states were rebuilt from one mask so their silhouettes now match exactly.

The shared presentation uses unresolved fill RGB 98,101,108, hatch RGB 66,69,75, outline RGB 151,154,161, qualifying fill RGB 70,148,103, outline RGB 25,56,45, and keyline RGB 155,216,165 with a 6px hatch period.

FORM03 state 36 was reviewed and left unchanged because its detached northern pieces correspond to real Friesland island provinces 6336, 9335, and 11318 in the installed map. Evidence is in review/form03_state36_no_edit_review.md and review/form03_state36_no_edit_review.json.

The parent owns updating docs/formables/state_puzzles/006_form11_state_puzzle/manifest.json and docs/formables/state_puzzles/006_form18_state_puzzle/manifest.json with the final runtime DDS hashes and new processed/source paths.

## Decorative ornamental ring animation

The state-neutral bronze overlay has eight real ImageGen source frames in animations/independence_wave_ornamental_ring/source_frames/ and eight frame-specific saved requests in animations/independence_wave_ornamental_ring/prompts/.

The processed frames are 64x64 and assemble left-to-right into a 512x64 sheet at animations/independence_wave_ornamental_ring/sheets/independence_wave_ornamental_ring_sheet.png and runtime gfx/interface/006_independence_wave/animations/independence_wave_ornamental_ring_sheet.dds. The static fallback is frame 000 at animations/independence_wave_ornamental_ring/processed_frames/independence_wave_ornamental_ring_static.png and runtime gfx/interface/006_independence_wave/animations/independence_wave_ornamental_ring_static.dds.

The loop is decorative, 5 FPS, 200ms per frame, looping, and play-on-show. Its anchor is fixed at (32,32), each frame retains at least 2px outer margin, and a centred 36px circle is exactly zero-alpha in every processed frame.

The prompt requested a 48px inner aperture; the smallest measured alpha>=16 inner gap is about 41px in frame 004, while the central 36px circle remains fully transparent in every frame. Composite previews show the status symbol remains visible.

The GIF review preview is animations/independence_wave_ornamental_ring/previews/independence_wave_ornamental_ring_preview.gif. Source and processed 4x sheets are animations/independence_wave_ornamental_ring/contact_sheets/ornamental_ring_source_frames_contact.png and animations/independence_wave_ornamental_ring/contact_sheets/ornamental_ring_processed_4x_contact.png. Native and 4x composites over all four status icons are review/ornamental_ring_over_status_icons_native.png and review/ornamental_ring_over_status_icons_4x.png.

The shared GFX alpha audit flags the ring sheet and static fallback for a nonzero-alpha mean below 200. This is the thin, intentionally translucent native-alpha ring treatment; it remains visible at 64x64 on a dark panel and over all four status symbols, and the centre stays transparent. No opacity boost or background flattening was applied.

## Recognition static strip state-0 replacement

The new ornate idle seal was assembled as cell 0 of a 320x64 recognition status-strip preview at animations/independence_wave_ornamental_ring/sheets/independence_wave_recognition_seal_states_state0_replacement.png. Frames 1-4 are pixel-identical to the original authored weak, rising, strong, and entrenched cells. The packaged DDS is at dds/gfx/interface/006_independence_wave/animations/independence_wave_recognition_seal_sheet.dds.

The replacement is installed at gfx/interface/006_independence_wave/animations/independence_wave_recognition_seal_sheet.dds after the parent repointed the looping GFX entries to the ornamental ring sheet. The static GFX_independence_wave_recognition_seal_states sprite remains a 5-frame strip, and the GUI selects frame 1 for its idle display.

## Review and processing evidence

Native and 4x review sheets are contact_sheets/icons_native_contact.png, contact_sheets/icons_4x_contact.png, contact_sheets/puzzles_native_contact.png, and contact_sheets/puzzles_4x_contact.png. The state-strip before/after comparison is animations/independence_wave_ornamental_ring/contact_sheets/recognition_state_strip_state0_comparison.png.

DDS round-trips are pixel-identical to processed PNGs. The GFX size profiles passed for the 64x64 recognition seal, 18x18 texticon, both 52x40 category subject layers, and 64x64 ring static fallback. The runtime alpha audit checked 17 installed DDS files and flagged only the ornamental ring sheet/static fallback for the explained mean-alpha triage finding.

The original runtime DDS files replaced by this package are preserved under review/original_runtime/ with their baseline hashes in review/runtime_target_baseline.json and the install receipt in review/runtime_install_report.json.

ImageGen prompts, source hashes, processing reports, runtime hashes, contact sheets, and map geometry evidence are retained under this workspace. This asset subagent did not edit GFX, GUI, gameplay, localisation, or event source files; the parent applied the GFX repoint after reviewing the shared ring assets.
