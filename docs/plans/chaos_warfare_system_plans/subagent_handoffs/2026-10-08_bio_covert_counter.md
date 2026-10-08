# Biological covert achievement continuity repair

Date: 2026-10-08.
Disposition: implemented in source under the parent's accepted narrow repair, with engine evidence limits below.
Ownership: only the biological recorder and misplaced biological-success block inside the chemical recorder in `common/scripted_effects/cbrn_achievement_effects.txt`.
The parent reviews and commits this repair.
No index or commit operations were performed.

## Acceptance and completed behavior

The parent explicitly authorized this continuity repair while retiring the competing biological intelligence-operation interface under accepted amendment 13.
The acceptance basis for that interface remains `docs/specs/chaos_warfare_system_specs/specs/13_2026_09_20_accepted_cbrn_overhaul.md:5-17` and the bounded source map in `2026-10-08_competing_biological_operations.md`.
This patch preserves shared covert achievement capability after the public-interface retirement.

`cbrn_achievement_record_biological_operation` records the biological covert family and increments the distinct operation-type count once.
Every accepted covert use-history invocation separately sets covert history, increments the covert operation count, and initializes the first-operation day only when absent.
Both `operative_release` and `food_water_medical_sabotage` still qualify.
The shared `operative_release` route remains available to Event 016's existing native owner.
A qualifying covert `bio_seed_result = constant:bio_lifecycle_result.success` records the shared strategic-result history inside the biological recorder.
The identical biological check was removed from the chemical recorder, where stale biological seed values could otherwise set that flag.
The chemical recorder's own covert success/catastrophic-result condition is structurally identical to the frozen baseline.

No achievement enablement, thresholds, disqualification flags, policy, random selection, payments, native callback deduplication, or other achievement logic was changed.
The hidden achievement registry remains untouched.
No gameplay simplifications were made.

## Helper contract and migration map

| Helper or call site | Scope | Inputs | Outputs and side effects | Contract and migration |
| --- | --- | --- | --- | --- |
| `cbrn_achievement_record_biological_operation` | Actor country | Caller-owned accepted deliberate seed `bio_seed_route`, `bio_seed_result`, `global.num_days` | Existing family flags and distinct type count, recurring covert history/count, persistent first day, qualifying success history | Existing API retained. The family guard encloses only the family flag and type increment. The existing count/first-day writes run in the route guard on each invocation. |
| `bio_lifecycle_dispatch_seed` | Exact selected state | Existing normalized seed validity and use-history proof/source | Invokes the existing deliberate-use recorder only behind both source gates | No call-site changes. The outer validity gate and inner supplied-history plus deliberate/doomsday-source gate remain untouched. |
| `bio_lifecycle_record_internal_deliberate_use` | State, then `event_target:bio_seed_actor` country | Accepted seed and real actor target | Calls the biological achievement recorder in the actor block | No call-site changes. The test asserts exactly one source call in that actor block, without asserting native invocation cardinality. |
| `cbrn_achievement_record_chemical_action` | Actor country | Existing accepted chemical action fields | Existing chemical histories and its own covert result condition | Removed only the misplaced biological route/result condition. No other source node in this recorder changes. |

The helper documentation consists of the corrected country-scope header and local comment in the biological recorder, plus this complete contract.
No new helper or neutral dynamic-registry entry is warranted for this existing local recorder.
No API, default, return temporary, or caller-storage contract changed.

Constants and tuning retain existing `cbrn_achievement_value.zero/one`, `bio_lifecycle_route` and `bio_lifecycle_result` entries.
The current Clean Hands trigger continues to require the existing count of three and 730-day duration.
No constants were added or changed.
No event target, flag cleanup, or variable cleanup was added.
These are persistent campaign achievement histories, so clearing them would change the retained contract.
Existing actor/victim targets and lifecycle cleanup remain parent-owned.

## Files and immutable evidence

- Gameplay: `common/scripted_effects/cbrn_achievement_effects.txt`, only the two assigned recorder definitions and biological recorder comments.
- Task source tests: `docs/testing/2026-10-08_bio_covert_counter/source_tests.js`.
- Test result, exact source snapshots, baseline provenance, and MCP receipts: `docs/testing/2026-10-08_bio_covert_counter/`.
- This handoff: `docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-10-08_bio_covert_counter.md`.

The initial copy command returned a running process and dependent editing proceeded before that process finished.
That first copy captured after-source and is rejected as baseline evidence.
Its bytes are retained only as `rejected_capture/after_source_mislabeled_before.bin`, with SHA-256 `fa2d4aa77447f5f68d617dc307d83d7c3e178be1fadef9f03f1584f874f1790f`.
The semantic baseline was recovered from the exact clean HEAD blob and verified against the explicit pre-task commit `4704913e8cf573cb3f03227fe75eeee9f29a81e5` supplied by the parent.
Both refs name achievement blob `f950b53fb81a16b86869d207e8c51be8378a8606`.
The recovered raw blob SHA-256 is `e393a7970e4edf671ebdf4fe316307e954f3bb23ec7e3ee9143827e9c79d53c7`.
The original checkout newline bytes are unproved, and this handoff makes no claim that the recovered baseline is an original checkout-byte capture.
`baseline_provenance.json` retains the exact refs and correction.

The task-local `.gitattributes` sets `** -text -filter` for the complete evidence directory.
`git check-attr` confirmed both attributes unset on the archived baseline.
The parent must verify committed raw blob hashes after staging because this subagent has no index ownership.
`source_results.json` hashes every exact after-source dependency and the unchanged imported parser/VM.
The snapshots represent this task's source-predicate fixture with current dependencies, not a historical whole-workspace baseline.

## Meaningful source scenarios

Command: `node docs/testing/2026-10-08_bio_covert_counter/source_tests.js --capture` creates exact current source snapshots and runs the checks.
Command: `node docs/testing/2026-10-08_bio_covert_counter/source_tests.js` replays those archived inputs.
Both commands passed after the final patch.
The shared parser and BaseVM in `docs/plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js` were imported unchanged.
Task-local adapters provide only missing regular counter/country-flag commands and declared typed scope context.
Anonymous complex constant schemas outside the test's used categories are explicitly excluded from parsing.
The exact necessary categories are extracted without changing the shared parser or source.

The dispatch projection uses the actual outer `bio_lifecycle_seed_record_is_valid` predicate, actual inner history/source predicates, and actual achievement call found inside the real actor block.
It evaluates the actual lifecycle seed-validation trigger definitions under the fixture's declared actor, victim, controller, population, and seed inputs.
It intentionally omits unrelated profile calculations, delivery, policy, payment, state storage, and unified-record effects.
Accepted projection calls are source receipts, not observed native callbacks.
Direct recorder bypass controls are explicitly separated from accepted/rejected source-gate tests.

| Scenario | Passing after-source evidence | Baseline regression evidence |
| --- | --- | --- |
| Three separate source-accepted partial/partial/full receipts for each covert route | Counts 1, 2, 3, distinct type count stays 1, first day stays 100, success history appears only on the third full receipt | Counts 1, 1, 1 and success history remains absent for both routes |
| Failed, rejected, missing actor, mismatched controller, missing debit proof, zero consumed payload, invalid agent, zero intensity, or ineligible target | All nine fail actual source validity and cannot enter the projected recorder call | No balancing or validity predicates were patched |
| Valid accident, valid spread, or valid deliberate seed without history proof | All three can pass seed validity but cannot enter deliberate-use history through the actual source gate | This distinguishes seed acceptance from deliberate achievement receipt |
| Accepted catastrophic covert result | Count increments, success history remains false for both routes, preserving the original success-only biological condition | No conversion of the catastrophic band to full success |
| Accepted noncovert strategic full result | No covert count or covert-success flag | Other existing strategic history remains outside this repair |
| Clean Hands eligibility after duration, then each exclusion | Existing full trigger passes after the three receipts and elapsed duration. Disclosure, coverup, strategic civilian attack, and doomsday history each make it fail, for both covert routes | Eight exclusion checks preserve the original predicate |
| Chemical result projection with stale biological success inputs | Failed covert and noncovert chemical results cannot gain strategic history. Chemical own success/catastrophic conditions still set it | The frozen misplaced block incorrectly sets it for stale biological inputs |
| Direct recorder calls with failed/rejected fixtures | Both intentionally bypass the caller guard and increment, exposing the contract boundary | These controls are never treated as accepted native receipts or source-gate rejection |

The suite also compares every unrelated achievement definition and the complete chemical recorder against baseline, allowing only removal of the biological block.
The suite checks executed dependency definitions and call placement rather than requiring an unrelated capture helper to remain defined.
This tolerates the parent's exclusive capture-helper removal without hiding a missing executed dependency.

## References and MCP limits

`mcp_evidence.json` retains the full reference-context/search/read receipts with paths, spans, revisions, and exact tool results.
The context call omitted Event modding and Triggers from its compact bundle.
Triggers were explicitly located and read separately.
Event-modification coverage is not claimed for this recorder-only patch.
Relevant reads include:

- Installed `documentation/effects_documentation.md:2343-2349`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, for `add_to_variable`, and `7888-7895` for `set_variable`.
- Installed `documentation/triggers_documentation.md:3624-3639`, `5006-5014`, and `2110-2135`, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, for country flags, variable existence, and comparisons.
- Installed `documentation/dynamic_variables_documentation.md:996-998`, revision `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`, for `num_days`.
- Installed Script Constants, `documentation/script_concept_documentation.md:216-222`, revision `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`, and `common/script_constants/documentation.md:2-34`, revision `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c`.
- Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:567-568,1470`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, for existence, additive creation, and elapsed-day input.
- Offline `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md:643`, revision `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06`, for country flag checks.
- Offline `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:4683-4714`, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`, for scripted-effect calls. Its pertinent `if` section at `4454-4477` was read directly after the search failed to locate that section precisely.
- Vanilla precedent `common/on_actions/13_goe_on_actions.txt:1759-1780`, revision `d76e1be4bae2e39ce17502b24ec4ece25e59fab3f3181c0eb45da624f9277c1f`, contains an additive event counter in country scope alongside a separately guarded cumulative value. MCP source lookup identified the exact nested counter at line 1779, and the surrounding vanilla source was read directly.

MCP source lookup found the original biological recorder and the dispatch's actual validity/history guards at indexed revision `74abd71221597ab90fa7a969cfc82ea59e17ca293f50e8b5d12414e426e885de`.
Its recorder references were incomplete, reporting zero returned references and 20,205 unresolved references.
The real call placement was therefore also traced in source and retained in the fixture.

The narrow bridge `.2` trace returned `EVENT_INSPECTED_PARTIAL`, focused analysis, zero helper projections, and deferred lifecycle passes.
Trace artifact URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fa0687fc80e4443ad0255b3f6acc510d9082fb56d0cbbf7dd20c7bfb5071fc0e/808989a6cac807805be15f0deed398e7acf636dc6c9359935f7aec5718f8c649/event-trace-3417e7cf9ba7.json`.
The matching narrow scope render returned `EVENT_RENDERED_PARTIAL` with `selectedNodes = 0`, `helpers = 0`, and 46,291 omitted nodes.
It does not establish the intended bridge or helper lifecycle coverage.
Its manifest URI is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0b102d44be57f02e1380d508eba061d9a379198e6845336eef4941ccd0bb8cec/156641d0b82ef67290b3e535c4c00ee228f62b66198aac9466eca6cbfaa963ac/event-scope-01552eecfb0c-manifest.json`.
All four render artifact identities are retained in `mcp_evidence.json`.
Artifact payload retrieval/provenance remains unverified because no artifact-resource retrieval route is exposed in the connected HOI4 tool list.
No render or trace payload is presented as proof of the recorder patch.

The requested before/current event comparison returned `EVENT_REVISION_NOT_CACHED` with the exact blocker `Requested event graph revision is not cached or retained as a graph artifact`.
Source comparisons above are source evidence and do not replace that missing engine-tool comparison.
No `helper_expansion`, job, or native MCP-task route was used because client negotiation was not confirmed.

Explicit country-scope `hoi4.script_validate` on the biological recorder returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, `parametersChecked = false`, with 19 unchecked argument blocks.
Its coverage is syntax, command kind, and declared scope only.
The cited native syntax was read separately, and the unchanged parameter forms were exercised in the source fixture.
This remains partial MCP coverage rather than a full validation pass.

## Simplifications, omissions, and blockers

There are no gameplay simplifications in this repair.
Native callback cardinality remains unproved, so these tests establish count-per-valid-invocation continuity only.
No synthetic replay identity or deduplication token was introduced.
The failed MCP event comparison, focused helper-boundary coverage, zero-node render selection, artifact provenance gap, and unchecked native argument blocks remain explicit validation limits.
No live-game launch, log search, or runtime-validation request was performed.
No probability surface was changed, so no probability rebalance or compare is claimed.
The parent retains final lifecycle/interface retirement, source review, documentation integration, and scoped commit ownership.

Skills used: `chaos-redux-events` and `chaos-redux-subagents`.
No skills were created or changed.
