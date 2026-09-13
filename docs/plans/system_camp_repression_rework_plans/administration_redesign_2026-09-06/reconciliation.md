# National administration redesign reconciliation

Snapshot: 2026-09-06.

Disposition: accepted and queued.

This is a documentation-only reconciliation of the accepted administration redesign against the current source tree.

It does not claim gameplay completion, engine validation, or GUI completion.

The exact identifier inventory is in [source_inventory.json](source_inventory.json).

## Scope and acceptance basis

The accepted source is [accepted_implementation.md](accepted_implementation.md), whose acceptance basis is the user's explicit request on 2026-09-06 for the complete Camps, Forced Labor and Repression plan.

The accepted contract requires automatic administration driven by priority, mandate and budget; quiet maintenance and eligible development; separate economic and institutional slots; finite surviving cohorts; exact-once loss records; bounded 50–100 percent limited-use research awards with a two-award annual cap; centralized payments and quotes; administration, locations and records views; and reform that releases survivors without restoring deaths or deleting civilian infrastructure.

Every accepted redesign item remains `accepted and queued` here until current source and required scenario, specialist and MCP evidence prove that item.

## Source-of-truth map

| Layer | Path | Current evidence | Disposition |
| --- | --- | --- | --- |
| Accepted design | `docs\plans\system_camp_repression_rework_plans\administration_redesign_2026-09-06\accepted_implementation.md` | Explicit user acceptance and integration boundary. | Accepted and queued. |
| Current system description | `docs\systems\cbrn_warfare\genocide\genocide_crisis_system.md` | Describes the legacy 84-action, 41-mission, 32-slot and five-tab package. | Historical/current runtime evidence; stale for the accepted redesign. |
| Foundation contract | `common\scripted_effects\camp_administration_effects.md` | Documents finite cohorts, payment ceilings, separate slots, release, reform, and award contracts. | Current source contract; implementation evidence only. |
| Foundation runtime | `common\scripted_effects\camp_administration_effects.txt` | Defines finite-cohort records, maintenance, economy accumulation, releases, reform, monthly processing, and award caps. | Partial implementation evidence; queued for scenario proof. |
| Integration runtime | `common\scripted_effects\camp_administration_integration_effects.txt` and `common\scripted_effects\camp_administration_occupation_effects.txt` | Hooks bounded country initialization, monthly processing, occupation records, routine cancellation and terminal cleanup. | Current integration evidence; parent review and engine evidence pending. |
| Country runtime | `common\scripted_effects\camp_administration_country_effects.txt` and `common\scripted_effects\camp_administration_country_decisions.txt` | Defines GER/JAP/SOV programs, oversight, archive/release decisions, single-use awards and finite Soviet release. | Accepted and queued; integration, localization and scenario evidence pending. |
| Civil runtime | `common\scripted_effects\camp_administration_civil_effects.txt`, `common\scripted_effects\camp_administration_civil_decisions.txt` and `common\scripted_triggers\camp_administration_civil_triggers.txt` | Defines ENG/Raj/USA/FRA/VIC/ITA/BEL/COG custody, review, claims, strike and reform paths. | Accepted and queued; parent review and scenario evidence pending. |
| GUI contract | `common\scripted_effects\camp_administration_ui_effects.txt` and `common\scripted_triggers\camp_administration_ui_triggers.txt` | Defines priority, budget, mandate, selected role, work toggle and survivor release helpers. | Accepted and queued; no current consumer GUI was found in scope. |
| Legacy package | `common\decisions\camp_repression_generic_decisions.txt`, `camp_repression_major_country_decisions.txt`, `camp_repression_colonial_country_decisions.txt`, `common\scripted_effects\camp_repression_rework_effects.txt` and country effect files | Current 84 operational decisions, four Ledger controls, 41 missions, country bridges and lifecycle effects. | Compatibility evidence; route-by-route reconciliation required. |
| Legacy duplicate package | `common\decisions\genocide_crisis_decisions.txt` and `common\scripted_effects\genocide_crisis_effects.txt` | Current 33 nested decisions and older cost, visibility and lifecycle routes. | Merge, replace or retire under parent decision; do not treat as a second administration bus. |
| Selected-site cost package | `common\scripted_effects\camp_repression_site_cost_effects.txt`, `common\scripted_triggers\camp_repression_site_cost_triggers.txt` and `common\script_constants\camp_repression_site_cost_constants.txt` | Separate location quote and payment family. | Candidate adapter into centralized administration payment contract. |
| Shared accounting | Existing Chaos Meter, exact state population-loss and Deaths APIs. | Called by the foundation and legacy routes. | Read-only boundary; parent must prove one physical debit per accepted loss. |

## Current route map

The package currently contains 84 operational legacy player actions, four Ledger visibility/open/close controls, 41 missions and 11 new administration decisions.

The 84 operational actions are 12 generic, 29 GER/JAP/SOV and 43 UK/USA/FRA/VIC/ITA/BEL actions.

The exact IDs and source line starts are recorded in `source_inventory.json`; the current package is evidence of what exists, not evidence that the accepted redesign is implemented.

| Route family | Current source | Accepted-plan behavior | Status |
| --- | --- | --- | --- |
| New GER/JAP/SOV administration decisions | `common\decisions\camp_administration_country_decisions.txt` | Retain as country authority, oversight and aftermath controls; route commitments through the national slots and bounded awards. | Accepted and queued. |
| New civil administration decisions | `common\decisions\camp_administration_civil_decisions.txt` | Retain as hidden AI policy/review controls; keep routine administration automatic and quiet. | Accepted and queued. |
| Generic activation, inspection, evidence, dismantlement and dormant-site closure | `common\decisions\camp_repression_generic_decisions.txt` | Retain as explicit lifecycle/location/records actions through the administration adapters. | Accepted and queued. |
| Generic expansion, labor routing, guard allocation, quota reduction, radicalization and routine labor/reform project | `common\decisions\camp_repression_generic_decisions.txt` | Merge into automatic administration, economic slot, mandate and continuing-support rules; retire manual duplicates after migration. | Accepted and queued. |
| GER/JAP/SOV country actions | `common\decisions\camp_repression_major_country_decisions.txt` | Retain meaningful institutions, oversight, records, reform and closure; merge routine output, admissions, guards and logistics; replace research wording with bounded awards. | Accepted and queued. |
| UK/USA/FRA/VIC/ITA/BEL country actions | `common\decisions\camp_repression_colonial_country_decisions.txt` | Retain distinct civil institutions, review, release, records, reform, strike and aftermath; merge routine labor, guard, transport and construction into automatic slots. | Accepted and queued. |
| Legacy `genocide_crisis_*` operational decisions | `common\decisions\genocide_crisis_decisions.txt` | Merge compatible authority/output routes, replace experimental/research and finite-release routes, retain meaningful evidence/crisis/foreign-response routes, and retire duplicate visibility controls. | Accepted and queued; exact per-ID choices are in `source_inventory.json`. |
| CBRN occupation decisions | `common\decisions\cbrn_occupation_decisions.txt` | Retain under its existing owner and use an explicit adapter if it shares a location; prevent duplicate cost, population-loss or lifecycle application. | Outside redesign owner; parent decision required for any adapter. |

## Mission disposition

Routine project missions must not remain compulsory monthly clicks or ordinary completion popups.

`generic_labor_project_cycle`, national labor/road/resource cycles, and similar maintenance or eligible-development missions are replaced by quiet automatic economy-slot progress.

Meaningful crisis, oversight, evidence, reform, closure and aftermath missions remain explicit only when their completion changes a player-visible historical or institutional state.

`camp_admin_integration_cancel_routine_projects` currently removes `generic_labor_project_cycle` and `generic_reform_and_dismantlement`; `camp_administration_civil_cancel_routine_projects` removes the identified UK/USA/FRA/ITA/BEL project missions.

The remaining 41-mission set requires a parent-owned final cleanup pass so routine country missions do not survive beside the automatic slots.

The complete 41-ID table with retained/replaced/retired dispositions is in `source_inventory.json`.

## Country bridge map

| Bridge | Evidence | Accepted-plan role | Status |
| --- | --- | --- | --- |
| `camp_rework_germany_monthly_bridge` | `common\scripted_effects\camp_repression_major_country_effects.txt:564` | Preserve Germany threshold, authority and evidence adapter; move routine output and institution progress to administration slots. | Accepted and queued. |
| `camp_rework_japan_monthly_bridge` | `common\scripted_effects\camp_repression_major_country_effects.txt:582` | Preserve Ishii, outbreak and evidence thresholds as meaningful outcomes; move routine projects and research to bounded programs. | Accepted and queued. |
| `camp_rework_soviet_monthly_bridge` | `common\scripted_effects\camp_repression_major_country_effects.txt:665` | Preserve famine, authority and collapse records; replace manpower release and routine quotas with finite release and automatic administration. | Accepted and queued. |
| `japan_ishii.1`, `.2`, `.3`, `.5` | `common\scripted_effects\camp_repression_major_country_effects.txt:621,637,648,660` | Retain threshold events when evidence, outbreak, review or exposure changes; suppress ordinary monthly completion noise. | Accepted and queued. |
| `soviet_gulag.3`, `.5` | `common\scripted_effects\camp_repression_major_country_effects.txt:697,711` | Retain meaningful famine/reform threshold events; do not fire for quiet maintenance. | Accepted and queued. |
| `camp_rework_refresh_colonial_focus_hooks` | `common\scripted_effects\camp_repression_colonial_country_effects.txt:23` | Preserve live focus adapters for distinct civil country institutions. | Accepted and queued. |
| `camp_rework_update_colonial_country_monthly_bridge` | `common\scripted_effects\camp_repression_colonial_country_effects.txt:301` | Preserve refugee/strike/reform pressure as meaningful country outcomes; merge routine administration into civil slots. | Accepted and queued. |
| `camp_rework_update_country_specific_monthly_bridges` | `common\scripted_effects\camp_repression_rework_effects.txt:4642` | Keep one bounded bridge caller after administration monthly processing. | Accepted and queued. |

The bridge list is an adapter map, not permission to add another whole-world recurring hook.

## Bonus, idea and modifier map

`camp_admin_country_award_program` now requests a bounded bonus and calls `camp_admin_try_claim_research_award`; the source uses `add_tech_bonus` with `uses = 1` and program values in the accepted range.

This is current source evidence only because annual two-award, no-stacking, authority, target-loss and scenario checks remain pending.

Japanese institutional ideas and their current localization still describe research or economic benefits in places, while the accepted contract requires bounded limited-use awards; their final carrier split remains queued for the country owner.

The current German Mengele/Auschwitz idea source still carries special-project and biowarfare-facility speed modifiers, while the accepted contract moves institutional benefits to bounded awards; the country owner must reconcile the source modifiers and stale descriptions together.

Automatic output and burden carriers in generic, major-country and colonial idea files should merge into `camp_admin_country_economy`, `camp_admin_state_economy` or the authoritative country/civil pressure variables.

Evidence, refugee, resistance, famine, reform, accountability, authority and postwar legacy carriers remain distinct when they represent a meaningful state rather than a second output meter.

The exact current idea and dynamic-modifier IDs, grouped dispositions and localization follow-ups are in `source_inventory.json`.

## GUI and action surface

The current GUI is `common\scripted_guis\camp_repression_ledger_scripted_gui.txt` plus `interface\camp_repression_ledger.gui`.

It exposes five tabs, six selected-location action buttons, four country action slots, persistent cost text and the old `camp_rework_gui_execute_country_action_1..4` bus.

The accepted interface has three views: administration, locations and records.

| Current surface | Current IDs | Accepted-plan mapping | Status |
| --- | --- | --- | --- |
| Open/close and tab navigation | `repression_ledger_category_open_button_click`, `camp_gui_close_window_click`, `camp_gui_tab_overview_click`, `camp_gui_tab_state_pools_click`, `camp_gui_tab_sites_click`, `camp_gui_tab_country_click`, `camp_gui_tab_discovery_click` | Merge navigation into administration, locations and records views. | Replaced; queued. |
| Pool/site selection | `camp_ui_pool_select_click`, `camp_ui_site_select_click` | Retain selection model under locations and records. | Retained; queued. |
| Expand, labor, guard and quota buttons | `camp_gui_expand_selected_pool_click`, `camp_gui_start_labor_project_click`, `camp_gui_allocate_guards_click`, `camp_gui_reduce_quotas_click` | Replace with priority, budget, mandate, selected-role and quiet automatic progress helpers. | Replaced/merged; queued. |
| Inspect, dismantle and evidence buttons | `camp_gui_inspect_selected_site_click`, `camp_gui_dismantle_selected_site_click`, `camp_gui_destroy_evidence_click` | Retain as explicit location/records actions with centralized quotes and lifecycle cleanup. | Retained; queued. |
| Chemical and biological method buttons | `camp_gui_chemical_method_click`, `camp_gui_biological_method_click` | Retain only through the separate CBRN/camp method contract, with no second death or cost route. | Retained as adapter; parent decision required. |
| Four country slots | `camp_gui_country_specific_primary_click`, `camp_gui_country_action_2_click`, `_3_click`, `_4_click` | Replace the four-slot legacy panel with the administration controls and the country module's valid actions. | Replaced; queued. |
| New UI helper contract | `camp_admin_set_priority`, `camp_admin_set_budget`, `camp_admin_set_mandate`, `camp_admin_set_selected_role`, `camp_admin_toggle_selected_work`, `camp_admin_release_selected` | Canonical administration actions. | Accepted and queued; no current scripted GUI consumer found. |

The new country trigger files expose only action-one/action-two predicates while the legacy GUI still checks four action slots, so parent wiring must resolve the mismatch before showing a disabled or stale action.

The accepted “no permanent button-price grids” rule also requires removal or replacement of current cost text and `camp_rework_gui_cost_package` display behavior.

Required MCP GUI inspect/render/compare evidence was not available in this environment.

Historical request JSON under `docs\plans\system_camp_repression_rework_plans\administration_redesign_2026-09-06\mcp\` is provenance, not service-health evidence.

## Reconciliation findings

### Duplicate costs and payments

Three cost families currently coexist: countrywide `camp_rework_cost` and equipment/reserve constants, selected-site `camp_site_cost` quotes, and legacy `genocide_decision_cost` routes.

New administration payment helpers use centralized support and political-power ceilings, while selected-site and legacy routes still have separate quote/payment entrypoints.

Parent must choose one adapter boundary and prove that a route cannot pay both its legacy and administration quote.

### Duplicate lifecycle and output

`camp_admin_integration_monthly_country` now calls foundation administration, occupation records, country/civil modules and legacy country pressure in one guarded callback.

The legacy `camp_rework_apply_country_monthly_pressure` and country idea refreshes can still mutate overlapping output, burden or lifecycle carriers, so automatic output must be removed from legacy carriers before the redesign is accepted.

The foundation contract requires replacing the old state-percent death pulse with finite monthly cohorts; source evidence must still prove no legacy immediate-burst or occupation route debits the same loss twice.

The integration handoff reports a bounded source integration and one legacy monthly driver, but its own limitations leave final scenario, MCP and cross-module acceptance pending.

### Noisy completion events

The 41 missions expose success/failure/timeout completion effects in the generic, major and colonial decision files.

Routine maintenance, eligible development, and authorized institutional progress must complete quietly through automatic processing.

Keep only meaningful threshold, evidence, crisis, reform, closure, oversight and aftermath notifications.

### Hidden gates and future mistakes

Legacy visibility flags `genocide_decisions_visible`, `genocide_gulag_decisions_visible` and broad `has_camp_category_visible_action` can expose routes without the new regime, authority, continuing-support, slot, budget and target gates.

The old Germany and Japan experiment-transfer routes must obey the new historical and institutional gates, including the Mengele Auschwitz hidden-before-1943-05-30 rule, controlled state and operational site.

The new `camp_admin_country_mengele_historical_gate` is present at `common\scripted_triggers\camp_administration_country_triggers.txt:68`, but the older `germany_transfer_prisoners_to_experiment_site` route still uses its own legacy variables and costs.

The GUI four-slot availability flags and the new country action-one/action-two trigger surface are inconsistent until parent integration resolves them.

Routine automatic maintenance and eligible development must remain hidden from player action lists and must not become a new monthly click obligation.

The accepted design prohibits protected-group selectors, casualty-score rewards and technical experimental/weapon procedures; any legacy route that exposes these concepts must be replaced or retired rather than merely relabeled.

### Finite losses and release

The current foundation records finite detainee cohorts, per-cause monthly/cumulative values, location and responsible-country projections through `camp_admin_record_deaths`.

The public contract says only that helper invokes the shared physical death API, but final acceptance still needs exact-once scenario evidence across legacy camp, occupation and CBRN entrypoints.

`camp_admin_country_release_registered_prisoners` and `camp_admin_release_survivors` release in place and do not create manpower; the Soviet decision and its old tooltip still describe an army manpower gain and require localization reconciliation.

### Scoped documentation location

The current system document is `docs\systems\cbrn_warfare\genocide\genocide_crisis_system.md`.

The older `docs\specs\system_camp_repression_rework_specs\package_index.md:13` link to `../../systems/genocide_crisis_system.md` is stale and should point to `../../systems/cbrn_warfare/genocide/genocide_crisis_system.md`.

This task does not patch that index because ownership is restricted to `reconciliation.md` and `source_inventory.json`.

## Plan and handoff disposition

| Document or handoff | Disposition | Acceptance basis or implementation evidence | Remaining reason or blocker |
| --- | --- | --- | --- |
| `accepted_implementation.md` | Accepted and queued | Explicit user request on 2026-09-06. | Required scenarios, specialist reviews, MCP comparisons and final parent integration remain. |
| `integration_handoff.md` | Accepted and queued for parent review | Parent delegation recorded in the handoff; source trace reports bounded initialization, monthly callback, lifecycle cleanup and retired candidate gates. | Handoff explicitly says cross-module acceptance, MCP and probability comparison remain pending. |
| `common\scripted_effects\camp_administration_effects.md` | Accepted foundation contract, queued for implementation proof | Public helper and award contract matches accepted plan. | Source contract does not prove engine behavior or exact-once route coverage. |
| `gui_native_mapping.md` | Accepted and queued | Parent plan and reference mapping. | Current source consumer and required MCP visual evidence remain pending. |
| `ai_audit.md` | Blocked for final completion | Named scenarios and baseline evidence exist. | The required probability MCP route timed out; no engine artifact was produced. |
| `docs\systems\cbrn_warfare\genocide\genocide_crisis_system.md` | Historical/current evidence, superseded for redesign claims | It records the legacy package and source references. | Counts, tabs, slots and “final re-audit” language do not prove accepted redesign completion. |
| `docs\specs\system_camp_repression_rework_specs\package_index.md` | Stale reference | Current path is known. | Link correction requires an owner outside this bounded file scope. |
| Older completion reports, tracker, audits and country maps under `docs\plans\system_camp_repression_rework_plans\` | Historical evidence | They explain previous package decisions and source paths. | Their “complete” or 84-action status must not be reused as current redesign status. |

## Contradictions and duplicate documents

The accepted plan says three views and quiet automatic processing, while the current system doc and GUI describe five tabs, four country action slots and routine manual project controls.

The accepted plan says limited-use research awards, while current Japan ideas and several localization keys describe permanent research or economic benefits.

The accepted plan says finite release in place, while the current Soviet decision tooltip and legacy effect path describe manpower transfer.

The accepted plan centralizes payments, while current legacy, selected-site and new administration cost families coexist.

The accepted plan requires hidden historical/institutional gates, while broad legacy visibility flags still expose older routes.

The current administration helper contract names a canonical UI surface, but no `interface\camp_administration*.gui` or `common\scripted_guis\camp_administration*.txt` consumer was found in this source snapshot.

The current documentation is not deleted or rewritten here because the parent granted only the two reconciliation files.

## Stale prompts and instructions

No scoped prompt file was supplied or patched in this task.

The stale package index path and historical “84 actions/final re-audit” claims are the actionable stale documentation surfaces.

Any prompt that instructs a worker to implement the old four-slot Ledger, permanent Japanese research ideas, Soviet manpower release, or a second monthly world hook should be superseded by the accepted plan before reuse.

## Markdown hard-wrap audit

No hard-wrap defects were introduced in this file.

The named existing docs were not rewritten because they are outside the two-file ownership boundary.

Their hard-wrap status therefore remains unmodified and is an open parent cleanup item if a later docs pass grants ownership.

## Parent decisions and proposed cleanup

1. Confirm whether selected-site `camp_site_cost` becomes an adapter over administration quotes or remains a separately owned location contract with an explicit no-double-payment guarantee.
2. Confirm the final retirement list for all routine missions and ordinary completion effects after country modules prove their quiet monthly paths.
3. Replace the legacy four-slot GUI with the three accepted views and bind the new UI helper contract before exposing any country action.
4. Remove permanent Japan research-speed carriers and stale German research/construction/efficiency wording; use temporary, single-use bounded awards.
5. Rewrite the Soviet release route and localization to release finite survivors in place without creating army manpower or restoring deaths.
6. Add the missing current system-doc path to the package index or assign that correction to the documentation owner with broader scope.
7. Require a successful probability MCP comparison and GUI inspect/render/compare route before any completion claim.
8. Prove exact-once population loss, attribution and conservation across administration, occupation, legacy camp and CBRN adapters.

Proposed cleanup is limited to the two files created here; gameplay, localization, GUI, spreadsheet, configuration and source-doc edits remain with their owners.

## Validation and limitations

Source checks run for this reconciliation included targeted `rg` inventories of decision IDs, mission IDs, bridge/helper names, GUI click/effect names, idea IDs, dynamic modifiers and stale documentation links.

`source_inventory.json` was generated from the current source snapshot and will be checked with `ConvertFrom-Json` after writing.

The repository contains unrelated concurrent edits, so validation is path-scoped and does not use a whole-tree clean-worktree claim.

The HOI4 MCP tools were unavailable in this session, so no current event, weighted-logic or GUI inspect/render/compare artifact was produced.

The existing integration handoff records a timed-out `hoi4.event_inspect` call and a request to stop further worker MCP submissions; that is recorded as a blocker, not as engine evidence.

No live game was launched.

## Files changed and remaining risks

Files changed by this task: `docs\plans\system_camp_repression_rework_plans\administration_redesign_2026-09-06\reconciliation.md` and `docs\plans\system_camp_repression_rework_plans\administration_redesign_2026-09-06\source_inventory.json`.

No runtime, localization, GUI, spreadsheet, configuration, asset or source-of-truth files were changed.

The redesign remains incomplete until the parent reconciles duplicate routes, finishes the GUI and localization decisions, proves scenario behavior, resolves the probability and GUI MCP blockers, and performs final specialist review.
