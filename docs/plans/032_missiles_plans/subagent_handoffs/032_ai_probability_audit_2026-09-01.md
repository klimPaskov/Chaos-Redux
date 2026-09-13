# Event 32 AI probability audit handoff

Disposition: superseded by the current `chaosx_ai_probability_auditor` handoffs. This file is retained as the historical pre-repair baseline and exact adapter-availability record; it must not be read as the final weighted-logic verdict. The current source state and same-scenario comparison evidence are recorded in the newer handoff paths and the Event 32 test ledger.

Date: 2026-09-01

Audit owner: `chaosx_ai_probability_auditor`

Scope: read-only weighted-logic audit of Event 32, rooted at `chaosx.nr32.1`.

Repository: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux`

## Executive result

The audit is not sufficient for an engine-backed balance or probability completion claim.

The mandatory first HOI4 MCP probability call was attempted before relying on source traces, but the installed route returned the exact blocker `MCP tool hoi4_agent_tools/hoi4.probability_inspect is not available to the model`.

Because `hoi4.probability_inspect` was unavailable, no probability evaluation, threshold sweep, same-scenario comparison, simulation, sequence analysis, or probability render could produce an artifact for this audit.

All engine-dependent conclusions below are therefore `unresolved`.

The source review still identifies concrete tuning and validity risks, but source inspection is not engine evidence and does not establish exact selection probabilities, normalized weights, timing distributions, or runtime candidate-pool completeness.

No gameplay, AI, event, focus, decision, mission, technology, doctrine, scripted logic, localisation, asset, spreadsheet, or runtime file was patched by this audit.

The only intended new repository artifact is this handoff.

## Required MCP workflow and blockers

### Probability workflow

The first probability call was:

```text
hoi4.probability_inspect
adapter = event_option_ai_chance
source = { eventId = chaosx.nr32.1 }
refresh = true
```

The exact response was:

```text
MCP tool `hoi4_agent_tools/hoi4.probability_inspect` is not available to the model
```

This is an exact MCP availability blocker, not an empty result and not evidence that Event 32 has no probability surface.

The requested prior references were preserved for a future rerun: baseline analysis `probability-57fedf8c2ca0972cbadd9612`, sweep `probability-9735d25129b2670c7d609392`, and baseline hash `ec4dc421`.

No scenario hash, MCP revision, analysis artifact URI, comparison id, rendered evidence URI, or sweep result was returned.

`hoi4.probability_evaluate`, `hoi4.probability_sweep`, `hoi4.probability_compare`, `hoi4.probability_render`, `hoi4.probability_simulate`, and `hoi4.probability_sequence` were not run because the mandatory inspect route was unavailable and no valid engine adapter response could be established.

The same-scenario comparison against `probability-57fedf8c2ca0972cbadd9612` and the requested sweep comparison against `probability-9735d25129b2670c7d609392` are therefore blocked for every scenario.

### Structural workflow

The required structural event inspection was also attempted for `chaosx.nr32.1`.

The exact callable-route failure was `TypeError: tools.mcp__hoi4_agent_tools__hoi4_event_inspect is not a function`.

No `hoi4.event_inspect` or `hoi4.event_render` artifact was produced.

Structural source review below is consequently a repository trace only and does not prove the parsed event graph.

### Sufficiency decision

Results are not sufficient for the requested probability audit sign-off.

The audit should be rerun with the probability and structural MCP routes restored, using the same scenario ids and the same baseline references recorded above.

## Inputs read

### Repository instructions and skills

The repository `AGENTS.md` was read first.

The following skills were read completely and applied:

- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `.agents/skills/chaos-redux-event-planning/SKILL.md`
- `.agents/skills/chaos-redux-mtth/SKILL.md`

The event-planning skill supplied the scenario-matrix discipline and the MTTH skill supplied the timing classification rules.

### Event 32 specification set

Every file under `docs/specs/032_missiles_specs/` was read:

- `README.md`
- `032_missiles_acceptance_criteria.md`
- `032_missiles_achievement_prompt.md`
- `032_missiles_asset_prompt.md`
- `032_missiles_coding_prompt.md`
- `032_missiles_decision_mission_prompt.md`
- `032_missiles_goal_prompt.md`
- `032_missiles_improvement_loop_closure.md`
- `032_missiles_package_manifest.md`
- `032_missiles_probability_scenario_matrix.md`
- `032_missiles_requirement_traceability.md`
- `032_missiles_research_notes.md`
- `032_missiles_source_review.md`
- `032_missiles_spec_part_1_core.md`
- `032_missiles_spec_part_2_program_and_launch_sites.md`
- `032_missiles_spec_part_3_operations_and_consequences.md`
- `032_missiles_spec_part_4_evolutions.md`
- `032_missiles_spec_part_5_decisions_missions_and_scenario.md`
- `032_missiles_spec_part_6_ai_and_probability.md`
- `032_missiles_spec_part_7_assets_text_and_achievements.md`
- `032_missiles_spec_part_8_implementation_contract.md`
- `032_missiles_system_connections.md`
- `032_missiles_test_matrix.md`

### Offline wiki and vanilla documentation

The required offline Paradox wiki core pages were read: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.

The relevant offline wiki evidence is that event `ai_chance` is probability-proportional, `ai_will_do` and MTTH-backed values are score-like rather than click probabilities, MTTH is a daily hazard, and `random_list` uses weights relative to the eligible list.

The vanilla documentation files read under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/` were `console_commands_documentation.md`, `dynamic_variables_documentation.md`, `effects_documentation.md`, `loc_formatter_documentation.md`, `loc_objects_documentation.md`, `modifiers_documentation.md`, `script_collection_input_documentation.md`, `script_collection_operator_documentation.md`, `script_concept_documentation.md`, `script_math_functions_documentation.md`, and `triggers_documentation.md`.

## Audited implementation surfaces

The following current source files and identifiers were traced without editing them:

| Surface | Source files and identifiers | Static role |
| --- | --- | --- |
| Event root and option races | `events/032_missile_crisis.txt`; `chaosx.nr32.1`, `chaosx.nr32.2`, `chaosx.nr32.3`, `chaosx.nr32.30`, `chaosx.nr32.31`, `chaosx.nr32.32`, `chaosx.nr32.40`, `chaosx.nr32.60`, `chaosx.nr32.80`, `chaosx.nr32.69`, `chaosx.nr32.82`, `chaosx.nr32.83`, `chaosx.nr32.89` | Event entry, integration, payload, policy, posture, rogue, warning, and hidden resolution choices. |
| Constants | `common/script_constants/032_missiles_constants.txt`; `common/script_constants/032_missiles_scenario_constants.txt` | AI weight ladders, site/guidance/rogue/evolution/queue tuning, caps, and SCN-015 scales. |
| Core program and sites | `common/scripted_effects/032_missiles_effects.txt`; `missiles_score_site_candidate`, `missiles_select_best_site`, `missiles_register_site`, `missiles_recalculate_network` | Recipient initialization, site scoring, site registration, capacity, and network state. |
| Operations | `common/scripted_effects/032_missiles_operations_effects.txt`; `missiles_select_operation_profile`, `missiles_select_operation_target_state`, `missiles_select_operation_site`, `missiles_prepare_guidance_weights`, `missiles_select_operation_impact_state` | Target/profile/site/payload/guidance selection and operation resolution. |
| Operations triggers | `common/scripted_triggers/032_missiles_operations_triggers.txt`; selected target/state, preflight, profile, payload, reach, custody, warning, queue, posture, and incident triggers | Candidate validity and operation gates. |
| General triggers | `common/scripted_triggers/032_missiles_triggers.txt`; recipient, target country/state, payload, evolution, retaliation, automatic, scenario, and rogue validity triggers | Eligibility filters and terminal-state guards. |
| Evolution and rogue effects | `common/scripted_effects/032_missiles_operations_effects.txt`; `missiles_update_firing_pressure_snapshot`, `missiles_evaluate_country_evolution_adoption`, `missiles_evaluate_evolution_unlocks`, `missiles_schedule_evolution_track`, `missiles_evaluate_rogue_incident_from_firing`, `missiles_open_rogue_incident` | Five evolution tracks, deterministic scheduling, rogue incident chance, and family selection. |
| Decisions | `common/decisions/032_missiles_decisions.txt` | Player and AI maintenance, posture, operations, incident, warning, and response score surfaces. |
| Missions | `common/decisions/032_missiles_missions.txt` | Timed objective score surfaces for survey, repair, recovery, preparation, and warning verification. |
| Decision category | `common/decisions/categories/032_missiles_categories.txt` | Category registration and priority; no separate AI weight surface. |
| Scenario package | `common/scripted_effects/032_missiles_scenario_effects.txt`; `common/scripted_triggers/032_missiles_scenario_triggers.txt`; `missiles_scenario_load_intensity_runtime`, `missiles_scenario_apply_country_package`, `missiles_scenario_launch_unregistered` | SCN-015 profile loading, recipient package setup, and rollback. |
| Warning and retaliation | `common/scripted_effects/032_missiles_operations_effects.txt`; `missiles_classify_operation_attribution`, `missiles_queue_warning_for_impact_country`, `missiles_retaliation_can_queue`, `missiles_accept_retaliation_response` | Attribution labels, queue caps, response timing, and retaliation preflight. |
| Related bridges | `common/scripted_effects/005_soviet_collapse_effects.txt`, `006_independence_wave_execution_effects.txt`, `013_natural_disasters_effects.txt`, `016_brilliant_scientist_raid_effects.txt`, `021_random_civil_war_parent_effects.txt` | Cross-event state handoffs relevant to reserve, site damage, capture, and inherited state. |

No Event 32-specific `common/ai_strategy` file or runtime consumer of the declared `missiles_ai_profile` constants was found.

No Event 32-specific `common/mtth` file or `mean_time_to_happen` or `mtth:` reference was found in the traced Event 32 source.

## Scenario inventory and status

The matrix contains 83 named scenarios.

The ids below are the complete requested set, and every id is blocked from MCP evaluation, sweep, comparison, and rendering by the unavailable probability-inspect route.

| Matrix surface | Exact scenario ids | Intended audit focus | MCP result |
| --- | --- | --- | --- |
| Sites | `SITE-01`, `SITE-02`, `SITE-03`, `SITE-04`, `SITE-05`, `SITE-06` | Interior/core/capital/occupied choice, one-state certainty, region, security, and capture compromise. | `unresolved`; no inspect/evaluate artifact. |
| Target countries | `TGT-C-01`, `TGT-C-02`, `TGT-C-03`, `TGT-C-04`, `TGT-C-05` | Enemy major versus minor, ally or neutral rejection, evidence, program ownership, and reserve constraints. | `unresolved`; no inspect/evaluate artifact. |
| Target states | `TGT-S-01`, `TGT-S-02`, `TGT-S-03`, `TGT-S-04`, `TGT-S-05`, `TGT-S-06` | Hub, railway, industry, air/radar/coastal, launch-site, restrained, and isolated-target ranking. | `unresolved`; no inspect/evaluate artifact. |
| Strike profiles | `STRIKE-01`, `STRIKE-02`, `STRIKE-03`, `STRIKE-04`, `STRIKE-05`, `STRIKE-06`, `STRIKE-07`, `STRIKE-08` | Precision, strategic, saturation, readiness, counterforce, empty-target, restrained, and immediate-defeat behavior. | `unresolved`; no inspect/evaluate artifact. |
| Payloads | `PAY-01`, `PAY-02`, `PAY-03`, `PAY-04`, `PAY-05`, `PAY-06`, `PAY-07` | Conventional fallback, chemical, nuclear, thermonuclear, biological, uncertain guidance, and rogue physical custody. | `unresolved`; no inspect/evaluate artifact. |
| Guidance | `GUIDE-01`, `GUIDE-02`, `GUIDE-03`, `GUIDE-04`, `GUIDE-05`, `GUIDE-06`, `GUIDE-07` | Mature/readiness, early/damaged, saturation, compromised, special, maintenance, and neutral/self outcomes. | `unresolved`; no inspect/evaluate artifact. |
| Rogue incidents | `ROGUE-01`, `ROGUE-02`, `ROGUE-03`, `ROGUE-04`, `ROGUE-05`, `ROGUE-06`, `ROGUE-07`, `ROGUE-08` | Secure control, civil war, captured payload, foreign actor, reserve starvation, recent rotation, crisis cooldown, and duplicate incidents. | `unresolved`; no inspect/evaluate artifact. |
| Posture | `POSTURE-01`, `POSTURE-02`, `POSTURE-03`, `POSTURE-04`, `POSTURE-05`, `POSTURE-06` | Restrained, hardened delegation, automatic control floor, vulnerable site, false warning, and verified special attack. | `unresolved`; no inspect/evaluate artifact. |
| Warning attribution | `WARN-01`, `WARN-02`, `WARN-03`, `WARN-04`, `WARN-05`, `WARN-06`, `WARN-07`, `WARN-08` | Confirmed, uncertain, conflicting, false, compromised-site, duplicate-root, queue-cap, and absent-site handling. | `unresolved`; no inspect/evaluate artifact. |
| Evolution | `EVO-01`, `EVO-02`, `EVO-03`, `EVO-04`, `EVO-05`, `EVO-06`, `EVO-07`, `EVO-08`, `EVO-09`, `EVO-10`, `EVO-11`, `EVO-12` | Rogue, unreliable, saturation, special, and automatic pacing, eligibility, disabled state, and recorded-state idempotence. | `unresolved`; no inspect/evaluate artifact. |
| SCN-015 profiles | `SCN15-01`, `SCN15-02`, `SCN15-03`, `SCN15-04`, `SCN15-05`, `SCN15-06`, `SCN15-07`, `SCN15-08`, `SCN15-09`, `SCN15-10` | Global proliferation, maximum coverage, saturation war, safe-conflict failure, command breakdown, special payload, retaliation network, warning cap, repeat idempotence, and atomic preflight failure. | `unresolved`; no inspect/evaluate artifact. |

The high-level scenario expectations from the matrix were reviewed, but no exact or bounded runtime result can be assigned to them.

## Candidate-pool and external-factor completeness

The table distinguishes source-visible candidates from the complete declared pool required for a probability claim.

| Surface | Source-visible pool or selection path | Candidate-pool completeness | External factors required for the matrix | Result classification |
| --- | --- | --- | --- | --- |
| Recipient | `missiles_is_valid_recipient` over `every_country`, with deferred and skipped branches in the global firing transaction. | The expression is source-visible, but parsed runtime eligibility and SCN-015 share filtering are unverified. | Country existence, capitulation, carrier/test exclusion, usable command, controlled land, subject/exile state, scenario share, and setup failure. | Source gate trace only; MCP `unresolved`. |
| Site candidate | `missiles_select_best_site` scans `every_owned_state` for controlled, non-impassable states and uses `missiles_score_site_candidate`; fallback is capital. | Visible expression, but no weighted engine artifact and no source-level random tie model. | Ownership/control, state type, infrastructure, supply, AA, radar, railway, factories, capital, region, damage, resistance, security, frontline, occupation, capture, and tie order. | Score-only; exact site probability `unresolved`. |
| Target country | `missiles_ensure_selected_target` and `missiles_select_target` use `random_country` from `missiles_target_is_valid`. | Incomplete relative to the matrix because no country score or evidence ranking exists; ally exclusion is not visible in the validity trigger. | War relation, alliance/faction, subject status, evidence, program ownership, target reserve, distance, and target validity. | Source random-scope trace; selection probability `unresolved`. |
| Target state | `missiles_select_operation_target_state` uses `random_owned_controlled_state` after profile filtering and falls through deterministic profile alternatives. | Incomplete relative to the matrix because no hub/industry/population/air/radar/launch-site value race exists. | Target ownership/control, profile values, factories, railway, supply, population, air/radar/coast, launch-site condition, guidance, isolation, and restrained policy. | Source random-scope trace; rank and probability `unresolved`. |
| Operation site | `missiles_select_operation_site` chooses custody-capable or current/from state, then random valid states and up to four saturation sites. | Incomplete for quality-weighted site scenarios; no quality score is applied at operation selection. | Custody, capacity, reserve, profile, site damage, reach, readiness, special payload, saturation cap, and site history. | Bounded gate trace only; MCP `unresolved`. |
| Evolution/profile selection | Event `ai_chance` options and deterministic `missiles_select_operation_profile`; decisions and missions use `ai_will_do` scores. | Candidate ids are visible, but parsed scope, gate ordering, external modifiers, and complete AI actor context are unavailable. | War state, major status, program stage, reserve, readiness, guidance, target values, payload stockpile, policy, posture, and AI profile. | Score-only for source constants; probability `unresolved`. |
| Payload integration | `chaosx.nr32.30` `ai_chance` plus deterministic special-payload integration order and custody gates. | Candidate list is visible, but runtime tech, stockpile, condemnation, policy, and custody pool are not available. | Integration flags, technology, stockpile, first-use history, condemnation, target profile, guidance, site custody, and rogue physical custody. | Score-only; normalized probability `unresolved`. |
| Payload selection | `chaosx.nr32.31` `ai_chance` followed by `missiles_prepare_operation_payload`; conventional is the normal fallback. | Candidate ids are visible, but no scenario-specific candidate-pool manifest was accepted by MCP. | Stockpile and integration, target and policy, special payload ownership, reserve, guidance, and operation profile. | Score-only and deterministic-gate trace; probability `unresolved`. |
| Guidance | `missiles_prepare_operation_drift_pool` builds bounded neighbor, neutral, self, and site pools; `missiles_prepare_guidance_weights` feeds `random_list`. | Pool construction is statically visible, but map adjacency, country relations, state validity, and parsed random-list normalization are unverified. | Guidance score, technology, readiness, control, training, hardened state, range, profile, special payload, instability, recalibration, neighbors, neutral/self eligibility, interception, and target state. | Source bounded pool and score trace; outcome probability `unresolved`. |
| Rogue incident chance | `missiles_evaluate_rogue_incident_from_firing` uses a no-incident versus incident `random_list`, then a family `random_list`. | Family branches and zero factors are visible, but valid actor/site/target arrays and runtime incident caps are unverified. | Control, civil war, site/code compromise, reserve, foreign actor and intel network, physical payload, target, cooldown, recent rotation, existing incident, generation, and active cap. | Source weight trace; probability `unresolved`. |
| Rogue attribution and response | `missiles_select_rogue_incident_foreign_actor`, `missiles_select_rogue_incident_launch_target`, and `chaosx.nr32.60` response event. | Random actor and target arrays are visible, but relevance ranking and response scopes are not weighted. | Foreign relation, war, intel network, code compromise, reserve, physical payload, control, posture, war state, and incident family. | Source gate/score trace; probability `unresolved`. |
| Warning attribution | `missiles_classify_operation_attribution` maps operation type/outcome to confirmed, highly likely, accidental, or disputed, then warning verification checks the label. | Incomplete relative to the matrix because unknown, forged, false-warning, and uncertain attribution paths are not assigned by the operation classifier. | Impact type, outcome, rogue/retaliation origin, evidence, site compromise, false signal, conflicting sources, warning root, verification state, and queue state. | Source classification trace; scenario outcome `unresolved`. |
| Retaliation queue | `missiles_retaliation_can_queue` and `missiles_queue_warning_for_impact_country` enforce automatic posture, reserve, active site, root, queue, incident, participant, and generation caps. | Gate list is visible, but queue state and scheduled warning events are not available to MCP. | Automatic evolution, posture, warning actionability, reserve, site, root id, queue 24 cap, incident 12 cap, participant 6 cap, generation 3 cap, expiry, and response cadence. | Bounded source gate trace; timing and response probability `unresolved`. |
| Maintenance and posture | `chaosx.nr32.40`, decisions, and missions use fixed AI score ladders with simple war/major/network modifiers. | Option and score names are visible, but actor-specific candidate availability and cooldown state are not complete. | War, major status, program phase, network, control, warning history, site damage, readiness, guidance, reserve, codes, cooldowns, and AI profile. | Score-only; selection and timing `unresolved`. |
| Evolution pacing/adoption | `missiles_evaluate_evolution_unlocks`, `missiles_schedule_evolution_track`, and `missiles_evaluate_country_evolution_adoption`. | No MTTH hazard or random adoption pool is visible; engine date and state transitions are unavailable. | Chaos, firing pressure counters, maturity, war, payload owners, retaliation, control, disabled/recorded flags, current date, and pending schedule. | Exact source gate/date arithmetic only; engine timing `unresolved`. |
| SCN-015 package | `missiles_scenario_apply_country_package` calls initialization over every valid recipient; profile flags and share/cap values are assigned. | Incomplete: package share and incident-cap variables are assigned but not consumed, and profile flags have no downstream consumers in the traced Event 32 path. | Intensity, share, package stage, reserve, site capacity, readiness, control, scenario profile, safe conflict, participant cap, incident cap, payload owners, and rollback. | Source assignment trace; profile behavior and coverage `unresolved`. |

No exact probability is stated for any row.

## Base values and source modifier traces

### Shared AI ladders

`common/script_constants/032_missiles_constants.txt` declares `missiles_ai_weight` as minimal `1`, low `3`, medium `6`, high `10`, and certain `100`.

The associated factors are rejection `0`, verification `2`, restraint `2`, escalation `2`, and special `1.5`.

These values are source constants, not normalized probabilities.

### Event option traces

The visible Event 32 option races are:

| Event | Base options and visible modifiers | Static interpretation |
| --- | --- | --- |
| `chaosx.nr32.30` integration | Chemical candidate medium `6` and special factor `1.5` after first chemical use; biological low `3`; nuclear high `10` and special factor `1.5` in war; thermonuclear low `3`; skip minimal `1`. | Nuclear or chemical can dominate integration by score, but stockpile, condemnation, guidance, and scenario-specific scarcity are not visible in the option weights. |
| `chaosx.nr32.31` payload | Conventional high `10`; chemical medium `6` when integrated; biological low `3`; nuclear medium `6`; thermonuclear low `3`. | Conventional is the default score leader and special payloads are flat across operation context. |
| `chaosx.nr32.32` policy | Prohibited medium `6`; retaliatory high `10`; military-target high `10`; unrestricted-war low `3` in war; emergency delegation minimal `1` for automatic evolution. | Retaliatory and military-target policy choices tie at the highest base score. |
| `chaosx.nr32.40` posture | Off low `3` and restraint factor after false-warning history; supervised high `10` with network; delegated medium `6` and escalation in war; automatic low `3` and escalation after verified special attack, rejected after false warning. | Supervised posture is the default score leader when available. Automatic and delegated viability depends mainly on gates and two visible factors. |
| `chaosx.nr32.60` rogue response | Rotate high `10` and verification factor for code compromise; isolate high `10` and restraint for site payload; negotiate medium `6` and restraint outside war; scuttle low `3` and escalation with payload; launch low `3` and escalation in war; wait minimal `1`. | Response scores are context-light and actor/site/target relevance is not ranked. |
| `chaosx.nr32.80` warning | Verify high `10` and verification factor when unverified; delay medium `6`; sever low `3` and restraint after false history; accept low `3` and escalation only when verified, otherwise rejected; hold minimal `1`. | Verify dominates unverified warnings by source score, while accept is deliberately gated. |

### Decision and mission traces

`common/decisions/032_missiles_decisions.txt` uses file-scoped AI values low `1`, medium `4`, high `8`, and urgent `14`.

Representative decision traces are survey high, command authority urgent with war factor `2`, capture medium with war factor `2`, study high outside war, integrate high in war, scuttle low with a pre-guided factor `4` and war factor `2`, replenish medium with war factor `2` and major factor `2`, readiness medium with war factor `2`, guidance medium with war factor `2`, codes high with a factor `3` when insecure, harden medium with war factor `2` and noncapital factor `2`, expansion medium with war factor `3`, secondary low with war factor `3`, precision high with war factor `3`, strategic medium with war factor `4`, saturation low with war factor `5`, counterforce high with war factor `4`, special integration low with war factor `4`, posture high with war factor `2`, and launch urgent with war factor `3`.

The decision file also makes target selection player-only with base zero and zeroes preparation actions when their prerequisite trigger fails.

`common/decisions/032_missiles_missions.txt` uses survey high, secondary medium with war factor `2`, repair high with war factor `2`, recovery high with war factor `2`, precision preparation high, strategic preparation medium with war factor `2`, saturation preparation low with war factor `5`, counterforce preparation high with war factor `3`, warning verification urgent, and restoration high.

Decision and mission scores are score-only until a complete candidate pool and actor state are supplied to the probability adapter.

### Site score trace

`missiles_score_site_candidate` starts from `-100000` and visibly adds existing rocket `1000`, existing Event 32 site `500`, core `40`, infrastructure steps `5`, supply `20`, AA `12`, radar `10`, railway, factories, and different-region `30`.

It visibly subtracts the capital penalty `25`, damaged penalty `40`, and the configured island penalty when `is_coastal = yes`.

The declared secure-control, frontline, occupied, resistance, and minimum-candidate tuning values are not visibly applied by this scorer.

The site selector uses strict greater-than replacement, so equal-score ties retain first iteration order rather than an explicit random tie pool.

This is a score race, not a probability-proportional selection claim.

### Guidance trace

`missiles_calculate_operation_guidance` starts from base score `45`, adds technology `8`, readiness contribution `.20`, command contribution `.15`, training contribution `.80`, hardened `8`, recalibration `15`, and subtracts range penalty `12`, saturation `14`, special `10`, and unstable `20` before clamping.

The visible `random_list` outcome weights are on-target `60`, degraded `22`, wrong object `8`, near miss `6`, breakup `4`, wrong state `7`, neutral `3`, self `2`, site `2`, and dud `3`, with unstable failure `10`.

The source clamps and zeroes invalid drift branches, but the parsed normalized outcome distribution is unavailable.

### Rogue trace

The incident random-list base is no incident `100` versus incident `5`.

The pressure factors are low `.35`, elevated `2`, high `3`, and severe `5`, with civil war `3`, recent rotation `.2`, and stable-control/security reductions visible in the surrounding constants.

The family weights are unauthorized `8`, mutiny `12`, defection `6`, regional `8`, bribery `6`, captured `10`, and payload `4`.

Family factors include protected `.2`, low `.35`, elevated `2`, high `3`, severe `5`, and branch-specific zero factors when site, recipient, foreign actor, reserve, payload, or target conditions fail.

These are weighted-list inputs only and are not exact incident probabilities without the complete runtime pool and MCP normalization result.

### Evolution trace

The five tracks are rogue commands, unreliable guidance, saturation arsenals, special payloads, and automatic retaliation.

The source unlock gates are chaos thresholds `200`, `400`, `600`, `800`, and `900` respectively, with track-specific requirements involving vulnerable sites, guided launches, mature programs, payload owners, and retaliation counts.

The nominal delays are rogue `120`, guidance `105`, saturation `90`, special `120`, retaliation `150`, and warning response `3` days.

The source shortens some delays by `.5` when pressure thresholds are met, but the declared delay-lengthening multiplier is not consumed by the traced code.

`missiles_schedule_evolution_track` stores an exact due date from the current date plus the selected delay.

There is no Event 32 MTTH entry, no daily hazard trace, and no random adoption race in the current source review.

### Queue and scenario trace

The declared chain caps are maximum generation `3`, participant countries `6`, incidents `12`, active warning queue `24`, and one declared maximum launch per country.

The source visibly consumes generation, participant, incident, and queue guards in warning/retaliation paths.

The declared `maximum_launches_per_country = 1` was not found as a runtime consumer in the traced source.

SCN-015 runtime intensity values are low share `10`, stage `1`, reserve `6`, site capacity `1`, readiness `70`, control `90`, incident cap `0`, participants `2`; medium share `35`, stage `2`, reserve `10`, site capacity `2`, readiness `75`, control `80`, incident cap `0`, participants `3`; high share `75`, stage `4`, reserve `16`, site capacity `3`, readiness `82`, control `65`, incident cap `1`, participants `4`; and maximum share `100`, stage `6`, reserve `24`, site capacity `4`, readiness `90`, control `50`, incident cap `1`, participants `6`.

The package effect assigns share, profile, and incident-cap variables, but the traced runtime package path consumes stage, reserve, site capacity, readiness, and control while not consuming package share or package incident cap.

## Findings by risk category

The severity labels below describe source-review risk, not an engine-confirmed defect severity.

### AI validity

The recipient validity trigger rejects missing, capitulated, carrier/test, unusable-command, and uncontrolled/impassable recipients, but the parsed runtime result is unavailable.

The target validity trigger requires an existing enemy at war with a usable controlled state and excludes subjects, but it does not visibly exclude allied or faction-compatible targets.

The site selector filters to owned, controlled, non-impassable states and uses a capital fallback, but operation-site selection can fall back to random valid states rather than the best scored site.

Special payload custody, reserve, reach, profile, warning, posture, and generation checks are present in source triggers and effects, but their runtime ordering remains unverified.

### Dominance

The nuclear integration option has base score `10`, chemical has `6`, and biological and thermonuclear have `3`.

The conventional payload option has base score `10`, chemical and nuclear `6`, and biological and thermonuclear `3`.

Supervised posture has base score `10`, delegated `6`, and automatic `3` before visible factors and gates.

These can create dominance in score races, but no exact share is claimed because `ai_chance` normalization and candidate validity were not observed through MCP.

### Starvation

Target country and state selection have no visible score for major status, evidence strength, industry, population, rail hub, launch infrastructure, or strategic relevance.

Declared AI profiles are not consumed by the current Event 32 runtime path, so restrained, belligerent, survival, retaliatory, and other scenario-specific behavior has no visible profile factor.

SCN-015 share is not visibly applied to recipient selection, so a low-coverage profile can initialize every valid recipient and starve the intended limited-coverage distinction.

No-reserve conditions zero unauthorized and defection rogue branches, but other rogue families can remain eligible under their own conditions.

### Rank reversal

The missing target ranking can reverse the expected enemy-major, evidence-first, hub-first, or industrial-target order.

The site scorer does not visibly apply secure-control, frontline, occupied, or resistance penalties even though corresponding tuning values exist.

The site scorer applies `island_penalty` when `is_coastal = yes`, which is a semantic mismatch worth owner review because coastal status and island status are not the same condition.

The target-state selector uses random scope selection after profile filtering and therefore cannot establish the matrix ranking without an additional value race.

### Repetition

Target country, target state, rogue site, foreign actor, rogue target, and operation site paths use random scope selection with no visible history-based diversification.

`missiles_target_sequence` and related counters limit sequence length but do not visibly prevent repeated selection of the same country or state.

This creates a repetition risk in long-running or saturation scenarios; MCP sequence evidence is unavailable.

### Exploit risk

The SCN-015 package assigns coverage and incident-cap values that are not visibly consumed, which can undermine intended bounded coverage and cap behavior.

The declared maximum launch-per-country tuning value has no traced runtime consumer.

Special payload dispatch debits or consumes payload custody before guidance outcome resolution, so a dud, interception, or breakup may still consume a scarce payload; this may be an intentional cost model, but it should be scenario-tested rather than assumed safe.

The source has queue, generation, participant, incident, reserve, and site guards, but duplicate-root, repeat, cap, and atomic-rollback behavior cannot be established without structural and probability artifacts.

## Surface-specific audit conclusions

| Surface | Current source conclusion | Classification | Required follow-up |
| --- | --- | --- | --- |
| Recipient | Deterministic `every_country` validity enumeration; SCN-015 does not visibly filter by share. | Source gate trace; engine `unresolved`. | Inspect the parsed recipient pool and evaluate low/maximum coverage scenarios. |
| Site | Scored best-site race exists, but operation selection also uses random valid states and the scorer omits declared factors. | Score-only; probability `unresolved`. | Evaluate `SITE-01` through `SITE-06`, including ties and compromised/captured states. |
| Target country | Random valid enemy-country selection with no visible relevance/evidence score and no visible ally exclusion. | Source random-scope trace; probability `unresolved`. | Build a complete enemy/ally/neutral pool and evaluate `TGT-C-01` through `TGT-C-05`. |
| Target state | Random valid state selection after profile filtering with deterministic fallback profile order. | Source random-scope trace; rank/probability `unresolved`. | Evaluate `TGT-S-01` through `TGT-S-06` for every profile and guidance state. |
| Strike profile | Event options and decision scores exist; derived profile maps counterforce to the strategic strike-profile enum. | Score-only and gate trace; probability `unresolved`. | Evaluate `STRIKE-01` through `STRIKE-08` with complete reserves, readiness, and war context. |
| Payload | Integration and selection options are flat relative to context, with custody and policy gates downstream. | Score-only and deterministic-gate trace; probability `unresolved`. | Evaluate `PAY-01` through `PAY-07` with complete stockpile and condemnation inputs. |
| Guidance | Bounded drift pools and variable `random_list` weights exist. | Source bounded pool; outcome probability `unresolved`. | Evaluate `GUIDE-01` through `GUIDE-07` and render the outcome matrix. |
| Evolution | Five tracks use counter thresholds and exact scheduled dates, not MTTH or random adoption. | Exact source gate/date trace; engine timing `unresolved`. | Evaluate `EVO-01` through `EVO-12` and compare timing distributions only after adapter restoration. |
| Rogue incidents | Incident and family lists have useful branch zeroing and pressure factors, but site/actor/target selection is random and profile factors are absent. | Source weight trace; probability `unresolved`. | Evaluate `ROGUE-01` through `ROGUE-08` with full site, actor, target, reserve, and cooldown pools. |
| Warning attribution | Four classifier labels are visible, but uncertain/forged/false/conflicting source paths are incomplete. | Source classification trace; scenario probability `unresolved`. | Evaluate `WARN-01` through `WARN-08` with explicit attribution states and queue state. |
| Retaliation queue | Queue/generation/participant/reserve/site gates are visible and responses schedule bounded expiry/cadence. | Bounded gate trace; timing/selection `unresolved`. | Include retaliation queue state in warning and posture scenarios. |
| Maintenance/posture | Decision, mission, and event score ladders are mostly flat with simple war, major, network, and warning factors. | Score-only; probability/timing `unresolved`. | Evaluate `POSTURE-01` through `POSTURE-06` and maintenance actions under complete cooldown state. |
| SCN-015 | Package stages and initial runtime values are assigned, but share, profile, incident cap, and participant behavior are not visibly consumed downstream. | Source assignment trace; coverage/profile behavior `unresolved`. | Evaluate `SCN15-01` through `SCN15-10` after profile consumers and package pool are exposed to MCP. |

## Recommended fixes for the owning implementation agent

These are recommendations only.

1. Restore or expose the callable `hoi4.probability_inspect` route and the structural `hoi4.event_inspect` route before making any weighted tuning decision.

2. Create complete MCP scenario manifests for all 83 ids with explicit candidate pools, external factors, scheduled changes, uncertain inputs, cadence, seeds where applicable, and terminal states.

3. Add or expose a target-country value race that enforces enemy relevance, evidence strength, program ownership, and ally/neutral exclusion, then add a target-state value race for industry, rail, hub, air/radar, launch-site, population, isolation, and profile-specific intent.

4. Either wire the declared `missiles_ai_profile` values into the Event 32 runtime or remove them from the scenario contract and revise the expected profile behavior; the current unconsumed constants cannot produce the specified AI distinctions.

5. Wire SCN-015 share, incident cap, participant behavior, profile flags, special-payload crisis, saturation-war behavior, command-breakdown behavior, retaliation-network behavior, and no-immediate-launch behavior into the consuming paths, with explicit atomic failure and idempotence checks.

6. Extend warning attribution and verification inputs so uncertain, conflicting, false, forged, and compromised-site scenarios are represented by actual source state rather than only by matrix assumptions.

7. Review site scoring and operation-site selection together, especially the coastal/island condition, omitted secure/frontline/occupied/resistance modifiers, strict tie retention, and random fallback paths.

8. Centralize the event, decision, and mission AI tuning ladders or document their intentional separation and scenario-test their cross-surface dominance and starvation behavior.

9. Decide whether evolution timing is intentionally exact-date scheduling or should be MTTH-backed; update the scenario contract accordingly and do not label current exact delays as MTTH distributions.

10. After any owner-applied weighted change, rerun `probability_inspect` first and then the same 83 ids through `probability_evaluate`, `probability_sweep`, `probability_render`, and `probability_compare` against `probability-57fedf8c2ca0972cbadd9612` and `probability-9735d25129b2670c7d609392` using baseline hash `ec4dc421`.

## Skipped analyses, exact reasons, and remaining uncertainty

- Probability inspection was blocked by the exact unavailable-tool response quoted above.
- Structural event inspection was blocked by the exact non-callable function error quoted above.
- No probability evaluation was performed because inspection could not establish an adapter or parsed source.
- No threshold or sensitivity sweep was performed because there was no MCP scenario result to sweep.
- No same-scenario baseline comparison was performed because no current or baseline probability artifact was returned.
- No probability or structural render was produced because no analysis id or render-capable artifact existed.
- No simulation was performed because the scenario matrix requires explicit uncertain inputs and the required adapter route was unavailable.
- No sequence analysis was performed because no complete MCP custom-pool manifest, cadence, and state-transition artifact could be registered.
- No Hearts of Iron IV process was launched.
- No gameplay file was edited.

The remaining uncertainty includes parsed Clausewitz scope semantics, runtime candidate-pool membership, `ai_chance` normalization, `random_list` normalization, tie behavior, scheduled event ordering, cooldown enforcement, state-control transitions, map adjacency, payload stockpile state, warning attribution state, and cross-event consumers.

## Handoff status

Audit status: incomplete and blocked for engine-backed probability conclusions.

Source-review status: concrete static risks and tuning targets documented above.

MCP evidence status: no artifacts, revisions, scenario hashes, comparison ids, or rendered URIs available.

Result sufficiency: not sufficient for balance sign-off or a claim that the Event 32 weighted surfaces are correct.

Simplifications or omissions by this auditor: none; the requested MCP analyses could not be substituted with source-only claims.
