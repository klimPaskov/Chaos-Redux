# IW-057 FER weighted-logic audit — 2026-08-28

Date: 2026-08-28

Status: HOLD / PARTIAL / READ-ONLY.

No gameplay, AI, decision, mission, trigger, effect, localisation, asset, central-admission, or runtime file was edited by this audit.

## Disposition

The Far Eastern Republic package (FER, package `iw_057`) remains package-local and fail-closed.

The current HOI4 MCP mission inspection proves that the source contains a complete eleven-ID `ai_will_do` candidate list, but the available scenario evidence does not prove a live FER ranking, activation timing, normalized selection probability, or balance acceptance.

The current strategy adapter exposes no weighted candidates, and the direct decision adapter delegates to the mission adapter rather than exposing a separate decision surface.

The known source risk in `independence_wave_fer_settled_compact` remains unresolved because its enable block omits the setup/current-generation guards used by the other FER profiles.

The current Event 006 boundary remains 32 content-attested selectable packages, 40 runtime adapters, 29 compatible reservation groups, and 161 unattested selectable rows out of 193 non-overlay rows.

## Audited surfaces and source authority

| Surface | Current source and identifiers | Scope finding |
| --- | --- | --- |
| FER mission and project AI | `common/decisions/006_independence_wave_far_eastern_decisions.txt:15-603`; category `independence_wave_fer_railway_compact_category` | One activation-only founding mission plus ten serialized FER projects, all with positive `ai_will_do` values. |
| FER package validity | `common/scripted_triggers/006_independence_wave_far_eastern_package_triggers.txt:11-252` | Exact FER identity, IW-057 package, origin, setup, ordered 408/409 anchor, current-generation force package, capital, former-host, route, ledger, roster, and resource gates are source-visible. |
| FER AI strategy | `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:589-657` | Four profile blocks are present in the canonical merged registry: railway-port survival, host restraint, settled compact, and coastal emergency guard. |
| FER tuning constants | `common/script_constants/006_independence_wave_constants_registry.txt:991-1008,1251-1265,1616-1657` | Shared decision score bands are `standard=10`, `high=25`, and `urgent=100`; FER strategy and duration constants are centralized in the registry. |
| FER package effects | `common/scripted_effects/006_independence_wave_far_eastern_package_effects.txt:1-497` | Setup, project, route, failure, and cleanup effects are package-local and remain downstream of the unresolved central admission/identity receipts. |
| Central admission | `history/general/006_independence_wave_character_recruitment_registry.txt`, `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`, `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt`, and `common/scripted_effects/006_independence_wave_join_effects.txt` | FER is intentionally absent from startup recruitment, central adapter/attestation, dispatch, preflight, and deterministic Join. |

The source-of-truth authority is `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` together with `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md`, `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md`, and `docs/specs/006_independence_wave_specs/quality/package_manifest.md`.

The current package authority is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw057_fer_admission_audit_next_2026-08-27.md`; the earlier decision/mission receipt is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw057_fer_decision_mission_audit_current_2026_08_15.md`.

The earlier handoffs' standalone AI path `common/ai_strategy/006_independence_wave_far_eastern.txt` is historical provenance; the current source path is the merged registry named above.

## Candidate pool and authored score trace

The exact mission candidate pool supplied to MCP is:

`independence_wave_fer_hold_railway_council`, `independence_wave_fer_secure_railway_ports`, `independence_wave_fer_integrate_coastal_guards`, `independence_wave_fer_register_fer_communities`, `independence_wave_fer_settle_former_host_ledgers`, `independence_wave_fer_ratify_constitutional_autonomy`, `independence_wave_fer_adopt_railway_charter_compact`, `independence_wave_fer_convene_coastal_councils`, `independence_wave_fer_establish_coastal_emergency_command`, `independence_wave_fer_codify_durable_sovereignty`, and `independence_wave_fer_open_pacific_corridor`.

The source candidate pool is complete relative to the eleven authored `ai_will_do` blocks, but runtime availability is not complete in the empty fixture.

| Candidate | Base willingness | Authored modifier trace | Source classification |
| --- | ---: | --- | --- |
| `independence_wave_fer_hold_railway_council` | `urgent = 100` | None; `available = { always = no }` and activation is separately gated. | Positive activation-only score; latent dead/hidden-weight review item. |
| `independence_wave_fer_secure_railway_ports` | `high = 25` | None. | Score-only. |
| `independence_wave_fer_integrate_coastal_guards` | `high = 25` | `factor = 2` when `has_war = yes`, giving 25 in peace and 50 in war. | Score-only; wartime sensitivity unresolved in a valid pool. |
| `independence_wave_fer_register_fer_communities` | `high = 25` | None. | Score-only. |
| `independence_wave_fer_settle_former_host_ledgers` | `standard = 10` | `factor = 2` when `NOT = { has_independence_wave_severe_host_threat = yes }`, giving 20 without severe threat and 10 otherwise. | Score-only; former-host state unresolved. |
| `independence_wave_fer_ratify_constitutional_autonomy` | `high = 25` | None. | Score-only; route validity unresolved. |
| `independence_wave_fer_adopt_railway_charter_compact` | `standard = 10` | None. | Score-only; route validity unresolved. |
| `independence_wave_fer_convene_coastal_councils` | `high = 25` | None. | Score-only; route validity unresolved. |
| `independence_wave_fer_establish_coastal_emergency_command` | `urgent = 100` | `factor = 2` when `has_war = yes`, giving 100 in peace and 200 in war. | Score-only; wartime dominance and emergency validity unresolved. |
| `independence_wave_fer_codify_durable_sovereignty` | `high = 25` | None. | Score-only; settlement, route, and resource state unresolved. |
| `independence_wave_fer_open_pacific_corridor` | `standard = 10` | None. | Score-only; network/League validity unresolved. |

These values are exact source willingness scores only.

They are not click probabilities, and they must not be divided by an assumed pool total.

## Named scenario contract

The only accepted named scenario set is `IW057_FER_EMPTY_TYPED_BASELINE_2026_08_15` with scenario hash `2c89ce66f56c07b9eff850e73dfa77bb48ade645331729407c489850b53e1c58`.

Its twelve scenario IDs are `FER_408_FRAGILE_PEACE`, `FER_409_FRAGILE_PEACE`, `FER_408_HOST_WAR`, `FER_409_HOST_WAR`, `FER_408_STABLE_ROUTE_LOCK`, `FER_409_STABLE_ROUTE_LOCK`, `FER_408_NETWORK_READY`, `FER_409_NETWORK_READY`, `FER_408_RESOURCE_STARVED`, `FER_409_RESOURCE_STARVED`, `FER_408_IMPOSSIBLE_AMBITION`, and `FER_409_IMPOSSIBLE_AMBITION`.

Every scenario supplied `state = {}` because the typed FER fixture shape was rejected by the available adapter in the prior source-of-truth handoff.

No scheduled state changes, seed, uncertain-input distribution, custom-pool cadence, cooldown, recovery rule, cap, removal rule, reset, or terminal-state transition was declared.

The scenario candidate list is complete relative to source, but the engine-available pool is incomplete because identity, package, setup, current-generation, anchor, capital, host, route, ledger, resource, and central-admission inputs are absent from the fixture.

## Mandatory MCP probability evidence

All calls used workspace `mod_chaos_redux_ea3b2d67c2c0`.

### Read-only inspections

| Adapter and source | Result | Artifact, revision, and hash |
| --- | --- | --- |
| `mission_ai_will_do`, `common/decisions/006_independence_wave_far_eastern_decisions.txt`, exact eleven-candidate pool | `PROBABILITY_SOURCE_INSPECTED`; `poolComplete=true`, 11 candidates, 0 available candidates, 18 required inputs, 0 inspect-unresolved items. | Artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/875f237fb1f621b1c52560fb1788ba2cfb8807dabdb8630d3cf81de59a3be1a2/dbfef2b071b0022b45b81011454b9f0c67f8da84bf96093027d8e36142b77f05/probability-inspect-e7735d0cc36c.json`; source revision `4b586b7e3a6d1a55782a9abb1d8fb9b9842eccf9db2fbb6f5ef91db70c498835`; source hash `e7735d0cc36c3a10d032980b0db89f9f557e22f8575a8b4aa8b363c7a1ad390d`. |
| `decision_ai_will_do`, same FER decision source | `PROBABILITY_SOURCE_DISCOVERED`; requested decision surface empty, suggested adapter `mission_ai_will_do`, 11 available candidates through that adapter. | Artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9ff81c1e8b860923c1e562ef977a4a3f4466329ae3bbf175e4ac8a87d0b76715/14d2392a473531b73fcbb08e9a907c787149a98aeb51fbaec30eff65eb89d6a5/probability-inspect-e7735d0cc36c.json`; source revision `4b586b7e3a6d1a55782a9abb1d8fb9b9842eccf9db2fbb6f5ef91db70c498835`; source hash `e7735d0cc36c3a10d032980b0db89f9f557e22f8575a8b4aa8b363c7a1ad390d`. |
| `ai_strategy_factor`, `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt` | `PROBABILITY_SOURCE_DISCOVERED`; `discoveryReason=no_weighted_surfaces`, 0 candidates, 0 required inputs, 0 unresolved. | Artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c7221bd9a3e7de9a72cb6a24d8d337301be1212203e9af29df4e5469b68cc500/24b551124c2b26919ea99059529ab89338d7ea64f88a21c2abb7dd5715e951a2/probability-inspect-c9a81863c89a.json`; source revision `4b586b7e3a6d1a55782a9abb1d8fb9b9842eccf9db2fbb6f5ef91db70c498835`; source hash `c9a81863c89aca8b611e55390f96c29e65cb3d7cbd406eac37ce2e7ecc4ee005`. |

The strategy inspection is an adapter-discovery limitation, not proof that the authored strategy directives are absent or safe.

### Scenario evaluation

The fresh `hoi4.probability_evaluate` call used `mission_ai_will_do`, the exact eleven-candidate pool, the twelve named scenarios above, and a 420-day horizon.

It returned `PROBABILITY_ANALYZED_PARTIAL` with analysis ID `probability-823f4866eaccfc2682667da6`, source revision `4b586b7e3a6d1a55782a9abb1d8fb9b9842eccf9db2fbb6f5ef91db70c498835`, source hash `e7735d0cc36c3a10d032980b0db89f9f557e22f8575a8b4aa8b363c7a1ad390d`, scenario hash `2c89ce66f56c07b9eff850e73dfa77bb48ade645331729407c489850b53e1c58`, 12 scenarios, 132 candidate/scenario rows, 156 unresolved items, and 11 diagnostics.

All eleven candidates returned `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` across the twelve empty-state scenarios.

This never-eligible result is exact for the supplied empty `{}` fixtures only.

It is not evidence that the FER choices are dead in a valid campaign, and it does not establish an exact probability, rank, timing distribution, dominance, starvation, or balance result.

The evaluation JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d36cd5928c150f1b1c2d85e504d3f98392e87eb51a8309fc3a5552ba533bed87/358f9ec5d1b5dc289939e101db1b3fec24c8f61a98eed3a5da30d853a3b62bf1/probability-823f4866eaccfc2682667da6.json`.

The direct `decision_ai_will_do` evaluation returned `PROBABILITY_SURFACE_EMPTY` with the exact blocker `No weighted blocks matched this request` and no artifact.

The direct `ai_strategy_factor` evaluation returned `PROBABILITY_SURFACE_EMPTY` with the exact blocker `No weighted blocks matched this request` and no artifact.

### Sweep

The required `hoi4.probability_sweep` attempt used `findRankReversals=true`, `pairwise=true`, path `has_war`, and the named scenario set above.

It returned `PROBABILITY_SWEEP_RANGE_REQUIRED` with the exact blocker `Every sweep path requires a scenario range, numeric alternatives, or numeric state value` for scenario `FER_408_FRAGILE_PEACE` and path `has_war`.

No threshold, sensitivity, or rank-reversal result is therefore proven.

No numeric alternatives were invented to force a sweep over the empty fixture.

### Same-scenario comparison

Because no owner-applied AI-weight patch exists, a true before/after baseline comparison is not currently possible.

For capability evidence, `hoi4.probability_compare` was run with the current FER decision source on both `before` and `after`, the same exact eleven-candidate pool, and the same twelve-scenario set.

It returned `PROBABILITY_ANALYZED_PARTIAL` with analysis ID `probability-53105f8b128dc430d2dd8715`, source revision `4b586b7e3a6d1a55782a9abb1d8fb9b9842eccf9db2fbb6f5ef91db70c498835`, source hash `e7735d0cc36c3a10d032980b0db89f9f557e22f8575a8b4aa8b363c7a1ad390d`, the same scenario hash, 12 scenarios, 132 rows, 156 unresolved items, 11 diagnostics, and `comparisonChanges=0`.

This is a capability-only current/current comparison, not a balance or patch result.

The comparison JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/664f668ac6f6a75b98bb1e63b5a91bbbe05de54143b486787447e5fee7fe67d4/4f81acc5aaedbfa8e3e8a2a87fe98a4e303b31f7e383249d115634bee25bad1e/probability-53105f8b128dc430d2dd8715.json`.

The comparison visualization is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/e50cc0df12a82b7979760447f464a7611fce54c1931675a8269ccab571ff8424/probability-probability-53105f8b128dc430d2dd8715-comparison.svg`.

### Rendered probability evidence

`hoi4.probability_render` was run for `probability-823f4866eaccfc2682667da6` with the expected scenario hash `2c89ce66f56c07b9eff850e73dfa77bb48ade645331729407c489850b53e1c58`.

It returned `PROBABILITY_ANALYZED_PARTIAL` with the same source revision/hash and scenario hash, 12 scenarios, 132 rows, 156 unresolved items, and 11 diagnostics.

The authoritative rendered JSON is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bcba27d37934b9d414d41079841e87a22c45955a517ff93638e24fd0f0d12262/cd65b23e83c5b2b702f05ca64570c307b724ae8d9fc1f90fb63f8459e2d48575/probability-823f4866eaccfc2682667da6.json`.

The uncertainty-visible SVG evidence is:

- Ranking: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e7056862e9d24688e6b3eb67a64cbb1e723ee52877560e73a8895abe3bc05e13/1a026f2d9442f23a94fed6254d34b2b7cca1438b05ffce89d341e40fd2a9c9cf/probability-probability-823f4866eaccfc2682667da6-ranking.svg`.
- Matrix: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b93d8a9cf6231b7a10b95deb2c808e6162cdcdb3b387d37956dfb729cd76ab47/a78c9c86b4209fa81ff2f046b4eec834fe0c867489a475cb1fdb8f95fc4ace57/probability-probability-823f4866eaccfc2682667da6-matrix.svg`.
- Unresolved: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/79f0c7f926bfc07c62fc40fed06cd4c8e9922608be7814aee5ec2b1413263494/b7ef10f33201ca19a32a29c8a0a7df5bc1becec7eef084188e3a7bf1eb6d775a/probability-probability-823f4866eaccfc2682667da6-unresolved.svg`.
- Timing: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/67b5a0ee447fe12f0e449495f6314c2e825bf12805a4c0a9037a433af0f09317/4b3475236dc9bee56d0966f44ea46d013a7977bfbc73fb71e299a01991998607/probability-probability-823f4866eaccfc2682667da6-timing.svg`.
- Sensitivity: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5b5c9f25c05e945e4802758bf83a6ae6c00e228396e9d6b66826e5e21c99ad27/ed71f2d7ade42976e632e666178ff3c58141a56b8ee32e40798b4543ca7401eb/probability-probability-823f4866eaccfc2682667da6-sensitivity.svg`.
- Current/current comparison: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/8f41e91fa3e1610901e333886ac64fd8da7095c174c75c869db133f182f472f1/probability-probability-823f4866eaccfc2682667da6-comparison.svg`.

The rendered ranking, matrix, timing, sensitivity, and comparison views are partial evidence views that expose empty-fixture uncertainty; they are not campaign rankings or normalized odds.

## Structural MCP companion evidence

The required event-chain companion inspection used `hoi4.event_inspect` with selector `{ kind: event, eventId: chaosx.nr6.1 }`, downstream direction, bounded depth 2, and helper expansion.

It returned `EVENT_INSPECTED_PARTIAL` with revision `c2878e0a5f2b2d2bbbaa42bbd299a378b5a6c1d4ef25b9c4f58df51bcc9a885a`, graph hash `2bc5cc2753ec5ce3994c41b6a1627e92e2932f35821662e549f53f1ee04d4149`, 9,510 events, 14,700 options, 1,075 entries, 37,141 edges, 8,315 unresolved nodes, 2,129 diagnostics, and zero blocking diagnostics.

The validation remained partial because the large workspace deferred workspace-wide helper projections and lifecycle passes, and the inline source inventory was truncated to 64 of 349 paths.

The lint artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9e9d26ba19269bb8b79f94097ae853ae39cc897ce4dff31edb73f233ffa9a42f/ae905cd4d7e453c3a416b0810b40fff7d0df0dd2a162303285526c13311542e0/event-lint-c2878e0a5f2b.json`.

The matching `hoi4.event_render` overview returned `EVENT_RENDERED_PARTIAL` with the same revision and graph hash.

Rendered structural evidence is preserved in the overview manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eabb00bcf7ff09edadc7fdbb5d48eef34217ce4e6df876d561d66dfa273f3e69/3edb52c439737b62ba50d23587eee2168929f3c3b2fa75ef2a8de440b8ebeb3a/event-overview-c2878e0a5f2b-manifest.json`, overview JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9212daa0546412493f2506abc105f05809a1e9997fe1703c0113fd7c0d550ab0/34bb88b9a77024127b79c6ee33aa4d29eea94a8f010000bfc4198e6823a42110/event-overview-c2878e0a5f2b.json`, and diagram `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/69a9a6447b570ff47b69d48b7ed1c3b918be7bf53896e6b9bce0f13be205ab68/b677c8b07979785b57fc10854f1bc784923d4bab8efba8d81fcaef8267c8024c/event-overview-c2878e0a5f2b.svg`.

This structural evidence does not replace the probability pass and does not prove FER mission or strategy balance.

## Eligibility, validity, and weighted-risk findings

`is_independence_wave_fer_project_ready` requires exact FER package identity, IW-057 setup completion, an owned/controlled 408 or 409 anchor, the current-generation force package, and no compact-crisis failure.

The runtime-ready and setup triggers add capital-anchor, former-host protected-state, roster, force, route, network, array, and lifecycle receipts, while project availability adds per-project completion state, cost resources, capital control, and one-active-project serialization.

The founding mission has a positive urgent score of 100 but `available = { always = no }`; this may be intentional activation-only design, but the engine treatment of its positive score remains unresolved and should be confirmed before calling it safe.

Four route-install decisions use route-specific `visible` predicates, but their `available` blocks repeat project readiness, cost, capital, and one-active-project checks without repeating the route predicate.

Whether the engine excludes a hidden route-incompatible decision from AI consideration is unresolved in the empty fixture, so this is a source-level validity risk rather than a proven defect.

The positive `high`, `urgent`, and `standard` scores create an authored ordering in which emergency command can reach 200 during war, but the MCP supplied pool has no eligible candidates and therefore cannot establish dominance or starvation.

The two wartime modifiers and one severe-host-threat modifier are the only authored FER decision score modifiers found in the current source.

The one-active-project predicate limits simultaneous project repetition and duplicate payment, but no complete sequence contract was supplied for cadence, cooldown, recovery, retries, reset, cap, or terminal transitions.

The package-local effects and earlier source receipt indicate costs are paid before timers and are not refunded on cancellation, which is a source-level anti-free-retry property, not a live exploit-safety proof.

The current strategy profile `independence_wave_fer_settled_compact` enables on package identity and `independence_wave_fer_compact_stabilized` but does not repeat `independence_wave_iw_057_setup_complete` or `has_independence_wave_force_package_for_current_generation`.

The other three profiles include setup/profile or host/emergency predicates, but the `ai_strategy_factor` adapter did not expose any analyzable blocks, so strategy dominance, stale-state persistence, and exact validity remain unresolved.

The FER package duration constants are `founding_crisis=420`, `project_short=45`, `project_standard=75`, and `project_long=105`, while the current decisions consume shared `independence_wave_decision_duration.short=75`, `.standard=120`, `.long=180`, and `.strategic=300` values.

This duration-source mismatch is a separate timing-drift review item and was not treated as an AI-weight conclusion.

## Result classification

The source score table is **exact, score-only**.

The mission inspection is **exact for source discovery** with a complete eleven-candidate source pool, but zero available candidates under the empty fixture.

The twelve-scenario evaluation and all rendered probability views are **bounded/partial**, with 132 candidate/scenario rows, 156 unresolved items, and all candidates never eligible under `state = {}`.

The same-scenario current/current compare is **partial capability evidence only** with `comparisonChanges=0`, not a true before/after comparison.

The strategy and direct decision surfaces are **unresolved for quantitative analysis** because their adapters returned no weighted surface.

No exact selection probability, normalized odds, timing distribution, dominance limit, starvation limit, rank reversal, repetition rate, or campaign snowball claim is supported.

## Skipped analyses and exact reasons

`hoi4.probability_sweep` produced `PROBABILITY_SWEEP_RANGE_REQUIRED` because the named empty scenarios contained no numeric alternative or range for `has_war`.

`hoi4.probability_simulate` was not run because no uncertain-input distribution, correlation model, seed, or sampling contract was declared.

`hoi4.probability_sequence` was not run because no complete custom weighted pool with cadence, cooldown, recovery, removal, reset, cap, retry, replacement, and terminal-state transitions was declared.

No callable `chaosx_ai_probability_auditor` worker route is exposed in this runtime, so these direct MCP receipts are not a worker sign-off.

No decision-specific structural MCP inspector is exposed; the mission probability adapter and the shared event/decision-window evidence are the available read-only routes.

No HOI4 launch or live consumer validation was performed.

## Safe next steps for the owning agent

1. Keep IW-057 outside central Event 006 admission, deterministic Join, and startup recruitment until identity/roster/flag receipts, central adapter/attestation/preflight, and typed scenario fixtures are accepted.

2. Preserve the exact candidate pool and scenario IDs above when a supported typed or engine-backed fixture becomes available, and rerun `hoi4.probability_inspect` before any AI change.

3. Provide all 18 required inputs, including original tag/active status, origin/setup/current-generation receipts, 408/409 ownership/control/capital, former-host validity and war, roster, compact/crisis ledgers, route/government, network/League, completion state, cost resources, and `has_war`/severe-host threat.

4. Re-run `hoi4.probability_evaluate` on the same twelve scenario IDs, then provide explicit `has_war=false/true` and severe-host-threat alternatives to `hoi4.probability_sweep` so rank reversals and modifier thresholds are actually tested.

5. Review the route-specific `available` blocks against AI eligibility semantics before admission; do not assume `visible` alone excludes hidden route-incompatible choices from AI scoring.

6. Review `independence_wave_fer_settled_compact` for setup/current-generation guards, but apply any change only through an owner-approved patch followed by a same-scenario `hoi4.probability_compare` using the exact scenario hash and candidate pool above.

7. Reconcile the FER package-specific 45/75/105 duration constants with the shared 75/120/180/300 decision durations in a separate timing-approved change, not inside a weight audit.

8. Use `hoi4.probability_sequence` only after the owner declares the complete serialized-project cadence, cooldown/recovery behavior, paid-cost and cancellation transitions, retry/removal/reset rules, and terminal states.

No simplification was applied to gameplay, no fallback identity or asset was introduced, and no balance target was chosen by this auditor.
