# Fallout manual population reconciliation proof

## Scope and status

The exact-province manual thermonuclear scenario remains dormant and release-
blocked. This contract changes only how a future manual request reconciles its
population: the first-week native/aggregate consequence remains intact, while
the later standard Fallout rewrite removes only the additional loss needed to
reach the ordinary grade ladder from the original prestrike population.

No scenario registry row, scheduler activation, public event, Zombie surface,
localisation, or asset is added by this proof. Assets: none.

## Helper map

| Helper | Scope | Inputs | Outputs | Side effects | Call site |
| --- | --- | --- | --- | --- | --- |
| `fallout_manual_capture_population_baselines` | Country | current `state_population_k`, `global.fallout_manual_generation` | per-state prestrike population in `k` and people, plus generation and counted ledger receipt | sets `fallout_manual_prestrike_population_recorded` and the O(1) global completion receipt after 1,081 rows | manual sweep initialization |
| `fallout_manual_record_state_population_loss_provenance` | State | prestrike receipt and live state population | first-week after-population, loss, reconciled total, and generation in people | sets `fallout_manual_first_week_population_loss_recorded`; does not write Deaths | manual aggregate state consequence |
| `fallout_manual_calculate_population_loss_intent` | State | authenticated baseline, frozen post-first-week population, standard grade | `fallout_state_loss_percent`, `fallout_expected_population_before_loss`, `fallout_expected_population_requested_loss` | none beyond temporary values | both standard population-loss receipt paths |
| `fallout_manual_preflight_population_contract` | Country | all manual receipts, frozen snapshot, grade rows | one state-bound replay receipt per row and one global generation receipt | performs the sole all-state population-contract replay before mutation | population-loss phase gate |
| `fallout_manual_population_contract_preflight_is_current` | Country trigger | manual source, preflight count and generation | true only after all 1,081 rows replay successfully | none; failure becomes terminal `manual_population_contract_unproven` | population-loss phase gate |

## Numerical contract

For each state, let `B` be the captured prestrike people receipt,
`C = round(fallout_pretransition_population_k * 1000)`, and `G` be the unchanged
standard Fallout grade percentage from 90 through 95. The helper computes:

1. `target_loss = round(B * 0.01 * G)`.
2. If `B > 0`, `target_survivors = max(1, B - target_loss)`; if `B = 0`, the target is zero.
3. `additional_request = max(0, C - target_survivors)`, where `C` is the frozen
   post-first-week `fallout_pretransition_population_k` used for both issue and
   replay. The live state is consulted only for the existing mutation clamp and
   observed receipt.

The preflight requires `C >= target_survivors` for every state. If native or
concurrent first-week loss has already pushed a state below the survivor target,
the transition records the terminal manual population-contract error before any
population row mutates. The system neither adds population nor silently accepts
loss above the grade contract.

The existing population transaction still clamps the request to the current
live amount above the one-person floor, performs exactly one mutation, observes
the resulting live delta, and registers that observed delta through Deaths with
state-population application disabled. A state already below its target blocks
the complete transaction and is never raised.

| Original `B` | Grade | Live `C` before rewrite | Target survivors | Additional request | Final loss from `B` |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 95% | 1 | 1 | 0 | 0 (floor) |
| 2 | 90% | 2 | 1 | 1 | 1 (50%, floor) |
| 10 | 90% | 5 | 1 | 4 | 9 (90%) |
| 1,000 | 95% | 500 | 50 | 450 | 950 (95%) |

Rounding is performed after applying the fixed-point percentage scale, matching
the existing standard helper and avoiding a large intermediate percentage value.

## Provenance and fail-closed behavior

Schema version 4 clears all manual baseline and replay fields before a new sweep.
Startup captures every state before the first native strike callback, storing
both the `k` and people forms of the baseline. Capture counts exactly 1,081 rows
and writes one generation-bound completion receipt. Batch, verifier, countdown,
and active-runtime checks use that O(1) receipt rather than repeating an all-state
collection scan. After the direct first-week loss, each
struck state records the observed baseline-to-live loss, post-loss population,
reconciled total, and the same generation token. The rewrite trigger requires:

- manual pretransition request source;
- current manual schema and generation;
- a nonnegative prestrike baseline;
- a nonnegative first-week observed loss; and
- a nonnegative first-week after-population and a reconciled total equal to the
  original baseline (`baseline = after_population + loss`); and
- matching generation values for both receipts;
- replayed `prestrike_people = round(prestrike_k * 1000)`;
- replayed `first_week_loss = max(0, prestrike_people - after_population)`; and
- frozen post-seven-day population at or above the grade survivor target.

Before the population phase iterates mutation rows, one all-state preflight
replays the arithmetic and freezes each accepted row's source values, target,
and requested additional loss. A missing, stale, corrupt, or overshot receipt
registers `fallout_transition_error_code.manual_population_contract_unproven`
and suppresses every population mutation. This code is not part of the ordinary
recoverable population-loss signature, so unreconstructable provenance cannot
enter a clear-and-retry loop. Final generic population receipts must retain the
matching manual preflight row and requested-loss value.

## Deaths and transition integration

The first-week manual aggregate continues to mutate each struck state with
`apply_exact_state_civilian_population_loss` and then sends one aggregate
thermonuclear Deaths entry, preserving the existing event-log volume and map
accounting. The seven-day request still enters the normal Fallout transition.
Only the two standard population-intent call sites branch to the manual helper.
The manual preflight is a terminal source-integrity gate, while successful rows
continue through the shared receipt, one-person-floor, owner, controller, and
ordinary transaction logic.

The standard grade constants and the seven-day countdown are unchanged. The
manual source is still unregistered and no runtime activation is implied.

## Validation and limitations

- Source inspection checked the offline wiki pages for variables, scopes,
  effects, triggers, event targets, and rounding, plus the installed vanilla
  effects/triggers/script-constants documentation.
- Static formula checks cover empty states, one- and two-person floor cases,
  an exact 90% case, an exact 95% case, overshoot refusal, and replay binding;
  no Hearts of Iron IV process was run.
- Existing unrelated strategic-singularity changes in the world-end files were
  preserved byte-for-byte outside the two population call-site edits.

The manual sweep remains dormant because native every-valid-province execution
and live engine acceptance are still unproven. The capture and population-phase
passes each traverse all 1,081 states once per transaction attempt. Callback-time
baseline validation is O(1), but runtime timing, save interruption, and
multiplayer behavior remain follow-up validation surfaces.
