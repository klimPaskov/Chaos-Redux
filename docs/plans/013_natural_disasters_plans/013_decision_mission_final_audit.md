# Event 013 decision and mission final re-audit

Final re-audit snapshot: 2026-07-10 03:57 Europe/Kyiv, after the deadline, queue-transfer, due-day, and controller-responsibility fixes.

Audit mode: gameplay and localisation were read-only. This report is the auditor's only edit. The bounded surface was the two former P1 blockers, the ownership/controller recovery path, and parser/scope risk in the replacement logic.

## Verdict

**Clean for the bounded re-audit.** No P0, P1, P2, or P3 findings remain on the audited decision/mission deadline, transfer lifecycle, or current-controller recovery surfaces. The two former P1 blockers are closed. No fallback or design simplification was used, and no further improvement-loop planning pass is required for these fixes.

## Severity-tagged findings

**None.**

## Closure evidence

### Exact typed-mission deadline

- `natural_disaster_activate_family_chain_mission` derives its extension from the persisted state due date as `due date - global date - 2` at `common/scripted_effects/013_natural_disasters_effects.txt:3482-3484`. The former 180-day upper clamp is absent; only negative extension is floored to zero at `:3485-3487`.
- Every typed mission has the one-day base timeout declared by `@ND_CHAIN_MISSION_BASE_DAYS = 1` at `common/decisions/013_natural_disasters_decisions.txt:24`, with the seven mission definitions at `:6113`, `:6195`, `:6277`, `:6359`, `:6441`, `:6523`, and `:6605`.
- For a reserved due date `D` days away, the active timeout is therefore `1 + (D - 2) = D - 1` days. Reservation collisions can extend `D` without truncating the mission extension, so the objective remains exactly one day before the actual reserved due date.

### Pending-job transfer and due-date preservation

- The control-change on-action preserves the documented `ROOT` new-controller, `FROM` former-controller, and `FROM.FROM` state layout at `common/on_actions/013_natural_disasters_on_actions.txt:14-29`.
- `natural_disaster_transfer_pending_jobs_for_state` scans the former country's queue at `common/scripted_effects/013_natural_disasters_effects.txt:3925-3976`. A match captures the type, sequence id, and due date from the same dynamic index, removes that index from all four aligned arrays, and appends the unchanged state, type, sequence id, and due date to the new responsible country at `:3935-3960`.
- A matched row does not increment the loop index, so the row shifted into the removed index is checked next; only a non-match increments the index at `:3967-3970`. This migrates every queued row for the transferred state without skipping adjacent matches.
- The helper does not call the reservation release or reservation allocation effects. The global sequence/day reservation therefore remains singular and unchanged.
- The new worker delay is `persisted due date - global date`, with only an already-overdue result floored to zero at `:3950-3955`. A due-today row retains `days = 0` at `:3962-3965`, which is explicitly supported by the official `country_event` effect and has a vanilla on-action precedent in `common/on_actions/06_bftb_on_actions.txt:11`. A future row wakes after its exact remaining delay; an overdue row wakes at the earliest supported time.

### Current-controller recovery responsibility

- The transfer handler accepts either ownership or control by the new responsible country at `common/scripted_effects/013_natural_disasters_effects.txt:4163-4170`, migrates the former country queue and pointers at `:4172-4177`, and registers the state to the new country at `:4179-4180`.
- The new responsible country receives warning/category state, the active-card array, recovery idea, priority mission refill, any still-live typed chain mission, and abnormal-card array/flags at `common/scripted_effects/013_natural_disasters_effects.txt:4109-4161`.
- Decision targeting is controller-based throughout: all 104 `state_target` declarations in `common/decisions/013_natural_disasters_decisions.txt` are `any_controlled_state`, and no recovery target uses `any_owned_state`, `is_owned_by = ROOT`, or `is_owned_and_controlled_by = ROOT`. Warning and aftermath action targets also require `is_controlled_by = ROOT`, beginning at `:3034`.
- Category visibility and state mission-slot lookup use controlled states/current `controller` at `common/scripted_triggers/013_natural_disasters_triggers.txt:154-197`; warning actions require current control at `:391-396`.
- Priority selection, capacity pressure, and phase refill use controlled states/current controller at `common/scripted_effects/013_natural_disasters_effects.txt:705-789`, `:3255-3321`, and `:3418-3462`. Initial queue ownership is assigned through the state controller at `:965-1003`; aftermath registration uses the state controller at `:4208-4257`; repeated-impact notification/refill uses it at `:5048-5052`; abnormal-card registration and notification use it at `:6313-6355`.

### Parser and scope review

- Dynamic array element access and removal indices are supported. The offline Data Structures reference defines zero-indexed `array^index` access and variable indices; vanilla uses dynamic `index = i` removals in `common/on_actions/13_goe_on_actions.txt:217`, `:229`, and `:234`, and dynamic `array^i` reads/writes in `common/scripted_effects/operation_strat_effects.txt:183-218`.
- The four migration payload variables and the loop index are temporary variables, so they remain unscoped while the effect enters `event_target:natural_disaster_new_responsible_country`; no invalid `ROOT.temp`, `PREV.temp`, or equivalent scoped temporary reference is used.
- `is_owned_by` and `is_controlled_by` are evaluated in state scope. Event targets are valid country targets for both forms, with vanilla precedents including `events/MTG_USA.txt:2498` and `common/ai_strategy/HOL.txt:281`.
- Every audited `controller = { ... }` recovery block is entered from a state scope. The resulting country scope matches the required scopes of mission activation, country flags, country arrays, category ideas, and queue worker events.

## Simplifications, omissions, and blockers

None within the bounded re-audit. This verdict does not replace broader Event 013 completion audits outside the two former P1s and the named ownership/controller recovery surface.

Skills used: `chaos-redux-subagents`, `chaos-redux-events`, `hoi4-decisions-missions`, and `chaos-redux-improvement-loop`. No skill was created or changed.
