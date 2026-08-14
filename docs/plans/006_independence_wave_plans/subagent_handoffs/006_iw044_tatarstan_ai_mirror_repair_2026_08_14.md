# IW-044 Tatarstan AI mirror repair — 2026-08-14

## Scope

This bounded reconciliation verifies that the parser-safe file-scoped values in `common/ai_strategy/006_independence_wave_tatarstan.txt` align with the authoritative `independence_wave_tatarstan_ai` constants in `common/script_constants/006_independence_wave_tatarstan_constants.txt`. The source was concurrently present in aligned form when the parent re-read it; this record does not claim a separate committed before/after source revision. Strategy block structure, enable gates, package admission, central dispatch, and Join order are unchanged.

## Changed values

The Tatarstan mirror now uses `82/44/58/26/62/76/112` for army, infantry production, support production, artillery production, infrastructure, bunker defense, and emergency army, with `-250/-420` for founding and settled war restraint. These exactly match the central constants block.

## Evidence and limits

The mandatory post-change `hoi4.probability_inspect` on `common/ai_strategy/006_independence_wave_tatarstan.txt` with `ai_strategy_factor` returned `PROBABILITY_SOURCE_DISCOVERED`, `discoveryReason=no_weighted_surfaces`, zero candidates, zero required inputs, and zero unresolved inputs. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6849f069b1eaabe0e2b0d48654656e89eb4281f7c4ef606d9d2c5ae181599530/e6bc772f021f1ed76201dbfc317e3faea722e8149efb912fcf7f8f56266c74d5/probability-inspect-68d35cd6faad.json`.

The required same-scenario compare was attempted with the six named TAT scenarios from `006_iw044_tatarstan_probability_audit_current_2026_08_13.md` (`TAT_FOUNDING_PEACE`, `TAT_FORMER_HOST_THREAT`, `TAT_LEDGER_STABLE_ROUTE_LOCK`, `TAT_NETWORK_READY`, `TAT_RESOURCE_STARVED_RESERVE_FLOOR`, and `TAT_IMPOSSIBLE_FORMABLE_AMBITION`). The adapter returned `PROBABILITY_SURFACE_EMPTY` (`No weighted blocks matched this request`), so no quantitative balance, ranking, timing, dominance, starvation, or live AI claim is made.

Static allocator authority remains 32 content-attested packages, 29 compatible reservation groups, 161 unattested selectable rows, and 40 runtime adapters; no admission or Join changes were made. The whole Event 006 disposition remains HOLD / PARTIAL.
