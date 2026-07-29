# IW-006 Wallonia Fernand Jacquet trial 01 independent portrait audit

Audit date: 2026-07-25.

Reviewer: /root/event6_wallonia_jacquet_trial01_audit (independent sourced-portrait reviewer).

## Decision

FAIL / rejected_and_unwired.

The identity-preservation gate fails because the repaint visibly broadens the lower face, enlarges and shifts the eyes, changes the wire-rim glasses, and thickens and curls the moustache relative to the unchanged archival subject.

The provenance gate also fails closed because the Commons public-domain assertion is an anonymous-author template and the underlying Memorix/Heuvel record identifies no photographer or separate archive rights certificate.

No DDS conversion, .gfx edit, character edit, localisation edit, sprite replacement, or runtime wiring was performed by this reviewer.

## Independence and scope

This reviewer did not source, crop, generate, process, or author the candidate package and is separate from the source-clearance and producing work.

The candidate package was reviewed at docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_25/wallonia_fernand_jacquet_trial_01/.

The source-clearance package was reviewed at docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/walloon_role_source_clearance/.

The named source handoff was reviewed at docs/plans/006_independence_wave_plans/subagent_handoffs/2026-07-25_event6_wallonia_alt_source_clearance.md.

No files outside this handoff were edited.

## Required references consulted

The offline portrait and graphics references consulted were paradox_wiki/Portrait modding - Hearts of Iron 4 Wiki.md, paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md, and paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md.

The canonical reference-library rules and catalog were consulted at .agents/skills/chaos-redux-event-assets/assets/vanilla_reference/README.md and .agents/skills/chaos-redux-event-assets/assets/vanilla_reference/CATALOG.md.

The role-specific canonical commander folder and contact sheet were consulted at .agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/ and .agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/contact_sheet.png.

The selected commander references were inspected at native 156x210 and at deterministic nearest-neighbour 4x 624x840 enlargement: eng_bernard_montgomery.png and ger_erwin_von_witzleben.png.

All nine 156x210 commander references in the canonical folder were also inspected in a temporary nearest-neighbour 4x comparison view outside the repository; that temporary view was not retained.

## Artifact and hash audit

The unchanged package master is source_masters/AFX_fernand_jacquet_1915_master.jpg, decoded as RGB 4579x3521, with recomputed file SHA-256 1c9ab5216e175fc7c47d4571810ba97f599f53dc510a6bd3330366aac036fcf6, matching the package manifest and the clearance master.

The exact package crop is source_crops/AFX_fernand_jacquet_1915_head_shoulders.png, decoded as RGB 2100x2100, with recomputed file SHA-256 9bf20613f007bb6291d456caa88f67f4ec3651c7604adefdcd437ac5adead33d.

The crop rectangle is half-open (1500, 500, 3600, 2600) from the unchanged 4579x3521 master.

The crop equality JSON is source_crops/AFX_fernand_jacquet_1915_head_shoulders.json, with recomputed file SHA-256 25545a1b84f30d4b552d68c8bd3802c432f48fd2ec087c72234fc1a348a0245e4.

Reopening both package files with Pillow and comparing the decoded RGBA rectangle produced decoded_pixels_equal: true, pixel_count: 4410000, and matching RGBA digest ad643ebc4f30c9ea4349671ac2e0725c56f9899ae353cbafb863aff58c9f92e6.

The raw source-locked ImageGen repaint is imagegen_results/AFX_fernand_jacquet_identity_preserve_trial_01.png, decoded as RGB 1023x1537, with recomputed file SHA-256 600f4065155e6cc559e9091d84f9a6a2e329279bfe07ef313b9b59f6c7c213df, matching the processing metadata.

The deterministic candidate is processed_png/portrait_AFX_walloon_reserve_commander.png, decoded as RGBA 156x210, with recomputed file SHA-256 a7e5a862270a0870974aa366256830bebe09a5936ff9fd477fead2cf08386180 and repository processor decoded-RGBA SHA-256 d2cf4550810c426f4cefc3d00c9804bcffa58f379c02adf18eae2fe379e94a26, both matching the metadata.

The candidate alpha channel is fully opaque (255, 255), matching the full commander texture family rather than an advisor or dossier-card surface.

The processing metadata is processed_png/portrait_AFX_walloon_reserve_commander.png.json, with recomputed file SHA-256 57fbd782505eff01bec358d948c118bcaf17716559da78da9b7740f0975fd47c.

The metadata records processor the retired portrait-processing utility version 5.0, role family commander, source kind real, positional mode leader, and raw crop (0, 0, 1023, 1377).

The metadata canonical payload hash recomputes to 86f6425cf6e1b50647271d0ca4cf467d39c04c77a2b3b6ddebd1ea86f09f480c, matching metadata_integrity.payload_sha256.

The processor review sheet is review/AFX_fernand_jacquet_commander_style_sheet.png, decoded as RGBA 1344x464, with recomputed file SHA-256 9fe04d105d92f5b63201fc37e101fd5dfdcad9803d99a26edfc17702aab9ed5d and repository decoded-RGBA SHA-256 741d9d55eab624eb1e8fde4f713f3cdf2d40ebaa72435a27b2a4456f7926755a, matching metadata.

The selected canonical commander reference hashes match the processing metadata: eng_bernard_montgomery.png 39b03871d7451ca96712a5ccf3c056528693f82642776e6c5e297e041943944e and ger_erwin_von_witzleben.png 10f4a1108f9d440213f70fb5802349a2291f298f9d132644241119561577d5b6.

The package contains no DDS, _small, female, advisor, dossier, operative, generic, miniature, or fallback derivative.

## Identity and visual audit

| Identity or style feature | Independent finding | Gate |
| --- | --- | --- |
| Narrow oval face | The archival face is narrow and vertically oval, while the repaint fills and broadens the lower face and cheeks; the processed candidate retains that broader shape at native and 4x. | FAIL |
| Forehead and hair waves | The high forehead, side-parted dark hair, and asymmetric forehead waves remain recognizable in the raw repaint and processed candidate. | PASS |
| Brow height and shape | Brow placement is retained, but the repaint darkens and regularizes the brows slightly. | PASS with minor stylization |
| Eye spacing and direction | The repaint enlarges the eyes and shifts the gaze toward a more forward, open look instead of preserving the source eye proportions and direction. | FAIL |
| Thin wire-rim glasses | The source has very thin, subtle wire rims; the repaint uses larger, brighter, rounder rims with a heavier bridge and more visible lens circles. | FAIL |
| Nose bridge and length | The source nose is straight and narrow; the repaint broadens the bridge and rounds the tip, changing the central facial geometry. | FAIL |
| Moustache width and tips | The repaint darkens and thickens the moustache, extends it wider, and turns the tips upward more than the source. | FAIL |
| Closed mouth | The mouth remains closed and neutral, with no open-mouth or teeth invention. | PASS |
| Cheeks | The repaint adds fuller cheek volume and reduces the source's narrow cheek planes. | FAIL |
| Jaw and chin | The repaint broadens and rounds the jaw and chin, especially below the moustache. | FAIL |
| Visible ear | The source-visible ear is retained on the right side, but the repaint enlarges and reshapes it slightly. | PARTIAL; identity gate remains failed |
| Age | The candidate remains a young adult male in the source's age band and does not age-shift the subject. | PASS |
| Expression | The upright neutral expression is broadly retained, though the repaint reads slightly more stern because of the enlarged eyes and heavier moustache. | PASS with minor stylization |
| Head angle | The near-frontal upright head angle and shoulder alignment are preserved. | PASS |
| Collar insignia | Star insignia remain in source-visible collar locations; painterly simplification prevents exact native-size star counting, but no unsupported medal or emblem is apparent. | PASS for visible placement |
| Shoulder strap | The shoulder strap and its button remain in the source-visible location. | PASS |
| Tunic pockets | Both upper flap pockets and the buttoned tunic front remain recognizable and correctly placed. | PASS |
| Aviator badge | The winged aviator badge remains on the source-visible sleeve in the same general position and silhouette. | PASS |
| Hidden or invented insignia | No new flag, text, medal bar, second person, or unsupported uniform ornament was observed. | PASS |
| Face asymmetry | Source asymmetry is softened by the repaint's smoother, more symmetrical lower-face construction. | FAIL as an identity-preservation detail |

Identity is a separate non-compensable gate, so the style passes below cannot offset these facial changes.

## Style, composition, role, and ownership gates

The raw repaint and deterministic candidate use subdued olive-gray military colors, restrained oil/gouache brushwork, a quiet dark vignette, and a head-and-shoulders commander composition consistent with the canonical HOI4 commander family.

The candidate has no border, lettering, UI frame, flag, modern prop, extra person, or advisor-card treatment.

The candidate is a full opaque 156x210 portrait, not a fabricated 50x67 texture, and the face remains readable at native size and at 4x nearest-neighbour enlargement.

The candidate is male-presenting and is assigned only to the existing full-size civilian-large and army-large consumers of AFX_walloon_reserve_commander.

The stable consumer boundary remains AFX_walloon_reserve_commander and GFX_portrait_AFX_walloon_reserve_commander.

The current Chaos Redux character definition is common/characters/006_independence_wave_wallonia_frisia_characters.txt:53-61, with gender = male and both civilian.large and army.large pointing to the stable sprite.

The current history recruit is history/countries/AFX - Wallonia.txt:18, and the current localisation still names the rejected working identity as Marcel Delcourt in localisation/english/006_independence_wave_wallonia_frisia_l_english.yml:4.

The existing runtime texture path gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander.dds already exists for the current working identity and was not replaced; the candidate package contains no DDS and no candidate wiring.

Exact and variant ownership searches covered Fernand, Jacquet, Maximillian, Maximilien, AFX_walloon_reserve_commander, and GFX_portrait_AFX_walloon_reserve_commander in current Chaos Redux, installed vanilla, Kaiserreich 1521695605, approved reference mods 2265420196 and 1458561226, restricted to character definitions, country histories, leader graphics, interfaces, and English localisation.

The only current-project hit is the existing AFX_walloon_reserve_commander token and sprite, which are the stable consumer boundary rather than an exact Fernand Jacquet owner; no exact Jacquet character, portrait, leader, commander, operative, or named-officeholder owner was found in the audited roots.

No guarded transfer contract exists because no exact owner was found; the parent must not perform any runtime replacement from this failed candidate.

The style and role gates pass, and the ownership search is clear, but the overall identity decision remains failed.

## Provenance and rights audit

The source page is https://commons.wikimedia.org/wiki/File:Fernand_Jacquet_vers_1915.jpg and the archived image is dated circa 1915.

The source-clearance record identifies the underlying archive as Memorix/Heuvel and the IIIF identifier as 139408cf-33f3-40a1-263f-b94d9468700a.

The unchanged image was sourced from the recorded IIIF endpoint and mirrored by the Commons file page; the package master hash and dimensions match the clearance package exactly.

The saved Commons page snapshot records Source as the Memorix image endpoint and Author as Unknown author.

The Commons page applies a public-domain template based on no public claim of authorship and the PD-EU-no_author_disclosure and PD-old reasoning, with a public-domain marker and no attribution requirement.

The local JPEG has no EXIF author or copyright metadata, consistent with the unidentified photographer record.

The archive record supplied in the package names no photographer and provides no separate rights certificate or archive-issued license statement.

This is usable provenance evidence for review, but it is not a defensible final rights clearance for the mod package without user or legal confirmation of the anonymous-author public-domain basis.

The rights uncertainty is therefore a fail-closed provenance gate and a precise independent reason for rejecting the candidate.

## Validation evidence and residual risks

The unchanged master, exact crop, crop-equality JSON, raw repaint, deterministic candidate, processor metadata, review sheet, native commander references, and nearest-neighbour 4x reference views were all inspected.

The source crop equality and all listed file hashes recomputed successfully, and the processor metadata integrity recomputed successfully.

The independent visual review found the candidate's HOI4 commander style and composition acceptable, but identity quality is not acceptable for a grounded real-person portrait.

The candidate remains candidate_requires_independent_audit in its manifest and must remain unwired.

No fallback, generic substitute, female portrait, advisor icon, commander-small card, operative image, or other forbidden derivative was created.

Residual risks are the non-compensable identity drift and unresolved anonymous-photographer rights basis; either issue independently blocks promotion.

The parent may retain the package as rejected evidence and may request a new source-locked repaint trial only after the rights question is resolved and the identity-preservation prompt is tightened against lower-face, eye, glasses, and moustache drift.
