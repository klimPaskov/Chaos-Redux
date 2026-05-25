# Event 005 Generated-Art First Batch Handoff

No `.gfx` edits are needed from this sidecar.

## Leader Portraits

The active audited leader/council portraits already exist as final DDS files under `gfx/leaders/005_soviet_collapse/` and are referenced by existing portrait sprite names in the Event 005 `.gfx` files.

Use existing sprite names from country history and interface files, including:

- `GFX_portrait_CFR_construction_board`
- `GFX_portrait_MFR_arsenal_board`
- `GFX_portrait_KRS_sailors_assembly`
- `GFX_portrait_UDC_emergency_military_committee`
- `GFX_portrait_SDZ_directorate_collegium`
- `GFX_portrait_RMC_council_of_red_witnesses`
- `GFX_portrait_DSC_congress_of_dead_regiments`
- `GFX_portrait_NRF_dead_convoy_admiralty`
- `GFX_portrait_TSC_observation_presidium`
- `GFX_portrait_ICD_dead_roll_commissariat`

Full portrait audit: `validation/leader_portrait_audit.tsv`.

Portrait contact sheet: `contact_sheets/active_council_leaders.png`.

## Country And Cosmetic Flags

HOI4 country flags do not need `.gfx` sprite definitions. The engine resolves them by tag, ideology suffix, and cosmetic tag filename from:

- `gfx/flags/<TAG>[_ideology].tga`
- `gfx/flags/medium/<TAG>[_ideology].tga`
- `gfx/flags/small/<TAG>[_ideology].tga`

No default no-suffix flag should be added for existing vanilla-supported countries. `UKR_BLACK_BANNER` remains an explicit route/cosmetic flag target and is not a `UKR` base override.

## Blocked Promotion Queue

The following active dirty small flags should be re-exported only when the parent asset owner is ready to overwrite the active files:

- `gfx/flags/small/CFR*.tga`
- `gfx/flags/small/KRS*.tga`
- `gfx/flags/small/UDC*.tga`
- `gfx/flags/small/SDZ*.tga`
- `gfx/flags/small/KZR*.tga`
- `gfx/flags/small/SOG*.tga`
- `gfx/flags/small/KHW*.tga`
- `gfx/flags/small/ALN*.tga`
- `gfx/flags/small/RMC*.tga`
- `gfx/flags/small/TSC*.tga`

Exact file list: `validation/problem_small_flags.txt`.

Required output if promoted: preserve current visible art and orientation, but export as `10x7` 32bpp true-color TGA with descriptor byte `0x08`.

Orientation confirmation: current contact sheet `contact_sheets/problem_small_flags_current.png` decodes upright; normal and medium files for the same tag families are already `82x52` and `41x26` with descriptor `0x08`.

## Suggested Parent Action

Do not generate new fictional art for this scoped first batch unless the parent rejects a specific visible design. The practical next asset action is a controlled re-export of the 50 listed small flags, preserving artwork and orientation.
