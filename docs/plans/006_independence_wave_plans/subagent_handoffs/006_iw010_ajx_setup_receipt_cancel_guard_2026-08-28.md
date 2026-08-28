# IW-010 Saar setup-receipt and founding-mission guard handoff

Date: 2026-08-28.

Owner: parent Event 006 implementation agent.

Scope: admitted IW-010 Saar (`AJX`) founding-mission lifecycle only.

The AJX category now requires `independence_wave_iw_010_setup_complete` before it is visible.

The `independence_wave_ajx_hold_saar_compact_together` cancellation trigger now closes the mission when the setup receipt is absent.

The mission success branch now requires the AJX package, setup receipt, stable compact values, and controlled capital before setting `independence_wave_ajx_compact_crisis_resolved`.

The Saar mission description now tells the player that capital control is required, without exposing the technical receipt flag.

Changed files:

- `common/decisions/006_independence_wave_rhineland_bavaria_saar_decisions.txt`
- `common/decisions/categories/006_independence_wave_categories.txt`
- `localisation/english/006_independence_wave_saar_l_english.yml`
- `docs/events/006_independence_wave/northern_western_europe_packages.md`
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`

The repair mirrors the accepted IW-008/IW-009 setup-receipt precedent in commit `223a23007`.

No admission, reservation, allocator count, package identity, portrait, flag, asset, cost, timer, AI weight, ledger value, route, or pre-event surface changed.

Focused lifecycle assertions cover setup clear/restore, activation and category visibility, receipt-loss cancellation, receipt-and-capital success guards, cleanup, and the player-facing capital wording.

The Event 006 allocator, country API, strict flag-family, FORM-16, and SCN-008 matrix audits remain required evidence for the unchanged 32/29/40/161 boundary.

Mandatory Event MCP inspect/render and comparison remain blocked by `ARTIFACT_MANIFEST_INTEGRITY_FAILED` and `EVENT_REVISION_NOT_CACHED` respectively, so no engine or live-runtime claim is made.

No fallback or simplification was promoted.
