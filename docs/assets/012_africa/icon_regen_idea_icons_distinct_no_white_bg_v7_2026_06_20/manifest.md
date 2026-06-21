# Event 012 Africa Idea Icon Regeneration

Event: `12`
Slug: `africa`
Package root: `docs/assets/012_africa/icon_regen_idea_icons_distinct_no_white_bg_v7_2026_06_20/`
Asset type: idea/national-spirit icons
Target size: `64x64`
Source mode: generated symbolic idea-source art, reprocessed from the prior generated idea source PNGs with stricter chroma-key removal, edge decontamination, transparent RGB cleanup, and live DDS replacement.

These are not smaller goal icons. Each idea icon uses its own idea-specific source PNG and compact 64x64 composition. None of the assets in this package is resized, cropped, recolored, padded, or lightly edited from a focus/goal icon.

All assets in this package use transparent unused canvas. The live DDS outputs were written to the existing `gfx/interface/ideas/012_africa/` paths and keep the existing `GFX_idea_africa_*` sprite names from `interface/012_africa.gfx`.

| Asset | Sprite | Source PNG | Processed PNG | Package DDS | Live DDS | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `idea_africa_authority_atlas` | `GFX_idea_africa_authority_atlas` | `source_png/idea_africa_authority_atlas_source.png` | `processed_png/idea_africa_authority_atlas.png` | `dds/idea_africa_authority_atlas.dds` | `gfx/interface/ideas/012_africa/idea_africa_authority_atlas.dds` | `complete` |
| `idea_africa_charter_league` | `GFX_idea_africa_charter_league` | `source_png/idea_africa_charter_league_source.png` | `processed_png/idea_africa_charter_league.png` | `dds/idea_africa_charter_league.dds` | `gfx/interface/ideas/012_africa/idea_africa_charter_league.dds` | `complete` |
| `idea_africa_high_chaos_actor` | `GFX_idea_africa_high_chaos_actor` | `source_png/idea_africa_high_chaos_actor_source.png` | `processed_png/idea_africa_high_chaos_actor.png` | `dds/idea_africa_high_chaos_actor.dds` | `gfx/interface/ideas/012_africa/idea_africa_high_chaos_actor.dds` | `complete` |
| `idea_africa_high_chaos_bestiary` | `GFX_idea_africa_high_chaos_bestiary` | `source_png/idea_africa_high_chaos_bestiary_source.png` | `processed_png/idea_africa_high_chaos_bestiary.png` | `dds/idea_africa_high_chaos_bestiary.dds` | `gfx/interface/ideas/012_africa/idea_africa_high_chaos_bestiary.dds` | `complete` |
| `idea_africa_is_one` | `GFX_idea_africa_is_one` | `source_png/idea_africa_is_one_source.png` | `processed_png/idea_africa_is_one.png` | `dds/idea_africa_is_one.dds` | `gfx/interface/ideas/012_africa/idea_africa_is_one.dds` | `complete` |
| `idea_africa_liberation_war_office` | `GFX_idea_africa_liberation_war_office` | `source_png/idea_africa_liberation_war_office_source.png` | `processed_png/idea_africa_liberation_war_office.png` | `dds/idea_africa_liberation_war_office.dds` | `gfx/interface/ideas/012_africa/idea_africa_liberation_war_office.dds` | `complete` |
| `idea_africa_paper_core_mandate` | `GFX_idea_africa_paper_core_mandate` | `source_png/idea_africa_paper_core_mandate_source.png` | `processed_png/idea_africa_paper_core_mandate.png` | `dds/idea_africa_paper_core_mandate.dds` | `gfx/interface/ideas/012_africa/idea_africa_paper_core_mandate.dds` | `complete` |
| `idea_africa_regional_authority` | `GFX_idea_africa_regional_authority` | `source_png/idea_africa_regional_authority_source.png` | `processed_png/idea_africa_regional_authority.png` | `dds/idea_africa_regional_authority.dds` | `gfx/interface/ideas/012_africa/idea_africa_regional_authority.dds` | `complete` |
| `idea_africa_rsa_continental_emergency` | `GFX_idea_africa_rsa_continental_emergency` | `source_png/idea_africa_rsa_continental_emergency_source.png` | `processed_png/idea_africa_rsa_continental_emergency.png` | `dds/idea_africa_rsa_continental_emergency.dds` | `gfx/interface/ideas/012_africa/idea_africa_rsa_continental_emergency.dds` | `complete` |

## Review Assets

- Processed checker contact sheet: `contact_sheets/idea_icons_processed_checker_contact.png`
- Live DDS checker contact sheet: `contact_sheets/idea_icons_live_dds_checker_contact.png`
- Processed dark contact sheet: `contact_sheets/idea_icons_processed_dark_contact.png`
- Live DDS dark contact sheet: `contact_sheets/idea_icons_live_dds_dark_contact.png`
- Alpha validation: `validation/validation_summary.md`

## Validation Summary

Every processed PNG and live DDS is `64x64`. All four corners are fully transparent. Transparent pixels have black RGB, not a white matte. The validation found zero transparent white RGB pixels, zero low-alpha bright halo pixels, and zero border-connected opaque light-background pixels for every live DDS.
