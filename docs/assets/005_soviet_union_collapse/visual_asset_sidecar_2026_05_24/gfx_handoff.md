# Event 005 Visual Asset Sidecar Handoff

Scope: active Event 005 Soviet Collapse leader/council portraits and country flags.

## Portrait Handoff

No new portrait sprite definitions are proposed by this sidecar. Active portrait DDS files already exist and match the expected `156x210` leader portrait size.

Existing sprite files:

- `interface/005_soviet_collapse_custom_icons.gfx`
- `interface/005_soviet_collapse_factory_ancient_icons.gfx`

Existing final DDS folder:

- `gfx/leaders/005_soviet_collapse/`

Existing active vanilla-supported release council sprites:

- `GFX_portrait_MOL_sfat_crisis_directorate` -> `gfx/leaders/005_soviet_collapse/MOL_leader.dds`
- `GFX_portrait_UZB_tashkent_emergency_majlis` -> `gfx/leaders/005_soviet_collapse/UZB_leader.dds`
- `GFX_portrait_TAJ_pamir_republican_council` -> `gfx/leaders/005_soviet_collapse/TAJ_leader.dds`
- `GFX_portrait_TMS_ashgabat_desert_authority` -> `gfx/leaders/005_soviet_collapse/TMS_leader.dds`
- `GFX_portrait_FER_far_eastern_republic_council` -> `gfx/leaders/005_soviet_collapse/FER_leader.dds`

## Flag Handoff

No `.gfx` file is needed for country flags. HOI4 resolves country flags from TGA filenames in:

- `gfx/flags/`
- `gfx/flags/medium/`
- `gfx/flags/small/`

Active Event 005 custom/cosmetic flag outputs are present for base and all four ideology suffixes at:

- normal: `gfx/flags/<TAG>[_<ideology>].tga`, `82x52`
- medium: `gfx/flags/medium/<TAG>[_<ideology>].tga`, `41x26`
- small: `gfx/flags/small/<TAG>[_<ideology>].tga`, `10x7`

Orientation confirmation: the active Event 005 flag sidecar state follows the existing handoff notes that current scoped outputs are vanilla-compatible 32-bit TGA files. This pass did not re-export or overwrite flag files.

## Parent-Agent Notes

- Do not create default mod-side flag overrides for vanilla-supported Event 005 release tags `MOL`, `UZB`, `TAJ`, `TMS`, or `FER`.
- Do not revive inactive stale tags without a new active gameplay reference.
- `ZZZ` duplicate ideology flags are outside this Event 005 sidecar scope.

