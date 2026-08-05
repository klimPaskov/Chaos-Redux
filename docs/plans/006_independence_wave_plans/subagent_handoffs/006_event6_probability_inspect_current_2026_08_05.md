# Event 006 probability-source inspection receipt (current)

Date: 2026-08-05.

Scope: read-only MCP inspection of the current shared Event 006 decision and mission AI surfaces after the CAT-inclusive authority update. No gameplay, localisation, asset, spreadsheet, or package-attestation file was changed. Obsolete pasted runtime logs were not used.

## Results

`hoi4_probability_inspect` with adapter `decision_ai_will_do` and source `common/decisions/006_independence_wave_decisions.txt` returned `PROBABILITY_SOURCE_INSPECTED`.

- Workspace: `mod_chaos_redux_ea3b2d67c2c0`.
- Source revision: `12bb3c683fce0418b66ca7d6d1be4da753258331f07b6a1419fbed8b26c22f5a`.
- Source hash: `153fd7ea18e5d7c4bc20ffcb77d69ce3dbd8244258d6ea6bfd78a0a9e15e0f85`.
- Discovered adapters: 11; decision candidates: 10; required inputs: 56; unresolved diagnostics: 0.
- Pool completeness: false, because world-state eligibility remains runtime-dependent.
- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/48382cdbe55d972ac365e7ca188ef9eb6867b41bacc43aecb7ba67c2df47dbde/88b17d00f1eac368b9681add62ea60fbfb60cb7438a9fce789c455edb4828c43/probability-inspect-153fd7ea18e5.json`.

The same source with adapter `mission_ai_will_do` also returned `PROBABILITY_SOURCE_INSPECTED`: 11 adapters, 54 mission candidates, 34 required inputs, zero unresolved diagnostics, and an intentionally incomplete runtime pool. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c7183246b2f51fbc8c00cf780dd9fb20b030f9bf83a392452fdb4b520b391935/fd4b29d330a79e3981ef27c86358b7183cca728e4f18ce83fab1298e5fb27695/probability-inspect-153fd7ea18e5.json`.

## Limits and next work

The inspections prove current source discovery and parser cleanliness only. They do not prove live AI choice, timing, route ordering, starvation, capacity, host survival, save/load persistence, or package admission. Those require named scenario inputs and the existing allocator/SCN-008 evidence. The whole-event status remains **HOLD / PARTIAL**.
