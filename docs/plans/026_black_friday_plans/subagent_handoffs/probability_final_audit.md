# Event 026 Black Friday: final weighted-logic audit handoff

Audit date: 2026-09-02.

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

Game receipt: Operation Postern 1.19.2.0, checksum `d245`, probability adapter `hoi4-1.19.2.v1`.

Final status: **INCOMPLETE / UNRESOLVED**.

The MCP pass proves the one informational event option only, while the actual Event 26 launch selector and the sale-discounted action pool remain incomplete to the probability adapter.

No gameplay, AI, event, cost, source, localisation, or runtime file was edited by this audit.

The only file written is this handoff.

## Evidence classification

`Exact` means the declared candidate pool and direct values were resolved by MCP for the named scenario fixture.

`Bounded` means the source or MCP evidence supports a limited gate, ordering, or state-transition observation but not a campaign probability.

`Score-only` means an AI willingness or factor value without a click or selection probability.

`MCP partial` means the adapter returned evidence but withheld a required pool, state, helper, or external factor.

`Compare-blocked` means no real before/after pair exists for the same scenarios and complete pool.

`Live-blocked` means no live HOI4 result was obtained; the user explicitly prohibited launching HOI4.

An empty MCP scenario state is not a populated campaign fixture.

## Specifications, source, and reference material reviewed

- `AGENTS.md`.
- `.agents/skills/chaos-redux-subagents/SKILL.md`.
- `.agents/skills/chaos-redux-events/SKILL.md`.
- `.agents/skills/chaos-redux-mtth/SKILL.md`.
- `.agents/skills/chaos-redux-event-planning/SKILL.md`.
- `docs/specs/026_black_friday_specs/026_black_friday_spec_part_5_ai_multiplayer_balance_and_exploit_controls.md`.
- `docs/specs/026_black_friday_specs/026_black_friday_spec_part_8_acceptance_scenarios.md`.
- `docs/plans/026_black_friday_plans/subagent_handoffs/probability_baseline.md`.
- `docs/plans/026_black_friday_plans/event26_part8_acceptance.md`.
- `docs/plans/026_black_friday_plans/event26_cost_surface_registry.md`.
- `events/026_black_friday.txt`.
- `common/scripted_effects/026_black_friday_effects.txt`.
- `common/scripted_triggers/026_black_friday_triggers.txt`.
- `common/script_constants/026_black_friday_constants.txt`.
- `common/ideas/026_black_friday_ideas.txt`.
- `common/dynamic_modifiers/026_black_friday_dynamic_modifiers.txt`.
- `common/scripted_effects/chaosx_logic_effects.txt`.
- `common/scripted_effects/chaosx_settings_effects.txt`.
- `common/scripted_triggers/chaosx_settings_triggers.txt`.
- `common/scripted_effects/chaosx_events_log_effects.txt`.
- `common/on_actions/chaosx_on_actions_system.txt`.
- `common/on_actions/chaosx_on_actions_chaos_meter.txt`.
- The required offline wiki pages in `paradox_wiki/`: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.
- The relevant vanilla documentation in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`: `script_concept_documentation.md`, `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, and `dynamic_variables_documentation.md`.

## Audited surfaces and source observations

| Surface | Source identifier | Result |
| --- | --- | --- |
| Canonical Event 26 entry | `events/026_black_friday.txt::chaosx.nr26.1` | One hidden, triggered-only dispatcher calls `black_friday_entry_event`. |
| Informational report option | `events/026_black_friday.txt::chaosx.nr26.2::chaosx.nr26.2.a` | One unconditional `ai_chance = { base = 100 }` option; no `ai_will_do`, MTTH, or random-list option race. |
| Automatic event selection | `common/scripted_effects/chaosx_settings_effects.txt::select_weighted_random_event_id`, `evaluate_random_event_selection_candidate` | A hand-rolled proportional picker reads the dynamic `global.all_events` pool and event weights. MCP did not enumerate this pool. |
| Event 26 registration and validity | `common/scripted_effects/chaosx_logic_effects.txt::initialize_all_events_array`, `initialize_event_chaos_level_registry`, `evaluate_random_event_active_pool_candidate`, `evaluate_event_pool_candidate_unavailability` | Event 26 is registered once in `global.fire_once_events`; reserved and active states are rejected before `get_event_weight`. |
| Sale activation and reservation | `common/scripted_effects/026_black_friday_effects.txt::black_friday_reserve_event`, `black_friday_activate_sale`, `black_friday_cancel_reservation`, `black_friday_expire_sale` | Source contains the sale state machine and native modifier refresh, but no MCP-readable action-selection pool. |
| Native sale factors | `common/ideas/026_black_friday_ideas.txt`, `common/dynamic_modifiers/026_black_friday_dynamic_modifiers.txt` | Baseline native cost factor is `-0.5`; Evolution I is `-0.75`; these are cost modifiers, not AI willingness scores. |
| Custom action costs | `docs/plans/026_black_friday_plans/event26_cost_surface_registry.md` | Registry records 2,224 custom cost-trigger occurrences and 2,225 custom cost-text references across 81 files, but owner quote/payment/receipt/refund and AI-pool integration remain incomplete outside the bounded adapters. |

No Event 26-owned MTTH, decision `ai_will_do`, mission `ai_will_do`, focus AI, research AI, doctrine AI, or AI-strategy factor was found.

## MCP probability evidence

### Current 2026-09-02 rerun

The current probability receipts supersede the older source revisions documented below while preserving them as provenance.

The refreshed `hoi4.probability_inspect` for `event_option_ai_chance` used `events/026_black_friday.txt` with candidate `chaosx.nr26.2.a` and returned `PROBABILITY_SOURCE_INSPECTED`. Its current source revision is `6f0ec42cb4c7f21d4ac7ef140322cd7e465b694e2e35ed39c9a7644d4359d8b8`, its source hash is `135da139b2368e30cf374cdcb389692bc649162f9bf7409dab57350a090b0995`, the pool is complete, and one candidate with zero unresolved inputs was found. The current artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9e1f06c515bcb20f1c94f931c82d727444d3d5bc8b8ee28344a887058e04bdef/aac32c18a1f5c0c2bef36ada306b8df4c9afc812d83a6bd594387c95cb47c323/probability-inspect-135da139b236.json`.

The refreshed eight-scenario `hoi4.probability_evaluate` returned `PROBABILITY_ANALYZED` with analysis ID `probability-6110e53d12bcbb99c317b797`, current source revision `6f0ec42cb4c7f21d4ac7ef140322cd7e465b694e2e35ed39c9a7644d4359d8b8`, scenario hash `50c2954c09f14ee6ed9a70ff368173fc40bbe08fab3a38e35fbd3cbd44691fd5`, eight candidate-state rows, zero unresolved rows, and nine diagnostics. Each row is the one-option acknowledgement candidate at raw value 100 and conditional probability 1.0; the dominance diagnostics are expected from that intentionally one-candidate fixture and do not prove sale-action AI. The JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fdd7c67153b0f2ec7744c437d59d2025b47afb2a621c802c5ead4e9c33f14b7e/bfea3faeb44b38b9f53ad1a5b346dc5e0a04ffcc18f8ff9764371956dae2cf7e/probability-6110e53d12bcbb99c317b797.json`.

The refreshed `hoi4.probability_render` for that analysis completed with current ranking, matrix, and unresolved visual outputs. Its JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/09e2dc84fab435d0405da7096ea8a8482d931b4cb075ae6bf9ce9c990da74eec/800f1d411bb9aa95120e8c848d5a4162d416e3bca0459597c4138511b86e8419/probability-6110e53d12bcbb99c317b797.json`; the rendered ranking, matrix, and unresolved resources are siblings in that refreshed render result. This is current visual evidence for the acknowledgement option only.

The refreshed `custom_weighted_pool` inspection against `common/scripted_effects/chaosx_settings_effects.txt` returned `PROBABILITY_SOURCE_INSPECTED` with `poolComplete=false`, zero candidates, and zero unresolved inputs. The current artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8115a6c95dfa9b2c379238d77f8cb506b0ad090e010a2f3f4d1c2b36fa98d45e/e11068069d34adc2365167ef17397956a408bbd62a53c78264439dd30ba097d6/probability-inspect-772e1fb27b48.json`; source revision is `96e2d82275102ae730d215285361cc6e80e647ab94b1818fa2a5bd7f049a06c2`. No normalized launch or sale-action probability is claimed because the owner/action pool is not declared to the adapter.

### Historical receipts retained for provenance

### Required inspections

The fresh final `hoi4.probability_inspect` for `event_option_ai_chance` used `events/026_black_friday.txt` and returned `PROBABILITY_SOURCE_INSPECTED`.

Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/47771d1e784b3d8ab4f06eb8197e2e613c72a7a31a518d43a5019114287759da/5b3079d7b0fc71ac276b15bc9a44d245327d50dcb82fd3f116c8a44e271e78b6/probability-inspect-135da139b236.json`.

Its source revision is `84a5c31c9a71dcbd5212929d9b7fa456408c7b556167cb2709d056e999f016e2`, its source hash is `135da139b2368e30cf374cdcb389692bc649162f9bf7409dab57350a090b0995`, the pool is complete, one candidate was found, zero required inputs were reported, and zero unresolved inputs were reported.

The candidate is `chaosx.nr26.2.a`.

The fresh final `hoi4.probability_inspect` for `custom_weighted_pool` against `common/scripted_effects/chaosx_settings_effects.txt` returned `PROBABILITY_SOURCE_INSPECTED`, but the pool is incomplete with zero candidates.

Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fd8ddd5ac4d9069d06398901cd213392f68534a016aae837916cf0384f7f34e9/241303a4a48679a3b061ceaf4d384ba7a327eaa97bcbb94575c00c94176ab980/probability-inspect-5711a4fe83d6.json`.

Its source revision is `84a5c31c9a71dcbd5212929d9b7fa456408c7b556167cb2709d056e999f016e2`, its source hash is `5711a4fe83d6c0928dcf7aa14cea95ae6435aeec39493130dc03850916febea9`, and no available candidate or normalized pool was exposed.

The corresponding `custom_weighted_pool` inspection against `common/scripted_effects/chaosx_logic_effects.txt` returned an incomplete zero-candidate discovery rather than a runtime candidate pool.

Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0f85c536e6f0d5874581d7230658f3f4551ced00de7ec5f380a3f537af3a8582/6f0333a9c867bc4e31be25b456e23bc9c1772894dd9066cdb4fc40fda13b1e46/probability-inspect-79b93383cfb2.json`.

Its source hash is `79b93383cfb294b9f9767213c41685b513b342b183b6612985287e17acd91fc2`.

Earlier mandatory inspection and discovery receipts were also obtained before the shared source changed, including source revision `c39ab08a68b3a2ed0e3a24e4295645b9b484f37128571d3afedf24c19bc5b9e4` and the artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5aadf86f013a4b803d9b8a85b10f6e4744390e00276996905e002ed7bb882878/6de8a594a7eccbf7a14e74d5228ad7b92fdea82408f401792391db7a517be56c/probability-inspect-3b514b589d57.json`.

Those earlier receipts are retained as provenance only and are not silently combined with the later source revisions.

### Named scenario evaluation

`hoi4.probability_evaluate` used adapter `event_option_ai_chance`, candidate pool `["chaosx.nr26.2.a"]`, horizon `1`, metrics `raw_value` and `conditional_probability`, and scenario set `BLACK_FRIDAY_AI_FINAL_2026_08_30`.

The exact scenario IDs were `bf_ai_01_low_reserve_advisor`, `bf_ai_02_valid_law_change`, `bf_ai_03_wartime_command`, `bf_ai_04_invalid_target`, `bf_ai_05_static_variant_pool`, `bf_ai_06_overlapping_discount`, `bf_ai_07_sale_expiry`, and `bf_ai_08_75_percent_high_chaos`.

Each supplied scenario used `state = {}` because the adapter reported no required inputs for this one-option event surface.

The latest successful evaluation artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0f3fd350909d61b28bca104d29f097d968af273c9d190f22558d1fb8552e7f3f/ab123d30c04db85b6a04d5b64a1b7f3e67a6881841c8bd2bce023950289307c0/probability-7fd20f24dc4c481787b5442d.json`.

Its analysis ID is `probability-7fd20f24dc4c481787b5442d`, its source revision is `8f14d020ede8043a0cbdc51bfd2f130affb6fdf0f11c220ba0f443f11272dadd`, its source hash is `135da139b2368e30cf374cdcb389692bc649162f9bf7409dab57350a090b0995`, and its scenario hash is `aa7ce2aeb6ed9d5b193f704d949a6948753a9c130ce7f9202f1e619edee3af9e`.

The evaluation returned eight candidate-state rows, zero unresolved rows, and nine diagnostics.

| Scenario ID | Candidate | Raw value | Conditional probability | Rank | Classification and boundary |
| --- | --- | ---: | ---: | ---: | --- |
| `bf_ai_01_low_reserve_advisor` | `chaosx.nr26.2.a` | 100 | 1.000000 / 100% | 1 | `Exact` for the one-option acknowledgement event only; intended advisor affordability and PP reserve policy are unresolved. |
| `bf_ai_02_valid_law_change` | `chaosx.nr26.2.a` | 100 | 1.000000 / 100% | 1 | `Exact` for the one-option acknowledgement event only; intended law-action candidates and final discounted affordability are unresolved. |
| `bf_ai_03_wartime_command` | `chaosx.nr26.2.a` | 100 | 1.000000 / 100% | 1 | `Exact` for the one-option acknowledgement event only; intended command-action candidates, battle state, and cooldown are unresolved. |
| `bf_ai_04_invalid_target` | `chaosx.nr26.2.a` | 100 | 1.000000 / 100% | 1 | `Exact` for the one-option acknowledgement event only; intended target validity and zero-weight behavior are unresolved. |
| `bf_ai_05_static_variant_pool` | `chaosx.nr26.2.a` | 100 | 1.000000 / 100% | 1 | `Exact` for the one-option acknowledgement event only; no static normal/discounted variants were found in Event 26 source, but the owner action pool is not MCP-enumerated. |
| `bf_ai_06_overlapping_discount` | `chaosx.nr26.2.a` | 100 | 1.000000 / 100% | 1 | `Exact` for the one-option acknowledgement event only; native sale factors are source-visible, while composed owner modifiers and action ranking are unresolved. |
| `bf_ai_07_sale_expiry` | `chaosx.nr26.2.a` | 100 | 1.000000 / 100% | 1 | `Exact` for the one-option acknowledgement event only; source expiry is bounded, but owner AI re-quote timing is unresolved. |
| `bf_ai_08_75_percent_high_chaos` | `chaosx.nr26.2.a` | 100 | 1.000000 / 100% | 1 | `Exact` for the one-option acknowledgement event only; the source Evolution I branch is visible, but high-chaos action selection is unresolved. |

The evaluator emitted `PROBABILITY_DOMINANT_OUTCOME` for all eight rows and `PROBABILITY_OUTCOME_DOMINANT_ACROSS_SCENARIOS` for `chaosx.nr26.2.a` in 8 of 8 scenarios.

That dominance warning is expected from a complete one-candidate, one-option pool and must not be interpreted as proof that a Black Friday action dominates the country AI.

The event-option result is therefore `Exact` but semantically narrow and does not satisfy the Part 5 action-selection acceptance criteria.

### Custom pool evaluation

`hoi4.probability_evaluate` was also run with adapter `custom_weighted_pool` against `common/scripted_effects/chaosx_settings_effects.txt` and the same eight named scenarios without inventing a candidate list.

The result was `PROBABILITY_ANALYZED` with analysis ID `probability-dd6eaa510558351912a616de`, source revision `df54dd5f1c8ca30bb7f6b5feb6dee3ee194a771d989ca7713d01fdb2f614d377`, source hash `5711a4fe83d6c0928dcf7aa14cea95ae6435aeec39493130dc03850916febea9`, and the same scenario hash `aa7ce2aeb6ed9d5b193f704d949a6948753a9c130ce7f9202f1e619edee3af9e`.

Its authoritative artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f2b102e29781491c4db5ec8816b572fa48e392b6391f6a96a7fa38b13c78ce4c/a7ae114ea63ad0d7bccdf436736667bfe95bcdba86511d3ba94a4f8b151b13a3/probability-dd6eaa510558351912a616de.json`.

The result had zero candidates and one diagnostic, `PROBABILITY_CANDIDATE_POOL_INCOMPLETE`, which explicitly withheld normalized probabilities.

This is `MCP partial`, not a zero-probability result.

The evaluation emitted ranking, matrix, and unresolved visual resources, including `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a9ece8858cce1543a317477003ab9edfdafbfa5879181ed7f4a92ed7eac366dd/9589a9ec7775ba4d8f4ef192578085f293be70780af22a9e16af13174b49224e/probability-probability-dd6eaa510558351912a616de-ranking.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9bd382f3e70b24c4104cb4062106391bc2671699401b8cb70b2509f75cf3721c/f6b1aafbbe55a5aee55ac495d16bee8e138b9f63143f32191d8a2bff14ae952c/probability-probability-dd6eaa510558351912a616de-matrix.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6cc34de4a6f32afd16a90b09c5631e732e81cfd45199abec74fe2209cf8029b/73ef6b577b2f75b31fcf4f25e3d19385afdad9a951c50a84f0acda4ad2220508/probability-probability-dd6eaa510558351912a616de-unresolved.svg`.

### Sweep and render disposition

`hoi4.probability_sweep` was attempted for the same eight scenarios with path `base`, three steps, pairwise sensitivity, and rank-reversal search.

The exact result was `PROBABILITY_SWEEP_RANGE_REQUIRED`: `Every sweep path requires a scenario range, numeric alternatives, or numeric state value`, with the first reported missing range at `bf_ai_01_low_reserve_advisor` and path `base`.

No threshold, sensitivity, or rank-reversal conclusion is claimed.

`hoi4.probability_render` was attempted for both the custom-pool analysis and the later event-option analysis.

The custom-pool render returned `PROBABILITY_ANALYSIS_STALE`, with analysis revision `df54dd5f1c8ca30bb7f6b5feb6dee3ee194a771d989ca7713d01fdb2f614d377` and current revision `948ac8da2a3c3dba9076656a1d870977ed69a7db0b5a2034ca9d4179260cfc24`.

The event-option render returned `PROBABILITY_ANALYSIS_STALE`, with analysis revision `8f14d020ede8043a0cbdc51bfd2f130affb6fdf0f11c220ba0f443f11272dadd` and current revision `15ac220e7ae57c45256c4a8dfa328e96e386b2606f9b8850bd11daa21e1116d66`.

The event-option stale-render receipt is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c7e79a4de6a4c896059cbc0a4a3877f31a202106c42a079690aed85a2d0a38d0/b8650820cae6867812ee8d1479b40255ca0645bccf099c38fdadf998048cb46f/probability-7fd20f24dc4c481787b5442d.json`.

The source changed during the audit, so no stale render is treated as a final current visual proof.

`hoi4.probability_compare` was not called because the existing baseline is source-only and explicitly excludes concurrent Event 26 and universal-cost changes, while the current Event 26 files are untracked or dirty and have no real same-scenario after artifact.

The compare state is therefore `Compare-blocked`, not a zero-delta comparison.

`hoi4.probability_simulate` was skipped because no uncertain input distribution, seed, or sample contract was declared.

`hoi4.probability_sequence` was skipped because the custom pool is incomplete and no complete cadence, cooldown, recovery, cap, removal, reset, timer, or terminal-state manifest is available to the adapter.

## Structural MCP evidence

`hoi4.event_inspect` was run for `chaosx.nr26.1` and for `events/026_black_friday.txt`.

The targeted event trace returned `EVENT_INSPECTED_PARTIAL` because the workspace analysis is large and helper expansion was deferred.

The trace artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1e322a18fcba87d6bd90856ad4020d4f1a3af864d12761695062732d5865188d/a6873f90d402bf5599da67e38e6384d470b1be0f840082cdb9adb28cf85a0803/event-trace-cfc045dd75b4.json`.

Its graph revision is `cfc045dd75b49a40be7744e4e0bcddc6b43131bb92b5deeac6378b3112ac56a2` and graph hash is `803de71c47f92a6f7e371130df868465a9880978fb8106f967467c7907baea20`.

The overview render returned `EVENT_RENDERED_PARTIAL` with manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ef5fe158798bb40082d206da72be37e832d0c3f422800f2e556a9c5532553b1b/9bbf6aeadba99afb0b54dba3523072ed2287b71037385251a2c7c649bbfc71d5/event-overview-cfc045dd75b4-manifest.json`.

The rendered SVG is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d57441cbe57c051b35a3b841492ed696b8029530acca2d6e7125107399b2b4c2/5156bb186140032079ce9a3e4d7bdc72eb46ec7322244d3b68143304c37cff7a/event-overview-cfc045dd75b4.svg` and the rendered PNG is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f48e71b8d3f937c81f68cea14e1a3599a66ca82fc8f02dbde3004c13824cf32c/4cb0a16505e31cda1c33bbc9ebb88113d16f91211f4ae875000881df33541c45/event-overview-cfc045dd75b4.png`.

The manifest identifies an unresolved helper at `events/026_black_friday.txt` line 13: `black_friday_entry_event` is absent from the active MCP helper catalog and is marked `EVENT_HELPER_UNRESOLVED`.

This structural result is `MCP partial` and does not replace source review.

The event-specific `hoi4.event_render` options request returned `INTERNAL_ERROR` with `Unexpected internal error` and no artifact.

## Candidate-pool and external-factor completeness

| Surface | Candidate pool | External factors | Disposition |
| --- | --- | --- | --- |
| `chaosx.nr26.2.a` | Complete one-candidate option pool. | No required adapter inputs; the event option has no eligibility or cost state. | `Exact`, but only the acknowledgement option. |
| Automatic Event 26 launch | Source loops over dynamic `global.all_events`; Event 26 is registered once in `global.fire_once_events`, but MCP did not enumerate the complete runtime pool. | Chaos gate, disabled/fired history, reserved/active flags, dynamic event weights, cadence, and all other event candidates are outside the declared adapter fixture. | `MCP partial` and normalized launch probability unresolved. |
| Sale-discounted decisions and missions | Registry has 2,175 custom cost declarations, but no complete owner action candidate pool is exposed. | Political power, reserve floors, target validity, action caps, cooldowns, route gates, war state, equipment/manpower/resource floors, and competing modifiers are not supplied. | `Unresolved`; no action probability or score claim. |
| Static normal/discounted variants | No Event 26 static variants were found, and the sale ideas are mutually refreshed rather than stacked at the Event 26 marker level. | Runtime owner records were not enumerable by MCP. | Source `Bounded`; duplicate-candidate proof remains unresolved for the owner pool. |

## Base values, modifier traces, and state transitions

The informational option base is `100` and has no option modifiers.

The baseline sale branch uses payment ratio `5000` over a `10000` basis and native cost factor `-0.5`, corresponding to a 50 percent discount in the source contract.

The Evolution I branch uses payment ratio `2500` and native cost factor `-0.75`, corresponding to a 75 percent discount when the evolution branch is enabled and `global.chaos_meter_value >= 600`.

The direct Event 26 reserve gate requires Chaos `>= 200` through `black_friday_can_reserve`.

The shared event registry assigns Event 26 internal tier 1, and `chaos_meter_constants.txt` defines tier 1 as `200..399`, so the central gate and the Event 26 direct gate are source-aligned at the lower threshold.

The shared automatic picker is proportional categorical sampling over its valid weighted pool, not an AI willingness score.

`initialize_event_weights` gives the event-system entries a default weight of `1000`.

`black_friday_reserve_event` now leaves Event 26's stored event weight unchanged during reservation.

`evaluate_random_event_active_pool_candidate` rejects `black_friday_reserved` and `black_friday_active` before the picker reads that weight.

Therefore reservation does not increase or decrease Event 26's effective automatic selection probability while the reserved or active blocker is present; the candidate is excluded before weight normalization.

`black_friday_cancel_reservation` clears the reservation flag and state; no weight restoration is needed because reservation does not mutate the stored weight.

If the event is disabled while reserved and later re-enabled before firing, the source preserves the event-system weight that existed before reservation.

The complete normalized event pool remains unresolved to MCP, but the reservation path no longer introduces a source-level weight starvation or timing-drift mutation.

After activation, fired-history exclusion prevents re-entry, so the activation-time weight marker is not itself a live repeat-selection chance.

The daily pulse updates the weekday flag from `global.num_days % 7`, enforces the Friday remainder, handles reservation and activation, and expires the one-day active sale.

No MTTH timing distribution was exposed for Event 26.

No target-selection or action-cost quote trace was exposed for the owner decisions, missions, advisors, laws, command abilities, or other native action families.

## Validity, dominance, starvation, rank reversal, repetition, and exploit findings

The one-option MCP evaluation is structurally dominant in all eight empty fixtures, but that is not a Black Friday action-dominance finding.

No complete action pool was available, so no valid conclusion can be made about advisor, law, command, target, overlapping-discount, expiry, or high-chaos action dominance.

The invalid-target requirement remains unresolved at the owner action layer because Event 26 does not own the target pool.

The source contains no normal-versus-discounted duplicate Event 26 option or action record.

The owner action pool was not enumerable, so runtime duplicate static variants cannot be ruled out by MCP.

No rank reversal was established because the sweep had no accepted numeric range and the candidate pool was incomplete.

No repetition or snowball rate was established because no complete sequence analysis was possible.

The reservation blocker itself prevents a reserved Event 26 from entering the automatic selector, so reservation does not alter a selection race while it is active.

No reservation-weight starvation is present in the current source; the complete event pool and normalized launch rate remain unproven.

The source does not pre-spend political power or lock an action quote during reservation, but the 2,175 owner cost declarations lack MCP-proven quote, payment, receipt, refund, and AI recheck integration.

Refund farming, quote locking, negative-cost inversion, duplicate payment, double AI evaluation, multiplayer race behavior, and action-cap preservation are therefore unresolved rather than cleared.

No direct Event 26 AI willingness or strategy weight patch was found.

The current source no longer mutates the runtime event-system weight during reservation; activation still records the fire-once marker after the sale becomes active.

Because the baseline has no real Event 26 before artifact, the audit cannot certify that no Event 26 weighted behavior changed without comparison.

## Recommended owner follow-up without applying it

1. Compare the current lifecycle against a real pre-change artifact using the same named scenarios once the complete event pool is exposed; the source-level reservation weight and timer correction is already applied.

2. Expose a complete declared candidate pool for `common/scripted_effects/chaosx_settings_effects.txt::select_weighted_random_event_id` and `evaluate_random_event_selection_candidate`, including every `global.all_events` candidate, eligibility reason, current weight, reserved/active/fired state, and terminal state.

3. Provide an adapter-supported owner action pool for the entries in `docs/plans/026_black_friday_plans/event26_cost_surface_registry.md`, including final discounted price, protected reserve, target validity, route gates, cooldown, caps, competing cost factors, payment, receipt, refund, and post-expiry recheck.

4. Re-run `bf_ai_01_low_reserve_advisor` through `bf_ai_08_75_percent_high_chaos` with populated state rather than `{}` and preserve the exact scenario hash, source revision, candidate pool, and external factors.

5. Run `hoi4.probability_sweep` only after a real numeric range or typed alternatives exist for sale ratio, Chaos threshold, reserve floor, and any owner AI factor, and render the threshold, sensitivity, and rank-reversal evidence.

6. Obtain a real pre-change Event 26 baseline and an owner-applied after state before calling `hoi4.probability_compare`.

7. Keep one logical active action candidate when adding any future normal or discounted static representation, with inactive records excluded before normalization.

8. Complete live timing, displayed-price, payment, save/reload, multiplayer, and natural-selection acceptance only in an authorized live session; this audit did not launch HOI4.

## Skipped analyses, exact blockers, and remaining uncertainty

- `hoi4.probability_sweep`: returned `PROBABILITY_SWEEP_RANGE_REQUIRED` for `base`; no range was fabricated.
- `hoi4.probability_compare`: not called because `probability_baseline.md` has no real Event 26 before artifact and excludes the concurrent Event 26/universal-cost changes.
- `hoi4.probability_simulate`: skipped because no uncertain input distribution and seed were declared.
- `hoi4.probability_sequence`: skipped because the custom pool and full cadence/state-transition manifest are incomplete.
- `hoi4.probability_render`: attempted, but both requested current renders returned `PROBABILITY_ANALYSIS_STALE` after source revisions changed during the audit.
- `custom_weighted_pool`: inspect and evaluate returned zero candidates with `PROBABILITY_CANDIDATE_POOL_INCOMPLETE`; this is an adapter visibility blocker, not proof of an empty runtime pool.
- Event-specific structural options render: returned `INTERNAL_ERROR` with `Unexpected internal error` and no artifact.
- Event structural graph: returned partial because workspace-wide helper analysis was deferred and `black_friday_entry_event` was absent from the active helper catalog.
- Live acceptance: blocked by the explicit no-launch instruction and remains required for timing, payment, multiplayer, and natural AI behavior.

The final audit is not a release sign-off for Event 26 weighted behavior.

## Parent post-audit correction

The source-level starvation concern above was addressed after this historical audit pass. `black_friday_reserve_event` now excludes a reserved candidate through the existing eligibility predicate without mutating its stored event weight, and the reservation path recalculates the current event timer only when the natural dispatch remains pending. A same-day eligible Friday activation therefore does not reset a timer already running from the earlier selection.

The current source also contains five bounded Communist-spread logical cost adapters: one national counter-agitation action, three local intervention levels through one target-preserving helper, and one emergency intervention action. These adapters provide nine shared quote, affordability, payment, and receipt callsites each and three settlement callsites, with no universal refund acknowledgement yet. They do not expand the probability conclusion: the owner action pool remains incomplete.

The latest event MCP inspection returned `EVENT_INSPECTED_PARTIAL` at revision `27c77545e9241b4398d074f7bae0aaedf8ebba6790c26141f6e3508bf4238175` with graph hash `9231a40d3395079e08c9610848afcd4d0fc93e97e2dd33dcff81f5d140de7291`. The focused overview render selected both Event 26 nodes and produced layout hash `3ea884981b1b4ab3fcaf97c911a7503b65b619f8757e3164f29a88b151b0d96a`; helper-expanded options, timing, and state views remained partial without selector blockers and selected no bounded branches. The custom-pool inspection still reported an incomplete zero-candidate pool, while the fresh probability inspect and evaluation resolved the canonical report option against source revision `a477c32d9183b75725e09db4c376b6207faf6cfb97047b2b577b89c455cf75d5`, again finding only the narrow `chaosx.nr26.2.a` informational option at 100 percent across the eight named empty scenarios. No complete before/after global-pool comparison or universal AI-affordability result is claimed.

The parent should treat the option result as a narrow exact conditional result and the launch/action surfaces as unresolved; a real before/after comparison with the complete event pool remains required.
