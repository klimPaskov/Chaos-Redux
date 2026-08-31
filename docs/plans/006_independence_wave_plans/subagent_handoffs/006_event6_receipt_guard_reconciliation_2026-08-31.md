# Event 006 receipt-guard reconciliation

Date: 2026-08-31 (Europe/Kyiv).

Owner: parent implementation pass.

## Scope

This handoff closes the documentation gap identified by the 2026-08-31 Event 006 completion audit. It records source-existing receipt and identity gates without changing gameplay, central admission, or the absolute no-pre-event boundary.

## Source evidence

- `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt` keeps `has_independence_wave_komi_command_roster` behind `independence_wave_iw_050_identity_rights_cleared` before publishing the generation-owned Komi roster and command-roster receipts. IW-050 remains package-local and absent from central adapter, attestation, preflight, normal, SCN-008, and deterministic Join surfaces.
- `common/scripted_triggers/006_independence_wave_mediterranean_package_triggers.txt` requires `is_independence_wave_package_content_active = yes` in `is_independence_wave_cor_package`, `is_independence_wave_arx_package`, and `is_independence_wave_asx_package`. The existing setup and cleanup receipts therefore remain the package-content boundary for COR, ARX, and ASX downstream consumers.
- `common/decisions/006_independence_wave_mediterranean_decisions.txt` retains the matching setup-receipt cancellation guards for the COR, ARX, and ASX founding missions, as recorded in `006_event6_mediterranean_receipt_audit_2026-08-26.md`.

## Disposition

No gameplay edit was made by this reconciliation. No adapter, attestation, preflight, Join entry, automatic weight, cost, route, category, queue, pressure, history, or other pre-event surface changed. The Event 006 boundary remains 32 content-attested selectable packages, 29 compatible reservation groups, 40 runtime adapters, and 161 unattested selectable rows out of 193 non-overlay rows. The whole-event disposition remains HOLD / PARTIAL.

## Validation and limitations

The existing focused source validators remain the relevant evidence: allocator, country API, strict flag-family, FORM-16, and SCN-008 scenario-matrix checks. No new engine or live-runtime claim is made. Current Event MCP inspection/render is unavailable through `Transport closed`/timeout, and the required typed probability comparison remains blocked by the probability-adapter error. The exact patch-owner handoff for IW-050 is `006_iw050_komi_roster_checkpoint_identity_guard_2026_08_30.md`; the Mediterranean mission-lifecycle handoff is `006_event6_mediterranean_receipt_audit_2026-08-26.md`.
