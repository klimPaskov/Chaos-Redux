# Main Menu Repair Ledger

## Native startup crash

File: `common/script_constants/002_zombie_constants.txt`

Cause: `zombie_outbreak_event.schema` used `id = int`, which is not a valid script-constant schema declaration and caused a native access violation before the engine could write a parser error.

Repair: declared `key = id` and `data = int` while preserving the public token `constant:zombie_outbreak_event.id`.

Evidence: removing only this file allowed startup to continue, and restoring it with the corrected schema removed the crash.

## Bashkiria and Mari decision registry

File: `common/decisions/006_independence_wave_bashkiria_mari_decisions.txt`

Cause: a UTF-8 BOM at the beginning of a non-localisation script was tokenized as an unknown decision category key.

Repair: removed the BOM without changing decision content.

Evidence: the category and all dependent decision IDs loaded on the next launch.

## Shared event-log scripted GUI

File: `common/scripted_guis/chaosx_scripted_gui_events_log.txt`

Cause: `events_log_event_detail_entry_meta_cluster_visible` was nested inside the preceding tertiary visibility trigger.

Repair: moved the existing closing delimiter so the tertiary and cluster visibility triggers are siblings.

Evidence: the invalid trigger and subsequent parser cascade disappeared from the next launch.

## Karelia and Crimea decision costs

File: `common/decisions/006_independence_wave_karelia_crimea_decisions.txt`

Cause: two `civilian_factory_use` fields referenced a file-scoped `@` constant that was declared only in other decision files.

Repair: added the matching local constant with value `1`, aligned with `constant:independence_wave_decision_cost.civilian_factory_light`.

Evidence: both malformed-token errors disappeared.

## Event 006 character recruitment

Files: `events/006_independence_wave.txt`, `history/general/006_independence_wave_character_recruitment_registry.txt`, and `docs/events/006_independence_wave/northern_western_europe_packages.md`

Cause: hidden event `chaosx.nr6.10` contained seventeen `recruit_character` effects, although the engine accepts that effect only during game or history initialization.

Repair: restored `chaosx.nr6.10` as an empty synchronous compatibility checkpoint and retained fixed-character ownership in the game-history recruitment registry. Documentation now describes the same ownership model.

Evidence: all seventeen effect validation errors disappeared, and the final launch produced an empty `error.log`.

## Simplifications, omissions, and blockers

No gameplay fallback or source simplification was used.

The required HOI4 MCP GUI and event routes were unavailable, so no MCP render or event trace was produced.

No exact main-menu screenshot was retained because non-interactive capture could not read the DirectX surface without foreground desktop interaction.
