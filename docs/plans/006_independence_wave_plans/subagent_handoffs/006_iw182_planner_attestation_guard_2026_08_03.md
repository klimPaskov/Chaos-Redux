# IW-182 GZX planner attestation guard — 2026-08-03

The region-14 GZX weight publisher now mirrors the admitted-package execution-id/content-attestation gate. It sets `independence_wave_execution_package_id` to `iw_182` before evaluating the candidate and requires `has_independence_wave_runtime_package_content_attestation_for_execution_id = yes`.

This keeps the dormant GZX shell out of the frozen allocation until its identity, portrait rights, gameplay package, and independent post-wire audit are promoted. No tag, state, territory, force, or release fallback was added.

Validation target: `python -B .tools/audit_event6_allocator.py` must continue to report the existing 14 admitted packages and fail closed for GZX rather than counting it as a release witness.
