# IW-053 Altai opening portraits: grounded source research handoff

Research date: 2026-08-15.

Disposition: `blocked` and fail-closed for runtime. Both real-person identities have defensible archival image candidates and exact source crops, but neither candidate is cleared for distribution and neither source proves the exact vanilla 1936 Altai country-leader role. No face was generated, no RunPod operation occurred, no DDS or GFX was installed, and no character, localisation, event, or gameplay file was changed.

## Installed-vanilla consumer audit

The installed vanilla files were inspected directly.

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/characters/ALT.txt:2-13` defines `ALT_grigory_gurkin` as a civilian country leader with `moderatism`, expiry `1940.1.1.1`, and consumer `GFX_portrait_Grigory_Gurkin`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/characters/ALT.txt:15-26` defines `ALT_samuil_yufit` as a civilian country leader with `stalinism`, expiry `1944.1.1.1`, and consumer `GFX_portrait_Samuil_Yufit`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/ALT - Altai Republic.txt:89-104` sets the 1936 political opening and recruits both characters.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/_leader_portraits.gfx:3064-3070` maps the two exact consumers to generic `gfx/leaders/Asia/Portrait_Asia_Generic_2.dds` and `Portrait_Asia_Generic_3.dds`; these generic textures were not reused as real-person evidence.

The vanilla role/date gate is therefore a country-leader opening on 1936-01-01, not a commander or advisor texture.

## Grigory Gurkin

Identity: Grigory Ivanovich Gurkin, also known as Choros-Gurkin, 1870-01-24 to 1937-10-11. The Russian Wikipedia biography and Living Heritage biography identify him as an Altai painter, ethnographer, educator, and public figure. Living Heritage records that he led the Karakorum-Altai Okrug administration during the 1917-1919 revolutionary period.

Source page: [Russian Wikipedia file page](https://ru.wikipedia.org/wiki/%D0%A4%D0%B0%D0%B9%D0%BB:%D0%93%D1%80%D0%B8%D0%B3%D0%BE%D1%80%D0%B8%D0%B9_%D0%98%D0%B2%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D1%87_%D0%93%D1%83%D1%80%D0%BA%D0%B8%D0%BD.jpg).

Direct original: [Wikimedia upload](https://upload.wikimedia.org/wikipedia/ru/f/f3/%D0%93%D1%80%D0%B8%D0%B3%D0%BE%D1%80%D0%B8%D0%B9_%D0%98%D0%B2%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D1%87_%D0%93%D1%83%D1%80%D0%BA%D0%B8%D0%BD.jpg), archived as [iw053_altai_grigory_gurkin_source_original_2026_08_15.jpg](../../../assets/portraits/006_independence_wave/iw053_altai_grigory_gurkin_source_original_2026_08_15.jpg). The original is 516x716 and SHA-256 `94d9551ce6db7e4cc8f308fea719ab8aed19161b45dffd514ef53067b01a667a`.

Source attribution and rights: the file page attributes the underlying image to `chtoby-pomnili.com/gallery/cache/350_154274994.jpg_max.jpg`, states that the author or rightsholder is unknown, and classifies the file as non-free fair-use material for the biography article. Rights verdict is `FAIL`; the image is not cleared for mod runtime distribution.

Crop and review: the handoff records an unchanged 280x377 lossless crop using half-open `[88, 20, 368, 397]`, SHA-256 `c59cdef26af2f06b5e9cc71f336716d987676fbf11578dd9291dd89cb88563f6`, and decoded RGBA equality hash `759054ea734a6e49f61f3b4e9709d041bce46b2e29e1ccb08cc59eb3227b844b`. The recorded 4x nearest review hash is `cdbc6aacd2e3db4281e1cbf673a339c6a27efe37e3d31740e2a449b9b286fc85`. Those processed PNGs are no longer present, so the original remains research evidence only and cannot be promoted.

Role/date/framing: identity is `PASS` and Gurkin was alive on the 1936 opening date, but the grounded sources do not document him as an Altai Republic country leader in 1936. His documented administrative leadership is 1917-1919. The crop is a reasonable head-and-upper-torso framing of an unchanged seated three-quarter archival photograph, but framing remains `REVIEW_ONLY` because the source is not rights-cleared and is not a final HOI4 portrait.

## Samuil Yufit

Identity: Samuil Naumovich Yufit, born 1902. The biography identifies him as first secretary of the Moshkovsky district committee in 1935-1937 and first secretary of the Oirot Autonomous Oblast regional committee from 1937-03-28 to 1938-02-12.

Source page: [Russian Wikipedia file page](https://ru.wikipedia.org/wiki/%D0%A4%D0%B0%D0%B9%D0%BB:%D0%A1%D0%B0%D0%BC%D1%83%D0%B8%D0%BB_%D0%9D%D0%B0%D1%83%D0%BC%D0%BE%D0%B2%D0%B8%D1%87_%D0%AE%D1%84%D0%B8%D1%82_.jpg).

Direct original: [Wikimedia upload](https://upload.wikimedia.org/wikipedia/ru/8/86/%D0%A1%D0%B0%D0%BC%D1%83%D0%B8%D0%BB_%D0%9D%D0%B0%D1%83%D0%BC%D0%BE%D0%B2%D0%B8%D1%87_%D0%AE%D1%84%D0%B8%D1%82_.jpg), archived as [iw053_altai_samuil_yufit_source_original_2026_08_15.jpg](../../../assets/portraits/006_independence_wave/iw053_altai_samuil_yufit_source_original_2026_08_15.jpg). The original is 490x730 and SHA-256 `d1a52fc861221c79bec30abd2c8e75171f7307468444a99b1de814cfe7dfcc39`.

Source attribution and rights: the file page identifies the source as `Алтайская правда, 09.12.1937` (Altayskaya Pravda, 1937-12-09), says the image creation time is not stated, says the author or rightsholder is unknown, and classifies the file as non-free fair-use material for the biography article. Rights verdict is `FAIL`; the image is not cleared for mod runtime distribution.

Crop and review: the handoff records an unchanged 490x659 lossless crop using half-open `[0, 0, 490, 659]`, SHA-256 `8d6e0939db8dc2ff4f6d5b9bdde6e299077627603cc44c97083be0c7795e49c9`, and decoded RGBA equality hash `f344bddfaeafdb911febc88e702f9145aa8a7ee2f9650866b8dd3de406551c20`. The recorded 4x nearest review hash is `2f242cd36f92f2b284ba4fe2678dd59f711097e9fd2e6c325eda71f74f7e923e`. Those processed PNGs are no longer present, so the original remains research evidence only and cannot be promoted.

Role/date/framing: identity is `PASS`, but exact 1936 Altai country-leader fit is `FAIL`. The source date is 1937-12-09, and the biography places Yufit in the Moshkovsky district role during 1935-1937 and in the Oirot regional role only from 1937-03-28. The crop is a readable single-subject head-and-shoulders newspaper portrait, but framing remains `REVIEW_ONLY` because the source is not rights-cleared and is not a final HOI4 portrait.

## Files and states

Originals are flat in `docs/assets/portraits/006_independence_wave/`:

- `iw053_altai_grigory_gurkin_source_original_2026_08_15.jpg`
- `iw053_altai_samuil_yufit_source_original_2026_08_15.jpg`

Crop, provenance, review, manifest, and captured source-page evidence are flat in `docs/assets/portraits/006_independence_wave/processed/`:

- `iw053_altai_grigory_gurkin_crop_evidence.json`, `iw053_altai_grigory_gurkin_provenance.txt`, `iw053_altai_grigory_gurkin_source_review.md`, and the Gurkin source-page captures.
- `iw053_altai_samuil_yufit_crop_evidence.json`, `iw053_altai_samuil_yufit_provenance.txt`, `iw053_altai_samuil_yufit_source_review.md`, and the Yufit source-page captures.
- `iw053_altai_portrait_source_research_manifest.md` summarizes both blocked gates.

The crop tool was `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py` version 2.0, SHA-256 `39cc567f820d60442b4d505724a3602eb387b0f727944f348fdf27cbe65d107a`. Temporary 156x210 files were used only for the tool invocation and were deleted; no 156x210 output remains in the archive or processed folder. No DDS, `.gfx`, runtime portrait path, character file, or gameplay file was touched.

## Parent decision gate

Do not promote either candidate to runtime. A future promotion requires rights clearance or a clearly licensed/public-domain replacement, plus evidence that the selected subject actually occupies the requested 1936 Altai country-leader role. Until then, retain this handoff and the flat evidence archive as the fail-closed record.
