# Event 005 High-Chaos Package Audit

Audit date: 2026-05-21

This audit checks the required high-chaos and evolved splinter list from the final clean merged Part 6 specification against the current worktree. It records direct source evidence only and does not claim final completion where a required actor is missing or only partially represented.

## Required Splinter Rows

| Required actor | Implemented tag or equivalent | Source evidence | Status | Deviation or blocker |
| --- | --- | --- | --- | --- |
| Kronstadt Free Soviet | `KRS` | Tag in `common/country_tags/chaosx_countries.txt`; history file; country localisation; flags; leader DDS; `KRS_soviet_collapse_focus_tree` with 47 focuses; setup effect; asset manifest row. | source_complete | None in source audit. |
| Green Army Congress | `GAC` | Tag in `common/country_tags/chaosx_countries.txt`; history file; country localisation; flags; leader DDS; `GAC_soviet_collapse_focus_tree` with 47 focuses; setup effect; asset manifest row. | source_complete | None in source audit. |
| Union Defense Committee | `UDC` | Tag in `common/country_tags/chaosx_countries.txt`; history file; country localisation; flags; leader DDS; `UDC_soviet_collapse_focus_tree` with 47 focuses; setup effect; asset manifest row. | source_complete | None in source audit. |
| Security Directorate Zone | `SDZ` | Tag in `common/country_tags/chaosx_countries.txt`; history file; country localisation; flags; leader DDS; `SDZ_soviet_collapse_focus_tree` with 47 focuses; setup effect; asset manifest row. | source_complete | None in source audit. |
| Basmachi Confederation | `BSC` | Tag in `common/country_tags/chaosx_countries.txt`; history file; country localisation; flags; leader DDS; `BSC_soviet_collapse_focus_tree` with 47 focuses; setup effect; asset manifest row. | source_complete | None in source audit. |
| Red Martyrs' Resurrection Cult | none found | Searches for `RMC` and `RMT` found no tag, history file, focus tree, setup effect, localisation, or asset package. | missing | Required death/martyr cult package is not implemented. |
| Black Banner Host | `BBH` | Tag in `common/country_tags/chaosx_countries.txt`; history file; country localisation; flags; leader DDS; `BBH_soviet_collapse_focus_tree` with 47 focuses; setup effect; asset manifest row. | source_complete | None in source audit. |
| Iron Commissariat of the Dead | none found | Search for `ICD` found no tag, history file, focus tree, setup effect, localisation, or asset package. | missing | Required rogue Soviet death-state authority package is not implemented. |
| Tunguska Star Committee | none found | Search for `TSC` found no tag, history file, focus tree, setup effect, localisation, or asset package. | missing | Required Siberian cosmic committee package is not implemented. |
| Pale Railway Authority | none found | Search for `PRA` found no tag, history file, focus tree, setup effect, localisation, or asset package. | missing | Required rail-state package is not implemented. |
| Dead Soldiers' Congress | none found | Search for `DSC` found no tag, history file, focus tree, setup effect, localisation, or asset package. | missing | Required veteran/revenant military memory state package is not implemented. |
| Northern Revenant Fleet | no direct `NRF`; partial naval equivalent `ARD` | `ARD` is registered as Arctic Naval Directorate with history, localisation, flags, leader DDS, setup effect, asset rows, and a 47-focus Arctic naval/port directorate tree. Direct search for `NRF` found no tag or package. | partial_equivalent | `ARD` covers an Arctic naval splinter with port and fleet mechanics, but it is not named or framed as Northern Revenant Fleet and does not satisfy the revenant/death-state identity by itself. |
| Civilian Factory of Russia | `CFR` | Tag in `common/country_tags/chaosx_countries.txt`; history file; country localisation; flags; leader DDS; `CFR_soviet_collapse_focus_tree` with 47 focuses; setup effect; factory asset manifest rows. | source_complete | None in source audit. |
| Military Factory of Russia | `MFR` | Tag in `common/country_tags/chaosx_countries.txt`; history file; country localisation; flags; leader DDS; `MFR_soviet_collapse_focus_tree` with 58 focuses; setup effect; factory asset manifest rows. | source_complete | None in source audit. |
| Old Great Bulgaria | `OGB` | Tag in `common/country_tags/chaosx_countries.txt`; history file; country localisation; normal/medium/small flags; `old_great_bulgaria` idea localisation. | partially_implemented | No Event 005 OGB focus tree, setup effect, decision package, asset manifest package row, or `GFX_portrait_OGB_volga_restoration_council` sprite wiring was found. |
| Ancient restoration states | Returned Names system only | Returned Names decisions, ideas, and localisation exist and are documented as placeholder-reuse assets in `docs/assets/005_soviet_union_collapse/manifest.md`. | partially_implemented | No one-row country package audit exists for individual ancient restoration countries, and the Returned Names assets are still documented as placeholder reuse. |

## Additional Implemented Successor Packages

The current worktree also implements additional Event 005 successor packages with 47-focus trees or equivalent package evidence: `FTH`, `TNC`, `ALA`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, and `NLC`. These help the broader Soviet Collapse successor ecosystem but do not replace the specifically missing required actors above unless the design explicitly remaps them.

## Blocking Summary

The high-chaos package requirement is not complete. The current blockers are:

- missing `RMC` or equivalent Red Martyrs' Resurrection Cult package
- missing `ICD` or equivalent Iron Commissariat of the Dead package
- missing `TSC` or equivalent Tunguska Star Committee package
- missing `PRA` or equivalent Pale Railway Authority package
- missing `DSC` or equivalent Dead Soldiers' Congress package
- missing direct `NRF` package or a fully documented functional remap from Northern Revenant Fleet to `ARD`
- partial `OGB` package without focus, setup, decision, portrait sprite, and asset-manifest completion
- partial ancient restoration coverage without one-row country packages and with placeholder-reuse Returned Names assets
