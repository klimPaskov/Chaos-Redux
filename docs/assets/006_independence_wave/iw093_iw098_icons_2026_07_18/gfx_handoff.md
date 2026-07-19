# Event 006 IW-093 / IW-098 icon GFX handoff

Parent-owned wiring handoff. This package does not edit `.gfx` or `.gui`. All sprite names below preserve the exact gameplay IDs supplied by the parent. Filenames and suggested interface file names are proposed lowercase snake_case values because no pre-registered texture contract was supplied.

## Runtime folders

- Focus DDS: `gfx/interface/goals/006_independence_wave/iw093_iw098/` (94x86).
- Decision and category DDS: `gfx/interface/decisions/006_independence_wave/iw093_iw098/` (32x32 decisions; 52x40 categories).
- Idea DDS: `gfx/interface/ideas/006_independence_wave/iw093_iw098/` (64x64).
- Suggested `.gfx` split: `interface/006_independence_wave_iw093_iw098_focus.gfx`, `interface/006_independence_wave_iw093_iw098_decisions.gfx`, `interface/006_independence_wave_iw093_iw098_categories.gfx`, `interface/006_independence_wave_iw093_iw098_ideas.gfx` (parent may merge into an existing Event 006 interface file).

## Ready-to-copy texture pattern

```text
spriteType = {
    name = <exact sprite_name>
    texturefile = "gfx/interface/<category>/006_independence_wave/iw093_iw098/<filename>.dds"
}
```

Use the exact texture paths in the tables below; do not point `.gfx` to `docs/assets/` paths.

## Focus sprites

| Sprite name | Target | Runtime DDS | Related id | Status |
|---|---:|---|---|---|
| `GFX_goal_independence_wave_iw093_border_policing` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw093_border_policing.dds` | `independence_wave_iw093_border_policing` | `complete` |
| `GFX_goal_independence_wave_iw093_cocoa_depots` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw093_cocoa_depots.dds` | `independence_wave_iw093_cocoa_depots` | `complete` |
| `GFX_goal_independence_wave_iw093_cocoa_ledger` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw093_cocoa_ledger.dds` | `independence_wave_iw093_cocoa_ledger` | `complete` |
| `GFX_goal_independence_wave_iw093_cocoa_rail` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw093_cocoa_rail.dds` | `independence_wave_iw093_cocoa_rail` | `complete` |
| `GFX_goal_independence_wave_iw093_constitutional_cabinet` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw093_constitutional_cabinet.dds` | `independence_wave_iw093_constitutional_cabinet` | `complete` |
| `GFX_goal_independence_wave_iw093_court_cabinet_conference` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw093_court_cabinet_conference.dds` | `independence_wave_iw093_court_cabinet_conference` | `complete` |
| `GFX_goal_independence_wave_iw093_forest_guard` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw093_forest_guard.dds` | `independence_wave_iw093_forest_guard` | `complete` |
| `GFX_goal_independence_wave_iw093_form24_preparation` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw093_form24_preparation.dds` | `independence_wave_iw093_form24_preparation` | `complete` |
| `GFX_goal_independence_wave_iw093_host_ledger` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw093_host_ledger.dds` | `independence_wave_iw093_host_ledger` | `complete` |
| `GFX_goal_independence_wave_iw093_host_settlement` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw093_host_settlement.dds` | `independence_wave_iw093_host_settlement` | `complete` |
| `GFX_goal_independence_wave_iw093_kumasi_administration` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw093_kumasi_administration.dds` | `independence_wave_iw093_kumasi_administration` | `complete` |
| `GFX_goal_independence_wave_iw093_royal_confederacy` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw093_royal_confederacy.dds` | `independence_wave_iw093_royal_confederacy` | `complete` |
| `GFX_goal_independence_wave_iw093_sovereign_confederacy` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw093_sovereign_confederacy.dds` | `independence_wave_iw093_sovereign_confederacy` | `complete` |
| `GFX_goal_independence_wave_iw093_stool_delegations` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw093_stool_delegations.dds` | `independence_wave_iw093_stool_delegations` | `complete` |
| `GFX_goal_independence_wave_iw093_supply_patrols` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw093_supply_patrols.dds` | `independence_wave_iw093_supply_patrols` | `complete` |
| `GFX_goal_independence_wave_iw093_veterans_guardianship` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw093_veterans_guardianship.dds` | `independence_wave_iw093_veterans_guardianship` | `complete` |
| `GFX_goal_independence_wave_iw093_veterans_screening` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw093_veterans_screening.dds` | `independence_wave_iw093_veterans_screening` | `complete` |
| `GFX_goal_independence_wave_iw098_caravan_approaches` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw098_caravan_approaches.dds` | `independence_wave_iw098_caravan_approaches` | `complete` |
| `GFX_goal_independence_wave_iw098_caravan_wells` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw098_caravan_wells.dds` | `independence_wave_iw098_caravan_wells` | `complete` |
| `GFX_goal_independence_wave_iw098_cavalry_staff` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw098_cavalry_staff.dds` | `independence_wave_iw098_cavalry_staff` | `complete` |
| `GFX_goal_independence_wave_iw098_civic_defence` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw098_civic_defence.dds` | `independence_wave_iw098_civic_defence` | `complete` |
| `GFX_goal_independence_wave_iw098_emirate_compact` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw098_emirate_compact.dds` | `independence_wave_iw098_emirate_compact` | `complete` |
| `GFX_goal_independence_wave_iw098_emirate_council` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw098_emirate_council.dds` | `independence_wave_iw098_emirate_council` | `complete` |
| `GFX_goal_independence_wave_iw098_form25_preparation` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw098_form25_preparation.dds` | `independence_wave_iw098_form25_preparation` | `complete` |
| `GFX_goal_independence_wave_iw098_frontier_command` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw098_frontier_command.dds` | `independence_wave_iw098_frontier_command` | `complete` |
| `GFX_goal_independence_wave_iw098_frontier_infantry` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw098_frontier_infantry.dds` | `independence_wave_iw098_frontier_infantry` | `complete` |
| `GFX_goal_independence_wave_iw098_frontier_security` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw098_frontier_security.dds` | `independence_wave_iw098_frontier_security` | `complete` |
| `GFX_goal_independence_wave_iw098_livestock_market` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw098_livestock_market.dds` | `independence_wave_iw098_livestock_market` | `complete` |
| `GFX_goal_independence_wave_iw098_native_accounts` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw098_native_accounts.dds` | `independence_wave_iw098_native_accounts` | `complete` |
| `GFX_goal_independence_wave_iw098_native_administration` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw098_native_administration.dds` | `independence_wave_iw098_native_administration` | `complete` |
| `GFX_goal_independence_wave_iw098_northern_constitution` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw098_northern_constitution.dds` | `independence_wave_iw098_northern_constitution` | `complete` |
| `GFX_goal_independence_wave_iw098_railway_customs` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw098_railway_customs.dds` | `independence_wave_iw098_railway_customs` | `complete` |
| `GFX_goal_independence_wave_iw098_route_guards` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw098_route_guards.dds` | `independence_wave_iw098_route_guards` | `complete` |
| `GFX_goal_independence_wave_iw098_sultanic_federal` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw098_sultanic_federal.dds` | `independence_wave_iw098_sultanic_federal` | `complete` |
| `GFX_goal_independence_wave_iw098_sultanic_settlement` | 94x86 | `gfx/interface/goals/006_independence_wave/iw093_iw098/independence_wave_iw098_sultanic_settlement.dds` | `independence_wave_iw098_sultanic_settlement` | `complete` |


## Decision sprites

| Sprite name | Target | Runtime DDS | Related id | Status |
|---|---:|---|---|---|
| `GFX_decision_independence_wave_iw093_cabinet_conference` | 32x32 | `gfx/interface/decisions/006_independence_wave/iw093_iw098/independence_wave_iw093_cabinet_conference.dds` | `independence_wave_iw093_cabinet_conference` | `complete` |
| `GFX_decision_independence_wave_iw093_cocoa_depots` | 32x32 | `gfx/interface/decisions/006_independence_wave/iw093_iw098/independence_wave_iw093_cocoa_depots.dds` | `independence_wave_iw093_cocoa_depots` | `complete` |
| `GFX_decision_independence_wave_iw093_forest_guard` | 32x32 | `gfx/interface/decisions/006_independence_wave/iw093_iw098/independence_wave_iw093_forest_guard.dds` | `independence_wave_iw093_forest_guard` | `complete` |
| `GFX_decision_independence_wave_iw093_form24_congress` | 32x32 | `gfx/interface/decisions/006_independence_wave/iw093_iw098/independence_wave_iw093_form24_congress.dds` | `independence_wave_iw093_form24_congress` | `complete` |
| `GFX_decision_independence_wave_iw093_host_settlement` | 32x32 | `gfx/interface/decisions/006_independence_wave/iw093_iw098/independence_wave_iw093_host_settlement.dds` | `independence_wave_iw093_host_settlement` | `complete` |
| `GFX_decision_independence_wave_iw093_kumasi_railway` | 32x32 | `gfx/interface/decisions/006_independence_wave/iw093_iw098/independence_wave_iw093_kumasi_railway.dds` | `independence_wave_iw093_kumasi_railway` | `complete` |
| `GFX_decision_independence_wave_iw093_royal_conference` | 32x32 | `gfx/interface/decisions/006_independence_wave/iw093_iw098/independence_wave_iw093_royal_conference.dds` | `independence_wave_iw093_royal_conference` | `complete` |
| `GFX_decision_independence_wave_iw093_veterans_emergency` | 32x32 | `gfx/interface/decisions/006_independence_wave/iw093_iw098/independence_wave_iw093_veterans_emergency.dds` | `independence_wave_iw093_veterans_emergency` | `complete` |
| `GFX_decision_independence_wave_iw098_caravan_wells` | 32x32 | `gfx/interface/decisions/006_independence_wave/iw093_iw098/independence_wave_iw098_caravan_wells.dds` | `independence_wave_iw098_caravan_wells` | `complete` |
| `GFX_decision_independence_wave_iw098_cavalry_screen` | 32x32 | `gfx/interface/decisions/006_independence_wave/iw093_iw098/independence_wave_iw098_cavalry_screen.dds` | `independence_wave_iw098_cavalry_screen` | `complete` |
| `GFX_decision_independence_wave_iw098_form25_congress` | 32x32 | `gfx/interface/decisions/006_independence_wave/iw093_iw098/independence_wave_iw098_form25_congress.dds` | `independence_wave_iw098_form25_congress` | `complete` |
| `GFX_decision_independence_wave_iw098_frontier_command` | 32x32 | `gfx/interface/decisions/006_independence_wave/iw093_iw098/independence_wave_iw098_frontier_command.dds` | `independence_wave_iw098_frontier_command` | `complete` |
| `GFX_decision_independence_wave_iw098_livestock_market` | 32x32 | `gfx/interface/decisions/006_independence_wave/iw093_iw098/independence_wave_iw098_livestock_market.dds` | `independence_wave_iw098_livestock_market` | `complete` |
| `GFX_decision_independence_wave_iw098_native_administration` | 32x32 | `gfx/interface/decisions/006_independence_wave/iw093_iw098/independence_wave_iw098_native_administration.dds` | `independence_wave_iw098_native_administration` | `complete` |
| `GFX_decision_independence_wave_iw098_northern_constitution` | 32x32 | `gfx/interface/decisions/006_independence_wave/iw093_iw098/independence_wave_iw098_northern_constitution.dds` | `independence_wave_iw098_northern_constitution` | `complete` |
| `GFX_decision_independence_wave_iw098_sultanic_compact` | 32x32 | `gfx/interface/decisions/006_independence_wave/iw093_iw098/independence_wave_iw098_sultanic_compact.dds` | `independence_wave_iw098_sultanic_compact` | `complete` |


## Decision-category sprites

| Sprite name | Target | Runtime DDS | Related id | Status |
|---|---:|---|---|---|
| `GFX_decision_category_independence_wave_iw093_asante_compact_category` | 52x40 | `gfx/interface/decisions/006_independence_wave/iw093_iw098/independence_wave_iw093_asante_compact_category.dds` | `independence_wave_iw093_asante_compact_category` | `complete` |
| `GFX_decision_category_independence_wave_iw098_sokoto_compact_category` | 52x40 | `gfx/interface/decisions/006_independence_wave/iw093_iw098/independence_wave_iw098_sokoto_compact_category.dds` | `independence_wave_iw098_sokoto_compact_category` | `complete` |


## Idea sprites

| Sprite name | Target | Runtime DDS | Related id | Status |
|---|---:|---|---|---|
| `GFX_idea_independence_wave_iw093_cocoa_rail_compact` | 64x64 | `gfx/interface/ideas/006_independence_wave/iw093_iw098/independence_wave_iw093_cocoa_rail_compact.dds` | `independence_wave_iw093_cocoa_rail_compact` | `complete` |
| `GFX_idea_independence_wave_iw093_unsettled_restoration` | 64x64 | `gfx/interface/ideas/006_independence_wave/iw093_iw098/independence_wave_iw093_unsettled_restoration.dds` | `independence_wave_iw093_unsettled_restoration` | `complete` |
| `GFX_idea_independence_wave_iw098_caravan_network_compact` | 64x64 | `gfx/interface/ideas/006_independence_wave/iw093_iw098/independence_wave_iw098_caravan_network_compact.dds` | `independence_wave_iw098_caravan_network_compact` | `complete` |
| `GFX_idea_independence_wave_iw098_disputed_emirate_compact` | 64x64 | `gfx/interface/ideas/006_independence_wave/iw093_iw098/independence_wave_iw098_disputed_emirate_compact.dds` | `independence_wave_iw098_disputed_emirate_compact` | `complete` |


## Validation and wiring notes

- All 57 rows have package DDS and runtime DDS copies with matching SHA-256 hashes recorded in `metadata/hashes.sha256`.
- Parent should wire each exact `sprite_name` to the corresponding runtime DDS and keep the gameplay IDs unchanged.
- Focus IDs intentionally reuse some source art across multiple focus nodes only where the gameplay consumer itself reuses the same sprite ID; no additional art is needed for repeated references.
- No flags, character art, or other non-icon surfaces are part of this handoff.
- No asset is blocked or marked needs review.
