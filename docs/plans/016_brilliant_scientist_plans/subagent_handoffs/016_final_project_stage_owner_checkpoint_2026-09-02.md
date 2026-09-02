# Event 016 project-stage receipt checkpoint

Date: 2026-09-02.

Status: narrow implementation and independent source review accepted for checkpoint; same-fixture probability comparison returned partial evidence.
This is a bounded lifecycle checkpoint, not completion of the project portfolio or Event 016.

## Contract and scope

The accepted closure contract now explicitly requires exact family/stage timer ownership, changed-only native Prototype settlement, invalid-context safety, and a separately verified no-DLC decision-board route.
This checkpoint implements receipt ownership for the 45 Theory, Deployment, and Weaponization decisions and the 15 native Prototype integration decisions.
It does not redesign stage costs, durations, priorities, family rewards, incident balance, no-DLC progression, or the other project-board actions that use the shared stage lock.

Changed gameplay files are `common/decisions/016_brilliant_scientist_directorate_project_board.txt`, `common/scripted_effects/016_brilliant_scientist_project_effects.txt`, `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt`, `common/scripted_effects/016_brilliant_scientist_effects.txt`, and `localisation/english/016_brilliant_scientist_projects_l_english.yml`.
The specification and project-system document carry the matching ownership contract.
No new visual asset, technology, unit, event, public meter, GUI, focus, achievement, or evolution is introduced.

## Implemented ownership

Every normal cancel and remove callback supplies its fixed family and stage.
Only a matching live receipt can settle or clear the order.
Normal finish also requires the exact predecessor, a valid current host and primary facility, and no actual terminal or world-end transition.
The generic upward-stage helper remains unchanged because inheritance legitimately restores a higher carried stage.

Native integration stores the same family/stage receipt at Prototype but deliberately omits `brilliant_scientist_active_project_capacity_delta`.
Zero is not stored because the existing Capacity and KRG-interruption consumers test variable presence.
Native project construction retains its own cost, duration, and output ownership.
The integration timer neither pays native costs nor reserves another wrapper burden.

The native completion helper advances only exact Theory with sufficient Capacity and valid live context.
Only a changed stage receives its family output, incident roll, runtime reconciliation, recognition, and permanent cumulative Capacity burden.
Native synchronization remains allowed while an integration timer is active.
A repeated completion or the remaining integration timer cannot award or charge the same Prototype again.

Finalization clears only the owned transient receipt and rebuilds available Capacity from gross Capacity, cumulative project stages, suspension state, and any remaining live reservation.
The rebuild runs after family-dependent effects because it uses the family temporary internally.
It does not return sunk equipment, fuel, manpower, experience, Political Power, or factory time.
Terminal cleanup closes an identified stage receipt before clearing laboratory pointers.

## Source review scenarios

These are explicit source-control-flow traces and arithmetic checks, not execution of the HOI4 engine.
The simple arithmetic examples assume gross Capacity 80, no unrelated project burden, and no incident changing the ledger.

| Scenario | Source expectation |
| --- | --- |
| Theory completes once | Start reserves 10, leaving 70; completion replaces the reservation with cumulative Theory burden 10, still leaving 70. |
| Deployment completes once | Prototype burden 20 leaves 60; start reserves 15, leaving 45; completion replaces that reservation with cumulative Deployment burden 35, still leaving 45. |
| Normal cancellation | Cancelling that Deployment clears its 15 reservation and rebuilds 60 from the unchanged Prototype ledger. |
| Mismatched family callback | The callback does not enter the owned branch; active family, stage, reservation, reward, and available Capacity remain unchanged. |
| Mismatched stage callback | A Theory callback cannot close a Prototype integration or a Deployment wrapper, even within the same family. |
| Native completion during integration | Theory burden 10 becomes Prototype burden 20 once; the integration owns no delta, so available Capacity becomes 60, not 50. |
| Repeated native notification | The exact-Theory gate fails after the first completion; no output, incident reroll, or Capacity mutation occurs. |
| Integration cancellation after native sync | Visibility loss can cancel the integration receipt; the committed Prototype burden remains 20 and no refund is invented. |
| Integration removal after native sync | The native helper no-ops, then the matching integration receipt closes; no reward or Capacity charge repeats. |
| Another family has a paid timer | Native completion preserves that active receipt and its delta; the gross rebuild retains its reservation. |
| Facility or host becomes invalid | Matching delayed finish awards nothing and closes its own receipt; mismatched callbacks remain no-ops. |
| Actual terminal or world end | The live-context gate blocks awards and the terminal owner closes the identified receipt before pointers are cleared. |
| Capacity was clamped during a timer | With gross 30, Prototype burden 20, and active Deployment delta 15, displayed availability is 0; cancellation rebuilds 10, rather than blindly adding 15 and inventing 5. |
| Kruger State interruption | Native integration omits delta and is excluded from the existing paid-wrapper interruption snapshot; paid normal wrappers retain their existing snapshot fields. |

Independent architecture and post-review evidence belongs in `016_final_project_stage_receipt_review_2026-09-02.md`.
Its postpatch review passed the requested 45/15 receipt correction and found no new in-scope ownership defect.
The earlier proposal for separate native-integration variables is superseded by the reviewed shared family/Prototype receipt with an absent delta.
The parent mechanically compared each exact prepatch wrapper with its postpatch counterpart: all 60 AI blocks, all 60 durations, all 45 native Political Power costs, and every temporary factory modifier are identical.
All 60 cancel/remove callback pairs contain the correct fixed family and stage.

## MCP evidence boundary

The retained before probability fixture is `E016_PROJECT_STAGE_LIFECYCLE_2026_09_02.scenarios.json`.
Its seven named scenarios and complete 60-candidate pool are unchanged.
The successful prepatch evaluate returned `PROBABILITY_ANALYZED_PARTIAL`, analysis `probability-1e1820c44d4143b5478752d0`, with 420 rows and 105 deduplicated unresolved items.
Nested custom eligibility remains unresolved; the 15 native integration scores resolve to 10 while the 45 advance scores retain the unresolved low-Capacity helper.
The separate probability handoff records exact source hashes, artifact URIs, schema corrections, and the completed same-fixture comparison.
The auditor's connection completed the single postpatch compare as `PROBABILITY_ANALYZED_PARTIAL`, analysis `probability-017b22b7e749254a8f109dd8`, over the same 420 rows.
It reported zero detected score/rank/declared-regression changes and 165 unresolved items, grouped as 120 custom-tooltip paths and 45 variable checks.
Both comparison sides resolve helper definitions from the current workspace, so this is not isolated historical-helper or engine-eligibility proof.
The exact artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6f3e91d12209bb88335f25a3dd12d8f2eadf87bf2fa73217ef82fda37d95ae4d/0950d22770d78865cc267d92ccf6c13e28eb23d49785b91a77ebc1eaec82f387/probability-017b22b7e749254a8f109dd8.json`.

The prepatch bounded Event 016 inspect returned `EVENT_INSPECTED_PARTIAL`, revision `65f53c2f4a099c16d11d6ab9960f409df2c881e6ad4b02f663cc098b6d5137bd`, with zero projected helper bodies and truncated inline inventory.
After the owner patch, narrow `hoi4.event_inspect`, `hoi4.event_render`, and `hoi4.event_compare` each failed with the exact transport error `Transport closed`.
The attempted current view was the `chaosx.nr16.1` neighborhood, depth 2, at most 40 nodes, without helper expansion.
No postpatch graph, visual comparison, callback-order certification, or engine scenario acceptance was produced.

## Remaining limits and queued work

Gross and available Capacity were previously changed and capped independently in some existing helpers.
Canonical rebuilding can expose or correct that prior drift; this checkpoint does not redesign gross Capacity growth or the 0–100 public range.

Native integration deliberately does not reserve Capacity while waiting.
If another native transition consumes the remaining available Capacity first, the integration closes without a stage reward and can be selected again when its native completion and Capacity requirements are valid.
This preserves the native payment and avoids over-capacity or duplicate settlement; reserving Capacity for integration would be a separate design change.

The other project-board actions sharing the progress flag, broader stage reward depth, strict affordability boundary issues, cost-count review, and no-DLC project progression require separate reviewed work.
No-DLC compatibility is a binding requirement, not a completed or silently substituted fallback.
Native decision callback order is not assumed: exact ownership makes cancellation-before-removal and removal-before-cancellation settle at most once for these 60 wrappers.
A complete Event 016 or all-projects claim is not supported by this checkpoint.

No model generation, model replacement, or live game launch was performed.

## Frozen source hashes

| File | SHA-256 |
| --- | --- |
| Project board | `6D58F497F4CB2E76537B15904ACB51B75B117AF0319259CB5F87D7A6B94F596B` |
| Project effects | `AF93CCABCB059F99BED1AEDF3D47B4F9816E471E6E16CCB96DF0F3964743640B` |
| Project triggers | `5B82CB6B8A816DB6039F7EAB08637CA62C9FBE667487E140DDD11A89216A05E8` |
| Main effects | `C20DC816356FB484E87510F7A2FBEF345F5F3C36494B6885709953F03EAEEB08` |
| Project localisation | `362C7D60A401FA8C7448D8101AAA2E3EB930E3214FEF72F470ED6869793A7004` |
