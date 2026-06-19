# 012 Africa Idea Icon Regeneration V3 Manifest

- Event id: `012`
- Event slug: `africa`
- Package path: `docs/assets/012_africa/icon_regen_idea_icons_distinct_no_white_bg_v3_2026_06_19/`
- Asset type: idea / national-spirit icons
- Target size: `64x64`
- Final DDS folder: `gfx/interface/ideas/012_africa/`
- Existing sprite file kept unchanged: `interface/012_africa.gfx`
- Reference folder inspected: `.agents/skills/chaos-redux-event-assets/assets/ideas`
- Source mode: dedicated Event 012 idea-icon source art, then local alpha cleanup, compact spirit-icon recomposition, and DDS rebuild
- Status: `complete`

## Distinct-Idea Rule

These nine icons are compact idea / national-spirit icons and are not smaller goal icons.

No v3 asset was cropped, resized, recolored, padded, or lightly edited from `gfx/interface/goals/012_africa/` or any goal-icon package. The `goal_vs_idea_distinctness_sheet.png` contact sheet exists only as validation proof. It was not used as source art.

## Processing Summary

- Preserved dedicated idea-icon source PNGs in `source_png/`.
- Removed border-connected chroma-key backgrounds and white/off-white matte residue.
- Recentered each subject onto a transparent `64x64` canvas sized for HOI4 idea-icon readability instead of focus-icon composition.
- Added a narrow dark outline and soft shadow for variable UI backgrounds.
- Zeroed RGB on fully transparent pixels to prevent hidden white bleed in DDS consumers.
- Converted final package and live files to `64x64` `ARGB8888` DDS with unchanged filenames and sprite names.

## Asset List

| Asset name | Intended use | Source note | Source PNG | Processed PNG | Package DDS | Live DDS | Sprite name | Target size | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `idea_africa_authority_atlas` | idea / national spirit | dedicated atlas-book source art with brass compass and route marks; compact book emblem, not the goal atlas composition | `source_png/idea_africa_authority_atlas_source.png` | `processed_png/idea_africa_authority_atlas.png` | `dds/idea_africa_authority_atlas.dds` | `gfx/interface/ideas/012_africa/idea_africa_authority_atlas.dds` | `GFX_idea_africa_authority_atlas` | `64x64` | `complete` |
| `idea_africa_charter_league` | idea / national spirit | dedicated treaty-ribbon and congress-seal source art; compact heraldic knot, not the handshake goal icon | `source_png/idea_africa_charter_league_source.png` | `processed_png/idea_africa_charter_league.png` | `dds/idea_africa_charter_league.dds` | `gfx/interface/ideas/012_africa/idea_africa_charter_league.dds` | `GFX_idea_africa_charter_league` | `64x64` | `complete` |
| `idea_africa_high_chaos_actor` | idea / national spirit | dedicated carved mask and court-token source art; compact uncanny mask emblem | `source_png/idea_africa_high_chaos_actor_source.png` | `processed_png/idea_africa_high_chaos_actor.png` | `dds/idea_africa_high_chaos_actor.dds` | `gfx/interface/ideas/012_africa/idea_africa_high_chaos_actor.dds` | `GFX_idea_africa_high_chaos_actor` | `64x64` | `complete` |
| `idea_africa_high_chaos_bestiary` | idea / national spirit | dedicated claw-slashed bestiary and eye source art; compact occult book emblem, not the larger goal-mask silhouette | `source_png/idea_africa_high_chaos_bestiary_source.png` | `processed_png/idea_africa_high_chaos_bestiary.png` | `dds/idea_africa_high_chaos_bestiary.dds` | `gfx/interface/ideas/012_africa/idea_africa_high_chaos_bestiary.dds` | `GFX_idea_africa_high_chaos_bestiary` | `64x64` | `complete` |
| `idea_africa_is_one` | idea / national spirit | dedicated joined-hands continent seal source art; compact unity emblem distinct from the regional focus-family map art | `source_png/idea_africa_is_one_source.png` | `processed_png/idea_africa_is_one.png` | `dds/idea_africa_is_one.dds` | `gfx/interface/ideas/012_africa/idea_africa_is_one.dds` | `GFX_idea_africa_is_one` | `64x64` | `complete` |
| `idea_africa_liberation_war_office` | idea / national spirit | dedicated broken-chain dispatch satchel source art; compact wartime office emblem, not the camp-scene goal icon | `source_png/idea_africa_liberation_war_office_source.png` | `processed_png/idea_africa_liberation_war_office.png` | `dds/idea_africa_liberation_war_office.dds` | `gfx/interface/ideas/012_africa/idea_africa_liberation_war_office.dds` | `GFX_idea_africa_liberation_war_office` | `64x64` | `complete` |
| `idea_africa_paper_core_mandate` | idea / national spirit | dedicated curled mandate parchment and archival spindle source art; compact paper-seal emblem | `source_png/idea_africa_paper_core_mandate_source.png` | `processed_png/idea_africa_paper_core_mandate.png` | `dds/idea_africa_paper_core_mandate.dds` | `gfx/interface/ideas/012_africa/idea_africa_paper_core_mandate.dds` | `GFX_idea_africa_paper_core_mandate` | `64x64` | `complete` |
| `idea_africa_regional_authority` | idea / national spirit | dedicated ledger-keys-seal source art; compact administrative emblem distinct from the regional integration goal map | `source_png/idea_africa_regional_authority_source.png` | `processed_png/idea_africa_regional_authority.png` | `dds/idea_africa_regional_authority.dds` | `gfx/interface/ideas/012_africa/idea_africa_regional_authority.dds` | `GFX_idea_africa_regional_authority` | `64x64` | `complete` |
| `idea_africa_rsa_continental_emergency` | idea / national spirit | dedicated cracked shield and emergency flare source art; compact crisis emblem with southern-Africa map plate | `source_png/idea_africa_rsa_continental_emergency_source.png` | `processed_png/idea_africa_rsa_continental_emergency.png` | `dds/idea_africa_rsa_continental_emergency.dds` | `gfx/interface/ideas/012_africa/idea_africa_rsa_continental_emergency.dds` | `GFX_idea_africa_rsa_continental_emergency` | `64x64` | `complete` |

## Validation Evidence

- Processed PNG contact sheets:
  - `contact_sheets/processed_checker_sheet.png`
  - `contact_sheets/processed_dark_sheet.png`
- Package DDS roundtrip contact sheets:
  - `contact_sheets/dds_roundtrip_checker_sheet.png`
  - `contact_sheets/dds_roundtrip_dark_sheet.png`
- Live DDS roundtrip contact sheets:
  - `contact_sheets/live_dds_roundtrip_checker_sheet.png`
  - `contact_sheets/live_dds_roundtrip_dark_sheet.png`
- Distinctness proof sheet:
  - `contact_sheets/goal_vs_idea_distinctness_sheet.png`
- Validation files:
  - `validation/processed_png_validation.json`
  - `validation/live_dds_validation.json`
  - `validation/validation_notes.md`
  - `validation/validation_summary.txt`

## Validation Summary

All nine processed PNGs and all nine live DDS files:

- exist at the exact `64x64` target size
- report transparent corners
- have fully transparent unused canvas
- have RGB cleared under `alpha=0`
- have no border white-matte pixels detected in the live DDS validation

No `.gfx`, localisation, gameplay, focus, idea, decision, event, GUI, script, history, spreadsheet, or unrelated asset files were edited during this pass.
