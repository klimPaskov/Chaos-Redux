# Event016 Rocketry native selection AI partial audit

Current follow-up: [the immutable-source comparison](../016_rocketry_native_ai_evidence_2026-10-07.md) supersedes this record's missing-baseline and unperformed-comparison status for fifteen declared scalar cases.
The nine repeated-state rows below remain rejected as distinct scenario evidence, and joint native-state, scope-88 and engine limits remain open.
This original audit record is preserved as dated evidence.

Date: 2026-10-07.
Authoring: parent record of the bounded `chaosx_ai_probability_auditor` return, with parent source review.
Auditor ID: `01a116da-4d33-7960-b114-3277205d2277`.
Disposition: partial source and MCP evidence retained, state-specific eligibility and before/after comparison unresolved.
Acceptance basis: the parent-owned Event016 completion audit and existing D27 policy in `agent_decisions_2026-10-04.md`.
The parent took over handoff authoring after stopping additional audit calls.
No gameplay, weight, cost, model, asset or game state changed in this audit.
This record grants no balance or full-event acceptance.

## Exact scope and source findings

The four decision IDs are `mengele_event016_native_select_flying_bomb`, `mengele_event016_native_select_jet_engine`, `mengele_event016_native_release_flying_bomb` and `mengele_event016_native_release_jet_engine`.
Their source is `common/decisions/016_mengele_native_prototype_selection_decisions.txt:59-104`, SHA-256 `6f3daf43c813c05086957225c71d90a7e35ece4808a46c34640bc25e52a3b902`.
Their wanted-source and stale-selection predicates are in `common/scripted_triggers/016_mengele_native_selection_decision_triggers.txt`, SHA-256 `1c64198fdcc8d26f770f18a0d60cfe362a8d1681a17b030e48bc54c2e3d3da67`.
The D27 change resolves to `dd10a3f3e36aa63d50a9cfd5294b75a23126bc46`, verified read-only.

The selection predicates prefer their exact project when it is being researched or completed, or when the opposite source is neither researched nor completed and its prerequisite technology gate fails.
The release predicates require the held source to be neither researched nor complete and the opposite source to be researched or complete.
Decision visibility and availability still apply separately from these scoring predicates.
No confirmed source defect was established by the bounded audit.

`common/script_constants/016_brilliant_scientist_project_constants.txt:73,76,288,290` defines suppressing factor 0, base score 10, war factor 2 and low-factory-margin factor 0.50.
For resolved source inputs, selection score is the base multiplied by its war, factory-margin and wanted-source factors.
Release score is the base multiplied by its stale-selection factor.
Both historical completions can have equal selection scores when the other modifiers match.
The audit makes no tie-break change, and distinct exact choice/eligibility behavior remains part of the uncompleted scenario evidence.
These are source expressions, not observed selection probabilities.

## Returned MCP evidence

The auditor received `PROBABILITY_SOURCE_INSPECTED` and `PROBABILITY_ANALYZED_PARTIAL` results.
The inspection covered the decision source, which also contains Cloning and Electronics controls, while the evaluation candidate pool was restricted to the four Rocketry paths.
An initial source-argument shape error was corrected and is not a service-health failure.

The narrow flying-bomb trace supplied peace, four available civilian factories and a forced-candidate override.
It confirmed base score 10, with war and caution modifiers inactive.
The wanted-source factor remained unresolved because native project research/completion and DLC/technology inputs were absent.
Provider and paid-receipt eligibility were also not validated.
No valid ranking or selection probability was established.

The aggregate evaluation used nine labels with identical peace/factory inputs and forced all four candidates in every row.
The labels included researched-source, held-selection, both-completed, invalid-provider and active-paid scenarios, but their states did not encode those distinctions.
Parent disposition: rejected as evidence for nine distinct project/provider/receipt scenarios.
Its returned partial results remain diagnostic evidence only.

Artifacts supplied by the auditor:

- Inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c236f080daeb15f5b01646c47dc9549ab26b34b546f08270d80ab8c915a27c59/f42f4edd2f852fcf0c75ef26528f627da9314acf42ee019a4dff59d18ff6235c/probability-inspect-1d5345253454.json`.
- Narrow evaluation: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/366d276331e9297f60a7f414175c3ec42cd779ef70157a0ea7a2643cea2af303/c1c0e219e0e3d1abb8684d5f2d8f8430a9432f2aab559e21a7b35aaa79ed75e3/probability-044c142f19aaf22aeb03e8a7.json`.
- Nine-label evaluation: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/56ce7df2013d6ddb5f2c2f524d4fcaedef5455d5d6b6210835fe00a24cba9c30/14aaf3e39643d382fe639e1968ad2ebd2867e65272a6095e4fc4bc7461ebe394/probability-7453d934efdb73c59b3db971.json`.

The parent verified the recorded inspect/evaluate call arguments and completed statuses from the auditor's task transcript.
The recorded render invocation failed and supplies no successful render acceptance.
No probability comparison call was performed.
The prepatch source was available as a Git object, but the audit did not prepare and validate an accepted prepatch source fixture for the compare route.
That missing comparison is an audit gap, not proof that the exposed compare route is unavailable.

## Required follow-up and limits

Complete the nine named cases only with documented, distinct native-project, technology, provider, selection and paid-receipt inputs that the live adapter actually supports.
Forced-candidate overrides cannot prove those eligibility states.
Prepare a verified immutable prepatch source fixture and compare the same complete scenarios before making a weighted acceptance claim or changing weights.
If the adapter cannot express required inputs, retain that precise coverage gap and keep any source truth-table analysis separate from MCP or engine evidence.
The current source policy is preserved without a simplification or waiver.
No model work or game launch occurred.
The full Event016 goal remains incomplete.

Skills used by the auditor: chaos-redux-subagents and chaos-redux-decisions-missions.
The parent uses chaos-redux-shared-git-commit to retain this record with the updated continuation checkpoints.
No skill was created or updated.
