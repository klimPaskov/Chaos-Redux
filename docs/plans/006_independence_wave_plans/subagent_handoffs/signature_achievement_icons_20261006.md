# Event 006 signature achievement icon handoff

Disposition: implemented. The parent accepted the three native ImageGen subject masters and reviewed and accepted the native-size and 4x triplet contact sheets on 2026-10-06. The accepted masters depict Oyo’s stool and paired horse-head figures, Aceh’s sailboat, harbour tower, and open book, and Mon’s hamsa bird, bridge, and book.

## Runtime assets

All nine DDS files are newly installed directly under `gfx/achievements/`, at 64x64, with a 16,512-byte strict legacy one-level uncompressed BGRA layout. Their alpha range is 254–255 because the exact supplied achievement backgrounds are nearly opaque. Source subject layers retain native transparency. The table records SHA-256 for the runtime bytes.

| Achievement id | State | Runtime path | SHA-256 |
|---|---|---|---|
| `chaosx_006_oyo_compact` | completed | `gfx/achievements/chaosx_006_oyo_compact.dds` | `1d51e4ffa8edd7ced03004d461f2e9e7a44b3429312d2e649bb9e00be495051f` |
| `chaosx_006_oyo_compact` | grey | `gfx/achievements/chaosx_006_oyo_compact_grey.dds` | `874dc66e3981894f82536de8459fd9b5374742063f08a0427b79bb323bd2ab9b` |
| `chaosx_006_oyo_compact` | not eligible | `gfx/achievements/chaosx_006_oyo_compact_not_eligible.dds` | `79d4760da1b31336dece08e364e18008e49c8530a9915ddf8b7a12d73c0e0fee` |
| `chaosx_006_aceh_free_ports` | completed | `gfx/achievements/chaosx_006_aceh_free_ports.dds` | `3488cb3fee745d3b42406c905867089821c215389a47c8b916efc5b7d22dbe86` |
| `chaosx_006_aceh_free_ports` | grey | `gfx/achievements/chaosx_006_aceh_free_ports_grey.dds` | `a88d4184eb9937aeaca81ad6bbedf24fbf3c15d5fdb07e46748363e2d0c3eef6` |
| `chaosx_006_aceh_free_ports` | not eligible | `gfx/achievements/chaosx_006_aceh_free_ports_not_eligible.dds` | `1db802f401ff7739c6de0cb295fa2194b47521b9b4bda8f2df3b3bb63c999631` |
| `chaosx_006_mon_federal_charter` | completed | `gfx/achievements/chaosx_006_mon_federal_charter.dds` | `24f3ae85945b77054a6f6faa277bd844e5bc93965d745f6050af9484a9f3656e` |
| `chaosx_006_mon_federal_charter` | grey | `gfx/achievements/chaosx_006_mon_federal_charter_grey.dds` | `4542e44addbfc2dd6838e8ff5c57b55d4063d2fc3812d7df917d0f2fc66390de` |
| `chaosx_006_mon_federal_charter` | not eligible | `gfx/achievements/chaosx_006_mon_federal_charter_not_eligible.dds` | `0fc18db4b79ece08b210088bdc2a882b3dd6fc902cbf5d0ca43dad177e3ebd8d` |

## Source and processing evidence

The immutable accepted masters and both ImageGen request records remain in `docs/assets/006_independence_wave/signature_achievements_20261006/`. The first, framed candidates are retained as rejected provenance and were not used. The accepted master hashes are `06b2459b52009de3e6a6c83504cdca7d308e21173c628d573757cb95823affe9` (Oyo), `345eb629fcc4b9f178343b0876deeb377b7769727e6f6d6a7faaffa5b60aaaca` (Aceh), and `cb7bf2bd0e5a4b8c8251b22e94614c86248d63e3f69a160ac2b9381b9bb7d9be` (Mon). Each folder also retains `initial_request_rejected.json`, `native_subject_edit_request.json`, and the rejected framed draft PNG.

`prepare_achievement_triplets.py` records the deterministic preparation: each untouched 1254x1254 RGBA master with alpha 0–255 was cropped to its alpha-at-least-2 silhouette with an 8px source guard, fitted toward a 45px maximum footprint by premultiplied-alpha Lanczos, and centered on a transparent 64x64 canvas. Isolated alpha=1 residue was cleared while the originals remained unchanged; the removed pixel counts were 8,151 for Oyo, 7,159 for Aceh, and 10,383 for Mon. The resulting alpha-at-least-2 bounds are 46x30, 46x44, and 45x46 respectively, leaving at least 9px of clear margin after raster rounding. The Oyo artwork is naturally horizontal and therefore occupies less vertical space; parent review accepted its native-size readability.

The complete source triplets are under `docs/assets/006_independence_wave/signature_achievements_20261006/source_triplets/`. Grey sources are deterministic grayscale RGB derivatives of each color source with the same alpha. Not-eligible sources are the exact supplied overlay composited over the corresponding grey source. Supplied template hashes were verified unchanged: completed background `248db006611eb3942550c43df83802aa6fb24761035fc928b5d34586c0c4c5ba`, grey background `70e073694c1a7d9fe40c63b1eb2e987a8a45b3ffd15ccf789eeaa5b843b90022`, and red-cross overlay `89bc80c6ac975bf6f1ff000ff3070b20c337bfb8b8ae966ae35a5540c004d6dd`.

The triplets were processed with `.agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py`. Its `--audit` pass against the nine installed runtime DDS files returned `AUDIT OK` for all three ids. Every DDS was strict-decoded and matched the exact supplied template-under-source composite byte-for-byte. `validation_evidence.json` records dimensions, hashes, alpha ranges, and source-to-runtime pixel checks.

Visual reviews are retained at `docs/assets/006_independence_wave/signature_achievements_20261006/review/native_contact_sheet.png` and `docs/assets/006_independence_wave/signature_achievements_20261006/review/4x_contact_sheet.png`; the processor’s individual composited review PNGs are under `docs/assets/006_independence_wave/signature_achievements_20261006/processed_outputs/review/`. The parent found the symbols distinct and readable at native size, the grey and red-cross states correctly aligned, and the template margins clean.

The package manifest is `docs/assets/006_independence_wave/signature_achievements_20261006/manifest.json`. The nine source-state PNGs, processor outputs, preparation script, triplet processing record, prompts, source masters, rejected candidates, contact sheets, and validation evidence are all retained in that owned archive directory.

## Scope and remaining work

No simplifications or blockers remain for this asset-processing task. Achievement registry, localization, `.gfx` wiring, and sprite aliases remain parent-owned and were not edited here. No commit was created.
