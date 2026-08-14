# IW-050 Komi lifecycle, cost, and tooltip repair handoff

Date: 2026-08-14

Status: source repair complete; package remains package-local and fail-closed for central attestation, normal/scenario preflight, and Join admission.

## Scope

This bounded repair closes three concrete Komi decision-surface defects identified by the current decision and mission audit.

The repair owns only `common/scripted_effects/006_independence_wave_komi_package_effects.txt`, `common/decisions/006_independence_wave_komi_decisions.txt`, and `localisation/english/006_independence_wave_komi_l_english.yml`.

No central adapter, attestation, preflight, Join, allocator, focus-tree, map, formable, flag, portrait, or workbook source was changed.

## Applied fixes

1. `independence_wave_komi_durable_sovereignty` is now cleared by both `independence_wave_setup_iw_050_komi` and `independence_wave_cleanup_iw_050_komi`. A new generation cannot inherit a previous sovereignty receipt, and package cleanup cannot leave the terminal route flag behind.

2. `independence_wave_komi_establish_taiga_emergency_command` now checks `can_pay_independence_wave_security_standard_cost` in both `available` and `custom_cost_trigger`, matching its existing `independence_wave_decision_pay_security_standard` payment effect and `independence_wave_cost_security_standard` display.

3. `independence_wave_komi_codify_durable_sovereignty_desc` no longer claims that the codify project secures the separate northern corridor outcome.

4. `independence_wave_komi_sovereignty_effect_tt` now describes only the settlement and sovereignty effects that the codify effect actually applies. The separate corridor tooltip remains responsible for network and League gains.

## Deferred design questions

The standard-cost factory reservation, strategic project spare-factory requirement, origin-ended cancellation guard, and former-host partial-success wording remain documented design questions from the decision audit. This repair does not invent new payment, reservation, refund, or partial-success semantics.

The Komi package remains absent from the central content-attestation OR list and deterministic Join sequence. The package is not promoted by this local repair.

## MCP evidence

The required post-change `hoi4.probability_inspect` targeted `common/decisions/006_independence_wave_komi_decisions.txt` with adapter `mission_ai_will_do`. It returned `PROBABILITY_SOURCE_INSPECTED` with source revision `72795dfd2c8d97cce2339e7ea5b1a5a3f6fd58f883d5c1890e92169fb85a9fdc`, source hash `71a7fae182b69d6594d9efa55d46badadbf418a651f4d5b39530c0a1d8d81adc`, eleven candidates, zero available candidates, fifteen required inputs, zero inspect-unresolved items, and `poolComplete=false`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b3cf778e2fb7465812bc89c3adeaefb6dea04926a0a0f151797d712d9a445984/5346f972e0031507a4824fc32c77330c400ca350c5061ddd47b5dfad8c9f6eb4/probability-inspect-71a7fae182b6.json`.

The earlier pre-repair inspection recorded source revision `b6c5fd7f6c917940f597716805e6cb845bdd38c7fbc2b302cfd721f5c2941218` and source hash `9583721e8b4a125ac3a6ffb64f30c549d26c8a85e89953b2d4794df3b5860765`. The adapter pool was also incomplete with zero available candidates, so no quantitative before/after balance claim is possible.

The same empty-fixture mission scenarios remain bounded by missing package identity, setup, ledger, capital, host, network, and cost state. No normalized selection probability, timing, dominance, starvation, or live-AI claim is made.

The required post-change `hoi4.event_inspect` scan targeted `chaosx.nr6.350` with helper expansion. It returned `EVENT_INSPECTED_PARTIAL`, revision `741883f50501db1f866db675ee6ad6cb4009a90ad539eb84b08ce5e82602f65b`, graph hash `37eb00185cb12c74f97438ecee7380780cf4eec14d3693f7930e97a91ce4b720`, zero selected blocking diagnostics, and the known deferred workspace-wide helper/lifecycle projection. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b7602918751580c9bc40120e18eb18b70c4a6077becdab6fa358f5bd95d5bf62/ed0618cec1453f8326dc1626173cf21c47cf93b6db7f5505256d88f5220ba76a/event-scan-741883f50501.json`.

No ordinary Komi decision-category GUI exists, so no decision GUI render or rewrite was applicable.

## Static review

The touched decision, effect, and localisation sources were re-read after the patch. The emergency decision now uses the security-standard affordability trigger only; the former-host and corridor projects retain their strategic-cost contracts. The sovereignty flag has exactly one package-local writer and is cleared in both setup and cleanup. The edited localisation keys remain present in the existing BOM-encoded Komi file.

## Remaining blockers

KOM is still not centrally admitted. Its portrait and neutral flag provenance gates, package state/registry reconciliation, central dispatch and attestation, deterministic Join, and typed non-empty probability scenarios remain unresolved. These blockers are outside this narrow repair and prevent a complete Event 006 claim.
