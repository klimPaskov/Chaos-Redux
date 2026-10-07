# Event 24 opening probability comparison

Audit date: 2026-10-07.

Status: the first mandatory same-scenario comparison returned `PROBABILITY_ANALYZED_PARTIAL` and reported zero scenario changes despite differing current-side O3/O4 bounds. A second authorized comparison using the explicit 14-scenario expansion timed out after 600 seconds without a structured result. Its remote completion is unknown, the numeric delta remains unresolved, and this is not balance signoff.

## Source identity and comparison request

The bounded owner patch changes the Controlled Staff Trial Totalen modifier in `events/024_hearts_of_iron.txt` from `video_game_in_sweden_ai_factor.opening_totalen_controlled` to `video_game_in_sweden_ai_factor.opening_totalen_controlled_safe`. The prior constant remains `0.5` for the frozen before source; the current safe factor is `2.0`. Officer Totalen remains `2.0`. Parent reports no other weights, effects, or routes changed.

Read-only physical identities checked before comparison:

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| Current `events/024_hearts_of_iron.txt` | 69,760 | `230ac77a8fc9943c51c61e466c89e5288f650df7606dc062c482fd5bf3684b98` |
| Frozen before event file | 69,755 | `60904703034703c8254f080b0bf63d2cf1829923db29087fe5687385ec09b095` |
| Current `common/script_constants/024_video_game_in_sweden_constants.txt` | 24,573 | `bd10bfad71d8216ea3182cac46eb925674f61e0c7be15ee0d16bd165e9690f1b` |
| Current `common/scripted_triggers/024_video_game_in_sweden_triggers.txt` | unchanged per parent/source inventory | `e0bfc38415f180643f69e29ba482d43deec996777a74fd760607e419c0262098` |

The before source is the committed snapshot `docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-07_pre_evolution_timing/source/events/024_hearts_of_iron.txt`, bound by `expectedSourceHash` to the exact byte hash above. The before selector used `path`, `snapshotPath`, `expectedSourceHash`, and `identifier = chaosx.nr24.2`; the after selector used only the current `path` and `identifier`. No `sourceRevision` or `sourceHash` keys were sent in either selector.

The exact parent-owned fixture `P24_OPENING_BENCHMARKS_20261007` from commit `03e28c3bd135a381e70273259f7f977707feee8a` was used unchanged, with candidate pool `.2.a`, `.2.b`, and `.2.c`. The connected frontend accepted the fixture's `uncertainInputs` and `eventTargets`; the 14 logical branches remained represented as bounded inputs across the four named scenarios. `compare_autonomy_state` remained unbound by design. The host target remains a conditional-delivery assumption and does not prove the `.2` current-host trigger.

## Compare result

The live `hoi4_probability_compare` result was `PROBABILITY_ANALYZED_PARTIAL`, status `ok`, analysis ID `probability-e555c9b12d0297c6089e444c`, scenario hash `cd04dc91cc63222f017e3a663f363c6ac51b2f17f49382f70d159225108ab900`, aggregate compare source hash `2bea9883077a9da16eba7c6c146ecaef820a9e8613ee9546d3d48263f77e4155`, and compare source revision `b8d7038abf0c4234d3fcb9fd5304405fd62165e4d06c4a737d27cc5f5e35ac9f`.

The tool analyzed 4 scenarios and 12 candidate rows, with 12 eligible, 0 excluded, 2 unresolved, 0 unresolved candidates, and 8 diagnostics. Its structured summary reports `comparisonChanges = 0`; the authoritative JSON's `comparison` object reports `adapterChanged = false`, `assumptionsChanged = false`, `regressions = []`, and `scenarioChanges = []`. It identifies before analysis `probability-8ec1241f4ae00fcbc84838ea` and after analysis `probability-56418dc05f3a979b7754f38f`.

The direct compare payload does not expose matched before/after rows or a numeric delta. The separate baseline row values from handoff 28 and the current-side rows below are both MCP-backed, but they do not replace the comparator's empty delta result. The discrepancy remains unresolved and must be reviewed by the parent. No hand-calculated delta or balance target is supplied.

## O3/O4 raw and conditional row evidence

The before columns below are the frozen pre-patch MCP bounds from handoff 28's `probability-e2f014038b67452f9116eecf` sweep artifact. The after columns are the current-side scenario candidate rows in the compare JSON. Shares are conditional on the visible `.2` event option pool and are not the event's own firing chance.

| Scenario | Candidate | Before raw / conditional share | After raw / conditional share | After row rank/status |
| --- | --- | --- | --- | --- |
| P24-O3 | Controlled `.2.a` | `0.56–1.12` / `0.018893387314439947–0.0691358024691358` | `1.12–2.24` / `0.0691358024691358–0.07151979565772669` | rank null; bounded |
| P24-O3 | Commercial `.2.b` | `1.08` / `0.03643724696356275–0.06666666666666667` | `1.08` / `0.034482758620689655–0.06666666666666667` | rank 1 among resolved rows; bounded |
| P24-O3 | Officer `.2.c` | `14–28` / `0.8641975308641975–0.9446693657219973` | `14–28` / `0.8641975308641975–0.8939974457215837` | rank null; bounded |
| P24-O4 | Controlled `.2.a` | `2.24–22.4` / `0.5614035087719298–0.9907120743034056` | `4.48–44.8` / `0.8366013071895425–0.9907120743034056` | rank null; bounded |
| P24-O4 | Commercial `.2.b` | `0` / `0` | `0` / `0` | rank 1 among resolved rows; impossible/starved under the declared crisis packet |
| P24-O4 | Officer `.2.c` | `0.21–1.75` / `0.009287925696594427–0.43859649122807015` | `0.21–1.75` / `0.009287925696594427–0.16339869281045752` | rank null; bounded |

These rows show the controlled factor's current-side bound moving on the declared Totalen branch. The compare artifact still reports no scenario changes and gives no direct row delta. The audit therefore records the row bounds and comparator inconsistency without claiming that the patch passed its compare gate.

P24-O2 remains tool-ranked under its declared state: Controlled `0.4727954971857411` (rank 1), Commercial `0.42213883677298314` (rank 2), Officer `0.1050656660412758` (rank 3). The two unresolved helper records below prevent an exact campaign-state interpretation.

## Unresolved inputs and diagnostics

The top-level unresolved list contains two `TRIGGER_UNRESOLVED` entries for `compare_autonomy_state`, each stating “Scenario does not declare trigger compare_autonomy_state.” The path is read by `video_game_in_sweden_is_low_autonomy_subject`. The fixture declares `is_subject = false` and intentionally supplies no autonomy ordinal. The adapter did not prove the helper false; no override was applied.

The eight compare diagnostics are one `PROBABILITY_STARVED_OUTCOME` warning for Commercial `.2.b` in P24-O4 and seven informational `PROBABILITY_MODIFIER_UNSATISFIED_IN_SCENARIOS` entries for `opening_neutral_controlled`, `opening_subject_controlled`, `opening_totalen_controlled_safe`, `opening_communist_commercial`, `opening_subject_commercial`, `opening_neutral_officer`, and `opening_totalen_officer`. The modifier diagnostics describe activation in the primary scenario states; the declared alternative branches are represented by the bounded row intervals. They do not authorize discarding those alternatives.

The current after-side O4 Officer lower share bound is `0.009287925696594427`, below the adapter's documented 1% d100 granularity boundary. No separate quantization diagnostic was returned, so that engine-effective branch share remains unresolved. The Commercial zero is AI weight behavior under the declared crisis helper, not an option-visibility gate for the human.

## Artifact provenance and rendered evidence

The authoritative compare JSON was read from the configured local workspace artifact path and verified at 226,356 bytes with SHA-256 `d76f71c95693b6fd7d4646df1c7ee3535703fe5c16ef7e47983928b74d332ce6`:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d76f71c95693b6fd7d4646df1c7ee3535703fe5c16ef7e47983928b74d332ce6/a0f1068a158d8a12936f5ea206eca2a2fa44bd2e784c2bf8a7bffb801089c24d/probability-e555c9b12d0297c6089e444c.json`

The configured root was read from `C:\Users\klimp\AppData\Roaming\hoi4-agent-tools\config.json`: `workspaceStorageRoot = C:\Users\klimp\AppData\Local\hoi4-agent-tools\workspaces`, with no workspace-specific override field. The verified file path was `C:\Users\klimp\AppData\Local\hoi4-agent-tools\workspaces\mod_chaos_redux_ea3b2d67c2c0\artifacts\d7\d76f71c95693b6fd7d4646df1c7ee3535703fe5c16ef7e47983928b74d332ce6\probability-e555c9b12d0297c6089e444c.json`.

The compare result returned these render resources:

| View | Bytes | URI |
| --- | ---: | --- |
| comparison.svg | 439 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/bff0b0a3a457e178507248afb03509665768e1e0006f46b0c4d8bed4b0c08c24/probability-probability-e555c9b12d0297c6089e444c-comparison.svg` |
| comparison.png | 7,804 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a1fd8e11d21dd2414c85f7412d454fa53b5b857ed9fb09593caa20f6277f498f/9f07de6c684d714eaff927d05615187b7001f669f1f648e11437a6851807f145/probability-probability-e555c9b12d0297c6089e444c-comparison.png` |
| ranking.svg | 1,332 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c0efcce7b5fc256ca4df24168663ccf70208e8d2686adc048e65c87caf450273/3b8698ac2e5d0451121b72ea645c83d903f2f910daeedf5ea799d97829852906/probability-probability-e555c9b12d0297c6089e444c-ranking.svg` |
| ranking.png | 16,608 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/39534fa6439a4238d8cd7b6c7c08d28e54965ae12556082dc4244bfe306c2f65/f1535bd16355f9f63eb2a99b1e439fc049ccf881c6d9c1d64963b8b9210038f5/probability-probability-e555c9b12d0297c6089e444c-ranking.png` |
| matrix.svg | 2,837 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7cbb35bd935c470877691e87daccccb85edc4595ef5ee35bbe803b16a6217b79/c1136b6fce0cc43dd90224b8b6cdf3331cd63e5675f885a4adc25fce6173f404/probability-probability-e555c9b12d0297c6089e444c-matrix.svg` |
| matrix.png | 10,298 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5f3992d5b9d652f89240a88e8b8fedb61a4260d0b3b222e7ee5680ac128e962b/b7deb1fd1ebe6ecb6aa00b1b395580ac733fab6a2d14a34b0a8cbc0eabc9c5f8/probability-probability-e555c9b12d0297c6089e444c-matrix.png` |
| unresolved.svg | 929 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7797581dc90f7719863256b7f0e69ba04209c5a40b9c83b988cbbf606811dbcc/5527e6d94a5f3e676109b20c72c84e16a0b7bd8a94b990808952df925482d722/probability-probability-e555c9b12d0297c6089e444c-unresolved.svg` |
| unresolved.png | 17,302 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/da402f52177bba660da3efbdbe6b8f23ec551196745a5b5213daf3a25a20d59b/41b01c112711b195e753a9c73e00ed6cd5ed56656833c9662f86afb65c8da2b8/probability-probability-e555c9b12d0297c6089e444c-unresolved.png` |

No source, weight, fixture, workbook, CSV, index, or commit change was made by this auditor. Parent review is required before commit. No balance target was selected, and the full Event 24 goal remains incomplete.

## Explicit 14-scenario compare attempt

The parent supplied `P24_OPENING_BENCHMARKS_20261007_EXPLICIT` at `docs/plans/024_video_game_in_sweden_plans/probability_evidence/2026-10-07_opening_benchmarks/P24_OPENING_BENCHMARKS_EXPLICIT.json`. The local fixture was read and validated as 14 unique scenario IDs. Its physical size is 11,130 bytes and SHA-256 is `831a1b731adf9ec76b4f62dff9b89bcafc62c72a1966579880699b3859197de9`. It explicitly expands, rather than averages, all declared alternatives into 42 scenario-candidate rows for the complete pool `.2.a`, `.2.b`, and `.2.c`.

| Base case | Explicit scenarios |
| --- | --- |
| O1 | `P24-O1`; `P24-O1-neutrality-chaos100` |
| O2 | `P24-O2` |
| O3 | `P24-O3`; `P24-O3-fascism-chaos799`; `P24-O3-fascism-chaos800` |
| O4 | `P24-O4`; `P24-O4-democratic-chaos800`; `P24-O4-neutrality-chaos250`; `P24-O4-neutrality-chaos800`; `P24-O4-fascism-chaos250`; `P24-O4-fascism-chaos800`; `P24-O4-communism-chaos250`; `P24-O4-communism-chaos800` |

The request reused the exact before selector and after selector recorded above, the exact explicit fixture, and the complete three-option candidate pool. The before selector used `path = events/024_hearts_of_iron.txt`, `snapshotPath = docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-07_pre_evolution_timing/source/events/024_hearts_of_iron.txt`, `expectedSourceHash = 60904703034703c8254f080b0bf63d2cf1829923db29087fe5687385ec09b095`, and `identifier = chaosx.nr24.2`. The after selector used the current `events/024_hearts_of_iron.txt` and `identifier = chaosx.nr24.2`. `refresh` was false. No `sourceRevision` or `sourceHash` selector fields were added. Parent-provided scope remains unchanged: declared state, flags, and event-target alternatives are preserved; no prevalence average or helper override was introduced; `compare_autonomy_state` remains intentionally unbound, and helper falsehood is not proven.

The tool call returned this exact error after the 600-second wait:

```text
tool call error: tool call failed for `hoi4_agent_tools/hoi4.probability_compare`

Caused by:
    timed out awaiting tools/call after 600s
```

No structured comparison payload or operation handle was returned. Therefore this attempt has no available tool-level status, comparison ID, analysis ID, scenario hash, source revision, row bounds, candidate rankings, diagnostic counts, unresolved count, artifact URI, or rendered evidence. The adapter's remote completion remains unknown. I did not retry it, per the bounded-call instruction. The previously recorded 4-scenario comparison artifacts above belong to the earlier call and are not evidence from this explicit 14-scenario attempt.

Artifact recovery boundary: a fresh recursive filename search under the configured workspace artifact tree for `compare`, `comparison`, `e555`, or `probability` found only `probability-inspect-7673328c88c6.json` (110,193 bytes, SHA-256 `f7bb4cdae2cae53f1e195e90bc72c3fb05172d880c4bbcecc2191a4f9ed95e96`) and its `.manifest.json` (718 bytes, SHA-256 `c5d6a8f4ec2dab4c2a20f56bf8448e56a89fc1765c6205f21c1204aa7e2e4259`). These are inspect artifacts, not an explicit comparison JSON or render. The timed-out tool returned no artifact URI, so there is no authoritative resource URI to retrieve or hash-verify for this attempt, and no new comparison JSON or render was copied into `processed_mcp/`. This does not establish that the remote service produced no artifact. No new comparison values, branch deltas, or balance conclusion can be reported. The required before/after comparison remains unresolved for parent review.

The current physical event source was verified after the request at 69,760 bytes with SHA-256 `230ac77a8fc9943c51c61e466c89e5288f650df7606dc062c482fd5bf3684b98`, matching the post-patch identity already recorded above. No source, weight, fixture, workbook, CSV, index, or commit change was made by this auditor.
