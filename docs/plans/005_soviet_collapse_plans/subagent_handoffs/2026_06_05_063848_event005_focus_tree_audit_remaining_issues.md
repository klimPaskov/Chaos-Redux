# Event005 Focus Tree Audit: Remaining Reward, Depth, And Layout Issues

Audit role: `chaosx_focus_tree_auditor`  
Timestamp: 2026-06-05 06:38 UTC  
Patch status: read-only audit handoff. No gameplay, localisation, interface, or flag files were changed.

## Scope

Audited the current Event005 Soviet Collapse focus tree surface for the active objective:

- remove focus reward and visible idea spam
- make trees meaningful with distinct political, industrial, expansion, military, diplomacy, and special branches
- keep chaos countries overpowered and aggressive
- fix focus layout/pathline problems
- do not touch `gfx/flags` or flag assets

Primary audited files:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/ideas/005_soviet_collapse_ideas.txt`

I did not patch gameplay because the Event005 surface is heavily dirty and the remaining fixes are mostly branch/layout design choices rather than isolated one-line fixes. The safest next action is parent-owned tranches.

## References Consulted

- Repo skill: `.agents/skills/hoi4-focus-trees/SKILL.md`
- Offline wiki: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding
- Vanilla docs: `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, `documentation/modifiers_documentation.md`, `common/ai_strategy/_documentation.md`, `common/focus_inlay_windows/documentation.md`, `common/script_constants/documentation.md`
- Vanilla precedent: `common/national_focus/generic.txt`, `china_nationalist.txt`, and broader vanilla focus search for prerequisites, `relative_position_id`, `ai_will_do`, focus reward idea use, and branch spacing
- Prior handoff: `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_05_061350_event005_focus_tree_audit_handoff.md`

Important reference conclusions:

- Focus prerequisites inside one `prerequisite = { ... }` block are OR; multiple prerequisite blocks are AND.
- Focus pathlines are most reliable when prerequisites sit above the child focus.
- Visible national spirits should usually be matured or swapped as a lifecycle, not repeatedly stacked.
- AI focus selection uses MTTH-style `ai_will_do`; route-specific AI should shape branch choice, not only generic focus weights.

## Current Parser Metrics

Parsed 41 focus trees and 1,698 focuses across the four focus files.

- Duplicate coordinates: 0 across all parsed trees.
- Ukraine parser status: 0 duplicate coordinates, 0 same-row adjacent pairs, 0 focus-through-line cases with this parser. It still has long edges and cross-branch links.
- Belarus parser status: 0 duplicate coordinates, 0 same-row adjacent pairs, 0 focus-through-line cases with this parser. It still has long edges and reversed/same-row prerequisite edges.
- Remaining same-row adjacent pairs: 10, concentrated in Central Asia, internal republics, Moldova, and Kazakhstan.
- Remaining focus-through-line cases: 20, with Kazakhstan the worst current hotspot.

## Reward And Idea Spam Findings

No direct duplicate `add_ideas` inside a single focus reward was found in the audited focus files.

The main issue is indirect visible idea churn through lifecycle helpers and repeated helper stacks:

- `soviet_collapse_clear_republic_staged_ideas` at `common/scripted_effects/005_soviet_collapse_effects.txt:5734` removes a large family of staged visible spirits.
- `soviet_collapse_update_consolidated_republic_ideas` at `common/scripted_effects/005_soviet_collapse_effects.txt:5889` is hidden and guarded, but many focus helpers lead into this staged-spirit lifecycle.
- `soviet_collapse_update_pra_authority_idea` at `common/scripted_effects/005_soviet_collapse_effects.txt:8006` clears one of four PRA authority spirits and adds a replacement. This avoids stacking, but several PRA focuses still present as repeated authority-spirit churn instead of distinct rewards.
- `soviet_collapse_clear_focus_starting_tension_ideas` at `common/scripted_effects/005_soviet_collapse_effects.txt:5904` removes early visible tension ideas. This is safe cleanup, but should remain hidden and should not become the visible payoff.

Worst current repeated PRA visible-idea lifecycle callers:

- `PRA_the_timetable_declares_authority` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:1227`
- `PRA_armored_train_directorate` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:1403`
- `PRA_passport_of_the_moving_state` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:1572`
- `PRA_league_transit_bargain` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:1638`

Worst reward-helper stack/churn areas still needing parent cleanup:

- Kazakhstan resource/Alash/socialist/resource branches repeatedly call generic staged reward helpers such as `soviet_collapse_apply_focus_depot_and_supply_control`, `soviet_collapse_apply_focus_socialist_sovereignty`, `soviet_collapse_apply_focus_legal_recognition`, and `soviet_collapse_apply_focus_lawful_supply_plan`. Examples: `kaz_soviet_collapse_mining_workers_councils` at `common/national_focus/005_soviet_collapse_republics.txt:11477`, `kaz_soviet_collapse_planned_economy_without_center` at line 11532, and `kaz_soviet_collapse_resource_sovereignty` at line 11701.
- Compact chaos trees repeatedly stack `soviet_collapse_apply_focus_chaos_assault_plan`, `soviet_collapse_apply_objective_source_pressure_delta`, `soviet_collapse_apply_focus_high_chaos_identity`, and custom expansion helpers. Examples: `TSC_sky_over_siberia` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:2233`, `NRF_northern_revenant_fleet` at line 3833, and `ICD_grave_columns_march` at line 4250.
- Ancient restoration expansion/endgame focuses still rely on generic aggressive helper stacks instead of route-specific wrappers, especially the expansionist and beyond-border focuses in `KZR`, `SOG`, `KHW`, and `ALN`.

Recommended smallest reward fix:

Create route-specific wrapper helpers for the worst repeated reward families instead of stacking generic helpers directly in focus rewards. The wrapper should keep the existing hidden mechanics but expose one country-specific custom tooltip. Start with PRA railway authority, Kazakhstan resource sovereignty/socialist branch, compact chaos assault routes, and ancient restoration expansion routes.

## Shallow Or Disconnected Trees

Worst shallow trees:

- `KZR_soviet_collapse_ancient_focus_tree`, `SOG_soviet_collapse_ancient_focus_tree`, `KHW_soviet_collapse_ancient_focus_tree`, `ALN_soviet_collapse_ancient_focus_tree`: 16 focuses each. They have symbolic politics, a narrow industry/support lane, expansion claims/wargoals, and an end state, but lack full military, diplomacy, internal politics, and special mechanics depth.
- `TSC_soviet_collapse_focus_tree`, `RMC_soviet_collapse_focus_tree`, `DSC_soviet_collapse_focus_tree`, `NRF_soviet_collapse_focus_tree`, `ICD_soviet_collapse_focus_tree`: 18 focuses each. They are stronger than before and suitably aggressive, but still compact fixed-purpose packages rather than full trees. Missing or thin families: diplomacy, industrial identity beyond one support lane, non-expansion political alternatives, and special mechanics with multi-focus progression.
- `PRA_soviet_collapse_focus_tree`: 22 focuses. Its railway identity is good, but repeated authority-idea updates should stop being the visible reward center. It needs more visible rail corridor, logistics, rail-guard, transit bargaining, and war-routing payoffs.
- `OGB_soviet_collapse_focus_tree`: 23 focuses. It is moderate depth but still light on military/diplomacy branch depth compared with the active objective.

Most meaningful/deeper trees:

- Ukraine, Belarus, Kazakhstan, Moldova, internal republics, Baltic, Caucasus, and Central Asia generally have real political/industry/military/diplomacy/expansion surfaces.
- Kazakhstan has the strongest branch count and strong country identity, but it is currently the worst layout hotspot.
- CFR/MFR have strong factory identities. CFR still hides too much construction power behind helpers; MFR is more visibly reward-rich.

## Layout And Pathline Hotspots

No duplicate coordinates were detected.

Remaining same-row adjacent pairs:

- Central Asia: `central_asia_soviet_collapse_the_cotton_question` `(3,4)` and `central_asia_soviet_collapse_negotiate_with_the_mountain_bands` `(4,4)`.
- Central Asia: `central_asia_soviet_collapse_the_basmachi_amnesty_ledger` `(6,6)` and `central_asia_soviet_collapse_desert_scout_columns` `(7,6)`.
- Central Asia: `central_asia_soviet_collapse_bishkek_pass_council` `(8,8)` and `central_asia_soviet_collapse_khwarazm_restoration_debate` `(9,8)`.
- Internal republics: `internal_soviet_collapse_crimean_tatar_councils` `(20,5)` and `internal_soviet_collapse_taiga_steppe_self_rule` `(21,5)`.
- Kazakhstan: `kaz_soviet_collapse_the_alash_courts` `(22,4)` and `kaz_soviet_collapse_a_state_across_distances` `(23,4)`.
- Kazakhstan: `kaz_soviet_collapse_lone_steppe_state` `(24,6)` and `kaz_soviet_collapse_restore_alash_names` `(25,6)`.
- Kazakhstan: `kaz_soviet_collapse_domestic_resource_state` `(20,7)`, `kaz_soviet_collapse_no_concession_without_a_republic` `(21,7)`, and `kaz_soviet_collapse_copper_and_chrome_ledgers` `(22,7)`.
- Kazakhstan: `kaz_soviet_collapse_league_resource_pool` `(23,8)` and `kaz_soviet_collapse_local_notable_compacts` `(24,8)`.
- Moldova: `moldova_soviet_collapse_river_guard_brigades` `(14,5)` and `moldova_soviet_collapse_ukrainian_grain_road` `(15,5)`.
- Moldova: `moldova_soviet_collapse_tiraspol_depot_belt` `(14,7)` and `moldova_soviet_collapse_reject_the_union_question` `(15,7)`.

Worst current focus-through-line cases:

- Kazakhstan: `kaz_soviet_collapse_steppe_federation_charter -> kaz_soviet_collapse_the_steppe_arbitration_court` crosses `kaz_soviet_collapse_foreign_technical_missions`, `kaz_soviet_collapse_horse_and_truck_columns`, `kaz_soviet_collapse_rail_guard_brigades`, and `kaz_soviet_collapse_call_the_steppe_congress`.
- Kazakhstan: `kaz_soviet_collapse_the_congress_chooses_a_past -> kaz_soviet_collapse_a_state_across_distances` crosses `kaz_soviet_collapse_rail_to_the_mines`.
- Kazakhstan: `kaz_soviet_collapse_rail_to_the_mines -> kaz_soviet_collapse_the_steppe_arsenal` crosses `kaz_soviet_collapse_a_state_across_distances`.
- Kazakhstan: `kaz_soviet_collapse_alash_memory_restored -> kaz_soviet_collapse_restore_alash_names` crosses `kaz_soviet_collapse_the_resource_towns_demand_seats`.
- Kazakhstan: `kaz_soviet_collapse_soviets_of_the_steppe -> kaz_soviet_collapse_collective_farm_bargains` crosses `kaz_soviet_collapse_planned_economy_without_center`.
- Baltic: `baltic_soviet_collapse_a_port_without_a_master -> baltic_soviet_collapse_the_baltic_question_resolved` crosses `baltic_soviet_collapse_tallinn_riga_vilnius_rotation`.
- Breakaway generic: `soviet_collapse_a_small_state_with_teeth -> soviet_collapse_rail_hub_or_mountain_pass` crosses `soviet_collapse_sponsor_aid_audit`.
- OGB: `OGB_the_council_takes_the_seal -> OGB_reopen_volga_trade_tolls` crosses `OGB_scholars_guard_the_charter`.
- Compact chaos trees: the repeated 18-focus diagonal pattern in `TSC`, `RMC`, `DSC`, `NRF`, and `ICD` passes through a midpoint guard/support focus.
- UWD: `UWD_league_arsenal_bargain -> UWD_arsenal_federation_terms` crosses `UWD_industry_plan`.
- NLC: `NLC_greenhouse_boards -> NLC_heated_workshop_contracts` crosses `NLC_settlement`.

Worst long prerequisite edges still present:

- Kazakhstan: `kaz_soviet_collapse_the_congress_chooses_a_past` from early trunk focuses, dx 10-14.
- Kazakhstan: `kaz_soviet_collapse_steppe_federation_charter -> kaz_soviet_collapse_the_steppe_arbitration_court`, dx -16 on same row.
- Kazakhstan: `kaz_soviet_collapse_emergency_oil_boards` from `kaz_soviet_collapse_oil_field_protection_orders`, dx -9 dy 5.
- Kazakhstan: `kaz_soviet_collapse_industrial_settlement_compacts` from `kaz_soviet_collapse_emergency_oil_boards`, dx 12.
- Kazakhstan: `kaz_soviet_collapse_tajik_pass_agreements` from `kaz_soviet_collapse_call_the_steppe_congress`, dx 12.
- Moldova: `moldova_soviet_collapse_republic_of_crossings` has multiple dy 6-10 convergence lines.
- Belarus: remaining long edges include `blr_soviet_collapse_eastern_line_watch`, `blr_soviet_collapse_league_supply_timetables`, `blr_soviet_collapse_baltic_wire_rooms`, and `blr_soviet_collapse_the_league_depot_at_minsk`.
- CFR/MFR: `CFR_the_concrete_committee`, `CFR_the_debt_map`, `MFR_officers_chair_the_board`, `MFR_artillery_from_broken_foundries`.
- FEV/SZA/BAC/ARD: endgame convergence still produces long fan-in pathlines.

## Smallest Safe Next Fixes

1. Kazakhstan layout tranche first. Keep the existing focus IDs and flags; move only coordinates/prerequisite layout where necessary. Separate the Alash, socialist, resource, southern congress, and military lanes so same-row adjacency and through-lines disappear. Do not redesign rewards in the same tranche.
2. Add route-specific wrapper helpers for Kazakhstan resource/socialist rewards. Keep existing variable gains and hidden effects, but replace repeated generic helper presentation with one route-specific tooltip per branch.
3. Fix compact chaos template pathline pattern in one small shared layout tranche for `TSC`, `RMC`, `DSC`, `NRF`, and `ICD`. The repeated diagonal through midpoint focus can be fixed without changing flags or route semantics.
4. Ancient restoration reward wrapper tranche. Wrap the aggressive expansion/endgame helper stacks for `KZR`, `SOG`, `KHW`, and `ALN` so the player sees one country-specific expansion payoff, while preserving overpowered/aggressive behavior.
5. CFR/MFR pathline cleanup. Fix the few worst factory-successor crosslines without changing construction/factory reward identity.

## Validation

Brace balance passed:

- `common/national_focus/005_soviet_collapse_republics.txt`: balance 0, min 0
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`: balance 0, min 0
- `common/national_focus/005_soviet_collapse_factory_successors.txt`: balance 0, min 0
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`: balance 0, min 0
- `common/scripted_effects/005_soviet_collapse_effects.txt`: balance 0, min 0
- `common/ideas/005_soviet_collapse_ideas.txt`: balance 0, min 0

`rg -n "<=|>="` returned no hits in the audited Clausewitz files.

Focus-layout parser metrics used:

- 41 trees, 1,698 focuses parsed.
- Duplicate coordinates: 0.
- Same-row adjacent pairs: 10.
- Focus-through-line cases: 20.

No flags or flag assets were touched.

## Skills Used

- `hoi4-focus-trees`
