# Event 006 current documentation alignment — FORM-16 tranche

Date: 2026-08-06.

Scope: reconcile current-facing Event 006 authority documents after the core/API repair, ordinary super-event numbering, and FORM-16 source/static closure. Historical handoffs remain intact as dated evidence; this pass does not rewrite accepted design or promote blocked content.

## Files aligned

- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`
- `docs/events/006_independence_wave/overview.md`
- `docs/events/006_independence_wave/transcaucasus_packages_and_form16.md`

## Current statements made explicit

- The current package boundary remains 23 content-attested selectable packages across 22 compatible reservation groups, 170 unattested selectable rows, 32 adapters, and nine adapter-only fail-closed rows.
- The current ordinary super-event identifiers remain `23` and `24`; four-digit labels are historical traceability only.
- The workbook/catalog authority remains Event 006 `Partially Available`, SCN-008 `Unavailable`, and Liberations `Partially Available`.
- FORM-16 is source/static PASS for its existing ARM/GEO/AZR carrier and readiness surface only. Exact anchors remain 230/231/229, and consent/refusal, identity, generation, integration, rollback, stale-generation, and cleanup gates remain fail-closed.
- FORM-16 does not add a package attestation, new tag, portrait, flag, GUI, or runtime bypass. Typed probability and GUI fidelity remain bounded evidence.

## Validation

The following focused audits pass after the documentation update:

- `.tools/audit_event6_allocator.py`
- `.tools/audit_event6_country_api.py`
- `.tools/audit_event6_flags.py`
- `.tools/audit_event6_scenario_matrix.py`
- `.tools/audit_event6_gui_matrix.py`
- `.tools/audit_chaosx_country_tags.py`
- `.tools/audit_event6_form16.py`
- `.tools/export_event_catalog_csv.py`

No gameplay, asset, workbook, localisation, or registry source was changed by this alignment pass. The whole event remains **HOLD / PARTIAL** because the accepted package, formable, asset/source, probability/balance, GUI-consumer, and audio-23 gates remain open.
