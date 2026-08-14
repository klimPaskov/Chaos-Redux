# IW-040 Kuban cleanup route-flag hardening — 2026-08-12

> Historical IW-040-only receipt: the package cleanup correction remains part of the admitted KUB contract, while the 30/27/38 audit counts below are superseded by the current 31/28/162/39 IW-044 authority.

## Scope

This bounded patch hardens the admitted IW-040 Kuban package cleanup without widening package admission or changing its route design.

## Source change

`common/scripted_effects/006_independence_wave_kuban_package_effects.txt` now clears `independence_wave_radical_sovereignty_route_excluded` during `independence_wave_cleanup_iw_040_kuban`.

IW-040 setup intentionally sets this shared exclusion while also clearing the radical-route availability flag. The central generation reset clears the availability flag and other shared Event 006 state, but does not clear the exclusion marker. Without the package cleanup clear, an ordinary KUB lifecycle or a later Event 006 generation could inherit a stale radical-route lock.

The fix matches the cleanup symmetry already present in the admitted Montenegro, Kosovo, and Ruthenia package effects. No route is enabled by this patch; cleanup only removes the package-owned exclusion.

## Validation

Static cleanup comparison shows the IW-040 setup/cleanup pair now covers all package-owned route-lock flags; only central-generation flags intentionally remain owned by the shared reset. The touched effect file has balanced braces.

At the IW-040-only snapshot, the allocator, SCN-008 scenario matrix, strict flag audit, GUI matrix, and protected-tag audit passed at 30 content-attested packages, 27 compatible reservation groups, and 38 runtime adapters.

The required fresh Event 006 MCP trace was retried after the source edit and remains blocked before source inspection by `ARTIFACT_MANIFEST_INVALID` (`Artifact provenance manifest is invalid`) in workspace `mod_chaos_redux_ea3b2d67c2c0`; it returned zero artifacts and scanned no files. No current engine trace/render or live HOI4 claim is made.

## Remaining boundaries

This patch does not restore vanilla political laws/popularities, add a formable route, change the KUB force contract, or alter central attestation/Join lists. Those surfaces remain governed by the existing IW-040 promotion handoff and whole-event HOLD/PARTIAL authority.
