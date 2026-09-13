# Event 027 weighted-logic baseline audit

> **Superseded status notice (2026-09-01):** This dated weighted-logic baseline is preserved as historical evidence and is superseded as a current source-status authority by ../documentation_state.md. It describes the pre-rework event pool and must not drive current registration or allowlist decisions.

Date: 2026-08-29.

Scope: the pre-change Event 027 implementation, its automatic event-pool registration and firing path, the surrounding event-cluster path, native doctrine and Chaos Warfare AI surfaces, and the DR-A01 through DR-G03 scenarios in `docs/specs/027_doctrine_research_specs/027_doctrine_research_probability_scenarios.md`.

Audit mode: read-only.

Conclusion status: incomplete for probability evidence and unresolved for every scenario that requires HOI4 MCP engine analysis.

No gameplay, AI, event, doctrine, cluster, localisation, or runtime file was changed by this audit.

## Executive result

The baseline implementation does not expose the Event 027 design assumed by the scenario matrix.

The current source registers Event 027 as a fire-once event, not a repeatable event.

The root event selects one random country matching `is_major = yes OR is_ai = no`, then opens one country event after one day.

The country event exposes only four hardcoded Army Grand Doctrine actions, each with `ai_chance = { base = 25 }`.

The four actions are `new_mobile_warfare`, `superior_firepower`, `grand_battleplan`, and `mass_assault`.

The actions have no event-level trigger, availability gate, active-doctrine guard, DLC gate, country gate, doctrine-domain adapter, track adapter, subdoctrine adapter, mastery step, batch state, queue state, or recalculation step.

The current cluster registry defines eight unrelated clusters and contains no `National Breakthroughs` cluster or Event 027 member mapping.

Event 027 is also absent from the default-enabled rework trigger, so initialization adds it to `global.disabled_events` unless a later settings action explicitly enables it.

These are source facts and risk findings only.

No exact selection probability, normalized event chance, timing distribution, rank, dominance, starvation rate, repetition rate, or human-versus-AI parity result is claimed because the mandated HOI4 MCP adapter was unavailable.

## Baseline revision and repository state

The source revision observed was Git commit `4c5f0c928af1f8f69044e7ae4a237491ade8f4a5`.

The worktree was already dirty when this audit began, including unrelated staged and untracked Event 025 and Event 028 work.

Those changes were preserved and were not reverted or overwritten.

The following source SHA-256 values identify the reviewed baseline snapshot.

| Source file | SHA-256 |
| --- | --- |
| `events/027_doctrine_research.txt` | `0F7B45425081520CB57EA2CA155F22E0E018EE27D4A2C828915614F26A172D6B` |
| `common/scripted_effects/chaosx_logic_effects.txt` | `2E2AF9F8C5460E8BB0B515035C7EDB39BB9FCB12300680CFEE8E19FB012135B2` |
| `common/scripted_effects/chaosx_settings_effects.txt` | `C653396BEFCF4FDA899626DC9DF399ACE74E73ECAF23C76E148DCE6DE5A6A330` |
| `common/scripted_effects/chaosx_event_cluster_effects.txt` | `3349C3363F6E9E2D07FE541EBE6EA2D34C026E5D9BAE8F6AADD2BB1FDA4C4B5C` |
| `common/scripted_triggers/chaosx_settings_triggers.txt` | `40AC63513EECA2B74849F7041ACF3A1FDEDC9C21CAA8BF72AEEBC27102C2A42E` |
| `common/doctrines/grand_doctrines/chaos_warfare_grand_doctrine.txt` | `E4A1A7D003150F685F52D24B60FDAF7A25C40E85163272E7AACFFE9AECABCB83` |
| `common/scripted_triggers/cbrn_doctrine_triggers.txt` | `ECBFF87A22F534A6EE35F3F751181205A5F38864CA40A764BE836D8E9F40285A` |
| `common/ai_strategy/chemical_warfare_research.txt` | `936DBD20FE24F85A14EC8645594A9AB718F9536FAA27DB746E67BE12413044A8` |

## Required references consulted

The repository `AGENTS.md`, `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-mtth`, and `chaos-redux-event-planning` skills were read before the audit.

The required offline Paradox wiki core pages were consulted, including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.

The relevant offline Technology modding and Doctrine modding pages were also consulted.

The installed vanilla documentation was consulted for script concepts and constants, triggers, effects, modifiers, collections, and doctrine structure.

The installed vanilla doctrine documentation states that Grand Doctrines own tracks and that Subdoctrines own mastery and rewards.

The installed vanilla effects documentation describes `set_grand_doctrine` as activating and assigning a named Grand Doctrine and describes `set_sub_doctrine` as assigning a named Subdoctrine to a matching track.

The parent-named probability matrix and the related Event 027 core, choice-flow, doctrine-registry, and acceptance specifications were read.

## MCP evidence ledger

The first audit action was a read-only availability probe for the required probability inspection route.

| Required route | Attempt and result | Consequence |
| --- | --- | --- |
| `hoi4.probability_inspect` | `mcp__hoi4_agent_tools__probability_inspect` was not callable and was absent from the current tool registry. | No probability adapter revision, source inspection artifact, or scenario hash exists. |
| Native tool inventory fallback | `mcp__codex_apps__codex_native2_codex_tool_inventory` queried for `hoi4 probability` returned `McpServerError: MCP SSE probe returned 404 from openai.org`. | The external registry could not expose the HOI4 server in this session. |
| `hoi4.probability_evaluate` | Not callable after the required inspection route was unavailable. | DR-A01 through DR-G03 have no exact or bounded engine traces. |
| `hoi4.probability_sweep` | Not callable. | No threshold, sensitivity, or rank-reversal evidence exists. |
| `hoi4.probability_simulate` | Not callable. | No seeded sampled result exists for DR-C04 or any other scenario. |
| `hoi4.probability_sequence` | Not callable, and the current Event 027 pool and cadence are not a complete declared custom pool. | No four-firing or queue sequence result exists. |
| `hoi4.probability_compare` | Not callable, and no patched source is in this audit scope. | No before-and-after comparison id exists. |
| `hoi4.probability_render` | Not callable. | No ranking, matrix, timing, sensitivity, sequence, comparison, or unresolved-view artifact was generated. |
| `hoi4.event_inspect` and `hoi4.event_render` | Both expected `mcp__hoi4_agent_tools__event_inspect` and `mcp__hoi4_agent_tools__event_render` routes were absent. | No structural event artifact or render exists. |
| `hoi4.tech_inspect` and `hoi4.tech_render` | Both expected `mcp__hoi4_agent_tools__tech_inspect` and `mcp__hoi4_agent_tools__tech_render` routes were absent. | No structural doctrine or technology artifact or render exists. |

The equivalent `hoi4_*`-prefixed route names were also absent from the current callable registry.

No MCP adapter revision, artifact URI, scenario hash, comparison id, or rendered evidence URI is available for the parent to reuse.

Source inspection below is therefore explicitly classified as source-only or score-only and never as a substitute for MCP probability evidence.

## Audited surfaces and source map

| Surface | Baseline identifiers and source files | Current source status |
| --- | --- | --- |
| Event identity and option page | `chaosx.nr27.1`, `chaosx.nr27.2`, `chaosx.nr27.2.a`, `.b`, `.c`, `.e` in `events/027_doctrine_research.txt` | Hidden root plus one visible country page. The option page has four Army Grand Doctrine choices. |
| Automatic event registration | `global.fire_once_events`, `global.repeatable_events`, `global.all_events`, `global.event_weights`, `global.event_max_caps` in `common/scripted_effects/chaosx_logic_effects.txt` | Event ID 27 is appended to `global.fire_once_events` at line 250 and is absent from the repeatable registration. |
| Automatic event selection | `evaluate_random_event_active_pool_candidate`, `evaluate_random_event_selection_candidate`, `select_weighted_random_event_id` in `common/scripted_effects/chaosx_logic_effects.txt` and `common/scripted_effects/chaosx_settings_effects.txt` | The picker loops the registered `global.all_events` array, filters disabled and invalid unique entries, then uses stored event weights. It has no Event 027-specific eligibility branch. |
| Automatic timer entry point | `check_event_timer`, `automatic_event_firing_context`, `select_weighted_random_event_id` in `common/on_actions/chaosx_on_actions_system.txt` | The country with an active event timer selects one event when its timer reaches zero. Event 027 does not fan out to all countries. |
| Default rework enablement | `event_log_event_is_reworked_default_enabled` in `common/scripted_triggers/chaosx_settings_triggers.txt` and `initialize_default_disabled_events_for_rework_queue` in `common/scripted_effects/chaosx_logic_effects.txt` | The default-enabled list has no Event 027 branch, so the rework initializer marks ID 27 disabled unless settings remove it. |
| Cluster definitions | `initialize_event_cluster_definitions`, `event_belongs_to_cluster`, `load_event_cluster_members`, `try_fire_event_cluster_for_selected_event` in `common/scripted_effects/chaosx_event_cluster_effects.txt` and `events/chaosx_event_clusters.txt` | Current IDs are Wars, Liberations, Diplomatic Panic, Peace, Natural Disasters, Formables, Economy Positive, and Diseases. No National Breakthroughs identifier or Event 027 mapping is present. |
| Event cluster tuning | `event_cluster_id`, `event_cluster_type`, `event_cluster_member_role`, participation matrix, roll and cooldown constants in `common/script_constants/event_cluster_constants.txt` | Existing cluster cadence and optional-member machinery cannot be applied to Event 027 because no cluster member row exists. |
| History actor mapping | `events_log_set_default_actor_for_current_event` and `record_events_log_history_entry` in `common/scripted_effects/chaosx_events_log_effects.txt` | Event ID 27 has no special actor override, so the generic current-event record defaults to no actor. This source fact is not an MCP-verified history result. |
| Event log and name registration | `chaosx.event_name.27`, settings event ID 27 mapping, and Event 027 localisation in `localisation/english/027_doctrine_research_l_english.yml`, `localisation/english/chaosx_event_names_l_english.yml`, and `common/scripted_localisation/chaosx_scripted_localisation_settings.txt` | The old event name resolves to Doctrine Research. The current option page has no chained domain, Grand Doctrine, track, or subdoctrine localisation surface. |
| Catalog snapshot | Event 027 row in `docs/spreadsheets/chaos_redux_events_catalog.csv` | The export snapshot labels it `Minor Fire-Once` and `To Be Reworked`. The editable workbook remains the catalog source of truth and was not modified. |
| Native Army doctrine graph | Vanilla `common/doctrines/grand_doctrines/land_grand_doctrines.txt` | The installed graph defines the four named Army Grand Doctrines used by Event 027. Their native AI surfaces are separate `ai_will_do` score blocks. |
| Native Navy and Air doctrine graph | Vanilla `common/doctrines/grand_doctrines/sea_grand_doctrines.txt` and `air_grand_doctrines.txt` | These domains exist in the installed graph but are unreachable from the baseline Event 027 page. |
| Chaos Warfare domain | `chaos_warfare`, `extermination_columns`, `chemical_suppression`, `contaminant_firebases`, and `integrated_chemical_operations` in the Chaos Redux doctrine files | The custom domain has native establishment and AI gates, but Event 027 has no adapter or branch that can call them. |
| Adjacent CBRN research AI | `cbrn_research_*` strategy blocks in `common/ai_strategy/chemical_warfare_research.txt` | These are native research strategy factors for CBRN technologies. Event 027 contains no research effect and does not consume these factors. |

## Baseline weights, pools, and traces

### Automatic Event 027 selection

`event_system_defaults.event_weight` is `1000`, `event_system_defaults.reduce_cap_factor` is `0.5`, and `event_system_defaults.recovery_rate` is `20` in `common/script_constants/event_system_constants.txt`.

The automatic timer range starts at 45 to 60 days through `event_system_timer_defaults.min_days` and `max_days`.

`initialize_event_weights` seeds the stored weight and cap arrays for every registered event to the default weight.

Because Event 027 is registered as fire-once, the baseline stored state is 1000 weight and 1000 cap after initialization, subject to the event being disabled by the rework queue.

The current event-specific chaos registry assigns ordinary events the tier-zero requirement unless they are the special White Peace entry, so Event 027 has no source-defined higher Chaos threshold.

When explicitly enabled and unfired, Event 027 can pass the generic disabled, fired, chaos, and zero-weight checks in source terms.

That statement is not a normalized event probability because the complete current event pool, live disabled state, and all external factors were not supplied to an MCP analyzer.

The weighted selector multiplies each accepted event weight by 100, sums the accepted candidates, rolls one integer over the total, and selects the first cumulative candidate crossing the roll in `select_weighted_random_event_id`.

This source trace establishes a probability-proportional selection algorithm, not an Event 027 chance.

After a fire-once event fires, `on_fire_once_event_fired` records the event ID in `global.fired_events` and stores the engine-safe floor value `1` rather than zero.

The active-pool evaluator then rejects an already-fired non-repeatable event with the `already_fired` reason.

The repeatable handler, which reduces an individual cap and recovers the event weight, is not called for baseline Event 027.

Therefore DR-F02's stated repeatable cap reduction and monthly recovery route is not reachable in the baseline category.

### Event 027 country target and choice page

`chaosx.nr27.1` uses `random_country` with `OR = { is_major = yes is_ai = no }` and sends the selected country to `chaosx.nr27.2` after one day.

This target pool includes AI majors and every human country, including human minors, but excludes AI minors and does not test doctrine validity.

The root event does not capture a participant snapshot, iterate over valid countries, create one batch per participant, or preserve any batch-owned state.

The visible page has four options with the following score-only declarations.

| Option | `ai_chance` base | Direct effect | Source location |
| --- | ---: | --- | --- |
| `chaosx.nr27.2.a` | `25` | `set_grand_doctrine = new_mobile_warfare` | `events/027_doctrine_research.txt:47-62` |
| `chaosx.nr27.2.b` | `25` | `set_grand_doctrine = superior_firepower` | `events/027_doctrine_research.txt:63-78` |
| `chaosx.nr27.2.c` | `25` | `set_grand_doctrine = grand_battleplan` | `events/027_doctrine_research.txt:79-94` |
| `chaosx.nr27.2.e` | `25` | `set_grand_doctrine = mass_assault` | `events/027_doctrine_research.txt:95-110` |

The four score declarations have no modifiers and no option triggers.

The four event options do not call the installed doctrine `ai_will_do` blocks, so native doctrine preference factors are not part of this event-choice score trace.

The current vanilla Army Grand Doctrine definitions use `available = { always = yes }`, but the baseline Event 027 page does not check whether the target already has an active Army Grand Doctrine or whether assigning another one would replace, no-op, or otherwise alter existing state.

The exact engine result of selecting an already active doctrine is unresolved because neither `hoi4.event_inspect` nor `hoi4.probability_evaluate` was available.

Each option also calls `brilliant_scientist_record_doctrine_research` as a hidden effect.

That helper records a one-time mandate, dependence, exposure, project-capacity, independent-capacity, and grievance change only when the current country is the active Kruger host and the associated flags are absent.

This conditional side effect does not change the `ai_chance` score, but it is an external state input for any exact outcome audit.

### Native doctrine and research surfaces adjacent to Event 027

The installed vanilla Army definitions give `new_mobile_warfare` a native `ai_will_do` base of `1` with a zero factor for non-majors, `superior_firepower` a base of `1` with the same non-major zero factor, `grand_battleplan` a base of `2`, and `mass_assault` a base of `1`.

Those are doctrine-selection willingness scores, not the Event 027 option scores and not click probabilities.

The baseline event ignores these native values and supplies the same event score to all four options.

The Chaos Warfare Grand Doctrine has `available = { cbrn_chaos_warfare_adoption_capable = yes }` and a native `ai_will_do` base of `0.20` with route, readiness, profile, war, enemy-use, and nonhuman modifiers in `common/doctrines/grand_doctrines/chaos_warfare_grand_doctrine.txt:31-91`.

The four Chaos Warfare subdoctrines each retain `available = { has_doctrine = chaos_warfare }`, `visible = { always = yes }`, a base AI willingness of `1.00`, and a zero factor when Chaos Warfare is not active.

The associated track identities are `infantry`, `armor`, `combat_support`, and `operations`, and the public compatibility identities are `extermination_columns`, `chemical_suppression`, `contaminant_firebases`, and `integrated_chemical_operations`.

The CBRN adoption gate requires at least one of basic masks plus an agent technology, a completed chemical project, an established command, a historical program profile, or a scenario override.

These native CBRN score and gate surfaces are not connected to the baseline Event 027 option pool.

The CBRN research strategy file supplies separate `research_weight_factor` and `research_tech` values such as 15 for protective foundation, 60 for known threat, 150 for chemical emergency, and 100 for emergency force research.

Those values affect technology research selection only and do not provide an Event 027 doctrine score.

### Current cluster pool

`event_cluster_id` currently defines `wars`, `liberations`, `diplomatic_panic`, `peace`, `natural_disasters`, `formables`, `economy_positive`, and `diseases` in `common/script_constants/event_cluster_constants.txt:9-23`.

`initialize_event_cluster_definitions` registers those eight IDs in `common/scripted_effects/chaosx_event_cluster_effects.txt:194-268`.

`event_belongs_to_cluster` maps current event IDs to those eight IDs in `common/scripted_effects/chaosx_event_cluster_effects.txt:429-540`.

The source scan found no `event_id = 27`, `value = 27`, `nr27`, or `National Breakthroughs` branch in the cluster definition, membership, or queue files.

Consequently, the baseline Event 027 cluster candidate pool is empty rather than incomplete.

The existing cluster machinery does support required and optional rows, severity floors, effective minimum tiers, activation chance, cooldown flags, append-only probability memory, and delayed member queues.

None of those surfaces can be attributed to Event 027 until a cluster ID and member row are actually registered.

## Scenario-by-scenario baseline evidence

The classifications below separate source-only observations from the unavailable MCP result.

`Score-only` means the source declares a score but no engine-normalized selection result.

`Unresolved` means the requested MCP analysis could not be executed or the required valid candidate pool and external factors do not exist in the baseline implementation.

No scenario below has an exact, bounded, or sampled probability result.

### Group A: domain selection

- **DR-A01, Doctrine-less land major.** The root can target an AI major, but the choice page has only four Army Grand Doctrines and no Army, Air, or Navy domain pool. The four options are flat score-only `25` entries. Classification: unresolved because the required domain candidates and MCP rank trace are absent. Final inputs must include the complete Army, Air, Navy, Special Forces, Chaos Warfare, and future-domain pool with doctrine state, force composition, war, production, route, and DLC factors.
- **DR-A02, Island naval power.** The baseline page has no Navy domain or Navy Grand Doctrine, and an active Army doctrine is not checked before any of the four positive Army options. Classification: source-only starvation risk for Navy and unresolved engine result. Final inputs must include the full naval graph, fleet and dockyard state, convoy war, overseas plan, active Army progress, and all invalidation reasons.
- **DR-A03, Air-centered continental power.** Air production, air wings, air war, and air strategy do not appear in the Event 027 source, and an active Army doctrine does not create an Air candidate because no Air adapter exists. Classification: source-only Air starvation risk and unresolved probability result. Final inputs must include Air and Army candidate traces with current branch completion and strategic relevance.
- **DR-A04, Landlocked small minor.** The root excludes AI minors because its target limit requires a major or a human country. A human landlocked minor can reach the page, but the page still offers the four Army options without a Navy validity test. Classification: source-only target-pool mismatch and invalid-domain risk, with probability unresolved. Final inputs must declare whether the scenario targets a human or AI minor and provide the native Navy availability and AI score factors.
- **DR-A05, Future maritime plan.** No current coastline, planned expansion, dockyard, naval invasion, or AI strategy factor is read by Event 027, and no Navy candidate exists. Classification: source-only absence of route-aware maritime scoring and unresolved probability result. Final inputs must include the planned route, route validity at confirmation, timing, current coast, dockyard plan, and full Army/Navy pool.
- **DR-A06, All ordinary domains complete.** The baseline page has no branch that closes when all domains are exhausted and no fallback or no-option state. Its four positive Army actions remain declared even when the target's doctrine state is unknown. Classification: source-only unsafe nonempty-pool risk and unresolved engine behavior. Final inputs must include every ordinary and conditional adapter state and prove the no-candidate terminal result.

### Group B: Grand Doctrine selection

- **DR-B01, Mobile armored army.** The baseline options do not read tanks, armored divisions, open terrain, fuel, or offensive plans, and the four scores remain equal. Classification: score-only flatness and unresolved ordering. Final inputs must include every currently valid Army Grand Doctrine, native graph availability, force-fit factors, route plans, and complete external modifiers.
- **DR-B02, Manpower-rich infantry state.** The baseline options do not read infantry composition, manpower, armor production, defensive posture, or broad-front war. Classification: score-only flatness and unresolved ordering. Final inputs must include the same complete Army pool and the declared force, manpower, war, terrain, and strategy factors.
- **DR-B03, Doctrine plan conflict.** No Event 027 option reads a historical AI plan, alternate AI plan, current force mismatch, or native doctrine willingness. Classification: source-only missing conflict model and unresolved under both required plan variants. Final inputs must run the same country state under both historical and alternate plans and preserve separate modifier traces.
- **DR-B04, Invalid doctrine candidate.** All four options have positive `ai_chance` and none has an option trigger, availability block, DLC check, country gate, or active-doctrine check. Classification: source-only positive-invalid-candidate risk and unresolved engine selection behavior. Final inputs must include the invalid candidate in the declared pool with its exact invalidation reason and show that it contributes zero before normalization.

### Group C: track and branch selection

- **DR-C01, Near-complete relevant branch.** Event 027 has no track, branch, mastery level, completion, or force-fit candidate surface. Classification: unresolved and not reachable from the baseline page. Final inputs must include the active Grand Doctrine, all track states, one-step completion value, fielded armor, tank production, and the full branch pool.
- **DR-C02, Near-complete irrelevant branch.** No branch completion value or strategic mismatch factor is calculated by the baseline event. Classification: unresolved and not reachable from the baseline page. Final inputs must include both the near-complete naval branch and the relevant land branch with their completion and strategic modifiers.
- **DR-C03, Empty track fills missing capability.** No active-doctrine track page or empty-track adapter exists, so supply problems cannot affect a valid operations or logistics candidate. Classification: unresolved and source-only missing-capability risk. Final inputs must include every empty and active track, supply state, branch availability, and one-step action validity.
- **DR-C04, Four equal tracks.** There is no four-choice batch, track score, seeded Event 027 simulation, or bounded top-pool rule in the baseline. Classification: unresolved and simulation skipped because the required probability route is unavailable. Final inputs must declare the four complete track pool, seed, cadence, continuation factors, and the exact distribution target.
- **DR-C05, One dominant track.** There is no five-choice batch, stacking rule, completion removal, or post-completion recalculation in the baseline. Classification: unresolved and source-only missing-recalculation risk. Final inputs must include all five candidate tracks, expected branch completion, removal timing, and re-evaluation after every choice.
- **DR-C06, Branch completes between choices.** The baseline has no second choice, batch state, or live confirmation revalidation. Classification: unresolved and source-only stale-target risk. Final inputs must schedule the native completion between choices and show the second pool after re-reading live state.
- **DR-C07, Banked mastery on empty track.** The baseline has no empty-track selection or mastery operation. The specification itself leaves native banked-mastery ordering unresolved until a local engine sequence is proven. Classification: unresolved for both baseline behavior and the required local sequence. Final inputs must include banked mastery, native level transitions, event attribution, and a complete declared sequence only after MCP support is restored.

### Group D: custom doctrine selection

- **DR-D01, CBRN-ready Chaos Warfare country.** Chaos Warfare has a native establishment gate and native AI score factors, but Event 027 has no Chaos Warfare domain or adapter. Classification: source-only custom-domain starvation and unresolved ordering. Final inputs must include the complete ordinary and Chaos domain pool, CBRN establishment prerequisites, fielded formations, investment, unconventional plan, and downstream gate state.
- **DR-D02, CBRN-unready ordinary country.** The native Chaos Warfare gate would reject an unready country, but the baseline Event 027 source never evaluates that gate because Chaos Warfare is absent from its options. Classification: source-only absent-adapter result and unresolved parity. Final inputs must include the rejected Chaos candidate with the exact gate failure and the remaining ordinary domains.
- **DR-D03, Active Chaos Warfare, infantry-heavy formations.** The four Chaos tracks have native identities and AI willingness blocks, but Event 027 cannot select or advance any track. Classification: source-only missing custom track pool and unresolved ordering. Final inputs must include all four tracks, Hazard Assault fielding, armored-delivery and projector state, headquarters state, branch levels, and native mastery action validity.
- **DR-D04, Active Chaos Warfare, theater command need.** Integrated CBRN Command has a native operations track and route-aware AI modifiers, but the baseline event has no operations track page or CBRN trigger call. Classification: source-only custom track starvation and unresolved ordering. Final inputs must include headquarters, contamination, biological threat, air and surface coordination, operations gates, and all other valid track scores.
- **DR-D05, Special nonhuman country without adapter.** Event 027 has no special-country adapter and its root target limit can exclude an AI special minor before doctrine selection. Classification: source-only missing-adapter and target-pool risk, with no fabricated reward observed in the baseline page. Probability remains unresolved. Final inputs must declare the special scope, control type, all adapter candidates, and the no-candidate terminal behavior.
- **DR-D06, Special country with valid adapter.** No owner-defined custom adapter registry is referenced by Event 027, so a valid special-country adapter cannot enter the baseline pool. Classification: source-only absent-participation risk and unresolved result. Final inputs must provide the adapter identity, branch pool, availability, action, maximum mastery, and proof that identity classification does not suppress the country.

### Group E: multi-choice sequence

- **DR-E01, Evolution I adoption sequence.** The baseline has one country page and no evolution stage, two-choice batch, adoption receipt, active-doctrine rebuild, or second-choice page. Classification: unresolved and not reachable from the baseline flow. Final inputs must include stage snapshot, domain pool, Grand Doctrine pool, track pool, and the two sequential confirmation states.
- **DR-E02, Evolution II mixed services.** The baseline has neither a three-choice batch nor Navy, Air, or cross-domain candidates, so Army stacking, Navy adoption, and post-adoption recalculation cannot be compared. Classification: unresolved and source-only cross-domain starvation risk. Final inputs must include all three service pools and live re-evaluation after each choice.
- **DR-E03, Evolution III broad curriculum.** There is no four-choice batch, track distribution, or seeded selection result. Classification: unresolved and simulation unavailable. Final inputs must include four valid close-score tracks, seed policy, continuity factors, and the parent's target distribution.
- **DR-E04, Evolution IV branch completion.** There is no five-choice batch or branch-completion path. Classification: unresolved and source-only missing-stacking capability. Final inputs must include a complete five-level branch, all alternatives, and confirmation-time revalidation after each step.
- **DR-E05, Queue with different stages.** No active batch, ordered queue, stage snapshot, or later-firing append exists in the baseline. Classification: unresolved and not reachable. Final inputs must include one-choice and three-choice batch records, queue order, persistence fields, and closure transitions.
- **DR-E06, Evolution unlock during batch.** No batch stage is stored, so the baseline cannot preserve two choices when Evolution II becomes available. Classification: unresolved and source-only stage-snapshot omission. Final inputs must schedule the evolution transition between choices and compare active-batch size with the next normal firing.

### Group F: repeatable-event and cluster selection

- **DR-F01, Initial event pool.** The required state says Event 027 is enabled and unfired, but baseline initialization marks it disabled by default and registers it as fire-once. If settings explicitly enable it, the source-stored starting weight is 1000 and the event enters the all-events selector as a unique candidate. Classification: score-only conditional source trace and unresolved normalized chance because the complete pool and MCP inspection are missing.
- **DR-F02, After first firing.** The baseline fire-once handler records the event as fired and stores weight 1, while the repeatable handler that reduces caps and recovers weights is not called. Classification: source-only category contradiction and unresolved timing result. The stated repeatable-cap premise cannot be evaluated without an owner-applied category change and a complete pool.
- **DR-F03, Sequence through four firings.** Event 027 cannot recur through the baseline automatic pool after its first fire because the non-repeatable fired check rejects it. The current source has timer, recovery, cap, reset, and cluster machinery for other event types, but no Event 027 repeatable route. Classification: source-only non-recurrence risk and unresolved sequence. `probability_sequence` was not run because the complete event pool and declared cadence were unavailable and the MCP route was absent.
- **DR-F04, Event 027 optional cluster member.** The current cluster registry has no National Breakthroughs cluster and no Event 027 member row. Classification: source-only unreachable cluster premise and unresolved optional participation. Final inputs must provide the full cluster member array, roles, base and final chances, tier and severity factors, optional-roll state, and cluster-size terminal behavior.
- **DR-F05, Event 027 selected cluster member.** `event_belongs_to_cluster` has no Event 027 branch, so the cluster wrapper leaves the candidate cluster ID at zero and dispatches the selected event directly. Classification: source-only absent guaranteed-member route and unresolved engine dispatch. Final inputs must prove the selected-member path and the no-duplicate-fanout guard after a cluster mapping exists.

### Group G: human parity and validity

- **DR-G01, Human and AI pool parity.** The visible country page and AI page currently refer to the same four declared options, but the root country target selection differs from the intended per-country participant model and neither path has a valid adapter pool. Classification: source-only partial surface similarity and unresolved parity. Final inputs must compare the exact human-visible and AI-valid candidate arrays for one fixed country state.
- **DR-G02, DLC matrix.** The baseline Event 027 page has no DLC or graph-version condition and does not expose the Navy, Air, Special Forces, or Chaos graph. Classification: source-only missing conditional adapters and unresolved matrix. Final inputs must enumerate every supported DLC combination and include absent content as zero-participation candidates.
- **DR-G03, Invalid adapter injection.** The baseline has no adapter registry or unknown-max-mastery path to inject, and its four hardcoded options have no fail-closed candidate validation. Classification: unresolved and source-only invalid-adapter guard omission. Final inputs must inject a missing branch and unknown maximum into an adapter while keeping valid ordinary domains in the pool.

## Validity, balance, and exploit-risk findings

### Confirmed source risks

1. **Repeatable-event starvation and timing mismatch.** Event 027 is in `global.fire_once_events` at `common/scripted_effects/chaosx_logic_effects.txt:250`, so it is not part of repeatable recovery, cap reduction, or recurring sequence behavior.

2. **Default-selection starvation.** Event 027 is not in `event_log_event_is_reworked_default_enabled`, and the rework initializer adds unlisted registered events to `global.disabled_events`.

3. **Army-domain dominance by construction.** The only doctrine candidates are four Army Grand Doctrines, so Air, Navy, Special Forces, Chaos Warfare, and any future domain are structurally starved rather than merely scored lower.

4. **Flat option score surface.** Every visible AI option uses `ai_chance base = 25` with no modifier trace.

5. **Positive invalid-candidate risk.** The four options have no trigger or availability block and no check for current Grand Doctrine state, country state, DLC, or route validity.

6. **Missing no-candidate terminal state.** The baseline page has no option or effect path for a country with no valid doctrine action.

7. **Missing participant and batch state.** The root picks one country and does not create a global participant snapshot, per-country batch, ordered queue, or persistence record.

8. **Missing recalculation.** There is no second choice, live state rebuild, completion removal, or confirmation-time revalidation.

9. **Native AI bypass.** Event 027 does not consume the native Army, Navy, Air, or Chaos Warfare `ai_will_do` and strategy factors.

10. **Cluster route absent.** Event 027 cannot be an optional or guaranteed member of a National Breakthroughs cluster because that cluster is not registered in the current source.

11. **Target-pool mismatch.** AI minors cannot be selected by the root event, while human minors can be selected regardless of doctrine validity.

12. **Direct activation bypass risk.** The event calls `set_grand_doctrine` directly and does not show a source-level cost, active-doctrine, or replacement guard. Whether the engine rejects or replaces an already active doctrine is unresolved.

### Findings not proven without MCP

No dominance conclusion is proven by probability evidence.

No valid domain starvation rate is proven beyond the structural absence of those candidates from the source.

No rank reversal threshold or sensitivity interval is available.

No event timing distribution or recurrence frequency is available.

No seeded variety or repetition result is available.

No exact human-versus-AI candidate parity result is available.

No exact effect of selecting an already active Grand Doctrine is available.

No exact native banked-mastery sequence is available.

## Required final comparison inputs

The owner-applied implementation and final auditor must use the same named scenario IDs and preserve the following inputs for the mandatory `hoi4.probability_compare` pass.

| Surface | Baseline IDs | Required baseline and patched comparison inputs |
| --- | --- | --- |
| Automatic Event 027 selection | DR-F01, DR-F02, DR-F03, DR-F05 | Complete `global.all_events` candidate manifest with every event ID, type, stored weight, cap, disabled state, fired state, Chaos gate, dynamic unavailability reason, timer state, recovery cadence, cap reduction, major reset, cluster context, and terminal state. |
| National Breakthroughs cluster | DR-F04, DR-F05 | Full cluster ID and ordered member arrays with required or optional role, base chance, final chance, tier, severity, eligibility, cooldown, optional roll, selected-member guarantee, and duplicate-fanout guard. |
| Participant and target selection | DR-A01 through DR-A06, DR-G01 | Complete live country set at firing, control type, major status, special or nonhuman status, valid adapter count, snapshot date, annexation or creation changes, and batch ownership. |
| Domain selection | DR-A01 through DR-A06, DR-D01 through DR-D06, DR-E02, DR-G01 through DR-G03 | Every currently supported domain and every filtered invalid domain with domain identity, graph revision, DLC gate, route gate, active Grand Doctrine state, score factors, hard invalidation reason, and source adapter revision. |
| Grand Doctrine selection | DR-B01 through DR-B04, DR-E01, DR-E02, DR-G02 | Complete current graph in native order, all eligible Grand Doctrines, native availability, country and DLC restrictions, historical and alternate strategy plans, force-fit factors, and exact action validity. |
| Track and subdoctrine selection | DR-C01 through DR-C07, DR-D03, DR-D04, DR-E01 through DR-E04, DR-G03 | Every track and branch, selected or empty state, current level, maximum level, completion value, banked mastery, one-step action, native transition result, owner-system gate, and live confirmation recheck. |
| Batch stages and queue | DR-E01 through DR-E06 | Batch ID, stage, size, remaining choices, firing date, active and queued order, evolution state at firing, stage changes between choices, save or reload receipt, closure, and no-compensation terminal result. |
| Human and AI parity | DR-G01, DR-G02, DR-G03 | The human-visible valid pool and AI-valid pool for the exact same country state, including pagination or navigation exclusion, hard-invalid candidates, hidden candidates, adapter failure behavior, and exact effect route. |
| Chaos Warfare integrity | DR-D01 through DR-D04, DR-G02, DR-G03 | Establishment gate, protective and agent technology, completed project, command flag, historical or scenario override, fielded CBRN formations, route posture, four compatibility IDs, native mastery levels, and downstream technology, equipment, policy, and operation gates. |

The final compare pass must use the same baseline and patched scenario states, the same declared seeds where sampling is authorized, the same external-factor declarations, and the same adapter revision contract.

The final report should preserve MCP comparison IDs, artifact URIs, scenario hashes, and rendered evidence paths.

## Recommended fixes for the owner

These are recommendations only.

No gameplay or AI patch was applied.

1. Reconcile Event 027's category in `common/scripted_effects/chaosx_logic_effects.txt:224-326` with the accepted Minor Repeatable design before any repeatable timing claim is made.

2. Add the Event 027 default-enabled decision to `common/scripted_triggers/chaosx_settings_triggers.txt` only when the complete reworked surface is ready for normal selection.

3. Replace the one-country `random_country` dispatch in `events/027_doctrine_research.txt:29-34` with an owner-defined bounded participant snapshot and per-country batch allocator that handles created, annexed, civil-war, subject, exile, human, AI, and special scopes.

4. Replace the four flat `ai_chance` blocks in `events/027_doctrine_research.txt:47-110` with a registry-driven valid candidate pool that filters before scoring and uses the same candidate identities for human and AI selection.

5. Keep doctrine actions in owner-system adapters under a dedicated Event 027 scripted-effect and scripted-trigger surface, with stable identifiers for domain, Grand Doctrine, track, subdoctrine, current level, maximum level, one-step action, and invalidation reason.

6. Reuse native `set_grand_doctrine`, `set_sub_doctrine`, and the verified native mastery operation only after `hoi4.tech_inspect` or the matching structural route proves the exact transition for the installed graph.

7. Add explicit fail-closed guards for active Grand Doctrine replacement, completed branches, missing DLC, unavailable country routes, unknown adapter branch IDs, and unknown maximum mastery.

8. Add the batch and queue state machine with stage snapshot, rebuild-after-choice, confirmation-time revalidation, native banked mastery preservation, transaction receipt, save and reload persistence, and no-compensation closure.

9. Register the accepted National Breakthroughs cluster in `common/script_constants/event_cluster_constants.txt`, `common/scripted_effects/chaosx_event_cluster_effects.txt`, and the related cluster event file only if the owner confirms that cluster ownership and member cadence.

10. Preserve the existing CBRN owner gates in `common/scripted_triggers/cbrn_doctrine_triggers.txt` and `common/doctrines/grand_doctrines/chaos_warfare_grand_doctrine.txt` rather than copying their factors into a second Event 027 table.

11. Keep the Kruger history side effect separate from doctrine scoring and include its host flags and event targets in any exact external-factor declaration.

12. After the owner patch, rerun `hoi4.probability_inspect`, evaluate DR-A01 through DR-G03, sweep thresholds and rank reversals, simulate only the declared seeded uncertain cases, sequence only the complete event pool, render the review views, and compare against this same baseline scenario set.

## Skipped analyses, blockers, and uncertainty

The HOI4 probability adapter and structural event and doctrine adapters were unavailable in the current session.

The exact blocker for the probability route was an absent callable `mcp__hoi4_agent_tools__probability_inspect` route.

The exact registry fallback blocker was `McpServerError: MCP SSE probe returned 404 from openai.org` from the Native2 tool inventory probe.

All downstream probability tools were skipped rather than replaced with hand normalization, source-only arithmetic, or memory.

All structural MCP renders and inspections were skipped for the same availability reason.

No live Hearts of Iron IV process was launched.

The source scan cannot prove engine behavior for invalid `set_grand_doctrine` targets, native mastery sequencing, hidden candidate pages, or final country-scope effects.

The source scan cannot supply a complete live event pool with all current weights, disabled states, firing history, and external modifiers.

The current baseline report is therefore suitable as a source and score inventory for the owner patch, but it is not a balance approval and must not be used as the final probability comparison.

## Completion statement

Completed: required read-only source, specification, offline wiki, and vanilla documentation review; baseline weight and pool mapping; all DR-A01 through DR-G03 scenario entries; explicit MCP blocker ledger; final comparison input contract; and un-applied recommended fixes.

Blocked: every MCP-dependent probability and structural conclusion, including exact event normalization, timing, ranking, seeded variation, sequence behavior, cluster participation, and post-change comparison.

Simplifications: none were applied to gameplay or AI.
