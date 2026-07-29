# Event 006 Scotland Cunninghame Graham trial 04 independent audit

This handoff records an independent fail-closed audit of the grounded real-male portrait trial 04 package on 2026-07-24 by the sourced-visual asset reviewer.

The reviewer did not create, repaint, process, overwrite, convert, or wire any candidate asset in the audited package.

No gameplay, GFX, localisation, character, country, DDS, advisor, dossier, `_small`, female, commander, alternate-country, or runtime file was edited by this audit.

## Audited package and intended consumer

The audited package is `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_24/scotland_cunninghame_trial_04/`.

The intended Event 006 consumer is the additive vanilla `SCO` carrier for IW-001 Scotland Civic Convention.

The stable character token is `SCO_independence_wave_civic_convention` and the stable sprite is `GFX_portrait_SCO_independence_wave_civic_convention`.

The requested surface is a male full-size `156x210` country-leader portrait only.

The subject is Robert Bontine Cunninghame Graham, 1852 to 1936, a Scottish politician and writer, founding president of the National Party of Scotland, and first president of the Scottish National Party.

The package remains source-mode `grounded_source_only` and does not authorize a fictional likeness or invented age reconstruction.

## Source provenance and rights evidence

The unchanged primary source page is <https://commons.wikimedia.org/wiki/File:Photo_of_R._B._Cunninghame_Graham.jpg>.

The primary archive record is <https://babel.hathitrust.org/cgi/pt?id=coo1.ark:/13960/t6xw50w29;view=1up;seq=191;size=150>.

The Commons record identifies Robert Bontine Cunninghame Graham, dates the photograph no later than 1907, leaves the photographer unstated, and records a `PD-US-expired` public-domain basis.

The unchanged primary master is `source_masters/SCO_cunninghame_graham_hathitrust_1907.jpg`, RGB `813x1101`, SHA-256 `401CC30D278122A6CC99B691E913A63C568A2EF82E1E0AE0513DC93F303D4FBB`.

The primary crop coordinates are `(120, 120, 700, 900)`.

The primary crop is `source_crops/SCO_cunninghame_graham_hathitrust_head_shoulders.png`, RGB `580x780`, SHA-256 `BC30EE3CCF31D8E31656678BF8B703658189E83CB300889E3461BFBA9A73B56A`.

Independent pixel comparison proved that the primary crop equals the exact `(120,120,700,900)` region of the unchanged primary master with zero differing pixels.

The same-person comparison source page is <https://www.rijksmuseum.nl/en/collection/object/Portret-van-Robert-Bontine-Cunninghame-Graham--58d50c7b9bd272d04b216d7494101918>.

The Rijksmuseum record identifies Alexander Bassano, circa 1881 to in or before 1891, subject Robert Bontine Cunninghame Graham, and marks the object public domain.

The package records the Rijksmuseum rights basis as CC0 and public domain, while this audit relies on the current public-domain museum record and retains the source attribution.

The unchanged same-person master is `source_masters/SCO_cunninghame_graham_rijksmuseum.jpg`, RGB `3846x4852`, SHA-256 `5D646596028A8A069651207E2058E8B59BDF7276D28921FD2A1DDEFE2FF7ABE7`.

The same-person crop coordinates are `(990, 735, 2900, 3310)`.

The same-person crop is `source_crops/SCO_cunninghame_graham_rijksmuseum_identity_crop.png`, RGB `1910x2575`, SHA-256 `49CB8464CB15A451C16FC0728E60963B93E3E4742C86F07BC923C35B83586069`.

Independent pixel comparison proved that the same-person crop equals the exact `(990,735,2900,3310)` region of the unchanged Rijksmuseum master with zero differing pixels.

Both sources show a younger or middle-aged Graham, so the repaint preserves the sourced age and does not claim a historically reconstructed 1936-age face.

## Identity-preserving repaint and deterministic processing

Only `source_crops/SCO_cunninghame_graham_hathitrust_head_shoulders.png` was passed to the built-in `identity-preserve` ImageGen edit.

The Rijksmuseum image was retained solely for independent same-person comparison and was not passed to ImageGen.

No external face reference or style image was passed to ImageGen.

The exact executed prompt is retained at `prompts/SCO_cunninghame_graham_identity_preserve_trial_04.txt`, SHA-256 `E66935270FE51B8A35871CF6C19E06221F64A9ED844564CFF624D4BBA2FE399A`.

The prompt explicitly locks the long narrow facial geometry, natural unequal eye openings, eyelids, nose, ears, moustache, pointed beard, hair, direct serious expression, age, frontal pose, collar, cravat, coat, and crop, while forbidding hidden detail, insignia, jewelry, modern props, text, and genericization.

The raw ImageGen result is `imagegen_results/SCO_cunninghame_graham_identity_preserve_trial_04.png`, RGB `1082x1454`, SHA-256 `3A34FFBE6A546F0F9E432C49B23019DCF3845DFF0E17BAB981AC1D59E991C106`.

The deterministic processor is `the retired portrait-processing utility` at SHA-256 `C6E78C01C025AD57FEF8DC25EB79BD216FF9809DF27E4C758EB9EC72594A3963`.

The processor metadata is `metadata/SCO_cunninghame_graham_processing.json`, SHA-256 `9F98C5554E3DE61089C5A5C48E347FC85F2990CE438716208F2FBC716DAE455C`.

The processor ran in `leader` mode with source kind `real`, full-result crop `(0,0,1082,1454)`, Python `3.9.12`, Pillow `11.1.0`, and render version `2.0`.

Independent metadata checks recomputed the recorded raw decoded RGBA hash, output decoded RGBA hash, review-sheet decoded RGBA hash, processor hash, payload hash, and saved-file hashes without mismatch.

The processed candidate is `processed_png/portrait_SCO_independence_wave_civic_convention.png`, opaque RGBA `156x210`, file SHA-256 `C3589D65BDD348450C53A8B895775987D5F8C3B730C70DC8D82DE3E0DD2423C2`.

The processed candidate decoded RGBA SHA-256 recorded by metadata is `51E6F3B60454219AC5024D90F93829FE6CEAAFB998E83B5DAAD485D374211585`.

The processor style sheet is `contact_sheets/SCO_cunninghame_graham_processor_style_comparison.png`, SHA-256 `F9FF63C0DE120E77989EABDBD188F731F51764D1487ABEF164F833B8C555A091`.

The identity-chain sheet is `contact_sheets/SCO_cunninghame_graham_identity_chain.png`, SHA-256 `34A1FE8DF904E5A3F4DADC4F7166D24E822FD1F1F356E9ACDA08B2C8A1C0E3BF`.

The package native and 4x comparison sheet is `contact_sheets/SCO_cunninghame_graham_native_4x_identity_comparison.png`, SHA-256 `69F53766C89FA0FAAB047E7DC33F18A285679CCBB5E82458F8AF5FD3CFC58619`.

An additional disposable 4x nearest-neighbour audit sheet placed outside the repository compared both unchanged source crops, the raw result, the processed candidate, and the role reference in a common `156x210` frame.

The package manifest is `manifest.md`, SHA-256 `F841F1D97A43FA4AED8C2A62B71EAEB98528980E93895F7D83F068E872ACCACD`.

The package GFX handoff is `gfx_handoff.md`, SHA-256 `92C77962338EB72737AAB022FB27D5E85B6F1363E958856D6B922ED9AAA2F460`.

The package hash ledger is `hashes.sha256`, SHA-256 `C484EF25C7C1E2244580FD3B5878DC5B47B44CFA00AFCDCCD63D9E7DC1A8BBF6`.

## Independent visual verdicts

### Provenance and rights: PASS

The primary Commons/HathiTrust source is attributed and has a defensible public-domain basis, and the Rijksmuseum cross-check has a current public-domain museum record.

Both masters are unchanged, both crops are exact pixel regions of their masters, and all package hashes and deterministic metadata checks agree.

The rights conclusion relies on the primary Commons/HathiTrust source for the candidate input and preserves archive and museum attribution for the corroborating source.

### Exact likeness and identity: PASS

Native and 4x nearest-neighbour inspection show the repaint retaining Graham's long narrow facial planes, high forehead, unequal deep-set eye openings, eyelid asymmetry, direct serious gaze, long straight nose, ear placement, curled moustache, pointed beard, wavy hair mass and hairline, frontal head scale, shoulder placement, collar, cravat, dark coat, and source age band.

The raw repaint and deterministic `156x210` candidate remain the same person rather than a generic Victorian bearded man.

No opened-eye or symmetrization drift, face broadening, beautification, nose shortening, moustache rounding, beard substitution, expression change, pose change, hidden-detail invention, or source-visible clothing drift was observed.

The identity gate is non-compensable and passes only because the identity-critical structure remains legible at native and enlarged inspection.

### HOI4 political-leader style: PASS

The candidate is a full opaque `156x210` painted leader portrait with modeled facial planes, restrained warm-gray period toning, a quiet backdrop, readable head-and-shoulders framing, and no text, watermark, UI, modern prop, or raw photographic finish.

The candidate was compared with canonical and curated male leader references, including `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/den_thorvald_stauning.png`, whose SHA-256 is `08732002182BDCB2BFF3D78B142CC2B3D75ADBDB29D4115F9E89CA5BDC6A21B6`.

The other canonical leader references inspected were `ire_eamon_de_valera.png` SHA-256 `FF5F8689F1E8EA75BF88BEA4C4A87DCF60518B1E062EA53BE4A9CEFF3509DCB0`, `fin_carl_mannerheim.png` SHA-256 `7E78E33E0B691B96B584393F2D363C07A302320F7E6300BDA0FFF261AA98D49E`, and `ice_sveinn_bjornsson.png` SHA-256 `860726D268873F21AE0DBD6FB170482F50FAD6393882B97B2B7B7A1814189D14`.

The canonical leader contact sheet hash is `8966AE351D1FE8FC13D47CA1C59EC3D8A34DA9101CE5FD65F7ACFF3421BD0401`, and the curated male-leader contact sheet hash is `BF1AC6A6ED7F1D91B3FA8E4069C7B9F396BB63F450AF1FE340005F7981A3CB60`.

The source-derived rendering is visibly painterly and belongs to the intended political-leader style family rather than a filter-only or photographic output.

### Role fit and gender contract: PASS

The source depicts a male civilian Scottish political and civic leader in period formal clothing, matching the Civic Convention country-leader slot.

The candidate does not introduce an advisor, dossier, commander, `_small`, female, fictional, alternate-country, or second-sprite derivative.

The sourced age caveat is disclosed and does not undermine role fit because the package explicitly avoids inventing a 1936-age reconstruction.

### Ownership and exclusivity: PASS

Exact and variant searches for `Robert Bontine Cunninghame Graham`, `R. B. Cunninghame Graham`, `Cunninghame Graham`, `Cunninghame-Graham`, `Cunninghame_Graham`, and `Cunninghame` found no active vanilla or current Chaos Redux character, portrait, recruitment, interface, GFX, or localisation owner beyond the intended Event 006 display key.

The current Chaos Redux prospective consumer is `common/scripted_effects/006_independence_wave_scotland_wales_package_effects.txt:210-225`, where the generated character is male and receives `GFX_portrait_SCO_independence_wave_civic_convention` as its large civilian portrait.

The display localisation is `localisation/english/006_independence_wave_scotland_wales_l_english.yml:2` with `SCO_independence_wave_civic_convention: "R. B. Cunninghame Graham"`.

The existing sprite declaration is `interface/006_independence_wave_region_01_portraits.gfx:54-55` and points to the stable runtime DDS path reserved for this consumer.

Approved reference-mod searches found no exact same-person hit, and no reference-mod art or source was copied into this package.

## Runtime authorization and remaining gate

All five required independent verdicts are PASS.

The parent is authorized to convert only the exact processed candidate `processed_png/portrait_SCO_independence_wave_civic_convention.png` to `gfx/leaders/006_independence_wave/portrait_SCO_independence_wave_civic_convention.dds` with the stable sprite `GFX_portrait_SCO_independence_wave_civic_convention`.

The authorized runtime target is the full `156x210` country-leader portrait only.

No advisor, dossier, `_small`, female, fictional, alternate, second, or copied-reference derivative is authorized.

This audit did not create or replace any DDS.

The repository currently contains an older DDS at the stable path with size `131168` bytes and SHA-256 `D2FA024AF32069DD83AEDC13190772FB0C02CCCF0947AF83C4A1317767CC245B`, and this audit does not approve that older file as trial 04 output.

Even after portrait conversion, IW-001 remains closed until Victor Morven Fortune and Cunninghame Graham are both wired to exact runtime DDS files and a fresh full Scotland country-package audit passes.

## Simplifications, omissions, and blockers

No simplification or identity substitution was used in trial 04.

No source-rights, crop, deterministic-processing, likeness, style, role, gender, or ownership blocker remains for this portrait candidate.

The only remaining work is the parent-owned DDS conversion, runtime wiring review, and fresh full Scotland package admission audit.
