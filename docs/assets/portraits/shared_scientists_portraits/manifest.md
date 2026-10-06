# Shared scientist portrait manifest

Updated 2026-10-06 for the `_scientists_portraits` GFX review tranche.

The installed portrait consumer uses the stable `GFX_portrait_*` sprites in `interface/_scientists_portraits.gfx`; no character definitions, sprite keys, or `.gfx` entries changed in this tranche.

## Runtime inventory

| Sprite | Runtime path | Dimensions | Runtime SHA-256 | Source state |
|---|---|---:|---|---|
| `GFX_portrait_GER_otto_ambros` | `gfx/leaders/scientists/portrait_GER_otto_ambros.dds` | 156×210 | `74c849c1da409c7724f25435d0a46710c417c691ef7cb98df7dcff7c5cfd298c` | Parent-approved authentic source placeholder; HOI4-style final pending user input. |
| `GFX_portrait_GER_perfect_aryan` | `gfx/leaders/scientists/portrait_GER_perfect_aryan.dds` | 156×210 | `2d2106356382023a252c1eb03a03f53f58dd41414d0c0ca7f84be82f0ab75e0c` | Fictional native ImageGen v2 final installed; parent-approved. |
| `GFX_portrait_POL_rudolf_weigl` | `gfx/leaders/scientists/portrait_POL_rudolf_weigl.dds` | 156×210 | `9787cd1f8d8967aa9871f7a8605bcb9eec6f0b90dd3071ba4f8b2cdceb8594f9` | Existing DDS unchanged; authentic study candidate failed pose gate and was not promoted. |
| `GFX_portrait_GER_sigmund_rascher` | `gfx/leaders/scientists/portrait_GER_sigmund_rascher.dds` | 156×210 | `b0554139d1f22e4af8d885e8e5533296163fffa3b599b43b8c3bd3c225fae0ae` | Existing DDS unchanged; no rights-cleared usable bust source found. |
| `GFX_portrait_FRA_charles_dufraisse` | `gfx/leaders/scientists/portrait_FRA_charles_dufraisse.dds` | 156×210 | `97c1ed43dad7541c61b25e20cc0238bbd3c56d0f01b6951f37585dfc889fb96f` | Existing DDS unchanged; available authentic sources fail pose or rights gates. |

## Otto Ambros source placeholder

Source: [Wikimedia Commons, Otto Ambros.jpg](https://commons.wikimedia.org/wiki/File:Otto_Ambros.jpg), credited to U.S. Army photographers acting for OUSCCPAC/OCCWC; the file page identifies the Nuremberg IG Farben trial and records the image as a U.S. public-domain official work.

The source original is archived as `GER_otto_ambros/portrait_GER_otto_ambros_original.jpg` (253×340, SHA-256 `d9b7cf01e00986c33b54190dc33d59584277064139dee4bf14d18a6bf84b8a13`).

The verified crop is `GER_otto_ambros/portrait_GER_otto_ambros_source_crop.png` (197×265, SHA-256 `89c3b3f85e95a43e9c5e80e8deb4a9b07c9ad9a10259e009f75afdb13dcfb6ff`); the crop removes the lower identification placard without retouching the subject.

The processed PNG is `GER_otto_ambros/portrait_GER_otto_ambros_156x210.png` (156×210, SHA-256 `e124d8cd46a5e9ff3a0b164c24a79d0c37662662e336c07ff297c42e7f5bd635`).

The prior runtime DDS is preserved at `GER_otto_ambros/legacy_unverified_dds/portrait_GER_otto_ambros_pre_fix.dds` (SHA-256 `091b35b0a80e6e223e9e62e92c3764d4fb6b85eda6d10c7bb5b5a5230560b73f`).

Parent review on 2026-10-06 passed identity, provenance, and framing, with role-date fit limited because the authentic source is a 1945–49 postwar trial photograph; approval is only for a named source placeholder.

The user-supplied HOI4-style final remains pending; no agent operated RunPod.

## Fictional GER perfect_aryan portrait

This character is a fictional high-chaos subject; no historical person is claimed.

Native ImageGen v1 is retained as the superseded source at `GER_perfect_aryan/source_imagegen/portrait_GER_perfect_aryan_v1.png`, with its matching prompt at `GER_perfect_aryan/prompts/portrait_GER_perfect_aryan_v1.txt`.

Native ImageGen v2 is retained at `GER_perfect_aryan/source_imagegen/portrait_GER_perfect_aryan_v2.png` (1082×1454 RGB, SHA-256 `a540781f7ffef642971c9ab706becbab200f04ba2c6c279fb38d56cb5f8de15b`) with edit prompt `GER_perfect_aryan/prompts/portrait_GER_perfect_aryan_v2_edit.txt`.

The processed v2 PNG is `GER_perfect_aryan/processed_png/portrait_GER_perfect_aryan_v2_156x210.png` (156×210 RGBA, SHA-256 `5fd5b15a8ab92659b1a3bd02b3c76b939428645d5fabb463bdf1c407f7a94f86`).

Parent reviewed native and 4× comparison evidence and approved v2 on 2026-10-06 for identity classification, HOI4 painted style, framing, and fictional temple-join motif.

Before/after evidence is `GER_perfect_aryan/review/portrait_GER_perfect_aryan_before_after_native.png` and `GER_perfect_aryan/review/portrait_GER_perfect_aryan_before_after_4x.png`; the previous DDS remains preserved as `GER_perfect_aryan/legacy_unverified_dds/portrait_GER_perfect_aryan_pre_fix.dds` (SHA-256 `992fd164fd779b10388e3019ff930a9fc3f6b63794df1997709528ffec1a9cdc`).

## Rudolf Weigl study only

The National Digital Archives of Poland source is authentic and marked public domain; the source, attribution, rights, crop, and reviewer findings are recorded in `POL_rudolf_weigl/portrait_POL_rudolf_weigl.txt` and the adjacent crop metadata.

The 2387×2692 archived source JPEG has SHA-256 `87f329bcca3e8c57c72dfae576f9be46b7863953caf99583540d9f31c9abe69c`; the 1100×1480 exact crop has SHA-256 `ded9852373a59efcb90cd37895573373cf8a27bfebe8bf2341c14db5ff3a4a20`; the 156×210 study PNG has SHA-256 `927a107928983656f9c6afd813f8ce267394658804be40f4370ffbc5211fa197`.

Parent review passed identity and provenance but failed framing because Weigl looks down in profile; the study is unpromoted, and the existing DDS remains installed unchanged.

## Blocked historical portraits

Rascher's only located standalone likeness is explicitly non-free, and the freely reusable archival experiment images do not show him as a suitable single bust; bounded evidence is in `GER_sigmund_rascher/blocked_research.md`.

Dufraisse's Commons public-domain laboratory group scene shows him in a cap with a long beard looking down and sideways, while the official College de France portrait preview is watermarked with no reuse license; bounded evidence is in `FRA_charles_dufraisse/blocked_research.md`.

No historical person was generated, repainted, or genericized.

## Processing and wiring evidence

Grounded candidates were cropped without face retouching, and accepted DDS files were made with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`.

The Otto and perfect_aryan DDS files were decoded after conversion and matched their processed 156×210 PNG pixels exactly; the runtime DDS payloads are 131,168 bytes with opaque alpha.

The runtime keys and existing references in `interface/_scientists_portraits.gfx` and the existing scientist character file were inspected and left stable.
