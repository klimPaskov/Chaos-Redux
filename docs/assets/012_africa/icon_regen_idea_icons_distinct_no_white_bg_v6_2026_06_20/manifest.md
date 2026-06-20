# Event 012 Africa Idea Icon Regeneration v6

- Event id: `012`
- Event slug: `africa`
- Package path: `docs/assets/012_africa/icon_regen_idea_icons_distinct_no_white_bg_v6_2026_06_20/`
- Asset type: `idea / national-spirit icons`
- Target size: `64x64`
- Source mode: generated symbolic spirit art through built-in `image_gen` and `chaosx_icon_artist` source outputs, copied into this package and processed with local chroma-key alpha extraction.
- Final DDS folder: `gfx/interface/ideas/012_africa/`
- Existing `.gfx` file kept unchanged: `interface/012_africa.gfx`
- Status: `complete` for all 9 live Event 012 Africa idea icons.

Asset-type separation note: these are distinct `64x64` spirit-style source artworks. They are not resized, cropped, recolored, padded, or lightly edited focus/goal icons.

## Assets

| Asset | Sprite | Intended use | Final source subject | Source PNG | Processed PNG | Package DDS | Live DDS | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `idea_africa_is_one` | `GFX_idea_africa_is_one` | Africa Is One and general congress spirits | interlocked Africa unity emblem | `source_png/idea_africa_is_one_source.png` | `processed_png/idea_africa_is_one.png` | `dds/idea_africa_is_one.dds` | `gfx/interface/ideas/012_africa/idea_africa_is_one.dds` | `complete` |
| `idea_africa_paper_core_mandate` | `GFX_idea_africa_paper_core_mandate` | paper-core mandate spirit | bound paper mandate scrolls and wax seal | `source_png/idea_africa_paper_core_mandate_source.png` | `processed_png/idea_africa_paper_core_mandate.png` | `dds/idea_africa_paper_core_mandate.dds` | `gfx/interface/ideas/012_africa/idea_africa_paper_core_mandate.dds` | `complete` |
| `idea_africa_charter_league` | `GFX_idea_africa_charter_league` | Charter League and federal charter spirits | compact charter shield and knot clasp | `source_png/idea_africa_charter_league_source.png` | `processed_png/idea_africa_charter_league.png` | `dds/idea_africa_charter_league.dds` | `gfx/interface/ideas/012_africa/idea_africa_charter_league.dds` | `complete` |
| `idea_africa_authority_atlas` | `GFX_idea_africa_authority_atlas` | Authority Atlas and origin spirits | compact atlas compass medallion | `source_png/idea_africa_authority_atlas_source.png` | `processed_png/idea_africa_authority_atlas.png` | `dds/idea_africa_authority_atlas.dds` | `gfx/interface/ideas/012_africa/idea_africa_authority_atlas.dds` | `complete` |
| `idea_africa_liberation_war_office` | `GFX_idea_africa_liberation_war_office` | Liberation War Office spirit | chain-bound operations papers and seal | `source_png/idea_africa_liberation_war_office_source.png` | `processed_png/idea_africa_liberation_war_office.png` | `dds/idea_africa_liberation_war_office.dds` | `gfx/interface/ideas/012_africa/idea_africa_liberation_war_office.dds` | `complete` |
| `idea_africa_high_chaos_bestiary` | `GFX_idea_africa_high_chaos_bestiary` | high-chaos Bestiary spirit | small fictional bestiary mask | `source_png/idea_africa_high_chaos_bestiary_source.png` | `processed_png/idea_africa_high_chaos_bestiary.png` | `dds/idea_africa_high_chaos_bestiary.dds` | `gfx/interface/ideas/012_africa/idea_africa_high_chaos_bestiary.dds` | `complete` |
| `idea_africa_regional_authority` | `GFX_idea_africa_regional_authority` | regional authority and seat spirits | round regional network medallion | `source_png/idea_africa_regional_authority_source.png` | `processed_png/idea_africa_regional_authority.png` | `dds/idea_africa_regional_authority.dds` | `gfx/interface/ideas/012_africa/idea_africa_regional_authority.dds` | `complete` |
| `idea_africa_high_chaos_actor` | `GFX_idea_africa_high_chaos_actor` | high-chaos actor and seat spirits | fictional nonhuman mask emblem | `source_png/idea_africa_high_chaos_actor_source.png` | `processed_png/idea_africa_high_chaos_actor.png` | `dds/idea_africa_high_chaos_actor.dds` | `gfx/interface/ideas/012_africa/idea_africa_high_chaos_actor.dds` | `complete` |
| `idea_africa_rsa_continental_emergency` | `GFX_idea_africa_rsa_continental_emergency` | RSA continental emergency spirits | cracked Africa shield and beacon | `source_png/idea_africa_rsa_continental_emergency_source.png` | `processed_png/idea_africa_rsa_continental_emergency.png` | `dds/idea_africa_rsa_continental_emergency.dds` | `gfx/interface/ideas/012_africa/idea_africa_rsa_continental_emergency.dds` | `complete` |

## Processing

- Source PNGs were copied into `source_png/`; original generated-image cache files were left in place.
- Chroma-key backgrounds were removed into real alpha with the installed imagegen chroma-key helper.
- Icons were centered on transparent `64x64` canvases and transparent pixels were blackened under alpha to prevent matte bleed.
- DDS outputs were converted as uncompressed ARGB8888 through ImageMagick because `.tools/convert_to_dds.py` still hits the known ffmpeg fallback header bug in this environment.
- The live DDS filenames and sprite names did not change.

## Validation

- `validation/all_idea_alpha_metrics.tsv`
- `validation/all_idea_alpha_validation.md`
- `contact_sheets/idea_icons_processed_checker_contact.png`
- `contact_sheets/idea_icons_processed_dark_contact.png`
- `contact_sheets/idea_icons_live_dds_checker_contact.png`
- `contact_sheets/idea_icons_live_dds_dark_contact.png`

All 9 processed PNGs and all 9 live DDS reads are `64x64`, have fully transparent corners, have no fully transparent white-RGB pixels, have no near-white halo pixels adjacent to transparency, and have no border-connected white/off-white matte pixels.

## Blockers

None for this asset family.
