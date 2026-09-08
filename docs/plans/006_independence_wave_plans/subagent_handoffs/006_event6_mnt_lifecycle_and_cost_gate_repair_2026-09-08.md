# Event 006 MNT lifecycle and cost-gate repair — 2026-09-08

Disposition: implemented in source; live engine and save/load behavior remain user-owned validation gates.

## Scope

This narrow repair closes two concrete decision-surface defects found during the Event 006 decision audit. It does not widen package admission, add a fallback, change the pre-event presentation, or alter the accepted cost palette.

## Source changes

- `common/scripted_triggers/006_independence_wave_balkan_package_triggers.txt`
  - `is_independence_wave_mnt_project_ready` now requires `independence_wave_mnt_compact_crisis_resolved` in addition to the existing setup receipt and failure guard. Ordinary Montenegro projects therefore stay hidden until the opening mountain-compact mission resolves successfully.
  - `has_independence_wave_mnt_active_package_project` now includes `has_active_mission = independence_wave_mnt_hold_mountain_compact_together`, matching the sibling Balkan package lifecycle contract.
  - MNT administration and strategic affordability checks now use inclusive `NOT = { value < cost }` gates for command power, manpower, and stability. The one-state civilian-factory floor remains `> 0` because it represents the available factory required by the one-factory project reservation, not a stockpile debit.
- `common/scripted_triggers/006_independence_wave_decision_triggers.txt`
  - Shared administration, diplomatic, security, border, coordinated-operation, integration, and strategic affordability helpers now use inclusive `NOT = { value < cost }` gates. Exact displayed stockpiles qualify, while payments continue to debit the same constants once.
  - DM-01 predecessor gate constants and the deliberate surplus helper remain unchanged.

## Evidence and validation

- The opening mission is `independence_wave_mnt_hold_mountain_compact_together` in `common/decisions/006_independence_wave_balkan_decisions.txt` and publishes `independence_wave_mnt_compact_crisis_resolved` only on a stable, capital-controlled cancellation path.
- The sibling AXX/BOS/MAC active-project helpers already include their opening missions; MNT now follows that pattern.
- Payment effects remain in `common/scripted_effects/006_independence_wave_decision_effects.txt` and continue using the existing `*_spend` constants.
- Focused Event 006 allocator, scenario matrix, GUI matrix, country API, flag, and FORM-16 validators were already passing before this narrow source repair. Re-run the decision/lifecycle validators after review; no live-game completion claim is made here.

## Remaining limits

The DM-55 military-union contract, status GUI render conflicts, package attestation boundary, typed probability comparison, portrait rights/role gates, and live Event 006 release/transaction receipts remain unresolved or user-owned. No generic country, portrait, flag, cost, or UI fallback was introduced.
