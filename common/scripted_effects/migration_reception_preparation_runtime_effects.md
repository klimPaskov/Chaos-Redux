# Sparse prospective reception runtime

All helpers below run in the exact origin STATE supplied by the existing registered-displacement-state scheduler.
The ordinary origin OWNER is saved explicitly; global-host ROOT is not the requester.
Public temporary outputs must be predeclared by callers and are reset to zero/invalid at helper entry.

| Helper | Inputs | Outputs and side effects | Caller |
| --- | --- | --- | --- |
| `migration_spontaneous_reception_stage_or_reuse` | Current bounded request/movable amount, saved actual origin owner, aligned current cohort ledger | `migration_spontaneous_reception_row_result`; stages one ordinary active unbound row only when none exists, or reuses the exact retained/current ordinary row; persists private cohort ID and returns actual whole row amount in request; no population/load/destination change | Submit and retained-row retry |
| `migration_spontaneous_reception_submit` | Both normal selectors returned zero, exact origin target and current request | `migration_spontaneous_reception_result`; complete preparable foreign draw, exact staged/reused row, new monotonic contract generation, matching country mirrors | Spontaneous owner and retained-row retry |
| `migration_spontaneous_reception_try_normal_destination` | Retained unmoved ordinary row and current request/floor | Normal selector result and owner movement result; reruns normal internal-first/foreign-safe selection, transfers only a full row with real current headroom; never makes another row | Retained-row retry |
| `migration_spontaneous_reception_process_owned_row` | Private exact cohort ID and live contract | Owner result; pending blocks duplicate attempts, accepted ordinary offer transfers on existing sparse schedule independently of attempt cooldown, successful measured passage immediately completes/cleans contract; terminal retries obey existing cooldown | `migration_process_spontaneous_movement_owner` |

Rows must be active, positive, uniquely hosted at their original state, and owned by that state's actual current owner/controller.
Only ordinary `internal_displacement` and `cross_border_flight` sources are reusable; custody, scenario and externally owned rows are not appropriated.
Flight pressure, outstanding flight population and live movable population must cover the full amount.
Malformed, ambiguous, stale or changed-authority rows stay fail-closed for the existing reconciliation owner rather than being replaced.
At owned-row processing entry, the private pointer may clear only when its positive ID is positively absent from aligned authoritative cohort IDs, the existing reconciled local live count is explicitly zero, local ambiguity/misalignment markers are absent, and no active contract matches that ID.
The existing authoritative terminal row-removal owner refreshes origin/host selector caches before this check.
The prune changes only `migration_spontaneous_reception_cohort_id`; it never deletes/resizes a row or clears flight/trapped pressure or contract fields.
If the pointer clears, the retained-row branch is skipped and the caller returns to the existing fresh ordinary path; an unrelated active contract still blocks that path through readiness.
Present live/malformed IDs, misaligned arrays, unknown/nonzero local count, ambiguous state or matching active contract retain the pointer and fail closed.
A present private pointer must be positive before `stage_or_reuse` invokes the core resolver.
Present zero/negative pointers stay in that explicit branch and return the initialized zero result without resolver, implicit current-row fallback or new-record branch, even when another valid current row exists.
No row is bound to the proposed front, no people are debited, and no host load is credited while pending.

The source retains the same cohort across rejection/expiry and allocates a fresh corridor generation for each new attempt.
A failed submission after preparation terminates only that new contract and preserves the row/flight/trapped obligation.
The next eligible attempt reruns normal internal-safe priority before considering preparable foreign states.
The optional one-shot `migration_destination_selection_required_people` input supplies the full retained/fresh request before both normal weighted passes, so every inadequate internal/foreign state contributes zero weight before the draw.
The general selector clears that input only after both pools complete; other callers default to zero and retain their prior candidate contract.
If post-selection current facts nevertheless reject execution, the result is cleared before a preparable fallback, and the row is never silently split or duplicated.
Accepted ordinary passages use the exact shared transfer/finalizer and spontaneous-exodus projection role, record protection evidence before cleanup, and skip manual corridor mission arming and manual full-term famine achievement starts.
The existing cooldown is refreshed after actual success; no new timer or job is introduced.
Manual organized corridor missions retain their prior behavior.

Regular targets are `migration_spontaneous_reception_origin`, `migration_spontaneous_origin_owner`, `migration_reception_preparable_front`, `migration_destination_selection_actor`, `humanitarian_corridor_requester`, and the existing exact civilian route targets.
Only the private cohort ID persists beyond the chain, and successful movement clears it while preserving the authoritative moved cohort, state/country reception ledgers and transfer projections.
No CXT grants, event IDs, world scan, GUI, asset or new canonical value is added.
