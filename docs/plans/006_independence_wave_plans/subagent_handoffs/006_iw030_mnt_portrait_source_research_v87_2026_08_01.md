# IW-030 Montenegro grounded male portrait source-research handoff v87

Date: 2026-08-01.
Subagent: `/root/event6_mnt_portrait_source_research_v87`.
Scope: real, archival, rights-clear source research for the grounded male Montenegro roster. No gameplay, character, localisation, `.gfx`, DDS, or runtime wiring was performed.

## Result

The existing v68 package remains the accepted evidence for the two named vanilla identities with visual and source/crop linkage gates passed but rights still review-pending:

- `MNT_blazo_jovanovic`: `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v68_2026_08_01/source_masters/mnt_blazo_jovanovic_livno_1942.jpg` (SHA-256 `a66cf887c8b28f86c92dedd763b3cb6bd046c01f6dff0f63825c07f30c64c120`), exact crop `source_crops/mnt_blazo_jovanovic_livno_1942_head_shoulders.png` (SHA-256 `fd5834027ece9dce94c7dd0f5a7f9b0b74559a85c2653619bc890b3fe117b880`). Commons identifies him as the central subject in the 1942 Livno group and marks the image public domain under a `PD-because` rationale, but the photographer is unknown; rights remain `NEEDS_USER_REVIEW`.
- `MNT_blazo_dukanovic`: `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v68_2026_08_01/source_masters/mnt_blazo_dukanovic_1938_1940.jpg` (SHA-256 `b099dff0ad5b45d8dd33a10c9a0ccc113d4e08afa8ca1fa7c2d5fe68b76a8be8`), exact crop `source_crops/mnt_blazo_dukanovic_1938_1940_head_shoulders.png` (SHA-256 `b626fe6089e3483f89a7fc0d553b69b16fa52ce8116b696d2f6e3362ec318cd9`). Commons explicitly identifies the subject, credits Mile S. Bjelajac's 2004 military-biography volume, and asserts `PD-old`/Public Domain Mark for an estimated 1938-1940 portrait, but the photographer/book reproduction chain is unknown; rights remain `NEEDS_USER_REVIEW`.
- `MNT_kristo_popovic` remains `BLOCKED`: the Commons `Krsto_Zrnov_Popovic.jpg` is CC BY-SA 3.0 with VRTS permission but has no machine-readable author, source, or capture date, and the Montenegrina scan has no image credit/date/license and restricts further distribution. Do not relabel either existing candidate or generate Popovic.

## New role-correct replacement lead: Mitar Martinovic

The search found a stronger documented archival candidate for an explicit roster redesign: **Mitar Martinovic (1870-1954)**, a Montenegrin divisional general who also served as prime minister, minister of war, and commander of the Lovcen Detachment. Role/life-date references: <https://encyclopedia.1914-1918-online.net/histperson/mitar-martinovic-1870-1954/> and <https://www.worldstatesmen.org/Montenegro.html>. This is a role-correct country-leader/corps-commander identity, but it is not Popovic and must not be silently assigned to `MNT_kristo_popovic`.

- Commons file page: <https://commons.wikimedia.org/wiki/File:Brigadir_Mitar_Martinovi%C4%87.jpg>.
- Canonical original: <https://upload.wikimedia.org/wikipedia/commons/3/3e/Brigadir_Mitar_Martinovi%C4%87.jpg>.
- Commons source credit: extracted from *Ilustrovana ratna kronika III broj.pdf*, page 3, published in 1912 by Izdavacka knjizarnica Svetozara F. Ognjanovica, Novi Sad.
- Underlying scan record: <https://commons.wikimedia.org/wiki/File:Ilustrovana_ratna_kronika_III_broj.pdf>.
- Serbian National Library record for the 1912 scan: <https://digitalna.nb.rs/view/URN:NB:RS:SD_5F9ABEA7946203201B672CD4AAF1F0F6>.
- Commons license basis: `PD-collective-work|Serbia`; the work was published in 1912 and is over a century old. The archive website itself displays a site-terms notice, so this handoff claims only the underlying historical publication's public-domain basis and preserves attribution/URL rather than claiming a waiver of site terms.
- Retained master: `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v87_2026_08_01/source_masters/mnt_mitar_martinovic_1912_chronicle.jpg` (684x1135 RGB JPEG, SHA-256 `202d349544bb4b36ee696120222c1ccfdb25e1a8c7213e65eef9ce910d185a76`).
- Exact source crop: `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v87_2026_08_01/source_crops/mnt_mitar_martinovic_1912_head_shoulders.png` (530x670 RGB PNG, rectangle `[80,90,610,760]`, SHA-256 `493846b7202b528ce81260a0227d5c4880575f97cc0cb45715b116390e37de2e`).
- Exact-pixel proof: `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v87_2026_08_01/crop_metadata/mnt_mitar_martinovic_1912_crop.json`; Pillow utility v1.0 reports `status=exact_source_crop_verified`, `decoded_pixels_equal=true`, equality hash `0c7f16cd55741be02cf693c2c0b6d5e92daee087ed873facb93ecb12a807b81f`.
- Review contact sheet: `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v87_2026_08_01/review/mnt_v87_source_candidates_contact_sheet.jpg`.

## Why this is a candidate, not an admission

The source is an active-life 1912 military portrait, 24 years before the 1936 scenario start. Martinovic lived until 1954 and the image shows a role-correct Montenegrin general in period uniform, but the parent must decide whether a pre-1936 historical figure is acceptable for the IW-030 roster. More importantly, replacing Popovic requires an explicit character/localisation/design amendment; identity-preserving portrait policy forbids putting Martinovic's face under Popovic's grounded name.

The v87 package intentionally stops before ImageGen repaint, deterministic 156x210 runtime candidate, independent likeness/style audit, DDS conversion, and `.gfx` wiring. An exact/variant search for `Mitar Martinovic`, `Mitar Martinović`, and likely token forms returned no matches in the current Chaos Redux tree or installed vanilla character/history/GFX/interface/localisation roots; the parent must rerun that ownership gate before admission. If the parent accepts the identity amendment, request the full grounded real-person portrait pipeline using the retained master/crop and the canonical leader/commander references. Until then, the v87 source and crop are evidence only.

## Rejected comparison leads

- Radomir Vesovic (1871-1938): Commons file <https://commons.wikimedia.org/wiki/File:Radomir_Ve%C5%A1ovi%C4%87.jpg>, circa 1910, `PD-Serbia`, but Commons records an own-work source and unknown author. Retained at `source_masters/mnt_radomir_vesovic_circa1910.jpg` (426x600, SHA-256 `3ec3233227fdf3a0d974d95e3a1542614dfb34fbe00cc061f1268bc2445e9af7`) as comparison only.
- Sekula Drljevic (1884-1945): Commons file <https://commons.wikimedia.org/wiki/File:Sekula_Drljevi%C4%87.jpg>, by 1925, `PD-Slovenia`, but political rather than corps-command role; retained at `source_masters/mnt_sekula_drljevic_by1925.jpg` (301x376, SHA-256 `9845456a8a3744e1e4fc6473ab56bc3bf0991cad45d7111182131ac53958bb5b`).
- Marko Miljanov (1833-1901): Commons file <https://commons.wikimedia.org/wiki/File:Vojvoda_Marko_Miljanov.jpg>, pre-1901, `PD-Serbia`; deceased before the 1936 start and rejected for the live roster; retained at `source_masters/mnt_marko_miljanov_pre1901.jpg` (629x974, SHA-256 `06c2e6026211e0a9ee70b93e229e598feb5e242ed702a2137f1c8520433a3bca`).
- `rejected_candidates/mnt_milutin_vucinic_1922.jpg` and `rejected_candidates/mnt_radomir_vesovic_lim_1912.jpg` are 429-response HTML retrieval failures, not image sources; they were not processed or selected.

## Parent action required

1. Keep Jovanovic and Dukanovic evidence-only until independent rights review resolves the unknown-photographer issues.
2. Keep Popovic blocked unless a defensible attributed archival source with author/source/date/license evidence is found.
3. If desired, accept or reject the explicit Mitar Martinovic identity amendment. Acceptance must name the new stable character/localisation identity and then request the normal full real-person portrait pipeline. No source-research asset can authorize a silent relabel, generated substitute, DDS, or runtime wiring.
