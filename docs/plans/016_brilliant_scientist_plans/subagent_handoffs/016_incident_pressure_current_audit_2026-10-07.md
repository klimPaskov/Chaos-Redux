# Event 016 incident pressure retrospective audit checkpoint — 2026-10-07

Disposition: incomplete probability audit; the caller-owned temporary correction is confirmed in current source, while MCP evaluation, sweep, and comparison coverage remain unresolved or pending.
This is a read-only audit of the two incident-dispatch random lists affected by commit `f0c043037ee49b8aee96d6fcb2a0297b78e6cbed`, not a completion audit of all Event 016 systems.
No gameplay, AI, event, decision, technology, localisation, asset, model, or runtime source was edited.
No game was launched, no tests were run, no Git index operation was performed, and no commit was created.
No simplifying substitute was used for missing probability evidence.

## Current source and frozen evidence

The repository was at `e9cd71fcddfc10310ed2112eef00610ed205e357` when the audit began, and `f0c043037` is an ancestor of that HEAD.
The two incident effect files have no descendant changes between `f0c043037` and the current HEAD, and the relevant accident/project constants also have no descendant changes.
Commit `f0c043037` changed the two scripted-effect sources, their matching Markdown documentation, and `docs/plans/016_brilliant_scientist_plans/agent_decisions_2026-10-04.md`.
The prior cold-lifetime handoff still describes this follow-up as outstanding, while the current D14 decision and source document the completed caller-owned storage correction.

| Weighted surface | Source identifier | Before bytes at `f0c043037^` | Before SHA-256 | Current bytes | Current SHA-256 |
| --- | --- | ---: | --- | ---: | --- |
| Computation incident | `brilliant_scientist_mengele_dispatch_computation_incident` in `common/scripted_effects/016_mengele_computation_incident_effects.txt:178-216` | 16,861 | `1a0eeb265d4d703b916c5c9df97bd24f7bacd313d3ea0ea62c5f6d8980c3c64f` | 17,231 | `620123042010149d726c4148b5ddb48b73757b2f213b6875e7e9a9aad00ab1a0` |
| Conventional incident | `brilliant_scientist_mengele_dispatch_conventional_incident` in `common/scripted_effects/016_mengele_conventional_incident_effects.txt:567-583` | 36,973 | `b26e66f7aa38faf7e34f72007b6a9b86dbd59ed992ce810639978e26eb8e97c9` | 37,343 | `3a52eb1aa60861a62940ba2c761f9e931f08370e87af983ea3db4ac4702ffee2` |

The immutable parent and current source byte copies are outside the repository at `C:\Users\klimp\AppData\Local\Temp\event016_incident_pressure_audit_20261007_f02b985a8f3542e5bb84830b87dbcf9a`.
Their manifest is `source_snapshot_manifest.json`, SHA-256 `cd831ee5c917dfc00bb051d7b1d3a409b179d043fa3709a3cf893903eddfa55f`.
The named scenario fixture is `fixtures\E016_MENGELE_INCIDENT_PRESSURE_RETROSPECTIVE_2026_10_07.json`, 4,498 bytes, SHA-256 `111ab8f8a144fcb7076e8355359ecbef206e29f4bff6177b13b91a82446258f1`.
The fixture declares scenario-set id `E016_MENGELE_INCIDENT_PRESSURE_RETROSPECTIVE_2026_10_07`.
The snapshots are the exact Git parent bytes and current workspace bytes; the current source hashes match the source state reviewed here.

## Source findings

The only gameplay-source delta in commit `f0c043037` for each dispatcher is the initialization of the pressure and complement temporaries to zero in the caller before calling `brilliant_scientist_mengele_load_computation_incident_pressure`.
The shared loader and both random-list branch definitions are otherwise unchanged across the commit and current HEAD.
The computation list weights `var:mengele_event016_computation_incident_pressure` on `brilliant_scientist_mengele_record_computation_incident` and `var:mengele_event016_computation_incident_complement` on an empty no-op block.
The conventional list uses those same two weight variables, with `brilliant_scientist_mengele_record_requested_conventional_incident` as its outcome branch and an empty no-op complement.
Each source therefore contains exactly two candidates at the weighted-selection site.
The pressure loader writes pressure and complement; `mengele_event016_computation_incident_factor` is only scratch inside that helper.
The loader reads the requested stage, stage-capacity constants, and stage-factor constants, clamps to the existing minimum/maximum constants, then sets complement to maximum minus pressure.
The loader does not read the global accident-pressure ledger, Exposure, Kruger state, Capacity, event targets, native project state, or learned-package state.

| Valid requested stage | Existing capacity constant | Existing factor constant | Source-derived raw pressure | Source-derived complement |
| --- | ---: | ---: | ---: | ---: |
| Theory | `brilliant_scientist_project_board.capacity_theory = 10` | `brilliant_scientist_accident.theory_stage_factor = 0.50` | 5 | 95 |
| Prototype | `brilliant_scientist_project_board.capacity_prototype = 10` | `brilliant_scientist_accident.prototype_stage_factor = 1.00` | 10 | 90 |
| Deployment | `brilliant_scientist_project_board.capacity_deployment = 15` | `brilliant_scientist_accident.deployment_stage_factor = 1.25` | 18.75 | 81.25 |
| Weaponization | `brilliant_scientist_project_board.capacity_weaponization = 15` | `brilliant_scientist_accident.weaponization_stage_factor = 1.60` | 24 | 76 |

The loader's minimum and maximum are 0 and 100.
The current valid-stage constants imply a maximum raw pressure of 24, so the upper clamp at 100 is unreachable under the current table.
A zero-pressure binding and the 100/0 upper-clamp binding are declared synthetic adapter-boundary cases, not reachable campaign states.
No MCP evaluation returned to verify these calculated source values as traces or normalized selection shares.

The Computation dispatcher enters its random list only when the shared provider predicate and one of the four valid-stage selectors pass and neither its incident nor recovery is active.
The Conventional dispatcher enters its random list only when the provider and stage checks pass and the selected family's own incident and recovery are inactive.
A different family's active incident does not block the requested Conventional family.
The project-stage settlement calls the Computation dispatcher only after `mengele_event016_computation_output_applied = 1` and the Conventional dispatcher only after `mengele_event016_project_output_applied = 1`.
Thus the weighted list share is conditional on a real successful output and its outer gate; it is not the probability of a stage being attempted, an event firing, or a player click.
After recovery, a later successful output may expose another incident; active incident/recovery state blocks another roll for that same incident while it is active.
This audit did not model the long-run frequency of successful stages or recovery cadence.

## References and source revisions

The required local instructions and the `chaos-redux-subagents` and `chaos-redux-events` skills were read and applied.
No MTTH entry or MTTH-backed AI weight is present in the audited surfaces, so `chaos-redux-mtth` was not applicable.
The current HOI4 Agent Tools status resource reported version `3.10.0`; the active workspace id was `mod_chaos_redux_ea3b2d67c2c0`.
Read-only `hoi4.source_lookup` located both current dispatcher definitions at source-location revision `49fa01ea606ef17c51e5aea0462178d2718b5051bdf2d189ac64072795e6b9fe`.
The focused workspace-index source lookup for the Computation dispatcher reported revision `71e22b10d3f5df7f8604751f45b1968c403d9b75b422933d7fb2fbc717dd4bee`, a complete definition, and no indexed references for that query.
The MCP probability inspection used an inline source object bound to the logical Computation file path and returned source hash `2c795966e0a2b685d7eb0b4897377ca46f805caa68c827d9e938e1878399d245` and source revision `f8b11cad340faf6b3a1f1080592125eab6eef177c2fbb2b07d41b781d12ad779`.
That inspect reported `filesScanned = ["proposed:inline-probability-source.txt"]`; it therefore proves analysis of the supplied exact current inline content, while the separate source lookup and raw Git hashes establish the workspace file identity.

Offline wiki references read:
- `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`, Random effects, lines 4504-4571, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`.
- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, Variable types, lines 435-443, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
- `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`, `random_list`, line 894, revision `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49`, returned by the current AI reference context.

Installed-game documentation read:
- `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md`, `random_list`, lines 5413-5432, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
- `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md`, `set_temp_variable`, lines 7482-7488, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.

The offline wiki says random-list branch weights are proportional and need not sum to 100, and that variable weights use the current scope's variable value.
The installed effects documentation confirms random-list variable weights are valid in the current scope.
The offline variable-lifetime section states that temporary variables defined inside scripted effects may not survive their return, while a caller-defined temporary is carried into the helper and modified there.
That documented rule matches the exact caller initialization correction and explains why the before-source random-list result cannot be treated as a known numeric baseline.

## Probability scenarios and completeness

The complete declared weighted scenario set is `E016_MENGELE_INCIDENT_PRESSURE_RETROSPECTIVE_2026_10_07`.
It contains `E016_WEIGHT_INPUT_ZERO_SYNTHETIC`, `E016_VALID_STAGE_THEORY`, `E016_VALID_STAGE_PROTOTYPE`, `E016_VALID_STAGE_DEPLOYMENT`, `E016_VALID_STAGE_WEAPONIZATION_MAX_REACHABLE`, `E016_SYNTHETIC_WEIGHT_RANK_TIE`, and `E016_SYNTHETIC_UPPER_CLAMP_OUTPUT`.
Each scenario binds both required MCP paths, `var:mengele_event016_computation_incident_pressure` and `var:mengele_event016_computation_incident_complement`.
The valid-stage bindings are source-derived assumptions for the adapter because the inspector reported both variables as required inputs and did not return a loader-expansion trace.
The synthetic zero, 50/50 tie, and 100/0 upper-clamp cases are sensitivity boundaries only and are not asserted as reachable game states.
No date, scheduled state transition, uncertainty distribution, seed, event horizon, custom-pool cadence, or terminal state was declared.

The separate eligibility-only cases in the fixture are `E016_COMPUTATION_PROVIDER_BLOCKED`, `E016_COMPUTATION_STAGE_INVALID`, `E016_COMPUTATION_INCIDENT_ACTIVE`, `E016_COMPUTATION_RECOVERY_ACTIVE`, `E016_CONVENTIONAL_PROVIDER_BLOCKED`, `E016_CONVENTIONAL_REQUESTED_FAMILY_INCIDENT_ACTIVE`, `E016_CONVENTIONAL_REQUESTED_FAMILY_RECOVERY_ACTIVE`, and `E016_CONVENTIONAL_OTHER_FAMILY_INCIDENT_ACTIVE`.
They were deliberately kept outside the probability scenario set because those gates suppress or admit the draw before the random list executes.
The source-visible pool is two branches with no in-list modifier blocks.
The Computation inspector confirmed `candidates = 2` and `poolComplete = true`, but did not return candidate examples.
The Conventional two-branch pool is visible in source but its probability inspection did not complete, so analyzer-confirmed pool completeness remains unresolved for that surface.
External campaign eligibility and the frequency of successful stage outputs are not complete inputs for an overall campaign incident probability.

## Confirmed MCP outcomes and pending analysis

The first valid current probability call was `hoi4.probability_inspect(adapter = random_list)` on the Computation source.
It returned `PROBABILITY_SOURCE_INSPECTED`, `candidates = 2`, `poolComplete = true`, `availableCandidates = 0`, `requiredInputs = 2`, the two pressure/complement input paths, and `unresolved = 0`.
Its artifact URI is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/209c8ca6cb116ff78fc2a37f13f4c277048a784904947e01183914b0a19347c7/5cd15bc2be39341cd771f0e81cdfeee0aba58732e1d320baaf3fbe10baa41ac9/probability-inspect-2c795966e0a2.json`.
Reading that artifact failed with `Mcp error -32603: Artifact provenance manifest is unavailable`.
A bounded retry using `?offset=0&length=2048` returned the same exact error.
The structured tool result is retained above; the artifact's full detailed payload and any renderable analysis id were not available.

The Conventional `probability_inspect` call with the full source timed out after 600 seconds.
A narrower retry using the complete 940-character dispatcher block at the same logical source path also timed out after 600 seconds.
The Computation `probability_evaluate` call with the full source and seven named scenarios timed out after 600 seconds.
A narrower retry using the complete 1,612-character dispatcher block with the same scenario set also timed out after 600 seconds.
The Computation `probability_sweep` request used the same source block and scenarios, both input paths, 101 steps, pairwise sensitivity, and rank-reversal detection; it timed out after 600 seconds.
These are current tool-call timeouts, not claims that the route is absent or that the HOI4 MCP service is globally unavailable.
No source-only calculation is substituted for those unanswered analyzer results.

A single `hoi4.probability_compare` call is still pending as of this checkpoint in live execution cell `48`.
It compares the immutable `f0c043037^` Computation dispatcher block against the current block, using the same seven-scenario set and the same logical engine path.
Do not start a duplicate compare for this surface while that call remains pending.
When it returns, append its exact status, comparison id, scenario hash, source hashes/revisions, artifact URI, and any artifact-read/render outcome to this handoff.

No successful evaluation, sweep, or comparison has produced an `analysisId`, so `hoi4.probability_render` has not been called.
No event graph transition or event-option probability is under review; the audited surfaces are random lists inside scripted effects, so `hoi4.event_inspect` and `hoi4.event_render` were not used.
`hoi4.probability_simulate` was skipped because no uncertain-input distribution was declared.
`hoi4.probability_sequence` was skipped because this is not a declared custom weighted pool with cadence, cooldown, recovery, cap, removal, reset, timer, and terminal-state transitions.

## Findings and recommendations

This surface is a probability-proportional two-branch random list, not an AI score race or a claim about a click probability.
The source formula has no duplicated, flat, or contradictory in-list weights; the complement is intended to make the second branch an explicit no-op.
Source-derived current stage outputs keep the incident branch below the complement branch and give it positive pressure for every valid stage, but this is not an analyzer-confirmed ranking or a balance result.
Starvation, dominance, threshold behavior, and rank reversal remain unresolved as MCP conclusions because the evaluation and sweep timed out.
Overall incident frequency, repetition across a campaign, and any snowball rate remain unresolved without successful-output cadence and eligibility-state inputs.
The source gates limit each draw to a valid provider/stage and to a clear incident/recovery state; later successful outputs can make the same family eligible again after recovery.
The current sources and D14 decision documentation agree that the correction initializes caller-owned pressure/complement temporaries without changing formula constants, weights, or incident outcomes.

No balance retuning target is recommended from this checkpoint.
Keep both caller initializations in place.
Do not infer a prepatch numeric probability from the before source because its helper-created temporaries may not survive the return to the caller.
The historical 2026-10-03 handoff recorded a prepatch inspection, but that was not a prepatch evaluate/compare baseline and this report does not claim one occurred.
This is a retrospective source comparison only; the original owner did not receive a completed before/after probability audit here.

## Remaining blockers and audit limits

The checkpoint is not a full probability audit and does not certify the complete Event 016 feature.
The Conventional weighted surface still lacks a successful probability inspection, and neither surface has a completed named-scenario evaluation, sensitivity sweep, or rendered comparison.
The Computation comparison remains pending in cell `48`.
No game-runtime observation is claimed.
No gameplay edits, tests, assets, models, index mutations, or commits were made.
No simplification was applied; the unresolved analyzer coverage is reported explicitly rather than replaced with hand arithmetic.

## Final outcome of the pending compare request

The previously pending `hoi4.probability_compare(adapter = random_list)` call completed with `tool call error: tool call failed for hoi4_agent_tools/hoi4.probability_compare; Caused by: timed out awaiting tools/call after 600s`.
The request compared the exact 1,240-character Computation dispatcher block from the immutable `f0c043037^` snapshot with the exact 1,610-character current dispatcher block at the same logical source path.
It used scenario-set id `E016_MENGELE_INCIDENT_PRESSURE_RETROSPECTIVE_2026_10_07` and requested JSON, ranking, matrix, waterfall, comparison, and unresolved outputs.
No comparison id, scenario hash, analyzer source revisions, artifact URI, ranking delta, or normalized probability result was returned.
No retry was issued, and no new MCP query was opened, in accordance with the parent checkpoint instruction.
The earlier statement that cell `48` was pending records the checkpoint state; this section records its final timeout outcome.
The audit remains incomplete and the required analyzer-derived before/after probability comparison remains unresolved.
## Bounded retry inventory and formatting checkpoint

The initial Computation `probability_inspect` on the current inline source succeeded, so no inspect retry was needed for that surface.
The Conventional `probability_inspect` full-source request timed out after 600 seconds and was retried once on the complete 940-character dispatcher block; that narrower request also timed out after 600 seconds.
The Computation `probability_evaluate` full-source request timed out after 600 seconds and was retried once on the complete 1,612-character dispatcher block with the same seven named scenarios; that narrower request also timed out after 600 seconds.
The Computation `probability_sweep` used the complete 1,612-character dispatcher block, the same seven-scenario fixture, both pressure/complement paths, 101 steps, pairwise sensitivity, and rank-reversal detection; it timed out after 600 seconds.
No Conventional `probability_evaluate` or `probability_sweep` request had been issued before this checkpoint, so there was no previous failed request to retry for those tools; those surfaces remain unresolved after the Conventional inspect timeouts.
The prior Computation comparison used seven scenarios and timed out; its one-scenario narrowed retry for `E016_VALID_STAGE_PROTOTYPE` is currently pending in execution cell `53` with JSON-only output.
All escaped-backtick sequences in this handoff were converted to actual Markdown code delimiters; the formatting scan found zero remaining escaped-backtick sequences.

## Parent continuation boundary

The parent continuation could not resume auditor handle `01a1160e-b5fa-7c41-918e-657ba7f16139`: the agent wait route returned `not_found`.
The narrowed comparison's server outcome is therefore unresolved; the missing agent handle does not establish that the server computation succeeded, failed or was cancelled.
No new incident source change is needed to install the already-committed initializers, and this checkpoint does not certify probability acceptance.
