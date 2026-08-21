# `parasitic_zombies` bespoke counter package

Status: `complete` after parent visual review and runtime promotion.

Unit identity: asymmetrical parasite-host silhouette with elongated tendrils or growths wrapping one shoulder and a hunched uneven torso.

## Final DDS deliverables

| Surface | Package DDS | Runtime destination (not copied by this subagent) | Existing sprite | Canvas | Frames |
| --- | --- | --- | --- | ---: | ---: |
| Large division counter | `large/unit_parasitic_zombies_icon.dds` | `gfx/interface/counters/divisions_large/unit_parasitic_zombies_icon.dds` | `GFX_unit_parasitic_zombies_icon_medium` | 152×42 | 2 |
| Small on-map counter | `small/onmap_unit_parasitic_zombies_icon.dds` | `gfx/interface/counters/divisions_small/onmap_unit_parasitic_zombies_icon.dds` | `GFX_unit_parasitic_zombies_icon_medium_white` | 60×12 | 2 |

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
| `alpha/large/parasitic_zombies_frame_00_alpha.png` | `e1f2d96632994b5e6bd7396f880eb5b2a81fda6cbec1564b527d37e8a8cb5afb` |
| `alpha/large/parasitic_zombies_frame_01_alpha.png` | `5282b3d3aede3c87bfec43ee4be42d37ae8b857baa9860839280bc7c73dabe45` |
| `alpha/small/parasitic_zombies_frame_00_alpha.png` | `ef106beed1802adb8c2ea3ddb7d509d71b753c709a28e8b9adb0cb1c07e2f473` |
| `alpha/small/parasitic_zombies_frame_01_alpha.png` | `4fc5840c4cd3bb339bf759afc39fa02bbffcf42c101210a29c351da3ec503ef4` |
| `contact_sheet.png` | `e5a035ef09cadd53c87d794be43c1768906af52753b1edc9b3115791a2129571` |
| `large/unit_parasitic_zombies_icon.dds` | `d41ebb36df5d11c43a853646e111a2f38215c9845695e9b5b65c5a78738e35a1` |
| `processed/large/parasitic_zombies_frame_00.png` | `8a5ad7350983aae602e7644191ad7a0d1478ec2ee0bd466a9cd9a42026e4930b` |
| `processed/large/parasitic_zombies_frame_01.png` | `db536d542aa54c879bbe1141877b2348ef132e34446829cd11c5f816a8eb0d69` |
| `processed/large/unit_parasitic_zombies_icon.png` | `4c5c855a405d509cd5fdbd91e48b35ed8f055194cff7c2c4725774da8b8240c4` |
| `processed/small/onmap_unit_parasitic_zombies_icon.png` | `47ff0ed55d5137904b3e3ed5af5d92fe1351e9f1d5faabf7d94c1c116a85a690` |
| `processed/small/parasitic_zombies_frame_00.png` | `ca924a094890e1b73c8c68c8dfe7e3f13ab4e448bfa6a905321652e2c2ae6759` |
| `processed/small/parasitic_zombies_frame_01.png` | `8b6bb318fc73a9eb1ae3bedc32e54b330893338bd83e0cef302062387dc63e1c` |
| `roundtrip/large/unit_parasitic_zombies_icon.png` | `4c5c855a405d509cd5fdbd91e48b35ed8f055194cff7c2c4725774da8b8240c4` |
| `roundtrip/small/onmap_unit_parasitic_zombies_icon.png` | `47ff0ed55d5137904b3e3ed5af5d92fe1351e9f1d5faabf7d94c1c116a85a690` |
| `small/onmap_unit_parasitic_zombies_icon.dds` | `ee0973f34cedca5593f4bfd4d84efecfab80731ef7c0e6e470c55effce79abe9` |
| `source/large/parasitic_zombies_counter_alternate_source.png` | `668113244e501df5b3e39d04f97a8a16a13f94d6066c86ad9db873d5e2f41e53` |
| `source/large/parasitic_zombies_counter_source.png` | `eac029c1cdfa5e0215152ddf70aed777ad14b29bcf9abc6962ae337799b11ae5` |
| `source/small/parasitic_zombies_counter_alternate_source.png` | `cd2b8bae50581dea8c7ff3dec1b7989749fe64739e80db21f338a34ce2cd7d0c` |
| `source/small/parasitic_zombies_counter_source.png` | `4f333c6eec94d7b96d9fdf101d797bfb01a386b06b9c0bc74b5b240cf0e810bd` |

## Runtime boundary

The bespoke DDS files were visually reviewed against the contact sheet and promoted to the runtime counter paths named above. Parent gameplay and live in-game validation remain separate concerns.
