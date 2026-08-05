# IW-033 / IW-041 post-patch probability compare handoff

Evidence date: 2026-08-05.

Audit owner: `chaosx_ai_probability_auditor`.

Scope: read-only post-patch review of `common/decisions/006_independence_wave_karelia_crimea_decisions.txt`, `common/scripted_triggers/006_independence_wave_karelia_crimea_package_triggers.txt`, and `common/script_constants/006_independence_wave_karelia_crimea_constants.txt`.

## Fresh source inspection

The mandatory `hoi4.probability_inspect` used adapter `mission_ai_will_do` against `common/decisions/006_independence_wave_karelia_crimea_decisions.txt` with the complete declared 21-ID candidate list.

- Status: `PROBABILITY_SOURCE_INSPECTED`.
- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0279abaa354293edefd66c1dcf388a31fdabc9f2f120641dfd32eab9a560873c/34717b4c80182fd7cecd564f8994d438b3228e778552b8196e22cef1f123c6ad/probability-inspect-e5af5906af88.json`.
- Source revision: `ba3b740f7132ca6668d869ff4fd79a6a0ed7e5fdf7772492e9770498263ba36f`.
- Source hash: `e5af5906af8821ee07434e025b363309d87e94ca103be95fd7b75ad27d6c4abb`.
- Adapter report: 19 discovered candidates, 14 required inputs, `poolComplete=false`, and 2 unresolved source items.

The same adapter against the trigger and constants files returned `PROBABILITY_SURFACE_EMPTY` with the exact blocker `No weighted blocks matched this request`; these files are helper and tuning dependencies, not weighted surfaces themselves.

## Named scenario evaluation

The prior named scenario ids were reused exactly: `PACKAGE_KAR_FOUNDING`, `PACKAGE_CRI_FOUNDING`, `PACKAGE_KAR_WAR`, and `PACKAGE_CRI_SETTLED`.

The typed state supplied to the adapter was the same empty state record (`state = {}`) used by the cached baseline receipt, so it cannot assert package flags, ledgers, resources, capital control, costs, or route state.

- Evaluation artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/df4c3967503207d39bc464d65e2e83ff047faea28270c66d01026744eaec949a/3fe05b06a5d82d269e0e92dd7de538ce4296e3d871ec3ebfe3ba6b0ab266ddb5/probability-873a83b5767ac818381d7b06.json`.
- Scenario hash: `f5ea20a48811380030e56b5865d0cba9057f6ef9ae9eb99b2e6f2c994745f922`.
- Classification: bounded typed evaluation, not runtime probability evidence.

The only diagnostics were intentional `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` warnings for `independence_wave_kar_hold_statehood_foundation` and `independence_wave_cri_hold_statehood_foundation`; both missions intentionally use `available = { always = no }` and remain passive activation-backed timers rather than selectable AI actions.

## Compare result and blocker

An exact post-patch `hoi4.probability_compare` against the cached baseline could not be completed.

The cached baseline receipt is `probability-dbc42b020c2684cb6900bff8` with source revision `829ca80edf9b0342786874c3484c9c0479f8ef55d3088fa078916b8f7b90f11e`, source hash `0ade9f81b363914d5de020c39be0b0d84a4607d32801dc147919dd3b5080c500`, and scenario hash `8e8a9836a34b1c158311e14c54a5ebf81ec0daafb816ff4d7c185b44ea0e9ebe`.

The installed compare route accepts `before` and `after` source objects with `{ path = ... }`, but rejects the cached baseline forms `{ analysisId = ... }`, `{ id = ... }`, `{ uri = ... }`, `{ artifact = ... }`, and `{ sourceHash = ... }`.

No pre-patch source path is present in the workspace, and the owner change is in the scripted-trigger helper rather than in the decision file's weighted block.

A same-path capability probe was completed but is not a patch compare: artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cc9dbecaf5a3967108998eaef6dda013ca4d5c7329edfc20906b7b8b7c04b6ff/c3b86f9738e71f157e159b21554febfe72e5678324cc0d384ea7246230fe8375/probability-1f9d31215f9ea367038586da.json` reports `comparisonChanges=0` for identical final paths, with the same four scenario ids and scenario hash `f5ea20a48811380030e56b5865d0cba9057f6ef9ae9eb99b2e6f2c994745f922`.

## Source-level conclusion

Classification: score-only and unresolved for runtime selection, not an exact probability claim.

`independence_wave_kc_ai_foundation_ready` now requires active IW-033/IW-041 package identity, rejects `independence_wave_kc_foundation_failed`, and accepts either `independence_wave_kc_foundation_settled` or the exact package setup-complete flag (`independence_wave_iw_033_setup_complete` for KAR or `independence_wave_iw_041_setup_complete` for CRI).

Therefore regular package decisions can receive nonzero AI willingness during setup/founding and after settlement, while a failed foundation remains zeroed by the helper.

The reserve floors, costs, capital and route gates, dynamic helper scopes, full candidate pool, normalized selection probability, dominance, starvation, rank reversal, timing, repetition, and runtime safety remain unresolved by MCP.

No gameplay or runtime source was changed by this audit.
