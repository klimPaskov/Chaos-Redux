# Event 32 Prepared-Payload Cost Texticons

Production date: 2026-10-07.

This package covers only the chemical and biological prepared-payload stockpile cost texticons requested by the parent task, plus exact native nuclear reuse evidence.

The explicit parent prompt authorizes the shared IDs and DDS paths listed below, requires native transparent ImageGen art for new alpha-backed icons, and limits this package to two static cost texticons.

The Event 32 decision prompt requires a correct texticon for every displayed custom cost at `docs/specs/032_missiles_specs/032_missiles_decision_mission_prompt.md:70`, and part 5 requires proper texticons for custom values at `docs/specs/032_missiles_specs/032_missiles_spec_part_5_decisions_missions_and_scenario.md:158-167`.

Part 3 defines chemical payload equipment and biological stockpile as real consumed payloads at `docs/specs/032_missiles_specs/032_missiles_spec_part_3_operations_and_consequences.md:500-529`.

## Dispositions

| Cost surface | Exact sprite and DDS | Disposition |
| --- | --- | --- |
| Chemical prepared payload | `GFX_cbrn_chemical_payload_texticon` → `gfx/texticons/cbrn_chemical_payload_texticon.dds` | `complete`; parent approved silhouette, palette, alpha, and the small poison mark with tooltip context on 2026-10-07. |
| Biological payload stock | `GFX_cbrn_biological_payload_texticon` → `gfx/texticons/cbrn_biological_payload_texticon.dds` | `implemented`; source, processed PNG and DDS are present, parent-reviewed and wired. |
| Nuclear payload | `GFX_unit_nuclear_missile_icon_small_texticon` → installed vanilla `gfx/texticons/unit_nuclear_missile_icon_small.dds` | Reuse existing vanilla sprite and texture; no new filename or duplicate art. |

The parent had already registered both proposed CBRN sprites in `interface/cbrn_payload_texticons.gfx` before this production pass; that file was inspected but not edited by this asset worker.

Both parent-registered CBRN texture paths now resolve to DDS files; this asset worker did not edit the parent-owned GFX file or any cost consumer.

## Existing-Asset Audit

No exact shared chemical or biological stockpile-cost texticon was found in the relevant vanilla or Chaos Redux texticon definitions or in the inspected Event 32 sibling assets.

The installed vanilla nuclear texticon is an exact match for the nuclear payload cost surface and remains the reuse choice.

The project-wide `GFX_support_equipment_text_icon` is defined in `interface/chaosx_texticons.gfx:89-94` and points to `gfx/texticons/support_equipment_text_icon.dds`; it is a Chaos Redux shared sprite, not an installed vanilla definition, and it represents generic support equipment rather than a CBRN payload.

The existing Event 32 sibling texticons at `interface/032_missiles.gfx:18-20` represent operational reserve, launch readiness, and command control on 24×24 canvases; they do not represent chemical or biological payload stock.

Other CBRN-named files inspected under `gfx/texticons/` are unit or support-category icons, not stockpile-cost texticons, so they were not resized or relabeled.

The bounded name/path audit searched installed `interface/texticons.gfx`, Chaos Redux texticon definitions, relevant texticon DDS filenames, and `gfx/texticons/032_missiles/*.dds`; it found no exact shared chemical or biological stockpile cost icon.

The HOI4 MCP source lookup revision `31977d2796a3ea19dbb054a09641b7336f9b51ef5113b8d1f71458e520bc04ac` resolved the nuclear sprite to `game:interface/texticons.gfx:2945-2950` with `overridden = false`, and the support comparator to `mod:interface/chaosx_texticons.gfx:89-94`.

That source lookup returned incomplete indexed reference enumeration, so the no-match claim is limited to the direct, bounded searches above and does not claim a full indexed usage inventory.

## Consumer and Canvas Evidence

The exact parent-registered chemical sprite is `GFX_cbrn_chemical_payload_texticon` with texture path `gfx/texticons/cbrn_chemical_payload_texticon.dds`.

The exact parent-registered biological sprite is `GFX_cbrn_biological_payload_texticon` with texture path `gfx/texticons/cbrn_biological_payload_texticon.dds`.

The parent registration uses `legacy_lazy_load = no` and the parent prompt specifies single-frame sprites; the produced chemical texture is a single 30×12 frame.

The Chaos Redux support comparator is a 60×12 left-to-right two-frame strip with 30×12 frames, `legacy_lazy_load = no`, and `noOfFrames = 2`; its decoded alpha range is 0–255.

The support frame 0 alpha bounds are `(2,2,27,10)`, and frame 1 bounds are `(2,0,28,12)`; the review sheet preserves both distinct source frames without assigning unverified state semantics.

The installed vanilla nuclear texticon is also a 60×12 left-to-right two-frame strip with 30×12 frames, `legacy_lazy_load = no`, and `noOfFrames = 2`; both decoded frames have alpha range 0–255 and bounds `(0,1,30,12)`.

The nuclear frames are two horizontal missile silhouettes with contrasting muted and light treatments; no extra state or animation meaning is inferred from the atlas alone.

The Event 32 sibling DDS files are each 24×24 RGBA with alpha range 0–255, and their GFX declarations omit `noOfFrames`.

The canonical family inspected before individual references was `.agents/skills/chaos-redux-event-assets/assets/gfx_references/icons/modifiers/contact_sheet.png`.

The selected family example was `.agents/skills/chaos-redux-event-assets/assets/gfx_references/icons/modifiers/modifier_supply_consumption_factor.png`, cataloged as a 30×20 Vanilla HOI4 modifier reference sourced from `gfx/interface/modifiers/MODIFIER_SUPPLY_CONSUMPTION_FACTOR.dds`.

The reference family guided review only; no canonical reference PNG was copied, traced, recolored, or shipped as runtime art.

The visual component catalog contained no matching stockpile texticon layer or background template; no visual component was used.

## ImageGen Candidate Lineage

The official built-in ImageGen tool was used; its schema did not expose a model selector, and no backend model name is claimed.

The first chemical request is retained at `prompts/cbrn_chemical_payload_texticon.imagegen.json`, SHA-256 `5F3FEA8E7804263C7C7520B75FA1F526F6F0FE0DDB0CE3597D6D1E0469982C70`; it requested genuine transparency and used the canonical modifier reference as a style-only input, but ImageGen rejected its output with moderation request ID `7eb52d9e-c6e3-4110-8849-621400ce3630`, producing no source image.

The successful chemical generation request is retained at `prompts/cbrn_chemical_payload_texticon_attempt_02.imagegen.json`, SHA-256 `CE1E35E544F1293F2683FEB069FEAC878EA2331FC0CF1CF2FC7AE531197F4578`; it requested genuine transparency and supplied no input images.

Its tool-reported output was `C:\Users\klimp\.codex\generated_images\01a1174d-16aa-7531-bad1-674901f952f9\exec-a8d4a6d9-1a01-47d5-a94b-a7bc42ea621a.png`, retained byte-for-byte as `source_png/cbrn_chemical_payload_texticon_imagegen_attempt_02.png` with SHA-256 `CC8919FE04E776BA43976056763F2FD659327D4249C77D4000613E4DF9E334F8`.

That candidate was rejected because its central warning mark depicted radiation, which would mislabel the chemical payload.

The selected focused edit request is retained at `prompts/cbrn_chemical_payload_texticon_edit_03.imagegen.json`, SHA-256 `91E60A65A6055BDA64086394A17A8ACE2B6BC8394EB3C2A0907271C0D10B6F1B`; it used the retained candidate as the edit target and changed only the warning mark from a radiation trefoil to a poison skull-and-crossbones mark.

The tool-reported edit output was `C:\Users\klimp\.codex\generated_images\01a1174d-16aa-7531-bad1-674901f952f9\exec-47c27ed5-4ad3-4114-9131-cd91a1bac36c.png`, retained byte-for-byte as `source_png/cbrn_chemical_payload_texticon_imagegen_edit_03.png` with SHA-256 `27598E800DF0FDAA13C62B6BBB6B1D16C28872F17224517F41407C391DB07EE9`.

The selected source is 1983×793 RGBA with alpha range 0–255 and transparent corners.

Its nonzero-alpha bounds are `(570,148,1420,684)`; its alpha-threshold 8 and 16 bounds are both `(573,257,1417,544)`, and no thresholded alpha touches the image boundary.

The source alpha review at `evidence/asset_reviews/cbrn_chemical_source_alpha_review.png` composites the unchanged alpha source on white, charcoal, and checkerboard review backgrounds; no matte or visible colored fringe was observed.

The parent reviewed `contact_sheet.png` and approved the chemical canister silhouette, muted palette, preserved alpha, and the small poison mark when paired with the exact tooltip context.

The first biological request is retained at `prompts/cbrn_biological_payload_texticon_attempt_02.imagegen.json`, SHA-256 `33E108D860340C8B3B4C666C20E53A031D476F01BC386FB80A64D3B951F7BB3F`; ImageGen refused its output with request ID `dfa3a081-163e-4bc8-bbcd-6227b56330ab`, and returned no source image.

The revised benign pictogram request is retained at `prompts/cbrn_biological_payload_texticon_attempt_03.imagegen.json`, SHA-256 `FE0F2B478551C70B7BE7FCA43C02BD226102408D358ACDE1EFA34207F525AAA4`; it requested only the standard public three-lobed biological-hazard pictogram on a genuinely transparent canvas and ImageGen produced a source.

That first successful biological source is retained at `source_png/cbrn_biological_payload_texticon_imagegen_attempt_03.png`, SHA-256 `479F013E37A21E28A7FB32C7BF892B59E7EFE022BAC763F0BD851A982E7ECB24`; its nested strokes were too dense at the 12×12 display footprint, so it remains preserved as a rejected candidate.

The focused simplification request is retained at `prompts/cbrn_biological_payload_texticon_edit_04.imagegen.json`, SHA-256 `F0D44BCB73E73F726D99F64576D5FA0015929F538AE1003E90A16C3BBB2B2BDC`; it removed extra nested strokes while preserving three lobes, the central node, the palette, placement, and genuine transparency.

The selected biological source is `source_png/cbrn_biological_payload_texticon_imagegen_edit_04.png`, SHA-256 `0DDB86F654C833D465AB4C4F928BAC664044D44717A32F027B37CD1C94C78B98`; it is 1983×793 RGBA with alpha range 0–255 and transparent corners.

Its nonzero-alpha bounds are `(698,113,1308,760)`; its alpha-threshold 8 and 16 bounds are both `(703,115,1279,661)`, and no thresholded alpha touches the image boundary.

The selected biological source alpha review at `evidence/asset_reviews/cbrn_biological_source_alpha_review_edit_04.png` composites the unchanged source on white, charcoal, and checkerboard review backgrounds.

The earlier biological prompt file `prompts/cbrn_biological_payload_texticon.imagegen.json` was prepared but never submitted; all submitted attempts and both successful sources remain preserved with their prompt records.

No CLI/API generation route, opaque-background route, or background-removal fallback was used.

## Chemical Processing and DDS Evidence

The processed PNG is `processed_png/cbrn_chemical_payload_texticon.png`, exactly 30×12 RGBA, with alpha range 0–255, nonzero bounds `(1,1,29,11)`, and transparent corner pixels.

Normalization used the selected source's alpha-threshold 8 subject bound `(573,257,1417,544)`, a symmetric crop `(556,248,1434,553)`, aspect-preserving premultiplied-alpha LANCZOS downsampling, and centered placement on a transparent 30×12 canvas.

No background-removal operation was used; the low-alpha exterior remains preserved in the raw source, while processing crops around the complete threshold-8 subject bounds.

The processed PNG SHA-256 is `FD103E6EAEDA459F1264715842304EC4AE9CDB19F0ABF71AFEB692C67D981EAA`.

The final runtime file is `gfx/texticons/cbrn_chemical_payload_texticon.dds`, SHA-256 `AB28CBD27CF08D8F7F1872CFDB953E17DFB57D10FD61B79AF081CD5BA883F266`.

The repository converter `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` produced a standard one-level 32-bit BGRA DDS with the exact 30×12 dimensions, 1568-byte length, expected BGRA masks, texture caps, and preserved alpha.

Pillow decoded the final DDS to pixels exactly equal to the processed PNG; the decoded round-trip PNG has the same SHA-256 as the processed PNG.

The selected biological processed PNG is `processed_png/cbrn_biological_payload_texticon.png`, exactly 30×12 RGBA with alpha range 0–255, transparent lateral margins, and alpha bounds `(9,0,21,11)`.

The biological normalization crops the complete threshold-8 symbol bounds `(703,115,1279,661)`, aspect-preservingly resizes the standard glyph with premultiplied-alpha LANCZOS to a centered 12×11 footprint, and places it at x=9 on the transparent 30×12 canvas.

The selected biological processed PNG SHA-256 is `4E28CD598B9EC6C4776188A2F3AAD248DC749247DEB0739FE09F0F6A09AA19A1`.

The final biological runtime file is `gfx/texticons/cbrn_biological_payload_texticon.dds`, SHA-256 `AFE5B7E8018BD8B604A825DFE2F27F447DA2A64C98AB6749191430DF16AC13C5`; it is a standard one-level 32-bit BGRA DDS with exact 30×12 dimensions and a 1568-byte length.

Pillow decoded the biological DDS to pixels exactly equal to the selected processed PNG; its decoded round-trip PNG has the same SHA-256 as the processed PNG.

The parent-approved chemical review sheet `contact_sheet.png` remains unchanged, SHA-256 `DD5CF6A2911B55913D2A97ED559EC6907B0321F4D654AF7C08046CEFBD01BD4F`.

The current combined native and 4× review sheet is `contact_sheet_current.png`, SHA-256 `3252FE853399D1EEA83C00212DE097180578D081D5263316446A447897AF66DE`; the consumer-only reference sheet is `evidence/consumer_reference_previews/consumer_reference_contact_sheet.png`.

The parent approved the chemical icon for its exact stockpile silhouette, muted palette, preserved alpha, and tooltip-context pairing.

The parent approved the biological pictogram after inspecting its native-size 30×12 and 4× views in `contact_sheet_current.png`, including the distinct three-lobed shape, centered footprint, muted contrast and transparent edges.

## Offline Reference Evidence

`hoi4.reference_context` returned workspace `mod_chaos_redux_ea3b2d67c2c0` with the offline wiki and installed-game documentation sources used below.

The offline wiki section `Localisation - Hearts of Iron 4 Wiki.md:221-243`, revision `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`, documents the £ token, `spriteType` texticon registration, `gfx/texticons/` paths, alias naming, and multi-frame selection.

The offline wiki section `Graphical asset modding - Hearts of Iron 4 Wiki.md:30-100`, revision `f8e3d4ad382f4e5f8e170492a484d090bad62e3711cabfb5d3bf84e58ab32dd9`, documents `spriteType`, `texturefile`, `noOfFrames`, and lazy loading.

The offline wiki section `Decision modding - Hearts of Iron 4 Wiki.md:324-336`, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, confirms that custom decision costs display texticons.

The installed-doc context returned only the heading of `documentation/loc_formatter_documentation.md`, and targeted installed-doc search found no texticon-specific section; exact installed vanilla GFX and DDS files were read directly.

The installed vanilla source is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/texticons.gfx:2937-2950` with DDS `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/texticons/unit_nuclear_missile_icon_small.dds`.

## Parent Review and Remaining Work

Chemical production is `complete` and parent-approved; the parent owns cost consumer wiring and use of the exact tooltip context.

Biological production is parent-approved; the revised benign prompt succeeded on the same built-in ImageGen route and the parent completed the native and 4× visual review.
Both exact shared cost sprites are wired in the Event 032 preparation localisation; the contact sheets do not establish final live decision-row fit.

Nuclear is `reuse`; keep the exact installed vanilla sprite and do not add an Event 32 copy.

The earlier ImageGen refusals remain in the prompt history and were not bypassed with another backend, background-removal route, or local drawing.

This package did not edit `.gfx`, localisation, gameplay, or any other engine-facing source, did not run Hearts of Iron IV, and did not perform Git/index operations.

