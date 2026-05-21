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
| Red Martyrs' Resurrection Cult | `RMC` | Tag in `common/country_tags/chaosx_countries.txt`; country/history files; normal/medium/small flags plus ideology variants; Event 005 setup/spawn hooks; RMC focus tree; decision category; decisions; event `chaosx.nr5_custom.40`; event-log stage mapping; package docs; manifest row; portrait/focus/decision/idea sprite keys. | partially_implemented | Gameplay package is wired, but RMC focus icons use the tag-specific generated emblem across the tree rather than distinct per-focus final art. |
| Black Banner Host | `BBH` | Tag in `common/country_tags/chaosx_countries.txt`; history file; country localisation; flags; leader DDS; `BBH_soviet_collapse_focus_tree` with 47 focuses; setup effect; asset manifest row. | source_complete | None in source audit. |
| Iron Commissariat of the Dead | `ICD` | Tag in `common/country_tags/chaosx_countries.txt`; country/history files; normal/medium/small flags; Event 005 setup/spawn hooks; ICD focus tree; decision category; decisions; event `chaosx.nr5_custom.39`; event-log stage mapping; package docs; manifest row; portrait/focus/decision/idea sprite keys. | partially_implemented | Gameplay package is wired, but ICD focus icons use the tag-specific generated emblem across the tree rather than distinct per-focus final art. |
| Tunguska Star Committee | `TSC` | Tag in `common/country_tags/chaosx_countries.txt`; country/history files; normal/medium/small flags; Event 005 setup/spawn hooks; TSC focus tree; decision category; decisions; event `chaosx.nr5_custom.38`; event-log stage mapping; package docs; manifest row; portrait/focus/decision/idea sprite keys. | partially_implemented | Gameplay package is wired, but TSC focus icons use the tag-specific generated emblem across the tree rather than distinct per-focus final art. |
| Pale Railway Authority | `PRA` | Tag in `common/country_tags/chaosx_countries.txt`; country/history files; normal/medium/small flags; Event 005 setup/spawn hooks; PRA focus tree; decision category; decisions; event `chaosx.nr5_custom.37`; event-log stage mapping; package docs; manifest row; portrait/focus/decision/idea sprite keys. | partially_implemented | Gameplay package is wired, but PRA focus icons use the tag-specific generated emblem across the tree rather than distinct per-focus final art. |
| Dead Soldiers' Congress | `DSC` | Tag in `common/country_tags/chaosx_countries.txt`; country/history files; normal/medium/small flags plus ideology variants; Event 005 setup/spawn hooks; DSC focus tree; decision category; decisions; event `chaosx.nr5_custom.41`; event-log stage mapping; package docs; manifest row; portrait/focus/decision/idea sprite keys. | partially_implemented | Gameplay package is wired, but DSC focus icons use the tag-specific generated emblem across the tree rather than distinct per-focus final art. |
| Northern Revenant Fleet | no direct `NRF`; partial naval equivalent `ARD` | `ARD` is registered as Arctic Naval Directorate with history, localisation, flags, leader DDS, setup effect, asset rows, and a 47-focus Arctic naval/port directorate tree. Direct search for `NRF` found no tag or package. | partial_equivalent | `ARD` covers an Arctic naval splinter with port and fleet mechanics, but it is not named or framed as Northern Revenant Fleet and does not satisfy the revenant/death-state identity by itself. |
| Civilian Factory of Russia | `CFR` | Tag in `common/country_tags/chaosx_countries.txt`; history file; country localisation; flags; leader DDS; `CFR_soviet_collapse_focus_tree` with 47 focuses; setup effect; factory asset manifest rows. | source_complete | None in source audit. |
| Military Factory of Russia | `MFR` | Tag in `common/country_tags/chaosx_countries.txt`; history file; country localisation; flags; leader DDS; `MFR_soviet_collapse_focus_tree` with 58 focuses; setup effect; factory asset manifest rows. | source_complete | None in source audit. |
| Old Great Bulgaria | `OGB` | Tag in `common/country_tags/chaosx_countries.txt`; history file; country localisation; normal/medium/small flags; Event 005 setup/spawn hooks; OGB focus tree; decision category; event `chaosx.nr5_custom.36`; event-log stage mapping; package docs; manifest row; portrait/focus/decision/idea sprite keys. | partially_implemented | Gameplay package is wired, but OGB-specific leader, focus, idea, and decision DDS files still use documented placeholder reuse rather than bespoke final art. |
| Ancient restoration states | Returned Names system only | Returned Names decisions, ideas, and localisation exist and are documented as placeholder-reuse assets in `docs/assets/005_soviet_union_collapse/manifest.md`. | partially_implemented | No one-row country package audit exists for individual ancient restoration countries, and the Returned Names assets are still documented as placeholder reuse. |

## Additional Implemented Successor Packages

The current worktree also implements additional Event 005 successor packages with 47-focus trees or equivalent package evidence: `FTH`, `TNC`, `ALA`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, and `NLC`. These help the broader Soviet Collapse successor ecosystem but do not replace the specifically missing required actors above unless the design explicitly remaps them.

## Blocking Summary

The high-chaos package requirement is not complete. The current blockers are:

- RMC has a gameplay package, but still needs distinct final per-focus icon art if the final pass requires every focus to have unique art rather than tag-emblem reuse.
- ICD has a gameplay package, but still needs distinct final per-focus icon art if the final pass requires every focus to have unique art rather than tag-emblem reuse.
- TSC has a gameplay package, but still needs distinct final per-focus icon art if the final pass requires every focus to have unique art rather than tag-emblem reuse.
- PRA has a gameplay package, but still needs distinct final per-focus icon art if the final pass requires every focus to have unique art rather than tag-emblem reuse.
- DSC has a gameplay package, but still needs distinct final per-focus icon art if the final pass requires every focus to have unique art rather than tag-emblem reuse.
- missing direct `NRF` package or a fully documented functional remap from Northern Revenant Fleet to `ARD`
- partial `OGB` package with gameplay wiring complete for this audit slice, but bespoke final art still pending
- partial ancient restoration coverage without one-row country packages and with placeholder-reuse Returned Names assets
