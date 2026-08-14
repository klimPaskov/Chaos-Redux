# Event 006 simplifications current-authority repair reconciliation

Date: 2026-08-14.

## Scope

This documentation-only check was limited to `docs/specs/006_independence_wave_specs/quality/simplifications_omissions_and_blockers.md` and this handoff.

## Disposition

The 2026-08-14 current authority override was accurate for 40 runtime adapters, 32 content attestations, 29 compatible reservation groups, 161 unattested rows, the `3/4/5/7/10` ladder, HOLD/PARTIAL status, the post-`42b18cf8c` focus receipt, and package-local Komi fail-closed status.

The override was stale because it did not record the committed NAV/GLC founding serialization and project-readiness repair in `fe7fd3925`.

The override was stale because it did not record the five-branch evolution removal-tail cleanup in `7a4e0d7a9`.

The override now records the existing Komi codify/corridor lifecycle repair `65da64229`, strategic/lifecycle hardening `85f5c9778`, and lifecycle/cost/tooltip repair `b8aa313a8` as package-local corrections.

No counts, admission gates, fail-closed blockers, deterministic Join entries, or historical sections were changed.

## Evidence disposition

`fe7fd3925` adds active-founding-mission guards to NAV and GLC activation and routes their paid projects through package-readiness helpers without central admission or Join widening.

`7a4e0d7a9` clears each matching evolution pending flag on inactive or disabled removal while preserving the enabled event branch, with focused Event MCP inspect/render still partial and zero selected blocking diagnostics.

The Komi repairs distinguish durable codification from the separate corridor lifecycle, harden project readiness and strategic costs, and reconcile durable-flag cleanup, emergency affordability, and codify tooltip wording while retaining package-local fail-closed status.

## Remaining limitations

The whole Event 006 boundary remains 40/32/29/161 and **HOLD / PARTIAL**.

NAV/GLC remain adapter-only and fail-closed, and Komi remains absent from central adapter, attestation, preflight, and deterministic Join surfaces.

The shared focus receipt remains partial/HOLD with authored and unrelated diagnostics, and live runtime, save/load, typed probability, portrait, flag, and broader package blockers remain unresolved where documented.

## Validation and boundaries

Targeted searches checked `fe7fd3925`, `7a4e0d7a9`, `65da64229`, `85f5c9778`, `b8aa313a8`, NAV/GLC founding readiness, evolution removal cleanup, Komi lifecycle wording, current counts, and fail-closed admission terms.

`git diff --check -- docs/specs/006_independence_wave_specs/quality/simplifications_omissions_and_blockers.md` was run after the prose-only patch.

No gameplay, assets, portrait archive, workbook, spreadsheet export, or other documentation file was changed by this authority check.
