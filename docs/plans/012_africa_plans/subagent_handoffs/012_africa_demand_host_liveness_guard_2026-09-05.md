# Event 012 demand host-liveness guard handoff — 2026-09-05

Status: `implemented`.

The active Gods of Africa demand contract now validates the current host's live Event 012 flags through `event_target:africa_host` before any participant payment, negotiation, substitute, or partial-payment trigger can succeed.

This closes a narrow stale-response race: a participant may retain the old generation pointer for the short interval before the host-loss or settlement cleanup executes, but a defeated or already-settled unifier can no longer receive a late tribute debit through the participant decision surface.

## Changed surface

- `common/scripted_triggers/012_africa_gods_triggers.txt`: `gods_of_africa_demand_contract_is_current` and the participant-safe host predicate now check the live Event 012 host before validating a frozen contract or participant action.
- `common/decisions/012_africa_gods_decisions.txt`: participant demand, defiance, preparation, and reconciliation surfaces use the participant-safe host predicate for both visibility and availability.

The participant-side guard uses the shared current-host predicate plus the host's active, activation-committed, non-capitulated, and non-settled flags instead of the host-only `gods_of_africa_active_host_is_valid` trigger, whose ROOT comparison is intentionally restricted to host scope.

The same participant-safe predicate now gates participant demand, defiance, defensive-preparation, and reconciliation availability/visibility; frozen substitute-slot triggers inherit the active-demand check through `gods_of_africa_demand_contract_is_current`.

The cleanup-only `gods_of_africa_demand_contract_can_resolve` trigger remains unchanged, so owner-local expiry and host-loss cleanup can still close an already-invalid contract without needing the defeated host to pass the active-host gate.

## Validation evidence

Read-only `hoi4_event_inspect` lint for `chaosx.nr12.603` returned `status: ok`, `code: EVENT_INSPECTED_PARTIAL`, and no blockers after the edit; aggregate validation remained false only because the service deferred workspace-wide helper and lifecycle projections.

The existing vanilla Elephantry decision is unaffected: `chaosx_elephant` continues to use `sprite = elephantry`, with no custom entity or model route introduced by this repair.

## Remaining boundary

Live-save timing around host capitulation and final settlement remains a user-owned runtime check; this source guard is an additional fail-closed protection and does not claim live gameplay completion for Event 012.
