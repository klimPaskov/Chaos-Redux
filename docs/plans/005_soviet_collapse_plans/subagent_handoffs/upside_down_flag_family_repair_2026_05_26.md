# Upside-Down Flag Family Repair - 2026-05-26

## Scope

Re-exported only the known upside-down Event 005 flag families:

- `ALN`
- `KHW`
- `KZR`
- `SOG`

For each tag, the base flag and ideology variants were replaced in all three HOI4 flag sizes:

- `gfx/flags/<TAG>*.tga` at 82x52
- `gfx/flags/medium/<TAG>*.tga` at 41x26
- `gfx/flags/small/<TAG>*.tga` at 10x7

No gameplay, localisation, `.gfx`, focus, decision, event, script, or country files were edited.

## Source Assets

The repair used the existing upright processed PNGs from:

```text
docs/assets/005_soviet_union_collapse/generated_asset_sidecar_flags_portraits/processed_png/
```

The existing designs were preserved. No new flags were generated, sourced, recolored, or substituted.

## Export Method

Each target TGA was regenerated from its matching processed PNG with the image data vertically flipped before TGA export. This corrects the previous TGA storage orientation issue: before the repair, each live TGA decoded as the vertical flip of the upright processed PNG; after the repair, each decoded TGA matches the upright processed PNG.

## Changed Files

Changed 60 TGA files:

```text
gfx/flags/ALN.tga
gfx/flags/ALN_communism.tga
gfx/flags/ALN_democratic.tga
gfx/flags/ALN_fascism.tga
gfx/flags/ALN_neutrality.tga
gfx/flags/KHW.tga
gfx/flags/KHW_communism.tga
gfx/flags/KHW_democratic.tga
gfx/flags/KHW_fascism.tga
gfx/flags/KHW_neutrality.tga
gfx/flags/KZR.tga
gfx/flags/KZR_communism.tga
gfx/flags/KZR_democratic.tga
gfx/flags/KZR_fascism.tga
gfx/flags/KZR_neutrality.tga
gfx/flags/SOG.tga
gfx/flags/SOG_communism.tga
gfx/flags/SOG_democratic.tga
gfx/flags/SOG_fascism.tga
gfx/flags/SOG_neutrality.tga
gfx/flags/medium/ALN.tga
gfx/flags/medium/ALN_communism.tga
gfx/flags/medium/ALN_democratic.tga
gfx/flags/medium/ALN_fascism.tga
gfx/flags/medium/ALN_neutrality.tga
gfx/flags/medium/KHW.tga
gfx/flags/medium/KHW_communism.tga
gfx/flags/medium/KHW_democratic.tga
gfx/flags/medium/KHW_fascism.tga
gfx/flags/medium/KHW_neutrality.tga
gfx/flags/medium/KZR.tga
gfx/flags/medium/KZR_communism.tga
gfx/flags/medium/KZR_democratic.tga
gfx/flags/medium/KZR_fascism.tga
gfx/flags/medium/KZR_neutrality.tga
gfx/flags/medium/SOG.tga
gfx/flags/medium/SOG_communism.tga
gfx/flags/medium/SOG_democratic.tga
gfx/flags/medium/SOG_fascism.tga
gfx/flags/medium/SOG_neutrality.tga
gfx/flags/small/ALN.tga
gfx/flags/small/ALN_communism.tga
gfx/flags/small/ALN_democratic.tga
gfx/flags/small/ALN_fascism.tga
gfx/flags/small/ALN_neutrality.tga
gfx/flags/small/KHW.tga
gfx/flags/small/KHW_communism.tga
gfx/flags/small/KHW_democratic.tga
gfx/flags/small/KHW_fascism.tga
gfx/flags/small/KHW_neutrality.tga
gfx/flags/small/KZR.tga
gfx/flags/small/KZR_communism.tga
gfx/flags/small/KZR_democratic.tga
gfx/flags/small/KZR_fascism.tga
gfx/flags/small/KZR_neutrality.tga
gfx/flags/small/SOG.tga
gfx/flags/small/SOG_communism.tga
gfx/flags/small/SOG_democratic.tga
gfx/flags/small/SOG_fascism.tga
gfx/flags/small/SOG_neutrality.tga
```

This handoff note was added:

```text
docs/plans/005_soviet_collapse_plans/subagent_handoffs/upside_down_flag_family_repair_2026_05_26.md
```

## Validation

Ran a pixel comparison for every repaired TGA against its matching upright processed PNG. All 60 repaired TGAs returned `RMSE 0 (0)` when decoded and compared to the upright preview.

Ran dimension checks for every repaired TGA:

- normal flags: 82x52
- medium flags: 41x26
- small flags: 10x7

Checked git status for the forbidden default-country base flags listed in the task. None of those default base flag files had status changes from this repair.

## Remaining Issues

No blockers or substitutions. No unrelated flags were created or modified.
