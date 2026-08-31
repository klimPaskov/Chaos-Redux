# Event 006 IW-177 planner attestation parity

Date: 2026-09-01

## Scope

The IW-177 automatic-weight wrapper in `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt` now seeds `independence_wave_execution_package_id` with the IW-177 package constant before evaluating its readiness limit and requires `has_independence_wave_runtime_package_content_attestation_for_execution_id` before loading the package or entering the candidate scorer.

## Why this is safe

The shared candidate scorer already reassigns the execution id from the loaded package and rejects any package absent from the central content-attestation trigger. This change therefore narrows the wrapper's work to the same fail-closed contract used by the adjacent adapter-only wrappers; it does not add IW-177 to the attested package set, alter weights, or widen automatic selection.

## Validation

The focused Event 006 allocator, country API, strict flag, FORM-16, and SCN-008 scenario-matrix validators all passed after the edit.

## Remaining limits

IW-177/Fiji remains adapter-only and is not promoted. Portrait/date/rights, FORM-39 member and flag receipts, central content attestation, Join coverage, probability evidence, and live Event 006 engine evidence remain unresolved. No fallback package, pre-event UI, pressure, category, queue, or gameplay admission was added.
