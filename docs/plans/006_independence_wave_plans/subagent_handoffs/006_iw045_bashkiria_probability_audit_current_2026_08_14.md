# IW-045 Bashkiria probability audit (current source, 2026-08-14)

## Disposition

IW-045 remains package-local complete but central-admission fail-closed. The current probability receipts establish source discovery and bounded scenario coverage; they do not prove normalized AI balance, activation timing, dominance, starvation, or live selection behavior because the adapter does not accept the typed campaign fixtures required by the package gates.

## Mandatory source inspection

`hoi4.probability_inspect` was run first against `common/decisions/006_independence_wave_bashkiria_decisions.txt` with adapter `mission_ai_will_do`.

- Code: `PROBABILITY_SOURCE_INSPECTED`
- Source revision: `4060832c53e9900f635edd17f688ee890c6342b9016de2d5c1b2519aede6f052`
- Source hash: `b7b031d727e03702aabc0decda0612f29957d2a01bfcb3565b1e30f06be54844`
- Candidates: 11
- Required inputs: 15
- Inspect unresolved: 0
- Pool complete: false; available candidates: 0
- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ca9886a771a12c74fc5a341ac6855123a9b28c5a2918eaa91354069428a63281/07d6f52b9f09d50edad4c1ffe0fb9af861eae88a70bbab45d770a3d267683f7f/probability-inspect-b7b031d727e0.json`

The source-level candidate pool is the founding mission plus ten serialized projects: `independence_wave_bsk_hold_frontier_congress`, `independence_wave_bsk_secure_frontier_depots`, `independence_wave_bsk_integrate_frontier_guards`, `independence_wave_bsk_register_bashkir_communities`, `independence_wave_bsk_settle_former_host_ledgers`, `independence_wave_bsk_ratify_constitutional_autonomy`, `independence_wave_bsk_adopt_agrarian_compact`, `independence_wave_bsk_convene_socialist_councils`, `independence_wave_bsk_establish_frontier_emergency_command`, `independence_wave_bsk_codify_durable_sovereignty`, and `independence_wave_bsk_open_ural_network_corridor`.

## Named scenario evaluation

`hoi4.probability_evaluate` used adapter `mission_ai_will_do`, the complete 11-ID candidate pool, six named scenarios (`BSK_FOUNDING`, `BSK_READY_PEACE`, `BSK_READY_WAR`, `BSK_HOST_LOSS`, `BSK_ROUTE_LOCKS`, and `BSK_NETWORK_READY`), raw-value output, and a 600-day horizon. The submitted scenarios retained explicit empty `state = {}` records because the recovered adapter rejected typed package fixtures.

- Code: `PROBABILITY_ANALYZED_PARTIAL`
- Analysis: `probability-d7d42495ef9d865081f06398`
- Scenario hash: `4167d1988fe6acbf8ebefe35ed2565a05292a5fcea9353db80758e4d2822ef3b`
- Rows: 66
- Unresolved: 136
- Diagnostics: 11 never-eligible outcomes under the empty fixtures
- JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0e92870d43d9aa4d9504fb9a680e54f88879b6f24ebbb2a071e01d7c4b99f18b/3ef18a1fa1e75644786275f06f99f923c4116076ac7ecee353e41c15194034dc/probability-d7d42495ef9d865081f06398.json`

The unresolved inputs include package/setup identity, state-651 ownership and capital control, ledger values, route flags, active-project/cooldown state, former-host relation and war, resource affordability, founding settlement, crisis resolution, network membership, and terminal cleanup state. The eleven never-eligible diagnostics are therefore fixture limitations, not claims that the authored missions are unreachable in gameplay.

## Same-source comparison

`hoi4.probability_compare` was run with the same BSK decision source before and after, the same 11-ID pool, and the same six named scenarios.

- Code: `PROBABILITY_ANALYZED_PARTIAL`
- Analysis: `probability-ffa3d98261c23c81e8cad1de`
- Scenario hash: `4167d1988fe6acbf8ebefe35ed2565a05292a5fcea9353db80758e4d2822ef3b`
- Rows: 66
- Unresolved: 136
- Diagnostics: 11
- `comparisonChanges`: 0
- Comparison artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ba5b752ec96812a061fcd0aefd1ce9e3f5d0359090ecfadb3161957471871dd1/450bf9bd1c19d58d4e94026ac2e7bb337d53acc1471af007459f3346fd6102cf/probability-ffa3d98261c23c81e8cad1de.json`

This is a capability/current-current receipt only. It is not a before/after balance proof because no source change was compared and the typed campaign state remains unresolved.

## Other mandatory evidence

The BSK `ai_strategy_factor` inspection returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason = no_weighted_surfaces`, zero candidates, and zero unresolved inputs. No quantitative strategy-factor claim is possible from that adapter. The current `.350` event inspect/render remains partial due deferred workspace-wide helper/lifecycle projection but reports zero selected blocking diagnostics. Static allocator, scenario-matrix, flag, and protected-tag audits continue to pass at 40 adapters, 31 content-attested packages, 28 compatible groups, 162 unattested selectable rows, and nine adapter-only fail-closed IDs including IW-045.

## Admission decision

Do not add IW-045 to `has_independence_wave_runtime_package_content_attestation_for_execution_id` or the deterministic Join sequence on this evidence. Preserve the exact source-placeholder portrait, generated route-flag provenance, current-generation cleanup, and package-local idea lifecycle. A future promotion requires either an adapter-supported typed fixture/evaluation or an explicit project-level waiver that accepts the unresolved probability limitation without claiming quantitative balance.
