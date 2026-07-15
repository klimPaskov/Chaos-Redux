# Fallout survival ledger identity transaction proof

## Verdict

The formula-neutral first phase of the Fallout survival ledger is implemented. It stages one exact country row for every finalized successor and one exact state row for every included state. It records transition generation, allocation provenance, region, archetype, and country-memory identities, destructive-phase provenance, stable physical indexes, and the fixed nine-resource identity order. An exact recovery transaction can discard and rebuild only a malformed uncommitted identity payload during survivor allocation.

No survival resource value is produced. No state numerator, denominator, share, country initial value, or mutable value is written. No effect sets `fallout_survival_ledger_ready`. The blackout transition therefore remains unable to pass this barrier until the numerical contract is reviewed and implemented.

## Source files

- `common/scripted_effects/fallout_survival_ledger_effects.txt`
- `common/scripted_triggers/fallout_survival_ledger_triggers.txt`
- `common/scripted_effects/fallout_world_end_effects.txt`
- `common/scripted_triggers/fallout_world_end_triggers.txt`
- `common/scripted_effects/fallout_world_end_event_effects.txt`
- `common/scripted_triggers/fallout_world_end_event_triggers.txt`
- `common/script_constants/fallout_world_end_constants.txt`
- `common/script_constants/fallout_world_end_event_constants.txt`

## Staged global identity

`fallout_stage_survival_ledger_identity_transaction` runs only after the final successor-allocation proof passes and before player continuation commits. It records:

- survival schema and transition generation
- source allocation schema and generation
- exact source country and state counts
- aligned country scope, generation, and physical-index arrays
- aligned state scope, generation, and physical-index arrays
- staging date and arithmetic day

The effect first clears only an uncommitted survival transaction. A future committed ledger makes that reset a no-op. The staging flag is written last, after the full payload trigger proves every aligned back-reference and all-and-only coverage.

## Uncommitted recovery

`fallout_recover_uncommitted_survival_ledger_identity_transaction` owns the sole retry route for an identity build that registered exactly one `survival_ledger_incomplete` error. Recovery is permitted only while the transition remains in survivor allocation, the final allocation and player planning ledgers are current, no committed survival ledger exists, survivor allocation has not committed, and player continuation has not committed or applied.

The wrapper clears only that exact error signature and immediately invokes the ordinary staging transaction. The recovery trigger proves the complete allocation structure without requiring the error to disappear first. The staging transaction performs the full uncommitted reset before rebuilding every country and state identity from the current allocation. If validation fails again, it writes the same single owned error. The static retry path can rebuild a persisted absent, building, or structurally invalid identity payload after an interruption. Runtime interruption behavior remains unobserved.

A malformed identity payload without an error is rebuilt because survivor allocation now tests the structural identity proof instead of trusting the staging flag alone. A committed ledger, a later transition phase, or any different error signature cannot enter this route. Numerical arrays remain empty and the ready flag remains absent.

The state list covers every state in `game:all_states`. Final allocation already proves that every landholding country is one of the assigned successors. Each staged state stores its exact owner scope and the transition generations for snapshot, Air Winter provenance, grading, population loss, state rewrite, and province supply-network collapse.

Each staged country stores the exact final allocation schema and generation, stable array index, owned-state count, region identity, government archetype identity, and country-memory identity.

## Nine-resource row shape

Both state and country rows store an explicit resource identity array. Index zero is the `none` sentinel. Indexes one through nine are Food, Clean water, Medicine, Scrap, Fuel, Power, Filters, Shelter capacity, and Recognition in the accepted order.

The future state numerical row is reserved as aligned raw numerator, raw denominator, and share arrays. The future country row is reserved as aligned raw numerator, raw denominator, immutable initial, and mutable current arrays. Row commit flags exist only as required shape markers. No current effect writes them.

The structural triggers do not approve coefficients, rounding, aggregation, range limits, modifier order, zero-state behavior, or the initialization relationship between immutable and mutable country arrays. Those checks must be added before the sole ready-flag setter is implemented.

## Transition barrier

The survivor-allocation phase now performs these steps in order:

1. prove the final successor allocation and player planning ledger
2. set initialization status to `survival_ledger_pending`
3. stage an absent uncommitted identity transaction
4. require the future committed survival ledger before setting `fallout_transition_survivor_allocation_applied`
5. require the same barrier before advancing to player continuation

Player continuation checks the barrier again before any player-country commit. Every selected player target must carry its committed country survival row. Map return also requires the same global barrier.

The stage effect does not invent resource values to escape this wait. A fresh staging failure records `survival_ledger_incomplete`. During survivor allocation, the exact single-error signature can clear and restage the uncommitted identity payload. A later phase that lacks the committed ledger records the same error and remains closed because later phases are outside the recovery gate.

## Scheduler ownership

The scheduler consumes this transaction but never creates or repairs it. Registry schema 2 binds each new registry to the survival schema, generation, and country count. Registry rows require the corresponding durable country resource row.

A completed save with scheduler initialization pending but no current survival ledger records `survival_ledger_not_current`. The scheduler does not substitute state grades, zero arrays, region, archetype, or country-memory identities, or later live ownership.

The post-reveal header and frozen back-reference proof do not require current state ownership. This keeps a committed ledger historical after legitimate annexation. Only the mutable country array is intended for later gameplay changes.

## Engine references and precedents

The installed official documentation was used as the primary syntax authority:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md` for `for_each_scope_loop`, `for_loop_effect`, variable writes, array writes, and scope iteration
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md` for `all_of`, matched values and indexes, `all_of_scopes`, `is_in_array`, variable comparison, and dynamic scope validation
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md` for scope variables and typed script constants
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/script_constants/documentation.md` for script-constant schema and access
- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` for arrays, numeric indexes, scope arrays, and temporary-variable lifetime

Repository precedents are the aligned successor-assignment ledger and living-world registry in the Fallout files, plus `006_independence_wave_effects.txt` and `006_independence_wave_triggers.txt` for stable indexed scope arrays and context-loaded dynamic-scope proof.

## Migration boundary

World transition schema remains 11 because this tranche cannot commit a survival ledger and does not replay any destructive phase. An active schema-11 transition at survivor allocation may stage current identities and wait for the reviewed numerical producer. A completed schema-11 Fallout save receives no fabricated ledger and cannot activate the scheduler.

Living-world registry schema advances from 1 to 2 because the registry now carries survival binding receipts. Paired runtime-schema-1 and registry-schema-1 rows may promote together only if a fully current committed survival ledger already exists, both scheduler activation flags remain absent, and the existing empty-transaction migration proof passes. A current runtime schema may bind an unbound schema-1 registry only while the registry is ready, both activation flags remain absent, no scheduler error exists, the map-return receipts and full survival ledger are current, and every indexed registry, allocation, and survival row agrees. When the full survival ledger is current, both migrations run before the post-migration header check. Otherwise the pre-migration missing-ledger check fails closed.

## Remaining blockers

- The numerical source formula for every resource is unapproved.
- Rounding, aggregation, range, zero-state, and overlay-order rules are unapproved.
- The initialization relationship between immutable and mutable country arrays is unapproved.
- No state numerical producer exists.
- No country aggregation producer exists.
- No numerical row commit effect exists.
- No global survival ready-flag setter exists.
- General successor allocation and package producers remain absent, so the identity stage is not reachable end to end in the current transition.
- Runtime persistence, interruption recovery, and multiplayer behavior are unobserved because HOI4 was not run.

These are intentional blockers. The identity transaction is not a completed survival mechanic and does not enable any living-world event.
