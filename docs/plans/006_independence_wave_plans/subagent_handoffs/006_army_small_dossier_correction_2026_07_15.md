# Event 006 army-small dossier correction handoff

> **Portrait-specific supersession (2026-07-16):** All small-card visual
> results, hashes, and acceptance evidence in this record are historical. The
> current ten commander-small dossiers are governed by the 2026-07-16
> male-HOI4 package manifest and final independent audit; custom advisor icons
> remain withdrawn.

## Result

The ten Event 006 commander `_small` runtime textures are corrected from the
invalid portrait reductions to independently composed `65x67` HOI4 dossier
cards. Stable filenames and sprite contracts were preserved. No gameplay,
`.gfx`, localisation, readiness, or scenario-preflight file was edited.

The parent visually accepted all ten individual review sheets. Automated
evidence confirms that every retained and runtime DDS is an exact one-level
legacy BGRA `65x67` texture of `17,548` bytes, has real alpha and transparent
outer corners, decodes pixel-identically to the approved PNG, and matches its
retained package DDS byte for byte.

## BRI package alignment

The Brittany package-owned small artifacts were replaced, not merely left with
a historical note:

- processed and decoded PNG dimensions: `65x67`;
- processed/decoded PNG SHA-256:
  `c3aa4f46caabc1d8dce7d509e99bf221e840f0c0d991c0a4cc1c5c24dfea091e`;
- installed and correction-package DDS SHA-256:
  `12c1a20d2cc1234895e7af557bda9baf7cddca58593527194b5edad3af058684`;
- rebuilt BRI contact-sheet SHA-256:
  `1a1ff2707281174d3bb7d58de18acac51ff3bc4302a97be1c1102b9c28700735`.

`validation_report.json` records
`bri_package_owned_small_artifacts_match_correction = true` and freezes the
three exact BRI paths it checked.

## Runtime DDS hashes

| Tag | Installed `_small.dds` SHA-256 |
|---|---|
| ACX | `25b4d20cc361cb12ec4e35250a1a749b9ad0e72268c439fa5eb0fb71fa483edf` |
| AEX | `9a6bb88447f440f397df2f8631a470826beeed62f4b27e3b9387c8e6aefde41d` |
| AFX | `59f3ec28b1c4bc38d8985a5a62bf9196012f7bb7b8716576fe041688b2151751` |
| AGX | `44b213c7570751816032f3a7187969efb54dc9b1cdc0f190302a7d4d2583cd7c` |
| AJX | `470c29fd6cc73f5b6a269969160f1f4d721f31d4197f3d070c8388765f269312` |
| BAY | `5ac39639f61af4382aed35b7bbeb324d6ca823cab044dc58038a709bf1e58eca` |
| BRI | `12c1a20d2cc1234895e7af557bda9baf7cddca58593527194b5edad3af058684` |
| RHI | `442b74a217c1d4fd19a4cef46f16afaf038ba0148c39a5b763b05dce56ef2c77` |
| SCO | `1142225bac6c2dd863b1823661fc290966d8504fe1942b148a9377f44fb78481` |
| WLS | `255e4d2f7420da9cf88552f1ed4c299a6c094e20039b9736c62cb9225d714d2e` |

## Preserved large portraits

The validator compares the ten current `156x210` commander files against their
pre-task hashes and reports all ten byte-preserved. The approved Rupprecht of
Bavaria and Josef Friedrich Matthes portraits were also independently confirmed
unchanged by the parent and were outside this correction's write set.

## Validation performed

- `python docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/_tooling/build_validation_evidence.py`
  returned `validated 10 army-small dossiers; preserved 10 large portraits`.
- `python .tools/extract_hoi4_asset_references.py --check` returned
  `validated 90 allowlisted references across 6 contact sheets`.
- Current asset manifests and GFX handoffs contain no live `50x67` claim; the
  sole remaining phrase is the correction manifest's explicit description of
  the rejected earlier reductions.
- The correction manifest contains correctly encoded `Günther von Kluge`; no
  `GÃ` mojibake is present in the correction package or canonical-reference
  documentation.

## Skills and references used

- `chaos-redux-event-assets` governed source mode, processing, review,
  conversion, manifest, and handoff requirements.
- `imagegen` was consulted for the raster workflow contract; no new ImageGen
  call was required because approved project-controlled masters and overlays
  already existed.
- Required offline Paradox wiki pages and relevant vanilla documentation were
  consulted before editing.
- Exact vanilla army-small precedents were verified through
  `common/characters/GER.txt`, `interface/_leader_portraits.gfx`,
  `interface/ideas.gfx`, and the Paulus, von Kluge, and Rommel DDS files.

## Explicit changed/new file ledger

### Canonical reference library and extractor

- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/CATALOG.md`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/README.md`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/flags/contact_sheet.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/army_small_ger_erwin_rommel.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/army_small_ger_friedrich_paulus.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/army_small_ger_gunther_von_kluge.png`
- `.tools/extract_hoi4_asset_references.py`

### Correction package

- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/_tooling/build_validation_evidence.py`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/contact_sheets/army_small_dossiers_enlarged_nearest_4x.png`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/contact_sheets/army_small_dossiers_native_1x.png`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/decoded_dds_png/portrait_ACX_cornish_coastal_commander_small.png`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/decoded_dds_png/portrait_AEX_flemish_industrial_security_commander_small.png`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/decoded_dds_png/portrait_AFX_walloon_reserve_commander_small.png`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/decoded_dds_png/portrait_AGX_friesland_coastal_commander_small.png`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/decoded_dds_png/portrait_AJX_saar_industrial_security_commissioner_small.png`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/decoded_dds_png/portrait_BAY_independence_wave_mountain_commandant_small.png`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/decoded_dds_png/portrait_BRI_independence_wave_coastal_commandant_small.png`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/decoded_dds_png/portrait_RHI_independence_wave_river_commandant_small.png`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/decoded_dds_png/portrait_SCO_independence_wave_territorial_commandant_small.png`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/decoded_dds_png/portrait_WLS_independence_wave_mountain_commandant_small.png`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/final_dds/portrait_ACX_cornish_coastal_commander_small.dds`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/final_dds/portrait_AEX_flemish_industrial_security_commander_small.dds`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/final_dds/portrait_AFX_walloon_reserve_commander_small.dds`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/final_dds/portrait_AGX_friesland_coastal_commander_small.dds`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/final_dds/portrait_AJX_saar_industrial_security_commissioner_small.dds`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/final_dds/portrait_BAY_independence_wave_mountain_commandant_small.dds`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/final_dds/portrait_BRI_independence_wave_coastal_commandant_small.dds`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/final_dds/portrait_RHI_independence_wave_river_commandant_small.dds`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/final_dds/portrait_SCO_independence_wave_territorial_commandant_small.dds`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/final_dds/portrait_WLS_independence_wave_mountain_commandant_small.dds`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/gfx_handoff.md`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/manifest.md`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/metadata/portrait_ACX_cornish_coastal_commander_small.json`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/metadata/portrait_AEX_flemish_industrial_security_commander_small.json`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/metadata/portrait_AFX_walloon_reserve_commander_small.json`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/metadata/portrait_AGX_friesland_coastal_commander_small.json`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/metadata/portrait_AJX_saar_industrial_security_commissioner_small.json`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/metadata/portrait_BAY_independence_wave_mountain_commandant_small.json`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/metadata/portrait_BRI_independence_wave_coastal_commandant_small.json`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/metadata/portrait_RHI_independence_wave_river_commandant_small.json`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/metadata/portrait_SCO_independence_wave_territorial_commandant_small.json`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/metadata/portrait_WLS_independence_wave_mountain_commandant_small.json`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/processed_png/portrait_ACX_cornish_coastal_commander_small.png`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/processed_png/portrait_AEX_flemish_industrial_security_commander_small.png`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/processed_png/portrait_AFX_walloon_reserve_commander_small.png`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/processed_png/portrait_AGX_friesland_coastal_commander_small.png`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/processed_png/portrait_AJX_saar_industrial_security_commissioner_small.png`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/processed_png/portrait_BAY_independence_wave_mountain_commandant_small.png`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/processed_png/portrait_BRI_independence_wave_coastal_commandant_small.png`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/processed_png/portrait_RHI_independence_wave_river_commandant_small.png`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/processed_png/portrait_SCO_independence_wave_territorial_commandant_small.png`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/processed_png/portrait_WLS_independence_wave_mountain_commandant_small.png`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/review_sheets/portrait_ACX_cornish_coastal_commander_small_review.png`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/review_sheets/portrait_AEX_flemish_industrial_security_commander_small_review.png`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/review_sheets/portrait_AFX_walloon_reserve_commander_small_review.png`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/review_sheets/portrait_AGX_friesland_coastal_commander_small_review.png`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/review_sheets/portrait_AJX_saar_industrial_security_commissioner_small_review.png`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/review_sheets/portrait_BAY_independence_wave_mountain_commandant_small_review.png`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/review_sheets/portrait_BRI_independence_wave_coastal_commandant_small_review.png`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/review_sheets/portrait_RHI_independence_wave_river_commandant_small_review.png`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/review_sheets/portrait_SCO_independence_wave_territorial_commandant_small_review.png`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/review_sheets/portrait_WLS_independence_wave_mountain_commandant_small_review.png`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/sha256_inventory.sha256`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/validation_report.json`
- `docs/assets/006_independence_wave/army_small_dossier_correction_2026_07_15/visual_review.md`

### Installed runtime textures

- `gfx/leaders/006_independence_wave/portrait_ACX_cornish_coastal_commander_small.dds`
- `gfx/leaders/006_independence_wave/portrait_AEX_flemish_industrial_security_commander_small.dds`
- `gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander_small.dds`
- `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_commander_small.dds`
- `gfx/leaders/006_independence_wave/portrait_AJX_saar_industrial_security_commissioner_small.dds`
- `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_mountain_commandant_small.dds`
- `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_coastal_commandant_small.dds`
- `gfx/leaders/006_independence_wave/portrait_RHI_independence_wave_river_commandant_small.dds`
- `gfx/leaders/006_independence_wave/portrait_SCO_independence_wave_territorial_commandant_small.dds`
- `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant_small.dds`

### Brittany package-owned alignment files

- `docs/assets/006_independence_wave/bri_package_2026_07_15/processed_png/portrait_BRI_independence_wave_coastal_commandant_small.png`
- `docs/assets/006_independence_wave/bri_package_2026_07_15/decoded_dds/portrait_BRI_independence_wave_coastal_commandant_small_decoded.png`
- `docs/assets/006_independence_wave/bri_package_2026_07_15/contact_sheets/006_bri_runtime_portraits_contact_sheet.png`
- `docs/assets/006_independence_wave/bri_package_2026_07_15/manifest.md`
- `docs/assets/006_independence_wave/bri_package_2026_07_15/gfx_handoff.md`

### Aligned source-of-truth documents and ledgers

- `docs/assets/006_independence_wave/manifest.md`
- `docs/assets/006_independence_wave/northern_western_europe_generated_art_manifest.md`
- `docs/assets/006_independence_wave/northern_western_europe_generated_art_gfx_handoff.md`
- `docs/assets/006_independence_wave/generated_nwe_hashes.sha256`
- `docs/assets/006_independence_wave/portrait_regeneration_2026_07_15/manifest.md`
- `docs/assets/006_independence_wave/portrait_regeneration_2026_07_15/visual_review.md`
- `docs/assets/006_independence_wave/portrait_regeneration_2026_07_15/portrait_package_hashes.sha256`
- `docs/assets/006_independence_wave/live_afx_agx_portrait_regen_2026_07_15/manifest.md`
- `docs/assets/006_independence_wave/live_afx_agx_portrait_regen_2026_07_15/hashes.sha256`
- `docs/assets/006_independence_wave/nwe_package_portraits_2026_07_15/manifest.md`
- `docs/assets/006_independence_wave/nwe_package_portraits_2026_07_15/gfx_handoff.md`
- `docs/assets/006_independence_wave/nwe_package_portraits_2026_07_15/checksums.sha256`

### Handoff

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_army_small_dossier_correction_2026_07_15.md`

Concurrent parent/user changes outside this ledger were preserved. No commit was
created, as required by the parent task.

## Simplifications, omissions, and blockers

No simplifications, fallbacks, placeholders, omitted cards, missing package
copies, or remaining blockers exist in this bounded correction. The only
intentional non-change is the stable `.gfx`/consumer contract.
