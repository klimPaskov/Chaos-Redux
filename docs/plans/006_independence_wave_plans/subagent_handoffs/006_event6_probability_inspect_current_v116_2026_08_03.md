# Event 006 probability-source inspection receipt v116

Date: 2026-08-03.

Scope: bounded read-only inspection of the current Event 006 decision and scenario AI surfaces. This receipt supplements the static decision/mission matrix and does not claim runtime selection probabilities, live AI timing, save/load persistence, or package admission. No gameplay, localisation, focus, asset, or spreadsheet file was changed.

## Current inspections

### Core decisions

`hoi4_probability_inspect` with adapter `decision_ai_will_do` and source `common/decisions/006_independence_wave_decisions.txt` returned `PROBABILITY_SOURCE_INSPECTED`.

| Field | Result |
| --- | --- |
| Workspace | `mod_chaos_redux_ea3b2d67c2c0` |
| Source revision | `6abd3bc8141de8584cb81c4bb8cf516be4a7be340f86723a2c8d541e9927622a` |
| Source hash | `153fd7ea18e5d7c4bc20ffcb77d69ce3dbd8244258d6ea6bfd78a0a9e15e0f85` |
| Adapter candidates | 10 |
| Required inputs | 52 |
| Unresolved source diagnostics | 0 |
| Pool complete | no; world-state eligibility remains runtime-dependent |
| Artifact | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/19bae25ea77beca4223eb07f756f52f2d54401f40f46e33c18362cb935082bb1/53411fe21a3a942b8f7dbb849e979332f6dac95c2523783f6ca350075a19cc7f/probability-inspect-153fd7ea18e5.json` |

The same source inspected with `mission_ai_will_do` also returned `PROBABILITY_SOURCE_INSPECTED`: 54 candidates, 30 required inputs, zero unresolved source diagnostics, and an intentionally incomplete runtime pool.

### SCN-008 scenario controls

`hoi4_probability_inspect` with adapter `decision_ai_will_do` and source `common/decisions/006_independence_wave_scenario_decisions.txt` returned `PROBABILITY_SOURCE_INSPECTED`.

| Field | Result |
| --- | --- |
| Source hash | `fcd8a24fbe89d3511d695a873797c426e8bce81f77179b4b6b392e0b0c2a58f7` |
| Adapter candidates | 3 |
| Required inputs | 1 |
| Unresolved source diagnostics | 0 |
| Pool complete | no; scenario ownership and world-state checks are intentionally supplied by the scenario matrix |
| Artifact | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f1ff328e4b7cb0aa6de85123361d817a5606bfca71c469be4ec6d628b0927da6/308460be58bbd953dff5382476d772a2431af1ca162c2b321e42dcafcebc3984/probability-inspect-fcd8a24fbe89.json` |

The scenario file has no mission-weighted blocks for the `mission_ai_will_do` adapter; the empty surface is expected and is not treated as a missing mission implementation.

## Disposition and limits

The old `SCAN_BYTE_LIMIT` result is no longer the current evidence for these two bounded decision surfaces. The successful inspections prove source discovery, candidate counts, required-input discovery, and zero unresolved parser diagnostics only. They do not normalize a click probability or prove route ordering, dominance, starvation, timing, allocator capacity, host survival, or live AI behavior. Those require named scenario inputs and the existing allocator/scenario matrices; live execution remains outside this receipt.

No source patch is justified by this inspection. The parent should link this receipt from the current Event 006 completion authority and retain the whole-event `PARTIAL / HOLD` disposition.
