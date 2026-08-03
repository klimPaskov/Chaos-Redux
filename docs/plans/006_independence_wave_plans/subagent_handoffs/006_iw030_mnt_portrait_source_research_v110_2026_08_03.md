# IW-030 Montenegro grounded male portrait source research handoff v110

Date: 2026-08-03.

Subagent: `/root/event6_iw030_mnt_portrait_source_research`.

Scope: source-only research for the existing all-male MNT roster, including archival source masters, exact head-and-shoulders crops, decoded-pixel equality metadata, deterministic `156x210` source-placeholder evidence, provenance, licence, era-fit, and identity notes.

No gameplay, character, history, localisation, `.gfx`, DDS, advisor, attestation, flag, or runtime file was edited.

The obsolete pasted flag log was excluded.

## Verdict

`SAFE_PACKAGE_PROMOTION = NO`.

The source/licence chain for Krsto Zrnov Popović is materially stronger than the previous blocked note: Commons records Serb Land of Montenegro (`njegos.org`) as the source, retains VRTS permission ticket `2010091210005142`, and exposes CC BY-SA 3.0 after GFDL migration. The image still has no recorded capture date or original photographer, so it remains `needs_user_review` and is not a silent generic replacement.

Blažo Jovanović now has archive-level Znaci evidence that records `1942-05-25`, the Museum of the Revolution of the Peoples of Yugoslavia as source, and an explicit public-domain statement for its archival materials. The Commons/Znaci record credits Savo Orović while the original photographer is unknown, so rights remain `needs_user_review` despite the stronger source record.

Blažo Đukanović remains `needs_user_review`: the 1938–1940 Commons portrait is explicitly identified and credited to Mile S. Bjelajac's 2004 military-biography volume and marked `PD-old`, but the photographer and first-publication rights chain are unknown.

Mitar Martinović remains a distinct role-correct replacement candidate, not a relabel of `MNT_kristo_popovic`. The 1912 archival source and exact crop are retained, while the v91 independent audit leaves human style approval and parent-owned identity/runtime admission open.

Therefore the full MNT roster is not cleared for runtime or content attestation.

## Evidence package

The complete source-only package is `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v110_2026_08_03/`.

It contains unchanged masters under `source_masters/`, exact source crops under `source_crops/`, equality JSON under `crop_metadata/`, evidence-only `156x210` PNGs plus processing JSON under `source_placeholders/`, source records under `research/`, a review contact sheet at `review/mnt_v110_source_placeholder_contact_sheet.png`, `manifest.md`, and `gfx_handoff.md`.

## Roster evidence and disposition

| Consumer | Source, identity, and 1936 role fit | Rights/date state | Disposition |
| --- | --- | --- | --- |
| `MNT_kristo_popovic` | Krsto Zrnov Popović (1881–1947), Montenegrin Army officer and Green separatist leader; alive at the 1936 start at age 55. Source master is `source_masters/mnt_krsto_popovic_commons_njegos_vrt.jpg` (791×1182 grayscale, SHA-256 `15ba6d47fc7a2f2d14bfff953d0b9615167e78e7c5f7e6a0666c3fe84c44c363`, Commons SHA-1 `400ed7e1bcbcaf7d581821feb6994e3fe274627a`) from [Commons](https://commons.wikimedia.org/wiki/File:Krsto_Zrnov_Popovic.jpg), canonical original `https://upload.wikimedia.org/wikipedia/commons/2/25/Krsto_Zrnov_Popovic.jpg`. | `njegos.org` source template plus VRTS ticket `2010091210005142` and CC BY-SA 3.0 are recorded; capture date, original photographer, and archive accession are not. | `needs_user_review`; source-only crop and placeholder exist, but no runtime promotion. |
| `MNT_blazo_jovanovic` | Blažo Jovanović (1907–1976), Montenegrin partisan leader and corps-commander consumer; source is a 1942 wartime image later than the scenario start but within his active adult life. Master SHA-256 `919393b924cee9c6de3d1e1fd4e864b4ffed387a3fe60fd52c43bc58b6d682a4`; source record [Znaci 8889](https://znaci.org/fotografija.php?br=8889) and canonical original `https://upload.wikimedia.org/wikipedia/commons/3/38/Grupa_boraca_i_rukovodilaca_iz_Crne_Gore%2C_Lipova_Ravan%2C_25._maja_1942.jpg`. | Znaci states `Muzej revolucije naroda Jugoslavije` and “all photographs, documents and other archival materials are public domain unless otherwise noted”; the record credits Savo Orović while the original photographer remains unknown. | `needs_user_review`; prior visual/source-linkage pass stands, but rights are not silently promoted. |
| `MNT_blazo_dukanovic` | Blažo Đukanović (1883–1943), Yugoslav military officer/general and fascist-route country-leader/corps-commander consumer; source estimated 1938–1940 and close to the scenario era. Master SHA-256 `b099dff0ad5b45d8dd33a10c9a0ccc113d4e08afa8ca1fa7c2d5fe68b76a8be8`; [Commons file](https://commons.wikimedia.org/wiki/File:Bla%C5%BEo_%C4%90ukanovi%C4%87.jpg), canonical original `https://upload.wikimedia.org/wikipedia/commons/7/77/Bla%C5%BEo_%C4%90ukanovi%C4%87.jpg`. | Commons credits Mile S. Bjelajac, *Generali i admirali Kraljevine Jugoslavije: 1918–1941* (2004), and asserts `PD-old`; photographer and first-publication chain remain unknown. | `needs_user_review`; no rights clearance or runtime promotion. |
| Proposed distinct identity `MNT_mitar_martinovic` | Mitar Martinović (1870–1954), Montenegrin divisional general, former prime minister and minister of war, and Lovćen Detachment commander; alive at the 1936 start at age 65. Master SHA-256 `202d349544bb4b36ee696120222c1ccfdb25e1a8c7213e65eef9ce910d185a76`; the 1912 *Ilustrovana ratna kronika* source and [source package v87](../../../assets/006_independence_wave/iw030_mnt_portrait_source_research_v87_2026_08_01/manifest.md) retain the `PD-collective-work|Serbia` basis with site-terms caveat. | v91 independent audit passes identity/source linkage and leaves style and parent ownership/runtime at `needs_user_review`. | Use only as a new stable identity after parent approval; never assign the face to Popović, Jovanović, or Đukanović. |

## Crop and placeholder evidence

The exact source crops were produced with `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py` v1.0 and report `decoded_pixels_equal=true` in RGBA mode.

| Subject | Crop path | Crop SHA-256 | Crop box |
| --- | --- | --- | --- |
| Popović | `source_crops/mnt_krsto_popovic_head_shoulders.png` | `0a4308b6fe2cf659d86011d5881d7e0bfb2ca8b7632555510e3e8820e2a58fb4` | `[120,40,675,785]` (555×745) |
| Jovanović | `source_crops/mnt_blazo_jovanovic_znaci_8889_lipova_ravan_1942_head_shoulders.png` | `e96c730d6d82702ea2937c1ff3bfa46b9d998921784aae2bf5be435a336cd737` | `[1040,500,1490,1200]` (450×700) |
| Đukanović | `source_crops/mnt_blazo_dukanovic_1938_1940_head_shoulders.png` | `b626fe6089e3483f89a7fc0d553b69b16fa52ce8116b696d2f6e3362ec318cd9` | `[30,20,420,475]` (390×455) |
| Martinović | `source_crops/mnt_mitar_martinovic_1912_head_shoulders.png` | `493846b7202b528ce81260a0227d5c4880575f97cc0cb45715b116390e37de2e` | `[80,90,610,760]` (530×670) |

Deterministic source-placeholder previews were made with Pillow cover crops and LANCZOS resize only, without repaint, recolour, retouch, padding, or DDS conversion. Their output SHA-256 values are Popović `aed6ca774105ad280fee84aa18da48ef3486c07eb2de13155c43fb494c50414a`, Jovanović `48c08ef6da21587c2eb704b4747cf8d272b247a8757737ed1e7c29f5d5c91986`, Đukanović `d65a38e9f9672eaf307d3c4b82a1ea5fcf66f46c9a9d2fd494c9ec5e67c85536`, and Martinović `e9798a7d5db6acf1761571cbcde0341ef40762feebd45a159790cb360fc9a45b`.

## Parent next gates

1. Keep Popović at `needs_user_review` until the parent decides whether the CC BY-SA/VRTS chain and unknown date/photographer satisfy the grounded source gate.
2. Decide whether the Znaci public-domain declaration plus creator discrepancy is sufficient for Jovanović rights admission.
3. Resolve the unknown-photographer/book chain for Đukanović.
4. Obtain human style approval and explicit parent-owned identity/runtime admission for `MNT_mitar_martinovic` if the role-correct amendment is accepted.
5. Only after all live consumers have separate identity, source, rights, visual-audit, and ownership passes may the parent convert an approved PNG with the repository DDS converter and wire the existing sprite contracts.

No fallback, generic acceptance, relabel, invented officeholder, advisor asset, flag edit, gameplay patch, or attestation promotion was made.
