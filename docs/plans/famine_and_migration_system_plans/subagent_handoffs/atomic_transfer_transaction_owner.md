# Atomic transfer transaction owner handoff

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

## Scope and outcome

This tranche audits and completes the shared exact civilian-transfer transaction in the owned famine/migration surfaces.

The population primitive remains private to `famine_migration_execute_exact_transfer_transaction`; all physical movement lanes use that wrapper and the deferred finalizer owns row, history, projection, paired-ledger, selection, and refresh reconciliation.

The terminal forced-return fix releases `famine_migration_forced_return_pending` after any finalize-valid forced-return row update, including all-death, while decision resolution, rewards, arrival effects, and missions remain positive-survivor gated. Voluntary-return eligibility is released on any finalize-valid voluntary-return row update, and finalization clears chain-local bind/rebind proof markers plus the request ID when the all-death branch skipped the receipt helper.

## Files changed

- `common/scripted_effects/chaosx_famine_migration_effects.txt`
  - Kept the sole primitive call inside the public wrapper.
  - Restricted destination headroom calculation to a valid capacity and role-appropriate admission-policy proof.
  - Reconciled state selectors and both persisted-owner/current-host country selectors during every finalized row update, including all-death.
  - Cleared the forced-return pending country lease only after a finalize-valid forced-return row update.
  - Cleared voluntary-return eligibility and skipped-bind chain-local proof inputs only after a finalize-valid terminal row update; no durable decision resolution was granted.
- `common/scripted_effects/famine_migration_decision_owner_effects.txt`
  - Normalized the malformed `check_variable` in `famine_migration_decision_set_policy` to explicit `var`, `value`, and `compare` fields.
- `common/scripted_effects/chaosx_dynamic_effects.md`
  - Updated the exact-transfer and cohort lifecycle contract to describe the wrapper-only primitive, all-death completed rows, transient forced-return release, and provisional-abort boundary.
- `docs/plans/famine_and_migration_system_plans/subagent_handoffs/atomic_transfer_transaction_owner.md`
  - This handoff.

No constants, decision AI weights, decision IDs, corridor triggers, or lane-owner files required source changes in this tranche.

## Exact transaction contract

Let `R` be the staged full cohort request, `F` the protected origin floor, `P = round(state_population_k * constant:chaos_meter_deaths.people_per_k) - F` clamped at zero, `D` the measured origin debit, `K` the measured route-death slice, and `S` the measured survivor credit.

The same-chain preflight requires `P >= R`, one aligned row with exact ID, exact current host, permitted live status, and row amount exactly `R`, a valid route request, a concrete movement role, and a role-correct bind/rebind mode.

For hosted lanes, preflight also requires both source state reception load and source-owner country reception load to cover `R`, so the later actual debit `D <= R` can be debited without an underflow.

For survivor lanes, preflight requires destination reception capacity headroom `capacity - load >= R` and the appropriate admission policy; headroom is left at zero when either capacity schema or policy proof is invalid.

The conservation equation is `D = K + S`, with any measured destination-credit shortfall restored at the origin before the transaction can become valid.

The primitive owns only the origin population debit, survivor destination population credit, route-death logging, and conservation counters.

Route deaths call the Deaths registrar with `chaos_deaths_apply_state_pop = 0` and therefore never debit population a second time.

Hosted reception source debit is exactly `D`; destination reception credit is exactly `S`.

New-origin lanes use source-reception-not-required and therefore apply no source reception debit.

The wrapper obtains a bind receipt only when `S > 0` and calls `famine_migration_finalize_exact_transfer` exactly once after reception and bind receipts are amount-matched.

All-death is represented by `S = 0` and `K = D`; it performs no destination reception credit, destination bind, destination history visit, destination population credit, arrival reward, or positive mission.

For all-death, the finalizer keeps the aligned row at its current host, sets amount to zero, marks status `completed`, settles proven paired ledgers, reconciles touched state/country selections, records only origin-side projection evidence, and refreshes state context.

For positive survivors, the finalizer writes the staged finalizer cohort ID to the destination/host/amount/status arrays, records destination history once, writes destination projection evidence, settles paired ledgers, reconciles both old/new state and country selectors, and refreshes.

No bind/rebind helper writes history or mutates aligned row identity.

## Physical-lane ownership table

| Lane | Owner entry point | Wrapper path | Bind mode | Reception mode | All-death outcome |
| --- | --- | --- | --- | --- | --- |
| Spontaneous internal/cross-border movement | `famine_migration_process_spontaneous_movement_owner` | `famine_migration_execute_exact_transfer_transaction` at `common/scripted_effects/famine_migration_spontaneous_movement_effects.txt:280` | Safe bind | New-origin, no source debit | Completed current-host row; no survivor outcome |
| Forced/deportation movement | `famine_migration_execute_forced_transfer_exact` | `famine_migration_execute_exact_transfer_transaction` at `common/scripted_effects/famine_migration_forced_movement_effects.txt:218` | Forced initial bind | New-origin, no source debit | Completed row; no positive deportation receipt |
| Corridor evacuation | `famine_migration_execute_corridor_evacuation` | `famine_migration_execute_exact_transfer_transaction` at `common/scripted_effects/famine_migration_corridor_effects.txt:542` | Safe bind | New-origin, no source debit | Finalized terminal row; corridor mission remains survivor-only |
| `fm_famine_evacuation` | Decision owner at `common/decisions/famine_migration_decisions.txt:1791` | `famine_migration_decision_execute_new_origin_organized_evacuation` -> wrapper | Safe bind | New-origin, no source debit | No positive evacuation mission/reward |
| `fm_evacuate_vulnerable` | Decision owner at `common/decisions/famine_migration_decisions.txt:1978` | `famine_migration_decision_execute_new_origin_organized_evacuation` -> wrapper | Safe bind | New-origin, no source debit | No positive arrival/mission |
| `fm_evacuate_workers` | Decision owner at `common/decisions/famine_migration_decisions.txt:2172` | `famine_migration_decision_execute_new_origin_organized_evacuation` -> wrapper | Safe bind | New-origin, no source debit | No positive arrival/mission |
| `fm_distribute_arrivals` | Decision owner at `common/decisions/famine_migration_decisions.txt:2978` | `famine_migration_decision_execute_hosted_transfer` -> wrapper | Safe rebind | Hosted, source debit `D` | No arrival/medical reward |
| `fm_transit_only` | Decision owner at `common/decisions/famine_migration_decisions.txt:3163` | `famine_migration_decision_execute_hosted_transfer` -> wrapper | Safe rebind | Hosted, source debit `D` | No arrival reward |
| `fm_enforce_closure` | Decision owner at `common/decisions/famine_migration_decisions.txt:3293` | `famine_migration_decision_execute_hosted_transfer` -> wrapper | Forced rebind | Hosted, source debit `D` | Condemnation gets exact positive `K` once; no survivor outcome |
| `fm_third_country_resettlement` | Decision owner at `common/decisions/famine_migration_decisions.txt:3590` | `famine_migration_decision_execute_hosted_transfer` -> wrapper | Safe rebind | Hosted, source debit `D` | No resettlement projection/reward |
| `fm_voluntary_return` | Decision owner at `common/decisions/famine_migration_decisions.txt:3760` | `famine_migration_decision_execute_hosted_transfer` -> wrapper | Safe rebind | Hosted, source debit `D` | No return reward/mission |
| `fm_forced_repatriation` | Decision owner at `common/decisions/famine_migration_decisions.txt:3939` | `famine_migration_decision_execute_hosted_transfer` -> wrapper | Forced rebind | Hosted, source debit `D` | Condemnation gets exact positive `K` once; no return projection/reward |

`fm_local_integration` is intentionally not a physical movement lane; it consumes an already hosted row through its separate integration accounting contract and therefore is not included in the 12 transfer lanes.

## Forced-return distinction

Initial deportation uses `transfer_bind_forced` on a newly staged active row.

Hosted forced return uses `transfer_rebind_forced`, requires the persisted origin as destination, proves current host differs from that origin, and requires explicit actor and destination-policy proof.

Forced return deliberately uses `famine_migration_forced_return_destination_is_valid` rather than fabricating ordinary food-safe or safe-route proof.

The finalizer clears `famine_migration_forced_return_pending` only after `famine_migration_exact_transfer_finalize_request_is_valid` and the row update succeed, so failed, partial, or non-finalized attempts retain no false success but also cannot strand a valid all-death transaction lease. It applies the same terminal-only rule to `famine_migration_voluntary_return_eligible` and clears chain-local destination bind/rebind proof markers plus `famine_migration_cohort_id_request` after the row update; it does not set durable resolution, reward, arrival, or mission outcomes on all-death.

The closure and forced-repatriation decision branches forward only positive `famine_migration_transfer_route_deaths` to their Condemnation adapters after finalize-valid, with no second Deaths write.

## Provisional row and cleanup boundary

New-origin decision and forced/spontaneous owners stage the provisional aligned row before invoking the wrapper.

`famine_migration_abort_staged_cohort_record` can remove that row and its origin history only while the same chain proves no positive population debit, no reception amount, no destination credit, and no finalize receipt.

Once a positive debit or reception receipt exists, ordinary failure paths do not erase the row; hosted survivor rows remain live and all-death rows remain completed zero rows at their current host.

## Helper map and call-site migration

| Helper | Scope | Inputs | Outputs | Side effects | Call sites |
| --- | --- | --- | --- | --- | --- |
| `famine_migration_preflight_exact_transfer` | Origin state | Exact row ID, request, role, bind mode, route and reception proofs | Preflight result and staged finalizer authority | Read-only proof; no population, reception, row, history, projection, or refresh mutation | Wrapper only |
| `famine_migration_transfer_civilians_exact` | Origin state | Preflight authority, route-death request/reason, protected floor, optional Deaths target | `D`, `K`, `S`, conservation ledger, primitive result | Sole origin debit, survivor credit, Deaths ledger write with state-population application disabled | Wrapper only |
| `famine_migration_apply_reception_delta` | State | Positive actual amount, mode, request proof | Reception result and exact applied amount | One matched state/country reception delta and dirty/refresh bookkeeping | Wrapper source debit and destination survivor credit; separate integration accounting remains outside physical lanes |
| `famine_migration_bind_cohort_destination` / `_forced` | Destination state | Finalizer ID and safe/forced proof | Bind receipt | Read-only receipt; no row or history mutation | Wrapper only for new-origin lanes |
| `famine_migration_rebind_cohort_destination_safe` | Destination state | Persisted host/owner, safe rebind proof, route and actor proof | Safe rebind receipt | Read-only receipt; no population or history mutation | Wrapper only for hosted transit/resettlement/voluntary return/distribution |
| `famine_migration_rebind_cohort_destination_forced` | Persisted origin state | Persisted origin, differing current host, forced actor/policy proof | Forced rebind receipt | Read-only forced-return receipt; no fabricated safety claim | Wrapper only for closure/forced repatriation |
| `famine_migration_finalize_exact_transfer` | Origin state | Finalizer authority plus source/destination/bind receipts | Finalize-valid or invalid | Sole row host/destination/amount/status, history/projection, paired ledgers, selector reconciliation, refresh, terminal transient-flag and skipped-bind proof cleanup | Wrapper exactly once |

The migration from direct primitive ownership is complete in the code surfaces: the primitive call census has one executable call at `chaosx_famine_migration_effects.txt:2520`, inside the wrapper, and the six bind/rebind calls plus finalizer call are likewise wrapper-local.

## Decision and weighted-surface census

The decisions file contains exactly 26 primary decision blocks, two response blocks (`fm_accept_corridor_offer`, `fm_reject_corridor_offer`), and six mission blocks.

No AI weight or probability-bearing source was changed.

The mandatory initial `hoi4.probability_inspect` accepted `source.path = common/decisions/famine_migration_decisions.txt` and returned the artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0e0894d7e4a255a02b09c3d4ea68de1181ce7c40084bd4e8401793046a369d31/f64100fbe8935cbfb7d34826f40599953e9a2bc1cdcf89baf6eb0129324c7b19/probability-inspect-cf7412349300.json` with source revision `710559ae665bf2231f1268e31d52fd0115d74d2da62b9da0802dc9ac56814393` and source hash `cf7412349300f0c0465917b4235db3adf02609ff69caa1f67793477c7f1b15dc`.

The requested `decision_ai_will_do` adapter was empty and redirected to `mission_ai_will_do`; the result is source discovery rather than balance evidence.

The required `chaosx_ai_probability_auditor` route is not present in the callable tool inventory, so no probability comparison or AI-balance conclusion is claimed.

## Source-level validation evidence

- Executable primitive/bind/finalizer census: one primitive call, all binding/rebinding calls and the single finalizer call are inside `famine_migration_execute_exact_transfer_transaction`; the 12 lane call sites map to the table above.
- Reception amount proof: `famine_migration_exact_transfer_finalize_request_is_valid` requires hosted source applied amount equal `D`, new-origin source applied amount zero, survivor destination credit equal `S`, destination reception applied equal `S`, and bind receipt valid; all-death requires `K = D` and destination reception applied zero.
- All-death proof: wrapper skips destination reception/bind when `S = 0`; finalizer updates the active row to amount zero/completed at current host, records no destination history, settles paired ledgers, reconciles state plus owner/host country selections, clears forced-return pending only for forced-return role, and leaves positive outcomes to caller gates.
- Reward/cleanup gate census: distribution, transit, closure, resettlement, voluntary return, and forced repatriation outcome branches require finalize-valid and positive survivor credit; closure and forced repatriation Condemnation branches require finalize-valid, positive debit, and positive route deaths; staged-row abort requires zero debit, zero reception, zero destination credit, and no valid finalize receipt.
- Corridor amount proof: corridor evacuation copies `famine_migration_cohort_resolved_amount` from the exact selected cohort; route deaths are reset deterministically to zero and the reason is explicitly `forced_displacement`.
- Comparison hygiene: all owned files have zero literal `<=` or `>=` tokens and zero malformed `check_variable` blocks lacking explicit `var =`, `value =`, and `compare =` fields.
- Brace hygiene: all ten owned source files have balanced braces after the patch.
- Scan hygiene: no new `every_state`, `every_country`, `on_daily`, `on_weekly`, or `on_monthly` scan was introduced; only bounded aligned-array `while_loop_effect` passes remain.
- Route safety hygiene: no executable `famine_migration_route_unsafe` proxy or fabricated unsafe marker is used by the transfer contract; the pre-existing `famine_migration_corridor_reason.route_unsafe` is only an expiry-history reason and is not route proof.

## Risks, blockers, and unsupported evidence

HOI4 was not launched, per repository instructions; live engine parsing and save/reload behavior remain user-owned validation.

The probability auditor MCP route is unavailable, so weighted AI parity is intentionally unclaimed even though no AI weights changed.

The source-level brace and comparison checks do not replace Clausewitz parser or live-engine validation.

Existing unowned markdown files still contain historical prose naming the old direct primitive call path; this tranche updates the owned dynamic helper contract but does not rewrite unrelated handoff documentation.

No constants or probability tuning were changed, and no simplification or fallback was introduced.
