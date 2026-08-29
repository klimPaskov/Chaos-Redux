# Famine and migration forced-movement owner handoff

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

## Scope and implementation result

This handoff covers the bounded exact deportation/camp-prison transfer owner added behind the existing Germany camp-prison owner transaction.

The implementation does not add a world scan, event, decision, GUI, map mode, localisation, random destination, Soviet proxy, fixed historical total, or movement-as-death path.

No commit was created.

## Required source review

Before editing, the famine/migration specifications and prepared prompts governing the shared ledger, forced movement, scripted-system architecture, probability audit, decision audit, and completion audit were read.

The offline Paradox wiki core pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, and AI modding were consulted.

Vanilla HOI4 documentation for effects, triggers, script constants, scopes, event targets, and arrays was consulted alongside the current Chaos Redux famine/migration helpers.

The authoritative current cohort and exact transfer owners were reviewed before introducing this caller.

## Changed files and identifiers

- `common/script_constants/famine_migration_forced_movement_constants.txt`
  - `famine_migration_forced_movement_result`
  - `famine_migration_forced_movement_cause`
  - `famine_migration_forced_movement_custody`
- `common/scripted_triggers/famine_migration_forced_movement_triggers.txt`
  - `famine_migration_forced_transfer_live_ledger_arrays_are_aligned`
  - `famine_migration_forced_transfer_contract_is_valid`
  - `famine_migration_forced_transfer_route_death_request_is_valid`
  - `famine_migration_forced_transfer_staged_cohort_proof_is_valid`
  - `famine_migration_forced_transfer_bound_cohort_proof_is_valid`
- `common/scripted_effects/famine_migration_forced_movement_effects.txt`
  - `famine_migration_forced_transfer_cleanup_staged_cohort`
  - `famine_migration_execute_forced_transfer_exact`
- `common/scripted_effects/famine_migration_forced_movement_effects.md`
  - contract, formulas, lifecycle, cleanup, and future-owner documentation
- `common/scripted_effects/chaosx_dynamic_effects.md`
  - documented the new forced-movement effect and its shared exact-transfer delegation
- `common/scripted_effects/camp_repression_major_country_effects.txt`
  - `camp_rework_germany_apply_prisoner_transfer` caller and state-88 defense-in-depth guard
- `common/decisions/genocide_crisis_decisions.txt`
  - exact `germany_transfer_prisoners_to_experiment_site` target and availability guards
  - both `FROM` guards reject state 88 before the decision can consume its cost or enter `complete_effect`

The pre-existing concurrent changes in the worktree were preserved.

## Exact caller and ownership

The owner caller is `camp_rework_germany_apply_prisoner_transfer` in `common/scripted_effects/camp_repression_major_country_effects.txt`.

It runs after the existing successful crisis, camp, evidence, pressure, autonomy, cloning, radicalization, tribunal, and country-recalculation effects.

The caller saves state `88` as `famine_migration_forced_transfer_destination` and supplies explicit intake proof there.

The caller then enters `FROM`, which is the exact source state, and invokes `famine_migration_execute_forced_transfer_exact`.

`ROOT` is the actor and source `OWNER` is both the source owner and pressure owner.

State `88` `OWNER` is the reception owner.

The cause is `deportation_camp_prison_transfer` and custody is `forced`.

The caller supplies no route-death proof and sets the requested route-death slice to zero.

The caller's authoritative outer limit also rejects `FROM` state 88 before any camp-owner transaction effects run.

The exact decision's `target_trigger` and `available` `FROM` blocks independently reject state 88, preventing the normal decision path from consuming resources or applying camp-side effects for an origin equal to the fixed destination.

This exclusion is necessary because the current `is_germany_occupied_poland_prisoner_source` trigger explicitly includes `state = 88`; state 88 is therefore not provably impossible as a source under the live predicates. The shared exact contract remains fail-closed with its distinct-origin requirement as a third defense.

## Post-success caller census

Before this follow-up, the successful caller reached `famine_migration_execute_forced_transfer_exact`, which staged the aligned cohort, performed the sole exact state population debit and destination population credit, bound the cohort as `destination_bound_unsafe`, and persisted transaction metadata, but emitted no reception-load receipt and no deportation condemnation.

After this follow-up, the exact owner performs the same population/cohort transaction and, only inside its valid positive-survivor branch, enters the saved destination state 88 and calls `famine_migration_apply_reception_delta` once with `famine_migration_forced_transfer_survivor_credit` as the credit amount. The canonical helper updates state reception load, state registration, destination-owner country reception load, country registration, reception context, and overcrowding evaluation.

The same branch then enters the saved `famine_migration_forced_transfer_actor` target, which is `ROOT` and therefore the exact responsible actor country, and calls `famine_migration_condemn_deportation` once with zero civilian-death and contamination inputs. It persists the accepted transaction, cohort, survivor amount, origin, and destination evidence on that actor country after the adapter call.

The reception call is made in the destination `OWNER` scope and uses the already-bound live cohort and its deportation/forced-custody metadata as context. Neither post-success receipt calls a population-loss, destination-credit, safe-bind, integration, resettlement, or Deaths effect.

Replay (`already_applied`), lower or mismatched transaction identity, failed validation, failed bind/route/conservation, and zero-survivor paths remain outside this branch and produce neither post-success receipt.

## Helper map and lifecycle

The live-array trigger proves equal lengths for IDs, origins, hosts, destinations, owners, amounts, sources, statuses, and the live count.

The contract trigger requires explicit positive request, origin, destination, actor, transaction identity, cause, custody, source pressure-owner proof, reception-owner proof, event targets, distinct valid states, and destination owner intake proofs.

The effect captures origin, actor, source owner, pressure owner, destination, and reception-owner targets before staging.

It rejects lower transaction identities and returns `already_applied` for a matching transaction signature with the same destination, actor, and requested amount.

For a new transaction, it records one provisional aligned cohort row with source `deportation`, resolves the row's exact origin, enters the explicit destination, and calls the existing forced bind helper.

The bound proof requires the actual route destination target to equal the caller-supplied state 88 target.

The effect then supplies the existing exact route helper with positive request, protected-origin floor, route/border/transport/safety/actor proof, actor target, zero route deaths, and the cohort ID.

The shared helper performs the only population mutation and records the one positive-survivor destination history receipt.

After destination credit, the shared host-update helper overwrites the live row amount with actual survivor credit and moves its host to state 88.

In that same valid-positive branch, the destination scope initializes missing reception projection variables and calls `famine_migration_apply_reception_delta` once with the measured survivor credit. Its canonical owner updates state reception load and the state sparse registry, then updates the destination owner's reception load and country sparse registry and refreshes reception/overcrowding context.

The branch then enters the saved ROOT actor country and calls `famine_migration_condemn_deportation` once with zero civilian-death and contamination inputs, persisting the accepted transaction/cohort/survivor/origin/destination evidence on that actor scope.

Failed stage, bind, route, or conservation validation calls the explicit cleanup helper, which removes the row and matching source, destination, and source-owner selection pointers.

Zero survivors also remove the row and its history; no dead people remain represented as a live cohort.

Successful positive transfer clears source selection pointers while retaining the destination selection pointer.

The source stores the last transaction signature and all actual outputs for idempotent retries.

The destination stores actor, origin, destination, source owner, reception owner, pressure owner, cause, custody, request, actual debit, route deaths, survivor credit, destination credit, and conservation output after a valid positive transfer.

No duplicate achievement receipt or separate camp population receipt is emitted; the one canonical reception-load receipt and one actor condemnation are post-success outputs of this exact transaction only.

## Dynamic formulas

The requested amount is `round(state_population_k * constant:chaos_meter_deaths.people_per_k * constant:famine_migration_decision_threshold.transfer_share)`.

The protected origin floor is `round(state_population_k * constant:chaos_meter_deaths.people_per_k * constant:famine_migration_decision_threshold.transfer_minimum_origin_share)`.

The existing centrally tuned share and floor are reused instead of duplicating tuning constants.

The current exact state-88 route uses a zero route-death request by default.

If a future owner submits a positive route-death request, it must also submit route-death proof, use the distinct `constant:chaos_meter_deaths_reason.forced_displacement` reason, and enable death logging.

## Conservation and ownership proof

The exact debit is measured from the source population before and after `apply_state_population_loss_without_recruitable_manpower_gain`.

The destination receives only the actual positive survivor credit through `famine_migration_apply_destination_credit`, which reconciles manpower against the state-population change.

The conservation equation is `actual_origin_debit = route_deaths + survivor_credit`.

Any positive residual is restored to the origin before the shared transfer can return valid.

The shared global ledgers receive actual debit, actual survivor credit, actual route deaths, and any restored residual separately.

The durable live cohort amount is therefore the actual debited survivor credit after destination credit, not the requested amount.

The reception delta source is exactly that measured survivor credit, not the requested amount, origin debit, route-death slice, or any fixed historical total. The helper's paired state/country accounting is the sole reception-load mutation and is called once after destination population credit.

The actor condemnation source is the same accepted positive transaction, identified by the monotonic transaction ID and live cohort ID recorded by the exact owner. Condemnation is actor-scoped and uses zero civilian deaths, so it creates no Deaths entry and does not alter conservation.

## Duplicate-producer audit

The older `genocide_germany_transfer_prisoners_to_experiment_site_in_from_accepted` and wrapper remain defined only in `common/scripted_effects/genocide_crisis_effects.txt`.

`rg` found no active call to that older wrapper or accepted effect outside their own definitions.

The current decision `genocide_transfer_prisoners_to_experiment_site` calls `camp_rework_germany_apply_prisoner_transfer`, which is the sole new forced-movement producer.

Its target and availability guards now exclude state 88 in the source scope, and the owner caller repeats that exclusion before its existing camp transaction.

`genocide_crisis_effects.txt`, generic camp decisions/effects, map modes, localisation, events, and unrelated files were not edited.

The new owner delegates to the existing exact transfer, cohort-history, and reception-delta helpers, so it does not add a second destination population credit, history receipt, or reception-load credit. The one actor-scoped condemnation call is reachable only from the non-replay valid-positive branch.

## MCP artifacts and blockers

The mandatory probability route was attempted once for the decision-adjacent owner surface with `hoi4.probability_inspect`.

The attempted request was `adapter = decision_ai_will_do` with source `{ files = [common/decisions/genocide_crisis_decisions.txt], decisionId = germany_transfer_prisoners_to_experiment_site }` and `refresh = yes`.

The installed MCP rejected that source schema with `-32602 Input validation error` and `Unrecognized keys: "files", "decisionId" at source`.

This exact blocker was recorded rather than retrying with an invented schema or substituting source review for MCP evidence.

No weighted value was changed, so no probability compare artifact exists.

No focus, event, GUI, map, technology, or doctrine surface is in scope for this patch.

## Validation and skipped validation

Static source review confirmed the new files have balanced Clausewitz braces, the forced triggers use the live-only alignment guard, the destination target is explicitly saved by the owner, and no forbidden `<=` or `>=` operators were introduced in the new files.

Static reference review confirmed every new effect and trigger identifier is defined once and the caller is referenced once.

The post-success source audit confirmed exactly one `famine_migration_apply_reception_delta` call and exactly one `famine_migration_condemn_deportation` call in the forced owner, both nested under positive valid transfer output; the replay branch remains separate and cannot reach either call.

The duplicate old genocide producer audit and source formulas were checked with `rg` and direct file inspection.

The HOI4 game was not launched, in accordance with repository instructions.

Live save validation and runtime population/conservation observation remain parent/user responsibilities.

Probability compare was skipped because the required probability inspection was blocked by the installed MCP input schema and no AI/weight source was changed.

## Residual gaps and uncertainty

State 88 intake safety remains an explicit owner proof because no dedicated camp intake-capacity API exists; the canonical reception helper now records the measured survivor load and refreshes the existing capacity/overcrowding projections without inventing a capacity model.

The existing live ledger has no actor column, so actor ownership is preserved in the contract targets and durable transaction metadata rather than adding a new parallel actor array.

The transaction identity is the actor-owned monotonic `genocide_decisions_taken` value, and the source keeps the last signature; a future owner with a different identity series must use a distinct transaction namespace or an expanded signed identity.

No non-zero route-death path is claimed until an owner can prove route conditions, so the state-88 route intentionally records zero route deaths.

No Soviet destination or proxy callsite was fabricated.
