# Main Menu Repair Run Manifest

Date: 2026-08-29

Launch target: `C:\Users\klimp\OneDrive\Desktop\hoi4.exe - Shortcut.lnk`

Resolved command line: `"C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\hoi4.exe" -debug`

Active playset: `mod/chaos_redux.mod`

## Baseline

The initial mod launch failed before the main menu and created crash directory `hoi4_20260829_133650`.

The exception was `C0000005` in `PHYSFS_swapULE64`, and `memory.log` stopped after `LoadAssets` without reaching `InitGame`.

A no-mod control launch reached the front end, which established that the native crash was mod-attributable.

## Isolation sequence

The repair used reversible launch cycles across model entities, all model assets, the complete `gfx` tree, interface files, sound, localisation, music, the complete `common` tree, scripted effects, and script constants.

The crash disappeared when `common/script_constants` was absent.

A binary search across 157 script-constant files isolated `common/script_constants/002_zombie_constants.txt`.

Removing only `001_communism_spread_constants.txt` did not change the crash.

Removing only `002_zombie_constants.txt` allowed startup to reach the front end.

All quarantined files were restored before source repair and final validation.

The complete baseline, isolation-cycle, and quarantine-manifest snapshots are preserved in `diagnostic_cycles.zip` with 252 archive entries.

## Repair relaunches

| Launch | Result | Evidence |
| --- | --- | --- |
| Schema repair | Reached the front end with decision and scripted-GUI parser errors | Fresh `error.log` and `memory.log` |
| Decision BOM and GUI delimiter repair | Reached the front end with a GUI brace cascade | Fresh `error.log` |
| GUI delimiter correction | Reached the front end with two decision constant errors and seventeen invalid event recruitment effects | Fresh `error.log` |
| Final repair | Reached `CFrontEnd`, `InitGame`, `InitMap`, and `_Super.InitMap`; remained responsive during the stability interval | `logs/final_clean/memory.log` and live process inspection |

## Final state

Final HOI4 process ID: `17528`

Final `error.log`: zero bytes and zero lines.

Newest crash directory remained `hoi4_20260829_142506`, which predates the successful repair launches.

The game was left running at the front end.

## Tooling notes

The HOI4 MCP event and GUI routes were not exposed in this session. Runtime debug launches supplied parser and engine evidence, but this is not presented as a substitute for the unavailable MCP visual audit.

Non-interactive DirectX window capture returned black or unrelated occluded desktop content. Those captures were excluded from the QA package. Obtaining an exact main-menu screenshot would have required foreground desktop interaction, which was intentionally not used.
