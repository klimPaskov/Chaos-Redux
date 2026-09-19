# Event 021 current weighted-surface MCP refresh

Audit date: 2026-09-19.

Scope: current parent-owned weighted-surface evidence after the scenario target-ticket repair. This handoff records parent evidence only and does not replace the required independent probability-auditor certificate.

## Source repair

`event021_parent_add_scenario_target_to_weighted_pool` now uses the centralized `random_civil_war_scenario_target_weight` ladder before the shared individual-crisis load adjustment.

Low uses minor `4` and major `1`, Medium uses minor `2` and major `2`, and High uses minor `1` and major `3`. Maximum copies the confirmation-time eligible country set and does not use this helper.

The post-change SHA-256 values are:

- `common/scripted_effects/021_random_civil_war_parent_effects.txt`: `EF1EC867277C0781ECFBDC057F569A81174717D4C49A33B008322FB833D68728`
- `common/script_constants/021_random_civil_war_constants.txt`: `ABE8472B402109E3ABE530AB6253BEF68B16EE9E27940AE6DDBCF5611A50347D`

## Current MCP receipts

The focused Event 021 lint used `hoi4.event_inspect` with selector `{ kind: event, eventId: chaosx.nr21.1 }`, downstream direction, depth 1, 80 nodes, 120 edges, helper expansion disabled, and refresh enabled. It returned `EVENT_INSPECTED_PARTIAL` at revision `a8fde3e58546f004e81d855d73d29674ae3c5be8f894a1caf9586621929a6657` and graph hash `c83030c9d67b704f9c6437d31b7e4f5000463e6431ae40865f5b74e4cb15af21`. It reported zero blocking diagnostics and zero skipped sources; validation was false only because the large workspace deferred workspace-wide helper and lifecycle projection. Artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/88478ee4f4900b1880473ba5ce7020899a46d2a734eff2a21c48970ceac85c26/20b15948f6fd10fcb15c8279c63dac4b6d9985885d79fbc24c6e55a76084578a/event-lint-a8fde3e58546.json`

The current archetype pool was inspected and evaluated successfully through the random-list adapter. The exact candidate pool, scenario IDs, source revision/hash, analysis IDs, scenario hashes, artifact URIs, and expected starvation warnings are recorded in `probability_parent_refresh_2026-09-19.md` and the current acceptance evidence.

The current strange-incident inner pool was inspected and evaluated successfully. The evaluation used incident `0.08` and no-incident `0.92`, returned one expected dominance warning, zero unresolved inputs, and validation passed. The JSON artifact is:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/690c781d7bc1bdd2eaf8ad149e6966dfe852e5f64a4c6d707a47a7ae2e27a8f/efd46bae33d426fb16b6482d775d5a00257c3e81be4a7b16b139793e12fc5047/probability-a7b3b4afaedc1bce37ebb9a0.json`

The Event 021 decision and mission source inspections were current and structurally valid: 18 decisions and 3 missions, with no inspect-time unresolved inputs. Empty-fixture evaluations remained explicitly partial because hidden country/front/resource state was not supplied. Their receipts are in `decision_mission_parent_refresh_2026-09-19.md`.

The evolution MTTH inspection of `common/mtth/021_random_civil_war_mtth.txt` returned `PROBABILITY_SOURCE_DISCOVERED` with `no_weighted_surfaces`, zero candidates, and zero unresolved inputs at source revision `0300a6ea5d055ef79bb281821f5988151ffbbabd3163faf3dcc253f196f36949`; artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cf7bcd6ce32d4b24690396ee3dbb99a2bb207cbe7c5fb32e1a42d02de8d2fad3/69205e4c6f76e8831c56dd04aea61c45543a0d8fd2575b16b26cf34a7e4198fe/probability-inspect-c55a108bcbf2.json`

## Boundaries and remaining gates

The dynamic scenario target pool expands a temporary array after applying the intensity ladder and the shared load curve. The typed MCP custom-pool inspection for that helper returned an internal adapter error, so no complete live-country candidate manifest or exact Low/High distribution certificate is claimed.

The full TGT/ARC/SEV/EVO/FRT/SPN/STR/SET/REC/GLB/CLU/SCN matrix, same-scenario before/after comparisons, and independent specialist certificate remain open. Maximum still needs a tested distinction between preflight-eligible and commit-eligible countries, and the full immutable multi-front plan contract remains open. Runtime lifecycle, Event 006 package/asset reachability, save/reload, and user-owned live performance evidence are also not claimed.
