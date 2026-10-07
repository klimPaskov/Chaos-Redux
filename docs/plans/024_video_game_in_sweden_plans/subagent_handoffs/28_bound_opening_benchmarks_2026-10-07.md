# Event 24 bound opening benchmark retry

Audit date: 2026-10-07.

Status: partial MCP evaluation and sensitivity sweep completed for the bounded opening surface. The fresh inspect and scenario analysis returned, with two unresolved `compare_autonomy_state` items and an inconsistency between summary ranking fields and candidate row bounds. This does not complete Event 24 stage, balance, or probability acceptance.

## Scope and unchanged sources

The entry/dispatch event is `chaosx.nr24.1`; it schedules the visible opening at `chaosx.nr24.2`. The complete source-local option pool is `chaosx.nr24.2.a`, `chaosx.nr24.2.b`, and `chaosx.nr24.2.c` in `events/024_hearts_of_iron.txt`. The parent reports no gameplay or weighted source changes. No source snapshots were copied during this continuation.

The prior handoff 27 records the last successful inspect: adapter `event_option_ai_chance`, 3 candidates, `poolComplete=true`, 9 required input paths, inspect source revision `2be9734ce2e357333ed5a81b7d2d0e5b3d62cccf9329be32befe3b2650329332`, aggregate source hash `2d2c31c4c1053d4b3006a116a88430f86350d5b247f44b961bbbaca49426224a`, and its artifact URI. That earlier inspect is context only and was not substituted for the fresh request in this continuation.

## Parent-declared benchmark fixture

The files below were read fully, without truncation:

- `docs/plans/024_video_game_in_sweden_plans/probability_evidence/2026-10-07_opening_benchmarks/P24_OPENING_BENCHMARKS.json`, 3,589 characters / bytes.
- `docs/plans/024_video_game_in_sweden_plans/probability_evidence/2026-10-07_opening_benchmarks/README.md`, 2,657 characters / bytes.

Fixture ID: `P24_OPENING_BENCHMARKS_20261007`. These are parent-declared hypothetical inputs within the accepted qualitative conditions, not observations from a Sweden campaign, save, or game run, and not new balance targets.

The fixture binds actor `SWE`; all eight supported native state paths from the prior inspect (`has_war`, `has_government`, `has_stability`, `has_army_experience`, `has_capitulated`, `is_subject`, `variable.global.chaos_meter_value`, `variable.global.threat`); the current-host event target; and explicit crisis flag packets. It intentionally leaves `compare_autonomy_state` unbound because `is_subject = false` and no autonomy ordinal is fabricated. If the adapter cannot prove the low-autonomy helper false from that state, that remains unresolved. The declared host event target is only a conditional-delivery assumption and does not prove the `.2` current-host gate; the option weights do not read that target.

| Accepted ID | Declared benchmark inputs and alternatives | Planned branch expansion if the live scenario schema rejects `uncertainInputs` |
| --- | --- | --- |
| P24-O1 | Peace, democratic or neutral government, stability 0.75, army experience 50, not capitulated, independent, Chaos 100, threat 0.20, active-program flag, host target SWE | 2 cases: democratic (base ID P24-O1) and neutral (`P24-O1-neutrality`) |
| P24-O2 | Peace, democratic, stability 0.75, army experience 10, not capitulated, independent, Chaos 100, threat 0.75, active-program flag, host target SWE | 1 case: P24-O2 |
| P24-O3 | War, fascist, stability 0.65, army experience 10, not capitulated, independent, threat 0.75, active-program flag, host target SWE; Chaos alternatives 250, 799, 800 | 3 cases: Chaos 250 (base ID P24-O3), 799 (`P24-O3-chaos799`), 800 (`P24-O3-chaos800`) |
| P24-O4 | War, four government alternatives, stability 0.15, army experience 10, not capitulated, independent, threat 0.75, active-program, supply-crisis, and recent-core-loss flags, host target SWE; Chaos alternatives 250 and 800 | 8 cases: government democratic/neutrality/fascism/communism × Chaos 250/800; base ID P24-O4 is democratic at Chaos 250, with clear government/Chaos suffixes for the other seven |

The fixture declares 14 logical alternative combinations and 42 candidate-in-branch outcomes with the complete three-option pool. No prevalence weighting or averaging is authorized. The connected route accepted the fixture's `uncertainInputs` and `eventTargets` fields without schema rejection, so the analyzer retained the four named scenarios and represented alternatives with bounded candidate intervals; no 14-scenario expansion was sent.

## Fresh live inspect attempt

The first broad-source inspect attempt used adapter `event_option_ai_chance`, source `{ path: "events/024_hearts_of_iron.txt" }`, all three `.2` options, `refresh: false`, and workspace `mod_chaos_redux_ea3b2d67c2c0`.

The connected tool returned exactly: `tool call error: tool call failed for hoi4_agent_tools/hoi4.probability_inspect. Caused by: timed out awaiting tools/call after 600s`.

That first attempt returned no inspect data and timed out after 600 seconds. It is retained as a historical failed call; its remote completion state was unknown.

The follow-up used the narrower source selector `{ path: "events/024_hearts_of_iron.txt", identifier: "chaosx.nr24.2" }`, the same adapter and all three options, with `refresh: false`. It returned `PROBABILITY_SOURCE_INSPECTED`, status `ok`, `candidateCount = 3`, `poolComplete = true`, `requiredInputs = 9`, and `unresolved = 0`. Required paths were `compare_autonomy_state`, `has_army_experience`, `has_capitulated`, `has_government`, `has_stability`, `has_war`, `is_subject`, `variable.global.chaos_meter_value`, and `variable.global.threat`. Inspect source revision: `2ce215be4a2aef156896b2e85f4e8abe040349a30d6eb9e8f04b888617f55b0c`; aggregate source hash: `2d2c31c4c1053d4b3006a116a88430f86350d5b247f44b961bbbaca49426224a`.

Inspect artifact URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7ce3bb83edafcc951da0ec939a913e8eee4f43b8f51570f22339bf283809ba87/1b0542f1bb70025024825437b24023881ab0a4693fe5db4d1abd7d06cefb126a/probability-inspect-2d2c31c4c105.json`, declared size 23,536 bytes.

## Evaluation and sensitivity status

The exact fixture was then submitted to `hoi4.probability_evaluate` with the three-option pool, source `{ path: "events/024_hearts_of_iron.txt", identifier: "chaosx.nr24.2" }`, `refresh: false`, and metrics `raw_value` and `conditional_probability`. It returned `PROBABILITY_ANALYZED_PARTIAL`, analysis ID `probability-801e0167484e374a043a5e40`, scenario hash `cd04dc91cc63222f017e3a663f363c6ac51b2f17f49382f70d159225108ab900`, source revision `73722338d405198e8afaa0dc4e21157ed74d11cbab0452952679f39f3761da0c`, and the same aggregate source hash `2d2c31c4c1053d4b3006a116a88430f86350d5b247f44b961bbbaca49426224a`. Summary: 4 named scenarios, 12 candidate rows, 12 eligible, 0 excluded, 2 unresolved, 0 unresolved candidates, 8 diagnostics, and 6 visual resources.

The result was followed by a targeted `hoi4.probability_sweep` over `variable.global.chaos_meter_value`, `has_stability`, and `has_army_experience`, with `findRankReversals = true`, `pairwise = false`, and no hand-chosen `steps`. It returned `PROBABILITY_ANALYZED_PARTIAL`, analysis ID `probability-e2f014038b67452f9116eecf`, the same scenario hash, source revision `8cf0c3a1a262b5bed53a6213c1a554ba007dd1a59281e7a89e761f6d824af2b9`, 15 sweep points, 12 candidate rows, 2 unresolved, 8 diagnostics, and 10 visual resources. The direct summary does not enumerate the 15 point values; this handoff does not claim that every requested numeric threshold was sampled.

The evaluation and sweep JSON artifact URIs, declared sizes, and render URIs are recorded below. The sweep JSON was read from the configured local workspace path, parsed, and verified at 234,975 bytes with SHA-256 `a81a159740a174245d2ecb033bf19cf206958027e228d6bf631457cfdadbcd9c`. The file was later absent on a workspace recheck. Its extracted candidate rows are reproduced below. The evaluation JSON URI declares 226,110 bytes and SHA-256 `72fff1e4dbed7e3c014600b53e9bb5622148d24c44a1985a135c76b6b64d5538`; its local file was absent when checked, so the verified sweep JSON is the available row-level evidence.

The live route accepted `uncertainInputs` and `eventTargets` without a schema error. The four named scenario rows therefore retain the declared 14 logical branch alternatives as bounded ranges rather than expanding them into separate scenario IDs. The event target remains a conditional-delivery assumption, not proof of the event's current-host gate. `compare_autonomy_state` remains intentionally unbound; no autonomy ordinal or candidate override was invented.

## Artifact recovery location

The actual configuration file was read at `C:\Users\klimp\AppData\Roaming\hoi4-agent-tools\config.json`. Its `workspaceStorageRoot` is `C:\Users\klimp\AppData\Local\hoi4-agent-tools\workspaces`; no workspace-specific override field was present in that configuration. The current workspace directory `C:\Users\klimp\AppData\Local\hoi4-agent-tools\workspaces\mod_chaos_redux_ea3b2d67c2c0` exists and contains `artifacts` and `cache` directories.

Configuration resolution used `C:\Users\klimp\AppData\Roaming\hoi4-agent-tools\config.json`; `workspaceStorageRoot` resolves to `C:\Users\klimp\AppData\Local\hoi4-agent-tools\workspaces` and no per-workspace override key was present. The active workspace is `C:\Users\klimp\AppData\Local\hoi4-agent-tools\workspaces\mod_chaos_redux_ea3b2d67c2c0`.

The explicit `hoi4.probability_render` request returned `PROBABILITY_ANALYSIS_NOT_CACHED` for `probability-801e0167484e374a043a5e40`, with blocker “Render requires a retained analysis ID from this authorized workspace.” The evaluation and sweep calls nevertheless returned the visual-resource URIs below. A bounded `read_mcp_resource` attempt for the sweep JSON at offset `0`, length `16384`, returned exactly `Mcp error -32603: Artifact provenance manifest is unavailable`. The local sweep JSON had already been read and hash-verified before it disappeared; all expected local paths for its rendered files were absent on recheck. No file copies were made and no MCP configuration or dependencies were changed.

## Scope findings and boundaries

- The candidate pool is complete for all four accepted scenarios. The scenarios are hypothetical and conditional on `chaosx.nr24.2` being delivered to a valid Swedish host.
- P24-O2 is the only scenario with tool-ranked exact rows: Controlled `0.4727954971857411` (rank 1), Commercial `0.42213883677298314` (rank 2), Officer `0.1050656660412758` (rank 3). The scenario artifact still includes the unresolved `compare_autonomy_state` helper path, so this is not promoted to an exact campaign probability claim.
- P24-O1, O3, and O4 return bounded conditional-probability intervals. Their candidate rank fields and `summary.topOutcomes` disagree with the row intervals in O1, O3, and O4. The ranking conclusion for those scenarios is unresolved despite the available bounds; no balance target is selected.
- O4 returns Commercial raw value and conditional probability `0`, lists `.2.b` as impossible in that scenario, and emits `PROBABILITY_STARVED_OUTCOME` for `.2.b`. This matches the accepted emergency direction when the declared supply/core-loss crisis packet activates the source helper. It is conditional evidence, not a source edit.
- The source-level observation that Commercial has a zero crisis factor is now corroborated by this declared O4 evaluation row. No source or weight change was made.
- Parent-owned `.50` state-flow work is a separate boundary and was not duplicated.
- D16's organization/rail/control/reserve proxy remains unapproved; the original exact supplied-division requirement remains binding. Field-Validated Planner remains retired. No gameplay, AI, event, weight, workbook, or CSV edits were made.

The parent-reported benchmark-fixture commit is `03e28c3bd135a381e70273259f7f977707feee8a`; the parent reports the physical hashes recorded in handoff 27 remain unchanged. The parent-reported HEAD was `b7aec0524`; the last local HEAD observed before this update was `03ae2d2c635a5c55fc64c8b35fef886502c64db9`. The shared tree was preserved. Handoff 28 remains the only owned file and is unstaged; no index update or commit was made.

## Continuation results: inspect, evaluation, and sweep

This section supersedes the earlier “blocked before evaluation” status and records the successful narrower inspect and subsequent partial analysis.

### Inspect result

The narrower source `{ path: "events/024_hearts_of_iron.txt", identifier: "chaosx.nr24.2" }` was accepted by the live frontend. It selected the visible `.2` option event, not the hidden `.1` dispatch root. The inspect result was `PROBABILITY_SOURCE_INSPECTED`, `poolComplete = true`, 3 candidates, 9 required paths, and 0 unresolved inspect items. Source revision `2ce215be4a2aef156896b2e85f4e8abe040349a30d6eb9e8f04b888617f55b0c`; aggregate source hash `2d2c31c4c1053d4b3006a116a88430f86350d5b247f44b961bbbaca49426224a`. Artifact URI and declared size are above.

### Scenario coverage and unresolved inputs

The evaluator retained the four fixture IDs and the complete three-option pool, yielding 12 scenario/candidate rows. The fixture's 14 logical alternative combinations were carried as uncertain bounds: O1 has two government alternatives; O2 has one state; O3 has Chaos 250/799/800; O4 has four governments crossed with Chaos 250/800. No prevalence weights were supplied.

The artifact's top-level unresolved list contains 2 `TRIGGER_UNRESOLVED` records, both `compare_autonomy_state` with message “Scenario does not declare trigger compare_autonomy_state.” This path is reached through `video_game_in_sweden_is_low_autonomy_subject`. `is_subject = false` was declared, but the adapter did not prove the helper false; no ordinal or helper override was supplied. The artifact repeats these same unresolved references by candidate/branch: 4 for O1, 2 for O2, 6 for O3, and 16 for O4. No separate `eventTargets` validation error appeared; the declared host target is still only a delivery assumption and does not validate `video_game_in_sweden_is_current_host`.

### Candidate rows and bounded conditional shares

All rows have `eligibility = true` and complete pool coverage. Raw values and conditional shares below are copied from the verified sweep JSON. Intervals are adapter-returned bounds across the declared alternatives; they are not sampled campaign outcomes or hand-calculated probabilities.

| Scenario | Candidate | Raw value or interval | Conditional share or interval | Returned rank/status |
| --- | --- | ---: | ---: | --- |
| P24-O1 | Controlled `.2.a` | 10.8–14.4 | 0.6545454545454545–0.7164179104477612 | rank null; bounded |
| P24-O1 | Commercial `.2.b` | 4.5 | 0.22388059701492538–0.2727272727272727 | rank 1 among resolved rows; bounded |
| P24-O1 | Officer `.2.c` | 1.2 | 0.05970149253731343–0.07272727272727272 | rank 2 among resolved rows; bounded |
| P24-O2 | Controlled `.2.a` | 7.56 | 0.4727954971857411 | rank 1; tool labels scenario exact, with unresolved helper input |
| P24-O2 | Commercial `.2.b` | 6.75 | 0.42213883677298314 | rank 2; tool labels scenario exact, with unresolved helper input |
| P24-O2 | Officer `.2.c` | 1.68 | 0.1050656660412758 | rank 3; tool labels scenario exact |
| P24-O3 | Controlled `.2.a` | 0.56–1.12 | 0.018893387314439947–0.0691358024691358 | rank null; bounded |
| P24-O3 | Commercial `.2.b` | 1.08 | 0.03643724696356275–0.06666666666666667 | rank 1 among resolved rows; bounded |
| P24-O3 | Officer `.2.c` | 14–28 | 0.8641975308641975–0.9446693657219973 | rank null; bounded |
| P24-O4 | Controlled `.2.a` | 2.24–22.4 | 0.5614035087719298–0.9907120743034056 | rank null; bounded |
| P24-O4 | Commercial `.2.b` | 0 | 0 | rank 1 among resolved rows; starved/impossible in declared crisis state |
| P24-O4 | Officer `.2.c` | 0.21–1.75 | 0.009287925696594427–0.43859649122807015 | rank null; bounded |

The tool's scenario `summary.topOutcomes` values are O1 `.2.b, .2.c, .2.a`; O2 `.2.a, .2.b, .2.c`; O3 `.2.b, .2.a, .2.c`; and O4 `.2.b, .2.a, .2.c`. These summary lists conflict with the candidate interval bounds in O1, O3, and O4, where the named top outcome is not the highest interval. Candidate `rank` is null for the bounded candidates. Therefore only O2 has an unambiguous returned row ranking; O1/O3/O4 remain ranking-unresolved despite the conditional intervals. No exact campaign selection probability is claimed.

The O4 Officer lower conditional bound `0.009287925696594427` is below the adapter's documented 1% d100 granularity boundary. No separate quantization diagnostic was returned, so its engine-effective d100 outcome remains unresolved. The O4 Commercial zero is a source-conditional AI weight, not an option visibility gate for a human.

### Exact diagnostics

The evaluation and sweep each returned 8 diagnostics: one warning and seven informational modifier-coverage notes.

| Severity/code | Candidate and scenario | Message |
| --- | --- | --- |
| warning `PROBABILITY_STARVED_OUTCOME` | Commercial `.2.b`, P24-O4 | Eligible but at or below the configured starvation threshold. |
| info `PROBABILITY_MODIFIER_UNSATISFIED_IN_SCENARIOS` | Controlled `.2.a` | `opening_neutral_controlled` not active in any primary scenario state. |
| info `PROBABILITY_MODIFIER_UNSATISFIED_IN_SCENARIOS` | Controlled `.2.a` | `opening_subject_controlled` not active in any primary scenario state. |
| info `PROBABILITY_MODIFIER_UNSATISFIED_IN_SCENARIOS` | Controlled `.2.a` | `opening_totalen_controlled` not active in any primary scenario state. |
| info `PROBABILITY_MODIFIER_UNSATISFIED_IN_SCENARIOS` | Commercial `.2.b` | `opening_communist_commercial` not active in any primary scenario state. |
| info `PROBABILITY_MODIFIER_UNSATISFIED_IN_SCENARIOS` | Commercial `.2.b` | `opening_subject_commercial` not active in any primary scenario state. |
| info `PROBABILITY_MODIFIER_UNSATISFIED_IN_SCENARIOS` | Officer `.2.c` | `opening_neutral_officer` not active in any primary scenario state. |
| info `PROBABILITY_MODIFIER_UNSATISFIED_IN_SCENARIOS` | Officer `.2.c` | `opening_totalen_officer` not active in any primary scenario state. |

These informational diagnostics describe modifier activation in primary states; the fixture also declares alternatives that appear in bounded intervals. They do not prove those alternatives were omitted from the intervals. Their exact per-branch trace cannot be reconciled with the conflicting summary rankings from the accessible outputs.

### Threshold sweep and retained visual evidence

Sweep request paths were `variable.global.chaos_meter_value`, `has_stability`, and `has_army_experience`, with rank-reversal search enabled and pairwise mode disabled. The evaluator returned 15 sweep points, 12 rows, 8 diagnostics, and 2 unresolved top-level items. The direct structured summary does not enumerate each sampled point; this handoff does not claim the exact 799/800, 0.20/0.35/0.50, or 25 values were all sampled. Scenario hash remained `cd04dc91cc63222f017e3a663f363c6ac51b2f17f49382f70d159225108ab900`; sweep source revision was `8cf0c3a1a262b5bed53a6213c1a554ba007dd1a59281e7a89e761f6d824af2b9`.

The sweep JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a81a159740a174245d2ecb033bf19cf206958027e228d6bf631457cfdadbcd9c/33d20efa4f1b0bc6420efc5aa16e9c93d30abdcc9e9cca073d5416dff3565f14/probability-e2f014038b67452f9116eecf.json`, 234,975 bytes, SHA-256 `a81a159740a174245d2ecb033bf19cf206958027e228d6bf631457cfdadbcd9c`. The configured local copy was read and hash-verified, then was absent on a later local recheck. A bounded `read_mcp_resource` attempt returned `Mcp error -32603: Artifact provenance manifest is unavailable`.

Evaluation JSON URI (declared size 226,110 bytes, SHA-256 `72fff1e4dbed7e3c014600b53e9bb5622148d24c44a1985a135c76b6b64d5538`): `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/72fff1e4dbed7e3c014600b53e9bb5622148d24c44a1985a135c76b6b64d5538/678cc473de4fbf9ec0a72000cdd1ae7bb7b59083eaaf9d8acdb0c8d2fdbd4b90/probability-801e0167484e374a043a5e40.json`. Its local copy was absent at the later workspace check. The row-level values above come from the verified sweep JSON, not from cached prior probabilities.

Evaluation render resources:

| View | Bytes | URI |
| --- | ---: | --- |
| ranking.svg | 1,332 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6b5046f4a68e8b79d1db5388da50451a672350afcbe3a81a41aa11c9ff592921/a342b4c8efded844c374ee85ed5deeb49575fa6837456194a97dae7fcca9aa26/probability-probability-801e0167484e374a043a5e40-ranking.svg` |
| ranking.png | 16,558 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/008267bbd47411be6ffa16f79969f8d437e42290ae014fe5dee2fb8d89f6875b/a4b07fdf358f31acc8e653a2896cfa828f23e8635f330f2115435853118af250/probability-probability-801e0167484e374a043a5e40-ranking.png` |
| matrix.svg | 2,836 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/74a957962e5a9374b35982cd561de177e84450b20cd2aab0b68d9630d28257de/e6034198996cb5318d5d9b3008b23b961d2e7c5cf7954677dd105d7f5a964898/probability-probability-801e0167484e374a043a5e40-matrix.svg` |
| matrix.png | 10,298 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5f3992d5b9d652f89240a88e8b8fedb61a4260d0b3b222e7ee5680ac128e962b/c2ce940b5d8c9b06195ffd7d8ece4446265dc436f3401b40bd22ac9450be7240/probability-probability-801e0167484e374a043a5e40-matrix.png` |
| unresolved.svg | 929 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7797581dc90f7719863256b7f0e69ba04209c5a40b9c83b988cbbf606811dbcc/bbdad3adc603dd02903cb22eb21760727b151033bbaa36f520c2201ec2ec7675/probability-probability-801e0167484e374a043a5e40-unresolved.svg` |
| unresolved.png | 17,302 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/da402f52177bba660da3efbdbe6b8f23ec551196745a5b5213daf3a25a20d59b/b9922f47285fc05c17364ba3b5a5bb98f62c194b5058d2459100210571bdbf0e/probability-probability-801e0167484e374a043a5e40-unresolved.png` |

Sweep render resources:

| View | Bytes | URI |
| --- | ---: | --- |
| ranking.svg | 1,332 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/58321a801dd50162bf9281fac408c87b2bc856d8dcf42d4f62c7c5b7f78f5550/7c2260dce916bd1f3479d2e56c2875db312d1316d15a07c59d3ac38072268bd2/probability-probability-e2f014038b67452f9116eecf-ranking.svg` |
| ranking.png | 16,406 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f0e80d85dd7edca04dc15a3d5af63ce196612c21457ff1bc97c3ed622abd599c/6c751fc1c61fc8d873dc9b6e8af583fbb0f100fa15deb055a3a672083b12b5df/probability-probability-e2f014038b67452f9116eecf-ranking.png` |
| matrix.svg | 2,836 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/74a957962e5a9374b35982cd561de177e84450b20cd2aab0b68d9630d28257de/fa3f96ba0d267fe0b4f1f40b4e18df24c99af6027f421958e848aa33dc0a7edc/probability-probability-e2f014038b67452f9116eecf-matrix.svg` |
| matrix.png | 10,298 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5f3992d5b9d652f89240a88e8b8fedb61a4260d0b3b222e7ee5680ac128e962b/b0696b9e805f0ce334b45036579d0034468d5081bfdaae4b447c3a8c6a0340cb/probability-probability-e2f014038b67452f9116eecf-matrix.png` |
| sensitivity.svg | 1,498 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1455778e63fa06f20e9c6b7b3d190dc59ea5d2ebb4065cc0e9ecc371f263aa0a/fd9c21c489d08f7a305b75624d889ed2930ccc9c4767814ac6cdd4aabdee92bc/probability-probability-e2f014038b67452f9116eecf-sensitivity.svg` |
| sensitivity.png | 47,820 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d4db31fa989b794d4f04f48d5d7b63e964d404a9b604c3847fc2943246b6e57e/a761cf81917acac730a2241a3d1e25636fa058972ac5071f271af4442fc7fe64/probability-probability-e2f014038b67452f9116eecf-sensitivity.png` |
| threshold.svg | 785 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ec50539182703663532b341ff64bb53107c421cb800e7fb186431cd28c25c67d/ab885bdb8f101c93544f25f5d62830b28e1232bfc53208c0ccb5f63c3da92563/probability-probability-e2f014038b67452f9116eecf-threshold.svg` |
| threshold.png | 14,355 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0a72519dc2bfc6ed12a2bb08e09b9f59716b623455f301e828f9d68c338f2897/ed610eb97d81ad03c76cde72107bc6caae57a154a9fadccdbb53568f3cd4caa8/probability-probability-e2f014038b67452f9116eecf-threshold.png` |
| unresolved.svg | 929 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7797581dc90f7719863256b7f0e69ba04209c5a40b9c83b988cbbf606811dbcc/382cf52b4b0eaa659d7da3581ed06de08c5f425bdb75ea737962c34ae3bf834e/probability-probability-e2f014038b67452f9116eecf-unresolved.svg` |
| unresolved.png | 17,302 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/da402f52177bba660da3efbdbe6b8f23ec551196745a5b5213daf3a25a20d59b/9ff3162b7103785001cd1283c2776384701b4affd71054f8330a120514e64da9/probability-probability-e2f014038b67452f9116eecf-unresolved.png` |

The standalone `hoi4.probability_render` call returned `PROBABILITY_ANALYSIS_NOT_CACHED`; the evaluation/sweep calls' own visual resources are retained above. Local copies for these rendered resources were absent on the workspace recheck, so their URI-declared byte sizes and SHA-256 values are preserved but not locally reverified.

## Frozen baseline identity for the owner patch

After this baseline was reviewed, the parent changed only the Controlled opening's Totalen modifier reference from `video_game_in_sweden_ai_factor.opening_totalen_controlled` to `video_game_in_sweden_ai_factor.opening_totalen_controlled_safe`. The old constant remains `0.5` for the frozen before source; the new current factor is `2.0`. The Officer Totalen factor remains `2.0`. This handoff remains the before baseline; the mandatory same-scenario comparison is recorded separately in `29_opening_probability_compare_2026-10-07.md`.

The byte-frozen before event source is `docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-07_pre_evolution_timing/source/events/024_hearts_of_iron.txt`, SHA-256 `60904703034703c8254f080b0bf63d2cf1829923db29087fe5687385ec09b095`. The parent confirms the constants and trigger source hashes retained from handoff 27 are `11872d5dd1da14b70a3cd231817e7d5c672a10ef46eb05cfc475558c5fefdb78` and `e0bfc38415f180643f69e29ba482d43deec996777a74fd760607e419c0262098` respectively. No new source copy was made.

Before the patch, the bounded benchmark sweep reported P24-O3 Controlled raw interval `0.56–1.12` and conditional interval `0.018893387314439947–0.0691358024691358`; P24-O4 Controlled raw interval `2.24–22.4` and conditional interval `0.5614035087719298–0.9907120743034056`. These are the MCP baseline bounds, not hand-calculated deltas or balance targets.

The parent later requested a mandatory compare against this frozen source. The compare's direct summary reported `comparisonChanges = 0` and `scenarioChanges = []`, while its current-side O3/O4 row intervals differ from the baseline rows above. The comparator delta is therefore unresolved; the exact result and row evidence are recorded in `29_opening_probability_compare_2026-10-07.md`.
