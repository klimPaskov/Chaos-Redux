# Event 006 DM-42 collective-recognition cost disclosure

Date: 2026-08-14

## Scope

This bounded repair covers only `independence_wave_request_collective_recognition` (DM-42) in `common/decisions/006_independence_wave_decisions.txt`.

The accepted decision matrix row `DM-42` requires a diplomatic-standard cost plus one civilian-factory commitment. The decision already reserves `@CR_SC_INDEPENDENCE_WAVE_DECISION_COST_CIVILIAN_FACTORY_LIGHT`, but its custom cost display used the non-factory diplomatic key. The selector now uses `independence_wave_cost_diplomatic_standard_factory`.

## Change

- Before: `custom_cost_text = independence_wave_cost_diplomatic_standard`
- After: `custom_cost_text = independence_wave_cost_diplomatic_standard_factory`
- The cost trigger, payment effect, duration, cooldown, target checks, AI score, and cleanup are unchanged.
- The factory-aware base/tooltip/blocked localisation triplet already exists in `localisation/english/006_independence_wave_decisions_l_english.yml`; no localisation file change was needed.

## Evidence

Fresh `hoi4.probability_inspect` on `common/decisions/006_independence_wave_decisions.txt` with adapter `decision_ai_will_do` returned `PROBABILITY_SOURCE_INSPECTED` for workspace `mod_chaos_redux_ea3b2d67c2c0`:

- source revision: `de4ea8794eabc91b142274a08be8da11d772fbc94a6141328f2cbe31fce549ba`
- source hash: `c7b8349df5ccbc3ef6c2511abdb7f1fe34e6d7dd45bff82970e2c726d43a635a`
- 10 decision candidates, 0 available under the empty fixture, 79 required inputs, 0 inspect-unresolved rows, `poolComplete=false`
- artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e1dd48e1e483868a201bb2fc3decaa6101fe13817edcdc80aa6a82ca715c57b3/eac4004b3954ce95c809ce6ead2c218d9caf0b3d976c5d14129e38c2db66e95d/probability-inspect-c7b8349df5cc.json`

This is a structural/current-source receipt only. It does not prove normalized click probability or campaign balance because the adapter reports no available candidates and an incomplete pool.

## Disposition

No central adapter, attestation, preflight, Join order, asset, AI, workbook, or shared cost/effect logic changed. The broader Event 006 authority remains 40 adapters / 32 attestations / 29 compatible groups / 161 unattested selectable rows, with MEL and KOM fail-closed and the whole event HOLD/PARTIAL.
