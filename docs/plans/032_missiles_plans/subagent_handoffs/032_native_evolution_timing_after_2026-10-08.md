# Event 32 native evolution timing after pass, 2026-10-08

Disposition: the bounded conditional clock pass is complete.
Pressure publication, successful unlock effects, finite first-pulse timing, and the old uniform-delay numeric delta remain unresolved.
The parent retains model and tuning ownership.

The exact five native candidates in `events/032_missiles_evolution_events.txt` were inspected first: `chaosx.nr32.201` Rogue, `.202` Guidance, `.203` Saturation, `.204` Special Warheads, and `.205` Automatic Retaliation.
The adapter recognized all five with `poolComplete = true`.
Event `.192` is a triggered-only notification and is outside that clock pool.

Evidence is under [after_20261008](../evidence/evolution_timing_20261007/after_20261008/).
[after_summary.json](../evidence/evolution_timing_20261007/after_20261008/after_summary.json) contains all 65 result rows, source revisions, scenario hashes, analysis IDs, exact artifact URIs and classification limits.
Every retained MCP artifact was read and checked against its advertised byte count and SHA-256.
No artifact over 2 MB was fetched.
The largest probability artifact was 1,160,612 bytes.

## Fixture and source continuity

The original five before snapshots and [original scenarioSet](../evidence/evolution_timing_20261007/scenarioSet.json) remain unchanged.
The original fixture SHA-256 is `2f5136de919f4e1b1a3b9459e061a9ce3d80c69e16e6aff401eb6cc49ac89608`.

The [paired v2 fixture](../evidence/evolution_timing_20261007/after_20261008/scenarioSet.paired.v2.json) was saved and schema-checked before evaluation.
Its SHA-256 is `6b60ca86b189bf26adb912d130610332558a51dc7987139d057aba14595f62cb`.
All evaluation requests and both comparison requests contain the identical parsed v2 object.
The thirteen named intents remain EVO-01 through EVO-12 and EVO-PACE.
The MCP scenario hash is `f1868ac504946c54a1c4c96ab6dfd39a0c2b27e21b5fdd7cbc67d93e60fdfc17`.

[paired_mapping.v2.json](../evidence/evolution_timing_20261007/after_20261008/paired_mapping.v2.json) records the explicit change to an armed, published-cache clock boundary.
Original temporary pressure values remain, actual global aliases are added, and unordered operational hostile pairs are recalculated separately from global response-capable countries.
Country enumeration is omitted from the clock request, while its declared world remains preserved in the original fixture.
GER is the single typed host.
The numeric `id = 1` and cached host ID of 1 are declared equality facts, not a claim about GER's actual native ID.
Complete-observation and program flags are explicit.
Ordinary cases declare pending/native mode, including stale armed clocks in negative cases so their actual gates are exercised.
EVO-PACE declares short mode and due-date presence, with the numeric due value used only as a presence fixture.
There are no candidate overrides or scripted-helper truth overrides.

Every scenario has complete declared primitive inputs for this conditional gate/day-factor calculation.
The full external world remains incomplete for every scenario.
Actual site validity, pressure publication, host selection/transfer, changing conditions, cross-track feedback, and successful effect dispatch are not established.
All ordinary clock states stay fixed over the horizon, with no scheduled changes or sampling seed.
The probability result is conditional on 365 active daily checks beginning at analysis day zero.
It does not include an undeclared initial inactive-trigger polling delay or prove a calendar-time unlock rate.

The source snapshots and hashes are in [source_manifest.json](../evidence/evolution_timing_20261007/after_20261008/source_manifest.json).
Core source files are:

| Source | Audited surface |
| --- | --- |
| `events/032_missiles_evolution_events.txt:9` | Five native gates and one-day bases multiplied by cached day scales |
| `common/mtth/032_missiles_evolution_mtth.txt:5` | Base values and ordered few-usable, high-pressure and final-tier factors |
| `common/scripted_triggers/032_missiles_evolution_triggers.txt:5` | Current host ID, program, observation-ready and world-end gate |
| `common/scripted_triggers/032_missiles_operations_triggers.txt:1073` | Cached eligibility and high-pressure predicates |
| `common/scripted_effects/032_missiles_operations_effects.txt:543` | Pressure publication and unordered hostile-pair count |
| `common/scripted_effects/032_missiles_evolution_effects.txt:6` | MTTH-value publication and finite notification/attempt helpers |
| `common/script_constants/032_missiles_constants.txt:414` | Timing, pressure and pacing constants |
| `common/script_constants/chaos_meter_constants.txt:29` | Final tier ID 5 and its 1000-chaos threshold |

The evaluated event snapshot SHA-256 is `8728c998407f6bbef6c88923ee40a6a7d78dc9c4007604fb91facce501398577`.
The MTTH-definition snapshot SHA-256 is `2b0497761772af55759cb75cd0d6cce890324136344462ea69c2e47e706a7a1c`.
Shared files changed during owner lifecycle work.
At the closing check, all five native event bodies still matched the evaluated snapshot after newline normalization, all ten eligibility/high-pressure helper bodies matched, and all existing timing/pressure/pacing values were unchanged.
The newly added `payload_completion_grace_days` key is outside these MTTH entries.
[source_continuity.json](../evidence/evolution_timing_20261007/after_20261008/source_continuity.json) preserves the differing whole-file hashes and the bounded continuity checks.
This is not a historical whole-workspace overlay.

## Conditional clock results

M denotes the effective native median-time parameter.
The base anchors remain Rogue 120, Guidance 105, Saturation 90, Special 120 and Automatic 150.
[cache_input_traces.v2.json](../evidence/evolution_timing_20261007/after_20261008/cache_input_traces.v2.json) derives declared cache inputs from the actual MTTH entries, constants and reviewed high-pressure predicates.
These traces are source calculation evidence.
The MCP then evaluates the real event's one-day base and cached factor.
It does not prove execution of `missiles_update_evolution_mtth_values` or the pressure publication effects.

| Scenario | Native result under declared state | M | Chance by 365 active days |
| --- | --- | ---: | ---: |
| EVO-01 | Rogue eligible | 60 | 98.53% |
| EVO-02 | Rogue excluded, secure world has zero vulnerable programs | N/A | 0% |
| EVO-03 | Guidance eligible, launch/readiness and war pressure | 52.5 | 99.19% |
| EVO-04 | Guidance eligible through explicit overstocking, one usable program | 157.5 | 79.94% |
| EVO-05 | Saturation eligible, four operational programs and two at war | 90 | 93.99% |
| EVO-06 | Saturation excluded, early non-operational program | N/A | 0% |
| EVO-07 | Special excluded, no payload owner | N/A | 0% |
| EVO-08 | Special eligible, two payload owners | 60 | 98.53% |
| EVO-09 | Automatic excluded below 900, Saturation independently eligible | N/A / 90 | 0% / 93.99% |
| EVO-10 | Automatic and Saturation independently eligible | 225 / 90 | 67.52% / 93.99% |
| EVO-11 | All five disabled clocks excluded | N/A | 0% |
| EVO-12 | All five already-unlocked clocks excluded | N/A | 0% |
| EVO-PACE | All five native clocks excluded by short mode | N/A | 0% for native clocks only |

There are eight eligible and 57 excluded rows, with zero unresolved primitive inputs.
The MCP classifies their fixed-state clock values and cumulative chances as exact.
No sampled or AI-score result is claimed.
Excluded rows have a tool value of zero, which means exclusion and must not be presented as instantaneous timing.
EVO-11 and EVO-12 establish clock gating under those flags, without proving recorder effects.
EVO-PACE establishes mode exclusion only, and its intended finite delay and popup spacing remain unresolved.

The five-clock evaluation returned effective M values but no cumulative-chance fields.
The installed analyzer computes horizon chance only for a one-candidate MTTH surface.
Five additional singleton calls therefore used the exact same thirteen-case fixture, with each already-inspected clock selected in turn.
These clocks are independent timing surfaces, so no probability-proportional normalization applies.
The full five-candidate pool and every singleton result are retained.

The two-point Automatic sweep used only 899 and 900 chaos.
It returned the expected threshold-cliff diagnostic, with raw endpoints zero/excluded and 225/eligible.
Its aggregate interval is bounded and has mixed eligibility.
The aggregate scalar chance is not a probability over an unspecified distribution of chaos values.
The exact fixed cases EVO-09 and EVO-10 supply the applicable cumulative results.
No rank-reversal or whole-workspace sweep was run.

The source's final-tier factor 0.80 was reviewed, but no original scenario reaches tier 5.
Its publication branch remains unexercised in this pass.
Saturation's few-operational-program factor is also inactive whenever the current two-operational-program eligibility floor is met.
That agrees with the explicitly ineligible EVO-06 fixture and does not establish a tuning defect.

## MCP identity, comparison and render limits

The recovered read-only stdio MCP connection reported `hoi4-agent-tools 3.10.0`.
The adapter is `hoi4-1.19.2.v1`, with installed-game verification for Operation Postern 1.19.2.0, checksum `d245`.
It uses the verified daily median-hazard model.
Native tasks were not negotiated.

| Analysis | ID |
| --- | --- |
| Five-clock matrix | `probability-5dd87eaeea057bedd924d375` |
| Rogue curve | `probability-ac964d92448f404040a3abcd` |
| Guidance curve | `probability-9f2efc10cd598b06a5d1ee41` |
| Saturation curve | `probability-f39a14a6230f0d305de076b3` |
| Special curve | `probability-84d14eda5610e869b5241b6a` |
| Automatic curve | `probability-6ec133fed95ef3cd443ae0ce` |
| Two-point threshold | `probability-cb4a2aae31d2aaaaedb65043` |

The probability source hash is `056277ba1e93f83f48b98536ca251d557d6f3e25259106bcc3a5b4a40430f3d5`, distinct from the physical event-file SHA.
Exact revisions and URIs are in the summary and the per-action `.response.json` and `.artifacts.json` files.
The primary five-clock source revision was `3dbe17c95dab142383ff63da879380fb7f50dd80455b793c5f9509a8cf39d719`.
The threshold fixture hash is `4e55fc4896b32ab77aad70e3e327c4ff0732771bfb7049d31270d100f2d067a1`, and its MCP scenario hash is `7e852de9aebfad58864bee6b5d8339437b89c1dd48eac2fb3fd7bdb00891736f`.

Mandatory `probability_compare` was attempted against the original operations snapshot and the native event snapshot.
One additional attempt used the original event-file snapshot as the zero-native before source.
Both used identical paired v2 objects and both returned `PROBABILITY_SURFACE_EMPTY`, with “No weighted blocks matched this request”.
Neither returned a comparison ID or numeric delta.
The original uniform-delay model remains unsupported.
No self-comparison, synthetic native before source or custom-pool proxy was used.

The initial connected-tool artifact read failed with `Artifact provenance manifest is unavailable`.
A separate initialized read-only MCP SDK connection using the configured executable, config and repository directory recovered inspection and analysis artifacts.
The standalone MTTH-file discovery attempt produced no observed result before its wait was terminated, and is not counted as numeric evidence.
Those route facts are preserved in `initial_route_evidence.json` and the connection records.

An explicit `probability_render` request returned `PROBABILITY_ANALYSIS_STALE` after the shared workspace revision changed.
The analysis-time matrix and singleton timing resources were retained and visually reviewed.
The generic matrix colors and ranks follow raw M magnitude, so a larger value must not be read as faster timing.
In EVO-10, Saturation's M of 90 is faster than Automatic's 225 despite the generic descending rank.
The timing graphic's axis extends beyond the 365-day modeled interval and holds the final plotted survival value afterwards.
That plateau is not evidence of starvation or a permanent survival floor.

The matching structural inspect/render calls were restricted to the new event file, depth one and twelve nodes.
They identified the five automatic native events and the triggered-only notification.
The timing render selected ten nodes.
Both results remained partial, with deferred helper/lifecycle coverage and unresolved helper projections.
The helpers exist in source, and these focused-catalog findings are not proof that their implementations are absent.
Structural revisions and rendered URIs are retained in the summary.
The diagram does not prove host recovery, callback coalescing or exactly-once recording.

## Remaining work and recommendations

The named fixed-state gates show no positive clock chance on the excluded cases.
The positive-clock tails are materially different, especially Guidance at 157.5 and Automatic at 225.
This pass establishes neither live starvation, repetitive unlocks, exploit frequency nor a coupled five-track unlock order.
The source and target tuning remain with the parent.

Finish the owner-side pressure-publication and lifecycle cases against `032_missiles_operations_effects.txt`, `032_missiles_evolution_effects.txt` and `032_missiles_evolution_triggers.txt`.
They should establish unordered pair counting separately from responders, atomic complete-observation publication, real cached-M values, host identity/recovery, short/native exclusivity, cancellation, and once-only recording.
Also cover final-tier publication, world-end true, non-host and incomplete-observation inputs, which are not separate cases in this saved matrix.
Do not interpret the conditional CDF as the probability of a successful unlock after its fresh effect-time revalidation.

Simulation and sequence were skipped because no sampled external distribution or complete custom pool was declared.
No recurring world scan was added.
No gameplay, AI, localisation, runtime, Git, game or game-log file was edited.
No gameplay simplification or tuning patch was applied.

References read through MCP include offline Data structures: MTTH variables, lines 887-913, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, and installed effects documentation: set_variable, lines 7888-7895, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
The previously read offline Event modding triggering section and vanilla `political.1` native MTTH precedent remain linked in [references.json](../evidence/evolution_timing_20261007/after_20261008/references.json).
Skills used: chaos-redux-subagents, chaos-redux-events, chaos-redux-mtth and the scenario discipline from chaos-redux-event-planning.
No skill was changed.

## Four-gate supplement, 2026-10-08

A separate [four-case fixture](../evidence/evolution_timing_20261007/after_20261008_gate_supplement/scenarioSet.gates.v1.json) was saved and schema-checked before one five-candidate evaluation.
Its SHA-256 is `47949bbf38da191a9df469316a70435441a36237b06a2f112f31576484f71917`.
All clocks use ordinary pending/native mode, all short flags are false, and every due-date key is absent.
No helper or candidate override is supplied.

| Scenario | Rogue .201 | Guidance .202 | Saturation .203 | Special .204 | Automatic .205 |
| --- | ---: | ---: | ---: | ---: | ---: |
| EVO-FINAL | 48 | 42 | 36 | 48 | 60 |
| EVO-WORLD-END | Excluded | Excluded | Excluded | Excluded | Excluded |
| EVO-NONHOST | Excluded | Excluded | Excluded | Excluded | Excluded |
| EVO-INCOMPLETE | Excluded | Excluded | Excluded | Excluded | Excluded |

The numbers are effective M in days.
Excluded rows return raw/effective values of zero.
All 20 rows are exact within the declared conditional model, with five eligible rows, 15 exclusions, zero diagnostics and zero unresolved inputs.
The three negative cases retain positive cached M inputs.
Their traces identify the world-end guard, native host-ID comparison and observation-ready flag in `missiles_evolution_clock_host_is_current`, respectively.
Non-host exclusions apply to the modeled GER root with ID 1 while the global host is FRA with ID 2.
Incomplete observation is explicitly declared absent, including omission from the present-flags list.

The [input traces and contract](../evidence/evolution_timing_20261007/after_20261008_gate_supplement/gate_contract_and_input_traces.json) derive M from the actual MTTH entries: bases 120/105/90/120/150, high-pressure factor 0.5 and final-tier factor 0.8, with no few-usable multiplier applied.
The baseline has chaos 1000, tier value 5, programs/operational/war counts of 4, vulnerable/payload-owner/responder/hostile-pair counts of 2, and explicit Guidance strain of two low-readiness programs and three launches.
This evaluates the native clock using those source-derived caches, without executing cache publication.

The analysis ID is `probability-8b4ba2c86f01733a8917075f`.
Its scenario hash is `2910fbf6eab29787791edcb5357dddea54fc3b6ab6229c465eab52a5ca4bbcee`, and source revision is `81d1c79d38f85844282a38fab6f78832033128b2aa26c106998ac1b7a7f0765c`.
The complete 367,153-byte artifact was retrieved and verified with SHA-256 `a24e03141a17d3b2d124f8e900aa4f14bf5265cf3627efa94b4f593c74327d6f`.
[result_summary.json](../evidence/evolution_timing_20261007/after_20261008_gate_supplement/result_summary.json) retains the exact artifact URI, all 20 rows, exclusion traces and source-continuity evidence.

All six [snapshotted sources](../evidence/evolution_timing_20261007/after_20261008_gate_supplement/source_manifest.json) remained hash-stable during the run.
The MTTH entries, host gate and five high-pressure predicates match the previous pass.
The existing two 13-case fixture hashes, prior summary and all 28 verified MCP artifacts remain unchanged.
The earlier handoff text is preserved as the prefix of this document.

The parent reports 23 passing actual-source clock tests.
Those are separate parent evidence and were not rerun here.
Native execution, log presentation and country adoption remain outside what this supplement proves.
The established old uniform-delay comparison limitation is unchanged.
No CDF, sweep, sequence, comparison retry or new render was requested.
Only this appendix and separate audit evidence were written, with no source/tuning edits, helper-code changes or Git operations.
