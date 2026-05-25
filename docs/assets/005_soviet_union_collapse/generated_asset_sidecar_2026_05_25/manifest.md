# Event 005 Generated Asset Sidecar Manifest

Audit date: 2026-05-25

Scope: Event 005 Soviet Collapse generated leader/council portrait and flag sidecar. This pass did not edit gameplay, focus, localisation, GUI, `.gfx`, event, decision, idea, history, country, or spreadsheet files.

## References

- `AGENTS.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `/home/klim/.codex/skills/.system/imagegen/SKILL.md`
- `tmp/soviet_collapse_final_clean_merged_spec_package/specs/005_soviet_union_collapse_final_clean_merged_part_7_assets_achievements_validation.md`
- `.agents/skills/chaos-redux-event-assets/assets/flags/`
- `docs/assets/005_soviet_union_collapse/manifest.md`
- `docs/assets/005_soviet_union_collapse/generated_asset_handoff_2026_05_25/manifest.md`
- `gfx/leaders/005_soviet_collapse/`
- `gfx/flags/`, `gfx/flags/medium/`, `gfx/flags/small/`

The required offline HOI4 wiki pages and vanilla documentation were opened for repository compliance. This pass touched only asset outputs and asset documentation.

## Inventory Result

- Active Event 005 generated or council portraits remain covered. The latest repo audit lists no missing active portrait DDS files, no duplicate active portrait hashes, and no vanilla leader hash matches across current `gfx/leaders/005_soviet_collapse/*_leader.dds`.
- Inactive deleted portrait files for `BEC`, `BLT`, `COU`, `ILU`, and `IRA` were not regenerated because the current sidecars report no active references. If those tags return to active use, they need unique fictional council portraits.
- Active custom and route flag files are present across normal, medium, and small sizes. Existing-game countries keep vanilla base flags; this pass did not create `UKR`, `BLR`, `KAZ`, `MOL`, `UZB`, `TAJ`, `TMS`, or `FER` default overrides.
- Priority generated work from the current repo state: `PRA` full flag-family visual-quality redo, `MFR` ideology-variant polish, and `UKR_BLACK_BANNER` ideology source-sidecar repair.

## Generated and Processed Assets

Flags use HOI4 final TGA outputs rather than DDS. All final TGA files keep the existing active filenames and therefore need no `.gfx` changes.

| Asset | Type | Source mode | Source PNG | Processed PNG previews | Final normal | Final medium | Final small | Target sizes | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `PRA` | fictional base flag | `$imagegen` | `docs/assets/005_soviet_union_collapse/generated_asset_sidecar_2026_05_25/source_png/PRA_source.png` | `.../processed_png/PRA_<normal|medium|small>.png` | `gfx/flags/PRA.tga` | `gfx/flags/medium/PRA.tga` | `gfx/flags/small/PRA.tga` | 82x52, 41x26, 10x7 | complete |
| `PRA_communism` | fictional ideology flag | `$imagegen` | `docs/assets/005_soviet_union_collapse/generated_asset_sidecar_2026_05_25/source_png/PRA_communism_source.png` | `.../processed_png/PRA_communism_<normal|medium|small>.png` | `gfx/flags/PRA_communism.tga` | `gfx/flags/medium/PRA_communism.tga` | `gfx/flags/small/PRA_communism.tga` | 82x52, 41x26, 10x7 | complete |
| `PRA_democratic` | fictional ideology flag | `$imagegen` | `docs/assets/005_soviet_union_collapse/generated_asset_sidecar_2026_05_25/source_png/PRA_democratic_source.png` | `.../processed_png/PRA_democratic_<normal|medium|small>.png` | `gfx/flags/PRA_democratic.tga` | `gfx/flags/medium/PRA_democratic.tga` | `gfx/flags/small/PRA_democratic.tga` | 82x52, 41x26, 10x7 | complete |
| `PRA_fascism` | fictional ideology flag | `$imagegen` | `docs/assets/005_soviet_union_collapse/generated_asset_sidecar_2026_05_25/source_png/PRA_fascism_source.png` | `.../processed_png/PRA_fascism_<normal|medium|small>.png` | `gfx/flags/PRA_fascism.tga` | `gfx/flags/medium/PRA_fascism.tga` | `gfx/flags/small/PRA_fascism.tga` | 82x52, 41x26, 10x7 | complete |
| `PRA_neutrality` | fictional ideology flag | `$imagegen` | `docs/assets/005_soviet_union_collapse/generated_asset_sidecar_2026_05_25/source_png/PRA_neutrality_source.png` | `.../processed_png/PRA_neutrality_<normal|medium|small>.png` | `gfx/flags/PRA_neutrality.tga` | `gfx/flags/medium/PRA_neutrality.tga` | `gfx/flags/small/PRA_neutrality.tga` | 82x52, 41x26, 10x7 | complete |
| `MFR_communism` | fictional ideology flag | `$imagegen` | `docs/assets/005_soviet_union_collapse/generated_asset_sidecar_2026_05_25/source_png/MFR_communism_source.png` | `.../processed_png/MFR_communism_<normal|medium|small>.png` | `gfx/flags/MFR_communism.tga` | `gfx/flags/medium/MFR_communism.tga` | `gfx/flags/small/MFR_communism.tga` | 82x52, 41x26, 10x7 | complete |
| `MFR_democratic` | fictional ideology flag | `$imagegen` | `docs/assets/005_soviet_union_collapse/generated_asset_sidecar_2026_05_25/source_png/MFR_democratic_source.png` | `.../processed_png/MFR_democratic_<normal|medium|small>.png` | `gfx/flags/MFR_democratic.tga` | `gfx/flags/medium/MFR_democratic.tga` | `gfx/flags/small/MFR_democratic.tga` | 82x52, 41x26, 10x7 | complete |
| `MFR_fascism` | fictional ideology flag | `$imagegen` | `docs/assets/005_soviet_union_collapse/generated_asset_sidecar_2026_05_25/source_png/MFR_fascism_source.png` | `.../processed_png/MFR_fascism_<normal|medium|small>.png` | `gfx/flags/MFR_fascism.tga` | `gfx/flags/medium/MFR_fascism.tga` | `gfx/flags/small/MFR_fascism.tga` | 82x52, 41x26, 10x7 | complete |
| `MFR_neutrality` | fictional ideology flag | `$imagegen` | `docs/assets/005_soviet_union_collapse/generated_asset_sidecar_2026_05_25/source_png/MFR_neutrality_source.png` | `.../processed_png/MFR_neutrality_<normal|medium|small>.png` | `gfx/flags/MFR_neutrality.tga` | `gfx/flags/medium/MFR_neutrality.tga` | `gfx/flags/small/MFR_neutrality.tga` | 82x52, 41x26, 10x7 | complete |
| `UKR_BLACK_BANNER_communism` | route ideology source repair | existing generated strip | `docs/assets/005_soviet_union_collapse/source_png/generated_custom_ideology_flags/UKR_BLACK_BANNER_communism_source.png` | existing generated ideology previews | existing active TGA unchanged | existing active TGA unchanged | existing active TGA unchanged | source crop only | complete |
| `UKR_BLACK_BANNER_democratic` | route ideology source repair | existing generated strip | `docs/assets/005_soviet_union_collapse/source_png/generated_custom_ideology_flags/UKR_BLACK_BANNER_democratic_source.png` | existing generated ideology previews | existing active TGA unchanged | existing active TGA unchanged | existing active TGA unchanged | source crop only | complete |
| `UKR_BLACK_BANNER_fascism` | route ideology source repair | existing generated strip | `docs/assets/005_soviet_union_collapse/source_png/generated_custom_ideology_flags/UKR_BLACK_BANNER_fascism_source.png` | existing generated ideology previews | existing active TGA unchanged | existing active TGA unchanged | existing active TGA unchanged | source crop only | complete |
| `UKR_BLACK_BANNER_neutrality` | route ideology source repair | existing generated strip | `docs/assets/005_soviet_union_collapse/source_png/generated_custom_ideology_flags/UKR_BLACK_BANNER_neutrality_source.png` | existing generated ideology previews | existing active TGA unchanged | existing active TGA unchanged | existing active TGA unchanged | source crop only | complete |

## Prompt Summaries

- `PRA`: five distinct fictional Pale Railway Authority flag panels with rail tracks, signal lamps, switch keys, station clocks, telegraph lines, depot seals, and period 1930s-1940s railway authority heraldry; no text, no real-country flag copying, no recolor-only variants.
- `MFR`: four distinct fictional Munitions Factory Republic ideology flag panels with factory rooflines, gear-and-shell emblems, cranes, safety chevrons, smokestacks, rivets, arsenal keys, and workers' council seal motifs; no text, no real-country flag copying, no recolor-only variants.

## Contact Sheets and Validation

- Normal sheet: `docs/assets/005_soviet_union_collapse/generated_asset_sidecar_2026_05_25/contact_sheets/pra_mfr_generated_flag_normals.png`
- Medium sheet: `docs/assets/005_soviet_union_collapse/generated_asset_sidecar_2026_05_25/contact_sheets/pra_mfr_generated_flag_mediums.png`
- Small sheet: `docs/assets/005_soviet_union_collapse/generated_asset_sidecar_2026_05_25/contact_sheets/pra_mfr_generated_flag_smalls.png`
- Size audit: `docs/assets/005_soviet_union_collapse/generated_asset_sidecar_2026_05_25/notes/identify_outputs.txt`
- TGA header audit: `docs/assets/005_soviet_union_collapse/generated_asset_sidecar_2026_05_25/notes/tga_header_checks.txt`

Validation result: touched final flag TGAs are present at expected dimensions. Normal and medium outputs are 32-bit TGA with descriptor `8`; small outputs were re-exported as 32-bit truecolor TGA with descriptor `8` after the first export palette-optimized them. Focused hash audit found no duplicate hashes among the touched PRA and MFR final flag files.

## Notes

- `MFR.tga`, `gfx/flags/medium/MFR.tga`, and `gfx/flags/small/MFR.tga` were intentionally preserved.
- `UKR_BLACK_BANNER.tga` and its active ideology TGA outputs were intentionally preserved; this pass only restored per-variant source PNG sidecars from the existing generated strip.
- The generated source sheets used square panels despite the prompt requesting 82:52 panels. The full emblem art was preserved and normalized into HOI4 flag sizes; review the contact sheets if this tradeoff needs a stricter regeneration pass.
