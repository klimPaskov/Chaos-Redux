# IW-038 Ruthenia cleanup route-flag hardening — 2026-08-12

## Scope

This bounded patch hardens the admitted IW-038 Ruthenia package cleanup without changing its route availability or central admission state.

## Source change

`common/scripted_effects/006_independence_wave_ruthenia_package_effects.txt` now clears `independence_wave_radical_sovereignty_route_excluded` during `independence_wave_cleanup_iw_038_ruthenia`.

IW-038 setup intentionally sets this shared exclusion while clearing the radical-route availability flag. The shared generation reset clears the availability flag and other generation state, but does not clear the exclusion marker. Without the package cleanup clear, an ordinary RUT lifecycle or a later Event 006 generation could inherit a stale radical-route lock.

The change matches the cleanup symmetry in the other admitted packages that use this shared exclusion. It does not enable the radical route; it only removes the package-owned exclusion during cleanup.

## Validation and limits

The source scan now finds every package file that sets `independence_wave_radical_sovereignty_route_excluded` also clears it in its cleanup surface. The touched effect file has balanced braces.

At the pre-IW-044 snapshot, the allocator, SCN-008 scenario matrix, strict flag audit, GUI matrix, and protected-tag audit were passing at 30 content-attested packages, 27 compatible reservation groups, and 38 runtime adapters; current Event 006 routing is 31/28/162/39.

The required fresh Event 006 MCP trace remains blocked before source inspection by `ARTIFACT_MANIFEST_INVALID` (`Artifact provenance manifest is invalid`) in workspace `mod_chaos_redux_ea3b2d67c2c0`; no current engine trace/render or live HOI4 claim is made.
