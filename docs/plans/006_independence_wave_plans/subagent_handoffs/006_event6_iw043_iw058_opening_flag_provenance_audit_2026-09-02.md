# IW-043 CHU / IW-058 ASY opening flag provenance audit — 2026-09-02

Date: 2026-09-02 (Europe/Kyiv).
Owner: `chaosx_asset_source_researcher` bounded flag/emblem provenance review.
Scope: opening flag/cosmetic families for IW-043 CHU Volga Bulgaria / Chuvash (states 249 and 256, `RG-MIDDLE-VOLGA-KAZAN`) and IW-058 ASY Assyria (state 676, `RG-NORTHERN-MESOPOTAMIA`).
Change boundary: this handoff is the only file added by this audit; no gameplay, flag, GFX, portrait, localisation, or `docs/assets` file was edited.

## Executive verdict

| Package | Exact opening basename | Period and identity finding | Historical-geometry finding | Technical finding | Redistribution finding | Overall |
| --- | --- | --- | --- | --- | --- | --- |
| IW-043 CHU | `CHU_independence_wave_middle_volga_congressX` | **PASS as an explicitly fictional 1936 Middle Volga civic-congress synthesis.** It is not a recovered Chuvash, Volga Bulgaria, or 1918 Idel-Ural flag. | **FAIL for any claim of an attested historical flag.** River lines and the neutral civic ring are generated abstractions grounded in regional/institutional research only. | **PASS.** Normal, medium, and small TGAs are present with expected dimensions, bottom-left origin, 32-bit format, and opaque alpha. | **NEEDS_USER_REVIEW.** ImageGen/provider output terms and redistribution permission are not recorded in the package. | **NEEDS_USER_REVIEW.** |
| IW-043 CHU later route | `CHU_independence_wave_volga_bulgariaX` | **PASS as a later Volga Bulgaria restoration-route synthesis, not as the opening authority.** The heritage reference is period/context grounding, not a medieval state flag. | **FAIL for any claim of an ancient Volga Bulgaria flag.** The arch/minaret/masonry geometry is an archaeological motif, not historical vexillology. | **PASS.** Complete normal, medium, and small ladder. | **NEEDS_USER_REVIEW.** ImageGen/provider output terms and redistribution permission are not recorded. | **NEEDS_USER_REVIEW.** |
| IW-058 ASY | `ASY_independence_wave_national_councilX` | **PASS as an explicitly fictional 1936 inclusive Assyrian national-council civic synthesis.** It preserves the dossier's Assyrian, Chaldean, Syriac, Aramean, church, and faction distinctions by avoiding an exclusive emblem. | **FAIL for any claim of an attested 1936 Assyrian flag.** The four-node civic ring is generated geometry, not a sourced movement, church, Levies, or ancient imperial flag. | **PASS.** Normal, medium, and small TGAs are present with expected dimensions, bottom-left origin, 32-bit format, and opaque alpha. | **NEEDS_USER_REVIEW.** ImageGen/provider output terms and redistribution permission are not recorded in the package. | **NEEDS_USER_REVIEW.** |

The earlier parent handoff `006_iw043_iw058_parent_nonportrait_visual_approval_2026_07_18.md` is a visual review and approved the ten flat flag designs, including these ladders, but it does not clear historical authenticity or redistribution rights.

The opening CHU family is `CHU_independence_wave_middle_volga_congressX`; `CHU_independence_wave_volga_bulgariaX` is a later route-specific cosmetic family and must not silently replace the congress opening.

The opening ASY family is `ASY_independence_wave_national_councilX`; the church compact, civic federation, and security guardianship families are route-specific and must not be used as the inclusive opening flag.

## Accepted historical and institutional basis

### IW-043 CHU

The accepted Event 006 resolution assigns the registered vanilla `CHU` tag to the high-chaos Volga Bulgaria route while sharing the tag with the Chuvashia package, so the opening design must identify a Middle Volga civic authority rather than imply a medieval khanate.

The accepted state anchors are 249 Kazan and 256 Cheboksary, with the opening authority represented by a Middle Volga congress in `RG-MIDDLE-VOLGA-KAZAN`.

The vanilla country file `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/CHU - Chuvashia.txt` confirms state 256 as the CHU capital and the existing `CHU` tag is registered in `common/country_tags/00_countries.txt`.

`SRC-IDEL-URAL-COMMITTEE` and `SRC-IDEL-URAL-STATE` in the source ledger support inclusive 1918 Volga-Ural committee/federal geometry, but they do not establish a settled flag.

`SRC-CHUVASH-PORTAL-SYMBOLS` and `SRC-CHUVASH-ARCHIVE-GUIDE` support a plural institutional route and the refusal to backdate an invented settled Chuvash flag, but neither supplies reusable flag art.

`SRC-BOLGAR-UNESCO` ([UNESCO Historic and Archaeological Complex of Bolgar](https://whc.unesco.org/en/list/981/)) supports the later route's Volga/Kama geography, medieval Bolgar site, Islam, masonry, arch, and minaret design vocabulary; it explicitly does not supply an ancient flag.

The source ledger records the UNESCO page's site text as CC BY-SA IGO 3.0 while warning that image rights vary, so no UNESCO photograph or copied artwork is part of the generated flag package.

The CHU opening prompt therefore correctly forbids a medieval crown, khan, tamga, universal crescent, ethnic hierarchy, and military eagle, and asks for deep river blue, restrained river lines, and a neutral open civic ring.

### IW-058 ASY

The accepted Event 006 resolution anchors IW-058 to state 676 Mosul in `RG-NORTHERN-MESOPOTAMIA` and requires a public Assyrian civic identity that preserves Assyrian, Chaldean, Syriac, Aramean, church, and faction distinctions.

The vanilla country file `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/ASY - Assyria.txt` confirms state 676 as Mosul and existing ASY officeholders; `common/country_tags/00_countries.txt` confirms the registered `ASY` tag.

`SRC-ASSYRIA-IRANICA`, `SRC-ARAMAIC-IRANICA`, and `SRC-ARAMAIC-NAMES-IW058` establish modern naming and community distinctions but provide text research only, not a reusable flag or emblem.

`SRC-MOSUL-UNESCO`, `SRC-MOSUL-UNESCO-DOCUMENTATION`, and `SRC-MOSUL-RENAISSANCE` support Mosul/Tigris, urban, limestone, brick, bridge, and multi-community civic geometry; they do not establish a 1936 state flag.

`SRC-ASSYRIAN-FLAG-EVOLUTION` and `SRC-ASSYRIAN-FLAG-CONTINUE` are attribution-sensitive community-history references with unclear image rights and retrospective interpretation; they are not copied into the opening design.

`SRC-ASSYRIAN-FLAG-BIO` documents the modern AUA design opportunity created in 1968 and the 1973 approval context, so that modern flag is anachronistic for the 1936 baseline and is explicitly excluded.

The ASY opening prompt therefore correctly forbids a current/post-1968/1973 Assyrian flag, cross as a pan-community mark, winged disk/Ashur, Levies badge, church seal, and ancient imperial claim, and asks for four equal civic nodes in a neutral ring.

## Sourced versus synthetic geometry

No direct, defensible 1936 flag source was located for either opening family.

The generated masters are not historical source images, and no source artwork was copied, traced, or redrawn locally.

The CHU congress flag is an alternate-history synthesis from Volga/Kama geography and inclusive committee research; it must be described as a fictional civic-congress flag if documented or exposed to a player.

The CHU Volga Bulgaria flag is an alternate-history restoration-route synthesis from Bolgar archaeological and Islamic heritage; it must never be labelled an ancient Volga Bulgaria flag or presented as a recovered medieval design.

The ASY national-council flag is an alternate-history synthesis from Mosul/Tigris civic geography and the accepted inclusive council structure; it must not be labelled a 1936 historical Assyrian movement flag.

The generated contact sheet shows the designs are visually distinct at normal and medium sizes and retain a central motif at small size, consistent with the parent visual PASS; small 10x7 readability is naturally limited by the engine canvas but is not a missing-ladder failure.

## Source masters and rights record

All three audited families were generated on 2026-07-18 under `source_mode: ImageGen flat graphic design` and retain source masters, processed PNG previews, runtime TGAs, prompts, a manifest, and hash records.

The package does not record an ImageGen provider name, output licence, redistribution permission, or applicable terms for these masters or their derived TGAs.

The package contains no explicit `license`, `rights`, `provider terms`, or `redistribution` field for these flag entries; the absence is a documentation gap, not evidence that the outputs are unlicensed or freely redistributable.

The historical research URLs establish identity, dates, institutions, and design constraints where stated, but they are not asset-specific permissions for the ImageGen outputs.

The correct release disposition is therefore `needs_user_review` until the parent/user confirms the applicable ImageGen output terms or supplies a documented redistribution policy.

## Exact asset paths and hashes

### IW-043 opening: `CHU_independence_wave_middle_volga_congressX`

Source master: `docs/assets/006_independence_wave/iw043_iw058_generated_visuals_2026_07_18/source_png/flags/CHU_independence_wave_middle_volga_congressX_source.png`.

Source SHA-256: `202b7d787198d9997317f6dfcf33a56a2d263c0b57f387ddcb451956c66f1ba1`.

| Size | Processed PNG and SHA-256 | Runtime TGA and SHA-256 | Header and dimensions |
| --- | --- | --- | --- |
| normal | `docs/assets/006_independence_wave/iw043_iw058_generated_visuals_2026_07_18/processed_png/flags/CHU_independence_wave_middle_volga_congressX_normal.png` — `548b458d7d26a8ffe99f7015989cefa6f996146af2c8b70ccd1c10fc631bca63` | `gfx/flags/CHU_independence_wave_middle_volga_congressX.tga` — `88461d5c345d40ed8bd7d31dfbfad07ceb59b5225174059547e6807776db0678` | `000002000000000000000000520034002008`; 82x52, 32-bit, bottom-left, opaque |
| medium | `docs/assets/006_independence_wave/iw043_iw058_generated_visuals_2026_07_18/processed_png/flags/CHU_independence_wave_middle_volga_congressX_medium.png` — `2534e8980900e23009610e5bccf9a441cd2f50e4bd2df7dd5360637d8bcc5a2c` | `gfx/flags/medium/CHU_independence_wave_middle_volga_congressX.tga` — `196ab37bfb4721e39ae7b77538a05260c875ad155da374e060ebaf078462fff7` | `00000200000000000000000029001a002008`; 41x26, 32-bit, bottom-left, opaque |
| small | `docs/assets/006_independence_wave/iw043_iw058_generated_visuals_2026_07_18/processed_png/flags/CHU_independence_wave_middle_volga_congressX_small.png` — `ddc48299af60d7f1eece910054fc69aa40682b1251e7f3583a38e3dc6ac358d5` | `gfx/flags/small/CHU_independence_wave_middle_volga_congressX.tga` — `36fc118be2c42edc9b1ac3449ed6a50b2db452317673c89f6e211591f8302ea8` | `0000020000000000000000000a0007002008`; 10x7, 32-bit, bottom-left, opaque |

### IW-043 later route: `CHU_independence_wave_volga_bulgariaX`

Source master: `docs/assets/006_independence_wave/iw043_iw058_generated_visuals_2026_07_18/source_png/flags/CHU_independence_wave_volga_bulgariaX_source.png`.

Source SHA-256: `75746cdbab0a203d8285d2687dd2c9b87ad48c2b7f9d910a98e0b1018624864b`.

| Size | Processed PNG and SHA-256 | Runtime TGA and SHA-256 | Header and dimensions |
| --- | --- | --- | --- |
| normal | `docs/assets/006_independence_wave/iw043_iw058_generated_visuals_2026_07_18/processed_png/flags/CHU_independence_wave_volga_bulgariaX_normal.png` — `683e711fda89749f6e9870aee46be202131d0041f54610b7fb8af5abe8f888be` | `gfx/flags/CHU_independence_wave_volga_bulgariaX.tga` — `fda372a784d2c06e75725465461e04c742b986527956ac8c8b32aedad8310146` | `000002000000000000000000520034002008`; 82x52, 32-bit, bottom-left, opaque |
| medium | `docs/assets/006_independence_wave/iw043_iw058_generated_visuals_2026_07_18/processed_png/flags/CHU_independence_wave_volga_bulgariaX_medium.png` — `38545ba9acfef18a540946cc1a9faf748144682a851bae0e8e22da0612c17df1` | `gfx/flags/medium/CHU_independence_wave_volga_bulgariaX.tga` — `501ea6d644d40133fb5896a3b8523734789e68319f436cdd4e8d0964fef369cd` | `00000200000000000000000029001a002008`; 41x26, 32-bit, bottom-left, opaque |
| small | `docs/assets/006_independence_wave/iw043_iw058_generated_visuals_2026_07_18/processed_png/flags/CHU_independence_wave_volga_bulgariaX_small.png` — `37828c605a28a859d7a63cb8c039be034dc768f0f69c93e7479c95c318993155` | `gfx/flags/small/CHU_independence_wave_volga_bulgariaX.tga` — `93a55ea49d77b68db97ac3342cf8de26b2db7ac2af5582d55ba712fd9803ea38` | `0000020000000000000000000a0007002008`; 10x7, 32-bit, bottom-left, opaque |

### IW-058 opening: `ASY_independence_wave_national_councilX`

Source master: `docs/assets/006_independence_wave/iw043_iw058_generated_visuals_2026_07_18/source_png/flags/ASY_independence_wave_national_councilX_source.png`.

Source SHA-256: `8cf752a4a3d54b28a123e83aa8c30a2bf0e1aebf0fbccd39c0a06861d7edcb66`.

| Size | Processed PNG and SHA-256 | Runtime TGA and SHA-256 | Header and dimensions |
| --- | --- | --- | --- |
| normal | `docs/assets/006_independence_wave/iw043_iw058_generated_visuals_2026_07_18/processed_png/flags/ASY_independence_wave_national_councilX_normal.png` — `7eae2f2d3f22da27f180a4bc5e99864f2cf0a77634704ccad90c794509409da8` | `gfx/flags/ASY_independence_wave_national_councilX.tga` — `baa2008e1ff1b2063b04c36142835c6534665bd811394accbfe7966c5cd47178` | `000002000000000000000000520034002008`; 82x52, 32-bit, bottom-left, opaque |
| medium | `docs/assets/006_independence_wave/iw043_iw058_generated_visuals_2026_07_18/processed_png/flags/ASY_independence_wave_national_councilX_medium.png` — `1a60c898fa149505357c8e607d4c18b34a42cbc5e452eca842ea38efa6cbb05c` | `gfx/flags/medium/ASY_independence_wave_national_councilX.tga` — `c3a31a5452569cd1d2800146ed147f5f1b78f40de07b398ad2f59c9ebcd0c96f` | `00000200000000000000000029001a002008`; 41x26, 32-bit, bottom-left, opaque |
| small | `docs/assets/006_independence_wave/iw043_iw058_generated_visuals_2026_07_18/processed_png/flags/ASY_independence_wave_national_councilX_small.png` — `437dee7f2e4cd9a16dd287b96843b0572b554d6b5c46ea3701c66bc89f88bbdd` | `gfx/flags/small/ASY_independence_wave_national_councilX.tga` — `89931888db5deba167779414629cfdfc31feb7475c86a6b0b07883eb706ed474` | `0000020000000000000000000a0007002008`; 10x7, 32-bit, bottom-left, opaque |

The live runtime SHA-256 values above were re-read on 2026-09-02 and match the package manifest entries.

## Vanilla and canonical reference checks

The required offline wiki flag conventions were checked in `paradox_wiki/Cosmetic tag modding - Hearts of Iron 4 Wiki.md` and `paradox_wiki/Country creation - Hearts of Iron 4 Wiki.md`: filename-based flag ladders use uncompressed 32-bit TGA, bottom-left origin, and normal/medium/small dimensions of 82x52, 41x26, and 10x7.

The canonical review shelf is `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/flags/contact_sheet.png` (SHA-256 `cbf35c6f96347537a5d8e781b198e5949a6515f959f1bc12b55d35847cb36b3e`) from the extracted Vanilla HOI4 flag family; it shows the expected clean, flat, minimal geometry.

Installed Vanilla HOI4 references were checked under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/flags/` and its `medium/` and `small/` folders.

Vanilla CHU has `CHU_neutrality.tga`, `CHU_democratic.tga`, `CHU_fascism.tga`, and `CHU_communism.tga` in all three sizes; the normal header is `000002000000000000000000520034002008` at 82x52, the medium header is `00000200000000000000000029001A002008` at 41x26, and the small header is `0000020000000000000000000A0007002000` at 10x7.

Vanilla CHU neutrality hashes checked were normal `73581aff21305ae888ec64f075bb1764c6c2b51f32b7773814e9ae2e56ba5929` and medium/small file sizes 4803/298 bytes; custom ladders use the same dimensions and bottom-left origin while carrying an explicit 8-bit alpha descriptor.

Vanilla ASY has `ASY_neutrality.tga`, `ASY_democratic.tga`, `ASY_fascism.tga`, and `ASY_communism.tga` in all three sizes, plus `ASY_neo_assyrian_empire_{neutrality,democratic,fascism,communism}.tga` in all three sizes.

Vanilla ASY and `ASY_neo_assyrian_empire` normal headers are `000002000000000000000000520034002000` at 82x52, medium headers are `00000200000000000000000029001A002000` at 41x26, and small headers are `0000020000000000000000000A0007002000` at 10x7.

Vanilla ASY neutrality normal SHA-256 is `3afbc4a6f8060c5f0d1895c5468b85a3c0fff6875950de0dbac5e9a6b5363581`; vanilla `ASY_neo_assyrian_empire_neutrality.tga` normal SHA-256 is `4914217d3a1bdc857897a26cbfcb777a0da2691b28c490a2ff618e0c62a3c3d7`.

The custom files conform to the required dimensions, uncompressed 32-bit pixel format, and bottom-left origin; their presence and hashes do not establish historical provenance or redistribution clearance.

## Contact sheet and GFX handoff

The existing comparison sheet is `docs/assets/006_independence_wave/iw043_iw058_generated_visuals_2026_07_18/contacts/flags/flags_ladders_contact_sheet.png` (SHA-256 `9c07547a662cd06410aa74ad9ac06b07451fb667874128a571a850b96aea5fa6`).

It compares all ten generated flag ladders, including the three audited here; no new candidate sheet was needed and no generated flag was created during this audit.

Flags are engine-convention TGAs and do not require custom `.gfx` sprites.

The exact proposed runtime basenames for parent wiring are `CHU_independence_wave_middle_volga_congressX`, `CHU_independence_wave_volga_bulgariaX`, and `ASY_independence_wave_national_councilX`, with matching `.tga` files in `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`.

The existing package `docs/assets/006_independence_wave/iw043_iw058_generated_visuals_2026_07_18/gfx_handoff.md` already records the filename-based flag handoff boundary; this audit adds no `.gfx` registration and no DDS because flags use TGA runtime files.

## Blockers and required parent action

Do not describe either opening design as a historical 1936 flag, a medieval Volga Bulgaria flag, a recovered Idel-Ural flag, a modern Assyrian movement flag, a church emblem, a Levies badge, or an ancient imperial standard.

Do not promote the technical `handed_off` status or the parent visual `Approved` finding into a rights-cleared or historically attested status.

Parent/user action is required to confirm the applicable ImageGen output terms and redistribution policy before release or to keep these flags explicitly evidence-only pending that confirmation.

No additional sourced candidate is recommended from the reviewed materials: the direct historical flag gates remain unsatisfied, and the accepted alternative-history synthesis is already separated by route and identity.
