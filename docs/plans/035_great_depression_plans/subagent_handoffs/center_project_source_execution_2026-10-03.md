# Event 35 center-project source execution

## Disposition

Implemented as a bounded source-execution regression pass for the current parent patch. This handoff does not close the full Event 35 goal or establish native game behavior.

The user authorized this test and handoff scope on 2026-10-03 and identified the accepted Event 35 package under `docs/specs/035_great_depression_specs/`, especially the state lifecycle map, decisions and missions, centers and repeatability, and reusable crisis API. The applicable acceptance basis is recorded in that package manifest and index.

The Event and decisions/missions skills were read and applied, with the subagent handoff rules from the subagents skill. No skill files were changed.

## Before and after

Before this pass, the center-project lifecycle had no retained Event35 source-execution regression executable in the assigned scope.

After this pass, nine tests execute the production helper paths listed below against explicit country, state, registry, episode, and resource fixtures.

## Files changed

- `.tools/test_event035_center_projects.py`
- `docs/plans/035_great_depression_plans/subagent_handoffs/center_project_source_execution_2026-10-03.md`

No gameplay source, localisation, assets, spreadsheet, or AI weight files were changed by this task. The parent owns the concurrent production edits. No staging or commit was performed.

## Production source exercised

The test reads and executes the current definitions from:

- `common/scripted_effects/035_great_depression_effects.txt`
- `common/scripted_effects/035_great_depression_decision_effects.txt`
- `common/scripted_effects/035_great_depression_region_effects.txt`
- `common/scripted_triggers/035_great_depression_triggers.txt`
- `common/scripted_triggers/035_great_depression_decision_triggers.txt`
- `common/scripted_triggers/035_great_depression_decision_surface_triggers.txt`

The exercised helper paths include `great_depression_center_has_current_registration`, `great_depression_center_project_target_is_open`, `great_depression_center_project_has_unspent_authorization`, the reopen, public-works, lasting-capacity, and selector gates, `great_depression_authorize_center_project`, `great_depression_process_center_project`, `great_depression_complete_center_project`, `great_depression_fail_center_project`, `great_depression_write_center_project_ledger`, `great_depression_clear_center_state_flags`, `great_depression_clear_center_resolution_receipts`, `great_depression_clear_registered_center_runtime`, `great_depression_reconcile_center_transfer`, `great_depression_adopt_transferred_center`, and the already-validated-row `great_depression_apply_inherited_center_state` helper.

The paid decision paths execute `great_depression_reopen_selected_center`, `great_depression_launch_regional_works_program`, and `great_depression_convert_works_into_lasting_capacity`, including the production cost refresh, affordability triggers, `great_depression_commit_country_action`, `great_depression_pay_action_cost`, `great_depression_record_action_receipt`, and the public Severity update path. The executor debits the fixture resources from the actual cost-family branches, checks the `great_depression_action_lock` native flag identifier and seven-day duration, and verifies caller-created temporary action storage survives nested helpers and disappears when its caller returns.

Transparent `custom_trigger_tooltip` and `hidden_trigger` blocks evaluate their contained trigger predicates. They are not skipped or treated as unconditional success. Unknown commands fail the test with helper ancestry and a source line.

## Cases and outcomes

The final run passed all nine tests:

| Case | Production behavior exercised |
| --- | --- |
| Reopen, Public Works, lasting capacity, and protection | Each paid authorization receives a distinct serial, completes only after total work time, keeps the center episode identity, updates every project ledger column, and grants the lasting-capacity receipt once. Clearing treatment flags later does not erase that one-shot receipt. The explicit protection completion branch also closes only after its full work interval. |
| Active project slot | A second project gate and action are rejected while a project is active, with no resource debit or cooldown write. |
| Old or foreign episode | A stale episode and a state owned by another country fail the real center target gate without payment. |
| Duplicate completion | A second completion call changes no project state, completion count, or reward. |
| Failure and retry | A failed later project leaves the earlier completion receipt and authorization ID intact. A newer paid authorization remains distinct from both spent IDs. |
| Inherited failed receipt | The test applies inheritance to an existing, prevalidated registry row. It does not append a second row. A failed receipt survives reclosure and a new paid reopening clears only the active failure marker. |
| Completed-project transfer | The state episode changes to the successor episode while the completed project episode and its serial/spent receipts remain historical. |
| Pending-project transfer | Pending work pauses at transfer, adopts once without a duplicate row, rebinds to the successor episode, preserves authorization serials and work, and does not count the lost interval as work. A second transfer opens once after adoption closes the first contract. Losing another registered center without a project leaves this center's active slot intact. |
| Terminal cleanup | Cleanup removes active state and project receipts only for the matching episode, clears the current project episode and working fields, and retains authorization serial and spent IDs. A foreign-episode center remains intact. |

The completed-project transfer case deliberately expects `great_depression_center_project_episode_id` to retain its original value when no work is pending. The pending-project transfer case separately expects that field to bind to the successor's current episode.

## Validation

Executed `python .tools/test_event035_center_projects.py` against the current shared working tree after the final center-project and transfer changes. Local result: 9 tests passed. The parent independently reported a successful 9/9 run of the same test tranche.

The parent did not provide a separate command line or source revision for its independent run, so only the local command and source hashes below are pinned here.

### Source identities

SHA-256 values were recorded from the exact files read by the local test run.

| File | SHA-256 |
| --- | --- |
| `common\scripted_effects\035_great_depression_effects.txt` | `B8AA8FE47A50784E9F2C6741820BE435F1444F961DD0214E4E171B6C45FAC617` |
| `common\scripted_effects\035_great_depression_decision_effects.txt` | `CDFD04CD08B8BED67BECDD7982516580BDF9359FE6E3F053288EE4B08EC479BE` |
| `common\scripted_effects\035_great_depression_region_effects.txt` | `75601200A8918B5524388B3DA7734F45637E90770804134B14AAAC09A74A55AE` |
| `common\scripted_triggers\035_great_depression_triggers.txt` | `FE2DC15DC22EA0D8F9336C7120412B1DA66CF7F7348D43E7EE1D7A72BC1566CA` |
| `common\scripted_triggers\035_great_depression_decision_triggers.txt` | `3CE93091974DD24754E26BE77F14218218DE6FC3E5E2728ECCACA06EDFECD7D8` |
| `common\scripted_triggers\035_great_depression_decision_surface_triggers.txt` | `FB98BB27A94888F9A6B45C1DA50E21DA843D84A51AD91D83603D7B62A27F18A1` |
| `common\script_constants\035_great_depression_constants.txt` | `B14E552EE2176907C3BF05EC2324E7F58A06C72D4F4865DCF3C9A9160AAEB1E7` |
| `.tools\test_event035_center_projects.py` | `E5A15507DD0674CE275535262DF8F28F591E29FCBCA0592A23646125608A1400` |

The production `complete_center_project` block parses from its definition through its helper close. The reopened-capacity, protection, and terminal project bookkeeping branches execute under the matching helper scopes. The code also rejects state-scope use of the country-only `exists` trigger, so the current registration gates must prove state identity through the state row and episode.

The first harness run reported parser defects, not gameplay failures: nested assignments were indexed as top-level helpers, then scoped arrays and the new tooltip wrappers were unsupported. Those were fixed in the test executor. The only semantic expectation correction was the completed-versus-pending transfer distinction described above.

## Limits and follow-up

The inherited-region test calls `great_depression_apply_inherited_center_state` with an explicit already-validated existing-row fixture. It does not prove `great_depression_validate_inherited_region`, `great_depression_preflight_inherited_region`, `great_depression_commit_inherited_region`, or the public `great_depression_register_inherited_region` transaction.

The native humanitarian pressure consumer is outside this task. The test records the `great_depression_submit_humanitarian_center_pressure` call in an explicit external-consumer fixture and does not invent an acknowledgement or callback success.

No Event 35 refund helper is defined or called by the inspected effects, decision-effects, region-effects, or decision definitions. The handoff therefore makes no refund claim. A rejected authorization after the production upfront debit is not exercised as a refund path.

The executor models native resource changes as fixture state and records timed-flag requests. Its date advancement and timed-flag expiry are model behavior, not observation of HOI4. No HOI4 process was launched and no live-game proof is claimed.

No AI or mission weight was changed or analyzed by this tester.
The changed shared target gates affect weighted decision eligibility, so the parent separately routed their immutable before/after sources and matching scenarios through `chaosx_ai_probability_auditor`.
These deterministic tests do not close that probability comparison or campaign balance requirement.
