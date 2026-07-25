# Event 013 firing-path runtime audit

Date: 2026-07-11

Closure note, 2026-07-12: this is the preserved pre-fix audit. The complete group/type-preserving family pass, selected-type Disaster Barrage launch proof, explicit direct/scenario rejection notice, direct-entry history ownership, immediate exact forecast card, cluster context arrays, hard geography registry, temporary random draws, inclusive documented endpoints, and caller-side initialization for nested temporary outputs were implemented afterward. The authoritative current verdict is `docs/plans/013_natural_disasters_plans/013_event_completion_final_audit.md`; its queued live-engine scenario matrix remains open, while the Event 013 source/provenance archive was restored on 2026-07-26.

Mode: read-only gameplay audit. This handoff is the audit's only repository edit. No gameplay, localisation, GUI, asset, workbook, or existing documentation file was changed.

Line references were captured from the shared working tree during this audit; identifiers are authoritative if concurrent parent edits move a block.

## Verdict

After a successful preflight, the current non-cluster dispatcher path is scope-correct by static trace: the firing country is preserved, an exact family/state pair is proven, `chaosx.nr13.1` consumes that proof, `natural_disaster_call` accepts at least the first hit, and the state/controller queue receives matching warning and impact rows. I found no second deterministic break inside that successful entry path.

There are nevertheless three independent ways for a legitimate fire to look inert after the geography registry exists:

1. random-family preflight can false-negative and the dispatcher silently suppresses the selected event;
2. direct console execution of the hidden root has neither same-day presentation nor its own Event Log history ownership;
3. a natural-disaster cluster appended behind an already-active cluster queue loses its exact target context before its required Event 013 member runs.

The delayed worker's dynamically indexed state-scope recovery remains an explicit live-engine proof gate. The syntax is consistent with the offline wiki's array-variable rules and with existing repository usage, so I do not label it a static defect, but no runtime proof artifact exists and failure at that one line would discard every due row without executing its handler.

The currently unresolved `natural_disaster_is_family_geographically_eligible` definition is a parent-owned transient from the active geography tranche. Its four live call sites currently make target validation fail, but it is excluded from the independent finding count because the parent confirmed that its definition will land before commit.

## End-to-end trace

| Stage | Current identifiers and lines | Result of static trace |
|---|---|---|
| Automatic timer | `common/on_actions/chaosx_on_actions_system.txt:143-167` selects an id in country scope and calls `fire_event_by_temp_id`. | Event 013 begins in the human firing country's scope. |
| Cluster attempt | `fire_event_by_temp_id` at `common/scripted_effects/chaosx_settings_effects.txt:4525-4539` first calls `try_fire_event_cluster_for_selected_event`. | A successful cluster bypasses the normal `.1` branch; see finding P1-C. |
| Normal dispatcher preflight | `fire_event_by_temp_id_no_cluster` at settings effects `:4578-4586` calls `natural_disaster_prepare_random_event_fire` and suppresses dispatch when `natural_disaster_prefire_ready < 1`. | This is fail-closed, but the preflight search is probabilistic and its failure is silent; see P1-A. |
| Normal event dispatch | Settings effects `:4694-4703` meta-builds `country_event = { id = chaosx.nr13.1 }`. | `country_event` is valid in the current country scope. Regular event targets created by preflight remain available to an event fired from the same effect chain. |
| Canonical root | `events/013_natural_disasters.txt:11-54` is hidden and triggered-only. It self-preflights when no exact state/family proof arrived, consumes the state marker when one did, sets caller/policy inputs, and invokes `call_natural_disaster`. | Console `event chaosx.nr13.1 <TAG>` therefore reaches the same scheduler, but bypasses the dispatcher-owned history handler. |
| Preflight | `natural_disaster_prepare_random_event_fire` at `common/scripted_effects/013_natural_disasters_effects.txt:481-518` locks selection to the firing country, rerolls family/target at most eight times, persists the family on the selected state, and saves regular state/country/log-actor targets. | Scope transfer is correct. Coverage is not exhaustive; see P1-A. |
| Public wrapper | `call_natural_disaster` at `common/scripted_effects/chaosx_dynamic_effects.txt:569-573` calls `natural_disaster_call` and resets only inputs. | The call result outputs survive for a caller that inspects them; `.1` does not inspect or display rejection. |
| Target proof | `natural_disaster_resolve_target` at Event 013 effects `:1957-2190` resets state/country proof flags, resolves by mode, and accepts only a freshly saved state/country pair whose controller matches. | The parent's fresh-target proof closes the stale regular-event-target path. |
| Sequence plan | `natural_disaster_plan_sequence` at Event 013 effects `:2514-2627` resolves family/target per hit, records the first resolved outputs, advances the gap, and schedules only proven hits. | A preflight-proven first selected state should schedule deterministically while it remains valid in this same synchronous chain. |
| Call acceptance | `natural_disaster_call` at Event 013 effects `:2629-2707` validates, provisionally allocates an id, plans, commits acceptance only when `natural_disaster_scheduled_hits > 0`, and otherwise restores the sequence id. | Rejection is fail-closed but hidden at the canonical root. |
| Queue append | `natural_disaster_enqueue_state_job` at Event 013 effects `:1029-1065` reserves a sequence/day, appends aligned state/type/sequence/due rows to the current controller, and schedules `chaosx.nr13.2`. | State-to-controller scope and `value = PREV` are supported by current vanilla array precedents. |
| Worker | `chaosx.nr13.2` at `events/013_natural_disasters.txt:58-65` calls `natural_disaster_process_due_job` at Event 013 effects `:1171-1246`. | It finds one due row, recovers the state at `:1204-1206`, removes all aligned rows, releases the date, then dispatches by job type. See proof gate V1. |
| First visible state | `natural_disaster_execute_warning` at Event 013 effects `:1067-1085` marks the state warning-active and exposes the decision category. The first random/cluster warning is forced at `:2478-2505`. | This is a delayed decision-category signal, not an event popup. |
| Impact and report | `natural_disaster_execute_impact` at Event 013 effects `:5713-5820` applies impact and schedules report/news/follow-up. `natural_disaster_schedule_family_report` at `:4738-4748` adds another delayed job; report delivery is at `:1088-1154`. | The first family report is intentionally later than the impact. |
| Normal Event Log owner | Settings effects `:4705-4715` calls `on_repeatable_event_fired`; `common/scripted_effects/chaosx_logic_effects.txt:793-830` records history. | The normal dispatcher gets one immediate history row. Direct console `.1` does not execute this handler. |

## Findings and prioritized fixes

### P1-A: bounded random-with-replacement preflight can reject a country that has a valid pair

Evidence:

- `natural_disaster_prepare_random_event_fire` chooses a random family and tries to resolve it against the firing country inside an eight-iteration `while_loop_effect` at Event 013 effects `:481-500`.
- A failed family is simply rerolled from the same weighted stage pool. The loop does not remember families already rejected and does not prove that every stage-eligible family was considered.
- The dispatcher converts `natural_disaster_prefire_ready < 1` into `event_single_fire_allowed = 0` at settings effects `:4578-4585`.
- The on-action ignores `event_fire_dispatched` at `chaosx_on_actions_system.txt:161-167`. Because `check_event_timer` only decrements positive timers at `chaosx_logic_effects.txt:328-334`, a denied selected event leaves the timer at zero and supplies no player feedback.

Impact:

Once hard geography narrows family eligibility, a country with one or a few valid family/state pairs can miss those families in all eight draws. That is a false `no_eligible_target`, not a legitimate lack of targets. The automatic event then visibly does nothing. Direct `.1` gets a second bounded planning attempt through its self-preflight/fallback path, but it can still reject silently.

Required fix:

- Build the stage-allowed family candidate set, prove `any_owned_state` eligibility for each family, and perform the weighted choice only among families with at least one valid state; or exhaust the permitted pool without replacement before declaring failure.
- Keep strict geography. Do not substitute an incompatible family/state or widen to a world target.
- If the eligible set is genuinely empty, return an explicit preflight reason and make the event dispatcher handle the denied selection deliberately instead of silently leaving a zero timer. Whether that means selecting another event or resetting the timer is an event-system design choice, not an Event 013 fallback, and should be decided explicitly.

### P1-B: successful direct console `.1` has no same-day visible acknowledgement or history row

Evidence:

- `chaosx.nr13.1` is hidden and has only an `immediate` block at `events/013_natural_disasters.txt:11-55`.
- It unconditionally sets `natural_disaster_call_log_mode = constant:natural_disaster_log_mode.event_system` at `:53`.
- `natural_disaster_record_call_history` self-records only `event_013_history` or `scenario_history` at Event 013 effects `:621-631`; `event_system` deliberately does nothing there.
- Direct console `event chaosx.nr13.1 <TAG>` executes the event, as documented in vanilla `documentation/console_commands_documentation.md:850-854`, but does not pass through `on_repeatable_event_fired` at `chaosx_logic_effects.txt:793-830`.
- Scheduling itself creates no category flag. The guaranteed first warning is queued for impact-minus-one day at Event 013 effects `:2489-2505`; only its worker sets `natural_disaster_aftermath_category_visible` at `:1067-1085`.
- Configured first impact is 2-4 days after the call and the report is another 1-2 days later at `common/script_constants/013_natural_disasters_constants.txt:381-385`. The first popup is therefore configured for roughly day 3-6, with reservation collisions able to move it later.

Impact:

A successful console fire while paused produces no popup, notification category, or Event Log row on the call day. Looking only for an event window makes the system appear completely inert even though state variables and queue rows were created correctly.

Required fix:

- Give the direct/manual entry an explicit history owner or same-day acceptance presentation while retaining the hidden scheduler design.
- Do not simply change `.1` to `event_013_history`, because the normal dispatcher would then write a duplicate row. Use a persistent dispatcher-context proof that survives the fired event, a dedicated manual entry, or a special-case history-suppression input in the repeatable handler.
- Preserve the delayed impact. The issue is acknowledgement/ownership, not a reason to collapse the disaster timeline into a same-day impact.

### P1-C: an overlapping cluster queue loses the required Event 013 target context

Evidence:

- The natural-disaster cluster prepares the exact Event 013 target and saves `event_cluster_actor` at `common/scripted_effects/chaosx_event_cluster_effects.txt:1355-1410`.
- `can_event_cluster_fire` at `:600-680` has no `event_cluster_pending_members_active` exclusion, so a new cluster can be accepted while the country already has a pending member queue.
- `event_cluster_queue_ordered_fired_members` at `:1177-1203` persists only event ids. When a queue was already active, it appends the new batch but does not fire its first member in the current effect chain.
- Regular event targets are then lost when that chain ends. Neither the target state nor its preflight family is aligned with the pending member row.
- `event_cluster_current_member_sequence` is set to the absolute pending-array index plus one at `:1134-1155`.
- The Event 013 member consumes the exact preflight state only when that value equals one at `:1098-1126`. An appended natural-disaster batch therefore skips the exact-target branch, keeps `natural_disaster_call_target_mode = random_valid`, and can affect a random world country or reject.
- The cluster has already been recorded and marked fired at `:1456-1463`, so the outer normal `.1` path is suppressed.

Impact:

The required Event 013 member can be logged as part of a successful natural-disaster cluster but produce no visible disaster for the firing country. This survives the parent's target-proof and geography fixes because the missing data is lost one layer earlier in the cluster pending queue.

Required fix:

- Persist aligned per-member runtime context with the pending event-id array: cluster-relative logical slot, Event 013 target-state scope, target-country scope, family, and supplied proofs. Recover that row before `fire_event_cluster_member_by_temp_id`.
- Alternatively, disallow overlapping cluster queues, but that is a broader cluster-system behavior change and should not be adopted implicitly.
- Do not replace the missing target with a random world target.

### V1: dynamically indexed state-scope recovery is still an unexecuted runtime gate

Evidence:

- Queue storage uses a scope value at Event 013 effects `:1042-1046`.
- The worker scopes through `var:natural_disaster_job_target_state_entries^natural_disaster_job_index` at `:1204-1206`, then unconditionally removes the row at `:1207-1211`.
- The offline wiki, `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` under **Variables** and **Arrays**, says an array element is a variable in every regard and that `var:` is mandatory when a variable is used as a scope. Official `effects_documentation.md:2278-2291` confirms scope values in arrays.
- Vanilla has current `value = PREV/THIS` scope-array precedents, for example `common/scripted_effects/TOA_scripted_effects.txt:1295-1297` and `GER_scripted_effects.txt:1255-1257`.
- I found no current vanilla example of a *dynamically indexed* array element used directly as the left-hand scope. The repository has similar forms, including Event 014, but that is not an engine proof for this feature.
- The accepted architecture explicitly required a focused parser/runtime proof and forbade continuing if it failed at `docs/plans/013_natural_disasters_plans/013_scripted_system_architecture.md:273-285` and `:1047-1057`. `013_implementation_validation_notes.md` and `013_event_completion_final_audit.md:86-98` confirm only static review; no live worker proof is recorded.

Impact if the form fails:

If the parser rejects the scope form, the worker effect can fail to load. If it loads but the dynamic element does not resolve as a state at runtime, the worker will not save `natural_disaster_impact_state`, will still delete and release the due row, and will skip every job handler behind `has_event_target` at `:1213-1239`. Either failure mode matches "accepted and queued, then visibly nothing."

Required action:

- Execute the focused V1 scenario below before treating Event 013 firing as runtime-proven.
- If recovery fails, stop and redesign the per-country queue with an approved scope-safe mechanism. Do not substitute a global event target, fixed state list, random state, or world iteration.

### P2: the 240-day wakeup clamp can strand a later reserved row

Evidence:

- `natural_disaster_reserve_job_day` can push `natural_disaster_job_due_date` forward until a sequence/day collision clears at Event 013 effects `:949-988`.
- `natural_disaster_enqueue_state_job` stores that unbounded due date but clamps only the scheduled wakeup delay to `season_expiry_days = 240` at `:1034-1040` before scheduling `.2` at `:1060-1063`.
- If the reserved due date is later than day 240, the worker wakes on day 240, finds no `due_date <= global.date` at `:1171-1197`, removes nothing, and schedules no replacement wakeup.

Impact:

This is not a baseline `.1` cause, because the first warning/impact is well inside the window. It can strand dense maximum-barrage/report/follow-up queues or any future caller whose desired/reserved date exceeds 240 days.

Required fix:

- Either schedule the exact reserved delay without the clamp, or make the early worker explicitly schedule the next wake for the earliest future row.
- If jobs beyond season expiry are meant to be rejected or expired, do so explicitly and release all aligned data; do not leave a live row with no wakeup.

## Exact runtime scenarios

### S1 - normal dispatcher success

1. Use a firing country with at least one geography-valid populated, owned, controlled state.
2. Enter `fire_event_by_temp_id` with `event_id = constant:natural_disaster_event.id` and no cluster fire.
3. Before `.1`, require `natural_disaster_prefire_ready = 1`, both regular state/country targets, and a positive `natural_disaster_prefire_family` on the exact state.
4. After `.1`, require one accepted sequence, `natural_disaster_last_sequence_scheduled_hits > 0`, aligned controller queue arrays, and `natural_disaster_impact_scheduled` on the queued state.
5. Require exactly one immediate Event 013 history row from `on_repeatable_event_fired`.
6. Advance through the configured warning, impact, and report dates. Require warning/category state, impact damage/aftermath, then one family report.

### S2 - direct console visibility and ownership

1. While paused, execute `event chaosx.nr13.1 <eligible TAG>`.
2. Confirm immediately that a sequence and warning/impact rows were created. This separates scheduling success from presentation.
3. Confirm the current defect: no same-day popup, category flag, or Event 013 history row.
4. After the visibility/history fix, require one same-day acknowledgement or history row and still require the delayed warning/impact/report order. Execute the normal dispatcher variant and prove that it still creates exactly one, not two, Event 013 rows.

### S3 - preflight coverage, not luck

1. Select a country whose reviewed geography exposes only a small subset of the current evolution's family pool.
2. Repeat preflight from a clean state enough times to cover different random seeds.
3. If at least one family/state pair exists and no state is guarded/open, require `natural_disaster_prefire_ready = 1` every time.
4. Separately test a country with genuinely no eligible pair. Require an explicit no-target result and deliberate dispatcher handling, with no state marker, queue row, sequence consumption, or history row.

### S4 - delayed worker state recovery (V1 gate)

1. From a known state/controller pair, enqueue exactly one impact job at a one-day delay with a unique sequence id.
2. Before the worker, require all 26 aligned delayed-job snapshot arrays to have length one and the state row to equal the selected state.
3. On `.2`, require `natural_disaster_job_index = 0`, `natural_disaster_impact_state` to resolve to that exact state before removal, and all 26 arrays to return to length zero.
4. Require the reservation row to be released, `natural_disaster_impact_scheduled` to clear, and the state to enter aftermath with actual family effects. A missing target with a consumed queue row is a hard failure.

### S5 - overlapping cluster queue

1. Give the firing country an already-active cluster pending queue with at least one delayed member left.
2. Fire the natural-disaster cluster before that queue drains.
3. Require its required Event 013 member's exact state, country, family, and cluster-relative slot to persist in aligned pending context.
4. When the appended member runs, require it to use that exact pair and affect the firing country. It must not default to `random_valid` or consume another cluster's context.
5. Require one cluster record and the intended number of Event 013 member history rows, with no normal `.1` duplicate.

### S6 - far-future wakeup

1. Construct a valid sequence whose reservation ledger pushes one job beyond `global.date + constant:natural_disaster_sequence.season_expiry_days`.
2. Advance to day 240 and confirm the row is not silently left without another wakeup.
3. Require either exact later execution or explicit expiry/cancellation with aligned-row and reservation cleanup, according to the chosen policy.

## References consulted

- Required offline wiki pages: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.
- Vanilla official documentation: `documentation/script_concept_documentation.md`, `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, `documentation/console_commands_documentation.md`, `common/on_actions/_documentation.md`, and `common/script_constants/documentation.md`.
- Vanilla precedents: variable-day `country_event` at `events/WUW_Germany.txt:22845`; regular event-target event chaining at `events/Germany.txt:10270-10290`; scope arrays at `common/scripted_effects/TOA_scripted_effects.txt:1295-1297` and `GER_scripted_effects.txt:1255-1257`.
- Repository guidance: `AGENTS.md`, `chaos-redux-events`, and `chaos-redux-subagents`.

## Simplifications, omissions, and blockers

No gameplay simplification or fallback was implemented. This is a static audit; no game process was launched, so V1 and scenarios S1-S6 remain execution requirements. The current workspace also remains blocked until the parent-owned geography dispatch trigger definition is present.
