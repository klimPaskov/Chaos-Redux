# Event 005 Flag and Portrait Gap Handoff - 2026-05-26

Scope: `chaosx_generated_event_art` style bounded asset production for Event 005 Soviet Collapse. This handoff assumes `fork_context=false`; all task constraints used here came from the parent prompt, `AGENTS.md`, and `.agents/skills/chaos-redux-event-assets/SKILL.md`, not inherited parent context.

## Completed Work

Replaced the user-named broken flag families in the live HOI4 flag folders:

- `CFR`, `KRS`, `RMC`, `SDZ`, `TSC`, `UDC`
- `SOG`, `ALN`, `KHW`, `KZR`
- base, `_communism`, `_democratic`, `_fascism`, and `_neutrality` variants for each tag
- normal, medium, and small TGA outputs for each variant

Final live paths:

- `gfx/flags/<TAG>.tga` and `gfx/flags/<TAG>_<ideology>.tga`
- `gfx/flags/medium/<TAG>.tga` and `gfx/flags/medium/<TAG>_<ideology>.tga`
- `gfx/flags/small/<TAG>.tga` and `gfx/flags/small/<TAG>_<ideology>.tga`

Total final flag files produced: 150 TGA files.

## Source Mode

Source mode: generated fictional/alternate-history flag art from the existing Event 005 sidecar package:

- Source PNGs: `docs/assets/005_soviet_union_collapse/generated_asset_sidecar_flags_portraits/source_png/`
- Processed PNG previews: `docs/assets/005_soviet_union_collapse/generated_asset_sidecar_flags_portraits/processed_png/`

No new `$imagegen` calls were made in this pass. I promoted the existing processed sidecar flag art into the live HOI4 flag folders because it already covered the exact user-named flag families and avoided inventing additional countries or route flags.

## Orientation And Validation

All scoped flag outputs were validated after export:

- normal flags: `82x52`
- medium flags: `41x26`
- small flags: `10x7`
- TGA type: `2`
- TGA bit depth: `32`
- TGA descriptor byte: `0x08`, matching vanilla samples inspected from `gfx/flags`
- every same-tag family has `5/5` unique hashes at normal, medium, and small size
- contact sheets decode upright; no upside-down or mirrored exported family was observed

Contact sheets:

- `docs/plans/005_soviet_union_collapse_plans/subagent_handoffs/contact_sheets/event005_named_flags_normal_live_contact.png`
- `docs/plans/005_soviet_union_collapse_plans/subagent_handoffs/contact_sheets/event005_named_flags_medium_live_contact.png`
- `docs/plans/005_soviet_union_collapse_plans/subagent_handoffs/contact_sheets/event005_named_flags_small_live_contact.png`
- `docs/plans/005_soviet_union_collapse_plans/subagent_handoffs/contact_sheets/event005_referenced_leader_portraits_contact.png`

Export note: the first small-flag export attempted by ImageMagick collapsed to indexed 8-bit TGAs because of the tiny palette. Those small TGAs were immediately re-exported with `-type TrueColorAlpha -define tga:bits-per-pixel=32`, and the final validation found no remaining header issues.

## Portrait Review

Inspected Event 005 leader/council portrait references in:

- `interface/005_soviet_collapse_custom_icons.gfx`
- `interface/005_soviet_collapse_factory_ancient_icons.gfx`

Result:

- referenced portrait DDS files: 37
- missing referenced portraits: none
- duplicate referenced portrait hashes: none
- referenced portrait dimensions: `156x210`

No new fictional leader or council portrait was generated because the active referenced portrait surface is already covered and unique.

## Files Changed

Asset files changed:

- `gfx/flags/{CFR,KRS,RMC,SDZ,TSC,UDC,SOG,ALN,KHW,KZR}*.tga`
- `gfx/flags/medium/{CFR,KRS,RMC,SDZ,TSC,UDC,SOG,ALN,KHW,KZR}*.tga`
- `gfx/flags/small/{CFR,KRS,RMC,SDZ,TSC,UDC,SOG,ALN,KHW,KZR}*.tga`

Documentation/review files added:

- this handoff
- the four contact sheets listed above

No gameplay, localisation, interface `.gfx`, GUI, focus, decision, event, history, country, spreadsheet, or non-asset docs were edited.

## Blockers And Uncertainty

No blocker remains for the named flag families: final normal, medium, and small TGA files were produced safely.

No DDS files were produced for these flags because HOI4 country flags use TGA files in `gfx/flags`, `gfx/flags/medium`, and `gfx/flags/small`.

No new portrait asset was produced because the current active Event 005 portrait references are complete. If the parent rejects a specific portrait on visual grounds, that should be routed as a new targeted fictional portrait request rather than a broad replacement pass.
