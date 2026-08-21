# `infected_zombies` bespoke counter package

Status: `complete` after parent visual review and runtime promotion.

Unit identity: hunched shambling infected human with torn coat hem, one reaching arm, and ragged hair.

## Final DDS deliverables

| Surface | Package DDS | Runtime destination (not copied by this subagent) | Existing sprite | Canvas | Frames |
| --- | --- | --- | --- | ---: | ---: |
| Large division counter | `large/unit_infected_zombies_icon.dds` | `gfx/interface/counters/divisions_large/unit_infected_zombies_icon.dds` | `GFX_unit_infected_zombies_icon_medium` | 152×42 | 2 |
| Small on-map counter | `small/onmap_unit_infected_zombies_icon.dds` | `gfx/interface/counters/divisions_small/onmap_unit_infected_zombies_icon.dds` | `GFX_unit_infected_zombies_icon_medium_white` | 60×12 | 2 |

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
| `alpha/large/infected_zombies_frame_00_alpha.png` | `31d5f643304db770a3fc27a57301088cdbf6f5db90d260a85f03375c9e578959` |
| `alpha/large/infected_zombies_frame_01_alpha.png` | `a8c339bd8c1089ff098bebbeead70e99bd0e9b6ac565b85c8ab77788d26961de` |
| `alpha/small/infected_zombies_frame_00_alpha.png` | `b6ead578ed940b2ef5c359adcd0504aca1db081913c16d3cba25296065e1a5bc` |
| `alpha/small/infected_zombies_frame_01_alpha.png` | `24578971557b2364fffe4d020cf60009c7f2fc082c4e11a753be51701ffb3ce5` |
| `contact_sheet.png` | `10da360c998ef8daf3b9c296b209f0241be56e4b014438cb24f89c8463e91ad4` |
| `large/unit_infected_zombies_icon.dds` | `0c048983fde1bc9740e169bec4af6c9e88b97bcc990e9915acf42a6814299c11` |
| `processed/large/infected_zombies_frame_00.png` | `a636c948b145ca77ff17f3c8c470e2d310b00e4164433078592f69cf6a599ae0` |
| `processed/large/infected_zombies_frame_01.png` | `70e6567dfa465dc1617505dfade9020b94c5a63a610a0c5f6e1f754d8b5787b9` |
| `processed/large/unit_infected_zombies_icon.png` | `29135a25c1934b886f99c15d0408c88ad57a48be55ca517045ee25775ab1636a` |
| `processed/small/infected_zombies_frame_00.png` | `d178650bf968592e9055a98b205e067b2194cda0ebbd8989ae2733ec690b9d23` |
| `processed/small/infected_zombies_frame_01.png` | `4881df26151c9b4ca4cbab398f57efcb25f95d03172677b93a92075526765b32` |
| `processed/small/onmap_unit_infected_zombies_icon.png` | `dadb0687187c09d2ce818deda507cdefc7d2624b5d96380f015be530d637e347` |
| `roundtrip/large/unit_infected_zombies_icon.png` | `29135a25c1934b886f99c15d0408c88ad57a48be55ca517045ee25775ab1636a` |
| `roundtrip/small/onmap_unit_infected_zombies_icon.png` | `dadb0687187c09d2ce818deda507cdefc7d2624b5d96380f015be530d637e347` |
| `small/onmap_unit_infected_zombies_icon.dds` | `0467070b0f919354a562138ebba9ce5d9a64033d0f1a8a52322e779aaeb53c46` |
| `source/large/infected_zombies_counter_alternate_source.png` | `d334c30d6975d7db469d28b683c57e4c1513f271c0b30745e9f7fd5e387f4cb0` |
| `source/large/infected_zombies_counter_source.png` | `41facb1833d8ec72e7caad59f6098da835e6ce96b437b9a7a1d7affa9e01472c` |
| `source/small/infected_zombies_counter_alternate_source.png` | `7b6f697ee5a1bfd738bcbfb0da3e3e8d6fbea7b1a39044d3ea0205241ac6dc4e` |
| `source/small/infected_zombies_counter_source.png` | `4260d9ddd92746b409e6296daa0620b2ff2b3d9e5409a815a8874431fc4ccfe2` |

## Runtime boundary

The bespoke DDS files were visually reviewed against the contact sheet and promoted to the runtime counter paths named above. Parent gameplay and live in-game validation remain separate concerns.
