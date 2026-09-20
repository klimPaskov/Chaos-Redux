# Event 006 KUB/TAT probability retry — 2026-09-20

Disposition: unresolved typed-fixture blocker; no balance or gameplay change.

Scope: the already admitted IW-040 Kuban and IW-044 Tatarstan mission AI surfaces only.

The retry preserved the 32 content-attested selectable packages, 29 compatible reservation groups, 40 runtime adapters, 161 unattested selectable rows, and the exact `3/4/5/7/10` automatic ladder with World Collapse at `10`.

## Current source inspection

The KUB source is `common/decisions/006_independence_wave_frontier_decisions.txt` and the TAT source is `common/decisions/006_independence_wave_siberian_decisions.txt`.

The current KUB `mission_ai_will_do` pool is complete at 11/11 candidates, with source revision `1982691edf850d408770b30b62150791d167f09fc48ee616a34711ec4ea73d9f`, source hash `ccbb75a16ead7ab72ea77e90cf562971f8ede81bba9993e9769c047510eb6c9f`, 17 required inputs, zero unresolved inspection inputs, and zero available candidates under the empty fixture.

The current TAT `mission_ai_will_do` pool is complete at 11/11 candidates, with source revision `14a739e05a5bcb7b2a9516cff7279d7c43c5118e9f1b8c1f4c51362080236379`, source hash `9fe87c1b20f9b999fc6e5732ab5d1dee87a8a7b9ed90de0cd31ddd4e7928a5e1`, 18 required inputs, zero unresolved inspection inputs, and zero available candidates under the empty fixture.

The same-source MCP artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6c778765dc6654618b7b41a0e2f1126766410bb444a6fd843207fc003814d985/18cda6b3203daf7a83f2e3ade0738e3156a80ff833d0a05107378afd537bf167/probability-inspect-ccbb75a16ead.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9f8dd02b90b39954cc00948ed195a981aec52c2aeb221bbc67e5152eca752f83/00e4c8e82b487a5480526642ce163f052317d8078fae32d7248d167c87b4f153/probability-inspect-9fe87c1b20f9.json`.

## Fixture blocker

The required typed KUB/TAT scenario contract cannot be represented by the available probability-tool schema without inventing unsupported shapes.

The exact validation blocker rejects `scenarioSet.scenarios[0].state.has_equipment`, `scenarioSet.scenarios[0].state.has_variable`, `scenarioSet.scenarios[0].state.check_variable`, `scenarioSet.scenarios[0].state.capital_scope`, `scenarioSet.scenarios[0].state.var:independence_wave_former_host`, and `scenarioSet.scenarios[0].state.flags`.

That prevents actor scopes, event-target scopes, setup variables, package ledgers, scoped trigger values, route state, resource affordability, and former-host validity from being supplied as a supported fixture.

The ten required scenarios remain unexecuted after the blocker: `KUB_FRAGILE_PEACE`, `KUB_SEVERE_HOST_WAR`, `KUB_STABLE_ROUTE_LOCK`, `KUB_NETWORK_READY`, `TAT_FRAGILE_PEACE`, `TAT_SEVERE_HOST_WAR`, `TAT_STABLE_ROUTE_LOCK`, `TAT_NETWORK_READY`, `BOTH_RESOURCE_STARVED`, and `BOTH_IMPOSSIBLE_AMBITION`.

## Balance boundary

No complete typed baseline exists, so no same-scenario `hoi4.probability_compare`, sweep, simulation, sequence, normalized probability, dominance, starvation, rank-reversal, or numeric balance conclusion is valid.

The source score ladder remains evidence only: founding and emergency actions use urgent `100`, core recovery and route actions use high `25`, ordinary host/agrarian/network actions use standard `10`, war doubles the border-security and emergency scores, and former-host settlement receives its existing no-severe-threat factor.

No AI, decision, mission, focus, strategy-factor, admission, or Join source was edited.

## Next gate

The next retry requires a documented probability-tool fixture schema that accepts country actor scope, capital and anchor scope, former-host targets, flags, variables, active decisions, ledger values, route-government state, and numeric trigger comparisons.

Until that schema exists, KUB and TAT remain source-complete but quantitatively unresolved, and their existing package admission must not be widened or reweighted from empty-fixture output.
