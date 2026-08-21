# `necrotic_zombies` bespoke counter package

Status: `complete` after parent visual review and runtime promotion.

Unit identity: collapsed necrotic corpse silhouette with sagging torso, exposed rib-like gaps, hanging jaw, and very decayed posture.

## Final DDS deliverables

| Surface | Package DDS | Runtime destination (not copied by this subagent) | Existing sprite | Canvas | Frames |
| --- | --- | --- | --- | ---: | ---: |
| Large division counter | `large/unit_necrotic_zombies_icon.dds` | `gfx/interface/counters/divisions_large/unit_necrotic_zombies_icon.dds` | `GFX_unit_necrotic_zombies_icon_medium` | 152×42 | 2 |
| Small on-map counter | `small/onmap_unit_necrotic_zombies_icon.dds` | `gfx/interface/counters/divisions_small/onmap_unit_necrotic_zombies_icon.dds` | `GFX_unit_necrotic_zombies_icon_medium_white` | 60×12 | 2 |

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
| `alpha/large/necrotic_zombies_frame_00_alpha.png` | `7e8a1eb9d26c76b937f2fe92f7e06c1afbce1570d75eb66ccc96a1cd81b1e119` |
| `alpha/large/necrotic_zombies_frame_01_alpha.png` | `24bc78758e7b79b09a771a9fdb1bf914a24234e60d753abe677f3250d77b735d` |
| `alpha/small/necrotic_zombies_frame_00_alpha.png` | `810cc6756e79654018d840cb393f615a868d9198969de023be3ca3fbb875c17c` |
| `alpha/small/necrotic_zombies_frame_01_alpha.png` | `438472008f416d78df32b91df7f2ca4ce82a1ff00fbb5ba10d6aa7c5c088937d` |
| `contact_sheet.png` | `60559b7c2274778f7b5ef6c46bda57805ea3b0746ca0c6554249c300672828da` |
| `large/unit_necrotic_zombies_icon.dds` | `f6497cb84905cc10a70c82590d8e952e5a1b2e4d07f5c6805ef35ffc07843b01` |
| `processed/large/necrotic_zombies_frame_00.png` | `e856a8a6c392a95d8dd819ba3aaa4842538cfcd0c3e9c2f90c2f25f2f3246b3d` |
| `processed/large/necrotic_zombies_frame_01.png` | `635f6b531352879fa915a1d5d1b6a83ad7aed2aac66e6209c125996ddbca6793` |
| `processed/large/unit_necrotic_zombies_icon.png` | `3ba1701a9e9080a65ca4a7203812e9af83af5c3ab995e1658032541174ed4046` |
| `processed/small/necrotic_zombies_frame_00.png` | `1cc1a3168e0a485b32a02021fc438a2e15f7391f13c319b0aeeabba019bd6eb8` |
| `processed/small/necrotic_zombies_frame_01.png` | `0096f7a4a4156119d93bfd107bf084d58d015f714dcfc6c6d53b96a04cbeea80` |
| `processed/small/onmap_unit_necrotic_zombies_icon.png` | `03d0e672a99c5ef8d5a359e455d9dc8227162a5a29161181c5031d609e404f88` |
| `roundtrip/large/unit_necrotic_zombies_icon.png` | `3ba1701a9e9080a65ca4a7203812e9af83af5c3ab995e1658032541174ed4046` |
| `roundtrip/small/onmap_unit_necrotic_zombies_icon.png` | `03d0e672a99c5ef8d5a359e455d9dc8227162a5a29161181c5031d609e404f88` |
| `small/onmap_unit_necrotic_zombies_icon.dds` | `48a931b536feac9c315ace0c9b057268bf65cb81648de3e176cf7a21341262a3` |
| `source/large/necrotic_zombies_counter_alternate_source.png` | `71e12a93dd373ee1928972344e877c0313b8a8a286a6d91ca2fbb1b0eebe3b1a` |
| `source/large/necrotic_zombies_counter_source.png` | `8a6aa53a153d67aebfff3f03d125b31000802b1bf405aca1685a8394f774ca75` |
| `source/small/necrotic_zombies_counter_alternate_source.png` | `d3e3ad499193eee5abe64d96e6f5bc908a07e959799e2d4e74401b65a9943965` |
| `source/small/necrotic_zombies_counter_source.png` | `8e6ff08a98d54b04b0e6d882693ca7eaec42c528076475f06eb3dbbbb126212a` |

## Runtime boundary

The bespoke DDS files were visually reviewed against the contact sheet and promoted to the runtime counter paths named above. Parent gameplay and live in-game validation remain separate concerns.
