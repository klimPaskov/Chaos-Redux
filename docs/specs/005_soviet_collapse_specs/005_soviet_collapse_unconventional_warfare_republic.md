# Unconventional Warfare Republic

## Overview

The Unconventional Warfare Republic is a high-chaos Soviet Collapse successor centered on the Tver biological warfare facility. It appears only through the high-chaos successor path, when Soviet collapse pressure is deep enough and the Tver facility state is still held by the Soviet Union, or when a force-all high-chaos scenario explicitly requests every high-chaos successor.

The country is led by Ivan Mikhailovich Velikanov and is built around forbidden biological, chemical, and zombie special-project warfare. It starts with an extreme high-chaos force package, a biowarfare/chemical national spirit, broad payload access, blacksite facilities, and an aggressive AI posture against the Soviet Union and nearby countries.

## Runtime Flow

1. `can_soviet_collapse_spawn_uwr` checks the high-chaos successor gate, tag existence, collapse pressure, depot vulnerability, and state 247 biowarfare facility ownership/control.
2. `soviet_collapse_spawn_uwr_if_enabled` cores and transfers state 247 to `UWR`.
3. `soviet_collapse_setup_uwr_successor` loads `UWR_soviet_collapse_focus_tree`, grants the experimental warfare idea, initial manpower, biowarfare and chemical facilities, an experiment camp, heavy biological and chemical payload stockpiles, advanced gas technology, starting breakthroughs, and random chaos special-project unlocks.
4. The high-chaos evolution log records stage `unconventional_warfare_stage` and fires `chaosx.nr5_custom.43`.

## Focus Tree

The UWR focus tree is intentionally compact and single-purpose. It has:

- a founding research focus that grants the country identity idea, biowarfare and chemical breakthrough progress, and random chaos special-project unlocks
- a biological facility branch
- a chemical facility branch
- an experimentation camp merge point
- a zombie-weapon branch
- a field-release doctrine branch that contaminates neighboring fronts and prepares expansion
- a final chaos warfare focus that combines special-project rolls, assault columns, contamination, claims, and neighbor conflict pressure

## Reusable Special-Project Helper

`grant_random_chaos_special_project_available_tech` is the central registry for experimental chaos project rewards. It rolls one not-yet-owned biological, chemical, or zombie project and sets the matching delivery technology. Future chaos biological or chemical projects should be added to that helper so existing UWR and future focus/decision rewards automatically roll from the expanded pool.

Documented helper file:

- `common/scripted_effects/chaosx_dynamic_effects.md`

## Assets

Registered idea sprite:

- sprite name: `GFX_idea_uwr_experimental_warfare_republic`
- gfx file: `interface/005_soviet_collapse_icons.gfx`
- placeholder texture: `gfx/interface/ideas/idea_anthrax_contamination.dds`

Country flags:

- `gfx/flags/UWR.tga`
- `gfx/flags/UWR_communism.tga`
- `gfx/flags/UWR_democratic.tga`
- `gfx/flags/UWR_fascism.tga`
- `gfx/flags/UWR_neutrality.tga`
- matching `medium/` and `small/` files

The current UWR flags are placeholders copied from the existing Dead Soldiers' Congress flag set. They exist to prevent missing-flag errors and can be replaced with final UWR artwork later.

## Future Plans

- Add dedicated UWR decisions for targeted field releases, prisoner intake, and facility overclocking.
- Add post-conquest contamination cleanup or integration choices for players fighting UWR.
- Add final UWR flag and focus icon art.
- Extend `grant_random_chaos_special_project_available_tech` whenever new bio/chemical chaos special projects are implemented.
