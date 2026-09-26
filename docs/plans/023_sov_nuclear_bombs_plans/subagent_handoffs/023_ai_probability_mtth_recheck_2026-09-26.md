# Event 23 MTTH scenario recheck

Status: MCP timing conclusion unresolved; source base-value correction verified.

Audit date: 2026-09-26.

This is a read-only recheck of Event 23 Evolution III timing for `P23_EVO3_MAJOR_RIVAL_NORMAL` and `P23_EVO3_ENEMY_USE_ACCELERATED`; no other probability scenarios were submitted.

The only file written by this task is this handoff; no source, specification, workbook, asset, or other documentation file was edited, and no commit was created.

No timing value was changed or recommended for change, consistent with the user's explicit “Defer tuning” direction.

## Correction and source basis

`docs/specs/023_sov_nuclear_bombs_specs/023_sov_nuclear_bombs_spec_part_5_evolutions_and_exchange.md:162` recommends a 180-day Evolution III base; line 214 recommends a 90-day Evolution IV base.

The current constants at `common/script_constants/023_sov_nuclear_bombs_constants.txt:510-513` are Evolution I 120, Evolution II 120, Evolution III 180, and Evolution IV 90 days.

The corresponding MTTH entries in `common/mtth/023_sov_nuclear_bombs_mtth.txt:10-42` use those constants, so Evolution III's current 180-day base matches the Part 5 design center and Evolution IV owns the 90-day base.

The prior probability resume, `docs/plans/023_sov_nuclear_bombs_plans/023_ai_probability_auditor_resume_2026-09-25.md:13`, explicitly corrects an earlier parent report that attributed Evolution IV's 90-day value to Evolution III; this recheck confirms that correction from both the specification and current source.

The named scenario prose is at `docs/specs/023_sov_nuclear_bombs_specs/023_sov_nuclear_bombs_probability_scenarios.md:110-134`.

## Workspace and source identities

Workspace Git HEAD at audit start: `3769251aecd159bcfd191aac5eabf11188308d10`.

The following SHA-256 values identify the physical files read from the current Windows workspace; they are not MCP source revisions.

| File | Physical SHA-256 |
|---|---|
| `docs/specs/023_sov_nuclear_bombs_specs/023_sov_nuclear_bombs_probability_scenarios.md` | `B2DC932928C132FE7F16F78A51F44F4A1B45DCA8FEF34FE73E052CEFC92B9D65` |
| `docs/specs/023_sov_nuclear_bombs_specs/023_sov_nuclear_bombs_spec_part_5_evolutions_and_exchange.md` | `DE1D5A9336F8CFDDFAD8924591B4119A72C499F765C8F7966BE9D13D13B2F434` |
| `common/mtth/023_sov_nuclear_bombs_mtth.txt` | `DCB60B1AE6F08C09B0E3D22E9E2442432EB424E3ED2BB103517F0DF3BBD1DE09` |
| `common/script_constants/023_sov_nuclear_bombs_constants.txt` | `073BC77FB14B4FC6D2CCF0CE8EC46939E96EE62DC9EE201B12C1A04F50F097CE` |
| `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt` | `C3F3BA0ACA7C5FEFE0B5BE84704ACE1C292BB146E32BADDA896FC2FA35D3FEB5` |
| `events/023_soviet_nukes.txt` (supplemental timer callback) | `AD7313D2E4AC1C0D78F96A45A70437892C57A224B1288B20792D6B5497B772EB` |
| `docs/plans/023_sov_nuclear_bombs_plans/023_ai_probability_auditor_resume_2026-09-25.md` | `21DA8DA3159E2F57C489CCFB0B570DB05286A99547FACB8406FDDE23D96A1E18` |

The previous detailed handoff `docs/plans/023_sov_nuclear_bombs_plans/subagent_handoffs/023_ai_probability_auditor_current.md` has physical SHA-256 `9C206545764D1CDCA04F924DE732F81F560C52C4D712195041BB07FE04E4C71A`; it is dated 2026-09-05 and describes older 180/240/300/360-day bases, so it is historical evidence rather than current timing evidence.

## Surfaces and source trace

Analyzed surface: Event 23's actor-scoped Evolution III interval, `sov_nuclear_bombs_evolution_iii_interval`, consumed by `sov_nuclear_bombs_schedule_evolution_check`.

Scenario IDs: `P23_EVO3_MAJOR_RIVAL_NORMAL` and `P23_EVO3_ENEMY_USE_ACCELERATED`.

Exact current base: `constant:sov_nuclear_bombs_mtth.evolution_iii_days` = 180 days.

The Event 23 MTTH source declares these Evolution III modifiers and current factors:

| Source condition | Constant | Current factor | Scenario input status |
|---|---|---:|---|
| `has_global_flag = sov_nuclear_bombs_major_exchange_active` | `sov_nuclear_bombs_mtth_factor.major_exchange_acceleration` | 0.60 | Not bound in either submitted scenario. |
| `has_country_flag = sov_nuclear_bombs_confirmed_enemy_nuclear_use` | `sov_nuclear_bombs_mtth_factor.serious_crisis_acceleration` | 0.65 | Stated in the accelerated scenario, but not supplied as a typed actor flag. |
| `has_war = yes` | `sov_nuclear_bombs_mtth_factor.war_acceleration` | 0.85 | War state was not bound; the normal case says stable peace, while the accelerated case inherits it and adds confirmed use. |
| `sov_nuclear_bombs_integrity < 40` | `sov_nuclear_bombs_mtth_factor.low_integrity_delay` | 1.35 | Both prose cases specify Integrity 80; this value was not bound to an adapter campaign variable. |
| `has_country_flag = sov_nuclear_bombs_atomic_moratorium` | `sov_nuclear_bombs_mtth_factor.moratorium_delay` | 1.50 | Neither named case declares moratorium state. |

These are source-declared operands, not an MCP modifier trace; no effective interval was calculated by hand.

The caller at `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:517-565` selects the next stage from `sov_nuclear_bombs_evolution_stage`, stores the `mtth:` result in `sov_nuclear_bombs_evolution_timing_delay`, and schedules hidden country event `chaosx.nr23.180` with `days = sov_nuclear_bombs_evolution_timing_delay`.

The event callback at `events/023_soviet_nukes.txt:63-76` clears the active timer and calls `sov_nuclear_bombs_try_evolution_progression`; that progression effect attempts the stage gates and then calls the scheduler again at `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:1716-1767`.

Accordingly, the `common/mtth` block is a scalar interval calculator at this call site; it is passed as a scheduled `country_event` delay, not used as an event's `mean_time_to_happen` daily hazard or as a probability-proportional selection weight.

The current caller permits one active timing event per Soviet actor and does not show a resampling path while that timer is active; any later external-factor change or early emergency path would require separate callback evidence and is not established by the requested probability analysis.

Evolution III's additional eligibility gate is separate from this interval; the scenario design requires Evolution II and either two operational nuclear majors or one of the specified active exchange/confirmed-strike conditions.

## Scenario inputs and completeness

The live probability route's JSON schema leaves `scenarioSet` typed as `unknown`; the repository's `chaos-redux-subagents` skill documents the currently accepted shape as `{ id, scenarios: [{ id, actor, state, flags, scopes }] }`, with each scope `{ id, state }`.

The evaluation used the exact two requested scenario IDs, actor `SOV` (the Event 23 actor), empty primitive `state`, empty `flags`, and empty `scopes`; no scenario-specific fields, variables, scopes, flags, war relations, or operational-major bindings were invented.

`P23_EVO3_MAJOR_RIVAL_NORMAL` prose declares Chaos 850, Evolution II active, two operational nuclear majors, stable peace, hotline available, Readiness 75, and Integrity 80; those values and relationships were not represented in the submitted state maps.

`P23_EVO3_ENEMY_USE_ACCELERATED` inherits that prose and adds confirmed enemy nuclear use against Soviet territory; that condition was not represented by the source flag in the submitted state maps.

Candidate-pool completeness is not applicable to this single-stage timer surface; the inspector found zero indexed candidates, so there is no normalized selection race or probability pool to report.

External-factor completeness is incomplete for both scenarios, including the moratorium flag, major-exchange flag, war status, nuclear-major operational state, world-gate state, and the typed country-variable context.

No scheduled state changes, uncertainty distributions, seed, observation horizon, or cumulative-stage start time were declared; cumulative timing from earlier stages or across later state changes is therefore not specified.

## Live MCP evidence

The live tool metadata exposed the read-only probability routes with these relevant signatures:

```text
hoi4.probability_inspect({ adapter?: Adapter, candidatePool?: string[], customPoolManifest?: unknown, refresh?: boolean, source?: unknown, workspaceId?: string })
hoi4.probability_evaluate({ acceptanceBands?: unknown, adapter?: Adapter, candidatePool?: string[], customPoolManifest?: unknown, diagnosticThresholds?: unknown, horizonDays?: number, metrics?: Metric[], outputs?: Output[], refresh?: boolean, scenarioSet: unknown, source?: unknown, workspaceId?: string })
hoi4.probability_render({ analysisId: string, expectedScenarioHash?: string, filter?: unknown, includeHtml?: boolean, outputs: Output[], workspaceId?: string })
```

`Adapter` included `event_mean_time_to_happen`, `event_option_ai_chance`, `decision_ai_will_do`, `mission_ai_will_do`, `national_focus_ai_will_do`, `technology_ai_will_do`, `doctrine_ai_will_do`, `direct_random`, `random_list`, `ai_strategy_factor`, and `custom_weighted_pool`.

`Metric` included `conditional_probability`, `raw_value`, `cumulative_chance`, and `effective_mtth_days`; `Output` included `json`, `ranking`, `matrix`, `waterfall`, `timing`, `sensitivity`, `threshold`, `sequence`, `comparison`, and `unresolved`.

The `chaos-redux-subagents` source contract documents `source: { path: "mod/relative/source.txt" }` for inspect/evaluate; this audit used `{ path: "common/mtth/023_sov_nuclear_bombs_mtth.txt" }`.

### Required first call: `hoi4.probability_inspect`

Exact request: adapter `event_mean_time_to_happen`, source path `common/mtth/023_sov_nuclear_bombs_mtth.txt`, and `refresh: true`.

Result: `status=ok`, code `PROBABILITY_SOURCE_DISCOVERED`, discovery reason `no_weighted_surfaces`, candidates 0, available candidates 0, required inputs 0, unresolved 0, and no blockers.

MCP workspace ID: `mod_chaos_redux_ea3b2d67c2c0`.

MCP source revision: `ea4669159bc268bcacb07b26a88c4b151990475a45248e401b6d1d6fd5936617`.

MCP source hash: `89b364cff8d70ba8114832f89e206c5a9f69ec8c28635880207ea785515f596c`; this is the adapter's reported hash and is distinct from the physical file SHA-256 above.

Inspect artifact URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9d565d9a62333e9afcdeca0685e85949181e894a33ee814a3fdbd5a15d2ea360/1945e5cfdd85c12179c98f4918c43e076d3526625fda1c2b96b4ecb50eb7aa42/probability-inspect-89b364cff8d7.json`.

### Named-scenario `hoi4.probability_evaluate` attempt

Exact request metrics were `effective_mtth_days` and `cumulative_chance`, with outputs `json`, `timing`, and `unresolved`, `refresh: true`, and source path `common/mtth/023_sov_nuclear_bombs_mtth.txt`.

The `scenarioSet` ID was `P23_EVO3_MTTH_RECHECK_2026-09-26`, and its only scenarios were `P23_EVO3_MAJOR_RIVAL_NORMAL` and `P23_EVO3_ENEMY_USE_ACCELERATED`, each with actor `SOV`, `state: {}`, `flags: []`, and `scopes: {}`.

Result: `status=error`, code `PROBABILITY_SURFACE_EMPTY`, `isError=true`, no files scanned, no diagnostics, no artifacts, no analysis ID, and no scenario hash.

Exact blocker message: `No weighted blocks matched this request`.

Blocker details: requested adapter `event_mean_time_to_happen`, source `{ path: "common/mtth/023_sov_nuclear_bombs_mtth.txt" }`, empty `candidatePool`, and empty `availableAdapters`.

The source revision/hash from inspection remains the only MCP identity for the weighted source; evaluation returned no source revision, scenario hash, or artifact URI.

## Structural event MCP evidence

`hoi4.event_inspect` was called read-only with mode `scan`, selector `{ kind: "event", eventId: "chaosx.nr23.180" }`, downstream direction, helper expansion disabled, depth 2, and refresh enabled.

It returned `EVENT_INSPECTED_PARTIAL`, workspace ID `mod_chaos_redux_ea3b2d67c2c0`, graph revision `d01913b64aa300696a2ca2ae195c93aa80c3017ed3c095ac145626724dca3b01`, graph hash `50324192d13f20ddba8b180fd0f1dd87bd7cf7fba4142af2d1ac486fdbda7316`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7208df92f2c7fb5370ab2ebfe8a637719bf6396b0b740d5da8553d924459b453/11b3387377a777023fc7fb1300c97d116e0286572a4c9ecbd1f08f5c5c152553/event-scan-d01913b64aa3.json`.

The focused scan deferred workspace-wide helper/lifecycle passes; counts were workspace-wide, and the inline source inventory was limited to 64 of 384 paths.

`hoi4.event_render` was called with view `timing` and the same event selector and boundary.

It returned `EVENT_RENDERED_PARTIAL`, graph revision `60d7bb069cf4775966ed1d430b161f4789d7de3f3784d2498cfa95def6ac54b8`, graph hash `f23b9d50107bf08726e0adb7041010a015574c496828940bde71067286de654f`, layout hash `cb2c55195ec96915e60d93cc54311a2211c0a5187c2b6d4fb452fbb69f8d4318`, `selectedNodes=0`, and `omittedNodes=42861`.

The timing render artifacts are preserved here: manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/19f4ee40c9d40d185f954c2b24b69f6d8b261e0e9df57fc86e0d83d7919e8fa2/6e1edcd07a5115f2b5f35409bb7e89700a596c3d063a49d1b5f16a2c07eb6c32/event-timing-60d7bb069cf4-manifest.json`, JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c6c5702de70ee938dbaa66b1ec42f6dd7a055fe4daf3f85cb5af872ebded93f6/3826ddc6839294e0a52a7e577bd449b2cc1dbbfc3e5792a44ae44f00818afab8/event-timing-60d7bb069cf4.json`, SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a9b1fe1b46e4a125c35ac842f1da3a83aa94f055eb70952fe938f72bb079cf9f/f91edbcafd3674ec7e3cb2349ca6289e723cce5f2d59e165f7007655a547efda/event-timing-60d7bb069cf4.svg`, PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dfabfac5f04d455990fb9f54ae9f1a95f8fec4e53a4b28b8183b7fdcfc1c0ba9/9bab00d2c9d586fd0cf106e3959dc123259d16635aa90f2dd789ac3d70f0f857/event-timing-60d7bb069cf4.png`, and HTML `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f8e20cc64ee1679108ab8b063af12d24b983d407bf0f0d12fa8875f724edbc58/6323710fc2de6a741c3db66e0c8ad83e4823119ef60d826c90ce67f3b27c5b5f/event-timing-60d7bb069cf4.html`.

Because the event timing render selected zero nodes, it is retained as a partial-route artifact and is not evidence that the Event 23 timer callback or eligibility gates were structurally resolved.

## Findings and classifications

| Claim | Classification | Evidence and limit |
|---|---|---|
| Evolution III base is 180 days and Evolution IV base is 90 days. | Exact source fact. | Current constants and both Part 5 recommendations agree. |
| `P23_EVO3_MAJOR_RIVAL_NORMAL` effective interval. | Unresolved. | Adapter indexed no MTTH surface; its state and external flags were not bound. |
| `P23_EVO3_ENEMY_USE_ACCELERATED` effective interval. | Unresolved. | Confirmed-use prose maps to a source modifier, but the adapter indexed no surface and no typed flag was supplied. |
| Cumulative chance or cumulative time across successive evolutions. | Unresolved. | No analysis ID, horizon, state-transition schedule, or cumulative history was accepted by the adapter. |
| Candidate ranking, dominance, starvation, or rank reversal. | Not applicable to this scalar timer; no pool was indexed. | No weighted candidate race was available. |
| Timer repetition and cadence. | Bounded source observation only. | Timer callback retries progression and the effect schedules again; no MCP lifecycle or sequence result quantifies repetition. |
| Sampled timing. | Not evaluated. | No uncertain-input distributions or seed were declared, and the source surface was empty. |

No exact or bounded effective interval, cumulative probability, threshold, rank, or modifier waterfall is claimed.

## Skipped analyses, blockers, and recommendations

`hoi4.probability_sweep` was not called because no numeric sweep axis or threshold range is defined in the named scenario inputs, the MTTH inspect found no surface, and the user deferred tuning.

`hoi4.probability_simulate` was not called because no uncertain-input distributions, correlation model, sample count, or seed was declared.

`hoi4.probability_sequence` was not called because this is a scalar MTTH-backed scheduled-event chain rather than a complete declared custom weighted pool; no cadence/state-transition manifest was supplied.

`hoi4.probability_compare` was not called because this audit made no before/after source change and no candidate comparison was requested.

`hoi4.probability_render` could not be called with a valid request because its live schema requires an `analysisId`, and the failed evaluation returned none; no scenario hash exists for an expected-hash render either.

No timing-value fix is recommended; retain the current 120/120/180/90-day bases pending an authorized tuning decision.

For future MCP evidence, the concrete tooling gap is support for indexing `common/mtth` entries reached through `mtth:` references in `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:530-554`, together with typed actor-variable, flag, scope, war, and scheduled-state inputs for the existing named scenarios.

Do not claim effective or cumulative timing from the source operands alone; the adapter proved discovery of the file but did not analyze its interval entries.

## Skills and documentation consulted

Read completely: `.agents/skills/chaos-redux-mtth/SKILL.md` and `.agents/skills/chaos-redux-subagents/SKILL.md`.

Consulted the offline Paradox wiki core pages, including the Data Structures MTTH variable section, AI Modding MTTH blocks, Event Modding timing semantics, and Effects event scheduling, alongside the required Triggers, Modifiers, Localisation, Scopes, On actions, Decision Modding, and Idea Modding pages.

Consulted installed vanilla `script_concept_documentation.md`, `common/script_constants/documentation.md`, and the `country_event`/`set_variable` entries in `documentation/effects_documentation.md`; the event documentation confirms that a supplied `days` value schedules the country event.

No skill was created or updated.
