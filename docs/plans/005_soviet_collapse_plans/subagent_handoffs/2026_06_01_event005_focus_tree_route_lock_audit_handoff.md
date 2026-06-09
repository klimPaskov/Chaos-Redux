# Event005 Soviet Collapse Focus Tree Route-Lock Audit Handoff

Date: 2026-06-01
Subagent scope: audit and small bounded focus-tree patches for `common/national_focus/005_soviet_collapse_republics.txt`, `005_soviet_collapse_custom_splinters.txt`, `005_soviet_collapse_factory_successors.txt`, and `005_soviet_collapse_ancient_restorations.txt`.

No gfx, flags, or flag sprites were touched.

## Route Coverage Table

| Required route family | Implemented branch/tree surface | Status | Notes |
|---|---|---|---|
| Ukraine republic routes | `soviet_collapse_ukraine_focus_tree`, 83 focuses | Partial | Route families exist, but socialist, League, military, foreign, and Black Sea/Bread Host branches still need a full identity/reward redesign pass. |
| Shared breakaway republic tree | `soviet_collapse_breakaway_focus_tree`, 36 focuses | Partial | Core political fork exists. I patched its three hidden route selectors to show visible mutual exclusions. Rewards still include generic support-equipment and scalar bonuses. |
| Internal republics | `soviet_collapse_internal_republic_focus_tree`, 62 focuses | Partial | Branches exist, but repeated support-equipment/depot rewards remain. |
| Baltic republics | `soviet_collapse_baltic_focus_tree`, 42 focuses | Partial | Four legal/front/League/foreign selectors exist. I patched visible mutual exclusions across all four. Wide same-row selector spacing remains a layout-arrow risk. |
| Caucasus/Central Asia/Moldova/Belarus/Kazakhstan | 40/45/48/53/92 focuses | Partial | Major regional branches exist. Moldova and Belarus route selectors received visible mutual exclusions. Belarus still has one same-row prerequisite layout risk. |
| Custom splinter full trees | 19 full 47-focus trees | Partial | Most have more depth than crisis trees, but many still repeat direct equipment stockpiles and scalar rewards. I patched only five existing settlement/radical hidden-lock pairs. |
| Custom crisis trees | `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, `ICD`, 18-22 focuses | Simplified | These are still shallow relative to the OP identity target and need route design, not small patching. |
| Factory successors | `CFR` 47, `MFR` 58, `OGB` 23 focuses | Partial | CFR/MFR have forks; OGB remains shallow. No safe bounded patch beyond audit in this pass. |
| Ancient restorations | `KZR`, `SOG`, `KHW`, `ALN`, 16 focuses each | Simplified | Existing trees are compact stubs for the requested ancient-restoration identity depth. Needs broad redesign. |

## High-Priority Fixes Applied

Visible mutual exclusions now match existing hidden route-lock logic for these lore-important route choices:

| File | Changed focus ids | Before | After |
|---|---|---|---|
| `common/national_focus/005_soviet_collapse_republics.txt` | `ukr_soviet_collapse_purge_moscow_loyalists`, `ukr_soviet_collapse_re_register_the_party` | Hidden `available` lock only. | Reciprocal `mutually_exclusive` blocks added. |
| `common/national_focus/005_soviet_collapse_republics.txt` | `soviet_collapse_socialist_sovereignty_committee`, `soviet_collapse_military_defense_council`, `soviet_collapse_foreign_liaison_government` | Three-way hidden route lock only. | Three-way visible mutual exclusions added. |
| `common/national_focus/005_soviet_collapse_republics.txt` | `baltic_soviet_collapse_legal_continuity_government`, `baltic_soviet_collapse_military_border_government`, `baltic_soviet_collapse_baltic_league_first`, `baltic_soviet_collapse_foreign_protection_council` | Four-way hidden route lock only. | Four-way visible mutual exclusions added. |
| `common/national_focus/005_soviet_collapse_republics.txt` | `moldova_soviet_collapse_alliance_not_union`, `moldova_soviet_collapse_conditional_union`, `moldova_soviet_collapse_reject_the_union_question` | Three-way hidden route lock only. | Three-way visible mutual exclusions added. |
| `common/national_focus/005_soviet_collapse_republics.txt` | `blr_soviet_collapse_national_council_of_minsk`, `blr_soviet_collapse_socialist_autonomy_without_moscow`, `blr_soviet_collapse_military_transit_directorate`, `blr_soviet_collapse_foreign_corridor_administration` | Partial visible exclusions plus hidden four-way lock. | Four-way visible mutual exclusions completed. |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | `UDC_settlement`/`UDC_radical_turn`, `SDZ_settlement`/`SDZ_radical_turn`, `GAC_settlement`/`GAC_radical_turn`, `DHC_settlement`/`DHC_radical_turn`, `KHC_settlement`/`KHC_radical_turn` | Hidden pair lock only. | Reciprocal visible mutual exclusions added. |

No localisation keys or icon ids were changed.

## Duplicate Idea And Reward Spam Audit

Same-idea duplicate in one focus: none found in the four audited files. Current parser found `0` direct `add_ideas` or `add_timed_idea` uses in focus rewards, so there is no current case of one focus adding the same idea multiple times.

Repeated low-impact direct equipment rewards remain broad and should be redesigned rather than patched piecemeal. Exact high-confidence backlog from the current files:

| Tree | Exact focus ids with repeated tiny stockpile-style rewards |
|---|---|
| `ARD_soviet_collapse_focus_tree` | `ARD_first_guard`, `ARD_war_plan`, `ARD_diplomatic_plan`, `ARD_kola_denial_posts`, `ARD_convoy_court_registers`, `ARD_naval_infantry_yards`, `ARD_fuel_and_convoy_escorts`, `ARD_winter_convoy_columns`, `ARD_white_sea_port_tolls`, `ARD_league_convoy_bargain`, `ARD_port_neutrality_statute`, `ARD_arctic_port_endurance` |
| `DHC_soviet_collapse_focus_tree` | `DHC_host_court_registers`, `DHC_grain_convoy_escorts`, `DHC_convoy_autonomy_guarantees`, `DHC_river_port_tolls`, `DHC_league_passage_bargain`, `DHC_river_and_steppe_compact` |
| `KRS_soviet_collapse_focus_tree` | `KRS_baltic_worker_letters`, `KRS_anti_party_soviet_clause`, `KRS_icebound_supply_ledger`, `KRS_naval_infantry_oaths`, `KRS_gulf_mine_watch`, `KRS_free_port_conference` |
| `FEV_soviet_collapse_focus_tree` | `FEV_customs_house_ledger`, `FEV_razdolnoye_rear_area`, `FEV_pacific_observer_missions`, `FEV_sakhalin_ferry_protocols` |
| `IUL_soviet_collapse_focus_tree` | `IUL_volga_fortified_crossings`, `IUL_no_requisition_without_federal_vote`, `IUL_rail_and_river_patrols`, `IUL_volga_trade_letters` |
| `NRF_soviet_collapse_focus_tree` | `NRF_salvage_the_dark_berths`, `NRF_dead_convoy_supply_board`, `NRF_ghost_convoy_escorts`, `NRF_northern_revenant_fleet` |
| Other exact ids | `FTH_ukrainian_border_letters`, `BSC_mountain_route_envoys`, `NLC_diplomatic_plan`, `NLC_ice_port_tolls`, `baltic_soviet_collapse_the_baltic_customs_desk`, `internal_soviet_collapse_far_eastern_port_authority`, `kaz_soviet_collapse_caspian_security_detachments`, `kaz_soviet_collapse_iranian_caspian_notes`, `moldova_soviet_collapse_neutral_bridge_statute`, `KZR_caspian_patrol_letters`, `KZR_khazar_charter` |

Additional current parser counts showing the scale of the reward spam:

| Direct stockpile group | Count in audited focus files | Risk |
|---|---:|---|
| `support_equipment_1` stockpile rewards | 125 | Too many focuses use direct support equipment as filler payoff. |
| `convoy_1` stockpile rewards | 49 | Repeated convoy rewards are concentrated in naval/river/arctic branches and often need decision, trade, port, or route mechanics instead. |
| `infantry_equipment` stockpile rewards | 37 | Several radical, militia, and guard paths still use generic equipment dumps. |
| `artillery_equipment_1`/`artillery_equipment` stockpile rewards | 19+ | Artillery branches need route-specific units, missions, or doctrine hooks instead of repeated dumps. |

## Pathline, Coordinate, And Mutual-Exclusion Layout Risks

Patched:

- Existing hidden-only route locks are now visible for the focus ids listed under High-Priority Fixes Applied.
- Parser found no duplicate focus ids in the audited files.
- Parser found no one-way mutual exclusions after patch.
- Parser found no duplicate focus coordinates and no same-row one-step coordinate collisions.

Remaining exact layout risks:

| File/tree | Focus id | Risk |
|---|---|---|
| `005_soviet_collapse_republics.txt` / `soviet_collapse_belarus_focus_tree` | `blr_soviet_collapse_minsk_central_dispatch` | Prerequisite `blr_soviet_collapse_timetable_state` is on the same `y = 6` row. The wiki notes parents should be above children for clean path generation. |
| `005_soviet_collapse_custom_splinters.txt` / `NLC_soviet_collapse_focus_tree` | `NLC_polar_neutrality_statute` | Prerequisite `NLC_winter_guarantees` is below it (`parent y = 10`, `child y = 9`), a likely bad pathline. Needs a layout pass rather than a blind one-focus move because nearby `NLC_endgame`, `NLC_extreme_gate`, and `NLC_polar_commune_endurance` occupy adjacent rows. |
| `soviet_collapse_baltic_focus_tree` | `baltic_soviet_collapse_legal_continuity_government`, `baltic_soviet_collapse_military_border_government`, `baltic_soviet_collapse_baltic_league_first`, `baltic_soviet_collapse_foreign_protection_council` | Four visible mutual exclusions now reflect the real route lock, but the selectors span `x = 14` to `x = 30` on the same row. Screenshot/layout review should confirm arrows do not visually clutter the branch. |
| `soviet_collapse_belarus_focus_tree` | `blr_soviet_collapse_national_council_of_minsk`, `blr_soviet_collapse_socialist_autonomy_without_moscow`, `blr_soviet_collapse_military_transit_directorate`, `blr_soviet_collapse_foreign_corridor_administration` | Four visible mutual exclusions now reflect the real route lock, but the selectors span `x = 7` to `x = 25` on the same row. Needs screenshot review. |

## Icon Coverage Table

| File | Focuses | Missing `icon =` | Missing sprite definition in repo/vanilla interface | Repeated icon ids >= 8 |
|---|---:|---:|---:|---:|
| `005_soviet_collapse_republics.txt` | 501 | 0 | 0 | 0 |
| `005_soviet_collapse_custom_splinters.txt` | 1005 | 0 | 0 | 0 |
| `005_soviet_collapse_factory_successors.txt` | 128 | 0 | 0 | 0 |
| `005_soviet_collapse_ancient_restorations.txt` | 64 | 0 | 0 | 0 |

## Localisation And Reward Mismatch List

- Focus localisation coverage: no missing focus name or `_desc` localisation keys found for the 1,698 focus ids in the audited files.
- No localisation edits were required for the mutual-exclusion patch.
- Reward mismatch risk remains design-level: many focus titles imply unique institutions, routes, naval/river economies, or chaos identities while rewards still use generic stockpiles, scalar XP/stability, or direct equipment. Exact repeated reward ids are listed above; this needs route redesign rather than a safe local patch.

## AI Behavior Gaps

- All 1,698 audited focuses have `ai_will_do`.
- Quality gap remains: many route selectors still use flat `base` weights plus a small number of generic pressure modifiers. Broad redesign should add more route-aware AI around war state, stability, Soviet pressure, foreign appetite, League readiness, chaos tier, and route flags.
- Patched mutual exclusions make route locks visible but do not by themselves improve AI strategy quality.

## Validation Run

- Brace balance check on all four audited focus files: final depth `0`, no early closes.
- Unsupported operator grep: no `<=` or `>=` found in the four audited focus files.
- Duplicate focus id parser: none found.
- Missing icon parser: none found.
- Missing localisation parser: none found.
- One-way mutual exclusion parser after patch: none found.
- Missing `ai_will_do` parser: none found.
- Missing `search_filters` parser: none found.

Skipped validation:

- No game launch or live UI screenshot validation was run in this subagent pass.
- No gfx/flag/flag sprite validation was run because gfx/flags were explicitly out of scope.

## Remaining Route Risks

- This is not a full rework completion. Shallow crisis trees, factory successor depth, ancient-restoration depth, OP identity-specific payoffs, and repeated generic rewards remain.
- Existing broad plan remains the current handoff for redesign direction: `docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md`.
- New patch handoff path: this file.
