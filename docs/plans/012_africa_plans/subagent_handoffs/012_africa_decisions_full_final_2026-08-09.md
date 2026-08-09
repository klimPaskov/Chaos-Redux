# Event 012 decisions and missions final audit handoff

Date: 2026-08-09

Owner: `chaosx_decision_mission_auditor` (`/root/event12_decisions_full_final`)

Scope: Event 012 decision and mission surfaces, shared action kernels, proof missions, RSA and priority-member support, natural-disaster calls, Scramble response, world-order and constitutional decision paths, costs, requirements, AI routes, cleanup, localisation, and every-country scan classification.

Explicit exclusions: Actions 71–76 (`contain_emergent_disease`, `research_disease_countermeasure`, `weaponise_fictional_pathogen`, `awaken_stone_cohort`, `train_gorilla_heavy_infantry`, `organise_pan_sappers`) and all GUI layout work.

No gameplay source patch was made in this pass because the two high-severity scan findings require an architectural choice and the shared action file is concurrently owned by the Action 71–76 workstream.

## Executive findings sorted by severity

### High: recurring whole-world roster scans are reached from recurring AI decisions

`common/decisions/012_africa_decisions.txt:10-16` re-enables `africa_ai_run_profiled_late_action_cycle` every `constant:africa_ai_controller.cycle_days` (14 days; `common/script_constants/012_africa_ai_constants.txt:136`).

The early branch of `common/scripted_effects/012_africa_ai_profile_effects.txt:3344-3359` calls `africa_refresh_bounded_african_target_roster` and `africa_refresh_bounded_external_target_roster`, which each execute `every_country` at `common/scripted_effects/012_africa_effects.txt:746-780`.

The two arrays are capped by `africa_has_selected_target_capacity` and the 5/9/16 selected-target caps (`common/script_constants/012_africa_constants.txt:430-435`), but the country iteration itself is not capped and repeats for every eligible AI host every 14 days.

Player decisions `africa_refresh_african_contacts` and `africa_refresh_external_crisis_targets` (`common/decisions/012_africa_decisions.txt:58-65,119-125`) are valid one-shot refreshes, but the same helpers are not one-shot when called by the AI controller.

Recommended owner fix: split the player refresh helper from an AI roster-consumption path, or make the AI path consume a previously frozen roster and refresh only when the host overlay, phase, or roster generation changes; then run a before/after `decision_ai_will_do` probability comparison under the same AI scenarios.

### High: priority-member natural-disaster AI refresh has an uncapped hostile array

`common/decisions/012_africa_decisions.txt:1679-1685` re-enables `africa_priority_member_natural_disaster_ai_cycle` every `constant:africa_natural_disaster.cooldown_days` (180 days; `common/script_constants/012_africa_action_constants.txt:786-792`) and calls `africa_priority_member_run_natural_disaster_ai_action` (`common/scripted_effects/012_africa_action_effects.txt:2836-2860`).

That effect calls `africa_refresh_priority_member_natural_disaster_targets` (`common/scripted_effects/012_africa_action_effects.txt:2759-2767`), which scans every country and appends every valid target to `africa_natural_disaster_enemy_targets` without an array-size guard before `random_scope_in_array` selects one.

The player refresh decision at `common/decisions/012_africa_decisions.txt:1629-1636` is bounded by explicit use, but the recurring AI route is a whole-world scan and can grow an unbounded array.

Recommended owner fix: add a named natural-disaster target-roster cap and a `ROOT` array-count limit in the scan, then prefer a reusable frozen roster or a bounded weighted pool for the recurring AI path; keep the 180-day cooldown and run probability/sequence evidence after the patch.

### Medium: shared mission timeout uses a host-scoped `FROM` variable without a vanilla precedent

The four shared missions use `days_mission_timeout = FROM.africa_active_action_duration_days` (`common/decisions/012_africa_decisions.txt:488-566`).

The offline Paradox wiki permits scoped variable references and dual scopes (`paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, Event targets and scoped variables sections), while installed vanilla documentation defines dynamic mission timeout fields (`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/dynamic_variables_documentation.md:238-239`).

Vanilla precedents found in `common/decisions/CHI_decisions.txt:5438,6454,6582` use country-prefixed variables or `var:` rather than `FROM.` in this field.

The Event MCP source lint accepted the current source with no blocking diagnostics, and the decision source is parseable, but no engine/runtime evidence proves that a `FROM.` expression is evaluated as the targeted mission owner in every duration-band case.

Recommended owner action: prove the targeted mission in a live test or an engine-backed targeted mission fixture; if the engine rejects the expression, copy the duration to a target-scoped normal variable and use the documented `var:` form rather than replacing it with a host variable that would desynchronise concurrent records.

### Medium: cancellation is state-safe but does not emit the normal result event

`africa_cancel_action` (`common/scripted_effects/012_africa_action_effects.txt:8591-8608`) records the cancelled outcome, applies confidence cleanup, resolves first-proof bookkeeping, clears the action ledger, and retries pending focus routes.

Unlike `africa_resolve_action` (`common/scripted_effects/012_africa_action_effects.txt:8457-8482`), it does not fire `chaosx.nr12.220`; therefore cancellation is localised through `GetAfricaLastActionOutcome` but does not produce the standard result popup/event-log entry.

This may be intentional for host shutdown or target capitulation, but the parent should decide whether every cancelled operation needs a ledger row or a compact cancellation event before claiming full player-facing lifecycle parity.

### Medium: probability coverage is source-complete for decision weights but not exhaustive pool proof

The direct probability adapter inspected `common/decisions/012_africa_decisions.txt` with source revision `8dc8ed923c6df4ed018b98f8a5cf3ebf37b78df96807f20d98db4ee5cb237df2`, 207 candidates, 23 required inputs, and zero unresolved inputs, but `poolComplete=false`.

The direct mission adapter returned `PROBABILITY_SURFACE_EMPTY` for the main Event 012 decision file because the shared missions have no `mission_ai_will_do` blocks; the controller decision is their AI equivalent.

RSA decision and mission adapters both resolved (`6` and `1` candidates respectively) with zero unresolved inputs, and the priority-member decision adapter resolved `54` candidates with zero unresolved inputs; no balance patch was applied, so no before/after comparison was required.

The requested `chaosx_ai_probability_auditor` subagent could not initialise because the required `meshy` MCP server timed out waiting for `tools/list` after 120 seconds; direct HOI4 probability evidence is recorded here instead.

## Coverage and structural proof

The source matrix `docs/specs/012_africa_specs/matrices/012_africa_decision_mission_matrix.csv` contains exactly 102 action concepts across 14 families.

Family counts are Protection 10, Accession 10, Regional congress 10, Integration 10, Economy 10, Diaspora 8, Rival blocs 8, High chaos 10, Scramble response 8, World order 8, Constitutional route crises 7, Host opening 1, Regional congress and restorations 1, and Post-unification governance 1.

The decision source has 102 unique action selector references matching the 102 matrix keys, plus eight non-action target/helper selectors; no matrix key is missing from the selector source and no action reference is absent from the matrix.

The six excluded Action 71–76 references are present in the complete registry but are not included in this audit’s semantic conclusions.

`africa_prepare_action_profile` and `africa_prepare_action_contract` cover all 102 action IDs; `africa_validate_action_specific_requirements` has numbered requirements through Action 102 and is called before payment and record creation (`common/scripted_effects/012_africa_action_effects.txt:2996-4210,4545`).

`africa_record_action_full_disposition`, `africa_record_action_partial_disposition`, and `africa_record_action_failure_disposition` each carry all 102 action IDs (`common/scripted_effects/012_africa_action_effects.txt:4616,5132,5647`), while the three semantic dispatchers are called from the shared resolver (`common/scripted_effects/012_africa_action_effects.txt:8253-8304`).

All 102 matrix rows have non-empty AI and cleanup fields; this is design coverage, not proof that every action has an independent AI score block.

## Shared action lifecycle

Selectors are quote selectors and intentionally use `cost = 0`; they set `africa_requested_action_id` and call `africa_select_action_for_quote`.

`africa_compute_action_quote` (`common/scripted_effects/012_africa_action_effects.txt:2543-2672`) derives political power, command power, manpower, equipment, trains, convoys, fuel, civilian capacity, intelligence, stability, and war-support costs from profile flags and target state, then scales them by target factories and states, selected-state count, integration burden, colonial pressure, active-action count, target confidence, overlay and constitution discounts, access, war risk, and a clamped multiplier before rounding.

`africa_begin_quoted_action_against_target` validates host, phase, action capacity, target capacity, target-specific requirements, diaspora gates, and all dynamic resource gates before paying and creating the generation-safe record.

The record stores action id, family, kernel, status, outcome, action and host generation, duration band and days, response days, objective, risk, target mode, all resource costs, and state-project locks (`common/scripted_effects/012_africa_action_effects.txt:4400-4550`).

Instant actions resolve immediately; timed actions activate one of four shared duration-band missions.

Full, partial, failure, timeout, and cancellation branches all converge on cleanup, with the response event at `events/012_african_union.txt:120-196` offering full, partial, and failure outcomes and calling the same resolver.

`africa_cleanup_action` is idempotent and removes the exact mission, diaspora state, disease receipts where applicable, natural-disaster reserve and cooldown state, active target arrays, civilian/intelligence capacity, state locks, active flags, generation variables, costs, and target cooldowns (`common/scripted_effects/012_africa_action_effects.txt:8339-8454`).

The active-action caps are 2 during opening, 3 during charter, and 5 during continental operation; selected-target caps are 5, 9, and 16 (`common/script_constants/012_africa_constants.txt:430-435`).

## Decision category lifecycle notes

Protection, Accession, Regional congress, Integration, Economy, Diaspora, Rival blocs, and High chaos actions use the shared quote, payment, four-mission, disposition, and cleanup kernel, with family-specific semantic dispatch and target validators.

Diaspora actions additionally open and close diaspora return, passage, housing, technical-mission, veterans, investment, citizenship, and evacuation ledgers through `africa_diaspora_*` helpers called from create, outcome, cancellation, and cleanup paths.

Priority-member natural-disaster actions use caller-side political-power and command-power reserves (`35` and `10`), the shared Event 012 action record, and Event 013 as the authoritative weather result; the AI path is the uncapped recurring scan finding above.

Scramble response has eight matrix selectors and four phase-window missions at `common/decisions/012_africa_decisions.txt:1916-1977`; recognition, coalition, intervention, and aftermath timers use named constants, phase-gated activation, phase-change cancellation, and timeout transitions.

World order has eight matrix actions plus world-package, sponsorship, and obligation surfaces; sponsorship obligations use named constant timers and default-mode timeout effects (`common/decisions/012_africa_decisions.txt:2404-2478,2545-2579`).

World polity package constituent decisions are guarded by package actor and target flags, and package foundation census is one-shot per installed package (`common/scripted_effects/012_africa_world_order_effects.txt:1455-1665`).

Constitutional route crises have seven host-specific actions with constitution, pending-route, member, and obligation flags; host opening recovery and post-unification governance each have one matrix action with dedicated phase and pending-proof gates.

RSA has a separate civil-war first-proof mission and ledger; priority-member withdrawal has a separate non-selectable timed mission; neither bypasses shared cleanup in their own systems.

## Mission quality notes

| Mission | Owner/category/region | Requirement and duration | Success | Failure/cancel/cleanup | Duplicate risk |
| --- | --- | --- | --- | --- | --- |
| `mission_africa_action_short`, `medium`, `long`, `epic` | Current Event 012 host; shared action category; active target array | Current host plus matching duration flag; dynamic `FROM.africa_active_action_duration_days` (short 60, medium 120, long 240, epic 540 defaults with per-action min/max ranges) | Objective completion calls `africa_resolve_action`; offer-response timeout opens `chaosx.nr12.210` | Event inactive, generation mismatch, target capitulation/non-existence, or timeout call `africa_cancel_action`/`africa_timeout_current_action`; cleanup removes exact mission and ledger | Active flag, generation equality, target array, and action cap prevent duplicate records; timer expression remains runtime-unproven |
| `mission_africa_complete_continental_peace_exemption` | Current host; member peace-exemption array; continental region | Active member flag and current host generation; `var:africa_peace_exemption_days` | Hidden completion is represented by the close helper when terms are complete | Event close, completion, breach, or generation mismatch calls `africa_close_continental_peace_exemption` | `fire_only_once = no` is intentional for repeatable member slots, but generation and active flags must remain current |
| `africa_rsa_first_proof_mission` | RSA coalition; bounded African target roster; South Africa civil-war corridor | `var:africa_rsa_first_proof_days`, seeded by `africa_rsa_initialize_defaults`; corridor secure tooltip | `africa_rsa_complete_civil_war_first_proof` | Civil-war inactive, coalition invalid, cancel, or timeout calls `africa_rsa_fail_civil_war_first_proof`; cleanup removes mission and clears `africa_rsa_first_proof_days` | Ledger-active flag and cleanup guard prevent duplicate proof missions |
| `africa_priority_member_withdrawal_mission` | Priority member package; member relationship | Package installed, withdrawal flag, and leaving/rival relationship; `constant:africa_priority_member_duration.withdrawal_days` | Timeout calls peaceful withdrawal completion | Relationship/flag loss cancels and runs withdrawal cleanup | `allowed = always no` and `selectable_mission = no` make it system-owned; no independent AI score is required |
| Scramble recognition/coalition/intervention/aftermath windows | Africa host; Scramble response phases | Phase-gated activation; named recognition, coalition, intervention, and aftermath constants | Timeout advances phase, launches unresolved expedition, ratifies/closes docket, or prolongs aftermath | Phase change cancels current window | One window per phase transition; phase flags prevent overlapping windows |
| Sponsorship obligation timers | Africa host and package target; world-order category | Target obligation flag and named obligation constant | Player or AI fulfils obligation before timeout | World end or obligation no longer due cancels; timeout defaults current mode | One obligation flag and target-array mission per mode; target checks prevent stale timers |

## Cost and requirement clarity

The zero-cost selector layer is not a free action exploit because selectors only set the quote id; resource payment occurs in `africa_begin_quoted_action_against_target` after dynamic quote and all cost triggers pass.

The dynamic cost tooltip exposes the resource and capacity components, including natural-disaster caller reserve and duration contract; custom cost triggers cover host transfer, RSA, priority-member, natural-disaster, world sponsorship, and package protocols.

No passive political-power store or flat selector exchange was found in the in-scope action engine.

Potential clarity follow-up: the shared mission description says success, cancellation, or failure are handled, but cancellation has no result event; confirm whether a silent state-log entry is acceptable for the player-facing ledger.

## AI validity and route-lock notes

Action selectors intentionally have `ai_will_do = { base = 0 }`; the host controller and family-specific AI dispatchers choose actions after target refresh, profile registry, host-policy snapshots, and caps.

RSA decisions have explicit AI bases and neighbour/relationship modifiers; the RSA proof mission has an AI base even though it is system-activated.

Priority withdrawal has explicit departure AI on the recall decision, while its mission is system-owned and non-selectable; priority natural-disaster AI uses nature-power factors and the shared cost gate.

World and Scramble decision targets use target arrays and final target validators, and their AI bases are named constants rather than raw magic values.

The main decision probability adapter reports 207 weighted candidates with zero unresolved inputs but `poolComplete=false`; this is sufficient source inspection but not an exhaustive world-state balance proof.

## Localisation and tooltip gaps

All 102 `africa_select_<action>` keys and `_desc` keys are present in `localisation/english/012_african_union_l_english.yml` and related Event 012 localisation files.

Shared action mission names/descriptions, peace-exemption mission text, RSA proof text, priority withdrawal text, custom cost tooltips, and response-event option text are present.

`africa_action_outcome_cancelled` and the scripted localisation path for cancelled outcomes exist, so cancellation text is not missing; only the optional result-event/log emission remains unresolved.

## Every-country and random-country classification

| Source and lines | Effect and caller | Classification | Risk or required follow-up |
| --- | --- | --- | --- |
| `common/scripted_effects/012_africa_effects.txt:138-146` | `africa_build_prefire_contact_pool`, called by explicit pre-fire host selection | One-shot and bounded by the temporary pool and 3–5 frozen-contact limits | Safe as designed; not reached from periodic on_action |
| `common/scripted_effects/012_africa_effects.txt:247-265` | `africa_select_weighted_prefire_host`, explicit Event 012 pre-fire pass | One-shot host/candidate census | Safe as designed; candidate pool is temporary and cleared |
| `common/scripted_effects/012_africa_effects.txt:749-760` | `africa_refresh_bounded_african_target_roster`, player refresh at decisions 58–65, RSA proof setup, and AI cycle | Player/RSA calls are one-shot and capped at selected-target capacity; AI call is recurring every 14 days | High-risk recurring scan through `012_africa_ai_profile_effects.txt:3344-3359`; split or cache AI roster |
| `common/scripted_effects/012_africa_effects.txt:772-780` | `africa_refresh_bounded_external_target_roster`, player refresh at decisions 119–125 and AI cycle | Player call is one-shot and capped; AI call is recurring every 14 days | High-risk recurring scan through same AI cycle; split or cache AI roster |
| `common/scripted_effects/012_africa_action_effects.txt:2763-2767` | `africa_refresh_priority_member_natural_disaster_targets`, player refresh and 180-day priority-member AI cycle | Recurring whole-world AI scan; output array has no explicit cap | High risk; add a named cap and bounded AI roster or weighted pool |
| `common/scripted_effects/012_africa_world_order_effects.txt:29-32` | `africa_world_emit_super_event`, called only by four global-flagged super-event wrappers | One-shot per named super-event slot; loops human countries only to play current audio | Safe as designed; no recurring hook found |
| `common/scripted_effects/012_africa_world_order_effects.txt:848-894` | Two-pass Scramble participant census in `africa_initialize_scramble_and_world_packages` | One-shot post-unification census with `participant_census_cap = 32` | Safe as designed; guarded by initialization state and participant cap |
| `common/scripted_effects/012_africa_world_order_effects.txt:1500-1658` | Six continent branches in `africa_world_initialise_package_polity_foundation` | One-shot per installed package, guarded by `africa_world_package_polity_foundation_initialised` | Safe as designed; package install call sites are explicit and finite |
| `common/on_actions/012_africa_world_order_on_actions.txt:11-17` | `random_country` startup registration for Event 019 providers and strange-force manifests | One-shot startup random selection, not an every-country scan | Safe; RSA on_actions contain no every-country/random-country iteration |

All Event 012 `every_country` occurrences were classified above. The only recurring world iterations are the two AI target-roster calls and the priority-member natural-disaster AI refresh.

## MCP and evidence references

Event lint: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8676e4332dbc1c74d0926c3fa8ae17b9cc83cc5fd25ab7e4b749445f2784ccda/55965da5e3c991bae77cada658a3429a9a6b587083107b35852801004695cd92/event-lint-08357425bddf.json`.

Event timing render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d5727f0f31bcab956898237723824c23f7558f2c5c25ab71b2a145235a06b52c/4cbfaf6afe7b21b040fac58bf20a1665e83cf724b33a831ce901cfca516492dd/event-timing-08357425bddf-manifest.json`.

The Event MCP run is `EVENT_INSPECTED_PARTIAL`/`EVENT_RENDERED_PARTIAL` with zero blocking diagnostics; the workspace-wide report remains partial because helper projections were deferred and the inline source inventory is capped at 64 paths, so it is evidence rather than a complete gameplay proof.

Main decision probability: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8393755fe1d37e45d0b98e1af696a23efc627d0680ede8d78246e91831659f82/181e6fe667c3b908eee69e8386c5bdce8e6ec74f292b599403562fb06019f8de/probability-inspect-bcee97bbe394.json`.

Main mission adapter result: `PROBABILITY_SURFACE_EMPTY` for `mission_ai_will_do`; no artifact was emitted because no weighted mission blocks matched the main source.

RSA decision probability: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/68c3e04ae36cd7685649a9ce7969c041306fc3ec6c2556e85a56b436f1c68634/b2eda238675b8155df7fc5a8b1e78b65df62b308c557288710d60010c9bc318f/probability-inspect-829a22a730a3.json`.

RSA mission probability: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7ada2b5591e91afff33095e6df10b7f8df0d181a49667a84a158125dd655805a/a6b0adf2537e85c19777d7f3da7a7ed6470b438be37834b4e6242ba2121a7650/probability-inspect-829a22a730a3.json`.

Priority-member decision probability: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6562742759020d80cee6aa88e7b43759731fd7b47d9fbe951a6269a50ae39dc0/fc6dede21c6f72c036649f37bfcf180e2eaded457888b4412888208ce38fe244/probability-inspect-8c5b3a7eae78.json`.

## Validation and remaining work

Source review covered the required offline wiki pages, installed vanilla documentation and decision precedents, the Event 012 matrix, constants, decision files, scripted effects/triggers, event response code, RSA and priority-member files, localisation, and on_actions.

Automated structural checks confirmed 102 matrix rows, 102 unique action selector references, no missing matrix-selector mapping, no missing AI or cleanup fields, all 102 profile/validation/disposition action IDs, and all in-scope selector localisation keys and descriptions.

GUI inspection and rendering were intentionally skipped because the parent task excludes GUI layout and no decision-owned GUI patch is in scope.

Live gameplay and save-based validation were not run because agents must not launch Hearts of Iron IV; mission timeout expression and recurring-scan behaviour remain runtime/engine proof items.

No source simplification was introduced. The unresolved high-severity recurring scans, the `FROM.` mission timeout engine semantics, the optional cancellation result-event decision, and the incomplete `poolComplete=false` probability coverage must remain visible in the parent completion report.
