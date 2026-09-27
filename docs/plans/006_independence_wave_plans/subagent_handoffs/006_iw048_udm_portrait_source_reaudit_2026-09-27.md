# IW-048 UDM portrait identity and source-rights re-audit

Date: 2026-09-27

Role: chaosx_portrait_creator

Status: blocked / fail-closed. This fresh pass found no candidate that clears both the requested identity/source standard and image-rights gate. Keep the package blocked and do not create or wire portrait assets.

## Disposition

The exact vanilla token is Boris Berman, and a secondary biographical directory identifies Boris Zakharovich Berman as first secretary of the Udmurt regional party committee during all of 1936. That is a plausible identity match, but this pass could not retrieve an authoritative archive, library, museum, or government-history record directly documenting the identity and 1936 office. The accessible secondary sources also disagree on the exact appointment and departure days.

The only exact portrait located is explicitly marked fair-use/non-free and copyrighted, with an unspecified photographer and no permission statement. No authentic image of a specifically identified 1936 Udmurt institution with image-level reuse rights was found. Identity/role verification therefore remains unclosed to the requested standard, and rights fail independently.

Do not substitute Boris Davidovich Berman, another Boris, a generic Udmurt face, an illustration, generated art, a modern government-building photo, or the installed vanilla generic texture. Do not reinterpret the package's alternate-history workshop congress or local councils as an authentic historical institution.

## Reviewed scope and references

- Read the Udmurtia package record, all three named 2026-08-14/15 portrait handoffs, the Part 5 leadership and Volga context, AGENTS.md, the asset skill, and its portrait-production reference.
- The reviewed design requires a sourced real male period leader valid for the release date or authentic image evidence for the actual institution, with image-level rights verification.
- The package remains package-local and fail-closed. Its parent-owned independence_wave_iw_048_identity_rights_cleared gate has no local setter.
- The local portrait archive contains no path matching IW-048, UDM, or Berman. The previous handoff's referenced file docs/assets/portraits/006_independence_wave/processed/iw048_udm_boris_berman_blocked_2026_08_14.md is absent in the current checkout.

## Installed vanilla identity consumer and portrait references

- Vanilla common/characters/UDM.txt:2-12 defines UDM_boris, display name Boris Berman, country-leader role, and GFX_portrait_Boris_Berman.
- Vanilla history/countries/UDM - Udmurtia.txt:1 and :101 sets capital 399 (Izhevsk) and recruits UDM_boris.
- Vanilla interface/_leader_portraits.gfx:7087-7088 points GFX_portrait_Boris_Berman at gfx/leaders/Europe/Portrait_Europe_Generic_1.dds.
- The generic DDS is 156x210, 87,368 bytes, SHA-256 E9EBF8DE1AF84CA29E65B572964B4EBF4FBA8B4E33CC2CE615CDEFF41CFBFE26. At least twelve sprite blocks in the installed leader GFX reference this texture, so it is not identity evidence.
- Inspected the canonical leader contact sheet and CATALOG.md before any backdrop consideration. The sheet contains eight 156x210 vanilla leader examples and has SHA-256 8966AE351D1FE8FC13D47CA1C59EC3D8A34DA9101CE5FD65F7ACFF3421BD0401. It is framing/style guidance only and contains no Boris source.
- The portrait_backdrops reference family was not consulted or used; no accepted source reached composition review, and that family cannot establish identity or substitute for a portrait.

## Identity and 1936 role research

The exact-token search led to Boris Zakharovich Berman, born in Chita in 1897, rather than Boris Davidovich Berman, the NKVD officer.

The [KnowBySight biographical directory entry](http://www.knowbysight.info/BBB/07869.asp) lists Boris Zakharovich Berman as first secretary of the Udmurt autonomous oblast / Udmurt regional committee from 20 December 1934 to 10 June 1937, which covers the entire 1936 release date. It cites the resolution of the XVI Udmurt regional party conference of 10–19 June 1937 and lists rusarchives.ru and memo.ru among its sources. This is a secondary directory, not the cited archival resolution.

The Russian Wikipedia article [Berman, Boris Zakharovich](https://ru.wikipedia.org/wiki/Берман,_Борис_Захарович) identifies the same office and links to the KnowBySight entry and an article by A. V. Sushkov. The cited [Alexanderyakovlev archive biography](http://www.alexanderyakovlev.org/almanah/inside/almanah-doc/person/1007325) returned HTTP 521 during this pass. The Sushkov PDF linked from that article returned HTTP 404 at its cited address: http://www.cdooso.ru/phocadownload/userupload/editions/a-v-sushkov-10-mesyacev-abrama-stolyara.pdf.

Search results for the derivative Ruwiki biography gave a different interval, 28 December 1934 to 10 July 1937. Both intervals include 1936, but the disagreement reinforces that the exact dates were not resolved from a retrieved primary record.

Exact search terms and routes checked included “Борис Захарович Берман Удмуртия 1934 1937 первый секретарь источник,” “Б.З. Берман Удмуртский обком 1936,” “site:gasur.ru Берман Удмуртского обкома,” “site:gasur.ru Борис Захарович Берман,” “site:udmurtia.ru Борис Захарович Берман,” “site:db.gasur.ru Берман Удмуртский обком,” “site:rusarchives.ru Берман Удмурт,” and “site:izh.ru Берман Удмуртский обком.” The official-domain searches returned no exact indexed record.

The Udmurt Archive Service electronic archive endpoint at http://gasur.ru/databases/eaur.php timed out. A search-index result for the archive photo-document announcement at http://www.gasur.ru/archives/gku-cdni/ob_foto.php did not identify a specific Udmurt leadership or institution image. No direct archival or government-history record was retrieved in this pass.

Identity finding: likely match, not cleared to the requested authoritative-source standard. The token's first and last name align with the secondary Udmurt-office record, but the token itself contains no patronymic or source attribution, and the cited primary evidence was not retrieved. No alternative leader is proposed; any different identity requires a separate accepted parent decision.

## Exact portrait candidate and rights review

The [Russian Wikipedia file record for Boris Berman](https://ru.wikipedia.org/wiki/Файл:Борис_Берман.jpg) describes the subject as Boris Zakharovich Berman and credits [Nekropole](https://nekropole.info/ru/Boris-Berman) as the image source. Its live image metadata reports 272x359 pixels, 55,281 bytes, SHA-1 e63c9660a6d13bad263d63fd2ab3c4602af44a9a, date “not later than 1938,” and author “not specified in the source.” The live metadata marks the image “Добросовестное использование” (fair use), Copyrighted=True, and has no permission statement.

The earlier 2026-08-15 handoff recorded SHA-256 9FA47A1288BDA065FBD33B749BCD378863767C92567430165C6AA4AA918E679F for the same 272x359 image. That SHA-256 was not recomputed here; the live metadata SHA-1 and dimensions were checked without downloading the image.

The [Sakharov Center record](http://www.sakharov-center.ru/asfcd/martirolog/?t=page&id=3603) and its image URL, http://www.sakharov-center.ru/asfcd/martirolog/photo/Auto/250399Y001733.jpg, were retained as source leads from the prior handoff. No image-specific license or rights-holder permission is stated in the reviewed records. Licensing on a text page does not license its photograph.

Wikimedia Commons searches for “Boris Zakharovich Berman” and “Борис Захарович Берман” returned the unrelated [Berman BD.jpg](https://commons.wikimedia.org/wiki/File:Berman_BD.jpg), whose Commons description identifies Boris Davidovich Berman. Its public-domain label does not make it usable for UDM_boris.

Rights finding: fail. The exact Berman image is non-free/copyrighted, its photographer is unspecified, and no redistribution license or explicit permission was found. It was not downloaded or archived.

## Actual-institution image branch

Checked “ЦИК Удмуртской АССР 1936 фото,” “Удмуртская АССР 1936 архивное фото ЦИК Совет народных комиссаров,” “Удмуртский обком фото архив 1936,” and “Удмуртская АССР 1936 фотографии архив Совет народных комиссаров лицензия.”

Wikimedia Commons file searches for “Удмуртская АССР 1936,” “Udmurt ASSR 1936,” and “Удмуртский обком” returned no relevant files. Broader “Удмуртия” and “Izhevsk 1936” results were modern buildings, later transport, maps, or unrelated material, not an authentic image of a documented 1936 Udmurt institution. Search results for the Central State Archive of Udmurtia describe a large photo-document collection, but no exact item or item-level license was located.

Institution finding: blocked. No specific historically documented provisional institution was identified in the accepted package records, and no image of an actual 1936 Udmurt institution with explicit reusable rights was found. The alternate-history workshop congress and local councils cannot be used as a historical institution identity without separate source-design acceptance.

## Asset lifecycle, wiring, and remaining gate

- Changed files: only this new research handoff.
- No source was accepted or archived. No original image, crop, crop-equality JSON, manifest, source-placeholder PNG, DDS, or runtime asset was created; therefore there are no output dimensions or output hashes.
- No crop/framing review, PNG processing, DDS conversion, portrait-specific GFX entry, character portrait reference, or gameplay wiring was performed.
- The portrait remains grounded_source_only and blocked, not source_placeholder, replacement_pending, or styled_final. There is no user-supplied styled final.
- RunPod was not opened or operated. Native ImageGen was not invoked. HOI4 was not launched.
- The package remains fail-closed, and independence_wave_iw_048_identity_rights_cleared still has no local setter. Keep UDM_boris on HOLD.
- Next clearance requires an authoritative record tying the exact Boris Zakharovich Berman to the Udmurt office in 1936 and a portrait with an explicit reusable license or rights-holder permission, or a separately accepted exact institution identity plus an authentic image with image-level rights.

## Research route notes

The default web-search connector stalled twice and the browser-state route timed out; public-source checks were completed through direct DuckDuckGo HTML search and the Wikimedia Commons and Russian Wikipedia APIs. The official Udmurt electronic-archive request also timed out, and the referenced archive biography and PDF routes returned HTTP 521 and 404 respectively.
