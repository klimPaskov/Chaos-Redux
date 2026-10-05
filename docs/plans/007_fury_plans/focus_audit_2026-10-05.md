# Event 007 Fury focus tree audit and patch handoff

## Status and acceptance basis

Status: partial. The source audit and bounded route fixes are complete. The parent reviewed the baseline inspect and raster and accepted a coordinate-only layout repair, but both final post-change MCP calls failed after 600 seconds. No after artifact, revision, or metrics exist, so layout acceptance remains incomplete. Numeric focus probability comparison remains unresolved. This handoff does not claim the focus tree or Event 007 is complete.

The parent authorized a bounded audit and small focus corrections, and explicitly approved the ordinary-target exhaustion gate with a manual hostile-scenario exception, the last-rival route into the existing world-end branch, and reuse of existing depot and shared-reserve actions.

The original focus specification and the follow-up implementation plan disagree about the Internal Fury branch. No explicit acceptance record authorizes dropping War Directorate, Civil Mobilization, and Compliance Administration as separate route choices, so that design claim remains unresolved.

## Spec and plan dispositions

| Claim | Source | Disposition | Basis |
|---|---|---|---|
| War Directorate, Civil Mobilization, and Compliance Administration are separate Internal Fury routes | `docs/specs/007_fury_specs/specs/007_fury_focus_tree_spec.md:112-162` and `docs/specs/007_fury_specs/focus_graphs/007_fury_focus_tree_route_map.mmd` | `unresolved` | The 52-focus implementation and the follow-up plan’s Phase 1 route list omit these routes, but no explicit user or parent decision accepts their removal or queues replacement design. |
| Normal Fury rivalry waits until ordinary valid targets are exhausted, with a manual hostile-scenario exception | Parent authorization in this task and the `fury_no_second_fury` focus | `implemented` | The focus and shared declaration helper now use `fury_can_target_rival_actor`. The manual exception requires both the actor scenario flag and the global hostile flag. Probability comparison remains unresolved. |
| The last surviving Fury can enter the existing world-end branch | Parent authorization in this task and the `fury_last_fury_standing` and `fury_the_last_neighbor_has_fallen` prerequisites | `implemented` | The last-standing focus requires that no other Fury actor remains, and the existing terminal focus accepts it as an alternate prerequisite path. Rendered connector clearance remains blocked. |
| Pact Command unlocks shared reserve support before terminal state | Parent authorization in this task and the existing reserve-sharing decision/effect path | `implemented` | The existing action now accepts Pact Command members before world-end and retains its terminal path. This extends an existing action without adding a decision family. |

The follow-up plan’s “Phase 1 implemented” label is implementation status evidence. It does not by itself supersede the original focus spec or establish design acceptance under the repository’s disposition rules.

## Changed files and identifiers

I changed `common/national_focus/007_fury_focus_tree.txt` and created this handoff at `docs/plans/007_fury_plans/focus_audit_2026-10-05.md`.

The current focus-file SHA-256 is `B9B2006A7210D5D213389218773472233C5D948BAD46BB150CA8B0E086852E3C`. The probability baseline copy retains the pre-edit source at `docs/plans/007_fury_plans/source_baseline_2026-10-05/common/national_focus/007_fury_focus_tree.txt` with SHA-256 `C5AE9029BE5642D1B5CD871722A365C990AC0348BCCF937ECE3BDBEDC75FBFD5`.

The gameplay-edited focus IDs are `fury_the_other_fire_answers`, `fury_depot_cadres`, `fury_depot_officers_without_leave`, `fury_no_second_fury`, `fury_last_fury_standing`, `fury_the_last_neighbor_has_fallen`, and `fury_main_fury_pact`. The later parent-approved layout-only patch also moved `fury_core_by_march`, `fury_last_fury_standing`, `fury_the_last_neighbor_has_fallen`, `fury_carry_the_orders_overseas`, `fury_continental_ignitions`, `fury_main_fury_pact`, `fury_world_in_fury`, and `fury_no_neutral_map`.

The accepted layout changes preserve every focus ID, prerequisite, mutual exclusion, reward, AI block, icon, and localization key. The old and new coordinates are `fury_core_by_march` (14,9) to (12,10), `fury_last_fury_standing` (20,8) to (17,11), `fury_the_last_neighbor_has_fallen` (10,10) to (9,11), `fury_carry_the_orders_overseas` (9,11) to (8,12), `fury_continental_ignitions` (11,11) to (10,12), `fury_main_fury_pact` (10,12) to (9,13), `fury_world_in_fury` (10,13) to (9,14), and `fury_no_neutral_map` (10,14) to (9,15). The parent accepted this local reflow to separate the last-standing connector from the coring and Pact Command lanes and to attempt to clear the crossing between the four coring prerequisite links. The paired post-change MCP calls timed out, so neither this crossing nor the six baseline connector-through-node warnings can be marked cleared.

No focus icon IDs changed. The parent added the associated custom availability tooltip keys `fury_no_other_fury_actors_tt` and `fury_project_pact_partner_available` in `localisation/english/007_random_expansion_l_english.yml`.

## Behavior before and after

`fury_the_other_fire_answers` now requires an eligible partner and marks every eligible Fury partner as a project-pact member. A partner must be a Fury actor, not capitulated, not on the rival route, and not at war with the completing actor. The `fury_project_pact_partner_available` tooltip describes the requirement. The focus creates no native faction or numeric meter.

`fury_depot_cadres` and `fury_depot_officers_without_leave` previously called the paid repeatable depot-deployment helper from focus rewards without a payment receipt. They now call the separate one-time focus helper `fury_spawn_focus_depot_units`, while retaining the two existing direct focus waves.

Those two depot focuses also add finite reinforcement reserves through the existing capped helper. `fury_depot_cadres` grants `constant:fury_focus_reward.depot_cadres_reserve`, currently 3, and `fury_depot_officers_without_leave` grants `constant:fury_focus_reward.depot_officers_reserve`, currently 2. Both call `fury_add_reinforcement_reserve` after setting its temporary input, so lifetime grants remain subject to the existing 100-division cap.

The paid repeatable `fury_open_forward_depots` decision is now gated by `fury_depot_cadres_unlocked`, which `fury_depot_cadres` sets. Its paid helper remains on the decision path.

The paid `fury_form_war_table` decision remains available as the earlier Evolution II route choice after `fury_second_war_table` establishes cooperation. It is not gated on `fury_the_other_fire_answers`. Its partner loop now uses the same eligibility trigger as that focus, so capitulated actors, rivals, and current enemies do not join project membership.

`fury_war_office_category` is now visible only after `fury_war_office_without_a_door` sets `fury_war_office_unlocked`, matching the focus specification’s category unlock.

`fury_no_second_fury` previously could declare on another Fury actor while ordinary valid neighbors remained. Its availability now uses the shared `fury_can_target_rival_actor` trigger. Normal rivalry waits until no ordinary valid neighbor remains. The explicit manual hostile-scenario exception requires both the actor’s `fury_triggerable_scenario_actor` flag and the global `fury_triggerable_scenario_hostile` flag. The declaration effect uses the same trigger, so the focus and helper share one rule.

`fury_last_fury_standing` previously became available without proving that other Fury actors had been eliminated and wrote an unconsumed candidate flag. It now requires that no other country has `fury_actor`, and the dead candidate flag write was removed.

`fury_the_last_neighbor_has_fallen` previously required the sequential expansion route and either coring method. Each prerequisite group now includes `fury_last_fury_standing` as another alternative, so the existing terminal route accepts either the normal `next neighbor` plus a coring method path, or the last-rival path. The new prerequisites do not form a source-graph cycle, but the connector from `(20,8)` to `(10,10)` may cross the pact and coring lanes. The MCP render blocker prevents confirming its path clearance.

`fury_main_fury_pact` now removes `fury_rival_doctrine` when the actor arrives through the rivalry route, before it adds `fury_pact_command`. The origin flag remains as route history. This prevents the terminal pivot from stacking both focus-granted route ideas.

The parent-owned integration files in the shared tree now connect the War Office category, paid depot action, preterminal Pact Command reserve sharing, project-pact membership, matching-target scoring, and shared rival declaration guard. These companion edits are recorded here for integration review and are not listed as files changed by me.

## Route coverage

| Route family | Specified content | Implemented focus IDs | Coverage and unresolved points |
|---|---|---|---|
| Opening trunk | War Office, opening army, first target, first war | `fury_open_the_war_office`, `fury_war_office_without_a_door`, `fury_count_the_rifles`, `fury_capital_guard`, `fury_first_target_files`, `fury_first_war_office_orders` | Present. The category unlock now follows its opening focus. The first target focus selects its target and fires the first-target event. |
| Army of the March | Columns, depot cadres, logistics, officer tables | `fury_field_columns`, `fury_depot_cadres`, `fury_storm_columns`, `fury_forward_depots`, `fury_logistics_under_movement`, `fury_officer_tables` | Present. The Cadres and Officers focuses preserve one-time direct waves and add capped reserve refills. The paid depot decision unlocks after Cadres. Remaining weight analysis for division, manpower, equipment, and reserve availability is unresolved. |
| Expansion | Sequential target preparation and declarations | `fury_one_border_at_a_time`, `fury_weak_neighbor_doctrine`, `fury_capital_first_plans`, `fury_cut_the_rail_before_the_war`, `fury_the_next_neighbor` | Present. Target-preparation values feed the shared candidate scorer. The Capital First and Cut the Rail focuses do not call a capital-specific selector or rail-sabotage effect, so their names and descriptions make a stronger claim than their direct rewards prove. |
| Occupation and integration | Settlement, rail registry, garrisoning, and two coring methods | `fury_occupation_registers`, `fury_census_of_taken_states`, `fury_new_registry_offices`, `fury_rail_and_registry`, `fury_garrison_the_names`, `fury_conquest_coring`, `fury_core_by_administration`, `fury_core_by_march` | Present. Captured-register, rail-registry, garrison-mission, and administrative/march coring hooks are connected to their focus flags or triggers. |
| Fury Cooperation | Pact formation, shared tables, partition, transfers, pact command | `fury_second_war_table`, `fury_the_other_fire_answers`, `fury_shared_war_tables`, `fury_partition_before_victory`, `fury_joint_cadre_transfers`, `fury_fury_pact_command` | Present. The partner-response focus marks eligible actors as project-pact members, and the paid War Table remains an earlier Evolution II choice. Pact and rivalry remain mutually exclusive. Pact Command enables the existing shared-reserve decision before terminal state. `fury_partition_before_victory` raises generic target preparation without assigning distinct target regions. |
| Fury Rivalry | Rival actor route and last-rival payoff | `fury_rival_column`, `fury_no_second_fury`, `fury_claim_the_same_map`, `fury_absorb_the_rival_fire`, `fury_last_fury_standing` | Present with corrected locks. Ordinary rival wars wait for valid normal neighbors to be exhausted except for the manual hostile scenario actor. `fury_claim_the_same_map` now feeds the shared target scorer, which boosts a candidate already targeted by another Fury actor. The last-standing focus waits until no other Fury actor remains and can reach the existing terminal branch. |
| Evolution I | Hardened army and occupation recruitment | `fury_hardened_doctrine`, `fury_harden_the_columns`, `fury_depot_officers_without_leave`, `fury_forced_march_tables`, `fury_occupation_as_recruitment` | Present. The gateway accepts already-applied Evolution I and bypasses rather than reapplying it. |
| Evolution III | All-neighbor escalation and multi-front logistics | `fury_all_borders`, `fury_three_war_offices`, `fury_storms_on_all_fronts`, `fury_no_target_is_first`, `fury_all_roads_are_front_roads` | Present. The gateway accepts already-applied Evolution III and calls the existing filtered all-neighbor declaration helper. Rendered route clarity is unverified. |
| No-neighbor and world-end | Reach buildup, main pact, terminal trigger | `fury_the_last_neighbor_has_fallen`, `fury_carry_the_orders_overseas`, `fury_continental_ignitions`, `fury_main_fury_pact`, `fury_world_in_fury`, `fury_no_neutral_map` | Present. The terminal helper checks readiness and seed capacity. The last-rival route now reaches this same terminal branch after all other Fury actors are cleared. |
| Internal Fury | War Directorate, Civil Mobilization, and Compliance Administration as separate paths | None | Missing from the 52-focus implementation. The occupation branch does not provide the specified political fork, leader/institution choice, or mobilization tradeoff. The original focus spec and the follow-up plan disagree, so design acceptance or an explicit queued disposition remains unresolved. |

## Focus decision and flag integration

| Focus or flag | Current consumer | Status |
|---|---|---|
| `fury_war_office_unlocked` | Visibility of `fury_war_office_category` | Connected by the decision owner. |
| `fury_depot_cadres_unlocked` | Visibility of paid repeatable `fury_open_forward_depots` | Connected by the decision owner. The focus also supplies a finite reserve refill and a separate one-time wave. |
| `fury_occupation_registers_unlocked` | `fury_count_captured_registers` | Connected. |
| `fury_rail_registry_unlocked` | `fury_rail_registry_survey` | Connected. |
| `fury_garrison_names_unlocked` | `fury_garrison_the_names_mission` | Connected. |
| `fury_admin_coring_unlocked`, `fury_march_coring_unlocked` | Coring scripted triggers | Connected. |
| `fury_pact_command_unlocked` | `fury_can_share_reserves` and the existing reserve-sharing decision | Connected through the preterminal pact path while retaining terminal sharing. |
| `fury_cooperation_route`, `fury_rival_route` | Pact and rivalry decisions, with reciprocal route locks | Connected. |
| `fury_the_other_fire_answers` partner response | `fury_pact_member` flags used by joint transfers and reserve sharing | Connected through shared `fury_is_valid_war_table_partner` eligibility. |
| `fury_rival_map_claims` | Shared target scoring bonus when another Fury actor already targets the same country | Connected by the helper owner. |
| Target-preparation focus effects | `fury_score_current_target_candidate` reads `fury_target_preparation` | Connected as a generic preparation bonus. Capital selection and rail sabotage remain unproved by these variable changes. |

Other focus marker flags remain set and are cleared by actor cleanup without a direct gameplay reader. They include `fury_first_war_orders_unlocked`, `fury_capital_first_plans_unlocked`, `fury_continental_ignitions_unlocked`, `fury_depot_officers_unlocked`, `fury_logistics_under_movement_unlocked`, `fury_one_border_route`, `fury_overseas_orders_unlocked`, `fury_partition_plans_unlocked`, `fury_rail_cutting_unlocked`, `fury_storm_columns_unlocked`, and `fury_weak_neighbor_doctrine_unlocked`.

These flags are metadata markers rather than gameplay on their own. Several associated focuses still grant used variables, ideas, stockpiles, command power, or direct actions. The `fury_partition_plans_unlocked` marker has no reader, and its focus does not yet allocate target regions, which remains a specific design simplification.

## Fury idea lifecycle and stack

| Idea | Entry path | Removal or replacement path |
|---|---|---|
| `fury_national_fury` | Actor package and opening focus | Replaced by `fury_hardened_fury` on Evolution I, or removed on actor cleanup. |
| `fury_hardened_fury` | `fury_apply_evolution_i` | Removed on actor cleanup. |
| `fury_overextension` | Occupation-pressure refresh while pressure is high | Removed when pressure falls below the high condition, or on actor cleanup. |
| `fury_compliance_drive` | Occupation focus and settlement decisions | Persists until actor cleanup. |
| `fury_pact_command` | Cooperation focus/decision and main-pact terminal focus | Persists until actor cleanup. A rivalry-origin actor loses `fury_rival_doctrine` before the terminal focus grants this idea. |
| `fury_rival_doctrine` | Rivalry focus/decision | Removed when a rivalry-origin actor takes `fury_main_fury_pact`, or on actor cleanup. |
| `fury_world_in_fury` | World-end start | Removed on actor cleanup. |

The current source caps focus-route ideas at three at once: one of National/Hardened, Compliance Drive, and one of Pact Command/Rival Doctrine. Overextension is pressure-created, and World in Fury is terminal-effect-created. With all of those active, the conservative maximum is five Fury ideas at once. The exact runtime overlap window remains unverified without a live scenario.

## AI behavior

All 52 focus blocks have `ai_will_do`. Source scores range from 2 to 30. Several route weights use state modifiers such as war state, evolution flags, overextension, or the presence of another Fury actor, while many branch nodes use flat bases.

The probability auditor preserved a baseline source snapshot for the focus file, but `hoi4.probability_inspect` timed out after 600 seconds. No candidate-pool completeness, scenario hash, score trace, ranking, or numerical probability result exists.

The proposed focus scenarios are `FURY_FOCUS_OPENING_PEACE`, `FURY_FOCUS_WAR_OVEREXTENSION`, `FURY_FOCUS_COOPERATION_OR_RIVALRY`, and `FURY_FOCUS_WORLD_END`. Their available-focus pools, prerequisites, bypasses, strategy plans, and campaign state remain incomplete.

The source-level weight review found that army selection does not consistently check current division count, reserve potential, manpower, or equipment exhaustion, although the AI balance matrix requires these states to influence army focus priorities. Several expansion nodes also lack a common high-overextension or no-target weight condition. Occupation focuses and terminal/world-end gates do use overextension or eligibility state.

The focus source changes do not alter `ai_will_do` expressions. Rivalry, last-standing, and reserve-gated focus behavior changes the candidate pool. The parent instructed that no more compare calls be made after repeated timeouts, so the final candidate-pool delta remains unresolved.

## Icon coverage

All 52 focuses have an icon assignment. The eight Fury-specific goal sprites are registered in `interface/007_fury.gfx` and have corresponding DDS files under `gfx/interface/goals/007_fury/`. The 17 unique generic focus icon IDs used by the tree resolve in the installed vanilla `interface/goals.gfx` definitions.

| Route family | Fury-specific icon IDs | Reused generic icon IDs most visible in the source |
|---|---|---|
| Opening | `GFX_goal_fury_war_office`, `GFX_goal_fury_target_files` | `GFX_goal_generic_political_pressure`, `GFX_goal_generic_army_artillery`, `GFX_goal_generic_construct_military`, `GFX_goal_generic_major_war` |
| Army | `GFX_goal_fury_depots` | `GFX_goal_generic_army_doctrines`, `GFX_goal_generic_construct_mil_factory`, `GFX_goal_generic_position_armies`, `GFX_goal_generic_construct_infrastructure` |
| Expansion | None | `GFX_goal_generic_demand_territory`, `GFX_goal_generic_attack_allies`, `GFX_goal_generic_intelligence_exchange`, `GFX_goal_generic_major_war`, `GFX_goal_generic_construct_infrastructure` |
| Occupation and integration | `GFX_goal_fury_occupation_registers` | `GFX_goal_generic_construct_civ_factory`, `GFX_goal_generic_construct_infrastructure`, `GFX_goal_generic_defence`, `GFX_goal_generic_forceful_treaty` |
| Cooperation | `GFX_goal_fury_pact` | `GFX_goal_generic_alliance`, `GFX_goal_generic_intelligence_exchange`, `GFX_goal_generic_demand_territory`, `GFX_goal_generic_army_artillery` |
| Rivalry | `GFX_goal_fury_rivalry` | `GFX_goal_generic_dangerous_deal`, `GFX_goal_generic_demand_territory`, `GFX_goal_generic_major_war` |
| Evolution I | None | `GFX_goal_generic_army_doctrines`, `GFX_goal_generic_construct_mil_factory`, `GFX_goal_generic_position_armies`, `GFX_focus_generic_manpower` |
| Evolution III | `GFX_goal_fury_all_borders` | `GFX_goal_generic_intelligence_exchange`, `GFX_goal_generic_major_war`, `GFX_goal_generic_demand_territory`, `GFX_goal_generic_construct_infrastructure` |
| World-end | `GFX_goal_fury_world_end`, `GFX_goal_fury_pact` | `GFX_goal_generic_demand_territory`, `GFX_goal_generic_attack_allies` |

The most reused sprite references are `GFX_goal_generic_demand_territory` on five focuses, `GFX_goal_generic_construct_infrastructure`, `GFX_goal_generic_army_doctrines`, and `GFX_goal_generic_major_war` on four each, and `GFX_goal_generic_construct_civ_factory` and `GFX_goal_generic_intelligence_exchange` on three each. The Fury-specific `world_end` sprite is used three times, and the `pact`, `rivalry`, and `occupation_registers` sprites are each used twice. These repetitions are partly route-coherent, but visual differentiation is unresolved without a focus raster/render review.

All focuses use supported-looking vanilla `search_filters` values in the current source, with 52 filter blocks for 52 focuses. The Fury-specific taxonomy suggested in the spec is not defined as separate search-filter sprites or labels. The source has no Focus Navigation or shortcut declarations. The 52-focus tree spans source coordinates `x = -1..25` and `y = 0..15`. Parent-reviewed baseline raster evidence exists; final first-glance clarity and navigation needs remain unverified because the matching post-change raster call timed out.

## Localization and reward mismatches

All 52 focus title and description keys exist in `localisation/english/007_random_expansion_l_english.yml`, and the three `custom_effect_tooltip` keys referenced by the tree are present. The last-rival and project-pact availability tooltip keys are also present. No localization key or icon ID was changed by me, though the parent added both availability keys as companion integrations.

`fury_capital_first_plans` has capital-specific title and description text, but its focus reward grants command power, momentum, and generic target preparation. No capital-specific selector or target-state effect consumes `fury_capital_first_plans_unlocked`.

`fury_partition_before_victory` describes prewar division of spoils, while its effect grants generic target preparation. The `fury_partition_plans_unlocked` marker has no gameplay reader and no focus decision assigns distinct target regions.

`fury_cut_the_rail_before_the_war` grants trucks and target preparation, but does not cut or damage a rail, and `fury_rail_cutting_unlocked` has no gameplay reader. Its focus text can be read as supply preparation, but the rail-cutting part remains presentation without a directly linked rail action.

`fury_the_last_neighbor_has_fallen` may become available through a controlled-state threshold even while a valid ordinary neighbor exists. This is consistent with the major-success world-end path but the title implies geographic exhaustion, so the focus description and eligibility criteria should remain aligned in the next localization pass.

## Layout, loading, and prerequisites

The static source graph has 52 unique focus IDs, no missing prerequisite or mutual-exclusion references, no prerequisite graph cycles, no duplicate focus coordinates, and 52 `ai_will_do` blocks. The core route locks are reciprocal for `fury_second_war_table` versus `fury_rival_column`, and for `fury_core_by_administration` versus `fury_core_by_march`.

The world-end prerequisite groups use OR semantics. The first accepts `fury_the_next_neighbor` or `fury_last_fury_standing`, and the second accepts `fury_core_by_administration`, `fury_core_by_march`, or `fury_last_fury_standing`. Because separate prerequisite blocks combine with AND, this represents `(next neighbor AND either core method) OR last fury standing`.

The focus tree has `default = no` and a country score of zero except for the `is_fury_actor` modifier. `fury_apply_package` loads it only after actor setup sets `fury_actor`. The ordinary candidate trigger requires `is_ai = yes`, excludes player-linked countries, and rejects subjects and majors before the package is applied. This is source-level loading evidence, not an in-game observation.

The baseline inspect reported the last-standing connector passing through both coring focuses and Pact Command, with its repeated prerequisite occurrence also reported; it also reported a crossing between `fury_conquest_coring` to `fury_core_by_administration` and `fury_garrison_the_names` to `fury_core_by_march`. The accepted coordinates place the terminal lane below the coring and Pact Command focuses and stack the two coring outcomes below their shared inputs. This is an independent source-coordinate projection only; without post-change domain diagnostics or a raster, none of the baseline crossings or connector-through-node findings can be claimed cleared.

## Reference evidence

The offline wiki file `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md` has local SHA-256 `BD989A13237C464F140A0AA671CC42C30A48E84A27DAE791B8914654FB9C6203`. I used lines 275–295 for prerequisite OR/AND and mutual-exclusion semantics, lines 405–430 for `available` and focus interaction, lines 455–480 for search filters, and lines 604–627 for AI focus selection.

The offline wiki file `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md` has local SHA-256 `ABC51AD18A2C46E46D47BAA795C5A840EBAF7C4AE3E777426C64A9F4C0C0CE06`. Line 109 defines `any_neighbor_country` as a country-scope neighbor search.

The installed trigger documentation at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md` has SHA-256 `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29`. Lines 1488–1495 document the country scope for `any_neighbor_country`. The installed documentation folder has no national-focus-specific documentation file.

The vanilla precedent `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/national_focus/afghanistan.txt` has SHA-256 `87EF0090E8F7AC0E626B747B476771CE14664FE8696348B43770A668AA9EC9A1`. Its active focus `AFG_look_to_other_partners` at lines 734–754 demonstrates focus prerequisite, mutual exclusion, AI score, availability, and completion reward syntax.

The focus MCP tool callables and MCP resource client were unavailable in this child runtime: `tools.mcp__hoi4_agent_tools__hoi4_focus_inspect`, `focus_render`, `focus_raster`, `focus_rewrite`, and `focus_compare` were undefined, while `read_mcp_resource` and `list_mcp_resources` timed out handshaking after 120 seconds. The parent saved `docs/plans/007_fury_plans/focus_release_evidence_2026-10-05/before_inspect.json` (271,290 bytes, revision `8f977cadc9c9afacff482cd023eea1edcec802d88f29a4150fa9017dc7ab7814`) and the parent-reviewed baseline raster `docs/plans/007_fury_plans/focus_release_evidence_2026-10-05/before.png` (SHA-256 `FCA62FB0BB4C87E95F585DB4D1DFB5E2841DE3772C6315DE89513B11983F3B7E`). The baseline inspect reported 52 focuses, 66 connectors, one crossing, five long-connector diagnostics (including a duplicate report for the last-standing edge), and six connector-through-node warnings. On 2026-10-06 at 00:48 EEST (2026-10-05 21:48 UTC), the parent reported that the final paired `hoi4.focus_inspect` and `hoi4.focus_raster` calls, against source SHA-256 `B9B2006A7210D5D213389218773472233C5D948BAD46BB150CA8B0E086852E3C`, each returned `timed out awaiting tools/call after 600s`. No after artifact, revision, raster, or post-change metrics were returned. No focus lint tool was exposed in my runtime. The nested reference tool callables were undefined, so I read the offline wiki, installed game documentation, and vanilla source directly as fallback.

## Validation and skipped checks

Task-specific source checks found 52 focus blocks and 52 unique IDs, 52 search-filter blocks, no missing AI blocks, no unresolved prerequisite or mutual-exclusion references, no prerequisite graph cycles, and no duplicate coordinates after the approved layout patch. All 52 title/description pairs and all custom focus tooltip keys resolve. All 34 unique `fury_focus_reward` constants referenced by the tree exist. The eight custom Fury goal sprites are registered with DDS files, and the 17 generic focus icon IDs resolve in the installed vanilla `interface/goals.gfx` definitions.

The helper cross-check confirms both direct focus waves call `fury_spawn_focus_depot_units`, no focus calls the paid `fury_spawn_depot_decision_units`, and that helper definition exists in the shared effects file. The rival focus availability and the rival declaration helper both use `fury_can_target_rival_actor`. Actor cleanup clears `fury_actor`, so the last-standing gate stops matching defeated Fury actors after cleanup.

My child runtime could not call `hoi4.focus_inspect`, `hoi4.focus_render`, `hoi4.focus_raster`, or the focus lint route. The parent inspected and rendered the baseline, but the final paired post-change inspect and raster calls both timed out after 600 seconds on 2026-10-06 at 00:48 EEST (2026-10-05 21:48 UTC). The changed connector paths, first-glance branch clarity, icon-image differentiation, filter usability, and Focus Navigation needs therefore remain unverified. No game or desktop session was launched, and no live save or runtime scenario was supplied.

The probability auditor’s earlier `hoi4.probability_inspect` and `hoi4.probability_compare` calls timed out after 600 seconds, and a prior all-surface batch could not confirm that it read the final after-source hash. The parent has reopened a bounded pass against the current focus hash `B9B2006A7210D5D213389218773472233C5D948BAD46BB150CA8B0E086852E3C`; its result is pending for this handoff revision. No numeric ranking or probability conclusion is included here. Do not treat the source score ranges or scenario names as probability evidence.

## Expected parent scenario setup

No save was supplied or needed for this source audit, and no game session was launched. The following named actor states or equivalent new-save setup remain useful for a future focus-candidate and route scenario review.

| Scenario | Setup | Expected route behavior |
|---|---|---|
| Ordinary neighbor and Fury rival | One Fury actor has at least one normal valid neighbor and a second non-hostile Fury actor | `fury_no_second_fury` stays unavailable until ordinary valid neighbors are exhausted. |
| Rivalry after exhaustion | One Fury actor has no normal valid neighbor and a separate eligible Fury actor remains | `fury_no_second_fury` becomes available and its shared declaration helper selects an eligible rival. |
| Manual hostile scenario | The actor has `fury_triggerable_scenario_actor`, the global hostile-scenario flag is set, and another valid Fury actor exists while normal neighbors may remain | The explicit manual actor-versus-actor exception allows the rivalry focus. A global hostile flag alone on an ordinary actor does not. |
| Last Fury standing | Complete the rival route and remove every other Fury actor through the existing cleanup path | `fury_last_fury_standing` becomes available, and its focus completion satisfies the last-rival prerequisite alternative for the existing world-end path. The world-end helper must still pass readiness and seed checks. |
| Project pact partner | Complete `fury_second_war_table` with another non-capitulated Fury actor who is not on the rival route and is not at war with the completing actor | `fury_the_other_fire_answers` becomes available and marks only the eligible other actors as project-pact members. A capitulated actor, rival-route actor, or current enemy is not marked. The paid War Table remains an earlier Evolution II action. |
| Finite depot refills | Deplete the initial reserve through weekly draws before completing `fury_depot_cadres`, then continue draws before `fury_depot_officers_without_leave` | Each focus adds its bounded refill through `fury_add_reinforcement_reserve`, retains its one-time direct wave, and enables the paid depot action only after the Cadres route flag is set. Lifetime grants stay capped. |

These are expected checks rather than live-game results. The baseline inspect and raster paths and revision are recorded above; both matching post-change MCP calls timed out after 600 seconds, so there is no after artifact path, revision, or diagnostics. No live campaign scenario hash is available.

## Remaining route risks and disposition

The high-priority design gap is the absent Internal Fury political branch. The focus spec names War Directorate, Civil Mobilization, and Compliance Administration as distinct internal choices. The follow-up plan calls its 52-focus tree complete for Phase 1 but does not include this family and states that no broad new premise is queued. Under the repository disposition rules, this conflict remains `unresolved` until the parent accepts a disposition or promotes an amended spec. No new route family or separate improvement plan was added.

The Army AI lacks consistent checks for division count, reserve potential, manpower, and equipment. The probability analysis required to judge the available-focus candidate pool remains blocked.

The baseline MCP render confirmed that the last-standing connector crossed Pact Command and the coring focuses, and that core-method connectors crossed. The accepted coordinate patch is intended to address those paths, but post-change visual acceptance is incomplete because the matching inspect and raster calls timed out. The baseline inspect also reported three distinct top-level long fan-out links from `fury_first_war_office_orders` to `fury_rival_column` (span 10), `fury_hardened_doctrine` (span 10), and `fury_all_borders` (span 14). Their acceptability as a clear, readable fan into distinct branch families was not established after reflow; no broader lane reflow was approved in this pass. A future visual acceptance pass should review all eight moved focuses: `fury_core_by_march`, `fury_last_fury_standing`, `fury_the_last_neighbor_has_fallen`, `fury_carry_the_orders_overseas`, `fury_continental_ignitions`, `fury_main_fury_pact`, `fury_world_in_fury`, and `fury_no_neutral_map`. The tree also contains no Focus Navigation definitions, so navigation needs remain unverified.

The `fury_partition_before_victory` focus still has no regional partition effect. `fury_capital_first_plans` and `fury_cut_the_rail_before_the_war` still provide general preparation rather than capital-specific target selection or an explicit rail action.

No Git commit was created because the parent’s shared-workspace instructions prohibit index changes in this subtask. The parent directed that no further focus MCP retries be made after the paired 600-second timeouts. The parent’s release report should keep layout acceptance incomplete, retain the eight-focus visual review list above, include the reopened probability result when available, and decide how to disposition the missing Internal Fury family before any Event 007 completion claim.
