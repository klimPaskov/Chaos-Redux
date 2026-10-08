# Event 033 severe-impact report return storage

Disposition: implemented bounded caller-storage repair; remaining F7 report work is unresolved.
The user's stored-fact report contract and Part 9 require the actual severe or superstorm episode and protection status to reach the responsible country's report.

The report preparer returns `acid_rain_impact_episode_key`, `acid_rain_impact_evacuation_status` and `acid_rain_impact_end_day` through temporary storage.
The original positive-loss caller did not reserve any of those three outputs before invoking it.
The caller reserves all three immediately before the helper, inside the existing positive-applied-loss and severe/superstorm guard.
This changes no mortality request, helper contract, accounting receipt, condition, weight, duration, cost, cap, Air mutation or report-ledger policy.
The preparer and the following controller/report consumers remain byte-identical.

Before runtime is `e5c34d8bd73971609e26b7aef2d4a01cdd4f3f795c2856d83189dfcd546f5def` in commit `0a2927e9b34d94f81758dba7070376bcac8cd0e2`.
After runtime is `3eb102bf6168362eadd58188d45791cd81f9713dc379d9e08da325334e65bd48`.
`.tools/validation/test_033_report_return_storage.js` checks exact whole-file reversal of the three declarations and executes the unchanged actual preparer body under declared state scalar and helper-frame fixtures.
Twenty-six cases cover severe/superstorm identity, no/partial/finished evacuation, present/absent stored end dates, cold and stale ambient outputs and two immutable cold before-source negative controls.
Unknown scalar facts fail rather than becoming invented zeros.
The native exact-loss guard, controller scope entry, report delivery, episode deduplication, physical damage, prevention accounting, migration and display evaluation are not executed by this narrow test.

Required references are the installed `set_temp_variable` section at `effects_documentation.md:7820-7827`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, and the caller-owned temporary storage rules already read for the preceding repairs.
The report helper's full unshadowed source was read directly, and the native report-sender lookup at `3379-3406` is retained in `report_episode_source_checkpoint_2026_10_08.md`.
Reference and model evidence are not native execution evidence.
The narrow live source lookup returned the unshadowed positive-loss caller slice at `3310-3335`, helper-index revision `4bc59cc32988a6b07ef1d864c993e1428e944c6944cc76a80b7e754b5b7bf728`.
It shows the original positive-applied-loss guard, the three declarations and the following controller consumer; its empty validation-check list is not native gameplay acceptance.

The maximum-only episode receipt still suppresses an older overlapping episode's first report.
Actual impact damage is applied after the current mortality/report helper, and mutable country report fields may also require a retained per-episode payload.
The architect's bounded F7 audit remains read-only and does not authorize an inferred migration history or an overflow/report-drop fallback.
The sealed F6 E5 receipt remains historical at its original source hash and is not relabelled as current report-repair evidence.
No fallback or simplification is introduced by this three-line caller repair; Event 033 remains incomplete.
