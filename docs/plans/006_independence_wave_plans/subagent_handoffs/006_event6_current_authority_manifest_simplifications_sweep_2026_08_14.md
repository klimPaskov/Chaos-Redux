# Event 006 current authority, manifest, and simplification sweep

Date: 2026-08-14.

## Scope

This docs-only sweep reconciles `overview.md`, `006_source_of_truth_map.md`, `006_independence_wave_resume_packet.md`, `quality/package_manifest.md`, and `quality/simplifications_omissions_and_blockers.md` against the current IW-045 authority.

No gameplay, localisation, asset, workbook, central-admission, or deterministic-Join source was edited.

## Current disposition

The current boundary remains 32 content-attested packages across 29 compatible reservation groups, 161 unattested selectable rows, and 40 runtime adapters, with the whole event **HOLD / PARTIAL**.

IW-045 BSK remains centrally admitted and appears in deterministic Join order after IW-044 and before IW-033.

IW-047 MEL and IW-050 KOM remain package-local and fail-closed, with no central attestation or deterministic Join entry, and MEL's current FORM-12/13 consumer rebind is state 833 while state 256 is historical traceability.

The active automatic ladder remains `3/4/5/7/10`, with World Collapse also targeting `10`.

The latest Komi administration-standard cost/localisation repair is owner commit `8b1aaeaae`; read-only re-audit commits `d84816ecc` and `3ad93a39d` confirm its current disposition without widening admission.

## Files changed

- `docs/events/006_independence_wave/overview.md`
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`
- `docs/specs/006_independence_wave_specs/quality/package_manifest.md`
- `docs/specs/006_independence_wave_specs/quality/simplifications_omissions_and_blockers.md`
- This handoff.

The current-facing blocks now link the latest Komi repair and re-audit receipts and state the MEL/KOM package-local boundary explicitly.

## Historical and unresolved boundaries

Dated 39/31/28/162 and earlier package arithmetic remains historical traceability and was not rewritten.

The older Komi cost finding is superseded by the current cost-localisation repair and re-audit handoffs; no historical decision-audit section was edited in this sweep.

Portrait, flag, typed probability, runtime, package-admission, and whole-event completion blockers remain open under their owning handoffs.

## Validation

`git diff --check` was run against the five scoped authority and quality documents.

Targeted searches confirmed the current 32/29/161/40 boundary, BSK Join placement, MEL/KOM exclusion, `3/4/5/7/10` ladder, and Komi commits `8b1aaeaae`, `d84816ecc`, and `3ad93a39d`.

No commit was created because the parent requested a shared-worktree docs-only reconciliation.
