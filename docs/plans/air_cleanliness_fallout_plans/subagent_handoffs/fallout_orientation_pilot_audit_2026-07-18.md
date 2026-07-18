# Fallout Ash-week orientation pilot audit

Status: blocked partial pilot

Audit date: 2026-07-18

Auditor: `chaosx_event_completion_auditor`

Parent disposition: reviewed and reconciled after the audit response

## Scope

The audit covered the dormant transaction substrate, events `chaosx.fallout.62` through `chaosx.fallout.65`, their localisation, dedicated assets, sprite wiring, and current documentation. Hearts of Iron IV was not run.

## Findings corrected in the same tranche

- Shared global state targets were replaced with country-owned variable scope pointers. Concurrent successor transactions no longer share one mutable target slot.
- Issued branch and issued due-day receipts now authenticate root and delayed-result work.
- National begin refuses a transaction with no affordable branch.
- One shared cleanup helper now clears transaction-owned transient variables after resolution, cleanup event 84, and stale-generation cancellation.
- Terminal cause memory now freezes from `global.fallout_cause_memory_source`. Successor country memory remains a separate typed value for future overlays.
- The exact source state now derives from `fallout_successor_assignment_capital_state` and must pass the current capital row.
- Country-proportion Deaths now traverse the stable Fallout state ledger and distribute exact population removal across all owned states before logging one country total.
- Closure validates its requested visible or hidden mode before writing a pending transaction.

## Remaining release blockers

- Events `62` through `65` have no caller and remain outside the 660-block release floor.
- Events `66` through `84` are not implemented.
- Regional, archetype, and country-memory orientation row producers are absent. Their typed approval gates remain unset.
- The exact live state-result mapping is absent. Components two through five remain blocked behind `fallout_orientation_state_result_surface_status`.
- The exact one-level infrastructure repair surface is unproven.
- The durable opening Cohesion value has no accepted authenticated producer.
- The curated character or institution registry is absent.
- Country-memory overlay text is absent from the national pilot.
- National AI choice evaluation is deterministic, shares human costs and effects, and scores each branch against the lowest resource in that branch's exact cost set. The four blocked later components still need their own reviewed branch-specific weights.
- Stale-generation reconciliation has no authorized recurring caller.
- Event-log rows, event-detail rows, evolution details, and workbook rows are absent.
- Successor materialization, player continuation, and live tag-conflict allocation are not proven, so no orientation caller may be wired.

## Count disposition

- Defined Ash-week orientation blocks: `4 of 23`
- Countable Ash-week orientation blocks: `0`
- Countable Fallout living-world blocks: `0 of 660`

No fallback was approved or used. The pilot remains blocked rather than being promoted into the release count.
