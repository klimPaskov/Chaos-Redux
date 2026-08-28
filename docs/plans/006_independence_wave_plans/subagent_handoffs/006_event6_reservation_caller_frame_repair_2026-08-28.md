# Event 006 reservation caller-frame repair — 2026-08-28

## Status

Bounded source repair complete for the Event 006 package reservation transaction. This handoff covers only temporary-variable lifetime at package load, reservation, host-capacity, and finish boundaries; it does not widen package admission, change costs or AI weights, reintroduce a pre-event surface, or claim live execution.

## Evidence and source review

The offline Paradox wiki `Data structures` page states that a temporary variable must already exist in the caller block before a nested scripted effect writes it when the caller needs the value afterward. The same caller-frame pattern is used by vanilla `common/scripted_effects/013_natural_disasters_effects.txt` for nested scoring values.

Event 006 package publishers load candidate metadata, call `independence_wave_begin_package_reservation`, then reserve the anchor and optional states before `independence_wave_finish_package_reservation`. The reservation helper publishes country/anchor receipts, highest territory, rejection reason, planner state metadata, and setup package id. The host-capacity helper publishes `independence_wave_host_can_lose_state`, which its three state-reservation consumers read after the nested call.

## Changed files

- `common/scripted_effects/006_independence_wave_effects.txt` seeds the automatic selector's reservation transaction outputs before regional random selection.
- `common/scripted_effects/006_independence_wave_package_planner_effects.txt` seeds the optional-territory dispatcher contract and the anchor/compact/extended host-capacity result.
- `common/scripted_effects/006_independence_wave_join_effects.txt` seeds the Join package probe contract before dynamic package dispatch.
- `common/scripted_effects/006_independence_wave_scenario_effects.txt` seeds the SCN-008 ranked package contract before loader and reservation dispatch.
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` records the repair as current source authority.
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md` records the repair for continuation.

## Validation

- `python -B .tools/audit_event6_allocator.py --strict` passed with 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, 40 adapters, 32 attested packages, and 29 compatible reservation groups.
- `python -B .tools/audit_event6_country_api.py --strict` passed with zero missing or duplicate carriers.
- `python -B .tools/audit_event6_flags.py --strict` passed with 102 complete flag families.
- `python -B .tools/audit_event6_form16.py --strict` passed.
- `python -B .tools/audit_event6_scenario_matrix.py` passed all 32 scenario cells and 8 edge cases.
- Focused source assertions passed for every automatic, optional-territory, Join, and SCN-008 reservation caller and all three host-capacity consumers.
- Required Event MCP inspect and render retries returned `ARTIFACT_MANIFEST_INTEGRITY_FAILED` with zero artifacts because the artifact provenance manifest does not match its immutable address.

## Boundary and remaining risks

The accepted Event 006 boundary remains 32 content-attested packages across 29 compatible reservation groups, 40 runtime adapters, and 161 unattested selectable rows, with the `3/4/5/7/10` automatic ladder unchanged. Nothing is visible before Event 006 fires. The whole event remains HOLD / PARTIAL because unattested package implementation, asset and identity gates, typed probability evidence, MCP artifact recovery, and live/save-load evidence are still outstanding.

No staging or commit was performed by this handoff.
