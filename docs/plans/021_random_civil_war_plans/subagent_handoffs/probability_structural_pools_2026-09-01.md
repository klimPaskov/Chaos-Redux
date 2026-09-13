# Event 021 independent probability audit: structural pools

Audit date: 2026-09-01.

Scope: FRT-01..05, SET-01..06, GLB-01..07, CLU-01..05, and SCN-01..07 from `docs/specs/021_random_civil_war_specs/021_random_civil_war_probability_scenario_matrix.md`.

This is a read-only independent audit. No gameplay, localisation, asset, workbook, configuration, or existing report was changed, and no commit was made. The only file written by this audit is this handoff.

## Certification result

This slice does not pass probability certification. The required `probability_inspect` calls completed for the present named source families, but the installed adapter found no live candidates in any of them, and `common/scripted_effects/021_random_civil_war_scenario_effects.txt` is missing. The structural event route also returned a partial graph sourced from vanilla `game:` files rather than an Event 021 mod-source graph. Consequently there is no valid MCP probability result for any requested scenario, no scenario hash, and no analysis id from `probability_evaluate`, `probability_sweep`, `probability_sequence`, or `probability_simulate`.

Source-derived values below are score, gate, cap, or lifecycle evidence only. They are not selection probabilities.

## Audited source surface

The exact named source families were:

- `common\scripted_effects\021_random_civil_war_parent_effects.txt`
- `common\scripted_effects\021_random_civil_war_effects.txt`
- `common\scripted_effects\021_random_civil_war_scenario_effects.txt` — absent from the workspace.
- `common\scripted_effects\chaosx_event_cluster_effects.txt`
- `common\scripted_triggers\021_random_civil_war_triggers.txt`
- `common\script_constants\021_random_civil_war_constants.txt`

The event entry and direct integration references reviewed were `events\021_random_civil_war.txt`, `events\chaosx_event_clusters.txt`, the Event 021 parent/effect/triggers helpers named above, and the Event 006 bridge families discovered in the repository. Event 021's root identifier is `chaosx.nr21.1`.

Relevant identifiers and source anchors include `event021_parent_select_archetype` at parent-effects line 908, `event021_parent_select_connected_anchor` at line 1001, `event021_parent_expand_connected_region` at line 1045, `event021_parent_plan_connected_states` at line 1076, `event021_parent_validate_opening_plan` at line 1375, `event021_parent_start_secondary_civil_war` at line 2298, `event021_parent_start_ordinary_civil_war` at line 2453, `event021_parent_evaluate_settlement_topology` at line 3222, `event021_parent_select_settlement_terms` at line 3317, `event021_parent_apply_settlement` at line 3997, `event021_parent_add_target_to_selection_pool` at line 4193, `event021_parent_add_scenario_target_to_weighted_pool` at line 4223, `event021_parent_prepare_scenario_country` at line 4375, `random_civil_war_trigger_manual_scenario` at line 4543, and `event021_parent_dispatch_opening` at line 4707.

The direct effects surface contains `event021_random_civil_war_prepare_target` at line 389, `event021_prepare_archetype_weights` at line 479, `event021_prepare_opening_severity` at line 533, reservation and transaction helpers at lines 607–834, Event 006 admission helpers at lines 1062–1133, global capacity and target-pool helpers at lines 1431–1514, critical queue helpers at lines 1688–1763, settlement at line 1776, recurrence at line 1851, and scenario bypass/cleanup at lines 2045–2166.

The cluster surface contains Wars member registration around lines 1592–1668, member availability at line 2203, activation scanning at line 2285, gates at lines 2610–2755, live activation rolling at line 2906, optional ordering at lines 3048–3712, cooldown and pending-queue handling at lines 3780–3885, firing at lines 3885 onward, and Event 021 cluster firing at lines 5665 onward.

The trigger surface includes `random_civil_war_is_normal_human`, route-validity predicates, `random_civil_war_country_can_be_target`, `random_civil_war_automatic_target_valid`, `random_civil_war_scenario_target_valid`, `random_civil_war_event_pool_available`, and global critical-queue validity. The normal-human gate excludes `actual_nonhuman`; automatic targets exclude scenario bypass; scenario targets have a separate manual/type-preflight path.

## Probability MCP provenance

All six present named weighted source families were first sent to `hoi4.probability_inspect` with adapter `custom_weighted_pool`, `refresh: true`, and workspace `current`. The resolved MCP workspace was `mod_chaos_redux_ea3b2d67c2c0`.

| Source | Result | Source revision | Source hash | Artifact |
|---|---|---|---|---|
| `common/scripted_effects/021_random_civil_war_parent_effects.txt` | `PROBABILITY_SOURCE_INSPECTED`; `poolComplete=false`; candidates 0; available candidates 0; required inputs 0; unresolved 0; available adapters empty | `236ab42704e6d4e0310af04174d67122394277835d68d0cd276df336a346c4dc` | `6d6a23e510f29da5ade41458b6772dc78e4f9eb057eb06507119a78fa4b64994` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1f49f2e8af53d9140cb13d916b64a4ae336c4634c4d917a1b9bad00cbc2b2843/31bbb59ca332a615ca8be5f5869eb6aee79782ea82125887859bd6a2b9cc23e9/probability-inspect-6d6a23e510f2.json` |
| `common/scripted_effects/021_random_civil_war_effects.txt` | `PROBABILITY_SOURCE_INSPECTED`; `poolComplete=false`; candidates 0; available candidates 0; required inputs 0; unresolved 0; available adapters empty | `236ab42704e6d4e0310af04174d67122394277835d68d0cd276df336a346c4dc` | `c0850793676ec832c0a88b719689933c1b06f969c3844ca6646f820ee6f0b8e6` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/98c8949d0a7f7b308e01b4deeebae2ea14bca673ae9f178de3b6fd91095626c5/d95075f1bd6760cc9d1f976179e1ab7fcdc5c4e8a42e68f60c5f297456450ba5/probability-inspect-c0850793676e.json` |
| `common/scripted_effects/021_random_civil_war_scenario_effects.txt` | `PROBABILITY_SOURCE_NOT_FOUND`; no artifact | unavailable | unavailable | none |
| `common/scripted_effects/chaosx_event_cluster_effects.txt` | `PROBABILITY_SOURCE_INSPECTED`; `poolComplete=false`; candidates 0; available candidates 0; required inputs 0; unresolved 0; available adapters empty | `270a110e17de311864c2a4e8e22814fe0a0e16d5e15af35c4b094ab80408f64b` | `dc57453fb2b53b887182267999521221d44dc66cc0815550b3f7ba8afd6f681f` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2fac341968593b67c69db2bca58df018856f941ca560e56e663d1c01bf494fcc/ddfe526fd471b10a6c3ee7b48d7bb629ee52bf876744ca006f151aa405154594/probability-inspect-dc57453fb2b5.json` |
| `common/scripted_triggers/021_random_civil_war_triggers.txt` | `PROBABILITY_SOURCE_INSPECTED`; `poolComplete=false`; candidates 0; available candidates 0; required inputs 0; unresolved 0; available adapters empty | `51e26a4598554b1498fdaec08417ed2c81e0cb94238fcfb725122172d59d0117` | `02bfab82ff317195c4dfcb0be7caa3e06b369913c1ee435d80c941789d06aa35` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7aad5b44eecda2946dafe39229c0c12e578ced2fc85f8724e498d19c2dd6bd9e/63d71771bf3f58be6130ef2a18d4e78b4d8aa4296c0b51a36d4c8fe3b652e9f1/probability-inspect-02bfab82ff31.json` |
| `common/script_constants/021_random_civil_war_constants.txt` | `PROBABILITY_SOURCE_INSPECTED`; `poolComplete=false`; candidates 0; available candidates 0; required inputs 0; unresolved 0; available adapters empty | `4870e4a00b19574ac9b7db6b3fa5c1ebb2f7f59159277d75f8aa255c85f01049` | `7ca90b0af31f4d4aa3cee6fdb80e1f21b13f4d0d14585ed14bdb04248379bb28` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fc3144c3ea1547916ef2a8dd3d264243ebed04381ad78a60e50d5e7c8c59430e/2cb70e54585baef5a92ae74d0cc34d1918de4f17f55671fcf37f0cd6ff1736a7/probability-inspect-7ca90b0af31f.json` |

The exact missing-file MCP call was `hoi4_probability_inspect({"adapter":"custom_weighted_pool","source":{"path":"common/scripted_effects/021_random_civil_war_scenario_effects.txt"},"refresh":true,"workspaceId":"current"})`, which returned `PROBABILITY_SOURCE_NOT_FOUND` with message `Probability source path was not found`.

No custom manifest was submitted. A complete manifest cannot be derived honestly from the available source because the live country, state, force-package, Event 006, event-target, cluster-reservation, cooldown, and external-war pools are runtime inputs. A manifest containing expected scenario outputs would violate the adapter contract and was not used.

## Structural MCP provenance

The first event-inspect attempts used the wrong guessed id `chaosx.nr021.1`. The exact errors were `Invalid discriminator value. Expected 'event' | 'namespace' | 'file' | 'source' | 'node' | 'manifest' at selector.kind`, followed by `expected string received undefined at selector.eventId; Unrecognized key identifier` when `kind: "event"` was paired with `identifier`.

The corrected bounded call was:

```json
{"mode":"trace","direction":"downstream","expandHelpers":false,"maxDepth":6,"maxEdges":200,"maxNodes":160,"refresh":true,"selector":{"kind":"event","eventId":"chaosx.nr21.1"},"workspaceId":"current"}
```

It returned `EVENT_INSPECTED_PARTIAL` with revision `8cde42798e040fdadd5e86c2c299c46a8802c4ba48ebe7af4175cc8665b7864d`, graph hash `46db6136a16ab3119b59fa9c08b10cfb018dcbbdfbef7cdbaf77d618720da6e8`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bd2250fb45aa625ab7cf76f60d5a218c18fafe5f8b92a4c8ef027ebdbd46d098/00d2471632e0a24dba08cdd51e49ffcbddb54f837924993feec960767e4d778c/event-trace-8cde42798e04.json`. The result reported 9,725 events, 15,153 options, 1,138 entries, 8,698 unresolved nodes, 7,771 terminals, 38,341 edges, 30,319 state accesses, 2,206 issues/diagnostics, and one blocking diagnostic. Its `filesScanned` entries were vanilla `game:` files, and validation reported that workspace-wide helper and lifecycle projections were deferred.

The first render call was rejected because `maxNodes: 250` exceeded the schema limit of 240. The bounded retry was:

```json
{"view":"overview","direction":"both","expandHelpers":true,"maxDepth":3,"maxNodes":200,"refresh":true,"selector":{"kind":"file","sourcePath":"events/021_random_civil_war.txt"},"workspaceId":"current"}
```

It returned `EVENT_RENDERED_PARTIAL` with the same revision and graph hash, layout hash `d75b3b2778ac4e8b369f62a4d18269995cf0706b5c906bc73b7672cb4e347644`, and these artifacts: manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a02fc69c3a92858e06a6b774279e8eaff2e5fd842897eb1e71a1413fb2b6065c/3989838d17bfafb7988c37e90b39dc7459727dad5eaaf8e0e1abcb7f8f8812ff/event-overview-8cde42798e04-manifest.json`, JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c4e3ff1e49aabf849ccf6f3f882f4b99b77914368b7f76ed099bd15466eb145e/82948372b362554b940aa4e81bad1073964121718a05a2a9f15f7a91be9d4d44/event-overview-8cde42798e04.json`, SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/602dd32ddd16ee31fba593d857870a05c0bbf735eb1ec4600cc2ab1ad65329b3/c1f711cfdcd70e2257fa56f2dd00d273f82b3dab26fe5a091bed34745d892a58/event-overview-8cde42798e04.svg`, and PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ff54ff5fe612201ff52df93e292091c850f14750be5ba0aabdb61d92bfa91be2/7a0cf8d2bd620062881d542d6c8bcf9622d8b49bfcc7c2d71101a3e529195b1a/event-overview-8cde42798e04.png`. The render also scanned vanilla `game:` files and therefore is not accepted as Event 021 source evidence.

No probability artifact has an analysis id or scenario hash because no probability analysis progressed beyond inspection. No rendered probability evidence exists; `probability_render` had no valid analysis id to consume.

## Score and lifecycle evidence

`event021_random_civil_war_prepare_target` starts a target score at 10 and applies source-level terms of pressure times 4, failing authority plus 90, collapsed authority plus 160, a valid actor route plus 80, evidence count times 12, fragmentation over two controlled states plus 45, occupied plus 70, weak manpower plus 35, an Event 006 route plus 45, major-stage plus 50, nearby-conflict plus 60, recent-memory minus 120, and subject plus 20. It clamps and rounds the result to the configured 0–1000 range and sets or clears target-pool candidacy according to the eligibility gate. This is a score trace, not a normalized selection probability.

`event021_prepare_archetype_weights` initializes route weights, filters routes through route-validity triggers, applies route-evidence scaling and route-specific bonuses, and clamps each route to its configured maximum. The source does not expose a complete runtime route pool to the probability adapter, so no route ranking or share is certified.

`event021_prepare_opening_severity` contains a local random-list surface. The observed starting weights for Limited and Serious are 100 each; Severe and Critical require evolution, pressure/authority/state gates, and scenario conditions before entering the local pool. Because the analyzer found no candidates and the external state was not declared, no severity probability or rank is certified.

The constants provide severity ids Limited 1, Serious 2, Severe 3, and Critical 4; archetypes Ideological 1, Legal 2, Regional 3, Event 006 4, Command 5, and Same Tag 6; settlement ids Government Victory 1, Opposition Victory 2, Independence 3, Autonomy 4, Coalition 5, Partition 6, Merger 7, and Evolution 8; scenario types Political Fracture 1, Independence Cascade 2, Command Collapse 3, and Universal Fragmentation 4; and intensities Low 1, Medium 2, High 3, and Maximum 4.

Relevant timing/cap constants are initial review 30 days, stable review 120 days, exposed review 90 days, fractured review 60 days, critical review 15 days, evolution review 60–180 days, recurrence 60–180 days, successor grace 45 days, target cooldown 365 days, event memory 180 days, reconstruction 120 days, exposure cooldown 30 days, scenario batch maximum 7 days, and active launch lock 7 days. Capacity constants include baseline/evolution theater caps 2/3/4/5/6/8, front caps 4/6/8/10/12/16, global review batch 6, critical queue batch 3, scenario review batch 4, maximum generation 2, minimum remnant 1, multi-front minimum 2, maximum 5, maximum one-state count 1, and minimum force divisions 1. These are lifecycle parameters and do not establish observed timing distributions.

The Wars cluster registers repeated Random War and Fury rows plus Event 021 and Event 006 rows. The cluster code has member availability, activation, multiplicity, ordering, pending queue, cooldown, reservation, and failure/skip paths. The source constants include explicit skip categories such as no actor, no target, role collision, occupied tag, state reservation failure, cap reached, generation blocked, stale reservation, and incomplete package. Since no complete runtime member/target pool was available, no member rank, activation share, overlap probability, or cooldown distribution is certified.

## Scenario results

`Pool` is the candidate-pool completeness status. `External` lists the state that would have to be declared for a valid normalized analysis. Every row is unresolved for engine probability; deterministic rows are explicitly not treated as weighted probabilities.

### Front-count scenarios

| Scenario | Result and evidence classification | Pool and external-factor status |
|---|---|---|
| FRT-01 | Unresolved; deterministic front-plan lifecycle with no MCP count result | Incomplete country/region/state/force pool; requires coherent-region topology, route validity, force availability, front cap, remnant, and reservation state |
| FRT-02 | Unresolved; front expansion may be route/evolution gated, not a click probability | Incomplete opposition-region pool; requires two valid regions, evolution state, state connectivity, force package, and cap state |
| FRT-03 | Unresolved; bounded only by source cap constants, not by a measured distribution | Incomplete actor/front pool; requires all eligible actors, capacity, multi-front eligibility, force ratios, and reservation state |
| FRT-04 | Unresolved; source gate can reject fake actors, but MCP did not prove the live count | Incomplete leader/actor pool; requires one valid leader, controlled-state topology, route gates, and target reservations |
| FRT-05 | Unresolved; collision/alternate-package behavior is a deterministic validity branch, not a normalized share | Incomplete Event 006 package pool; requires both package manifests, anchors, origin reservations, tags, state reservations, and cluster ownership |

### Settlement scenarios

| Scenario | Result and evidence classification | Pool and external-factor status |
|---|---|---|
| SET-01 | Score-only/deterministic lifecycle; no numeric probability | Settlement terms are selected by topology/authority/legitimacy conditions; requires government profile, authority, fronts, and valid military/firm terms |
| SET-02 | Score-only/deterministic lifecycle; no numeric probability | Requires homeland, recognition, independence/autonomy eligibility, state ownership, and successor validity |
| SET-03 | Score-only/deterministic lifecycle; no numeric probability | Requires front parity, exhaustion, coalition/partition candidates, active fronts, and separate-peace validity |
| SET-04 | Score-only/deterministic lifecycle; no numeric probability | Requires hardliner profile, legitimacy, recurrence flags, pressure, and viable post-settlement state |
| SET-05 | Score-only/deterministic lifecycle; no numeric probability | Requires negotiator profile, guarantee/obligation candidates, enforceability, sponsor state, and settlement topology |
| SET-06 | Unresolved deterministic invalidity gate; no probability claim | Requires complete successor/remaining-state pool and viability checks; no complete pool was available to prove the invalid result |

The event file's downstream popup events use fixed `ai_chance` values of 100 where present, while the settlement popup has no competing AI chance. Those presentation events therefore do not supply a settlement choice probability. The actual terms helper remains state-dependent and was not accepted as a normalized pool without a complete declared state model.

### Global queue scenarios

| Scenario | Result and evidence classification | Pool and external-factor status |
|---|---|---|
| GLB-01 | Unresolved deterministic queue lifecycle; no probability | Critical-country queue incomplete; requires all critical eligible countries, scan order, queue cursor, caps, and launch locks |
| GLB-02 | Unresolved deterministic exclusion lifecycle; no probability | Requires complete actor/route pool to prove that no valid actor exists |
| GLB-03 | Unresolved deterministic timing lifecycle; no timing distribution | Requires stability band, review timers, pressure/authority state, and all competing queue entries |
| GLB-04 | Unresolved deterministic blocked-cap lifecycle; no probability | Requires live cap usage, queued critical entries, capacity-release transitions, and launch lock state |
| GLB-05 | Unresolved deterministic cleanup lifecycle; no probability | Requires queued entries, annexation state, cleanup cursor, and target identity |
| GLB-06 | Unresolved deterministic grace/admission lifecycle; no probability | Requires complete Event 006 package and human-target pool, grace timer, origin/tag reservations, and bridge state |
| GLB-07 | Source gate observed to exclude actual nonhuman; MCP confirmation unresolved | Requires complete normal-human candidate pool and current nonhuman flags |

### Wars cluster scenarios

| Scenario | Result and evidence classification | Pool and external-factor status |
|---|---|---|
| CLU-01 | Unresolved cluster activation/order result; no member probability | Incomplete Wars member and target pools; requires all active member rows, target identities, chaos tier, trigger multiplicity, cooldown, and reservation state |
| CLU-02 | Unresolved; overlap is a possible source path but not a measured probability | Requires external-war target set, Event 004/021 member eligibility, target reuse policy, and cluster cooldown state |
| CLU-03 | Unresolved deterministic same-transaction reservation gate | Requires active transaction identity, same-tag target, reservation flags, and cluster member state |
| CLU-04 | Unresolved deterministic reroll/skip path | Requires Event 006 reservation owner, member availability, reroll/order candidates, and exact skip reason state |
| CLU-05 | Unresolved deterministic skip-and-continue path | Requires complete live Event 021 target pool and all other active cluster members to prove the continuation order |

### Fracture Cascade scenarios

| Scenario | Result and evidence classification | Pool and external-factor status |
|---|---|---|
| SCN-01 | Unresolved; source share parameter is not a measured scenario probability | Requires all eligible normal-human targets, Political Fracture type, Low intensity gates, route weights, and global/cluster state |
| SCN-02 | Unresolved; source share parameter is not a measured scenario probability | Requires all eligible targets, Independence Cascade type, Medium intensity gates, Event 006 packages, and reservation/cap state |
| SCN-03 | Unresolved; source share parameter is not a measured scenario probability | Requires all eligible targets, Command Collapse type, High intensity gates, major/multi-front capacity, and force pool |
| SCN-04 | Unresolved; source share parameter is not a measured scenario probability | Requires every eligible normal-human target, Maximum intensity, caps, batch cadence, and terminal/commit transitions |
| SCN-05 | Source normal-human exclusion gate observed; engine result unresolved | Requires complete normal-human pool and actual-nonhuman state for every candidate |
| SCN-06 | Unresolved deterministic same-tag route preference | Requires one-state human target, same-tag candidate pool, island/state topology, and takeover validity |
| SCN-07 | Unresolved deterministic batch/timer lifecycle; source exposes a 7-day scenario-batch and launch-lock parameter but no measured stall | Requires complete locked-plan queue, batch transitions, terminal states, recovery, and exact cadence |

The source scenario share constants are Low 0.10, Medium 0.25, High 0.50, and Maximum 1.0. They were recorded as tuning inputs only. They cannot be reported as exact Event 021 selection probabilities because the scenario target pool, eligibility, caps, cooldowns, and external factors are incomplete.

## Skipped analyses and exact reasons

- `hoi4.probability_evaluate` was not run for FRT, SET, GLB, CLU, or SCN because inspection returned no available adapter/candidates and `poolComplete=false`; the missing scenario-effects source also prevents a source-backed scenario model. No complete live candidate pool could be declared without inventing runtime state.
- `hoi4.probability_sweep` was not run because no valid evaluated baseline or complete continuous sensitivity path existed. Any sweep would have varied an incomplete pool.
- `hoi4.probability_compare` was not run because the user supplied no before/after source revision and no source change was authorized. No before revision was invented.
- `hoi4.probability_simulate` was not run because no explicitly declared uncertain-input model, complete pool, seed, or sampling contract existed.
- `hoi4.probability_sequence` was not run because no complete custom manifest with live candidates, cadence, transitions, recovery, cooldowns, removals, resets, and terminal states could be derived without encoding expected outputs as inputs.
- `hoi4.probability_render` was not run because no probability analysis id or scenario hash existed.
- Event structural evidence remains partial and unresolved because the adapter scanned vanilla `game:` files rather than the Event 021 mod source. The exact `PROBABILITY_SOURCE_NOT_FOUND` blocker is the absent `021_random_civil_war_scenario_effects.txt` file; the structural blocker is workspace/source routing that did not produce a Chaos Redux Event 021 graph.
- No additional open-ended MCP calls were made after the user requested a bounded finish.

## Recommended fixes without applying them

1. Restore or intentionally register `common\scripted_effects\021_random_civil_war_scenario_effects.txt`, then expose the scenario dispatcher and its complete target/intensity pool to the probability adapter.
2. Add an analyzer-supported manifest boundary for front-plan candidates, settlement terms, global critical entries, Wars member rows, and Fracture Cascade targets. The manifest must derive eligibility and current weights from live source state and must include reservations, cooldowns, caps, recovery, resets, and terminal transitions.
3. Make the Event 021 structural adapter resolve the mod workspace and `events\021_random_civil_war.txt` instead of falling back to vanilla `game:` files, then rerun `hoi4.event_inspect` and `hoi4.event_render` on `chaosx.nr21.1`.
4. Rerun `probability_evaluate` for every genuinely weighted named scenario, `probability_sweep` for severity/target/cluster sensitivities, and `probability_render` for the resulting rankings and timing views. Use `probability_compare` only after an actual owner-applied source revision exists.
5. Keep deterministic settlement and global queue lifecycle scenarios explicitly separate from normalized selection probabilities; report their exact transition traces or bounded timing only after a complete `probability_sequence` manifest is available.

## Remaining uncertainty

No requested scenario has exact, bounded, sampled, or MCP-certified probability evidence in this audit. SET and GLB are primarily deterministic/score-only lifecycle surfaces in the observed source, but their runtime outcomes remain unresolved without complete state and structural MCP resolution. FRT, CLU, and SCN contain weighted or state-dependent behavior, but their candidate pools and external factors are incomplete. This report is therefore a complete bounded handoff of the available evidence, not a balance certification.
