# Event 39 player condition parser repair

Status: the three parser repairs are implemented; native confirmation remains pending and the probability comparison is incomplete.
Scope is exactly three unsupported `is_player = yes` conditions replaced with `is_ai = no` under the existing `OR = { is_major = yes ... }` conditions.
The intended predicate is major country or human-controlled country.
No AI weight, random selection operation, surrounding condition, scope, or mechanic is redesigned.

## Files and exact conditions

| File under `common/scripted_triggers/` | Line | Owning trigger |
| --- | --- | --- |
| `039_murder_mystery_integration_triggers.txt` | 16 | `murder_mystery_prefire_host_is_valid` |
| `039_murder_mystery_integration_triggers.txt` | 77 | `murder_mystery_foreign_high_value_leader_is_safe` |
| `039_murder_mystery_runtime_triggers.txt` | 108 | `murder_mystery_host_is_valid` |

Exact backups are under `docs/testing/live_qa/2026-09-04_catalog_01/pre_patch_event39_player17/common/scripted_triggers/` with matching filenames.
Backup creation checks the source hashes captured during initial inspection and refuses an existing backup destination.
Applying the patch also compares each current file against its exact backup to prevent overwriting concurrent changes.

Integration trigger before SHA-256: `f4c079446f2a4ad4e7928f8c2324bdbc87f9a471700fa05a9ab41e755d707fa9`.
Runtime trigger before SHA-256: `3e55839890b2b3827d3cd29c8de1222956510c2f8407666d78cd430b577e15e1`.
Integration trigger after SHA-256: `b22b9346977ee0efd41d832ac862dca6312094b96dbef78d2589776c1287a52f`.
Runtime trigger after SHA-256: `b5e45b0d09c95c7b670aec96a9150f11a804f1af705c80d6e064872cce94cfd0`.
The owner applied the three exact token replacements after a prepatch `probability_inspect` call; all other bytes match the backups.
The four intended-polarity scenarios in the table were checked explicitly.

## Evidence and country scope

The parent-provided `logs/launch_16/logs/error.log` records the three `Invalid trigger 'is_player'` errors at lines 415, 417, and 419, each followed by an `Unknown trigger-type` diagnostic.
Installed vanilla `documentation/triggers_documentation.md:5244` documents `is_ai`, explicitly states `Supported Scopes: COUNTRY`, and defines it as checking whether the country is AI controlled.
The offline `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md:284` confirms the Boolean argument.
Vanilla `events/AAT_Iceland.txt:74` uses `OVERLORD = { is_ai = no }` as a country-scope precedent.
The supported inverse Boolean therefore represents the intended human-controlled branch without adding a `NOT` block or changing the existing `OR` polarity.

- Prefire: `events/039_murder_mystery.txt:16` declares the entry as a `country_event`, and its trigger calls `murder_mystery_prefire_host_is_valid` at line 22.
  The same helper is called in `any_country` in integration triggers line 36, in the saved prefire country target at line 43, and in `every_country` in `039_murder_mystery_integration_effects.txt:32`.
  That `every_country` filters candidate countries before the unchanged ticket-weighted host selection.
- Host registration: the same entry event invokes the opening package in country scope, which calls `murder_mystery_register_original_host` at integration effects line 370.
  Runtime effects line 231 checks `murder_mystery_host_registration_is_valid`; runtime triggers line 121 delegates to `murder_mystery_host_is_valid` without changing scope.
- Foreign target: `039_murder_mystery_decision_effects.txt:547` calls the foreign transaction inside `event_target:murder_mystery_selected_cell`.
  The selected-cell target is saved inside `random_neighbor_country` in integration effects lines 1330–1345.
  Its country-scoped transaction checks `murder_mystery_foreign_high_value_leader_is_safe` at integration effects line 819.

## Intended Boolean behavior

Other unchanged gates are assumed true for this isolated truth table.

| Scenario | Major | Human controlled | Intended former predicate | Supported replacement |
| --- | --- | --- | --- | --- |
| major_ai | yes | no | true | true |
| major_human | yes | yes | true | true |
| minor_ai | no | no | false | false |
| minor_human | no | yes | true | true |

This table proves intended Boolean polarity, not the behavior of the engine when it encountered the invalid former trigger.
The invalid source was not an operational probability baseline.

## MCP evidence and limits

Narrow event trace and neighborhood render used `chaosx.nr39.1` and returned `EVENT_INSPECTED_PARTIAL` / `EVENT_RENDERED_PARTIAL` at revision `17b3aac359b767085af37746c2ad9e7a1bc9437f4d9712ff9ce7e3d72ba43614`.
Both report `validation.passed = false`, deferred helper projections and lifecycle passes, and zero indexed helpers.
This limited graph evidence does not prove helper behavior or native parser acceptance.
The post-change `event_compare` call requested the captured inspection revision and returned `EVENT_REVISION_NOT_CACHED`: "Requested event graph revision is not cached".
No graph-equivalence claim follows from that failed comparison.

Trace artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d747cd3ab5262caedbef3b7b0ef0ffc6db4e5cdc02378f8637f74328edd812b3/b833cf5b950698d2ff8e76f54b2e8124ddfcee8d3a000eb97badd40bbe67ce2b/event-trace-17b3aac359b7.json`.
Render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/19e4af0b72abef1edd681a0cae1c0bafec86bc6b65077e56fc74c9ef9f46a814/738588cb9fc18a14961a9c9ab66804f79cc283952169d2e2a4bd61a188d78220/event-neighborhood-17b3aac359b7-manifest.json`.

The prefire eligibility helper is an input to a ticket-weighted pool, so `chaosx_ai_probability_auditor` was routed for the mandatory read-only baseline and comparison evidence pass.
No numeric pool weights or balance targets are invented for this repair.
The owner's prepatch `probability_inspect` requested `custom_weighted_pool` with the integration effect file and identifier `murder_mystery_select_weighted_prefire_host`.
It returned `PROBABILITY_SOURCE_DISCOVERED` but `discoveryReason = identifier_not_found`, zero candidates, and no available adapters for the selected identifier.
This result cannot certify the custom pool.
Prepatch probability artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/194503d20cf13b18d43c983e68120b631fc969b7df7175bca1ec3fd043a9c4fe/540a6bde668b4b605f87c64f6943a89becc97df3c30ab45a55fa9adb1268df6c/probability-inspect-78983f42b93e.json`.
The delegated auditor had not returned evidence after repeated bounded status requests, so its run was interrupted and a compact evidence-only final requested.
The mandatory probability comparison is therefore incomplete at this handoff; no unreturned auditor result is counted as validation.
The known analytical limitation is that the selected custom ticket pool was not discovered, and a complete declared pool with external ticket factors was not supplied.

## Remaining limits

No game launch or commit is performed by this worker.
Native parser confirmation belongs to the parent QA run.
No helpers, constants, event targets, cleanup logic, localisation, or assets are added.
No simplifications are introduced.
Skills used: `chaos-redux-events` and `chaos-redux-subagents`; none created or modified.
