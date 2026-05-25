# Generated Portrait and Flag Sidecar Manifest

Event: `005_soviet_union_collapse`

Package date: 2026-05-25

Allowed output root: `docs/assets/005_soviet_union_collapse/generated_portrait_flag_sidecar_2026_05_25/`

## Scope and Evidence

Read before work:

- `AGENTS.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `tmp/soviet_collapse_final_clean_merged_spec_package/specs/005_soviet_union_collapse_final_clean_merged_part_6_countries_splinters_restorations.md`
- `tmp/soviet_collapse_final_clean_merged_spec_package/specs/005_soviet_union_collapse_final_clean_merged_part_7_assets_achievements_validation.md`
- Required offline Paradox wiki core pages were opened for repository process compliance.

Reference folders and source surfaces inspected:

- `.agents/skills/chaos-redux-event-assets/assets/flags/`
- `gfx/leaders/005_soviet_collapse/` dimensions and existing portrait surface
- `gfx/flags/` filename surface only; no files changed
- `docs/assets/005_soviet_union_collapse/manifest.md` for current Event 005 asset claims

No gameplay, localisation, `.gfx`, focus, event, country, history, spreadsheet, live leader, or live flag files were edited.

## Generated Assets

### CFR Leader Portrait

| Field | Value |
| --- | --- |
| Asset name | `CFR_leader` |
| Related event | `005_soviet_union_collapse` |
| Asset type | fictional/council leader portrait |
| Intended use | Civilian Factory of Russia leader/council portrait |
| Source mode | Codex built-in `$imagegen` |
| Prompt file | `prompts/generated_prompts.md` |
| Source PNG | `source_png/CFR_leader_source.png` |
| Processed PNG | `processed_png/CFR_leader.png` |
| Final DDS | `final_dds/CFR_leader.dds` |
| Target size | `156x210` |
| Proposed live DDS | `gfx/leaders/005_soviet_collapse/CFR_leader.dds` |
| Proposed sprite | keep existing CFR sprite if already wired, otherwise `GFX_portrait_CFR_civilian_works_directorate` |
| Suggested `.gfx` file | `interface/005_soviet_collapse_factory_ancient_icons.gfx` |
| Status | `converted` |
| Notes | Fictional generated portrait; not a real leader likeness. Parent should compare against existing dirty/runtime CFR portrait before promotion. |

### CFR Communism Flag

| Field | Value |
| --- | --- |
| Asset name | `CFR_communism` |
| Related event | `005_soviet_union_collapse` |
| Asset type | fictional/alternate-history ideology flag |
| Intended use | Civilian Factory of Russia communism ideology flag |
| Source mode | Codex built-in `$imagegen` |
| Prompt file | `prompts/generated_prompts.md` |
| Source PNG | `source_png/CFR_communism_flag_source.png` |
| Processed PNG normal | `processed_png/CFR_communism_normal.png` |
| Processed PNG medium | `processed_png/CFR_communism_medium.png` |
| Processed PNG small | `processed_png/CFR_communism_small.png` |
| Final TGA normal | `final_tga/normal/CFR_communism.tga` |
| Final TGA medium | `final_tga/medium/CFR_communism.tga` |
| Final TGA small | `final_tga/small/CFR_communism.tga` |
| Target sizes | normal `82x52`, medium `41x26`, small `10x7` |
| Proposed live paths | `gfx/flags/CFR_communism.tga`, `gfx/flags/medium/CFR_communism.tga`, `gfx/flags/small/CFR_communism.tga` |
| Contact sheet | `contact_sheets/CFR_communism_flag_sizes.png` |
| Orientation confirmation | Header descriptor byte is `0x08`; dimensions validate for all three sizes; contact sheet is left-to-right normal, medium, small. |
| Status | `converted` |
| Notes | Generated from a new source concept. Not a recolor, filter, flip, copied emblem, or one-shape edit over an existing base flag. |

## Queued and Blocked Items

`queued_asset_ledger.md` lists the remaining fictional/council portrait and fictional/alternate-history flag queue.

No tool blocker was encountered for the pilot assets: `$imagegen`, PNG processing, DDS conversion, and TGA export all worked. The remaining rows are queued because this sidecar was intentionally isolated from the dirty live Event 005 flag and portrait files. Parent-agent review is required before promoting or replacing any live asset.

## Validation

Validation output: `validation/identify_outputs.txt`

Confirmed:

- `processed_png/CFR_leader.png`: `156x210`
- `final_dds/CFR_leader.dds`: `156x210`
- `final_tga/normal/CFR_communism.tga`: `82x52`
- `final_tga/medium/CFR_communism.tga`: `41x26`
- `final_tga/small/CFR_communism.tga`: `10x7`
- TGA descriptor byte for normal flag: `0x08`

