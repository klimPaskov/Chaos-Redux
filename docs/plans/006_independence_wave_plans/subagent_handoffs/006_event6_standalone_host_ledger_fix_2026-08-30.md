# Event 006 standalone host-ledger reference repair — 2026-08-30

## Scope

This bounded repair addresses the Event 006 standalone execution path and its committed-wave achievement initializer. It does not change package admission, allocation weights, country identities, pre-event UI, pressure, queues, costs, or release design.

## Root cause

`independence_wave_validate_execution_metadata` checked the former host against `global.independence_wave_plan_hosts`, but no such Event 006 array is populated anywhere in the runtime. The shared liberation coordinator owns the live host ledger at `global.liberation_plan_hosts`. The wrong array made the former-host validation fail closed before the release barrier, so a manually fired standalone Event 006 plan could select packages and still produce no countries.

The committed-wave achievement initializer used the same stale array name, preventing host-remnant tracking after a successful wave.

## Changes

- `common/scripted_effects/006_independence_wave_execution_effects.txt`: former-host validation now reads `global.liberation_plan_hosts`.
- `common/scripted_effects/006_independence_wave_achievement_effects.txt`: committed-wave host iteration now reads `global.liberation_plan_hosts`.

## Evidence

- `global.liberation_plan_hosts` is initialized, populated, validated, and cleaned by `common/scripted_effects/chaosx_liberation_release_effects.txt`.
- A repository-wide Event 006 search now has no `global.independence_wave_plan_hosts` references.
- Focused audits passed: allocator (149 publishers, 32 attested packages, exact 3/4/5/7/10 ladder), strict flag families (102/102), SCN-008 matrix (32 cells/eight edge cases), and country API (242 broad rows, 191 resolved carriers, zero missing/duplicate mappings).

## Limits

No live HOI4 launch, save/load, or in-game country-release claim is made here. The fix is source-backed and should be verified by the user with a fresh manual `event chaosx.nr6.1` invocation and the terminal receipt fields if the runtime still fails.
