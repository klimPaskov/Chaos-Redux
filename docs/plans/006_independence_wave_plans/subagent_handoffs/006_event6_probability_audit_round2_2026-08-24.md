# Event 006 Independence Wave probability audit round 2 — 2026-08-24

## Status and scope

This is a read-only weighted-logic audit handoff for Event 006.

Disposition: **MCP-BLOCKED / CURRENT ENGINE CONCLUSIONS UNRESOLVED**.

The earlier same-day handoff at `docs\plans\006_independence_wave_plans\subagent_handoffs\006_event6_probability_audit_round_2026_08_24.md` contains historical partial MCP receipts from older source revisions.
This round does not invalidate those receipts, but it cannot re-use them as current evidence because the current local source hashes differ and the installed MCP transport closed during the current source-qualified calls.

No gameplay, AI, event, focus, decision, mission, strategy, random-list, localisation, technology, doctrine, country, asset, or runtime file was edited.
Only this documentation handoff is in scope.

Repository root: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.

## Required references reviewed

The repository instructions and the applicable skills were read before the audit.

The offline Paradox wiki pages reviewed were `Data structures - Hearts of Iron 4 Wiki.md`, `Triggers - Hearts of Iron 4 Wiki.md`, `Effects - Hearts of Iron 4 Wiki.md`, `Modifiers - Hearts of Iron 4 Wiki.md`, `Localisation - Hearts of Iron 4 Wiki.md`, `Scopes - Hearts of Iron 4 Wiki.md`, `On actions - Hearts of Iron 4 Wiki.md`, `Event modding - Hearts of Iron 4 Wiki.md`, `Decision modding - Hearts of Iron 4 Wiki.md`, `Idea modding - Hearts of Iron 4 Wiki.md`, and `AI modding - Hearts of Iron 4 Wiki.md`.

The vanilla documentation reviewed was `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, `dynamic_variables_documentation.md`, and `script_collection_input.md`.

The applicable repository skills were `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-mtth`, `chaos-redux-focus-trees`, and `chaos-redux-decisions-missions`.

The wiki distinction used in this handoff is material: `ai_will_do` and focus AI are willingness score races, `ai_chance` is probability-proportional event-option sampling, and `random_list` is probability-proportional weighted sampling after the complete valid pool is known.
Raw score constants are not reported as click probabilities.

## Audited source surfaces and current static census

| Surface | Current source files or identifiers | Static census and MCP route |
| --- | --- | --- |
| Automatic allocator outer and inner pools | `common\scripted_effects\006_independence_wave_package_allocator_effects.txt`, `common\scripted_effects\006_independence_wave_package_planner_effects.txt`, `common\scripted_effects\006_independence_wave_package_region_effects_registry.txt` | One outer `random_list` at allocator line 58 with 14 regional entries; each region has a nested package `random_list`; 14 region prepare blocks, 14 region select blocks, and 144 explicit `prepare_weight_iw_*` wrappers were found. Required adapter: `random_list` and the declared custom-pool route. Current inspect/evaluate/sweep/compare/render all blocked by transport. |
| Exact ladder and allocation factors | `common\script_constants\006_independence_wave_constants_registry.txt`, planner `independence_wave_capture_wave_tuning` | Automatic target counts are Calm 3, Gathering 4, Rising 5, Chaos Tier 7, Totalen 10, and World Collapse 10. Required adapter: allocator `random_list` under named ladder scenarios. Current engine result unresolved. |
| MTTH and evolution timing | `common\mtth\006_independence_wave_evolution_mtth.txt`, `common\scripted_effects\006_independence_wave_evolution_effects.txt` | `independence_wave_evolution_interval` is consumed through `mtth:` and clamped to 90–720 days after calculation. Required adapter: `event_mean_time_to_happen` or the installed equivalent. Current inspect/evaluate blocked; no timing distribution exists for this round. |
| Root Event 006 options | `events\006_independence_wave.txt` | 11 `ai_chance` blocks and the 20 root option IDs identified by the prior same-day source census. Required adapter: `event_option_ai_chance`. Current inspect/evaluate/sweep/compare/render blocked. |
| Support event options | `events\006_independence_wave_support_events.txt`, `events\006_independence_wave_form01_02_04.txt`, `events\006_independence_wave_iw043_iw058.txt`, `events\006_independence_wave_iw093_iw098.txt`, `events\006_independence_wave_mediterranean.txt`, `events\006_independence_wave_rhineland_bavaria.txt`, and `events\006_independence_wave_wallonia_frisia.txt` | Current static census is 16, 12, 68, 6, 14, 14, and 6 `ai_chance` blocks respectively, 147 across the eight current Event 006 event files. Each source-qualified inspect was attempted and returned `Transport closed`. |
| Shared and package decisions/missions | `common\decisions\006_independence_wave_decisions.txt` plus the current `common\decisions\006_independence_wave_*_decisions.txt` family | 774 `ai_will_do` blocks across the current Event 006 decision family, including 64 in the shared decision file. Required adapters: `decision_ai_will_do` and `mission_ai_will_do`. Current source-qualified inspect calls were blocked. |
| National focus AI | `common\national_focus\006_independence_wave_focus.txt`, `common\national_focus\006_independence_wave_iw043_iw058_focus.txt`, `common\national_focus\006_independence_wave_iw093_iw098_focus.txt`, and `common\national_focus\006_independence_wave_pacific_focus.txt` | 318 `ai_will_do` blocks, including 207 in the shared tree. Required adapter: `national_focus_ai_will_do`; structural routes are `hoi4.focus_inspect` and `hoi4.focus_render`. Current probability and structural calls were blocked. |
| AI strategy factors | `common\ai_strategy\006_independence_wave_ai_strategy_registry.txt` | 724 `ai_strategy = { ... }` blocks. Required adapter: `ai_strategy_factor`. The source uses strategy values and enable/abort predicates rather than a probability-proportional candidate pool. Current inspect was blocked, so no strategy trace is claimed. |
| SCN-008 and other custom pools | `common\scripted_effects\006_independence_wave_scenario_effects.txt`, `common\scripted_effects\006_independence_wave_join_effects.txt` | SCN-008 navigation is an ordered registry/control path in source, not a discovered weighted pool. Join has an explicit 90-day cooldown and ordered retry/cleanup behavior, but no complete custom-pool manifest was available. Required custom-pool and sequence routes are unresolved. |

The current exact file census was obtained from the live tree rather than copied from a stale handoff.
The event file names above are the files currently present under `events\`; older handoffs mention event files that are no longer in the current tree.

## Current local source fingerprints

These are local SHA-256 fingerprints, not MCP source revisions.
They are included to prevent accidentally treating older MCP artifacts as current.

| Source | Current local SHA-256 |
| --- | --- |
| `events\006_independence_wave.txt` | `897DCB16BD33149D884D33CEF80AE80C9F0555419C18B2F442D8759929224112` |
| `common\scripted_effects\006_independence_wave_package_allocator_effects.txt` | `06B16540BC44C0D937EBBDCE3D0ECA8E66729AC58F5D092A16C5E08F80839159` |
| `common\scripted_effects\006_independence_wave_package_planner_effects.txt` | `AB54B783EDB02360143905D7F44D76EEF2991111D352A4A3FEC96CF304E815DF` |
| `common\scripted_effects\006_independence_wave_package_region_effects_registry.txt` | `37B2BF724CCB7AD92870DFB8B6661AD4CB2964366453F5FA26FC529F48A03110` |
| `common\mtth\006_independence_wave_evolution_mtth.txt` | `0BD139B5B2A64FB784231A200EC92C5721CEBBC548CA8E740347721A453A5854` |
| `common\decisions\006_independence_wave_decisions.txt` | `41F4E187D8A114796A7C4A8A21856AF6DFA49891828EC4A4488083E4C29EA33D` |
| `common\national_focus\006_independence_wave_focus.txt` | `C45549019A381410A9E7BD2173F574E3F10D43F49E95B922DC379056A3B959B4` |
| `common\ai_strategy\006_independence_wave_ai_strategy_registry.txt` | `029D37F162F48EDEF10F88762117F35381EB5004E5CF7B6AE133899B9676259C` |

## Source-only weighted logic facts

These facts are a source trace only.
They are not engine probability, timing, dominance, starvation, or balance results.

### Automatic ladder and allocator topology

`independence_wave_capture_wave_tuning` maps the global `chaos_tier` flag to the exact ladder `3/4/5/7/10/10`.
Calm defaults to compact territory and fragile force, Gathering and Rising use compact territory with viable force, Chaos Tier and Totalen use extended territory with armed force, and World Collapse uses extended territory with high-chaos force.

`independence_wave_select_one_automatic_package` recomputes all 14 region totals before every draw, then performs an outer weighted region draw.
The selected region performs a second weighted draw over that region's package wrappers.
The planner comment and source calls recompute novelty and prior-wave memory before every draw, so this is a stateful without-replacement-like process rather than one static normalized pool.

The allocation loop stops when the target count is reached, when the pool is exhausted, or when the 206-attempt ceiling is reached.
An empty pool sets `independence_wave_plan_pool_exhausted`; a short joint plan fails closed with `insufficient_pool`, while a non-empty standalone plan may freeze the selected aligned subset.
This distinction requires a `probability_sequence` state machine to prove cadence, repetition, reset, and terminal behavior, and no complete sequence manifest was available.

The current constants expose base 100, sponsored candidate +100, registered tag +25, new region +30, new host +20, prior package -80, prior region -25, prior host -20, low-chaos signature -35, high-chaos +45, and minimum 1.
Evolution feedback values add or subtract separate package weights for replicable support, dormant registration or depth, armed-birth archetypes, sovereign-congress depth, and open-sovereignty routes.
World Collapse multiplies candidates whose earliest band is Totalen by 1.35 in the source.

The current planner gates the base weight behind runtime content attestation and the candidate earliest-band check.
The minimum-weight clamp is also inside the content-attestation gate in the current source.
The dated 2026-08-20 handoff records that this gate placement repaired the prior positive floor on unattested rows; this round does not re-patch or re-balance it.

The current constants registry declares 206 package IDs, while the region registry contains 144 explicit weight-wrapper IDs.
The difference is source inventory context only and must not be called a defect without a typed package-attestation and dispatcher trace.

### MTTH and timing

`independence_wave_evolution_interval` declares base 300 days, minimum 90 days, maximum 720 days, Gathering factor 1.15, Rising factor 1, Chaos Tier factor 0.85, Totalen factor 0.7, World Collapse factor 0.55, thin-network factor 1.25, dense-network factor 0.8, and dense-network threshold 15 active countries.

The consumer at `common\scripted_effects\006_independence_wave_evolution_effects.txt:692` assigns `mtth:independence_wave_evolution_interval`, clamps the result to the declared minimum and maximum, then adds the delay to `global.independence_wave_next_evolution_date`.
No MCP timing distribution, median, quantile, cumulative chance, or repetition interval was produced in this round.
The constants must not be hand-multiplied into an asserted timing result.

### Event options and AI scores

The root Event 006 option pool has 20 statically identified option IDs and 11 `ai_chance` blocks.
The support files add 136 more `ai_chance` blocks for the current 147-block total.
Every option's valid pool depends on event gates, package identity, host and target state, route flags, and helper triggers.
The static count does not prove that all 20 root options are simultaneously valid in any scenario.

The shared decision constants are `blocked = 0`, `very_low = 2`, `low = 5`, `standard = 10`, `high = 25`, `urgent = 100`, with score modifiers `0.5`, `2`, and `5`.
The focus constants are `none = 0`, `cautious = 5`, `standard = 10`, `high = 25`, `urgent = 100`, with preference factors `2`, `4`, prerequisite boost `1.5`, avoid factor `0.1`, and war-avoid factor `0.25`.
These values are score inputs and are not direct click probabilities.

The 724 strategy blocks use `ai_strategy` values with package setup, host threat, former-host, ledger, route, and crisis predicates.
No current strategy adapter trace proves whether any factor is active, additive, suppressed, or attached to an impossible route.

### Custom pool and sequence state

The source allocator has a custom stateful pool shape even though its exposed engine construct is nested `random_list`.
The complete state needed for a sequence audit includes current chaos band, target count, 206-attempt cap, runtime attestation, package earliest bands, host and anchor reservation, current-wave selected package/region/host arrays, previous-wave package/region/host arrays, optional expansion phase, Event 005 collision state, and exact-count failure mode.

SCN-008 uses deterministic scenario registry traversal and navigation decisions rather than an exposed weighted block.
The Join path records cooldown, retry, reset, and terminal history, but it is an ordered first-success path rather than a probability pool.
No current `probability_sequence` result proves cadence, cooldown recovery, removal, reset, cap, or terminal-state behavior for either system.

## Named scenarios and completeness contract

The following scenario names are retained from the Event 006 audit contract and must be re-used after MCP recovery.
They are listed here as required control IDs, not as current results.

| Scenario set | Named scenarios | Candidate-pool completeness | External-factor completeness | Round 2 result |
| --- | --- | --- | --- | --- |
| `E6_ALLOCATOR_LADDER_2026_08_24` | `ALLOC_UNIFORM_COMPLETE`, `ALLOC_CALM_3`, `ALLOC_RISING_5`, plus target-count cases 3, 4, 5, 7, 10, and World Collapse 10 | The 14 outer region keys can be declared, but current per-package validity and the 32-attested/40-adapter runtime state were not supplied to MCP this round | Missing live attestation, earliest-band, host/anchor, novelty, previous-wave, collision, sponsorship, and optional-expansion state | Unresolved; inspect/evaluate/sweep/compare/render all returned `Transport closed` |
| `E6_ROOT_OPTION_MATRIX_2026_08_24` | `E6_CORE_EMPTY_CURRENT_2026_08_24`, `E6_SHARED_DECISION_EMERGENCY_2026_08_24`, `E6_SHARED_DECISION_PROVISIONAL_2026_08_24` | The 20 root option IDs are statically known; complete valid option pool is not proven | Missing event helper predicates, route, host, target, league, patron, ownership, capacity, recognition, and instability state | Unresolved; no current analysis ID or scenario hash |
| `E6_EVOLUTION_MTTH_MATRIX_2026_08_24` | Base, chaos-tier, network-thin, and network-dense timing states | MTTH source and consumer are known, but the installed adapter did not return a typed block | Missing date, active-country count, chaos flag, and MTTH distribution inputs | Unresolved timing |
| `E6_SHARED_DECISION_EMPTY_2026_08_24` and `E6_SHARED_DECISION_NUMERIC_MATRIX_2026_08_24` | Empty, emergency, provisional, low/high capacity, low/high recognition, and low/high instability fixtures | Shared action IDs are present in source; route and target validity are incomplete | Missing package identity, capital, host, costs, ledgers, resources, war, and external modifiers | Unresolved score race |
| `E6_KUB_MISSION_MATRIX_2026_08_24` and `E6_TAT_MISSION_MATRIX_2026_08_24` | `KUB_FRAGILE_PEACE`, `KUB_SEVERE_HOST_WAR`, `TAT_FRAGILE_PEACE`, `TAT_SEVERE_HOST_WAR` | 11-action package mission pools are source-known but not current MCP-confirmed | Missing setup, country identity, package project, activation, capital/control, former-host, ledger, and resource state | Unresolved score race |
| `E6_FOCUS_ROUTE_RACE_2026_08_24` and `E6_FOCUS_EXTERNAL_MATRIX_2026_08_24` | `FOCUS_OPEN_CALM`, `FOCUS_HOST_CRISIS`, `FOCUS_ROUTE_LOCKED`, `FOCUS_NO_VALID_ROUTE`, and external-complete companion state | 318 focus score blocks exist, but a country-specific available/prerequisite pool is not supplied | Missing prerequisite completion, strategy plan, patron/former-host, package route, and host state | Unresolved score race |
| `E6_SCENARIO_MODE_2026_08_24` | SCN-008 mode/intensity navigation cases | Ordered registry is source-known; no weighted candidate pool was exposed | Missing complete scenario transition and terminal-state manifest | Unresolved custom-pool/sequence behavior |

No scenario in this round has a current scenario hash, analysis ID, current MCP source revision, or current rendered evidence.

## MCP calls, artifacts, and exact blockers

### Initial discovery and source-qualified inspect

The first read-only call was `hoi4.probability_inspect({})`.
It returned `PROBABILITY_ADAPTERS_LISTED`, status `ok`, workspace `mod_chaos_redux_ea3b2d67c2c0`, `adapters = 11`, `candidates = 0`, `availableCandidates = 0`, `availableAdapters = []`, and no artifact.

The first invalid source probe used a string and returned the exact validation error `MCP error -32602: Input validation error for tool hoi4.probability_inspect: Invalid input: expected object, received string at source`.
The `{ relativePath = ... }` source probe returned `Unrecognized key: "relativePath" at source`.
The `{ path = ... }` source form was accepted by schema, but the allocator/planner path call timed out with `tool call failed for hoi4_agent_tools/hoi4.probability_inspect; Caused by: timed out awaiting tools/call after 180s`.
After that timeout, the probability transport closed.

The current source-qualified `hoi4.probability_inspect` batch covered all 17 weighted paths listed below.
Every call returned the exact error `tool call error: tool call failed for hoi4_agent_tools/hoi4.probability_inspect; Caused by: Transport closed`.

```text
events\006_independence_wave.txt
events\006_independence_wave_support_events.txt
events\006_independence_wave_form01_02_04.txt
events\006_independence_wave_iw043_iw058.txt
events\006_independence_wave_iw093_iw098.txt
events\006_independence_wave_mediterranean.txt
events\006_independence_wave_rhineland_bavaria.txt
events\006_independence_wave_wallonia_frisia.txt
common\mtth\006_independence_wave_evolution_mtth.txt
common\decisions\006_independence_wave_decisions.txt
common\national_focus\006_independence_wave_focus.txt
common\ai_strategy\006_independence_wave_ai_strategy_registry.txt
common\scripted_effects\006_independence_wave_package_allocator_effects.txt
common\scripted_effects\006_independence_wave_package_planner_effects.txt
common\scripted_effects\006_independence_wave_package_region_effects_registry.txt
common\scripted_effects\006_independence_wave_scenario_effects.txt
common\scripted_effects\006_independence_wave_join_effects.txt
```

### Related probability tools

The current allocator fixture calls were attempted after the inspect failure.
`hoi4.probability_evaluate`, `hoi4.probability_sweep`, `hoi4.probability_compare`, and `hoi4.probability_render` each returned the exact `Transport closed` tool error.
No current analysis ID, comparison ID, scenario hash, artifact URI, or rendered evidence path was generated.

`hoi4.probability_simulate` was not run because no uncertain-input distribution, correlation model, seed, or horizon was explicitly declared.
`hoi4.probability_sequence` was not run because the allocator and SCN-008 state transitions lack a complete declared cadence, cooldown, removal, recovery, reset, cap, and terminal-state manifest.

### Structural MCP tools

Current `hoi4.event_inspect`, `hoi4.event_render`, `hoi4.focus_inspect`, and `hoi4.focus_render` calls were attempted with source-qualified Event 006 selectors.
Each returned `tool call error: tool call failed for hoi4_agent_tools/hoi4.<tool>; Caused by: Transport closed`.
No current structural revision, graph/layout hash, or rendered path is claimed.

### Historical control receipts retained for parent review

The following prior artifacts remain useful as dated capability and fixture evidence only.
They are not current-revision proof for this round.

| Surface | Prior revision/hash and scenario receipt | Artifact or rendered evidence |
| --- | --- | --- |
| Outer allocator inspect | Prior source revision `3771942e4d960525d9213bb00bc6d4e257650cc3f466c5aba0920128723f67d8`; source hash `bc6f7ff8598df33b610442e6ada24c28d7d82167fe135474debb18094b3b6cf83`; 14-entry pool complete for that fixture | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/51ba0f1ca30228868d32e098eccf06028b6af9d4fff0b88996c9cac8c026765d/a6337fa215e774e3109e3ad2a27dc907af3a20bc638f2f1b330340675d6e7387/probability-inspect-bc6f7ff8598d.json` |
| Allocator ladder fixture | Analysis `probability-820fc7081d76f1373d2ed61d`; source revision `267b26adf8675821e3e6693136584a7185f5c297e1ebe12b500117a757bd734a`; scenario hash `68b32e03267da5726b7df85f725bc57a61e7ef2adafb27488351b60bfa37c4fc`; `ALLOC_UNIFORM_COMPLETE`, `ALLOC_CALM_3`, and `ALLOC_RISING_5` only | JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b24d1113a5ab8c48245f69008a8d1c8ef5d6d52a879b923abce0bcc8f41fc0b9/038a3674d893c729427b17c7ab3d1399ee4e45f5f297cc51618eb5b2c3ba4848/probability-820fc7081d76f1373d2ed61d.json`; calm ranking `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5cb72ade9675f4bfc3b47ff3d01d2ab228cd67b9ac191ec1fe38002d22f19d34/55363aa40a9c48eab791e0c052ec7b3829ea3f19c4fc4abbd34a3af9f8822dc5/probability-probability-820fc7081d76f1373d2ed61d.json` |
| Allocator current/current control | Analysis `probability-86c4f3e6f2cfb5bd4c041c27`; scenario hash `68b32e03267da5726b7df85f725bc57a61e7ef2adafb27488351b60bfa37c4fc`; zero comparison changes for identical prior paths | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/83af3f617f1c808ff06e68dd4e41c715934a22b487f8cd1b69e0b23291ad6eb4/ea72a26805189622e161ecc0d69c7a6c01c4523543f2d7429219bac5e5799c17/probability-86c4f3e6f2cfb5bd4c041c27.json` |
| Root option partial matrix | Analysis `probability-e9dbbb5097d2250d656746df`; scenario hash `c2e87adec18afe6a1068492c3e2c31f2d51d7798a05a75407a3dc362da750703`; partial score-only result with unresolved validity inputs | JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/76f353970d1095f3a702e723a5acbab255084defc9ac7cbcfc177b94fb701583/2b282bb37b5fda82829992a18ef316a3d455ac369bd5c27258b99019f086f0ee/probability-e9dbbb5097d2250d656746df.json`; ranking `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a47ee50da9342da0bcc76ea98d54f1715fb8c6528def160a669380c573c58dfa/e9e0c31e6c7fb9cfff803624ac64a58061aa5580e9f9fc895069be6361654df9/probability-probability-e9dbbb5097d2250d656746df-ranking.svg` |
| Focus partial route race | Analysis `probability-5157df1afa15b89c3fa9403f`; scenario hash `2f723739b3836a436a5b314738e798c5da8b2a6b2185a8c7658df27c949704b3`; 184 candidates with unresolved external state | JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ca2845112f548ea8491deed84958c941e05eadffe4722fad1f2c3dd4c967b709/c2323ce7381afa0197115f0e052efe4b099aa4749c8299b39671b75ac8212e9f/probability-5157df1afa15b89c3fa9403f.json`; unresolved render `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9eb0edc98dd27d749dceb875ef30db0097ae4f38d2707885ca6a388649105f6f/b4b00b58d5abf8d0714efe5a4bbcd582f1efed5f33f574dc474d164fb789c7c0/probability-probability-5157df1afa15b89c3fa9403f-unresolved.svg` |
| MTTH discovery blocker | Prior `PROBABILITY_SOURCE_DISCOVERED` reported `no_weighted_surfaces` for the MTTH consumer, so it did not prove timing | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d3f9027725b333fcfd5d56d6cec28d87ae8c7a0c0a84a64efa8cf728c28a5515/699c006ae1f51b21dcb2e1fe17a7ed19dd21c517a82f28b6f2f160a95904f471/probability-inspect-4632b46c85507e33aebecedde8c423cdffa88506f790698b71f9396369a1a617.json` |

The complete prior artifact index remains in `006_event6_probability_audit_round_2026_08_24.md`.
No prior artifact is re-labelled as a current round 2 result.

## Findings and classifications

| Finding | Classification | Evidence boundary |
| --- | --- | --- |
| Exact ladder is 3/4/5/7/10/10 | Source-only | Constants and planner mapping are visible; no current MCP trace proves campaign availability or successful exact-count commits. |
| Outer allocator is a 14-entry weighted region draw with nested package draws | Source-only | The random-list topology is visible; current normalized region/package probabilities are unresolved. |
| Candidate weight modifiers and attestation/earliest-band gate are present | Source-only | Planner source trace only; no current modifier trace proves active values in a live scenario. |
| MTTH uses a 300-day base, named chaos/network factors, and 90–720-day clamp | Source-only | Source and consumer trace only; no timing distribution or repetition claim. |
| Event `ai_chance` and allocator random-list values are not interchangeable | Exact engine rule from offline documentation; current Event 006 result unresolved | Event options are proportional sampling; allocator is nested proportional sampling; decision/focus AI remains score-based. |
| Decision and focus score dominance | Unresolved | Candidate availability, prerequisites, and external state were not MCP-evaluated this round. |
| Positive weight on dead, hidden, blocked, or route-incompatible candidates | Unresolved | Current source has gates, but current MCP could not prove all gate outcomes. |
| Starvation and dominance | Unresolved | No current complete-pool evaluation or rendered ranking exists. Prior fixture starvation is confined to its historical fixture. |
| Rank reversal and sensitivity | Unresolved | Current sweep returned `Transport closed`; no current threshold or reversal artifact exists. |
| Repetition, cadence, cooldown, recovery, removal, reset, cap, and terminal behavior | Unresolved | No current sequence manifest or sequence analysis exists. |
| AI strategy additive/abort behavior | Unresolved score surface | Current strategy inspect was blocked and the source does not itself define a normalized candidate pool. |

The current source does not justify choosing a numeric balance target.
The dated attestation clamp repair is a source-history note, not a new patch recommendation.

## Recommended owner follow-up without applying a patch

1. Restore the HOI4 MCP transport and begin again with source-qualified `hoi4.probability_inspect` on every weighted source listed in this handoff.
2. Re-run `E6_ALLOCATOR_LADDER_2026_08_24` against the current source hashes with all 14 outer entries, every current package candidate, runtime attestation, earliest-band, host/anchor, novelty, previous-wave, sponsorship, collision, and optional-expansion state declared.
3. Re-run `E6_ROOT_OPTION_MATRIX_2026_08_24` with all 20 root option IDs retained in the pool, including zero-available options, and bind every helper trigger behind the 13 required inputs.
4. Re-run the same named decision, mission, focus, strategy, MTTH, SCN-008, and Join scenarios with typed route, prerequisite, resource, capital, host, former-host, ledger, patron, league, and terminal state.
5. Use `probability_sweep` for numeric sensitivity and rank reversals only after the complete candidate pool is accepted by inspect/evaluate.
6. Preserve a pre-change source path before any owner patch so `probability_compare` can compare two source objects with the same named scenarios; do not use a stale analysis ID as an unverified baseline.
7. Use `probability_sequence` only after the owner declares cadence, cooldown, recovery, removal, reset, cap, replacement, retry, and terminal-state transitions for the allocator or custom pool.
8. Keep all current numeric constants unchanged until the typed before/after comparison proves a specific issue; this audit selected no balance target.

## Skipped analyses and blockers

The current probability inspect batch was blocked by `Transport closed` after one source-qualified call timed out at 180 seconds.

Current `probability_evaluate`, `probability_sweep`, `probability_compare`, and `probability_render` calls were each blocked by `Transport closed`.

Current `event_inspect`, `event_render`, `focus_inspect`, and `focus_render` calls were each blocked by `Transport closed`.

Simulation was skipped because no uncertain-input distribution, seed, or sampling horizon was declared.

Sequence analysis was skipped because no complete custom-pool state-transition manifest was declared.

Technology, doctrine, and GUI weighted surfaces were not discovered in the Event 006 source inventory and were not in scope for this audit.

No gameplay patch, numeric tuning choice, or balance target was applied.
