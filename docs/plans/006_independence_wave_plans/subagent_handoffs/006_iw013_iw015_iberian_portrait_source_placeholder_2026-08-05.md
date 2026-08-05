# Event 006 IW-013 NAV / IW-015 GLC primary portrait source-placeholder production handoff

Date: `2026-08-05`.

Owner scope: portrait-only production for the primary grounded candidates selected by the parent: NAV José Antonio Aguirre and GLC Alfonso Daniel Rodríguez Castelao.

Disposition: `SOURCE_PLACEHOLDER_READY / REPLACEMENT_PENDING`; this handoff does not claim a final HOI4-style replacement, package admission, or gameplay completion.

## Changed runtime and evidence files

- Added `interface/006_independence_wave_iberian_portraits.gfx` with stable sprites `GFX_portrait_NAV_jose_antonio_aguirre` and `GFX_portrait_GLC_alfonso_daniel_castelao` pointing to `gfx/leaders/006_independence_wave/`.
- Added runtime `gfx/leaders/006_independence_wave/portrait_NAV_jose_antonio_aguirre.dds` and `gfx/leaders/006_independence_wave/portrait_GLC_alfonso_daniel_castelao.dds`.
- Added active evidence workspace `docs/assets/006_independence_wave/source_placeholder_2026_08_05_iberian/` containing copied source masters, source pages, person-only prompt records, exact crops, crop JSON, deterministic processing JSON, processed PNGs, temporary DDS copies, decoded DDS PNGs, validation JSON, comparison sheets, manifest, and SHA-256 ledger.
- Added this handoff under `docs/plans/006_independence_wave_plans/subagent_handoffs/`.
- Durable source archive files under `docs/assets/portraits/006_independence_wave/` were preserved byte-for-byte and not replaced.

## NAV Aguirre package

- Source: `docs/assets/portraits/006_independence_wave/portrait_NAV_jose_antonio_aguirre_source.jpg`, `669x1024` RGB, SHA-256 `1d34f7b23459f750dcbfcb8e300dc3d41f7087c4b24caf544d6ab2f8671e6bc9`.
- Provenance: Pascual Marín, Marín Collection, GureGipuzkoa photo 1112433, Aberri Eguna 1933; source page `https://commons.wikimedia.org/wiki/File:Jose_Antonio_Agirre,_Aberri_Eguna_1933.jpg`.
- Rights: Commons body/category CC BY-SA 3.0 with a machine-readable CC BY-SA 4.0 discrepancy; attribution/share-alike and independent rights review remain required, and public-domain status is not claimed.
- Exact crop: `232x275` RGB, rectangle `[268,235,500,510]`, SHA-256 `960948067a1478798f82da673099fff1d34bf9ca23b29bfa7fc8490ebf80f366`; equality JSON `docs/assets/006_independence_wave/source_placeholder_2026_08_05_iberian/metadata/portrait_NAV_jose_antonio_aguirre_source_crop.json` reports `exact_source_crop_verified` and `decoded_pixels_equal=true`.
- Processed placeholder: `docs/assets/006_independence_wave/source_placeholder_2026_08_05_iberian/processed_png/portrait_NAV_jose_antonio_aguirre.png`, `156x210` RGB, SHA-256 `15fab20a126a5201f95dfc8b70096cbe670731002680396d76e812051f810cc0`.
- Runtime DDS: `gfx/leaders/006_independence_wave/portrait_NAV_jose_antonio_aguirre.dds`, SHA-256 `8f38eefc44b92fbd2f55ca9bc1752fc4569050a4b8d1721ccb2bb587bc35ef73`; temporary copy is `final_dds/portrait_NAV_jose_antonio_aguirre.dds`.
- DDS validation passes `DDS ` magic, 124-byte header, `156x210`, exact `131168` bytes, 32-bit BGRA masks, flags `65`, `DDSCAPS_TEXTURE`, no mipmaps, alpha `255..255`, runtime-copy hash equality, and decoded-pixel equality to the processed PNG; validation JSON is `review/portrait_NAV_jose_antonio_aguirre_dds_validation.json`.
- Decoded DDS RGBA SHA-256 is `a46c355acd11daa0fb736a8ec6bf39e771c899aa90f9e1ac0cd8d62f937852a5`; review PNG is `review/decoded_dds/portrait_NAV_jose_antonio_aguirre.png`.

## GLC Castelao package

- Source: `docs/assets/portraits/006_independence_wave/portrait_GLC_alfonso_daniel_castelao_source.png`, `620x634` L, SHA-256 `e022556b94a983f590dc2accde2dc6d6261fbe19369f688e4cca2f0adcdaa242`.
- Provenance: `Vida gallega`, issue 442, 10 March 1930, Galiciana/Biblioteca Dixital de Galiza, original author unknown; source page `https://commons.wikimedia.org/wiki/File:Castelao_Vida_Gallega_442.png`.
- Rights: Commons Public domain / CC-PD-Mark and PD-old-80 wording, but unknown original author and scan-chain jurisdiction remain a rights-review caveat.
- Exact crop: `464x622` L, rectangle `[88,8,552,630]`, SHA-256 `1fb10ebf8c7f5d9e97f81d1ed93a7442cbf9f83561e911a1c65a09f68b8ff232`; equality JSON `docs/assets/006_independence_wave/source_placeholder_2026_08_05_iberian/metadata/portrait_GLC_alfonso_daniel_castelao_source_crop.json` reports `exact_source_crop_verified` and `decoded_pixels_equal=true`.
- Processed placeholder: `docs/assets/006_independence_wave/source_placeholder_2026_08_05_iberian/processed_png/portrait_GLC_alfonso_daniel_castelao.png`, `156x210` RGB, SHA-256 `80f77a25c4c30fae67aefab7619aae390983afa22d2685d27746eb3d96df90c6`.
- Runtime DDS: `gfx/leaders/006_independence_wave/portrait_GLC_alfonso_daniel_castelao.dds`, SHA-256 `33aa76c4bbcbb87e7f9ce1508beadee4799a558a429f92b4d5ac8fc09c4a4b7f`; temporary copy is `final_dds/portrait_GLC_alfonso_daniel_castelao.dds`.
- DDS validation passes `DDS ` magic, 124-byte header, `156x210`, exact `131168` bytes, 32-bit BGRA masks, flags `65`, `DDSCAPS_TEXTURE`, no mipmaps, alpha `255..255`, runtime-copy hash equality, and decoded-pixel equality to the processed PNG; validation JSON is `review/portrait_GLC_alfonso_daniel_castelao_dds_validation.json`.
- Decoded DDS RGBA SHA-256 is `f4c5240dec022af29b5753606615589abd81e12e8aaa64850095569ca4949001`; review PNG is `review/decoded_dds/portrait_GLC_alfonso_daniel_castelao.png`.

## Review and wiring

- Canonical leader reference family and contact sheet were inspected before processing; comparison sheets include the unchanged master, exact crop, processed PNG, DDS round-trip, and `den_thorvald_stauning`, `ire_eamon_de_valera`, and `fin_carl_mannerheim` leader references.
- Native and 4x nearest-neighbour review confirms source identity, source-visible facial geometry, and crop/DDS equality; the raw monochrome source look is intentional because these outputs are placeholders.
- No independent reviewer was assigned in this bounded production, so no final likeness/style/provenance PASS is claimed.
- Bóveda remains an archived source-only alternate under `docs/assets/portraits/006_independence_wave/portrait_GLC_alexandre_boveda_source.jpg` and `portrait_GLC_alexandre_boveda.png`; no Bóveda DDS or GFX sprite was created.
- No mod character references exist for the proposed Aguirre/Castelao keys, and vanilla GLC Castelao ownership was not modified; parent gameplay scope must select or wire any consumer without changing the stable sprite names.

## Skipped checks, blockers, and replacement state

- RunPod/provider operation, final 832x1120 masters, final HOI4-style repaint, independent identity/style/provenance audit, character roster, country setup, flags, advisor icons, package attestation, and live in-game validation were skipped by scope.
- `source_placeholder` and `replacement_pending` remain the honest states for both runtime textures.
- Aguirre licensing discrepancy and Castelao unknown-author scan chain remain `needs_user_review` blockers for any final distribution or admission claim.
- No gameplay, tag, flag, localisation, decision, focus, AI, or attestation files were edited.
