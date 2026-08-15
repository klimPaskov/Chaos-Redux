# Event 006 adapter and attestation parity audit (2026-08-12)

## Disposition

The central runtime registry was structurally fail-closed and internally consistent at the pre-IW-044 authority of 38 runtime adapters, 30 content-attested packages, 27 compatible reservation groups, and 163 unattested selectable rows.

Superseded current-authority note (2026-08-13): the IW-044 promotion raises the live boundary to 39 adapters, 31 content-attested packages, 28 compatible reservation groups, and 162 unattested selectable rows. The parity conclusions and eight adapter-only IDs remain valid; the counts above are the pre-IW-044 snapshot.

No package was promoted by this audit.

## Registry parity

`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` contains 38 exact adapter IDs and 30 exact content-attestation IDs.

The adapter-only set is exactly `IW-013`, `IW-015`, `IW-043`, `IW-058`, `IW-093`, `IW-098`, `IW-177`, and `IW-179`.

There are no attested IDs missing from the adapter list.

`is_independence_wave_runtime_package_preflight_ready` requires both the adapter trigger and the content-attestation trigger before its origin and identity gates can pass.

## Dispatcher phase parity

`common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` exposes 24 shared family wrappers.

Each family appears exactly once in all three central phases: package setup, final validation, and cleanup.

The 24 wrappers intentionally cover the 38 package IDs through family adapters; wrapper count is not a package-admission count.

## Historical pre-IW-044 package boundary

At the pre-IW-044 snapshot, the Join and allocator surfaces used only the exact 30-ID attestation set for execution.

The eight adapter-only packages remain registered for future audits but cannot execute through the preflight gate.

This audit does not resolve package-specific identity, flag, portrait, formable, AI, or MCP evidence blockers for those eight rows.

## Evidence and limits

The parity check is source-level evidence from the then-current files: adapter IDs, attestation IDs, preflight conjunction, and setup/final-validation/cleanup wrapper sets were parsed from that pre-IW-044 snapshot.

The required current `hoi4.event_inspect` namespace scan was attempted against workspace `mod_chaos_redux_ea3b2d67c2c0` and returned `ARTIFACT_MANIFEST_INVALID` / `Artifact provenance manifest is invalid` before scanning.

No live release, save/load, engine compile, MCP artifact, or quantitative probability claim follows from this audit.
