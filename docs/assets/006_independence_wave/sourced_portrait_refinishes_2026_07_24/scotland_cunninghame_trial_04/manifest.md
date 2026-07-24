# R. B. Cunninghame Graham source-locked portrait trial 04

Status: `candidate_requires_independent_review`.

This package retries the grounded real-male IW-001 Scotland civic-leader portrait after trial 03 failed the exact-identity gate.

No DDS, runtime, GFX, gameplay, advisor, dossier, `_small`, female, fictional, flag, focus, decision, or localisation asset is authorized by this package.

## Subject and role

- Event 006 package: IW-001 Scotland, using the vanilla `SCO` carrier additively.
- Stable consumer: `SCO_independence_wave_civic_convention`.
- Subject: Robert Bontine Cunninghame Graham, 1852 to 1936.
- Role basis: Scottish politician and writer, founding president of the National Party of Scotland, and first president of the Scottish National Party.
- Source-mode classification: `grounded_source_only`.
- Gender contract: male only.
- Ownership disposition: prior exact and variant searches found no active vanilla or current Chaos Redux character or portrait owner, while reference-mod same-person use remains disclosure-only and grants no permission to copy art or sources.

## Unchanged archival sources

- Primary source page: <https://commons.wikimedia.org/wiki/File:Photo_of_R._B._Cunninghame_Graham.jpg>.
- Primary archive record: <https://babel.hathitrust.org/cgi/pt?id=coo1.ark:/13960/t6xw50w29;view=1up;seq=191;size=150>.
- Primary rights basis: photograph published no later than 1907 with photographer unstated, recorded by Commons as `PD-US-expired`.
- Unchanged primary master: `source_masters/SCO_cunninghame_graham_hathitrust_1907.jpg`, `813x1101`, SHA-256 `401CC30D278122A6CC99B691E913A63C568A2EF82E1E0AE0513DC93F303D4FBB`.
- Explicit primary head-and-shoulders crop coordinates: `(120, 120, 700, 900)`.
- Explicit primary crop: `source_crops/SCO_cunninghame_graham_hathitrust_head_shoulders.png`, `580x780`, SHA-256 `BC30EE3CCF31D8E31656678BF8B703658189E83CB300889E3461BFBA9A73B56A`.
- Same-person source page: <https://www.rijksmuseum.nl/en/collection/object/Portret-van-Robert-Bontine-Cunninghame-Graham--58d50c7b9bd272d04b216d7494101918>.
- Same-person rights basis: Rijksmuseum CC0 and public-domain record for an anonymous Bassano cliché from approximately 1881 to 1891.
- Unchanged same-person master: `source_masters/SCO_cunninghame_graham_rijksmuseum.jpg`, `3846x4852`, SHA-256 `5D646596028A8A069651207E2058E8B59BDF7276D28921FD2A1DDEFE2FF7ABE7`.
- Explicit same-person crop coordinates: `(990, 735, 2900, 3310)`.
- Explicit same-person crop: `source_crops/SCO_cunninghame_graham_rijksmuseum_identity_crop.png`, `1910x2575`, SHA-256 `49CB8464CB15A451C16FC0728E60963B93E3E4742C86F07BC923C35B83586069`.
- Date caveat: both sources show a younger or middle-aged Cunninghame Graham, so the repaint preserves the sourced age and does not invent a 1936-age reconstruction.

## Source-locked ImageGen repaint

- ImageGen mode: built-in `identity-preserve` edit.
- Identity input: only `source_crops/SCO_cunninghame_graham_hathitrust_head_shoulders.png`.
- The same-person Rijksmuseum image was retained for audit comparison and was not passed to ImageGen.
- No external face or style image was passed to ImageGen.
- The exact prompt is retained at `prompts/SCO_cunninghame_graham_identity_preserve_trial_04.txt`.
- Raw ImageGen result: `imagegen_results/SCO_cunninghame_graham_identity_preserve_trial_04.png`, `1082x1454`, SHA-256 `3A34FFBE6A546F0F9E432C49B23019DCF3845DFF0E17BAB981AC1D59E991C106`.
- The repaint request locks the narrow face, natural eye asymmetry, eyelid openings, nose, ears, moustache, beard, hair, expression, pose, collar, cravat, coat, and crop.
- The repaint request changes only the rendering medium and neutral tonal backdrop.

## Deterministic 156x210 processing

- Processor: `.agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py`.
- Mode: `leader`, which is the processor's full-size `156x210` country-leader and commander export mode.
- Source kind: `real`.
- Raw-result crop: `(0, 0, 1082, 1454)`.
- Canonical comparison family: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/`.
- Processed candidate: `processed_png/portrait_SCO_independence_wave_civic_convention.png`, `156x210`, SHA-256 `C3589D65BDD348450C53A8B895775987D5F8C3B730C70DC8D82DE3E0DD2423C2`.
- Processor metadata: `metadata/SCO_cunninghame_graham_processing.json`, SHA-256 `9F98C5554E3DE61089C5A5C48E347FC85F2990CE438716208F2FBC716DAE455C`.
- Processor review sheet: `contact_sheets/SCO_cunninghame_graham_processor_style_comparison.png`, SHA-256 `F9FF63C0DE120E77989EABDBD188F731F51764D1487ABEF164F833B8C555A091`.

## Independent-audit evidence

- Full identity-chain sheet: `contact_sheets/SCO_cunninghame_graham_identity_chain.png`, SHA-256 `34A1FE8DF904E5A3F4DADC4F7166D24E822FD1F1F356E9ACDA08B2C8A1C0E3BF`.
- Matched native and 4x nearest-neighbour sheet: `contact_sheets/SCO_cunninghame_graham_native_4x_identity_comparison.png`, SHA-256 `69F53766C89FA0FAAB047E7DC33F18A285679CCBB5E82458F8AF5FD3CFC58619`.
- Style-only audit reference: `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/leaders/den_thorvald_stauning.png`, SHA-256 `08732002182BDCB2BFF3D78B142CC2B3D75ADBDB29D4115F9E89CA5BDC6A21B6`.
- The independent reviewer must open the unchanged master, explicit crop, raw result, processed candidate, and role-specific references separately at native resolution in addition to using the contact sheets.
- Provenance, exact likeness, HOI4 painted style, role fit, and ownership require separate verdicts.
- Exact identity is non-compensable and must fail if the face, eye asymmetry, moustache, beard, hair, age, expression, pose, or source-visible clothing drifts.

## Runtime gate

No DDS exists.

Do not convert, copy, register, wire, or use this candidate until an independent reviewer who did not produce it records PASS for provenance, exact likeness, HOI4 painted style, role fit, and ownership.

Even after a portrait PASS, IW-001 remains closed until Victor Morven Fortune and Cunninghame Graham are both wired to exact runtime DDS files and a fresh full Scotland country-package audit passes.
