# Event 023 achievement source recovery handoff

Date: 2026-09-25.

Disposition: implemented for source recovery, deterministic processing, package DDS reproduction, and static visual review. Exact per-icon prompt provenance remains unresolved, and live HOI4 consumer review remains `needs_user_review`.

## Scope and ownership

This pass was limited to `docs/assets/023_sov_nuclear_bombs/` and this handoff. It did not edit runtime DDS files, GFX, achievement definitions, localisation, gameplay, or the validator `notes/validate_icon_package.py`, which the parent has taken ownership of updating and validating. No source material was deleted; the 21 derived input layers were retained under their correct processed-input folder rather than represented as source originals.

## Restored source-of-truth and exact paths

The only seven source originals are the unchanged ImageGen masters at `docs/assets/023_sov_nuclear_bombs/source_png/achievements/<achievement_id>_native_source.png`. Each is a 1254x1254 RGBA PNG with alpha extrema 0..255; the current copies match both the supplied expected hashes and the parent’s independent confirmation.

| Achievement id | Native source path | Native source SHA-256 |
| --- | --- | --- |
| `023_sov_nuclear_bombs_a_hundred_suns` | `source_png/achievements/023_sov_nuclear_bombs_a_hundred_suns_native_source.png` | `039f66206ee616d1d2a17fb9223a5dd6152e24e9472b9e761dcd03f83a10bcc9` |
| `023_sov_nuclear_bombs_the_bomb_never_fell` | `source_png/achievements/023_sov_nuclear_bombs_the_bomb_never_fell_native_source.png` | `78fa5bf34efa944c136fae00cfd54ebcb4e2eadf7ae8045f1f1f937fc32da15f` |
| `023_sov_nuclear_bombs_ultimatum_without_ash` | `source_png/achievements/023_sov_nuclear_bombs_ultimatum_without_ash_native_source.png` | `4d1b531f0f92bdccd4ffa9cc5b5581c28a011626ff6d93225265c7ca65dcfa4c` |
| `023_sov_nuclear_bombs_scattered_arsenal` | `source_png/achievements/023_sov_nuclear_bombs_scattered_arsenal_native_source.png` | `dd2db7c50aa2968087804e97d39cb8e8fe421c6aeef976f93824449517f580b8` |
| `023_sov_nuclear_bombs_firebreak` | `source_png/achievements/023_sov_nuclear_bombs_firebreak_native_source.png` | `0c3ef8cea9bac718357f62b86b1366dcdd434c70cb3a37aac99aa4a22b6f01d6` |
| `023_sov_nuclear_bombs_first_and_last` | `source_png/achievements/023_sov_nuclear_bombs_first_and_last_native_source.png` | `d9486a9a82a7ff4220ed2b9946dd6e398afa3a713fa0945412005547e97b3483` |
| `023_sov_nuclear_bombs_the_last_telephone` | `source_png/achievements/023_sov_nuclear_bombs_the_last_telephone_native_source.png` | `9b1684dce16ce988761ebc7c748d50abbcb3cfe6cfe7ccc84fe3eefabee84222` |

The exact per-icon prompt text was not recovered. The earlier icon-audit handoff points to `docs/assets/023_sov_nuclear_bombs/prompts/icon_prompt_set.md`, but that file is absent in this checkout; the active package and cited handoffs were searched. No prompt was inferred, reconstructed, or claimed as original.

The 21 derived 64x64 subject-state inputs are at `docs/assets/023_sov_nuclear_bombs/processed_png/achievement_subject_layers/<achievement_id>{,_grey,_not_eligible}.png`. They are derived processing inputs, not original masters or source triplets. The deterministic derivation fits each native master with LANCZOS into a centered 62x62 maximum on a transparent 64x64 RGBA canvas, makes grey RGB with grayscale while preserving the color layer’s exact alpha/canvas, and composites the unchanged 64x64 red-cross overlay above that grey layer for not-eligible.

The 21 final processor-composited PNG states are at `docs/assets/023_sov_nuclear_bombs/processed_png/achievement_layers/<achievement_id>{,_grey,_not_eligible}.png`; identical processor review PNGs are at `docs/assets/023_sov_nuclear_bombs/dds/achievements/review/<achievement_id>{,_grey,_not_eligible}.png`. Package DDS outputs are at `docs/assets/023_sov_nuclear_bombs/dds/achievements/<achievement_id>{,_grey,_not_eligible}.dds`. The runtime comparison targets are the existing `gfx/achievements/<achievement_id>{,_grey,_not_eligible}.dds`; none was overwritten or promoted.

## Immutable template inputs

The canonical template and overlay files were preserved unchanged and verified against the asset-skill hashes: `achievement_template.png` SHA-256 `248DB006611EB3942550C43DF83802AA6FB24761035FC928B5D34586C0C4C5BA`, `achievement_template_grey.png` SHA-256 `70E073694C1A7D9FE40C63B1EB2E987A8A45B3FFD15CCF789EEAA5B843B90022`, and `overlay.png` SHA-256 `89BC80C6AC975BF6F1FF000FF3070B20C337BFB8B8AE966AE35A5540C004D6DD`.

## Per-ID hashes and equivalence

State hashes in each triplet below are ordered `color / grey / not_eligible`. “Derived input SHA-256” refers only to the 64x64 working layers under `processed_png/achievement_subject_layers/`; “processed PNG SHA-256” refers to the completed-background previews under `processed_png/achievement_layers/`. Package DDS hashes equal the current runtime DDS hashes byte-for-byte for all three states of every ID.

| Achievement id | Derived input SHA-256 | Processed PNG SHA-256 | Package/runtime DDS SHA-256 | Per-ID equivalence |
| --- | --- | --- | --- | --- |
| `023_sov_nuclear_bombs_a_hundred_suns` | `08e9df67988a50fea1ce431af3ab26ffb2bdcf1dc21a42a30c291e58964cad4e / 704463233c823db4700eacc036b0ea0e5d7bd69a4c6f50125880e0c0675b3ff0 / 7317141a3071359b1f656c615b0121610c3574addba3581a377736745d7f3ba4` | `67993f9e58a924f42241b2985c3d783cd36c8e1145681ed709a874e2fbba1242 / 3b2e8ab116b1ca704ff75086bb990bc3ea8181c325e9932a1fb88550cd93339d / 422f22e4d30f3b59a416a4d1c0d2ebb364dbfe3ce2ffe9a15278e1c16ac82633` | `426a76abe0b64cc10f1151fd5547f55ebc405853d22cce207ca72dd526204a5b / f1dbe6be5a9c132ec1f3d8541f0da842a5b43292103ec5bfc90d3047d7e1818c / 11951c082040a4d288ff436a7a621e7c1bf85b45f2c2476df8b55d4b573086ea` | 3/3 PNG pixels = strict package/runtime DDS pixels; DDS byte hashes equal |
| `023_sov_nuclear_bombs_the_bomb_never_fell` | `87647a3b192f672cfa371af5c0f1f703c7b5acb8949e82ef570fb2b256909c7f / 5887d6f464dd665ccdae043ee0060a940ec1ce5160d0a58207adecf6d9197f88 / afc965866d9b55538b9508349c72a46320cd2171618b7c22ab0c97e580dca2f6` | `bb4a30d7d1ec803e161eb57b417f2712c5eee199fefb7955da94a322d2bae315 / 1414afa6062142bd17d206d546c12dca9d877201585cde4bf13ff660ea8fcbac / fc7bbb6152dc19fcf0a5cb4f7f93e55f95ce7dc0bf1ccb8916539f3a647bf80f` | `c26db13c9027dc41698d346aedc8fb3fb81e0b594f04d399649784029a78ae5c / 7d00df3ef099e894d65427d52c9ddc9aca888c80d60021547c69574655d5b725 / 04bc5101c407d1aa827382299fb2f2fc7dd8e1b7a1023b8bf0c4c866fc7a9e10` | 3/3 PNG pixels = strict package/runtime DDS pixels; DDS byte hashes equal |
| `023_sov_nuclear_bombs_ultimatum_without_ash` | `5849e0bba7a1de85a13764133ea5730e1e2a766adab366dbd3f5e852c4ec9d1e / 10ed877f517ffe3ef04d6de3a32f589d1e50bf4282cd83ac17a3cc26a4ed1893 / 3fd2f2902fa20f58ecd9906336642c4b9e302efd0bfe67a64bab9db275dbd04f` | `ab9bfb194742b3e79db6a40793076a2463f5fc2272f1c1125cbbc7880ac76431 / bde13c4dbd9a2272e02a043dc0741877012acef22bcd691f48980ad83fc90141 / 3f6d2db9613c8ee082bea7c7dab2eda6224dae4765bbc76fead81353fd993bff` | `83f2722e1d979e0ff48d977ad83568b90e0c142f34ddcc5ac8a705015b2e53f2 / d2d12440295ce7f4a31c9c6dc4b6a48ece943a9823cb12f9b2e7bcd1a6f5add0 / 6ddd57b287b0dd6f4efcbe863cd77e51493747f78a6de34f9147bb8c77d356e6` | 3/3 PNG pixels = strict package/runtime DDS pixels; DDS byte hashes equal |
| `023_sov_nuclear_bombs_scattered_arsenal` | `dea16e2717e0a70387750e0f06284d4642470e412e18534fb93cff69bffed51b / 906491b01099e6c68b15023fb24328510f381f7a067a1bf29ef7e2c47244c770 / 3ba0565e69b5438c2fe281af59d92cc91330a55fd0e85f264ff101c2d7f0f571` | `069bfa0ac10f6edbd4cdf62e6204cc8bcdae6bbc9eae79a464e6258685880f7c / 9bd35b76ae1ec4e62955a75cdb1c5e4c53f6a5cab1ec345115adc80e4d049432 / c847b71b7869f62234e5dba50511c33456fb0283c817bce3ac3b9901975e77e5` | `c039b9f009d887cb6119c851c1359eb7915e28ec77ea7bcf8abadef756fe6dd2 / 03635d1a0e58669bc4dccdc00b85acc8835d132073556f926a24f0ab61ba3b6d / 187466e4b334a35c8944641d00d0e910e035c64f11f1ed9a4b3012321c9444dd` | 3/3 PNG pixels = strict package/runtime DDS pixels; DDS byte hashes equal |
| `023_sov_nuclear_bombs_firebreak` | `b347803ed89269f5f47f22a108d7c7704a14444549e7e66c0bf08159294c9025 / 6e8552f40ecd1788faf5a12450cf189edb3327731fd0e4a7685e8a0fb2a52050 / d9cae391cdcbf54a84ccf7bb144ab993132a3771624fc56b55dc4c25d378af42` | `43dfd2f8bd83954cd6aa3c3124d15a01545d32e2cea096be410879d75c9f9a37 / a8b5229d9682c4a6c14fc699e5fc693021d83df182f5e59317bde72adbb9c448 / 0544454cd9ae04b767244e4167b9759d1b0efe11778b729a727c88927b53bf62` | `58d9d5751d01285cacb445aed62c47940eaba06c1d9d8030d21a7bdfd32daf8e / ef8aac97382ef02b15241b7161ed46eacdea1a5fb2615a71ee6cc3d82c04e049 / cd89810fa9f5e6239f93ac1575400c5914b723f13ec722b8f9c16a17c2ed27e3` | 3/3 PNG pixels = strict package/runtime DDS pixels; DDS byte hashes equal |
| `023_sov_nuclear_bombs_first_and_last` | `6f1c3d8049fd091ef17851710b6633b17ea75316cc826b3ab1321f686731d89e / 4b501dd27a5b116c60d1a15776b6d864be91d14445b8b3952b16592c49695ef1 / 27cffedf233650cc9054f4e3df23f588e5ef8f5c6afa4172f0ed4d5cb7c982f2` | `e4f0ba156e6e9ee9e0dc45a28103d6fd7c460ab4d6e59a9e038b1a774a5b24ae / 182656c28f8763217c824551663e501bf9ffcc16bd3eeee2a8ded007301a15f5 / e0093491871c81af9827da50da1af8ad63cc9863c860b134d571441133b67c08` | `b07f5355d7b7137507092c9fd51fdfd3d619c946ab88c3beb8bb4559b93a3b1b / 4b694e421e0b6c45e46f2ce7bb184b1029f1102f65f1916ca35c59d3a7ba03d1 / 5b5a57258787b3e9732feffac67b70fb605b03cd3684436c06d44fc223bb33dd` | 3/3 PNG pixels = strict package/runtime DDS pixels; DDS byte hashes equal |
| `023_sov_nuclear_bombs_the_last_telephone` | `79d0ab8483f0665430a7ad8d94fe604afa58c2112559a02a8650a7e39101eb93 / d0263d7817bed7071964a7d7467addd3fcddaf142469c8520af07436efed36a6 / 8a32b69ed6f2aeb8c19d64cd2085169184c6115b40f810066d99203a78ee49fa` | `5df4cfd16139f1034ae5cff39c6c8ef25788f5c72f3df4ad220c0be1e0efd775 / 63c3a599b41d0c46a3563079218f68549ce61ae133f329ca35af6c0980a1d8fa / 1769b25207ee95bc39e4ec157f79cbd7cb121dd277f44a382ecd9382b801cb39` | `7a4a0846f8879c8f5ae4a9b8c5891ea005c55dba19e7f9ad10c0406d2a885fec / c6d7109aeb3f01e5afd5f6f36fa7bb87c955be8a2f48e0c9f46f1b8d1a1d34d0 / 44b7c32193b550c298a04ee2e87a9d33f05698d54260bb090dd4f0795271201b` | 3/3 PNG pixels = strict package/runtime DDS pixels; DDS byte hashes equal |

Parent audit identified `processed_png/achievement_layers/023_sov_nuclear_bombs_scattered_arsenal_grey.png` as the only processed-PNG SHA-256 differing from its historical record, while confirming pixel identity. The prior `023_icon_asset_audit_repair.md` digest is `9bd35b76ae1ec4e62955a75cdb1c4e5c53f6a5cab1ec345115adc80e4d049432`; the current file SHA-256 is `9bd35b76ae1ec4e62955a75cdb1c5e4c53f6a5cab1ec345115adc80e4d049432`. Its pixels equal the processor review PNG and strict-decoded package/runtime DDS. The matching runtime/package DDS SHA-256 is `03635d1a0e58669bc4dccdc00b85acc8835d132073556f926a24f0ab61ba3b6d`. This is a non-visual PNG encoding/hash delta, not an art or pixel mismatch.

## Commands and validation results

The canonical processor was used to regenerate all package triplets from `processed_png/achievement_subject_layers/`; `--force` targeted only the package output directory, never runtime. The seven separate audit runs all returned `AUDIT OK`, confirming strict 64x64 BGRA triplets and source-layer equality.

```powershell
python -B .agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py --completed "docs/assets/023_sov_nuclear_bombs/processed_png/achievement_subject_layers/$id.png" --grey "docs/assets/023_sov_nuclear_bombs/processed_png/achievement_subject_layers/$($id)_grey.png" --not-eligible "docs/assets/023_sov_nuclear_bombs/processed_png/achievement_subject_layers/$($id)_not_eligible.png" --achievement-id $id --output-dir docs/assets/023_sov_nuclear_bombs/dds/achievements --write-png --force
python -B .agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py --input docs/assets/023_sov_nuclear_bombs/processed_png/achievement_subject_layers --achievement-id <achievement_id> --output-dir docs/assets/023_sov_nuclear_bombs/dds/achievements --audit
python -B docs/assets/023_sov_nuclear_bombs/tools/build_achievement_source_recovery_sheets.py
```

The sheet builder strict-decodes package and runtime DDS through the canonical processor’s BGRA decoder and asserts 64x64 dimensions, nonblank cells, PNG/package/runtime pixel equality, package/runtime byte-hash equality, and expected populated counts before writing sheets.

## Exact changed paths

- `docs/assets/023_sov_nuclear_bombs/source_png/achievements/` now contains exactly the seven `<achievement_id>_native_source.png` originals listed above.
- `docs/assets/023_sov_nuclear_bombs/processed_png/achievement_subject_layers/` contains the 21 `<achievement_id>{,_grey,_not_eligible}.png` derived subject-state inputs listed by hash above.
- `docs/assets/023_sov_nuclear_bombs/processed_png/achievement_layers/` contains the 21 final processed composite PNGs listed by hash above.
- `docs/assets/023_sov_nuclear_bombs/dds/achievements/` contains 21 regenerated package DDS files listed by hash above; `dds/achievements/review/` contains the matching 21 processor PNG review files.
- The corrected comparison sheets are `docs/assets/023_sov_nuclear_bombs/contact_sheets/achievement_source_recovery_contact_sheet.png` (SHA-256 `236bfaf289f11253756c419a0d9fa7f60d6156d5e9374f9305fdbc48476f9a4d`), `achievement_source_recovery_contact_sheet_4x.png` (`994169bc26df4040cd4c438b32069a311458b14d9daa363ba4946f3eb1e33917`), `achievement_package_runtime_dds_contact_sheet.png` (`57facf9e8414de41762b3ffe98d534c49bb7c60dbed4a8454d4b3d719537977d`), and `achievement_package_runtime_dds_contact_sheet_4x.png` (`18ac18534c11baba64063d411abd949d57187b61ecd674c8195a5e0514d8dfd7`).
- `docs/assets/023_sov_nuclear_bombs/tools/build_achievement_source_recovery_sheets.py` is the repeatable explicit-path sheet builder; it replaces the earlier broken mapping for this comparison.
- `docs/assets/023_sov_nuclear_bombs/manifest.md`, `docs/assets/023_sov_nuclear_bombs/gfx_handoff.md`, and `docs/assets/023_sov_nuclear_bombs/notes/achievement_state_audit_2026-09-25.md` were updated to reflect recovered masters, derived-versus-original boundaries, package/runtime equivalence, contact-sheet evidence, prompt provenance, and the PNG hash note.
- This file, `docs/plans/023_sov_nuclear_bombs_plans/subagent_handoffs/023_achievement_source_recovery_2026-09-25.md`, is the new recovery handoff.

## Visual findings and remaining limits

The seven native masters were inspected individually at native 1254x1254 size. The derived subject-state inputs, processed PNGs, and decoded package DDS were reviewed at native 64x64 and 4x nearest-neighbour scale through the populated source-recovery sheets; package DDS and current runtime DDS were reviewed side-by-side at both scales. The images and state distinctions are intact, no visual mismatch was found, and source-to-package reproduction is exact at decoded-pixel level.

No background-removal fallback, repaint, independently generated state artwork, or appearance-changing substitute was used. Runtime DDS, GFX, achievement definitions, localisation, and gameplay were unchanged. The exact per-icon prompt remains unavailable, and no live HOI4 consumer test or user-owned visual sign-off is claimed.
