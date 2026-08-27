# Repression Ledger decision and GUI audit handoff

Date: 2026-08-27

Scope: Current concurrent state of the Repression Ledger and camp/repression decision system in `common/decisions/categories/genocide_crisis_categories.txt`, `common/on_actions/genocide_crisis_on_actions.txt`, `common/script_constants/camp_repression_rework_constants.txt`, `common/scripted_triggers/camp_repression_rework_triggers.txt`, `common/scripted_effects/genocide_crisis_effects.txt`, `common/scripted_guis/camp_repression_ledger_scripted_gui.txt`, `common/scripted_localisation/camp_repression_ledger_scripted_localisation.txt`, `interface/camp_repression_ledger.gui`, `localisation/english/camp_repression_rework_l_english.yml`, `localisation/english/camp_repression_country_kits_l_english.yml`, and the existing generic/major decision and rework-effect dependencies.

## Executive result

The current five-tab source is structurally aligned with the parent contract: Overview, State Pools, Active Sites, Country System, and Evidence & Reform are separate tabs with real buttons, matching visibility flags, and separate state-pool and active-site panels. The current source does not expose pipe-delimited telemetry, fake bar layouts, developer/meta/debug wording, or Japan text in the Soviet country summary. Startup initialization also contains explicit GER, JAP, and SOV historical baselines, and the monthly pulse and later Soviet escalation routes remain wired in source.

The principal unresolved defect is cost clarity and cost-count compliance. Several gameplay-changing decisions and the GUI expansion route consume six distinct spendable types, exceeding the four-type ceiling, while the generic decision and ledger GUI surfaces conceal most of those spends instead of presenting icon-first numeric costs. This should be treated as the highest-priority corrective pass before completion.

No gameplay or GUI source file was changed by this audit. The only file added by this subagent is this handoff; all other current edits belong to the parent or concurrent users and were preserved.

## Findings sorted by severity

### P1: Several actions exceed the four-spendable-cost limit

The following existing actions combine political power, manpower, command power, infantry equipment, support equipment, and trains, for six distinct spendable types:

- `common/decisions/camp_repression_major_country_decisions.txt`: `germany_build_ss_laboratory_annex_at_auschwitz`, `japan_establish_pingfang_research_bureau`, `sov_transfer_prisoners_to_industrial_camps`, and `sov_authorize_extreme_periphery_repression`.
- `common/decisions/camp_repression_generic_decisions.txt`: `generic_expand_labor_quotas` and `generic_upgrade_existing_site_to_radicalized_atrocity_site`.
- `common/scripted_guis/camp_repression_ledger_scripted_gui.txt`: the expansion branch of `camp_gui_expand_selected_pool_click_enabled` requires the same six spendable types.

The issue is not merely prose length: shared effects visibly consume these resources, so the player-facing action contract is over budget and cannot be inferred safely from a short political-power line. The parent should reduce each affected route to at most four spendable types while preserving the accepted mechanic, then expose the complete remaining cost set.

### P1: Gameplay-changing GUI actions hide real costs

The country-action tooltip keys used by the ledger show political power and `display_camp_country_action_n_cost`, but the routed actions also consume manpower, equipment, command power, motorized equipment, support equipment, or trains depending on the action. The bottom action tooltips in `camp_repression_ledger_scripted_gui.txt` likewise use prose such as “required transport and equipment” without numeric icon-first costs. `camp_gui_expand_selected_pool_tt` names several resource categories but provides no complete cost line, and the guard, evidence, and labor-project tooltips omit their numeric non-political costs.

The generic decision file similarly has no `custom_cost_trigger` or `custom_cost_text` for most resource-consuming generic actions, even though availability and shared effects enforce those costs. This leaves the ordinary decision cost row unable to communicate the actual spend. Use existing texticons such as `£pol_power`, `£GFX_train_texticon`, `£infantry_equipment_text_icon`, `£GFX_support_equipment_text_icon`, and `£GFX_motorized_equipment_text_icon` only after confirming the exact registered icon names in the interface, and keep every remaining spendable value visible in the primary action surface.

### P2: GUI engine evidence has a category-inspection blocker and global diagnostics

`hoi4.gui_inspect` succeeded for `repression_ledger_window` under scenario `repression_ledger_five_tab_current`, but the category inspection for `repression_ledger_category_window` returned the exact engine error `INTERNAL_ERROR` with no artifact. The successful main inspection reported global graph truncation (`1999` retained and `1654` dropped), unresolved references, index collisions, and mixed-fidelity diagnostics. These are workspace-level diagnostics and are not evidence of a source-local overlap in the current ledger, but they prevent a clean engine validation claim.

`hoi4.gui_render` succeeded for both the main and category windows at 1920x1080 and 1280x720, with the requested normal, hover, selected, locked, disabled, warning, active, completed, empty-list, full-list, minimum-value, maximum-value, long-text, and missing-localisation states where applicable. The render responses were wire-truncated after returning valid artifact references, so rendered pixels were not independently read back in this audit.

### P2: GUI execution pays political power and records cooldown before final route validation

`camp_rework_gui_execute_prepared_country_action` in `common/scripted_effects/camp_repression_rework_effects.txt` pays the political-power cost and prepares the selected state before dispatching the route. `camp_rework_route_country_specific_action` records the GUI slot cooldown before the downstream action-specific effect. If a stale selection, changed resource pool, or route condition invalidates the action after preparation, political power or cooldown can be lost without a completed gameplay action. Review the ordering so final route eligibility and all costs are validated before irreversible payment and cooldown state, or provide an explicit rollback path.

### P2: Hidden mission overlap and Soviet famine-cycle semantics need owner review

Germany has six hidden, non-selectable mission blocks and Japan has five; Soviet routes have six hidden cycle/crisis missions. Their individual contracts include owner, category context, duration, availability, completion, timeout, cancellation, and cleanup, but several can overlap when crisis conditions coexist. Because the missions are not selectable and the ledger does not show a mission wall, this is not a current visible-action-count failure, but simultaneous hidden mission state can increase cognitive and balance risk and should be checked against the intended event cadence.

`sov_famine_pressure_cycle` is named as a pressure cycle but its available condition is `famine_pressure = 0 OR grain_extraction_burden = 0`; its completion and timeout branches are also opposite to the emergency relief mission. This may be intentional as a reset/closure cycle, but the condition and name should be confirmed by the Soviet-system owner before completion.

### P2: One chemical-action tooltip is too dense and one legacy value dump appears stale

`camp_gui_chemical_method_tt` contains a long technical explanation of Gas-Chamber Saturation Drills, killing efficiency, payload use, evidence, and status. It is not developer or debug language, but it is denser than the concise action guidance required for this surface and risks exposing implementation-heavy detail without a clear player response. `repression_ledger_discovery_values` remains an eight-line raw value dump in localisation, while the current interface uses the four discovery cards instead. Remove or repurpose the stale key only after confirming no other consumer uses it.

## Category lifecycle and startup notes

`camp_repression_network_category` is currently `visible_when_empty = yes` and requires `camp_rework_country_is_eligible = yes` plus `has_camp_category_visible_action = yes`. The visible-action trigger accepts an active camp network, visible reform work, the historical visibility flag, managed or inherited network flags, the generic detention unlock, or an active genocide crisis. This supports game-start display for an eligible country with an operating camp without requiring a player action first.

`gulag_and_mass_repression_system` is also `visible_when_empty = yes` and has Soviet, active-network, active-site-count, famine-pressure, and system-flag visibility paths.

`on_startup` in `common/on_actions/genocide_crisis_on_actions.txt` initializes the system once, explicitly calls the historical GER, JAP, and SOV initializers when those countries exist, and then runs the versioned migration through a bounded `random_country` scope. The source comments and effect structure indicate that the migration reconstructs active arrays from state flags/buildings rather than replacing the historical registrations.

The German initializer records `genocide_german_1936_baseline`, sets low starting radicalization and archive-control values, activates the historical detention site in state 53, and marks dormant states 64 and 60. The Japanese initializer records `genocide_japanese_1936_baseline`, sets low starting Kwantung/Ishii/occupation-record values, activates state 716, and marks state 611 dormant. The Soviet initializer records `genocide_soviet_1936_baseline`, initializes NKVD authority, forced-labor quota, grain-extraction burden, famine pressure, republic fear, and movement grievance, activates gulag states 644, 874, and 881, and marks state 881 for famine aftermath. Source evidence supports the requested 1936 baselines, but live new-game startup and save-load behavior were not run by this audit.

The host Chaos Meter pulse calls `genocide_initialize_system_if_needed` and `genocide_monthly_global_pulse`; the monthly effect cleans active sites, applies monthly state and country pressure effects, and performs cleanup. Later Soviet deportation, confiscation, purge, forced-labor, gulag registration, death-record, and collapse-memory effects remain present in `common/scripted_effects/genocide_crisis_effects.txt`; no escalation branch was removed during this audit.

## Cognitive-load audit

The main ledger presents five purpose-specific tabs rather than a combined locations warehouse. Overview and Evidence & Reform use card-based summaries, while State Pools and Active Sites cap visible rows at six each. Country System exposes a bounded set of route actions. This is materially clearer than a raw telemetry wall and keeps the primary action count within the requested category limit per surface.

Displayed values generally have a clear label and consequence: reach, output/burden, human cost, evidence risk, reform pressure, country authority, paranoia, famine pressure, and site/pool state. The six-row cap is implemented by per-row visibility checks in the scripted GUI and interface. The remaining concern is that several action costs are not displayed beside the action, so the player can understand the state but cannot reliably understand the complete response price before clicking.

The category itself is a compact entry point and does not expose the raw arrays. The separate panels and five real tab buttons avoid fake textual layout and avoid more than six visible primary row actions at once. Hidden missions are not selectable, but their overlapping automatic state should be reviewed separately from visible cognitive load.

## Mission quality notes

Germany’s hidden mission set is owned by GER and uses the repression category context: occupied-Poland expansion, eastern-fortifications labor, SS laboratory annex, Auschwitz military review, Auschwitz evidence destruction, and Auschwitz dismantlement. Durations are 180, 180, 180, 120, 45, and 270 days respectively. Each has availability and state/control requirements, success or failure effects, cancellation conditions, and cleanup helpers; duplicate risk is overlap between crisis/reform/review missions when several Auschwitz flags coexist.

Japan’s hidden mission set is owned by JAP and covers the Pingfang research bureau, army medical review, epidemic containment, Pingfang evacuation, and prisoner-experiment shutdown. Durations are 180, 120, 150, 45, and 270 days. The missions gate on state 328/site responsibility, Ishii influence, outbreak risk, retreat/control state, or closability and provide success, failure, timeout, cancellation, and cleanup paths. Duplicate risk is simultaneous review, containment, evacuation, and shutdown flags during a retreat or outbreak transition.

Soviet hidden missions are owned by SOV and cover the gulag quota cycle, famine-pressure cycle, emergency famine relief, camp-administrator review, overextended-gulag dismantlement, and retreat-records crisis. Durations are 180, 180, 180, 150, 270, and 45 days. They use reform-route, quota, authority/paranoia, famine, active-gulag, state-control, and retreat-target requirements with success/failure/cancel helpers. The famine-pressure-cycle availability condition described above is the main semantic review point; overlapping quota, relief, review, and dismantlement flags are the main duplicate-risk point.

Generic missions include the labor-project cycle, network-overstretch crisis, retreat-evidence crisis, and reform/dismantlement flow. They are not selectable and use activation flags, requirement checks, route locks, and cancellation cleanup. Their AI blocks are zero-weight bridge state rather than a separate mission-choice pool.

## Cost and requirement clarity audit

The major-country decisions have explicit `allowed`, `visible`, `available`, `complete_effect`, and `ai_will_do` blocks, with target-state and responsibility checks for GER, JAP, and SOV routes. Their custom cost blocks cover several costs, but the six-type combinations listed under P1 exceed the four-type rule.

The generic decisions use route, pool, cap, and state checks, but most resource-consuming decisions do not declare custom cost text. The generic activation route is four spendables (political power, manpower, command power, and support equipment), and guard actions are four spendables (political power, manpower, command power, and infantry equipment). The generic expansion and radicalization routes are six spendables and need reduction.

The ledger activation branch is four spendables, while its expansion branch is six. Labor projects are generally four spendables when capacity gates are treated as non-consumed requirements, but their GUI tooltip still needs a complete numeric icon-first line. State responsibility, site-control, route, cooldown, and cap checks are requirements rather than spendable costs and should remain visually separated from consumed resources.

## AI validity and route-lock notes

Major decisions contain AI weights and caps for site, experiment, extreme-route, and country project selection. The source includes reform-route suppression, war/surrender/condemnation factors, active-site and responsibility checks, and country identity guards. GER state 88, JAP state 328, Soviet remote gulag pools, and generic `camp_rework_state_can_accept_responsibility_from_root` route locks are present. No invalid dead-country target or impossible-border target was identified in the inspected contracts.

The required custom `chaosx_ai_probability_auditor` route was not callable in this environment, so no normalized runtime balance claim is made. Direct `hoi4.probability_inspect` score-source inspection found 17 major decision candidates and 8 generic decision candidates with unresolved source inputs reported as zero, but it did not evaluate runtime scenarios or normalized probabilities. The mission adapter discovered no mission candidates in the source and suggested the decision adapter, so mission AI behavior remains source-only evidence.

## Localisation and tooltip notes

The current tab labels are exactly `Overview`, `State Pools`, `Active Sites`, `Country System`, and `Evidence & Reform`. Category and main summaries contain no bar-delimited prose. All observed `|0`, `|1`, and `|%0` occurrences are valid HOI4 formatter syntax inside dynamic values, not pipe-separated telemetry.

The Soviet country summary branches on `original_tag = SOV` before generic branches and mentions only gulag reach, NKVD authority, paranoia, and famine pressure. The Japan branch is separate and contains Pingfang, Ishii, Kwantung, and China evidence wording; no Japan wording was found in the Soviet summary. Germany-specific Mengele/Auschwitz wording is gated behind a GER-specific relevance trigger.

The semicolon in `camp_selected_state_detail` is ordinary prose punctuation rather than a telemetry delimiter, but that line is dense. The chemical-method tooltip and stale discovery-value key are the main text-density cleanup candidates. Costs need icon-first numeric localisation in the primary decision and GUI surfaces.

## Cleanup and exploit-risk notes

The inspected decision and mission routes generally provide cancellation and completion cleanup for flags, active-site registration, project targets, and cooldown markers. Historical initializers and migration are guarded by initialization/version flags, and the monthly pulse cleans inactive sites before applying recurring effects.

The GUI payment/cooldown ordering described under P2 is the main transactional risk. Review it for stale selections, resource changes between preparation and dispatch, repeated clicks, and cooldown consumption after failed downstream validation. The existing cap triggers and cooldown flags reduce spam risk, but no runtime click/reload test was performed.

## Recommended corrective fixes

1. In `common/decisions/camp_repression_major_country_decisions.txt`, reduce the six-spendable cost packages for `germany_build_ss_laboratory_annex_at_auschwitz`, `japan_establish_pingfang_research_bureau`, `sov_transfer_prisoners_to_industrial_camps`, and `sov_authorize_extreme_periphery_repression` to no more than four types and keep their custom cost localisation synchronized.
2. In `common/decisions/camp_repression_generic_decisions.txt`, reduce `generic_expand_labor_quotas` and `generic_upgrade_existing_site_to_radicalized_atrocity_site` to no more than four spendable types, and add complete custom cost text for resource-consuming generic decisions that currently hide equipment, trains, manpower, or command costs.
3. In `common/scripted_guis/camp_repression_ledger_scripted_gui.txt` and the corresponding localisation files, expose the complete numeric icon-first cost for each gameplay-changing bottom action and make the expansion route’s displayed cost match its reduced <=4-type contract.
4. In `common/scripted_effects/camp_repression_rework_effects.txt`, review `camp_rework_gui_execute_prepared_country_action` and `camp_rework_route_country_specific_action` so final route validation precedes payment and cooldown, or add a safe rollback for failed dispatch.
5. Confirm the intended semantics and owner-facing name of `sov_famine_pressure_cycle` in `common/decisions/camp_repression_major_country_decisions.txt` and keep its completion, timeout, cancellation, and relief interaction explicit.
6. Shorten `camp_gui_chemical_method_tt` to the player decision, threshold, consequence, and response, and remove or repurpose `repression_ledger_discovery_values` only after checking its consumers.
7. Re-run the GUI inspect/render comparison after the parent’s final merge and investigate the category `INTERNAL_ERROR`; treat the global graph diagnostics as an environment/workspace blocker until a source-local diagnostic is available.
8. Route all final weighted balance comparison through `chaosx_ai_probability_auditor` when that custom subagent/tool is available; direct score inspection is not a substitute.

## Evidence and validation

Main GUI inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a4aea950c875ffe646f6ecf80fd43f47b816c97f0f9d88b663ed7292d9a17ca5/419a5f98e0bf835ad9d14504eaba284e07f8cbc8c4ece571618742dd14db0c53/gui-inspect.f323d376d55c4e21.json`.

Main GUI render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b0179a2e4c0df19f733c338fc2bdf7d696c1236dd7cad8fa8ea08fc1d146f48b/c72eb7b994372a5107551192d7564eb62f4e40e25f416d989f4771eb7668c6bd/repression_ledger_window-full.svg`.

Category GUI render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/329de700000bcf60f3ae6a5c6944feb02199e57371a007e6a3fa302231160374/4c69af5a36a7c76bd0c7148c33e6408914f4338bc3825dab42ef6ded13c048a6/repression_ledger_category_window-full.svg`.

Category GUI inspect blocker: `INTERNAL_ERROR`, no artifact returned.

Major decision probability artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5dca976f1cb6f98c4037af7e7233506e0495924c12642ad1a563b4a831b70e32/f7594cb522487dd8e32da9bfb9a9579b48e779670bd11319823f028ebcbf32af/probability-inspect-86161d8558e4.json`.

Mission-adapter discovery artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/42c3347a68ecd382fa2aa32b16fda3ecb5f81a5652e075a97dde54020d7c5be0/d24590bca35745a0c6a070e0d3f4958a06e74c7859cba98d1ce85dc38589dc59/probability-inspect-86161d8558e4.json`.

Generic decision probability artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cf78a55d7ec9fe6946a42057096994792fba13ae85e0525346e878a379d65d33/f4c0180f65cca1b245b55d291fd4420676cbb0244f59f9a812c6e3a80f3461a0/probability-inspect-15747dd2bf63.json`.

Meaningful source validation included inspection of category visibility, startup initializers, monthly pulse wiring, later Soviet escalation, GUI tab/panel/state-row mappings, scripted-localisation country branches, decision costs/effects/cooldowns, mission contracts, route guards, and a literal-pipe search distinguishing formatter syntax from prose. The required GUI inspect/render surfaces were used read-only; no `hoi4.gui_rewrite` was needed because no GUI patch was made.

Skipped validation: live game startup, save/load, click-through, monthly death outcomes, and runtime AI/balance scenarios were not run because agents must not launch HOI4 and the custom probability auditor was unavailable. The category inspect error and global GUI diagnostics remain open blockers for a clean engine-level completion claim.

## Changed files and remaining risks

Changed files: `docs/plans/repression_ledger_plans/subagent_handoffs/2026-08-27_repression_ledger_decision_audit.md` only. No decision, mission, scripted GUI, interface, effect, trigger, on-action, constant, or localisation identifier was changed by this subagent.

Remaining risks are the six-type cost packages, hidden GUI and generic-decision costs, payment/cooldown ordering, mission overlap, the Soviet famine-cycle semantic question, category inspect failure, global GUI graph diagnostics, and the absence of live/runtime probability evidence. No simplification or fallback was introduced by this audit.

## Post-patch re-audit — 2026-08-27

This dated section records the read-only post-patch review requested by the parent. The earlier pre-patch cost findings above are superseded where the current source now has the matching custom cost trigger, localisation, and resource helper.

### Severity-sorted findings

1. **P1 residual — `generic_restricted_contaminated_site_escalation` still hides a consumed payload cost.** The decision charges political power and can consume a researched chemical payload through `cbrn_try_debit_action_payload` or a biological stockpile through `camp_rework_consume_biological_stockpile`, but it has no `custom_cost_trigger` or `custom_cost_text`. `camp_gui_cost_restricted_method` only says that a researched payload is required and does not show its icon or numeric quantity. This is the remaining direct violation of the requirement that every resource-consuming generic decision expose its full non-PP cost.

2. **P1/P2 scope risk — the colonial expansion helper remains five spendable types when political power is counted.** `camp_rework_consume_colonial_expansion_resources` consumes manpower, infantry equipment, support equipment, and command power; `uk_expand_raj_detention_districts` is the confirmed decision consumer. That is four non-PP resources plus political power, unlike the repaired core expansion/transfer package. `camp_rework_consume_colonial_project_resources` likewise defines four non-PP resources, although no current Country System slot audited here uses it. This needs an owner decision on whether the four-type cap applies to the broader colonial decision family; under the repository-wide cost rule it remains an exception.

3. **P2 residual transaction risk — no ordinary stale-slot failure remains, but a theoretical no-op path remains.** Each `camp_rework_gui_execute_country_action_[1-4]` rebuilds the action slots and availability in the same effect, then refuses to prepare or pay unless the fresh `_available` flag is present. `camp_rework_route_country_specific_action` records cooldown only after its dispatch branches. This closes the normal stale selection and preflight-failure payment path. However, `camp_rework_gui_execute_prepared_country_action` still pays before dispatch, and the route tail records cooldown unconditionally. A nested state or route guard can therefore no-op after preflight if state/control changes inside the same transaction; the relevant defensive examples are the UK colonial guard, USA supervised release, and Italian security-battalion effects. No runtime proof of reachability was available, so this is a source-level residual rather than a confirmed ordinary click failure.

4. **P2 semantic risk — `sov_famine_pressure_cycle` reads as a closure/reset sentinel, not an active pressure-building cycle.** The mission is owned by SOV, sits in the repression decision category, is hidden and non-selectable with `allowed = { always = no }`, has a 180-day duration, and its availability is keyed to `famine_pressure = 0` or `grain_extraction_burden = 0`. The inspected contract has explicit completion, timeout failure, and cancellation handling. Its region is the country-wide Soviet ledger state rather than a province-specific target. Those zero-state requirements classify it as an automatic reset/closure sentinel. If the intended meaning is a mission that runs while famine pressure is active, the trigger is semantically inverted; owner confirmation is still required before changing it. Its overlap with the quota cycle, emergency relief, administrator review, and gulag dismantlement missions remains the main duplicate risk.

5. **P3 cleanup candidate — `repression_ledger_discovery_values` remains a possible stale raw-value localisation key.** The current interface uses the four card summaries instead of this raw dump, so no visible fake layout was found. Its consumers should be checked before removal or repurposing.

### Decision category lifecycle and cognitive-load review

The category remains available at game start for countries with operating camps through the existing startup initialization and category visibility path, while the monthly maintenance and later escalation hooks remain wired. The current ledger uses five purpose-specific tabs: Overview, State Pools, Active Sites, Country System, and Evidence & Reform. State Pools and Active Sites cap visible rows at six, and Country System exposes a bounded four-slot action surface. No category or tab is being used as a warehouse for an unbounded action wall.

Displayed values have identifiable significance and response paths: reach, output or burden, human cost, evidence risk, reform pressure, country authority, paranoia, famine pressure, and site or pool state. Hidden automatic missions are not selectable primary actions. The remaining cognitive-load gaps are cost visibility for the restricted payload method and the semantic ambiguity of the Soviet famine-cycle label, not raw telemetry presentation.

### Post-patch cost and requirement audit

The repaired core expansion and transfer packages are now within the four-spendable limit. `germany_build_ss_laboratory_annex_at_auschwitz`, `japan_establish_pingfang_research_bureau`, `sov_transfer_prisoners_to_industrial_camps`, `sov_authorize_extreme_periphery_repression`, `generic_expand_labor_quotas`, and `generic_upgrade_existing_site_to_radicalized_atrocity_site` each present political power plus manpower, support equipment, and trains through a custom trigger and icon-first custom cost text. Their effects dispatch to `camp_rework_consume_expansion_resources`, so the displayed four types match the real deduction.

The other resource-consuming generic decisions audited also expose their complete non-PP package: activation uses manpower, command power, and support equipment; labor construction and extraction use motorized, trains, and support equipment; guards use manpower, command power, and infantry equipment; evidence uses manpower, command power, and support equipment; and dismantlement or dormant-site closure use manpower and support equipment. `generic_restricted_contaminated_site_escalation` is the explicit exception because its chemical or biological payload is consumed dynamically without a custom cost trigger or text.

Every current Country System slot rebuilt by `camp_rework_rebuild_country_gui_actions` for GER, JAP, SOV, ENG, USA, FRA, VIC, ITA, and BEL was matched against its dispatch effect. The package families are consistent: labor project equals motorized, trains, and support equipment; guard equals manpower, command power, and infantry equipment; evidence equals manpower, support equipment, and command power; dismantlement equals manpower and support equipment; support-only equals support equipment; colonial guard equals manpower, infantry equipment, and support equipment; support plus convoys equals support equipment and convoys; transport guard equals motorized, command power, and fuel; and `none` has no non-PP debit. The tooltip family `camp_gui_country_action_[1-4]_tt` displays political power followed by `GetCampCountryActionNCostDetails`, whose branches use icon-first numeric localisation for those exact packages.

The observed spendable text-icon coverage is `£pol_power`, `£manpower_texticon`, `£command_power`, `£infantry_equipment_text_icon`, `£support_equipment_text_icon`, `£GFX_motorized_equipment_text_icon`, `£GFX_train_texticon`, `£convoy_texticon`, and `£GFX_fuel_texticon`. No Country System action audited exceeds four total spendable types or presents a literal resource name in place of its icon.

### AI validity, route locks, and mission quality

The major and generic decision contracts retain country identity, state control, responsibility, route, cooldown, cap, and active-site checks. No dead-country target or impossible-border target was found in the audited dispatch paths. The required custom `chaosx_ai_probability_auditor` route was not callable, so this append makes no normalized runtime balance claim; the earlier direct probability artifacts remain source-level evidence only.

The hidden mission owners, categories, and lifecycle contracts remain intact. GER missions remain owned by GER and target the occupied-Poland or Auschwitz route; JAP missions remain owned by JAP and target Pingfang, epidemic, or retreat state; SOV missions remain owned by SOV and target gulag, famine, authority, and retreat state; and generic missions remain automatic bridge-state missions. The famine-cycle contract is the only post-patch mission whose requirement semantics need owner confirmation as described above. Existing timeout, success, failure, cancellation, and cleanup helpers were present in the inspected blocks, with overlapping automatic flags still the duplicate-risk area.

### Localisation, GUI, and exploit review

The current interface source contains separate State Pools and Active Sites panels and five real tab buttons or icons. The read-only source review found no pipe or bar-delimited telemetry prose, no fake textual layout, and no visible developer, debug, meta, or update-history wording. The only observed `|0`, `|1`, and `|%0` forms are valid HOI4 value formatters. The Soviet summary has an explicit SOV branch before generic country branches and contains gulag, NKVD authority, paranoia, and famine wording; Japan-specific Pingfang, Ishii, Kwantung, and China wording remains in the Japan branch and does not leak into Soviet UI.

The rebuild-before-availability preflight, cooldown tail placement, decision cooldown flags, active-site caps, and cleanup helpers reduce repeated-click, free-resource, and cooldown-spam risk. The remaining exploit concern is the theoretical payment-before-dispatch no-op path, not a confirmed free loop. No live game, save/load, click-through, monthly death, or runtime AI scenario was run by this audit.

### Evidence, changed file, and remaining work

The only changed file in this post-patch audit is `docs/plans/repression_ledger_plans/subagent_handoffs/2026-08-27_repression_ledger_decision_audit.md`. No gameplay, decision, mission, scripted GUI, interface, effect, trigger, constant, or localisation file was edited, and no identifiers were changed.

The existing read-only GUI artifacts remain the evidence for the five-tab surface: main inspect `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a4aea950c875ffe646f6ecf80fd43f47b816c97f0f9d88b663ed7292d9a17ca5/419a5f98e0bf835ad9d14504eaba284e07f8cbc8c4ece571618742dd14db0c53/gui-inspect.f323d376d55c4e21.json`, main render `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b0179a2e4c0df19f733c338fc2bdf7d696c1236dd7cad8fa8ea08fc1d146f48b/c72eb7b994372a5107551192d7564eb62f4e40e25f416d989f4771eb7668c6bd/repression_ledger_window-full.svg`, and category render `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/329de700000bcf60f3ae6a5c6944feb02199e57371a007e6a3fa302231160374/4c69af5a36a7c76bd0c7148c33e6408914f4338bc3825dab42ef6ded13c048a6/repression_ledger_category_window-full.svg`. The category inspect surface returned the exact blocker `INTERNAL_ERROR` with no artifact. No fresh MCP call was made for this append after the parent’s stop-work instruction; a final-merge inspect/render comparison remains advisable if that surface becomes callable.

Recommended follow-up is to add dynamic icon-and-quantity custom cost coverage for the chemical or biological payload, decide whether colonial expansion packages are included in the four-spendable rule and reduce or reclassify them if so, and make dispatch success explicit before payment and cooldown or provide a safe rollback. Confirm the intended active-versus-closure semantics of `sov_famine_pressure_cycle` before changing its trigger. No simplification or fallback was introduced by this audit.

## Final owner-fix clearance — 2026-08-27

The parent applied and reviewed the remaining fixes identified by the post-patch audit.

- Every audited spendable package is now within the four-type maximum, including the United Kingdom/Raj expansion order.
- `generic_restricted_contaminated_site_escalation` exposes an exact icon-first chemical or biological payload cost, and the mastery quantities agree across availability, display, and consumption.
- `uk_expand_raj_detention_districts` and `camp_rework_consume_colonial_expansion_resources` use political power, manpower, infantry equipment, and support equipment only.
- The guarded Soviet prisoner-transfer checks match the shared expansion helper: political power, manpower, support equipment, and trains.
- German prisoner-labor construction is war-gated in both the ordinary decision and Country System availability path.
- `sov_famine_pressure_cycle` is activated by the monthly Soviet bridge while both famine pressure and grain-extraction burden are positive. Its `available` block is the hidden mission's success condition: removing either pressure completes relief before timeout. It is not an inverted activation sentinel.

Country System clicks rebuild the current four action slots and their complete availability gates synchronously before an action id or political cost is prepared. Clausewitz effect execution is synchronous, so state control, selection, and non-political resources cannot change between that fresh preflight and the immediately following dispatcher unless the same effect chain changes them; none of the audited pre-dispatch helpers does so. The route records cooldown after dispatch. No ordinary reachable stale-slot, payment-without-action, or cooldown-without-action defect remains in the current chain.

The dispatcher does not carry a separate success receipt or rollback path. That remains a defensive architectural consideration if a future pre-dispatch helper is allowed to mutate route state inside the same effect chain, not a current reachable gameplay defect.

The earlier residual recommendations in this handoff are superseded by this clearance. No remaining decision, cost, mission-semantics, or Country System transaction defect was identified in the final source.

## Final owner-fix clearance — 2026-08-27

This final post-fix pass re-read the current decision, dispatcher, effect, scripted-localisation, constant, and Country System blocks. Only this handoff was changed; no gameplay, GUI, or localisation source was edited and no commit was made.

### Clearance matrix

- **Four-spendable limit: PARTIAL.** The repaired live packages pass: `germany_build_ss_laboratory_annex_at_auschwitz`, `japan_establish_pingfang_research_bureau`, `sov_transfer_prisoners_to_industrial_camps`, `sov_authorize_extreme_periphery_repression`, `generic_expand_labor_quotas`, `generic_upgrade_existing_site_to_radicalized_atrocity_site`, and `uk_expand_raj_detention_districts` are political power plus, respectively, the matching three-resource expansion package (`common/scripted_effects/camp_repression_rework_effects.txt:5025`, `common/scripted_effects/camp_repression_colonial_country_effects.txt:799`). The dormant `camp_rework_consume_colonial_project_resources` helper has no current consumer. Two still-reachable legacy transfer decisions in `common/decisions/genocide_crisis_decisions.txt` remain five-type actions: `germany_transfer_prisoners_to_experiment_site` and `japan_transfer_prisoners_to_experimental_facilities` each charge political power, army experience, manpower, support equipment, and trains. This is the remaining concrete four-type violation.
- **Restricted payload exactness: NOT FULLY CLEARED.** `generic_restricted_contaminated_site_escalation` now exposes `custom_cost_trigger` and `custom_cost_text = camp_cost_restricted_method_non_pp` (`common/decisions/camp_repression_generic_decisions.txt:684-698`), and the current nerve-mastery constants `18`, `15.75`, and `12.60` (`common/script_constants/camp_repression_rework_constants.txt:976-987`) match the real `0.45` debit factor in `camp_rework_prepare_chemical_method_outcome` (`common/scripted_effects/camp_repression_rework_effects.txt:4699-4769`). The remaining display defect is selector scope: `GetCampRestrictedPayloadCost` chooses the chemical string from the country-level chemical-capacity trigger before the biological branch (`common/scripted_localisation/camp_repression_ledger_scripted_localisation.txt:502-505`), while the dispatcher chooses chemical versus biological from both country capacity and the selected state target (`common/scripted_effects/camp_repression_action_dispatcher_effects.txt:191-206`). A country with chemical capacity selecting a biological-only target can therefore see a chemical payload cost while dispatching the biological payload. The displayed quantity is exact once the method family is selected, but the family selection is not target-exact.
- **Colonial expansion package: CLEARED.** `uk_expand_raj_detention_districts` checks and displays political power plus manpower, infantry equipment, and support equipment (`common/decisions/camp_repression_colonial_country_decisions.txt:240-248`); `camp_rework_consume_colonial_expansion_resources` deducts exactly those three non-PP resources (`common/scripted_effects/camp_repression_colonial_country_effects.txt:799-809`). No command power deduction remains in this route.
- **Soviet prisoner transfer: CLEARED for the ordinary decision path.** The decision’s cost trigger, target trigger, and availability all require manpower, support equipment, and trains plus a state satisfying both `camp_rework_state_can_accept_responsibility_from_root` and `is_soviet_remote_gulag_pool_state` (`common/decisions/camp_repression_major_country_decisions.txt:1068-1118`). The dispatcher repeats the same state guard (`common/scripted_effects/camp_repression_action_dispatcher_effects.txt:307-318`), and the expansion helper deducts the displayed manpower/support/train package. The action-state effect performs the debit before its own nested state guard (`common/scripted_effects/camp_repression_major_country_effects.txt:2293-2301`), but that is only a theoretical direct-call hazard after the matching decision/dispatcher preflight, not an ordinary reachable decision failure.
- **Germany war-construction gate: CLEARED for decision and Country System.** Both `germany_route_prisoner_labor_to_war_construction` visibility/availability contain `has_war = yes` (`common/decisions/camp_repression_major_country_decisions.txt:40-68`), and the GER Country System slot-1 rebuild gate repeats it (`common/scripted_effects/camp_repression_rework_effects.txt:2966-2995`). The direct route effect has no independent war guard, so bypassing both front doors remains a theoretical caller-contract risk only.
- **Soviet famine mission semantics: CLEARED.** `sov_famine_pressure_cycle` is an automatic, hidden, non-selectable SOV mission with a 180-day timeout. The monthly bridge activates it while both `famine_pressure` and `grain_extraction_burden` are positive; its success condition is removing either pressure before timeout (`available` is an `OR` of either variable equalling zero), with explicit success, timeout failure, and cancellation effects (`common/decisions/camp_repression_major_country_decisions.txt:1475-1495`). Current localisation states that same relief-success meaning (`localisation/english/camp_repression_country_kits_l_english.yml:288-292`). It is not a pressure-building mission; it is the relief-success cycle described by the source comments.

### Country System transaction result

Under synchronous same-frame execution, no ordinary reachable stale-slot or no-op payment/cooldown defect was found. Each `camp_rework_gui_execute_country_action_[1-4]` first rebuilds and clears the action display/availability flags, then pays only when the fresh slot flag is set (`common/scripted_effects/camp_repression_rework_effects.txt:2535-2552`, `3697-3741`). The route records the slot cooldown after dispatch (`:3747-3827`). A merely theoretical defensive risk remains because political power is paid before dispatch and cooldown recording is unconditional if a caller bypasses the fresh preflight or a nested route guard fails; no ordinary Country System path was shown to reach that state.

### Presentation and evidence

The current five-tab interface still has separate State Pools and Active Sites panels and real tab controls. Source review found no bar-delimited telemetry, fake text layout, developer/debug/meta prose, or Japan wording in the Soviet country branch. Fresh read-only GUI evidence for `repression_ledger_window` under `repression_ledger_final_five_tab_audit` is inspect artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f08c8f536454b8ebb6442faffefa39a0cbbb4945b6b38770fb5b67087ac2bee4/05c830edf4c31bd227dfc5c493b55fe68b40268278685664541fc0c73d26b69b/gui-inspect.efc34f872ea1a4da.json` and full render artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/125c3b778d52bee555772509f03a11c3fe23da527cd883fde7a3ee338475afbc/f7bfcf5432cabf3c3e9d3dcea0df6ed61407e31c807321d4da72dca9a7c9ddd5/repression_ledger_window-full.svg`. The inspect returned `GUI_INSPECTED` with 94 elements; the render returned `GUI_RENDERED` with a wire-truncation warning but a valid artifact. The category-window inspect and render each hit the exact MCP timeout `timed out awaiting tools/call after 180s`, so category engine evidence remains blocked.

### Remaining concrete follow-up

Reduce or reclassify the two legacy five-type transfer decisions, and make `GetCampRestrictedPayloadCost` resolve from the selected target’s actual chemical/biological route before presenting its icon-and-quantity string. No other owner-fix clearance item above remains open on the ordinary decision or Country System path. Runtime game startup, click-through, save/load, and probability comparison remain skipped because agents must not launch HOI4 and the custom probability-auditor route was unavailable.
