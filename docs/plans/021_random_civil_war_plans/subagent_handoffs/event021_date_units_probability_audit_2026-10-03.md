# Event 021 MTTH date-unit baseline and after-audit

Audit date: 2026-10-04. The filename retains the parent-provided 2026-10-03 date. This is a read-only probability and date-wiring handoff; this audit changed no gameplay source and made no commit.

## Bounded finding

The saved baseline scheduler wrote each clamped Evolution I–III delay, still measured in days, directly into an absolute `global.date` due-date variable. The offline wiki documents `global.date` in game-hour units, with one hour equal to `0.00001`; this establishes a source-level unit mismatch, but no exact elapsed-time result was returned by the probability adapter.

The current shared working copy of the parent source copies the unchanged clamped day value into caller-initialized `event021_date_offset`, calls `event021_days_to_date_offset`, then adds the converted offset to the due date. Its three MTTH definitions are byte-identical to the frozen baseline. The published commit’s MTTH blob differs from this current working copy, so the working-copy comparison below is not a commit-tree comparison. The post-patch probability inspect did not resolve the helper, and the bounded parent-effects compare returned `PROBABILITY_SURFACE_EMPTY`, so no full MCP clock trace or engine-confirmed 90-day result is claimed.

The MTTH adapter returned `PROBABILITY_SURFACE_EMPTY` for the exact three Evolution IDs in the saved source and in the valid compare of that snapshot against the current shared-worktree MTTH path. This compare did not read the pinned commit’s different MTTH blob. Evaluation, comparison, and sweep values, scenario hashes, comparison IDs, and probability render artifacts therefore do not exist. The appropriate timing result classification is unresolved.

A separate source-level disabled-evolution issue remains: the daily scheduler can schedule an unlocked, unrecorded evolution before `is_current_evolution_enabled` is checked by the hidden event effect. When disabled, that effect skips activation and recording; the due date has already been cleared, so the next scheduler pulse can sample the same stage again. Evolution II also requires Evolution I to be recorded, and Evolution III requires Evolution II to be recorded. This creates repeat-scheduling and later-stage starvation risk while a prerequisite evolution remains disabled. Runtime cadence and player-visible effects are unresolved.

## Audited surfaces and exact source files

- `common\mtth\021_random_civil_war_mtth.txt`: `random_civil_war_evolution_i_days`, `random_civil_war_evolution_ii_days`, and `random_civil_war_evolution_iii_days`.
- `common\scripted_effects\021_random_civil_war_parent_effects.txt`: `event021_parent_select_evolution_mtth_actor`, `event021_parent_schedule_evolution_due_date`, `event021_parent_process_evolution_schedule`, and the due-date variables `global.random_civil_war_evolution_i_due_date`, `_ii_due_date`, and `_iii_due_date`.
- `common\scripted_effects\021_random_civil_war_date_effects.txt`: `event021_days_to_date_offset`, with caller-owned in-place temporary `event021_date_offset`.
- `common\script_constants\021_random_civil_war_date_constants.txt`: `event021_calendar.hours_per_day = 24`, `hours_per_date_unit = 100000`, and `hour_step = 1`.
- `common\script_constants\021_random_civil_war_constants.txt`: `random_civil_war_evolution_mtth` base/factor constants and the shared 60–180 day clamp.
- `common\scripted_effects\021_random_civil_war_date_effects.md` and `common\mtth\021_random_civil_war_mtth.md`: helper and MTTH contracts.
- Current helper call-site counts are 3 in `common\scripted_effects\021_random_civil_war_decision_effects.txt`, 12 in `common\scripted_effects\021_random_civil_war_evidence_effects.txt`, 13 in `common\scripted_effects\021_random_civil_war_effects.txt`, 12 in `common\scripted_effects\021_random_civil_war_parent_effects.txt`, and 1 in `common\scripted_effects\021_random_civil_war_treaty_effects.txt`, for 41 executable calls total. The parent file’s 12 calls include the three Evolution scheduler writes.
- `common\on_actions\chaosx_on_actions_chaos_meter.txt` calls `event021_parent_global_scheduler_pulse` from `on_daily`; `events\021_random_civil_war.txt` defines hidden triggered-only `chaosx.nr21.11`, `.12`, and `.13` dispatch events.
- `events\021_random_civil_war.txt` also contains event-option `ai_chance` candidates. The probability inspector found 11 such candidates, but event-option selection is outside this MTTH date-unit audit and was not evaluated.

## Baseline values and modifier traces

The three entries are separate stage-specific delay expressions selected by the scheduler’s `event021_evolution_schedule_stage` branch. They are not a normalized candidate pool or a score race, and the scheduler does not rank the three entries against each other.

| Entry | Base days | Source modifiers | Shared clamp |
| --- | ---: | --- | --- |
| `random_civil_war_evolution_i_days` | 90 | Authority failing `0.75`; controlled states above 8 `0.85`; extra active actor `0.75`; near defeat above surrender progress `0.70` `1.50`; settlement phase `1.40`; no extra active actor `1.35`. | 60–180 days |
| `random_civil_war_evolution_ii_days` | 135 | Border exposure `0.75`; sponsor commitment `0.75`; active Event 006 actor `0.80`; extra actor/multifront `0.85`; settlement phase `1.40`; any neighbor stability above `0.65` `1.25`; no exposure route `1.25`. | 60–180 days |
| `random_civil_war_evolution_iii_days` | 120 | Severe or critical opening severity `0.80`. | 60–180 days |

Those are exact source constants, not evaluated scenario outputs. The pinned commit’s constants blob contains the same listed numeric bases, factors, thresholds, and clamp values. Its MTTH condition expressions differ from the current working copy, so the table’s predicate descriptions refer to the current worktree and frozen snapshot, not the committed MTTH blob. No factor products, effective-day values, cumulative event probabilities, or survival curves are claimed.

The actor-selection helper walks `global.random_civil_war_active_theaters` and takes the first active front side that passes `event021_parent_active_front_side`; when none is saved, the scheduler host evaluates the MTTH entry. The MTTH notes state that the actor predicates require valid same-crisis actor/front receipts and fail closed when those receipts are absent. The actor order and the MTTH day input were unchanged by the date conversion.

## Frozen baseline and current source verification

The immutable baseline `docs\plans\021_random_civil_war_plans\probability_snapshots\event021_date_units_before_2026-10-03\021_random_civil_war_mtth.txt` has SHA-256 `7982F0768B8ED04AE7154BCFF8CBDAC33589F8F7B031CFE12353F625891881C1`. The current shared working copy of `common\mtth\021_random_civil_war_mtth.txt` has the same SHA-256, so its byte-level source delta from the frozen baseline is exactly zero. The pinned commit stores a different MTTH blob, so this zero-delta statement applies only to the current worktree comparison.

The immutable baseline parent-effects source `docs\plans\021_random_civil_war_plans\probability_snapshots\event021_date_units_before_2026-10-03\021_random_civil_war_parent_effects.txt` has SHA-256 `0DBD60BF8259F6848413F84DB79F988D6D29CABB26FA09C283066A7A03E1DF61`. The current shared-worktree parent-effects source has SHA-256 `01B4676C83150DE2D452566DDDC28335959C8E30E815CAEFB81A5E183197794E`.

The current helper source has SHA-256 `863E1D0B51DE7DE141067F8982A6CB156530C42025002DD67495FA8C1FB019F0`, and the current calendar constants source has SHA-256 `195DC390CE1CBD5C081743AEE6820E6A2E8E56906E8D72CAC080B94EDB00A80B`.

The current working-copy scheduler’s three branches preserve the `mtth:` assignment, actor selection, and `clamp_temp_variable` against `random_civil_war_timing.evolution_minimum_days` and `.evolution_maximum_days`; each then initializes `event021_date_offset` from `event021_evolution_delay_days`, converts that separate temporary, and adds the result to its absolute due-date variable. The committed parent-effects blob also contains the three conversion calls, confirmed with read-only `git show`. A scoped search found no remaining direct addition of an Event 021 `*_days` constant to a date-like target in the inspected scripted-effect files.

The helper multiplies the caller’s day duration by 24, stores the unrounded hours, rounds the offset, adds one hour only when the rounded result is below the unrounded value, then divides by 100,000. Under the documented rounding semantics, this is a source-level ceil-to-hour conversion, with whole-day inputs preserved and fractional-hour inputs rounded forward by less than one hour. This is a bounded source reading, not an MCP evaluation or live-game measurement.

Git confirms primary implementation commit `015a7820a22727a72cc567ea54abd2abed35f303`, tree `118e66db36f76dcaa818cc24955ba37d85ed2945`, subject `Fix all Event 21 day durations added to encoded dates`. The parent reports this tree was based on `0d9f7a4cd9436bd0c35862ad2d6849e7a91ec7a`, contains 41 offset conversions plus schema/helper/docs/tests/evidence archives, and passed 6 calendar and 12 metadata tests on that exact tree; the parent also reports raw-byte baseline archive verification and an architect inverse-AST confirmation of pure 41 conversions with 18 reproduced earlier tests. The commit identity and tree were verified here, while the parent’s test and archive claims were not independently rerun by this read-only audit.

After that commit, the shared working copy reports `M` for `common\mtth\021_random_civil_war_mtth.txt`, `common\scripted_effects\021_random_civil_war_parent_effects.txt`, and `common\script_constants\021_random_civil_war_constants.txt`. The current MTTH and parent-effects Git blob IDs are `9f725827a5b972a00c95ee90fd20dedcaa385bc6` and `f867595711cf7a8200985e371d2fbb03d77517ac`; the pinned commit’s corresponding blob IDs are `123c4f6f4964715be173c1dd580aae53ff1f0d62` and `c9e36e4a7b84988b0a960c1f2e0965fd756cd231`. The current MTTH worktree matches the frozen snapshot, while the commit blob uses direct flag checks for extra-actor and Event 006 predicates; the current worktree uses `event021_evolution_has_extra_active_actor` and `event021_evolution_has_active_event6_actor`. The numeric MTTH constants listed above match in the pinned commit and the worktree. This is a material shared-worktree source divergence, not attributed to the date-only implementation without further review.

## Named scenario set and completeness

The same scenario-set ID was submitted to the baseline evaluation and the MTTH source comparison: `event021_date_units_before_after_20261003`, schema version `1.0`. The exact named cases and declared inputs were:

```json
{
  "schemaVersion": "1.0",
  "id": "event021_date_units_before_after_20261003",
  "scenarios": [
    {"id":"EVO1-01","state":{"random_civil_war_authority_is_failing":true,"num_of_controlled_states":60,"event021_evolution_has_extra_active_actor":true,"surrender_progress":0.2,"random_civil_war_settlement_phase":false}},
    {"id":"EVO1-02","state":{"random_civil_war_authority_is_failing":false,"num_of_controlled_states":8,"event021_evolution_has_extra_active_actor":false,"surrender_progress":0.95,"random_civil_war_settlement_phase":false}},
    {"id":"EVO2-01","state":{"random_civil_war_land_border_exposure_ready":true,"random_civil_war_sponsor_commitment_active":true,"event021_evolution_has_active_event6_actor":true,"event021_evolution_has_extra_active_actor":true,"random_civil_war_settlement_phase":false,"neighbor_stability":0.8}},
    {"id":"EVO2-02","state":{"random_civil_war_land_border_exposure_ready":false,"random_civil_war_sponsor_commitment_active":false,"event021_evolution_has_active_event6_actor":false,"event021_evolution_has_extra_active_actor":false,"random_civil_war_settlement_phase":true,"neighbor_stability":0.8}},
    {"id":"EVO3-01","state":{"opening_severity":3,"severe_event021_war_active":true}},
    {"id":"EVO3-02","state":{"evolution_iii_prefire_active":true,"first_event021_firing":true}},
    {"id":"EV21-DISABLED-01","state":{"evolution_enabled":false}},
    {"id":"CLOCK-00000-90D","date":"-5000.1.1","state":{"global_date":0,"event021_evolution_delay_days":90,"expected_calendar_delay_days":90}},
    {"id":"CLOCK-INTENDED-90D","date":"1936.1.1","state":{"event021_evolution_delay_days":90,"expected_calendar_delay_days":90}}
  ]
}
```

The three MTTH entries form a complete list of the Event 021 evolution-delay definitions, but they are not a complete normalized selection pool. Scenario input completeness is incomplete: the adapter did not materialize the active theater roster, the first-valid actor selection, the full same-crisis front receipts, the derived authority predicate, or the live neighbor/sponsor/Event 006 state. The disabled case also depends on the shared evolution-enable state outside the MTTH definitions. The current-worktree scenario fields for the helper predicates do not match the pinned commit’s direct-flag expressions. The clock cases were declarations only; the evaluator returned no analysis, so `date = "-5000.1.1"` and `expected_calendar_delay_days = 90` are not evidence that the adapter represented `global.date = 0` or a 90-day result.

No scenario hash was produced. The successful inspect artifacts contain source hashes and revisions only; those do not substitute for a scenario hash.

## MCP evidence and verdicts

| Route and source | Result | Evidence identity |
| --- | --- | --- |
| `hoi4.probability_inspect`, `common\mtth\021_random_civil_war_mtth.txt`, adapter `event_mean_time_to_happen`, all three IDs | `PROBABILITY_SOURCE_DISCOVERED`, requested adapter had zero candidates and no available adapter; `discoveryReason = no_weighted_surfaces`. | Artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/15144409f08ea18e50412227f2a6e2ff01591bfebe4df9cc1297587f043d9fef/c0334f0a3cacae093eae4c76bc0dc5531f808a64049d0263b42af0dc86406f6d/probability-inspect-090cf4c0e32c.json`; source hash `090cf4c0e32cde8b8b04c1f4e7b92e74179b4e17ded2ad7f10450cc05fd6e102`; revision `2172b3cd7b86aeec55d4a22ea15d08ad03c15edd4607f1da50f3474602149c52`. |
| `hoi4.probability_inspect`, current `common\mtth\021_random_civil_war_mtth.txt`, same adapter and IDs | Same source hash and no weighted surfaces; no current MTTH candidate was exposed. | Artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8c464267d85e52ba1d986403cf6b14cb499b8b8265ef03346a42222537b82b58/069a1efc6796ba29844a1c89f80774803198f1925b927d11a536ef734a6be44c/probability-inspect-090cf4c0e32c.json`; source hash `090cf4c0e32cde8b8b04c1f4e7b92e74179b4e17ded2ad7f10450cc05fd6e102`; revision `c34f600541f74b771d0b7c00110cc7f919f07cb2d1c4acb531a6169493c02d9e`. |
| `hoi4.probability_evaluate`, frozen MTTH source and the scenario set above | `PROBABILITY_SURFACE_EMPTY`, “No weighted blocks matched this request”; no analysis ID or artifact. | Exact source path was the saved snapshot path listed above. |
| `hoi4.probability_compare`, frozen MTTH snapshot versus current shared-worktree `common\mtth\021_random_civil_war_mtth.txt`, same candidate IDs and scenario-set ID | `PROBABILITY_SURFACE_EMPTY`; no comparison ID, scenario hash, or numeric delta. | Both `before.path` and `after.path` were nonempty workspace source paths. The `after.path` was the working copy, not the pinned commit blob; the compare did not prove an engine-model zero delta. |
| `hoi4.probability_inspect`, baseline `common\scripted_effects\021_random_civil_war_parent_effects.txt`, requested MTTH adapter | Requested adapter empty; 8 `random_list` entries were discovered instead. | Artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/913609454d38445b475693374dc7afeba788295f28692972b8ca84dee9571804/3323495989111309e64d69dfc35f36e60a7d49b3929d8ba6706b7bae4693b9c8/probability-inspect-0eebafc0e94a.json`; source hash `0eebafc0e94a0f8b88b155f58889dd594101296ff59a306ab3586242896e4495`; revision `2172b3cd7b86aeec55d4a22ea15d08ad03c15edd4607f1da50f3474602149c52`. |
| `hoi4.probability_inspect`, current parent-effects working copy after the date patch, requested MTTH adapter | `PROBABILITY_SOURCE_DISCOVERED`, requested adapter empty; the available adapter was `random_list` with 8 candidates and no resolved date helper or required MTTH inputs. | Artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4dd91682d592e3bf912ccefd33af4f82820724b18f282a7297567d76d1b4d23c/2f0908337da21865f7151fae464352d17476b8daad54eca6612f29d3c78fa582/probability-inspect-cb249fcbbc39.json`; source hash `cb249fcbbc39d58c38f7416c3c39cee3f2f921758ebe9f8966e33ed52ced810`; revision `2bcfcc6558b940a32eabac6ed8bc71902deaa32c7b9b2099797767bd1d8bac95`. |
| `hoi4.probability_compare`, frozen parent-effects snapshot versus current shared-worktree `common\scripted_effects\021_random_civil_war_parent_effects.txt`, same candidate IDs and scenario-set ID | `PROBABILITY_SURFACE_EMPTY`; blocker details were truncated by the tool, with no comparison ID, scenario hash, analysis, or clock result. | Both source paths were valid and nonempty. This is the separate parent clock-wiring compare; it did not resolve the date helper or inspect the pinned commit blob. |
| `hoi4.probability_inspect`, `events\021_random_civil_war.txt`, MTTH adapter | The file exposed 11 `event_option_ai_chance` candidates and suggested that adapter; it exposed no event MTTH candidate. Those options are out of scope. | Artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d42b11525d2884c23de5c7cd2d6fc770cedf0c42c3d5add602b31cf1bcb8be45/b73f05e9e2905cd33dd6366d57106a84d647e4ecf0f551f6a5a002d03d8701cf/probability-inspect-d8275e2107ff.json`; source hash `d8275e2107ffde3195eb3d451fc839c7fe0b99ce2018d9aeb2321ccd21572b61`; revision `28decc80444759c8a3dec8d598f3def5d3d09685c584449daa12651273e831b7`. |
| `hoi4.probability_inspect`, `common\scripted_effects\021_random_civil_war_active_evolution_effects.txt`, MTTH adapter | `no_weighted_surfaces`; no candidates or helper expansion were returned. | Artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3b37b2cd2bb9a2659967ba755513dcbf609984b222979e427f24ad904b2d3148/57f91472d8d8b6be65b7c517504b42563d5115a25902756feeeb5b34e45e3fb0/probability-inspect-86fbf03fc291.json`; source hash `86fbf03fc291240a25f80e1f9a46baf14fc5f9f2b6fb515d5dd626e15e7380ad`; revision `f3b80002159eddc84859f68be3b91169d953bdebb67a00d89a5a3a5925a97640`. |

An after-patch full evaluation and sweep call, a narrower one-entry `EVO1-01` evaluation retry, and a pre-commit parent-effects clock compare did not return tool results before their execution cells were terminated after extended waits. The bounded post-commit parent-effects comparison is recorded separately in the table and returned `PROBABILITY_SURFACE_EMPTY`. None of these calls produced a valid analysis or comparison artifact, scenario hash, or numeric clock result. An adapter-only inspect was first rejected because the installed route requires a source object; subsequent inspections used mod-relative source objects. The scenario route rejected numeric `date` once; the successful empty-surface attempt used string dates.

`hoi4.probability_render` was not called because no evaluate or compare analysis ID exists for its required input. `hoi4.probability_simulate` was not called because no uncertain-input distribution or seed-based question was declared. `hoi4.probability_sequence` was not called because this is not a declared custom weighted pool with cadence and state transitions. No rank-reversal sweep result exists; the three stage entries are not competing candidates.

## Structural MCP evidence

`hoi4.event_inspect` traced `chaosx.nr21.1` with `selector = { kind = event eventId = "chaosx.nr21.1" }` and returned `EVENT_INSPECTED_PARTIAL`, revision `828ca59a9a1fa1a44d0bf5a12bce75e5cb65e717d2d055388d5ac1994d71fe92`, graph hash `db36826f88e04b62673db3f3908a3ef1dbcc2e27abf44c1047338abd9c5ad351`, helper count 0, unresolved-node count 8,977, and an inline inventory truncation diagnostic (64 of 388 paths). The trace artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7475d6c6bc24d56d290a818b28b120d450f0cae3a567c50c1173b3f90fd010e5/8ef303274dcb0df16d7339a7e7a05cee71918efc3d2498564097b0453823b965/event-trace-828ca59a9a1f.json`.

`hoi4.event_render` returned partial timing and unresolved views at the same revision with helper count 0; these focused event views do not establish the helper clock trace. Timing SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/44dd6a61bfef5e90b9634508288d56bf10ff39a3478931619a96886516b12a59/a434d9ae2909ddad6d3c3642ee2707d59aecb19206f2bd38be4960df3fc0e98e/event-timing-828ca59a9a1f.svg`. Timing PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a7829222970cd8a2bdc77d1fe91efa8b261171e0eaf4377fa036a86671e2af1d/5a8617e28d059c79398ff8c00f7777dee643693cd0a58db993a49b729eb58718/event-timing-828ca59a9a1f.png`. Unresolved SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/845c2b0e65821b0e22172f7142805027b892df5153b818b4c033fa34b160e59b/26a796b0803ff466bda14ccd11ccd6097a6659f230a4a8fe0f6edc1862bdfe80/event-unresolved-828ca59a9a1f.svg`. Unresolved PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c5fab7874c948130ab313eb8267ab543c8bba8d2e38ec6fa0089d55eaed4dfcf/12cf869f6b88cff0b72afa37d002c2209b961e7e53f6db6ce329803208d8c24c/event-unresolved-828ca59a9a1f.png`.

`hoi4.source_lookup` for `event021_days_to_date_offset` was retried with the corrected `maxReferences = 5` schema after an initial `maxReferences = 60` validation error. The corrected request did not return a tool result before its execution cell was terminated; the call graph is therefore source-reviewed locally but not MCP-indexed in this handoff.

## Disabled, repetition, and starvation findings

`event021_parent_process_evolution_schedule` tests `*_unlocked` and `NOT = { *_recorded }`, then schedules or fires the hidden event based on the due date. It does not test `is_current_evolution_enabled` before sampling. The daily global-host pulse calls this scheduler.

`event021_parent_apply_evolution_i`, `_ii`, and `_iii` test `is_current_evolution_enabled` only after their hidden event fires. When disabled, they do not apply the evolution or set its `*_recorded` flag. Because the due date was cleared when the hidden event fired, the still-unlocked, unrecorded stage remains eligible for another MTTH due-date sample on a later daily scheduler pulse.

Evolution II scheduling additionally requires `random_civil_war_evolution_i_recorded`; Evolution III requires `random_civil_war_evolution_ii_recorded`. Thus a disabled earlier evolution can prevent later unlocked evolutions from reaching their scheduling branch. This is an exact source-path finding; the actual event dispatch, repeated firing cadence, and campaign consequence were not live-game tested or resolved by MCP.

## Conclusion classes and balance findings

- Exact source finding: the baseline added day-valued MTTH results directly to encoded absolute date variables.
- Exact source finding: the current helper wiring preserves MTTH day inputs and clamps, and the frozen and current MTTH files have identical SHA-256.
- Bounded source finding: the helper rounds a fractional-hour offset forward to the next hour; the claimed less-than-one-hour bound follows the inspected source and documented rounding behavior, not an MCP timing trace.
- Unresolved: baseline versus after effective MTTH timing, exact calendar deadlines at `global.date = 0`, the intended 90-day clock-boundary case, and parent before/after clock application.
- Not applicable: selection probability, normalized ranking, dominance, and rank reversal among the three MTTH entries, because the scheduler chooses one stage by deterministic branch and does not race these entries.
- Exact source risk: disabled, unrecorded stages may be rescheduled, and a disabled predecessor may hold later stages behind its recorded flag.
- No source evidence of a snowball or probability-proportional selection effect was established in this MTTH date-unit scope.

## Recommended follow-up, not applied

1. Keep the date-unit helper and its centralized integer constants for every Event 021 absolute-date addition, while retaining native `days =`, mission/flag durations, MTTH bases/factors/clamps, and actor selection in their existing units and order.
2. Define and implement an explicit disabled-evolution scheduler policy in `event021_parent_process_evolution_schedule` and `event021_parent_apply_evolution_i`, `_ii`, and `_iii`, so disabled stages do not repeatedly resample and do not unintentionally block later enabled stages.
3. When the connected probability adapter supports these `mtth:` expressions or their documented helper path, rerun `probability_inspect`, same-scenario `probability_evaluate`, `probability_sweep`, and `probability_compare` against the frozen MTTH source, current MTTH source, and separate parent-effects before/after sources. Preserve the exact scenario set above and request timing/comparison render artifacts only after a valid analysis ID exists.

## Skipped analyses, blockers, and uncertainty

The MTTH adapter’s exact blocker is that all three candidate IDs resolve to `no_weighted_surfaces` / `PROBABILITY_SURFACE_EMPTY`; it cannot supply engine-evaluated modifier traces or timing. No scenario hash, comparison ID, probability result, or probability-render artifact exists. The parent-effects inspector returned only the unrelated `random_list` adapter candidates and did not resolve `event021_days_to_date_offset`.

The offline wiki date row was available, but targeted installed-game documentation searches did not locate a `global.date` unit section or a dedicated MTTH-variable documentation section. The installed vanilla `common\mtth\mtth_variables.txt` contains the `set_variable = { a = mtth:entry_name }` usage example; installed `effects_documentation.md` supplies arithmetic-effect definitions at lines 2327–2340, 3587–3605, 5012–5025, and 6476–6484. The installed script-constant schema and Script Constants sections were read directly through the reference route.

No game was launched, no logs were requested, no tests were run by this auditor, no gameplay or AI source was edited, and no commit was made. Only this report is written by this audit.

## Reference sections used

- Offline wiki `Data structures - Hearts of Iron 4 Wiki.md`, “Game variables,” lines 1458–1527, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`; the `date` row documents one game hour as `0.00001` and the encoded origin.
- Offline wiki `AI modding - Hearts of Iron 4 Wiki.md`, “MTTH blocks,” lines 26–36, revision `917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818`; it distinguishes MTTH value manipulation from AI score races and event-option probability-proportional sampling.
- Offline wiki `Event modding - Hearts of Iron 4 Wiki.md`, “Triggering,” lines 117–150, revision `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d`; native event `mean_time_to_happen` uses a daily hazard and is distinct from these stored scalar due-date delays.
- Offline wiki `Data structures - Hearts of Iron 4 Wiki.md`, “Operators,” lines 555–634, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, plus “AI modding,” “Example,” lines 38–73, revision `917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818`.
- Installed vanilla `common\script_constants\documentation.md`, lines 1–34, revision `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c`, and installed `documentation\script_concept_documentation.md`, “Script Constants,” lines 216–222, revision `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`.
- Installed vanilla `documentation\effects_documentation.md`, arithmetic effects listed above, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.

Skills applied: `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-mtth`, and the event-planning scenario guidance for the supplied Event 021 probability matrix.
