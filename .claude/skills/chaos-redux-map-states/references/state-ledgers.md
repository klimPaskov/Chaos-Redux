# State ledgers: civilian transfers, cohort registries, reception, and map projections

Read this when work moves people between states, keeps cohorts that outlive one effect chain, tracks reception on a state and its owner country, or projects those flows onto a state map mode.
The live consumers are the exact civilian transfer primitive (`docs/systems/civilian_transfer_system.md`, `common/scripted_effects/civilian_transfer_effects.txt`), migration (`docs/systems/migration_system.md`, `migration_core_effects`, `migration_cohort_history_effects`, `migration_adapter_effects`), exact camp cohort transfer (`docs/systems/camp_exact_cohort_transfer.md`), and the state map modes (`docs/systems/state_map_modes.md`, `common/map_modes/chaosx_state_map_modes.txt`).
Read the owner document for the system you extend.
A new owner submits proof to the transfer owner; it does not write a second movement path.
Causes, event prose, historical identities, decision ids, and owner balance stay in the owning system.

Shared tuning goes in `common/script_constants/`, the contract in `common/scripted_effects/` and `common/scripted_triggers/`, lifecycle seams in bounded `common/on_actions/` hooks, and projections in `common/map_modes/` with scripted localisation.

## Scope and temporary-variable rules

- Normal variables belong to their scope. Temporary variables have no scope prefix, so `ROOT.some_temp` and `PREV.some_temp` point nowhere. Use scoped normal variables for durable state and country ledgers, event targets for a short pointer, and explicit outputs for a cross-scope handoff.
- Before each scripted-helper call, preinitialize every temporary output consumed after the return (including outputs forwarded through nested helpers) to zero or its invalid sentinel in the caller's chain; the child modifies that inherited storage. Do not assume an output first created inside a helper survives return. See [Helper output lifetime](../../chaos-redux-events/references/scripted-systems-and-country-integration.md#helper-output-lifetime).
- Helpers reset public outputs at entry and clear one-shot input envelopes on both success and rejection, without erasing published results before the caller reads them.
- Regular event targets suit a destination or the current chain because the engine clears them when the originating effect chain ends. Use a global event target only for an intentional long-lived pointer, with explicit clear and stale-target handling. A target name is never a cohort id.
- Keep state effects in state scope and country effects in country scope; measure and update each ledger in its owning scope instead of relying on `OWNER`, `CONTROLLER`, `ROOT`, or `FROM` surviving nested scopes. Use `state_population_k` for arithmetic.

## Exact transfer contract

One helper is the sole owner of physical movement. Owners submit proof (route, actor, amounts, reason); they never debit or credit population themselves.

1. Validate a positive request, origin state, destination state, route proof, actor proof, and any protected floor before mutating. Default outputs to zero or invalid and fail closed on missing or ambiguous proof.
2. Save the destination target only after entering the actual destination state scope.
3. Read `state_population_k` before the debit, convert with the shared people-per-thousand constant, subtract the protected minimum, clamp the request, and run the existing exact state-loss helper exactly once.
4. Measure the actual origin debit from before and after population. The requested amount is not the debit, because floors, rounding, and engine reconciliation change it.
5. Clamp route deaths to the actual debit, compute `survivors = actual_debit - route_deaths`, and credit only survivors, measuring the destination credit before and after.
6. Reconcile observed owner or controller manpower side effects with the established correction pattern. `add_manpower` is state-local in state scope and country-wide in country scope.
7. Record route deaths as a slice of the same debit and call the Deaths surface once; a death log never triggers a second debit.
8. Keep a conservation residual `actual_debit - route_deaths - actual_destination_credit`. Accept a transaction only when it is zero, after bounded engine rounding is handled.

Return actual debit, route deaths, survivor credit, destination credit, residual, and a valid or invalid result. Clear one-shot request variables after success and rejection so stale proof cannot replay.

## Sparse aligned cohort registry

Cohorts that outlive one chain use a sparse registry, never a world scan. Parallel arrays form one row: id, original state, current host, destination, owning country, amount, source, lifecycle status.

- Every append, update, and removal touches every array at the same index. Initialize every array and count once; keep the count equal to the id array length.
- Identity is a monotonic id. Indexes are an implementation detail that shifts on removal.
- A new row may hold the origin as a placeholder destination, but status must stop it being treated as bound.
- Resolve by explicit id first. A state- or country-derived selection is valid only when exactly one row matches; ambiguity, a missing row, a stale target, or invalid ownership fails closed.
- Bind a destination only from the actual destination state scope, updating destination, host, and status together. A nonterminal row can rebind destination and host only; origin, owner, survivors, source, and history are preserved.
- Retire a row only through an explicit terminal transaction or invalidation rule, never because its origin recovered.
- Process registered active states and countries through bounded hooks. No unscoped `on_daily`, `on_weekly`, `on_monthly`, `every_state`, or `every_country` registry maintenance.

Row status distinguishes active, destination-bound, unsafe-bound, integrated, resettled, returned, and retired as needed. A status change is metadata; the people have already moved in the owning transaction.

## Reception and outcome accounting

- Reception capacity lives on the receiving country; reception load lives on both the destination state and the receiving country. State load says how many are in the state; country load and capacity say what the country can receive overall. Do not substitute one for the other.
- Apply a reception delta exactly once per accepted survivor transaction. A credit raises both ledgers by the same actual survivor amount; a debit is valid only if both can cover it, otherwise neither changes. Refresh overcrowding flags and modifiers after the symmetric update.
- Integration, resettlement, and return are accounting projections, not population creation. Record the actual survivor amount and cohort status, and never call a population-adding effect to represent an outcome. If a flow ends without movement, record only the proven outcome and its cleanup marker.

## Co-located custody receipts

When an action resolves infrastructure that may share a site with administered custody, decide the receipt obligation from current site infrastructure, living custody, and actor authority, not from the action's own feature marker, and recheck it at execution. An open administered site with infrastructure or living custody needs a valid closure or release receipt. Invalid or misaligned living rows, a closed site with live custody, lost authority, or a stale target refuse cleanup and rewards and refund any paid cost. A closed-empty unrelated site may keep its infrastructure, and a truly facility-only target takes its own resolution path. Test valid and invalid living rows, closed-live, closed-empty, facility-only, and capture or stale-target cases.

## Transaction-time map projections

- Global cohort arrays are ledgers, not mapmode inputs. When a map mode needs origin, outflow, trapped, destination, reception, overload, route status, return, integration, or resettlement, write a state-local projection flag and amount at the validated transaction boundary. Never scan global arrays during map refresh.
- Scripted map modes have two layers: the bottom for the primary state role, the top for a critical border or route status. Keep `type = state`, evaluate the current state through `FROM`, centralize colors and thickness in script constants, and use `far_text = country`, `near_text = state`, and `update_daily = yes` where the owner requires them.
- The engine has no route-arrow layer. Show movement with endpoint projections, border emphasis, and scoped tooltips. Choose a deterministic primary-role priority for overlapping flags and expose secondary roles in tooltip text.
- Gate exact ledgers, capacity, source, cohort amounts, and outcome totals to the state owner or controller; other viewers get qualitative stage or role text. Distinguish state-local load from owner-country totals in every authorized tooltip, and clear or default every value when the registration retires.

## No double counting

Trace every population-changing call site and prove that each accepted movement has exactly one origin debit and at most one measured destination credit. These stay separate: the physical origin debit, the route-death slice of it, the survivor credit, the state and country reception deltas, and the cohort outcome totals and projection flags. Owner adapters submit proof only; outcome and projection helpers change ledgers, flags, modifiers, or metadata but never create the population they describe. A failed route, invalid destination, failed credit, or failed reception delta leaves the physical and accounting ledgers unchanged.

## Validation and handoff

- One physical loss helper owns all movement debits; Deaths logging is not a second debit.
- Aligned arrays share append, update, and removal sites, and every read variable has initialization and cleanup.
- No whole-world scan; every registry processor is bounded to active entries or an explicit lifecycle callback.
- Route targets come from the destination state scope; stale or ambiguous cohort resolution fails closed.
- Reception deltas are symmetric; map projections are written by validated transactions.
- Map mode definitions use supported layers and state scope, and public versus authorized tooltips match the projection data.
- Scenarios: movement with no deaths, with route deaths, protected-floor clamping, blocked route, partial or failed credit, reception credit and debit, ambiguous selection, safe and unsafe binding, rebind, terminal resolution, state-control or annexation cleanup.
- For dated historical scenarios, reconcile totals against documented causes, rescue or deportation, custody, outside losses, and policy timing. Quarantine controller-only or incomplete scenarios as negative controls; do not use them for acceptance or death-rate tuning.
- Use the owning MCP inspect, render, and compare tools where supported, or record the exact unavailable route. Source review is not runtime evidence.

The handoff lists changed files, public helper names, scope and target contracts, aligned-array fields and statuses, conservation evidence, projection fields and privacy rules, skipped checks with reasons, blockers, and parent-owned wiring.
