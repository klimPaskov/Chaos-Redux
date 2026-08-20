# Event 006 dormant carrier release fix

Date: 2026-08-20.

Disposition: implemented source fix; Event 006 remains a partial system and no live-game completion claim is made.

## User-facing defect

The pre-event Independence Wave Crisis decision/category surface was not allowed to exist before the event fired. That surface is retired: no live crisis category, pressure decision, pre-event mission, crisis cost localization, or queue remains in the active decision UI. The hidden `chaosx.nr6.1` entry is the first player-facing release entry, and `chaosx.nr6.2` is shown only after a committed release.

The reported `capital_scope` errors came from fixed dormant package checks that tried to resolve a capital on an unformed carrier. The Banat, Thrace, and Epirus package checks now use fixed state scopes with `is_capital = yes`, so they do not dereference `capital_scope` on an absent carrier.

## Release-path correction

Several Event 006 tags have startup character shells so their character definitions can load. They are not playable countries: they own and control zero states. The old `exists = no` gate rejected those empty shells, so automatic allocation could select no executable rows even though the package and anchor were valid.

`is_independence_wave_dormant_country_scope` now accepts either an absent tag or an existing tag with zero owned and controlled states, no active/prepared/committed Event 006 origin flags, and no living-country state footprint. Living countries remain rejected.

The generic country reservation effect accepts that dormant shell form and still rejects duplicate country-array entries. The execution metadata validator and normal/SCN-008 package preflights use the same dormant predicate. The immutable package identity trigger also permits the target's reservation marker when it belongs to the current plan, because the marker is set before execution preflight; stale reservation markers from another plan remain rejected.

This preserves the release order: reserve the dormant target, validate the frozen package, set the anchor capital during finalization, release the target, transfer the frozen states, then commit the public event report. No pre-event category or pressure surface is reintroduced.

## Changed files

- `common/scripted_triggers/006_independence_wave_package_triggers.txt` adds the dormant empty-shell predicate and current-plan reservation allowance.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` uses the dormant predicate for normal and SCN-008 preflight branches.
- `common/scripted_triggers/006_independence_wave_iw093_iw098_package_triggers.txt` uses the dormant predicate for the fixed-origin preflights.
- `common/scripted_effects/chaosx_liberation_release_effects.txt` accepts dormant empty shells when reserving a country and reports living-tag rejection otherwise.
- `common/scripted_effects/006_independence_wave_execution_effects.txt` validates dormant reserved targets instead of requiring literal tag absence.
- `.tools/audit_event6_allocator.py` accepts either a missing target or the new dormant predicate in its execution metadata audit.

The compact decision-cost localization is already present in `localisation/english/006_independence_wave_decisions_l_english.yml`; this source fix does not re-expand or alter those cost rows.

## Evidence

`python .tools/audit_event6_allocator.py` passes with 149 publishers, 40 runtime adapters, 32 attested packages, 29 compatible groups, and no pre-event crisis category, mission, cost, or queue.

The reported Banat, Thrace, and Epirus package trigger files contain no fixed numeric `capital_scope` check after the repair.

Focused `hoi4.event_inspect` lint and `chaosx.nr6.1` state-flow inspections returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics at revision `a0d209ec728fe48cc44e3412c64b7c86ab0d1fea28713348d4dac1ba52035c67`. Lint artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/06c0973c3cdae3e2636a45bb609d7118eb85cff4b5dcbc5b1b3c4b97ac34ac6c/891ae50f3ef612dc26b61c5df5c06e4c6a9422b10165dc8ec6fdcce00c5f2334/event-lint-a0d209ec728f.json`. State-flow artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/532d60b273918d4a5121c0fd0d5ec02727925b54a29f2667c2bc159d90fdcdd8/162d969ee7ef3fb6970691f6f09858f0fee42ef546ebe2685500486e3800dd8c/event-state_flow-a0d209ec728f.json`.

The MCP result remains partial because the large workspace defers workspace-wide helper and lifecycle projection. No live game was launched and no in-game release result is claimed here.

The mandatory weighted-surface inspect of `common/scripted_effects/006_independence_wave_package_planner_effects.txt` returned `PROBABILITY_SOURCE_INSPECTED` with `poolComplete = false`, zero discovered candidates, and zero unresolved diagnostics under the custom weighted-pool adapter. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/66af6e2a1d85942e62c502de106b378ed196df8a20b44f98d5656f525098e24d/1acb071505f52c02858ccf7f3e7e730a5186764adb397734df14a9975c4ac581/probability-inspect-998f95c632e0.json`. This is structural evidence only and does not support a quantitative balance claim.

## Remaining boundary

Packages that are not in the current adapter/content-attestation authority remain fail-closed. This fix makes the release transaction able to consume an accepted package whose registered tag exists only as an empty startup carrier; it does not invent missing country packages, portraits, flags, or admission evidence.
