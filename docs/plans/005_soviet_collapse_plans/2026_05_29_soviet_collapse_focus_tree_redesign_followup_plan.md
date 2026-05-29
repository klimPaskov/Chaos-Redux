# Soviet Collapse Focus Tree Redesign Follow-Up Plan

Date: 2026-05-29
Owner: main Soviet Collapse implementation agent
Source audit: active focus-tree subagent pass over the four Soviet Collapse focus files.

## Scope

This plan covers the broad route redesign work that is outside the bounded active small-patch pass. The small patch cleaned visible mutual exclusions, layout collisions, continuous panel obstruction, missing icon references, and two obvious repeated tiny convoy rewards. It did not redesign whole trees or add new route families.

## Route Coverage Baseline

| File | Trees | Focuses | Coverage status |
|---|---:|---:|---|
| `common/national_focus/005_soviet_collapse_republics.txt` | 9 | 501 | Ukraine, Belarus, Kazakhstan and shared republic trees exist, but Ukraine/Belarus still need a full route readability and reward-identity pass. |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | 25 | 1005 | Most full custom splinters have 47 focuses; crisis splinters have 18-22. Several high-chaos trees still rely on repeated convoy/truck/AA rewards. |
| `common/national_focus/005_soviet_collapse_factory_successors.txt` | 3 | 128 | CFR and MFR have real forks; OGB remains a shallow 23-focus successor and needs specialization depth. |
| `common/national_focus/005_soviet_collapse_ancient_restorations.txt` | 4 | 64 | KZR, SOG, KHW, ALN are 16-focus stubs compared with the requested ancient-restoration identity depth. |

## High-Priority Route Work

1. Ukraine route readability and identity pass.
   - Branch selectors: `ukr_soviet_collapse_socialist_republic_without_moscow`, `ukr_soviet_collapse_black_banner_compact`, `ukr_soviet_collapse_elections_under_shellfire`, `ukr_soviet_collapse_officers_above_parties`, `ukr_soviet_collapse_protectorate_debate`.
   - Follow-up work: make each route produce a distinct government identity, leader/advisor/law pressure or cosmetic path where existing hooks allow it, and add route-aware AI weights that respond to Soviet Collapse variables rather than mostly flat bases.
   - Reward integration targets: keep using existing focus helper effects, but add explicit unlocks or tooltips for existing Soviet Collapse decision systems where the route meaning promises trade, grain, League, Black Sea, protectorate, or Bread Host mechanics.
   - Layout target: keep visible mutual exclusions from the small patch, then re-run pathline screenshots or parser coordinates after any route movement.

2. Belarus route structure and spacing pass.
   - Existing selectors needing visible-semantics review: `blr_soviet_collapse_national_council_of_minsk`, `blr_soviet_collapse_socialist_autonomy_without_moscow`, `blr_soviet_collapse_military_transit_directorate`, `blr_soviet_collapse_foreign_corridor_administration`.
   - Mechanic anchors: `blr_soviet_collapse_prepare_league_freight_tables`, rail authority rewards, corridor/trade identity, forest committees, and League freight integration.
   - Follow-up work: separate crowded focus rows, reduce repeated rail/truck framing, and make the corridor paths unlock or strengthen existing decisions/effects rather than only adding variables.

3. Custom splinter identity and OP specialization pass.
   - Full 47-focus trees to review first: `FTH`, `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC`.
   - Crisis/shallow trees to deepen or explicitly classify as crisis trees: `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, `ICD`.
   - Follow-up work: route end states should create dangerous expansion/specialization payoffs tied to existing Soviet Collapse pressure, depot, recognition, League, war, foreign appetite, or old-movement mechanics. Avoid adding direct idea stacks.

4. Factory successors.
   - `CFR`: governance fork now has visible mutual exclusions. Redesign pass should make `CFR_elect_the_site_committees`, `CFR_publish_the_planners_charter`, `CFR_invite_the_foreign_contract_board`, `CFR_the_concrete_committee` produce distinct operating models.
   - `CFR`: strategy fork now has visible mutual exclusions. Redesign pass should specialize `CFR_cities_first`, `CFR_rails_first`, `CFR_factories_first`, `CFR_contracts_first`.
   - `MFR`: route fork now has visible mutual exclusions. Redesign pass should specialize `MFR_officers_chair_the_board`, `MFR_armorers_elect_delegates`, `MFR_merchants_of_ammunition`, `MFR_eternal_arsenal`.
   - `OGB`: expand beyond the current 23-focus shape or document it as intentionally narrow. Current depth is not enough for an OP successor route.

5. Ancient restorations.
   - Trees: `KZR_soviet_collapse_ancient_focus_tree`, `SOG_soviet_collapse_ancient_focus_tree`, `KHW_soviet_collapse_ancient_focus_tree`, `ALN_soviet_collapse_ancient_focus_tree`.
   - Follow-up work: each currently has 16 focuses. Add route identity and existing-mechanic hooks before claiming completion. Do not add a new formable chain unless explicitly approved by the parent.

## Reward Cleanup Backlog

Direct tiny generic equipment rewards remain in 47 focuses. Replace these with existing helpers, decision unlock hooks, state-building effects, variable progression, or route-specific payoffs where appropriate.

| Tree | Focus ids |
|---|---|
| `ARD_soviet_collapse_focus_tree` | `ARD_first_guard`, `ARD_war_plan`, `ARD_diplomatic_plan`, `ARD_kola_denial_posts`, `ARD_convoy_court_registers`, `ARD_naval_infantry_yards`, `ARD_fuel_and_convoy_escorts`, `ARD_winter_convoy_columns`, `ARD_white_sea_port_tolls`, `ARD_league_convoy_bargain`, `ARD_port_neutrality_statute`, `ARD_arctic_port_endurance` |
| `BSC_soviet_collapse_focus_tree` | `BSC_mountain_route_envoys` |
| `DHC_soviet_collapse_focus_tree` | `DHC_host_court_registers`, `DHC_grain_convoy_escorts`, `DHC_convoy_autonomy_guarantees`, `DHC_river_port_tolls`, `DHC_league_passage_bargain`, `DHC_river_and_steppe_compact` |
| `FEV_soviet_collapse_focus_tree` | `FEV_customs_house_ledger`, `FEV_razdolnoye_rear_area`, `FEV_pacific_observer_missions`, `FEV_sakhalin_ferry_protocols` |
| `FTH_soviet_collapse_focus_tree` | `FTH_ukrainian_border_letters` |
| `IUL_soviet_collapse_focus_tree` | `IUL_volga_fortified_crossings`, `IUL_no_requisition_without_federal_vote`, `IUL_rail_and_river_patrols`, `IUL_volga_trade_letters` |
| `KRS_soviet_collapse_focus_tree` | `KRS_baltic_worker_letters`, `KRS_anti_party_soviet_clause`, `KRS_icebound_supply_ledger`, `KRS_naval_infantry_oaths`, `KRS_gulf_mine_watch`, `KRS_free_port_conference` |
| `KZR_soviet_collapse_ancient_focus_tree` | `KZR_caspian_patrol_letters`, `KZR_khazar_charter` |
| `NLC_soviet_collapse_focus_tree` | `NLC_diplomatic_plan`, `NLC_ice_port_tolls` |
| `NRF_soviet_collapse_focus_tree` | `NRF_salvage_the_dark_berths`, `NRF_dead_convoy_supply_board`, `NRF_ghost_convoy_escorts`, `NRF_northern_revenant_fleet` |
| `soviet_collapse_baltic_focus_tree` | `baltic_soviet_collapse_the_baltic_customs_desk` |
| `soviet_collapse_internal_republic_focus_tree` | `internal_soviet_collapse_far_eastern_port_authority` |
| `soviet_collapse_kazakhstan_focus_tree` | `kaz_soviet_collapse_caspian_security_detachments`, `kaz_soviet_collapse_iranian_caspian_notes` |
| `soviet_collapse_moldova_focus_tree` | `moldova_soviet_collapse_neutral_bridge_statute` |

## Hidden Route Locks Needing Semantics Review

The parser still finds 26 focus blocks using hidden `has_completed_focus` locks without visible mutual exclusions. Some may be valid end-state gates, but they need manual review so the player can understand route locks.

Ids: `ukr_soviet_collapse_purge_moscow_loyalists`, `ukr_soviet_collapse_re_register_the_party`, `soviet_collapse_socialist_sovereignty_committee`, `soviet_collapse_military_defense_council`, `soviet_collapse_foreign_liaison_government`, `baltic_soviet_collapse_legal_continuity_government`, `baltic_soviet_collapse_military_border_government`, `baltic_soviet_collapse_baltic_league_first`, `baltic_soviet_collapse_foreign_protection_council`, `moldova_soviet_collapse_alliance_not_union`, `moldova_soviet_collapse_conditional_union`, `moldova_soviet_collapse_reject_the_union_question`, `blr_soviet_collapse_national_council_of_minsk`, `blr_soviet_collapse_socialist_autonomy_without_moscow`, `blr_soviet_collapse_military_transit_directorate`, `blr_soviet_collapse_foreign_corridor_administration`, `UDC_settlement`, `UDC_radical_turn`, `SDZ_settlement`, `SDZ_radical_turn`, `GAC_settlement`, `GAC_radical_turn`, `DHC_settlement`, `DHC_radical_turn`, `KHC_settlement`, `KHC_radical_turn`.

## Validation Required After Redesign

- Re-run bracket depth, duplicate focus id, missing localisation, missing icon definition, unsupported operator, and wrong focus filter checks.
- Re-run coordinate audits for same tree/same row focus boxes at distance 0 or 1.
- Re-run continuous focus panel obstruction checks.
- Grep every changed focus id and helper id.
- Validate that each new decision unlock or effect hook points to existing decision/effect identifiers unless the parent explicitly approves new systems.
