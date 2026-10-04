# Event 32 probability audit handoff: evolution gates

Date: 2026-10-03.

Status: priority source baseline returned; probability analysis blocked by HOI4 MCP timeout; broad 83-scenario matrix remains unaudited.

Role: read-only `chaosx_ai_probability_auditor`.

Repository: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux`.

Workspace requested for MCP: `mod_chaos_redux_ea3b2d67c2c0`.

Parent supplied current event-trace revision: `9632ca4524ded062f0beebccbb91f0593efa38cb58d00af4b079afca066fc2ad`. This audit did not receive its own event-trace artifact or probability source revision.

## Priority baseline verdict

The five immutable snapshots under `docs/plans/032_missiles_plans/baselines/2026-10-03_evolution_gates/` are byte-identical to the corresponding current source files. The full paths, current counterparts, and SHA-256 identities are in the fixture JSON beside this report. No gate correction has been applied in those files.

The shared Event Details toggle at `common/scripted_effects/chaosx_events_log_effects.txt:2886-2904` sets or clears `events_log_disabled_evolution_[EVENT]_[TYPE]_[STAGE]`. `has_disabled_current_evolution` in `common/scripted_triggers/chaox_settings_triggers.txt:32-42` reads the same generated key. Event 32 records event id `32`, evolution types `1` through `5`, and stage `1`, so the UI keys are `events_log_disabled_evolution_32_1_1` through `events_log_disabled_evolution_32_5_1`.

Event 32 instead reads `event_evolution_disabled_32_1` through `_5`. A repository search found no `set_global_flag` or `clr_global_flag` producer for those legacy names. I counted 45 legacy read-token occurrences on 42 lines across the five Event 32 source files: operations effects 18 lines, scenario effects 14, scenario triggers 5, achievement effects 4, and missile triggers 1. The parent’s estimate of 40 should be reconciled against this path-scoped count before patching.

### EVO-10: Automatic Retaliation

The source branch in `common/scripted_effects/032_missiles_operations_effects.txt:550-613` is reached only after `missiles_program_ever_initialized` and the global guided-count variable exist. Automatic Retaliation then requires chaos at least `900` and at least two retaliation programs. Its configured delay is `missiles_evolution_timing.retaliation_days = 150`; this branch does not apply the shortening factor used by some other tracks.

`missiles_schedule_evolution_track` at `common/scripted_effects/032_missiles_operations_effects.txt:455-545` checks the legacy disable flag before setting a pending flag and due date. With the canonical UI flag set and the legacy flag absent, the source path still queues the track. The branch itself contains no `world_end` or explicit hostile-missile-pair check. Whether a caller provides either gate is unresolved because the focused event inspect timed out.

Classification: source gate mismatch is exact from the inspected definitions; campaign eligibility, caller guards, and timing distribution are unresolved. This is a scheduled due-date transition checked on later firing transactions, not a native MTTH hazard, so the source’s 150-day due date is not an exact campaign unlock date without the pulse cadence.

### EVO-11: disabled before or during pending

For each type `1` through `5`, `missiles_schedule_evolution_track` clears pending only when `event_evolution_disabled_32_N` is set. Otherwise, when the track is not unlocked and not pending, it sets the pending flag and due date. Once pending and due, it calls `missiles_record_evolution_unlock`, which checks the same legacy flag before recording.

Therefore, with only the canonical UI key set, the baseline source does not block a pre-pending schedule and does not clear a pending timer. Once the stored due date is reached and the scheduler is called again, the legacy check also permits the record path. This is an exact source-path finding, not a numeric probability result.

Expected contract from the scenario matrix: a disabled evolution has zero chance and no record. Baseline source does not satisfy that contract for the canonical UI toggle.

### EVO-12: already recorded or adopted

An already unlocked track is protected from a new pending schedule by its `missiles_evolution_<track>_unlocked` flag, so the ordinary un-unlocked path does not queue a second unlock. The record helper also refuses to set an already-unlocked track again.

The canonical toggle does not gate `missiles_evaluate_country_evolution_adoption` because that helper also reads the legacy names. No removal path was found that clears an already-applied country evolution flag when the UI toggle changes. Thus duplicate scheduling is separately guarded, while stopping later country adoption and reversing prior adoption remain unresolved behaviors that the owner should decide explicitly.

## Scenario fixture and compare readiness

The saved fixture is [032_probability_matrix_audit_2026-10-03_evolution_gate_scenarios.json](C:/Users/klimp/OneDrive/Documents/Paradox%20Interactive/Hearts%20of%20Iron%20IV/mod/chaos_redux/docs/plans/032_missiles_plans/subagent_handoffs/032_probability_matrix_audit_2026-10-03_evolution_gate_scenarios.json). It preserves `EVO-10`, the canonical-disabled EVO-10 case, and before-pending, while-pending, and already-unlocked/adopted cases for all five track types. It records exact source identifiers and threshold inputs without claiming that the MCP adapter accepted their global or country-scope bindings.

This is not yet an MCP-validated scenario set. Candidate-pool normalization is not applicable to these deterministic gate and due-date paths. The matrix’s world-end and hostile-pair conditions, global pulse cadence, due-date state, and country-scope adoption inputs are not established by an accepted probability scenario binding. Do not quote numeric chance or exact campaign timing from this fixture.

Use the same saved scenario IDs and inputs after the owner patch. Compare each preserved `before.path` in the fixture with its corresponding current `common/...` path after the patch. Do not compare the current files to themselves. The owner has not patched the source, so no after result exists yet.

## MCP evidence and exact blockers

The source-only `hoi4.probability_inspect` request for `common/scripted_effects/032_missiles_operations_effects.txt` passed the explicit workspace id but timed out with the exact service error `timed out awaiting tools/call after 600s`. It returned no adapter inventory, artifact URI, source revision, or scenario hash. Per the probability workflow, `hoi4.probability_evaluate` was not run because the required inspect result and accepted scope bindings were unavailable.

The focused `hoi4.event_inspect` trace for selector `{ kind: "event", eventId: "chaosx.nr32.1" }`, also with the explicit workspace id, timed out with `timed out awaiting tools/call after 600s`. No event graph or caller-scope evidence was returned. `hoi4.event_render` was not run without a completed focused inspection result.

`hoi4.probability_compare` is deferred until the owner applies the gate correction. There is no before/after source change to compare, and comparing these byte-identical snapshots with their current counterparts now would be a self-comparison. `hoi4.probability_render` has no analysis id to render. `hoi4.probability_sweep` was not used because the requested priority surface is a deterministic scheduled gate and the inspect route timed out. `hoi4.probability_simulate` and `hoi4.probability_sequence` were not used because no uncertain-input distribution or complete MCP-accepted cadence/state-transition manifest was available.

No probability artifact URIs, comparison ids, probability source revisions, or scenario hashes were produced. The parent-supplied event-trace revision above remains parent evidence only.

## Owner handoff

The exact candidate correction is to make each Event 32 consumer read the canonical per-type, stage-1 toggle key: `events_log_disabled_evolution_32_N_1` for type `N` from `1` through `5`. The owner must apply that mapping across operations, scenario, achievement, and trigger consumers; this auditor has not edited them. Preserve the five `before.path` files already named in the fixture for the subsequent same-scenario `hoi4.probability_compare`.

The owner should also resolve two contract edges during the patch review: whether caller-level logic guarantees EVO-10 cannot progress after `world_end` or without a hostile missile pair, and whether disabling an evolution after country adoption is meant to stop only future adoption or remove existing country flags. The current source does not prove either behavior.

## Coverage limits and remaining audit

The full 83-scenario Event 32 matrix is not complete. No normalized event-option pools, random-list outcomes, target/site score races, decision or mission AI scores, rogue incident probabilities, payload probabilities, guidance outcomes, or broad SCN-015 scenarios are covered by this priority handoff. No balance patch or balance target was chosen. Parent-reported unchanged AI weights are not a substitute for the missing probability analysis.

The source references read for this priority pass were the Event 32 probability matrix and Part 6 specification, `AGENTS.md`, the `chaos-redux-subagents`, `chaos-redux-events`, and `chaos-redux-mtth` skills, the relevant offline wiki sections in `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md`, `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`, and `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`, plus installed documentation under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`. The reference-context MCP request initially exceeded its 160-character question limit; local offline references were read directly. No web sources were used.

Only this handoff and its JSON fixture were written by the auditor. Gameplay, weights, gates, tuning, and runtime files were not edited. No game or desktop session was launched.
