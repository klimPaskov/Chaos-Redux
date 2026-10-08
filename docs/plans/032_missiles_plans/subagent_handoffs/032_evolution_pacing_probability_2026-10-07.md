# Event 32 evolution pacing probability baseline — 2026-10-07

Disposition: unresolved. The read-only audit captured the current source and the requested scenario set, but the connected probability analyzer matched neither the evolution helper's timing model nor its random input, so it produced no numeric timing baseline.

Accepted design basis: `docs/specs/032_missiles_specs/032_missiles_spec_part_4_evolutions.md`, `docs/specs/032_missiles_specs/032_missiles_spec_part_6_ai_and_probability.md`, and `docs/specs/032_missiles_specs/032_missiles_probability_scenario_matrix.md`, supplied as the accepted Event 32 design inputs for this audit.

The matching fixture is [032_evolution_pacing_probability_2026-10-07_scenarios.json](032_evolution_pacing_probability_2026-10-07_scenarios.json). It preserves `EVO-01` through `EVO-10`, adds `EVO-PACE`, records the exact MCP request states, and leaves unavailable scope data explicitly unresolved. Its scenario set id is `E32_EVOLUTION_PACING_2026-10-07`; HOI4 MCP returned no scenario hash or analysis artifact. The local fixture file SHA-256 is `44DE496A1377CC279D59898790A600D5FC1A25874CA323C0D9D41C29B426601F`, not an MCP scenario hash.

## Audited surface and source identities

The named weighted surface is the five independent Event 32 evolution unlock tracks: Rogue Launch Commands, Unreliable Guidance, Saturation Arsenals, Special Warheads, and Automatic Retaliation. The helper is `missiles_arm_evolution_track` in `common/scripted_effects/032_missiles_operations_effects.txt`; its pressure inputs and eligibility come from `missiles_measure_evolution_pressure`, `missiles_evolution_*_is_eligible`, and the five `missiles_evolution_*_pressure_is_high` triggers.

| Source | Identifiers and relevant lines | Local SHA-256 | MCP source revision |
| --- | --- | --- | --- |
| `common/scripted_effects/032_missiles_operations_effects.txt` | `missiles_measure_evolution_pressure` 543–594; `missiles_arm_evolution_track` 655–712; track evaluation 816–978; watch 983–1015; delayed job 1020–1123 | `5EC05957945AD6F2F2E71ADF4091EDECA7B08E57A233F8267585B7428CBCD6E7` | source-location revisions `640f18464a7eae92e6808dbe1a8b1a0a5e355f91aa86076ca7de7d1f959f3e76` and `4a27c70bd4e962fc09e2680ab8342d387756cc4b245e299904ea9aef0881a3bd`; structure index revision `369e182c77c427cfbe9a740ca6d1ff3c7c298bd1ea7bc1073a76fe59aa30a7f8` |
| `common/script_constants/032_missiles_constants.txt` | `missiles_evolution_timing` 414–435; `missiles_evolution_pressure` 786–808; `missiles_evolution_pacing` 812–837 | `1DABADF3281586EF3106819E5B130F0685C726C85D495A5EF59798FA3C368A94` | source-location revision `174a3d894524b4e78a7a1eeb32042d53ce7b437c5686b1bb9c73b7618188d790` |
| `common/scripted_triggers/032_missiles_operations_triggers.txt` | eligibility and high-pressure helpers 1041–1089; current enabled-track gates 1091–1116 | `424E1749A463C7621C89F8A881ECCFD05109F78B8911F6598601C7D324948504` | source-location revision `8a5a4f3972667eb1dd0cd0bb9865a1e3d0fbe791711c2c224007c383b07c468e`; structure index revision `369e182c77c427cfbe9a740ca6d1ff3c7c298bd1ea7bc1073a76fe59aa30a7f8` |
| `common/scripted_effects/032_missiles_effects.txt` | `missiles_global_firing_transaction` calls the evolution evaluator at 274 | `B28EF2A3CE3E88C177E29FCF7DEEFC0AE253531D17FF41AFB1EABEE90A7F4E64` | source-location revision `f80448312962dc62d3a6568168f1b29b5e763acb0160dc770ee869e6c1222dd8` |
| `events/032_missile_crisis.txt` | triggered-only job `chaosx.nr32.190` at 62–67; triggered-only watch `chaosx.nr32.191` at 72–76 | `2416FC6159201C6059925CD68218DE159EE0F37ADE4F89896403801FEC99A50A` | source-location revision `8a069c1e5049b5f1356f651580963c6afa9dba88b3a039db153d06d61194b243` |

The five current Event Log gates remain `events_log_disabled_evolution_32_32_1` through `events_log_disabled_evolution_32_32_5`, mapped to Saturation, Guidance, Special Warheads, Rogue Commands, and Automatic Retaliation respectively. The older dated gate baseline and its fixture were left untouched.

## MCP probability and structural evidence

The first audit call was `hoi4.probability_inspect` for `direct_random`, the supplied workspace `mod_chaos_redux_ea3b2d67c2c0`, source path `common/scripted_effects/032_missiles_operations_effects.txt`, and identifier `missiles_arm_evolution_track`. It returned `PROBABILITY_SOURCE_DISCOVERED`, but `discoveryReason` was `identifier_not_found`; the only matched adapter was `random_list`, with 19 other list-entry candidates in the file. The adapter source hash was `02d2c9f5dce675e336c3c67ccc35a866f85d16a56f372d60b3a03129f13801cb`, source revision `2fcfa414fb60c0fef1fe7cea70bba47a1d2eff58a5dc7f3adb9919a3b4060324`, and artifact URI `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/79ee188405c6dce5d9013a80203f7369626386e73912600a0393e535483aeee8/60f402dd2d0cf416601682cd0ce67aad3067a9adba13c9790c0852e75ac8f3f7/probability-inspect-02d2c9f5dce6.json`.

A second `probability_inspect` for `event_mean_time_to_happen` on the same source and helper returned `requested_adapter_empty`, the same source hash, source revision `c822e464e8aac03b93d77f5f12e6b088865e39e330ec97a4e8569598a145cf62`, and artifact URI `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/90b72757aa1bc8515ee93a122f4ad1fe777f564ef9d032856515be24485bb6c7/b058d793c1a7a447a064e343a2fe772e23137bc4ac92cf879abfeab9c619acc7/probability-inspect-02d2c9f5dce6.json`. The helper uses `set_temp_variable_to_random`; it does not present a normalized `random_list` choice or an event MTTH block. The 19 unrelated `random_list` entries were not used as a proxy.

`probability_evaluate` was run for both `event_mean_time_to_happen` and `direct_random` against all eleven named cases in the fixture. Both returned `PROBABILITY_SURFACE_EMPTY` with blocker “No weighted blocks matched this request,” no analysis artifact, and no scenario hash. `probability_sweep` was run over the five base-day constants, the shortening and lengthening multipliers, and the spread minimum and width under the same scenario IDs; it returned the same blocker and no artifacts. Thus the base constants and source gates below are exact source facts, while realized timing, cumulative chance, sensitivity, and rank reversals are unresolved.

`probability_render` could not be called because the evaluations returned no `analysisId`. `probability_simulate` was skipped because the connected `direct_random` adapter did not match the uniform draw and no seedable model was produced. `probability_sequence` was skipped because the five tracks are not a declared custom weighted pool. `probability_compare` was not run: no weighted timing edit or after-source exists, and the parent will freeze the pre-edit physical sources before requesting the same-scenario comparison. No comparison id exists.

The required structural route was also called for event `chaosx.nr32.190`. `hoi4.event_inspect` returned `EVENT_INSPECTED_PARTIAL`, one blocking diagnostic, graph revision `8f4a82aa5d847df22b40a90e209f8bd0e27f3d6ebe79d13e4fb3dbaf45dc33b0`, graph hash `d494c41cf68a6eb896650d0f95ea38572ce93b8c83273a07a92d60c74eb41ceb`, and trace URI `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c26dad0c97f217c5851f4b2e198a482d1ae093e42d585488d0ec6f5fdefd10bf/f0189c19b981fc16f073e84c3562b9594cdea98e5407648a1cade053c175f98f/event-trace-8f4a82aa5d84.json`.

`hoi4.event_render` returned `EVENT_RENDERED_PARTIAL` for view `timing` at the same graph revision and hash. Its manifest reports zero selected node ids, zero branch renders, and 45,964 total graph nodes. The manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/80e79c4c36df450f7bd57b2025aaba4d343a06c6bc093220151fc4f3c6227018/dbecfd93f1dd0d166b08b4679681af06c673144ea217c134076df7c46eef11f1/event-timing-8f4a82aa5d84-manifest.json`; JSON, SVG, and PNG are linked in the fixture. The physical event exists at the source location verified by `hoi4.source_lookup`, but the MCP selection did not resolve it to renderable nodes. Structural timing remains unresolved. The full trace resource could not be reliably parsed from the oversized range response, so its hidden blocking-diagnostic detail remains unresolved as well.

The connected tool catalog exposed live schemas for probability inspect/evaluate/sweep/compare/render and event inspect/render. It exposed no separate server version or health route, so the exact running server version was not independently confirmed. The applied request shapes and responses are preserved in the JSON fixture.

## Source timing trace

| Track | Base constant | Eligibility gate | High-pressure shortening |
| --- | --- | --- | --- |
| Rogue Launch Commands | 120 days | Chaos at least 200; vulnerable managed-program count at least 1 | Vulnerable count at least 2 |
| Unreliable Guidance | 105 days | Chaos at least 400; at least 1 operational program; at least one low-readiness, overstocking, launch-count, or maintenance-neglect condition | Managed programs at war at least 2 |
| Saturation Arsenals | 90 days | Chaos at least 600; operational count at least 2; operational share at least 0.40; managed programs at war at least 2 | Managed programs at war at least 4 |
| Special Warheads | 120 days | Chaos at least 800; payload-owning managed-program count at least 1 | Payload-owner count at least 2 |
| Automatic Retaliation | 150 days | Chaos at least 900; no `world_end`; at least 2 operational programs; at least 1 hostile retaliation-capable pair | Hostile-pair count at least 2 |

On ordinary arming, a total managed-program count below 2 multiplies the input delay by 1.50. The helper samples a temporary random value, maps it through `spread_min = 0.75` and `spread_width = 0.50`, multiplies the delay, rounds it, and clamps to at least one day. Installed game documentation states that `set_temp_variable_to_random` returns a value in `[0,1)`. These are source and engine-reference facts, not an MCP-derived timing distribution.

On the first pulse, the helper executes the random draw and then overwrites the delay with `first_fire_delay_days = 21` plus `missiles_evolution_armed * first_fire_stagger_days = 14` per previously armed track, followed by rounding and clamping. Track order is Rogue, Guidance, Saturation, Special Warheads, Automatic Retaliation. The sampled random value does not determine that first-pulse due date.

Each new track arm queues a hidden `chaosx.nr32.190` event. A job remeasures registry pressure and eligibility and commits at most one due track during that invocation; remaining due tracks request a 7-day requeue. There is no single global job-queued guard in `missiles_queue_evolution_job`. The source therefore establishes per-track pending flags and due dates but does not establish how the engine orders multiple same-day queued jobs. The first-pulse formula staggers tracks, but ordinary rounded random delays could coincide; collision frequency and whether repeated event invocations defeat the intended 7-day separation are unresolved.

One hidden `chaosx.nr32.191` watch is queued for a living program host every 30 days while any enabled track remains locked. It recounts `global.missiles_program_registry`; it is not a daily or weekly all-country `on_action`, but it is a recurring global program-registry scan. That distinction should be resolved against the parent requirement for no recurring global scan.

No `mtth:` token or `mean_time_to_happen` block was found in the four scoped implementation files. The code therefore does not implement the accepted “MTTH” scenario contract as a daily hazard. It samples one delay when arming, then executes a scheduled event and rechecks eligibility on firing and watch pulses. The source comments call this a base MTTH, but the exact engine MTTH survival curve is not what this helper implements.

## Scenario completeness and outcome classification

The candidate pool is not applicable because the tracks are not competing selections. The dynamic program registry is nevertheless required to compute every pressure count, share, and hostile pair. The submitted MCP states supplied only initialization, the scenario's global chaos value, the corresponding current `events_log_disabled_evolution_32_32_N` flag, `world_end = false` for `EVO-10`, and `missiles_evolution_first_pulse_done = false` for `EVO-PACE`.

All scenario world states remain incomplete. Missing inputs include the full managed program registry and country bindings, operational and vulnerable program membership, each track's readiness/overstocking/maintenance conditions, payload owners, global launch count, war-program count, operational-share denominator, hostile retaliation-capable pairs, all other tracks' enabled/unlocked/pending/due-date flags for `EVO-PACE`, first-pulse state for `EVO-01` through `EVO-10`, and any changes in chaos, war, payload, site, disable state, or host during the delay. No date, seed, or scheduled state transitions were submitted.

Classifications are exact for source constants and visible gates, bounded for the source-defined first-pulse and random-spread formulas, and unresolved for all numeric timing and probability results. No score-only or sampled result was produced. There is no candidate ranking or normalized selection probability for this surface.

Two accepted scenarios need clarification before an exact trace. `EVO-02` expects a longer-than-base Rogue delay for a stable world and one secure program, while both the accepted evolution spec and current source require a vulnerable program; if the scenario has zero vulnerable programs, it is ineligible. `EVO-04` expects longer-than-base Guidance timing from few launches and high readiness, but the source still requires another strain predicate such as overstocking or maintenance neglect. `EVO-05` says “many mature programs” without declaring how many managed programs are at war, even though the shortening threshold is four. These are fixture and design ambiguities, not numeric analyzer findings.

## AI validity, dominance, repetition, and exploit risk

No `ai_will_do`, `ai_chance`, AI strategy factor, or probability-proportional candidate pool controls the five global unlock timers. AI score ranking and dead/allied target validity are outside this weighted surface.

There is no source-level random-selection dominance or normalized rank race. Deterministic branch order gives Rogue priority over Guidance, Saturation, Special Warheads, and Automatic Retaliation when several are due within one job invocation. Remaining due tracks are staged by 7 days in that invocation; separately queued same-day `.190` jobs may affect that cadence, but engine ordering is unresolved. The finite five-track set bounds source-level starvation; no infinite repeated unlock path is evident. The watch does repeat every 30 days while a track remains locked, and each track can be rearmed if its pending state is cleared and eligibility later returns. Runtime repetition and exploit behavior were not established.

The source shows no positive timing weight on an ineligible track at the arming gate: disabled and already-unlocked tracks are excluded, and special-warhead and automatic-retaliation requirements are explicit. The `EVO-02` matrix mismatch is a scenario-contract conflict. The potential cadence risks are the recurring 30-day registry recount and multiple independent `.190` schedules without a visible global coalescing guard; neither is a proven live exploit.

## Recommendations for the owner; no changes applied

1. Reconcile the accepted requirement for five MTTH tracks with `missiles_arm_evolution_track` in `common/scripted_effects/032_missiles_operations_effects.txt`. Use a probability-adapter-supported per-track timing construct or expose a supported analyzer model; retain five independent gates and do not recast the uniform draw as `random_list`.
2. Resolve `EVO-02` in `docs/specs/032_missiles_specs/032_missiles_probability_scenario_matrix.md` against the Rogue vulnerability gate in `common/scripted_triggers/032_missiles_operations_triggers.txt`; either specify a vulnerable but otherwise stable case or make the expected result ineligible.
3. Complete `EVO-04` and `EVO-05` inputs in the scenario matrix: identify which strain predicate makes Guidance eligible and set the war-program count around Saturation's four-program shortening threshold.
4. To satisfy the no-recurring-global-scan goal, review `missiles_queue_evolution_watch`, `missiles_run_evolution_watch`, and `chaosx.nr32.191`. Prefer bounded event-driven wakeups at exact registry/eligibility transitions; do not replace the watch with a daily or weekly all-country action.
5. Define and verify one-job-at-a-time semantics across the five `.190` schedules so the intended seven-day spacing survives tied due dates. Preserve current gate names and independently test each track's disable, already-unlocked, ineligible-at-due, and reeligible-after-clear cases.
6. Before any weight edit, have the parent freeze the physical pre-edit source files and this exact scenario fixture. After the owner applies the authorized change, rerun the same scenario IDs and request `hoi4.probability_compare`; the current handoff is not a comparison baseline.

## Skipped analyses and blockers

- Numeric baseline: blocked by `PROBABILITY_SURFACE_EMPTY` for both `event_mean_time_to_happen` and `direct_random`.
- Threshold/sensitivity/rank-reversal results: blocked by the same empty-surface result from `probability_sweep`.
- Probability render: no `analysisId` was returned, so there is no renderable probability analysis.
- Structural event chain: event inspector and renderer returned partial reports with zero selected event nodes and one blocking diagnostic; exact engine graph resolution remains unknown.
- Simulation: not run because the direct-random adapter did not match the helper's uniform draw and no supported seedable model exists.
- Sequence: not run because no complete custom weighted pool exists.
- Before/after comparison: not run because the user stated no timing edit has occurred and the parent will freeze the pre-edit physical sources before requesting comparison.
- Installed documentation search for an event `mean_time_to_happen` section returned no game-doc matches. The installed effects documentation section for `set_temp_variable_to_random` and the offline wiki MTTH/event sections were read and are cited in the fixture.
- No gameplay, event, trigger, constant, localisation, runtime, or index file was edited. No test, game launch, log search, subagent, comparison, commit, or Git write was performed.
