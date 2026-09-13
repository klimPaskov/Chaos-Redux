# Event 028 Asteroid Incoming: Baseline AI and Probability Audit

> Historical baseline only. The implementation has since replaced the legacy Event 028 source and added the Event 028 AI and recovery weights. The current disposition and authoritative blockers are in `../final_audit.md`; this file is retained to preserve the preimplementation evidence.

Audit date: 2026-08-29.

Audit mode: read-only baseline review for the Event 028 package.

Scope: opening target-choice weights, target-country and target-state selection, global Event 028 pool registration, hidden impact entry points, planned recovery decision AI, and the named AST_AI_01 through AST_AI_10 and recovery scenarios.

No gameplay, AI, event, decision, scripted effect, scripted trigger, localisation, or other runtime source was changed by this audit.

## Executive result

The requested runtime probability pass is blocked because the callable tool inventory for this turn exposes no hoi4.probability_inspect, hoi4.probability_evaluate, hoi4.probability_sweep, hoi4.probability_simulate, hoi4.probability_sequence, hoi4.probability_render, or hoi4.probability_compare route.

The matching structural hoi4.event_inspect and hoi4.event_render routes are also not callable.

The repository does register an hoi4-agent-tools MCP server in .codex/config.toml, but no callable hoi4 MCP tools are exposed in this runtime.

Therefore this handoff contains source-derived facts and specification coverage findings only.

Source-only reasoning is not runtime evidence.

The current Event 028 implementation does not expose the planned four candidate entries as a complete weighted choice surface.

The current source has three duplicated three-target option layouts plus a miss option, no explicit ai_chance weights, no target-state identity in the option pool, no target suitability scorer, and no Event 028 recovery decision category or action AI.

The current event-system registry classifies Event 028 as repeatable, while the specification describes a global fire-once major event.

This classification mismatch changes event-pool repetition, cap, recovery, history, and pacing behavior and must be reconciled by the implementation owner before probability conclusions can be drawn.

## Required reading completed

I read AGENTS.md and all 23 files under docs/specs/028_asteroid_incoming_specs/.

I read .agents/skills/chaos-redux-subagents/SKILL.md, .agents/skills/chaos-redux-events/SKILL.md, .agents/skills/chaos-redux-decisions-missions/SKILL.md, .agents/skills/chaos-redux-mtth/SKILL.md, and .agents/skills/chaos-redux-event-planning/SKILL.md.

I read the current auditor configuration in .codex/agents/chaosx_ai_probability_auditor.toml.

There is no standalone probability or weighted-logic SKILL.md under .agents/skills.

The current probability guidance is supplied by AGENTS.md, .codex/agents/chaosx_ai_probability_auditor.toml, chaos-redux-subagents, chaos-redux-events, chaos-redux-decisions-missions, chaos-redux-mtth, chaos-redux-event-planning, and 028_asteroid_incoming_ai_probability_prompt.md.

I read the required offline Paradox wiki pages:

- paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md
- paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md
- paradox_wiki/Effects - Hearts of Iron 4 Wiki.md
- paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md
- paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md
- paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md
- paradox_wiki/On actions - Hearts of Iron 4 Wiki.md
- paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md
- paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md
- paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md
- paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md
- paradox_wiki/Map modding - Hearts of Iron 4 Wiki.md

I read the relevant installed vanilla documentation in C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation:

- effects_documentation.md
- triggers_documentation.md
- modifiers_documentation.md
- dynamic_variables_documentation.md
- script_concept_documentation.md
- script_math_functions.md
- loc_objects_documentation.md
- loc_formatter_documentation.md

The relevant semantic references state that ai_chance is proportional event-option sampling, ai_will_do is a highest-score AI race, MTTH is a timing distribution, and random_list is weighted effect selection.

## MCP route status

| Required route | Status | Exact blocker and evidence |
| --- | --- | --- |
| hoi4.probability_inspect | Blocked before first adapter call | No callable hoi4 or probability tool was present in the current runtime tool inventory. |
| hoi4.probability_evaluate | Unavailable | No callable probability adapter route. |
| hoi4.probability_sweep | Unavailable | No callable probability adapter route. |
| hoi4.probability_simulate | Not run | No callable adapter and no unresolved input was authorized for sampling. |
| hoi4.probability_sequence | Not run | No callable adapter and no complete implemented custom pool with cadence and state transitions exists. |
| hoi4.probability_render | Unavailable | No callable probability adapter route. |
| hoi4.probability_compare | Not run | No callable adapter and no owner-applied candidate patch exists for a before-and-after comparison. |
| hoi4.event_inspect | Unavailable | No callable structural event adapter route. |
| hoi4.event_render | Unavailable | No callable structural event adapter route. |

No MCP adapter revision, artifact URI, scenario hash, comparison id, or rendered evidence path was produced.

No source-only result below should be treated as an MCP engine trace.

## Audited surfaces and source inventory

| Surface | Source or identifier | Baseline finding | Result classification |
| --- | --- | --- | --- |
| Opening event | events\028_asteroid_impact.txt:22-109, chaosx.nr28.1 | Legacy target-country prediction event with ten duplicated target-position options and one miss option. | Exact source fact; runtime unresolved. |
| Hidden impact event | events\028_asteroid_impact.txt:110-247, chaosx.nr28.2 | Hidden resolution uses random_owned_state and has no locked target-state input. | Exact source fact; scope and runtime result unresolved. |
| Slot layout randomizer | events\028_asteroid_impact.txt:47-51 | Three source branches with weights 33, 33, and 33. | Exact source-weight ratio; not the four-option AI pool. |
| Event 028 global pool entry | common\scripted_effects\chaosx_logic_effects.txt:274-326 | Event id 28 is registered in global.repeatable_events. | Exact source fact; runtime active-pool membership unresolved. |
| Default event enablement | common\scripted_triggers\chaosx_settings_triggers.txt:10-33 and common\scripted_effects\chaosx_logic_effects.txt:349-363 | Event 28 is absent from the default reworked-event allowlist and is consequently added to global.disabled_events during initialization. | Exact source fact; save-specific state unresolved. |
| Global random-event selection | common\scripted_effects\chaosx_settings_effects.txt:4329-4442 | Complete global.all_events traversal, active-candidate filtering, scaled weights, random roll, and cumulative selection. | Exact selection rule in source; runtime pool probability unresolved. |
| Repeatable event recovery | common\scripted_effects\chaosx_logic_effects.txt:986-1043 and :1113-1152 | Eligible repeatable weights recover from zero to one, then to the configured recovery rate, then by the recovery step, capped by the reduced cap after firing. | Exact source rule; Event 028 behavior is incompatible with the planned fire-once contract. |
| Target suitability scoring | common\scorers\ and Event 028-specific scripted helpers | No Event 028 scorer or target-suitability helper was found. | Unresolved planned surface. |
| Protected relations | events\028_asteroid_impact.txt and Event 028-specific scripted helpers | No ally, guarantee, subject, faction, opinion, or war-relation protection test was found in the Event 028 source. | Exact source absence; runtime behavior unresolved. |
| MTTH and Event 028 ai_will_do | common\mtth\chaosx_mtth_variables.txt, common\decisions\, common\ai_strategy_plans\ | No Event 028 MTTH entry, decision ai_will_do block, or Event 028 AI strategy factor was found. | Unresolved planned surface. |
| Recovery decision category | common\decisions\ and common\decisions\categories\ | No Event 028 category or Event 028 recovery action file was found. | Exact source absence; all recovery results unresolved. |
| Hidden cross-system impact calls | events\070_africa_gods.txt:284, :311, :341 | Other event branches directly fire chaosx.nr28.2 from weighted random lists. | Exact source fact; scope and exploit outcome unresolved. |
| Impact callback | common\on_actions\chaosx_famine_migration_on_actions.txt and docs\plans\famine_and_migration_system_plans\subagent_handoffs\owner_callback_census.md | Existing owner handoff identifies the generic on_nuke_drop callback as the sole nuclear aftermath adapter for the legacy launch_nuke call. | Source and handoff fact; no probability conclusion. |

## Semantic rules used for this audit

The offline AI modding reference states that ai_will_do selects the highest score from an AI race and that ai_chance uses weights proportionally for event options.

The offline Event modding reference states that an event option without ai_chance uses the engine default option weight of one.

The same reference states that ai_chance is evaluated over the visible option pool and does not mean that an authored score is a willingness score.

The offline AI and MTTH references state that an MTTH entry is a timing distribution and must not be reported as a direct selection probability.

The offline Effects reference and installed effects documentation state that random_list entries are selected proportionally to their weights and that modifiers can change those weights.

The offline Decision modding reference states that decisions use ai_will_do scores and that the AI defaults to zero for a decision without an ai_will_do block.

The installed dynamic-variable documentation confirms native state inputs for owner, controller, population, buildings, distance, and strategic value, but none of those inputs are wired into the current Event 028 selection surface.

## Major-event option precedents

The existing event option pools use explicit ai_chance blocks when the AI outcome is intended to be weighted.

events\030_time_traveler.txt:99-121 uses explicit 90 and 10 ai_chance bases for a two-option event choice.

events\030_time_traveler.txt:126-145 uses explicit 60 and 40 ai_chance bases for another two-option choice.

events\044_space_race.txt:41-82 uses an explicit 100 ai_chance base for its one-option AI-visible choice.

These are source precedents for making Event 028 option weights explicit and reviewable.

They do not provide Event 028 target scores or replace the required MCP evaluation.

The current Event 028 source contains no comparable ai_chance block.

## Implemented opening option pool

The current root event is chaosx.nr28.1 in events\028_asteroid_impact.txt.

The event has a five-day timeout and schedules chaosx.nr28.2 eight days after the random-country block at events\028_asteroid_impact.txt:28-37.

The source selects a random country satisfying num_of_controlled_states > 10 and stores its id in global.asteroid_country.

It then selects two random_other_country entries with the same state-count gate and tag exclusions at events\028_asteroid_impact.txt:38-45.

This is not the planned three distinct valid country/state pairs.

It does not verify the chooser exclusion, a viable backup state, land adjacency, population, settlement, industry, logistics, crater validity, or state survival during the lock.

It does not score unique land states within three adjacency steps, direct neighbors, population, industry, logistics, victory points, supply, rail, air, naval value, or isolation.

The source randomizes the visible layout with three equal branches:

| Layout branch | Raw source weight | Visible target options | Correct-answer flag |
| --- | ---: | --- | --- |
| asteroid_location_options_1 | 33 | chaosx.nr28.1.a, .b, .c | .a sets asteroid_location_guessed |
| asteroid_location_options_2 | 33 | chaosx.nr28.1.e, .f, .g | .f sets asteroid_location_guessed |
| asteroid_location_options_3 | 33 | chaosx.nr28.1.h, .i, .j | .j sets asteroid_location_guessed |

The three layout weights have an exact source ratio of 33:33:33.

The source ratio is a random-list layout choice and is not an AI option score or a four-candidate target probability.

Within a single layout branch, the three target options and chaosx.nr28.1.k are the apparent four visible options.

The event defines no ai_chance block for any option.

Under the offline engine semantics, the authored raw ai_chance score is therefore absent and the implicit score is one for each visible option.

The source-level ordering is a complete tie among the visible options if exactly one layout flag is present and all four options are visible.

No normalized selection probability is reported because the visible pool is not stable: the current source has eleven option blocks, the layout flags are not cleared in events\028_asteroid_impact.txt, and repeated firing can leave multiple layout flags active.

The current option pool is also not the planned pool because the three target entries carry country labels only and resolve the state later through random_owned_state.

The planned pool is target pair one, target pair two, target pair three, and miss.

The implementation pool is duplicated target-position branches, target-country ids, a later unscored random state, and miss.

The planned pool is complete conceptually in the specification, but the implementation pool is incomplete for normalization and target validity.

Opening option result: unresolved.

Opening option raw-score result: bounded source semantic only, with an implicit default of one per visible option and no authored differentiation.

Opening option normalized-probability result: unresolved.

Opening option ordering result: score-only source tie under the single-layout assumption, not a runtime probability result.

The correct-answer flags asteroid_location_guessed are set by options .a, .f, and .j, but no AI weight distinguishes them from the two wrong target guesses or the miss.

The current source also does not clear asteroid_location_guessed, asteroid_location_options_1, asteroid_location_options_2, asteroid_location_options_3, or global.asteroid_country in chaosx.nr28.2.

Those uncleared values are hidden external inputs for repeat firing and can change the visible pool or predicted branch independently of the current opening transaction.

## Current hidden impact and target-state inputs

chaosx.nr28.2 is hidden and triggered only at events\028_asteroid_impact.txt:110-116.

Its immediate block clears global.rand_country_1 and global.rand_country_2 but does not clear global.asteroid_country.

The predicted branch tests FROM for asteroid_location_guessed and then uses random_owned_state.

The unpredicted branch also uses random_owned_state and applies a materially different damage package.

There is no saved event target or state id for the state selected at the opening event.

There is no two-day lock record for a country/state pair.

There is no fail-closed invalid-state branch tied to a locked state.

There is no complete candidate-pool trace for random_owned_state.

The hidden event therefore contains an unresolved scope dependency: the state used by random_owned_state, ROOT, FROM, and PREV depends on the event firing context, which differs between chaosx.nr28.1 and the direct chaosx.nr28.2 calls from events\070_africa_gods.txt.

The existing owner_callback_census.md and event_adapter_owner_map.md handoffs identify the legacy launch_nuke call at events\028_asteroid_impact.txt:129-135 and :180-187 as covered by the generic on_nuke_drop owner.

That callback is a hidden external effect input for casualty and pressure accounting, not an Event 028 AI choice weight.

The audit did not reclassify or duplicate that callback.

## Global Event 028 pool and pacing

common\scripted_effects\chaosx_logic_effects.txt:274-326 registers event id 28 in global.repeatable_events.

common\scripted_effects\chaosx_logic_effects.txt:328-346 appends repeatable events to global.all_events.

common\scripted_effects\chaosx_logic_effects.txt:349-363 adds every event absent from event_log_event_is_reworked_default_enabled to global.disabled_events.

common\scripted_triggers\chaosx_settings_triggers.txt:10-33 lists the default-enabled ids and does not list 28.

On a fresh initialization following that source path, Event 028 is therefore disabled in the shared random pool unless another owner enables it.

common\scripted_effects\chaosx_logic_effects.txt:365-398 initializes ordinary event weights and caps to global.default_event_weight, whose event-system default is 1000 in common\script_constants\event_system_constants.txt.

Because Event 028 is in the repeatable array, the repeatable recovery path at common\scripted_effects\chaosx_logic_effects.txt:986-1043 and :1113-1152 can reset, recover, and cap its weight if it is enabled and fired.

The source-level repeatable recovery behavior is exact as a state transition rule.

The probability of Event 028 among the global active pool is unresolved because no runtime active candidate pool, save state, or probability adapter is available.

The source does not support a claim that Event 028 has a fixed or exact global firing probability.

The specification requires Event 028 to behave as a global fire-once major event.

The current registry instead gives it repeatable recovery, repeated eligibility after firing, a reduced cap, and direct hidden-entry callers.

This is a repetition and event-type contradiction, not a balance target.

The Event 028 idea file at common\ideas\028_asteroid_impact_ideas.txt:7-20 contains only the asteroid_prediction_correct country idea and a research_speed_factor modifier.

That idea has no ai_will_do, ai_chance, MTTH, or target-selection weight and is not a weighted surface.

## Direct hidden callers and repetition risk

events\070_africa_gods.txt:284 directly fires chaosx.nr28.2 as one 10-weight branch among five branches.

events\070_africa_gods.txt:311 directly fires chaosx.nr28.2 with a one-day delay and one-to-four random days as one 10-weight branch among five branches.

events\070_africa_gods.txt:341 directly fires chaosx.nr28.2 with a one-day delay and one-to-four random days as one 10-weight branch among four branches.

Those random-list weights are source-level branch weights for the Africa event, not Event 028 opening-option probabilities.

They bypass chaosx.nr28.1, the planned four-option pool, the planned three-pair construction, and the planned target lock unless another unobserved wrapper supplies that state.

The direct calls also create an unresolved ROOT/FROM/PREV scope path for the hidden impact event.

This is a positive-path repetition and invalid-context risk that requires owner review before any probability claim.

## Target scoring and protected relationships

No Event 028 scorer was found under common\scorers\.

No Event 028 target-suitability scripted trigger or scripted effect was found under common\scripted_triggers\ or common\scripted_effects\.

The current source has no target_trigger, target_root_trigger, scorer, relation modifier, or relation-protection helper for the opening choices.

The specification requires a valid country/state pair pool with three distinct country/state pairs and a genuine miss.

The specification requires country and state validity gates, backup-state viability, settlement and population checks, non-wasteland checks, adjacency, and survival through the lock.

The specification assigns suitability emphasis to unique states within three adjacency steps, population, industry and logistics, and victory points or national significance, with isolation penalties and diversity constraints.

The current source has none of those score inputs.

The specification scenarios require subject and faction-ally targets to score zero or a proven protected minimum in AST_AI_06.

AST_AI_10 requires ally, guarantee, and subject targets to leave miss effectively certain.

The current Event 028 source has no is_ally_with, has_guaranteed, is_guaranteed_by, is_subject_of, is_in_faction_with, has_war_with, or has_opinion protection check.

The native relation triggers exist in the offline wiki and installed vanilla documentation, but their existence does not establish Event 028 protection.

Protected-relationship score result: no authored protection found; runtime result unresolved.

Protected-relationship normalization result: unresolved because no complete four-entry pool or protected floor is implemented.

## Recovery decision AI surface

No Event 028 recovery decision category, decision action, mission, or Event 028 ai_will_do block exists in common\decisions\ or common\decisions\categories\.

The planned recovery actions in the specification are:

- Deploy mobile hospitals
- Open an emergency rail corridor
- Clear unstable debris
- Distribute emergency water and filters
- Rebuild a supply spine
- Restore outer-ring industry
- Rehouse displaced workers
- Reconnect the national network
- Harden factories against dust
- Protect transport and reserves
- Join the atmospheric observation network
- Secure the crater perimeter
- Survey extraordinary material
- Fortify access routes
- Bounded rival reconnaissance and disruption

The planned missions include Keep the rescue route open, Stabilize the damaged zone, Restore the outer ring, Reconnect the national network, and Rebuild the regional economy for the original target.

No exact decision ids, candidate pool, availability trace, cost trace, ai_will_do base, modifier factors, cooldown, active-mission cap, or terminal state is implemented for those actions.

No raw recovery AI scores are available.

No normalized recovery selection probability is available or implied.

If implemented with ai_will_do, these actions must be evaluated as a willingness-score race rather than as a probability distribution.

The existing precedent at common\decisions\016_brilliant_scientist_former_host_recovery_decisions.txt:16-190 uses availability gates, concrete equipment and factory costs, cancellation logic, and constant-backed ai_will_do bases and factors.

The existing natural-disaster precedent at common\decisions\013_natural_disasters_decisions.txt:868-905 uses target validity, cost ability, capital, population, and industry factors and explicitly sets invalid or presentation-only cards to ai_will_do factor zero.

Those precedents provide structural guidance only and are not Event 028 runtime evidence.

Recovery AI result: unresolved and unimplemented.

## Named opening scenarios

The candidate pool required by every row below is the complete planned set:

1. TARGET_1: first locked valid country/state pair.
2. TARGET_2: second locked valid country/state pair.
3. TARGET_3: third locked valid country/state pair.
4. MISS: no impact.

The target identifiers are not concrete source identifiers because the package specifies dynamic selection.

The specification supplies qualitative scenario states but not exact country tags, state ids, numeric target suitability values, relation values, capitulation fractions, stability values, war-support values, strategy factors, or seeds.

The planned pool is therefore conceptually complete but not adapter-ready.

The implementation pool is incomplete for every row.

All result classifications in the table are unresolved.

The expected ordering column is a specification expectation only and is not an observed MCP result.

| Scenario id | Declared state and planned pool | Specification expectation | Raw scores and ordering observed | Candidate and external-input completeness | Classification |
| --- | --- | --- | --- | --- | --- |
| AST_AI_01 | Stable democratic major at peace; TARGET_1, TARGET_2, TARGET_3, MISS; three neutral or friendly targets. | MISS should dominate every strike option. | No Event 028 authored scores; current visible branches are implicit-default ties when one layout is active; no runtime ordering. | Planned four entries declared, but exact pairs, values, relations, and save state are missing; implementation pool is not the planned pool. | Unresolved. |
| AST_AI_02 | Democratic major losing an existential war; one hostile major and two neutrals. | MISS remains strong; only hostile major is plausible. | No target score, war-state factor, capitulation factor, or normalized result. | Qualitative hostile and neutral relations declared; exact war, capitulation, target values, and complete source pool unavailable. | Unresolved. |
| AST_AI_03 | Fascist major in total war; enemy faction leader, weak enemy, neutral. | Faction leader ranks first or close to MISS; neutral remains near zero. | No ideology, war, faction, or target-value score exists; no ordering. | Planned candidates named by role only; exact faction and target state inputs unavailable. | Unresolved. |
| AST_AI_04 | Nonaligned minor at peace; three unrelated majors. | MISS strongly dominates. | No minor-country, peace, target-value, or miss-protection score exists; no ordering. | Qualitative chooser and targets declared; exact tags, states, values, and source pool unavailable. | Unresolved. |
| AST_AI_05 | Destructive special actor; three enemies. | Best strategic enemy can dominate MISS when route identity supports use. | No route-identity input, destructive-actor gate, target score, or normalized result exists. | Route identity is qualitative and not exposed by implementation; exact target values unavailable. | Unresolved. |
| AST_AI_06 | Ordinary country; subject, faction ally, enemy. | Subject and ally score zero or protected minimum; enemy competes with MISS. | No relation protection, protected minimum, enemy factor, or ordering exists. | Relations are declared by role only; no complete source pool or relation trace. | Unresolved. |
| AST_AI_07 | Fragile chooser at 700 Chaos with fragmentation; one strong enemy, compared with otherwise identical 500 Chaos. | Fragmentation risk raises MISS preference at 700 relative to 500. | No fragmentation state, mineral-site state, fragile-chooser factor, or sweep result exists. | Chaos values are declared, but exact fragmentation state, target pair, score factors, and comparison route are unavailable. | Unresolved. |
| AST_AI_08 | Near-capitulation chooser at 700 Chaos; one existential enemy. | Enemy strike becomes materially more likely than for a stable chooser. | No capitulation-progress factor, existential-war factor, or ordering exists. | Chaos and qualitative capitulation are declared; exact progress, target value, and external modifiers unavailable. | Unresolved. |
| AST_AI_09 | Chooser controls several mineral sites; one distant enemy. | MISS gains weight because new fragments can threaten the existing advantage. | No mineral-site ownership input, distance penalty, fragmentation factor, or ordering exists. | Qualitative mineral and distance state declared; exact sites, control, distances, and pool unavailable. | Unresolved. |
| AST_AI_10 | Ally, guarantee, and subject as all three targets. | MISS is effectively certain. | No relation protection or miss floor exists; no runtime result. | Relations are declared by role only; complete exact target pair pool and relation trace unavailable. | Unresolved. |

No AST_AI scenario has an exact, bounded, sampled, or score-only runtime result because the required probability adapter and implementation surface are unavailable.

The only score-only statement is the source-semantic observation that the legacy visible options have an implicit equal default when visible and unmodified.

That observation does not establish the required scenario ordering.

## Recovery decision scenarios

The package does not assign ids to the recovery bullets.

This handoff uses AST_REC_01 through AST_REC_07 as audit labels only; they are not implementation identifiers.

| Audit label | Declared situation | Required decision behavior | Implemented pool and raw score trace | Normalization and result |
| --- | --- | --- | --- | --- |
| AST_REC_01 | High preventable deaths with adequate equipment. | Deploy mobile hospitals should outrank non-medical recovery actions. | No Event 028 category, action, availability gate, or ai_will_do score. | No decision normalization; unresolved. |
| AST_REC_02 | Capital supply disconnection. | Open an emergency rail corridor should be prioritized when reserve floors permit. | No rail action or route-validity score exists. | No decision normalization; unresolved. |
| AST_REC_03 | Active frontline collapse with low train reserve. | Expensive rail and reconstruction actions should be blocked or suppressed. | No train-reserve trigger, front-collapse factor, cost gate, or score exists. | No decision normalization; unresolved. |
| AST_REC_04 | Severe dust with strong industry. | Harden factories against dust should be preferred over lower-impact global contribution. | No dust-stage action, industry factor, or ai_will_do block exists. | No decision normalization; unresolved. |
| AST_REC_05 | Controlled main crater under threat. | Secure the crater perimeter should outrank optional survey or mitigation when valid supplied forces exist. | No crater action, supplied-division gate, threat factor, or score exists. | No decision normalization; unresolved. |
| AST_REC_06 | Distant enemy fragment site with homeland defense pressure. | Rival fragment action should not override urgent homeland defense. | No fragment target, distance factor, homeland-defense score, or action pool exists. | No decision normalization; unresolved. |
| AST_REC_07 | Urgent national damage with an otherwise available global observation contribution. | National recovery should delay Join the atmospheric observation network until reserve floors are met. | No national-damage factor, reserve-floor gate, observation action, or score exists. | No decision normalization; unresolved. |

No recovery scenario can be classified as exact, bounded, sampled, or score-only from the implemented surface.

## Sensitivity sweeps and comparisons

No sweep was run because hoi4.probability_sweep is unavailable and the Event 028 weighted surface is not implemented.

The following required sweep dimensions remain unresolved:

- Chaos from 0 through 999.
- Capitulation progress from safe to near defeat.
- Relation from ally through neutral to active enemy.
- Target value from weak minor to hostile faction leader.
- Fragmentation off versus on.
- Chooser stability and war support.
- Chooser route identity.

No exact rank-reversal threshold, dominance threshold, starvation threshold, or timing threshold was obtained.

No simulation was run because no callable simulator exists and the package does not provide a complete declared uncertain-input model with seeds.

No sequence analysis was run because no complete implemented custom pool, cadence, cooldown, recovery, cap, removal, reset, or terminal-state contract exists.

No render was produced because hoi4.probability_render and hoi4.event_render are unavailable.

No comparison was run because there is no owner-applied patch and no callable hoi4.probability_compare route.

The post-patch comparison remains a required follow-up using the same AST_AI_01 through AST_AI_10 and recovery scenario inputs after the owner implements the surfaces.

## Validity, dominance, starvation, repetition, and exploit findings

Validity: the current country gate is only num_of_controlled_states > 10, and the later random_owned_state has no Event 028 validity contract.

Candidate completeness: the current pool does not contain the required three country/state pairs plus miss as explicit entries.

Protected relationships: no Event 028 relation protection or zero/protected minimum is present.

Dominance: no runtime dominance result is available, but the legacy implicit equal option scores cannot produce the specification-required miss dominance or route-sensitive enemy dominance.

Starvation: Event 028 is default-disabled in the shared pool by the current rework allowlist, so it can be starved from ordinary global selection unless another owner enables it.

Repetition: Event 028 is registered as repeatable, its flags and country variables are not cleared, and multiple direct chaosx.nr28.2 callers exist.

Timing drift: the legacy root schedules hidden impact eight days after setup while the root option timeout is five days; the planned two-day target lock and recovery cadence are not implemented.

Rank reversal: no threshold can be proven for Chaos, capitulation, relations, target value, fragmentation, stability, war support, or route identity.

Recovery starvation: the planned recovery category and actions have no implementation, so no action can win an AI score race.

Positive weight on impossible or stale choices: the legacy visible option flags, country ids, and predicted branch are not cleared by the Event 028 source, creating stale-state risk on repeat firing.

Hidden-context exploit risk: direct calls to chaosx.nr28.2 bypass the opening pool and may enter the hidden event without the planned target lock or complete ROOT/FROM/PREV context.

Nuclear-adapter risk: existing handoffs identify the generic on_nuke_drop callback as the sole owner of the legacy launch_nuke aftermath; adding a second Event 028 pressure or deaths path would duplicate effects.

Global snowball risk: if the event is enabled without reconciling repeatable versus fire-once ownership, repeatable recovery and direct hidden calls can produce repeated impact transactions and escalating destruction outside the planned one-shot contract.

## Recommended owner fixes

These are concrete implementation recommendations only.

No balance target was selected and no recommendation was applied.

1. Reconcile the Event 028 type in common\scripted_effects\chaosx_logic_effects.txt:274-326, common\scripted_triggers\chaosx_settings_triggers.txt:10-33, the event-system constants or registry used for id 28, and the Event 028 history path. The owner must decide the specification-required fire-once major contract and align active-pool membership, pacing, caps, recovery, and fired-state behavior.

2. Replace the legacy country-only random selection in events\028_asteroid_impact.txt:31-51 with an explicit transaction builder that constructs the complete TARGET_1, TARGET_2, TARGET_3, MISS pool, verifies all country and state gates, enforces distinct pairs and diversity rules, and fails closed when fewer than three pairs exist.

3. Persist the selected country/state pairs and the two-day lock with event targets or another supported transaction-owned state pointer. Preserve the selected state through control changes and fail closed to the planned near miss when the locked state is invalid.

4. Add an Event 028 target-suitability scorer and relation helper under the owner-selected common\scorers\, common\scripted_triggers\, or common\scripted_effects\ surface. The helper must expose the specification factors and explicit protected-relationship handling without assigning positive weight to invalid, blocked, stale, subject-protected, or route-incompatible entries.

5. Implement one four-entry ai_chance pool in events\028_asteroid_impact.txt with explicit target and miss identifiers. Keep ai_chance evidence separate from any ai_will_do decision evidence and do not report authored weights as click probabilities until the complete visible pool is inspected by the probability adapter.

6. Guard or reroute the direct chaosx.nr28.2 callers at events\070_africa_gods.txt:284, :311, and :341. They must not bypass the Event 028 transaction contract or fire the hidden resolver with missing locked inputs.

7. Add the planned recovery category and action files under common\decisions\ and common\decisions\categories\, with constants and scripted validity helpers. Give each meaningful action an availability gate, reserve floors, route or target validity, cooldown and cleanup, explicit ai_will_do score, and a terminal or cancellation path.

8. Define concrete implementation identifiers for AST_REC_01 through AST_REC_07 and run the decision AI audit as a score race. Use the existing Event 016 recovery and Event 013 natural-disaster conventions as structural precedents without treating their weights as Event 028 tuning targets.

9. Clear obsolete flags and variables, including asteroid_location_guessed, asteroid_location_options_1, asteroid_location_options_2, asteroid_location_options_3, and global.asteroid_country, at the transaction terminal state. Ensure repeat prevention and direct hidden-entry guards are owner-defined rather than relying on stale global values.

10. Preserve the sole generic nuclear callback ownership documented in docs\plans\famine_and_migration_system_plans\subagent_handoffs\owner_callback_census.md and event_adapter_owner_map.md. Do not add a second Event 028 deaths or pressure transaction around launch_nuke.

11. After implementation, rerun hoi4.probability_inspect first, then evaluate the complete four-entry pool for AST_AI_01 through AST_AI_10, sweep the named sensitivity dimensions, render the matrix or unresolved views, and preserve adapter revisions, artifact URIs, scenario hashes, and comparison ids.

12. After an owner-applied patch, run hoi4.probability_compare with the same named scenarios and recovery cases and check for changed ordering, miss-dominance failure, protected-target regression, action starvation, repetition, and new invalid-target weight.

## Skipped analyses and remaining uncertainty

The mandatory probability inspection was skipped only because the exact hoi4.probability_inspect route was not callable in this runtime.

All probability evaluate, sweep, simulate, sequence, render, and compare passes were skipped for the exact route and implementation reasons documented above.

The matching event structural inspect and render passes were skipped because those routes were also not callable.

No exact source-derived normalized probability is claimed for the opening event, global Event 028 pool, target selection, recovery decisions, or any sensitivity scenario.

No sampled result was produced.

No bounded runtime result was produced.

The current implicit option weight of one and the 33, 33, 33 layout weights are source semantic facts only.

The exact runtime candidate pool, visible-option cardinality after stale flags, ROOT/FROM/PREV scope behavior, current save enablement, relation state, target state, external event modifiers, strategy factors, seeds, and active global event pool remain unknown.

The specification’s expected ordering is not a baseline observation.

## Handoff conclusion

The baseline audit is complete as a read-only source and specification review but incomplete as a runtime probability audit.

The parent has the current weighted surfaces, source identifiers, raw authored or implicit values, semantic normalization rules, expected scenario ordering, protected-relationship gaps, recovery scenario coverage, repetition and starvation risks, exact MCP blockers, and owner-only recommended fixes.

The affected conclusions remain unresolved until the four-entry Event 028 pool, target-state transaction, protected relationship logic, and recovery decision AI are implemented and the mandatory HOI4 MCP probability and structural routes become callable.
