# Event 006 dispatch parity audit — 2026-08-12

## Superseding IW-040 promotion note

The IW-044 promotion supersedes the pre-promotion counts in this handoff. Current parity is 39 runtime adapters, 31 content-attestation IDs, 24 central dispatcher families, 31 Join wrappers, and 28 compatible reservation groups. The eight adapter-only IDs remain unchanged.

## Scope

This bounded source audit protects the current Event 006 fail-closed package boundary. It does not promote a package, alter the allocator, or claim live engine evidence.

## Checks

At the pre-IW-044 snapshot, `.tools/audit_event6_allocator.py` verified the exact 38 runtime adapter IDs, the exact 30 content-attestation IDs, the eight adapter-only fail-closed IDs, the requirement that normal runtime preflight requires both gates, and setup/final-validation/cleanup parity for all 24 central dispatcher families.

The pre-IW-044 adapter-only set was `IW-013`, `IW-015`, `IW-043`, `IW-058`, `IW-093`, `IW-098`, `IW-177`, and `IW-179`. The dated attested closure was 30 packages across 27 compatible reservation groups, with IW-040 immediately after IW-038 and before IW-033 in deterministic Join priority.

## Result

`python -B .tools/audit_event6_allocator.py` passed at that pre-IW-044 snapshot with 149 publishers, 126 automatic/high-chaos selectable rows, 138 SCN-008 ranked rows, 30 content-attested packages, 27 compatible groups, and the existing static 20-package witness. The ladder was already 3/4/5/7/10 with World Collapse at 10.

The parity assertions are static source evidence only. They do not replace package-specific identity, portrait, flag, formable, AI, probability, MCP, live execution, or save/load evidence, and they do not widen the content-attestation gate.
