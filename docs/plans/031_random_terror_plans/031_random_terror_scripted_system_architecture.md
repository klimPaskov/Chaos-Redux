# Event 31 Random Terror scripted-system architecture handoff

## Status and scope

This is an architecture-only handoff for Event 31 Random Terror.

No gameplay file was edited.

No Internal Fracture cluster was created or registered.

No Event UI, scripted GUI, 3D model, unit model, counter, or audio asset was created or wired.

The current worktree was not clean before this handoff was written, so unrelated parent changes were preserved and not reconciled.

The only intended file change from this pass is this handoff.

The current source, not the original design bundle, is authoritative for the baseline below.

## Executive conclusion

Event 31 has an extensive but incomplete local scaffold in common/scripted_effects/031_random_terror_effects.txt and common/scripted_triggers/031_random_terror_triggers.txt.

The accepted design cannot be wired by adding a few calls to the existing root event because the current source has no shared scenario dispatch entry, no safe eight-carrier allocation, no decision or on-action owner, no complete event-log identity mapping, no registered world-end row, no super-event or audio runtime mapping, and no cleanup transaction.

The safest implementation order is to reserve identities and carriers first, then make the root dispatch transactional, then connect the existing pressure, incident, evolution, actor, response, and action helpers to explicit owners.

The current five carrier tokens JHX, JIX, JKX, JLX, and JMX are only source references in the scaffold.

The constants file declares carrier_count = 8, so the current source cannot satisfy its own capacity contract.

SCN-014 is not free, SCN-015 is ambiguous and must be treated as reserved, cluster ID 9 is occupied by National Breakthroughs, and proposed world-end and super-event identities remain unregistered.

The current probability surface is not supported by complete MCP evidence because the direct inspect timed out and the named auditor did not return evidence during the preparation window.

## Evidence basis

The complete specification package under docs/specs/031_random_terror_specs/ was read, including all 28 files present in that directory.

The required repository instructions were read from AGENTS.md.

The applicable skills were read from .agents/skills/chaos-redux-events/SKILL.md, .agents/skills/chaos-redux-decisions-missions/SKILL.md, .agents/skills/chaos-redux-focus-trees/SKILL.md, .agents/skills/chaos-redux-event-assets/SKILL.md, .agents/skills/chaos-redux-super-events/SKILL.md, .agents/skills/chaos-redux-subagents/SKILL.md, and .agents/skills/chaos-redux-mtth/SKILL.md.

The offline wiki pages read for this pass were Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface modding, and Scripted GUI modding under paradox_wiki.

The vanilla documentation read for this pass included documentation/script_concept_documentation.md, common/script_constants/documentation.md, documentation/effects_documentation.md, documentation/triggers_documentation.md, documentation/modifiers_documentation.md, documentation/dynamic_variables_documentation.md, and documentation/loc_objects_documentation.md.

The most relevant source anchors are events/031_terrorist_attack.txt:1-77, common/script_constants/031_random_terror_constants.txt:9-226, common/scripted_triggers/031_random_terror_triggers.txt:11-225, and common/scripted_effects/031_random_terror_effects.txt:1-1017.

The event catalog source is docs/spreadsheets/chaos_redux_events_catalog.xlsx, where the Events sheet row for ID 31 is Random Terror with status To Be Reworked.

The exported scenario catalog is evidence only and is not an editable source.

## Identity and collision audit

| Surface | Current evidence | Status | Required gate |
| --- | --- | --- | --- |
| Event identity | events/031_terrorist_attack.txt:1,23,41 defines namespace chaosx.nr31 and roots chaosx.nr31.1 and chaosx.nr31.2. | Safe as the Event 31 root identity, but the current behavior is the legacy two-event implementation. | Replace the legacy root dispatch only after the transaction and log owner are defined. |
| Shared triggerable scenario | common/script_constants/031_random_terror_constants.txt:9-25 proposes triggerable_scenario_id = 15. The shared constants expose IDs 1 through 14 in common/script_constants/chaosx_triggerable_scenarios_constants.txt:10-30, and the registry registers only those IDs in common/scripted_effects/chaosx_triggerable_scenarios_effects.txt:68-175. | ID 15 is unregistered and has no shared dispatch branch. | Do not allocate the number until the scenario registry, dispatcher, launch gate, localisation, event detail row, and workbook are reconciled. |
| SCN-014 | docs/systems/event_system/triggerable_scenarios.md:172 labels SCN-014 as the Fallout manual consequence sandbox. The source workbook exported at docs/spreadsheets/chaos_redux_scenarios_catalog.csv:56 labels SCN-014 Assassin Network and attributes it to Event 039. | Not free, with a current documentation and catalog ownership conflict. | Keep Event 31 off SCN-014 and resolve the conflict in the owning scenario documentation before any new allocation. |
| SCN-015 | localisation/english/021_random_civil_war_l_english.yml:138 labels Event 021 random_civil_war as SCN-015. Event 021 has its own scenario implementation and no shared triggerable_scenario_id = 15 branch was found. | Not a collision in the shared registry, but a live Event 021 label claim makes it ambiguous and unsafe. | Treat SCN-015 as reserved until Event 021 ownership is explicitly migrated or released. |
| Internal Fracture cluster | common/script_constants/031_random_terror_constants.txt:24 proposes internal_fracture_cluster_id = 9. common/script_constants/event_cluster_constants.txt:9-26 assigns ID 9 to national_breakthroughs, and common/scripted_effects/chaosx_event_cluster_effects.txt:194-290 registers it. Event 027 uses the same cluster in common/script_constants/027_doctrine_research_constants.txt:15-26 and common/scripted_effects/027_doctrine_research_effects.txt:1445-1459. | Collision confirmed. Internal Fracture remains forbidden and unregistered. | Remove this proposed Event 31 identity from any future implementation plan unless a parent design explicitly resolves the cluster ownership conflict. |
| World-end identity | common/script_constants/031_random_terror_constants.txt:9-25 proposes world_end_scenario_id = 15. common/script_constants/world_end_scenario_registry_constants.txt:11-33 contains IDs 1, 3 through 14 and no 15. The live initializer in common/scripted_effects/chaosx_events_log_effects.txt:1135-1304 has no Event 31 row. | The numeric slot is currently absent, but it is not registered or available for use without the complete owner and active-state wiring. | Add a row only after the owner event, scenario flag, availability helper, title key, details key, super-event identity, active evaluator, and event-detail arrays are all specified. |
| Reveal and defeat super-events | common/script_constants/031_random_terror_constants.txt:19-20 proposes super-event IDs 106 and 107. common/scripted_localisation/chaosx_scripted_localisation_super_events.txt:274-275 maps visible IDs 104 and 105, and interface/chaosx_super_events.gfx:216-218 defines visible 105. No visible 106 or 107 mapping was found. | Proposed IDs are unregistered. Existing 104 and 105 must not be reused. | Allocate separate visible slots and wire GFX, scripted localisation, runtime assignment, settings-aware playback, and event-log references together. |
| Reveal and defeat audio | common/script_constants/031_random_terror_constants.txt:21-22 proposes audio IDs 106 and 107. common/script_constants/023_sov_nuclear_bombs_constants.txt:53-54 already uses audio ID 104, while common/script_constants/025_alien_technology_in_antarctica_constants.txt:23-24 and common/script_constants/028_asteroid_incoming_constants.txt:198-199 use super/audio ID 105. No 104 through 107 Event 31 sound wrapper was found in sound/chaosx_sound.asset. | Proposed audio IDs are unregistered, and 104 and 105 are already live or reused. | Assign collision-free audio identities, then add base tracks, sound wrappers, volume variants, and settings-aware calls. |

The existing Event 31 sound files sound/031_random_terror/super_event_104_false_revelation_reveal.wav and sound/031_random_terror/super_event_105_false_revelation_defeat_aftermath.wav are asset candidates only.

Their filenames do not establish safe runtime IDs.

The existing Event 31 super-event DDS files are likewise not runtime registration.

## Tag candidates and carrier capacity

The current actor allocator is common/scripted_effects/031_random_terror_effects.txt:544-631.

It hard-codes the five candidate tags JHX, JIX, JKX, JLX, and JMX and guards them with the five global flags random_terror_slot_jhx_used, random_terror_slot_jix_used, random_terror_slot_jkx_used, random_terror_slot_jlx_used, and random_terror_slot_jmx_used.

The same allocator transfers the selected state, adds a core, initializes the country, and sets a created receipt without an atomic carrier ledger.

The current source search found no definitions for those five tokens in common/country_tags, common/countries, history/countries, localisation/english, common/script_constants, or common/collections.

The installed vanilla country-tag search also returned no matches for those five tokens.

The current Event 006 audit at docs/plans/006_independence_wave_plans/tag_audit/006_installed_tag_collision_audit_2026_08_06.md identifies the X-ending replacement pool as unused by vanilla, Chaos Redux, and scanned installed mods at the time of that audit, and includes JHX, JIX, JKX, JLX, and JMX.

That historical audit makes the five tokens plausible candidates, not allocated tags.

The audit is not a substitute for a fresh allocation transaction because the current worktree and installed mod set may have changed since the audit.

The Event 006 live registry exposes the relevant reservation surface through common/script_constants/006_independence_wave_constants_registry.txt:806-816 and reports 191 unique resolved carrier tags, 89 unique registered-reuse carriers, 137 unique bound carriers, 55 unique unbound carriers, and 111 reservation groups at lines 967-989.

There is no generic Event 31 free-capacity counter in the current registries.

The proposed capacity is therefore unresolved as 5 declared source candidates versus 8 required carriers.

An implementation must use an explicit Event 31 carrier ledger rather than five slot flags.

Each ledger row must preserve the carrier tag, origin, parent actor or generation, organization identity, region, controlled states, route, leader identity, allocation flag, active flag, and outstanding reference count.

The allocator must preflight every required carrier before transferring a state or creating units.

The allocator must reject the whole transaction if any carrier is missing, declared elsewhere, reserved by Event 006 or another active package, not materializable, or not cleanable.

A release must clear actor state, cores, flags, variables, event targets, and external references before returning the carrier to the free pool.

No silent sharing is permitted.

## Classifiers and target eligibility

The shared classifier surface is common/scripted_triggers/chaosx_dynamic_triggers.txt:10-75.

is_special_chaos_country includes the existing Chaos country flags and tags but does not include random_terror_actor.

is_actual_nonhuman_country likewise has no Event 31 actor marker.

The Event 31 target trigger at common/scripted_triggers/031_random_terror_triggers.txt:40-55 already excludes actual nonhuman countries, special Chaos countries, actor countries, cleanup-complete countries, reserved targets, incompatible routes, world-end state, and countries with no populated controlled state.

The Event 31 actor trigger at lines 11-31 uses the random_terror_actor flag and the actor profile values.

The actor is a special Chaos actor in the design, but it is human-populated and must never be added to is_actual_nonhuman_country.

The parent implementation should either add the owner flag to the shared is_special_chaos_country classifier or retain an explicit documented exclusion at every shared consumer.

The shared classifier is preferable because ordinary target pools, civilian systems, world-threat aggregation, and other cross-event systems otherwise receive divergent answers.

No duplicated local copy of is_special_chaos_country or is_actual_nonhuman_country should be created.

The baseline target logic must remain independent of Muslim-majority, refugee, ethnicity, nationality, or ordinary ideology filters unless a later accepted specification adds those distinctions.

## Current helper inventory and gaps

The existing file already contains the following helper groups.

| Existing helper or range | Scope | Current inputs and outputs | Current side effects and call sites | Architecture assessment |
| --- | --- | --- | --- | --- |
| random_terror_initialize_global_state at 20-58 | Global | Initializes global pressure-related variables and the system flag. | Used by incident, evolution, and wave helpers. | Reuse as the first phase of owner transactions, but add an explicit generation and terminal-state guard. |
| random_terror_initialize_country_state at 60-77 | Country | Creates country pressure, legitimacy, incident count, and response capacity variables. | Called by pressure, legitimacy, and incident flows. | Reuse, then centralize defaults in constants. |
| random_terror_initialize_state_state at 79-92 | State | Creates state activity, stage, and pressure variables. | Called by activity, incident, and response flows. | Reuse, but pair stage changes with counter reconciliation. |
| random_terror_clamp_country_values at 94-105, random_terror_apply_pressure at 107-115, and random_terror_apply_legitimacy at 118-126 | Country | Applies pending deltas and clamps pressure and legitimacy to the 0 through 100 band. | Shared by incident and response helpers. | This is the correct local numeric API; remove direct magic deltas at the call sites. |
| random_terror_update_state_stage at 129-177 | State | Derives stage flags from state activity and updates the active-crisis count when crossing a threshold. | Called by activity and response reduction. | Add downward transition accounting and a single owner for stage flags. |
| random_terror_add_state_activity, random_terror_mark_state_cooldown, random_terror_record_chaos, and random_terror_apply_exact_state_loss at 180-221 | State and global | Adds activity, sets cooldown, records chaos, and reuses exact civilian population loss. | Called from incident resolution. | Reuse the exact population-loss helper and make cooldown and loss receipt part of the incident transaction. |
| random_terror_apply_incident at 223-329 | State and global | Selects a temporary incident type, applies state and country effects, sends chaosx.nr31.2, records counters, and may spawn an actor or civil war. | Called by random_terror_run_global_wave at 438-460. | Repair in place. The current random_list contains only nine of the 24 defined incident types and its weights are not backed by completed probability evidence. |
| random_terror_resolve_evolution and random_terror_record_evolution at 332-426 | Global | Resolves the highest unlocked evolution from global chaos and records an evolution row. | Called by the wave entry point. | Keep the evolution owner local, but record each crossed stage exactly once and add Event 31 event-log localisation mappings. |
| random_terror_resolve_wave_target_count and random_terror_run_global_wave at 429-464 | Global, country, and state | Resolves a target count, sets a wave flag, loops over random countries, finds a valid state, reserves a timed target flag, and applies an incident. | No external Event 31 owner call site was found in events, decisions, focuses, or on_actions. | Add a dispatch owner and complete preflight receipts before calling this helper. |
| random_terror_initialize_actor at 467-541 | Country | Applies actor flags, profile values, government values, technology, and existing Infantry Division units. | Called by the five hard-coded carrier branches. | Reuse only after a valid carrier is allocated and record the generated package in the ledger. |
| random_terror_try_spawn_actor at 544-631 | State, controller, and global | Saves the former owner, chooses one of five tag branches, transfers the state, adds a core, initializes the actor, and updates territorial counters. | Called after incidents cross a stage threshold. | Replace slot flags with an eight-row reservation and rollback receipt. |
| random_terror_start_pressure_civil_war at 638-671 | Country | Uses a meta effect to pass dynamic ratios into start_civil_war. | Called from incident resolution after actor creation. | Keep as a narrow adapter, but verify dynamic field support before relying on ideology, size, and ratio injection. |
| random_terror_response_* at 674-876 | Country and state | Applies government response effects and records response flags. | No Event 31 decision file or external call site was found. | Keep response effects local and create decision wrappers only after costs, triggers, and action-state targets are defined. |
| random_terror_actor_action_common and random_terror_actor_action_* at 879-1008 | Actor country | Applies readiness, control, authority, supply, unity, or terminal-route changes and sets action locks. | No Event 31 decision file or external call site was found. | Keep action effects local and route the terminal call through the missing False Revelation helper. |
| random_terror_clamp_actor_values at 1013-1017 | Actor country | Clamps actor control, authority, supply, and territorial control. | No external owner was found. | Reuse from an actor action transaction and add cleanup-safe defaults. |

The current actor action random_terror_actor_accelerate_revelation at 1001-1006 calls random_terror_begin_false_revelation, but no definition for that effect exists in the current source.

No random_terror_cleanup helper or effect that sets random_terror_cleanup_complete was found.

The current scaffold therefore has a terminal call-site gap and a cleanup gap before any decision or actor-action wiring can be considered complete.

## Proposed helper map

The following map is an implementation plan, not an instruction to add helpers without call sites.

| Helper | Scope | Inputs | Outputs | Side effects | Intended call sites |
| --- | --- | --- | --- | --- | --- |
| random_terror_validate_dispatch_transaction | Global or ROOT | Requested scenario, wave profile, intensity, bypass flag, current evolution, terminal state, and requested target count. | Validation flag, rejection code, and normalized transaction variables. | None. | Event 31 root dispatch, manual scenario confirmation, and any future decision confirmation. |
| random_terror_reserve_wave_target_receipt | Country or state | Transaction generation, candidate country, state, incident type, and target index. | Reserved flag, generation variable, state and country receipt variables, and regular event target. | Reserves only after whole-wave preflight succeeds. | random_terror_run_global_wave before random_terror_apply_incident. |
| random_terror_apply_incident | State and global | Existing temporary incident type plus normalized transaction values. | Incident receipt, pressure and legitimacy deltas, stage transition, and optional actor-request flag. | Applies one incident, records exactly one child report, and updates the global ledger. | Root wave owner and future bounded manual scenario owner. |
| random_terror_commit_evolution_transition | Global | Current and requested evolution, disabled-evolution flags, delayed anchor, and transaction generation. | One-time evolution flag and evolution receipt. | Sets one stage and records one evolution entry only after its delayed gate. | The pacing owner around random_terror_resolve_evolution. |
| random_terror_allocate_actor_carrier | Global, country, and state | Profile, generation, parent actor, region, target state, route, and required carrier count. | Carrier tag receipt, allocation index, actor generation, and failure code. | Atomically reserves a declared, collision-cleared carrier before transfer. | random_terror_try_spawn_actor and later actor expansion. |
| random_terror_release_actor_carrier | Country and global | Carrier receipt, actor generation, resolution outcome, and remaining-reference check. | Released flag and cleanup receipt. | Removes owner state, cores, flags, variables, and references before clearing the reservation. | Defeat, surrender, merge, partition, transform, reject, abort, and world-end cleanup. |
| random_terror_validate_jihad_transaction | Global or ROOT | Jihad type, intensity, eligible target receipt, evolution, bypass, and terminal lock. | A normalized 16-combination receipt or rejection code. | None. | Manual scenario confirmation and government or actor route confirmation. |
| random_terror_commit_jihad_transaction | Global, country, and state | Validated jihad receipt and all aligned target, state, and division arrays. | Commit flag and applied counts. | Applies the whole transaction, including exact targets and bypass effects. | The Global Jihad dispatch owner only after validation. |
| random_terror_record_event31_history | Global or ROOT | Event identity, type, evolution, intensity, payload, and pre-fire representative actor. | History sequence and row receipt. | Writes one global row and refreshes the shared views. | Event 31 root dispatch once per global firing. |
| random_terror_begin_false_revelation | Global | Terminal actor, accepted result, readiness receipt, territory receipt, and public toggle. | Terminal accepted flag, world-end scenario flag, and super-event receipt. | Freezes ordinary random pacing, schedules or commits the world-end branch, starts the unique reveal or defeat presentation, and hands off to cleanup. | random_terror_actor_accelerate_revelation and the terminal decision or scenario owner. |
| random_terror_cleanup_runtime | Global, country, and state | Transaction generation, outcome, affected states, actor list, and carrier ledger. | Cleanup-complete flag and cleanup receipt. | Clears flags, variables, arrays, event targets, and owner effects, then releases carriers. | Every abort, rejected transaction, incident completion, actor resolution, and terminal branch. |
| refresh_world_threat_state | Global shared helper | Existing source flags, including a future random-terror source flag. | global.world_threat_source_count and world_in_threat. | Recomputes the shared aggregate. | Call the existing cross-event helper after Event 31 sets or clears world_threat_source_random_terror. Do not duplicate its logic. |

Clausewitz scripted effects do not return ordinary function values, so every output in this map means a flag, variable, array entry, or event-target receipt.

Event 31 orchestration should remain in common/scripted_effects/031_random_terror_effects.txt.

Only the cross-event world-threat source addition belongs in common/scripted_effects/chaosx_dynamic_effects.txt, and that shared documentation must be updated when implementation is allowed.

## Constants and tuning table plan

The current constant groups in common/script_constants/031_random_terror_constants.txt already cover identity, evolution types, stage values, incident IDs, jihad types, intensities, actor profiles, routes, thresholds, wave counts, delays, and costs.

The identity entries at lines 9-25 must remain provisional until the collision gates above are complete.

The tuning entries at lines 167-226 should be split conceptually into stage thresholds, evolution delays, wave target counts, cooldown bands, incident weights, pressure and legitimacy deltas, actor force sizes, carrier limits, and terminal transition delays.

The current effect file still contains direct tuning literals, including add_to_variable = { global.random_terror_network_reach = -5 } at line 722, subtract_from_variable = { global.random_terror_international_unity = 4 } at line 745, add_stability = 0.02 at line 715, add_stability = -0.03 at line 767, and the manpower and equipment values at lines 804-807.

Those values must move to named script constants or a normal variable loaded from a constant before the effect call.

The incident pool at common/scripted_effects/031_random_terror_effects.txt:228-238 currently uses weights 16, 12, 10, 8, 7, 7, 12, 10, and 8 for nine incident types.

The full design defines 24 incident types, so the owner must decide whether the missing types are disabled by accepted design or add them to a complete constant-backed pool.

No balance target should be inferred from the current nine weights.

Use constant:random_terror_* for fixed-point values where the field supports script constants.

For duration fields that reject constants, assign the constant to a normal or temporary variable first.

If MTTH, AI chance, random selection, decision score, mission score, or any other probability-bearing field changes, follow the P01-P10 and W01-W08 scenario contract from the Event 31 specification.

The required sequence is baseline probability_inspect, named scenario evidence, owner-applied patch, and probability_compare through chaosx_ai_probability_auditor using the same scenarios.

The current pass produced no usable probability artifact.

## Event-target, variable, and cleanup plan

The incident helper saves a regular event target named random_terror_current_state at common/scripted_effects/031_random_terror_effects.txt:226.

The actor allocator saves random_terror_spawn_state at lines 550, 570, 585, 601, and 617.

The response helper reads random_terror_action_state at lines 676-684, but no current owner was found that saves that target.

These short-lived targets should stay regular event targets when they remain inside one effect chain and its child events.

Every consumer must check has_event_target before dereferencing them.

The parent dispatch should save the pre-fire representative actor and source country before any state transfer, civil-war start, or actor creation.

Use global event targets only for a pointer that must survive beyond the originating chain, and clear each one explicitly with clear_global_event_target after all event and decision references have gone.

The persistent actor ledger should use generation, parent, route, carrier, state, and reference variables or arrays rather than relying on temporary variables.

The cleanup order is preflight rollback, child-event completion, actor outcome resolution, carrier cleanup, state and country flag cleanup, global target cleanup, aggregate refresh, and only then setting random_terror_cleanup_complete.

Cleanup must cover actor defeat, surrender, absorption, partition, transformation, False Revelation acceptance, False Revelation rejection, failed materialization, interrupted dispatch, and world-end completion.

The current trigger checks random_terror_cleanup_complete at common/scripted_triggers/031_random_terror_triggers.txt:14 and 46, but no Event 31 effect currently sets that flag.

The current update helper increments global.random_terror_crisis_state_count at common/scripted_effects/031_random_terror_effects.txt:176 without a matching recovery or cleanup decrement.

That counter must be reconciled by the same stage and cleanup owner.

## Dispatch and event-log hooks

The current root event at events/031_terrorist_attack.txt:22-36 is triggered-only and schedules chaosx.nr31.2 after one day.

The current child event at lines 40-77 is a generic riot report that damages buildings, removes manpower, and starts a fascist civil war.

The current incident helper also schedules chaosx.nr31.2 at common/scripted_effects/031_random_terror_effects.txt:309.

Events 070 Africa directly call chaosx.nr31.2 at events/070_africa_gods.txt:285, 312, and 342, which bypasses the future Event 31 transaction and global-row contract.

Those calls must either migrate to an explicit legacy adapter or route through the Event 31 root owner.

The existing evolution path calls record_events_log_evolution_entry at common/scripted_effects/031_random_terror_effects.txt:420-426, but no Event 31-specific event name, type, or evolution localisation mapping was found.

The shared generic history path is record_events_log_history_entry at common/scripted_effects/chaosx_events_log_effects.txt:684-837.

The explicit system-row pattern is record_events_log_system_history_entry at lines 537-646.

The default actor mapping is events_log_set_default_actor_for_current_event at lines 198-468 and has no Event 31 branch.

The Event 31 root should capture the pre-fire representative actor, set an explicit payload or actor override, record exactly one global history row, and then allow child report events to remain local follow-ups without creating additional global rows.

The row should contain Event 31 identity, incident type, evolution, intensity, representative actor, target count, and terminal or non-terminal result.

Evolution rows should be emitted once per crossed evolution and should not depend on the generic child report event.

## World-end, super-event, and audio integration

The False Revelation gate is present only as a trigger at common/scripted_triggers/031_random_terror_triggers.txt:161-176.

The gate checks terminal state, Evolution V, public enablement, Chaos 1000, readiness, international unity, territorial control, crisis and strategic counts, and a viable jihadist actor.

The effect called by random_terror_actor_accelerate_revelation is missing.

The world-end registry append contract is common/scripted_effects/chaosx_events_log_effects.txt:1307-1318.

It appends aligned arrays for ID, owner event, sort order, visibility, public details readiness, default enabled state, scenario flag, super-event ID, title key, details key, and availability helper.

The active-state evaluator is at lines 1333-1387, and the Event Details rebuild is at lines 1410-1484.

An Event 31 world-end row therefore needs all aligned fields, an active flag branch, public title and details localisation, and a complete availability helper.

The existing settings-aware playback helper in common/scripted_effects/chaosx_settings_effects.txt:4911-4952 consumes super_event_visible and global.current_super_event_audio_id through meta-effect construction.

The False Revelation owner must set those runtime values only after the terminal transaction is accepted.

Ordinary Random Terror firing must be frozen before the terminal branch becomes active.

The reveal and defeat presentation must use distinct visible super-event slots and distinct audio identities.

Do not reuse visible 104 or 105, and do not treat the current Event 31 WAV filenames as registered audio.

No audio or visual wiring is part of this handoff.

## CXT carrier contract

The current accepted Event 31 design uses existing HOI4 Infantry Division units and existing infantry and support equipment.

That does not create a new land sub-unit, concrete equipment type, special project, special facility, doctrine, general system, or other CXT extension database object.

No Event 31 CXT carrier registration is therefore required for the accepted scope.

The current trigger random_terror_can_register_cxt_extension at common/scripted_triggers/031_random_terror_triggers.txt:218-223 only checks whether the CXT country is initialized or registration is pending.

No Event 31 idempotent registration wrapper, modifier-free hidden idea, _apply effect, startup registration, or on_daily_CXT repair block was found.

The CXT hook source currently provides on_daily_CXT and on_weekly_CXT at common/on_actions/chaosx_test_country_on_actions.txt:13-29.

The contract documentation is docs/testing/chaosx_test_country.md:105-170.

If a later accepted design introduces CXT-eligible content, the package must add a modifier-free hidden carrier idea whose ID matches the setup effect before its _apply suffix, an idempotent setup effect, one bounded existing-country on_startup registration, and an additive guarded on_daily_CXT fallback for loaded saves.

Any future custom land sub-unit also needs its Event 19 disposition and provider integration.

No CXT registration should be invented for the current existing-unit implementation.

## Migration sequence

1. Freeze the provisional scenario, world-end, super-event, audio, and cluster identities until the collision table is resolved.

2. Replace the five slot flags with a carrier reservation ledger and verify all eight rows before any transfer or unit creation.

3. Add the Event 31 root dispatch owner and route all accepted automatic, manual, and bypass entries through one transaction validator.

4. Reuse the existing pressure, legitimacy, stage, exact population loss, incident, evolution, actor initialization, response, and actor action helpers while removing duplicated literals and adding receipts.

5. Add bounded wave target reservation and exact target-count accounting before random_terror_run_global_wave can commit incidents.

6. Add decision and mission owners only after action-state event targets, costs, trigger tooltips, AI scores, and cleanup paths exist.

7. Add Global Jihad validation and commit as a single aligned target, state, and division transaction.

8. Add Event 31 event-log name, type, evolution, actor, world-end, and details mappings and enforce one global firing row.

9. Add the world-end registry row and False Revelation effect only after the terminal cleanup and ordinary scheduler freeze are testable.

10. Allocate and wire super-event and audio identities only after the live registries are updated and collision-free.

11. Update localisation, event details, event log, assets, and the workbook source after behavior is stable.

12. If the workbook is updated, edit docs/spreadsheets/chaos_redux_events_catalog.xlsx and run python .tools/export_event_catalog_csv.py from the mod root.

13. Do not edit the export CSV files directly.

## MCP evidence and blockers

| Route | Request and result | Evidence or blocker |
| --- | --- | --- |
| hoi4.event_inspect | Scan of events/031_terrorist_attack.txt with both directions, depth 3, node cap 100, edge cap 200, helper expansion disabled, and refresh enabled. | Returned status ok with code EVENT_INSPECTED_PARTIAL in workspace mod_chaos_redux_ea3b2d67c2c0. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/56aefb55b8c5725a639df4db9e2d32f2dc96cf23dbee6d78086b77fadf084b3a/270f3adb212172dbaae3dd2b55c8ff1067360ca68224e93782488b6c85420fbd/event-scan-687013323071.json. Revision 6870133230714ade0916271d194c174062301db948a19e24564b8972821af8ac. The scan counted 9550 events, 14762 options, 1089 entries, 8396 unresolved nodes, 7673 terminals, 37306 edges, and 2136 diagnostics, with 0 blocking diagnostics. It was partial because the inline inventory retained 64 of 353 sources and deferred large workspace helper and lifecycle passes. |
| hoi4.event_render | Corrected overview render of chaosx.nr31.1 with both directions, depth 3, node cap 100, helper expansion disabled, and refresh enabled. | Returned status ok with code EVENT_RENDERED_PARTIAL and artifactCount 4. The returned summary did not expose artifact URIs. The first caller-shaped request was rejected because workspace is not a recognized event_render argument; the corrected route completed. |
| hoi4.focus_inspect | Requested common/national_focus and treeId random_terror. | Returned status error with code FOCUS_SOURCE_NOT_FOUND and message No active focus source matched the request. No Event 31 focus surface exists to inspect, and no focus call site is in scope. |
| hoi4.map_inspect | Queried random terror with queryLimit 20 and no overview. | Returned status ok with code MAP_INSPECTED. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/230912a7dd40a84ceb71bf1105b51efa3d329d4fc8cc500fe5282ec629a0360d/5bfdaa3919e86ddaf5b5e5c7bed32a4bfa1c373054a3a26fe6dc0a917f988c87/map-inspect.def41ff859321422.json. Revision def41ff85932142240b95243a43d8b288c611b0ae920fa36e0db8be2da3e4504. The query returned zero Event 31 matches and zero inspected coordinates, provinces, and states. The complete map catalog reported 5632 by 2048 dimensions, 13414 definitions, 1081 states, 304 regions, and 534 ports, but workspace-wide retained diagnostics included 1332 MAP_PORT_ADJACENT_SEA_INVALID and 1323 MAP_BUILDING_POSITION_INVALID errors. This is catalog evidence only and does not support an Event 31 map claim. |
| hoi4.probability_inspect | First attempt used adapter custom_weighted_pool with candidatePool random_terror_target_pool and no source. | Returned MCP error -32602: Input validation error: Invalid arguments for tool hoi4.probability_inspect: An adapter requires a source; provide a source alone to discover compatible adapters. |
| hoi4.probability_inspect | Second attempt used adapter direct_random with source events/031_terrorist_attack.txt and identifier chaosx.nr31.1, candidatePool chaosx.nr31.1 and chaosx.nr31.2, and refresh enabled. | Timed out awaiting tools/call after 180 seconds. No probability artifact, scenario hash, sweep, simulation, or comparison evidence was produced. |
| chaosx_ai_probability_auditor | The named read-only auditor was invoked with fork_context=false against the current weighted incident surface and was instructed not to edit files. | No completed evidence was returned during the handoff preparation window. The direct probability route remains unresolved, so the current nine weights are source observations only and not an audited balance result. |
| GUI routes | No GUI inspect or render route was used. | The specification explicitly excludes Event UI and no dedicated Event 31 GUI is present. The shared Event Log and super-event interfaces remain outside this bounded handoff. |
| 3D routes | No 3D route was used. | The specification explicitly excludes 3D and the accepted design uses existing HOI4 units. |

The MCP results do not replace source review, offline wiki review, vanilla documentation review, or parent validation.

No game executable was launched and no in-game or log validation is claimed.

## Risks, unsupported fields, and follow-up evidence

The current actor materialization path depends on country tags and country definitions that are absent from the current source tree.

The current source declares five carrier branches but eight required carriers.

The current carrier slot flags do not record origin, generation, parent, route, leader, state references, or release conditions.

The current weighted incident pool contains nine types while the constants define 24 types, and probability MCP evidence is unavailable.

The dynamic start_civil_war meta-effect at common/scripted_effects/031_random_terror_effects.txt:638-671 requires an engine-backed check that the injected ideology, size, and force-ratio fields are accepted in the exact effect form used.

State transfer, core creation, actor country materialization, existing-unit creation, delayed event-target persistence, and carrier cleanup require a focused engine validation pass after implementation.

The current stage counter has an increment path without a matching recovery path.

The current False Revelation trigger has no implementing effect.

The current cleanup-complete trigger has no implementing effect.

The current Event 31 event log path has an evolution call but no complete name, type, actor, or detail mapping.

The current public scenario dispatch has no shared ID 15 branch.

The current world-end registry has no Event 31 row or active evaluator branch.

The current super-event and audio constants are provisional and conflict with existing 104 and 105 use if interpreted as visible or audio runtime IDs.

The historical tag audit is useful evidence but must be refreshed at allocation time.

The map MCP result is not evidence for target selection because the query returned no Event 31 states and the workspace contains unrelated locator errors.

The no-focus result is a source absence, not permission to create a focus tree.

## Completion and simplifications

The requested architecture handoff is written at docs/plans/031_random_terror_plans/031_random_terror_scripted_system_architecture.md.

No gameplay files were edited.

No Internal Fracture cluster was created.

No Event UI or 3D system was created.

No fallback mechanic or silent identity substitution was used.

No probability or balance claim is made where MCP evidence was unavailable.

The Event 31 gameplay scaffold remains incomplete and is not represented as implementation-complete.

The handoff is isolated to this file; unrelated parent modifications remain untouched and outside this pass.
