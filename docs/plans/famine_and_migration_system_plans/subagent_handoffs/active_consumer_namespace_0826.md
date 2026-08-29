# Active Consumer Namespace Audit, 26 August 2026

## Scope and verdict

This was a read-only audit of the current famine and migration player-facing and visual-consumer namespace. I inspected the separate decision categories, decisions and missions, localisation, scripted localisation, report-header GUI consumers, GFX sprite registrations, achievements, scripted mapmodes, mapmode localisation, texticons, and the current asset manifests. No gameplay, localisation, interface, asset, documentation source, or spreadsheet was edited. This handoff is the only new file.

The active mechanic identity is separated correctly after parent closure of ACN-01. `famine_decision_category` and `migration_decision_category`, their decisions and missions, the two report-header windows, the eight achievements, the two mapmodes, and the shared humanitarian cost display use their owning `famine_*`, `migration_*`, or narrowly allowed `humanitarian_*` namespaces.

No active `famine_migration_*`, `migration_famine_*`, or `fm_*` identifier was found in the inspected runtime text sources, interface/GFX sources, localisation, or current asset manifests. No player-facing title calls the feature a united famine-and-migration mechanic, category, or mapmode.

## Closed defect

### ACN-01: shared cost presentation used an unapproved neutral namespace

Status: closed by the parent and accepted by bounded re-audit on 26 August 2026.

Before closure, the shared selectors and localisation keys used `GetCivilianResponse*` and `civilian_response_cost_*`, which fell outside the authorized neutral prefixes.

Accepted closure:

- `common/scripted_localisation/humanitarian_cost_scripted_localisation.txt:12-98` defines 15 unique selectors named `GetHumanitarianCostPp10Cost` through `GetHumanitarianCostTransportPlanes5Cost`.
- `localisation/english/humanitarian_cost_l_english.yml:2-31` defines 30 unique ready/blocked keys named `humanitarian_cost_*`.
- `localisation/english/famine_l_english.yml:50-59` contains 10 famine-owned cost strings with 32 calls to the new selectors.
- `localisation/english/migration_l_english.yml:69-84` contains 16 migration-owned cost strings with 49 calls to the new selectors.
- All 81 calls resolve to one of the 15 selectors. All 30 scripted-localisation branches resolve to one of the 30 keys. There are no undefined calls, unused selectors, missing branch keys, or unused humanitarian cost keys in this bounded package.
- `common/scripted_localisation/civilian_response_scripted_localisation.txt` and `localisation/english/civilian_response_l_english.yml` are absent.
- A current active-source census returned zero `GetCivilianResponse*` or `civilian_response_cost_*` hits. Historical audit prose elsewhere under `docs/plans/` still quotes the superseded selector names, but those documents are not active consumers and were outside the authorized handoff-only edit.
- `humanitarian_cost_l_english.yml`, `famine_l_english.yml`, and `migration_l_english.yml` begin with UTF-8 BOM bytes `239,187,191`.

Display behavior is unchanged: the ready/blocked amounts, icons, colors, and selector conditions are identical. Only the active namespace and file ownership changed. ACN-01 is closed.

The unrelated temporary variable `cbrn_action_civilian_response_exposure_mult` in `common/scripted_effects/cbrn_exposure_effects.txt:515-524` describes a CBRN action's civilian response and is not a famine/migration consumer or shared mechanic label. It remains outside this bounded closure.

## Accepted separated consumers

### Decisions, missions, and categories

- `common/decisions/categories/famine_decision_category.txt:3-14` owns `famine_decision_category`, `famine_report_header_scripted_gui`, `GFX_famine_category`, and `GFX_famine_category_picture`.
- `common/decisions/categories/migration_decision_category.txt:3-20` owns `migration_decision_category`, `migration_report_header_scripted_gui`, `GFX_migration_category`, and `GFX_migration_category_picture`.
- `common/decisions/famine_decisions.txt:35-1420` contains 2 famine missions and 10 famine decisions. All top-level consumer ids use `famine_*`.
- `common/decisions/migration_decisions.txt:35-2571` contains 4 migration missions and 18 migration decision IDs: 16 primary actions plus the 2 auxiliary corridor-response decisions `migration_accept_corridor_offer` and `migration_reject_corridor_offer`. All top-level consumer ids use `migration_*`; corridor infrastructure remains narrowly `humanitarian_*` where it crosses owners.
- Every inspected decision and mission id has its title and description key. All six missions also have success, failure, and tooltip localisation.

### Player-facing category and report identity

- `localisation/english/famine_l_english.yml:2-7` presents the separate category label `Famine` and famine-only phase text.
- `localisation/english/migration_l_english.yml:2-7` presents the separate category label `Migration` and migration-only phase text.
- `interface/famine_report_header.gui:6-22`, `common/scripted_guis/famine_report_header_scripted_gui.txt:4-23`, and `interface/famine_report_pictures.gfx:2-4` are famine-owned.
- `interface/migration_report_header.gui:6-25`, `common/scripted_guis/migration_report_header_scripted_gui.txt:4-26`, and `interface/migration_report_pictures.gfx:2-5` are migration-owned.
- All report-header text and sprite keys resolve to an existing localisation or GFX definition. No combined live report-header window remains in source.

### Achievements

- `common/achievements/chaos_redux_achievements.txt:3850-3888` defines 3 `famine_*` achievements and 5 `migration_*` achievements. Their predicates use narrowly shared `humanitarian_achievement_*` contracts.
- `interface/famine_system.gfx:12-20` and `interface/migration_system.gfx:16-30` register distinct completed, grey, and not-eligible sprite triplets for all eight achievements.
- `localisation/english/famine_l_english.yml:88-96` and `localisation/english/migration_l_english.yml:124-138` provide all `_NAME`, `_DESC`, and `_tooltip` keys.

### Mapmodes

- `common/map_modes/chaosx_state_map_modes.txt:390-569` defines only `famine_state_map_mode` for food-security state.
- `common/map_modes/chaosx_state_map_modes.txt:571-910` defines only `migration_state_map_mode` for displacement, route, reception, resettlement, and return state.
- `localisation/english/chaosx_map_modes_l_english.yml:130-147` provides the separate famine mapmode name, description, tooltip, and detail keys.
- `localisation/english/chaosx_map_modes_l_english.yml:149-233` provides the separate migration mapmode name, description, tooltip, and detail keys.
- `interface/mapmodes_interface.gfx:55-69` registers separate selected and deselected sprites for the two mapmodes. All four DDS paths exist.
- No third combined mapmode definition, label, tooltip, or sprite consumer was found.

## Accepted legitimate prose mentioning both mechanics

The following migration-owned strings legitimately describe famine as a cause, destination hazard, host constraint, or concurrent crisis. They do not name a combined mechanic and should not be renamed merely because famine and movement appear in the same passage:

- `localisation/english/migration_l_english.yml:120`, `migration_cohort_shortage: "Famine-Displaced Civilians"`, names a migration cohort by its causal hazard.
- `localisation/english/migration_l_english.yml:126`, `migration_no_one_left_at_the_gate_tooltip`, requires a receiving area to stay below catastrophic famine while resolving a migration cohort.
- `localisation/english/migration_l_english.yml:131`, `migration_hungry_not_contagious_DESC`, describes safe reception of a famine-displaced cohort.
- `localisation/english/migration_l_english.yml:135`, `migration_a_place_at_the_table_tooltip`, uses famine as a host-state safety condition.
- `localisation/english/migration_l_english.yml:137-138`, `migration_the_country_did_not_empty_DESC` and tooltip, deliberately require simultaneous war, famine, and displacement while keeping the achievement in the migration namespace.
- `localisation/english/migration_l_english.yml:150`, `migration_condemnation_forced_return_desc`, lists famine among the proven dangers to which civilians may be forcibly returned.

Comments such as `common/map_modes/chaosx_state_map_modes.txt:9-10` explicitly state that famine and migration remain separate. Package headings and paths under `docs/assets/famine_and_migration_system/` describe the archival work package, not an active mechanic id or player-facing combined label.

## Localisation and scripted-localisation findings

- Missing key list: none for the inspected categories, 32 decisions/missions, 8 achievements, 7 report scenes, or 2 mapmodes.
- Duplicate key list: none in the relevant famine, migration, humanitarian achievement, and mapmode localisation files. Repeated `l_english:` headers are file headers, not duplicate localisation entries.
- Scripted-localisation issue list: none after closure of ACN-01. All referenced `famine_*`, `migration_*`, and allowed `humanitarian_cost_*` branch keys resolve.
- Dynamic text opportunities: none required for namespace separation. Current player-facing state, country, policy, population, reserve, capacity, route, corridor, and cost values are already dynamic where the consumer needs them.
- Cross-surface mismatch notes: none after closure of ACN-01. Category labels, decision ids, cost selectors, achievement ids, report keys, mapmode names, sprite names, and manifest rows agree on separate famine and migration ownership with only allowed neutral infrastructure.
- File encoding concerns: none found. `famine_l_english.yml`, `famine_missions_l_english.yml`, `migration_l_english.yml`, `migration_missions_l_english.yml`, `humanitarian_achievement_l_english.yml`, `humanitarian_cost_l_english.yml`, and `chaosx_map_modes_l_english.yml` are UTF-8 with BOM.
- Prose-quality issues: no player-facing passage in this bounded identity audit presents one united mechanic or uses a generic combined category/mapmode label. The closed ACN-01 was an identifier problem rather than visible prose. No additional vagueness, bloat, repetition, obvious explanation, overcomplication, or style-rule defect materially affecting the separation contract was found.
- Sourced-quotation preservation: no sourced or attributed quotation surface was present in the inspected localisation. Nothing was normalized or rewritten.

## Sprite and asset-manifest findings

- The current GFX consumer census found no missing decision, category, report, achievement, texticon, or mapmode texture among the inspected famine/migration families.
- `docs/assets/famine_and_migration_system/manifest.csv` contains 50 separate root-system rows and all declared source, processed, final DDS, and target GFX paths exist.
- `docs/assets/famine_and_migration_system/report_art/manifest.md` declares 3 famine and 4 migration report sprites, matching the separate report-header consumers.
- `docs/assets/famine_and_migration_system/mapmode/manifest.csv` contains 4 rows, one selected and one deselected sprite for each separate mapmode, and all declared paths exist.
- `docs/assets/famine_and_migration_system/category_picture/manifest.md` and `gfx_handoff.md` map the two category pictures only to their owning decision category.
- Visual review of the category, mapmode, achievement, and report-art contact sheets found only separate `famine_*` and `migration_*` labels. No combined label or stale `fm_*` label was visible.

## MCP evidence and blockers

Current mandatory visual inspection did not complete:

- Parallel `hoi4.gui_inspect` calls for `famine_report_header_window` with scenario `namespace_audit_famine` and `migration_report_header_window` with scenario `namespace_audit_migration` produced no result after more than 150 seconds and were terminated. No current artifact URI was returned.
- `hoi4.map_inspect` with query `famine_state_map_mode` produced no result after more than 90 seconds and was terminated. A second migration query and map render were not started because the same route was already unresponsive.
- `hoi4.gui_render` was not attempted because the required current inspect calls did not return a workspace or diagnostics. Therefore current report-header overflow, clipping, state variants, and missing-localisation renders remain unproven.
- The installed map route cannot execute custom scripted-mapmode color or tooltip branches, and the GUI route cannot inject a selected custom mapmode. Dynamic mapmode colors, expanded tooltip layout, selected-button behavior, and click behavior remain unproven; source inspection and static contact sheets are not equivalent runtime evidence.

Useful retained static artifacts, recorded by the current mapmode validation, are:

- Mapmode button-window inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3dfcf63cd977826ebcf0c0929da3e9271a79ef0c4b6cfdfda0f5246780fd3575/6c2b73d7c89de9ae8ffc085b6aec51c8a1b87fe3ce92224c22e5e7bfac4c35d8/gui-inspect.9590e797d841572a.json`
- Static mapmode button-window render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b917c62bdfce4541d5f58ddc41eaf6ed5884f630a57a3ea88effd5f0cd3cf003/b10b1c79f83a9f0403079ff59ebdde72a9fafc41aeb639eec9df9890da29af8a/MapmodesInterface_Ingame-full.svg`
- Base map substrate inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a75193c5b26cd1180f60405e66b535e35ff3e96ad25d03aeeded209441129c2f/60deb73e299b4ab6ff6bc342e905d5758b8a18037e0444c2bdc859a58a4dfec6/map-inspect.24d421bcc68e84bf.json`
- Base state render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/54aca4aae57c108e044637123ef5a3cd9097ba9bc13d6f6f8670f5257d9e51dc/a53e6cad1f9c809827b8869d2d25e08c59aa60f048c0cfe2b7d362fdef8a8538/map-state.png`

These retained artifacts prove only the static button-window and base map substrate. They do not prove current dynamic mapmode execution or the two current separate report-header windows.

## Parent follow-up

1. ACN-01 requires no further source patch. Preserve the accepted `humanitarian_cost_*` and `GetHumanitarianCost*` namespace.
2. When the HOI4 GUI route responds, inspect and render `famine_report_header_window` and `migration_report_header_window` separately at normal, long-text, and missing-localisation states and at 1920x1080 plus 1280x720. Treat overflow as unresolved until those renders exist.
3. Keep the exact-two mapmode limitation explicit. Do not use the static artifact as proof of scripted colors, tooltips, selected states, or click behavior.

No commit was created.
