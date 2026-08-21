# `undead_zombies` bespoke counter package

Status: `complete` after parent visual review and runtime promotion.

Unit identity: upright skeletal undead infantry figure with exposed skull profile, rigid shoulders, and a tattered long coat.

## Final DDS deliverables

| Surface | Package DDS | Runtime destination (not copied by this subagent) | Existing sprite | Canvas | Frames |
| --- | --- | --- | --- | ---: | ---: |
| Large division counter | `large/unit_undead_zombies_icon.dds` | `gfx/interface/counters/divisions_large/unit_undead_zombies_icon.dds` | `GFX_unit_undead_zombies_icon_medium` | 152×42 | 2 |
| Small on-map counter | `small/onmap_unit_undead_zombies_icon.dds` | `gfx/interface/counters/divisions_small/onmap_unit_undead_zombies_icon.dds` | `GFX_unit_undead_zombies_icon_medium_white` | 60×12 | 2 |

Frame order: frame 0 is the normal state; frame 1 is the pale sparse alternate state. Each sheet is two native frames side by side.

## Source and processing evidence

- Source PNGs: `source/large/` and `source/small/`.
- Alpha-separated PNGs: `alpha/large/` and `alpha/small/`.
- Exact target-size processed frames and sheets: `processed/large/` and `processed/small/`.
- DDS decoder round-trip previews: `roundtrip/large/` and `roundtrip/small/`.
- Contact sheet: `contact_sheet.png`.
- Processing metrics: `processing_metrics.json`.
- Validation evidence: `validation.json`.
- SHA-256 list: `sha256sums_artifacts.txt`.
- Shared vanilla/reference evidence: `../counter_evidence/`.

Palette: processed opaque pixels are sampled from the corresponding installed vanilla infantry frame palette. No arbitrary green was introduced.

## Artifact SHA-256

| Relative file | SHA-256 |
| --- | --- |
| `alpha/large/undead_zombies_frame_00_alpha.png` | `e7ffd32b2b78ae840aabb86b2b99fe5352f20f40b4ef5526b95db556586f3293` |
| `alpha/large/undead_zombies_frame_00_alpha_v2.png` | `4f2847dbe7f8e56ecc1bf4517297b33223d1bb71848c0a59db2c6d4ba9a67f6d` |
| `alpha/large/undead_zombies_frame_01_alpha.png` | `b2f68def33d201ca303112ec422e1892e745eb12111f3266dfd302b87d4362c5` |
| `alpha/small/undead_zombies_frame_00_alpha.png` | `12dbe1dd2df5e3e18f1ba09f74db091f6bc926d4d79ca54047ee49b7d0ec4c45` |
| `alpha/small/undead_zombies_frame_00_alpha_v2.png` | `b0aaef79e08c7604f3aff337efde670d7c6bdbc5ec94c7b19cb668598027738b` |
| `alpha/small/undead_zombies_frame_01_alpha.png` | `7227499220daa159dfe7f04d06e5bab6fef5424fbcff30e8a0385252052c6ea4` |
| `contact_sheet.png` | `e6e46627e69b86010ef08c6ec70973408184d4db258fff9ef6b861da02c83342` |
| `large/unit_undead_zombies_icon.dds` | `b5b07ca200e9fbaa8e22e4f0794dcc1de3ece90906f53e23d10b4f2ca54127db` |
| `processed/large/undead_zombies_frame_00.png` | `b4575855a30c83253813be4500da2f3eceea2ce15c4f3ee95091873c18f6fd3e` |
| `processed/large/undead_zombies_frame_01.png` | `c04b400a93f98ad93f2eccc4a6004e7c6940e79280e4eb573eb5d0f8855a99ca` |
| `processed/large/unit_undead_zombies_icon.png` | `63928b51aae84f5952631ffdeaf4b86dc44477ad691b8e5fb8311fbb865c2318` |
| `processed/small/onmap_unit_undead_zombies_icon.png` | `1c8563693acd8777839966a05848b150c4deca274465fad01ee7789391561de4` |
| `processed/small/undead_zombies_frame_00.png` | `b52c97c10a05cc5c5cd9821c323b120a00df9d0aef25b7008d4ec54828f59916` |
| `processed/small/undead_zombies_frame_01.png` | `c3305a8566c5c8c9611e646fe2c761fb23917d17d5d25c19ae1e2e08db4e0e0c` |
| `roundtrip/large/unit_undead_zombies_icon.png` | `63928b51aae84f5952631ffdeaf4b86dc44477ad691b8e5fb8311fbb865c2318` |
| `roundtrip/small/onmap_unit_undead_zombies_icon.png` | `1c8563693acd8777839966a05848b150c4deca274465fad01ee7789391561de4` |
| `small/onmap_unit_undead_zombies_icon.dds` | `236b04ced05f5bcd391c2a293373d042b1c1c4905c1e87f503d99d002259adac` |
| `source/large/undead_zombies_counter_alternate_source.png` | `f1285b79f5bcb638e8231fa4f5ef60754455853dfc86122cde72101df1c622d6` |
| `source/large/undead_zombies_counter_source.png` | `9a0ba492ff57910b039d532cbf41870f7ac2ea77c7c2d6461ca99056027d5865` |
| `source/large/undead_zombies_counter_source_v2.png` | `79e69976218fbacb34cee61b598d953f27824435ebb6c4dc10d92474a049548c` |
| `source/small/undead_zombies_counter_alternate_source.png` | `0ee5b75f77abd88c16da7ecc24802fe9dfc8adfdc2a7eba091fbdc59d94970de` |
| `source/small/undead_zombies_counter_source.png` | `13349005e1c4819a5927a6c130c57293ad89d304637e1b8a715e6b04dd507392` |
| `source/small/undead_zombies_counter_source_v2.png` | `9036a01e5091b9989b76fec1396126de184ed737d135a8df0ba0f8fa1b42ca01` |

## Runtime boundary

The bespoke DDS files were visually reviewed against the contact sheet and promoted to the runtime counter paths named above. Parent gameplay and live in-game validation remain separate concerns.
