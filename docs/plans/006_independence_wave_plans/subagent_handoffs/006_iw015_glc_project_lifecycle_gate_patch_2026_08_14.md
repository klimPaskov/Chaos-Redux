# IW-015 GLC project lifecycle gate patch

Date: `2026-08-14`.

Scope: narrow source repair for the IW-015 GLC decision category. The patch does not change country identity, flags, portraits, AI weights, formable admission, central content attestation, scenario admission, or Join order.

## Source change

Added `is_independence_wave_glc_project_ready` to `common/scripted_triggers/006_independence_wave_iberian_package_triggers.txt`. The trigger requires the exact GLC package identity, `independence_wave_iw_015_setup_complete`, and absence of `independence_wave_glc_compact_crisis_failed`.

Applied that trigger to all eleven GLC project surfaces in `common/decisions/006_independence_wave_iberian_decisions.txt`: visible, available, and timed cancellation paths use the package-ready gate, while the immediate sovereignty project uses it for visible and available eligibility. The network project now exposes and starts only after founding settlement and crisis resolution, with stable ledgers, membership, League-route, capital-control, and one-active-project requirements; its running timer cancels if any of those lifecycle gates are later lost.

Timed GLC cancellation effects now apply the shared failure deltas only while the package-ready trigger remains true. A founding-crisis failure therefore closes the projects without applying a second non-idempotent project-failure penalty.

## Validation

Static source inspection found eleven GLC visible references, eleven GLC available references, ten timed GLC cancellation-trigger references, and ten guarded timed cancellation effects; the sovereignty project is immediate and intentionally has no cancellation effect.

`python .tools/audit_event6_allocator.py` passed with 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, 39 adapters, 31 attested packages, 28 compatible groups, and the 3/4/5/7/10 ladder with World Collapse at 10.

`python .tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 cells and 8 edge cases.

The mandatory current `hoi4.probability_inspect` on `common/decisions/006_independence_wave_iberian_decisions.txt` after the network lifecycle hardening returned `PROBABILITY_SOURCE_INSPECTED` with source revision `b261f5cd32f39068e2919235cc1adca9ea363daca320b359aee25362c63d7adb`, source hash `8a8f0e9d341c7963e8d341fe6d99e1f1509597f1e110db0651bcb3a78a446720`, 22 mission candidates, 12 required inputs, zero inspect-unresolved inputs, and an incomplete runtime pool with zero available candidates. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/19f69ed3c08364102002bda5afa8022b490373a6aa7b271236583820a93a7e34/0a034f91b2e831a6910cbb3587afd0843244d70a65ad89c00f1f2dd17747b8f9/probability-inspect-8a8f0e9d341c.json`.

No quantitative balance, ranking, timing, dominance, starvation, or live-runtime claim follows from this source inspection. No compare was required because no AI or score weight changed.

## Remaining gates

IW-015 remains central-admission HOLD / fail-closed pending its independent flag, portrait, identity, and package audit decisions, current typed probability scenarios, and the parent-owned content-attestation review. FORM-07 remains separately fail-closed. No live game, save/load, or player-owned runtime validation was performed.

Skills used: `chaos-redux-decisions-missions`, `chaos-redux-events`, and `chaos-redux-subagents`, with the required offline wiki and vanilla documentation references.
