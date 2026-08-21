# `demonic_zombies` bespoke counter package

Status: `complete` after parent visual review and runtime promotion.

Unit identity: tall demonic humanoid with small swept horns, sharp wing-like shoulder silhouette, long limbs, and predatory posture.

## Final DDS deliverables

| Surface | Package DDS | Runtime destination (not copied by this subagent) | Existing sprite | Canvas | Frames |
| --- | --- | --- | --- | ---: | ---: |
| Large division counter | `large/unit_demonic_zombies_icon.dds` | `gfx/interface/counters/divisions_large/unit_demonic_zombies_icon.dds` | `GFX_unit_demonic_zombies_icon_medium` | 152×42 | 2 |
| Small on-map counter | `small/onmap_unit_demonic_zombies_icon.dds` | `gfx/interface/counters/divisions_small/onmap_unit_demonic_zombies_icon.dds` | `GFX_unit_demonic_zombies_icon_medium_white` | 60×12 | 2 |

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
| `alpha/large/demonic_zombies_frame_00_alpha.png` | `fb4c810ede9d498e95d2d1cf13c262a6373d5d3523e972e8867ba66bb5d3249d` |
| `alpha/large/demonic_zombies_frame_01_alpha.png` | `a75814e8824e58a30d8ea9b0f089a0232deec3a90a19b006e64b84c8741b8a3d` |
| `alpha/small/demonic_zombies_frame_00_alpha.png` | `f573a1adb178cc515b6044211bc8b2e3c8716cb1911938acdc5b4526fe76eb96` |
| `alpha/small/demonic_zombies_frame_01_alpha.png` | `89736b545979cc0cb74f68a632133c82ed6cf157b751f7dbc2cc5646b34a9010` |
| `contact_sheet.png` | `8e0daec9cf4fe9adbec660547dbec7bdf2fcfa2860260fe5113fa3b1860955e6` |
| `large/unit_demonic_zombies_icon.dds` | `dd657c7eba183cffc7346896b95378ffb965397dd033c57646ccb0fc75274e9f` |
| `processed/large/demonic_zombies_frame_00.png` | `3bed5badeee244bbe793e26d50bb107666ebe6a850be6cb9d86ce98a9eb07f02` |
| `processed/large/demonic_zombies_frame_01.png` | `daebad7844ffae6ad4d790ffc560d9efaaac4e9dfc3be8f862997ed0087f08d2` |
| `processed/large/unit_demonic_zombies_icon.png` | `37c6b8156e48e364666753e3530490c50de0ebd30202ed007b19994b5492f60b` |
| `processed/small/demonic_zombies_frame_00.png` | `340b2e2a657a242ec2f2cfd5120715b8f82ed11ea479b8034f052406540bd071` |
| `processed/small/demonic_zombies_frame_01.png` | `967dddc569892e83d70e13c8dd2ecc223b882761c9e7d432001ddebd84da8a5a` |
| `processed/small/onmap_unit_demonic_zombies_icon.png` | `32309c1459f02070f743e4570fa6f69809f4560e2d8c14b56566a3d59a513aab` |
| `roundtrip/large/unit_demonic_zombies_icon.png` | `37c6b8156e48e364666753e3530490c50de0ebd30202ed007b19994b5492f60b` |
| `roundtrip/small/onmap_unit_demonic_zombies_icon.png` | `32309c1459f02070f743e4570fa6f69809f4560e2d8c14b56566a3d59a513aab` |
| `small/onmap_unit_demonic_zombies_icon.dds` | `a6f63d46e73ba827cb378b98391ebac7c7042f5af23ceab80ec5b4aeeebfa92e` |
| `source/large/demonic_zombies_counter_alternate_source.png` | `f259082f58efec48a8b659bdf91de178d4af640a2a622aff015d122bea89e363` |
| `source/large/demonic_zombies_counter_source.png` | `d0080eab7edc6f7a24fa1d350b57a5d45d7b8597cdad04048aa4134bb2c6b722` |
| `source/small/demonic_zombies_counter_alternate_source.png` | `78767dc3d3814fa44187f1bc56220ced76302e8f4c84c35f93ecd3f7089c6e9f` |
| `source/small/demonic_zombies_counter_source.png` | `0de21e631faf93436fe03a7c1cbe5e2be5ed9fe2b670dc916881afc080f5080a` |

## Runtime boundary

The bespoke DDS files were visually reviewed against the contact sheet and promoted to the runtime counter paths named above. Parent gameplay and live in-game validation remain separate concerns.
