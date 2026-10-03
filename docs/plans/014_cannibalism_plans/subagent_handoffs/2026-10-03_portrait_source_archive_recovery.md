# Event 014 exact portrait source archive recovery

Date: 2026-10-03.

Worker: `chaosx_portrait_creator`.

Disposition: all 16 authorized HATE source packages recovered and accepted by the parent at the archive boundary; the isolated archive commit follows this review. This is archive recovery, not Event 014 completion or final-art acceptance.

The parent independently verifies all 121 archive hashes, all sixteen original/crop/candidate historical hashes and decoded crop/candidate pixel equality, and 62 protected runtime/definition hashes in `docs/plans/014_cannibalism_plans/evidence/2026-10-03_portrait_archive_parent_review.json`.
The parent inspects the runtime aliases, protected static pair and H05/H06 source comparison sheet.
Package-owned `.gitattributes` preserve the recorded receipt, source-page and baseline bytes through Git without disabling inherited image LFS filters.

## Result and approval basis

Recovered H01-H16 from their 16 exact recorded original-image URLs. Every HTTP response was 200 and every accepted original SHA-256 exactly matched the historical original SHA-256. The bundled portrait tool reproduced all 16 historical lossless-crop PNG byte hashes and all 16 historical RGB 156x210 candidate PNG byte hashes. Each candidate has exactly the same decoded RGBA pixels as the current runtime DDS: 0 differing pixels, 0 changed channels, and maximum channel delta 0 for all 16.

Earlier specific user selection of this direct HATE source set is preserved from the August portrait-source recovery, recrop, and 2026-08-25/26 handoff records. The broad current user resume is not treated as a new specific art approval. The current parent action separately authorizes fetching the recorded originals, accepting only exact historical byte hashes, restoring the historical crop packages, and writing archive evidence. No source substitution, repaint, alternative crop, new art approval, or runtime edit is inferred from that archive authorization.

All portraits remain `source_placeholder`. Rights remain `copyrighted_reference_only_user_authorized`; user authorization does not supply a rights-holder redistribution license. No `styled_final` or final-acceptance state was assigned.

## Fetch and attribution evidence

The image fetches occurred between `2026-10-03T09:58:33.544648+00:00` and `2026-10-03T09:58:34.791154+00:00`. All requests used the recorded URLs, with no alternative-image URLs or source replacements. The 16 original responses total 1,038,998 bytes. Original files were decoded as JPEGs and admitted to their subject archives only after exact historical SHA-256 comparison. There are no absent, mismatching, or unrecovered subjects.

The recorded [Alkony HATE base-set source page](https://alkony.enerla.net/english/the-nexus/board-games-nexus/board-game/hate-board-game-base-set-hate-board-game-coolminiornot-2019-board-game-base-set-review) was browsed and downloaded as the attribution record. It credits the artwork to Adrian Smith and image material to CoolMiniOrNot/CMON. The product page identifies production in 2019; an exact creation date for every selected drawing is not established. No permissive redistribution license or public-domain grant is evidenced by this page, so the rights state remains reference-only/user-authorized.

Archived page: `docs/assets/portraits/014_cannibalism/source_archive_recovery_2026-10-03/alkony_hate_attribution.html`, HTTP 200, 131,842 bytes, SHA-256 `d7ade56dfddd12d67a525df3b8cb29e62a0e913b12aff6cc3cec3cf2b958866f`. The unmodified HTML bytes and fetch headers/date/final URL are retained. Direct-image opens through the browser research tool failed internally for the two attempted image URLs; the separately authorized raw HTTP downloads of all 16 exact image URLs succeeded and passed the SHA gate.

The full fetch receipts, original URLs, response headers, UTC times, original/crop/PNG/DDS file hashes, decoded RGBA hashes, crop coordinates, and complete changed-path inventory are recorded in [`source_archive_recovery_2026-10-03.json`](../../../assets/portraits/014_cannibalism/source_archive_recovery_2026-10-03.json), SHA-256 `c20b9c752ef753508637deb985a0ecec41aa4961b5a98836de4c0df666beb588`.

## Recovered subjects

Each archive directory is `docs/assets/portraits/014_cannibalism/<runtime_basename>/`. The last column is HTTP status / crop PNG historical byte-hash result / 156x210 PNG historical byte-hash result / candidate-to-current-DDS differing RGBA pixel count. All original SHA values below equal the previously recorded historical values.

| ID | Runtime basename and durable subject directory | Original dimensions; exact half-open crop rectangle | Recovered original SHA-256 | HTTP / crop PNG / candidate PNG / differing pixels |
| --- | --- | --- | --- | --- |
| H01 | `leader_CBA_warlord_middle_east` | 639x626; [190, 20, 450, 370] | `709941d00812c74426bc3da5ee75c9444b406cf1b75bc11b7cfb70b0127ae486` | 200 / exact / exact / 0 |
| H02 | `leader_CBA_warlord_south_america` | 639x636; [310, 0, 570, 350] | `502d754c06da147a1dfe6ef5db5a291a8279354cc5146dad074d47feb5f97cd7` | 200 / exact / exact / 0 |
| H03 | `leader_CBB_warlord_middle_east` | 639x670; [190, 25, 450, 375] | `9abe67aaa3980881fb106a07f3c9a8b5314b41d1df028a5fa42239eadab1455c` | 200 / exact / exact / 0 |
| H04 | `leader_CBC_warlord_south_america` | 639x708; [165, 45, 425, 395] | `3b5103ba13f00503a88609795e89569d3789ae41702cc3df5d3cc6105054f5a6` | 200 / exact / exact / 0 |
| H05 | `leader_CBC_warlord` | 639x650; [190, 20, 450, 370] | `0b45fbbf20df74c811304a4c18134fb3820585ecdf833bcb195f0d69d3bf756f` | 200 / exact / exact / 0 |
| H06 | `leader_CBD_warlord_north_america` | 920x920; [304, 100, 616, 520] | `7b459af75368acd858996163833eb7f7a27f915124d1961003e5c6f69eaf8691` | 200 / exact / exact / 0 |
| H07 | `leader_CBD_warlord_south_america` | 639x774; [170, 30, 430, 380] | `e252e82e96aadcad805cf7b7a9d75ca388366ba263ebd0f530b4938c0d027b5c` | 200 / exact / exact / 0 |
| H08 | `leader_CBE_warlord_north_america` | 639x659; [185, 15, 445, 365] | `c05d86f699274505b86ac60a7d0bf2c26411ec683c27eb71a62f59edda780bb9` | 200 / exact / exact / 0 |
| H09 | `leader_CBE_warlord_south_america` | 639x681; [145, 80, 405, 430] | `2129af54948660f87e1351d789961f69c26ca6910558ae59277bcac589a10c2d` | 200 / exact / exact / 0 |
| H10 | `leader_CBE_warlord` | 639x671; [190, 20, 450, 370] | `259dc113ec50c0bf39c4b5eaa5458973b80055b79f833805f6a2219257886c3a` | 200 / exact / exact / 0 |
| H11 | `leader_CBF_warlord_africa` | 639x628; [190, 10, 450, 360] | `2f86fb72cbf6fdf6b422876a5c3b2debe1563e66bb7bfedbf9790d09eef533ef` | 200 / exact / exact / 0 |
| H12 | `leader_CBF_warlord_oceania` | 497x600; [130, 20, 390, 370] | `e28e9b5224306e4562ee1500ae5731f8c7f5f6efd109eb9f07a5cbad00629419` | 200 / exact / exact / 0 |
| H13 | `leader_CBF_warlord` | 606x600; [170, 10, 430, 360] | `5d083f9e9bbb87665229f87bde0d9d608467a2d2613d090b642faf932c403e1e` | 200 / exact / exact / 0 |
| H14 | `leader_CBH_warlord_north_america` | 577x600; [167, 30, 390, 330] | `7a72ea9660c2ff97ce2512457fb55a8db99a692e631b51c9654751a2443535b1` | 200 / exact / exact / 0 |
| H15 | `leader_CBH_warlord_south_america` | 598x600; [170, 30, 430, 380] | `c9db8fbd240418a45ea84717f9d0e142dedd081f61504b651280540058aec66a` | 200 / exact / exact / 0 |
| H16 | `leader_CBH_warlord` | 571x600; [155, 0, 415, 350] | `0eb86c7de71f03d857afa08bbdb62a7ef8bbd40fe250a369b1814cfdb9fcb2fe` | 200 / exact / exact / 0 |

Recovered subjects: H01-H16, 16/16. Unrecovered subjects: none. The recorded crop remains 260x350 for most subjects, 312x420 for H06, and 223x300 for H14; candidates are RGB 156x210.

## Package layout and reproducibility

Every subject directory contains the complete co-located package:

```text
<runtime_basename>_downloaded_original.jpg
<runtime_basename>_original.jpg
<runtime_basename>_source_crop.png
<runtime_basename>_source_crop.json
<runtime_basename>_156x210.png
<runtime_basename>.txt
<runtime_basename>_fetch_receipt.json
```

The untouched downloaded original is retained as a stable co-located input. The bundled complete-package tool requires distinct master and source-copy paths, so `<runtime_basename>_original.jpg` is its byte-identical canonical source copy. Both JPG files match the historical original SHA-256. This duplicate is a reproducibility input, not a second artwork source.

All packages were produced through `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py`, tool version 2.0, SHA-256 `f8f764c9f607b880ce305bc4a2b49d9ef2747c8431d2523a14a435418065ad13`, with explicit historical `--crop LEFT TOP RIGHT BOTTOM` arguments and no `--force`. Pillow version is 11.1.0; crops are lossless PNGs, and candidates use RGB Pillow LANCZOS resize to 156x210 with `optimize=False`, `compress_level=9`. No detector or face-box evidence was invented for these manual historical crops.

Each crop JSON retains the tool's normalized command, exact co-located master/output paths, original/crop/candidate dimensions and file hashes, RGBA pixel checks, current DDS comparison, source/page evidence, historical hashes, and approval-basis distinction. Every normalized package path exists and shares the subject directory; its normalized argument checksum was checked. Re-encoding each crop and candidate in memory with the same bundled tool functions reproduced its stored PNG bytes exactly for 16/16. No deleted temporary path is used.

PNG file-byte equality and decoded-pixel equality are separate results. Here both historical crop/candidate PNG file hashes match for all 16. Separately, each lossless crop's decoded pixels equal the original's exact recorded rectangle, and each 156x210 candidate's RGBA bytes equal the current DDS's RGBA bytes. File hashes alone were not used as a substitute for the decoded-pixel checks.

## Worker visual review and H06

All eight new comparison sheets were inspected with the image tool. Each contains the fetched source thumbnail with the historical crop marked, the lossless crop, native candidate/current-DDS views, and 4x nearest-neighbor candidate/current-DDS views. The review confirms fidelity to the selected originals and historical framing. Tight upper crop extents are retained exactly; no independent final-art or alternate-framing approval is inferred.

H06's white field is present in the recovered exact original, the lossless crop, the exact historical candidate PNG, and the current DDS. It remains fully opaque and was not darkened, removed, or repainted. The parent has reviewed the two existing runtime contact sheets and agrees it is opaque; that review is recorded as review of existing pixels, not fresh specific art approval or authorization to edit them. Parent review of these newly recovered archive packages remains pending.

New sheets live under `docs/assets/portraits/014_cannibalism/source_archive_recovery_2026-10-03/review/`:

| New review PNG | Dimensions | SHA-256 |
| --- | ---: | --- |
| `recovered_source_pair_H01_H02.png` | 1320x2796 RGB | `e9e5f34292b62c1f22a91df20a4ade62fb2e79cb635efdb63fc9a2b2764bdc17` |
| `recovered_source_pair_H03_H04.png` | 1320x2796 RGB | `17652e95f49c10fd6161c74af5007be7dcb0815132fbc529df44c3c729d4db5f` |
| `recovered_source_pair_H05_H06.png` | 1320x2796 RGB | `1e5def02c81e023993bed8178e08210309de70c0e9995cf19d79fe054ca644ee` |
| `recovered_source_pair_H07_H08.png` | 1320x2796 RGB | `8e6d16786332dd0f19a3c2cbf6fee31c9a70be857b3ef21538b2ad58d7e3adfa` |
| `recovered_source_pair_H09_H10.png` | 1320x2796 RGB | `d95be113117991287bcc7aa52edc2028eea4d8f16204b4f9c25084e3c1823c58` |
| `recovered_source_pair_H11_H12.png` | 1320x2796 RGB | `f2235c0cb41b942344ca12e4f138d2fdcf0d393cbede85a6aaddca571347dfe4` |
| `recovered_source_pair_H13_H14.png` | 1320x2796 RGB | `5363b8885bba687a7f5526ed0196a11a01eab80dbe365a6d7da1bd42435d25f9` |
| `recovered_source_pair_H15_H16.png` | 1320x2796 RGB | `3106796bce33f11a9f1b5e547563a7a98751b82b3be2ee2a83ad0513f43c1df8` |

## Runtime and shared-checkout preservation

All 60 existing DDS files in `gfx/leaders/014_cannibalism/` have unchanged before/after byte hashes. The portrait GFX registry and existing character file are unchanged. The two earlier review contact PNGs are unchanged.

| Protected existing DDS | Bytes | Current SHA-256 | Before/after |
| --- | ---: | --- | --- |
| `hannibal.dds` | 174,608 | `5c48c9a5b503c3185dcb38ee1aabc403d7668094079b78a20010323930d10b88` | equal |
| `hannibal_wendigo.dds` | 174,608 | `26d7566f7b93d17c4d7fde5b262ab8b6e4b04fba0b862315404d6a33abe34717` | equal |
| `leader_CBL_hannibal_sheet.dds` | 1,572,608 | `f67a1b33a1d4f9b9b1b5ec0d6fb716ad1f2342083e9992550b5dd7356f590587` | equal |
| `leader_ZZZ_hannibal_wendigo_sheet.dds` | 2,096,768 | `f0dfa61ea29293f8393711f97eb67524d336cb6c2a2d55734c0c38484219d18b` | equal |

During recovery, the parent changed approval-basis wording in `2026-10-03_event014_portrait_receipt_repair.md` and `hannibal_static_receipt.md`. Those parent edits are preserved and separately listed in the JSON before/after evidence. The historical source URLs, original/crop/candidate/DDS hashes, and crop boxes in the parent-edited prior handoff were independently checked to be unchanged. This worker did not rewrite either parent-owned document.

## Changed files and remaining gates

This task creates 122 archive files (12,565,985 bytes): 16 subject directories with seven files each, one raw attribution HTML page, eight recovery review PNGs, and one recovery JSON manifest. Every exact path, byte length and SHA-256 except the manifest's own self-hash is listed in the manifest; its self-hash is given above. This handoff is the only new plan document. Existing contacts, the static receipt, runtime textures, GFX, character definitions, gameplay, specs and spreadsheets were not written by this worker.

The missing-original and missing-crop package blockers for H01-H16 are resolved by exact recovery. The prior portrait-receipt repair handoff remains a historical pre-recovery inventory; this handoff supersedes its missing-source statements for these 16 subjects only. User-supplied final-art acceptance, a real permissive rights basis, independent parent review of the new archive, and user-owned live consumer validation remain separate gates. The protected Hannibal statics' external original/crop/creator/rights provenance remains outside this recovery and unresolved.

No simplification, source replacement, or image edit was made. No new DDS was produced; the converter was not rerun because this archive task requires preserved runtime DDS files and direct candidate/current-DDS decoded-pixel comparison. ImageGen, RunPod, and HOI4 were not operated. No source was chosen as a fallback.

No files were staged or committed by the worker. `docs/assets/` is Git-ignored; the parent must include the accepted new archive paths through its shared-index commit workflow. Archive recovery is ready for parent review, while Event 014 and the portraits' final/rights gates are not marked complete.
