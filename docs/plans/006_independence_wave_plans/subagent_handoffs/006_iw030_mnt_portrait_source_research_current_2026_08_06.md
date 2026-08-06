# IW-030 Montenegro three-consumer portrait source handoff

Date: 2026-08-06.

Subagent: `/root/iw030_mnt_portrait_research`.

Scope: source and crop evidence for the three native male Montenegro country-leader consumers `MNT_kristo_popovic`, `MNT_blazo_jovanovic`, and `MNT_blazo_dukanovic`. No gameplay, character, history, event, attestation, localisation, flag, advisor, `.gfx`, DDS, or runtime file was edited.

## Verdict

`SAFE_PACKAGE_PROMOTION = NO`.

All three consumers remain `needs_user_review`. The existing package is unchanged-source evidence mode: archival master, exact head-and-shoulders crop, deterministic `156x210` source placeholder, processing metadata, and provenance captures. There is no repaint, recolour, retouch, invented detail, female portrait, advisor icon, or fictional substitute. The user remains responsible for any grounded HOI4-style RunPod final; RunPod was not opened or operated.

## Source, role, and rights gates

| Consumer and role | Source evidence and current gate |
| --- | --- |
| `MNT_kristo_popovic` — Krsto Zrnov Popović (1881–1947), Montenegrin officer and Green leader; native country-leader consumer. | [Commons source](https://commons.wikimedia.org/wiki/File:Krsto_Zrnov_Popovic.jpg), original `https://upload.wikimedia.org/wikipedia/commons/2/25/Krsto_Zrnov_Popovic.jpg`; archived API/raw evidence `research/commons_popovic_imageinfo_2026_08_06.json` and `research/commons_popovic_raw_2026_08_06.txt`; role page capture `research/njegos_zrnov_2026_08_06.html`. Commons records `njegos.org` source, VRTS ticket `2010091210005142`, GFDL migration, and CC BY-SA 3.0, but no capture date, original photographer, or archive accession. Identity and male-role linkage are supported; rights/date/photographer/attribution-chain review remains open. |
| `MNT_blazo_jovanovic` — Blažo Jovanović (1907–1976), Montenegrin partisan leader/corps commander; native country-leader consumer. | Selected source [Znaci record 8889](https://znaci.org/fotografija.php?br=8889), dated `1942-05-25`, source `Muzej revolucije naroda Jugoslavije`; site terms state photographs/documents/archival materials are public domain unless otherwise noted. Commons corroboration [File:Blažo Jovanović.jpg](https://commons.wikimedia.org/wiki/File:Bla%C5%BEo_Jovanovi%C4%87.jpg) and archived API/raw evidence are `research/commons_jovanovic_imageinfo_2026_08_06.json` and `research/commons_jovanovic_raw_2026_08_06.txt`. Identity, male role, and date are supported; the original photographer remains unknown and the Savo Orović/unknown-photographer creator discrepancy is unresolved. |
| `MNT_blazo_dukanovic` — Blažo Đukanović (1883–1943), Yugoslav officer/general; fascist-route country-leader/corps-commander consumer. | [Commons source](https://commons.wikimedia.org/wiki/File:Bla%C5%BEo_%C4%90ukanovi%C4%87.jpg), original `https://upload.wikimedia.org/wikipedia/commons/7/77/Bla%C5%BEo_%C4%90ukanovi%C4%87.jpg`; archived API/raw evidence `research/commons_dukanovic_imageinfo_2026_08_06.json` and `research/commons_dukanovic_raw_2026_08_06.txt`. Commons dates the image between 1938 and 1940, credits Mile S. Bjelajac's 2004 *Generali i admirali Kraljevine Jugoslavije: 1918–1941*, and asserts `PD-old`, while listing an unknown author and no first-publication chain. Identity and male role are supported; the PD-old assertion is not treated as unconditional clearance. |

## Processing evidence

Package root: `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v110_2026_08_03/`. The single manifest was refreshed in that package at `manifest.md`; no nested portrait shelf was created. Crops were produced with `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py` v1.0 and record `decoded_pixels_equal=true`.

| Consumer | Master dimensions/SHA-256 | Exact crop dimensions/SHA-256 and box | `156x210` source placeholder SHA-256 |
| --- | --- | --- | --- |
| Popović | 791×1182, `15ba6d47fc7a2f2d14bfff953d0b9615167e78e7c5f7e6a0666c3fe84c44c363` | 555×745, `0a4308b6fe2cf659d86011d5881d7e0bfb2ca8b7632555510e3e8820e2a58fb4`, box `[120,40,675,785]` | `aed6ca774105ad280fee84aa18da48ef3486c07eb2de13155c43fb494c50414a` |
| Jovanović | 2083×1380, `919393b924cee9c6de3d1e1fd4e864b4ffed387a3fe60fd52c43bc58b6d682a4` | 450×700, `e96c730d6d82702ea2937c1ff3bfa46b9d998921784aae2bf5be435a336cd737`, box `[1040,500,1490,1200]` | `48c08ef6da21587c2eb704b4747cf8d272b247a8757737ed1e7c29f5d5c91986` |
| Đukanović | 443×599, `b099dff0ad5b45d8dd33a10c9a0ccc113d4e08afa8ca1fa7c2d5fe68b76a8be8` | 390×455, `b626fe6089e3483f89a7fc0d553b69b16fa52ce8116b696d2f6e3362ec318cd9`, box `[30,20,420,475]` | `d65a38e9f9672eaf307d3c4b82a1ea5fcf66f46c9a9d2fd494c9ec5e67c85536` |

Artifact paths are `source_masters/mnt_krsto_popovic_commons_njegos_vrt.jpg`, `source_crops/mnt_krsto_popovic_head_shoulders.png`, and `source_placeholders/portrait_MNT_popovic_source_placeholder_156x210.png` for Popović; `source_masters/mnt_blazo_jovanovic_znaci_8889_lipova_ravan_1942.jpg`, `source_crops/mnt_blazo_jovanovic_znaci_8889_lipova_ravan_1942_head_shoulders.png`, and `source_placeholders/portrait_MNT_jovanovic_source_placeholder_156x210.png` for Jovanović; and `source_masters/mnt_blazo_dukanovic_1938_1940.jpg`, `source_crops/mnt_blazo_dukanovic_1938_1940_head_shoulders.png`, and `source_placeholders/portrait_MNT_dukanovic_source_placeholder_156x210.png` for Đukanović. Matching crop and placeholder JSON files sit beside their respective artifacts.

The 4× visual review sheet is `review/mnt_v110_three_consumer_source_placeholder_4x.png` (`656x2800` RGB, SHA-256 `2a2d634e47f67304999e7bc432f0fd91b48bd8e4034a6608f5c868eb8b7449ce`); it shows unchanged source placeholders and no invented detail. PNG-to-DDS conversion and `.gfx`/runtime wiring were intentionally skipped because all three independent provenance/rights gates remain open. Existing vanilla contracts remain documented in `gfx_handoff.md` and were not changed.

## Files changed or added

- `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v110_2026_08_03/manifest.md` received the 2026-08-06 evidence-refresh section.
- New source evidence under the package `research/` folder: `commons_popovic_imageinfo_2026_08_06.json`, `commons_popovic_raw_2026_08_06.txt`, `commons_jovanovic_imageinfo_2026_08_06.json`, `commons_jovanovic_raw_2026_08_06.txt`, `commons_dukanovic_imageinfo_2026_08_06.json`, `commons_dukanovic_raw_2026_08_06.txt`, and `njegos_zrnov_2026_08_06.html`.
- New visual review sheet: `review/mnt_v110_three_consumer_source_placeholder_4x.png`.
- This handoff: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw030_mnt_portrait_source_research_current_2026_08_06.md`.
- Existing masters, crops, crop metadata, placeholders, `gfx_handoff.md`, and all runtime/gameplay files were not modified.

## Remaining parent gates

1. Obtain independent identity, framing, and provenance review for each source placeholder.
2. Decide whether Popović's CC BY-SA/VRTS chain and missing date/photographer satisfy the grounded-source gate.
3. Resolve Jovanović's unknown original photographer and Savo Orović/creator discrepancy.
4. Resolve Đukanović's unknown photographer and first-publication chain despite the Commons `PD-old` assertion.
5. Only after all three are admitted may the parent convert an approved PNG with `convert_to_dds.py` and wire the existing portrait contracts.

Skipped checks: runtime/in-game validation, final HOI4-style replacement review, parent rights admission, DDS conversion, and `.gfx` installation. No simplification was presented as complete; source-placeholder mode is explicitly pending review.
