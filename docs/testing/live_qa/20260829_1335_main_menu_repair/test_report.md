# Main Menu Repair Test Report

## Outcome

Chaos Redux reaches the Hearts of Iron IV front end and map initialization without crashing.

The final debug launch remained responsive after `_Super.InitMap`, produced no new crash directory, and left `error.log` at zero bytes and zero lines.

## Task-specific validation

- The no-mod control reached the front end, proving the initial access violation was introduced by the active mod surface.

- Reversible subsystem isolation located the crash in `common/script_constants`.

- A file-level binary search proved that only `002_zombie_constants.txt` controlled the crash result.

- The corrected schema loaded with its original `constant:zombie_outbreak_event.id` consumers intact.

- The Bashkiria and Mari decision package loaded after removal of its script BOM.

- The event-log GUI parser accepted the repaired sibling trigger structure.

- The Karelia and Crimea factory-use fields resolved after receiving their required local constant.

- Event 006 no longer asks the engine to execute startup-only character recruitment from an event.

- The final log scan found no parser errors, invalid triggers, malformed tokens, failed validations, fatal errors, or exceptions in the final snapshot.

## Final evidence

- `logs/final_clean/error.log` is empty.

- `logs/final_clean/memory.log` records `CFrontEnd`, `InitGame`, `InitMap`, and `_Super.InitMap` completion.

- The final process remained responsive through the stability interval.

- No crash directory newer than `hoi4_20260829_142506` was created.

## Tooling limitations

The HOI4 MCP GUI and event tools were unavailable in the active tool set. Source inspection plus repeated debug runtime launches were used, and no MCP visual-comparison claim is made.

An exact main-menu screenshot could not be captured without foreground interaction because non-interactive DirectX capture returned no valid HOI4 frame.

## Simplifications, omissions, and blockers

No implementation simplifications remain.

The only evidence omissions are the unavailable MCP traces and exact screenshot described above. They do not affect the zero-error runtime result.
