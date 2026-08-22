# Event 006 Independence Wave probability audit

Date: 2026-08-22.

Owner: `/root/event6_probability_audit`.

Parent: `/root`.

Mode: read-only weighted-logic audit.

Disposition: **PARTIAL / HOLD**.

No gameplay, AI, event, focus, decision, mission, technology, doctrine, scripted-effect, localisation, spreadsheet, or runtime file was changed by this audit.

## Executive verdict

The current HOI4 MCP probability inspector successfully parsed the outer Event 006 automatic allocator `random_list` as a complete 14-entry proportional-categorical source pool, but the required current six-band evaluation timed out after 180 seconds.

That inspect proves source-level entry discovery only; it does not prove that any package is runtime-eligible, that the inner package pool is complete, or that a wave reaches its nominal target count.

The highest-impact weighted blocker is the mismatch between the tuning contract and the allocator fallback: `independence_wave_allocate_automatic_packages` commits a partial wave after pool exhaustion by replacing the nominal target with the number selected at `common/scripted_effects/006_independence_wave_package_allocator_effects.txt:124-142`.

The exact owner action is for the allocator owner to make this contract explicit in `independence_wave_allocate_automatic_packages`: if the accepted contract is exact bands, gate contribution readiness on `selected_count == target_count` and fail closed when the pool is short; if partial waves are intended, promote that fallback to an explicit accepted tuning/acceptance rule and add typed scenarios for it.

No balance target or numeric weight change is selected here.

The 2026-08-20 attestation-weight owner fix is present in the current source: the minimum clamp at `common/scripted_effects/006_independence_wave_package_planner_effects.txt:689-699` is inside the content-attestation gate, so unattested rows no longer receive the positive minimum weight.

## Authority and source boundary

The current source-of-truth map is `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`.

The current authority override dated 2026-08-22 reports 40 runtime package adapters, 32 content-attested selectable packages, 29 compatible reservation groups, and 161 unattested selectable rows out of 193 non-overlay rows.

The eight adapter-only rows remain fail-closed: IW-013 NAV, IW-015 GLC, IW-043 CHU, IW-058 ASY, IW-093 DOX, IW-098 SOK, IW-177 FIJ, and IW-179 FSM.

The active automatic target ladder is `3/4/5/7/10`, and World Collapse also targets `10`.

The current accepted deterministic Join order is `IW-001, IW-002, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-012, IW-014, IW-017, IW-018, IW-019, IW-023, IW-024, IW-026, IW-027, IW-028, IW-029, IW-030, IW-031, IW-038, IW-040, IW-044, IW-045, IW-033, IW-041, IW-070, IW-071, IW-072, IW-173, IW-184`.

The accepted tuning matrix is `docs/specs/006_independence_wave_specs/matrices/006_wave_tuning_model.csv`.

The accepted AI behavior matrix is `docs/specs/006_independence_wave_specs/matrices/006_ai_strategy_matrix.csv`.

The latest resume packet is `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`.

## References consulted

I read `AGENTS.md` before analysis.

I read `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-mtth/SKILL.md`, `.agents/skills/chaos-redux-focus-trees/SKILL.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, `.agents/skills/chaos-redux-event-planning/SKILL.md`, and `.agents/skills/chaos-redux-improvement-loop/SKILL.md`.

I consulted the offline wiki pages `Data structures - Hearts of Iron 4 Wiki.md`, `Triggers - Hearts of Iron 4 Wiki.md`, `Effects - Hearts of Iron 4 Wiki.md`, `Modifiers - Hearts of Iron 4 Wiki.md`, `Localisation - Hearts of Iron 4 Wiki.md`, `Scopes - Hearts of Iron 4 Wiki.md`, `On actions - Hearts of Iron 4 Wiki.md`, `Event modding - Hearts of Iron 4 Wiki.md`, `Decision modding - Hearts of Iron 4 Wiki.md`, `Idea modding - Hearts of Iron 4 Wiki.md`, `AI modding - Hearts of Iron 4 Wiki.md`, and the focus-tree reference under `paradox_wiki/`.

I read the relevant vanilla documentation in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`, including `script_concept_documentation.md`, `script_collection_input.md`, `script_collection_operator.md`, `effects_documentation.md`, and `triggers_documentation.md`.

The relevant engine semantics are that a Clausewitz `random_list` selects an effect proportionally to its associated weight, event `ai_chance` is a proportional option pool only when its local candidate set is complete, decision and mission `ai_will_do` values are willingness scores rather than click probabilities, focus `ai_will_do` is a highest-score race over available focuses, and MTTH is a timing distribution after trigger validity rather than a choice score.

## Successful current MCP probability evidence

### Automatic allocator outer random list

Source: `common/scripted_effects/006_independence_wave_package_allocator_effects.txt`.

Adapter: `random_list`.

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

Source revision: `41d66c17291950a6de61c209c91c54ad6a71121681093eeab95d4e1865324bec`.

Source hash: `9cab0bffea71b78719b2c8634363338e9f12e4d214de1603dc0f9b6b24ef72b9`.

Result code: `PROBABILITY_SOURCE_INSPECTED`.

Selection rule: `proportional_categorical`.

Normalized probability support: `true` at the source-entry level.

Raw score support: `true`.

Sequence support: `false`.

Time-distribution support: `false`.

Complete-pool requirement: `true`.

Evaluation cadence: when the enclosing `random_list` executes.

Current inspect counts: 14 candidates found, 0 statically available candidates, 14 required inputs, and 0 unresolved diagnostics.

The 14 source candidate identifiers supplied by the inspector are:

`common/scripted_effects/006_independence_wave_package_allocator_effects.txt:57.entry.1`.

`common/scripted_effects/006_independence_wave_package_allocator_effects.txt:57.entry.2`.

`common/scripted_effects/006_independence_wave_package_allocator_effects.txt:57.entry.3`.

`common/scripted_effects/006_independence_wave_package_allocator_effects.txt:57.entry.4`.

`common/scripted_effects/006_independence_wave_package_allocator_effects.txt:57.entry.5`.

`common/scripted_effects/006_independence_wave_package_allocator_effects.txt:57.entry.6`.

`common/scripted_effects/006_independence_wave_package_allocator_effects.txt:57.entry.7`.

`common/scripted_effects/006_independence_wave_package_allocator_effects.txt:57.entry.8`.

`common/scripted_effects/006_independence_wave_package_allocator_effects.txt:57.entry.9`.

`common/scripted_effects/006_independence_wave_package_allocator_effects.txt:57.entry.10`.

`common/scripted_effects/006_independence_wave_package_allocator_effects.txt:57.entry.11`.

`common/scripted_effects/006_independence_wave_package_allocator_effects.txt:57.entry.12`.

`common/scripted_effects/006_independence_wave_package_allocator_effects.txt:57.entry.13`.

`common/scripted_effects/006_independence_wave_package_allocator_effects.txt:57.entry.14`.

The required input variables are `independence_wave_region_01_total_weight` through `independence_wave_region_14_total_weight`.

Current inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1f1eab086b3e8102dccbc7f708abf49abb9fb094c4c654d0b811a57e9ee7e827/5937aa6bdf2b62b553a76b10fe82ced8217f407254d9a16fe6b4bdac971329b2/probability-inspect-9cab0bffea71.json`.

The inspector limitation is explicit: dynamic entry keys and effect-derived weights remain unresolved unless they are declared as scenario inputs.

The current result is therefore **exact for source-level outer-pool discovery**, not exact for runtime package selection.

## Current named allocator scenarios

The evaluate request used scenario set `E6_ALLOCATOR_BANDS_CURRENT_2026_08_22`.

The six named scenarios were `CALM_BAND_3`, `GATHERING_BAND_4`, `RISING_BAND_5`, `CHAOS_BAND_7`, `TOTALEN_BAND_10`, and `WORLD_COLLAPSE_BAND_10`.

All scenarios used actor `WORLD`, date `1936.1.1`, and explicit values for all fourteen region total-weight variables.

`CALM_BAND_3` declared region 01 weight `525`, region 02 weight `175`, and regions 03 through 14 weight `0`.

`GATHERING_BAND_4` declared region 01 weight `700`, region 02 weight `325`, region 14 weight `150`, and all other regions weight `0`.

`RISING_BAND_5`, `CHAOS_BAND_7`, `TOTALEN_BAND_10`, and `WORLD_COLLAPSE_BAND_10` each declared region 01 weight `850`, region 02 weight `325`, region 14 weight `150`, and all other regions weight `0`.

The evaluate request supplied the complete 14-entry outer candidate pool listed above.

Requested metrics were `conditional_probability` and `raw_value`.

Requested outputs were `json`, `ranking`, `matrix`, `waterfall`, and `unresolved`.

The evaluate call failed with the exact error `tool call failed for hoi4_agent_tools/hoi4.probability_evaluate: Caused by: timed out awaiting tools/call after 180s`.

No analysis ID, scenario hash, current ranking artifact, current matrix artifact, current waterfall artifact, current unresolved artifact, or current rendered probability evidence exists for this request.

The outer 14-variable fixture is complete for the declared source inputs, but the full runtime candidate pool is incomplete for package-level claims because the scenarios did not declare package attestation, package identity, anchor and capital validity, host survival, reservation collisions, target validity, sponsor records, patron or league state, prior-wave arrays, selected-host and selected-region arrays, or attempt and cooldown transitions.

The current allocator evaluation classification is therefore **unresolved**, not exact, bounded, or sampled.

## Source evidence for the blocker

`independence_wave_prepare_all_automatic_weights` prepares all fourteen regional totals and sums them before every draw at `common/scripted_effects/006_independence_wave_package_allocator_effects.txt:15-44`.

`independence_wave_select_one_automatic_package` executes the outer weighted list at `common/scripted_effects/006_independence_wave_package_allocator_effects.txt:47-76`.

`independence_wave_allocate_automatic_packages` repeats draws until the target count or attempt cap and then handles exact count and pool exhaustion at `common/scripted_effects/006_independence_wave_package_allocator_effects.txt:79-151`.

The pool-exhaustion branch at lines 124-142 sets `global.independence_wave_plan_target_count` and `global.liberation_plan_expected_country_count` to `global.independence_wave_plan_selected_count` before setting `independence_wave_plan_contribution_ready` when arrays align.

That branch can turn target 3, 4, 5, 7, or 10 into a smaller committed wave when runtime admissions, host reservations, or package content reduce the viable pool.

`independence_wave_calculate_candidate_allocation_weight` recomputes package weights before each draw at `common/scripted_effects/006_independence_wave_package_planner_effects.txt:484-700`.

Its dynamic terms include earliest chaos band, attestation, sponsorship, registered-tag status, new-region and new-host novelty, prior package, prior region and prior host penalties, signature low-chaos penalty, dormant nations, Armed Birth, Sovereign Congress, open sovereignty, and World Collapse rarity.

The package reservation path additionally requires content attestation, package mapping, country and anchor targets, host reservation, and country reservation before an accepted candidate increments the plan at `common/scripted_effects/006_independence_wave_package_planner_effects.txt:101-106` and its surrounding helpers.

Those inner dynamic candidates and event-target transitions were not normalized by the current MCP call.

## Other audited weighted surfaces

### Event options and random surfaces

Core event source: `events/006_independence_wave.txt`.

The root is `chaosx.nr6.1` at `events/006_independence_wave.txt:12`.

The file contains event-option `ai_chance` blocks, including the visible decision options beginning at lines 247, 271, 305, 342, 368, 386, 412, 424, 444, 455, and 467.

The current probability inspect/evaluate route for this source was not completed after the allocator timeout; the dated 2026-08-13 handoff records a superseded source-revision inspect and a bounded empty-fixture evaluate with an incomplete runtime option pool.

Historical inspect artifact, not current acceptance evidence: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ebf6bff0e3403d6f2f586014cf2126a1ed52e88573098538c6a78b6391a1a989/a99789fe32cde798d4b4a63ccadc6a3ab12bb43017f6af6d223142d01f936d6b/probability-inspect-b97c0de3de07.json`.

Historical empty-fixture analysis, not current acceptance evidence: analysis `probability-7b8d41ba0b9d22d0b3b5fd32`, scenario `E6_CORE_EMPTY_CURRENT_2026_08_13 / CORE_EMPTY`, scenario hash `8034753966613b5e97c825478b2c5fec4c55145c2b9f86bcb4d75975aa2cd7b3`, with 23 unresolved inputs and normalized probabilities withheld.

The source-level classification is **score/proportional semantics known, current runtime probability unresolved**.

Random surfaces reviewed include the allocator `random_list`, `common/scripted_effects/006_independence_wave_package_allocator_effects.txt`, direct-random discovery, and custom-pool discovery in the dated probability handoffs.

The dated allocator evidence from 2026-07-24 is bounded first-draw context only and uses a superseded source hash.

Its eight-attested-package control reported 75% region 01 and 25% region 02 in Calm, 59.574% / 27.660% / 12.766% for regions 01/02/14 in Gathering, and 64.151% / 24.528% / 11.321% for regions 01/02/14 in Rising, Chaos, Totalen, and World Collapse.

Those figures are not reused as current evidence because the source revision and admission boundary changed, and they cover only first draw under declared assumptions.

### Evolution MTTH

Source: `common/mtth/006_independence_wave_evolution_mtth.txt`.

The MTTH entry is `independence_wave_evolution_interval` at line 9.

The source applies chaos-tier factors and thin or dense network factors based on `global.independence_wave_active_country_count` at lines 12-48.

The dated 2026-08-13 probability inspect reported `no_weighted_surfaces` for this source and the matching evolution effects source, which is an adapter-capability result rather than proof of zero timing.

The matching dated evaluate was blocked by transport, so no effective MTTH days, timing horizon, cumulative chance, or median interval is proven.

Current MTTH classification: **unresolved adapter surface**.

Owner follow-up is to provide a current adapter-supported timing fixture or preserve this as an MCP limitation; no MTTH numeric change is recommended by this audit.

### Decisions and missions

Shared source: `common/decisions/006_independence_wave_decisions.txt`.

Scenario source: `common/decisions/006_independence_wave_scenario_decisions.txt`.

Package sources explicitly in scope are `common/decisions/006_independence_wave_ruthenia_decisions.txt`, `common/decisions/006_independence_wave_kuban_decisions.txt`, and `common/decisions/006_independence_wave_tatarstan_decisions.txt`.

The latest peer handoff `006_event6_decision_mission_current_audit_2026-08-22.md` records a successful dated shared decision inspect with 10 candidates, 0 available candidates, 88 required inputs, and no unresolved parser inputs, plus package mission inspection artifacts.

My current retry of `decision_ai_will_do` on the shared source timed out after 180 seconds, so the peer artifact is retained as dated discovery evidence and not relabelled as a current same-revision evaluation.

Decision and mission candidates are runtime-gated by phase, package identity, setup, capital control, route and government flags, active-project locks, ledgers, resource and civilian-factory affordability, former-host state, war state, and target validity.

No complete current decision or mission candidate pool was available for normalized selection probabilities.

Decision and mission result classification is **score-only and unresolved**, not click probability.

No current `probability_evaluate`, `probability_sweep`, `probability_compare`, or `probability_render` result exists for these surfaces in this audit.

### Focus AI

Source: `common/national_focus/006_independence_wave_focus.txt`.

The current source-of-truth override reports 184 focuses, 195 connectors, zero crossings, and zero node intersections, while authored layout warnings and unrelated vanilla diagnostics keep focus acceptance at HOLD.

Focus selection is a highest-score race over the currently available and valid focus pool, not a normalized probability pool.

The complete available focus pool, prerequisite and bypass state, mutual exclusions, route lock, package identity, and hidden state were not supplied to a current probability evaluation.

The current `national_focus_ai_will_do` inspect was not completed because the structural focus inspect itself timed out after 180 seconds once the MCP route degraded.

Focus classification is **score-only and unresolved**.

No focus dominance, starvation, or rank-reversal claim is made.

### Host, patron, league, and AI strategy factors

Strategy sources are `common/ai_strategy/006_independence_wave_generic.txt`, `common/ai_strategy/006_independence_wave_rival_bloc.txt`, `common/ai_strategy/006_independence_wave_ruthenia.txt`, `common/ai_strategy/006_independence_wave_kuban.txt`, and `common/ai_strategy/006_independence_wave_tatarstan.txt`.

The AI matrix profiles most relevant to this surface are AI-06 patron-dependent autonomy seeker, AI-07 client state, AI-08 league internationalist, AI-13 conciliatory former host, AI-14 revanchist former host, AI-15 former-host remnant, AI-17 great-power patron, AI-18 league leader, AI-19 small league member, and scenario profiles AI-21 through AI-24.

These profiles define qualitative priorities and avoidances for patron capture, league contribution, host settlement, collective defense, recognition, proxy conflict, and revisionist pressure.

The dated source review records repeated package strategy ladder values for the RUT, KUB, and TAT package files, including army 86, infantry 40, support 50, artillery 24, infrastructure 70, defense 82, emergency army 118, and founding or settled restraint values of -260 and -430.

Those values are source-level score inputs only; no current `ai_strategy_factor` inspect, evaluate, sweep, or compare completed in this run.

The current classification is **score-only and unresolved**.

No strategy-factor dominance, overlap, rank reversal, patron snowball, league starvation, or host-war probability is claimed.

## Candidate-pool and external-factor completeness

The allocator outer source pool is complete at 14 region entries for the current inspect.

The six requested band scenarios declared all 14 region total-weight variables, so the declared outer numeric inputs were complete.

The runtime package pool is incomplete because the scenario set did not include the admitted package IDs, package-content attestation flags, exact package-region bindings, country and anchor targets, host survival and control, reservation groups and collisions, sponsorship records, patron and league state, previous-wave package and host arrays, selected-region and selected-host arrays, attempt and rejection transitions, or cleanup terminal state.

The current authority's 161 unattested rows and eight adapter-only rows make an all-registry candidate pool invalid for normalized probability claims.

The outer `poolComplete=true` receipt must not be interpreted as `all runtime packages available`.

The decision, mission, focus, and strategy pools are also runtime-dependent and were not complete in a current named evaluation.

No uncertain-input distributions, seed, cadence manifest, or complete custom-pool sequence state were declared.

## Findings by required risk class

### AI validity and dead choices

The current MCP evidence does not prove that any package, decision, mission, focus, or strategy factor is live, dead, hidden, route-compatible, or target-valid under a real campaign fixture.

The source gates are visible, but source-only gates are not a substitute for a typed MCP scenario.

### Dominance and starvation

No current dominance or starvation result is valid because the weighted evaluation timed out before runtime candidate eligibility and post-selection state were resolved.

The dated 2026-07-24 first-draw control shows region 01 dominance under its eight-package assumptions, but it is bounded historical context and not a current ranking claim.

Zero-weight outer regions are expected to be unselectable when their preparation helpers find no eligible package, but the current inspector did not evaluate those helpers under runtime state.

### Rank reversal

The planner recomputes novelty and prior-wave penalties on every draw, so rank reversals are possible as selected-region, selected-host, and prior-wave arrays change.

No `probability_sweep` result exists to identify a current threshold or reversal point.

### Repetition and sequence risk

The source carries selected-region, selected-host, and previous-wave memory, but no complete custom-pool manifest with cadence, removal, cooldown, reset, cap, and terminal state was supplied.

No `probability_sequence` or simulation result is claimed, so repetition rate and recovery behavior remain unresolved.

### Timing drift

The MTTH source has chaos-tier and network-density modifiers, but the current adapter did not produce an effective timing analysis.

No timing drift, burstiness, or cumulative evolution chance is claimed.

### Exploit and snowball risk

The 2026-08-20 owner patch prevents unattested candidates from receiving the minimum positive weight before reservation rejection.

The remaining high-impact risk is contract ambiguity: the pool-exhaustion fallback can commit a smaller wave while the tuning matrix names a fixed target ladder.

No unsafe patron, league, host, or package snowball was proven without a current strategy and sequence evaluation.

## MCP blockers and exact routes

The first malformed probability source attempts used `relativePath`, adapter-only input, and a source string.

The exact errors were `Unrecognized key: "relativePath" at source`, `An adapter requires a source; provide a source alone to discover compatible adapters`, and `Invalid input: expected object, received string at source`.

The accepted source shape was `{path:"common/..."}`.

The current allocator inspect then succeeded with adapter `random_list` and the artifact recorded above.

The current allocator evaluate timed out with `tool call failed for hoi4_agent_tools/hoi4.probability_evaluate` and `timed out awaiting tools/call after 180s`.

A line-scoped allocator probability inspect retried after that evaluate and timed out with the same 180-second error.

A current shared decision probability inspect retried after that and timed out with the same 180-second error.

The required event structural route first rejected a missing selector kind with `Invalid discriminator value. Expected 'event' | 'namespace' | 'file' | 'source' | 'node' | 'manifest' at selector.kind`.

The corrected selector `{kind:"event",eventId:"chaosx.nr6.1"}` reached the route but timed out after 180 seconds.

The required focus structural inspect on `common/national_focus/006_independence_wave_focus.txt` also timed out after 180 seconds.

Because event and focus inspect did not return source-linked graphs, `hoi4.event_render` and `hoi4.focus_render` were not run; no structural render artifact is claimed.

The current transport state therefore prevented valid current `probability_evaluate`, `probability_sweep`, `probability_simulate`, `probability_sequence`, `probability_compare`, `probability_render`, event render, and focus render evidence.

No source-only arithmetic was substituted for any timed-out MCP result.

## Required owner follow-up

1. The allocator owner must resolve the exact-count contract at `common/scripted_effects/006_independence_wave_package_allocator_effects.txt:124-142` by failing closed for short pools or by explicitly accepting and documenting partial waves in the tuning and acceptance matrices.

2. The central package-admission owner must complete or deliberately retain fail-closed status for the 161 unattested rows and supply a complete typed runtime package fixture before any ten-country band probability is claimed.

3. The probability-audit owner must restore the MCP route and rerun the exact scenario set `E6_ALLOCATOR_BANDS_CURRENT_2026_08_22` with the same 14-entry candidate pool and a declared package, host, patron, league, reservation, and prior-wave state.

4. The same restored route must inspect and evaluate the shared event-option, decision, mission, focus, strategy, and MTTH surfaces using named fixtures from the accepted matrices, then render ranking, matrix, waterfall, timing, sensitivity, and unresolved evidence where supported.

5. A future owner-applied weighted patch requires `hoi4.probability_compare` on the same named scenarios against a recorded pre-change revision; this audit has no valid before/after compare.

## Skipped analyses and uncertainty

No current exact band probability is reported because the evaluator timed out.

No package-level probability is reported because the inner dynamic pool and external factors were incomplete.

No focus selection probability is reported because focus AI is a score race and the available pool was unresolved.

No decision or mission click probability is reported because those values are willingness scores and the current candidate pools were incomplete.

No strategy-factor probability is reported because strategy factors are additive scores and the current inspect route timed out.

No MTTH timing is reported because the dated adapter discovery found no weighted surface and the current timing route did not produce a scenario result.

No rank reversal, repetition, timing, or sequence result is reported because sweep, simulation, and sequence calls require complete declared inputs that were not available.

No whole-event acceptance claim is made.

No simplification or gameplay fallback was applied.
