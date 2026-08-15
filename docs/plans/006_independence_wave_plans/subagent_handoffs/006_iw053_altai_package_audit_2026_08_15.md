# IW-053 Altai package audit — 2026-08-15

## Disposition

IW-053 ALT remains registry/map-ready only and is fail-closed. No package-local gameplay, central adapter, content-attestation, normal or SCN-008 preflight, deterministic Join, portrait, flag, or country-history patch is justified by the current evidence.

## Current source evidence

- The accepted registry row is `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:54`.
- The accepted research-resolution row is `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:54`.
- The installed binding is `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:54`, using state `654` (Oyrot Region) as the compact anchor, optional state `40` (Altai Krai), host `SOV`, capital `219`, and reservation group `RG-654-40`.
- The region-05 planner contains only the dormant package loader/reservation/weight references for `iw_053`; no ALT package-local effects, triggers, decisions, ideas, AI strategy, focus hooks, or localisation family exists.
- Vanilla identity is present in `common/country_tags/00_countries.txt:215`, `common/countries/Altay.txt`, `history/countries/ALT - Altai Republic.txt`, and `common/characters/ALT.txt`. The opening vanilla characters are `ALT_grigory_gurkin` and `ALT_samuil_yufit`, but their current portrait consumers are generic Asian textures and no Event 006 source-backed portrait manifest exists.
- Vanilla ALT ideology ladders are structurally present, but no Event 006 identity/origin attestation authorizes reuse or route-specific replacement.
- Central dispatch, attestation, preflight, and Join lists contain no `iw_053` entry. Do not widen those lists from the registry row alone.
- The accepted force mapping row assigns IW-053 military tradition `61`, while the shared `006_independence_wave_force_package_constants.txt` currently exposes `p61 = 57`. This is a source-contract mismatch that must be reconciled before any ALT force setup is admitted; no silent tuning or shared-constant rewrite is made here.

## MCP evidence

Read-only map inspection covered states `654` and `40` and returned state membership/network success with unrelated global map diagnostics remaining noisy/truncated. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8e9008c9e061253b28c16f735c27244fc7f982b251b8910bea664ed5f1ec6e2d/6fa80bd61c49e1ad3682e1103be49f4dc045d74e0932850726dba6f0080c6d1d/map-inspect.633fcc8140a5342c.json`.

The selected state render passed at the same map revision. This proves installed map inspection only; it does not prove ALT package readiness, identity rights, asset provenance, or runtime admission.

## Required next gates

1. Source and independently review a defensible 1936 Altai/Oyrot institution or leader identity for the opening package, with a rights-cleared portrait or an explicitly accepted institutional treatment.
2. Resolve neutral 1936 flag/symbol provenance separately from any alternate-history route art.
3. Reconcile Event 005 Soviet-origin release/collision semantics and verify the SOV protected-remnant rule on the exact installed states.
4. Only after those gates, build a distinct package-local adapter with the `mounted_mobile` p61 force contract, dynamic ledgers, full decision/mission/idea/AI/focus/localisation surfaces, cleanup, and package-local MCP/probability evidence.
5. Keep central attestation, preflight, scenario, and Join fail-closed until the complete package packet is independently accepted.

No gameplay or asset files were changed by this audit.
