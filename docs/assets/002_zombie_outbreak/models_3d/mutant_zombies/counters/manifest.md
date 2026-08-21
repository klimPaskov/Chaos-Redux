# `mutant_zombies` bespoke counter package

Status: `complete` after parent visual review and runtime promotion.

Unit identity: broad-shouldered mutant with oversized forearms and a heavy loping stance, low head, and massive upper body.

## Final DDS deliverables

| Surface | Package DDS | Runtime destination (not copied by this subagent) | Existing sprite | Canvas | Frames |
| --- | --- | --- | --- | ---: | ---: |
| Large division counter | `large/unit_mutant_zombies_icon.dds` | `gfx/interface/counters/divisions_large/unit_mutant_zombies_icon.dds` | `GFX_unit_mutant_zombies_icon_medium` | 152×42 | 2 |
| Small on-map counter | `small/onmap_unit_mutant_zombies_icon.dds` | `gfx/interface/counters/divisions_small/onmap_unit_mutant_zombies_icon.dds` | `GFX_unit_mutant_zombies_icon_medium_white` | 60×12 | 2 |

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
| `alpha/large/mutant_zombies_frame_00_alpha.png` | `015836ba17dd1e7cf7adc99932d3779305ef45bd3c33daf7762e4aea3a49b271` |
| `alpha/large/mutant_zombies_frame_01_alpha.png` | `eff5b27b467cfebf4afeca7f6c4f3899513165b8b07bf87a149b20ccc79ff943` |
| `alpha/small/mutant_zombies_frame_00_alpha.png` | `a80d254a8d62c5a9e97fa85785dd11fdaf673e8151ff86e58007f0ce662334ae` |
| `alpha/small/mutant_zombies_frame_01_alpha.png` | `e823ecb961025808785a3f20373085d209f70909ec6ebd77de01110c5e3dc17c` |
| `contact_sheet.png` | `31a16f2191b62e91e80c9e7c642020609818dfbf440e32ff69cc38f5bb45cd57` |
| `large/unit_mutant_zombies_icon.dds` | `41a03a4fcff3fe7409dbb68e5dde7a56747f06ce1c39152792abdb56569a597a` |
| `processed/large/mutant_zombies_frame_00.png` | `61604f25c9f51cde7f66ec0327ebc19c4d44984524c3e31176af64b2c6869b2f` |
| `processed/large/mutant_zombies_frame_01.png` | `4ec03a0a835aa642e22f52959973bc493b70a890f75031bf81d63961a9d67496` |
| `processed/large/unit_mutant_zombies_icon.png` | `ea8dc385ca1682303bf11015c77d4500dcae29599d42c4225c22fa789cdb3476` |
| `processed/small/mutant_zombies_frame_00.png` | `c5009e6111ba15fe76bde5a8dc4424390efd2dab20d35eb89f5705843814612c` |
| `processed/small/mutant_zombies_frame_01.png` | `5cabee1074505139936664f33b8a86cb2a095e38a990923353a2372496c744e4` |
| `processed/small/onmap_unit_mutant_zombies_icon.png` | `e0916e8ec0053c4cc6be963d8c7c1bfe5a9b6113d2b423f2b46a3fced7a94ff1` |
| `roundtrip/large/unit_mutant_zombies_icon.png` | `ea8dc385ca1682303bf11015c77d4500dcae29599d42c4225c22fa789cdb3476` |
| `roundtrip/small/onmap_unit_mutant_zombies_icon.png` | `e0916e8ec0053c4cc6be963d8c7c1bfe5a9b6113d2b423f2b46a3fced7a94ff1` |
| `small/onmap_unit_mutant_zombies_icon.dds` | `4f3f3d2080a6a66390eae72004645494c17bb142bf67a04ca7e4c2af7271b08a` |
| `source/large/mutant_zombies_counter_alternate_source.png` | `5b876f61e88faf31c14d0148d48199ba97c8d9778ddfe3b8103d6d5f72f1ab8a` |
| `source/large/mutant_zombies_counter_source.png` | `3eac341f6e464a4c38d9d1e0dbf2aff16c2926a4a431e0bed0d918e3f70ae1eb` |
| `source/small/mutant_zombies_counter_alternate_source.png` | `6f0ee7af56ae0e2f9d552ddc1eb1526ea2a9fec062d2585ad07c044d1cfcbff1` |
| `source/small/mutant_zombies_counter_source.png` | `e09d8c2cf6930b6744f3250c75e49707e4c978853795a24d9847faa594f2450c` |

## Runtime boundary

The bespoke DDS files were visually reviewed against the contact sheet and promoted to the runtime counter paths named above. Parent gameplay and live in-game validation remain separate concerns.
