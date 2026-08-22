# Event 006 manual-entry no-countries audit — 2026-08-21

## Audit status

**PARTIAL / ENGINE-STATE UNRESOLVED.** I found no remaining concrete source defect that proves why a current direct `chaosx.nr6.1` invocation would release zero countries after the capital-scope, dormant empty-shell, existing-shell execution, and allocation-attestation repairs.

The current source has a statically viable standalone path and a 20-package admitted witness. The observed zero-country result can still arise from a world-state-specific empty eligible pool, a pre-mutation transaction rejection, or an execution failure followed by compensating rollback, but the supplied evidence contains no terminal receipt values that distinguish those cases. Source review alone cannot prove which engine stage occurred.

No gameplay file was edited.

## Exact source findings

### Manual entry and transaction envelope — source-complete

- `events/006_independence_wave.txt:11-63` defines `chaosx.nr6.1` as a hidden triggered country event. A valid committed joint delivery is presented first; otherwise the event clears an orphaned joint-presentation marker and calls `independence_wave_prepare_and_execute_standalone_incident`. `chaosx.nr6.2` is fired only after `independence_wave_standalone_incident_committed` is present.
- `common/scripted_effects/006_independence_wave_execution_effects.txt:840-923` opens a standalone Event 006 plan, enters allocation, allocates, expands optional territory, executes only a ready contribution, classifies the terminal state, and snapshots a diagnostic receipt.
- `common/scripted_triggers/chaosx_liberation_release_triggers.txt:50-74` permits a new plan when the shared coordinator is absent, idle, committed, or aborted. A prior committed wave therefore does not by itself block a repeat manual entry.
- An in-progress joint plan, rollback failure, or finalization failure intentionally blocks a second transaction. The standalone stale-plan reset at `common/scripted_effects/006_independence_wave_execution_effects.txt:805-833` is deliberately limited to pre-execution Event 006-only plans. No evidence supplied for this audit shows that such a shared-coordinator state was present when the symptom occurred.

### Allocator and planner — statically viable; runtime eligibility unresolved

- `common/scripted_effects/006_independence_wave_package_planner_effects.txt:19-59` always publishes a positive target count. With no `chaos_tier` flag, the direct manual path defaults to calm-world count 3; the accepted ladder is 3/4/5/7/10 in `common/script_constants/006_independence_wave_constants.txt:62-74`.
- `common/scripted_effects/006_independence_wave_package_planner_effects.txt:484-700` begins every candidate at weight zero and grants positive base/minimum weight only inside the exact runtime content-attestation gate. The formerly misplaced minimum clamp is now inside that gate at lines 689-699.
- `common/scripted_effects/006_independence_wave_package_planner_effects.txt:95-150` increments the attempt count only for attested anchor-phase candidates, matching the repaired weight contract.
- `common/scripted_effects/006_independence_wave_package_allocator_effects.txt:15-77` recomputes all fourteen region totals before each draw and explicitly sets `independence_wave_plan_pool_exhausted` when the total is zero. Lines 79-151 either freeze the requested count, accept a positive partial count after genuine pool exhaustion, or fail closed before ownership mutation.
- `.tools/audit_event6_allocator.py` passed on the current tree: 149 publishers, 126 automatic/high-chaos-selectable packages, 32 attested packages, 29 compatible reservation groups, and a static standalone witness of 20 admitted packages with protected former-host states. The current default target of 3 is therefore statically satisfiable. This audit does not simulate the user's actual ownership, controller, living-tag, origin, reservation, or anchor state.

The probability audit confirms that the allocator's outer `random_list` is structurally complete: 14 region candidates and 14 dynamic required inputs, with `poolComplete = true`, source revision `fd5dc6ea1a576a2ef01c47f07b83a4ab7603bb81eef8d9300c9504b1bcb9cf64`, and source hash `9cab0bffea71b78719b2c8634363338e9f12e4d214de1603dc0f9b6b24ef72b9`. Region 01 and Region 02 also returned complete nine-candidate pools with zero unresolved entries. MCP could not evaluate a nonzero probability because all weights are effect-derived and no typed world-state scenario was supplied. The evidence rules out a missing outer pool entry; it does not rule out all runtime candidates becoming ineligible.

### Dormant carriers and package dispatch — repaired source is coherent

- `common/scripted_triggers/006_independence_wave_package_triggers.txt:20-69` now accepts either an absent tag or an existing shell with zero owned states and no controlled states, while excluding living, prepared, committed, Soviet-origin, and Event 012 carriers. It uses documented `num_of_controlled_states > 0`, not the invalid `num_controlled_states` variable.
- `common/scripted_effects/chaosx_liberation_release_effects.txt:1044-1168` validates every country row and, at lines 1092-1110, rejects an existing target only when it is Event 005-owned or fails the Event 006 dormant-shell predicate. The previous blanket rejection of existing shells is absent.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:9-202` separates runtime adapters from the compile-time content-attestation set. Lines 204-401 require the dormant carrier, adapter, attestation, origin safety, and exact package/tag proof before execution.
- `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:13-89` dispatches package setup and final validation through the admitted regional adapters and retains the common focus/AI barrier.
- The Banat, Thrace, and Epirus pre-release exact-package gates use fixed state 82/184/185 plus explicit ROM/GRE ownership checks at `common/scripted_triggers/006_independence_wave_banat_package_triggers.txt:14-21`, `common/scripted_triggers/006_independence_wave_thrace_package_triggers.txt:14-21`, and `common/scripted_triggers/006_independence_wave_epirus_package_triggers.txt:14-21`. None dereferences a dormant country's `capital_scope`.

### Instantiation, transfer, and rollback — no provable remaining source defect

- `common/scripted_effects/006_independence_wave_execution_effects.txt:348-451` temporarily limits release cores to the frozen package. Absent tags are released by the former host; existing dormant shells skip the engine `release` no-op and are counted as instantiated before the state-transfer formation step.
- `common/scripted_effects/006_independence_wave_execution_effects.txt:453-506` requires every selected carrier to exist, then transfers each frozen state and verifies both ownership and control.
- `common/scripted_effects/006_independence_wave_execution_effects.txt:680-797` locks and revalidates metadata, relocates endangered host capitals, begins execution, instantiates, transfers, validates frozen ownership, finalizes packages, and commits. A failure while still executing is deliberately exposed as `independence_wave_execution_failed`.
- `common/scripted_effects/006_independence_wave_execution_effects.txt:896-907` sends a post-mutation execution failure through the shared compensating rollback. A completed rollback would leave zero newly released countries even though the allocator had selected candidates.
- `common/scripted_effects/chaosx_liberation_release_effects.txt:1483-1552` relocates a host capital only if its current capital is in the frozen transfer rows, and verifies the protected state before execution. The static allocator witness found protected remnants for every witness host. No runtime host-capital receipt was supplied.

## Likely failure stage

The symptom **does not identify one exact stage**.

1. If `independence_wave_terminal_receipt_cancelled_before_mutation` is set, the failure was before release: most plausibly no eligible weighted candidate in the actual world state, a shared-coordinator state that refused the new plan, frozen metadata rejection, optional-expansion failure, or protected-capital preparation failure.
2. If `independence_wave_terminal_receipt_rolled_back_after_mutation` is set, carriers were selected but instantiation, transfer, or frozen-ownership verification failed and the transaction intentionally restored the map.
3. A finalization failure is less consistent with literally zero countries because finalization begins only after frozen ownership matches and the finalization-failed path does not run compensating rollback.

The missing discriminator is the current engine receipt written at `common/scripted_effects/006_independence_wave_execution_effects.txt:18-199`: terminal flags plus `global.independence_wave_terminal_receipt_phase`, `last_failure`, `target_count`, `selected_count`, `attempt_count`, `expected_state_count`, `instantiated_count`, `transferred_state_count`, `prepared_count`, `activated_count`, `validated_count`, and `initialized_count`. No values from the failing invocation were available to this audit.

## MCP status and limits

- Fresh `hoi4.event_inspect` lint for `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL` at revision `bc0062fc8506bf5505d078e07d30ec754f89ff356b2b63f89df990e808aa23b`, graph hash `b1d3bee3988caf66732214ea0c5dade1d84fbeeefe8d3c2cab0d2be636205e18`, with zero blocking diagnostics. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c39950b524584050d039f0a412514d02c6721ab988f1bda227b9e01393d6b026/204de3d3fc38cc063b04ae2111e6b103cfad746d403e175c072d38c533212e6f/event-lint-bc0062fc8506.json`.
- Focused state-flow inspection for the actual receipt variable `global.independence_wave_terminal_receipt_instantiated_count` also returned `EVENT_INSPECTED_PARTIAL`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/111e892005f1fc9e0c0f0b58f6e26e01ca093e292dd1e082d0a66c32b9567af8/226e53caa3b4fc8fdcfd76586fb8a599c7f5f9cc0e0ca357249d4660de5fe343/event-state_flow-bc0062fc8506.json`.
- `hoi4.event_render`, state view, returned `EVENT_RENDERED_PARTIAL` at the same revision. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cb5a1144ef41fd9bd24a9a660974be66632de594b1d21c5dff59934611b06e31/30c93d987634143d024ceaf6c78adf6890f2d3e7314debcf4341a27c3f9ad895/event-state-bc0062fc8506.json`; SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d37de88bdc7b736ff912f7ff0fed5ae43dff3b8afdd247857d4db1cea4a33f2d/8c8809a9a6c7cf5eb9be4ce85e696eae4dbe450426348d5dce1dc9c674a5c0e8/event-state-bc0062fc8506.svg`.
- These event results are not full transaction evidence. The server reported `helpers = 0` and deferred workspace-wide helper/lifecycle projections, so it did not traverse the standalone scripted-effect allocator/executor. Source-only tracing is not treated as equivalent engine evidence.
- `hoi4.event_compare` from recorded revision `a0d209ec728fe48cc44e3412c64b7c86ab0d1fea28713348d4dac1ba52035c67` to current `bc0062fc...` returned exact blocker `EVENT_REVISION_NOT_CACHED`; no comparison artifact exists.
- Probability artifact for the complete outer region pool: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7c9f4e1c352da4ffa84bfd445037b073d6c7752a397f07b895de6f7632adc0c2/33959a362d180de62f8fc23f37ad3b4cb40faffd1add8bc6517f456beef2eb83/probability-inspect-9cab0bffea71.json`. Region 01: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0cbf22cd1589a225077271d9978eaddf199e03cde53b39ffef7d646749e7975e/e671f5f5e87e6739e6e7c434e37e94bc3d3cbe0038a015fbeb7ee35e485175e2/probability-inspect-183d00a51772.json`. Region 02: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dd14d237e621f2eb1bef7dc6d9e652e14bd853c1a74712d39b7ea70bc77f8665/3d30834eeceb6dff6de46fd805d81196d32630e386f44f35b2724606ffd8797c/probability-inspect-56b159655eab.json`.

## Accepted-plan disposition and owner action

The recent handoffs `006_event6_capital_scope_regression_guard_2026_08_21.md`, `006_event6_empty_shell_release_validation_fix_2026_08_20.md`, `006_event6_existing_shell_release_execution_fix_2026_08_20.md`, and `006_event006_allocator_attestation_weight_fix_2026-08-20.md` are **implemented in current source**. This audit found no stale accepted fix or undisclosed simplification inside the bounded manual-entry path.

**No owner patch is justified from current evidence.** A speculative relaxation of eligibility, host survival, transaction mutual exclusion, metadata validation, or rollback would weaken accepted safety contracts without identifying the failing stage.

The safe next owner action is diagnostic, not a gameplay patch: obtain the terminal receipt from the same failing invocation, classify it using the three cases above, then patch only the identified stage. If the receipt says selected count zero, audit actual candidate eligibility/region totals in that world state. If it says instantiated count below selected count, isolate absent-tag `release` versus existing-shell state transfer. If transferred states are below expected states, isolate the first frozen ownership row. Until one of those engine facts exists, the zero-country symptom remains unresolved rather than a provable current-source defect.
