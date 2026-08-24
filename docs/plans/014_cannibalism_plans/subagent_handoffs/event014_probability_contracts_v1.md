# Event 014 probability contracts v1

## Outcome

This tranche adds five machine-readable, source-linked analyzer contracts and this handoff. No gameplay source, weights, costs, thresholds, route gates, timers, player behavior, or AI balance values were changed.

The contracts expose deterministic selectors, conditional random pools, raw score surfaces, queue cadence and cleanup, MTTH declarations, mission-to-decision adapters, and the four AI strategy profiles without converting deterministic choices or scores into campaign probabilities.

## Completed contracts

| Contract | File | Coverage |
| --- | --- | --- |
| Contract index | [event014_contract_index.json](../probability_contracts/event014_contract_index.json) | Source snapshots, classification legend, MCP receipts, true-probability receipts, and non-claims. |
| Deterministic selectors | [event014_selector_contracts.json](../probability_contracts/event014_selector_contracts.json) | First host, highest-risk state, warlord origin state/branch/region, convergence host, Wendigo merge host/anchor, and conditional random/score surfaces. |
| Spread sequence | [event014_spread_sequence_contract.json](../probability_contracts/event014_spread_sequence_contract.json) | Eight route contracts, nine aligned queue arrays, status lifecycle, cadence, generation guard, arrivals, invalidation, reconciliation, compaction, and a synthetic sequence probe. |
| MTTH and mission adapter | [event014_mtth_mission_contracts.json](../probability_contracts/event014_mtth_mission_contracts.json) | Evolution I/II timing contracts, Evolution III convergence scheduling, unified/Wendigo target scores, and all fourteen mission lifecycle adapters. |
| AI strategy profiles | [event014_ai_strategy_profiles.json](../probability_contracts/event014_ai_strategy_profiles.json) | Common, island, siege, and march fixed strategy intensities and deterministic enable flags. |

## Classification and exact source contracts

True probabilities are limited to source random pools: capture cooperation is 85/15, each selected regional warlord name is 1/4, and warlord personality is 1/6. These are conditional on their source helper or option gate and do not imply event reach, region frequency, warlord frequency, or campaign frequency.

Raw scores include Event 014 `ai_chance`, decision `ai_will_do`, MTTH modifiers and target scores, and AI strategy intensities. The manifests retain raw values and source constants; normalized score rows are explicitly marked as conditional score normalization rather than frequency.

Deterministic selectors include `cannibalism_select_first_host`, `cannibalism_select_highest_risk_state`, `cannibalism_select_warlord_candidate_state`, origin and region precedence in `cannibalism_prepare_warlord_creation_context`, `cannibalism_select_unification_host`, `cannibalism_select_wendigo_merge_host`, and `cannibalism_select_next_initial_wendigo_anchor`. The contracts preserve eligibility, score components, array order, strict-greater replacement, human-first passes, lower-country-id ties, outputs, and side effects.

The spread contract preserves the eight source route values and their deterministic delay/strength parameters: retreat 24/34, prisoner transfer 32/45, convoy 38/40, volunteer return 28/32, occupation turnover 20/48, deliberate seed 30/55, conquest 14/60, and survivor 35/28. It declares no route weight.

The queue contract preserves the nine aligned global arrays, status values queued/in-transit/arrived/contained/invalidated, due date as global date plus route delay, source generation identity, targeted arrival events `chaosx.nr14.60`, `.61`, and `.62`, and terminal-row compaction.

The cadence contract records first pulse 7 days, baseline pulse 14 days, ritual pulse 10 days, network/convergence pulse 7 days, automatic route cooldown 45 days, and foreign-seed re-enable 90 days. These are deterministic scheduler values, not MTTH frequencies.

The cleanup contract records country and state invalidation, target-cache reconciliation, pending-ledger rebuilds, generation checks, warning cleanup, and global target lifecycle. It preserves the existing global unification and Wendigo target clear-before-select behavior and identifies regular spread targets separately from persistent global targets.

The current MTTH contract contains only the Evolution I and II timing entries. `cannibalism_try_schedule_evolution_iii` uses convergence gates, warning timing, and hard timing constants, so Evolution III is represented as a deterministic convergence scheduler rather than an MTTH runtime probability.

The mission map covers compact vigilance, restore supply corridor, rotate compromised formations, investigation, hold prison, reach island, break network, stop unification, stop transformation, unified command, unified larder, unified war machine, unified counterwar, and Wendigo terminal hunt. Each row records timeout, activation flag, starter, decision or operation adapter IDs, objective, recorder where present, persistent targets where present, and cleanup outcomes. `cannibalism_hold_prison_mission` is explicitly a pulse auto-start with no decision adapter.

The four strategy profiles retain literal fixed intensities and enable flags. Common values are build army 220, infantry equipment 180, support 160, infantry template priority 220, and infantry role ratio 180. Island values are convoy ratio 35, one minimum convoy factory, screen ratio 20, and naval base 120. Siege values are artillery 190, bunker 170, and arms factory 120. March values are motorized 190, infrastructure 160, and spare units 130. None is reported as a probability.

## Helper architecture map

| Existing helper family | Scope and inputs | Outputs and side effects | Source callsite contract |
| --- | --- | --- | --- |
| Host/state selectors | Global country or selected-host state enumeration, with scripted eligibility and score inputs. | Event targets and temporary arrays; clear temporary arrays after selection. | Host initialization and origin setup call the selectors; analyzer must preserve array order and score races. |
| Warlord origin context | Selected origin state plus origin eligibility flags. | Former owner/controller targets, origin and region flags, starting-unit/experience/frenzy variables. | Warlord creation consumes the context; origin branch and region are deterministic precedence. |
| Convergence/Wendigo selectors | Actor registry or controlled-state arrays, generation and viability gates. | Global host/anchor targets, generation, anchor arrays, and live-anchor caps. | Convergence and transformation setup call the selectors; targets require retirement cleanup. |
| Spread route/queue helpers | Country scope with route value and source/target country/state targets. | Temporary route parameters, nine queue arrays, counters, warning/seed flags, and arrival event. | Action and on-action producers enqueue rows; pulse processing loads context, checks generation, resolves due rows, and compacts terminal rows. |
| Mission lifecycle helpers | Country scope with mission activation and objective state. | Mission flags, timeout variables, operation receipts, target changes, and three-way cleanup. | Decisions start or record operations; pulse/objective processing updates and resolves mission rows. |
| MTTH target score helpers | Targeted decision actor and candidate country/state. | Raw target score used by decision AI willingness. | Unified and Wendigo target decisions consume the scores; invalid target factors remain explicit. |
| AI strategy profile blocks | Warlord country plus origin profile flags. | Fixed strategy factors and self-removing abort when disabled. | Common profile always applies to eligible warlords; one deterministic origin profile is enabled by origin flags. |

No new helper was needed for analyzer visibility. The existing helper map is documented rather than duplicated in scripted effects.

## Constants, tuning, and migration plan

The manifests reference existing `cannibalism_host_threshold`, `cannibalism_host_weight`, `cannibalism_state_weight`, `cannibalism_warlord_creation`, `cannibalism_unification`, `cannibalism_wendigo_merge`, `cannibalism_wendigo_anchor`, `cannibalism_spread`, `cannibalism_timing`, `cannibalism_target_score`, `cannibalism_evolution_mtth`, and `cannibalism_ai_strategy` categories. No constants were added or changed.

The AI file's file-scoped `@CR_SC_CANNIBALISM_AI_STRATEGY_*` literals remain documented as parser-compatible mirrors of the shared strategy constants. No dynamic-value workaround or gameplay helper hook was introduced.

The migration path is manifest-only: future analyzer work reads contract IDs and supplies explicit scenario state, candidate identities, adapter-supported transitions, target scopes, cooldowns, caps, resets, and terminal actions. No source migration is required, and no source helper should be added solely to make an unsupported analyzer adapter appear complete.

## MCP evidence and blockers

The mandatory first weighted inspection was `hoi4.probability_inspect` with the `custom_weighted_pool` adapter against the Event 014 effects source. It returned `PROBABILITY_SOURCE_INSPECTED`, `poolComplete=false`, zero candidates, zero required inputs, and zero unresolved entries. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f7113f1b2aeb4c5e416d97f989fabed2142635f729244733f8e5da5644bb5c9d/a678dd5aa1c2bcfb5be56ea0becf5f2b5471fb39d30627635c017a0591eb18c5/probability-inspect-a2195480e458.json`.

The event source inspection returned `PROBABILITY_SOURCE_INSPECTED` with 40 candidates, 15 required inputs, one unresolved item, and an incomplete pool. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/94dbb6bbb8dee923067152aa438c66f1508aa1905b44eb3afaef593f606a6e95/8ed959a260547246b46b9749e3680445c524a5be0ba68fac2b4d7600aa138e38/probability-inspect-607776243870.json`.

The random-list inspection returned `PROBABILITY_SOURCE_INSPECTED` with 42 candidates, five required inputs, one unresolved item, and an incomplete pool. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dbcd8a0defbf22e21ed5760a21c3499841f311765e98af9c02aa78e85a6f519c/ab9e2c43f71a36e7284ae4e3a5412b9c02856c581fe227313846dd28bb4e3d3d/probability-inspect-a2195480e458.json`.

The decision inspection returned `PROBABILITY_SOURCE_INSPECTED` with 95 candidates, 32 required inputs, zero unresolved items, and an incomplete pool. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cc29dd5799af8e3871aba086353b4ade20c10bfc172915352d11cbcda03e5652/574b534bf02f4fb134835d619bc1ed51ecdc81fca8621e562f18e3f2d59220bb/probability-inspect-f0e56bfe94bb.json`.

The requested `mission_ai_will_do` inspection discovered no candidates and suggested `decision_ai_will_do` instead because the requested adapter was empty. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/884a3936fe58851b7ab983f77c53881241b88f735487f38058ff7a839457e63b/938f2a706ad596ecf778eb3508c9c253def1e0df6ae32f0ea46c942874fac6ed/probability-inspect-f0e56bfe94bb.json`.

The baseline MTTH inspection returned `PROBABILITY_SOURCE_DISCOVERED` with no weighted surfaces. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ed92883c79b0b9849d1052ad073589de9e5a1e81ece26b6e413fa7669967cc90/7273d43ba19227cf546aa9c01b9805f99fdd437d6f629813faaced0e388d155d/probability-inspect-a1950692f970.json`. The post-cleanup inspection is recorded in the bounded handoff for this tranche.

The AI strategy inspection returned `PROBABILITY_SOURCE_DISCOVERED` with no weighted surfaces. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0f9b360bd13cf61f9ac0fdd41f53b0d1352df14146a09f19f664e35d7385f158/627558277a60af17dbafc95a9223c4458d2ae65e8ac127f9f677dd998db93cec/probability-inspect-02bd4b54a3b6.json`.

The installed `hoi4_probability_sequence` tool accepted an exact one-candidate manifest-only queue probe with 100 samples, one candidate, zero unresolved transitions, zero diagnostics, and `analysisStatus=complete`. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/86df5076a6cb23b9ae20e9c945fcd230f1d0492c51bd69e3d14060b86f151f2a/3bcf87893dde2bad849c7eebcd9717bfeb0dc693443014eee7d9e215b3a0ce36/probability-959793529f480f0842ef5cd5.json`. Sequence artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/087b0325aaa04d9778f092a41f5f827bbd5e5f59e455e5c822f395e472e4dfbd/6e20d65560f5aa333e3b49352073599cf394d3ee8b8d4deda04128aac38bbdbe/probability-probability-959793529f480f0842ef5cd5-sequence.svg`.

That sequence result proves only that the installed adapter can analyze the declared one-candidate manifest shape. It does not execute Event 014 effects, event targets, route producers, generation checks, or transitions. A prior two-candidate transition test returned `SEQUENCE_TRANSITION_UNRESOLVED`; the manifests retain this as an adapter blocker.

No callable `chaosx_ai_probability_auditor` route was exposed in this runtime, so no auditor result or unsupported `probability_compare` success is claimed. Direct read-only HOI4 probability inspections and the supported manifest-only sequence probe are recorded instead.

Remaining true adapter blockers are the incomplete effects/custom-pool adapter, incomplete event adapter, incomplete decision adapter, empty mission adapter, no MTTH weighted surface, no AI strategy weighted surface, unsupported Clausewitz loops/every-scope traversal, unsupported event-target persistence and dynamic effect side effects, and unresolved source-like sequence transition identities. These blockers prevent source-executed candidate pools or campaign-frequency claims.

## Validation

All five JSON manifests parse with PowerShell `ConvertFrom-Json`. The manifests were checked against the current local source hashes after concurrent edits, with symbol names retained as the authoritative references where line ranges can move. The probability inspection and sequence calls above were run read-only. Hearts of Iron IV was not launched.

## Changed files and gameplay status

Changed files are [event014_contract_index.json](../probability_contracts/event014_contract_index.json), [event014_selector_contracts.json](../probability_contracts/event014_selector_contracts.json), [event014_spread_sequence_contract.json](../probability_contracts/event014_spread_sequence_contract.json), [event014_mtth_mission_contracts.json](../probability_contracts/event014_mtth_mission_contracts.json), [event014_ai_strategy_profiles.json](../probability_contracts/event014_ai_strategy_profiles.json), and this handoff.

No gameplay logic changed. No helper, constant, manifest hook, scripted effect, scripted trigger, decision, mission, event, on-action, or AI profile source was edited by this tranche.

## Simplifications, omissions, and follow-up

No gameplay simplification or balance change was made. The only limitation is analyzer capability: source-linked rows remain declarative where the installed adapter cannot evaluate the underlying Clausewitz scopes and effects. Future work should add only adapter-supported scenario/custom-pool inputs or improve the analyzer contract; it should not infer route frequencies, replace score races with random draws, or add gameplay helpers for tooling visibility alone.
