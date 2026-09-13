# Repo Explorer Handoff

## Scope read

- Parent task: read-only repository exploration for the complete Event 029 Riches Found rework.
- Explicit constraints: inspect the complete specification pack, current Event 029 and related sources, Event 018 and Event 088 separation surfaces, offline wiki and vanilla documentation, and write only this report under `docs/plans/029_riches_found_plans/`.
- Files and identifiers requested: `chaosx.nr29.1`, `chaosx.nr29.2`, `chaosx.news.31`, the Event 029 repeatable registration, recipient/state target gates, state/controller lifecycle, decisions and missions, modifiers/ideas/constants/scripted helpers, AI and MTTH, Event Log/Details/evolutions, achievements, assets/GFX, on_actions, documentation, and catalog alignment.
- Specification pack read in full: `README.md`, `029_riches_found_goal_prompt.md`, `029_riches_found_acceptance_criteria.md`, `029_riches_found_coding_prompt.md`, `029_riches_found_decision_mission_prompt.md`, `029_riches_found_ai_probability_scenarios.md`, `029_riches_found_asset_prompt.md`, `029_riches_found_catalog_alignment.md`, `029_riches_found_research_notes.md`, `029_riches_found_source_review_manifest.md`, and all six `029_riches_found_spec_part_*.md` files.
- Repo skills read: `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-mtth`, and `chaos-redux-subagents`.
- Offline wiki pages read: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface Modding, Scripted GUI Modding, Achievement modding, and Map modding.
- Vanilla documentation read from `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation`: `script_concept_documentation.md`, `dynamic_variables_documentation.md`, `loc_objects_documentation.md`, `effects_documentation.md`, `triggers_documentation.md`, and `modifiers_documentation.md`.
- Observed-state caveat: parent-side Event 029 files were being added or changed during this exploration. The findings below describe the final observed snapshot and distinguish in-progress scaffolding from validated implementation; this report makes no completion claim.

## Primary findings

- `events/029_riches_found.txt:22-52` is still a two-event stub: `chaosx.nr29.1` randomly chooses a country and fires `.2`, while `.2` uses the Finland Petsamo picture and grants `2000` political power. It does not select or commit a state, initialize a mine, show the required `1000` political-power grant, open decisions, or start an evolution chain.
- `common/scripted_effects/chaosx_logic_effects.txt:228-290` already registers Event 029 in `global.repeatable_events`, but the entry is a raw `29` rather than `constant:riches_found_event.id`; the shared active-pool and pacing machinery still depends on a valid event-specific prefire contract.
- A substantial in-progress scaffold exists in `common/script_constants/029_riches_found_constants.txt`, `common/scripted_triggers/029_riches_found_triggers.txt`, and `common/scripted_effects/029_riches_found_effects.txt`, with registry, state values, lifecycle, controller, evolution, and achievement helper names. The scaffold is not connected to the event root and is not engine-validated.
- The shared dispatcher expects `riches_found_prefire_owner` and `riches_found_prefire_state` at `common/scripted_effects/chaosx_settings_effects.txt:4633-4645,4780-4789`, but the current Event 029 preparation helper saves only `riches_found_prepared_mine_state` and never sets the expected owner or ready value. The repeatable event therefore has a concrete prefire wiring gap.
- The repository does have a proven narrow controller-change surface: `on_state_control_changed` with `ROOT` as new controller, `FROM` as old controller, and `FROM.FROM` as the exact state. The current Event 029 on-action calls `riches_found_handle_state_control_change`, but MCP engine inspection was unavailable, so this remains source-level evidence pending runtime validation.
- Decisions, missions, AI strategy/MTTH, Event 029 localisation, achievement definitions, Event 029 `.gfx`, and the Event 029 gameplay documentation file were absent in the observed snapshot. Runtime report/category DDS files exist, but their GFX registration and most icon consumers do not.
- The specification intentionally has no cluster, super-event, focus tree, technology, map-resource addition, country tag, portrait, animation, unit, model, or audio surface. Those should not be invented during implementation.

## Relevant files

| Path | Why it matters | Evidence |
| --- | --- | --- |
| `events/029_riches_found.txt` | Event roots and options for `chaosx.nr29.1/.2`. | Lines 22-52 still use `random_country`, `GFX_report_event_FIN_petsamo_mine`, and `add_political_power = 2000`; no state target or `riches_found_commit_discovery`. |
| `events/_chaosx_news.txt` | News wrapper for `chaosx.news.31`. | Lines 428-444 define the existing major triggered-only news event using `GFX_news_random_resource`; the rework must decide whether this wrapper remains the opening notice and localise it accordingly. |
| `common/scripted_effects/chaosx_logic_effects.txt` | Event registration, active-pool evaluation, repeatable weights, pacing, and `get_event_type`. | `initialize_event_categories` is defined at line 228; Event 029 is added to `global.repeatable_events` at line 290; the shared pool evaluates custom eligibility before dispatch. |
| `common/scripted_effects/chaosx_settings_effects.txt` | Shared random-event prefire and dispatch contract. | Lines 4633-4645 call `riches_found_prepare_random_event_fire` and require owner/state targets; lines 4780-4789 dispatch `chaosx.nr29.1` only when both expected targets exist. |
| `common/scripted_triggers/chaosx_settings_triggers.txt` | Shared reworked-event allowlist/default behavior. | The current addition around line 30 recognizes `constant:riches_found_event.id`; the specification says Event 029 should remain disabled by default until the complete rework is wired. |
| `common/script_constants/029_riches_found_constants.txt` | Shared Event 029 IDs, thresholds, profiles, phases, values, timings, AI weights, evolution thresholds, and achievement keys. | Defines `riches_found_event`, `riches_found_value`, `riches_found_profile`, `riches_found_operating_state`, `riches_found_phase`, policy/contract/mission tables, and 9 achievement-related keys; those keys do not match the 7 achievement IDs in the achievement prompt. |
| `common/scripted_triggers/029_riches_found_triggers.txt` | Recipient, state, mine, contract, mission, controller, closure, and evolution predicates. | `riches_found_country_is_valid_recipient` starts at line 15; `riches_found_state_is_valid_target` at line 27; `riches_found_country_can_receive_discovery` at line 64; evolution gates begin around line 239. |
| `common/scripted_effects/029_riches_found_effects.txt` | In-progress registry/discovery, values, modifiers, contracts, missions, closure, controller, evolution, and achievement helper surface. | `riches_found_initialize_registry` line 26; preparation line 42; commit line 61; mine initialization line 130; controller change line 944; evolution entry helpers lines 1094, 1115, and 1136; achievement helpers begin around line 1186. |
| `common/on_actions/029_riches_found_on_actions.txt` | Event 029-specific runtime refresh hooks. | `on_state_control_changed` lines 22-29 saves exact state/new/old controller targets; `on_annex` lines 33-45 handles removed actors; `on_peaceconference_ended` lines 48-59 handles owner refresh; `on_capitulation` lines 63-74 performs bounded registry handling. |
| `common/scripted_effects/029_riches_found_cxt_effects.txt` | Package-owned CXT test fixture registration and idempotent setup. | Defines `riches_found_register_cxt_test_content` and `chaosx_cxt_extension_event029_riches_found_apply`; it creates a capital-state fixture but does not prove production discovery behavior. |
| `common/ideas/029_riches_found_cxt_ideas.txt` | Hidden CXT carrier required by the repository test-country setup contract. | Defines `chaosx_cxt_extension_event029_riches_found`; keep this separate from production ideas. |
| `common/on_actions/029_riches_found_cxt_on_actions.txt` | Bounded startup and `on_daily_CXT` synchronization for the CXT fixture. | Registers the test content through a bounded existing-country scope and synchronizes only the test-country path. |
| `common/decisions/categories/029_riches_found_categories.txt` | Intended ordinary Event 029 decision category. | Defines `riches_found_mine_management`, static picture, and state-flag visibility, but uses `GFX_decision_category_riches_found`, `GFX_decision_cat_picture_riches_found_category_picture`, and `riches_found_mine_state`, none of which is aligned with the current asset/effect names. |
| `common/decisions/029_riches_found_decisions.txt` | Expected production decisions and missions. | Missing in the observed snapshot; the decision prompt requires bounded claims/access, rush, development, revenue, concession, security, emergency, and supernatural actions plus eight named missions. |
| `common/dynamic_modifiers/029_riches_found_state_modifiers.txt` | State mine presentation and controller aggregate modifier definitions. | Defines `riches_found_mine_state` and `riches_found_controller_aggregate` at lines 10-28; the controller modifier reads `var:riches_found_controller_consumer_goods_factor`, while the effect scaffold writes `riches_found_controller_consumer_goods_relief`. |
| `common/ideas/029_riches_found_ideas.txt` | Event-specific country ideas for evolutions/late outcomes. | Defines 5 ideas from lines 20-65, including `riches_found_resource_curse`, `riches_found_gold_disease`, `riches_found_demons_beneath_mine`, `riches_found_gilded_sovereignty`, and `riches_found_bottomless_account`; their localisation and icons are absent. |
| `common/mtth/029_riches_found_mtth.txt` | Expected Event 029 timing/MTTH table. | Missing; use the shared `common/mtth/chaosx_mtth_variables.txt` and the MTTH skill contract for paced evolution/incidents rather than scattering timing literals. |
| `common/ai_strategy/029_riches_found_ai_strategy.txt` | Expected policy, development, revenue, foreign, security, evolution, and late-outcome AI behavior. | Missing; the AI prompt defines scenario IDs `RF_POLICY_*`, `RF_DEV_*`, `RF_REV_*`, `RF_FOREIGN_*`, `RF_SEC_*`, `RF_EVO1_*`, `RF_EVO2_*`, `RF_EVO3_*`, `RF_GOLD_*`, `RF_DEMON_*`, `RF_GILDED_*`, `RF_ACCOUNT_*`, `RF_INCIDENTS_*`, and `RF_REPEAT_*`. |
| `common/scripted_effects/chaosx_events_log_effects.txt` | Shared Event Log history, actor, event-detail, and evolution plumbing. | Existing Event 029 additions around lines 348-351 and 782-785 expect `riches_found_prefire_owner/state`; the shared history/detail branches must be invoked by the final event/evolution effects, not merely defined. |
| `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` | Shared dynamic labels for Event Log, Details, evolution stages, and summaries. | Event 029 branches reference keys such as `riches_found.event_details.history`, `riches_found.event_details.description`, `riches_found.evolution.type`, and `riches_found.evolution.stage_1.title` around lines 6245-6256 and 6794-6835. |
| `common/scripted_guis/chaosx_scripted_gui_events_log.txt` and `interface/chaosx_events_log_popup.gui` | Shared Event Log UI consumer. | No Event 029-specific GUI is required; the rework must feed the existing shared log/detail framework. |
| `localisation/english/029_riches_found_l_english.yml` | Event-localised text. | Current file has only 10 `chaosx.nr29.*` and `chaosx.news.31.*` keys; it lacks the `riches_found.*` state, decision, mission, modifier, evolution, achievement, and Event Log/detail keys referenced by the new shared branches. |
| `localisation/english/chaosx_event_names_l_english.yml` | Event name mapping. | `chaosx.event_name.29: "Riches Found"` exists at line 31. |
| `gfx/event_pictures/029_riches_found/` and `gfx/interface/decisions/029_riches_found/` | Runtime image consumers. | Nine report DDS files and the decision-category DDS are present; no Event 029 `.gfx` registration was found. |
| `docs/assets/029_riches_found/gfx_handoff.md` | Asset naming and parent-owned GFX handoff. | Proposes `GFX_report_event_riches_found_discovery`, `_rush`, `_concession`, `_raid`, `_collapse`, `_gold_disease`, `_opened_depths`, `_gilded_sovereignty`, `_bottomless_account`, and `GFX_decision_cat_picture_riches_found`; current category uses a different suffix. |
| `interface/018_resources_found.gfx` | Existing GFX precedent and separation surface. | Defines Event 018 report sprites, idea icons, and decision category; use its structure as a precedent without reusing its names. |
| `common/achievements/chaos_redux_achievements.txt` | Chaos Redux achievement registry. | Root-only registry exists, but no `029_public_fortune`, `029_claim_jumper`, `029_the_pay_train_runs`, `029_all_that_glitters`, `029_no_man_owns_the_mountain`, `029_close_the_account`, or `029_the_last_shift` entry was found. |
| `gfx/achievements/` | Achievement icon triplets. | No Event 029 achievement icon triplets were found; each achievement needs normal, grey, and not-eligible images if the prompt is implemented. |
| `events/018_random_resource.txt` | Explicit Event 018 event and prefire precedent. | Uses `chaosx.nr18`, prefire owner/state targets, bounded direct selection, and distinct field/enrichment/cave routes; it owns physical strategic-resource discovery rather than Event 029 wealth governance. |
| `common/scripted_triggers/018_resources_found_triggers.txt`, `common/scripted_effects/018_resources_found_effects.txt`, `common/scripted_effects/018_resources_found_cave_effects.txt`, `common/decisions/018_resources_found_decisions.txt`, `common/decisions/categories/018_resources_found_categories.txt`, `common/dynamic_modifiers/018_resources_found_state_modifiers.txt`, `common/ideas/018_resources_found_cave_ideas.txt`, `common/ai_strategy/018_resources_found_ai_strategy.txt`, `common/mtth/018_resources_found_mtth.txt`, and `common/on_actions/018_resources_found_on_actions.txt` | Closest complete Chaos Redux package for persistent state records, selected targets, dynamic state modifiers, decisions/missions, AI, MTTH, cave/evolution handling, and exact controller refresh. | Important reusable names include `resources_found_is_valid_new_field_state`, `resources_found_initialize_field_record`, `resources_found_handle_state_control_change`, and the bounded state registry; none should be called as Event 029 mechanics. |
| `events/088_mines.txt` | Explicit Event 088 separation surface. | `chaosx.nr88.1` is a naval minelaying event using a random sea region and `meta_add_mines`; it has no persistent state mine, country recipient, controller refresh, or wealth system. |
| `docs/events/029_riches_found.md` | Required Event 029 gameplay documentation. | Missing; the events skill requires event behavior, integrations, future plans, and icon/GFX wiring documentation. |
| `docs/spreadsheets/chaos_redux_events_catalog.xlsx` | Editable event catalog source. | The current Event 029 row is `Minor Repeatable`, has a one-sentence discovery description, and status `To Be Reworked`; the supplied source-review note’s `Unavailable` status is stale or provenance-only relative to the workbook and exported CSV. |
| `docs/spreadsheets/chaos_redux_events_catalog.csv` | Export-only catalog output. | Mirrors the workbook’s Event 029 `To Be Reworked` row; do not edit directly. The implementation owner must update the XLSX first and run `.tools/export_event_catalog_csv.py`. |

## Current-vs-spec gaps

### Core event, registration, and repeatability

- The specification keeps Event 029 as a minor repeatable event with a hidden entry root and one bounded ordinary-country/state discovery per firing. The current root still performs unrestricted `random_country` selection, has no ordinary-country trigger, and has no selected state in the event scope.
- The current option grants `2000` political power, while the specification and acceptance tests require exactly `1000` political power to the discovery recipient once per firing. `RF_TEST_REPEAT_01_TWO_COUNTRIES` and `RF_TEST_REPEAT_02_SAME_COUNTRY` require two successful grants, including two different mine states for the same country.
- `riches_found_country_can_receive_discovery` currently rejects any country with `riches_found_discovery_grant_paid`. That permanent recipient flag contradicts the same-country repeat scenario and should be treated as a transaction/exploit-prevention design conflict, not accepted behavior.
- The shared dispatcher requires `riches_found_prefire_owner` and `riches_found_prefire_state`, but the current helper produces only `riches_found_prepared_mine_state`; there is no connected `riches_found_prefire_ready` assignment. The event cannot be considered registered end-to-end until this contract is unified.
- Event 029 is recognized by the shared Event Log reworked-event predicate in the current scaffold even though the complete rework is not present. The default allowlist should remain disabled until the root, effects, localisation, log, and detail contracts are complete.

### Recipient and state target gates

- The current country gate excludes special Chaos countries, actual nonhuman countries, the CXT test carrier, and capitulated countries, and requires a controlled capital. It does not visibly cover every specification exclusion such as civil-war shells, temporary/system carriers, valid-government requirements, or the required political-power/modifier suitability checks.
- The current state gate rejects impassable states, special/nonhuman owner/controller, missing control, world-end, registered mine, target-excluded, and incompatible-terminal flags. It does not explicitly reject Event 018 field/cave markers or other persistent-site reservations.
- The current `OR` accepts `is_coastal = yes` without a port check, so an empty remote island can pass. The specification requires the island/port distinction and rejects a remote island without a valid port or transport route.
- The gate does not show explicit active-disaster, unstable-transfer, reserved-site, or complete state-quality handling. Population, infrastructure, rail, supply, and geography need to be separated into hard eligibility and weighted suitability.
- `riches_found_prepare_random_event_fire` uses unweighted `random_owned_controlled_state`. The specification requires a bounded weighted state selection that favors population, buildability, connected infrastructure, industry, adjacency, and plausible borders while retaining valid low-quality cases.

### Persistent mine and controller lifecycle

- The scaffold has a bounded global mine array, monotonic sequence, public values, hidden values, state flags, profiles, and state/controller presentation helpers. It is not yet called by the event root or proven against the acceptance transfer matrix.
- The required controller refresh is broader than the current visible hook: remove the previous contribution, save the new controller, recalculate state presentation and country aggregate, replace decisions/missions, clear invalid foreign targets, and preserve mine identity, development, damage, contracts, and evolution history.
- The current `on_state_control_changed` route is the right narrow entry point, but release, annexation, capitulation, owner-change, peace-settlement, and civil-war behavior need separate exact-state tests. The capitulation helper currently iterates the entire bounded registry without an evident affected-country filter.
- The scaffold has occupation/owner/controller helpers and closure/collapse/recovery names, but there is no complete visible implementation of the decision/mission cleanup and one-time compensation rules required by the prompt.

### Decisions, missions, modifiers, ideas, and constants

- Only the category file exists; the production decision file is missing. The specification requires one ordinary static-picture category, bounded selected-mine/foreign-target interactions, eight decision families, and three or fewer active mission lines at a time.
- Mission IDs and objective behavior are absent: Secure First Rush, Open Railhead, Protect Pay Train, Break Claim War, Restore Shaft, Hold Mine During War, Complete Public Settlement, and Audit Concession must be real objectives with success, partial, failure, timeout, cleanup, and no pre-satisfied auto-completion.
- The category’s `GFX_decision_category_riches_found` icon, `_category_picture` picture name, and `riches_found_mine_state` visibility flag do not align with the asset handoff, current effect flags, or the dynamic modifier name.
- The state dynamic modifier and controller aggregate conceptually match the specification’s one state presentation plus one aggregate modifier, but the consumer-goods variable name is mismatched and the referenced icons are not registered.
- The current ideas file defines five late/evolution ideas, while the asset prompt calls for a larger set of distinct controller-idea icon consumers. IDs, icon names, localisation keys, and whether ideas or dynamic modifiers own each visible effect must be reconciled before asset wiring.
- Constants are a useful centralization scaffold, but the 9 achievement-related constant keys do not match the 7 achievement IDs in the achievement prompt. The parent needs one source-of-truth mapping before writing achievement definitions or icons.

### Evolutions, Event Log, and localisation

- The scaffold contains three evolution entry helpers with thresholds `600`, `800`, and `1000`, but no Event 029 MTTH file, no complete repeatable incident/event branches, and no proof of the required local plausibility and pacing conditions.
- `riches_found_prepare_prefire_evolution_opening` appears to set prefire evolution flags and pressure when chaos thresholds are met. Chaos alone is insufficient under the specification; active state, local pressure/exposure/depth, meaningful operation, and paced timing must be part of the entry gate.
- `riches_found_enter_evolution_i/ii/iii` set state flags and values but do not visibly call `record_events_log_evolution_entry = yes`. The shared log branch therefore has no proven producer for the three required chronology entries or the current-controller/historical-actor distinction.
- Shared Event Log and scripted-localisation branches reference many `riches_found.*` keys, while `localisation/english/029_riches_found_l_english.yml` contains only the old ten event/news keys. Missing keys cover history, details, stage titles/bodies, state values, decisions, missions, modifiers, late outcomes, and achievements.
- The three evolutions must remain distinct from Event 018’s resource/cave/Oth-Kesh/The World Opens Below content. Gold Disease must remain fictional obsession rather than biological contamination, and Demons Beneath Mine must remain fictional valuation/possession rather than a living religion or generic mining tradition.

### AI, achievements, assets, and documentation

- No Event 029 AI strategy or MTTH file was present. The five policy profiles and the 45 named AI scenario cases have no implementation or engine evidence; the separate probability auditor reported 0/45 scenarios evaluated because the required MCP tool was unavailable.
- No Event 029 achievements are registered, localised, or represented by normal/grey/not-eligible icon triplets. The current effect scaffold records internal flags, but internal flags are not achievement definitions or proof of unlock conditions.
- Report and category DDS assets exist in runtime folders and in the asset handoff, but no `interface/029_riches_found.gfx` or other runtime GFX registration was found. Decision/mission/state-modifier/idea/evolution/achievement icon wiring remains absent or unresolved.
- `docs/events/029_riches_found.md` is missing. The catalog row and export are still pre-rework and must be updated only after implementation wording and behavior are verified; the XLSX, not the CSV, is the source of truth.

## Existing patterns

- Event 018 is the closest full Chaos Redux package for a persistent state record: it prepares an owner and state target before dispatch, selects once, binds a sequence, stores state values, maintains selected targets, refreshes state modifiers, and handles controller changes through a bounded exact-state helper. Reuse its structural discipline, not its resource/cave semantics or `resources_found_*` predicates.
- `common/on_actions/018_resources_found_on_actions.txt` is the clearest local controller/owner precedent. It explicitly avoids whole-world periodic scans and routes state geography through state control/ownership/peace hooks or explicit milestones.
- `common/on_actions/015_utopia_manifesto_on_actions.txt:483-548`, `common/on_actions/006_independence_wave_on_actions_registry.txt:13-31`, `common/on_actions/humanitarian_runtime_on_actions.txt:46-57`, and `common/on_actions/fallout_consolidated_on_actions.txt:35-59` all demonstrate narrow state-control handling rather than a daily global scan.
- `common/scripted_effects/chaosx_events_log_effects.txt` provides the repository’s reusable history, actor, detail, and evolution framework. `events_log_set_default_actor_for_current_event` must run after the Event 029 prefire actor is saved, and evolution context variables must be populated immediately before `record_events_log_evolution_entry = yes`.
- `common/scripted_effects/chaosx_logic_effects.txt` and `common/scripted_effects/chaosx_settings_effects.txt` provide the shared repeatable-event pool, cap/recovery, prefire, and dispatch machinery. Event 029 should fit that contract instead of creating a second random-event pipeline.
- `common/decisions/018_resources_found_decisions.txt` and `common/decisions/categories/018_resources_found_categories.txt` show selected state-targeted decisions, `target_trigger`, AI weights, mission activation, and category organization. `common/decisions/AFG.txt:145-207` is a vanilla/local mission precedent with `days_mission_timeout` and explicit activation/timeout handling.
- `common/dynamic_modifiers/018_resources_found_state_modifiers.txt` and `common/ideas/018_resources_found_cave_ideas.txt` show the local pattern for state dynamic modifiers, idea carriers, lifecycle refresh, and icon references.
- The CXT Event 029 files follow the repository’s bounded test-extension contract: hidden carrier idea, idempotent setup effect, one bounded startup registration, and `on_daily_CXT` fallback. They are test fixtures, not production discovery logic.

## Vanilla or reference precedents

- Repeatable/event selection: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/on_actions/00_on_actions.txt:215-237` shows a random-event list in an on-action, and `:349-375` shows weighted event pulses. `events/AAT_Iceland.txt:182-207` and `events/BBA_Switzerland.txt:194-215,272-280` show country event and MTTH layout. These prove event-list structure, not the full Chaos Redux registry contract.
- State control hook: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/on_actions/00_on_actions.txt:5075-5085` documents `on_state_control_changed`: `ROOT` is the new controller, `FROM` is the old controller, and `FROM.FROM` is the changed state. This is the exact narrow hook needed by Event 029.
- State transfer/control: `events/AAT_Generic_Events.txt:133-148,220-235` and `events/BBA_Italy.txt:51-80` show bounded state transfer, `has_full_control_of_state`, and state/controller effects. `effects_documentation.md:7691-7711` documents `set_state_controller` and `set_state_controller_to`.
- Decisions and missions: `common/decisions/_generic_decisions.txt:1-35,65-104` shows an ordinary category/targeted decision layout; `common/decisions/AFG.txt:145-207` shows mission activation, `days_mission_timeout`, and timeout behavior. Official `effects_documentation.md:652-704` and `5959-6090` document mission/decision activation and removal behavior.
- Dynamic modifiers and ideas: `common/dynamic_modifiers/aat_dynamic_modifiers.txt:1-28,537-576` shows dynamic modifier definitions; `common/ideas/bulgaria.txt:10,1808-1818,3717-3726` shows idea definitions and modifiers. Official `effects_documentation.md:1153-1171,2200-2208` covers `add_dynamic_modifier` and `add_state_modifier`.
- Achievement triplets: `common/achievements.txt:8220-8234` with `gfx/achievements/a_bridge_too_far.dds`, `_grey.dds`, and `_not_eligible.dds` demonstrates the vanilla three-image pattern. The offline Achievement modding page confirms the `unique_id`, `possible`, `happened`, localisation, and triplet expectations.
- No vanilla equivalent for the Chaos Redux Event Log/evolution registry was found. The shared Chaos Redux Event Log framework is therefore the authoritative local precedent for history/detail/evolution plumbing.
- No Technology Tree Viewer is installed in the available package. Event 029 has no technology surface, so no technology evidence or invented viewer route is applicable.

## Narrow controller-change hook

There is a proven narrow hook. The exact engine contract is `on_state_control_changed`: `ROOT` is the new controller, `FROM` is the old controller, and `FROM.FROM` is the state whose controller changed. The current package uses the expected shape in `common/on_actions/029_riches_found_on_actions.txt:22-29`:

```text
on_state_control_changed = {
    FROM.FROM = { save_event_target_as = riches_found_changed_state }
    ROOT = { save_event_target_as = riches_found_new_controller }
    FROM = { save_event_target_as = riches_found_old_controller }
    if = { limit = { FROM.FROM = { riches_found_mine_is_registered = yes } } FROM.FROM = { riches_found_handle_state_control_change = yes } }
}
```

This is narrower and safer than a whole-world daily/weekly/monthly scan. It is not sufficient by itself for every ownership route: the current package also has bounded `on_annex`, `on_peaceconference_ended`, and `on_capitulation` handlers, while release, liberation, civil-war, annexation, and peace-settlement behavior still need exact acceptance tests. The capitulation handler’s registry loop should be reviewed for affected-country filtering. No MCP engine artifact exists for this hook because the required HOI4 server tools were not callable in this runtime.

## Target-selection and Event 018 separation risks

- Event 018 owns physical strategic-resource discovery, deeper deposits, caves, fossils, Oth-Kesh, and The World Opens Below. Its target API includes `resources_found_is_valid_new_field_state`, `resources_found_prefire_owner`, `resources_found_prefire_state`, field/cave markers, and resource ledgers. Event 029 must not call those predicates or inherit their state/resource records.
- Event 029 owns wealth governance around a fictional persistent mine: discovery windfall, claims, rush, development, revenue, concessions, private security, raids, corruption, and its three own evolutions. It must use only `riches_found_*` markers, its bounded registry, and its own values.
- The current Event 029 state trigger has no explicit `resources_found_*` exclusion. This is a confirmed separation gap: an Event 018 field or cave state can be eligible for Event 029 unless another unobserved marker prevents it.
- `events/088_mines.txt` is unrelated naval minelaying. It selects a sea region with `get_random_sea_region` and calls `meta_add_mines`; reusing its name, state, or mine terminology would confuse naval minefields with Event 029’s persistent land-state record.
- The shared settings dispatcher has separate Event 018 and Event 029 branches. The Event 029 branch currently checks `riches_found_prefire_owner/state`, so a final selector must save those exact targets and must not accidentally route the state into Event 018’s `.1` or `.2` events.
- State eligibility needs hard exclusions first and weighted suitability second. The final implementation must reject wasteland/impassable states, invalid owner/controller, Event 018 and existing Event 029 records, reserved persistent sites, active disasters, unstable transfer states, and unsuitable remote islands before applying state-quality weights.

## Likely edit order for the parent

1. Freeze the moving scaffold and reconcile source-of-truth conflicts before adding more files: per-firing versus permanent discovery-grant state, the category picture name, the mine visibility flag, the controller consumer-goods variable, the 7 achievement IDs versus 9 constants, and the exact report/idea icon inventory.
2. Keep Event 029 disabled in the shared default allowlist until the complete contract exists, then finalize `riches_found_*` constants and scripted triggers for ordinary recipients, hard state exclusions, bounded registry capacity, state suitability, lifecycle, controller ownership, and evolution plausibility.
3. Implement the prefire transaction contract first: select one eligible ordinary country and one weighted eligible state, save `riches_found_prefire_owner` and `riches_found_prefire_state`, set the ready value, and ensure the shared dispatcher can fire `chaosx.nr29.1` without reselecting.
4. Replace the stub event chain with discovery commit logic: initialize the state record, preserve discoverer/current controller separately, grant exactly `1000` political power once for that firing, create the persistent state identity, open the first notice/news event, and wire event localisation and Event Log history.
5. Finish state lifecycle and transfer handling through the exact control/owner hooks: contribution removal/addition, one state dynamic modifier, one controller aggregate with diminishing returns/cap, decision/mission cleanup/replacement, contract target cleanup, occupation and release handling, closure/collapse/recovery, and preservation of local history.
6. Lock the category, decisions, missions, selected-mine and selected-foreign-target mechanics, costs, cooldowns, AI scores, mission objectives, and cleanup rules. Keep the category ordinary and static-picture based; do not introduce a custom GUI.
7. Add and localise the state modifier, controller aggregate, evolution/late-outcome ideas, decisions, missions, reports, event details, and three evolution chronology entries. Register the report/category GFX before final asset consumption and reconcile all sprite names with the asset handoff.
8. Add MTTH/evolution timing and incident handlers with the required local plausibility gates, three independent toggles, bounded movement/target pools, public-death condemnation, no closure loop, and no Bottomless Account death farming.
9. Add AI strategy/MTTH and run the same named probability scenarios for baseline and comparison. The five profiles need direct bounded decisions for AI, while human foreign-target decisions may use selected target lists.
10. Add the seven achievement definitions, exact unlock conditions, localisation, and three icon triplets, then add any missing Event Log actor/detail/evolution integration required by the final in-game text.
11. Write `docs/events/029_riches_found.md`, update the editable XLSX catalog row after behavior and wording are final, run `python .tools/export_event_catalog_csv.py`, and verify the generated CSV rather than editing it directly.
12. Run source audits, acceptance scenarios, Event Log/detail checks, asset/GFX checks, and MCP/auditor routes before any completion claim. Live HOI4 testing remains the user’s responsibility; this agent did not launch the game.

## Validation checks

### Source and contract checks

- Run `rg --text -n 'chaosx\.nr29\.[123]|chaosx\.news\.31|riches_found_' events common localisation interface docs` and verify every production identifier has one owner and one consumer.
- Confirm the event root, shared settings dispatcher, Event Log default actor/history, state record, and news event agree on the same `riches_found_prefire_owner` and `riches_found_prefire_state` targets.
- Check duplicate event IDs, decision IDs, mission IDs, state flags, scripted effect/trigger names, localisation keys, dynamic modifier names, idea names, and achievement IDs.
- Verify the current shared registration uses the final constant form consistently and that Event 029 is not enabled by default before its full implementation is present.

### Target and lifecycle checks

- Execute the acceptance state matrix `RF_TEST_STATE_01_CORE_INLAND`, `RF_TEST_STATE_02_ISLAND`, `RF_TEST_STATE_03_NO_VALID_STATE`, `RF_TEST_STATE_04_EVENT_018_CONFLICT`, and `RF_TEST_STATE_05_EXISTING_MINE` against the final target helper.
- Execute `RF_TEST_TRANSFER_01_OCCUPATION`, `_02_RECAPTURE`, `_03_ANNEXATION`, `_04_RELEASE`, `_05_CIVIL_WAR`, and `_06_MULTI_MINE`; confirm only the changed state is refreshed, old contributions are removed, new contributions are added once, and mine/evolution history survives.
- Execute `RF_TEST_REPEAT_01_TWO_COUNTRIES`, `RF_TEST_REPEAT_02_SAME_COUNTRY`, and `RF_TEST_REPEAT_03_WEIGHT`; verify one `1000` political-power grant per firing, no permanent-country lock, and weighted state suitability rather than uniform state selection.
- Check Event 018 marker exclusions directly against `common/scripted_triggers/018_resources_found_triggers.txt` and its cave effects, and verify Event 088 remains a separate sea-region `meta_add_mines` route.
- Confirm no unapproved `on_daily`, `on_weekly`, or `on_monthly` whole-world scan was added; registry loops must be bounded and preferably filtered to the affected actor/state.

### Decisions, missions, AI, and evolution checks

- Verify the category is visible only for an active eligible mine, has one static picture, and exposes no more than the specified bounded action set. Check the active mission count and no duplicate activation.
- Validate all eight named missions for real objective progress, success/partial/failure/timeout behavior, cleanup on controller change, and prevention of automatic completion from pre-satisfied state.
- Validate `RF_TEST_EVO1_01_DELAYED_MANAGED`, `_02_CAPTURED`, `_03_DISABLED`, `RF_TEST_GILDED_01`, `_02_RECOVERY`; `RF_TEST_EVO2_01_ENTRY` through `_05_DISABLED`; and `RF_TEST_EVO3_01_ENTRY` through `_04_DISABLED`.
- For AI, begin with `hoi4.probability_inspect`, then route the full scenario set through `chaosx_ai_probability_auditor` using the named policy, development, revenue, foreign, security, evolution, late-outcome, incident, and repeat scenarios. Run the same scenarios through `hoi4.probability_evaluate`, `hoi4.probability_sweep`, `hoi4.probability_simulate`, `hoi4.probability_sequence`, `hoi4.probability_render`, and `hoi4.probability_compare` where supported, preserving artifact URIs and unsupported cases.
- Check that Evolution I/II/III are independently toggleable, have exactly one chronology entry each, use current controller actor plus historical actor where required, and do not borrow Event 018 cave/resource outcomes.

### Localisation, Event Log, assets, catalog, and MCP checks

- For every `localization_key` in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`, verify an actual UTF-8-with-BOM key exists in the Event 029 localisation files and describes the current world state rather than implementation history.
- Verify Event Log history, Event Details, actor mapping, event type, state values, three evolution stage labels/bodies, and news/report picture selection through the shared framework.
- Check that every referenced report/category/decision/mission/state/idea/evolution/achievement `GFX_*` token has a `.gfx` definition, correct runtime path, expected dimensions, and the required normal/grey/not-eligible triplet where applicable.
- Update only `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, then run `python .tools/export_event_catalog_csv.py` from the mod root and verify the generated Event 029 row, detail wording, evolution wording, and status. Do not edit the export CSV directly.
- Required HOI4 MCP routes after the server is callable are narrow `hoi4.event_inspect` queries for `chaosx.nr29.1/.2`, read-only `hoi4.event_render` and compare, and the probability routes listed above. A dedicated GUI route is not required because the specification calls for a static decision category; map inspection is not required because the feature adds no map resources or topology.
- Current exact MCP blocker: `.codex/config.toml`, `.qoder/mcp.json`, and `.cursor/mcp.json` register `hoi4_agent_tools`, and `C:/Users/klimp/AppData/Roaming/npm/hoi4-agent-tools.cmd` exists, but this runtime exposed no callable `hoi4.event_inspect`, `hoi4.event_render`, `hoi4.event_compare`, `hoi4.probability_inspect`, `hoi4.probability_evaluate`, `hoi4.probability_sweep`, `hoi4.probability_simulate`, `hoi4.probability_sequence`, `hoi4.probability_render`, `hoi4.probability_compare`, `hoi4.gui_*`, or map routes. The attempted mandatory `mcp__hoi4_agent_tools__hoi4_probability_inspect` returned `MCP tool hoi4_agent_tools/hoi4.probability_inspect is not available to the model`; therefore there are no MCP artifact URIs and no engine-evaluated AI scenarios to report.

## Risks and blockers

### Confirmed blockers

- The Event 029 event root is still the old stub with wrong grant amount, no state selection, and no mine commit.
- The current prefire helper and shared dispatcher use different target names and readiness variables, so the repeatable selection path is not connected.
- The current recipient gate permanently blocks a country after one discovery, contradicting the required same-country repeat scenario.
- Event 018 marker exclusions, full remote-island/port filtering, weighted state selection, and several ordinary-country/state hard gates are not present in the observed target helper.
- Production decisions, missions, AI/MTTH, achievements, Event 029 localisation, `.gfx`, and `docs/events/029_riches_found.md` are missing in the observed snapshot.
- Category picture/visibility names and the controller consumer-goods variable are inconsistent with their current consumers.
- The current constants’ achievement mapping conflicts with the achievement prompt’s seven-ID requirement.
- Required HOI4 MCP inspection/rendering/probability routes are unavailable in this agent runtime; source, wiki, and documentation evidence cannot substitute for the required engine evidence.
- Parent-side files were changing during exploration, so the report cannot certify the observed scaffold as a stable implementation.

### Ordinary implementation risks

- `on_state_control_changed` covers controller change, not every owner/release/peace/civil-war route; each additional route needs bounded exact-state cleanup and acceptance evidence.
- Regular event target lifetime and event-target comparisons must follow the documented scope rules; global targets should not be introduced for short-lived discovery context without cleanup.
- State and country modifier field support, dynamic variable syntax, and aggregate diminishing returns need parser/engine validation, especially the current `industrial_capacity_factory` and consumer-goods fields.
- The shared Event Log has no vanilla analogue, so actor ordering and evolution context must be validated through Chaos Redux’s own renderer/consumer rather than inferred from vanilla event syntax.
- Asset files are present but names and consumers are not locked; changing sprite tokens after localisation/decision/idea wiring will create avoidable missing-GFX failures.
- The catalog status discrepancy between the source-review manifest and the current XLSX/CSV needs a documentation decision, not a guessed overwrite.

## Recommended next action

Freeze the current scaffold and resolve its naming and transaction conflicts first, especially the prefire owner/state contract, per-firing `1000`-PP grant, Event 018 exclusions, weighted target selection, category/GFX names, and seven-achievement source of truth. Then implement and validate the bounded discovery/commit and exact-state controller-refresh path while Event 029 remains disabled by default; do not claim completion until the missing decisions, missions, evolutions, AI, localisation, assets/GFX, achievements, docs/catalog, and unavailable MCP/auditor evidence are addressed.
