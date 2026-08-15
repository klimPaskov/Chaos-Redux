# IW-057 FER probability audit — current 2026-08-15

Status: partial, read-only, and not a balance pass. The HOI4 MCP mission adapter discovered all eleven FER `ai_will_do` blocks, but the supplied state fixtures produced zero available candidates and no exact selection probabilities. No gameplay, AI, source, asset, central-admission, or Join file was edited by this auditor, and no staging or commit was performed.

## Scope and source boundary

The audited weighted surface is the FER package decision/mission set in `common/decisions/006_independence_wave_far_eastern_decisions.txt:16-585`. The exact candidate pool is:

`independence_wave_fer_hold_railway_council`, `independence_wave_fer_secure_railway_ports`, `independence_wave_fer_integrate_coastal_guards`, `independence_wave_fer_register_fer_communities`, `independence_wave_fer_settle_former_host_ledgers`, `independence_wave_fer_ratify_constitutional_autonomy`, `independence_wave_fer_adopt_railway_charter_compact`, `independence_wave_fer_convene_coastal_councils`, `independence_wave_fer_establish_coastal_emergency_command`, `independence_wave_fer_codify_durable_sovereignty`, and `independence_wave_fer_open_pacific_corridor`.

The related package trigger and validity surface is `common/scripted_triggers/006_independence_wave_far_eastern_package_triggers.txt:22-175`, especially `is_independence_wave_fer_project_ready`, `is_independence_wave_exact_package_iw_057_runtime_ready`, `is_independence_wave_exact_package_iw_057_tag_available`, `has_independence_wave_fer_command_roster`, `has_independence_wave_fer_active_package_project`, the state 408/409 anchor checks, former-host checks, route-government checks, and the three FER cost helpers.

The related static strategy surface is `common/ai_strategy/006_independence_wave_far_eastern.txt:1-70`. The related effect source is `common/scripted_effects/006_independence_wave_far_eastern_package_effects.txt`. The shared evolution timing source checked for an IW-057 timing surface is `common/mtth/006_independence_wave_evolution_mtth.txt`; it contains a shared evolution MTTH entry and no FER-specific entry.

The score constants are in `common/script_constants/006_independence_wave_decision_constants.txt`, under `independence_wave_decision_ai`: `blocked = 0`, `very_low = 2`, `low = 5`, `standard = 10`, `high = 25`, `urgent = 100`, `modifier_half = 0.5`, `modifier_double = 2`, and `modifier_major = 5`.

A concurrent owner edit landed in the decision file during this audit. The current local SHA-256 is `2364db2662e2dcaffca35332c3f4844b78d0bab503526f3d83e41ed9200a8a9e`, and the current MCP source hash is `d5c1417fc7a7483b6e9b3fbe2d62eff37b7eaa3f0a205eaf210590ff769ca51f`. The concurrent diff changes FER cost-text keys, the former-host loss tooltip branch, and the strategic cost display modifier; it does not change an `ai_will_do` block. Pre-edit artifacts with source hash `f55a437b...` are superseded. The current receipts below were rerun after the edit.

## Scenario contract

The named scenario set is `IW057_FER_EMPTY_TYPED_BASELINE_2026_08_15` with scenario hash `2c89ce66f56c07b9eff850e73dfa77bb48ade645331729407c489850b53e1c58`:

`FER_408_FRAGILE_PEACE`, `FER_409_FRAGILE_PEACE`, `FER_408_HOST_WAR`, `FER_409_HOST_WAR`, `FER_408_STABLE_ROUTE_LOCK`, `FER_409_STABLE_ROUTE_LOCK`, `FER_408_NETWORK_READY`, `FER_409_NETWORK_READY`, `FER_408_RESOURCE_STARVED`, `FER_409_RESOURCE_STARVED`, `FER_408_IMPOSSIBLE_AMBITION`, and `FER_409_IMPOSSIBLE_AMBITION`.

Every scenario deliberately used the explicit empty state fixture `state = {}` because the current adapter rejected the nested typed fixture shape supplied by the FER handoff. There were no scheduled state changes, no seed, no uncertain distributions, no cadence, and no terminal-state declaration. The candidate list is complete relative to the eleven source `ai_will_do` IDs, but the engine-available pool is not complete: the fresh mission inspection reported `poolComplete = false`, `availableCandidates = 0`, `requiredInputs = 15`, and `unresolved = 0`.

The omitted external factors include the original FER identity and active-country gates, IW-057 package/origin receipts, setup-complete/current-generation force-package flags, state 408/409 ownership/control/capital state, former-host existence and protected-state receipt, command-roster flags, crisis and compact ledgers, route-government flags, founding-settlement and durable-sovereignty flags, network/League membership, active-project/completion flags, war and severe-host-threat state, and all cost resources (civilian factories, command power, manpower, stability, war support, army experience, infantry/support equipment, and convoy/train alternatives).

## MCP evidence

All calls used workspace `mod_chaos_redux_ea3b2d67c2c0`.

| Surface and call | Result and revision/hash | Artifact |
| --- | --- | --- |
| FER decisions, `mission_ai_will_do`, fresh `hoi4.probability_inspect` | `PROBABILITY_SOURCE_INSPECTED`; source revision `e2259d68c63f39978057d74e226353f239f802196fc6b57d0d0dc2d6a63e2b0a`; source hash `d5c1417fc7a7483b6e9b3fbe2d62eff37b7eaa3f0a205eaf210590ff769ca51f`; 11 candidates, 0 available, 15 required inputs, 0 unresolved, `poolComplete = false` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/17e0fc763ab5961a183137cef30d4b6c2f3af715edc9a4e4b1adf3723a0f5929/2d7ae0a1976bbadd7832d75dd4a5117ae274f4669fa63d35f7b6585a91efaf83/probability-inspect-d5c1417fc7a7.json` |
| FER decisions, `mission_ai_will_do`, `hoi4.probability_evaluate` | `PROBABILITY_ANALYZED_PARTIAL`; analysis `probability-430cca0af78c796f8bae6d73`; source revision `caa5ba48776b4a23659d027590752e89057e4d2c6db0429f21130173d7c6b1e7`; source hash `d5c1417fc7a7483b6e9b3fbe2d62eff37b7eaa3f0a205eaf210590ff769ca51f`; 12 scenarios, 132 candidate/scenario rows, 135 unresolved items, 11 diagnostics | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6a8887ebe1d850fede912c1d57489c7db580099ccbde23155b75b03cf501107/d32820d5f7dbff95aa895811383a20ae673e0109ad4d52bf80e9fe8a199efc60/probability-430cca0af78c796f8bae6d73.json` |
| Current mission ranking/matrix/unresolved render, `hoi4.probability_render` | `PROBABILITY_ANALYZED_PARTIAL`; same analysis, source hash, and scenario hash; uncertainty-visible validation passed with 135 unresolved/bounded items | Ranking SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/36985afd59ff897d9f270e06ee01187326aa0e2d8030206f0c16ad706612f618/d1e4d42e7cfc7e763a511e327cea59a9f27fb09be489cfb786ddad29107541dd/probability-probability-430cca0af78c796f8bae6d73-ranking.svg`; matrix SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b93d8a9cf6231b7a10b95deb2c808e6162cdcdb3b387d37956dfb729cd76ab47/100c93ba92845050f66cddd307ec127e8ccfda1646ca75995bbe472e0a7480a5/probability-probability-430cca0af78c796f8bae6d73-matrix.svg`; unresolved SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b4d9ac00a6f5001f3901b43128ba388eab85253192464cdb21fecda6ca6e8b8a/ae9d3c88c98162eb56dac03ca17f0043b17a2f84283c606c7b85b27ccf9d9821/probability-probability-430cca0af78c796f8bae6d73-unresolved.svg` |
| FER decisions, same current source on both sides, `hoi4.probability_compare` | `PROBABILITY_ANALYZED_PARTIAL`; analysis `probability-642a1dcab1febdcfb92d192a`; source revision `d930d9df7f220a33db1a1648644669613bd49255b77a3900253f0668933d7046`; source hash `d5c1417fc7a7483b6e9b3fbe2d62eff37b7eaa3f0a205eaf210590ff769ca51f`; same scenario hash; `comparisonChanges = 0`, 135 unresolved, 11 diagnostics | Comparison SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/94873917c1300381dd0ddeda3e99e2b304fd22822dad21a113cbf52c42ce92f6/probability-probability-642a1dcab1febdcfb92d192a-comparison.svg`; JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/385926258ac145afe1a124c848463aacedf20c2e16533a9599d1602054c3234a/fd8392e65eab2f6881caa4fe5a926ce129d01b7e6bec57bc103d2a0d3fa06188/probability-642a1dcab1febdcfb92d192a.json` |
| FER strategy source, `ai_strategy_factor`, fresh `hoi4.probability_inspect` | `PROBABILITY_SOURCE_DISCOVERED`, `discoveryReason = no_weighted_surfaces`; source revision `f2f675a134661c8c8b478d890d9b7a5cdad51ccb9407fd1efac7b9c7cc6bd6ac`; source hash `4b1b9d0035ee704475ed5faaad6446cd72f2aed9825371019f429ead124a33a7`; 0 candidates, 0 required inputs, 0 unresolved | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a801a23575be991f1624d47aa40a26cfb260081a68963fc5dcd07fc867fb83a3/bddbf572fe037fcbabae50d6158026c9760dc17d3588b33b0ae02910036272f0/probability-inspect-4b1b9d0035ee.json` |
| FER strategy source, `ai_strategy_factor`, `hoi4.probability_evaluate` | `PROBABILITY_SURFACE_EMPTY`; exact blocker: `No weighted blocks matched this request` | No artifact |
| FER package effects, `random_list`, `hoi4.probability_inspect` | `PROBABILITY_SOURCE_DISCOVERED`, `discoveryReason = no_weighted_surfaces`; source revision `caa5ba48776b4a23659d027590752e89057e4d2c6db0429f21130173d7c6b1e7`; source hash `cabd6c7bac752713b60e51d95c95d823ba1922f55644a8d0847a6473e1a2f9c1`; 0 candidates, 0 required inputs, 0 unresolved | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dc39a23dfdc7f34e5b7380ac98764e6f992bebf0fdbc6c8d00227b9c05b0f7ad/5c83a6c47e1bad778583808b95442e1f6451d1a5abf88fdb04afde1c38f60b92/probability-inspect-cabd6c7bac75.json` |
| FER package effects, `direct_random`, `hoi4.probability_inspect` | `PROBABILITY_SOURCE_DISCOVERED`, `discoveryReason = no_weighted_surfaces`; same source revision/hash as the random-list probe; 0 candidates | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8a6c42bd9f6d91ce8296e84f95f75b5d64fa727087ff90dd665ed10c8a88d3de/5b2e19638106520855b1c2f520d74ce80e5d43d6f8b85b6abf951b8637b46032/probability-inspect-cabd6c7bac75.json` |
| Shared evolution MTTH source, `event_mean_time_to_happen`, `hoi4.probability_inspect` | `PROBABILITY_SOURCE_DISCOVERED`, `discoveryReason = no_weighted_surfaces`; source revision `caa5ba48776b4a23659d027590752e89057e4d2c6db0429f21130173d7c6b1e7`; source hash `8632297cf059164892a537ff3a987cddd0406c020e98234331014d42b4b8f8a2`; 0 candidates, 0 required inputs, 0 unresolved | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d7b70828aeaed40fb6a7580ecab640bec229d30666374d78bce426ac438d038b/81c0987d5de78edf9c39668593b62f378b0d137347e99b8cc6518ba93fd5d10b/probability-inspect-8632297cf059.json` |
| Current mission sweep, `hoi4.probability_sweep` | `PROBABILITY_SWEEP_RANGE_REQUIRED`; exact blocker: `Every sweep path requires a scenario range, numeric alternatives, or numeric state value`; details identify `FER_408_FRAGILE_PEACE`, path `has_war` | No artifact |

The MCP source revision token changed between read-only calls while the source hash stayed stable, so each artifact retains its own revision above. The stable current decision source hash is the stronger content identity for this receipt.

## Source score and modifier trace

These are exact source score traces, not normalized probabilities. Decision and mission `ai_will_do` values are willingness scores in an AI score race; they are not click probabilities and must not be divided by a guessed pool total.

| Candidate | Base score | Authored modifier trace | Static score bands |
| --- | ---: | --- | --- |
| `independence_wave_fer_hold_railway_council` | `urgent = 100` | No modifier; `available = { always = no }` and activation is separately gated | 100, activation-only/unavailable in the supplied source shape |
| `independence_wave_fer_secure_railway_ports` | `high = 25` | None | 25 |
| `independence_wave_fer_integrate_coastal_guards` | `high = 25` | `factor = 2` when `has_war = yes` | 25 peace, 50 war |
| `independence_wave_fer_register_fer_communities` | `high = 25` | None | 25 |
| `independence_wave_fer_settle_former_host_ledgers` | `standard = 10` | `factor = 2` when `NOT has_independence_wave_severe_host_threat` | 10 severe threat, 20 without severe threat |
| `independence_wave_fer_ratify_constitutional_autonomy` | `high = 25` | None | 25 |
| `independence_wave_fer_adopt_railway_charter_compact` | `standard = 10` | None | 10 |
| `independence_wave_fer_convene_coastal_councils` | `high = 25` | None | 25 |
| `independence_wave_fer_establish_coastal_emergency_command` | `urgent = 100` | `factor = 2` when `has_war = yes` | 100 peace, 200 war |
| `independence_wave_fer_codify_durable_sovereignty` | `high = 25` | None | 25 |
| `independence_wave_fer_open_pacific_corridor` | `standard = 10` | None | 10 |

The source-only static ordering is urgent above high above standard, with the two wartime modifiers capable of raising emergency command to 200 and coastal guards to 50. This is score-only evidence. The MCP did not produce a valid live ranking because all eleven candidates were ineligible under the empty fixture.

## Eligibility, validity, and risk findings

The current `is_independence_wave_fer_project_ready` gate requires the exact FER package identity, IW-057 setup completion, the current-generation force package, and no FER compact-crisis failure. Candidate availability additionally depends on per-project completion/route flags, one-project-at-a-time serialization through `has_independence_wave_fer_active_package_project`, cost resources, former-host target validity, route government, crisis/founding/compact state, and network/League state for the Pacific corridor.

The FER identity and anchor surface is deliberately fail-closed: the live runtime gate requires an owned/controlled state 408 or 409 anchor, a capital anchor in 408 or 409, a valid former-host protected-state receipt, and the two command-roster flags. The package-local availability helper also uses fixed 408/409 anchor availability and does not use the dormant vanilla state 563. Earlier handoff wording that accepted 563 is stale against the current trigger source and should not be used as probability input.

The fresh evaluate returned `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` for all eleven candidates across all twelve empty-state scenarios. The diagnostics are exact for the supplied empty fixtures only; they do not prove that authored decisions are dead in a valid FER campaign. No exact dominance, starvation, rank reversal, repetition rate, timing drift, or exploit-risk conclusion is supported by this run because the available candidate pool is empty and 135 rows remain unresolved.

The founding mission has a positive urgent score of 100 but `available = { always = no }`. This may be intentional because it is activation-driven, but the positive score should be treated as a latent dead/hidden-weight review item until the owner confirms whether the engine ever evaluates its `ai_will_do` for activation. The MCP never-eligible diagnostic is not by itself a gameplay defect.

The one-active-project gate is visible in source and reduces simultaneous project repetition risk, but no cadence, cooldown, recovery, removal, reset, or completion timing distribution was declared for a sequence analysis. No repetition or snowball safety claim is made.

The four strategy profiles are source-visible static directives, not a probability-proportional pool. Their source constants are: railway-port survival `build_army 86`, infantry production `48`, artillery production `30`, support production `56`, infrastructure `82`, and bunker `70`; host restraint `avoid_starting_wars -270`; settled compact `build_army 86`, `avoid_starting_wars -430`, and infrastructure `82`; coastal emergency guard `build_army 122` and bunker `70`. The installed `ai_strategy_factor` adapter exposes no analyzable candidates, so no strategy dominance or validity conclusion is available.

## Classification and next requirements

The source score table is **exact, score-only**. It does not establish a click probability, normalized odds, or live rank.

The eleven empty-fixture eligibility diagnostics are **exact for the supplied empty `{}` state**, but the overall evaluation is **partial/bounded** because `poolComplete = false`, available candidates are zero, and 135 rows are unresolved.

The rendered ranking, matrix, and unresolved views are **partial evidence views**. They make the empty-pool diagnostics visible; they are not a valid campaign ranking.

The AI strategy result is **no-weighted-surface / unresolved for quantitative strategy analysis**, not evidence that the static strategy directives are absent or invalid.

The random-list and direct-random probes are **no-weighted-surface**. No FER package random selector was found by MCP or source scan.

The shared evolution MTTH probe is **no-weighted-surface for FER-specific timing**. No IW-057 timing distribution is proven.

The current/current compare is **capability-only** with `comparisonChanges = 0`. It is not a true before/after result because both sides used the same current source path. A true compare requires an owner-preserved pre-patch source revision and a post-patch source revision under this same scenario hash and candidate pool.

The next required analysis is a supported typed-state or engine-backed scenario adapter for all twelve named scenarios. It must carry at least original tag/active status, IW-057 origin and setup receipts, current generation, 408/409 anchor ownership/control/capital, former-host validity and war, command roster, compact/crisis ledgers, route/founding/network/League/durable flags, active/completed decisions, `has_war`, severe-host threat, and every project cost resource. After those fixtures are accepted, rerun `hoi4.probability_evaluate`, rerun `hoi4.probability_sweep` with explicit `has_war = false/true` and severe-host-threat alternatives, render the resolved ranking/matrix, and run a true same-scenario `hoi4.probability_compare` after any owner-applied AI-weight change.

No `hoi4.probability_simulate` call was made because no uncertain input distribution or seed was declared. No `hoi4.probability_sequence` call was made because no complete custom weighted pool with cadence, cooldown, recovery, removal, reset, cap, or terminal state was declared. No decision-specific structural MCP inspector is exposed for this surface; the probability adapter and source/trigger review are the available read-only evidence routes.
