# Chaos Redux shared-system migration plan

Date: 2026-08-22

Owner: `chaosx_scripted_system_architect` (plan-only handoff to the parent agent)

Status: design and migration plan only; no gameplay, localisation, spreadsheet, interface, scripted GUI, asset, `.codex`, or `.qoder` file was changed by this plan.

Exact file written by this task: `docs/plans/repo_cleanup/shared_system_migration_plan_2026-08-22.md`.

No commit was created, as required by the parent task.

## Executive decision

The seven findings in this plan are coupled through saved event IDs, global arrays, scripted-localisation context variables, dynamic `meta_effect` dispatch, event targets, and the shared Event Log window, so they must not be cleaned up as one bulk rewrite.

The safe route is a sequence of independently reviewable, source-compatible phases: establish inventories and owner contracts first, prove engine behavior through the applicable read-only MCP routes, add compatibility adapters where required, compare old and candidate behavior under named scenarios, and only then remove duplicated code in a separately approved change.

The mixed event-category registry, Event 006 registry/collection boundary, Event 019 provider dispatch, and global event-target lifecycle remain blocked for implementation until their save-state and runtime contracts are proven.

The Event Log work may be considered only as a bounded functional consolidation in `common/scripted_effects/chaosx_events_log_effects.txt` and `common/scripted_guis/chaosx_scripted_gui_events_log.txt`; it must not touch `interface/chaosx_events_log_popup.gui`, geometry, coordinates, click regions, window layout, or assets.

No new unqualified `on_daily`, `on_weekly`, or `on_monthly` world iteration is permitted by this plan. Any scheduler change that would add or widen whole-world iteration requires explicit user authorization before implementation.

## Scope and non-goals

This plan covers shared consumers of Events 1–20 and only the shared selectors, registries, schedulers, targets, and Event Log consumers that are also visible to Events 21+.

Events 21+ are not to be individually redesigned, renamed, localized, or inspected as standalone gameplay events under this plan; they are included only where shared registry, event-name, Event Log, or provider consumers require reference proof.

This plan does not redesign gameplay, event balance, event narrative, event ownership, route logic, country allocation policy, provider content, or the visual design of the Event Log.

This plan does not renumber event IDs, reorder persisted category arrays, remove compatibility aliases, regenerate localization keys for unregistered IDs, or replace dormant-capable Event 006 arrays with live country collections.

This plan does not create a central MCP router, wrapper skill, generic target cleanup system, generic dynamic-localisation engine, or cross-event provider registry without an accepted design decision.

This plan does not add a whole-world on-action, move the existing scheduler to a new broad on-action, or change the cadence or scope of the existing scheduler as a cleanup convenience.

This plan does not edit `interface/*.gui`, any layout or geometry field, any coordinate, any click region, any sprite or texture, or any asset manifest.

This plan does not route the shared Event Log to `chaosx_event_ui_worker`; that worker is reserved for a dedicated event-owned GUI and the shared Event Log is explicitly excluded by the repository skill.

This plan does not launch Hearts of Iron IV or claim live consumer validation; live game validation remains the user's responsibility.

## Evidence reviewed

Repository instructions and scope were read from `AGENTS.md` and `docs/plans/repo_cleanup/chaosx_repo_cleanup_master_prompt.md`.

The required repo skills were read from `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, and `.agents/skills/chaos-redux-decisions-missions/SKILL.md` because the scope includes the shared Event Log scripted GUI bindings.

The offline wiki pages read before source inspection were `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`, `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`, `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md`, `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`, `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`, `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md`, `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`, `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`, `paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md`, `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md`, `paradox_wiki/Interface Modding - Hearts of Iron 4 Wiki.md`, and `paradox_wiki/Scripted GUI Modding - Hearts of Iron 4 Wiki.md`.

The required vanilla documentation read was `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md`, `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/common_script_documentation.md`, `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`, `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`, `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/loc_objects_documentation.md`, `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/dynamic_variables_documentation.md`, `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/collections_documentation.md`, `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/script_constants/documentation.md`, and the relevant event, scripted GUI, on-action, and scripted-localisation documentation in the same installation.

The existing shared helper sources were inspected before proposing any new helper: `common/scripted_effects/chaosx_dynamic_effects.txt`, `common/scripted_effects/chaosx_dynamic_effects.md`, `common/scripted_effects/chaosx_logic_effects.txt`, `common/scripted_effects/chaosx_events_log_effects.txt`, and `common/scripted_effects/chaosx_settings_effects.txt`.

The read-only cleanup baseline was reviewed from `docs/plans/repo_cleanup/subagent_handoffs/shared_helper_architecture_baseline_2026-08-22.md` and `docs/plans/repo_cleanup/subagent_handoffs/repo_map_2026-08-22.md`.

The baseline Event 006 inspection artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/440bd3d04a1e0d7617e63ae389692acf1838289aba2ef4461168a7b80d44d5c9/89348b9e318930689c96a75e0bfef0d2e5db9a22d94c3640ec6cbb6b60a2ff1c/event-lint-bc0062fc8506.json`.

The baseline Event 019 inspection artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cc8e7c1ad8d2d0009b471248e13b8a491a42cc0e8d51fde3d61adb3a60a4643e/01cc17d7d05d15ce372a3614f5faeb981d0166e77edde1ef7d672cef2fb36f85/event-lint-0d89fc74a70e.json`.

Both event artifacts are structural, partial inspection evidence rather than runtime proof; helper and lifecycle projections were deferred.

The baseline shared Event Log GUI inspection artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/922e791efa3e7f79b89c8554be19b5da743f0abcb4dcbe4dcbf285f8a420b805/453308075164395336e7c4c3de561b72fba8007710d9826e1f0e617edc436376/gui-inspect.1391d8530b419297.json`.

That GUI artifact reports 16 window elements, 156 modeled items, 2 approximated items, 35 ignored items, 1 missing item, 16 unsupported items, and 1 unresolved item; the graph diagnostics were truncated at 2,000 entries and included six visible overlaps, so it cannot authorize a layout or geometry conclusion.

The baseline weighted inspection artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b3a7bed6e8e3d5e23416794b68e928d4a3c14aaecba41d8618761acbcdfc7e8e/d28276c76aee90b542dc05f97871aa4c06fc2f676a36f690d1d545757b012bf2/probability-inspect-6d5d6adb4e5b.json`.

That probability inspection covered the `custom_weighted_pool` adapter in `common/scripted_effects/chaosx_logic_effects.txt`, found zero custom-pool candidates and no unresolved required inputs, and did not include the required compare or auditor evidence.

During this planning pass, bounded `hoi4.event_inspect` calls for `chaosx.nr6.1` and `chaosx.nr19.1` did not return and were terminated after the tool timeout, so the baseline artifacts are the only available event MCP evidence for those surfaces.

During this planning pass, `hoi4.gui_inspect` for `events_log_popup_window` with scenario `event_log_shared_architecture_baseline` timed out after 180 seconds; no current GUI rewrite or post-change comparison was attempted.

During this planning pass, `hoi4.probability_inspect` for the custom weighted pool also timed out after 180 seconds.

The callable tool inventory did not expose a `chaosx_ai_probability_auditor` route, so the required auditor evidence is a recorded blocker rather than an inferred pass.

The worktree is concurrently dirty with unrelated and in-progress Event 006, Event 016, Event 019, scripted-localisation, and documentation changes; later implementation must establish ownership and a clean baseline for each tranche instead of assuming the current worktree is a stable release snapshot.

## Current owner map and proposed helper contracts

The following table is the proposed ownership boundary; names marked `candidate` are design targets only and are not files or helpers created by this plan.

| Surface | Current source owner and identifiers | Candidate helper or adapter | Scope and inputs | Outputs and side effects | Call sites and migration rule |
| --- | --- | --- | --- | --- | --- |
| Canonical event name selector | `common/scripted_localisation/chaosx_scripted_localisation_debug.txt:GetEventName`; duplicate selectors `GetSettingsEventName`, `GetLastEventName`, `GetEventsLogEvolutionSourceEventNameView`, and `GetEventsLogHistoryEventName` in the settings and Event Log scripted-localisation files | `GetEventName` in a dedicated canonical event-name selector file, or an explicitly chosen existing owner after engine proof; context bridges remain thin adapters | Current localisation scope with a temporary or context-specific event ID; adapter input is the source variable or row-array entry and any special-provider discriminator | One localized event name; no gameplay side effect; fallback must resolve to `chaosx.event_name.unknown` | Debug logging, settings event selection, last-fired display, history rows, evolution rows, event detail rows, and shared Events 21+ consumers; retain special Fallout and non-system selectors outside the numeric table until proof is complete |
| Per-country event scheduler | `common/on_actions/chaosx_on_actions_system.txt:on_daily` at line 57; startup ownership at `on_startup`; selection/accounting in `common/scripted_effects/chaosx_logic_effects.txt` | `chaosx_event_scheduler_tick_country` (candidate) called from the existing on-action only | COUNTRY scope; timer, activation flags, settings, and current country are inputs | Timer decrement, weighted event selection, automatic context, fire dispatch, context cleanup, and optional debug logging; no additional iteration | One existing `on_daily` call site; helper extraction may preserve the existing whole-world caller but may not add another whole-world caller without user approval |
| Category registry and type lookup | `common/scripted_effects/chaosx_logic_effects.txt:initialize_event_categories`, `initialize_all_events_array`, `get_event_type`; type values in `common/script_constants/event_system_constants.txt:event_system_event_type` | `get_event_type` remains the narrow lookup owner; a generated category table or compatibility assertion is candidate-only | Any scope carrying temp `event_id`; category arrays and immutable ID aliases are inputs | Temp `event_type`; initialization mutates global category arrays and `global.all_events`; no ID renumbering | `select_weighted_random_event_id`, weight/cap initialization, default-disabled queue, debug logs, Event Log type/name paths, and all shared registrations; preserve array order and numeric values |
| Event 006 registry | `common/collections/006_independence_wave_country_collections.txt`; `common/script_constants/006_independence_wave_country_registry_constants.txt`; `common/scripted_triggers/006_independence_wave_country_registry_triggers.txt`; `common/scripted_effects/006_independence_wave_country_registry_effects.txt`; `006_independence_wave_package_dispatch_effects.txt` | Existing `independence_wave_registry_record_event6_origin` and `independence_wave_registry_clear_event6_origin` remain lifecycle wrappers; a compatibility adapter or row-contract assertion is candidate-only | COUNTRY for origin wrappers; planner/allocator scopes for row and package data; static registry row, carrier tag, package, reservation group, and active collection view are explicit inputs | Origin flags and `liberation_origin` values; dispatch/cleanup effects preserve package and ledger state; no nearby-carrier substitution | Event 006 setup/cleanup and dispatch call sites only; Event 012 must not call Event 006 origin wrappers; no collection replacement until save and row identity proof |
| Event 019 provider dispatch | `common/scripted_effects/019_infantry_spawn_core_effects.txt:infantry_spawn_evaluate_current_registry_row`; `019_infantry_spawn_unit_registry_effects.txt:infantry_spawn_unit_registry_dispatch_static_token`; derivative package file and Event 016 bridge | Existing meta-effect contracts remain the API; `infantry_spawn_validate_provider_contract` is candidate-only and may be added only if it does not alter dispatch semantics | COUNTRY or current registry scope; provider ID from aligned arrays or provider constants, plus provider-specific payload | Eligibility, template, spawn, sustainment, and cleanup callback results; dynamic effect name is generated from provider ID; unknown provider must fail closed | Event 019 registry loops and Event 016 providers 504–510/522; do not move owner adapters or replace dynamic dispatch with fixed tags |
| Global event-target lifecycle | Event-specific save/clear sites across Event 006, 011, 016, 019, and other event files; Event Log only consumes targets in `chaosx_events_log_effects.txt` | Source-specific cleanup wrappers, not a central target helper; each wrapper is candidate-only after lifecycle proof | Owning event chain, target name, terminal/cancel/failure path, and persistent-history classification | Clear or preserve exactly one target according to its lifecycle; no blanket global clear | Every `save_global_event_target_as`, `clear_global_event_target`, `clear_global_event_targets`, `has_event_target`, and `event_target:` use must be inventoried before any call-site move |
| Event Log functional bindings | `common/scripted_guis/chaosx_scripted_gui_events_log.txt` tab click effects; rebuild and detail ownership in `common/scripted_effects/chaosx_events_log_effects.txt` | `events_log_set_tab_state_and_rebuild` (candidate) plus existing detail-close helpers | COUNTRY/player context; selected tab, existing flags, detail state, and view arrays are inputs | Mutually exclusive tab flags, detail cleanup, and exactly one corresponding rebuild; no layout state mutation | Eight duplicated status/history/evolution/events/clusters idle/active effects and close shell; `interface/chaosx_events_log_popup.gui` remains read-only |

The helper map is intentionally conservative: existing owners are reused, new helpers are candidates for a later implementation tranche, and no helper is to be created without a call site, a matching markdown contract, and an engine-backed equivalence test.

## Finding 1: replicated scripted-localisation event-name selectors

### Current debt and source ownership

`GetEventName` in `common/scripted_localisation/chaosx_scripted_localisation_debug.txt` contains explicit branches for event IDs 1 through 1000 and a literal fallback of `"Unknown Event"`.

`localisation/english/chaosx_event_names_l_english.yml` currently defines `chaosx.event_name.unknown`, IDs 1 through 99, 163, 635 through 641, and 991, so the debug selector references undefined destinations for most IDs 100 through 1000.

`GetSettingsEventName` and `GetLastEventName` in `common/scripted_localisation/chaosx_scripted_localisation_settings.txt` repeat the same broad numeric selector pattern with different source variables.

`GetEventsLogEvolutionSourceEventNameView` and `GetEventsLogHistoryEventName` in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` repeat numeric branches while also handling special Fallout, CBRN, evolution, and history IDs that are not ordinary event-system IDs.

The localisation file is the destination authority for player-facing names; the scripted-localisation files are selector authority; event files and Event Log rows are data producers and must not each invent another selector table.

### Migration design

First inventory every `defined_text` name, source variable, numeric trigger, `localization_key`, special constant, and fallback across the three selector files and all shared call sites, including the shared consumers that expose Events 21+ IDs.

Create a machine-checkable mapping during implementation planning, not as a runtime router, with columns `selector`, `source`, `numeric_or_constant_id`, `localization_key`, `special_context`, `fallback`, and `owner`.

Choose one canonical `GetEventName` owner only after proving whether a selector can safely bridge a context-specific variable such as `settings_event_id`, `global.last_fired_event_id`, or `global.events_log_view_event_id_entries^events_log_history_index` into the canonical selector without leaking or overwriting caller state.

If a context bridge is supported, the bridge must save the source value into a temporary variable or an explicitly scoped normal variable, call the canonical selector, and restore or clear the bridge context before returning; temporary variables must not be addressed through `ROOT` or `PREV`.

If scripted localisation cannot safely parameterize another selector in the relevant UI context, retain thin explicit adapters generated from the same reviewed mapping rather than forcing an unsupported dynamic localisation key or a global context variable.

The canonical fallback must be `chaosx.event_name.unknown`; the current literal `"Unknown Event"` is not an acceptable second fallback because it bypasses the named localisation key and creates language drift.

Do not synthesize `chaosx.event_name.100` through `chaosx.event_name.1000` merely to make the table compile; every destination must correspond to a registered system event, an explicitly supported history/provider ID, or the canonical unknown key.

Keep Fallout history keys, CBRN action key 991, Doctor Wu 163, Event 006 history/evolution payload keys, and any other non-system selectors in explicit special branches until their source ID contract is documented.

### Reference proof and tests

The source proof must include `rg` references for every selector and destination, a localisation-key inventory, and a generated report showing no undefined destination remains in an active branch.

The dynamic-localisation proof must use `hoi4.gui_inspect` and `hoi4.gui_render` on settings, history, evolution, event detail, and debug-visible contexts where the route supports them, with before/after comparison artifacts; source-only proof is insufficient for the context bridge.

The semantic test matrix must include IDs 1, 2, 6, 11, 13, 20, 21, 99, 100, 163, 635, 641, 991, an Event 21+ shared ID, a Fallout history ID, an evolution source row, an unregistered ID, and zero or missing source values.

The expected result is exactly the previous visible name for each defined destination, the same special-provider name for special rows, and the same unknown fallback for an undefined or unavailable ID.

The adapter test must confirm that the caller's settings, `last_fired`, and Event Log row variables are unchanged after name resolution.

### Rollback boundary

Retain the existing selector tables and all existing localisation keys until the canonical selector and every adapter have passed the matrix and compare artifacts.

Remove duplicated branches only in a separate commit after a zero-reference audit proves no caller still targets the removed selector name or source-variable contract.

If the dynamic bridge is unsupported, roll back only the adapter change and keep the explicit tables generated from the reviewed mapping; do not introduce a new global context variable as a fallback.

## Finding 2: shared periodic and on-action scheduler ownership

### Current ownership

`common/on_actions/chaosx_on_actions_system.txt:on_startup` initializes the event system and iterates `every_country` and `every_possible_country` for activation, timers, settings, and window values.

`common/on_actions/chaosx_on_actions_system.txt:on_daily` is the shared scheduler and is explicitly documented as running for every country.

The daily path performs tag-switch detection, event activation changes, timer handling, random filter setup, `select_weighted_random_event_id`, automatic context assignment, `fire_event_by_temp_id`, context cleanup, and optional debug logging.

`common/on_actions/chaosx_on_actions.txt` owns shared startup and state-control hooks and documents that unqualified periodic on-actions evaluate all countries; event-owned hooks live in event-specific files.

`common/scripted_effects/chaosx_logic_effects.txt` owns selection and category/accounting helpers, while `common/scripted_effects/chaosx_settings_effects.txt` owns manual settings controls and generic firing controls.

### Migration design

Build an ownership matrix for every `on_startup`, `on_daily`, `on_weekly`, `on_monthly`, and tag-specific on-action before moving or extracting any call.

An optional `chaosx_event_scheduler_tick_country` helper may be extracted from the existing daily body only if its scope is COUNTRY, its inputs and outputs are explicit, and the existing single `on_daily` call remains the only broad caller.

The helper must preserve the order of tag-switch handling, timer decrement, random selection, automatic context assignment, event firing, and context cleanup, because moving a cleanup effect across a branch can change duplicate firing or stale-context behavior.

No new whole-world iteration may be added to refresh Event Log views, target cleanup, category migration, or localization migration.

If a narrower caller exists for a feature-specific update, use a country-scoped or tag-specific call site; do not convert it into `every_country` merely to make a helper convenient.

Any proposal to split the current `on_daily` into multiple broad on-actions, change its cadence, or replace it with a global scheduler is blocked pending explicit user authorization and a scenario-level performance and behavior baseline.

### Semantic tests

For a fixed country set and seed, compare timer values before and after each daily tick, activation flags after tag switch, selected event ID, automatic context flags, fired event count, and cleanup state.

The equivalence test must prove that no country receives more than one scheduler attempt per existing daily iteration and that no country outside the original caller scope is touched.

The scheduler test must include disabled countries, human-to-AI and AI-to-human switches, timer zero, timer greater than zero, no candidates, a selected event with a failed trigger, and a successful fire.

Weighted selection is covered by the probability route in the validation matrix below; source weights alone are not sufficient.

### Rollback boundary

Keep the original on-action body until the candidate helper produces identical state snapshots for the named scheduler scenarios.

If helper extraction changes an effect order or scope, revert the helper call only and leave the original scheduler owner intact.

No scheduler migration is implementation-ready while the required probability auditor or the current probability MCP route is unavailable.

## Finding 3: mixed literal and script-constant event-category IDs

### Current ownership and compatibility risk

`initialize_event_categories` in `common/scripted_effects/chaosx_logic_effects.txt:223` currently mixes literal IDs and constants in `global.major_events`, `global.fire_once_events`, and `global.repeatable_events`.

The major list currently contains literal IDs 2, 25, 30, 44, 49, 70, 80, and 91.

The fire-once list contains literal IDs plus constants such as `africa_event.id`, `cannibalism_event.id`, `utopia_manifesto_event.id`, `brilliant_scientist_event.id`, `doctor_wu_event.id`, and `black_plague_identity.event_id`.

The repeatable list contains literal IDs plus `natural_disaster_event.id`, `random_faction_event.id`, `resources_found_event.id`, and `infantry_spawn_event.id`.

`initialize_all_events_array` concatenates the three arrays in major, fire-once, repeatable order, and `get_event_type` at line 1192 searches those arrays and returns `constant:event_system_event_type.*` in a temp variable.

Category membership and order feed weighted selection, weight and cap initialization, unfired counters, default-disabled queues, event log type/name paths, and any saved array state, so a syntactic constant cleanup can still be a save-breaking data migration if it changes a value, duplicate, or order.

`common/script_constants/event_system_constants.txt:event_system_event_type` defines the type values unknown 0, major 1, repeatable 2, fire-once 3, fallout-country-memory 4, and CBRN action 5; these type values must remain stable.

### Migration design

Produce a resolved category table that records each entry's numeric value, source spelling, category, array index, event root, localization key, and whether the ID is a system category member or a special Event Log/history ID.

Use named script constants only as aliases for already-resolved numeric IDs and only in fields that accept `constant:` tokens, with an engine parse check for each effect field.

Do not reorder arrays while replacing literals, do not remove duplicate entries without proving they are unintended and absent from saved state, and do not change the numeric values of any category or type.

Retain a compatibility layer for old literal references until all direct call sites and saved-array assumptions are audited; compile-time constants do not migrate already-saved runtime arrays.

Keep the category registry owner in `chaosx_logic_effects.txt`; do not create a second registry in `chaosx_dynamic_effects.txt` or a cross-file local `@` constant table.

If a script constant is rejected by an array or comparison field, retain the literal in that field and document the unsupported field rather than adding a dynamic/meta workaround without proof.

### Semantic and save tests

Before any change, serialize the resolved major, fire-once, repeatable, and `global.all_events` sequences, event weights, caps, unfired counters, and disabled queue for a representative new game and a loaded save.

After the candidate change, compare exact ordered arrays and all derived arrays, not merely set membership.

Run `get_event_type` checks for every category ID, every special constant ID, an unlisted ID, and the type values used by Event Log history rows.

The save-compatibility gate is a hard equality of persisted ID values and array positions for all existing saves in the test set; no migration proceeds if old saves require reinterpretation of a category array.

The probability gate must compare the same weighted scenarios before and after the category refactor, including no-candidate, repeatable, fire-once, major-triggered, disabled, and capped-event cases.

### Rollback boundary and authorization

The first implementation tranche may add aliases or an audit-only resolved table without changing consumers.

Replacing literals in the live registry is blocked until save compatibility and probability comparison evidence are available.

Any renumbering, array reordering, category reassignment, removal of a legacy ID, or change to an old-save interpretation requires explicit user authorization and a versioned migration strategy that this plan does not define.

## Finding 4: Event 006 registry and collection migration risk

### Current source contract

`common/collections/006_independence_wave_country_collections.txt` states that its named collections are active views over dormant-capable country-group arrays and are not replacements for static arrays when checking dormant carrier availability or reserving a package.

The collection definitions include `independence_wave_all_resolved_carriers`, `independence_wave_event6_owned_new_tags`, `independence_wave_registered_reuse_tags`, selectable bound and unbound views, Event 006 owned bound and unbound views, registered reuse bound and unbound views, and overlay route-carrier views.

`common/script_constants/006_independence_wave_country_registry_constants.txt` is the static authority for the 206-row registry, 191 unique resolved carrier tags, 102 Event 006-owned X tags, 89 registered reuse tags, and the bound, unbound, and shared counts used by the allocator and audits.

`common/scripted_triggers/006_independence_wave_country_registry_triggers.txt` owns exact-tag membership and provenance gates, including Event 006 origin, Soviet origin, Africa origin, Event 006-owned tag, registered reuse tag, resolved carrier, and Africa overlap predicates.

`common/scripted_effects/006_independence_wave_country_registry_effects.txt` owns the narrow Event 006 origin wrappers `independence_wave_registry_record_event6_origin` and `independence_wave_registry_clear_event6_origin`; the file explicitly prohibits Event 012 from calling them.

`common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` owns the central adapter chain for setup, final validation, and cleanup without a world iteration.

The package and row authorities are `common/script_constants/006_independence_wave_package_constants.txt`, `docs/spreadsheets/006_candidate_country_registry.csv` as an audit/input artifact where applicable, and `docs/spreadsheets/006_current_installed_map_package_bindings.csv`; these files must not be treated as interchangeable runtime authorities.

### Migration design

Before a collection migration, snapshot every row's row ID, carrier tag, provenance, package ID, reservation group, bound/unbound status, active country existence, formable/overlay role, and current ledger state.

Prove that the static arrays remain authoritative for dormant or reserved tags and that every collection is only an active scope view with a missing-country result that is expected and not a prompt to substitute another carrier.

Use the existing lifecycle wrappers as the only origin-state mutation boundary; do not add Event 012 calls or merge Africa ownership into Event 006 helpers.

If a compatibility adapter is needed, it may translate an old row or package token into the canonical row contract while leaving the old array and flags readable for old saves; it must not silently allocate a nearby carrier.

Do not replace static arrays with collection inputs until dynamic country creation, tag reservation, save loading, package cancellation, reclamation, cleanup, and protected-tag audit behavior are all covered.

The registry migration requires an explicit decision on whether row identity, carrier identity, collection identity, and reservation identity are separately persisted; a collection name alone cannot be used as proof of row compatibility.

### Required audits and semantic tests

Run `.tools/audit_chaosx_country_tags.py`, `.tools/audit_event6_allocator.py`, `.tools/audit_event6_country_api.py`, `.tools/audit_event6_flags.py`, and `.tools/audit_event6_scenario_matrix.py` against the approved source snapshot after any implementation tranche.

Compare the 206-row registry and the 191 unique resolved-carrier set exactly before and after the candidate change, including the 89 registered-reuse, 137 bound, 55 unbound, and 1 shared counts recorded by the constants.

Exercise bound, unbound, dormant, missing active country, reserved, overlay, Africa-overlap, reclaimed, cancelled, and terminal rows.

Prove that package allocation, event origin flags, `liberation_origin`, reservation ledgers, and cleanup remain identical for the same scenario and that no Event 012 state is touched by an Event 006 helper.

Run `hoi4.event_inspect` for `chaosx.nr6.1` with bounded helper expansion, then `hoi4.event_render` and `hoi4.event_compare` for the relevant entry and cleanup scenarios; the current route timeout means this gate is currently blocked.

### Rollback boundary and authorization

Keep the existing static arrays, collection definitions, old flags, and compatibility readers until all approved scenarios pass.

Any change to row order, carrier tag, reserved tag identity, package identity, collection identity, allocator capacity, protected tag behavior, or old-save interpretation requires explicit user authorization.

No Event 006 registry/collection migration is implementation-ready merely because collections compile or the structural event inspect passes.

## Finding 5: Event 019 dynamic provider and `meta_effect` dispatch contract

### Current source contract

`common/scripted_effects/019_infantry_spawn_core_effects.txt:infantry_spawn_evaluate_current_registry_row` reads `global.chaos_unit_family_provider_id_entries^chaos_unit_family_registry_index` into `infantry_spawn_current_registry_provider_id` and calls `chaos_unit_family_provider_[PROVIDER]_event19_evaluate_eligibility = yes` through `meta_effect`.

`common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt:infantry_spawn_unit_registry_dispatch_static_token` calls `infantry_spawn_unit_registry_token_provider_[PROVIDER_ID] = yes` through `meta_effect` using `infantry_spawn_unit_registry_current_provider_id`.

The same unit registry file uses dynamic `meta_effect` injection for `division_template`, unit tokens, and provider callbacks at the template and derivative paths.

`common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt` contains additional provider dispatch, cleanup, and meta-trigger paths that must be treated as part of the contract, not as incidental duplication.

`common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt` registers Event 016 provider IDs and eligibility, template, spawn, sustainment, and cleanup callbacks, including providers 504 through 510 and 522.

The current Event 019 source-of-truth policy keeps owner adapters for providers 511–514, 518, and 520–522 in their existing parent integrations; moving these adapters into a new consolidated registry would change ownership and requires a new design decision.

### Migration design

Treat the generated names `chaos_unit_family_provider_[PROVIDER]_event19_evaluate_eligibility` and `infantry_spawn_unit_registry_token_provider_[PROVIDER_ID]` as a stable API contract.

Document each provider ID's callback set, required input variables, output variables, failure behavior, template token, dynamic localisation or meta-effect fields, and cleanup owner before any helper extraction.

Add a narrow provider contract validation helper only if it can inspect the aligned registry arrays without changing provider order, candidate weighting, provider-specific gating, template generation, spawn behavior, or cleanup.

Unknown or missing provider IDs must fail closed and mark the existing ledger/invariant failure state; a fixed-tag or fixed-provider fallback is not permitted without user approval.

Keep Event 016 bridge ownership and fixed provider constants in their current file until the parent approves a provider registry redesign.

### Dynamic/meta reference proof

The implementation audit must enumerate every `meta_effect` and `meta_trigger` in the three Event 019 files and Event 016 bridge, including the placeholder variables `[PROVIDER]`, `[PROVIDER_ID]`, `[UNIT_TOKEN]`, and `[DIVISION_TEMPLATE]`.

For each generated effect name, prove the generated token for a valid provider, an invalid provider, a disabled provider, and a provider whose callback intentionally fails.

Use `hoi4.event_inspect` with helper expansion and `hoi4.event_render` or a bounded event scenario to verify the generated dispatch path, then use `hoi4.event_compare` after any candidate change; source text alone cannot prove dynamic effect expansion.

The current Event 019 MCP call timed out, so this proof is blocked.

### Semantic tests and rollback

Compare native family selection, eligibility flags, total weight, selected registry index, generated template token, spawn payload, sustainment state, derivative package state, and cleanup for every provider family in the approved scenario matrix.

The test set must include Event 016 providers 504–510 and 522, parent-owned providers 511–514, 518, and 520–522, an unavailable provider, an invalid provider ID, and a provider callback failure.

Do not collapse aligned arrays or replace provider callbacks until the candidate output and failure/cleanup traces match the current contract.

Rollback is limited to the new validation or adapter call; provider callback definitions and current dispatch names remain intact until the parent accepts a provider-contract migration.

## Finding 6: global event-target lifecycle cleanup proof

### Ownership rule

The event that saves a global target owns its lifetime decision; Event Log effects are consumers and must not clear a target merely because a row is being rendered.

Regular event targets saved with `save_event_target_as` are chain-scoped and automatically clear when the originating effect chain ends, while global targets saved with `save_global_event_target_as` persist until an explicit `clear_global_event_target` or `clear_global_event_targets` call.

`has_event_target` proves only current target availability; it does not prove that a target is stale, safe to clear, or intended to be persistent.

### Inventory and classifications

Build one inventory with columns `target_name`, `save_file:line`, `clear_file:line`, `has/use_file:line`, target kind, owner, chain entry, terminal path, cancel path, failure path, reload behavior, tag-switch behavior, and persistence rationale.

The first inventory pass must include `independence_wave_latest_actor`, `independence_wave_reclamation_front_coordinator`, `holy_realm_country`, `random_war_aggressor`, `black_plague_rat_evolution_actor`, `fury_latest_actor`, `secret_alliance_target`, `utopia_manifesto_latest_actor`, `brilliant_scientist_prefire_host`, `africa_host`, `africa_prefire_host`, `cannibalism_first_host`, `cannibalism_latest_actor`, `random_faction_target_country`, `resources_found_prefire_owner`, `white_peace_primary`, `natural_disaster_log_actor`, and `death_country`, plus every other `save_global_event_target_as` and `event_target:` occurrence found by the owner audit.

Event 006 targets such as `independence_wave_latest_actor` and `independence_wave_reclamation_front_coordinator` must be reviewed with package, reclamation, and super-event cleanup rather than a generic Event Log cleanup.

Event 011, Event 016, and Event 019 targets require their own source-owner tables because provider or alliance chains can outlive a single event option.

Targets used for persistent history, achievement, localisation, scenario, or terminal pointers may legitimately have no local clear; the absence of a clear is a review finding, not proof of debt.

### Migration design

Classify each target as short-lived chain state, active scenario state, persistent history pointer, or unresolved.

For short-lived chain state, prefer regular event targets when the pointer only needs to cross events fired from the same chain; use a global target only when the persistence requirement is documented.

For persistent global targets, add an owner-specific clear only at a documented terminal or replacement boundary and preserve the last historical value when Event Log or achievement consumers require it.

For unresolved targets, do not add a clear; first prove all writes and reads and obtain owner direction.

Where a target is overwritten, prove whether the old target must be cleared before the new save and whether any consumer can observe the transition between effects.

No generic `clear_global_event_targets` call is allowed in `on_daily`, Event Log refresh, window close, save/load initialization, or a shared cleanup helper.

### Semantic tests and rollback

For every target owner, exercise success, cancellation, trigger failure, timeout, terminal/world-end, reload, and human tag-switch paths, then assert `has_event_target`, target scope, flags, variables, and Event Log row behavior.

Prove that regular targets auto-clear at chain end and that global targets marked persistent remain available to their documented consumers.

If a new clear causes a consumer to lose an actor or pointer, revert that owner-specific clear without changing unrelated target lifecycles.

Target lifecycle migration is blocked for any target lacking a complete save/use/clear inventory or an owner-approved persistence classification.

## Finding 7: bounded functional Event Log tab/reset/detail consolidation

### Current ownership and duplication

`common/scripted_guis/chaosx_scripted_gui_events_log.txt` repeats tab-state, detail-close, and view-rebuild effects for status, history, evolutions, events, and clusters in idle and active click bindings.

The repeated bindings clear the mutually exclusive tab flags, close event details, clear evolution detail state, close history and cluster detail views, and rebuild the selected view.

`common/scripted_effects/chaosx_events_log_effects.txt` owns the data-side helpers `refresh_events_log_system_history_views`, `events_log_close_history_details_view`, `events_log_rebuild_history_details_view`, `events_log_rebuild_open_event_details_view`, `events_log_close_all_event_details_entries`, `rebuild_events_log_history_view`, `rebuild_events_log_evolution_view`, `rebuild_events_log_events_view`, `initialize_events_log_settings`, and the corresponding cluster/world-end detail helpers.

The current Event Log shell is `events_log_popup_window` in `interface/chaosx_events_log_popup.gui`; its tabs and dynamic lists are visual consumers, not ownership for gameplay data or cleanup.

### Bounded candidate

The only candidate consolidation is a functional helper such as `events_log_set_tab_state_and_rebuild` in `common/scripted_effects/chaosx_events_log_effects.txt` or a narrow scripted-GUI helper in `common/scripted_guis/chaosx_scripted_gui_events_log.txt`.

The helper input is the selected tab token or existing tab-state context; its output is one selected tab flag and one corresponding rebuild; its side effects are the same detail-close and array cleanup currently performed by the individual bindings.

The status tab must preserve its current no-list behavior and weight recalculation; history, evolutions, events, and clusters must preserve their current rebuild helper and detail close order.

Idle and active bindings may call the same helper only after proving that the current active/idle visibility and click semantics are identical.

The helper must be idempotent, must not rebuild unrelated views, must not clear persistent history rows, and must not alter `events_log_window_open` ownership.

This is a functional-only consolidation; it must not modify `interface/chaosx_events_log_popup.gui`, any `.gui` geometry, coordinates, click regions, window names, assets, sprite definitions, or visual hierarchy.

The shared Event Log is not eligible for `chaosx_event_ui_worker`; a parent-owned bounded source change is required if this phase is approved.

### Mandatory GUI evidence

Before any helper rewrite, run `hoi4.gui_inspect` for `events_log_popup_window` with a named scenario and retain the full artifact, state matrix, resolution matrix, hierarchy, modeled click regions, and unsupported-field diagnostics.

Before the rewrite, run `hoi4.gui_render` for the full window and cropped status, history, evolutions, events, clusters, event-detail, history-detail, and world-end-detail states, including annotated and comparison outputs where the route supports them.

After the rewrite, repeat the same inspect and render set and compare geometry, click regions, window hierarchy, visible states, and binding behavior; any visual or click-region difference blocks acceptance.

If `hoi4.gui_rewrite` is used, it must remain a narrow helper-only rewrite with dry-run, review, apply, post-validation, and rollback/recovery evidence; no layout rewrite is authorized.

The current GUI inspect route timed out after 180 seconds, so no implementation or rewrite is authorized until the route returns usable evidence.

### Semantic tests and rollback

For each tab, click idle and active states, switch from every other tab, close the window, reopen it, open and close each detail view, and click a row before and after switching tabs.

Compare all tab flags, `events_log_*_details_open` flags, selected IDs, aligned detail arrays, evolution arrays, world-end arrays, and rebuild counters or equivalent artifacts.

The source diff must contain only functional scripted-effect or scripted-GUI call-site changes; a diff touching `interface/`, assets, coordinates, or click regions is an automatic rollback.

Rollback is a single-source-file revert of the helper call sites and helper body, leaving the existing visual surface unchanged.

## Constants and tuning-table plan

Event category IDs and `event_system_event_type` values are compatibility constants, not balance knobs; assign names only after resolving and locking their existing numeric values.

Scheduler cadence, initial random timer range, timer minimum and maximum, and event weight/cap values remain owned by the existing event-system constants and logic files; a cleanup helper must not introduce duplicate timing or weight literals.

Event 006 registry counts, group identities, reservation classes, and row/package IDs remain owned by the existing `006_independence_wave_country_registry_constants.txt` and package constants; collection names are not substitutes for static count or row constants.

Event 019 provider IDs, family IDs, registry indices, and invalid-index values remain owned by the existing Event 019 and Event 016 constants; generated provider names must receive numeric IDs from the existing arrays or named constants rather than a second local table.

Event Log tab states, detail states, and filter/type values remain state variables or existing constants; introduce a tab enum only if the engine accepts it in every candidate field and the helper improves explicitness without changing saved state.

Script constants are global and file-independent, but fields that reject `constant:` tokens must retain a compatible literal or variable path; each proposed replacement needs a parser and runtime field check.

No new tuning table is approved until its owner, numeric stability, save impact, and all consumers are documented.

## Event-target and cleanup plan

The cleanup inventory is a prerequisite, not an after-the-fact audit.

Each owner-specific cleanup wrapper must document scope, target name, inputs, outputs, side effects, terminal paths, and the reason a target is cleared or intentionally retained.

Short-lived chain pointers should use regular event targets when they do not need persistence beyond the originating chain.

Global targets that persist for history or terminal scenarios require explicit replacement or terminal cleanup boundaries and a documented `has_event_target` consumer list.

Event Log refresh, tab switching, window close, and on-action scheduler paths must never perform blanket global-target cleanup.

Any cleanup helper added during implementation must be documented in the matching markdown file, especially `common/scripted_effects/chaosx_dynamic_effects.md` if and only if the helper is truly part of that dynamic-effect API; unrelated Event 006 or Event 019 helpers belong with their own source documentation.

## Migration phases and gates

### Phase 0: freeze, inventory, and baseline ownership

Capture `git status --short`, file hashes for each in-scope source file, the current owner map, and the concurrent dirty-worktree ownership before implementation.

Record every selector, category array, scheduler caller, collection, provider callback, target save/clear/use, and Event Log binding with file and line anchors.

No gameplay or UI source change is allowed in this phase.

Gate: the parent accepts the inventory and names a separately reviewable tranche.

### Phase 1: selector destination and context proof

Resolve the selector-to-localisation mapping, choose the canonical owner, prove context bridging or document why explicit adapters remain, and replace the literal unknown fallback only in an approved implementation change.

Gate: no undefined active destination, all special IDs classified, GUI context evidence available, and old/new visible names equal under the selector matrix.

Rollback: retain all old selector tables and revert only the candidate adapter or canonical call sites.

### Phase 2: scheduler ownership proof

Build the on-action ownership matrix and, only if approved, extract the existing country-scoped scheduler body without adding a new broad caller.

Gate: the original daily caller remains unique, cadence and scope are unchanged, and fixed-seed selection and tag-switch scenarios match.

Rollback: restore the original on-action body and leave helper documentation as a queued plan if extraction is not equivalent.

### Phase 3: category constant compatibility

Resolve literal and constant IDs, add only value-preserving aliases or audit scaffolding first, then compare category arrays, all-events order, weights, caps, counters, and old saves.

Gate: exact numeric and positional equality, probability compare evidence, and no unresolved special ID ownership.

Rollback: remove only aliases or candidate call sites; never rewrite old saved arrays.

### Phase 4: Event 006 registry/collection compatibility

Freeze the 206-row source contract, run the Event 006 audits, compare static arrays to active collection views, and design an additive compatibility adapter if one is necessary.

Gate: row/package/reservation identity, dormant handling, dynamic country lifecycle, Event 006 origin flags, and Event 012 isolation all match.

Rollback: retain static arrays and compatibility readers; do not delete legacy row or carrier names.

### Phase 5: Event 019 provider API proof

Enumerate provider callback contracts, prove generated meta-effect names and payloads, compare Event 016 and parent-owned providers, and add only a narrow validation helper if it is semantically inert.

Gate: dynamic dispatch, invalid-provider failure, template/spawn/sustainment, and cleanup evidence match under event MCP inspection and compare.

Rollback: restore the previous dispatch call sites; do not move provider adapters or add a fixed fallback.

### Phase 6: global target lifecycle cleanup

Classify every target, add owner-specific cleanup only for proven non-persistent state, and test terminal, cancellation, failure, reload, and tag-switch paths.

Gate: every target has a documented owner and lifecycle proof, and persistent targets remain available to their consumers.

Rollback: revert each new clear independently; do not add a shared clear loop.

### Phase 7: Event Log functional consolidation

Only after GUI MCP routes return, capture before evidence, add the narrow tab/reset/detail helper, update functional call sites, and capture identical after evidence.

Gate: tab/detail behavior and arrays are equivalent, geometry and click regions are byte- or artifact-equivalent where the MCP supports comparison, and no interface or asset file changed.

Rollback: revert the scripted helper and call sites only.

### Phase 8: documentation and catalog reconciliation

Update matching helper markdown, system docs, localisation mapping documentation, and event catalog source only after gameplay facts are accepted.

If event detail or evolution wording changes, edit `docs/spreadsheets/chaos_redux_events_catalog.xlsx` as the only spreadsheet source and run `python .tools/export_event_catalog_csv.py` from the mod root; never edit export CSVs directly.

Gate: source identifiers, player-facing localisation, docs, and workbook wording agree; no stale plan or handoff claims an unimplemented migration.

## Semantic-equivalence test matrix

| Surface | Baseline snapshot | Candidate comparison | Required edge cases | Acceptance condition |
| --- | --- | --- | --- | --- |
| Event-name selectors | Selector name, source variable, ID, destination, fallback, and special branch | Rendered localized text plus caller variable state | IDs 1, 2, 6, 11, 13, 20, 21, 99, 100, 163, 635, 641, 991, Event 21+ shared ID, Fallout history ID, zero, missing, unknown | Defined names unchanged, special names unchanged, undefined IDs use `chaosx.event_name.unknown`, and no caller context leaks |
| Scheduler | Per-country timer, flags, selected ID, fire count, automatic context, cleanup | Same fixed-seed daily and tag-switch trace | Disabled, no candidate, timer zero, timer positive, human-to-AI, AI-to-human, trigger failure, successful fire | Same scope, cadence, event count, selected IDs, and post-tick state; no added broad iteration |
| Category registry | Ordered major, fire-once, repeatable, all-events arrays, weights, caps, counters, disabled queue | Exact value and index comparison on new game and old save | Special constants, unknown ID, duplicate audit, category overlap, major trigger, cap and default-disabled paths | Numeric values and order are identical; weighted outcomes compare under same scenarios |
| Event 006 registry | 206 rows, 191 unique carriers, provenance, package/reservation groups, counts, flags | Static registry and collection view plus allocator/cleanup trace | Bound/unbound, dormant, missing active country, reserved, overlay, Africa overlap, reclaimed, cancelled, terminal | No carrier substitution, no row/package identity drift, Event 012 remains isolated, flags and ledgers match |
| Event 019 provider API | Provider ID arrays, callback names, templates, spawn/sustainment/cleanup outputs | Generated meta-effect tokens and provider traces | Providers 504–510, 522, 511–514, 518, 520–522, disabled, invalid, missing, callback failure | Valid provider outputs and failures match; no fixed fallback; cleanup remains provider-owned |
| Event-target lifecycle | Save/clear/has/use inventory and persistence classification | Target existence, scope, flags, and consumer behavior at each terminal | Success, cancel, failure, timeout, world-end, reload, tag switch, replacement | Only proven short-lived targets clear; documented persistent pointers remain available |
| Event Log bindings | Tab flags, detail flags, selected IDs, aligned arrays, rebuild helper and click mapping | Before/after MCP GUI and functional scripted state | Every idle/active tab, window close/open, each detail type, row click, tab switch while detail open | Same functional state and click mapping; no geometry, coordinates, click regions, or assets change |

## MCP and probability route matrix

| Surface | Required route | Required sequence | Current status and blocker |
| --- | --- | --- | --- |
| Event 006 | `hoi4.event_inspect`, `hoi4.event_render`, `hoi4.event_compare` | Inspect bounded entry and helper projections, render setup/cleanup or relevant states, compare before/after | Baseline structural artifact exists; current bounded `hoi4.event_inspect` for `chaosx.nr6.1` timed out after approximately 220 seconds |
| Event 019 | `hoi4.event_inspect`, `hoi4.event_render`, `hoi4.event_compare` | Inspect dynamic helper/meta projections, render provider scenarios, compare generated dispatch and cleanup | Baseline structural artifact exists; current bounded `hoi4.event_inspect` for `chaosx.nr19.1` timed out after approximately 220 seconds |
| Event Log GUI | `hoi4.gui_inspect`, `hoi4.gui_render`, and only if required `hoi4.gui_rewrite` | Inspect full/state/resolution/hierarchy/click regions, render full/cropped/annotated before, apply narrow helper rewrite, repeat after and compare | Baseline partial artifact exists; current `events_log_popup_window` inspect timed out after 180 seconds; no rewrite is authorized |
| Weighted scheduler and category selection | `hoi4.probability_inspect` first, then `hoi4.probability_evaluate`, `hoi4.probability_sweep`, `hoi4.probability_compare`, and sequence/simulation/render as scenario requires | Establish named baseline scenarios, apply owner patch, compare with identical inputs and seeds | Baseline custom-pool artifact exists; current inspect timed out after 180 seconds and `chaosx_ai_probability_auditor` is not callable in this runtime |
| Focus, map, and unrelated GUI surfaces | Matching read-only route only if a later implementation touches them | Inspect before designing or changing a helper | Out of this plan; no source-only substitute is allowed if a future call site enters scope |

Weighted surfaces include random event selection, category-dependent weights and caps, event `ai_chance`, decision or mission scores if discovered in shared consumers, random lists, MTTH-backed scores, and any custom weighted pool.

Every approved weighted patch requires a baseline audit, an owner-applied patch, and a `hoi4.probability_compare` pass using the same named scenarios through `chaosx_ai_probability_auditor`.

If the auditor route remains unavailable, the weighted migration remains blocked; source review and the existing baseline probability artifact do not substitute for the required evidence.

## Dynamic, meta, and scripted-localisation reference proof

The implementation owner must produce a reference inventory for every `meta_effect`, `meta_trigger`, generated provider name, generated localisation key, and scripted-localisation source variable touched by a migration.

The inventory must identify the exact placeholder expansion, the scope in which it is evaluated, the required input variable, the output variable or text, the failure behavior, and any cleanup required after the expansion.

For Event 019, the proof must show the generated provider token and the callback definition for each provider family.

For event names, the proof must show the source ID, destination key, special override, and unknown fallback for every active selector branch.

For Event Log details, the proof must show that row arrays remain aligned after detail close, tab switch, and rebuild and that localization context does not depend on a stale event target.

No dynamic or meta contract is accepted solely because the source parser accepts the text; the applicable event or GUI MCP inspect/render/compare artifact is required.

## Documentation, localisation, and catalog impacts

This planning pass changes no localisation, catalog, helper markdown, or gameplay file.

An approved selector migration must update `localisation/english/chaosx_event_names_l_english.yml` only for keys confirmed by the resolved mapping and must document why each special or unknown key exists.

An approved new dynamic helper must be documented in `common/scripted_effects/chaosx_dynamic_effects.md` only when it belongs to the shared dynamic-effect API; Event 006 helpers remain documented in `common/scripted_effects/006_independence_wave_country_registry_effects.md` or the owning Event 006 markdown file, and Event 019 contracts must be documented with the Event 019 registry/spec source.

An approved Event Log functional consolidation must update `docs/systems/event_system/events_log_window.md`, `docs/systems/event_system/events_log_evolutions_and_clusters.md`, and `docs/systems/event_system/events_log_world_end_scenarios.md` if their ownership or lifecycle descriptions change; it must not update the interface layout description to claim a geometry change.

Event catalog rows are changed only when player-facing event detail, evolution, or cluster wording changes; the workbook is the editable source and the export command must be run after a successful workbook update.

Documentation must describe scope, inputs, outputs, defaults, side effects, cleanup, unsupported fields, call sites, and rollback behavior for every accepted helper.

## Blockers and explicit authorization requests

The Event 006 and Event 019 MCP routes currently time out, so their dynamic helper and lifecycle migrations are blocked.

The shared Event Log GUI inspect route currently times out, so the functional binding consolidation is blocked until before/after evidence can be captured.

The required `chaosx_ai_probability_auditor` is not callable in the current tool inventory, so weighted migrations are blocked pending that route or an equivalent parent-orchestrated evidence pass.

Any new or widened whole-world periodic iteration requires explicit user authorization; this includes moving Event Log refresh or target cleanup into a new `every_country` or unqualified on-action.

Any Event 006 change to row order, carrier identity, collection identity, reservation identity, protected tags, allocation counts, or old-save interpretation requires explicit user authorization.

Any Event 019 move of provider ownership, replacement of dynamic dispatch with fixed providers, or fallback for an unknown provider requires explicit user authorization.

Any event-category renumbering, category reassignment, array reorder, legacy ID removal, or save migration requires explicit user authorization and is outside this plan's implementation scope.

Any target cleanup without a complete save/clear/has/use inventory and documented persistence classification is blocked.

Any interface, geometry, coordinate, click-region, asset, or layout change is a non-goal and requires a separate task.

The undefined event-name destinations cannot be resolved by inventing localization keys; the parent must choose between a registered-only map, the canonical unknown fallback, or an explicitly approved special-ID mapping after the reference audit.

## Rollback and recovery policy

Each phase is a separate implementation tranche with a separate review and rollback boundary; no phase may rely on an unreviewed future phase.

Old selector tables, category arrays, Event 006 static registry data, Event 019 provider callbacks, and Event Log functional bindings remain in place until their replacement has passed the relevant semantic tests.

Compatibility aliases are additive and reversible; removal requires a zero-reference audit, saved-state proof, and a parent-approved commit.

Any failed MCP comparison, unresolved parser field, changed scope, changed effect order, changed click region, or missing localization destination stops the phase and leaves the previous owner active.

Recovery evidence must record the failed scenario, artifact reference, source diff, and exact rollback boundary; do not mask a blocked route with source-only claims.

## Completion criteria for a future implementation

A future implementation is complete only when the accepted phase has its source-owner map, helper documentation, call-site list, constants table, cleanup proof, semantic-equivalence artifacts, applicable MCP evidence, probability baseline/compare evidence where weighted, localisation/catalog updates, and rollback record.

The parent must report any queued, rejected, superseded, or unresolved migration explicitly and must not call a partial selector, scheduler, registry, provider, target, or Event Log cleanup pass complete merely because the game parses.

## Remaining risks

The dirty shared worktree can make line-level diffs and MCP source snapshots non-reproducible until each implementation tranche establishes its own baseline.

The current Event MCP graph is partial and may omit helper expansion or cross-file dynamic dispatch, so event inspection artifacts must be read with their diagnostics and unsupported-field report.

The current GUI artifact has truncated diagnostics and unsupported or unresolved items, so it cannot prove geometry or click-region equivalence.

The probability route and auditor are unavailable in this runtime, leaving weighted behavior unproven.

Scripted-localisation context bridging may be engine-limited; an explicit adapter table may remain necessary, but its destinations must still come from one reviewed mapping.

Event category arrays, global event IDs, and saved variables may encode order and numeric identity more deeply than source references reveal.

Event 006 static arrays and live collection views have intentionally different dormant-country semantics; conflating them can silently allocate the wrong carrier.

Event 019 provider IDs are an API boundary across multiple files, and a generated meta-effect name can fail without a clear source parser error if its provider token or scope is wrong.

Global event targets may be persistent by design for history, achievement, localisation, scenario, or terminal consumers, so an apparently clean blanket clear can be a regression.

The shared Event Log has parallel tab, detail, evolution, cluster, and world-end arrays; a harmless-looking reset consolidation can break alignment or stale selection behavior.

## Handoff summary

Exact changed file: `docs/plans/repo_cleanup/shared_system_migration_plan_2026-08-22.md` only.

Gameplay, localisation, spreadsheet, interface, scripted GUI, asset, `.codex`, and `.qoder` files were not changed.

No commit was created.

Evidence reviewed: required repository instructions, the repo cleanup master prompt, the events, decisions/missions, and subagents skills, required offline wiki pages, required vanilla documentation, current shared helper and owner files, existing cleanup baseline handoffs, Event 006 and Event 019 structural MCP artifacts, the shared Event Log GUI artifact, and the baseline custom weighted-pool artifact.

Known blockers: current Event 006/Event 019 event-inspect timeouts, current Event Log GUI-inspect timeout, current probability-inspect timeout, unavailable `chaosx_ai_probability_auditor`, dirty concurrent worktree, and unresolved engine support for dynamic scripted-localisation and provider/meta-effect proof.

No simplification or fallback was implemented; every blocked migration is marked as blocked rather than represented as complete.
