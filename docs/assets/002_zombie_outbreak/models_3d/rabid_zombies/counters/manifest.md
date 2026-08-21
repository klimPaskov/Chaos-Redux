# `rabid_zombies` bespoke counter package

Status: `complete` after parent visual review and runtime promotion.

Unit identity: forward-leaning rabid sprinter with jaw thrust forward, both clawed hands raised, and compact aggressive posture.

## Final DDS deliverables

| Surface | Package DDS | Runtime destination (not copied by this subagent) | Existing sprite | Canvas | Frames |
| --- | --- | --- | --- | ---: | ---: |
| Large division counter | `large/unit_rabid_zombies_icon.dds` | `gfx/interface/counters/divisions_large/unit_rabid_zombies_icon.dds` | `GFX_unit_rabid_zombies_icon_medium` | 152×42 | 2 |
| Small on-map counter | `small/onmap_unit_rabid_zombies_icon.dds` | `gfx/interface/counters/divisions_small/onmap_unit_rabid_zombies_icon.dds` | `GFX_unit_rabid_zombies_icon_medium_white` | 60×12 | 2 |

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
| `alpha/large/rabid_zombies_frame_00_alpha.png` | `b08fd3acbd2ee3447c87ceb153f9cf2f5bd51709996c17776a01a5ddf952a6e7` |
| `alpha/large/rabid_zombies_frame_01_alpha.png` | `fa9c874189a734df3bf23cf1df16ee99605d67990e37b91e733cb423e31fd725` |
| `alpha/small/rabid_zombies_frame_00_alpha.png` | `a9e50a95ea580cce3227ee74e2863238ac4561c94fa91734fdf5a4c149397537` |
| `alpha/small/rabid_zombies_frame_01_alpha.png` | `71b389c285e26be5d1d26a85cab8442bfe818d9453fd62a8ec35c36daf8481ac` |
| `contact_sheet.png` | `006172b49c345ef867ece427ba20bcbb8a375958e035097db0f9de96970a5721` |
| `large/unit_rabid_zombies_icon.dds` | `eda3e72eaa258c69bd3464509260ce8431f6175f9c27a8f664d74cbe8312b456` |
| `processed/large/rabid_zombies_frame_00.png` | `ef780be4a7a734e440a0f168db8611f34e12bd6b9192ce3e8a6bad6531a08b2a` |
| `processed/large/rabid_zombies_frame_01.png` | `683567486e68c9cce5fd438ba7f4a83be5ef6731db377894f8dbd27eef224f62` |
| `processed/large/unit_rabid_zombies_icon.png` | `6bcc7c60f249d1b11a5ade0c9f54dadc0d12d9dc48990674a32f6faf6a0c27f3` |
| `processed/small/onmap_unit_rabid_zombies_icon.png` | `907bb59c207773001508a770daada470dfb8cdff90926316119b5f8b7b05ccbb` |
| `processed/small/rabid_zombies_frame_00.png` | `544bc6b19f110c04f2cf6e40339dacc6b85968f2674e0e7de1df6a6f55c6c19d` |
| `processed/small/rabid_zombies_frame_01.png` | `ff41be9be58376fefb6b69f837d6ca5748dbc9dda7c213754e6ad350e08abcae` |
| `roundtrip/large/unit_rabid_zombies_icon.png` | `6bcc7c60f249d1b11a5ade0c9f54dadc0d12d9dc48990674a32f6faf6a0c27f3` |
| `roundtrip/small/onmap_unit_rabid_zombies_icon.png` | `907bb59c207773001508a770daada470dfb8cdff90926316119b5f8b7b05ccbb` |
| `small/onmap_unit_rabid_zombies_icon.dds` | `35a79073bba767dc7e7a5bf7aed74aff19a1c905b6076de3eb9ce0efbb2fe5ab` |
| `source/large/rabid_zombies_counter_alternate_source.png` | `46331f0f1ad62424ba8d8deaa1050b2cffd4ceb1de5b03f1000fcf05f97d08a5` |
| `source/large/rabid_zombies_counter_source.png` | `4b9475c224b6ce2544cd5325cb9d50489e8f491eddac8f6dc4dd631a5c42eb4a` |
| `source/small/rabid_zombies_counter_alternate_source.png` | `5ac24b8a8376b304e4d44148a52d5664f6440eaaad6067abb840bea3740778cd` |
| `source/small/rabid_zombies_counter_source.png` | `812a592a7d3961fcc397ee6e69b1759c550d538404242d6ef1dab3c5193ad131` |

## Runtime boundary

The bespoke DDS files were visually reviewed against the contact sheet and promoted to the runtime counter paths named above. Parent gameplay and live in-game validation remain separate concerns.
