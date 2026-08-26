# Event 006 IW-044 founding-mission receipt guard handoff — 2026-08-26

Scope: one bounded IW-044 lifecycle repair for the Tatarstan founding mission.

Whole-event status remains **HOLD / PARTIAL**.

## Source change

`common/decisions/006_independence_wave_siberian_decisions.txt` now cancels `independence_wave_tat_hold_river_compact_together` when `independence_wave_iw_044_setup_complete` is absent.

The mission activation already requires the same setup receipt, so the cancellation block now uses the matching generation boundary.

No decision id, route, duration, effect, AI weight, cost, localisation key, admission gate, or package count changed.

## Why this is required

`common/scripted_effects/006_independence_wave_tatarstan_package_effects.txt` clears `independence_wave_iw_044_setup_complete` at setup entry and restores it only after the package preparation proof succeeds.

Before this repair, an active founding mission could survive that reset window and run its cancellation or failure path without a valid IW-044 setup receipt.

The new cancellation guard makes an incomplete or retried setup fail through the existing Tatarstan mission cleanup path instead of retaining a stale mission generation.

## Cost boundary

The Tatarstan strategic affordability trigger still requires the existing war-support floor, stability floor, civilian-factory floor, and standard diplomatic resources.

The compact Tatarstan strategic cost triplet remains unchanged and displays only the spendable stability, command power, convoy-or-train, and civilian-factory commitments.

The war-support floor is a non-spendable availability requirement and is intentionally not added to the cost string.

## Validation

The source assertion confirms that mission activation requires the receipt, cancellation now requires the same receipt, and setup clears and later restores it.

The six Event 006 static validators remain the required post-change checks: allocator, country API, strict flag families, FORM-16, GUI matrix, and scenario matrix.

Because this change touches a decision-owned event surface, a read-only `hoi4.event_inspect` and `hoi4.event_render` pass for `chaosx.nr6.1` are required after the final source state is settled.

No probability surface changed, so no balance or AI-weight conclusion is claimed.

No live Hearts of Iron IV process, save/load test, or player-owned runtime receipt was used.

## Remaining risks

The broader Event 006 decision and mission audit remains partial, and other admitted package founding missions may have analogous receipt-cancellation gaps that are outside this bounded IW-044 patch.

Central package admission, whole-event runtime execution, typed probability evidence, and other asset, formable, and super-event blockers remain unchanged.

No fallback or design simplification was introduced.
