# Event 018 achievement icon manifest

## Production contract

Event 018 has fifteen independent achievement masters generated with the built-in image workflow. No focus, idea, decision, portrait, flag, event picture, or other cross-type source was resized or reused. The accepted masters are stored twice by design:

- the generation and prompt package remains under `docs/assets/018_resources_found/achievement_icons_imagegen/`;
- the deterministic Event 018 processor consumes the canonical copies under `docs/assets/018_resources_found/source_png/achievements/`.

Every accepted master is a square, fully opaque, text-free completed-state image. The processor writes a `64x64` completed PNG, derives an exact grayscale PNG, composites the canonical unavailable overlay onto that grayscale image, and writes the three matching one-mip uncompressed BGRA DDS files. The overlay is `.agents/skills/chaos-redux-event-assets/assets/achievements/overlay.png`, SHA-256 `89bc80c6ac975bf6f1ff000ff3070b20c337bfb8b8ae966ae35a5540c004d6dd`.

## Asset map

| Achievement ID | Semantic subject | Source master | Runtime triplet |
| --- | --- | --- | --- |
| `018_resources_found_one_vein_market` | one dominant vein feeding an industrial market | `achievement_018_resources_found_one_vein_market_source.png` | completed, grey, not eligible |
| `018_resources_found_all_resources_one_state` | six standard resources converging on one field | `achievement_018_resources_found_all_resources_one_state_source.png` | completed, grey, not eligible |
| `018_resources_found_every_worker_home` | sealed safe shaft and every lamp returned | `achievement_018_resources_found_every_worker_home_source.png` | completed, grey, not eligible |
| `018_resources_found_full_seal_evolution_three` | engineered bulkhead holding under pressure | `achievement_018_resources_found_full_seal_evolution_three_source.png` | completed, grey, not eligible |
| `018_resources_found_contract_of_century` | sealed contract, mine, rail, and ore wagon | `achievement_018_resources_found_contract_of_century_source.png` | completed, grey, not eligible |
| `018_resources_found_resolve_field_dispute` | unoccupied border posts, lowered rifles, and inspection road | `achievement_018_resources_found_resolve_field_dispute_source.png` | completed, grey, not eligible |
| `018_resources_found_thirty_from_below` | massed Oth-Kesh breach against a small prepared gun line | `achievement_018_resources_found_thirty_from_below_source.png` | completed, grey, not eligible |
| `018_resources_found_last_shaft_closed` | final battle-scarred shaft sealed at dawn | `achievement_018_resources_found_last_shaft_closed_source.png` | completed, grey, not eligible |
| `018_resources_found_ten_from_one_state` | full resource-anchor lattice from one state | `achievement_018_resources_found_ten_from_one_state_source.png` | completed, grey, not eligible |
| `018_resources_found_no_men_no_guns` | empty human barracks above resource-born broods | `achievement_018_resources_found_no_men_no_guns_source.png` | completed, grey, not eligible |
| `018_resources_found_moving_mountain` | armored Stone Phalanx under anti-tank fire | `achievement_018_resources_found_moving_mountain_source.png` | completed, grey, not eligible |
| `018_resources_found_front_has_a_floor` | prepared tunnel beneath a fortified surface line | `achievement_018_resources_found_front_has_a_floor_source.png` | completed, grey, not eligible |
| `018_resources_found_hills_begin_to_move` | fast Scree Tide descending from a fractured ridge | `achievement_018_resources_found_hills_begin_to_move_source.png` | completed, grey, not eligible |
| `018_resources_found_continental_appetite` | generic stone continent crossed by a breach network | `achievement_018_resources_found_continental_appetite_source.png` | completed, grey, not eligible |
| `018_resources_found_ground_quiet_again` | repaired world industry above a permanently sealed chasm | `achievement_018_resources_found_ground_quiet_again_source.png` | completed, grey, not eligible |

For every row, the source path is relative to `docs/assets/018_resources_found/source_png/achievements/`. Processed files are `docs/assets/018_resources_found/processed_png/achievements/<id>.png`, `<id>_grey.png`, and `<id>_not_eligible.png`. Runtime files are `gfx/achievements/<id>.dds`, `<id>_grey.dds`, and `<id>_not_eligible.dds`.

## Wiring and inspection

All 45 sprites are registered as `GFX_achievement_<id><state_suffix>` in `interface/chaosx_achievements.gfx`. Visual review used:

- `docs/assets/018_resources_found/contact_sheets/achievements_source_contact_sheet.png`;
- `docs/assets/018_resources_found/contact_sheets/achievements_contact_sheet.png`;
- `docs/assets/018_resources_found/contact_sheets/achievements_dds_decoded_contact_sheet.png`.

The final audit found 15 unique source hashes, 15 unique completed pixel hashes, 45 processed PNGs, 45 runtime DDS files, 45 registrations, canonical `64x64` BGRA masks, and zero DDS-to-PNG pixel mismatches. Grey and unavailable derivations match their defined transforms exactly.

## Disposition

All fifteen achievement art identities are complete and wired. There is no placeholder, reused final icon, cross-type resize, missing state, fallback substitution, or unresolved asset mapping in this package.
