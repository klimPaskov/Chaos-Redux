# IW-184 California/HBX civic convention chair source-clearance handoff

Source-clearance result: `PASS` for one grounded real-person candidate, William Dennison Stephens (William D. Stephens), with runtime promotion intentionally withheld.

## Candidate

William D. Stephens was California governor from 1917 to 1923 and a Los Angeles Chamber of Commerce director from 1902 to 1911. The California State Library records his death in Los Angeles on April 24, 1944, so he was alive and historically active in the 1936 setting. A former governor and chamber director is a defensible fictional constitutional-convention chair for the alternate-history HBX role, but this handoff does not claim he chaired a real 1936 convention.

The fictional working identity `HBX_independence_wave_civic_convention_chair` / Daniel Mercer can be reviewed for replacement by `William D. Stephens`. No gameplay, character, localisation, or GFX file was changed.

## Source evidence

- Archive/object: [Library of Congress item 2014715011](https://www.loc.gov/pictures/item/2014715011/).
- Persistent handle: [hdl.loc.gov/loc.pnp/ggbain.34859](https://hdl.loc.gov/loc.pnp/ggbain.34859).
- Direct source used: [https://cdn.loc.gov/service/pnp/ggbain/34800/34859v.jpg](https://cdn.loc.gov/service/pnp/ggbain/34800/34859v.jpg).
- Secondary identity cross-check: [Wikimedia Commons file record](https://commons.wikimedia.org/wiki/File:William_D._Stephens_LCCN2014715011_(cropped).jpg) labels the subject "William D. Stephens, Governor of California" and maps back to LOC LCCN 2014715011; its derivative pixels are not used as the retained master.
- Retrieval date: 2026-07-24 (UTC).
- LOC catalog title: `Wm. D. Stephens`; creator/publisher: Bain News Service; date: `[between ca. 1920 and ca. 1925]`; medium: glass negative; reproduction `LC-DIG-ggbain-34859`.
- LOC rights advisory: `No known restrictions on publication`; retain the linked [Bain Collection rights guidance](https://www.loc.gov/rr/print/res/274_bain.html). This is not represented as a Creative Commons license.
- Identity/role: [California State Library Governors' Gallery, William Stephens](https://governors.library.ca.gov/24-Stephens.html), which records the 1917-1923 governorship, 1859 birth, 1944 death, U.S. Congressman and lieutenant-governor service, and Los Angeles Chamber of Commerce directorship.

## Retained files and hashes

| File | Purpose | SHA-256 |
| --- | --- | --- |
| `docs/assets/006_independence_wave_california_civic_source_clearance/source_png/william_stephens_loc_master.jpg` | Unchanged LOC-served archival master, `743x1024`, grayscale `L`, 111194 bytes | `5ba60d2fd0fab9a0dcf6a47b08a89bed486e35e5c14fc200c7fc6204b8652b5d` |
| `docs/assets/006_independence_wave_california_civic_source_clearance/crops/william_stephens_head_shoulders.png` | Explicit head-and-shoulders crop, `610x810`, lossless PNG, 274399 bytes | `d87f5fe6773844b597a4a1175dd26a6016a5a9df87a6295ce074f92d33ea2085` |
| `docs/assets/006_independence_wave_california_civic_source_clearance/crops/william_stephens_head_shoulders_crop.json` | Pillow crop/equality evidence | `4e7c4625a712eb55931902e004cfe316bedf0db96db437ad7c5da5c71c55f7b0` |
| `docs/assets/006_independence_wave_california_civic_source_clearance/manifest.md` | Source manifest, rights, role fit, ownership scan, risks, and runtime boundary | `5bc5f6ab3a5cf656752b14fce9fe44ab94bac8e4afd89fc1948f4ddd71203f7c` |
| `docs/assets/006_independence_wave_california_civic_source_clearance/gfx_handoff.md` | Source-only future sprite/path handoff; no runtime registration | `b0e5ff71e4cf862e2bf3572b40e532bc6487301aa74e17782b49625e2f977537` |

Exact crop command and box: `extract_portrait_source_crop.py`, `[75, 130, 685, 940]` half-open master coordinates. The JSON records `status=exact_source_crop_verified`, `decoded_pixels_equal=true`, RGBA master-rectangle hash `3d3d617eefff51f0fc629625a41a36c167d35f26c98239ccd81e3ee36a82f883`, identical reopened-crop hash, and Pillow `11.1.0`.

## Ownership scan

No exact or variant William D. Stephens identity match was found in current Chaos Redux, installed vanilla HOI4, or approved reference mods `1521695605`, `2265420196`, and `1458561226`. Searches covered `common/characters`, `history/countries`, `gfx/leaders`, `interface`, localisation, `.gfx` consumers, and filename variants including `William D. Stephens`, `William Dennison Stephens`, `William Stephens`, `Wm. D. Stephens`, `Stephens William`, `Governor Stephens`, `william_d_stephens`, and `william_stephens`.

Incidental filename matches such as `Donald_Stephens.dds`, `AST_percy_reginald_stephensen.png`, `AST_stephenson`, and `CAN_william_samuel_stephenson.png` are different people and do not resolve to this candidate. Hiram Johnson was not used because Kaiserreich/ACC owns `ACC_hiram_johnson` in `common/characters/ACC characters.txt:44`, `interface/kaiserreich/portraits/ACC_portraits.gfx:15`, and its ACC localisation entry.

## Main-agent next gate

This is a source package only. The parent must keep the source and crop immutable, inspect the country-leader canonical references, run source-locked identity-preserving ImageGen, produce the deterministic full `156x210` candidate, obtain an independent likeness/style/provenance PASS, and only then convert to DDS and wire a stable sprite or character token. No final DDS, `.gfx` snippet, or runtime path is claimed here.

Runtime status: `not_promoted` / `pending_full_portrait_pipeline`.

Risks remain that LOC's "No known restrictions on publication" is a repository advisory rather than a CC/PDM license, that the source is circa 1920-1925 rather than 1936, and that the constitutional-convention role is fictional alternate-history fit.
