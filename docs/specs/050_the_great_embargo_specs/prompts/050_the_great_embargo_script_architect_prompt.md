# Event 050 scripted-system architect prompt

Design and, when parent scope permits, implement the reusable scripted foundation for Event 050.

Read `AGENTS.md`, `chaos-redux-events`, `chaos-redux-decisions-missions`, the Event 50 specs and runtime ledger matrix, the shared dynamic trigger and effect registries, relevant offline wiki pages, current vanilla documentation, and existing Chaos Redux active-ledger patterns.

## Required architecture

Create an event-owned bounded active-crisis registry. Each crisis needs a unique sequence identity and isolated state for target, coalition, Pressure, dependence, duration, review schedule, routes, concessions, evolutions, reports, achievements, resolution, and cleanup.

Evolution II must support up to three active ledgers. One country can hold different participant roles in several crises. Do not rely on one unscoped country flag for coalition membership.

Process registered active crises and stored participants. Do not add unrestricted daily, weekly, or monthly all-country loops.

## Required helper families

Plan or implement bounded helpers for:

- target validation and selection
- active slot reservation and rollback
- coalition role selection
- practical contribution classification
- opening Pressure calculation
- hidden dependence classification
- Pressure adjustment and stage refresh
- economic impact refresh
- scheduled coalition review
- selected neutral and member targets
- smuggling and intermediary route lifecycle
- concession lifecycle
- defiance commitment and exhaustion
- Resource Seizure preparation handoff
- Evolution I secondary targets
- Evolution II additional targets and cooperation network
- target and participant invalidation
- independent crisis resolution and cleanup
- event history and evolution context handoff
- achievement receipts

Use script constants for shared thresholds and tuning when supported. Keep event-specific selectors and lifecycle helpers in Event 50-owned files. Add a shared dynamic helper only when its contract is neutral and has real cross-system callers, then update its Markdown registry in the same change.

## Failure behavior

Every public call must fail closed on missing proof or invalid scope. A failed opening transaction must release its reserved slot and queue no delayed work. Cleanup must be idempotent.

One crisis cleanup cannot remove another crisis's participant state. A convenor loss must select a replacement or move the correct crisis toward collapse. An invalid intermediary must close only its route.

## Shared boundaries

Reuse `is_special_chaos_country`, `is_actual_nonhuman_country`, and `uses_normal_civilian_systems` for broad eligibility. Do not copy their logic into Event 50.

Do not own Condemnation, Famine, Migration, Deaths, Air Cleanliness, war casualties, annexation, peace, or native DLC embargo lifecycle. Use documented owner APIs or narrow adapters.

## Handoff

List changed files, helper names, constants, inputs, outputs, defaults, side effects, call sites, rollback behavior, and cleanup ownership. Include task-specific validation and unresolved engine questions. Do not claim probability or live-runtime proof without the required tools.
