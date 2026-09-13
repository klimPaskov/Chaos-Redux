# Event 021 Sponsor AI Post-Repair Audit

Date: 2026-09-02.

Repository: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.

Scope: read-only bounded audit of Event 021 sponsor decisions `SPN-01` through `SPN-05`.

Classification: **NON-CERTIFIED / INCOMPLETE**.

The current MCP evidence shows the requested post-repair score relationships, but it does not certify campaign selection behavior or an exact action probability.

## Outcome

The current five-row MCP matrix is:

| Scenario | `event021_support_government` | `event021_support_opposition` | `event021_offer_mediation` | Current interpretation |
|---|---:|---:|---:|---|
| `SPN-01` | `1.6875` | `0` | `0.75` | Government support ranks first in the declared fixture, with mediation second. |
| `SPN-02` | `0` | `0` | `0` | Desperate-war, low-equipment fixture suppresses all three rows. |
| `SPN-03` | `1.6875` | `1.6875` | `0.75` | Both declared support rows remain competitive and tied in raw score. |
| `SPN-04` | `0` | `0` | `1` | Invalid support targets are suppressed while mediation remains eligible in the fixture. |
| `SPN-05` | `0` | `0` | `1.5` | Mediator profile hard-zeros military support and favors mediation. |

These are raw `decision_ai_will_do` scores, not normalized probabilities, because the installed adapter is `score_only` and explicitly reports `normalizedProbability=false`.

The current source has a score/availability coupling defect: the two support decisions have political-power, infantry, and convoy availability gates, but their `ai_will_do` blocks only mirror the viability, mediator, war/surrender, and infantry conditions; they do not mirror the political-power or convoy gates at `common\decisions\021_random_civil_war_decisions.txt:387-401` and `:440-454`.

The MCP inspection confirms the support score inputs are `has_equipment`, `has_war`, `hidden_trigger`, `surrender_progress`, and `var:random_civil_war_exposure_source_country_scope`, with no separate political-power or convoy score input.

This can leave a positive raw willingness trace associated with an unavailable action when resources fail only the missing gates, although the exact campaign incidence is unresolved because the decision adapter does not model the full AI decision-selection loop.

## Audited source truth

| Surface | Source and identifiers | Raw SHA-256 captured at final check |
|---|---|---|
| Sponsor decisions | `common\decisions\021_random_civil_war_decisions.txt`, `event021_support_government` lines 380-431, `event021_support_opposition` lines 433-484, `event021_offer_mediation` lines 486-519 | `3851afb4a8a3f4736b5333b3e8edd4320547f6bd02a671e9042513c023c884f1` |
| Target validity and alignment | `common\scripted_triggers\021_random_civil_war_parent_triggers.txt`, `event021_country_can_manage_exposure` lines 585-604, validity lines 606-634, viability lines 636-698, alignment lines 700-730 | `cb9c12a261de7ce9b0b4ef6d044ff6857651179bb730a93d8e6d9692075b37d5` |
| Constants snapshot used by the current source | `common\script_constants\021_random_civil_war_constants.txt`, `event021_action_cost` lines 444-463 and `event021_ai` lines 559-570 | `b02ae147ce8ce700792c2b9110d0bf34d5c65d1403ba15f685a968d8c1d09ec1` |
| Parent profile assignment and lifecycle context | `common\scripted_effects\021_random_civil_war_parent_effects.txt`, `event021_parent_expose_neighbor` lines 4982-5017 and related sponsor lifecycle helpers | `62db002165dadb00a700cd3c343ecea4cdb9ac81b003fda38a993052604b92e4` |
| External AI strategy context | `common\ai_strategy\021_random_civil_war_ai_strategy.txt`, `event021_neighbor_containment_ai` lines 95-105, `event021_neutral_mediator_ai` lines 107-116, `event021_opportunistic_sponsor_ai` lines 118-129 | `6adbb93b2cd17665c4bd967368f08bc953738d81db7a2069171241f45c309dca` |
| Structural Event 021 root | `events\021_random_civil_war.txt`, root `chaosx.nr21.1` | Covered by the same-revision Event MCP graph; the full parent manifest reports 368 source hashes, including the Event 021 mod event and on-action files. |

The current constants completion handoff is `docs\plans\021_random_civil_war_plans\subagent_handoffs\script_constant_completion_2026-09-02.md`.

That handoff reports 231 previously undefined unique constant keys supplied, zero missing filtered occurrences after the patch, zero missing unique keys, and nine inferred tuning groups awaiting parent review.

The sponsor constants now resolve to government support gates `20` political power, `150` infantry equipment, and `5` convoys; opposition support gates `20`, `150`, and `5`; mediation gates `20` political power, `10` command power, and `5` convoys; `event021_ai.base_action = 1`; `priority_major = 1.5`; `discourage_concession = 0.75`; `exposure_mediator_stability = 0.65`; and `near_defeat_threshold = 0.70`.

The historical constants snapshot recorded in the prior handoff was raw SHA-256 `8fc148a0d41777f2ca44b4f16409ee330ade7d641b6b77f41524a9850c047126`.

The constants snapshot therefore changed from `8fc148a0...` to `b02ae147...` while this post-repair audit was in progress, and the final results must not be treated as a stable source certificate.

The parent-effects source also changed repeatedly during evidence collection, from the initial captured `a84dd5d3ade357b346452c940accc6bf6293ae57fea7a4c90d049289e04cd32e` to `0c79dfe20d99f45504f8beb5f100f05cc9e01a9dd120ecf0e8eefb2c1d10e5fd`, then `da50e9bf9c83c8ce5c16de472e346951b62507ca67cee4c28740de834b92852c`, and finally `62db002165dadb00a700cd3c343ecea4cdb9ac81b003fda38a993052604b92e4`.

The decision and target-trigger hashes remained stable across the final checks, but the concurrent source drift alone is sufficient to block certification under the requested rule.

## Scenario contract and completeness

The declared candidate pool was complete for the bounded decision surface: `event021_support_government`, `event021_support_opposition`, and `event021_offer_mediation`.

The final evaluation scenario set was `event021_sponsor_ai_spn_01_05_postrepair_2026_09_02_final` with scenario hash `07c2af48de65561b2ab83dffa776a1c0ff70f36780b6a6158b96daa609e021d3`.

The final threshold sweep scenario set was `event021_sponsor_ai_spn_01_05_postrepair_2026_09_02_sweep` with scenario hash `08d00630206417d93ffd8dc60285334cb2b4a5d06a1e1fe2e20c2a91316b3155`.

Both sets retained the required names `SPN-01` through `SPN-05` and the matrix meanings from `docs\specs\021_random_civil_war_specs\021_random_civil_war_probability_scenario_matrix.md`.

The fixtures declared profile flags, neighbor exposure, coarse hidden-availability state, equipment state, saved-source-scope state, war state, surrender progress, political power, command power, infantry equipment, convoy stockpile, and invalid-candidate overrides for the scenarios that explicitly describe an absent survival path or rival side.

The saved-scope values were adapter fixture shorthands for `var:random_civil_war_exposure_source_country_scope`; they are not a complete runtime country/host/actor scope graph.

The MCP evaluator left `surrender_progress` unresolved because `surrender_progress > constant:random_civil_war_evolution_mtth.near_defeat_threshold` could not compare the declared scenario value.

The final evaluate and sweep each report two unresolved items, one in each armed-support decision.

No seed, probability distribution, daily cadence, action receipt, cooldown transition, commitment cap, removal, reset, or terminal-state manifest was declared for this bounded sponsor audit.

The external `ai_strategy` factors were not composed into the decision score scenarios.

## MCP evidence

### Decision inspection

The mandatory current `hoi4.probability_inspect` call used adapter `decision_ai_will_do`, the exact decision source path, the three-candidate pool, and current expected source hash.

It returned `PROBABILITY_SOURCE_INSPECTED`, `poolComplete=true`, `candidates=3`, `requiredInputs=5`, `unresolved=0`, source hash `e21827f869368e3758d6409c67319d97ebd9e56694ed767dbdc9796aff845c59`, and source revision `cb934ac6aa085d9f875ad6af562b87c16fde132ebe2908ff74eb0382d5316f6e`.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7066de9b2f41f00cda5cd05e89f6914b54f26986b621091e9be0e9bb918100c9/6d6f7cf94eff5c97215aa9900725592c6f4dc672220a6e9e6d00f845b3a350fb/probability-inspect-e21827f86936.json`.

### Current five-scenario evaluation and render

The current `hoi4.probability_evaluate` call returned `PROBABILITY_ANALYZED_PARTIAL` with analysis id `probability-4e1958dacabd56d2217cd407`, source revision `b0427472f3fff1a5cd1e87c915bebd4613fab1d6571bbeb99c95d783c7c6d7b6`, decision source hash `e21827f869368e3758d6409c67319d97ebd9e56694ed767dbdc9796aff845c59`, scenario hash `07c2af48de65561b2ab83dffa776a1c0ff70f36780b6a6158b96daa609e021d3`, five scenarios, fifteen candidate rows, two unresolved items, and eight rendered resources.

Authoritative JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1146806469718f81c60e2bfd0d1711299f014f07b7e436621e93d8aed518a26a/5b1f9ef8d56cd35d6a1413ea2a63cb6df20d26fc318ee69b0630f2f1c068ba46/probability-4e1958dacabd56d2217cd407.json`.

Rendered ranking for `SPN-01`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2eb8792b2d835cdd300e25962188fa42bb5a4838a0189c2bf15c23b17e84392d/e27d6b7466b44a0ec0153cfd41f7211a745ae764e9b434951a4e14b755b8f427/probability-probability-4e1958dacabd56d2217cd407-ranking.svg`.

Rendered five-row matrix: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/833b55fc1353107167d56f011d9d8e322bbd5a425427eec98e1c024e8ae07e16/4e4894a2cc3c3020c592272eec6d7788b0cfb05de3dd475bb9a638865eacef27/probability-probability-4e1958dacabd56d2217cd407-matrix.svg`.

Rendered modifier waterfall: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dc70c27c59156136434045e0a2b14e0e8ed0aa27c7a1f154bf5efc9738051335/3f77c63c5e919767ef1969b569e314207def715c73324a60cf208c72f954c747/probability-probability-4e1958dacabd56d2217cd407-waterfall.svg`.

Rendered unresolved view: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/107cb06cec462704c6605621a1769dd55dfc3ef1a5cf4b6b942e1ae8c6dcc0fe/0fdee13f0e7de194776d819fd9cb30df56734d4f3fa9cb359698906d3374a3ac/probability-probability-4e1958dacabd56d2217cd407-unresolved.svg`.

The `SPN-01` ranking render shows government support `1.68750`, mediation `0.750000`, and opposition support `0.00000`.

The current government-support trace is base `1`, opportunistic profile factor `1.5`, government-alignment factor `1.5`, and opposition-alignment reduction `0.75`, yielding `1.6875` while retaining the unresolved surrender-progress branch.

The current `SPN-05` single-scenario trace records mediation `1.5` and a `random_civil_war_value.zero` factor applied to each support decision when `random_civil_war_mediator_profile` is true.

### Current sensitivity sweep

The current `hoi4.probability_sweep` varied the declared uncertain input `surrender_progress` over `[0,1]` with five steps, one path, pairwise interactions disabled, and rank-reversal detection enabled.

It returned `PROBABILITY_ANALYZED_PARTIAL` with analysis id `probability-20e8cdb8edda7573d6e4a9ae`, source revision `177e732e26163e1c57e5bb398eb35a1207e48324602aa8bb7aed834b82ffb7cc`, scenario hash `08d00630206417d93ffd8dc60285334cb2b4a5d06a1e1fe2e20c2a91316b3155`, twenty-five sweep points, and two unresolved items.

Sensitivity render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fc2f7db2f3ce493c98044c5dde029981570521145b7bebe4564b957e6e03779f/cbc0b396fdd8ab898a0d35b9177af371ffd56b1537edfd109049aa300dbd8ed7/probability-probability-20e8cdb8edda7573d6e4a9ae-sensitivity.svg`.

Threshold render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a6d32ffc270e06218fbe6e53b5f3d111d3f383d152a2e17fa057722f7cf35cc8/c1952ed344271b7493c0ce423f8b55d8a42cb419bf1a9f6fb1cc0a08fa6507db/probability-probability-20e8cdb8edda7573d6e4a9ae-threshold.svg`.

The threshold render reports `0 rank reversals and 0 threshold observations`, but this is a partial score sweep with an unresolved trigger comparison and cannot certify rank stability.

### Strategy-factor inspection

The required `hoi4.probability_inspect` call on `common\ai_strategy\021_random_civil_war_ai_strategy.txt` used adapter `ai_strategy_factor` and returned `PROBABILITY_SOURCE_DISCOVERED` with discovery reason `no_weighted_surfaces`, zero candidates, zero required inputs, source revision `d27af1d9d6db77204dcbaf9f95d29456bc02c069d5dc36bfcf547403a4c70aea`, and source hash `74d73084d977d42abe822021d859cb7b7a075aa89565a9c9dd861c9261b37db9`.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/82e670e8af2e4f6a5f3ce558dde9d98e777145a7a9097c1955b5227366b40262/044056cb8048c911e6e2883eecbb21c8defeb8a7c6b21882fff6c693082e1133/probability-inspect-74d73084d977.json`.

No strategy-factor evaluate was issued because the installed adapter found no weighted surface in this source, and the decision adapter does not compose these strategy blocks into the sponsor score.

### Structural Event MCP

The bounded `hoi4.event_inspect` trace for selector `{kind:event,eventId:chaosx.nr21.1}` returned `EVENT_INSPECTED_PARTIAL`, revision `23d07f38466bd55877a4f79f36a99c34bb9b7f0790f582a264bb307cc60e4646`, graph hash `38c248ff95d2c1efe04ff3c5a340f4af0f65f201989d8a235d0aec2d3c68519f`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cb52d334ec0ae0236f7ac2464c290f0835d6a1dbfcb6ed723f73225b4e8618ad/a09381e7d92002cacbf6107892000b37d8290323f3989cfdb4c881410b8e63f6/event-trace-23d07f38466b.json`.

The structural result contained 9,725 events, 15,153 options, 8,688 unresolved nodes, 2,205 issues, and no blocking diagnostics in the compact response.

The bounded `hoi4.event_render` unresolved view returned `EVENT_RENDERED_PARTIAL` with the same graph revision and unresolved render `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0075032ea3e772678eb24043af56871211c7c0b6a4cb1b94f15d78471e90439f/e8344168263a5c9db2eeb362d1eed21a73c45d2faaf7266dd0f177be7c7bc973/event-unresolved-23d07f38466b.svg`.

The compact `filesScanned` field was truncated by `MCP_INLINE_FILES_TRUNCATED` and therefore was not a complete source inventory.

The same-revision parent manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/909f0e9c8fb99fb70f04ec8d4c2aa2aa30e4261e3fe37f69a441b9b872dcc2f9/044b9532f9aa9bcc64c1eaaa36af1adba12cbd37fe1d3aeb46331770861defc8/event-options-23d07f38466b-manifest.json` confirms `sourceHashCount=368`, includes `mod:common/on_actions/021_random_civil_war_cxt_on_actions.txt` and `mod:events/021_random_civil_war.txt`, and selects `event:chaosx.nr21.3`, its option node, and its terminal node.

The parent manifest has `complete=false`, but its selected view reports no omitted nodes and no truncation; the existing helper-deferred validation remains false and the graph-wide unresolved/helper boundary remains a structural limitation.

## Historical before/after evidence and baseline availability

The prior parent diagnostic recorded the following pre-repair sponsor scores:

| Scenario | Prior government support | Prior opposition support | Prior mediation |
|---|---:|---:|---:|
| `SPN-01` | `1.5`, eligible, rank 1 | `0`, ineligible | `0.75`, eligible, rank 2 |
| `SPN-02` | `0`, ineligible | `0`, ineligible | `0`, ineligible |
| `SPN-03` | `1.5`, eligible, rank 1 | `1.5`, eligible, rank 2 | `0.75`, eligible, rank 3 |
| `SPN-04` | `0`, ineligible | `0`, ineligible | `1`, eligible, rank 1 |
| `SPN-05` | `0.75`, eligible, rank 2 | `0.75`, eligible, rank 3 | `1.5`, eligible, rank 1 |

The prior evidence is `ai_probability_spn_parent_diagnostic_2026-09-01.md`, analysis `probability-b5163d0f1c04bd490bff6dcc`, and scenario hash `315c23693b64d7443f02aab3ce3b439c1742d941ff59b2dd30f5ff4148108435`.

Its artifact was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aa33ec717bf707f57688d565e00fa118951e6d82cbded06efa8afa8b1614b102/3b70efca158195ff62b13d0d9f11ca20f119c3154702d7e758e0c8f5260f9752/probability-b5163d0f1c04bd490bff6dcc.json`.

Reading that artifact during this audit returned the exact error `Mcp error: -32603: Artifact provenance manifest is unavailable`.

The prior inspection artifact similarly returned `Mcp error: -32603: Artifact provenance manifest is unavailable` when read.

The prior handoff preserves a source revision `21666e64d1d772ede92e2b9b8595ce770ca7b5049cb21468d3aa2ae2ee5bd2c7` and an inspection artifact named `probability-inspect-b012bf7ee578.json`, but it does not preserve a complete before-source body that can be supplied to `hoi4.probability_compare`.

The prior source snapshot for constants is available only as raw file hash `8fc148a0...`; the current constants snapshot is raw file hash `b02ae147...` and is named above.

Therefore the table in this section is truthful historical before/after evidence, not a new MCP comparison.

`hoi4.probability_compare` was not called with a fabricated before selector because a source revision, artifact name, or canonical source hash without a readable old source body is not a valid before source for this adapter.

No comparison id, comparison artifact, or exact before/after attribution claim exists.

## Findings by audit dimension

### Validity and target gates

`SPN-04` support is suppressed by the declared invalid-candidate overrides and the source viability/validity contract, while mediation remains eligible in the bounded fixture.

`SPN-02` support and mediation end at zero under the low-resource and desperate-war fixture, but the surrender-progress comparison remains unresolved.

`SPN-01` and `SPN-03` are not fully target-scope proven because the evaluator's coarse saved-scope representation does not faithfully bind the nested host and actor scopes used by the source helpers.

### Dominance and starvation

Mediation dominates both military-support rows in the current `SPN-05` score trace because the mediator hard-zero is applied to both support decisions and mediation receives `priority_major = 1.5`.

The `SPN-03` support tie is a raw-score tie and does not mean equal action probability or equal campaign prevalence.

No starvation conclusion is available for the live action pool because the decision adapter has no normalized denominator and no sequence model.

### Rank reversal and sensitivity

The bounded surrender-progress sweep produced 25 evaluated points and reported zero observed rank reversals, but two unresolved armed-support trigger comparisons remain across the sweep.

This is a bounded partial result rather than a certified threshold or rank-reversal proof.

### Repetition, commitment, and snowball risk

The source declares a 30-day action cooldown, a 90-day sponsor commitment, and a support amount of 100 in `event021_action_tuning`, but these transitions are outside the decision score adapter.

No `probability_sequence` manifest was declared, so repetition, receipt recovery, cap enforcement, removal, reset, and terminal-state behavior remain unresolved in this audit.

### Current source bug and exploit risk

The missing AI mirrors for political-power and convoy availability are the current sponsor-score bug requiring owner review.

The mediator hard-zero is a direct safety improvement for `SPN-05`, but the target-scope binding limitation prevents certifying that the intended aligned-side bonus and rival-side reduction apply to exactly one physical target.

The nine inferred tuning groups in the constants completion handoff remain parent-review items rather than undefined-key defects.

## Recommendations without applying fixes

1. In `common\decisions\021_random_civil_war_decisions.txt`, add score-side resource suppression for the political-power and convoy gates of `event021_support_government` and `event021_support_opposition`, and decide whether `event021_offer_mediation` also needs score-side resource factors.

2. Re-run the same five scenario ids after the owner applies any score/availability correction, using a genuine saved-scope fixture for `var:random_civil_war_exposure_source_country_scope`, the host scope, and the opposition actor scope.

3. Preserve a complete pre-patch decision source snapshot or a readable MCP artifact before the next patch so `hoi4.probability_compare` can attribute the same-scenario change without inference.

4. Parent-review the nine inferred constant tuning groups before treating the current numeric gates, commitment duration, and support amount as balance-approved.

## Future broader-audit blocker only

The constants handoff identifies a separate target-pool quantization issue that is outside `SPN-01` through `SPN-05` and was not analyzed here.

The target conversion uses `target_pool_weight_scale = 100`, `target_pool_weight_cap = 10`, and a lower clamp of one ticket after rounding, so a normal target score of `90` and a major target score near `31.5` can both become one ticket after their reduced major weighting and the `1..10` clamp.

This can erase intended reduced-weight distinctions in the broader target pool and must be handled by a future target-selection audit with its complete candidate pool.

No target-pool probability, rank, or balance conclusion is claimed in this sponsor handoff.

## Skipped analyses, errors, and blockers

`hoi4.probability_compare` was skipped because no genuine readable before-source snapshot exists; no baseline was fabricated.

`hoi4.probability_simulate` was skipped because no uncertain probability distribution or seed-based selection question was declared.

`hoi4.probability_sequence` was skipped because no complete custom pool manifest declared cadence, recovery, caps, cooldowns, removals, resets, and terminal states.

Timing metrics were skipped because `decision_ai_will_do` reports `timeDistribution=false` and the decision surface is a score race rather than MTTH timing.

The AI-strategy evaluate pass was skipped after the required inspection returned `no_weighted_surfaces` and zero candidates.

Structural Event MCP coverage is partial because helper projections were deferred and validation remained false, not because the mod event file was absent.

An initial strategy inspection with an uppercase expected hash returned the exact schema error `MCP error -32602: Input validation error: Invalid arguments for tool hoi4.probability_inspect: Invalid string: must match pattern /^[a-f0-9]{64}$/u at source.expectedSourceHash`; the corrected lowercase call succeeded.

An initial render retry included the unsupported `refresh` field and returned `MCP error -32602: Input validation error: Invalid arguments for tool hoi4.probability_render: Unrecognized key: \"refresh\"`; the corrected same-process render succeeded without that field.

The source changed during analysis as recorded above, so this handoff intentionally does not certify the current source as stable.

No gameplay, AI, decision, trigger, effect, constants, manifest, configuration, localisation, or runtime file was edited by this audit, and no commit was made.
