# Event 027 achievement icon visual audit handoff

Audit date: 2026-10-03.

Current disposition, 2026-10-03: the accepted Joint Curriculum replacement and final triplet pass the static asset audit. All nine achievement states pass the reopened native and enlarged visual review. The earlier candidate-pending statements below are historical and superseded by the final repair section at the end of this handoff. No GFX, registry, gameplay file, index, or commit was changed by this documentation and audit pass.

## Scope and accepted asset basis

The accepted Event 027 asset set requires three distinct achievement icon triplets with final IDs `027_doctrine_research_first_lesson`, `027_doctrine_research_single_school`, and `027_doctrine_research_joint_curriculum`, as stated in `docs/specs/027_doctrine_research_specs/README.md`, `027_doctrine_research_spec_part_4_presentation_assets_achievements.md`, and `027_doctrine_research_asset_prompt.md`.

The inspected output scope was the three original masters in `docs/assets/027_doctrine_research/source_png/`, the nine transparent state layers in `docs/assets/027_doctrine_research/processed_png/source_layers/`, the nine composited PNG previews in `docs/assets/027_doctrine_research/processed_png/review/`, and the nine runtime DDS files directly under `gfx/achievements/`.

The nine PNGs in `processed_png/final_staging/review/` have the same SHA-256 values as their matching `processed_png/review/` PNGs. The nine DDS files in `processed_png/final_staging/` have the same SHA-256 values as their runtime DDS counterparts, so the individually opened review PNGs and decoded runtime DDS also cover those staged copies by byte identity.

The referenced older `assets/vanilla_reference` path is absent both at the mod root and under `.agents/skills/chaos-redux-event-assets/assets/`. The current canonical reference root exists at `.agents/skills/chaos-redux-event-assets/assets/gfx_references/` and was used directly. No files from the absent attachment path or another project visual-reference directory were read.

The canonical achievement contact sheet was inspected before individual references. Individual Vanilla references opened for comparison were the complete `30_minutes_of_hel` and `crusader_kings_2` state triplets under the canonical family. I also briefly opened the three contact-sheet items cataloged as `Moved legacy review copy` during reference orientation, then excluded them from visual comparisons and acceptance judgments. The comparisons rely on the installed Vanilla DDS and the canonical Vanilla PNG examples.

## Consumer and wiring evidence

Installed Vanilla `interface/achievements.gui` defines the `achievement_entry` and its `achievement_icon` slot, whose default sprite is `GFX_idea_unknown`. Installed Vanilla `interface/achievements.gfx` defines the generic achievement bars and backgrounds, not per-achievement sprite IDs. The installed Vanilla achievement DDS samples and the canonical family establish the 64x64 achievement canvas and the three-state filename convention. No live UI capture was available, so this is static consumer evidence rather than rendered in-game consumer proof.

The current prompt names `interface/027_doctrine_research.gfx` as the owner of nine achievement sprites. That file contains the Event 027 report image sprite only. All nine achievement aliases are in `interface/chaosx_achievements.gfx`, and each alias resolves to the expected root `gfx/achievements/<full_id>{,_grey,_not_eligible}.dds` path. The three IDs occur in `common/achievements/chaos_redux_achievements.txt` and match the expected basenames. This is a prompt path mismatch, not a defect in the observed alias-to-DDS paths.

The installed Vanilla sample triplets decode to 64x64. Four inspected Vanilla triplets use 16,512-byte uncompressed BGRA DDS files with alpha 255. The `the_revolution_triumphant` triplet is a 4,224-byte compressed legacy exception with compression-adjusted alpha values. The current Chaos Redux supplied achievement backgrounds and the final Event 027 states use the expected full-canvas presentation. The source masters and source layers retain genuine transparent pixels, with alpha 0..255. The completed and grey workflow templates both have alpha 254..255, and the final composite PNGs and DDS files have that same alpha range.

The current workflow template hashes match the canonical catalog: `achievement_template.png` is `248DB006611EB3942550C43DF83802AA6FB24761035FC928B5D34586C0C4C5BA`, `achievement_template_grey.png` is `70E073694C1A7D9FE40C63B1EB2E987A8A45B3FFD15CCF789EEAA5B843B90022`, and `overlay.png` is `89BC80C6AC975BF6F1FF000FF3070B20C337BFB8B8AE966AE35A5540C004D6DD`.

## Individual visual and DDS review

Each original master was opened individually at 1254x1254 and as a 2x nearest-neighbour inspection view. Each of the nine transparent source layers and nine composited PNG previews was opened individually at 64x64 and as a 4x nearest-neighbour inspection view. Each runtime DDS was decoded from the exact DDS file bytes with Pillow, then its 64x64 decoded image and 256x256 nearest-neighbour view were opened individually. No visual conclusion below relies on a contact sheet or dimensions alone.

Temporary enlarged and decoded inspection images are in `C:/Users/klimp/AppData/Local/Temp/event027_icon_audit_2dea27524b0440349a33aa9cd9ff065c/`. They are derived audit views, not product assets. The masters and processed PNGs were also opened directly from their repository paths.

The existing achievement processor was run in read-only `--audit` mode against the complete source-layer directory and runtime output directory. It returned `AUDIT OK` for all three IDs, confirming strict 64x64 BGRA output and exact source-layer compositing equality. Independent pixel comparison of each decoded runtime DDS against its processed review PNG also returned exact equality. Each staged DDS hash equals its runtime DDS hash.

| Achievement state | Transparent source-layer SHA-256 | Processed preview PNG SHA-256 | Runtime DDS SHA-256 | Native and enlarged visual result |
| --- | --- | --- | --- | --- |
| `027_doctrine_research_first_lesson` completed | `ED3BD9DE007F7AE5786817F32A9870407C6701121D34A9999077F3581473076B` | `3F3E292CBA7102BFBA2687B3F51CDCF38E92F36569EB7765325F661A3E33D7D5` | `E2AB92E0066439BC85DF6D2B3E6A913E0E5A8EBCAA629F3C0E9C46215FC084CE` | Pass. The open manual and first marker read at 64x64. No clipped silhouette or visible matte. |
| `027_doctrine_research_first_lesson` grey | `72EA23597595351339FD607A1945DE5CB108F5C9288094371C806F4C3ADA5EC8` | `D0FC6A70CEF03C7C73DABDD6712A2AC34A2E54A93B77C69DD4BA63FA15E09556` | `7105734156BDE4C93F685A50A79DF817CB1134C99A2323E2F30DD2848EABB79B` | Pass. The grey art remains legible and matches the completed-state placement. |
| `027_doctrine_research_first_lesson` not eligible | `8A6770F3AAB9191055A0DEF52464E6DFF9704DE43FAD4E6596D91621C9CF4F3E` | `5A98F0A92CC054D465317AFA1DF5130EFC5D6327F828CC7A29013AE77D1A0264` | `1701448BDF01D64DF3123C7ABFE9D3F42BC84F798F0C49A935377E45116B721E` | Pass. The unchanged red cross is centered and does not clip. |
| `027_doctrine_research_single_school` completed | `12C317FAE980F1E90080D7BF18294A96D16037A24D880BBA3C495AE6B3463F7B` | `2CB1F052C711D072635F4FA4C953900F5190358D17C85CB4F4E2A3C17320B71F` | `CD88A460F6BF4D4A461D4FB885E2AE08043A63BCAB0F4098008B2E6B49D766C1` | Pass, with dense detail. The fan of lesson markers and central school crest remain distinguishable at 64x64. |
| `027_doctrine_research_single_school` grey | `8214B5DB167F350BA47B2D4A1831ACCA491774CC9799F34C07964D920F247378` | `30C9383A34010DB6BA1380496319715780B9AB17A8899B8C08CAB393344DC463` | `30D4637C8BEC116107C066BFD02C52FC764CD8D0F2FFCEF0BE08B725DF953C6F` | Pass. The grey crest and marker fan remain distinct at native size. |
| `027_doctrine_research_single_school` not eligible | `46DAD03936AB3A22315764E16CDFBCA4E37F276E20884EDC626F25F0B022EF53` | `14643F66FA1E3ECE769C6B539F5E4156DBFC966226F5F3B65953D7CB06A60CF9` | `33F9EBDE47D8394C2377815335D4E5575BE094A268B3866CAA0692285FEFB492` | Pass. The red cross reads clearly; the state is correctly aligned. |
| `027_doctrine_research_joint_curriculum` completed | `2C0428E9429AA6E7BDF00E83401448FD6801E512A900C33FF2C4C112D49AAD86` | `045491FE49E1660946FC0BD86CFBF828EC33FABC9AABE89C983C8CAC638720E6` | `4EE3F0F20D0C716418450539D400412475977F41BED1A8C0D8F913E59DC4240F` | Needs user review. The master clips outer emblems at the canvas edges, and that clipped silhouette carries into the triplet. |
| `027_doctrine_research_joint_curriculum` grey | `5F8F944396B8D9F522240F30125426D6C3999D21D9461DAB64CA555497290B6A` | `1C8FE8F28E4CCABBA4AFE7162543170F661CB358CFC252443E6499244AB5819A` | `D80F96BE8D87290436B5B71CC7A811DACBFEF020C77A956418203009D7FF46AB` | Needs user review for the shared master defect. DDS dimensions, alpha, state derivation, and pixel equality pass. |
| `027_doctrine_research_joint_curriculum` not eligible | `35FAE2B153DAEF91029EF5B3DFD85EAC64503172EDE5B6233A7940055779D69F` | `AF216D3A2F1B965AF7E7B4E51694ABB79A7AD72859A1E928C7F54AFDDA000515` | `E4628A234F03D49C8D96A9C0DE6231FEEBE6B774625514FA7B06F8E14E15A2C9` | Needs user review for the shared master defect. The red-cross layer and DDS round trip pass. |

All nine runtime DDS files are 64x64, 16,512 bytes, one-level uncompressed BGRA, strict legacy header format, with decoded alpha 254..255. Every decoded DDS is pixel-identical to its corresponding 64x64 processed PNG. The final DDS hashes above also match the DDS copies in `processed_png/final_staging/`.

## Source master review and confirmed defect

| Achievement | Source master | SHA-256 | Dimensions and alpha | Source review |
| --- | --- | --- | --- | --- |
| First Lesson | `docs/assets/027_doctrine_research/source_png/027_doctrine_research_first_lesson_source.png` | `6994FC60F9F6C28B6B73534C128E59632484A61FE8C2E43DEC963BE072AB33F2` | 1254x1254 RGBA, alpha 0..255 | Pass. The manual, lesson marker, and pencil have transparent clearance around the complete silhouette. |
| Single School | `docs/assets/027_doctrine_research/source_png/027_doctrine_research_single_school_source.png` | `CF8D2E754C698C1BD1BD3BE5FB1C2B00E96EBAF942606ECAC0D240848A835CC0` | 1254x1254 RGBA, alpha 0..255 | Pass. The five scroll markers and school crest stay inside the canvas. The detail is dense but survives at native size. |
| Joint Curriculum | `docs/assets/027_doctrine_research/source_png/027_doctrine_research_joint_curriculum_source.png` | `39DC3CE14F6E40A8E72D05D9FC22FAC5DABEE10D52C37225EE1060DFC3D2AA69` | 1254x1254 RGBA, alpha 0..255 | Defect confirmed. The airplane emblem clips at the left edge, the naval emblem clips at the right edge, and the top and bottom emblems also reach the canvas boundary. |

Joint Curriculum alpha-mask evidence confirms strong-alpha pixels in the outer 8-pixel bands on all four sides: left 65 pixels with bounds x=2..7, right 175 pixels with bounds x=1246..1253, top 203 pixels with bounds y=3..7, and bottom 5 pixels with bounds y=1246..1247. First Lesson and Single School have no alpha-over-128 pixels in those outer 8-pixel bands. The Joint Curriculum source was also composited over a neutral light background for edge inspection, confirming that the plane and anchor artwork is cut by the source canvas rather than merely hidden by the transparent preview background.

Proposed repair for parent review: replace only the Joint Curriculum master with a new native-transparent composition that preserves the central binder and compass and keeps four distinct service or track emblems fully inside a clear margin on every side. Then create one centered 64x64 color subject layer, derive the grey layer deterministically from it, composite the unchanged supplied overlay for not-eligible, and rerun `process_achievement_icons.py` with the exact immutable templates. Parent review should approve the replacement source before any runtime DDS is replaced. The initial read-only audit made no candidate. The later authorized candidate edit is recorded below and has not replaced the original master or any runtime state.

## Remaining evidence limits

The parent prompt states that HOI4 MCP timing is unhealthy. No MCP render or live game session was used, and this handoff does not claim one-to-one in-game consumer proof. Static Vanilla consumer source, current Chaos Redux GFX aliases, root registry IDs, canonical DDS references, and actual runtime DDS decoding were inspected.

The current Joint Curriculum runtime triplet remains based on the clipped original master while the candidate awaits parent acceptance. The next authorized production step is still blocked on parent acceptance of the source preview. The wiring note remains the prompt's filename correction from `interface/027_doctrine_research.gfx` to `interface/chaosx_achievements.gfx` for the nine achievement aliases. MCP consumer proof remains blocked.

## 2026-10-03 authorized ImageGen candidate edit

The parent confirmed that the original Joint Curriculum master and its completed and not-eligible states show clipping, and authorized a non-destructive candidate edit only. The original file `docs/assets/027_doctrine_research/source_png/027_doctrine_research_joint_curriculum_source.png` remains unchanged at SHA-256 `39DC3CE14F6E40A8E72D05D9FC22FAC5DABEE10D52C37225EE1060DFC3D2AA69`.

The candidate was made with the built-in ImageGen edit flow and `transparent_background=true`. No CLI or API fallback was used. The existing source master was loaded and inspected before the first edit. One intermediate edit failed the margin requirement and was kept only in the ImageGen output folder. A second focused edit, using the first draft as its edit target, is the candidate retained for review.

| Artifact | Path | SHA-256 | Dimensions, alpha, and status |
| --- | --- | --- | --- |
| Rejected first edit draft | `C:/Users/klimp/.codex/generated_images/01a10182-5230-7fb2-978d-025e9acb274c/exec-02e7703a-1ae9-405b-af74-83c283eed22d.png` | `7F7F492DFFDD24A288D49C9201AEC3CD96EA0849139C4A599AEED9FB52139C12` | 1254x1254 RGBA, alpha 0..255. Rejected because 65,298 pixels in the outer 10% bands had nonzero alpha, including fully opaque artwork. |
| Candidate master for parent review | `docs/assets/027_doctrine_research/source_png/027_doctrine_research_joint_curriculum_source_candidate.png` | `2904EBD2660EB748965A9AE8C7275950CB982246FABFF47E4BBBD3F6C56F74E9` | 1254x1254 RGBA, alpha 0..255. The alpha-over-1 bounds are `(132, 147, 1127, 1109)`, giving more than 10% visible clearance on every side. Sixty pixels in the outer 10% have alpha 1; no pixel there has alpha above 1. Status: `needs_user_review`. |
| Proposed native subject layer preview | `docs/assets/027_doctrine_research/processed_png/candidate_review/027_doctrine_research_joint_curriculum_source_candidate_subject_64.png` | `29224ECE990AF93DAF30C9A25AC9963F5B3ACD83B8AFB1CF4BB374166F8AF6D6` | 64x64 RGBA, alpha 0..255, visible bounds `(6, 7, 58, 57)`. Status: `needs_user_review`, preview only. |

The candidate master keeps the central binder and compass with the same four Army, Air, Naval, and CBRN motifs. Its full-resolution view shows the aircraft, anchor, tank crest, and CBRN crest inside the canvas. The 64x64 preview remains a compact achievement subject with genuine transparent unused canvas. The preview was made by cropping to the candidate's `alpha > 1` bounds, resizing in premultiplied-alpha space with Lanczos to fit within 52x58 pixels, and centering on a transparent 64x64 canvas. It is a visual proposal only and is not a completed/grey/not-eligible source triplet.

The ImageGen output was copied to the named candidate path without altering the generated original under `C:/Users/klimp/.codex/generated_images/01a10182-5230-7fb2-978d-025e9acb274c/`. The original Joint Curriculum source hash was checked again after the copy and remains unchanged. No grey or not-eligible layer was derived, no `process_achievement_icons.py` pass was run on the candidate, and no runtime DDS was generated or replaced.

Prompt for the rejected first edit, submitted with the original master as Image 1 edit target and native transparency requested:

```text
Use case: stylized-concept
Asset type: one original 1254-square source master for a Hearts of Iron IV achievement icon
Input images: Image 1: edit target, the current Event 027 Joint Curriculum master
Primary request: correct the clipped composition by rebalancing the existing emblem group inward. Preserve the central open curriculum binder and brass compass, with the same four service motifs: an Army tank emblem above, an Air aircraft emblem on the left, a Naval anchor emblem on the right, and a CBRN gas-mask emblem below.
Style/medium: keep the existing richly painted HOI4-era achievement-emblem treatment, crisp dark outlines, worn brass, parchment, charcoal, deep navy, muted steel, restrained red, and small desaturated green details.
Composition/framing: square transparent canvas. Keep the binder and compass central. Scale and arrange the same four motifs so each complete emblem is fully visible, balanced, and clearly separated around the binder. Leave at least a 10% genuinely transparent margin on every edge. Make the entire silhouette readable after reduction to 64x64.
Constraints: change only the composition and spacing needed to remove clipping. Preserve the subject identity, materials, palette, and four existing motifs. No part of any emblem may touch or cross the canvas boundary. No achievement frame, border, square background, or background texture.
Avoid: text, numerals, letters, flags, national insignia, watermarks, fake checkerboard, added objects, extra symbols, split panels, opaque or chroma backgrounds, halos, and cut-off silhouettes.
```

Prompt for the retained candidate edit, submitted with the first draft as Image 1 edit target and native transparency requested:

```text
Use case: stylized-concept
Asset type: one transparent source master for the Event 027 Joint Curriculum HOI4 achievement icon
Input images: Image 1: edit target, the first ImageGen edit candidate with the preserved Joint Curriculum artwork
Primary request: make one precise composition edit only: uniformly reduce and center the complete existing emblem group so its full silhouette, including every outline and small projection, fits inside the central 76% of the square canvas. Leave at least 12% genuinely transparent padding on all four edges, with no painted pixels touching or entering the outer 10% band.
Subject invariants: preserve the same central open curriculum binder and brass compass, Army tank emblem above, Air aircraft emblem on the left, Naval anchor emblem on the right, and CBRN gas-mask emblem below. Keep the existing HOI4-era painted achievement style, worn brass, parchment, charcoal, deep navy, muted steel, restrained red, and small desaturated green details.
Composition/framing: retain a balanced vertical arrangement and the same relative placement and overlap of the binder and four motifs. Scale the complete group inward as one unit. Keep every aircraft wingtip, anchor fluke, tank crest, and CBRN crest whole and clearly separated from the canvas edge. Preserve a strong central silhouette readable after later fitting into a 64x64 subject layer.
Constraints: change only the overall group scale and centering needed to create the required empty transparent border. Keep a square canvas and genuine transparency. No achievement frame, border, square background, texture, or painted padding.
Avoid: text, numerals, letters, flags, national insignia, watermarks, fake checkerboard, added or removed motifs, split panels, opaque or chroma backgrounds, halos, clipped outlines, and any art in the outer 10% of the canvas.
```

Pre-edit status: the original Joint Curriculum source and runtime triplet were flagged for clipping, and the candidate and preview paths were absent. Post-edit status: the original source and runtime DDS triplet remain unchanged; the candidate master and native 64x64 preview now exist and await parent acceptance. First Lesson and Single School were not regenerated. No GFX, gameplay, registry, or index changes were made. The current MCP visual-consumer limitation is unchanged.

## Shared-worktree observation

A read-only status check during this candidate task showed current changes in `common/achievements/chaos_redux_achievements.txt` and in unrelated Event 023 and Event 042 achievement DDS files. This candidate task did not modify those paths. Their ownership and contents were left untouched for their active owners to reconcile.

The candidate master and subject preview are present at the paths above, but `.gitignore` excludes `docs/assets/`. They remain local review artifacts and were not staged or force-added.

## 2026-10-03 accepted repair and final asset audit

This section is the current asset disposition and supersedes the historical statements above that the Joint Curriculum candidate awaited acceptance or that its runtime triplet remained unchanged. The user authorized repair of all asset defects. The parent conveyed individual visual acceptance of the selected master and 64x64 preview in the current task instruction. The asset package passes its static visual and file audit. This does not close Event 027 or establish a `Playable` status.

### Source lineage and native transparency

The clipped predecessor remains byte-for-byte preserved at `docs/assets/027_doctrine_research/source_png/027_doctrine_research_joint_curriculum_source_explicit_superseded_clipped.png`, SHA-256 `39DC3CE14F6E40A8E72D05D9FC22FAC5DABEE10D52C37225EE1060DFC3D2AA69`. This archive resolves the prior-source provenance concern.

The current canonical master is `docs/assets/027_doctrine_research/source_png/027_doctrine_research_joint_curriculum_source.png`, SHA-256 `2904EBD2660EB748965A9AE8C7275950CB982246FABFF47E4BBBD3F6C56F74E9`. It is byte-identical to `docs/assets/027_doctrine_research/source_png/027_doctrine_research_joint_curriculum_source_candidate.png` and to the retained native ImageGen output `C:/Users/klimp/.codex/generated_images/01a10182-5230-7fb2-978d-025e9acb274c/exec-9e6c50f0-c3a3-442d-a8db-292c896cd4fc.png`. All three files decode as 1254x1254 RGBA with alpha 0..255. The on-disk native canvas is 1254x1254. The task note described a 1280px master, while the exact supplied hash and its matching native ImageGen output both measure 1254x1254. This record uses the decoded file dimensions.

The selected file has alpha-above-1 bounds `(132, 147, 1127, 1109)`. Sixty alpha-1 pixels remain in the outer 10% band, with no alpha values above 1 there. The original, candidate, and canonical source were compared by hash. The source was opened at native resolution and at 2x nearest-neighbour size. Tank, aircraft, anchor, CBRN crest, binder, and compass are whole and inside the canvas. Transparent padding is genuine. No opaque intermediate, chroma treatment, background removal, or visual-component layer was used.

The two built-in ImageGen edit calls both requested `transparent_background=true`. The first output, `C:/Users/klimp/.codex/generated_images/01a10182-5230-7fb2-978d-025e9acb274c/exec-02e7703a-1ae9-405b-af74-83c283eed22d.png`, is rejected for insufficient transparent margin and has SHA-256 `7F7F492DFFDD24A288D49C9201AEC3CD96EA0849139C4A599AEED9FB52139C12`. The second output is the selected candidate. Both exact submitted prompts, input roles, and edit deltas are retained above under `2026-10-03 authorized ImageGen candidate edit`.

### Final triplet, processor audit, and visual review

The accepted completed subject layer is `docs/assets/027_doctrine_research/processed_png/source_layers/027_doctrine_research_joint_curriculum.png`, 64x64 RGBA with alpha 0..255, visible bounds `(6, 7, 58, 57)`, SHA-256 `29224ECE990AF93DAF30C9A25AC9963F5B3ACD83B8AFB1CF4BB374166F8AF6D6`. The deterministic grey layer hash is `0EAC5362E3F4FA8E6E30CB28965D72D879FC02544FB8CE9FFDA2831486199945`. The not-eligible source hash is `B850DC02BD9FF61E26E84CA84A9FEA547D22B3043D4E5A5C2E922C145FF1EA22`.

The immutable supplied template hashes remain `248DB006611EB3942550C43DF83802AA6FB24761035FC928B5D34586C0C4C5BA` for `achievement_template.png`, `70E073694C1A7D9FE40C63B1EB2E987A8A45B3FFD15CCF789EEAA5B843B90022` for `achievement_template_grey.png`, and `89BC80C6AC975BF6F1FF000FF3070B20C337BFB8B8AE966AE35A5540C004D6DD` for the unchanged `overlay.png`.

`python -B .agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py --audit --input docs/assets/027_doctrine_research/processed_png/source_layers --output-dir gfx/achievements` returned `AUDIT OK` for First Lesson, Joint Curriculum, and Single School. All nine source layers, review PNGs, staged review PNGs, staged DDS files, and runtime DDS files were checked. Each staged review PNG is byte-identical to its review PNG, and each staged DDS is byte-identical to its runtime counterpart.

All nine review PNGs and all nine runtime DDS files were opened individually at native 64x64 and 4x nearest-neighbour size. First Lesson and Single School remain unchanged from their prior audited hashes and pass again. All three Joint Curriculum states are visually complete at native size. The red-cross overlay stays centered and intact in the not-eligible state. Each actual runtime DDS decodes pixel-for-pixel to its matching processed review PNG.

All nine DDS outputs are 64x64 and 16,512 bytes, uncompressed BGRA with a strict 128-byte legacy header and one top-level image. The DDS header's mip-count field is 0, meaning no additional mip levels. Pixel-format flags are 65, bit depth is 32, the masks are `0x00FF0000`, `0x0000FF00`, `0x000000FF`, and `0xFF000000`, texture caps are `0x1000`, and decoded alpha is 254..255. The exact triplet hashes are:

| State | Processed review PNG SHA-256 | Final runtime DDS SHA-256 |
| --- | --- | --- |
| Joint Curriculum completed | `ECE9C2CCDD7E6575EB22522FD120D9E51E140824142FE3800D86F51F5F6F543D` | `878BC382D884283C335688F5299E1A2226861F10C9624249DE4D0F6B794F72B8` |
| Joint Curriculum grey | `39C733BA310555BD09ABE404875D37625C55D83F367C65EDBE5C14720126E18E` | `BB6EA520A24B8E4C2BF3C712490649DEC0A23CB039C37B3F506FC4AEC4027614` |
| Joint Curriculum not eligible | `6DFC2F12A18876E99A3B4313879458E1D7F1A240B0C62C572997A9FAD558CEB6` | `0629D1BCF9F3341B25EF1B7E3ABBBD2CA331FA7A34AF0EE3EBE3D95AE5E5E49B` |

The current review-only contact sheet is `docs/assets/027_doctrine_research/contact_sheets/027_doctrine_research_achievement_icons_contact_sheet.png`, 1652x1097, SHA-256 `FD642EF5DD74550A575F819325F25C8E8BE88B7BEB61EC69AC9231842846CDAE`. It was opened and shows the accepted source and current triplet.

Decoded runtime DDS readbacks for the repaired Joint Curriculum triplet are available for the parent at:

- `C:/Users/klimp/AppData/Local/Temp/event027_icon_repair_audit_20261003_full_va1jre63/decoded_027_doctrine_research_joint_curriculum.png`
- `C:/Users/klimp/AppData/Local/Temp/event027_icon_repair_audit_20261003_full_va1jre63/decoded_027_doctrine_research_joint_curriculum_4x.png`
- `C:/Users/klimp/AppData/Local/Temp/event027_icon_repair_audit_20261003_full_va1jre63/decoded_027_doctrine_research_joint_curriculum_grey.png`
- `C:/Users/klimp/AppData/Local/Temp/event027_icon_repair_audit_20261003_full_va1jre63/decoded_027_doctrine_research_joint_curriculum_grey_4x.png`
- `C:/Users/klimp/AppData/Local/Temp/event027_icon_repair_audit_20261003_full_va1jre63/decoded_027_doctrine_research_joint_curriculum_not_eligible.png`
- `C:/Users/klimp/AppData/Local/Temp/event027_icon_repair_audit_20261003_full_va1jre63/decoded_027_doctrine_research_joint_curriculum_not_eligible_4x.png`

### Wiring and remaining event limits

Read-only checks confirm the three achievement IDs remain in `common/achievements/chaos_redux_achievements.txt` and all nine state aliases remain in `interface/chaosx_achievements.gfx`, each pointing to the exact root `gfx/achievements/<id>{,_grey,_not_eligible}.dds` path. No GFX or registry change was needed or made.

No frame-consumer MCP render passed, and no native game session was launched. Event 027's MCP bank, persistence, and probability work remains open. This handoff closes the requested static icon repair and audit only. It does not claim overall Event 027 completion or `Playable` status.

### Files changed in this handoff

- `docs/assets/027_doctrine_research/audit.md`
- `docs/assets/027_doctrine_research/manifest.md`
- `docs/assets/027_doctrine_research/gfx_handoff.md`
- `docs/plans/027_doctrine_research_plans/subagent_handoffs/achievement_asset_visual_refresh_2026-10-03.md`

No source images, processed PNGs, contact sheets, DDS files, GFX, gameplay files, achievement registry, git index, or commit were changed in this audit pass. Event 023 and Event 042 asset files were not edited.
