# Event 025 active pulse settings guards

Disposition: implemented for recurring pulse hazards only; full disabled-track acceptance remains unresolved.
Acceptance basis: the user's five independently enabled evolutions with clean disabled behavior, plus specs/004 and acceptance section 6.

Nine evolution-bearing branches of `chaosx_nr25_run_bounded_pulse` use exact stage-specific `*_evolution_in_force` predicates.
Disabling a track suppresses its signal intensity/exposure growth and initialization, survivor crew burden and initialization, militarised exposure/outpost seizure, wreck decay/fragment activation, or Dependence growth/accident callback.
The other four tracks remain independently active.
The guards read activation plus the track's own settings key, not a transient evolution-log context or the highest current evolution.
They preserve historical activation flags and do not log another milestone.
Chaos thresholds remain entry gates; previously activated hazards do not require earning the same threshold again after Chaos falls.
MTTH, AI weights, hazard magnitudes, timing, and participant-registry scheduling are unchanged.

Four new tests execute the nine hazard branches from source and check independent toggles, all-disabled state, existing activated tracks below entry Chaos, original survivor profile dispatch, and complete pulse guard coverage.
The custody test interpreter now supports subtraction without breaking adjacent if/else dispatch.
All 40 Event 025 source tests pass.
The shared Deaths callback is an explicit invocation spy in the hazard tests; casualty amounts and live ledger delivery are not emulated.
Neither the scheduler nor a live game is emulated.

The direct flag/trigger syntax follows the already-read offline Data structures targeted/global flag sections and installed trigger documentation retained in the earlier callback and physical-custody handoffs.
The connected MCP reference routes and the narrower exact-section retry timed out after 600 seconds during this continuation.
No successful event/GUI/probability artifact or independent completion pass is claimed by these tests.

Changed files: the Event 025 runtime effects, evolution-gate triggers, `.tools/test_event025_active_hazards.py`, and the reused custody test interpreter.
Remaining disabled-track work includes policy/action visibility and availability, highest-stage response selection, Board art and text, aftermath activation and timed achievements, pending projects, and evolved first openings.
This pulse-only repair does not waive those requirements or approve a fallback.
