# Event 012 Africa Idea Icon Regeneration Manifest

Package: `icon_regen_idea_icons_distinct_no_white_bg_v5_2026_06_20`

Scope: regenerated Event 012 Africa idea and national spirit icons only. Focus/goal icons are a separate package and must not be treated as sources for these assets.

Source mode: generated symbolic icon art through `chaosx_icon_artist`.

DDS conversion: local ImageMagick fallback, `convert <processed_png> -define dds:compression=none <dds>`, after `.tools/convert_to_dds.py` hit its known ffmpeg fallback `struct.pack` issue in this environment.

Status: complete for the nine idea/national-spirit icons listed below.

| Asset | Intended use | Source PNG | Processed PNG | Package DDS | Live DDS | Sprite | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `idea_africa_is_one` | `africa_is_one_spirit`, origin general congress spirit | `source_png/idea_africa_is_one_source.png` | `processed_png/idea_africa_is_one.png` | `dds/idea_africa_is_one.dds` | `gfx/interface/ideas/012_africa/idea_africa_is_one.dds` | `GFX_idea_africa_is_one` | complete |
| `idea_africa_paper_core_mandate` | paper-core mandate spirit | `source_png/idea_africa_paper_core_mandate_source.png` | `processed_png/idea_africa_paper_core_mandate.png` | `dds/idea_africa_paper_core_mandate.dds` | `gfx/interface/ideas/012_africa/idea_africa_paper_core_mandate.dds` | `GFX_idea_africa_paper_core_mandate` | complete |
| `idea_africa_charter_league` | Charter League and federal charter spirits | `source_png/idea_africa_charter_league_source.png` | `processed_png/idea_africa_charter_league.png` | `dds/idea_africa_charter_league.dds` | `gfx/interface/ideas/012_africa/idea_africa_charter_league.dds` | `GFX_idea_africa_charter_league` | complete |
| `idea_africa_authority_atlas` | Authority Atlas and related origin spirits | `source_png/idea_africa_authority_atlas_source.png` | `processed_png/idea_africa_authority_atlas.png` | `dds/idea_africa_authority_atlas.dds` | `gfx/interface/ideas/012_africa/idea_africa_authority_atlas.dds` | `GFX_idea_africa_authority_atlas` | complete |
| `idea_africa_liberation_war_office` | liberation war office spirit | `source_png/idea_africa_liberation_war_office_source.png` | `processed_png/idea_africa_liberation_war_office.png` | `dds/idea_africa_liberation_war_office.dds` | `gfx/interface/ideas/012_africa/idea_africa_liberation_war_office.dds` | `GFX_idea_africa_liberation_war_office` | complete |
| `idea_africa_high_chaos_bestiary` | high-chaos bestiary and forest/river origin spirits | `source_png/idea_africa_high_chaos_bestiary_source.png` | `processed_png/idea_africa_high_chaos_bestiary.png` | `dds/idea_africa_high_chaos_bestiary.dds` | `gfx/interface/ideas/012_africa/idea_africa_high_chaos_bestiary.dds` | `GFX_idea_africa_high_chaos_bestiary` | complete |
| `idea_africa_regional_authority` | regional authority subject spirit | `source_png/idea_africa_regional_authority_source.png` | `processed_png/idea_africa_regional_authority.png` | `dds/idea_africa_regional_authority.dds` | `gfx/interface/ideas/012_africa/idea_africa_regional_authority.dds` | `GFX_idea_africa_regional_authority` | complete |
| `idea_africa_high_chaos_actor` | high-chaos actor role spirit | `source_png/idea_africa_high_chaos_actor_source.png` | `processed_png/idea_africa_high_chaos_actor.png` | `dds/idea_africa_high_chaos_actor.dds` | `gfx/interface/ideas/012_africa/idea_africa_high_chaos_actor.dds` | `GFX_idea_africa_high_chaos_actor` | complete |
| `idea_africa_rsa_continental_emergency` | RSA continental emergency spirit | `source_png/idea_africa_rsa_continental_emergency_source.png` | `processed_png/idea_africa_rsa_continental_emergency.png` | `dds/idea_africa_rsa_continental_emergency.dds` | `gfx/interface/ideas/012_africa/idea_africa_rsa_continental_emergency.dds` | `GFX_idea_africa_rsa_continental_emergency` | complete |

Prompt records: `prompts/generated_prompts.md`.

Validation records:

- `validation/final_alpha_metrics.tsv`
- `validation/final_alpha_validation.md`

Asset-type separation note: these assets were generated from idea/national-spirit briefs and target `64x64` spirit readability. They are not resized, cropped, padded, recolored, or otherwise derived from Event 012 focus/goal icons.
