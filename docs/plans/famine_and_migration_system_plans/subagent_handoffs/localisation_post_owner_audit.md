# Famine and migration localisation post-owner audit

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

Status: complete within the exclusive localisation scope. This audit did not create an event, event ID, event log, Event Details entry, pacing row, workbook row, third mapmode, or gameplay change. No commit was created.

## Scope and sources

The audit covered the current shared famine and migration gameplay, decision, mission, dynamic-modifier, achievement, report-header, mapmode, scripted-localisation, interface, Deaths-reason, specification, matrix, prompt, routing, bibliography, closure-review, asset, and owner-handoff sources named in the parent task.

The package is a shared system rather than an event. The `chaos-redux-events` rules were used for the shared player-facing prose standard and to confirm that event-only surfaces do not apply. The decisions/missions, event-assets, state-ledgers, and subagents skills supplied the cost, tooltip, exact-population, asset-consumer, and handoff contracts.

The required offline Paradox wiki localisation, decision, interface, and scripted-GUI pages were consulted together with the core wiki pages required by `AGENTS.md`. Installed vanilla localisation formatter and localisation-object documentation were consulted. Vanilla `mapmode_l_english.yml`, refugee/resettlement localisation, and selected decision precedents were used as comparison material.

## Changed files and keys

Changed `localisation/english/famine_migration_l_english.yml`:

- `fm_invite_relief_desc`
- `fm_open_reception_desc`
- `famine_migration_decision_target_available_tt`
- `famine_migration_decision_effect_tt`
- `famine_migration_decision_transfer_tt`
- `famine_migration_state_preparing_to_leave_desc`
- `famine_migration_state_depopulated_districts_desc`
- `famine_migration_state_return_readiness_desc`
- `famine_migration_achievement_eligible_tooltip`
- `famine_migration_break_the_blockade_tooltip`
- `famine_migration_roads_home_tooltip`
- `famine_migration_a_place_at_the_table_tooltip`
- `famine_migration_the_country_did_not_empty_tooltip`

Changed `localisation/english/chaosx_map_modes_l_english.yml`:

- `famine_state_map_mode_detail_authorized`
- `famine_state_map_mode_relief_delivery_proven`
- `famine_state_map_mode_relief_route_proven`
- `famine_state_map_mode_relief_none`
- `MAPMODE_MIGRATION_STATE_MAP_MODE_DESCRIPTION`
- `migration_state_map_mode_detail_authorized`
- `migration_state_map_mode_origin_recorded`
- `migration_state_map_mode_origin_unproven`
- `migration_state_map_mode_host_recorded`
- `migration_state_map_mode_host_unproven`
- `migration_state_map_mode_destination_recorded`
- `migration_state_map_mode_destination_unproven`
- `migration_state_map_mode_flight_share_recorded`
- `migration_state_map_mode_flight_share_none`
- `migration_state_map_mode_reception_share_recorded`
- `migration_state_map_mode_reception_share_none`
- `migration_state_map_mode_capacity_invalid`
- `migration_state_map_mode_identity_return_ambiguous`
- `migration_state_map_mode_identity_integration_owner`
- `migration_state_map_mode_identity_unresolved`
- `migration_state_map_mode_route_relief_delivered`
- `migration_state_map_mode_route_relief_route_proven`
- `migration_state_map_mode_route_proven`
- `migration_state_map_mode_corridor_prepared`
- `migration_state_map_mode_corridor_generation_recorded`
- `migration_state_map_mode_corridor_generation_none`

Added this handoff. No package key lives in `localisation/english/chaosx_achievements_l_english.yml`, so that file was audited but not changed. No genuine selector defect was found in `common/scripted_localisation/chaosx_scripted_localisation_map_modes.txt`, so it was not changed.

## Consumer census

The exact package census found:

- 34 decision-file entries: six missions, 26 primary actions, and two corridor responses.
- All 34 entries have title and description keys. The six mission families also have success, failure, and tooltip text, with two reception-observation status keys.
- 56 title/description keys cover the 26 primary actions and two corridor responses.
- 32 mission and mission-status keys cover all six mission families.
- 14 dynamic modifier identifiers have all 28 title/description keys. This includes the four food stages and all ten dynamic movement/reception phases.
- 24 achievement title/description/condition keys cover all eight achievements, plus the shared eligibility tooltip.
- 14 report-header title/summary keys cover all seven report scenes.
- 105 keys cover the two dedicated famine and migration mapmodes, their complete legends, public and authorized tooltips, roles, sources, routes, corridors, capacity status, ambiguity status, and terminal states.
- 192 package scripted-localisation key references resolve to English definitions.
- 36 dynamic famine/migration localisation calls resolve to 41 available selector definitions, with no missing called selector.
- 15 package custom-tooltip consumers resolve to English definitions.
- 333 unique consumer-expected keys across decisions, missions, scripted localisation, report GUI, dynamic modifiers, tooltips, and achievements have zero missing definitions.
- 513 definitions were examined across the package localisation files, with zero duplicate keys in the package and zero duplicate package keys elsewhere in English localisation.
- Exactly two dedicated mapmode definitions exist: `famine_state_map_mode` and `migration_state_map_mode`.

## Deaths reason audit

The shared Deaths localisation contains the required visible labels:

- `chaos_meter.deaths.cause.famine`: `From famine`
- `chaos_meter.deaths.cause.forced_displacement`: `From forced displacement`
- `chaos_meter.deaths.cause.forced_labor`: `From forced labor`
- `chaos_meter.deaths.cause.occupation_repression`: `From occupation repression`

Current exact consumers use famine for starvation, forced displacement for coercive route and return deaths, forced labor for lethal labor, and occupation repression for lethal occupation conduct. Transit and trapped status do not have separate proximate Deaths-reason constants. The ownership matrix assigns trapped-border starvation to famine and coercive transit or return exposure to forced displacement. No unsupported `From transit` or `From trapped` label was invented. These shared Deaths keys live outside the exclusive write boundary and required no patch.

## Localisation audit results

Missing key list: none.

Duplicate key list: none.

Scripted localisation issue list: none. All called package selectors and every package `localization_key` resolve. No scripted-localisation mechanics were altered.

Dynamic text opportunities: no missing dynamic value warranted a new selector. Existing state names, country names, costs, timers, populations, food values, capacity, policy, corridor state, cohort ambiguity, and achievement thresholds already use dynamic localisation. The retained mapmode owner blocker prevents exact origin, host, and destination names from being recovered during map refresh without a new producer or scan, so the tooltip continues to report whether those roles were recorded rather than inventing names.

Cross-surface mismatch notes: no unresolved wording mismatch was found among the decision category, 26 primary decisions, two corridor responses, six missions, ten dynamic presentation phases, seven report headers, two mapmodes, eight achievements, and Deaths reason labels. The category retains one primary `Displacement Load` value with `Reception Capacity` and `Border Policy` as supporting values. Ideology is not presented as a guarantee of safety, and direct famine, persecution, occupation, bombing, camp, contamination, outbreak, and route conditions remain capable of overriding affinity in the inspected gameplay sources.

File encoding concerns: none. The three audited package localisation files retain UTF-8 BOM. The changed files use the repository key style without `:0`.

Sourced-quotation preservation: no inspected package surface contains a sourced or attributed quotation. No quotation was changed.

## Display before and after

Before the patch, several player-facing lines exposed implementation vocabulary such as `measured transaction`, `debits`, `credits`, `projection`, `owner ledger`, `generation`, `validated`, and `state-local`. Several sentences also joined complete clauses with forbidden semicolons.

After the patch, decisions state the concrete requirement or consequence: a selected state and cohort must still qualify, only people who leave are removed from the origin, survivors arrive, and route deaths remain separate. Reception text describes shelter, sanitation, and medical services sized to the local population without claiming that the action opens a route.

The mapmode retains every value and dynamic selector while using player-readable labels such as `Recorded origin`, `People waiting to leave`, `People in reception`, `Relief route confirmed`, and `Operation`. Neutral text remains neutral when the source cannot prove a role, route, movement type, or capacity revision.

Achievement conditions retain their thresholds and disqualifiers but replace internal phrases such as `failed population ledger`, `transfer cycling`, and `tag switching` with direct descriptions of unaccounted movement, repeated cohort movement, and continuing as another country.

## Prose-quality repair summary

Vagueness: replaced abstract success language with the exact player-visible requirement and result. Neutral mapmode states remain deliberately noncommittal only where owner evidence is unavailable.

Bloat: shortened implementation explanations that described accounting internals instead of the player consequence.

Obvious explanation: removed phrases that narrated internal credit/debit mechanics after the visible action result was already clear.

Repetition: reduced repeated `exact`, `projection`, `recorded`, and `owner` labels in the long migration tooltip while preserving the distinction among origin, host, destination, and movement type.

Overcomplication: split semicolon-linked clauses and simplified long noun stacks such as `exact relief-action route proof` and `owner integration ledger`.

Style-rule repair: removed all em dashes and semicolons from the three package localisation files. No staccato chain, dialectical hedge, staged contrast, prompt fragment, tuning note, or implementation-history wording remains in the inspected package text.

Disease wording: `Controlled Medical Reception` and its mission text remain conditional on proven exposure. The text attributes disease risk to exposure, crowding, water, sanitation, shelter, and medical conditions, never to displaced civilians as a group.

## Validation and retained artifacts

Task-specific validation confirmed zero missing consumer keys, zero missing dynamic selectors, all 14 dynamic modifiers localized, all seven report title/summary pairs present, all eight achievement text triplets present, and exactly two dedicated mapmode definitions.

The retained owner map evidence is the successful map render at revision `9d7d710f11e4dd5241055e8852e095d90394b8827f55ce0b9316c570b3da96a1`. Its resources are:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/52b108966ee8fa0c47ca7458c9be87112fed5d84a5836a4c5f9bb313cb021685/a4ed0f4e4349464582c7319bf91e6d89db2e191788fcb321acb1f747e00e264b/map-state.png`
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/84eb5b7c422ff71112b888848f2c899ee967a9a89aed9b60c81c00279bcb12a3/5ade08eb606ec77870a3307a4883f1453eb49114f00d2535964b11cc963add43/map-state.json`
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/41fadb1662a2e53190a562b2a95d8f9569fd5239735371be9d0e81ede0bb4e21/3da704960661cfb4072e30b25f69e38521f2869d620ab71f51697e89874a0ab5/map-state.html`

The hardcoded mapmodes GUI inspect/render route resolved zero elements or exposed no linked raster or payload in the owner pass. The map renderer proves state geometry and transport substrate only. It does not execute dynamic map colors, tooltip authorization, overflow, or click regions. Per the parent instruction, this audit retained that exact owner blocker and did not claim source review as rendered tooltip proof.

No new GUI or map MCP call was run because this patch edits localisation only and GUI/map source edits were forbidden. No live game was launched.

## Simplifications, omissions, blockers, and unresolved wording decisions

No gameplay, localisation-surface, or key-coverage simplification was introduced.

The only material presentation blocker is unchanged: current MCP rendering cannot execute the two mapmodes' dynamic colours or tooltips, and the hardcoded GUI route cannot provide overflow evidence. Live overflow and runtime token expansion therefore remain user-owned validation.

No exact endpoint-name wording was added because the mapmode owner proved that map refresh lacks those names without a new producer or scan. The neutral role-record wording is intentional.

No plan handoff beyond this required audit report was needed because the audit found no missing mechanic or design-depth gap.

Dynamic tokens, formatting codes, state and country references, values, conditions, and selector calls were preserved. No sourced quotation exists in the inspected surface, so there is no quotation exception or uncertainty.
