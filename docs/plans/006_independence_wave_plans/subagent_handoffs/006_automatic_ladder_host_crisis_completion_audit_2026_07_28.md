# Event 006 automatic-ladder and host-crisis completion audit

> Documentation reconciliation note (2026-07-28): This focused audit remains current for the crisis source/runtime HOLDs, exact ladder, capacity fail-closed result, and queue/receipt/disclosure gaps. Subsequent documentation cleanup corrected the accepted Part 1 and tuning-matrix wording so World Collapse retains the 20-country count rather than 'doubling' an already-20 Totalen count, and marked catalog handoff v13 superseded for current counts. Use the current Event 006 source map for those reconciled wording dispositions.

Date: 2026-07-28

Scope: focused read-only completion audit of the doubled automatic ladder, the high-chaos `6002` predicate, the pre-wave crisis trigger/mission/queue/event path, current localisation, current Event 006 catalog facts, and accepted-plan disposition. This audit did not edit gameplay, localisation, assets, or the workbook.

## Verdict

**HOLD / PARTIAL.**

The exact automatic count ladder is implemented at source level as `6 / 8 / 10 / 14 / 20`, with World Collapse also at `20`. The active high-chaos `6002` predicate uses `20`, not the historical ten-country threshold. The ordinary planner and execution path require the selected count to equal the target, so the currently impossible 14- and 20-country bands fail closed instead of publishing a partial or overlapping wave.

The crisis is a real country-scoped selectable mission and not a second release system. Its source now includes the command-power affordability check, keeps the mission visible while active, serializes requests behind one global queue, rechecks the shared coordinator before execution, retries a busy coordinator for a bounded period, and delegates successful consumption to the ordinary synchronized allocator.

The crisis is not complete against the accepted specification. It does not preserve a durable success receipt or publish the requesting host and crisis cause to the Event Log. The cause flags are cleared before the queued event runs. Its player-facing text omits one accepted eligibility route and does not disclose the concrete blocked, cancelled, or timeout consequences. Queue cleanup covers every path on which `chaosx.nr6.3` executes, but there is no independent recovery owner if the scheduled requester callback is lost before execution. The accepted “remains pending” contract is also simplified to fourteen daily retries without an explicit design disposition.

## Completion status by surface

| Surface | Status | Evidence | Remaining boundary |
| --- | --- | --- | --- |
| Automatic count constants | **PASS, source** | `common/script_constants/006_independence_wave_constants.txt:35-47` defines Calm `6`, Gathering `8`, Rising `10`, Chaos `14`, Totalen `20`, and World Collapse `20`. | No live band execution is proved. |
| Planner count capture | **PASS, source** | `common/scripted_effects/006_independence_wave_package_planner_effects.txt:19-59` captures the six constants by chaos band. `common/scripted_triggers/006_independence_wave_triggers.txt:572-599` uses the same constants for capacity preflight. | The static audit is not synchronized engine evidence. |
| Exact-count allocation and upper-band failure | **PASS, fail-closed** | `common/scripted_effects/006_independence_wave_package_allocator_effects.txt:79-132` publishes `independence_wave_plan_contribution_ready` only when selected count equals target and otherwise records `insufficient_pool`. `common/scripted_effects/006_independence_wave_execution_effects.txt:15-26` rejects a count mismatch again before execution. | Only eleven package IDs across ten compatible reservation groups are attested. The 14- and 20-country bands have no current capacity route. |
| `6002` high-chaos threshold | **PASS, active source; HOLD reachability** | `common/script_constants/006_independence_wave_super_event_constants.txt:19` sets `exact_high_chaos_wave_count = 20`; the predicate consumes it at `common/scripted_triggers/006_independence_wave_triggers.txt:262-268` and the transaction evaluator consumes it at `common/scripted_effects/006_independence_wave_super_event_effects.txt:30-45`. | The 20-country predicate is unreachable from the admitted pool, and predicate playback remains unproved. |
| Crisis thresholds and scope | **PASS, source; PARTIAL player description** | `common/scripted_triggers/006_independence_wave_crisis_triggers.txt:10-31` implements stability below `0.35`, an enemy-controlled owned state above `50` resistance, or a controlled foreign-owned state above `50` resistance. This matches the accepted scope in `006_independence_wave_spec_part_2_event_flow_and_evolutions.md:35-41` and Part 3 at `:9-13`. | The Event Details and crisis-category text describe only controlled foreign-owned resistance, so the enemy-controlled owned-state route is undisclosed. |
| Crisis opening gate | **PASS, source** | `common/scripted_triggers/006_independence_wave_crisis_triggers.txt:34-47` rejects `world_end`, pending joint presentation, pending Event 005 opening presentation, non-reset coordinator state, active/cooldown country state, and an occupied global crisis queue. No world-wide periodic on-action was added. | Country-scope evaluation needs live visibility and save/load proof. |
| Crisis cost and mission visibility | **PASS after bounded source repair; HOLD runtime** | `common/scripted_triggers/006_independence_wave_crisis_triggers.txt:49-52` now requires the standard security cost plus command power. `common/decisions/006_independence_wave_crisis_decisions.txt:15-32` and `common/decisions/categories/006_independence_wave_crisis_categories.txt:10-15` keep the mission/category visible while active and provide the 120-day selectable mission, cancellation, and timeout path. | No live affordability-boundary, AI choice, timer, cancellation, or timeout scenario exists. |
| Crisis queue and consumer | **PARTIAL** | `common/scripted_effects/006_independence_wave_crisis_effects.txt:81-92` creates one global queue, marks the requesting country, initializes retry state, and schedules `chaosx.nr6.3`. `events/006_independence_wave.txt:69-132` consumes the queue only after the normal release barrier passes, retries a busy barrier daily, clears on success or retry exhaustion, and delegates only to `independence_wave_prepare_and_execute_standalone_incident`. | The bounded retry limit is `14` at `common/script_constants/006_independence_wave_crisis_constants.txt:29-32`, whereas the accepted plan says a busy crisis remains pending. No explicit plan disposition authorizes the fourteen-day cutoff. |
| Queue cleanup and lifecycle | **PARTIAL / BLOCKED evidence** | The event clears the global queue on successful barrier admission, retry exhaustion, and an executing callback that no longer has a requester flag. No direct state mutation or duplicate queue writer exists. | The global queue has no timed global flag, global event target, reset hook, death/annexation recovery, or independent on-action owner. If the requester-scoped scheduled event is lost before it executes, the global flag can remain and prevent all later crises. If the queue is cleared before the callback, the requester flag and retry variable are not cleaned by the empty path. Live death, annexation, save/load, and stale-flag evidence is missing. |
| Crisis receipt and Event Log | **MISSING accepted requirement** | The mission records `independence_wave_crisis_occupation_origin` and `independence_wave_crisis_stability_origin` at `common/scripted_effects/006_independence_wave_crisis_effects.txt:23-31`. | `independence_wave_clear_crisis_runtime` clears both causes at `:42-46` before the queued event. No durable success receipt, requesting-host pointer, crisis-specific Event Log writer, actor mapping, detail/evolution payload, or localisation was found. This misses the accepted requirement at `006_independence_wave_spec_part_2_event_flow_and_evolutions.md:39` and Part 3 at `:13`. |
| Crisis failure presentation | **PARTIAL** | Source consequences exist at `common/scripted_effects/006_independence_wave_crisis_effects.txt:48-79` and `:113-118`: blocked resolution applies stability, war-support, and resistance changes; cancellation applies stability loss and cooldown. | No crisis event or explicit mission tooltip exposes the actual blocked/cancelled/timeout deltas. `independence_wave_crisis_blocked` and `independence_wave_crisis_abandoned` have no scoped player-facing resolution or Event Log consumer. |
| Localisation | **PARTIAL** | The category, mission, cost, and Event Details keys exist at `localisation/english/006_independence_wave_decisions_l_english.yml:230-234` and `localisation/english/chaosx_gui_l_english.yml:953`. The static ladder and controlled-foreign-state/stability thresholds agree with source. | The cost phrase can render “falls by -5%”; `shared allocator` is implementation language; the accepted enemy-controlled owned-state entry route is absent; and actual failure/cancellation consequences are undisclosed. |
| Current event documentation | **PASS for capacity reconciliation; PARTIAL accepted-spec cleanup** | `docs/events/006_independence_wave/overview.md:39,124,247`, `006_source_of_truth_map.md:157-158,278-281,377`, and `006_independence_wave_resume_packet.md:164-167,278-281` now state that 6/8/10 are only conditionally viable and 14/20 have no admitted capacity route. | The prior audit snapshot found a stale World Collapse “doubles” phrase; the documentation reconciliation corrected the accepted core spec and tuning matrix to retain the 20-country count. Crisis success-receipt/Event Log requirements still have no implementation disposition. |
| Catalog | **PASS for latest Event 006 static row; PARTIAL whole-event alignment** | Read-only workbook inspection confirms `Events!C7` and the exported Events CSV contain `6/8/10/14/20`, World Collapse `20`, and the current crisis sentence. Event 006 and Liberations remain `In progress`; SCN-008 remains `Needs Testing`. Dynamic rival-bloc suffixes are intentionally not flattened into the static workbook summary. | `Scenarios!C9` and the scenarios CSV still say “Every researched Event 6 independence movement,” while `006_independence_wave_scenario_l_english.yml:14` says “Every researched independence movement.” `006_catalog_alignment_v13_2026_07_28.md:19` retains a stale `3/4/5/7/10` claim, but its new superseded notice now prevents it from being routed as current catalog authority. |
| Crisis assets | **PASS for this tranche** | The mission reuses registered `GFX_decision_independence_wave_border_arbitration` from `interface/006_independence_wave.gfx:52`; its DDS is listed as final in `docs/assets/006_independence_wave/manifest.md:88`. The accepted host-crisis report image is produced and registered as `GFX_report_event_006_asset_002_host_crisis`. | The missing crisis receipt/Event Log/event presentation is a wiring and design gap, not a missing bitmap for this mission. Whole-event country portrait and identity-asset admission gaps remain separate blockers. |

## Exact count and fail-closed result

The focused allocator audit passed with:

- 149 publishers;
- 126 automatic/high-chaos selectable packages;
- 138 SCN-008 ranked selectable packages;
- eleven attested package IDs across ten compatible reservation groups;
- the bounded IW-008 RHI / IW-010 AJX capacity-two exception with distinct anchors `51` and `42`;
- automatic counts `6 / 8 / 10 / 14 / 20`, with World Collapse `20`;
- anchor, compact, extended, then lock order;
- Event 005 reservations before Event 006 reservations in a joint transaction.

The lower three counts have static capacity paths only. They remain runtime-held by live host, anchor, Event 005 collision, force, reservation, lock, rollback, and save/load gates. The 14- and 20-country counts are design targets with no current admitted capacity path. They fail closed at capacity/preflight and allocation rather than releasing a reduced wave.

## High-chaos super-event threshold

No active gameplay threshold of ten remains for the wave-based `6002` predicate. The current spec, super-event research, prompts, constant, trigger, and evaluator use twenty.

`docs/plans/006_independence_wave_plans/subagent_handoffs/006_super_event_6002_architecture_2026_07_16.md` still contains ten-country wording in its historical audit body at lines `36`, `94`, `98`, `125`, `259`, and `401`. Its header at lines `7-19` explicitly marks the audit resolved and the body historical/superseded. Those occurrences are trace evidence, not an active threshold. They should remain classified as historical rather than being cited as current implementation authority.

## Crisis transaction trace

The source transaction is:

1. A country exposes the category through low stability, enemy occupation of an owned high-resistance state, or its control of a foreign-owned high-resistance state.
2. The opening gate requires a reset Liberations coordinator and no world-end, presentation, cooldown, active-mission, or crisis-queue conflict.
3. Selecting the mission pays manpower, army experience, command power, infantry equipment, support equipment, and stability, then stores cause flags.
4. Cancellation when pressure disappears applies the cancellation consequence and cooldown.
5. Timeout while pressure persists creates the one global queue and schedules `chaosx.nr6.3` in the requesting country.
6. `chaosx.nr6.3` rechecks the full release barrier. A busy barrier receives up to fourteen daily attempts; successful admission clears the queue before calling the ordinary standalone planner; exhausted retry records a blocked consequence and clears queue/requester state.
7. A committed ordinary incident opens the normal Event 006 presentation. A failed allocator applies the crisis blocked consequence. No crisis code changes ownership directly.

This trace proves single-queue serialization and ordinary-planner delegation. It does not prove requester survival, save/load persistence, a durable crisis receipt, or Event Log attribution.

## Accepted-plan disposition

| Requirement or artifact | Disposition |
| --- | --- |
| Earlier `3/4/5/7/10` automatic ladder | **Superseded.** Current spec, constants, planner, Event Details, and workbook row use `6/8/10/14/20`. Historical audits may retain dated evidence but must not be routed as current. |
| Exact `6/8/10/14/20`, World Collapse `20` | **Implemented at source; runtime HOLD.** Counts are consistent through constants, tuning capture, capacity capture, static audit, and Event Details. |
| 14- and 20-country operational waves | **Accepted design, blocked implementation capacity.** No fallback is authorized; current source correctly fails closed. |
| Twenty-country `6002` wave predicate | **Implemented source, unreachable from admitted pool.** No active ten-country threshold remains. |
| `006_pre_wave_crisis_and_doubled_ladder_2026_07_28.md` | **Partly implemented evidence.** It correctly records the count and ordinary-planner delegation, but it overstates completion because the accepted crisis receipt/Event Log contract is absent and live queue evidence is missing. |
| Busy crisis remains pending | **Simplified without explicit disposition.** Source uses a centralized fourteen-day retry limit, then blocks the crisis. Parent must accept the bounded cutoff or align it with the accepted pending contract. |
| Crisis host/cause receipt and Event Log entry | **Missing.** Cause flags are transient and cleared; no current log/detail/localisation surface consumes them. |
| Current capacity documentation | **Reconciled.** Canonical event, source-map, and resume documents now say the RHI/AJX exception enables exact ten only and that 14/20 have no admitted capacity route. |
| `006_catalog_alignment_v13_2026_07_28.md` | **Superseded current-state claim.** Its row/export evidence is useful, but its stated `3/4/5/7/10` ladder is explicitly superseded by the dated notice and current source map. |

## Meaningful validation and limits

- Ran `python -B .tools/audit_event6_allocator.py`; it passed with the counts and pool figures recorded above.
- Traced every non-document writer and clearer of `independence_wave_crisis_release_queued`, `independence_wave_crisis_release_requester`, and `independence_wave_crisis_retry_count`. Only the crisis effect creates the queue, and only `chaosx.nr6.3` clears the global queue.
- Compared the crisis trigger, effects, decision, category, event consumer, and localisation against the accepted crisis clauses in Event 006 spec Parts 2 and 3.
- Inspected the workbook read-only and compared `Events!C7`, `Scenarios!C9`, and the exported CSV text with current localisation.
- A narrow `hoi4.event_inspect` pass for `chaosx.nr6.3` returned partial inspection artifacts with no blocking diagnostic, but the workspace-size limit deferred helper projection and lifecycle analysis. The state-flow artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2afd2a0605f2122402941c6c1eb9efce64f00929f7bc9e7da35bfc13046c7e8e/665b10bf8b16a3afbfa44d7fcae13e00a67cf010f1fb4dec13e5ac3062864820/event-state_flow-246b0ed54c04.json`. It is not queue-cleanup proof.
- No game or runtime consumer was launched. Mission timing, AI selection, requester death, annexation, save/load, busy-coordinator retries, exact-count allocation, rollback, Event 005 collisions, and presentation playback remain untested.

## Remaining blockers and recommended next actions

### Latest tranche

1. Decide whether the accepted busy-coordinator behavior is indefinite pending or a fourteen-day retry. Record the decision in the spec and player-facing text before treating the queue as complete.
2. Add or explicitly reject the accepted durable crisis-success receipt and host/cause Event Log contract. A complete implementation needs a persistent generation-safe host/cause record, actor mapping, log/detail wording, and cleanup ownership.
3. Give the global queue an independent recovery owner or prove that a requester-scoped delayed country event always executes after annexation, tag death, and save/load. Cover lost requester, missing requester flag, stale global queue, world-end transition, pending presentations, and retry exhaustion.
4. Expose both accepted resistance entry routes and the real blocked/cancel/timeout consequences in player-facing localisation. Correct the signed stability-loss display and remove implementation language.
5. Correct or supersede the stale `3/4/5/7/10` assertion in catalog handoff v13, align `Scenarios!C9` with current scenario localisation, and export from the workbook source.
6. Keep 14/20 and the wave-based `6002` predicate fail-closed until at least the required complete package and compatible reservation capacity exists. Do not promote registered-but-unattested packages to fill a count.
7. Record live 6-, 8-, and 10-country ordinary transactions, both RHI/AJX orders, same-GER-host protected-remnant cases, Event 005 collisions, late invalidation, rollback, repeat firing, and save/load before calling even the lower bands operational.

### Whole Event 006

- The current whole-event authority remains `006_event_completion_audit_v31_2026_07_28.md`, with **HOLD / PARTIAL** unchanged.
- Only eleven of 206 package rows are content-attested. The remaining package, route, research, portrait, exact-symbol, and formable dispositions are incomplete; 14/20 capacity cannot close without additional fully audited packages.
- The restored shared-focus baseline still has fourteen blocking geometry diagnostics. Generic meaningful-tree insertion remains fail-closed, and focused runtime visibility for imported shared focuses is missing.
- IW-012 is statically admitted, but live release, focus visibility, AI activation, force materialization, and rollback evidence remains absent. The current country audit also reports a hard-coded `DEN` AI diplomacy target despite the persisted former-host scope, and the route-AI addendum remains unresolved.
- The 32-cell SCN-008 mode/intensity runtime matrix, collision sweeps, determinism, cleanup, save/load, achievement interaction, and balance evidence remain open. Its catalog status must remain `Needs Testing`.
- AI and balance still lack representative released-state, host, neighbor, patron, league, radical-route, spending-safety, war-restraint, and long-horizon survival evidence.
- Super-event `6002` has source, art, audio, predicates, and FIFO wiring, but its twenty-country and hidden-formable routes remain unreachable and playback is unproved. Super-event `6001` remains blocked by exact-recording rights, with no fallback authorized.
- Sixteen achievement definitions and their icon states exist, but runtime reachability, persistence, save/load, and blocked-route matrices remain incomplete.
- Grounded country portrait and identity admission remains partial for unadmitted packages. The crisis tranche itself has no new bitmap blocker because it reuses final registered assets.

## Audit file record

Changed file: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_automatic_ladder_host_crisis_completion_audit_2026_07_28.md` only.

No gameplay, localisation, interface, asset, workbook, or CSV file was edited by this audit. No simplification or fallback was approved by this audit.
