# IW-053 Altai opening portrait provenance recovery handoff

Date: 2026-08-15.

## Disposition

Both vanilla ALT opening portrait identities remain **blocked** for runtime replacement. The research package preserves attributed source evidence for `ALT_grigory_gurkin` and `ALT_samuil_yufit`, but neither candidate has a rights-cleared source and neither proves the exact vanilla 1936 opening country-leader role/date. No generic, generated, repainted, or substitute likeness was used.

This is a fail-closed source-recovery result, not a portrait approval. No DDS, `.gfx`, character, localisation, gameplay, central-admission, deterministic Join, RunPod, or ImageGen operation was performed.

## Exact installed-vanilla consumer evidence

The installed vanilla source root is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`; the repository reference shelf records the extracted build as Operation Postern v1.19.2.0.a729 (d245).

Installed `common/characters/ALT.txt` defines `ALT_grigory_gurkin` as “Grigory Gurkin” with `civilian.large = GFX_portrait_Grigory_Gurkin`, a moderatism country-leader role expiring 1940-01-01, and `ALT_samuil_yufit` as “Samuil Yufit” with `civilian.large = GFX_portrait_Samuil_Yufit`, a stalinism country-leader role expiring 1944-01-01.

Installed `history/countries/ALT - Altai Republic.txt` starts the democratic Altai Republic with `last_election = "1936.1.1"` and recruits both characters at lines 103-104.

Installed `interface/_leader_portraits.gfx` currently maps `GFX_portrait_Grigory_Gurkin` to `gfx/leaders/Asia/Portrait_Asia_Generic_2.dds` and `GFX_portrait_Samuil_Yufit` to `gfx/leaders/Asia/Portrait_Asia_Generic_3.dds`.

The current generic vanilla textures are 156x210 DXT1 DDS files, not identity sources: `Portrait_Asia_Generic_2.dds` SHA-256 `75ea54febbfb76011e9827d0c30feb82bd4747bcb0c976c9bb3e1792ab1d360c`, and `Portrait_Asia_Generic_3.dds` SHA-256 `7931b57e900ca175b0fd1c297584f8f755ebbc887655ef5670f967157d6feb7d`. They remain untouched.

The matching role shelf was inspected at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/contact_sheet.png`; it contains eight lossless 156x210 leader references and is style evidence only, never a face source.

## Grigory Gurkin evidence

Subject identity: Grigory Ivanovich Gurkin, also Choros-Gurkin, 1870-01-24 to 1937-10-11, Altai painter, ethnographer, and public figure.

The archived source is `docs/assets/portraits/006_independence_wave/iw053_altai_grigory_gurkin_source_original_2026_08_15.jpg`, RGB 516x716, 203077 bytes, SHA-256 `94d9551ce6db7e4cc8f308fea719ab8aed19161b45dffd514ef53067b01a667a`.

The source file page is [Russian Wikipedia File:Григорий Иванович Гуркин.jpg](https://ru.wikipedia.org/wiki/%D0%A4%D0%B0%D0%B9%D0%BB:%D0%93%D1%80%D0%B8%D0%B3%D0%BE%D1%80%D0%B8%D0%B9_%D0%98%D0%B2%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D1%87_%D0%93%D1%83%D1%80%D0%BA%D0%B8%D0%BD.jpg), with original upload URL `https://upload.wikimedia.org/wikipedia/ru/f/f3/%D0%93%D1%80%D0%B8%D0%B3%D0%BE%D1%80%D0%B8%D0%B9_%D0%98%D0%B2%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D1%87_%D0%93%D1%83%D1%80%D0%BA%D0%B8%D0%BD.jpg`; the page credits `http://chtoby-pomnili.com/gallery/cache/350_154274994.jpg_max.jpg`, gives no creation date, and names no author or rightsholder.

The current Russian Wikipedia API image-info record confirms 516x716, upload timestamp 2014-10-03, `NonFree = true`, `Copyrighted = True`, and `LicenseShortName = Добросовестное использование`; this is non-free article fair use and is not a mod-runtime licence.

Identity is corroborated by the archived biography capture `docs/assets/portraits/006_independence_wave/processed/iw053_altai_grigory_gurkin_biography_page_capture.md` and the regional Living Heritage capture `docs/assets/portraits/006_independence_wave/processed/iw053_altai_grigory_gurkin_livingheritage_page_capture.md` from [livingheritage.ru](http://livingheritage.ru/brand/respublika-altaj/grigorij-choros-gurkin).

The Living Heritage account places Gurkin at the head of the Karakorum-Altai Okrug Administration in 1917-1919; it does not establish him as a 1936 Altai Republic country leader. He was alive on 1936-01-01, but the exact vanilla opening office/date gate fails.

The retained exact source crop is `docs/assets/portraits/006_independence_wave/processed/iw053_altai_grigory_gurkin_source_crop.png`, RGB 280x377, crop box `[88, 20, 368, 397]`, SHA-256 `c59cdef26af2f06b5e9cc71f336716d987676fbf11578dd9291dd89cb88563f`; `iw053_altai_grigory_gurkin_crop_evidence.json` records decoded RGBA equality with master-rectangle hash `759054ea734a6e49f61f3b4e9709d041bce46b2e29e1ccb08cc59eb3227b844b`. The 4x nearest review is `iw053_altai_grigory_gurkin_review_4x_nearest.png`, 1120x1508, SHA-256 `cdbc6aacd2e3db4281e1cbf673a339c6a27efe37e3d31740e2a449b9b286fc85`.

The source is therefore **identity PASS, source-attribution PASS, exact 1936 role/date FAIL, rights FAIL, runtime BLOCKED**. The existing provenance contract is `docs/assets/portraits/006_independence_wave/processed/iw053_altai_grigory_gurkin_provenance.txt`.

Commons category/search review found paintings, a monument, museum scenes, and other non-portrait material but no rights-cleared portrait alternative for Gurkin; no alternative was substituted.

## Samuil Yufit evidence

Subject identity: Samuil Naumovich Yufit, born 1902, Soviet party and state official.

The archived source is `docs/assets/portraits/006_independence_wave/iw053_altai_samuil_yufit_source_original_2026_08_15.jpg`, RGB 490x730, 338656 bytes, SHA-256 `d1a52fc861221c79bec30abd2c8e75171f7307468444a99b1de814cfe7dfcc39`.

The source file page is [Russian Wikipedia File:Самуил Наумович Юфит .jpg](https://ru.wikipedia.org/wiki/%D0%A4%D0%B0%D0%B9%D0%BB:%D0%A1%D0%B0%D0%BC%D1%83%D0%B8%D0%BB_%D0%9D%D0%B0%D1%83%D0%BC%D0%BE%D0%B2%D0%B8%D1%87_%D0%AE%D1%84%D0%B8%D1%82_.jpg), with original upload URL `https://upload.wikimedia.org/wikipedia/ru/8/86/%D0%A1%D0%B0%D0%BC%D1%83%D0%B8%D0%BB_%D0%9D%D0%B0%D1%83%D0%BC%D0%BE%D0%B2%D0%B8%D1%87_%D0%AE%D1%84%D0%B8%D1%82_.jpg`; the page credits `Алтайская правда, 09.12.1937`, gives no image-creation date, and names no author.

The current Russian Wikipedia API image-info record confirms 490x730, upload timestamp 2018-01-13, `NonFree = true`, `Copyrighted = True`, and `LicenseShortName = Добросовестное использование`; the newspaper credit and fair-use status do not clear mod-runtime redistribution.

The archived biography capture `docs/assets/portraits/006_independence_wave/processed/iw053_altai_samuil_yufit_biography_page_capture.md` places Yufit as first secretary of the Moshkovsky district committee in 1935-1937, acting Oirot regional first secretary from 1937-03-28 to 1937-05-17, and Oirot regional first secretary from 1937-05-22 to 1938-02-12. The source credit is dated 1937-12-09, after the 1936 opening, and the biography does not establish the vanilla 1936 Oirot country-leader office.

The retained exact source crop is `docs/assets/portraits/006_independence_wave/processed/iw053_altai_samuil_yufit_source_crop.png`, RGB 490x659, crop box `[0, 0, 490, 659]`, SHA-256 `8d6e0939db8dc2ff4f6d5b9bdde6e299077627603cc44c97083be0c7795e49c`; `iw053_altai_samuil_yufit_crop_evidence.json` records decoded RGBA equality with master-rectangle hash `f344bddfaeafdb911febc88e702f9145aa8a7ee2f9650866b8dd3de406551c20`. The 4x nearest review is `iw053_altai_samuil_yufit_review_4x_nearest.png`, 1960x2636, SHA-256 `2f242cd36f92f2b284ba4fe2678dd59f711097e9fd2e6c325eda71f74f7e923e`.

The source is therefore **identity PASS, source-attribution PASS, exact 1936 role/date FAIL, rights FAIL, runtime BLOCKED**. The existing provenance contract is `docs/assets/portraits/006_independence_wave/processed/iw053_altai_samuil_yufit_provenance.txt`.

Commons search returned no Samuil Yufit file, portrait, or rights-cleared alternative; no alternative was substituted.

## Archive and forbidden-output audit

The two untouched originals remain directly under `docs/assets/portraits/006_independence_wave/`.

All crop, equality JSON, page captures, provenance contracts, source reviews, and review previews remain directly under the existing `docs/assets/portraits/006_independence_wave/processed/` directory; no subject subfolders or archive relocation were introduced.

The IW-053 archive contains no retained 156x210 PNG or DDS. The only image dimensions for these two subjects are the originals (Gurkin 516x716; Yufit 490x730), exact source crops (280x377; 490x659), and 4x nearest review previews (1120x1508; 1960x2636). The crop-tool temporary 156x210 candidates were not retained.

## Required unblock conditions

1. Obtain a rights-cleared original or explicit redistribution permission for each portrait, with durable attribution and licence evidence.
2. Obtain a source dated on or before the 1936 opening, or an accepted design decision that changes the historical office/date requirement; do not infer either from the vanilla token alone.
3. Re-run independent identity, framing, provenance, and role/date review only after both gates are satisfied.
4. Keep the generic vanilla textures and all ALT character consumers unchanged until the parent explicitly accepts a complete source package.

No fallback portrait is authorized. RunPod remains a user-only action if a later explicit styled-final request is made; this research tranche never opened or operated it.

## Skipped checks and blockers

- DDS conversion and runtime dimension/header validation were skipped because the user explicitly scoped this tranche to provenance recovery and forbade DDS/GFX/character wiring.
- Portrait-specific `.gfx` and existing character references were not edited.
- ImageGen and RunPod were not used.
- Live HOI4 loading, MCP runtime portrait inspection, and in-game validation were skipped because no runtime surface changed.
- The durable blockers are unknown/uncleared image rights and the absence of exact 1936 opening role/date evidence for both vanilla consumers.
