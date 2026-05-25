# Event 005 UDC Generated Ideology Flag Sidecar Manifest

Date: 2026-05-25

Scope: bounded generated-art sidecar for the Union Defense Committee (`UDC`) ideology flag variants only. This package did not edit gameplay, localisation, `.gfx`, focus, decision, event, history, country, spreadsheet, active `gfx/flags/**`, or active `gfx/leaders/**` files.

## References

- `AGENTS.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `/home/klim/.codex/skills/.system/imagegen/SKILL.md`
- `tmp/soviet_collapse_final_clean_merged_spec_package/specs/005_soviet_union_collapse_final_clean_merged_part_6_countries_splinters_restorations.md`
- `tmp/soviet_collapse_final_clean_merged_spec_package/specs/005_soviet_union_collapse_final_clean_merged_part_7_assets_achievements_validation.md`
- `.agents/skills/chaos-redux-event-assets/assets/flags/`
- `docs/assets/005_soviet_union_collapse/generated_flag_replacements/manifest.md`
- `docs/assets/005_soviet_union_collapse/leader_portrait_recovery_2026_05_25/manifest.md`

The required offline HOI4 wiki pages and vanilla documentation were opened for repository compliance. This pass touched only generated sidecar assets and scoped asset documentation.

## Why Generation Is Appropriate

`UDC` is a fictional Union Defense Committee / non-Moscow Soviet continuity authority from the Event 005 high-chaos splinter set. The requested variants are fictional ideology handoff assets, not historical flags or real leader portraits.

## Inventory Result

- Active `UDC` normal, medium, and small base/ideology TGA files already exist and are currently dirty in the worktree.
- Those active files were intentionally not overwritten.
- Existing sidecar audits identified `UDC` as a generated-source gap after `SOG`, while `CFR`, `KRS`, `RMC`, `SDZ`, and most `TSC` ideology variants already had generated source coverage.
- `ALN`, `KHW`, and `KZR` remain blocked for this generated-art subagent because they are ancient/restoration-state flags with historical-symbol uncertainty. They should be routed to source research unless the parent explicitly frames the needed ideology variants as fictional/alternate-history inventions.

## Generated Assets

| Asset | Asset type | Source mode | Source PNG | Processed PNG previews | Review TGA outputs | Review DDS outputs | Target sizes | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `UDC_communism` | fictional ideology flag | `$imagegen` | `source_png/UDC_communism_source.png` | `processed_png/UDC_communism_<normal|medium|small>.png` | `tga/UDC_communism_<normal|medium|small>.tga` | `dds/UDC_communism_<normal|medium|small>.dds` | 82x52, 41x26, 10x7 | handed_off |
| `UDC_democratic` | fictional ideology flag | `$imagegen` | `source_png/UDC_democratic_source.png` | `processed_png/UDC_democratic_<normal|medium|small>.png` | `tga/UDC_democratic_<normal|medium|small>.tga` | `dds/UDC_democratic_<normal|medium|small>.dds` | 82x52, 41x26, 10x7 | handed_off |
| `UDC_fascism` | fictional ideology flag | `$imagegen` | `source_png/UDC_fascism_source.png` | `processed_png/UDC_fascism_<normal|medium|small>.png` | `tga/UDC_fascism_<normal|medium|small>.tga` | `dds/UDC_fascism_<normal|medium|small>.dds` | 82x52, 41x26, 10x7 | handed_off |
| `UDC_neutrality` | fictional ideology flag | `$imagegen` | `source_png/UDC_neutrality_source.png` | `processed_png/UDC_neutrality_<normal|medium|small>.png` | `tga/UDC_neutrality_<normal|medium|small>.tga` | `dds/UDC_neutrality_<normal|medium|small>.dds` | 82x52, 41x26, 10x7 | handed_off |

Full generated sheet:

- `source_png/UDC_ideology_sheet_source.png`

Prompt log:

- `prompts/UDC_ideology_flags_prompt.md`

## Contact Sheets And Checks

- Large contact sheet: `contact_sheets/UDC_ideology_flags_large_contact_sheet.png`
- Normal contact sheet: `contact_sheets/UDC_ideology_flags_normal_contact_sheet.png`
- Small contact sheet: `contact_sheets/UDC_ideology_flags_small_contact_sheet.png`
- Size audit: `notes/identify_outputs.txt`

Validation:

- Normal outputs are 82x52.
- Medium outputs are 41x26.
- Small outputs are 10x7.
- Review TGA outputs are 32-bit truecolor TGA, descriptor `8`, bottom-left origin.
- The four generated ideology variants are visually distinct, upright, and not byte-identical.
- No base `UDC.tga` replacement was produced.

## Blocked Or Deferred Assets

- `ALN`, `KHW`, and `KZR` generated/restoration flag work is blocked for this subagent because the spec says ancient and medieval restoration countries should use sourced historical symbols where possible. Route these to `chaosx_asset_source_researcher` or explicitly reframe them as fictional ideology variants before generation.
- No new leader or council portraits were produced because the current active Event 005 leader portrait inventory is already covered by `gfx/leaders/005_soviet_collapse/*_leader.dds` and the prior recovery sidecar.

