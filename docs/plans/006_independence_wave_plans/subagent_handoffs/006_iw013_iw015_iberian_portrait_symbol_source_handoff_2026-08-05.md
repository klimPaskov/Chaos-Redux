# Event 006 IW-013 NAV / IW-015 GLC sourced portrait and symbol handoff

Date: `2026-08-05`

Scope: source-only research for the grounded male leader and historical-symbol requirements of IW-013 Basque Country (`NAV`) and IW-015 Galicia (`GLC`). This handoff uses the current Event 006 registry, current installed-map binding, the 2026-08-03 Iberian source package, and the canonical leader/flag reference shelves. It does not edit gameplay, history, country, localisation, interface, or GFX files, and it creates no advisor icon, processed portrait, DDS, or runtime flag.

## Current contract

| Package | Tag | Current installed-map compact anchor | Optional extension | Source/identity implication |
| --- | --- | ---: | ---: | --- |
| IW-013 Basque Country | `NAV` | **792 País Vasco** | `172` Navarra and `806` French Basque Country | Preserve the current region-02 loader crosswalk. State `172` remains the baseline registry/reservation group (`RG-172`) and a possible extension, not the installed compact release anchor. |
| IW-015 Galicia | `GLC` | **171 Galicia** | none in the current binding | Keep the `RG-171` compact release anchor. |

The map evidence is `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` and the current Iberian package audit `subagent_handoffs/006_iw013_iw015_iberian_package_audit_2026-08-03.md`. No FORM-07, allocator, or map change is implied by this asset handoff.

The portrait role family is the vanilla country-leader `portraits/leaders/` family: final game texture `156x210`, not an advisor/dossier or `_small` card. The canonical style reference inspected was `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/contact_sheet.png`.

## Ownership gate

- Current project search of `common/characters`, `history/countries`, `gfx`, `interface`, `localisation`, and the Event 006 specs/plans found no `José Antonio Aguirre/Agirre`, `Alexandre Bóveda/Boveda`, or Castelao character consumer.
- Installed vanilla search found no Aguirre/Agirre or Bóveda/Boveda consumer. `GLC - Galicia.txt` already owns **Alfonso Daniel Castelao** as a vanilla country leader (`GFX_portrait_Alfonso_Daniel_Castelao`); reuse that owner rather than cloning Castelao into another country. No current NAV leader owns Aguirre.
- The current vanilla NAV roster remains Ramón Ormazábal Tife and Luis Urrengoetxea. The current vanilla GLC roster remains Fuco Gómez, Alfonso Daniel Castelao, Vicente Martínez Risco, and Santiago Casares Quiroga. This handoff does not remove, rename, or recruit any of them.

## Portrait source candidates

### IW-013 NAV — José Antonio Aguirre y Lecube

**Disposition:** `needs_user_review` source candidate; suitable for the parent-owned grounded portrait pipeline after rights and identity review. Aguirre (1904–1960) was a Basque nationalist politician and became the first Lehendakari of the Basque Government in October 1936, making him alive and role-valid for a 1936 release. The source is a contemporary 1933 rally photograph, two years before the opening date.

- Immutable source master: `docs/assets/006_independence_wave/iberian_portrait_source_research_2026_08_03/source_masters/NAV_jose_antonio_aguirre_1933.jpg`; JPEG `669x1024`, SHA-256 `1d34f7b23459f750dcbfcb8e300dc3d41f7087c4b24caf544d6ab2f8671e6bc9`.
- Source page: [Commons file page](https://commons.wikimedia.org/wiki/File:Jose_Antonio_Agirre,_Aberri_Eguna_1933.jpg); [direct original](https://upload.wikimedia.org/wikipedia/commons/2/2c/Jose_Antonio_Agirre%2C_Aberri_Eguna_1933.jpg). Commons identifies the date as 1933, the source archive as [Guregipuzkoa photo 1112433](http://www.guregipuzkoa.net/photo/1112433), and the photographer as Pascual Marín of the Marín Collection.
- Rights: the page body and category declare **CC BY-SA 3.0**; attribution, license link, and share-alike treatment are required. The page's generic machine-readable `rel=license` currently advertises CC BY-SA 4.0, so retain this discrepancy as a rights review item before promotion. Do not claim public-domain status.
- Exact immutable crop already verified by the repository tool: rectangle `left=268 top=235 right=500 bottom=510` (decoded master coordinates), output `232x275`, source crop `docs/assets/006_independence_wave/iberian_portrait_source_research_2026_08_03/source_crops/NAV_jose_antonio_aguirre_head_shoulders.png`, SHA-256 `960948067a1478798f82da673099fff1d34bf9ca23b29bfa7fc8490ebf80f366`; equality metadata `crop_metadata/NAV_jose_antonio_aguirre_head_shoulders.json`, SHA-256 `bca461f4d6502927efa35e9792e9bd39846cd642bb88a624f8dae483b5f7e49f`.
- If the crop must be regenerated, use exactly:

  ```powershell
  python -B .agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py `
    docs/assets/006_independence_wave/iberian_portrait_source_research_2026_08_03/source_masters/NAV_jose_antonio_aguirre_1933.jpg `
    docs/assets/006_independence_wave/iberian_portrait_source_research_2026_08_03/source_crops/NAV_jose_antonio_aguirre_head_shoulders.png `
    --crop 268 235 500 510 `
    --metadata docs/assets/006_independence_wave/iberian_portrait_source_research_2026_08_03/crop_metadata/NAV_jose_antonio_aguirre_head_shoulders.json
  ```

- Visual note: the source shows Aguirre clean-shaven, dark-haired, in a dark suit with white shirt and tie, speaking with both hands raised at a public rally. Preserve the source-visible facial geometry, expression, hairline, suit, and pose; do not use the crowd, podium, or Basque banner as identity pixels.
- Proposed stable runtime basename: `portrait_NAV_jose_antonio_aguirre`; proposed sprite: `GFX_portrait_NAV_jose_antonio_aguirre`; proposed runtime path (not created): `gfx/leaders/006_independence_wave/portrait_NAV_jose_antonio_aguirre.dds`.
- Provider handoff: country-leader family, one `832x1120` master plus one `156x210` game output through the locked RunPod/`chaosx_portrait_creator` route. No source-only DDS or styled output exists.
- Person-only prompt for the portrait job:

  ```text
  hoi4_portrait, a young Basque nationalist civilian leader in 1930s Spain, approximately thirty years old, clean-shaven with dark hair combed back, an angular oval face, narrow straight nose, alert deep-set eyes, and an intent speaking expression, wearing a dark double-breasted suit, white shirt, and tie, head and shoulders only, subdued period photographic-paint treatment, neutral warm-gray HOI4 leader background, no text, no crowd, no podium, no flag, no watermark.
  ```

### IW-015 GLC — Alfonso Daniel Rodríguez Castelao

**Disposition:** `needs_user_review` source candidate, with the strongest identity fit for the existing vanilla GLC Castelao leader. Castelao (1886–1950) was a Galician politician, writer, painter, physician, and founder/president of the Galicianist Party; he was a Galicianist deputy in 1936 and remains alive throughout the opening period.

- Immutable source master: `docs/assets/006_independence_wave/iberian_portrait_source_research_2026_08_03/source_masters/GLC_castelao_vida_gallega_442.png`; PNG `620x634`, SHA-256 `e022556b94a983f590dc2accde2dc6d6261fbe19369f688e4cca2f0adcdaa242`.
- Source page: [Commons file page](https://commons.wikimedia.org/wiki/File:Castelao_Vida_Gallega_442.png); [direct original](https://upload.wikimedia.org/wikipedia/commons/9/91/Castelao_Vida_Gallega_442.png). Commons identifies the source as *Vida gallega*, issue 442 (10 March 1930), Galiciana/Biblioteca Dixital de Galiza, with an unknown original author.
- Rights: Commons marks the scan **Public domain / CC-PD-Mark** and categorises it as an author-dead-more-than-80-years image. Because the original author and exact publication date are recorded as unknown on the file page, retain the unknown-author caveat and obtain an independent rights check before a styled replacement is promoted. The source is a period publication scan, not a modern actor or generated likeness.
- Exact immutable crop already verified: rectangle `left=88 top=8 right=552 bottom=630`, output `464x622`, source crop `docs/assets/006_independence_wave/iberian_portrait_source_research_2026_08_03/source_crops/GLC_castelao_castelao_vida_gallega_head_shoulders.png`, SHA-256 `1fb10ebf8c7f5d9e97f81d1ed93a7442cbf9f83561e911a1c65a09f68b8ff232`; equality metadata `crop_metadata/GLC_castelao_castelao_vida_gallega_head_shoulders.json`, SHA-256 `f960ab95689d6193ea92ce138e53d703b424b81a0354e8af449ec9b552534582`.
- If the crop must be regenerated, use the same utility with `--crop 88 8 552 630` and the existing master/output/metadata paths above. Do not resize, enhance, recolour, or retouch the immutable crop.
- Visual note: the scan shows Castelao with dark swept hair, round glasses, a long oval face, clean-shaven jaw, and dark jacket, shirt, and tie. Preserve the halftone facial geometry and glasses; the scan's paper texture is not a runtime background.
- Proposed stable runtime basename: `portrait_GLC_alfonso_daniel_castelao`; proposed sprite: `GFX_portrait_GLC_alfonso_daniel_castelao`; proposed runtime path (not created): `gfx/leaders/006_independence_wave/portrait_GLC_alfonso_daniel_castelao.dds`.
- Provider handoff: reuse the existing vanilla GLC Castelao owner and route the source crop through the country-leader `156x210` pipeline. Do not create a duplicate Castelao character or an advisor/dossier card.
- Person-only prompt for the portrait job:

  ```text
  hoi4_portrait, a middle-aged Galician nationalist politician, writer, painter, and physician of the early 1930s, approximately forty-four years old, dark thick hair brushed back, round wire-rim glasses, clean-shaven long oval face, steady thoughtful eyes, straight nose, restrained mouth, wearing a dark jacket with a white shirt and tie, head and shoulders only, subdued period photographic-paint treatment, neutral warm-gray HOI4 leader background, no text, no newspaper lettering, no watermark.
  ```

### IW-015 GLC — Alexandre Bóveda Iglesias (conditional alternate)

**Disposition:** `needs_user_review`, secondary/route candidate only. Bóveda (1903–1936) was a Galician nationalist politician and financial officer, a key organiser of the Partido Galeguista and the 1936 autonomy project. He was executed on 17 August 1936, so he is valid only for a release/route before that date; he must not be presented as a living leader after his death without a separate memorial or institutional design.

- Immutable source master: `docs/assets/006_independence_wave/iberian_portrait_source_research_2026_08_03/source_masters/GLC_alexandre_boveda_1933.jpg`; JPEG `583x758`, SHA-256 `229ad908ca33625cd66fe5b73efe01a1c907ccf0895f33e99ba0fdbc329a6b05`.
- Source page: [Commons file page](https://commons.wikimedia.org/wiki/File:Alexandre_B%C3%B3veda_1933.jpg); [direct original](https://upload.wikimedia.org/wikipedia/commons/9/96/Alexandre_B%C3%B3veda_1933.jpg). Commons records a 1933 *Vida Gallega* image (20 March 1933, p. 38), sourced through Galiciana, and marks it Public domain / `PD-scan (PD-old-80)` / `CC-PD-Mark`.
- Exact immutable crop already verified: rectangle `left=55 top=25 right=530 bottom=730`, output `475x705`, source crop `docs/assets/006_independence_wave/iberian_portrait_source_research_2026_08_03/source_crops/GLC_alexandre_boveda_head_shoulders.png`, SHA-256 `0a46be15a7492f24a08fb0cfc4fc8a5cb0c7c33aac5ecc54ad5fa221520e122b`; equality metadata `crop_metadata/GLC_alexandre_boveda_head_shoulders.json`, SHA-256 `47b9949c513b3f7a07ed394f9f86500bc98dce0b4e2aca23329120fe892e1ce9`.
- Visual note: the period portrait shows a young clean-shaven man with dark hair, high forehead, long narrow face, dark suit, white collar, and direct gaze. Keep the source as an alternate identity candidate; do not infer a military uniform or later martyr iconography.
- Proposed stable runtime basename: `portrait_GLC_alexandre_boveda`; proposed sprite: `GFX_portrait_GLC_alexandre_boveda`; proposed runtime path (not created): `gfx/leaders/006_independence_wave/portrait_GLC_alexandre_boveda.dds`.
- Person-only prompt for the portrait job:

  ```text
  hoi4_portrait, a young Galician nationalist political organiser and financial officer in 1930s Spain, approximately thirty years old, dark hair neatly combed back, high forehead, long narrow face, clean-shaven jaw, direct serious eyes, straight nose, wearing a dark suit with a white collar and tie, head and shoulders only, subdued period photographic-paint treatment, neutral warm-gray HOI4 leader background, no text, no newspaper lettering, no watermark.
  ```

The retained `source_masters/GLC_castelao_oviedo_1933_group.jpg` (747x470, SHA-256 `b6e15437c80a9152901c4c2f70ad320a5b9b19496d4f1de80d9459c3d8a4f12a`) is context-only group evidence; its face footprint is too small for an immutable one-person portrait crop and it is not a portrait handoff.

## Historical flags and symbols

Final Event 006 flags still require the separate ImageGen flat-flag workflow. The following are sourced design references, not final runtime flags.

### IW-013 NAV — Ikurriña / Basque flag

- Reference master: `docs/assets/006_independence_wave/iberian_portrait_source_research_2026_08_03/source_masters/flag_basque_country_reference.svg`, nominal `1000x560`, SHA-256 `f282e4ea7981c707c5db8a10094e5cd3094c3e9689b384d6882cdda89c91b255`.
- Source: [Commons file page](https://commons.wikimedia.org/wiki/File:Flag_of_the_Basque_Country.svg); [direct SVG](https://upload.wikimedia.org/wikipedia/commons/2/2d/Flag_of_the_Basque_Country.svg). The page identifies author Daniele Schirmo (Frankie688), own-work vector dated 28 December 2006, licensed CC BY-SA 2.5 Generic.
- Historical geometry: red field; white upright cross reaching the edges; green diagonal saltire reaching the corners. The design is by Sabino and Luis Arana; the Basque Government adopted the Ikurriña for the Basque Autonomous Region on 19 October 1936. The modern Commons SVG is a clean geometry reference, not a surviving 1936 flag photograph.
- ImageGen constraint: reproduce only the documented flat geometry and colours; no fabric, folds, pole, shadows, gradients, or invented lettering. Preserve CC BY-SA attribution in the source record if the SVG is used as an input reference. Status: `needs_user_review` pending parent ImageGen output and historical-era review.

### IW-015 GLC — Galician flag and coat of arms

- Reference master: `docs/assets/006_independence_wave/iberian_portrait_source_research_2026_08_03/source_masters/flag_galicia_reference.svg`, nominal `600x400`, SHA-256 `fbdaf8a27bd279ba167a8956ce94bccee4a06257bfa4bafedf2d1560c8ec8db5`.
- Source: [Commons file page](https://commons.wikimedia.org/wiki/File:Flag_of_Galicia.svg); [direct SVG](https://upload.wikimedia.org/wikipedia/commons/6/64/Flag_of_Galicia.svg). Commons identifies Pedro A. Gracia Fajardo as author of an own-work Inkscape/Sodipodi vector and marks the file Public domain in the United States (PD-US).
- Geometry: white field with a blue diagonal band from the upper hoist toward the lower fly and a detailed crowned Galician coat of arms centred on the band. The official current legal references are [Xunta “A bandeira”](https://www.xunta.gal/a-bandeira) and [Xunta “O escudo”](https://www.xunta.gal/o-escudo).
- Era caveat: the Commons vector and Xunta pages document the modern legal form, not an uncontested 1936 government flag. Contemporary Galicianist usage included alternate stars and heraldic proposals; do not present a later route or party variant as the neutral compact baseline without an explicit design decision. Status: `needs_user_review` pending parent ImageGen reconstruction and 1936-era symbol review.

## Parent/portrait-creator handoff

1. Keep all three source masters and exact crop JSON files unchanged. Before any provider run, copy the accepted crop under `docs/assets/portraits/006_independence_wave/` using the exact runtime basename (`portrait_NAV_jose_antonio_aguirre`, `portrait_GLC_alfonso_daniel_castelao`, or `portrait_GLC_alexandre_boveda`) and retain the matching person-only prompt TXT.
2. Run the locked RunPod portrait route for one `832x1120` master and one `156x210` leader output per accepted identity. The source researcher has not created a styled output or DDS; `chaosx_portrait_creator` owns supplied-output validation, independent likeness/framing/provenance review, and final conversion after approval.
3. Use the `portraits/leaders/` canonical family. Do not create advisor icons, army-small/dossier cards, commander textures, or a plain photographic runtime DDS.
4. Do not wire the proposed sprites or runtime paths until the parent decides which grounded identity replaces or supplements the existing vanilla roster and resolves rights/era review.

## Blockers and uncertainty

- NAV Aguirre is a strong role/date/identity candidate, but the Commons page has a CC BY-SA 3.0 body declaration versus a generic CC BY-SA 4.0 machine-readable link. Preserve attribution and obtain rights confirmation before promotion.
- GLC Castelao is the best match for the existing vanilla GLC owner, but the source scan records an unknown original author/date despite a Commons public-domain mark. Require independent rights review and treat the image as an archival scan, not an illustration or generated likeness.
- GLC Bóveda has the clearest public-domain scan record and exact crop, but his 17 August 1936 execution imposes a release-date gate and he is not a current vanilla GLC owner.
- Both flag references are modern vector reconstructions. They document geometry and heraldry only; parent ImageGen must produce new flat normal/medium/small flags and manually check historical-era fit. No final flag, portrait PNG, or DDS is promoted by this handoff.
- IW-013 remains bound to installed-map compact state 792 with optional 172/806 extensions; do not silently restore the obsolete baseline-only 172 contract while wiring assets. IW-015 remains compact state 171.
