# Event 005 Generated Asset Sidecar Current-State Handoff

Date: 2026-05-26

Scope: generated-fictional leader/council portraits and fictional/custom flag variants for Event 005 Soviet Collapse. This pass used only the prompt, repo files, `AGENTS.md`, `.agents/skills/chaos-redux-event-assets/SKILL.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, and `/home/klim/.codex/skills/.system/imagegen/SKILL.md`. It did not inherit parent context.

Forbidden surfaces respected: no gameplay, localisation, `.gfx`, GUI, event, focus, decision, history, country, or spreadsheet files were edited. No existing base flags or leader DDS files were overwritten.

## Files Changed

- Added this handoff only: `docs/plans/005_soviet_union_collapse_plans/subagent_handoffs/event005_generated_asset_sidecar_current_state_2026_05_26.md`

No asset files were created or modified.

## References Inspected

- `docs/assets/005_soviet_union_collapse/manifest.md`
- `docs/assets/005_soviet_union_collapse/gfx_handoff.md`
- `docs/assets/005_soviet_union_collapse/republic_focus_and_influence/manifest.md`
- `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_26_release_councils/manifest.md`
- `gfx/leaders/005_soviet_collapse/`
- `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`
- `.agents/skills/chaos-redux-event-assets/assets/flags/`
- Existing Event 005 contact sheets for generated replacement leaders and live named flags.

## Current Generated-Fictional Portrait Need

No additional generated-fictional leader/council portraits are needed for the active Event 005 set.

Active portrait audit:

- Checked `37` active portrait DDS files: the `32` active custom Event 005 tags from the manifest plus `MOL`, `UZB`, `TAJ`, `TMS`, and `FER` release council portraits.
- Result: no missing DDS files, all checked DDS headers are `156x210`, no duplicate active portrait hashes, and no SHA-256 matches against vanilla leader DDS files under `/home/klim/projects/Hearts of Iron IV/`.
- No `$imagegen` calls were made because the active portrait surface is already complete and unique.

Existing generated-fictional portrait records that remain the current handoff surface:

| Tag | Asset | Source PNG | Processed preview | Final DDS | Dimensions | Source mode |
| --- | --- | --- | --- | --- | --- | --- |
| `KZR` | Khazar Toll Khaganate council | `docs/assets/005_soviet_union_collapse/source_png/generated_replacements/KZR_leader_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/generated_replacements/KZR_leader.png` | `gfx/leaders/005_soviet_collapse/KZR_leader.dds` | 156x210 | `$imagegen`, fictional council |
| `SOG` | Sogdian City League council | `docs/assets/005_soviet_union_collapse/source_png/generated_replacements/SOG_leader_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/generated_replacements/SOG_leader.png` | `gfx/leaders/005_soviet_collapse/SOG_leader.dds` | 156x210 | `$imagegen`, fictional council |
| `OGB` | Old Great Bulgaria council | `docs/assets/005_soviet_union_collapse/source_png/generated_replacements/OGB_leader_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/generated_replacements/OGB_leader.png` | `gfx/leaders/005_soviet_collapse/OGB_leader.dds` | 156x210 | `$imagegen`, fictional council |
| `KHW` | Khwarazmian Oasis Authority council | `docs/assets/005_soviet_union_collapse/source_png/generated_replacements/KHW_leader_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/generated_replacements/KHW_leader.png` | `gfx/leaders/005_soviet_collapse/KHW_leader.dds` | 156x210 | `$imagegen`, fictional council |
| `ALN` | Alan Pass Principality council | `docs/assets/005_soviet_union_collapse/source_png/generated_replacements/ALN_leader_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/generated_replacements/ALN_leader.png` | `gfx/leaders/005_soviet_collapse/ALN_leader.dds` | 156x210 | `$imagegen`, fictional council |
| `MOL` | Sfat Crisis Directorate | `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_26_release_councils/source_png/MOL_leader_source.png` | `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_26_release_councils/processed_png/MOL_leader.png` | `gfx/leaders/005_soviet_collapse/MOL_leader.dds` | 156x210 | `$imagegen`, fictional council |
| `UZB` | Tashkent Emergency Majlis | `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_26_release_councils/source_png/UZB_leader_source.png` | `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_26_release_councils/processed_png/UZB_leader.png` | `gfx/leaders/005_soviet_collapse/UZB_leader.dds` | 156x210 | `$imagegen`, fictional council |
| `TAJ` | Pamir Republican Council | `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_26_release_councils/source_png/TAJ_leader_source.png` | `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_26_release_councils/processed_png/TAJ_leader.png` | `gfx/leaders/005_soviet_collapse/TAJ_leader.dds` | 156x210 | `$imagegen`, fictional council |
| `TMS` | Ashgabat Desert Authority | `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_26_release_councils/source_png/TMS_leader_source.png` | `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_26_release_councils/processed_png/TMS_leader.png` | `gfx/leaders/005_soviet_collapse/TMS_leader.dds` | 156x210 | `$imagegen`, fictional council |
| `FER` | Far Eastern Republic Council | `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_26_release_councils/source_png/FER_leader_source.png` | `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_26_release_councils/processed_png/FER_leader.png` | `gfx/leaders/005_soviet_collapse/FER_leader.dds` | 156x210 | `$imagegen`, fictional council |

The remaining active custom portraits also exist and passed the uniqueness/dimension audit. They were not regenerated because the task prioritized missing generated-fictional/council portraits and forbade overwriting existing leader DDS files unless clearly required.

## Current Fictional Flag Variant Need

No additional generated-fictional custom or cosmetic flag variants are needed for the active Event 005 flag set.

Active flag audit:

- Checked `33` active custom/cosmetic flag families: the `32` active custom Event 005 tags from the manifest plus `UKR_BLACK_BANNER`.
- For those families, all normal, medium, and small TGA files exist for the base flag plus `_communism`, `_democratic`, `_fascism`, and `_neutrality`.
- No duplicate hashes were found within active same-tag flag families, so active ideology variants are not byte-identical base copies.
- Exact default flag override check for existing-game tags `UKR`, `BLR`, `KAZ`, `MOL`, `LIT`, `LAT`, `EST`, `GEO`, `ARM`, `AZR`, `UZB`, `KYR`, `TAJ`, `TMS`, `KAR`, `KOM`, `CRI`, `TAT`, `BSK`, `FER`, `YAK`, `BYA`, and `TAN` found no mod-side `gfx/flags/<TAG>.tga` or `gfx/flags/<TAG>_<ideology>.tga` overrides. `UKR_BLACK_BANNER` remains a separate route/cosmetic flag family, not a default `UKR` override.

## Blockers And Uncertainty

- The active portrait and fictional/custom flag variant production need is currently clear: no new generated-fictional portrait or fictional flag variant asset is required.
- The small historical-restoration flag files for `KZR`, `SOG`, `KHW`, and `ALN` exist, but their small outputs are color-mapped 8 bpp TGAs with descriptor `0x00`, not the 32 bpp descriptor `0x08` format recorded by prior handoffs and manifest notes. Exact affected files are:
  - `gfx/flags/small/KZR.tga`, `KZR_communism.tga`, `KZR_democratic.tga`, `KZR_fascism.tga`, `KZR_neutrality.tga`
  - `gfx/flags/small/SOG.tga`, `SOG_communism.tga`, `SOG_democratic.tga`, `SOG_fascism.tga`, `SOG_neutrality.tga`
  - `gfx/flags/small/KHW.tga`, `KHW_communism.tga`, `KHW_democratic.tga`, `KHW_fascism.tga`, `KHW_neutrality.tga`
  - `gfx/flags/small/ALN.tga`, `ALN_communism.tga`, `ALN_democratic.tga`, `ALN_fascism.tga`, `ALN_neutrality.tga`
- I did not re-export those files in this pass because that would overwrite existing base small flags for `KZR`, `SOG`, `KHW`, and `ALN`, and this prompt explicitly restricted overwriting existing base flags. A separate parent-approved technical flag export correction can re-export the same visible art from the existing processed PNGs without new generation.
- Inactive/stale on-disk families `BEC`, `BLT`, `COU`, `ILU`, `IRA`, `LID`, `RCD`, `RLD`, `SEP`, and `TRS` still have byte-identical normal flag variants. I did not generate replacements because the current manifest/handoffs treat them as inactive or stale, and reviving them would require parent design ownership.

## Validation

- Parsed DDS headers for active generated/council portrait dimensions.
- Parsed TGA headers for active normal/medium/small flag dimensions, bpp, type, and descriptor.
- Compared SHA-256 hashes within active leader portraits and same-tag flag families.
- Compared active Event 005 portrait hashes against vanilla leader DDS files.
- Checked exact default flag override filenames for vanilla-supported ordinary/internal republic tags.

Skipped validation: no in-game validation was run, and no Photoshop processing was needed because no new report-event or portrait assets were generated.
