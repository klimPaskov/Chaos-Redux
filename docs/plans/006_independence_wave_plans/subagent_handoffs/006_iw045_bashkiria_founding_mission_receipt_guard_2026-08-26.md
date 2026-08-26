# IW-045 Bashkiria founding-mission receipt guard

Date: 2026-08-26

## Finding

The admitted IW-045 Bashkiria founding mission `independence_wave_bsk_hold_frontier_congress` activates only while `independence_wave_iw_045_setup_complete` exists, but its cancellation trigger did not test that same setup receipt.

`independence_wave_setup_iw_045_bashkiria` clears the receipt at setup entry and restores it only after the prepared-setup proof succeeds. A failed or retried setup could therefore leave the old mission active outside its generation contract, after which its existing cancellation fallback would apply the package failure penalties.

## Patch

`common/decisions/006_independence_wave_bashkiria_mari_decisions.txt` now adds `NOT = { has_country_flag = independence_wave_iw_045_setup_complete }` to the existing `independence_wave_bsk_hold_frontier_congress` cancellation `OR` block. The activation receipt and cancellation guard are now symmetric.

## Boundary

This is a one-line lifecycle guard for the already content-attested IW-045 package. It does not alter admission, deterministic Join order, package identity, anchor state, host ledger, force mapping, focus, costs, AI weighting, localisation, assets, or the 32/161 boundary.

## Validation

Focused source assertions confirm the mission activation receipt, the new cancellation receipt guard, and the setup clear/restore ordering. `python -B .tools/audit_event6_allocator.py` passes with 32 attested packages, 29 compatible groups, 40 adapters, and the unchanged 3/4/5/7/10 ladder. `hoi4.probability_inspect` on the Bashkiria/Mari decision registry reports the existing mission weight surface without diagnostics; this patch changes no weight, so no probability comparison is applicable. Event MCP inspection/render remain partial with zero blocking diagnostics because broad workspace helper/lifecycle projections are deferred. Hearts of Iron IV was not launched, and no live parser, save/load, or runtime claim is made.
