# Event 006 Adapter and Attestation Parity Re-audit

Date: 2026-08-12

The source boundary in this pre-IW-040 snapshot was re-extracted from `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`.

The then-current runtime adapter gate contained 37 package IDs and the content-attestation gate contained 29 package IDs.

The exact adapter-only set is:

- IW-013 NAV
- IW-015 GLC
- IW-043 CHU
- IW-058 ASY
- IW-093 DOX
- IW-098 SOK
- IW-177 FIJ
- IW-179 FSM

There are no attestation-only IDs. `is_independence_wave_runtime_package_preflight_ready` requires both the adapter and content-attestation triggers, so these eight rows remain fail-closed without any source bypass.

At that audit point, the admitted authority was 29 content-attested selectable packages, 26 compatible reservation groups, 164 unattested selectable rows out of 193 non-overlay rows, and 37 runtime adapters. The post-IW-040 current authority is 30 content-attested packages, 27 compatible reservation groups, 163 unattested selectable rows, and 38 runtime adapters, with IW-040 immediately after IW-038 and before IW-033 in deterministic Join order.

The shared dispatcher contains setup, final-validation, and cleanup wrappers for the current family adapters, including the IW-038 Ruthenia package and the adapter-only grouped families. This re-audit found no missing central phase wrapper that can be safely added without a package-specific admission decision.

Static checks remain authoritative for this pre-promotion re-audit: allocator 149 publishers / 29 attested / 26 groups, scenario matrix 32 cells plus 8 edge cases, and flags 102/102 complete. The current post-IW-040 allocator is recorded in the source-of-truth map and promotion handoff.

Fresh HOI4 MCP evidence was attempted but remains blocked before source scanning by `ARTIFACT_MANIFEST_INVALID` (`Artifact provenance manifest is invalid`) in workspace `mod_chaos_redux_ea3b2d67c2c0`. No current engine or probability result is claimed.

This is a parity and fail-closed audit only. It does not promote any package or change gameplay source.
