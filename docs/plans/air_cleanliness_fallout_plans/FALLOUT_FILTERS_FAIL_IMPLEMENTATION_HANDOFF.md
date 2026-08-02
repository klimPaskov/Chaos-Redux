# Filters Fail at Night implementation handoff

## Scope completed

The dormant Filters Fail at Night tranche is implemented under the Fallout namespace. Human play starts at event `chaosx.fallout.217`, hidden AI starts at `chaosx.fallout.218`, branch results occupy `219` through `226`, the callback occupies `227` and `228`, and cleanup occupies `229`.

The candidate producer adds one lowest-owned-state row with candidate `217`, transaction key `710009`, route `7109`, the medicine cooldown family, and the produced Air Winter shelter receipt. Candidate production remains outside the scheduler release gate.

## Deterministic contract evidence

- `fallout_event_217_calculate_outcome` computes shelter, filters, medicine, adaptation, and exposure using the accepted weighted formula, then clamps the score before the branch thresholds are checked.
- The opening stores the target state, owner, generation, branch, outcome, resource snapshot, shelter snapshot, cause memory, and cleanup ticket before the delayed result is committed.
- Human and hidden AI results call the same result resolver and the same callback resolver.
- AI branch scores use the same viability inputs, affordability gates, cause, government archetype, war, filter pressure, exposure, prior memory, success and partial bonuses, and documented tie order.
- Failure casualties call `apply_exact_state_civilian_population_loss` through the shared Deaths contract. No direct population mutation is used.
- State metrics are clamped after result and callback writes. Air Winter variables are updated when still present, while the durable Fallout state receipt remains available after transition.

## Presentation and log evidence

- Human surfaces use `GFX_report_event_fallout_filters_fail`, registered in `interface/fallout_consolidated.gfx`.
- The dedicated asset package, source, processed PNG, DDS, prompt, contact sheet, manifest row, and hashes are recorded in `docs/assets/air_cleanliness_fallout/fallout_filters_fail_gfx_handoff.md`.
- History id `9114` has fifteen payload selectors in the dedicated scripted localisation file. Central Event Log detail, name, and open-detail type routes include the new history id.
- Localisation names the affected shelter state, filters, medicine, food, night crews, and government authority. The file uses UTF-8 with BOM.

## Catalog alignment note

The event catalog worker updated `Events!A203:M203` with the five reviewed Filters Fail report titles and ran the required CSV export. The workbook and generated CSV snapshots remain in the working tree, but are not part of this tranche commit because they also contain unrelated concurrent catalog edits that cannot be staged safely as a binary workbook delta.

## Static review evidence

The targeted audit found unique event ids `217` through `229`, balanced braces in the touched script surfaces, no unsupported comparison operators, no Zombie path or asset reference, and a complete localisation reference set for the new events and Event Log payloads. HOI4 was not run, as requested.

## Remaining review gate

The chain is implemented but dormant. It is not counted toward the 660 manually reviewed event-block floor until the Fallout scheduler caller is reviewed and activated in a later tranche. The exact engine-native thermonuclear province sweep remains a separate documented blocker and is not weakened by this chain.
