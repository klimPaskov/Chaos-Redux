# Event 005 Soviet Collapse Focus Tree Fresh Audit

Date: 2026-05-30

Scope:
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`

Dependency context read:
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`

This audit was performed from the current worktree. Older handoffs were not used as source material.

## Route Coverage Table

| Tree or group | Focus count | Coverage status | Main risk |
| --- | ---: | --- | --- |
| Ukraine | 83 | Broad political, military, industry, diplomacy, and expansion routes exist | Many rewards are helper-only; major route fork is visually stretched; endpoints such as `ukr_soviet_collapse_the_directory_state` and Black Sea focuses need direct mechanics. |
| Belarus | 53 | Corridor, forest, League, Baltic, and statehood themes exist | Tight mid-tree spacing and long crossing pathlines; core forest/army choice lacks units/templates/decisions. |
| Kazakhstan | 92 | Largest republic tree, with Alash, socialist, resource, federation, foreign, military, and chaos themes | Excessively wide layout; route rewards are often staged-helper updates instead of state-targeted rail, supply, resource, units, and expansion mechanics. |
| Generic republic templates | 315 | Breakaway, internal republic, Baltic, Caucasus, Central Asia, Moldova branches exist | Helper churn dominates; many focuses read as statehood flavor without durable gameplay hooks. |
| Custom splinter 47-focus family | 846 | FTH/BSC/TNC/ALA/BBH/KRS/UDC/SDZ/GAC/DHC/KHC/FEV/SZA/UWD/MRC/IUL/BAC/ARD/NLC are present | Repeated identity ladder structure; many route focuses share helper shapes, repeated icons, and weak aggression. |
| Compact chaos splinters | 117 | PRA/TSC/RMC/DSC/NRF/ICD/OGB exist | Several are too shallow for chaos countries; DSC/NRF/OGB especially need deeper military, diplomacy, expansion, and AI hooks. |
| Factory successors | 105 | CFR and MFR are present | CFR/MFR mutual-exclusion groups are spread too wide; more decisions, contracts, rail/supply projects, and war behavior are needed. |

## Idea Spam And Helper Churn

Direct focus idea spam is low, but hidden idea churn is very high.

- Direct `add_ideas` or `remove_ideas` calls in focus rewards: 1 focus.
- Repeated same idea calls within one focus reward: 0.
- Direct `soviet_collapse_update_consolidated_republic_ideas = yes` calls in focus rewards: 100.
- Focuses that call helpers which transitively call `soviet_collapse_update_consolidated_republic_ideas`: 1345 of 1634.

The churn source is `common/scripted_effects/005_soviet_collapse_effects.txt:5513`, `soviet_collapse_update_consolidated_republic_ideas`. It calls `soviet_collapse_clear_republic_staged_ideas`, starting at `common/scripted_effects/005_soviet_collapse_effects.txt:5323`, which removes all staged republic idea variants before adding one current variant.

High-volume focus helpers that transitively feed this update path:

| Helper id | Direct focus calls | Issue |
| --- | ---: | --- |
| `soviet_collapse_apply_focus_legal_recognition` | 301 | Generic legality reward, frequent hidden staged idea churn. |
| `soviet_collapse_apply_focus_depot_and_supply_control` | 258 | Supply flavor often does not create railways, hubs, depots, or decisions directly. |
| `soviet_collapse_apply_focus_military_consolidation` | 254 | Military flavor often lacks units, templates, or doctrine hooks in the focus itself. |
| `soviet_collapse_apply_focus_league_preparation` | 220 | League rewards often do not unlock targeted diplomacy or league decisions. |
| `soviet_collapse_apply_focus_foreign_channel` | 176 | Foreign-channel flavor often lacks relation, guarantee, lend-lease, or target decisions. |
| `soviet_collapse_apply_focus_high_chaos_identity` | 97 | More aggressive than most helpers, but still repeats broad reward shape. |

Trees most affected by hidden updater churn:

| Tree | Focuses with transitive update calls |
| --- | ---: |
| Kazakhstan | 87/92 |
| Ukraine | 78/83 |
| Internal republic | 62/62 |
| Belarus | 50/53 |
| Moldova | 48/48 |
| FTH | 45/47 |
| Central Asia | 44/45 |
| PRA | 21/22 |
| DSC | 16/18 |
| NRF | 13/18 |
| OGB | 5/23 |

## Shallow Or Simplified Content

Static reward keyword counts show that the trees are much richer in flags and variables than in direct gameplay surface:

| Reward surface | Direct focus count |
| --- | ---: |
| `set_country_flag` | 1609 |
| `add_building_construction` | 376 |
| `add_equipment_to_stockpile` | 200 |
| `unlock_decision_tooltip` | 50 |
| `create_wargoal` | 12 |
| `add_claim_by` | 9 |
| `add_core_of` | 2 |
| `add_ai_strategy` | 20 |
| `create_unit` | 0 |
| `division_template` | 0 |

Priority examples:

- `common/national_focus/005_soviet_collapse_republics.txt:722`, `ukr_soviet_collapse_the_directory_state`: political endpoint, but reward is still mainly flag, war support, and consolidation. It should carry leader, law, advisor, officer, unit, or decision consequences.
- `common/national_focus/005_soviet_collapse_republics.txt:1228`, `ukr_soviet_collapse_black_sea_port_ledgers`: port theme, but needs direct dockyard, naval base, convoy, coastal defense, supply, or Black Sea decision hooks.
- `common/national_focus/005_soviet_collapse_republics.txt:9637`, `blr_soviet_collapse_partisans_or_army`: key doctrine choice, but lacks unit templates, spawned units, or a partisan/regular mission branch.
- `common/national_focus/005_soviet_collapse_republics.txt:10136`, `blr_soviet_collapse_baltic_wire_rooms`: diplomacy theme, but no direct targeted Baltic/League diplomatic mechanics.
- `common/national_focus/005_soviet_collapse_republics.txt:10288`, `kaz_soviet_collapse_the_congress_chooses_a_past`: major route fork, but needs visible route lock, leader/cosmetic/advisor changes, and state-targeted mechanics.
- `common/national_focus/005_soviet_collapse_republics.txt:11794`, `kaz_soviet_collapse_industrial_settlement_compacts`: settlement/resource theme, but reward is too generic for Kazakhstan's resource route.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:1635`, `PRA_league_transit_bargain`: transit theme needs toll, rail, supply, and League decision hooks.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:2952`, `DSC_grave_ordnance_claims`: ordnance theme should unlock depot raids, claims, cores, or special arms mechanics.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:25520`, `NLC_industry_plan`; `:25545`, `NLC_hidden_doctrine`; `:25568`, `NLC_extreme_gate`: helper/custom-tooltip focuses with thin direct mechanics.
- `common/national_focus/005_soviet_collapse_factory_successors.txt:1153` through `:1675`, OGB tree: only 23 focuses and too shallow for a chaos/factory successor compared with the requested aggressive standard.

## Layout Risks

The audit used static x/y span checks and focus prerequisite/mutual-exclusion structure. It cannot prove rendered overlap, but it identifies high-risk shapes.

High-risk clusters:

- Ukraine route fork: `ukr_soviet_collapse_officers_above_parties`, `ukr_soviet_collapse_socialist_republic_without_moscow`, `ukr_soviet_collapse_elections_under_shellfire`, `ukr_soviet_collapse_black_banner_compact`, and `ukr_soviet_collapse_protectorate_debate` are mutually exclusive across roughly 23 columns and rows 4-7. This is not sibling-shaped and likely causes crossing pathlines and unreadable fork intent.
- Ukraine endpoints: late lines to `ukr_soviet_collapse_last_harvest_plan` and `ukr_soviet_collapse_league_security_zone_mandates` make the tree feel overly linear and stretched.
- Belarus: long spans involving `blr_soviet_collapse_timetable_state`, `blr_soviet_collapse_prepare_league_freight_tables`, `blr_soviet_collapse_state_between_armies`, `blr_soviet_collapse_join_the_league_when_war_comes`, `blr_soviet_collapse_baltic_wire_rooms`, `blr_soviet_collapse_the_league_depot_at_minsk`, and `blr_soviet_collapse_the_forest_state_rumor`.
- Kazakhstan: very wide spans around `kaz_soviet_collapse_the_congress_chooses_a_past`, `kaz_soviet_collapse_alash_memory_restored`, `kaz_soviet_collapse_socialist_steppe_republic`, `kaz_soviet_collapse_resource_defense_directorate`, `kaz_soviet_collapse_steppe_federation_charter`, `kaz_soviet_collapse_the_steppe_arbitration_court`, `kaz_soviet_collapse_emergency_oil_boards`, and `kaz_soviet_collapse_airstrips_on_the_steppe`.
- CFR: `CFR_the_unfinished_city_speaks` fans into governance and construction branches across too much horizontal distance; `CFR_elect_the_site_committees`, `CFR_publish_the_planners_charter`, `CFR_invite_the_foreign_contract_board`, and `CFR_the_concrete_committee` form an overly spread mutual-exclusion set.
- MFR: `MFR_who_owns_the_rifle` fans to `MFR_officers_chair_the_board`, `MFR_armorers_elect_delegates`, `MFR_eternal_arsenal`, and `MFR_merchants_of_ammunition` across roughly 22 columns.
- FEV/SZA/MRC/BAC/ARD/NLC: several late endpoints have long vertical or diagonal prerequisite lines, especially `FEV_endgame`, `SZA_endgame`, `MRC_black_sea_transit_protocols`, `BAC_endgame`, `ARD_endgame`, and `NLC_heated_workshop_contracts`.

## Icon Coverage Table

All 1634 focuses have `icon =`, and all focus icons resolve to a sprite definition in repo or vanilla interface files.

| Tree or group | Icon issue |
| --- | --- |
| Ukraine | 83 focuses, 76 unique icons; repeated democratic and generic radio/chaos icons should be diversified during rework. |
| Belarus | 53 focuses, 51 unique icons; low duplicate risk. |
| Kazakhstan | 92 focuses, 92 unique icons; good coverage. |
| FEV | 47 focuses, 32 unique icons; 28 focuses use repeated icon ids. |
| SZA | 47 focuses, 32 unique icons; 27 focuses use repeated icon ids. |
| UWD | 47 focuses, 28 unique icons; 34 focuses use repeated icon ids. |
| MRC | 47 focuses, 31 unique icons; 28 focuses use repeated icon ids. |
| IUL | 47 focuses, 24 unique icons; 38 focuses use repeated icon ids. |
| CFR | 47 focuses, 32 unique icons; 26 focuses use repeated icon ids. |
| PRA/DSC/NRF/OGB/MFR | No missing focus icons found; special trees need more content depth before icon uniqueness is the main issue. |

Most repeated icon ids include:
- `GFX_focus_soviet_collapse_guard_the_radio_stations`
- `GFX_ukr_soviet_collapse_democratic`
- `GFX_focus_soviet_collapse_no_masters_in_kyiv_or_moscow`
- `GFX_focus_soviet_collapse_steppe_supply_congress`
- `GFX_central_asia_soviet_collapse_rail_and_irrigation_boards`
- `GFX_focus_FEV_diplomatic_plan`
- `GFX_focus_SZA_diplomatic_plan`
- `GFX_focus_MRC_civil_rule`
- `GFX_focus_IUL_supply`

## Localisation And Reward Mismatches

Localisation coverage is complete at the key level: all 1634 focus ids have name and `_desc` localisation keys in `localisation/english`.

Mismatch risks are content-level rather than missing-key issues:

- Ukraine democratic focuses reuse `GFX_ukr_soviet_collapse_democratic` and similar legal-recognition rewards even when descriptions imply institutions, coalitions, and civilian command.
- Black Sea and port descriptions in Ukraine need direct naval, port, convoy, coastal, or Black Sea diplomacy mechanics.
- Belarus forest and army descriptions need actual militia/regular templates, unit grants, forest defense decisions, or state modifier hooks.
- Kazakhstan resource, Alash, and federation descriptions imply state-building systems, but rewards frequently stay at generic variables/helpers.
- Chaos splinter localisation often promises extreme or predatory identity, while rewards stay within generic identity, stockpile, or staged idea helpers.
- Factory successor text implies contracts, arsenals, construction cities, and arms boards; CFR/MFR need more decision and mission integration.

## AI Behavior Gaps

- Direct `add_ai_strategy` appears in only 20 focus rewards across 1634 focuses.
- Chaos countries are not consistently aggressive enough. `soviet_collapse_apply_focus_high_chaos_identity` has some anti-SOV strategy behavior, but many custom chaos branches and compact trees do not carry persistent route-aware aggression.
- Ukraine, Belarus, and Kazakhstan have route choices with `ai_will_do`, but lack broader AI plans that make the country follow through with expansion, diplomacy, rail/supply investment, or defensive posture.
- Belarus corridor and forest routes need AI behavior that builds and defends rail/supply corridors or commits to partisan versus regular army choices.
- Kazakhstan needs route-aware AI for Alash, socialist, resource-defense, federation, foreign patron, and high-chaos branches.
- PRA/DSC/NRF/OGB/FEV need explicit aggressive AI hooks tied to their intended threats: claims, war goals, border wars, target priorities, and strategic construction.

## High Priority Implementation Sequence

1. Reduce hidden staged idea churn.
   - Target `common/scripted_effects/005_soviet_collapse_effects.txt:5513`, `soviet_collapse_update_consolidated_republic_ideas`.
   - Remove automatic updater calls from broad helpers where possible: `soviet_collapse_apply_focus_legal_recognition`, `soviet_collapse_apply_focus_depot_and_supply_control`, `soviet_collapse_apply_focus_military_consolidation`, `soviet_collapse_apply_focus_league_preparation`, `soviet_collapse_apply_focus_foreign_channel`, and the custom splinter identity helpers.
   - Keep staged idea recalculation on explicit milestone helpers or route-changing focuses.

2. Rework Ukraine before other republics.
   - Re-layout the major mutually exclusive branch around `ukr_soviet_collapse_officers_above_parties`, `ukr_soviet_collapse_socialist_republic_without_moscow`, `ukr_soviet_collapse_elections_under_shellfire`, `ukr_soviet_collapse_black_banner_compact`, and `ukr_soviet_collapse_protectorate_debate`.
   - Add direct mechanics to `ukr_soviet_collapse_the_directory_state`, `ukr_soviet_collapse_black_sea_port_ledgers`, Black Sea endpoints, League security zone endpoints, and bread/grain endpoints.

3. Rework Belarus spacing and mechanics.
   - Re-layout long spans around the rail corridor, Baltic wire rooms, League depot, and forest-state branch.
   - Convert `blr_soviet_collapse_partisans_or_army`, `blr_soviet_collapse_regular_forest_brigades`, and `blr_soviet_collapse_decentralized_detachments` into real unit/template/decision branches.

4. Rework Kazakhstan as a state-targeted mechanic tree.
   - Re-layout the very wide congress/resource/federation strands.
   - Add railways, supply hubs, oil/coal/resource decisions, cavalry and motorized templates, state claims, and route-specific AI.

5. Deepen compact and chaos splinter trees.
   - Prioritize PRA, DSC, NRF, OGB, FEV, and NLC.
   - Add direct war goals, claims, cores, special units/templates, raiding decisions, and AI strategies.
   - OGB should be expanded beyond 23 focuses in a full rework, not patched locally.

6. Rework CFR/MFR layout and factory mechanics.
   - Tighten mutual-exclusion geometry.
   - Add contract decisions, rail/supply projects, factory shipment missions, arms export/black market hooks, and aggressive AI behavior.

## Validation

Static checks run:
- Focus block count and tree distribution parse.
- Direct reward keyword scan.
- Helper call and transitive `soviet_collapse_update_consolidated_republic_ideas` scan.
- Missing focus icon definition scan against repo and vanilla interface files.
- Localisation name/description key coverage scan across `localisation/english`.
- Static layout span and mutual-exclusion spread scan.

Skipped:
- No game validation was run, per task instruction.
- No gameplay file patch was made.

## Changed Files

Only this audit handoff was added:
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_30_soviet_collapse_focus_tree_fresh_audit.md`

