# Event 032 payload observation hooks

Date: 2026-10-08.
Disposition: `implemented` for the bounded source patch, with final integrated tests owned by the parent.
Acceptance basis: the parent's explicit PATCH instruction for the transaction map in `032_payload_observation_boundaries_2026-10-08.md`, including temporary country-scope arrays for nuclear return notifications.
All 14 mapped call sites are installed across the five authorized runtime files.
No pending hunk or in-place write blocker remains.

| File | Owner | Notification line |
| --- | --- | --- |
| `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt` | `sov_nuclear_bombs_initialize_event_state` | 581 |
| `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt` | `sov_nuclear_bombs_credit_evolution_devices` | 430 |
| `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt` | `sov_nuclear_bombs_register_production_devices` | 460 |
| `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt` | `sov_nuclear_bombs_commit_reserved_device` | 785 |
| `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt` | `sov_nuclear_bombs_operationalize_breakaway_site` | 1305 |
| `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt` | `sov_nuclear_bombs_mark_site_transferred` | 1447 |
| `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt` | `sov_nuclear_bombs_return_site_custody_to_soviet` | 1610 |
| `common/scripted_effects/biological_facility_capture_effects.txt` | `bio_facility_capture_initialize_exact_state_ledger` | 192 |
| `common/scripted_effects/biological_facility_capture_effects.txt` | `bio_facility_capture_restore_on_original_recapture` | 262 |
| `common/scripted_effects/biological_facility_capture_effects.txt` | `bio_facility_capture_transfer_fraction_to_controller` | 385 |
| `common/scripted_effects/biological_stockpile_safety_effects.txt` | `bio_stockpile_safety_resolve_selected_ordinary_accident` | 751 |
| `events/biological_native_raid_bridge_events.txt` | `biological_native_raid_bridge.1` | 65 |
| `events/biological_native_raid_bridge_events.txt` | `biological_native_raid_bridge.2` | 127 |
| `events/biological_native_raid_bridge_events.txt` | `biological_native_raid_bridge.3` | 189 |

COUNTRY methods keep the existing actor ROOT and call `missiles_note_payload_change` directly after the accepted transaction's final reconciliation or opening assessment.
The breakaway operationalization method enters its proven living country holder after reconciliation and only when the native-with-holder receipt exists.
The biological initial-capture notification runs in the recorded original arsenal custodian, after the state ledger and existing notices.
Original-custodian recapture notifies CONTROLLER after ledger closure.
The completed facility-recovery transfer notifies CONTROLLER once when its existing transaction total is positive.
The ordinary stockpile-accident notification remains inside the existing supplied-loss-proof branch, after the selected outcome notice.

The three biological bridge calls follow their resolvers inside the existing exact actor/agent/outcome identity gates.
They therefore also observe native equipment already collected for failed or rejected-release outcomes.
They do not add a debit, refund, policy change, or new raid result.

## Temporary notification identities

`sov_nuclear_bombs_return_site_custody_to_soviet` clears its private TEMP array `sov_nuclear_bombs_return_payload_notice_countries` before entering the transaction.
The old holder is appended as `THIS` only inside the existing native-debit branch, immediately after that debit.
SOV is appended in a separate SOV scope immediately after the existing native credit, without rewriting the credit.
Both country objects survive the existing holder-pointer overwrite for notification purposes.
Only after the accepted settlement's final reconciliation does a `for_each_scope_loop` notify living recorded countries.
`sov_nuclear_bombs_return_payload_notice_break` is explicitly reset to the existing `constant:sov_nuclear_bombs_ledger.zero` immediately before that loop.
The TEMP array is cleared after the entire accepted/rejected branch structure.

The transfer helper uses the same bounded pattern with distinct private names, `sov_nuclear_bombs_transfer_payload_notice_countries` and `sov_nuclear_bombs_transfer_payload_notice_break`.
This records only the actual native debit source from the existing holder or SOV branch, avoiding a notification attributed to a country whose stock did not change.
The transfer array has at most one entry, and the return array has at most the donor and SOV.
Any coincident country entries still delegate to the parent's coalesced observation helper and do not repeat stock effects.
Neither array is returned to callers or persisted, and no regular event target or ownership field was added.
Both arrays are initialized in the owning helper, consumed there, and cleared on exit.
No notification is emitted from the arithmetic branches themselves, which only capture temporary identities.

## Preservation and verification

- The five pre-edit raw hashes matched the reviewed current-byte inventory. No Git command was used.
- Every edit used `apply_patch`. The first runtime-file request failed context matching before writing, and its unchanged raw hash was verified. Corrected hunk anchors then applied successfully. No file replacement, removal, permission change, or recovery fallback was used.
- Removing only the exact owned additions in memory reproduced every pre-edit raw SHA-256 without line-ending normalization. This proves preservation of the pre-existing stock, policy, receipt, ownership, outcome arithmetic, and other owners' source edits.
- Source-location MCP reads resolved all 14 inserted calls to their intended owner and branch. The two notification loops are inside accepted settlement branches. Original capture enters `var:bio_stockpile_safety_arsenal_actor`, recapture enters CONTROLLER, and native bridge calls remain actor-country immediate effects.
- Source review verified array reset before either transaction, donor registration only in actual native-debit branches, SOV registration after the existing credit, notification after final reconciliation, separate immediately reset loop-break names, and final array cleanup after rejection paths.

| File | Pre-edit raw SHA-256 | Post-edit raw SHA-256 |
| --- | --- | --- |
| `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt` | `5731ac6922418322fc7d6870ff015d07d1c6465c47951b32e917313c8c683f9f` | `04c47079103a684bf02f220f5e097a7b2aec9914e4bfff69a27aedc1a5bfb8ba` |
| `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt` | `8a071d832f2aabf8a4c37ac85680ebcd61be60bc4a4b912449d28e407d2de338` | `9cf6c619f477c6989a724029463e078603155f4ab2f83585021393696f027db7` |
| `common/scripted_effects/biological_facility_capture_effects.txt` | `00d870fe2fc877ca389368b5809b5b9ec741fcf9bab018fdf524fc158fad34f0` | `50861b7a8314c698d11a7a40ade3e35cc2de614cf8c03db15c80c65ac7c8a47f` |
| `common/scripted_effects/biological_stockpile_safety_effects.txt` | `610af2118ef4fa2a5b195c4e799f12dbfe97475ce66c8374ab4286bf54285c75` | `f0e4fcace8370241dfce862d9c2668e18fee709117d30cf7f748e7a6f378a06b` |
| `events/biological_native_raid_bridge_events.txt` | `5796e5527386360858b3bfc9fa7ca85f2dc6b03c92a8c27fe774325d0085bbbc` | `fbd946402156b30a69f26e04ae361cf2a59db02a65ef5c3f2d0656386f2de038` |

## Source and MCP references

The events, subagents, and native-raids skills remain applicable, and the events skill's `references/loop-break-isolation.md` was read for the private-loop rule.
Installed `documentation/effects_documentation.md:2312-2326,2763-2772,4296-4311`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, was read through the reference tools for temporary arrays, current-scope entries, array clearing, and explicit break variables.
Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:1086,1217`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, provides `THIS` scope entries and scope-changing foreach behavior.
Installed vanilla `common/scripted_effects/GER_scripted_effects.txt:1264-1286` was inspected as a scope-array iteration precedent.
The prior reviewed handoff retains the native-raid scope and cost references and bounded pre-edit event artifacts.

The unchanged notifier resolved through `hoi4.source_lookup` at revision `5a467cfde2ebf8882b88fc4f9e07445e33a2f264eded15274bc2db2756d0cdee`.
Post-edit owner locations resolved at revision `407b5cf14526b108a2c0515f1e4ea443333360ac4b6b4adf0d0b4d17c555dc1e` for scripted effects and `95498c8e74cc3cf7098a3ab8f62817e579dda48cf465db9ab663ddb254b309a5` for bridge events.

`hoi4.script_validate` on the STATE-scope return-notification structure returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, with syntax, command-kind, and declared-scope checks.
It checked five native commands, left the dynamic holder scope unresolved, and left three argument blocks unchecked: `add_to_temp_array`, `set_temp_variable`, and `for_each_scope_loop`.
No findings were omitted, and `parametersChecked = false`.
The supplied holder binding did not resolve the `var:` expression in this checker.
The installed array documentation and source scope proofs above were reviewed separately, and this result is not described as complete engine validation or loop-body coverage.
Validation documentation revision: `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.

## Integration limits

Final tests remain with the parent, including accepted and rejected returns, inherited default/private break values, repeated calls with stale temporary storage, old-holder and SOV notification identity, and coalescing when several owners notify in the same hour.
No runtime execution, probability comparison, full event render/compare, or parent fixture suite was run here.
The implemented sites provide finite transaction observations and do not establish immediate discovery of generic native production, research, raid collection, or cancellations without a proven callback.

No new numeric tuning, stock grant/debit, refund, policy change, persistent ownership state, periodic reconciliation hook, lifecycle-tick hook, or chemical duplicate was introduced.
Event 023 and Event 076 ownership remains unchanged.
The retired operative-effect and operation-definition paths remain absent.
The only additional file written is this handoff. Existing helper definitions and their separate documentation remain parent-owned.
No Git, game, logs, unrelated source changes, or subagents were used.
No gameplay simplification or omitted mapped hook remains in this patch.
