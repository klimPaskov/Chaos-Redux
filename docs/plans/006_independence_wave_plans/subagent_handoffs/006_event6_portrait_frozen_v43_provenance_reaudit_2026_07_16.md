# Event 006 Male HOI4 Portrait Frozen v4.3 Provenance Re-audit

**Date:** 2026-07-16

**Mode:** Independent, read-only follow-up audit

**Scope:** Frozen processor/reference provenance repair and runtime immutability

## Verdict: PASS

The frozen v4.3 provenance repair is complete and internally consistent. All 30 metadata records resolve to the retained processor with the expected hash, all ten small-portrait metadata records resolve every embedded absolute provenance path and paired hash, and the frozen input bundle is an exact 17-file reconstruction of commit `6729ad0cd74e0ed294a0b603a0eb677a0533099c`. The repair did not alter generated pixels, processed PNGs, runtime DDS files, retained DDS copies, or either protected portrait.

## Frozen v4.3 bundle and ledger

- Frozen root: `docs/assets/006_independence_wave/portrait_regeneration_male_hoi4_2026_07_16/_tooling/v4_3_frozen_inputs`
- Ledger: `docs/assets/006_independence_wave/portrait_regeneration_male_hoi4_2026_07_16/hashes/frozen_v4_3_inputs_sha256.sha256`
- Reconstruction source commit: `6729ad0cd74e0ed294a0b603a0eb677a0533099c`
- Files present: **17**
- Ledger entries: **17**
- Missing ledger paths: **0**
- Unledgered frozen files: **0**
- Current-file/ledger SHA-256 mismatches: **0**
- Current-file/source-commit blob mismatches: **0**

The retained files comprise the v4.3 processor, overlay manifest, six canonical advisor references, the canonical advisor contact sheet, both approved frame/paper source-overlay-prompt sets, and both recorded superseded generation inputs. The processor pin is:

`c300a0acc6ca91beb98d5ae62fcb6c98ad61c39bb7c271491c761295ca11b411`

## Metadata processor provenance

All **30/30** portrait metadata records were traversed independently.

- Unique `processor` path: `docs/assets/006_independence_wave/portrait_regeneration_male_hoi4_2026_07_16/_tooling/v4_3_frozen_inputs/.agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py`
- Resolved processor files: **30/30**
- `processor_sha256` values equal the v4.3 pin: **30/30**
- Resolved processor byte hashes equal the v4.3 pin: **30/30**
- `processor_version` values equal `4.3`: **30/30**
- Missing, divergent, or stale processor records: **0**

## Small-portrait embedded provenance

All **10/10** 65x67 small-portrait metadata records were recursively traversed rather than sampled.

- Absolute path fields inspected: **270** (**27 per record**)
- Missing absolute paths: **0**
- Operating-system temporary paths: **0**
- Provenance inputs outside the retained frozen bundle: **0**
- `reference_dir` mismatches from the frozen canonical advisor-reference directory: **0**
- Explicit file-path/SHA-256 pairs recomputed: **250** (**25 per record**)
- Path/hash mismatches: **0**

The paired checks cover each record's processor, raw source, overlay manifest, six manifest canonical references, frame and paper prompts, four recorded generation inputs, frame and paper source/overlay files, and six advisor-validation references. Record-specific outputs and review evidence remain in the portrait package; every external provenance dependency resolves inside `_tooling/v4_3_frozen_inputs`.

## Pixel and runtime immutability

The provenance edit was metadata/tooling-only. Independent byte and decoded-pixel comparisons found:

- Runtime DDS files checked against the existing runtime ledger: **32/32**, with **0** mismatches.
- Runtime inventory aggregate SHA-256: `4b4ec07ad24433a71eddf013c600416d89c8197ab40bbe14dbf31af207e6a26a`.
- Regenerated DDS files decoded against their processed PNGs: **30/30**, with **0** pixel mismatches.
- Saved DDS-decode evidence compared with current runtime DDS decodes: **30/30**, with **0** pixel mismatches.
- Retained second-tranche DDS copies compared byte-for-byte with runtime: **15/15**, with **0** mismatches.
- `portrait_BAY_rupprecht_of_bavaria.dds`: current and repository `HEAD` SHA-256 both `7f0af64fdf4fecd49df454d1198935bb3ce6a8f74afc1ac82f8223704eaaad2b`.
- `portrait_RHI_josef_friedrich_matthes.dds`: current and repository `HEAD` SHA-256 both `aa61cc3a12fb6670b690c7685feb9383383ce58599c9e6d6e7c14f20fab3bce2`.

These results match the pre-repair independent audit snapshot: no portrait pixels, DDS bytes, runtime inventory hashes, or protected hashes changed during provenance resolution.

## Simplifications, omissions, and blockers

None. The previously identified non-portable v4.3 processor/reference paths are closed by the retained, ledgered, source-commit-identical bundle. No fallback or substitute provenance was used.
