# Event Details Registry Repairs Handoff

## Scope

This bounded repair keeps the existing Event Details world-end registry and adds only implemented terminal identities and Event 11 evolution preview rows.

The registry now covers Holy Realm Final Silence, Africa The World, the existing Cannibalism pair, the registered hidden Wendigo Ascendancy identity, Brilliant Scientist endings, Black Plague, Zombie Apocalypse, Fury, Death, and Resources Found.

Fallout remains outside the registry because it is a separate consequence coordinator without an ordinary event-log or world-end scenario row contract.

## Helper map

`initialize_world_end_scenario_registry` owns aligned numeric registry arrays and appends stable rows for scenario IDs 3, 9, and 14 in addition to the existing rows.

`events_log_evaluate_world_end_scenario_active` maps Final Silence to `world_end_final_silence` or `world_end_final_silence_completed`, Wendigo Ascendancy to `world_end_wendigo`, and Africa The World to `world_end_africa_the_world`.

`events_log_rebuild_event_detail_world_end_scenarios` selects by owner event only, preserving independent enabled, active, and available state for every registered row.

The Event 11 preview block injects `secret_alliance_event.evolution_type`, the three authored tiers, and the three authored stages into the shared preview arrays.

## Constants and tuning

`world_end_scenario_id.africa_the_world = 14` is appended without renumbering existing save-facing identities.

`world_end_scenario_owner_event.africa_world_order = 12` maps the Africa owner event.

`world_end_scenario_super_event.africa_the_world = 104` maps the authored Event 012 terminal presentation slot.

No new probability, MTTH, duration, or AI tuning was introduced.

## Localisation and docs

The shared scripted localisation dispatches title, owner, and body keys for Final Silence, Africa The World, and Wendigo Ascendancy in both row and selected-detail contexts.

The GUI localisation adds player-facing title and body text for all three registered identities.

World-end catalog, Event Details window, evolution/cluster, and Event 011 overview documentation describe registered hidden rows and the owner-only rebuild contract.

The event catalog workbook was intentionally not edited because the parent task explicitly bounded this repair away from workbook changes.

## Cleanup and migration

No event targets, global arrays, flags, or variables were removed, renamed, or migrated.

Existing `global.disabled_world_end_scenarios` values remain the independent per-scenario enable store, and the new scenario IDs are seeded through the existing registry helper.

## Risks and unsupported analysis

Read-only MCP artifacts: Event 3 `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5efd12ba399c44bd613f5d680c791cd89f2550ae6da34f54ca363590493ccaec/5a81ead4b8688aa9b0d5bc717b605ff4633e38611b57f606abc421626a3898d7/event-scan-5bd3d3e1d2cc.json`, Event 11 `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eab048c6788c8421b9c51d07bacafff60c63df6738c09d14d24c67b8dcd13621/e2563e2fa302077f0daeed47b7ea523ff15fc24f4e896c965ff508cbbd7d7bd5/event-scan-5bd3d3e1d2cc.json`, Event 12 `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a93b649637ab479f99556ff68ba8a82a1908a9cb814e128e975495cef5ada9f4/8f27d77680b738d46c5aec7cbe24205a80af5a647f7692dc4c15664feb7edca7/event-scan-5bd3d3e1d2cc.json`, Event 14 `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8f6e1ef42b6adbb8ad5020b47f092dd7b4ee1784f1f8368b80d9444e6f649c6a/0f2c457bcc5290c39e884fa1439cb91a9a520229bfbaadffffbd4a2ab701efa2/event-scan-5bd3d3e1d2cc.json`, and the Event Details GUI `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4c41ea7d0051a1e8491dd20a961a45d9ef74a839de92dd37236d1fb8429b9e1d/9ee93674eb31a7b7ebd1bbcb0138d8936b9e0daeceb4aaa3b6ac76ebab5aa3f0/gui-inspect.49458fe99a33df2d.json`.

The read-only HOI4 event scans completed with the large-workspace partial-analysis diagnostic, so the returned artifact is authoritative for the inspected event surface but not a workspace-wide clean bill of health.

The read-only GUI inspection completed for `events_log_popup_window` but reported pre-existing source-graph collisions, overlap, and truncation diagnostics; no GUI geometry was changed here.

Africa's source terminal branch already writes `world_end_africa_the_world` and emits super-event slot 104; this task only maps those existing identities into the shared Event Details contract.

The current Holy Realm terminal effect records `world_end_final_silence_completed` before requesting the separate Fallout aftermath, so the row preserves the stable Final Silence identity and treats either its active or completed flag as active rather than inventing a new Fallout row.

The Wendigo and Africa source routes retain their existing natural readiness conditions; this bounded change does not rewrite their gameplay gates or add a new route-specific trigger helper.
