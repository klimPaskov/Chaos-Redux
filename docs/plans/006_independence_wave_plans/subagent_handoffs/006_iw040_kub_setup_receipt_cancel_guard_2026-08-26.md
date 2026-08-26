# IW-040 Kuban setup-receipt cancellation guard

Date: 2026-08-26

## Scope

This handoff records one bounded lifecycle repair for the admitted IW-040 Kuban package.

## Defect

The `independence_wave_kub_hold_mounted_compact_together` founding mission activates only while `independence_wave_iw_040_setup_complete` exists, but its cancellation trigger previously did not test that same generation receipt.

The setup effect `independence_wave_setup_iw_040_kuban` clears `independence_wave_iw_040_setup_complete` before rebuilding the package and restores it only after `has_prepared_independence_wave_iw_040_package_setup = yes` succeeds.

Without the matching cancellation branch, an active mission could survive a setup reset or failed retry outside the generation that created it.

## Change

In `common/decisions/006_independence_wave_frontier_decisions.txt`, the existing cancellation `OR` block now includes:

```text
NOT = { has_country_flag = independence_wave_iw_040_setup_complete }
```

The existing `cancel_effect` remains responsible for the package failure path. No admission, route, cost, identity, asset, focus, or reservation logic changed.

The durable package description in `docs/events/006_independence_wave/kuban_package.md` now documents setup-receipt loss as a founding-mission cancellation condition.

## Evidence

- Mission activation requires `independence_wave_iw_040_setup_complete`.
- Setup clears that receipt at setup entry and restores it only after successful package preparation.
- The existing cancellation failure branch calls `independence_wave_kub_apply_project_failure`.
- The static targeted lifecycle assertion passed after the patch.

## Validation

- `python -B .tools/audit_event6_allocator.py` passed: 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, 40 adapters, 32 attested packages, 3/4/5/7/10 ladder, and retired pre-event crisis surface.
- `python -B .tools/audit_event6_country_api.py` passed: 242 broad rows, 191 unique carriers, 34 Soviet, 45 Africa, zero missing, zero duplicates, and IW-031 crosswalk pass.
- `python -B .tools/audit_event6_flags.py --strict` passed: 102 registered and 102 complete flag families.
- `python -B .tools/audit_event6_form16.py` passed.
- `python -B .tools/audit_event6_gui_matrix.py` passed.
- `python -B .tools/audit_event6_scenario_matrix.py` passed: all 32 SCN-008 cells and eight edge cases.
- Event MCP lint for `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics after the source change; broad helper/lifecycle projections remain deferred by the workspace artifact-manifest limitation. Revision: `744cd12bca3e5b1a25d3d012a4e58a1e2c4e3623c268724b38679e806883d9c9`; graph hash: `4b0d98848c436e8f6c8363056e3ae62cfad7785e4b2f1396ac9f1439f91de8df`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b18cee17f1014bf47ec11c0948acc2e8a53be824af5fe59f5e052c35f45960db/71d0944ea603b4e6da3fb1caf6f7bc7b18bef7db007ddb29e580cd2c3066e0e7/event-lint-744cd12bca3e.json`.

## Boundaries and follow-up

This is source-level evidence only; no live save/load or in-game runtime claim is made.

The analogous IW-038/RUT and other unpaired founding-mission receipt guards remain a separate audit queue and were not batch-edited in this tranche.

The whole Event 006 implementation remains **HOLD / PARTIAL** under the current source-of-truth map.
