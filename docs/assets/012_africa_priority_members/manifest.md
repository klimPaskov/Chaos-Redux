# Event 012 Priority Member Asset Manifest

Status date: 2026-07-18

This manifest covers the bounded visual tranche for the sixteen promoted priority-member packages. It does not claim completion of the full 239-row Event 012 asset matrix.

## Current disposition

- 40 decision-icon source PNGs are present and visually reviewed.
- 40 transparent 32x32 processed PNGs are present.
- 40 uncompressed 32-bit BGRA DDS files are present at their registered runtime paths.
- 40 of the 56 registered priority-member decision sprites therefore resolve to final files.
- The remaining 16 registered decision sprites are package-specific post-settlement icons and have no source art yet.
- The eight focus icons, thirty-five idea icons, four report pictures, sixteen institutional-council portraits, and forty-eight three-size cosmetic flags remain unresolved.
- No generic, resized-from-another-type, or vanilla fallback is wired for an unresolved row.

## Source provenance disposition

The 40 source PNGs were already present in the Event 012 working tree when this processing tranche began. They contain no embedded generator, prompt, author, or licence metadata. Their technical source files are retained, but their original generation record is unresolved. This is a documentation blocker for final Event 012 asset completion and is not silently represented as verified provenance.

## Processing contract

All source files use an opaque magenta production matte. Processing was performed after visual review with this bounded pipeline:

1. Lanczos scale into a 32x32 canvas while preserving aspect ratio.
2. Pad non-square sources with the same production matte.
3. Remove pixels whose red and blue channels jointly exceed green by the reviewed chroma threshold.
4. Zero the removed pixels' RGB values to prevent magenta spill during alpha filtering.
5. Apply a one-pixel alpha-only box filter for a usable game-resolution edge.
6. Convert the processed PNG through `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` at 32x32.

The runtime DDS set is uncompressed 32-bit BGRA with masks `R=0x00FF0000`, `G=0x0000FF00`, `B=0x000000FF`, and `A=0xFF000000`.

## Shared decision icons

All paths below are relative to this asset package for source and processed files. Final files live under `gfx/interface/decisions/012_africa/priority_members/`.

| Asset | Source PNG | Processed PNG | Runtime sprite | Disposition |
|---|---|---|---|---|
| Category | `source_png/decision_012_africa_priority_member_category_source.png` | `processed_png/decision_012_africa_priority_member_category.png` | `GFX_decision_012_africa_priority_member_category` | Final DDS present |
| Ratification | `source_png/decision_012_africa_priority_member_ratification_source.png` | `processed_png/decision_012_africa_priority_member_ratification.png` | `GFX_decision_012_africa_priority_member_ratification` | Final DDS present |
| Political settlement | `source_png/decision_012_africa_priority_member_political_settlement_source.png` | `processed_png/decision_012_africa_priority_member_political_settlement.png` | `GFX_decision_012_africa_priority_member_political_settlement` | Final DDS present |
| League bargain | `source_png/decision_012_africa_priority_member_league_bargain_source.png` | `processed_png/decision_012_africa_priority_member_league_bargain.png` | `GFX_decision_012_africa_priority_member_league_bargain` | Final DDS present |
| Overlap settlement | `source_png/decision_012_africa_priority_member_overlap_settlement_source.png` | `processed_png/decision_012_africa_priority_member_overlap_settlement.png` | `GFX_decision_012_africa_priority_member_overlap_settlement` | Final DDS present |
| Departure terms | `source_png/decision_012_africa_priority_member_departure_terms_source.png` | `processed_png/decision_012_africa_priority_member_departure_terms.png` | `GFX_decision_012_africa_priority_member_departure_terms` | Final DDS present |
| Withdrawal recall | `source_png/decision_012_africa_priority_member_withdrawal_recall_source.png` | `processed_png/decision_012_africa_priority_member_withdrawal_recall.png` | `GFX_decision_012_africa_priority_member_withdrawal_recall` | Final DDS present |
| Withdrawal mission | `source_png/decision_012_africa_priority_member_withdrawal_mission_source.png` | `processed_png/decision_012_africa_priority_member_withdrawal_mission.png` | `GFX_decision_012_africa_priority_member_withdrawal_mission` | Final DDS present |

## Package-specific decision icons

For each package key below, the source, processed, final, and sprite names are exact applications of these stable patterns:

- mechanic source: `source_png/decision_012_africa_priority_member_mechanic_<key>_source.png`
- mechanic processed: `processed_png/decision_012_africa_priority_member_mechanic_<key>.png`
- mechanic final: `decision_012_africa_priority_member_mechanic_<key>.dds`
- mechanic sprite: `GFX_decision_012_africa_priority_member_mechanic_<key>`
- force source: `source_png/decision_012_africa_priority_member_force_<key>_source.png`
- force processed: `processed_png/decision_012_africa_priority_member_force_<key>.png`
- force final: `decision_012_africa_priority_member_force_<key>.dds`
- force sprite: `GFX_decision_012_africa_priority_member_force_<key>`

| Package key | Mechanic | Force | Post-settlement |
|---|---|---|---|
| `asante` | Final DDS present | Final DDS present | Registered; source and final missing |
| `oyo` | Final DDS present | Final DDS present | Registered; source and final missing |
| `sokoto` | Final DDS present | Final DDS present | Registered; source and final missing |
| `kanem_bornu` | Final DDS present | Final DDS present | Registered; source and final missing |
| `manden` | Final DDS present | Final DDS present | Registered; source and final missing |
| `kongo` | Final DDS present | Final DDS present | Registered; source and final missing |
| `buganda` | Final DDS present | Final DDS present | Registered; source and final missing |
| `aksum` | Final DDS present | Final DDS present | Registered; source and final missing |
| `harar` | Final DDS present | Final DDS present | Registered; source and final missing |
| `kilwa` | Final DDS present | Final DDS present | Registered; source and final missing |
| `nubia` | Final DDS present | Final DDS present | Registered; source and final missing |
| `luba` | Final DDS present | Final DDS present | Registered; source and final missing |
| `lunda` | Final DDS present | Final DDS present | Registered; source and final missing |
| `great_zimbabwe` | Final DDS present | Final DDS present | Registered; source and final missing |
| `merina` | Final DDS present | Final DDS present | Registered; source and final missing |
| `zulu` | Final DDS present | Final DDS present | Registered; source and final missing |

## Unresolved registered surfaces

| Surface | Count | Stable registration | Disposition |
|---|---:|---|---|
| Package post-settlement decisions | 16 | `interface/012_africa_priority_member_assets.gfx` | Source, processed PNG, and final DDS missing; queued for original art |
| Shared focus overlay | 8 | `interface/012_africa_priority_member_assets.gfx` | Source, processed PNG, and final DDS missing; queued for original art |
| Lifecycle ideas | 35 | `interface/012_africa_priority_member_assets.gfx` | Source, processed PNG, and final DDS missing; queued for original art |
| Priority report events | 4 | `interface/012_africa_priority_member_assets.gfx` | Source, processed PNG, and final DDS missing; queued for original art |
| Institutional councils | 16 | `interface/012_africa_priority_member_characters.gfx` | People-free portrait source, processed PNG, and final DDS missing |
| Cosmetic flags | 48 | Country definitions and three flag-size folders | Base, medium, and small files missing for all sixteen identities |

The unresolved rows remain blockers. Nothing in this manifest promotes them to complete merely because their sprite IDs or filenames are known.
