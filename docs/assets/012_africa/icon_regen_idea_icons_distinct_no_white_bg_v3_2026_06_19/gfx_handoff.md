# 012 Africa Idea Icon Regeneration V3 GFX Handoff

This pass does not require `.gfx` edits. Existing sprite names and texture paths remain unchanged in `interface/012_africa.gfx`.

## Explicit Non-Goal Statement

Every idea icon in this package comes from dedicated Event 012 idea-icon source art and local alpha cleanup. No idea icon derives from a goal icon, goal DDS, or goal package asset. The goal comparison sheet is validation-only proof.

## Final Sprite Targets

| Asset | Sprite name | Final DDS path | Existing `.gfx` file | Related idea / spirit id note | Status |
| --- | --- | --- | --- | --- | --- |
| `idea_africa_authority_atlas` | `GFX_idea_africa_authority_atlas` | `gfx/interface/ideas/012_africa/idea_africa_authority_atlas.dds` | `interface/012_africa.gfx` | Africa authority atlas spirit icon | `complete` |
| `idea_africa_charter_league` | `GFX_idea_africa_charter_league` | `gfx/interface/ideas/012_africa/idea_africa_charter_league.dds` | `interface/012_africa.gfx` | Africa charter league spirit icon | `complete` |
| `idea_africa_high_chaos_actor` | `GFX_idea_africa_high_chaos_actor` | `gfx/interface/ideas/012_africa/idea_africa_high_chaos_actor.dds` | `interface/012_africa.gfx` | Africa high chaos actor spirit icon | `complete` |
| `idea_africa_high_chaos_bestiary` | `GFX_idea_africa_high_chaos_bestiary` | `gfx/interface/ideas/012_africa/idea_africa_high_chaos_bestiary.dds` | `interface/012_africa.gfx` | Africa high chaos bestiary spirit icon | `complete` |
| `idea_africa_is_one` | `GFX_idea_africa_is_one` | `gfx/interface/ideas/012_africa/idea_africa_is_one.dds` | `interface/012_africa.gfx` | Africa is one spirit icon | `complete` |
| `idea_africa_liberation_war_office` | `GFX_idea_africa_liberation_war_office` | `gfx/interface/ideas/012_africa/idea_africa_liberation_war_office.dds` | `interface/012_africa.gfx` | Africa liberation war office spirit icon | `complete` |
| `idea_africa_paper_core_mandate` | `GFX_idea_africa_paper_core_mandate` | `gfx/interface/ideas/012_africa/idea_africa_paper_core_mandate.dds` | `interface/012_africa.gfx` | Africa paper core mandate spirit icon | `complete` |
| `idea_africa_regional_authority` | `GFX_idea_africa_regional_authority` | `gfx/interface/ideas/012_africa/idea_africa_regional_authority.dds` | `interface/012_africa.gfx` | Africa regional authority spirit icon | `complete` |
| `idea_africa_rsa_continental_emergency` | `GFX_idea_africa_rsa_continental_emergency` | `gfx/interface/ideas/012_africa/idea_africa_rsa_continental_emergency.dds` | `interface/012_africa.gfx` | RSA continental emergency spirit icon | `complete` |

## Validation Handoff

- Package DDS files and live DDS files are byte-identical after promotion.
- `file` reports every final live icon as `64 x 64, 32-bit color, ARGB8888`.
- Transparency and hidden-RGB checks are recorded in:
  - `validation/processed_png_validation.json`
  - `validation/live_dds_validation.json`
  - `validation/validation_notes.md`
