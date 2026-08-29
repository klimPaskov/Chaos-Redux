# Famine and migration final localisation audit

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

Date: 2026-08-24.

Status: the bounded localisation patch is complete. Source coverage is clean. Runtime visual proof remains blocked by repeated HOI4 MCP timeouts.

## Scope and changed files

- `localisation/english/famine_migration_l_english.yml`
- `localisation/english/chaosx_map_modes_l_english.yml`
- This handoff.

Both localisation files already contained concurrent uncommitted work when this audit began. The audit preserved those edits and changed only the keys listed below. No gameplay, decision, mission, scripted-localisation, GUI, GFX, achievement, mapmode, map, asset, event, workbook, or source-spec file was changed.

## Changed keys

Category and priority:

- `chaosx_famine_migration_category_desc`
- `famine_migration_priority_response_stable`

Relief, evacuation, corridor, resettlement, and movement text:

- `fm_emergency_imports_desc`
- `fm_escorted_relief_convoy_desc`
- `fm_emergency_airlift_desc`
- `fm_invite_relief_desc`
- `fm_famine_evacuation_desc`
- `fm_negotiate_corridor_desc`
- `fm_accept_corridor_offer_desc`
- `fm_reject_corridor_offer_desc`
- `fm_third_country_resettlement_desc`
- `famine_migration_decision_transfer_tt`
- `famine_migration_achievement_eligible_tooltip`

Famine mapmode:

- `famine_state_map_mode_detail_authorized`
- `famine_state_map_mode_blockade_proven`
- `famine_state_map_mode_blockade_not_proven`

Migration mapmode:

- `migration_state_map_mode_detail_authorized`
- `migration_state_map_mode_source_event`
- `migration_state_map_mode_source_cluster`
- `migration_state_map_mode_source_scenario`
- `migration_state_map_mode_route_relief_access`
- `migration_state_map_mode_route_unproven`
- `migration_state_map_mode_corridor_operation_pending`
- `migration_state_map_mode_corridor_disqualified`
- `migration_state_map_mode_corridor_expired`
- `migration_state_map_mode_cohort_exact`

## Coverage census

### Missing key list

None found in the assigned source surface.

- 28 live decision ids have title and description keys.
- All 26 `custom_cost_text` consumers resolve.
- All three `custom_trigger_tooltip` consumers resolve.
- All six live missions have title, description, success, failure, and tooltip keys.
- All nine famine and migration state modifiers have title and description keys.
- All 14 compact report-header title and summary consumers resolve.
- The four Deaths reasons `famine`, `occupation_repression`, `forced_labor`, and `forced_displacement` resolve in `chaosx_chaos_meter_l_english.yml`.
- All eight achievements have `_NAME`, `_DESC`, and `_tooltip` keys.
- All eight achievements have completed, grey, and not-eligible DDS files, for 24 achievement assets in total.
- The source defines exactly `famine_state_map_mode` and `migration_state_map_mode`. No combined or third famine and migration mapmode exists.

### Duplicate key list

None found for the famine and migration category, decisions, missions, costs, modifiers, reports, achievements, Deaths reasons, or either mapmode family across the English localisation tree.

### Scripted localisation issue list

No unresolved reference or duplicate selector name was found.

- `common/scripted_localisation/famine_migration_scripted_localisation.txt` contains 23 famine or migration selectors and 98 localisation branches.
- `common/scripted_localisation/chaosx_scripted_localisation_map_modes.txt` contains nine famine or migration map selectors and 164 localisation branches.
- All 262 branch keys resolve in localisation.
- The category phase, priority, border-policy, historical-profile, route, cohort, and cost selectors retain explicit fallback branches.
- The two mapmode detail selectors retain public qualitative branches and owner/controller-authorized detail branches.
- Scripted localisation contains no direct `§` or `£` formatting characters.

### Dynamic text opportunities and changes

The category now names Displacement Load as the primary value and retains only Reception Capacity and Border Policy as supporting country values. The migration mapmode owner summary mirrors the same hierarchy and no longer substitutes reception load for displacement load.

Dynamic country and state names in corridor offers were preserved. Dynamic scope tokens, variables, constants, formatting codes, and selector calls were preserved except for the raw numeric cohort-id display, which was deliberately replaced with the qualitative status `One active cohort selected`. The internal source branches previously shown as `Related event`, `Event cluster`, and `Scenario context` now display `Related crisis`, `Overlapping crises`, and `Starting emergency conditions` without changing their triggers.

### Cross-surface mismatch notes

- `docs/plans/famine_and_migration_system_plans/completion_report.md` still says Food Security is primary and names Displacement Load and Reception Capacity as supporting numeric values. The binding assignment and current localisation instead make Displacement Load primary, with Reception Capacity and Border Policy as the only supporting values. This documentation mismatch is outside the authorised localisation-only patch and requires parent reconciliation.
- The earlier `subagent_handoffs/localisation_auditor.md` repeats the old Food Security hierarchy. It is superseded for this point by this final audit.
- The earlier completion report describes three missions, while current source contains six fully localised missions. The current source and this census are authoritative for localisation coverage.
- Report image labels and summaries all resolve in the compact report header. This audit did not change the report-scene selection logic or asset consumers.
- Deaths wording continues to distinguish famine and forced-displacement deaths. Movement descriptions state that civilians leave the origin and survivors settle at the destination, while route deaths are recorded separately. No movement action is described as a death transaction.

### File encoding concerns

None found. `famine_migration_l_english.yml`, `famine_migration_missions_l_english.yml`, `chaosx_map_modes_l_english.yml`, and the inspected Deaths localisation file all begin with the UTF-8 BOM. No `:0` key version appears in the assigned files.

## Display before and after

- Before, the compact category used an em dash in its primary label. After, it reads `Primary: Displacement Load` and exposes only the accepted supporting values.
- Before, the authorized migration mapmode showed owner reception load plus integrated and resettled totals, and it omitted the actual country Displacement Load. After, it shows Displacement Load, Reception Capacity, and Border Policy.
- Before, mapmode source text exposed internal event, cluster, scenario, proof, contract, and numeric cohort-id language. After, it describes current crises, route availability, corridor phases, and cohort selection in player-facing terms.
- Before, relief and transfer descriptions used implementation terms such as contract, exact donor debit, credit, bounded cohort, and proven capacity. After, they state who supplies or moves people, which route must remain open, and what happens to survivors and route deaths.
- Corridor and relief phases were preserved exactly in meaning: request pending, request accepted and evacuation pending, civilians moved and protection mission pending, protection active, attacked, completed, rejected, expired, and recent relief access.

## Prose-quality repairs

### Vagueness

Relief descriptions now name the selected donor, delivery mode, endpoints, and failure conditions. Corridor text names the controller, origin, front state, request receipt, acceptance, and the later evacuation.

### Bloat

Technical transaction explanations were replaced with shorter statements about shipments, civilians, routes, and arrival.

### Obvious explanation

The transfer tooltip no longer narrates internal debit and credit bookkeeping. It adds the non-obvious rule that survivors settle at the destination while route deaths are recorded separately.

### Repetition

Repeated `contract`, `proven`, `debit`, and `credit` language was removed. The relevant route requirement appears once in each action description.

### Overcomplication

`Unique valid enemy front`, `exact foreign donor state`, and `bounded civilian cohort` were replaced with direct player-facing descriptions without changing the accepted target or route meaning.

### Style-rule repair

The assigned famine, migration, mission, and mapmode text now contains no em dash or semicolon. No event id, random-event pool, internal cohort id, implementation history, or hidden achievement disqualification label remains on the inspected general presentation surfaces. Achievement requirement tooltips retain visible conditions and disqualifiers where that information belongs.

## Sourced-quotation preservation

No sourced or attributed quotation appears in the inspected famine, migration, Deaths, achievement, compact report, decision, mission, modifier, or mapmode localisation. No quotation was altered.

## Validation and MCP evidence

Task-specific source validation found no missing or duplicate relevant key, no unresolved scripted-localisation branch, exactly two package mapmodes, all 24 achievement state assets, and the accepted value hierarchy in both the category and migration mapmode summary.

Current mandatory MCP attempts:

- `hoi4.gui_inspect` for `famine_migration_report_header_window` with scenario `default` timed out after 180 seconds.
- `hoi4.gui_render` for the same window, using normal, warning, long-text, and missing-localisation states at 1920x1080 and 1280x720, timed out after 180 seconds.
- `hoi4.map_inspect` with the famine and migration query and overview timed out after 180 seconds.
- `hoi4.map_render` for the state layer with coastlines, ports, supply nodes, and railways timed out after 180 seconds.
- `hoi4.gui_inspect` for the engine-hardcoded `mapmodes` window with scenario `famine_migration_mapmodes_final_localisation_audit` timed out after 180 seconds.
- `hoi4.gui_render` for the same mapmode scenario, using normal, hover, selected, warning, long-text, and missing-localisation states at 1920x1080 and 2560x1440, timed out after 180 seconds.

The current calls returned no artifact URI. The retained earlier map substrate artifact remains `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c6957bfb217fc3705f617c9e630721b50d8ba690e22f3ca6a168b9e136408271/284bf98a3a9ac115976ca90a5caf0815c18713e4ac231b6a08d6c6d2c6abe398/map-inspect.a672f4ba67035c47.json`. The prior report-header handoff also records `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eb1f19a21bbec4ecdbb9717a41d0a34b45c1cc68bc2bd527f30e4aa725588d37/df9f59d4ecc363ba846230814ce41e9c3fc515eed4bdcb46add8cda63dca69a5/famine_migration_report_header_window-full.svg`, but it is inherited evidence and not a post-patch render.

## Skipped meaningful validation and blockers

Runtime overflow, final line wrapping, scripted mapmode colors, button states, click regions, and tooltip rendering remain unproven because every correctly shaped current MCP inspect or render request timed out. Source review, BOM checks, branch coverage, and the older artifacts are not treated as equivalent runtime evidence.

The installed map renderer can render the underlying map substrate, but it does not render dynamic scripted-mapmode colors or tooltips. The GUI route for the hardcoded `mapmodes` window is the required complementary route, and that route timed out in this final audit. This is the exact scripted-mapmode runtime-rendering blocker.

Live in-game validation remains user-owned under repository policy and was not performed.

## Unresolved wording decisions

None. The remaining issues are documentation reconciliation and runtime visual evidence, not localisation wording choices.

## Simplifications and plan handoff

No fallback or wording simplification changed gameplay meaning. No design-depth gap requiring a new plan was found. This file is the required final patch handoff.
