# HQ helper temporary-output lifetime audit

Disposition: parent repair implemented in source and independently reviewed against the exact output map, with native interpretation limits retained.
This audit supports exact HQ costs, bounded preparation and upkeep, and completed commander service within the existing CBRN overhaul.
Only this handoff was written.
No gameplay, test, shared documentation, index, or commit changes were made.

## Confirmed source defect and minimal repair

The five HQ starters call package setters that first create their temporary outputs inside returning scripted effects.
The starters then consume those outputs in preparation calculation, CP accounting, operating debits, and delayed-event scheduling.
`cbrn_hq_preparation_days` is likewise first created inside its returning calculation helper and subsequently read by the starter and commit helper.
The five upkeep wrappers have the same package-setter boundary.
Native ability callers provide no earlier storage.
Under the repository's required conservative helper-frame model, those values disappear on return.

Allocate the sixteen output scalars below literally in each starter immediately before its activation-package call.
Allocate the nine operating-package scalars literally in each upkeep wrapper immediately before its upkeep-package call.
Allocate the three consumed stock-debit result names in the operating-package debit caller immediately before their respective helper calls.
Do not create a returning initializer scripted effect, because its new declarations would disappear at the same boundary.
No ability or event rewrite is necessary for these consumed-output repairs.

## Exact callers and returned-output map

All starters and wrappers execute in the named unit leader's character scope.
Temporary storage is unscoped and belongs to the active effect frame, not to `OWNER`, `ROOT`, or a saved country.
The table separates temporary storage from persistent character or country state.

| Caller or frame | Producing helper | Outputs consumed after return | Required storage placement |
| --- | --- | --- | --- |
| Five starters, `cbrn_hq_effects.txt:660-719` | Matching `cbrn_hq_set_*_activation_package` | Nine package debit scalars and preparation base/min/max, active duration, CP native/total | Sixteen literal zero allocations in each starter before its package call, including the separate preparation-days output |
| Same starter | `cbrn_hq_calculate_preparation_days`, lines 55-102 | `cbrn_hq_preparation_days` | Starter-owned zero allocation before calculation. It remains available to discount, budget, commit, trait, recovery and preparation scheduling |
| Five upkeep wrappers, lines 722-745 | Matching `cbrn_hq_set_*_upkeep_package` | Nine package debit scalars | Nine literal zero allocations in each wrapper before its package call |
| `cbrn_hq_debit_operating_package`, `OWNER` block, lines 227-290 | `cbrn_debit_mask_stockpile_oldest_first` | `cbrn_mask_stock_debit_completed` | Literal zero allocation in this debit caller before the mask helper at line 232 |
| Same `OWNER` caller | `cbrn_hq_debit_decontamination_stock_oldest_first` | `cbrn_hq_family_debit_completed` | Literal zero allocation before the decontamination helper at line 250 |
| Same `OWNER` caller | `cbrn_hq_debit_instrument_stock_oldest_first` | Same `cbrn_hq_family_debit_completed` | Literal zero allocation before the instrument helper at line 256, keeping the two family receipts separate |
| Same `OWNER` caller | `cbrn_debit_motorized_stockpile_oldest_first` | `cbrn_motorized_stock_debit_completed` | Literal zero allocation before the motorized helper at line 269 |

The exact starter names are `cbrn_hq_start_theater_protective_posture`, `cbrn_hq_start_decontamination_corridor`, `cbrn_hq_start_seal_operational_area`, `cbrn_hq_start_mass_antidote_response`, and `cbrn_hq_start_seal_infection_corridor`.
Their matching upkeep wrappers are `cbrn_hq_debit_protective_upkeep`, `cbrn_hq_debit_decon_upkeep`, `cbrn_hq_debit_seal_area_upkeep`, `cbrn_hq_debit_antidote_upkeep`, and `cbrn_hq_debit_infection_upkeep`.
The nine debit outputs are:

```txt
cbrn_hq_mask_debit
cbrn_hq_filter_condition_debit
cbrn_hq_decon_debit
cbrn_hq_instrument_debit
cbrn_hq_support_debit
cbrn_hq_motorized_debit
cbrn_hq_fuel_debit
cbrn_hq_medical_debit
cbrn_hq_manpower_debit
```

The seven additional starter allocations are:

```txt
cbrn_hq_preparation_base
cbrn_hq_preparation_min
cbrn_hq_preparation_max
cbrn_hq_active_duration
cbrn_hq_command_power_native
cbrn_hq_command_power_total
cbrn_hq_preparation_days
```

Use `set_temp_variable = { <name> = constant:cbrn_math.zero }` for these pure outputs.
Do not reset the committed-force band, operation code, stock-debit requested amounts, readiness, generation/service flags, or another input in this initialization block.
All nine debit values must be present, including zero-cost fields for a particular order, because the common debit helper checks all nine and stale values must not become another order's charge.

Package setters call `cbrn_hq_reset_operating_package` at their entry.
That reset helper also creates the nine values only within its own frame when no ancestor storage exists.
Starter or upkeep-wrapper allocation gives every nested call the same surviving caller-owned storage.
The existing reset helper can remain a reset of already owned values, preserving its API and package defaults.
Allocating only inside the returning reset helper or only inside the returning package setter would not fix the outer consumer.

## OWNER effects and family accounting

`OWNER` in character scope selects the country that recruited the commander.
It changes the regular-variable and native stockpile recipient, not temporary-variable scope.
The common debit effect uses that country for masks, filter condition, decontamination, instruments, support equipment, motorized, fuel, medical capacity, and reserved manpower.
Consumption totals and replacement demand are regular country variables.
The operation code, committed-force band, upkeep ticks, service counters, and completion flag belong to the character.

The decontamination helper at lines 135-175 removes models `_1`, `_2`, then `_3` and computes `cbrn_hq_family_debit_completed` as the actual sum removed.
The instrument helper at lines 177-217 removes instrument models `_1`, `_2`, then `_3` using the same result name.
The mask helper in `cbrn_protection_effects.txt:1919-1991` removes reconditioned, basic `_1`, improved `_2`, advanced `_3`, then sealed `_4` masks.
The motorized helper in `chaosx_dynamic_effects.txt:762-794` removes `motorized_equipment_0` before `_1`.
These sequences and requested amounts must remain unchanged.

Each helper sets its requested amount in the caller before invocation and creates its completed result inside the helper.
Without completed-result storage in the debit caller, native inventory removal can still occur inside the helper while the later consumption ledger receives zero or a missing result under the conservative return model.
This is a separate accounting defect from the outer package disappearance, and fixing only the starters would leave it present.
The family helpers' `*_remaining`, model availability/take/debit, and local work values are not consumed after return by the HQ debit caller.
Do not allocate those outputs merely to copy a broad public helper contract when this caller does not use them.
The shared motorized API documentation should still distinguish caller-owned completed and remaining outputs for callers that consume either after return.

Filter accounting is already different and must stay so.
The debit caller creates `cbrn_hq_filter_condition_before_debit`, supplies `cbrn_mask_loss_fraction = 0` and the condition-loss input, calls `cbrn_apply_military_mask_loss`, and subtracts the changed regular country filter condition from the saved before value.
Its `cbrn_hq_filter_condition_debit_completed` is computed in that same debit frame after return, rather than returned by the mask-loss helper.
`cbrn_apply_military_mask_loss` changes regular issued-mask, filter-condition, and replacement-demand state.
There is no additional HQ consumed temporary output to allocate at that call boundary.

## Values already owned by their consuming frame

| Value | Ownership and usage | Repair disposition |
| --- | --- | --- |
| `cbrn_hq_command_power_remainder` | Created in the CP helper and used by its nested `OWNER.add_command_power` before return | Keep local. Native ability pays the existing minimum, this helper pays only the standard/mass remainder |
| `cbrn_hq_preparation_budget_floor` | Created and used inside the efficiency-budget helper | Keep local. Preserve the 50% floor and absolute min/max clamps |
| `cbrn_hq_recovery_days` | Created in `cbrn_hq_commit_preparation:649-650` as preparation plus active duration, then passed into the debit and scheduling helpers before commit returns | Already caller-owned for those nested calls. No outer starter read needs this return value |
| `cbrn_hq_scheduled_event_id`, `cbrn_hq_scheduled_event_days` | Explicitly created in commit, each starter, or next-upkeep scheduler before `cbrn_hq_schedule_current_event` reads them | Already owned by the relevant scheduler caller |
| `cbrn_hq_next_upkeep_days` | Created inside next-upkeep helper and used there before return | Keep local |
| `cbrn_hq_active_days` | Created directly in `cbrn_hq.1` before the native timed-trait command | Already event-owned, no returning producer |
| Direct equipment/fuel/manpower negative amounts | Created inside the operating debit effect and used before it returns | Keep local and preserve the existing multiply-by-minus-one calculation |
| `cbrn_mask_stock_debit_requested`, `cbrn_hq_family_debit_requested`, `cbrn_motorized_stock_debit_requested` | Created in the debit caller before their helpers read them | Preserve as inputs, do not reset during output allocation |

The native abilities call each starter inside `hidden_effect` at `cbrn_hq_abilities.txt:73,110,152,189,226` and consume no starter temporary output afterwards.
They do not need a second outer allocation block when the starter owns every nested output that it itself consumes.
The event dispatcher likewise consumes no returned upkeep-wrapper temporary scalar.
It relies on the wrapper's country mutations and character-owned operation/tick state.
Allocating package storage in the wrapper is sufficient at that boundary.

`cbrn_hq_schedule_current_event` saves the existing regular `cbrn_hq_commander` event target immediately before scheduling from the current character.
The target is consumed by the scheduled event chain, not read as a newly returned scalar by an outer helper.
Do not replace it with a global target or add a target registry to solve temporary outputs.

## Completed service, cancellation, and scheduling boundaries

`cbrn_hq.2` checks positive remaining ticks, operation identity, active role trait, valid command, and affordability before calling the matching upkeep debit.
It then completes the tick and calls `cbrn_commander_record_completed_hq_operation` in that order.
`cbrn_commander_hq_completion_is_eligible` checks an assigned non-field-marshal army leader with units, zero remaining ticks, no previous completion flag, and an eligible matching active operation.
The recorder writes the completion flag and bounded service counters only on that existing final paid-operation path.
Preparation and cancellation do not call the recorder.

`cbrn_hq_fail_upkeep` removes benefits and clears ticks, but does not clear the operation code.
`cbrn_hq_has_no_preparation_or_active_posture` blocks a new activation while that code exists.
`cbrn_hq.3` clears it at the existing planned end.
The present source therefore preserves the earlier operation lock until that scheduled cleanup.
This audit found no demonstrated old-event collision and proposes no generation-system replacement.
The caller-storage defect can invalidate prices and timers in the conservative model, but it is not evidence that a correctly priced new operation can currently cross the existing operation lock.

Preserve the original preparation and active durations, readiness multipliers, commander discount, decontamination designer discount, residual floor, min/max clamps, tick counts, and restoration events `.20-.25`.
Recovery is scheduled at the existing preparation-plus-active duration, and the regular committed-force band selects the restoration amount.
No new trait, service award, cancellation refund, permission, paid action, or raid adapter is required.

## Demonstrated source-frame failure cases

The existing exported `VM`, parser, fixed-point arithmetic, and conservative helper return cleanup from `docs/plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js` were reused in an in-memory Node invocation.
The checked-in `docs/testing/2026-10-06_cbrn_helper_output_source_tests.js` was read as the existing regression pattern.
No shared VM or test file was edited and no new generic VM was created.
The light-force and committed-light predicates were bound explicitly as fixture truths.
The actual package and reset bodies were executed for the supported cases below.

| Actual helper or fragment | Without caller storage | With caller-owned storage |
| --- | --- | --- |
| Protective activation package | Every returned nonzero package/preparation/CP field absent | Masks 500, filter condition 2, support 20, preparation base/min/max 2/1/3, active duration 28, CP native/total 10/10 |
| Seal-area activation package | Returned fields absent | Support 30, manpower 500, preparation 4/2/7, active duration 30, CP 10/10 |
| Antidote activation package | Returned fields absent | Masks 100, support 30, medical commitment 5, preparation 1/1/1, active duration 14, CP 10/10 |
| Infection activation package | Returned fields absent | Masks 200, decontamination 30, instruments 20, support 40, medical commitment 5, manpower 500, preparation 3/2/5, active duration 60, CP 15/15 |
| Protective upkeep package | Returned fields absent | Masks 250, filter condition 2, support 10 |
| Antidote upkeep package | Returned fields absent | Masks 50, support 15 |
| Actual first preparation-calculator assignment with preparation base 4 | `cbrn_hq_preparation_days` absent, read as 0 by the fixture | Present as 4 |

These are source-frame results, not observed HOI4 behavior.
The proof did not simulate the full OWNER transaction, model inventory, scheduled events, readiness branches, designer branch, or completed-service engine callback.
It isolates the returning output defect using actual source.
An initial attempt to parse the entire complex system constant file failed in the bounded parser.
The invocation was corrected to read only the required exact constant blocks, following the existing source-test pattern, and the supported cases above then executed successfully.
No engine defect is inferred from that parser limitation.

Parent-owned meaningful regression work should cover all five operation types and three force bands, each allowed readiness band, the operations commander and truck-wash discounts, min/max/floor preservation, and exact activation and upkeep ledgers.
Include mixed-model mask/decontamination/instrument/motorized inventories to verify ordered actual removals and returned completed totals.
Use the existing conservative helper-frame cleanup and regular scoped storage separation rather than a flat dictionary that makes every helper output survive.
Retain checks that preparation alone and failed/cancelled upkeep award no service, and that only the final successful paid tick awards one eligible receipt.
Scheduling and restoration assertions must compare the actual bounded event days and existing committed-force amounts, without inventing an old-event failure.

## Inline-script option and helper documentation

An installed native parse-time source include could avoid repeated literal declaration text only if the include expands into the consuming caller frame before script execution.
A runtime initializer scripted effect cannot substitute for that behavior.
The current installed game has no `common/inline_scripts` directory, the bounded reference search for `inline_script` returned no section, and a vanilla `common/**/*.txt` search found no `inline_script =` precedent.
No supported installed inline-script schema or example was established.
Therefore the recommended implementation uses literal allocations in the exact consuming helpers rather than introducing an unverified include feature.
This is an explicit capability/reference gap, not permission to import another Paradox game's inline-script pattern.

Parent documentation should add the output contract to `docs/systems/cbrn_warfare/cbrn_hq_command.md` and narrow public comments at the package/preparation helper definitions.
State that output storage must already exist in the consuming ancestor frame, list the sixteen starter and nine upkeep fields and their zero defaults, and name the three stock completed-result outputs consumed by this caller.
The existing `chaosx_dynamic_effects.md` motorized API should document caller-owned outputs for post-return consumers if its contract is updated in the parent change.
No new neutral dynamic helper belongs in the central registry for this feature.
No new constants, event targets, persistent variables, flags, lifecycle cleanup, or tuning table changes are required.

## References, MCP evidence, and limits

The required `chaos-redux-events` skill's Helper output lifetime section at lines 175-184 was read, along with `chaos-redux-subagents` ownership rules already applied in this task.
Live `hoi4.reference_read` read offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:435-443`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
Line 440 records the scripted-effect return caveat and caller-preinitialization guarantee, and line 442 establishes unscoped temporaries.
Live reference reading covered installed `documentation/effects_documentation.md:7820-7827` for `set_temp_variable`, and lines 6496-6504 for `save_event_target_as`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
Live reading also covered offline `Effects:271` for character `OWNER`, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`, and the equivalent offline `Scopes:266` was read locally.
The installed effect reference supports temporary assignment in any scope but does not itself guarantee caller-return lifetime.
No online Paradox wiki was accessed.

The event context bundle omitted several source sections at its requested limit.
Targeted reads supplied the relevant temporary lifetime, assignment, target, and owner rules above rather than claiming the context bundle read them all.
`hoi4.event_inspect(mode=trace, selector={kind=event,eventId=cbrn_hq.2}, maxDepth=1, maxNodes=12, maxEdges=20, expandHelpers=false)` returned `EVENT_INSPECTED_PARTIAL` with one blocking diagnostic.
Source revision: `8f4a82aa5d847df22b40a90e209f8bd0e27f3d6ebe79d13e4fb3dbaf45dc33b0`.
Graph hash: `d494c41cf68a6eb896650d0f95ea38572ce93b8c83273a07a92d60c74eb41ceb`.
Artifact: [event trace](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/911c1b3ff94b83d669a53a80146616af15f5f86aa88d337090eea0f6d273b84d/859f43fd82d641d9d255979db71f0375d6f4c19fee1745c5f061b7ad8d548dc3/event-trace-8f4a82aa5d84.json).
The summary does not identify whether that blocking diagnostic concerns this HQ chain, and helper expansion was disabled.
The parent and agent trace artifact reads returned `provenance-manifest-unavailable`, including attempts with and without byte ranges.
The blocking diagnostic is therefore unreadable and cannot be classified as an HQ-chain issue or dismissed as unrelated.
No native helper-lifetime proof or event validation pass is claimed from this partial result.

Audited source SHA-256 snapshots:

| File | Revision |
| --- | --- |
| `common/scripted_effects/cbrn_hq_effects.txt` | `5c6c5a4d174de2baa933f093e0368752194bcf061f3a9a063d7cd40211300832` |
| `common/abilities/cbrn_hq_abilities.txt` | `7669bfba4f71954d26af6e465b7f051beba1acb57ecbdec1629081f2c060297f` |
| `events/cbrn_hq_events.txt` | `1460920e9a620fd742716265b9559c5044be42d4e0b0a2bcec2b6ef5bd55e53e` |
| `common/scripted_effects/cbrn_protection_effects.txt` | `62248367f0e75540ad18141d3636c31215f4a5a1d1502a0ce92824dc5182fdb6` |
| `common/scripted_effects/chaosx_dynamic_effects.txt` | `dd9f1d4144575753fe2de087991f9499b4618384ab36c52cb18f00738a09e131` |

## Final review of the parent repair

The parent froze a patch limited to `common/scripted_effects/cbrn_hq_effects.txt` and captured eight before files under `docs/testing/2026-10-07_cbrn_hq_lifetime/before/`.
Its manifest records baseline commit `269215ef29d8f5b5e4d09865b0b475c7c8869bda`.
An independent in-memory parsed-source comparison verified the full repair against that snapshot.
All five starters contain the exact sixteen mapped zero allocations as their first statements, before any helper call.
All five upkeep wrappers contain the exact nine mapped zero allocations as their first statements.
The operating debit caller contains exactly four additional completed-output allocations, immediately before the mask, decontamination, instrument, and motorized calls.
The shared family result is allocated at each of its two consumption sites.
The total is exactly `5 * 16 + 5 * 9 + 4 = 129` declarations.

After removing only those mapped output declarations from the parsed after source, every original command, value, branch, helper call, and callback order matches the before source.
Every other HQ helper body is identical.
The other seven captured ability, event, constant, trigger, and commander-receipt files are byte-identical to the before snapshot.
No requested debit input, cursor, persistent operation variable, flag, price, timer, ability ID, stock-model order, role gate, service threshold, receipt, or AI coefficient was replaced or reset by the new output declarations.
The repaired source SHA-256 is `eef1bceafc226b303d3568e7081bf4e2286cbb9a109ff6389538991852039a11`.
The earlier SHA-256 table and line references describe the audited before source.

This review confirms that the parent patch implements the smallest supported caller-storage repair and preserves the original behavior contract apart from restoring the intended returned values.
The separate source-test worker owns the full operation/band and transaction scenarios, and the parent owns its final test acceptance.
No new generic VM, inline script, gameplay wrapper, rebalance, event-generation scheme, or fallback was introduced.
The bounded audit and patch-preservation review are complete as implementation support.
Native event/transaction interpretation and the unreadable MCP blocking diagnostic remain explicit validation limits.
This agent made no source patch, simplification, fallback, rebalance, game launch, or gameplay-completion claim.
