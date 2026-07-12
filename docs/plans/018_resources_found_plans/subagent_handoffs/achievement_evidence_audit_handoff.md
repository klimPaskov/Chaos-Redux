# Event 018 achievement evidence audit handoff

## Scope and audit basis

This is a read-only completion audit of the Event 018 evidence contracts for six achievements. No gameplay, localisation, registry, asset, or spreadsheet file was edited by this audit.

The audit used the complete `chaos-redux-events`, `chaos-redux-subagents`, and `hoi4-decisions-missions` skills. It checked the Event 018 achievement prompt and related specs against the live implementation, the required offline wiki pages, the official vanilla trigger/effect/script-constant documentation, and vanilla precedents for explicitly activated missions and state-control evidence.

The live tree already contains partial repairs added during this audit. The verdicts below describe that live state, not the older implementation that preceded those repairs.

## Verdict summary

| Achievement | Verdict | Evidence result |
| --- | --- | --- |
| Ten From One State | PASS | The normal capacity-deficit spawn path now latches an exact state-backed, capacity-10, non-origin, non-World-End spawn. |
| The Last Shaft Closed | FAIL | The dedicated three-anchor cleanup ledger is present, but World-End footholds can still be classified as mature regional anchors. |
| The Front Has a Floor | FAIL | Target and defender sampling are partially present, but no action-window mission is activated and the capture hook still awards from the state marker alone. |
| The Ground Is Quiet Again | PASS | The immutable Event 018 World-End super-event history flag is required, so near-global defeat classification alone cannot qualify. |
| Thirty From Below | FAIL | Only the field owner is recorded. The physical controller at Evolution IV breach is a valid candidate under the mandatory prompt and is not recorded. |
| When the Hills Begin to Move | FAIL | The required value of three raiding formations exists as a constant but is never counted or required. |

## 1. Ten From One State: PASS

### Current proof chain

`resources_found_cave_spawn_one_if_below_capacity` now does all of the following after the exact selected state calls `resources_found_cave_spawn_selected_brood_here`:

- requires `resources_found_cave_anchor_active`
- excludes `resources_found_cave_anchor_disrupted`
- excludes the cave origin
- requires `resources_found_active_anchor_capacity` to equal `constant:resources_found_achievement.full_anchor_capacity`, which is 10
- excludes `resources_found_cave_world_end`
- sets `resources_found_achievement_ten_capacity_spawn` on that exact state
- sets `resources_found_achievement_ten_from_one_state` on DHO

The achievement trigger requires the resulting DHO historical flag. Opening-emergence allocation, the direct Scree Pack release, and World-End foothold free spawns do not pass through this proof point. The evidence therefore proves that a normal brood was created from the exact active, non-origin, capacity-10 anchor before World End.

### Repair contract

No gameplay repair is required. Do not move the setter down into `resources_found_cave_spawn_selected_brood_here`, because that lower-level helper is also used by direct and World-End spawn packages.

### Required acceptance cases

- PASS: the normal deficit spawner selects an active, nondisrupted, non-origin anchor whose recorded capacity equals 10 and creates a brood there.
- FAIL: a capacity-10 anchor exists but no normal brood is spawned from it.
- FAIL: the origin creates a brood.
- FAIL: a release-raiders project creates a Scree Pack directly.
- FAIL: a World-End foothold creates its scripted opening broods.
- FAIL: the recorded anchor capacity is 9 or 11.

## 2. The Last Shaft Closed: FAIL

### What is already correct

The live implementation has the correct foundation:

- `constant:resources_found_achievement.minimum_regional_anchors` equals 3.
- Completed non-origin activation sets `resources_found_cave_mature_non_origin_anchor`.
- Cleanup grants at most one dedicated credit per state through `resources_found_mature_anchor_cleanup_credited`.
- The cleaning country receives `resources_found_mature_anchor_cleanup_contribution`.
- The achievement trigger requires that dedicated value to be at least `minimum_regional_anchors`.
- The generic `resources_found_anchor_cleanup_contribution` is no longer sufficient by itself.

Three credited state records therefore prove three distinct completed anchor activations. Origin cleanup and activating-only cleanup do not satisfy the dedicated ledger.

### Exact failure

`resources_found_cave_activate_anchor_if_ready` currently sets `resources_found_cave_mature_non_origin_anchor` on every completed non-origin activation. It does not exclude `resources_found_cave_world_end_foothold` or an active Event 018 World End. A World-End foothold can therefore enter the regional maturity ledger.

The achievement's separate non-global gate normally prevents that polluted ledger from unlocking the achievement after World End, but it does not make the evidence contract correct. Regional anchor evidence itself must never include an origin, an activating-only state, or a World-End foothold.

### Minimal exact implementation plan

1. Keep the existing state flags, dedicated country variable, and `minimum_regional_anchors` threshold.
2. In the successful activation branch of `resources_found_cave_activate_anchor_if_ready`, set `resources_found_cave_mature_non_origin_anchor` only when all of these are true:

   - the state is not the cave origin
   - the state does not have `resources_found_cave_world_end_foothold`
   - `resources_found_cave_world_end` is not active
   - the state has not already received the maturity marker

3. Keep `resources_found_record_anchor_cleanup_contribution` gated by the maturity marker and the per-state credited marker.
4. Keep the maturity marker until cleanup records its credit. Do not clear it before `resources_found_record_anchor_cleanup_contribution` runs.
5. The final trigger must continue to require the dedicated contribution count at `constant:resources_found_achievement.minimum_regional_anchors`. The generic cleanup ledger may remain for shared reconstruction and contribution systems, but it must not replace this condition.

No additional world iterator or recurring on-action is needed.

### Required acceptance cases

- PASS: one ordinary country completes cleanup in three distinct states that previously completed normal, non-origin, pre-World-End anchor activation.
- FAIL: three arbitrary cleanup projects with fewer than three mature regional anchor markers.
- FAIL: origin cleanup plus two mature non-origin anchors.
- FAIL: one activating-only state plus two mature anchors.
- FAIL: a World-End foothold plus two mature regional anchors.
- FAIL: repeated cleanup or reactivation of one previously credited state attempts to increment the dedicated ledger twice.

## 3. The Front Has a Floor: FAIL

### What is already correct

The live tree now has:

- `constant:resources_found_achievement.burrow_objective_window_days = 90`
- a target variable, `resources_found_transport_target_state`
- target markers for the transport objective, active objective, and defender-at-start fact
- `resources_found_cave_is_burrow_objective_candidate`
- `resources_found_cave_burrow_objective_context_valid`
- a real defender check through `CONTROLLER = { divisions_in_state = { state = PREV ... } }`

These are useful foundations, but the context trigger is not connected to an active mission or the state-control award path.

### Exact failures

1. `resources_found_cave_prepare_burrow_approach` is available for any enemy neighbor of any active anchor. It does not require an exact eligible Burrow objective.
2. The target predicate accepts any level of land or coastal fort. The source prompt requires a heavily fortified state when the target is neither a capital nor a supply hub.
3. The target predicate requires only adjacency to any DHO-controlled state. It does not prove adjacency to an active, nondisrupted anchor.
4. No `resources_found_burrow_objective_window_mission` exists or is activated.
5. `resources_found_burrow_objective_window_active` is referenced but never set.
6. `resources_found_record_cave_control_achievement_state` sets `resources_found_achievement_burrow_objective_captured` whenever the captured state has `resources_found_burrow_objective_active`. It does not check the 90-day window, active mission, exact stored target, defender-at-start evidence, eligibility snapshot, or World-End exclusion.
7. Retarget and defeat cleanup do not clear `resources_found_burrow_objective_defended_at_start`. There is no timeout or cancellation cleanup.

### Minimal exact implementation plan

1. Strengthen `resources_found_cave_is_burrow_objective_candidate` so one state must satisfy all of these at preparation time:

   - it is not controlled by DHO
   - it is adjacent to a DHO-controlled state with `resources_found_cave_anchor_active` and without `resources_found_cave_anchor_disrupted`
   - it is a capital, has a supply node, or has at least level 3 land or coastal fortification
   - its controller exists, is not DHO, and has at least one division in the state

   Level 3 can be expressed without an unsupported operator as `bunker > constant:resources_found_value.two` or `coastal_bunker > constant:resources_found_value.two`.

2. Add one reusable DHO-scope trigger that proves at least one exact candidate exists. Use it in both decision availability and target selection so the project cannot begin with a broader eligibility rule than the selector.
3. Before selecting a new target, call one cleanup helper that clears any previous target markers, target variable, window flag, window-duration variable, and active mission.
4. When selection succeeds, snapshot the exact start evidence on that state:

   - `resources_found_cave_transport_objective`
   - `resources_found_burrow_objective_active`
   - `resources_found_burrow_objective_defended_at_start`

   The stored `resources_found_transport_target_state` remains the exact persistent pointer. Because the selection predicate is exact, `resources_found_cave_transport_objective` is also the eligibility-at-start snapshot. A separately named eligibility flag is optional, not required.

5. Set a normal DHO duration variable from `constant:resources_found_achievement.burrow_objective_window_days`, set `resources_found_burrow_objective_window_active`, and explicitly activate `resources_found_burrow_objective_window_mission`.
6. Define the mission in `resources_found_cave_decision_category` with:

   - `allowed = { always = no }`
   - `activation = { always = no }`
   - `selectable_mission = no`
   - `days_mission_timeout` from the normal duration variable
   - cancellation when the exact target context ceases to be valid for a reason other than successful DHO capture
   - both cancel and timeout effects routed through the same cleanup helper

7. Replace the marker-only award in `resources_found_record_cave_control_achievement_state` with a success helper. In the state-control hook, qualification must require:

   - the new controller is DHO
   - the 90-day window flag and mission are active
   - the captured state's ID equals DHO's stored `resources_found_transport_target_state`
   - the exact state has all three start-evidence markers
   - Event 018 World End has not begun

   Capture the current state ID in a temporary variable before switching to DHO scope, then compare it with the stored target variable. This avoids accepting a stale marked state.

8. On success, set the historical `resources_found_achievement_burrow_objective_captured`, remove the mission, and call the common cleanup helper.
9. Call the same cleanup helper on expiry, cancellation, retarget, cave defeat, and Event 018 World-End transition. It must clear all three state markers, the stored target variable, duration variable, and window flag. The historical success flag must persist.
10. Keep the existing bounded `on_state_control_changed` route. Do not add a daily or world-wide recurring scan.

### Required acceptance cases

- PASS: an exact defended capital, supply hub, or level-3 fortified target adjacent to an active nondisrupted anchor is marked and captured by DHO inside the 90-day mission.
- FAIL: an infrastructure or railway state that is not a capital, supply hub, or level-3 fortified state.
- FAIL: a level-1 or level-2 fort that is neither a capital nor a supply hub.
- FAIL: an eligible-looking target that had no defending division when preparation completed.
- FAIL: a target adjacent only to a DHO state without an active nondisrupted anchor.
- FAIL: capture before preparation, after expiry, or after cancellation.
- FAIL: a different marked or stale state is captured during the window.
- FAIL: a World-End foothold effect supplies the capture.
- CLEANUP: success and timeout leave no active marker, defender snapshot, target variable, window flag, or mission.

## 4. The Ground Is Quiet Again: PASS

### Current proof chain

The final trigger requires both:

- `resources_found_world_end_super_event_fired`
- `resources_found_global_defeat_super_event_fired`

`resources_found_world_end_super_event_fired` is set only by `resources_found_emit_world_end_super_event`, and that effect is called only inside the verified success branch of `resources_found_cave_begin_world_end`. The flag is not set by `resources_found_classify_defeat_scale`, the cross-continent foothold test, or the 365-day consumed-continent test. It is not cleared during cave defeat.

It is therefore already an immutable historical proof that the Event 018 World-End scenario actually began. `resources_found_cave_global_defeat_eligible` alone is not enough to unlock the achievement.

The trigger also requires an ordinary-country contribution, reconstruction completion, cave defeat, global defeat aftermath, no remaining DHO-owned state, no live or pending anchor cleanup, and no cave threat source.

### Repair contract

No additional `resources_found_cave_world_end_occurred` flag is needed. Adding a second flag with the same sole setter would duplicate an already exact historical fact.

Keep `resources_found_world_end_super_event_fired` immutable and keep it in the achievement trigger. Do not replace it with `resources_found_cave_global_defeat_eligible` or the current-state `resources_found_cave_world_end` flag.

### Required acceptance cases

- FAIL: defeat is classified as global through a long consumed-continent campaign, but verified Event 018 World End never began.
- FAIL: near-global defeat and reconstruction complete without `resources_found_world_end_super_event_fired`.
- PASS: verified Event 018 World End emits its super event, the Host is later globally defeated, every territory and cleanup site is cleared, the threat source is removed, and the qualifying ordinary country completes reconstruction.

## 5. Thirty From Below: FAIL

### Adjudication

The physical controller at Evolution IV breach is a legal achievement candidate.

The story paragraph mentions the field owner, but the mandatory unlock list explicitly says the player "owned or controlled the field at Evolution IV emergence." Event 018 also distinguishes the legal owner from the physical controller at breach. The implementation must therefore support either role and must snapshot the role at breach before transfer to DHO.

### Exact failure

`resources_found_record_cave_emergence_achievement_state` records only `event_target:resources_found_cave_former_owner` and sets `resources_found_achievement_cave_former_owner`. A player who physically controlled the field at breach but did not own it can never qualify. That contradicts the explicit unlock condition.

The controller also may not have `resources_found_achievement_starting_capital`, because that variable is currently established through original field-owner registration.

### Minimal exact implementation plan

1. Add a country-scope helper named `resources_found_record_thirty_from_below_candidate`.
2. Call it from the origin state on both `OWNER` and `CONTROLLER` immediately after cave starting strength is frozen and before state transfer. Calling it twice when owner and controller are the same is harmless because its writes must be idempotent.
3. The helper must:

   - require an existing ordinary country that is not DHO
   - set a semantic role flag such as `resources_found_achievement_cave_breach_owner_or_controller`
   - copy the exact frozen `resources_found_cave_starting_divisions`
   - snapshot that candidate's capital at breach only if `resources_found_achievement_starting_capital` is missing

4. Change the achievement trigger to require the semantic owner-or-controller role flag instead of the owner-only flag.
5. Preserve the existing exact 30-division equality, survival, independence, uncapitulated, recorded-capital control, cave-defeat, and pre-global gates.
6. Update achievement localisation and `docs/achievements/018_resources_found_achievements.md` to say "owner or controller at breach." Do not retain player-facing owner-only wording.

### Required acceptance cases

- PASS: owner and controller are the same player country, starting cave strength is exactly 30, and all survival conditions are met.
- PASS: the player is the physical controller but not the legal owner at breach, starting strength is exactly 30, and all survival conditions are met.
- PASS: the player is the legal owner but another ordinary country controls the field, provided the owner meets the later survival conditions.
- FAIL: a country was neither owner nor controller at breach.
- FAIL: the cave strength was 29 or 31.
- FAIL: owner and controller being the same country causes duplicate or conflicting capital evidence.

## 6. When the Hills Begin to Move: FAIL

### Adjudication

A defined active raiding-formation count is mandatory, not optional flavour.

The achievement prompt explicitly requires "at least a defined number of raiding brood formations active." The live constant `constant:resources_found_achievement.rapid_raiding_broods` defines that number as 3. The unique package identity is the deployed Oth-Kesh Scree Pack template, which contains `cave_scree_tide_brood` battalions.

### Exact failure

The constant value 3 is unused. The release-raiders project directly creates one Scree Pack, resets the route counters, and opens the timed flag regardless of how many Scree Packs exist. State captures and country defeats increment counters without checking active Scree Pack formations. The achievement trigger checks only five states and two defeated countries.

### Minimal exact implementation plan

1. Add a DHO-scope helper named `resources_found_refresh_active_raiding_brood_formations`.
2. Reset `resources_found_active_raiding_brood_formations` to zero, then use `every_country_division` to count deployed divisions whose template satisfies `division_has_battalion_in_template = cave_scree_tide_brood`.
3. After the release-raiders project creates its Scree Pack, refresh total brood capacity, the deployed formation count, and the raiding count.
4. Start a qualifying route window only when:

   - `resources_found_active_raiding_brood_formations` is at least `constant:resources_found_achievement.rapid_raiding_broods`
   - DHO is not over `resources_found_total_brood_capacity`
   - Event 018 World End has not begun

5. Only when that gate passes, reset the five-state and two-country counters and set the 180-day route-window flag. A release action that leaves only one or two active Scree Packs may still create its unit, but it must not open or reset a qualifying attempt.
6. Add `resources_found_try_complete_hills_begin_to_move`. Call it after each qualifying state capture and country capitulation. It must refresh formation and capacity evidence, then require in the same active window:

   - at least 5 captured states
   - at least 2 defeated countries
   - at least 3 active Scree Pack formations
   - no over-capacity state
   - no Event 018 World End

7. On success, set a historical flag such as `resources_found_achievement_hills_begin_to_move_completed`.
8. Change the achievement trigger to require the historical completion flag rather than evaluating persistent counters outside the action window.
9. Expiry or a later valid attempt may clear or reset active-attempt counters and flags. Cave defeat and World End must clear active-attempt evidence. The historical completion flag must persist.
10. Update localisation and achievement documentation to state "at least 3 active Oth-Kesh Scree Pack formations". This is the mandatory package wording and should not be reduced to generic "broods" or an undefined "several."

The existing bounded state-control and capitulation hooks are sufficient. No recurring global country scan is required.

### Required acceptance cases

- FAIL: one or two active Scree Packs when the release action completes.
- FAIL: three Scree Packs exist but DHO is over brood capacity.
- FAIL: the five-state and two-country counters were accumulated across different windows.
- FAIL: the thresholds are reached after the route window expires.
- FAIL: fewer than three qualifying Scree Packs remain when the final threshold is reached.
- PASS: at least three active Scree Packs exist at attempt start and completion, DHO remains within capacity, and five states plus two country defeats are recorded inside the same 180-day window.

## Exact file ownership for the repair pass

The failing contracts can be repaired without changing the achievement registry, icons, event IDs, or adding broad on-actions.

Gameplay and tuning surfaces:

- `common/script_constants/018_resources_found_constants.txt`
- `common/decisions/018_resources_found_decisions.txt`
- `common/scripted_triggers/018_resources_found_cave_triggers.txt`
- `common/scripted_triggers/018_resources_found_achievement_triggers.txt`
- `common/scripted_effects/018_resources_found_cave_effects.txt`
- `common/scripted_effects/018_resources_found_decision_effects.txt`
- `common/scripted_effects/018_resources_found_achievement_effects.txt`
- `common/on_actions/018_resources_found_on_actions.txt`, only if the existing bounded hook call needs its called helper renamed. No new hook is required.

Player-facing and proof surfaces:

- `localisation/english/chaosx_achievements_l_english.yml`
- the Event 018 decision localisation file for the Burrow deadline mission
- `docs/achievements/018_resources_found_achievements.md`
- `docs/events/018_resources_found.md`
- the Event 018 cave-country/helper documentation that inventories these flags and variables
- the Event 018 acceptance criteria and static acceptance report

The source achievement prompt already contains the required design. It does not need a design rewrite.

## Completion gate for the parent

Do not claim the achievement package complete until every FAIL case above is repaired and the positive and negative fixtures are represented in the Event 018 acceptance evidence. Ten From One State and The Ground Is Quiet Again need verification coverage, not duplicate gameplay flags.

No fallback, simplification, asset omission, or design substitution was used in this audit.

## Closure re-audit - 2026-07-12

This section supersedes the four original FAIL verdicts for The Last Shaft Closed, The Front Has a Floor, Thirty From Below, and When the Hills Begin to Move. It records a second read-only audit of the live worktree after the parent repair pass and the final corrections made from adversarial review.

### Closure verdicts

| Achievement | Gameplay evidence | Player-facing surfaces | Closure result |
| --- | --- | --- | --- |
| The Last Shaft Closed | PASS | PASS | PASS |
| The Front Has a Floor | PASS | PASS | PASS |
| Thirty From Below | PASS | PASS | PASS |
| When the Hills Begin to Move | PASS | PASS | PASS |

No residual blocker remains for these four contracts.

### The Last Shaft Closed closure proof

The live implementation proves three distinct mature regional anchors rather than three arbitrary cleanup projects.

Positive path:

1. `constant:resources_found_achievement.minimum_regional_anchors` is 3.
2. `resources_found_cave_activate_anchor_if_ready` can set `resources_found_cave_mature_non_origin_anchor` only after completed anchor activation.
3. The maturity setter excludes the cave origin, `resources_found_cave_world_end_foothold`, duplicate maturity, and active `resources_found_cave_world_end`.
4. World-End footholds receive `resources_found_cave_world_end_foothold` before their activation begins, so the exclusion is in force at the only maturity setter.
5. `resources_found_complete_anchor_cleanup` preserves the maturity marker until `resources_found_record_anchor_cleanup_contribution` runs.
6. The recorder requires the maturity marker and non-origin status, then sets `resources_found_mature_anchor_cleanup_credited` before adding one credit to that state's cleaning owner.
7. The credited marker has no cleanup path, so one state cannot increment the dedicated ledger twice.
8. The final trigger requires `resources_found_mature_anchor_cleanup_contribution` at or above `minimum_regional_anchors`, the dedicated contributor flag, regional cave defeat, no global-defeat classification, no active, disrupted, activating, or cleanup-required cave state, and no remaining cave threat source.

Negative evidence:

- Origin cleanup never has the maturity marker.
- Activating-only states never have the maturity marker.
- Generic restoration sites never have the maturity marker.
- World-End footholds cannot receive the marker from their activation.
- Repeated cleanup or reactivation of one credited state cannot add a second dedicated credit.
- Two mature anchors plus any number of unrelated cleanup projects remain below the dedicated threshold.

The achievement's `possible` text now uses `resources_found_achievement_ordinary_defender_eligible_tooltip`, which matches the repaired trigger's ordinary-human cleaner scope and no longer claims that the player had to develop the original field.

### Thirty From Below closure proof

The live implementation accepts either the legal owner or the physical controller at breach and records both before transfer.

Scope and order:

1. `resources_found_begin_first_cave_emergence` remains in the breach state's scope.
2. It saves the pre-transfer owner as `resources_found_cave_former_owner` and keeps the state as `resources_found_emergence_state`.
3. `resources_found_calculate_cave_starting_strength` freezes `resources_found_cave_starting_divisions` on that exact state.
4. `resources_found_record_cave_emergence_achievement_state` runs after the strength calculation and before `resources_found_record_cave_origin`, the emergence choice event, and the later state transfer.
5. The recorder calls `resources_found_record_thirty_from_below_candidate` on the saved owner and on the live state `CONTROLLER`.
6. The helper sets `resources_found_achievement_cave_breach_owner_or_controller`, copies the exact frozen starting-division value, and snapshots the candidate's capital if no earlier capital snapshot exists.
7. When owner and controller are the same country, the double call is idempotent. It has no counter, writes the same strength, and does not replace an existing capital snapshot.
8. The final trigger requires the semantic owner-or-controller flag, exact equality with 30, cave defeat before global scale, existence, independence, no capitulation, control of the stored capital, and no cave-country continuation.

Negative evidence:

- A country that was neither owner nor controller receives no candidate flag.
- A value of 29 or 31 fails exact equality.
- Subject status, capitulation, stored-capital loss, or continuing as DHO fails the final trigger.
- Event 018 World End or another global-defeat-scale outcome fails the pre-global gate.

The achievement registry now uses `resources_found_achievement_breach_actor_eligible_tooltip`, whose text explicitly names the legal owner or physical controller. The earlier former-owner-only presentation mismatch is closed.

### The Front Has a Floor closure proof

The live implementation binds target eligibility, target identity, the 90-day mission, the state-control hook, and every cleanup route.

Target and start evidence:

1. `resources_found_cave_is_burrow_objective_candidate` requires a state not controlled by DHO and adjacent to a DHO-controlled active, nondisrupted anchor.
2. The target must be a capital, contain a supply node, or have at least level 3 land or coastal fortification.
3. The target controller must exist, must not be DHO, and must have at least one division in the state.
4. `resources_found_cave_has_burrow_objective_candidate` is the shared decision-availability gate.
5. `resources_found_cave_mark_transport_target` traverses a DHO-controlled active, nondisrupted anchor and selects one exact neighboring state with the same candidate trigger.
6. Selection stores `resources_found_transport_target_state` and snapshots `resources_found_cave_transport_objective` plus `resources_found_burrow_objective_defended_at_start` on the target.
7. Project completion rechecks that Event 018 World End has not begun, sets `resources_found_burrow_objective_active`, stores the 90-day duration, sets the live-window flag, and explicitly activates `resources_found_burrow_objective_window_mission`.

Exact success scope:

1. The bounded `on_state_control_changed` hook saves ROOT as the new controller, FROM as the old controller, and FROM.FROM as the changed state, then calls the state-scoped Event 018 handler.
2. The achievement helper snapshots `THIS` into the unscoped temporary `resources_found_captured_burrow_state` before entering the new-controller scope.
3. Success requires the new controller to be DHO, the live Burrow context and mission, stored target equality with the captured state, all three target markers on the previous state scope, and no Event 018 World End.
4. The context deliberately does not require the target to remain outside DHO control. That allows the post-control on-action to prove success while exact state equality and the start markers still prevent a different capture from qualifying.
5. Success sets only the historical achievement flag and then removes and clears the live attempt.

Mission lifecycle and cleanup:

- Timeout calls `resources_found_clear_burrow_objective_runtime`.
- Mission cancellation calls the same runtime cleanup.
- Explicit success calls `resources_found_cancel_burrow_objective_window`, which uses `remove_mission` and then clears runtime. Official engine documentation confirms `remove_mission` does not run completion or timeout effects, so the explicit cleanup is required and present.
- Retargeting calls the same cancel wrapper before selecting another state.
- Event 018 World End calls the cancel wrapper immediately after setting the terminal flags.
- Cave defeat calls the cancel wrapper before cave-country teardown.
- The defeat cleanup also includes a defensive state-marker sweep.

Every cleanup route clears the objective, active, and defender-at-start state flags, target and duration variables, and live-window flag. It does not clear the historical success flag.

Negative evidence:

- Infrastructure or railway status alone is insufficient.
- Level-1 and level-2 forts fail the level-3 gate.
- Undefended targets fail the controller division check.
- A target without an adjacent active, nondisrupted anchor cannot be selected.
- A wrong or stale state fails stored-state equality.
- A capture before preparation, after timeout, or after cancellation lacks the live mission context.
- World-End project completion and World-End captures are rejected and cleaned.

### When the Hills Begin to Move closure proof

The live implementation requires the Scree Tide capstone, three deployed Scree Packs, legal capacity, and one bounded capture-and-capitulation ledger.

Capstone and formation identity:

1. `resources_found_achievement_hills_move_route` now has exactly one setter, the completion reward of `DHO_the_hills_begin_to_move`.
2. Release Raiding Broods no longer sets that route flag. It can open a qualifying attempt only when the capstone flag already exists.
3. `resources_found_refresh_active_raiding_brood_formations` runs in DHO country scope and uses `every_country_division`.
4. A formation counts only when its template satisfies `division_has_battalion_in_template = cave_scree_tide_brood`.
5. The locked Oth-Kesh Scree Pack is the package containing that unique battalion identity, so unrelated broods cannot satisfy the count.

Attempt start:

1. Release Raiding Broods records whether its exact Scree Pack spawn succeeded.
2. It refreshes current division and brood-capacity totals and the deployed Scree formation count.
3. It opens a qualifying window only with the capstone flag, a successful spawn, at least `constant:resources_found_achievement.rapid_raiding_broods`, no over-capacity state, and no Event 018 World End.
4. That gate resets the state and country counters before setting the 180-day timed flag, so a later valid attempt cannot inherit an earlier ledger.

Attempt completion:

1. State-control evidence increments only while the timed route flag is active and the state has not already been credited to that attempt sequence.
2. Capitulation evidence increments only when an ordinary country capitulates to the exact DHO winner while that flag is active and the country has not already been credited to that attempt sequence.
3. Both bounded hooks call `resources_found_try_complete_hills_begin_to_move` after incrementing.
4. The completion helper refreshes live total capacity and deployed Scree formations again.
5. It requires the same active window, at least five different state captures, at least two different DHO-won country capitulations, at least three active Scree Packs, legal brood capacity, the capstone flag, and no Event 018 World End.
6. Only that block sets `resources_found_achievement_hills_begin_to_move_completed`; the final achievement trigger requires the historical completion flag and the capstone flag.

Expiry and negative evidence:

- One or two active Scree Packs cannot open the attempt.
- Three Scree Packs while over capacity cannot open it.
- Falling below three formations or becoming over capacity before the final hook prevents completion.
- Natural expiry removes the timed flag. Remaining counter values are inert, and the next valid attempt resets them.
- Thresholds split across two windows cannot latch success.
- Recapturing one state or recording a second capitulation for one country inside the same attempt cannot add duplicate credit.
- Event 018 World End and cave defeat clear the active flag and both counters.
- A pre-capstone Release Raiding Broods project may create its normal unit, but it cannot open a qualifying achievement window.

The current ledger counts different state and country identities. The attempt sequence is stored by DHO, while the last credited attempt is stored on each state or defeated country. That makes repeat hooks idempotent inside one surge without permanently excluding the same identity from a later surge.

### Final closure statement

All four repaired gameplay contracts and their player-facing eligibility/description surfaces pass this re-audit. The previous Last Shaft, Burrow, owner/controller, formation-count, capacity, capstone, and eligibility-tooltip blockers are closed.

The re-audit made no gameplay or localisation edits. It updated only this handoff. No fallback, simplification, or unreported omission remains in the four audited contracts.
