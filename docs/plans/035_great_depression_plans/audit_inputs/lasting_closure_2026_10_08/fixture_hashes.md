# Lasting-capacity closure audit fixture identities

All digests are SHA-256 over the checked-in bytes at the paths below. The parent-provided source snapshots and original six-case fixture are immutable inputs for this audit.

| Input | SHA-256 | Use |
| --- | --- | --- |
| `before/decisions.txt` | `AA6357DB29620998A29C7FD666857D3F95106F362C2099F8673C754EC94DAB14` | Pre-patch `common/decisions/035_great_depression_decisions.txt` bytes |
| `before/surface_triggers.txt` | `80C139E893740963248DB726C264FBD36C682A2BDABF39ABACD0A1E7BC85255A` | Pre-patch `common/scripted_triggers/035_great_depression_decision_surface_triggers.txt` bytes |
| Live `common/decisions/035_great_depression_decisions.txt` | `EF05B0A0C53F9EE804F1C3FE1128A51B18F8916974C2EA38B42D00A07825C080` | Post-AI-factor-condition source; before decision bytes remain pinned at `AA6357DB29620998A29C7FD666857D3F95106F362C2099F8673C754EC94DAB14` |
| Live `common/scripted_triggers/035_great_depression_decision_surface_triggers.txt` | `B8E69B3F9196EA8BDBEE08C6885792A07222AE1ED14CC9C9DD6E81B3100B6369` | Post-patch trigger source containing the owner-applied closure gate |
| Initial observed `common/scripted_effects/035_great_depression_decision_effects.txt` | `F29884873961B254D8357BBCF016FC0FCC111232642E41B2C95BECBDBC082953` | Hash recorded during the first source read; no immutable before bytes were retained |
| Current `common/scripted_effects/035_great_depression_decision_effects.txt` | `2919E0882EEA6EDF59183B4CDD79D757378D165FA7C4E1B1A3C774B2131F178D` | Owner-reported stale/depleted-click payment preflight using `great_depression_can_pay_public_works`; no cost coefficient change reported |
| Live `common/script_constants/035_great_depression_constants.txt` | `E516D865F9EE45DED5B2D49950B536F02081F6CC8043F1119087B04AC69E3773` | Current decision AI-weight and cost constants |
| Live `common/scripted_effects/035_great_depression_effects.txt` | `235C9A3775913C41DEA22940A0AB4FCEC7BB23D887D524256231E8BBF9C563A3` | Current completion receipt producer (`great_depression_public_works_last_completed_*`) |
| `lcc_scenario_set_2026-10-08.json` | `1014D69C7AC8EAD604206D7930E1FA405B9296A92FE9A3F120E761C8BC5B80EB` | Parent-provided six named cases, retained unchanged |
| `lcc_scenario_set_2026-10-08_ger64.json` | `69C147070093ADBF3C848B2E3E6DF4D1605E882C20139D805E074F448C93311C` | Audit variant using GER, state 64 (Berlin), matching ownership/controller and specified resource reserves |

The GER/state-64 variant preserves all six scenario IDs, route and project states, completion/failure receipts, episode IDs, phase variants, AI profile values, and cost variables from the parent fixture. It maps the placeholder country/state identifiers `AAA`/`121` to `GER`/`64`, adds the actual `trigger.is_controlled_by` input required by `great_depression_selected_center_target_is_valid`, and sets country resources to 500 political power, 500000 manpower, 5000 fuel, 500 trains, and 20 available civilian factories. It does not add eligibility overrides or invented predicate keys.

The current source cost constants at cost factor 1 are 25 political power, 500 manpower, 500 fuel, 2 trains, and 1 civilian factory. The larger figures above are the scenario's available reserves, not cost coefficients. No immutable before snapshot was supplied for the constants file, so this manifest does not claim a byte-for-byte constants comparison.

The parent reports three post-patch LCC test methods covering the six named positive/negative cases, four direct rejected-payment cases, and five malformed-plan proofs, with all 88 test methods passing in 87.871 seconds. This auditor did not run those tests.

Scenario IDs, in fixture order: `LCC-PAID-COMPLETED-STABLE`, `LCC-REOPENED-NO-WORKS`, `LCC-FAILED-WORKS`, `LCC-STALE-EPISODE`, `LCC-PANIC-COMPLETED`, `LCC-REPEAT-CLOSED`.

The connected probability adapter accepted the GER/state-64 fixture and assigned scenario hash `bacb1dfe46e4c6a7bbdb6848e4b450b5df7f7955832bb93c06a94ff2fd14caf8` for both the target evaluation and same-six comparison. The analyzer marked both partial, so hash stability proves fixture identity, not complete state coverage.

The parent-provided source-harness baseline is: paid completed stable = true; reopened/no works = true; failed works = true; stale episode = true; Panic/completed = true; repeat closed = false. Only the first and last outcomes match the accepted closure invariant.
