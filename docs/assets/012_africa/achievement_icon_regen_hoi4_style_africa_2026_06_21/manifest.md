# Event 012 Africa Achievement Icon Regeneration Manifest

Date: `2026-06-21`

Related event id: `012`

Related event slug: `africa`

Asset type: achievement icons

Intended in-game use: replace the existing Africa achievement icon families with full `64x64` HOI4-style achievement tiles while preserving the exact live DDS filenames already used by the mod.

Source mode: reused prior `$imagegen`-derived Africa achievement motifs from earlier Africa asset packages, then locally recomposed into new square HOI4-style achievement tiles for this package.

Style target:

- full opaque `64x64` achievement tiles, not transparent focus or idea icons
- dark square plaque with bronze medal framing and a centered readable subject
- `_grey` derived from the completed icon
- `_not_eligible` derived from the grey icon with a red crossed overlay

Reference inspection completed:

- Chaos Redux achievement references: `.agents/skills/chaos-redux-event-assets/assets/achievements/`
- Vanilla achievement examples: `~/projects/Hearts of Iron IV/gfx/achievements/`

Processing summary:

- Extracted each subject motif from the prior Africa processed normal icon.
- Rebuilt every completed icon onto a shared HOI4-style square achievement backplate.
- Derived `_grey` and `_not_eligible` variants from the rebuilt completed icon.
- Exported package DDS copies and replaced the live DDS families in `gfx/achievements/`.

DDS conversion note:

- The repository DDS helper fallback currently errors in this environment.
- Package and live DDS outputs were therefore written through Pillow's DDS exporter after PNG processing.
- Validation confirmed every package and live DDS produced here is a `64x64` `DDS` file.

## Asset List

| Achievement ID | Source PNG | Processed PNG variants | Package DDS variants | Live DDS variants | Target size | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `ACH_AFRICA_TERRACOTTA_LINE` | `source_png/ACH_AFRICA_TERRACOTTA_LINE_source.png` | `processed_png/ACH_AFRICA_TERRACOTTA_LINE.png`, `processed_png/ACH_AFRICA_TERRACOTTA_LINE_grey.png`, `processed_png/ACH_AFRICA_TERRACOTTA_LINE_not_eligible.png` | `dds/ACH_AFRICA_TERRACOTTA_LINE.dds`, `dds/ACH_AFRICA_TERRACOTTA_LINE_grey.dds`, `dds/ACH_AFRICA_TERRACOTTA_LINE_not_eligible.dds` | `gfx/achievements/ACH_AFRICA_TERRACOTTA_LINE.dds`, `gfx/achievements/ACH_AFRICA_TERRACOTTA_LINE_grey.dds`, `gfx/achievements/ACH_AFRICA_TERRACOTTA_LINE_not_eligible.dds` | `64x64` | `complete` |
| `ACH_AFR_ANANSE_WROTE_THE_ORDERS` | `source_png/ACH_AFR_ANANSE_WROTE_THE_ORDERS_source.png` | `processed_png/ACH_AFR_ANANSE_WROTE_THE_ORDERS.png`, `processed_png/ACH_AFR_ANANSE_WROTE_THE_ORDERS_grey.png`, `processed_png/ACH_AFR_ANANSE_WROTE_THE_ORDERS_not_eligible.png` | `dds/ACH_AFR_ANANSE_WROTE_THE_ORDERS.dds`, `dds/ACH_AFR_ANANSE_WROTE_THE_ORDERS_grey.dds`, `dds/ACH_AFR_ANANSE_WROTE_THE_ORDERS_not_eligible.dds` | `gfx/achievements/ACH_AFR_ANANSE_WROTE_THE_ORDERS.dds`, `gfx/achievements/ACH_AFR_ANANSE_WROTE_THE_ORDERS_grey.dds`, `gfx/achievements/ACH_AFR_ANANSE_WROTE_THE_ORDERS_not_eligible.dds` | `64x64` | `complete` |
| `ACH_AFR_BAOBAB_FILIBUSTER` | `source_png/ACH_AFR_BAOBAB_FILIBUSTER_source.png` | `processed_png/ACH_AFR_BAOBAB_FILIBUSTER.png`, `processed_png/ACH_AFR_BAOBAB_FILIBUSTER_grey.png`, `processed_png/ACH_AFR_BAOBAB_FILIBUSTER_not_eligible.png` | `dds/ACH_AFR_BAOBAB_FILIBUSTER.dds`, `dds/ACH_AFR_BAOBAB_FILIBUSTER_grey.dds`, `dds/ACH_AFR_BAOBAB_FILIBUSTER_not_eligible.dds` | `gfx/achievements/ACH_AFR_BAOBAB_FILIBUSTER.dds`, `gfx/achievements/ACH_AFR_BAOBAB_FILIBUSTER_grey.dds`, `gfx/achievements/ACH_AFR_BAOBAB_FILIBUSTER_not_eligible.dds` | `64x64` | `complete` |
| `ACH_AFR_BIGGER_CARAVAN` | `source_png/ACH_AFR_BIGGER_CARAVAN_source.png` | `processed_png/ACH_AFR_BIGGER_CARAVAN.png`, `processed_png/ACH_AFR_BIGGER_CARAVAN_grey.png`, `processed_png/ACH_AFR_BIGGER_CARAVAN_not_eligible.png` | `dds/ACH_AFR_BIGGER_CARAVAN.dds`, `dds/ACH_AFR_BIGGER_CARAVAN_grey.dds`, `dds/ACH_AFR_BIGGER_CARAVAN_not_eligible.dds` | `gfx/achievements/ACH_AFR_BIGGER_CARAVAN.dds`, `gfx/achievements/ACH_AFR_BIGGER_CARAVAN_grey.dds`, `gfx/achievements/ACH_AFR_BIGGER_CARAVAN_not_eligible.dds` | `64x64` | `complete` |
| `ACH_AFR_BIRD_WAS_RIGHT` | `source_png/ACH_AFR_BIRD_WAS_RIGHT_source.png` | `processed_png/ACH_AFR_BIRD_WAS_RIGHT.png`, `processed_png/ACH_AFR_BIRD_WAS_RIGHT_grey.png`, `processed_png/ACH_AFR_BIRD_WAS_RIGHT_not_eligible.png` | `dds/ACH_AFR_BIRD_WAS_RIGHT.dds`, `dds/ACH_AFR_BIRD_WAS_RIGHT_grey.dds`, `dds/ACH_AFR_BIRD_WAS_RIGHT_not_eligible.dds` | `gfx/achievements/ACH_AFR_BIRD_WAS_RIGHT.dds`, `gfx/achievements/ACH_AFR_BIRD_WAS_RIGHT_grey.dds`, `gfx/achievements/ACH_AFR_BIRD_WAS_RIGHT_not_eligible.dds` | `64x64` | `complete` |
| `ACH_AFR_COMMAND_OVER_CONGRESS` | `source_png/ACH_AFR_COMMAND_OVER_CONGRESS_source.png` | `processed_png/ACH_AFR_COMMAND_OVER_CONGRESS.png`, `processed_png/ACH_AFR_COMMAND_OVER_CONGRESS_grey.png`, `processed_png/ACH_AFR_COMMAND_OVER_CONGRESS_not_eligible.png` | `dds/ACH_AFR_COMMAND_OVER_CONGRESS.dds`, `dds/ACH_AFR_COMMAND_OVER_CONGRESS_grey.dds`, `dds/ACH_AFR_COMMAND_OVER_CONGRESS_not_eligible.dds` | `gfx/achievements/ACH_AFR_COMMAND_OVER_CONGRESS.dds`, `gfx/achievements/ACH_AFR_COMMAND_OVER_CONGRESS_grey.dds`, `gfx/achievements/ACH_AFR_COMMAND_OVER_CONGRESS_not_eligible.dds` | `64x64` | `complete` |
| `ACH_AFR_CONGRESS_OVER_COMMAND` | `source_png/ACH_AFR_CONGRESS_OVER_COMMAND_source.png` | `processed_png/ACH_AFR_CONGRESS_OVER_COMMAND.png`, `processed_png/ACH_AFR_CONGRESS_OVER_COMMAND_grey.png`, `processed_png/ACH_AFR_CONGRESS_OVER_COMMAND_not_eligible.png` | `dds/ACH_AFR_CONGRESS_OVER_COMMAND.dds`, `dds/ACH_AFR_CONGRESS_OVER_COMMAND_grey.dds`, `dds/ACH_AFR_CONGRESS_OVER_COMMAND_not_eligible.dds` | `gfx/achievements/ACH_AFR_CONGRESS_OVER_COMMAND.dds`, `gfx/achievements/ACH_AFR_CONGRESS_OVER_COMMAND_grey.dds`, `gfx/achievements/ACH_AFR_CONGRESS_OVER_COMMAND_not_eligible.dds` | `64x64` | `complete` |
| `ACH_AFR_ELEPHANTS_REMEMBER` | `source_png/ACH_AFR_ELEPHANTS_REMEMBER_source.png` | `processed_png/ACH_AFR_ELEPHANTS_REMEMBER.png`, `processed_png/ACH_AFR_ELEPHANTS_REMEMBER_grey.png`, `processed_png/ACH_AFR_ELEPHANTS_REMEMBER_not_eligible.png` | `dds/ACH_AFR_ELEPHANTS_REMEMBER.dds`, `dds/ACH_AFR_ELEPHANTS_REMEMBER_grey.dds`, `dds/ACH_AFR_ELEPHANTS_REMEMBER_not_eligible.dds` | `gfx/achievements/ACH_AFR_ELEPHANTS_REMEMBER.dds`, `gfx/achievements/ACH_AFR_ELEPHANTS_REMEMBER_grey.dds`, `gfx/achievements/ACH_AFR_ELEPHANTS_REMEMBER_not_eligible.dds` | `64x64` | `complete` |
| `ACH_AFR_FOREST_GUARDIAN_PACT` | `source_png/ACH_AFR_FOREST_GUARDIAN_PACT_source.png` | `processed_png/ACH_AFR_FOREST_GUARDIAN_PACT.png`, `processed_png/ACH_AFR_FOREST_GUARDIAN_PACT_grey.png`, `processed_png/ACH_AFR_FOREST_GUARDIAN_PACT_not_eligible.png` | `dds/ACH_AFR_FOREST_GUARDIAN_PACT.dds`, `dds/ACH_AFR_FOREST_GUARDIAN_PACT_grey.dds`, `dds/ACH_AFR_FOREST_GUARDIAN_PACT_not_eligible.dds` | `gfx/achievements/ACH_AFR_FOREST_GUARDIAN_PACT.dds`, `gfx/achievements/ACH_AFR_FOREST_GUARDIAN_PACT_grey.dds`, `gfx/achievements/ACH_AFR_FOREST_GUARDIAN_PACT_not_eligible.dds` | `64x64` | `complete` |
| `ACH_AFR_GENTLE_VETO` | `source_png/ACH_AFR_GENTLE_VETO_source.png` | `processed_png/ACH_AFR_GENTLE_VETO.png`, `processed_png/ACH_AFR_GENTLE_VETO_grey.png`, `processed_png/ACH_AFR_GENTLE_VETO_not_eligible.png` | `dds/ACH_AFR_GENTLE_VETO.dds`, `dds/ACH_AFR_GENTLE_VETO_grey.dds`, `dds/ACH_AFR_GENTLE_VETO_not_eligible.dds` | `gfx/achievements/ACH_AFR_GENTLE_VETO.dds`, `gfx/achievements/ACH_AFR_GENTLE_VETO_grey.dds`, `gfx/achievements/ACH_AFR_GENTLE_VETO_not_eligible.dds` | `64x64` | `complete` |
| `ACH_AFR_NOT_A_MAP_COLOUR` | `source_png/ACH_AFR_NOT_A_MAP_COLOUR_source.png` | `processed_png/ACH_AFR_NOT_A_MAP_COLOUR.png`, `processed_png/ACH_AFR_NOT_A_MAP_COLOUR_grey.png`, `processed_png/ACH_AFR_NOT_A_MAP_COLOUR_not_eligible.png` | `dds/ACH_AFR_NOT_A_MAP_COLOUR.dds`, `dds/ACH_AFR_NOT_A_MAP_COLOUR_grey.dds`, `dds/ACH_AFR_NOT_A_MAP_COLOUR_not_eligible.dds` | `gfx/achievements/ACH_AFR_NOT_A_MAP_COLOUR.dds`, `gfx/achievements/ACH_AFR_NOT_A_MAP_COLOUR_grey.dds`, `gfx/achievements/ACH_AFR_NOT_A_MAP_COLOUR_not_eligible.dds` | `64x64` | `complete` |
| `ACH_AFR_NO_COUNTERFEIT_CROWNS` | `source_png/ACH_AFR_NO_COUNTERFEIT_CROWNS_source.png` | `processed_png/ACH_AFR_NO_COUNTERFEIT_CROWNS.png`, `processed_png/ACH_AFR_NO_COUNTERFEIT_CROWNS_grey.png`, `processed_png/ACH_AFR_NO_COUNTERFEIT_CROWNS_not_eligible.png` | `dds/ACH_AFR_NO_COUNTERFEIT_CROWNS.dds`, `dds/ACH_AFR_NO_COUNTERFEIT_CROWNS_grey.dds`, `dds/ACH_AFR_NO_COUNTERFEIT_CROWNS_not_eligible.dds` | `gfx/achievements/ACH_AFR_NO_COUNTERFEIT_CROWNS.dds`, `gfx/achievements/ACH_AFR_NO_COUNTERFEIT_CROWNS_grey.dds`, `gfx/achievements/ACH_AFR_NO_COUNTERFEIT_CROWNS_not_eligible.dds` | `64x64` | `complete` |
| `ACH_AFR_OLD_SEATS_NEW_UNION` | `source_png/ACH_AFR_OLD_SEATS_NEW_UNION_source.png` | `processed_png/ACH_AFR_OLD_SEATS_NEW_UNION.png`, `processed_png/ACH_AFR_OLD_SEATS_NEW_UNION_grey.png`, `processed_png/ACH_AFR_OLD_SEATS_NEW_UNION_not_eligible.png` | `dds/ACH_AFR_OLD_SEATS_NEW_UNION.dds`, `dds/ACH_AFR_OLD_SEATS_NEW_UNION_grey.dds`, `dds/ACH_AFR_OLD_SEATS_NEW_UNION_not_eligible.dds` | `gfx/achievements/ACH_AFR_OLD_SEATS_NEW_UNION.dds`, `gfx/achievements/ACH_AFR_OLD_SEATS_NEW_UNION_grey.dds`, `gfx/achievements/ACH_AFR_OLD_SEATS_NEW_UNION_not_eligible.dds` | `64x64` | `complete` |
| `ACH_AFR_OLD_THRONES_VOTE` | `source_png/ACH_AFR_OLD_THRONES_VOTE_source.png` | `processed_png/ACH_AFR_OLD_THRONES_VOTE.png`, `processed_png/ACH_AFR_OLD_THRONES_VOTE_grey.png`, `processed_png/ACH_AFR_OLD_THRONES_VOTE_not_eligible.png` | `dds/ACH_AFR_OLD_THRONES_VOTE.dds`, `dds/ACH_AFR_OLD_THRONES_VOTE_grey.dds`, `dds/ACH_AFR_OLD_THRONES_VOTE_not_eligible.dds` | `gfx/achievements/ACH_AFR_OLD_THRONES_VOTE.dds`, `gfx/achievements/ACH_AFR_OLD_THRONES_VOTE_grey.dds`, `gfx/achievements/ACH_AFR_OLD_THRONES_VOTE_not_eligible.dds` | `64x64` | `complete` |
| `ACH_AFR_THE_ALLIES_SIGN` | `source_png/ACH_AFR_THE_ALLIES_SIGN_source.png` | `processed_png/ACH_AFR_THE_ALLIES_SIGN.png`, `processed_png/ACH_AFR_THE_ALLIES_SIGN_grey.png`, `processed_png/ACH_AFR_THE_ALLIES_SIGN_not_eligible.png` | `dds/ACH_AFR_THE_ALLIES_SIGN.dds`, `dds/ACH_AFR_THE_ALLIES_SIGN_grey.dds`, `dds/ACH_AFR_THE_ALLIES_SIGN_not_eligible.dds` | `gfx/achievements/ACH_AFR_THE_ALLIES_SIGN.dds`, `gfx/achievements/ACH_AFR_THE_ALLIES_SIGN_grey.dds`, `gfx/achievements/ACH_AFR_THE_ALLIES_SIGN_not_eligible.dds` | `64x64` | `complete` |
| `ACH_AFR_THE_FOREST_SIGNED_BACK` | `source_png/ACH_AFR_THE_FOREST_SIGNED_BACK_source.png` | `processed_png/ACH_AFR_THE_FOREST_SIGNED_BACK.png`, `processed_png/ACH_AFR_THE_FOREST_SIGNED_BACK_grey.png`, `processed_png/ACH_AFR_THE_FOREST_SIGNED_BACK_not_eligible.png` | `dds/ACH_AFR_THE_FOREST_SIGNED_BACK.dds`, `dds/ACH_AFR_THE_FOREST_SIGNED_BACK_grey.dds`, `dds/ACH_AFR_THE_FOREST_SIGNED_BACK_not_eligible.dds` | `gfx/achievements/ACH_AFR_THE_FOREST_SIGNED_BACK.dds`, `gfx/achievements/ACH_AFR_THE_FOREST_SIGNED_BACK_grey.dds`, `gfx/achievements/ACH_AFR_THE_FOREST_SIGNED_BACK_not_eligible.dds` | `64x64` | `complete` |
| `ACH_AFR_TIDE_TOOK_THE_PORT` | `source_png/ACH_AFR_TIDE_TOOK_THE_PORT_source.png` | `processed_png/ACH_AFR_TIDE_TOOK_THE_PORT.png`, `processed_png/ACH_AFR_TIDE_TOOK_THE_PORT_grey.png`, `processed_png/ACH_AFR_TIDE_TOOK_THE_PORT_not_eligible.png` | `dds/ACH_AFR_TIDE_TOOK_THE_PORT.dds`, `dds/ACH_AFR_TIDE_TOOK_THE_PORT_grey.dds`, `dds/ACH_AFR_TIDE_TOOK_THE_PORT_not_eligible.dds` | `gfx/achievements/ACH_AFR_TIDE_TOOK_THE_PORT.dds`, `gfx/achievements/ACH_AFR_TIDE_TOOK_THE_PORT_grey.dds`, `gfx/achievements/ACH_AFR_TIDE_TOOK_THE_PORT_not_eligible.dds` | `64x64` | `complete` |
| `ACH_AFR_WHO_GAVE_THEM_A_MICROPHONE` | `source_png/ACH_AFR_WHO_GAVE_THEM_A_MICROPHONE_source.png` | `processed_png/ACH_AFR_WHO_GAVE_THEM_A_MICROPHONE.png`, `processed_png/ACH_AFR_WHO_GAVE_THEM_A_MICROPHONE_grey.png`, `processed_png/ACH_AFR_WHO_GAVE_THEM_A_MICROPHONE_not_eligible.png` | `dds/ACH_AFR_WHO_GAVE_THEM_A_MICROPHONE.dds`, `dds/ACH_AFR_WHO_GAVE_THEM_A_MICROPHONE_grey.dds`, `dds/ACH_AFR_WHO_GAVE_THEM_A_MICROPHONE_not_eligible.dds` | `gfx/achievements/ACH_AFR_WHO_GAVE_THEM_A_MICROPHONE.dds`, `gfx/achievements/ACH_AFR_WHO_GAVE_THEM_A_MICROPHONE_grey.dds`, `gfx/achievements/ACH_AFR_WHO_GAVE_THEM_A_MICROPHONE_not_eligible.dds` | `64x64` | `complete` |

## Review Surfaces

- `review/chaos_refs_sheet.png`
- `review/vanilla_sheet.png`
- `review/current_sheet.png`
- `contact_sheets/source_motifs.png`
- `contact_sheets/final_variants.png`
- `contact_sheets/final_variants_compact.png`

## Validation Notes

- Verified `54` processed PNG variants exist and all report `64x64`.
- Verified `54` package DDS variants exist and all report `DDS 64x64`.
- Verified `54` live DDS variants exist under `gfx/achievements/` and all report `DDS 64x64`.
- No `.gfx`, gameplay, localisation, or shared manifest files were edited in this package.
