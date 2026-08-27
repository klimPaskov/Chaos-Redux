# Chaos Redux weighted-logic baseline audit

Date: 2026-08-22.

Status: read-only baseline evidence for the repository cleanup; no gameplay, AI, event, focus, decision, mission, localisation, source, scripted-GUI, or interface layout files were changed.

The parent’s GUI constraint is applied: `interface\*.gui` coordinate/layout work is out of scope, while functional selector, toggle, content, and scripted-GUI binding logic was inspected as a weighting/availability surface only.

## Scope and result vocabulary

The audit covers shared automatic random-event selection, event type/category filters, settings/manual firing where a random or weighted path exists, event clusters, triggerable scenarios, world-end registry selection, weighted super-event-related paths, and probability-bearing event/decision/focus surfaces associated with Events 1–20.

Event-specific content for Events 21+ was not audited; legacy 21+ entries were considered only where they remain in shared event registries or selection loops.

`Exact` means the MCP adapter proved the requested arithmetic or score under the declared candidate pool and state fixture.

`Bounded` means the source/MCP result establishes a bounded mechanism or quantization rule, but not a complete live-campaign probability.

`Sampled` means a seeded MCP simulation result; none was run because no uncertain-input distribution and seed contract was declared.

`Score-only` means a willingness/AI score race, not a normalized click or selection probability.

`Unresolved` means that candidate pool, hidden state, adapter support, artifact freshness, or MCP availability prevented a runtime probability conclusion.

## Runtime and required references

MCP workspace: `mod_chaos_redux_ea3b2d67c2c0`.

Game runtime reported by MCP: Hearts of Iron IV Operation Postern `1.19.2.0.a729`, checksum `d245`.

The required `AGENTS.md`, cleanup master prompt, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-focus-trees`, `chaos-redux-subagents`, and `chaos-redux-mtth` skills were read in full.

The required offline Paradox wiki core pages and the relevant national-focus, event, decision, AI, trigger, effect, modifier, scope, localisation, and data-structure pages were read.

The relevant vanilla documentation under `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\` was consulted, including script concepts/constants, triggers, effects, modifiers, dynamic variables, event, decision, focus, AI, and localisation documentation.

Parent review confirmed that the current `chaos-redux-mtth` skill references the existing `common\mtth\chaosx_mtth_variables.txt` file. The earlier `.md` path observation was stale and is not a blocker.

## MCP audit matrix

| Surface and source | First MCP inspect | Scenario/evaluation | Pool and external-state completeness | Classification and evidence |
|---|---|---|---|---|
| Shared automatic event selector and settings selector in `common\scripted_effects\chaosx_settings_effects.txt`, with shared gates in `common\scripted_effects\chaosx_logic_effects.txt` | `custom_weighted_pool`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fd0366d11b9ec85027eda4687c00768af18b0771f3f2d11bf57074ef1b76e4e2/cc32fc3f3e2ad558a5741aac734e4f4b9f0563121abd32d92b9271ca44037bf9/probability-inspect-820d32f80f16.json` | No evaluation or sequence was justified because the adapter returned zero manifest candidates | `candidateCount=0`, `poolComplete=false`, `completePoolRequired=true`; the source is scripted array logic, not a manifest-defined custom pool | Bounded algorithm/source evidence; live normalized odds unresolved. Source hash `820d32f80f1627b48d83b351598634476fe26f62d948336503a235fc6b285483`; source revision `0b582f5b761b1f861482a5609130d1bb3d6382894eb0bc69ab09351be5ad5f76` |
| Event-option AI chance surfaces in `events\001_communism_spread.txt` | `event_option_ai_chance`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5a52c8bc2076e12d1c805334636be61b47015bc334f87f93a39be60eb1ae3cf0/23e3e615529bf9b7cacef0c4b8b22a4fffd2b03008df854662d031b0d8769b6e/probability-inspect-0e8925e17bee.json` | No evaluation because the file contains multiple event-option roots and hidden state was not supplied | 39 discovered options; `poolComplete=false`; required inputs include `any_controlled_state`, `has_government`, `has_stability`, `has_war`, `hidden_trigger`, and `num_of_controlled_states`; unsupported diagnostic `MULTIPLE_CATEGORICAL_POOLS` | Unresolved; the adapter documents proportional categorical selection with d100 quantization, but no option score is a percentage and no root-local pool was complete. Source hash `0e8925e17bee0d212a8c40d8733beef32a31b3bd03954f5f2a71b67b8baecbcc`; source revision `0b582f5b761b1f861482a5609130d1bb3d6382894eb0bc69ab09351be5ad5f76` |
| Event 002 MTTH roots in `events\002_zombie_outbreak.txt` | `event_mean_time_to_happen`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/982171dc9b5cfea8fb251f0cfb50027bdd6dfde626fd3db8fa52d66fb8555c26/03915914d1f537cc0d1a149678c691ab25f705554e6767701d01631bad9bd328/probability-inspect-b467454649cc.json` | `CR_CLEANUP_MTTH_002_BASELINE_2026_08_22` and `CR_CLEANUP_MTTH_002_EXACT_2026_08_22` | Inspect found six roots with a complete adapter pool, but trigger inputs include flags, event targets, country/state relations, variables, and hidden triggers | Exact arithmetic for declared traces; runtime eligibility remains unresolved where the scalar fixture cannot represent flag membership. Source hash `b467454649cc70a715058256247e24d522d818a77ccddd7c1d43cc9f10135dde`; inspect revision `8acf3e189b0c8a61e1d5fe090adc802c4c3eb533e4c24a2557298177394cdd02` |
| Event 002 six-root baseline | `probability_evaluate` analysis `probability-f82a8237a071eee2ec52b489`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/96509ea841334d4575a40cff2f450457bc196b6f16e08bdc64c2583db8cecc6d/3a4bc894b26d4bbf940f021c5b255795a92cc041c77fe7c94dbe2e977894ded2/probability-f82a8237a071eee2ec52b489.json` | `CR_CLEANUP_MTTH_002_BASELINE_2026_08_22`, scenarios `E002_EMPTY_STATE`, `E002_AI_COUNTRY`, and `E002_WORLD_END_FLAG`, horizon 3650 days, metrics `effective_mtth_days`, `cumulative_chance`, and `raw_value` | Candidate pool was supplied, but every scenario omitted required trigger state; 35 unresolved-trigger rows were reported | Unresolved/partial; diagnostic `PROBABILITY_OUTCOME_NEVER_ELIGIBLE`; scenario hash `8e4544ea67db66f473143b69f86e163f10a7ebf45d223030f7a3d6c42c13285f`; candidate-pool hash `de38eddd14b8786e7c3f6bfacbf73cc2715762bb2f1393733e7cc15428a2c888`; source revision `db66eb28f03a2ff607653780ff373b30d46649ab3138248e9057ef72260b50e0` |
| Event 002 root `chaosx.nr2.3` | `probability_evaluate` analysis `probability-544a422365e094e969c72fcb`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e627ec0ff034aee4fb10671dc5517f095aaf6c77bdd563d40e6c7158801228ff/6b38071b74357d29776137658935c4923ca7168851f481fda0e971f195cbd9c9/probability-544a422365e094e969c72fcb.json` | `CR_CLEANUP_MTTH_002_EXACT_2026_08_22`, scenarios `E002_3_PLAYER_OUTBREAK` (`has_global_flag=true,is_ai=false`) and `E002_3_NO_OUTBREAK` (`has_global_flag=false,is_ai=false`), horizon 365 days | Candidate pool is complete for one root, but the adapter interpreted `has_global_flag` as the unresolved flag gate `has_zombie_outbreak`; both supplied fixtures evaluated ineligible | Exact for the arithmetic trace: the root’s MTTH path adds 10 days for `is_ai=no`; unresolved for actual activation/cumulative chance. Diagnostics include `MTTH_HORIZON_CHANCE_NEGLIGIBLE` and `PROBABILITY_OUTCOME_NEVER_ELIGIBLE`; scenario hash `76cd851004213601c3aa6ed596d23c67867ce1653e222a9e67c4fbc8f29236dc`; candidate-pool hash `238ec51d448f1e26c46aa642f7e536138fe5ebeaa2376decd9b1823206398df9`; source revision `f0d028199a3b254b15a74355d155f0404c0ca4de89de39d9cc33e94c9475f460` |
| MTTH variable file `common\mtth\chaosx_mtth_variables.txt` | `event_mean_time_to_happen`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5e0c509154e8bfe15b97672752efe31c94e6bda9b6ecd05c89825745b899b8ad/3593168fbd54f01c7ba246929a2d859cc146fbb89384b6f363a64c8b3cef1b1a/probability-inspect-2aa94d436c12.json` | None; this is a variable-definition source, not an event-root pool | MCP returned `no_weighted_surfaces` and `availableAdapters=[]`; source hash `2aa94d436c126802792a731509f71f4ba0a85e782a635a9063cae247021d5f30`; source revision `b23904a886c6f5231e6427e809271629095dcab02c0ad02efc1a7007fbad12dd` | Unresolved for engine timing; source definitions were reviewed but source-only review is not treated as timing proof |
| Event 002 decision AI scores in `common\decisions\002_zombie_outbreak_decisions.txt` | `decision_ai_will_do`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f733b7b04a5eda7a88ea857257333e5ddc160f5736f06cbb2937c624896e79c3/24291601c5836afe35039181665eb09d3c7a4dff2dbdc0169efe92d1dc00d485/probability-inspect-e53eed7c6010.json` | `CR_CLEANUP_DECISION_002_SCORE_2026_08_22`, scenarios `D002_NO_THREAT_STATE`, `D002_ACTIVE_WAR`, and `D002_AI_MAJOR` | 13 discovered decision candidates; no unsupported adapter construct, but required state includes country/state ownership, flags, government, stability, ideas, wars, variables, and major status | Score-only and partial; no click probability. Evaluate artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c2251c96c612c868f08319536530f596e3fe0a0bf58c8694da9fb5b020fd0bf9/c7adee5d162bde3dc594c236a765d8fc2d3be72a7ebf78d9871f9345393c79a2/probability-ebe04f8a1bf9a38e5efda884.json`; analysis `probability-ebe04f8a1bf9a38e5efda884`; scenario hash `55a270ceb1762b3a0215dabb29dac50a1763ec6197b54c1fe00957991447c80b`; candidate-pool hash `d82935c42d10cdf01dbf6049162d1b1a3dfeb0b863b1f34e52ed27b11c4462ab`; source hash `e53eed7c60108dbca80d04a24a49fe831296346aafd48a701b6e04b828780b40`; source revision `15b5dc217c815552895085943a1126a88b9183ce15a3d583a579cecc5c7496aa` |
| Event 003 focus AI scores in `common\national_focus\003_holy_realm.txt` | `national_focus_ai_will_do`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/40da3f25de0de9f41196ffa2703396b808e815b6ebb381c8e9a2c6a25033fd08/d39e0ebe308c2bcf1af22a2f59fd6c1d3c06cd98dcbac4dae0153362d39b6f4b/probability-inspect-e34fd2031c96.json` | `CR_CLEANUP_FOCUS_003_SCORE_2026_08_22`, scenarios `F003_EMPTY_STATE`, `F003_EXTERNAL_FACTORS_DECLARED`, and `F003_WAR_STATE` | 111 focus candidates; `poolComplete=false`; external focus factors, prerequisites, bypasses, available route, and strategy plans were not complete | Score-only/unresolved. Evaluate artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d43bcc74f1073947d0cb38008724a5f483b0f335e841650799adbc916523c04b/9008c24f7d9123280bb329006b5888a31d2b3bc0f995ece1f9d287c0b5bccbab/probability-9d0d90b1908715582414aa67.json` returned partial diagnostics including `PROBABILITY_CANDIDATE_POOL_INCOMPLETE`, `PROBABILITY_OUTCOME_NEVER_ELIGIBLE`, `PROBABILITY_MODIFIER_UNSATISFIED_IN_SCENARIOS`, and `TRIGGER_UNRESOLVED`; no rank dominance claim is made. |
| Triggerable scenario random lists in `common\scripted_effects\chaosx_triggerable_scenarios_effects.txt` | `random_list` inspect was attempted first for this weighted source | No evaluation, sweep, simulation, or sequence | Source contains weighted profile perturbations and profile pools, but the adapter timed out after 180 seconds | Unresolved; source review identifies repeated `2/6/2` profile-attribute lists, an `8/8/8/8/8/8/8/1` random profile list, a six-way `1/1/1/1/1/1` non-Wendigo list, and a chaos-tier dynamic special/no-special list, but these are not MCP-proven normalized probabilities |
| Event 016 host/facility/foreign weighted candidate builders in `common\scripted_effects\016_brilliant_scientist_effects.txt` | `custom_weighted_pool` inspect was attempted first | No evaluation because inspect timed out after 180 seconds | Source has explicit bounded integer weight pools and candidate expansion loops, but no returned MCP manifest/artifact | Unresolved; this path is a weighted candidate builder, not evidence that super-event IDs themselves are randomly selected |
| World-end registry and row selector in `common\scripted_effects\chaosx_events_log_effects.txt`, `common\scripted_triggers\chaosx_world_end_scenario_triggers.txt`, `common\script_constants\world_end_scenario_registry_constants.txt`, and `events\fallout_world_end_events.txt` | No probability inspect was applicable because the registry has no weighted candidate draw | No probability scenario | Registry rows are sorted by `world_end_scenario_sort_order`, then selected by row index; availability is a boolean gate based on disabled flags, `world_end_disabled`, `world_end`, and active terminal flags | Bounded deterministic/availability evidence, not a probability surface. Fallout’s manual route and the world-end catalog are separate from normal random-event weights |
| Structural Event 002 trace/render | `event_inspect` with selector `{kind:event,eventId:chaosx.nr2.3}`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bfe506939a5719f12359ea81d4c50d9dc93b114cea8c74fef327711db8ffa644/d110937d28dfb519591a395b4edd594c782e6659c252e7f2fde2714b8dda8275/event-state_flow-2af1fa63424e.json` | Structural state-flow only | Partial due workspace/helper projection limits | Structural evidence is supplementary and does not replace the probability pass |
| Structural Event 002 timing render | `event_render` timing view with selector `{kind:event,eventId:chaosx.nr2.3}` | No probability timing claim | Partial render artifacts: manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/98b4a101d534a7647b235b29635c182cf58077573d40651313aefc69fd97bbc5/ac01b4cb9548492464e760db404f9847dc33eea8b4445a06844eb63c2a9d136e/event-timing-2af1fa63424e-manifest.json`; JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5885f018d6aaedd4ce958ecee19d4683ca4ce81b7b7337cdb8b10e5779589dba/5a00d3d802e732aea9f51dced76166f8c8a14dc71b2cbc1b54ff13c70ca41870/event-timing-2af1fa63424e.json`; SVG/PNG were also returned | Structural timing view only; probability render was separately stale |
| Structural Event 003 focus inspect/render | `focus_inspect` first rejected Windows backslashes (`FOCUS_SOURCE_NOT_FOUND`), then succeeded with `common/national_focus/003_holy_realm.txt`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4355c89fb246f5ee4f6e14b126956ed62616b712020546790cdaf0298e81df76/51500893e85823139079f425c2781a6b1859e77bf5bf257d4cc9bbde68b36a88/focus-inspect.2f9f3986507a3e77.json` | `focus_render` was attempted after inspect | Focus render returned `ARTIFACT_STORAGE_LIMIT` and no render URI | Structural focus evidence is partial; no visual layout edits were made |

## Shared selector semantics proven by source review

`common\scripted_effects\chaosx_settings_effects.txt:4329-4441` evaluates each candidate through `evaluate_random_event_active_pool_candidate`, applies the settings category filter, reads the current event weight, multiplies it by 100, rounds it, rejects a scaled value below 1, totals the valid scaled values, draws an integer from 1 through the total, and selects the first cumulative candidate meeting the roll.

This is an exact proportional categorical algorithm over the valid, current, scaled pool; it is not an AI willingness score race and it is not an MTTH hazard.

`common\scripted_effects\chaosx_settings_effects.txt:1734-1745` uses the weighted selector normally, but `force_trigger_mode_enabled` switches to `select_unweighted_random_event_id`.

The force selector samples directly from the selected array and does not run the active-pool eligibility pass first; `common\scripted_effects\chaosx_settings_effects.txt:4443-4507` therefore represents a deliberate non-normal uniform/manual bypass, not a campaign selection probability.

Manual `fire_event_by_id` and the event-details trigger path are availability/trigger operations, not weighted choices.


The active-pool gate and the event-specific prefire contexts are separate; a positive stored weight does not prove dispatch readiness.

## Ranked cleanup findings

### High: repeatable weights recover while candidates are unavailable

`common\scripted_effects\chaosx_logic_effects.txt:787-844` updates every repeatable entry using only required Chaos tier and current cap, then changes zero to 1, one to `global.minor_event_recovery_rate`, or adds that recovery rate.

It does not call the full active-pool gate used by `evaluate_random_event_selection_candidate`, so context-gated entries such as Fury, Tensions, White Peace, Resources, Independence Wave, Africa, and Random Faction can accumulate weight while their dispatch context is absent.

When the gate becomes true, the stale accumulated weight can re-enter the categorical pool at a burst level and dominate lower-weight candidates; the source behavior is exact, but campaign dominance, starvation, and repetition frequency are unresolved because no complete custom-pool/sequence adapter contract was available.

Recommended owner follow-up: decide whether unavailable entries should freeze, decay, clear, or recover only while active, centralize the re-entry reset rule, and rerun a before/after `probability_compare` with a complete pool and the same named scenarios.

### High: the shared pool mixes live entries with a rework queue

`common\scripted_effects\chaosx_logic_effects.txt:328-363` builds `global.all_events` from major, fire-once, and repeatable arrays, then `initialize_default_disabled_events_for_rework_queue` disables every event not accepted by `event_log_event_is_reworked_default_enabled`.

`common\scripted_effects\chaosx_logic_effects.txt:260-327` still registers many legacy 21+ IDs in those arrays, while `common\scripted_effects\chaosx_settings_effects.txt:4388-4415` scans `global.all_events` for every weighted draw.

The disabled gate prevents a disabled candidate from entering the normal pool, so this is not a proven direct odds error; it is an exact pool-completeness, diagnostics, settings-export, and future-maintenance hazard that makes “all candidates” ambiguous and can hide stale weights.

Recommended owner follow-up: separate a live selectable registry from the rework/legacy registry, or publish an MCP manifest that explicitly marks disabled candidates and their reason so pool-complete analyses cannot accidentally include them.

### High: clusters are layered random processes, not one weighted pool

`common\scripted_effects\chaosx_event_cluster_effects.txt:760-860` first checks member availability, then rolls optional participation; `:869-1000` assigns independent 1–100 order scores with danger offsets and sorts by score; `:1089-1165` schedules each queued member with a Chaos-tier cooldown draw.

`common\script_constants\event_cluster_constants.txt` defines cluster roll chances of 5, 10, 15, 25, 35, and 50 by Chaos tier, cluster cooldowns of 90 or 120 days, optional member participation values, and member cooldown ranges.

Natural Disasters Event 013 is intentionally registered in five logical seasonal member slots with required/optional participation values of 100, 85, 60, 60, and 35 and baseline/evolution batch indices; `common\scripted_effects\chaosx_event_cluster_effects.txt:1516-1661` carries per-slot state, target, family, and evolution context.

The exact semantics are cluster-roll chance, conditional member participation, score-based order, and delayed queue dispatch; none of these values should be normalized together as one event probability.

No MCP custom-pool manifest describes the complete cluster member pool, cooldown/recovery/cap/reset state, optional-roll semantics, or Event 013 terminal sequence, so repetition, dominance, starvation, and timing drift are unresolved.

Recommended owner follow-up: create a declared cluster sequence manifest for each cluster, explicitly listing member pool, gates, participation, order strata, cooldown distribution, queue cadence, context reset, and terminal state before using `probability_sequence` and `probability_sweep`.

### Medium: inactive weight floor is conflated with selectable weight

The fire-once handler says “Set weight to 0 permanently” but writes `new_weight = 1` at `common\scripted_effects\chaosx_logic_effects.txt:886-900`; the major handler similarly documents a zero weight but writes 1 at `:955-970`, and unfired major reset writes 1 at `:984-1000`.

The engine-safe floor is understandable, but the same positive numeric field is used for inactive entries, active selection weights, and UI/settings displays; this invites stale-weight interpretations and cleanup mistakes.

Recommended owner follow-up: name and centralize an explicit inactive-floor constant, keep eligibility as the authoritative selectable gate, and expose inactive state separately from weight in any functional selector/ledger binding.

### Medium: recovery comments and tuning constants are stale or duplicated

`common\script_constants\event_system_constants.txt:40-53` sets `recovery_rate = 20`, while `common\scripted_effects\chaosx_logic_effects.txt:814-833` repeatedly says “next multiple of 40” and comments `1 -> 40` and “Add 40”.

The code uses the dynamic 20-point global value, so the comments are stale documentation and a tuning audit hazard rather than proof of a runtime 40-point step.

`event_system_dynamic_major_gain.baseline_total_events = 100` is defined but not referenced; the calculation uses only `baseline_major_events = 10` and `baseline_non_major_events = 90` at `common\scripted_effects\chaosx_logic_effects.txt:717-744`.

Hardcoded shared IDs 3, 7, and 91 remain in active-pool, initialization, and dynamic-major branches, and settings logic contains literal 100 scaling, weight increments, timer multipliers, and cap steps.

Recommended owner follow-up: reconcile comments with the constant-driven formula, remove or wire the unused baseline total, and centralize shared IDs and tuning values before changing balance targets.

### Medium: force/manual selection is a probability semantic bypass

The normal settings selector is weighted, but force mode uses uniform array selection and manual firing can set `temp_bypass_checks`; this is intentional tooling behavior, not campaign odds.

The bypass can choose a disabled, unavailable, or stale-floor entry before its later dispatch context rejects or redirects it, so GUI-linked selectors and functional toggles should label force/manual behavior distinctly from automatic selection.

Recommended owner follow-up: keep the bypass explicit and inspection-only, ensure functional UI copy/telemetry distinguishes uniform force selection from weighted automatic selection, and do not include force-mode draws in balance claims.

### Medium: triggerable scenario random lists contain repeated probability formulas without MCP proof

`common\scripted_effects\chaosx_triggerable_scenarios_effects.txt:1192-1231` repeats five independent `2/6/2` attribute perturbation lists; `:1582-1614` uses an `8/8/8/8/8/8/8/1` profile pool unless Wendigo already exists and a six-way equal non-Wendigo profile pool otherwise; `:1616-1638` derives a dynamic special-profile/no-special list from Chaos tier constants.

These are source-identified duplicate formula and magic-tuning opportunities, but the mandatory `random_list` inspect timed out after 180 seconds, so no normalized or bounded MCP result is claimed.

Recommended owner follow-up: expose the lists as named manifests/constants, define whether profile selection is intended to be uniform or weighted after eligibility filtering, then rerun inspect/evaluate/sweep with declared Chaos-tier scenarios.

## Event, decision, focus, world-end, and super-event observations

The source inventory shows `ai_chance` across Event 1–20 packages, including `events\001_communism_spread.txt`, `events\002_zombie_outbreak.txt`, `events\003_the_holy_realm.txt`, `events\004_random_war.txt`, `events\005_soviet_collapse.txt`, the many `events\006_independence_wave_*.txt` files, `events\007_fury.txt`, `events\008_tensions_rising.txt`, `events\009_white_peace.txt`, `events\011_secret_alliance.txt`, the `events\012_*.txt` package, `events\013_natural_disasters.txt`, `events\014_cannibalism.txt`, `events\015_utopia_manifesto.txt`, the `events\016_*.txt` package, `events\017_join_faction.txt`, `events\018_random_resource.txt`, `events\019_infantry_spawn*.txt`, `events\020_black_death.txt`, and the separate Fallout world-end package.

Decision AI-score surfaces were inventoried under `common\decisions\001_*` through `common\decisions\020_*`, and focus AI-score surfaces under `common\national_focus\003_*`, `005_*`, `006_*`, `007_*`, `010_*`, `012_*`, `014_*`, `015_*`, `016_*`, `018_*`, `019_*`, and `020_*`.

The MCP batch inspect for Event-option sources 001–020 returned internal errors for the batch and `ARTIFACT_STORAGE_LIMIT` for Event 020; individual retry for `events\019_infantry_spawn_scenario.txt` also timed out after 180 seconds.

Therefore no exact option probability, option rank dominance, unreachable-candidate claim, decision click probability, focus selection probability, or cross-event comparison is made for uninspected roots.

Event 002’s decision result is score-only; positive `ai_will_do` values are not click probabilities.

Event 003’s focus result is score-only/unresolved; the adapter requires a complete available focus pool plus external factors, prerequisites, bypasses, and strategy state.

The world-end catalog in `common\scripted_effects\chaosx_events_log_effects.txt:1102-1298` registers scenario IDs, owner events, super-event IDs, visibility, sort order, default-enabled state, and disable flags; `:1358-1471` evaluates boolean active/available status; `:1474-1506` selects by row index and toggles disabled state.

World-end selection is deterministic registry sorting plus availability, not a weighted candidate race; the associated super-event ID is a mapping field, not a weighted super-event draw.

Event 016’s super-event path in `common\scripted_effects\016_brilliant_scientist_super_event_effects.txt` queues explicit IDs FIFO and dispatches the first queue element when no super-event is visible; the weighted host/facility/foreign actor builders in `common\scripted_effects\016_brilliant_scientist_effects.txt` are separate candidate-selection surfaces and remain MCP-unresolved.

## Scenario completeness and analysis decisions

`CR_CLEANUP_MTTH_002_BASELINE_2026_08_22`: candidate IDs were complete for the six inspected roots, but state was incomplete for flags, targets, country relations, variables, and hidden triggers; result unresolved.

`CR_CLEANUP_MTTH_002_EXACT_2026_08_22`: candidate pool was complete for `chaosx.nr2.3`, but the adapter could not encode the named `has_zombie_outbreak` flag as a scalar fixture; arithmetic trace exact, runtime activation unresolved.

`CR_CLEANUP_DECISION_002_SCORE_2026_08_22`: all 13 discovered decision candidates were supplied, but external country/state/flag/idea/war/variable inputs were incomplete; result score-only and partial.

`CR_CLEANUP_FOCUS_003_SCORE_2026_08_22`: the discovered 111-focus source was analyzed without a complete available pool, prerequisites, bypasses, external factors, or strategy plans; result score-only/unresolved.

No custom weighted-pool scenario had a complete manifest; no `probability_sequence` run was valid.

No before/after source pair or accepted candidate comparison existed in this read-only baseline; `probability_compare` was not applicable.

No uncertain input distribution or seed contract was declared; `probability_simulate` was not justified.

No stable numeric trigger range with a complete candidate pool was available; `probability_sweep` was not justified.

## MCP blockers and stale evidence

The parallel Event-option inspect batch for 001–020 returned `INTERNAL_ERROR` for most sources and `ARTIFACT_STORAGE_LIMIT` for Event 020.

`random_list` inspect for `common\scripted_effects\chaosx_settings_effects.txt`, `random_list` inspect for `common\scripted_effects\chaosx_triggerable_scenarios_effects.txt`, `random_list` inspect for `common\scripted_effects\018_resources_found_prefire_effects.txt`, and `direct_random` inspect for `events\013_natural_disasters.txt` each timed out after 180 seconds.

`custom_weighted_pool` inspect for `common\scripted_effects\016_brilliant_scientist_effects.txt` timed out after 180 seconds.

The Event 002 MTTH inspect retry later timed out after 180 seconds, so the successful artifacts above are preserved as the usable baseline rather than repeatedly re-running an overloaded route.

The probability render requested for analysis `probability-544a422365e094e969c72fcb` returned `PROBABILITY_ANALYSIS_STALE` because the evaluation revision `f0d028199a3b254b15a74355d155f0404c0ca4de89de39d9cc33e94c9475f460` no longer matched the current source revision; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bd6ad91e36194fb99f0e51bc0d1072fe199b25c738dbc15259ebb75c5fcb86da/dd61c84621e648b4a8d8b01d7411e79cf045989d62fe0269bd38a1219d884da5/probability-544a422365e094e969c72fcb.json` is retained only as a stale diagnostic and not as valid rendered timing evidence.

The focus render returned `ARTIFACT_STORAGE_LIMIT`; no focus render URI exists.

No probability ranking, sensitivity, threshold, sequence, comparison, or simulation artifact is claimed beyond the returned inspect/evaluate artifacts and the structural Event 002 render artifacts listed above.

## Recommended cleanup sequence for the owning agents

1. Define one authoritative live automatic-event registry and one explicit legacy/rework registry, then add a complete MCP custom-pool manifest that records type, category, disabled status, weight, cap, Chaos gate, fired gate, and special prefire context.

2. Decide and document the unavailable-repeatable weight policy, patch only through the owning gameplay agent, and run `probability_compare` using named gated/un-gated scenarios that cover stale accumulation and re-entry.

3. Centralize inactive-floor, weight-scale, recovery-step, shared event IDs, timer multipliers, cap increments, and cluster roll constants; reconcile the `20` recovery constant with stale `40` comments before retuning.

4. Publish complete cluster manifests, including Event 013’s five seasonal slots, optional participation, danger/order strata, per-tier delay ranges, cluster cooldown, context recovery, and terminal queue behavior, then use `probability_sequence` and `probability_sweep`.

5. Split and inspect each Event-option root rather than whole multi-root files, and declare hidden triggers, target scopes, candidate pool, and external factors before making any probability or unreachable-candidate claim.

6. For decisions and focuses, supply complete AI score races and strategy/prerequisite state; report rank/score changes separately from click probabilities.

7. Treat world-end row selection, force/manual selection, and scripted-GUI toggles as deterministic/availability or bypass paths unless an explicit weighted adapter contract is added.

No recommendation above was applied in this handoff.

## Completion and remaining uncertainty

Completed: required documentation/skills/wiki/vanilla references, read-only source inventory, shared selector semantics, cluster/world-end/triggerable/super-event source review, first MCP inspect per successfully attempted weighted surface, named scenario evaluations, artifact/revision/hash capture, structural Event 002 and Event 003 MCP evidence, and blocker recording.

Blocked: full Events 1–20 option/decision/focus MCP coverage, complete cluster/custom-pool sequence analysis, triggerable random-list normalization, Event 016 weighted builder normalization, valid probability rendering for the stale MTTH analysis, and focus rendering due the exact MCP timeout/storage errors above.

No gameplay or interface changes were made, and no exact runtime probability is asserted where the candidate pool or external state was incomplete.
