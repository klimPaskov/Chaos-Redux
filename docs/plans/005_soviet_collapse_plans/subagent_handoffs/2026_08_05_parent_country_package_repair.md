# Event 005 Country Package Repair Handoff

Date: 2026-08-05
Owner: parent agent
Scope: UWR, KMB, ancient restoration decision surfaces, route AI, localisation, and MCP evidence after the focus-selector repair.

## Implemented

- `common/decisions/005_soviet_collapse_decisions.txt` adds `soviet_collapse_uwr_blacksite_category` with `uwr_overclock_blacksite_network`, `uwr_expand_experiment_camp_registry`, and `uwr_authorize_field_release_raids`.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` unlocks the three UWR decisions from their route focuses and unlocks `kmb_integrate_conquered_basin` from `KMB_concession_treaties`.
- `common/decisions/005_soviet_collapse_decisions.txt` adds `kmb_integrate_conquered_basin`, gated on KMB owning and controlling states 570, 571, 572, and 578 after the concession route.
- `common/scripted_triggers/005_soviet_collapse_triggers.txt` adds `has_soviet_collapse_kmb_conquered_basin`.
- `common/scripted_effects/005_soviet_collapse_effects.txt` adds `soviet_collapse_kmb_integrate_conquered_basin`, which cores and improves the four basin states, advances the existing KMB resource-expansion stage, raises depot control, and records a one-time completion flag.
- `common/decisions/005_soviet_collapse_decisions.txt` adds `soviet_collapse_write_restored_charter` to the shared Returned Names category. It requires the ancient restoration successor flag, an ancient charter focus, and the old-banner stage, then applies legal recognition, foreign-channel, and League-support effects.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt` unlocks the restored-charter decision from the INX, SOG, ANX, and ABX charter focuses.
- `common/ai_strategy/005_soviet_collapse.txt` adds route-aware symbolic and expansionist posture overlays for INX, SOG, ANX, and ABX with centralized file-scoped tuning values.
- `common/script_constants/005_soviet_collapse_constants.txt` centralizes the new UWR and KMB decision costs and the KMB basin infrastructure level.
- `localisation/english/005_soviet_collapse_l_english.yml` adds the decision titles, descriptions, and effect tooltips with its UTF-8 BOM preserved.

## Validation evidence

- The changed Clausewitz files are brace-balanced by source-level counts.
- New decision and tooltip localisation identifiers occur exactly once each, and the localisation file retains the UTF-8 BOM.
- The reused decision sprite references resolve in `interface/005_soviet_collapse.gfx`; no new binary asset was added.
- `python .tools/audit_chaosx_country_tags.py` reports 136 protected Event 006/Soviet tags, zero external country-definition collisions, and zero external identity-surface collisions.
- Focus MCP inspection returned `FOCUS_INSPECTED` for `NLC_soviet_collapse_focus_tree`, `CFR_soviet_collapse_focus_tree`, and `INX_soviet_collapse_ancient_focus_tree`; prior post-repair UWR and KMB inspections also returned `FOCUS_INSPECTED` with no Event 005 source blockers. Remaining MCP focus diagnostics are vanilla continuous-focus palette errors and authored layout warnings.
- Focused `hoi4.event_inspect` lint for `chaosx.nr5.1` returned `EVENT_INSPECTED_PARTIAL`, no blockers, and zero blocking diagnostics. The workspace-wide helper and lifecycle analysis remains deferred by the MCP because of repository scale.
- The full focus probability evaluations used complete candidate pools of 515 republic, 1,021 custom-splinter, 128 factory-successor, and 64 ancient focuses under named calm and war scenarios. Results remain partial because the analyzer cannot resolve several declared campaign inputs, including actor tags, completed-focus state, scoped country checks, stability, global flags, and custom tooltip wrappers.
- The `ai_strategy_factor` probability adapter was attempted for `common/ai_strategy/005_soviet_collapse.txt` and returned `PROBABILITY_SURFACE_EMPTY`; no unsupported normalized strategy-factor claim is made.

## Remaining risks and boundaries

- The KMB repair implements the direct board-rule conquered-basin outcome. Treaty competition and alternative concession-puppet or resource-corridor outcomes remain a later supplemental-spec tranche.
- UWR post-conquest contamination cleanup and final UWR art remain outside this source-only repair. The active Event 005 asset boundary still forbids new flags, route-flag sprites, portraits, and binary artwork.
- The final focus-layout rewrite gate ran after every source and evidence repair. MCP quality-blocked the NLC compact proposal because node intersections increased from 16 to 18, and quality-blocked the INX compact proposal because it introduced one node intersection and sibling-anchor regressions; both changed no files.
- The ancient national-focus probability sweep completed across three explicit prerequisite-multiplier states with zero unresolved inputs and produced artifact `probability-047328b6997b518558dcf0e7.json`.
- The broader 43-tree route-depth, helper-generic reward, event-catalog parity, full map setup, and workspace-wide event-analysis backlogs remain open; this handoff does not claim Event 005 completion.
