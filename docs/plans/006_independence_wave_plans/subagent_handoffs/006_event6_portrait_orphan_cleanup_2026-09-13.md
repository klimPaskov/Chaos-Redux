# Event 006 runtime portrait orphan cleanup

Date: 2026-09-13.

Disposition: implemented bounded runtime cleanup; no package or identity promotion.

The current Event 006 portrait audit identified six tracked DDS files under `gfx/leaders/006_independence_wave/` with no registered `.gfx` texture path and no character or scripted-effect consumer:

- `portrait_ACX_cornish_coastal_commander.dds`
- `portrait_ACX_cornish_port_and_mines_committee.dds`
- `portrait_AEX_flemish_civil_industrial_board.dds`
- `portrait_AEX_flemish_industrial_security_commander.dds`
- `portrait_ARX_independence_wave_gavino_piras.dds`
- `portrait_ARX_independence_wave_vittorio_pala.dds`

Those files were legacy generated or superseded runtime outputs, not accepted portrait consumers. They were removed from the engine-facing runtime folder to eliminate false runtime inventory and duplicate mod payload. The preserved source, processed, review, metadata, and evidence outputs remain under `docs/assets/006_independence_wave/`; no source shelf file under `docs/assets/portraits/006_independence_wave/` was changed.

No `.gfx`, character, history, event, scripted-effect, localisation, package-admission, identity, rights, or portrait consumer was added or changed. The thirteen unresolved supplied grounded rows remain blocked, and no replacement, relabel, or fallback was introduced.

## Validation

The Event 006 GFX path census now resolves 324 unique Event 006 DDS files from 324 unique texture paths with zero missing paths and zero unconsumed runtime DDS files. A repository search found no remaining gameplay or interface reference to the six removed basenames. The existing 64 registered Event 006 portrait texture pairs remain unchanged.

This cleanup does not claim live Hearts of Iron IV rendering, save/load, or source-rights completion. ASSET-045 remains blocked only for unresolved identity, role/date, rights, or package-consumer gates among the supplied grounded rows.
