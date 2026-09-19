# Event 006 state-puzzle visual repair review — 2026-09-19

Status: `review complete; safe owner-applied repair identified; no asset/runtime bytes changed in this subagent turn`

This evidence was captured before concurrent owner-side repair activity appeared in the shared worktree. Any later owner changes to manifests, PNGs, or DDS files are outside this review and must be validated independently; the runtime hashes below are the pre-repair baseline.

Scope: ASSET-006 state-puzzle pieces for Event 006 Independence Wave. This review covers the 14 accepted runtime families (`FORM-01`, `FORM-02`, `FORM-03`, `FORM-04`, `FORM-05`, `FORM-07`, `FORM-08`, `FORM-09`, `FORM-12`, `FORM-13`, `FORM-16`, `FORM-18`, `FORM-39`, and `FORM-48`), 50 accepted state IDs, and 100 accepted unresolved/qualifying runtime sprites. Four unmanifested Form12/Form13 state-256 runtime pairs are retained and explicitly excluded from the repair scope.

## Decision

A narrow repair is safe and sufficiently specified. The accepted decisions-missions state-puzzle template requires unresolved pieces to use a grey fill with diagonal hatch and an interior outline, and qualifying pieces to use a green fill with a solid pale inner keyline and dark silhouette outline. Existing installed state-puzzle runtime families (`form_commonwealth`, `form_baltic_federation_category`, and `unite_maghreb`) visibly implement this treatment. The repair can be applied entirely inside each existing nonzero-alpha mask, so no map geometry, projection, canvas size, GUI placement, sprite name, GFX path, or GUI file needs to change.

The owner-applied target treatment is:

- unresolved: established grey base `RGB (98, 101, 108)` with alpha preserved from the current runtime, diagonal hatch `RGB (66, 69, 75)`, and a one-pixel interior light outline `RGB (151, 154, 161)`;
- qualifying: established green base `RGB (70, 148, 103)` with alpha preserved from the current runtime, a one-pixel interior dark silhouette outline `RGB (25, 56, 45)`, and an inset pale keyline `RGB (155, 216, 165)` where the existing mask has sufficient interior width.

These palette/treatment values are taken from the inspected accepted `form_commonwealth` runtime family and the repository validation template, not invented state shapes or generated art. The operation must preserve the current per-pixel alpha exactly, keep alpha zero outside the current mask, and never enlarge the tight sprite canvas. Do not modify `.tools/archive/build_formable_state_puzzle_consumer.py`; it is only evidence of the current flat-color defect and is not a safe repair mechanism for the required cues.

## Concrete wiring/provenance defect

Every manifest-referenced source and processed PNG is absent in the current worktree. There are exactly 200 missing paths: 100 `source_png` paths and 100 `processed_png` paths across the 14 manifests listed below. The 100 accepted runtime DDS files are present and decodable, but there is no original source-master or processed-PNG provenance available in this checkout. If the owner recovers review PNGs by decoding the runtime DDS, they must be labeled `recovered_runtime_dds_decode_not_original_master`; the recovered images cannot be claimed as original masters.

The missing path ledger is exact:

- `docs/formables/state_puzzles/006_form01_state_puzzle/processed/independence_wave_form01_state_121_qualifying.png`
- `docs/formables/state_puzzles/006_form01_state_puzzle/processed/independence_wave_form01_state_121_unresolved.png`
- `docs/formables/state_puzzles/006_form01_state_puzzle/processed/independence_wave_form01_state_122_qualifying.png`
- `docs/formables/state_puzzles/006_form01_state_puzzle/processed/independence_wave_form01_state_122_unresolved.png`
- `docs/formables/state_puzzles/006_form01_state_puzzle/processed/independence_wave_form01_state_133_qualifying.png`
- `docs/formables/state_puzzles/006_form01_state_puzzle/processed/independence_wave_form01_state_133_unresolved.png`
- `docs/formables/state_puzzles/006_form01_state_puzzle/processed/independence_wave_form01_state_14_qualifying.png`
- `docs/formables/state_puzzles/006_form01_state_puzzle/processed/independence_wave_form01_state_14_unresolved.png`
- `docs/formables/state_puzzles/006_form01_state_puzzle/source/independence_wave_form01_state_121_qualifying.png`
- `docs/formables/state_puzzles/006_form01_state_puzzle/source/independence_wave_form01_state_121_unresolved.png`
- `docs/formables/state_puzzles/006_form01_state_puzzle/source/independence_wave_form01_state_122_qualifying.png`
- `docs/formables/state_puzzles/006_form01_state_puzzle/source/independence_wave_form01_state_122_unresolved.png`
- `docs/formables/state_puzzles/006_form01_state_puzzle/source/independence_wave_form01_state_133_qualifying.png`
- `docs/formables/state_puzzles/006_form01_state_puzzle/source/independence_wave_form01_state_133_unresolved.png`
- `docs/formables/state_puzzles/006_form01_state_puzzle/source/independence_wave_form01_state_14_qualifying.png`
- `docs/formables/state_puzzles/006_form01_state_puzzle/source/independence_wave_form01_state_14_unresolved.png`
- `docs/formables/state_puzzles/006_form02_state_puzzle/processed/independence_wave_form02_state_100_qualifying.png`
- `docs/formables/state_puzzles/006_form02_state_puzzle/processed/independence_wave_form02_state_100_unresolved.png`
- `docs/formables/state_puzzles/006_form02_state_puzzle/processed/independence_wave_form02_state_121_qualifying.png`
- `docs/formables/state_puzzles/006_form02_state_puzzle/processed/independence_wave_form02_state_121_unresolved.png`
- `docs/formables/state_puzzles/006_form02_state_puzzle/processed/independence_wave_form02_state_133_qualifying.png`
- `docs/formables/state_puzzles/006_form02_state_puzzle/processed/independence_wave_form02_state_133_unresolved.png`
- `docs/formables/state_puzzles/006_form02_state_puzzle/processed/independence_wave_form02_state_331_qualifying.png`
- `docs/formables/state_puzzles/006_form02_state_puzzle/processed/independence_wave_form02_state_331_unresolved.png`
- `docs/formables/state_puzzles/006_form02_state_puzzle/processed/independence_wave_form02_state_337_qualifying.png`
- `docs/formables/state_puzzles/006_form02_state_puzzle/processed/independence_wave_form02_state_337_unresolved.png`
- `docs/formables/state_puzzles/006_form02_state_puzzle/source/independence_wave_form02_state_100_qualifying.png`
- `docs/formables/state_puzzles/006_form02_state_puzzle/source/independence_wave_form02_state_100_unresolved.png`
- `docs/formables/state_puzzles/006_form02_state_puzzle/source/independence_wave_form02_state_121_qualifying.png`
- `docs/formables/state_puzzles/006_form02_state_puzzle/source/independence_wave_form02_state_121_unresolved.png`
- `docs/formables/state_puzzles/006_form02_state_puzzle/source/independence_wave_form02_state_133_qualifying.png`
- `docs/formables/state_puzzles/006_form02_state_puzzle/source/independence_wave_form02_state_133_unresolved.png`
- `docs/formables/state_puzzles/006_form02_state_puzzle/source/independence_wave_form02_state_331_qualifying.png`
- `docs/formables/state_puzzles/006_form02_state_puzzle/source/independence_wave_form02_state_331_unresolved.png`
- `docs/formables/state_puzzles/006_form02_state_puzzle/source/independence_wave_form02_state_337_qualifying.png`
- `docs/formables/state_puzzles/006_form02_state_puzzle/source/independence_wave_form02_state_337_unresolved.png`
- `docs/formables/state_puzzles/006_form03_state_puzzle/processed/independence_wave_form03_state_34_qualifying.png`
- `docs/formables/state_puzzles/006_form03_state_puzzle/processed/independence_wave_form03_state_34_unresolved.png`
- `docs/formables/state_puzzles/006_form03_state_puzzle/processed/independence_wave_form03_state_36_qualifying.png`
- `docs/formables/state_puzzles/006_form03_state_puzzle/processed/independence_wave_form03_state_36_unresolved.png`
- `docs/formables/state_puzzles/006_form03_state_puzzle/processed/independence_wave_form03_state_6_qualifying.png`
- `docs/formables/state_puzzles/006_form03_state_puzzle/processed/independence_wave_form03_state_6_unresolved.png`
- `docs/formables/state_puzzles/006_form03_state_puzzle/source/independence_wave_form03_state_34_qualifying.png`
- `docs/formables/state_puzzles/006_form03_state_puzzle/source/independence_wave_form03_state_34_unresolved.png`
- `docs/formables/state_puzzles/006_form03_state_puzzle/source/independence_wave_form03_state_36_qualifying.png`
- `docs/formables/state_puzzles/006_form03_state_puzzle/source/independence_wave_form03_state_36_unresolved.png`
- `docs/formables/state_puzzles/006_form03_state_puzzle/source/independence_wave_form03_state_6_qualifying.png`
- `docs/formables/state_puzzles/006_form03_state_puzzle/source/independence_wave_form03_state_6_unresolved.png`
- `docs/formables/state_puzzles/006_form04_state_puzzle/processed/independence_wave_form04_state_42_qualifying.png`
- `docs/formables/state_puzzles/006_form04_state_puzzle/processed/independence_wave_form04_state_42_unresolved.png`
- `docs/formables/state_puzzles/006_form04_state_puzzle/processed/independence_wave_form04_state_51_qualifying.png`
- `docs/formables/state_puzzles/006_form04_state_puzzle/processed/independence_wave_form04_state_51_unresolved.png`
- `docs/formables/state_puzzles/006_form04_state_puzzle/source/independence_wave_form04_state_42_qualifying.png`
- `docs/formables/state_puzzles/006_form04_state_puzzle/source/independence_wave_form04_state_42_unresolved.png`
- `docs/formables/state_puzzles/006_form04_state_puzzle/source/independence_wave_form04_state_51_qualifying.png`
- `docs/formables/state_puzzles/006_form04_state_puzzle/source/independence_wave_form04_state_51_unresolved.png`
- `docs/formables/state_puzzles/006_form05_state_puzzle/processed/independence_wave_form05_state_114_qualifying.png`
- `docs/formables/state_puzzles/006_form05_state_puzzle/processed/independence_wave_form05_state_114_unresolved.png`
- `docs/formables/state_puzzles/006_form05_state_puzzle/processed/independence_wave_form05_state_115_qualifying.png`
- `docs/formables/state_puzzles/006_form05_state_puzzle/processed/independence_wave_form05_state_115_unresolved.png`
- `docs/formables/state_puzzles/006_form05_state_puzzle/processed/independence_wave_form05_state_1_qualifying.png`
- `docs/formables/state_puzzles/006_form05_state_puzzle/processed/independence_wave_form05_state_1_unresolved.png`
- `docs/formables/state_puzzles/006_form05_state_puzzle/source/independence_wave_form05_state_114_qualifying.png`
- `docs/formables/state_puzzles/006_form05_state_puzzle/source/independence_wave_form05_state_114_unresolved.png`
- `docs/formables/state_puzzles/006_form05_state_puzzle/source/independence_wave_form05_state_115_qualifying.png`
- `docs/formables/state_puzzles/006_form05_state_puzzle/source/independence_wave_form05_state_115_unresolved.png`
- `docs/formables/state_puzzles/006_form05_state_puzzle/source/independence_wave_form05_state_1_qualifying.png`
- `docs/formables/state_puzzles/006_form05_state_puzzle/source/independence_wave_form05_state_1_unresolved.png`
- `docs/formables/state_puzzles/006_form07_state_puzzle/processed/independence_wave_form07_state_165_qualifying.png`
- `docs/formables/state_puzzles/006_form07_state_puzzle/processed/independence_wave_form07_state_165_unresolved.png`
- `docs/formables/state_puzzles/006_form07_state_puzzle/processed/independence_wave_form07_state_171_qualifying.png`
- `docs/formables/state_puzzles/006_form07_state_puzzle/processed/independence_wave_form07_state_171_unresolved.png`
- `docs/formables/state_puzzles/006_form07_state_puzzle/processed/independence_wave_form07_state_792_qualifying.png`
- `docs/formables/state_puzzles/006_form07_state_puzzle/processed/independence_wave_form07_state_792_unresolved.png`
- `docs/formables/state_puzzles/006_form07_state_puzzle/source/independence_wave_form07_state_165_qualifying.png`
- `docs/formables/state_puzzles/006_form07_state_puzzle/source/independence_wave_form07_state_165_unresolved.png`
- `docs/formables/state_puzzles/006_form07_state_puzzle/source/independence_wave_form07_state_171_qualifying.png`
- `docs/formables/state_puzzles/006_form07_state_puzzle/source/independence_wave_form07_state_171_unresolved.png`
- `docs/formables/state_puzzles/006_form07_state_puzzle/source/independence_wave_form07_state_792_qualifying.png`
- `docs/formables/state_puzzles/006_form07_state_puzzle/source/independence_wave_form07_state_792_unresolved.png`
- `docs/formables/state_puzzles/006_form08_state_puzzle/processed/independence_wave_form08_state_82_qualifying.png`
- `docs/formables/state_puzzles/006_form08_state_puzzle/processed/independence_wave_form08_state_82_unresolved.png`
- `docs/formables/state_puzzles/006_form08_state_puzzle/processed/independence_wave_form08_state_84_qualifying.png`
- `docs/formables/state_puzzles/006_form08_state_puzzle/processed/independence_wave_form08_state_84_unresolved.png`
- `docs/formables/state_puzzles/006_form08_state_puzzle/source/independence_wave_form08_state_82_qualifying.png`
- `docs/formables/state_puzzles/006_form08_state_puzzle/source/independence_wave_form08_state_82_unresolved.png`
- `docs/formables/state_puzzles/006_form08_state_puzzle/source/independence_wave_form08_state_84_qualifying.png`
- `docs/formables/state_puzzles/006_form08_state_puzzle/source/independence_wave_form08_state_84_unresolved.png`
- `docs/formables/state_puzzles/006_form09_state_puzzle/processed/independence_wave_form09_state_104_qualifying.png`
- `docs/formables/state_puzzles/006_form09_state_puzzle/processed/independence_wave_form09_state_104_unresolved.png`
- `docs/formables/state_puzzles/006_form09_state_puzzle/processed/independence_wave_form09_state_105_qualifying.png`
- `docs/formables/state_puzzles/006_form09_state_puzzle/processed/independence_wave_form09_state_105_unresolved.png`
- `docs/formables/state_puzzles/006_form09_state_puzzle/processed/independence_wave_form09_state_106_qualifying.png`
- `docs/formables/state_puzzles/006_form09_state_puzzle/processed/independence_wave_form09_state_106_unresolved.png`
- `docs/formables/state_puzzles/006_form09_state_puzzle/processed/independence_wave_form09_state_184_qualifying.png`
- `docs/formables/state_puzzles/006_form09_state_puzzle/processed/independence_wave_form09_state_184_unresolved.png`
- `docs/formables/state_puzzles/006_form09_state_puzzle/processed/independence_wave_form09_state_185_qualifying.png`
- `docs/formables/state_puzzles/006_form09_state_puzzle/processed/independence_wave_form09_state_185_unresolved.png`
- `docs/formables/state_puzzles/006_form09_state_puzzle/processed/independence_wave_form09_state_802_qualifying.png`
- `docs/formables/state_puzzles/006_form09_state_puzzle/processed/independence_wave_form09_state_802_unresolved.png`
- `docs/formables/state_puzzles/006_form09_state_puzzle/source/independence_wave_form09_state_104_qualifying.png`
- `docs/formables/state_puzzles/006_form09_state_puzzle/source/independence_wave_form09_state_104_unresolved.png`
- `docs/formables/state_puzzles/006_form09_state_puzzle/source/independence_wave_form09_state_105_qualifying.png`
- `docs/formables/state_puzzles/006_form09_state_puzzle/source/independence_wave_form09_state_105_unresolved.png`
- `docs/formables/state_puzzles/006_form09_state_puzzle/source/independence_wave_form09_state_106_qualifying.png`
- `docs/formables/state_puzzles/006_form09_state_puzzle/source/independence_wave_form09_state_106_unresolved.png`
- `docs/formables/state_puzzles/006_form09_state_puzzle/source/independence_wave_form09_state_184_qualifying.png`
- `docs/formables/state_puzzles/006_form09_state_puzzle/source/independence_wave_form09_state_184_unresolved.png`
- `docs/formables/state_puzzles/006_form09_state_puzzle/source/independence_wave_form09_state_185_qualifying.png`
- `docs/formables/state_puzzles/006_form09_state_puzzle/source/independence_wave_form09_state_185_unresolved.png`
- `docs/formables/state_puzzles/006_form09_state_puzzle/source/independence_wave_form09_state_802_qualifying.png`
- `docs/formables/state_puzzles/006_form09_state_puzzle/source/independence_wave_form09_state_802_unresolved.png`
- `docs/formables/state_puzzles/006_form12_state_puzzle/processed/independence_wave_form12_state_249_qualifying.png`
- `docs/formables/state_puzzles/006_form12_state_puzzle/processed/independence_wave_form12_state_249_unresolved.png`
- `docs/formables/state_puzzles/006_form12_state_puzzle/processed/independence_wave_form12_state_397_qualifying.png`
- `docs/formables/state_puzzles/006_form12_state_puzzle/processed/independence_wave_form12_state_397_unresolved.png`
- `docs/formables/state_puzzles/006_form12_state_puzzle/processed/independence_wave_form12_state_399_qualifying.png`
- `docs/formables/state_puzzles/006_form12_state_puzzle/processed/independence_wave_form12_state_399_unresolved.png`
- `docs/formables/state_puzzles/006_form12_state_puzzle/processed/independence_wave_form12_state_651_qualifying.png`
- `docs/formables/state_puzzles/006_form12_state_puzzle/processed/independence_wave_form12_state_651_unresolved.png`
- `docs/formables/state_puzzles/006_form12_state_puzzle/processed/independence_wave_form12_state_833_qualifying.png`
- `docs/formables/state_puzzles/006_form12_state_puzzle/processed/independence_wave_form12_state_833_unresolved.png`
- `docs/formables/state_puzzles/006_form12_state_puzzle/source/independence_wave_form12_state_249_qualifying.png`
- `docs/formables/state_puzzles/006_form12_state_puzzle/source/independence_wave_form12_state_249_unresolved.png`
- `docs/formables/state_puzzles/006_form12_state_puzzle/source/independence_wave_form12_state_397_qualifying.png`
- `docs/formables/state_puzzles/006_form12_state_puzzle/source/independence_wave_form12_state_397_unresolved.png`
- `docs/formables/state_puzzles/006_form12_state_puzzle/source/independence_wave_form12_state_399_qualifying.png`
- `docs/formables/state_puzzles/006_form12_state_puzzle/source/independence_wave_form12_state_399_unresolved.png`
- `docs/formables/state_puzzles/006_form12_state_puzzle/source/independence_wave_form12_state_651_qualifying.png`
- `docs/formables/state_puzzles/006_form12_state_puzzle/source/independence_wave_form12_state_651_unresolved.png`
- `docs/formables/state_puzzles/006_form12_state_puzzle/source/independence_wave_form12_state_833_qualifying.png`
- `docs/formables/state_puzzles/006_form12_state_puzzle/source/independence_wave_form12_state_833_unresolved.png`
- `docs/formables/state_puzzles/006_form13_state_puzzle/processed/independence_wave_form13_state_249_qualifying.png`
- `docs/formables/state_puzzles/006_form13_state_puzzle/processed/independence_wave_form13_state_249_unresolved.png`
- `docs/formables/state_puzzles/006_form13_state_puzzle/processed/independence_wave_form13_state_397_qualifying.png`
- `docs/formables/state_puzzles/006_form13_state_puzzle/processed/independence_wave_form13_state_397_unresolved.png`
- `docs/formables/state_puzzles/006_form13_state_puzzle/processed/independence_wave_form13_state_399_qualifying.png`
- `docs/formables/state_puzzles/006_form13_state_puzzle/processed/independence_wave_form13_state_399_unresolved.png`
- `docs/formables/state_puzzles/006_form13_state_puzzle/processed/independence_wave_form13_state_651_qualifying.png`
- `docs/formables/state_puzzles/006_form13_state_puzzle/processed/independence_wave_form13_state_651_unresolved.png`
- `docs/formables/state_puzzles/006_form13_state_puzzle/processed/independence_wave_form13_state_833_qualifying.png`
- `docs/formables/state_puzzles/006_form13_state_puzzle/processed/independence_wave_form13_state_833_unresolved.png`
- `docs/formables/state_puzzles/006_form13_state_puzzle/source/independence_wave_form13_state_249_qualifying.png`
- `docs/formables/state_puzzles/006_form13_state_puzzle/source/independence_wave_form13_state_249_unresolved.png`
- `docs/formables/state_puzzles/006_form13_state_puzzle/source/independence_wave_form13_state_397_qualifying.png`
- `docs/formables/state_puzzles/006_form13_state_puzzle/source/independence_wave_form13_state_397_unresolved.png`
- `docs/formables/state_puzzles/006_form13_state_puzzle/source/independence_wave_form13_state_399_qualifying.png`
- `docs/formables/state_puzzles/006_form13_state_puzzle/source/independence_wave_form13_state_399_unresolved.png`
- `docs/formables/state_puzzles/006_form13_state_puzzle/source/independence_wave_form13_state_651_qualifying.png`
- `docs/formables/state_puzzles/006_form13_state_puzzle/source/independence_wave_form13_state_651_unresolved.png`
- `docs/formables/state_puzzles/006_form13_state_puzzle/source/independence_wave_form13_state_833_qualifying.png`
- `docs/formables/state_puzzles/006_form13_state_puzzle/source/independence_wave_form13_state_833_unresolved.png`
- `docs/formables/state_puzzles/006_form16_state_puzzle/processed/independence_wave_form16_state_229_qualifying.png`
- `docs/formables/state_puzzles/006_form16_state_puzzle/processed/independence_wave_form16_state_229_unresolved.png`
- `docs/formables/state_puzzles/006_form16_state_puzzle/processed/independence_wave_form16_state_230_qualifying.png`
- `docs/formables/state_puzzles/006_form16_state_puzzle/processed/independence_wave_form16_state_230_unresolved.png`
- `docs/formables/state_puzzles/006_form16_state_puzzle/processed/independence_wave_form16_state_231_qualifying.png`
- `docs/formables/state_puzzles/006_form16_state_puzzle/processed/independence_wave_form16_state_231_unresolved.png`
- `docs/formables/state_puzzles/006_form16_state_puzzle/source/independence_wave_form16_state_229_qualifying.png`
- `docs/formables/state_puzzles/006_form16_state_puzzle/source/independence_wave_form16_state_229_unresolved.png`
- `docs/formables/state_puzzles/006_form16_state_puzzle/source/independence_wave_form16_state_230_qualifying.png`
- `docs/formables/state_puzzles/006_form16_state_puzzle/source/independence_wave_form16_state_230_unresolved.png`
- `docs/formables/state_puzzles/006_form16_state_puzzle/source/independence_wave_form16_state_231_qualifying.png`
- `docs/formables/state_puzzles/006_form16_state_puzzle/source/independence_wave_form16_state_231_unresolved.png`
- `docs/formables/state_puzzles/006_form18_state_puzzle/processed/independence_wave_form18_state_413_qualifying.png`
- `docs/formables/state_puzzles/006_form18_state_puzzle/processed/independence_wave_form18_state_413_unresolved.png`
- `docs/formables/state_puzzles/006_form18_state_puzzle/processed/independence_wave_form18_state_421_qualifying.png`
- `docs/formables/state_puzzles/006_form18_state_puzzle/processed/independence_wave_form18_state_421_unresolved.png`
- `docs/formables/state_puzzles/006_form18_state_puzzle/processed/independence_wave_form18_state_676_qualifying.png`
- `docs/formables/state_puzzles/006_form18_state_puzzle/processed/independence_wave_form18_state_676_unresolved.png`
- `docs/formables/state_puzzles/006_form18_state_puzzle/source/independence_wave_form18_state_413_qualifying.png`
- `docs/formables/state_puzzles/006_form18_state_puzzle/source/independence_wave_form18_state_413_unresolved.png`
- `docs/formables/state_puzzles/006_form18_state_puzzle/source/independence_wave_form18_state_421_qualifying.png`
- `docs/formables/state_puzzles/006_form18_state_puzzle/source/independence_wave_form18_state_421_unresolved.png`
- `docs/formables/state_puzzles/006_form18_state_puzzle/source/independence_wave_form18_state_676_qualifying.png`
- `docs/formables/state_puzzles/006_form18_state_puzzle/source/independence_wave_form18_state_676_unresolved.png`
- `docs/formables/state_puzzles/006_form39_state_puzzle/processed/independence_wave_form39_state_523_qualifying.png`
- `docs/formables/state_puzzles/006_form39_state_puzzle/processed/independence_wave_form39_state_523_unresolved.png`
- `docs/formables/state_puzzles/006_form39_state_puzzle/processed/independence_wave_form39_state_636_qualifying.png`
- `docs/formables/state_puzzles/006_form39_state_puzzle/processed/independence_wave_form39_state_636_unresolved.png`
- `docs/formables/state_puzzles/006_form39_state_puzzle/processed/independence_wave_form39_state_669_qualifying.png`
- `docs/formables/state_puzzles/006_form39_state_puzzle/processed/independence_wave_form39_state_669_unresolved.png`
- `docs/formables/state_puzzles/006_form39_state_puzzle/source/independence_wave_form39_state_523_qualifying.png`
- `docs/formables/state_puzzles/006_form39_state_puzzle/source/independence_wave_form39_state_523_unresolved.png`
- `docs/formables/state_puzzles/006_form39_state_puzzle/source/independence_wave_form39_state_636_qualifying.png`
- `docs/formables/state_puzzles/006_form39_state_puzzle/source/independence_wave_form39_state_636_unresolved.png`
- `docs/formables/state_puzzles/006_form39_state_puzzle/source/independence_wave_form39_state_669_qualifying.png`
- `docs/formables/state_puzzles/006_form39_state_puzzle/source/independence_wave_form39_state_669_unresolved.png`
- `docs/formables/state_puzzles/006_form48_state_puzzle/processed/independence_wave_form48_state_378_qualifying.png`
- `docs/formables/state_puzzles/006_form48_state_puzzle/processed/independence_wave_form48_state_378_unresolved.png`
- `docs/formables/state_puzzles/006_form48_state_puzzle/processed/independence_wave_form48_state_629_qualifying.png`
- `docs/formables/state_puzzles/006_form48_state_puzzle/processed/independence_wave_form48_state_629_unresolved.png`
- `docs/formables/state_puzzles/006_form48_state_puzzle/processed/independence_wave_form48_state_684_qualifying.png`
- `docs/formables/state_puzzles/006_form48_state_puzzle/processed/independence_wave_form48_state_684_unresolved.png`
- `docs/formables/state_puzzles/006_form48_state_puzzle/source/independence_wave_form48_state_378_qualifying.png`
- `docs/formables/state_puzzles/006_form48_state_puzzle/source/independence_wave_form48_state_378_unresolved.png`
- `docs/formables/state_puzzles/006_form48_state_puzzle/source/independence_wave_form48_state_629_qualifying.png`
- `docs/formables/state_puzzles/006_form48_state_puzzle/source/independence_wave_form48_state_629_unresolved.png`
- `docs/formables/state_puzzles/006_form48_state_puzzle/source/independence_wave_form48_state_684_qualifying.png`
- `docs/formables/state_puzzles/006_form48_state_puzzle/source/independence_wave_form48_state_684_unresolved.png`

The manifest files containing those entries are:

- `docs/formables/state_puzzles/006_form01_state_puzzle/manifest.json`
- `docs/formables/state_puzzles/006_form02_state_puzzle/manifest.json`
- `docs/formables/state_puzzles/006_form03_state_puzzle/manifest.json`
- `docs/formables/state_puzzles/006_form04_state_puzzle/manifest.json`
- `docs/formables/state_puzzles/006_form05_state_puzzle/manifest.json`
- `docs/formables/state_puzzles/006_form07_state_puzzle/manifest.json`
- `docs/formables/state_puzzles/006_form08_state_puzzle/manifest.json`
- `docs/formables/state_puzzles/006_form09_state_puzzle/manifest.json`
- `docs/formables/state_puzzles/006_form12_state_puzzle/manifest.json`
- `docs/formables/state_puzzles/006_form13_state_puzzle/manifest.json`
- `docs/formables/state_puzzles/006_form16_state_puzzle/manifest.json`
- `docs/formables/state_puzzles/006_form18_state_puzzle/manifest.json`
- `docs/formables/state_puzzles/006_form39_state_puzzle/manifest.json`
- `docs/formables/state_puzzles/006_form48_state_puzzle/manifest.json`

## Before-state evidence

All 100 accepted runtime pieces decode as uncompressed 32-bit BGRA DDS through Pillow. Every unresolved/qualifying pair has identical nonzero-alpha geometry (`50/50` mask comparisons match; `0` geometry mismatches) and identical runtime dimensions. The unresolved runtime pixels are a single ochre color `RGB (190, 150, 40)` with alpha `230` on the shape and alpha `0` outside. The qualifying runtime pixels are a single green color `RGB (40, 180, 80)` with alpha `255` on the shape and alpha `0` outside. Therefore the current state distinction is color/opacity only; there is no border, hatch, keyline, label, or other non-color cue.

The accepted geometry provenance recorded by the prior Event 006 handoffs remains the installed-map registry hash `9777af66b45f2539296e2cc1efaf5b0a8d6146b087f31b2bc1a4c646cc0cc6c5`, map-file hash `e131d30e5dcb13d9c2a8598f820a2de0ae9828f3a24f2bddc1bcfff40f71660a`, and map revision `5070618991ee5bd9f3076ed92beecfc6a0788c12333e35fc0b648631e800002d`. This review did not regenerate or redraw geometry.

## Exact accepted pair/runtime evidence

Each row gives the manifest family/state, tight runtime dimensions, manifest canvas bbox, exact unresolved runtime path and SHA-256, exact qualifying runtime path and SHA-256, decoded alpha sets, and decoded mask hashes. Source/processed hashes are unavailable because the corresponding paths are absent; the legacy `png_sha256` values remain only in the unchanged manifests and are not verifiable in this checkout.

| Family | State | Runtime size | Manifest bbox | Unresolved runtime DDS path / SHA-256 | Qualifying runtime DDS path / SHA-256 | Alpha (unresolved / qualifying) | Mask SHA-256 (unresolved / qualifying) |
|---|---:|---:|---|---|---|---|---|
| independence_wave_form01 | 14 | 43x23 | `[206, 149, 248, 171]` | `gfx/interface/formables/state_puzzles/006_form01_state_puzzle/states/independence_wave_form01_state_14_unresolved.dds`<br>`06de9b39630883084f831d3d623087df8559882cdb08a27a5ba4e16483a16ca1` | `gfx/interface/formables/state_puzzles/006_form01_state_puzzle/states/independence_wave_form01_state_14_qualifying.dds`<br>`1226f5498b03554376e12e403d5772be60e2600f2bbf168e195e968ae57d568a` | `0, 230` / `0, 255` | `10eafc523af6e1f5f5aff5ed2e1bce84865f021245c9f8992a27998f71d7a22a` / `10eafc523af6e1f5f5aff5ed2e1bce84865f021245c9f8992a27998f71d7a22a` |
| independence_wave_form01 | 121 | 29x28 | `[204, 8, 232, 35]` | `gfx/interface/formables/state_puzzles/006_form01_state_puzzle/states/independence_wave_form01_state_121_unresolved.dds`<br>`cb9f060ac4d43f068c7c7138e888253d3c9468191bdcee3d2422e0fec5195e81` | `gfx/interface/formables/state_puzzles/006_form01_state_puzzle/states/independence_wave_form01_state_121_qualifying.dds`<br>`736273eaad6c2e0b4d0aee89fc2f0fd89314e97f208da81c27223cf827d00ce1` | `0, 230` / `0, 255` | `30ace2b7a6066bf4ef223613772ff2ae720c97ccf246900728064a0d78f21019` / `30ace2b7a6066bf4ef223613772ff2ae720c97ccf246900728064a0d78f21019` |
| independence_wave_form01 | 122 | 33x35 | `[191, 64, 223, 98]` | `gfx/interface/formables/state_puzzles/006_form01_state_puzzle/states/independence_wave_form01_state_122_unresolved.dds`<br>`b02144f1fca15b932d13b189c27aa7c5fc3039368d1aba63904320982689522d` | `gfx/interface/formables/state_puzzles/006_form01_state_puzzle/states/independence_wave_form01_state_122_qualifying.dds`<br>`8449c99961a066262a5f44a3e36c6689e376a1f79d86fed4559f6e77561aafef` | `0, 230` / `0, 255` | `520577a0402235c460d43ec17c74f35cc54c6ef1328560d7575ec48f0f58949c` / `520577a0402235c460d43ec17c74f35cc54c6ef1328560d7575ec48f0f58949c` |
| independence_wave_form01 | 133 | 31x37 | `[192, 8, 222, 44]` | `gfx/interface/formables/state_puzzles/006_form01_state_puzzle/states/independence_wave_form01_state_133_unresolved.dds`<br>`17677bb38a4c556e244ae025a745012ba1459d12013d8774633b1f1df530874b` | `gfx/interface/formables/state_puzzles/006_form01_state_puzzle/states/independence_wave_form01_state_133_qualifying.dds`<br>`56eb3e101ed027d6e0a427030d3b868ac752a37e5e667610e6291a440cfb4af5` | `0, 230` / `0, 255` | `c6d5d861fd7d41ed815b67e7d556ac631bfc620afdde76069f27b91bf69e0b33` / `c6d5d861fd7d41ed815b67e7d556ac631bfc620afdde76069f27b91bf69e0b33` |
| independence_wave_form02 | 100 | 83x40 | `[268, 14, 350, 53]` | `gfx/interface/formables/state_puzzles/006_form02_state_puzzle/states/independence_wave_form02_state_100_unresolved.dds`<br>`bc2917cf24a83a1c3a908d102e8ae45d084486cff352e52cec720901a29a6a29` | `gfx/interface/formables/state_puzzles/006_form02_state_puzzle/states/independence_wave_form02_state_100_qualifying.dds`<br>`ab05b4f62c58f26e6867991d48e0d9fb38366b832e645a5e52ebd277e4020a1d` | `0, 230` / `0, 255` | `de27b5123804c4f4aeffdfe15e9b726bcd7947895fcb51454bde65616b0fe408` / `de27b5123804c4f4aeffdfe15e9b726bcd7947895fcb51454bde65616b0fe408` |
| independence_wave_form02 | 121 | 17x17 | `[415, 143, 431, 159]` | `gfx/interface/formables/state_puzzles/006_form02_state_puzzle/states/independence_wave_form02_state_121_unresolved.dds`<br>`f12869932859a581065761debe1e15c0b17892b57a11dbe97080861d672f415a` | `gfx/interface/formables/state_puzzles/006_form02_state_puzzle/states/independence_wave_form02_state_121_qualifying.dds`<br>`51f594a0f32a899133a94bac2d29a5db54069acf42e5c6bf1de9baa36b6c2bc9` | `0, 230` / `0, 255` | `439a22bca3476a97976995748bc75132472703a81287d9451978445921aefd13` / `439a22bca3476a97976995748bc75132472703a81287d9451978445921aefd13` |
| independence_wave_form02 | 133 | 19x23 | `[408, 143, 426, 165]` | `gfx/interface/formables/state_puzzles/006_form02_state_puzzle/states/independence_wave_form02_state_133_unresolved.dds`<br>`82304826165140ec6470423f54ab0153869b8a0dd568a3c1704c65a700f1e798` | `gfx/interface/formables/state_puzzles/006_form02_state_puzzle/states/independence_wave_form02_state_133_qualifying.dds`<br>`ff2fc49f241cc7bf2fa667020897f7ec3a1e75f270e5c8b39d4a74cbe2b81183` | `0, 230` / `0, 255` | `2d58fb0fd632db484bbd4ea6ae520cb0ebadd29b2f2ffccec80ee9b259849c21` / `2d58fb0fd632db484bbd4ea6ae520cb0ebadd29b2f2ffccec80ee9b259849c21` |
| independence_wave_form02 | 331 | 51x49 | `[8, 94, 58, 142]` | `gfx/interface/formables/state_puzzles/006_form02_state_puzzle/states/independence_wave_form02_state_331_unresolved.dds`<br>`76ae91bb4ae5e298aa378991b68f4471c5be66ee5e5e3e8b6eecc727bfa74e55` | `gfx/interface/formables/state_puzzles/006_form02_state_puzzle/states/independence_wave_form02_state_331_qualifying.dds`<br>`dbf3d8a843d06a34aad772088937c95c2d68b94be0530e1c66a96e2af2860439` | `0, 230` / `0, 255` | `cab59a2ccc885bc27c28e667191e4d80dcc7f8ecd96460456fe579726c73f1eb` / `cab59a2ccc885bc27c28e667191e4d80dcc7f8ecd96460456fe579726c73f1eb` |
| independence_wave_form02 | 337 | 9x13 | `[391, 79, 399, 91]` | `gfx/interface/formables/state_puzzles/006_form02_state_puzzle/states/independence_wave_form02_state_337_unresolved.dds`<br>`c00a3f989e8b9439fa56d8ddee1ed1da37090dd70dfb3c2ceca7ebd73932fb90` | `gfx/interface/formables/state_puzzles/006_form02_state_puzzle/states/independence_wave_form02_state_337_qualifying.dds`<br>`a1deb8a7cc492d1927c1f6b4b47d488813d4d5b48c500c383430058ab72732f2` | `0, 230` / `0, 255` | `ccd34f56b721602b6b1d3c80a7b7918a422f97c767ce2db760031a4a42f86d8e` / `ccd34f56b721602b6b1d3c80a7b7918a422f97c767ce2db760031a4a42f86d8e` |
| independence_wave_form03 | 6 | 74x39 | `[139, 107, 212, 145]` | `gfx/interface/formables/state_puzzles/006_form03_state_puzzle/states/independence_wave_form03_state_6_unresolved.dds`<br>`96ee27a8d5cc5c98326618732d6ed66203ceccf2917742e06c9b66aec95913ef` | `gfx/interface/formables/state_puzzles/006_form03_state_puzzle/states/independence_wave_form03_state_6_qualifying.dds`<br>`14c4be726484c9703cf8490f0453520a98fb064d76a40690a007d397f5282469` | `0, 230` / `0, 255` | `e21d47b4ddfae9bbc7e15d479d92e06c4a3a62c58dd4ebe4250208671294e2b2` / `e21d47b4ddfae9bbc7e15d479d92e06c4a3a62c58dd4ebe4250208671294e2b2` |
| independence_wave_form03 | 34 | 74x47 | `[174, 125, 247, 171]` | `gfx/interface/formables/state_puzzles/006_form03_state_puzzle/states/independence_wave_form03_state_34_unresolved.dds`<br>`a5c4c59e20e4be2d294dd2ef987ed324d2b886b8678515a712bfb9a5a49c6107` | `gfx/interface/formables/state_puzzles/006_form03_state_puzzle/states/independence_wave_form03_state_34_qualifying.dds`<br>`a6089d7a0ec33611008ce9c10fb218d937091d5b3b03f5ebf4f999a3dbff331d` | `0, 230` / `0, 255` | `1ac8f615c5e187f8217acafd82483d13061abccf2a72e88750d0e3360deb2ac0` / `1ac8f615c5e187f8217acafd82483d13061abccf2a72e88750d0e3360deb2ac0` |
| independence_wave_form03 | 36 | 78x76 | `[223, 8, 300, 83]` | `gfx/interface/formables/state_puzzles/006_form03_state_puzzle/states/independence_wave_form03_state_36_unresolved.dds`<br>`a888fa04a638a836221078eefb34b906daf25bd7adf8a96b1891d8281949996b` | `gfx/interface/formables/state_puzzles/006_form03_state_puzzle/states/independence_wave_form03_state_36_qualifying.dds`<br>`6aa5c0a7b4b4b72d29947a86cce0a5ddd199674276cf2d7d398bb30070d9f61f` | `0, 230` / `0, 255` | `82b76f7d046516f3cda9e1451d3e834bcb351a188b3e72249dc0fb5f4a57d849` / `82b76f7d046516f3cda9e1451d3e834bcb351a188b3e72249dc0fb5f4a57d849` |
| independence_wave_form04 | 42 | 103x89 | `[171, 83, 273, 171]` | `gfx/interface/formables/state_puzzles/006_form04_state_puzzle/states/independence_wave_form04_state_42_unresolved.dds`<br>`f62157969a84156ae6f571308f5ad7f89ab72f65744c04df7756efdfcd994dc4` | `gfx/interface/formables/state_puzzles/006_form04_state_puzzle/states/independence_wave_form04_state_42_qualifying.dds`<br>`33ca369f97dd2a143e1555fb0833aa922de2dc5f40ad7ff213f4ddd1fec6afa5` | `0, 230` / `0, 255` | `501c81816cc6967e6bdd2c80d3992a8ba05da6fbd5b8cc41eb057ebad911e893` / `501c81816cc6967e6bdd2c80d3992a8ba05da6fbd5b8cc41eb057ebad911e893` |
| independence_wave_form04 | 51 | 76x89 | `[166, 8, 241, 96]` | `gfx/interface/formables/state_puzzles/006_form04_state_puzzle/states/independence_wave_form04_state_51_unresolved.dds`<br>`05de4d6cf4cbc9e5c4081b9137b150f7d283b3b049d60fc889fece2f0a0903dd` | `gfx/interface/formables/state_puzzles/006_form04_state_puzzle/states/independence_wave_form04_state_51_qualifying.dds`<br>`944a5e3a40a0c818b4930affe8bdb5b5571867db9ff151a7ed4e46e5cf4ad760` | `0, 230` / `0, 255` | `fec05f76ecdebe5cb3b3551c4da34d9e53c7b14c2bf3a97fc173b223d9220a29` / `fec05f76ecdebe5cb3b3551c4da34d9e53c7b14c2bf3a97fc173b223d9220a29` |
| independence_wave_form05 | 1 | 24x42 | `[149, 8, 172, 49]` | `gfx/interface/formables/state_puzzles/006_form05_state_puzzle/states/independence_wave_form05_state_1_unresolved.dds`<br>`7b9fad9e2ccc3e6265cd3414a63ed48b352456db262d9b526a18de3e00078d6e` | `gfx/interface/formables/state_puzzles/006_form05_state_puzzle/states/independence_wave_form05_state_1_qualifying.dds`<br>`06436d6c4a6c728e8ed523f1394348723e9fd1ad2113cd8403e15d47296e4127` | `0, 230` / `0, 255` | `8892f81b204c7e5fe19f625f5001af16c39a0fb6fd8f7a7da14647c2cc31be69` / `8892f81b204c7e5fe19f625f5001af16c39a0fb6fd8f7a7da14647c2cc31be69` |
| independence_wave_form05 | 114 | 37x64 | `[140, 52, 176, 115]` | `gfx/interface/formables/state_puzzles/006_form05_state_puzzle/states/independence_wave_form05_state_114_unresolved.dds`<br>`69dbc461a5f4af8ab6da8d1e37feae9b8a2f2af8db5c5f6cc1bc4503fdfed39c` | `gfx/interface/formables/state_puzzles/006_form05_state_puzzle/states/independence_wave_form05_state_114_qualifying.dds`<br>`746f022ce446f1a7a86cbdeb62e6a1bfda7dcaa73bbb140d790034b8b10ad871` | `0, 230` / `0, 255` | `bed4ab03b45e8077c7249b4f7ec3113bb2dc6d69f86d05558ba7000f828f68a3` / `bed4ab03b45e8077c7249b4f7ec3113bb2dc6d69f86d05558ba7000f828f68a3` |
| independence_wave_form05 | 115 | 67x41 | `[233, 131, 299, 171]` | `gfx/interface/formables/state_puzzles/006_form05_state_puzzle/states/independence_wave_form05_state_115_unresolved.dds`<br>`bb2afc484c45db646313587b6645a14e4d22ea3058c883b2682df4342baaa1f2` | `gfx/interface/formables/state_puzzles/006_form05_state_puzzle/states/independence_wave_form05_state_115_qualifying.dds`<br>`9035d647fae97124a33d3678f8ee2d6ad118d7176990094369cf3d1865f39fca` | `0, 230` / `0, 255` | `5a8430fe5fdf65b4aadbdb725b94a56b637c4f490e5c175c6ec90fcff10b0870` / `5a8430fe5fdf65b4aadbdb725b94a56b637c4f490e5c175c6ec90fcff10b0870` |
| independence_wave_form07 | 165 | 104x93 | `[328, 62, 431, 154]` | `gfx/interface/formables/state_puzzles/006_form07_state_puzzle/states/independence_wave_form07_state_165_unresolved.dds`<br>`e52af06c844a4f88d91f22ae3447a644476bab54ec9de66155fdc0e17c06480b` | `gfx/interface/formables/state_puzzles/006_form07_state_puzzle/states/independence_wave_form07_state_165_qualifying.dds`<br>`3e9e9ce1eff4b48af2d99ae3d4fb773ed4d379bb7e65daa1e0f766af26cbc88b` | `0, 230` / `0, 255` | `fb2a03460e04d9a66ae9cfea8464b0ae633f2304c1b715acab13949957f11d71` / `fb2a03460e04d9a66ae9cfea8464b0ae633f2304c1b715acab13949957f11d71` |
| independence_wave_form07 | 171 | 89x83 | `[8, 25, 96, 107]` | `gfx/interface/formables/state_puzzles/006_form07_state_puzzle/states/independence_wave_form07_state_171_unresolved.dds`<br>`6b3ce5e0d43b9ac375fd9f61c6f635503fa7bcbcf1b4287a96635ee4bcbeeee8` | `gfx/interface/formables/state_puzzles/006_form07_state_puzzle/states/independence_wave_form07_state_171_qualifying.dds`<br>`4b7fbf909eb001b9a7b4cc84d6ceff9d915cb6949ae11e9933278f4ad9508958` | `0, 230` / `0, 255` | `9ca63a4833ad6c729fb2ba16108daae1c01d9f86381d07508f1670db26ec23ec` / `9ca63a4833ad6c729fb2ba16108daae1c01d9f86381d07508f1670db26ec23ec` |
| independence_wave_form07 | 792 | 61x42 | `[206, 38, 266, 79]` | `gfx/interface/formables/state_puzzles/006_form07_state_puzzle/states/independence_wave_form07_state_792_unresolved.dds`<br>`e07e754a89f6c2ce73bceefbc1d6fc29e165479a23db43c53c82a817608123ec` | `gfx/interface/formables/state_puzzles/006_form07_state_puzzle/states/independence_wave_form07_state_792_qualifying.dds`<br>`f5d0751bb2c0684c94f2a4c4148bedfa33d50de965535a6b74a32870aad9d798` | `0, 230` / `0, 255` | `1cb716ad6c08e0e9c4f3f5c4eefd5b7641d24f2cf0c14a69894befd6cd7447d3` / `1cb716ad6c08e0e9c4f3f5c4eefd5b7641d24f2cf0c14a69894befd6cd7447d3` |
| independence_wave_form08 | 82 | 136x115 | `[47, 57, 182, 171]` | `gfx/interface/formables/state_puzzles/006_form08_state_puzzle/states/independence_wave_form08_state_82_unresolved.dds`<br>`590d73364ea14f00fdc1ce1d38711eb293c290ee8b0ec4077afbe7dcfff91698` | `gfx/interface/formables/state_puzzles/006_form08_state_puzzle/states/independence_wave_form08_state_82_qualifying.dds`<br>`56dd7f302bcfa45e695accda72514a4d4b488b8289a58719465a9eec79dadcb9` | `0, 230` / `0, 255` | `a59b3b7d9756267ce18bb07a473a6284a6c652d616519a8a7ecf6de28daf2350` / `a59b3b7d9756267ce18bb07a473a6284a6c652d616519a8a7ecf6de28daf2350` |
| independence_wave_form08 | 84 | 225x115 | `[168, 8, 392, 122]` | `gfx/interface/formables/state_puzzles/006_form08_state_puzzle/states/independence_wave_form08_state_84_unresolved.dds`<br>`c19e36fa4c4dda2cedb929dc57ea07ad43268390bf4f0f904a16c9841fff9815` | `gfx/interface/formables/state_puzzles/006_form08_state_puzzle/states/independence_wave_form08_state_84_qualifying.dds`<br>`031928453b8e1105e65e63ed1a533047df5022ccd7485390c3faef4955468f1d` | `0, 230` / `0, 255` | `65a871d7565041b56963f86c0eddeff9aaaa02d78d71a70a5341fa1632eabf9e` / `65a871d7565041b56963f86c0eddeff9aaaa02d78d71a70a5341fa1632eabf9e` |
| independence_wave_form09 | 104 | 72x44 | `[121, 8, 192, 51]` | `gfx/interface/formables/state_puzzles/006_form09_state_puzzle/states/independence_wave_form09_state_104_unresolved.dds`<br>`430adb962e7ddcfa1177cae1b2a2edb326629e7b2306256caeb57858419f8eb4` | `gfx/interface/formables/state_puzzles/006_form09_state_puzzle/states/independence_wave_form09_state_104_qualifying.dds`<br>`a4503eb4c7cb6355cce2eac70b606c108a8b4d920faa3744c9b0a96dd5a19a5f` | `0, 230` / `0, 255` | `d677b199660da550ce43f815edebdaa93d13d1a95eee7acfd75a6c96ebc5af85` / `d677b199660da550ce43f815edebdaa93d13d1a95eee7acfd75a6c96ebc5af85` |
| independence_wave_form09 | 105 | 37x38 | `[170, 46, 206, 83]` | `gfx/interface/formables/state_puzzles/006_form09_state_puzzle/states/independence_wave_form09_state_105_unresolved.dds`<br>`c9a1d23bd44f992ebebd36038ac0c6da41c956ff505275a432bc178e4563e699` | `gfx/interface/formables/state_puzzles/006_form09_state_puzzle/states/independence_wave_form09_state_105_qualifying.dds`<br>`9e7e55cc1d086659348506ed3af48a69fa556c5edfae70594b11ee695ff51126` | `0, 230` / `0, 255` | `f66022a16a4e229626cb81c759f67adeeb036d2ff7cf82ca17cc44abc2778069` / `f66022a16a4e229626cb81c759f67adeeb036d2ff7cf82ca17cc44abc2778069` |
| independence_wave_form09 | 106 | 38x31 | `[216, 72, 253, 102]` | `gfx/interface/formables/state_puzzles/006_form09_state_puzzle/states/independence_wave_form09_state_106_unresolved.dds`<br>`dc769e97d909f9f9b7b557d7c9cdbb1ffe2e7aa23abf70c1dbf2b81c22588b7d` | `gfx/interface/formables/state_puzzles/006_form09_state_puzzle/states/independence_wave_form09_state_106_qualifying.dds`<br>`b6a174b6eeb28cc916d2ff2ef2f2c0c84d1127c99250d0d0c1f331d9c3da51dd` | `0, 230` / `0, 255` | `e8545f1dbe48f4514e097036da9eadd2b3e8f65756bfe80dc2540902aee6f583` / `e8545f1dbe48f4514e097036da9eadd2b3e8f65756bfe80dc2540902aee6f583` |
| independence_wave_form09 | 184 | 52x29 | `[267, 81, 318, 109]` | `gfx/interface/formables/state_puzzles/006_form09_state_puzzle/states/independence_wave_form09_state_184_unresolved.dds`<br>`84fe4beec3010ce8f7b544101a993f8e629afff639a03be7baeaae7b65237edf` | `gfx/interface/formables/state_puzzles/006_form09_state_puzzle/states/independence_wave_form09_state_184_qualifying.dds`<br>`50d6a0ff80987edbed16b6252d598c006dc2b50d8841854e2132f6f102b53f88` | `0, 230` / `0, 255` | `3a515c0fbc4ec6eb674405d0fc11f15bc87a2146aac2a1c9c5166bef29b1e02d` / `3a515c0fbc4ec6eb674405d0fc11f15bc87a2146aac2a1c9c5166bef29b1e02d` |
| independence_wave_form09 | 185 | 48x71 | `[188, 101, 235, 171]` | `gfx/interface/formables/state_puzzles/006_form09_state_puzzle/states/independence_wave_form09_state_185_unresolved.dds`<br>`618fa0e4702b3b9ea6234c4364c09935cd42f27172d609cd23ebce6b16cff529` | `gfx/interface/formables/state_puzzles/006_form09_state_puzzle/states/independence_wave_form09_state_185_qualifying.dds`<br>`fdeccf4e558c9a7a43a709e02e3e9b682890fb633280997a5ed4daf4b2beffe0` | `0, 230` / `0, 255` | `ea6d761594cc5ef759e55660cd0ff8380c8159309bb153805ce7dc009062f787` / `ea6d761594cc5ef759e55660cd0ff8380c8159309bb153805ce7dc009062f787` |
| independence_wave_form09 | 802 | 31x25 | `[201, 54, 231, 78]` | `gfx/interface/formables/state_puzzles/006_form09_state_puzzle/states/independence_wave_form09_state_802_unresolved.dds`<br>`be9329b5fbf9efd14e49deef7d53b62f576e655de8215e75c236ebf988e6e991` | `gfx/interface/formables/state_puzzles/006_form09_state_puzzle/states/independence_wave_form09_state_802_qualifying.dds`<br>`410715bdbf89fa0ac299b97fc560beda4b7719ee71470f696ff2cb412c7af747` | `0, 230` / `0, 255` | `542af703f2cfd15e59353cbd9ea55091dce28b7fe65ca8e8e89ecf0fb42f217e` / `542af703f2cfd15e59353cbd9ea55091dce28b7fe65ca8e8e89ecf0fb42f217e` |
| independence_wave_form12 | 249 | 55x29 | `[182, 126, 236, 154]` | `gfx/interface/formables/state_puzzles/006_form12_state_puzzle/states/independence_wave_form12_state_249_unresolved.dds`<br>`0d69b93ce5d0f24680a79cfcc0c94fd4394178c2c3080685037ac2cf6c68d1e6` | `gfx/interface/formables/state_puzzles/006_form12_state_puzzle/states/independence_wave_form12_state_249_qualifying.dds`<br>`1add9dea46430f2cf42281cb2ce758f85fb6d2afb5fd7ea7d003277d251bbd3e` | `0, 230` / `0, 255` | `4845d48d32863183c97935807d83f890aedb59c050ce2d896883ee69a9873b3d` / `4845d48d32863183c97935807d83f890aedb59c050ce2d896883ee69a9873b3d` |
| independence_wave_form12 | 397 | 104x72 | `[169, 8, 272, 79]` | `gfx/interface/formables/state_puzzles/006_form12_state_puzzle/states/independence_wave_form12_state_397_unresolved.dds`<br>`e385ee4de5a767155847e7fce61c4ea7bc7057f7521b09762fd1ba040ecab7f6` | `gfx/interface/formables/state_puzzles/006_form12_state_puzzle/states/independence_wave_form12_state_397_qualifying.dds`<br>`2807ea435721616b9b64052887a7c06111f458669ff712115dde82eeef7260e3` | `0, 230` / `0, 255` | `a8cff615ebea13f3eb4e9d269ed46a90d1c016570c16dbb33119e1b1dc62f2c9` / `a8cff615ebea13f3eb4e9d269ed46a90d1c016570c16dbb33119e1b1dc62f2c9` |
| independence_wave_form12 | 399 | 34x34 | `[205, 101, 238, 134]` | `gfx/interface/formables/state_puzzles/006_form12_state_puzzle/states/independence_wave_form12_state_399_unresolved.dds`<br>`3c1ff82f6921b6c7b63d6c2b819a2d64363a1e767dfafb9d83c1333938c03e4a` | `gfx/interface/formables/state_puzzles/006_form12_state_puzzle/states/independence_wave_form12_state_399_qualifying.dds`<br>`5f4c16998091ab971de8e95e9ca5f3467f17ad50e81e397fc7e42dd324c6db70` | `0, 230` / `0, 255` | `c8d30a04a37965956041878e5c01233df27e3157ee5c99d27d5dcfd743b8e163` / `c8d30a04a37965956041878e5c01233df27e3157ee5c99d27d5dcfd743b8e163` |
| independence_wave_form12 | 651 | 49x46 | `[228, 126, 276, 171]` | `gfx/interface/formables/state_puzzles/006_form12_state_puzzle/states/independence_wave_form12_state_651_unresolved.dds`<br>`60fc87eb8439dad6e156cd11f129a6cd69004173920b4023692157c3e3fcdb14` | `gfx/interface/formables/state_puzzles/006_form12_state_puzzle/states/independence_wave_form12_state_651_qualifying.dds`<br>`192781eff2bbe33dbbb7a407b21426060594b2b9e255f3abc244da88b99419a5` | `0, 230` / `0, 255` | `d958bb206eba768f022dba39f758e1f0d928aefc30755beba1e04526e8f3f755` / `d958bb206eba768f022dba39f758e1f0d928aefc30755beba1e04526e8f3f755` |
| independence_wave_form12 | 833 | 37x24 | `[163, 113, 199, 136]` | `gfx/interface/formables/state_puzzles/006_form12_state_puzzle/states/independence_wave_form12_state_833_unresolved.dds`<br>`fd0d2f4f8e68116d59d92a29d65f2aa1d00c5403e537ac35c5a5a5eb16882e67` | `gfx/interface/formables/state_puzzles/006_form12_state_puzzle/states/independence_wave_form12_state_833_qualifying.dds`<br>`5d07b4809153740f74a8ac50e9ceedd1b756399461736b077cfa32ac08ccabdf` | `0, 230` / `0, 255` | `d9c573c9c81cf04d63946e15f48355a77f99ffcf6701b0e613d967e83d17a4d3` / `d9c573c9c81cf04d63946e15f48355a77f99ffcf6701b0e613d967e83d17a4d3` |
| independence_wave_form13 | 249 | 55x29 | `[182, 126, 236, 154]` | `gfx/interface/formables/state_puzzles/006_form13_state_puzzle/states/independence_wave_form13_state_249_unresolved.dds`<br>`0d69b93ce5d0f24680a79cfcc0c94fd4394178c2c3080685037ac2cf6c68d1e6` | `gfx/interface/formables/state_puzzles/006_form13_state_puzzle/states/independence_wave_form13_state_249_qualifying.dds`<br>`1add9dea46430f2cf42281cb2ce758f85fb6d2afb5fd7ea7d003277d251bbd3e` | `0, 230` / `0, 255` | `4845d48d32863183c97935807d83f890aedb59c050ce2d896883ee69a9873b3d` / `4845d48d32863183c97935807d83f890aedb59c050ce2d896883ee69a9873b3d` |
| independence_wave_form13 | 397 | 104x72 | `[169, 8, 272, 79]` | `gfx/interface/formables/state_puzzles/006_form13_state_puzzle/states/independence_wave_form13_state_397_unresolved.dds`<br>`e385ee4de5a767155847e7fce61c4ea7bc7057f7521b09762fd1ba040ecab7f6` | `gfx/interface/formables/state_puzzles/006_form13_state_puzzle/states/independence_wave_form13_state_397_qualifying.dds`<br>`2807ea435721616b9b64052887a7c06111f458669ff712115dde82eeef7260e3` | `0, 230` / `0, 255` | `a8cff615ebea13f3eb4e9d269ed46a90d1c016570c16dbb33119e1b1dc62f2c9` / `a8cff615ebea13f3eb4e9d269ed46a90d1c016570c16dbb33119e1b1dc62f2c9` |
| independence_wave_form13 | 399 | 34x34 | `[205, 101, 238, 134]` | `gfx/interface/formables/state_puzzles/006_form13_state_puzzle/states/independence_wave_form13_state_399_unresolved.dds`<br>`3c1ff82f6921b6c7b63d6c2b819a2d64363a1e767dfafb9d83c1333938c03e4a` | `gfx/interface/formables/state_puzzles/006_form13_state_puzzle/states/independence_wave_form13_state_399_qualifying.dds`<br>`5f4c16998091ab971de8e95e9ca5f3467f17ad50e81e397fc7e42dd324c6db70` | `0, 230` / `0, 255` | `c8d30a04a37965956041878e5c01233df27e3157ee5c99d27d5dcfd743b8e163` / `c8d30a04a37965956041878e5c01233df27e3157ee5c99d27d5dcfd743b8e163` |
| independence_wave_form13 | 651 | 49x46 | `[228, 126, 276, 171]` | `gfx/interface/formables/state_puzzles/006_form13_state_puzzle/states/independence_wave_form13_state_651_unresolved.dds`<br>`60fc87eb8439dad6e156cd11f129a6cd69004173920b4023692157c3e3fcdb14` | `gfx/interface/formables/state_puzzles/006_form13_state_puzzle/states/independence_wave_form13_state_651_qualifying.dds`<br>`192781eff2bbe33dbbb7a407b21426060594b2b9e255f3abc244da88b99419a5` | `0, 230` / `0, 255` | `d958bb206eba768f022dba39f758e1f0d928aefc30755beba1e04526e8f3f755` / `d958bb206eba768f022dba39f758e1f0d928aefc30755beba1e04526e8f3f755` |
| independence_wave_form13 | 833 | 37x24 | `[163, 113, 199, 136]` | `gfx/interface/formables/state_puzzles/006_form13_state_puzzle/states/independence_wave_form13_state_833_unresolved.dds`<br>`fd0d2f4f8e68116d59d92a29d65f2aa1d00c5403e537ac35c5a5a5eb16882e67` | `gfx/interface/formables/state_puzzles/006_form13_state_puzzle/states/independence_wave_form13_state_833_qualifying.dds`<br>`5d07b4809153740f74a8ac50e9ceedd1b756399461736b077cfa32ac08ccabdf` | `0, 230` / `0, 255` | `d9c573c9c81cf04d63946e15f48355a77f99ffcf6701b0e613d967e83d17a4d3` / `d9c573c9c81cf04d63946e15f48355a77f99ffcf6701b0e613d967e83d17a4d3` |
| independence_wave_form16 | 229 | 149x127 | `[205, 45, 353, 171]` | `gfx/interface/formables/state_puzzles/006_form16_state_puzzle/states/independence_wave_form16_state_229_unresolved.dds`<br>`859c3492fc65c948ac2d4066e0c7af5e36a92ff6a93e2bade31a802ad3ea9ba4` | `gfx/interface/formables/state_puzzles/006_form16_state_puzzle/states/independence_wave_form16_state_229_qualifying.dds`<br>`99bc68cb1e4f2c731e349555fb8cf999038316997979fbd2734185651d455f3a` | `0, 230` / `0, 255` | `89a84d699d654d426470789684cd863516875754fc8fe28c44cbcf63151f01ae` / `89a84d699d654d426470789684cd863516875754fc8fe28c44cbcf63151f01ae` |
| independence_wave_form16 | 230 | 106x93 | `[135, 62, 240, 154]` | `gfx/interface/formables/state_puzzles/006_form16_state_puzzle/states/independence_wave_form16_state_230_unresolved.dds`<br>`b647b09fe95605d84c3b0d374e34f75a68eabfebe58eade8e13677154925c597` | `gfx/interface/formables/state_puzzles/006_form16_state_puzzle/states/independence_wave_form16_state_230_qualifying.dds`<br>`cd2c3dff53758e688c1ee5c96462d25a758d76e9b15295eefb413a310110f6cb` | `0, 230` / `0, 255` | `af466c0e051cddf8b6b8d376efcab9cf764d0f7385c49eb5f90f89b891ec38ba` / `af466c0e051cddf8b6b8d376efcab9cf764d0f7385c49eb5f90f89b891ec38ba` |
| independence_wave_form16 | 231 | 157x69 | `[86, 8, 242, 76]` | `gfx/interface/formables/state_puzzles/006_form16_state_puzzle/states/independence_wave_form16_state_231_unresolved.dds`<br>`1bd4878e02be4d197379099b209683fd582ed6765328f55fb866cb9ffd860c9d` | `gfx/interface/formables/state_puzzles/006_form16_state_puzzle/states/independence_wave_form16_state_231_qualifying.dds`<br>`f352807627d202dfd7b4bfedd24982f74f41a6588578fa4854e35da39762b075` | `0, 230` / `0, 255` | `dd42630a6179d6e5fb226192028fc7aba5c44bb3b2560fc5263c285e2b4fffe0` / `dd42630a6179d6e5fb226192028fc7aba5c44bb3b2560fc5263c285e2b4fffe0` |
| independence_wave_form18 | 413 | 80x70 | `[241, 102, 320, 171]` | `gfx/interface/formables/state_puzzles/006_form18_state_puzzle/states/independence_wave_form18_state_413_unresolved.dds`<br>`34cc226fdce041e2d149a6b6a9582ddd66bb30472cf518e7cc043bf3f4f3531d` | `gfx/interface/formables/state_puzzles/006_form18_state_puzzle/states/independence_wave_form18_state_413_qualifying.dds`<br>`8bddd8e917b4953b87b25af4c5969c4a90f493d5cf0786817dc9e312b4b91dd4` | `0, 230` / `0, 255` | `0168b95b95a976f58ec6a969ffffa34f676f59ba1dd7338030bf3b31b886130b` / `0168b95b95a976f58ec6a969ffffa34f676f59ba1dd7338030bf3b31b886130b` |
| independence_wave_form18 | 421 | 55x56 | `[209, 76, 263, 131]` | `gfx/interface/formables/state_puzzles/006_form18_state_puzzle/states/independence_wave_form18_state_421_unresolved.dds`<br>`bf42c1fb211a96fb9d98de7abe8a680354ab595326881fe593a9bc56cfb75a19` | `gfx/interface/formables/state_puzzles/006_form18_state_puzzle/states/independence_wave_form18_state_421_qualifying.dds`<br>`c05a12542d9178c6799e7d137573798a603d5ea49308807c765a0aa8452e40a7` | `0, 230` / `0, 255` | `c566a45d65d6e57a24de8f8e2e64e99cc47989be78d185ca17f9f720d99a84eb` / `c566a45d65d6e57a24de8f8e2e64e99cc47989be78d185ca17f9f720d99a84eb` |
| independence_wave_form18 | 676 | 97x81 | `[119, 8, 215, 88]` | `gfx/interface/formables/state_puzzles/006_form18_state_puzzle/states/independence_wave_form18_state_676_unresolved.dds`<br>`2c17e0ed24d48b85f060ee2d8561d9973627ce9c62f66267838920301516efa2` | `gfx/interface/formables/state_puzzles/006_form18_state_puzzle/states/independence_wave_form18_state_676_qualifying.dds`<br>`8f5151cf1b90ace76d3d4ab5fb6828e43c90768302e6bbaf60862d5f9910c312` | `0, 230` / `0, 255` | `c9ea5e7168c124d33114d861567209379abc351dde342ef0e168d6ad2285b564` / `c9ea5e7168c124d33114d861567209379abc351dde342ef0e168d6ad2285b564` |
| independence_wave_form39 | 523 | 88x35 | `[104, 68, 191, 102]` | `gfx/interface/formables/state_puzzles/006_form39_state_puzzle/states/independence_wave_form39_state_523_unresolved.dds`<br>`ae89671b89200c67535a75d6ecd909b6bffed44d91bac0c2567c906d8b2a45f7` | `gfx/interface/formables/state_puzzles/006_form39_state_puzzle/states/independence_wave_form39_state_523_qualifying.dds`<br>`dd5952f263f9342c796f8603fab7e77c63e41fbd4e6d2e50c62c98f967560a8c` | `0, 230` / `0, 255` | `f4cfd367b46bc26b963d75d6e08e961ffeb24bff9479ca365e3bd9e92c33d6b2` / `f4cfd367b46bc26b963d75d6e08e961ffeb24bff9479ca365e3bd9e92c33d6b2` |
| independence_wave_form39 | 636 | 26x19 | `[406, 150, 431, 168]` | `gfx/interface/formables/state_puzzles/006_form39_state_puzzle/states/independence_wave_form39_state_636_unresolved.dds`<br>`a6b3b36a994798dd1c084b1d936e379b8e7e79ceca139f2c979bc30ba6dab14b` | `gfx/interface/formables/state_puzzles/006_form39_state_puzzle/states/independence_wave_form39_state_636_qualifying.dds`<br>`baeca1527d22cca680d9eb55632327cab761885429fbd840c57bfabd73454822` | `0, 230` / `0, 255` | `be389a0f5f1ba240186e9b54045b5c98985c5050ec4f2d2b59a3b32bc9afbe1a` / `be389a0f5f1ba240186e9b54045b5c98985c5050ec4f2d2b59a3b32bc9afbe1a` |
| independence_wave_form39 | 669 | 98x42 | `[8, 11, 105, 52]` | `gfx/interface/formables/state_puzzles/006_form39_state_puzzle/states/independence_wave_form39_state_669_unresolved.dds`<br>`8a42a81920ea2d8ba9ac68eb49f80734e028cfba4980f16fe0b58664b6c5793c` | `gfx/interface/formables/state_puzzles/006_form39_state_puzzle/states/independence_wave_form39_state_669_qualifying.dds`<br>`d8443d38105a32865ecb0eccc7de7f1ab70f99e943531ade39f366fe4b3b02a4` | `0, 230` / `0, 255` | `a680088362c78ed7afc45c44b45266cf13af8f00ccf0040badaf27bd69f3b700` / `a680088362c78ed7afc45c44b45266cf13af8f00ccf0040badaf27bd69f3b700` |
| independence_wave_form48 | 378 | 31x34 | `[352, 8, 382, 41]` | `gfx/interface/formables/state_puzzles/006_form48_state_puzzle/states/independence_wave_form48_state_378_unresolved.dds`<br>`3d94fda61092116b9a36fdacb9d7dcd59b4c0707753fa12a5c79fbe03d3f41b1` | `gfx/interface/formables/state_puzzles/006_form48_state_puzzle/states/independence_wave_form48_state_378_qualifying.dds`<br>`504884f03bd831f2c0320adf9884d1cb54cfecdf932196a3697895e5e18a2adc` | `0, 230` / `0, 255` | `19821fb6e4c5e0f37a00a3811ec41437bd4cca7006b2d5eef63008ba248c03de` / `19821fb6e4c5e0f37a00a3811ec41437bd4cca7006b2d5eef63008ba248c03de` |
| independence_wave_form48 | 629 | 20x13 | `[253, 110, 272, 122]` | `gfx/interface/formables/state_puzzles/006_form48_state_puzzle/states/independence_wave_form48_state_629_unresolved.dds`<br>`fe82564f9ef516a394b3c1e62bf463f7b6316aae159e47416d1fb76fbe1094e3` | `gfx/interface/formables/state_puzzles/006_form48_state_puzzle/states/independence_wave_form48_state_629_qualifying.dds`<br>`a86afbbc5fb008ab5bc0749153a8d97d4d99ebaee88af6d67c754e7935e9906b` | `0, 230` / `0, 255` | `7ac2ef55a5c97bd91de00cd9f6d93dea334ea4a8f72e1ad2f2645f09bce5fc86` / `7ac2ef55a5c97bd91de00cd9f6d93dea334ea4a8f72e1ad2f2645f09bce5fc86` |
| independence_wave_form48 | 684 | 78x18 | `[57, 154, 134, 171]` | `gfx/interface/formables/state_puzzles/006_form48_state_puzzle/states/independence_wave_form48_state_684_unresolved.dds`<br>`128a6edb8d5e40cb416a381710e397dd38ecf10aa6d45b8cb6ef71bf72db87a9` | `gfx/interface/formables/state_puzzles/006_form48_state_puzzle/states/independence_wave_form48_state_684_qualifying.dds`<br>`f5b4ef36150d13d15bd605b3072552667ef18035b7177db813183c6f06d87f5f` | `0, 230` / `0, 255` | `4b3a0c876a5dfa8d16ea36149d3bff153c40c073516f60f2e1d9a0d1efc267bf` / `4b3a0c876a5dfa8d16ea36149d3bff153c40c073516f60f2e1d9a0d1efc267bf` |

The exact legacy manifest `png_sha256` values are present in each unchanged asset entry, but no source or processed file exists to validate them. The current runtime SHA-256 values above are the pre-repair values that the owner must record before replacing DDS bytes and then update in the manifest/handoff after conversion.

## Orphan runtime files deliberately excluded

These four files are present under the Event 006 runtime roots but are not referenced by the accepted manifests or current Event 006 GFX/GUI wiring. They are retained and must not be deleted or silently folded into the repair:

| Runtime DDS path | Size | SHA-256 | Alpha values | Mask SHA-256 |
|---|---:|---|---|---|
| `gfx/interface/formables/state_puzzles/006_form12_state_puzzle/states/independence_wave_form12_state_256_qualifying.dds` | 21x22 | `771d4b633bc4a3c47519a6d9c68199f89a259946e36fcd7c08052cabf1b653c4` | `0, 255` | `4ebc241f0697bb5704a38510d10497c07111e5998e1653e14d1827631ab1094a` |
| `gfx/interface/formables/state_puzzles/006_form12_state_puzzle/states/independence_wave_form12_state_256_unresolved.dds` | 21x22 | `4fdc83caabb2d8350c1ea34196afa1f87a23d57c3e697566977d983ec551f5cb` | `0, 230` | `4ebc241f0697bb5704a38510d10497c07111e5998e1653e14d1827631ab1094a` |
| `gfx/interface/formables/state_puzzles/006_form13_state_puzzle/states/independence_wave_form13_state_256_qualifying.dds` | 21x22 | `771d4b633bc4a3c47519a6d9c68199f89a259946e36fcd7c08052cabf1b653c4` | `0, 255` | `4ebc241f0697bb5704a38510d10497c07111e5998e1653e14d1827631ab1094a` |
| `gfx/interface/formables/state_puzzles/006_form13_state_puzzle/states/independence_wave_form13_state_256_unresolved.dds` | 21x22 | `4fdc83caabb2d8350c1ea34196afa1f87a23d57c3e697566977d983ec551f5cb` | `0, 230` | `4ebc241f0697bb5704a38510d10497c07111e5998e1653e14d1827631ab1094a` |

## Validation performed

- Read `AGENTS.md`, the complete `chaos-redux-event-assets` skill, the relevant `chaos-redux-decisions-missions` state-puzzle guidance, the accepted Event 006 specifications, and the two prior Event 006 visual/audit handoffs.
- Consulted the required offline Paradox wiki pages and the installed vanilla documentation relevant to interface/sprite and state-puzzle consumer behavior.
- Inspected the one canonical vanilla-reference root required by the asset skill. It has no dedicated state-puzzle reference family; its decision-category picture contact sheet was inspected as a generic UI reference only. No reference art was copied.
- Inspected the current Event 006 runtime DDS pieces at native and enlarged scale and compared them against the established installed `form_commonwealth`, `form_baltic_federation_category`, and `unite_maghreb` state-puzzle runtime family at native and enlarged scale.
- Decoded all 104 Event 006 runtime DDS files (100 accepted pieces plus four retained orphans), verified strict uncompressed BGRA DDS headers and exact payload lengths, runtime dimensions, decoded alpha values, nonzero masks, and SHA-256 evidence, and compared all 50 accepted unresolved/qualifying masks.
- Audited all 200 manifest-referenced source/processed paths and confirmed every one is missing in this worktree.
- Read-only inspected `interface/chaosx_formable_state_puzzles.gfx` and `interface/chaosx_formable_state_puzzle_group_independence_wave_formables.gui`; no GFX or GUI bytes were changed.
- No ImageGen call was made because the safe repair is a deterministic mask-preserving treatment of existing installed geometry, not new art.

## Skipped validation and remaining risks

MCP map/GUI inspection, live-game rendering, and in-game validation were skipped in this bounded asset review. The owner must run the repository conversion tool on recovered source/processed PNGs, verify strict DDS decode and exact post-conversion dimensions, compare post-repair alpha/mask hashes against the pre-repair values above, inspect native-size small pieces, and perform the required parent-side MCP/live validation where available. No live-game completion claim is made here.

The principal remaining risk is provenance: runtime-decoded PNGs preserve the installed geometry and current alpha but are recovered runtime views, not original masters. A later owner patch must preserve that distinction in the manifest and handoff, must not invent new state borders or projective geometry, must not change the archived generator as a shortcut, and must leave the four orphan runtime pairs untouched.

## Review-snapshot manifest hash evidence

At the review snapshot, the following existing `manifest_sha256` values were not recomputed because this review made no manifest edits. They are recorded as the pre-repair baseline; concurrent owner-side manifest updates may have changed the current values and are outside this review:

- `docs/formables/state_puzzles/006_form01_state_puzzle/manifest.json`: `325c794c9b2d66deffbeeae47bbd062c3f0dfd9de1157f105ece8f88f04a747c` (unchanged; no manifest bytes were edited by this review)
- `docs/formables/state_puzzles/006_form02_state_puzzle/manifest.json`: `820ac595eadcdbce7e23712a2ceb689006915cf823cc83e9a398af9267da474f` (unchanged; no manifest bytes were edited by this review)
- `docs/formables/state_puzzles/006_form03_state_puzzle/manifest.json`: `4c3daf764346de2894722072593ccc3fc6b512350128930f63e729c0e9fc9700` (unchanged; no manifest bytes were edited by this review)
- `docs/formables/state_puzzles/006_form04_state_puzzle/manifest.json`: `5a0f891330d6be46e8833b17763af284f3e094673acce05c206c3a433661a452` (unchanged; no manifest bytes were edited by this review)
- `docs/formables/state_puzzles/006_form05_state_puzzle/manifest.json`: `780204c04a9f212f93f6f8b516023584ff8fe953403322411eff28e4969e3188` (unchanged; no manifest bytes were edited by this review)
- `docs/formables/state_puzzles/006_form07_state_puzzle/manifest.json`: `afc60c1e6c93fcf59694cb4b9ae62b6c60e8b113743e102baf8315c78ae6fb01` (unchanged; no manifest bytes were edited by this review)
- `docs/formables/state_puzzles/006_form08_state_puzzle/manifest.json`: `06b47db539381f9f8e8b199ff972a0bc3ccfb37ef66ad981a0f9e4caa8dda0f3` (unchanged; no manifest bytes were edited by this review)
- `docs/formables/state_puzzles/006_form09_state_puzzle/manifest.json`: `0bbb01a4a0ec12850392f3e12ea0fca75e1163f39a5b481a7576b397cc864018` (unchanged; no manifest bytes were edited by this review)
- `docs/formables/state_puzzles/006_form12_state_puzzle/manifest.json`: `1a83f62b5e09d0c7f3343fb778966c13bb20f9b03fd8d43e4c70bb1e68e9a8fd` (unchanged; no manifest bytes were edited by this review)
- `docs/formables/state_puzzles/006_form13_state_puzzle/manifest.json`: `66ea20336c527ebcb0a4b59b5192526b52b3177a47e3caf3bd6ce22240391107` (unchanged; no manifest bytes were edited by this review)
- `docs/formables/state_puzzles/006_form16_state_puzzle/manifest.json`: `ed6dbfc9f68da4ce36fa5383d86d6314e3bdb150da2ec1517bd9367124fc0f45` (unchanged; no manifest bytes were edited by this review)
- `docs/formables/state_puzzles/006_form18_state_puzzle/manifest.json`: `e3a85009a7fe4010b639a6a788f6a9148728574e43e57850785dc88bd263c40d` (unchanged; no manifest bytes were edited by this review)
- `docs/formables/state_puzzles/006_form39_state_puzzle/manifest.json`: `4c9c2e56225c3ca99f4756058cdb19e6405547d42541bb34f9181148e8b55bce` (unchanged; no manifest bytes were edited by this review)
- `docs/formables/state_puzzles/006_form48_state_puzzle/manifest.json`: `f02fe60ae6373bdef12ad284eb3df6459cd06e7b1993b94927bb98892f971c84` (unchanged; no manifest bytes were edited by this review)

This review changed no gameplay, localisation, event, focus, decision, country, history, AI, spreadsheet, GFX, GUI, or archived-generator files. This handoff is not a whole-event completion claim.
