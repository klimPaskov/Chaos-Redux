# Event 006 army-small dossier correction manifest

## Purpose and authority

This package is the current source of truth for the ten Event 006 commander
`_small` textures listed below. Each texture is an independently composed
`65x67` HOI4 dossier card with transparent outer corners. It replaces the
earlier `50x67` reductions while preserving every stable runtime filename and
sprite contract.

The corresponding ten `156x210` commander portraits were read only. Their
pre-task SHA-256 values are embedded in `_tooling/build_validation_evidence.py`
and match their post-task values in `validation_report.json`.

## Source and production record

No additional portrait generation was needed. Nine cards use the approved
fictional commander masters in
`../portrait_regeneration_2026_07_15/source_png/`; the Brittany card uses the
approved Jodoc Tanet master in
`../source_png/generated_nwe/registered_command_portraits/`.

Every card was produced with `.tools/process_hoi4_portrait.py advisor`, an
explicit source crop, `--source-kind fictional`, the canonical advisor
reference directory, and these approved project-controlled overlays:

- `.agents/skills/chaos-redux-event-assets/assets/advisor_dossier_overlays/advisor_frame_overlay.png`
- `.agents/skills/chaos-redux-event-assets/assets/advisor_dossier_overlays/advisor_paper_overlay.png`

The complete processor command, source hash, crop, overlay hashes, output
hashes, and review status for each card are frozen in `metadata/`.

## Canonical vanilla references

The cards were compared with three exact vanilla army-small dossier textures,
all `65x67`:

| Reference | Vanilla texture | Vanilla character/GFX evidence | Frozen project reference |
|---|---|---|---|
| Friedrich Paulus | `gfx/interface/ideas/idea_GER_friedrich_paulus.dds` | `common/characters/GER.txt`; `interface/_leader_portraits.gfx` | `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/army_small_ger_friedrich_paulus.png` |
| Günther von Kluge | `gfx/interface/ideas/idea_GER_gunther_von_kluge.dds` | `common/characters/GER.txt`; `interface/_leader_portraits.gfx` | `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/army_small_ger_gunther_von_kluge.png` |
| Erwin Rommel | `gfx/interface/ideas/idea_erwin_rommel.dds` | `common/characters/GER.txt`; `interface/ideas.gfx` | `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/army_small_ger_erwin_rommel.png` |

## Corrected asset inventory

Each DDS is a one-level legacy uncompressed `65x67` BGRA texture with real
alpha, transparent outer corners, and exact length `17,548` bytes.

| Tag | Runtime stem | Explicit source crop | Final DDS SHA-256 |
|---|---|---:|---|
| ACX | `portrait_ACX_cornish_coastal_commander_small` | `[200, 20, 1020, 1028]` | `25b4d20cc361cb12ec4e35250a1a749b9ad0e72268c439fa5eb0fb71fa483edf` |
| AEX | `portrait_AEX_flemish_industrial_security_commander_small` | `[200, 40, 960, 974]` | `9a6bb88447f440f397df2f8631a470826beeed62f4b27e3b9387c8e6aefde41d` |
| AFX | `portrait_AFX_walloon_reserve_commander_small` | `[270, 30, 1030, 964]` | `59f3ec28b1c4bc38d8985a5a62bf9196012f7bb7b8716576fe041688b2151751` |
| AGX | `portrait_AGX_friesland_coastal_commander_small` | `[170, 35, 1010, 1067]` | `44b213c7570751816032f3a7187969efb54dc9b1cdc0f190302a7d4d2583cd7c` |
| AJX | `portrait_AJX_saar_industrial_security_commissioner_small` | `[200, 40, 1000, 1023]` | `470c29fd6cc73f5b6a269969160f1f4d721f31d4197f3d070c8388765f269312` |
| BAY | `portrait_BAY_independence_wave_mountain_commandant_small` | `[150, 30, 990, 1062]` | `5ac39639f61af4382aed35b7bbeb324d6ca823cab044dc58038a709bf1e58eca` |
| BRI | `portrait_BRI_independence_wave_coastal_commandant_small` | `[240, 80, 940, 940]` | `12c1a20d2cc1234895e7af557bda9baf7cddca58593527194b5edad3af058684` |
| RHI | `portrait_RHI_independence_wave_river_commandant_small` | `[220, 50, 1020, 1033]` | `442b74a217c1d4fd19a4cef46f16afaf038ba0148c39a5b763b05dce56ef2c77` |
| SCO | `portrait_SCO_independence_wave_territorial_commandant_small` | `[230, 35, 1030, 1018]` | `1142225bac6c2dd863b1823661fc290966d8504fe1942b148a9377f44fb78481` |
| WLS | `portrait_WLS_independence_wave_mountain_commandant_small` | `[220, 35, 1020, 1018]` | `255e4d2f7420da9cf88552f1ed4c299a6c094e20039b9736c62cb9225d714d2e` |

For every row:

- processed PNG: `processed_png/<stem>.png`;
- retained final DDS: `final_dds/<stem>.dds`;
- decoded final DDS: `decoded_dds_png/<stem>.png`;
- installed texture: `gfx/leaders/006_independence_wave/<stem>.dds`;
- individual comparison: `review_sheets/<stem>_review.png`.

The Brittany package-owned processed and decoded small PNGs were also replaced
with the accepted `65x67` result, and its decoded-runtime contact sheet was
rebuilt. The BRI manifest and GFX handoff point to the same installed hash.

## Review and validation evidence

- `contact_sheets/army_small_dossiers_native_1x.png` compares all ten cards at
  native size with Paulus, von Kluge, and Rommel.
- `contact_sheets/army_small_dossiers_enlarged_nearest_4x.png` repeats the
  comparison at nearest-neighbour 4x scale.
- `validation_report.json` records DDS headers, dimensions, masks, byte length,
  alpha extrema, corner alpha, transparent-pixel counts, decoded-pixel equality,
  package/runtime hash equality, and the pre/post large-portrait hash guard.
- `sha256_inventory.sha256` inventories the complete correction package and its
  referenced sources, tools, overlays, vanilla comparisons, runtime textures,
  and guarded large portraits.

## Integration boundary

Texture paths and sprite names did not change. No gameplay, `.gfx`,
localisation, readiness, or scenario-preflight file was edited by this
correction. ACX and AEX remain portrait-pool assets unless their existing
package owners register them separately.

## Simplifications, omissions, and blockers

No simplification, placeholder, fallback, transform-only substitute, or
identity reuse was used. There are no asset-production blockers in this
correction package.
