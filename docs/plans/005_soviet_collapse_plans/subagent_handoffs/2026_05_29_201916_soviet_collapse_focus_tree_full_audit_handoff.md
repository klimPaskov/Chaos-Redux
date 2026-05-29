# Soviet Collapse Focus Tree Full Audit Handoff

Subagent: Chaos Redux focus tree subagent  
Date: 2026-05-29  
Scope audited:
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`

User objective audited against: remove focus reward idea spam and duplicate same-idea grants; give every Soviet Collapse tree real depth and purpose; ensure distinct political, industrial, military/logistics, diplomacy, and expansion branches where relevant; make chaos-country trees extremely overpowered and lore-specific; keep Ukraine, Belarus, and major republic trees clean, compact, non-linear, and free of pathline or continuous focus panel overlap.

No gameplay patch was made in this pass. The remaining failures are broad route design and reward-system quality work, not a narrow safe prerequisite/icon/localisation fix.

## References Read

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki pages consulted: Data structures, Triggers, Effect/Effects reference, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- Vanilla documentation consulted: `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`, `~/projects/Hearts of Iron IV/documentation/triggers_documentation.md`, `~/projects/Hearts of Iron IV/documentation/modifiers_documentation.md`, `~/projects/Hearts of Iron IV/documentation/script_concept_documentation.md`.
- Event source docs consulted: `docs/events/005_soviet_collapse.md`, `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_5_focus_trees.md`, `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_6_countries_splinters_restorations.md`.

## Current Audit Totals

| File | Trees | Focuses | Direct `add_ideas` | Direct `swap_ideas` | Direct `remove_ideas` | Focuses with flat rewards |
|---|---:|---:|---:|---:|---:|---:|
| `common/national_focus/005_soviet_collapse_republics.txt` | 9 | 501 | 0 | 0 | 0 | 305 |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | 25 | 1005 | 0 | 0 | 7 | 548 |
| `common/national_focus/005_soviet_collapse_factory_successors.txt` | 3 | 128 | 0 | 0 | 1 | 53 |
| Total | 37 | 1634 | 0 | 0 | 8 | 906 |

Important interpretation: direct focus-surface idea spam is currently removed. The remaining problem is repeated helper/update rhythm and flat reward density. Across the three files, 100 focuses still call `soviet_collapse_update_consolidated_republic_ideas = yes`, and the major shared focus helpers are repeated heavily:

- `soviet_collapse_apply_focus_legal_recognition`: 301 calls
- `soviet_collapse_apply_focus_depot_and_supply_control`: 257 calls
- `soviet_collapse_apply_focus_military_consolidation`: 252 calls
- `soviet_collapse_apply_focus_league_preparation`: 220 calls
- `soviet_collapse_apply_focus_foreign_channel`: 176 calls
- `soviet_collapse_apply_focus_high_chaos_identity`: 96 calls

Flat reward counts across the audited focus rewards:

- `add_building_construction`: 375 focuses
- `add_stability`: 241 focuses
- `add_equipment_to_stockpile`: 197 focuses
- `add_command_power`: 147 focuses
- `army_experience`: 132 focuses
- `add_political_power`: 125 focuses
- `add_manpower`: 112 focuses
- `add_extra_state_shared_building_slots`: 88 focuses
- `add_war_support`: 75 focuses
- `navy_experience`: 43 focuses
- `air_experience`: 14 focuses
- `add_offsite_building`: 5 focuses

Mechanical payoff counts:

- War goal focuses: 12
- Claim focuses: 10 when including state-scoped `add_claim_by`; only 2 direct `add_state_claim` focus blocks
- Core focuses: 2
- Decision or mission unlock tooltip focuses: 44
- Missing `ai_will_do`: 0
- Missing focus title or description localisation: 0
- Missing focus icon assignment: 0
- Missing referenced `.gfx` focus icon definition: 0

## Route Coverage Table

| Tree | File line | Focuses | Coverage status | Main gap |
|---|---:|---:|---|---|
| `soviet_collapse_ukraine_focus_tree` | `common/national_focus/005_soviet_collapse_republics.txt:17` | 83 | Broad political, military, industry, diplomacy, League, foreign, and high-chaos lanes exist. | Still too wide and reward-heavy; needs final route readability pass and more concrete expansion/postwar outcomes. |
| `soviet_collapse_breakaway_focus_tree` | `common/national_focus/005_soviet_collapse_republics.txt:2355` | 36 | Compact shared breakaway skeleton exists. | Only 1 expansion-class focus; no decision unlocks found; too generic for major republics. |
| `soviet_collapse_internal_republic_focus_tree` | `common/national_focus/005_soviet_collapse_republics.txt:3152` | 62 | Political, industry/logistics, military, and regional coverage present. | No decision unlocks; expansion and end states remain thin for a major shared internal republic tree. |
| `soviet_collapse_baltic_focus_tree` | `common/national_focus/005_soviet_collapse_republics.txt:4656` | 42 | Political, border, military, and diplomatic coverage present. | No decision unlocks; expansion is still mostly claims/branch flavor instead of a settlement system. |
| `soviet_collapse_caucasus_focus_tree` | `common/national_focus/005_soviet_collapse_republics.txt:5620` | 40 | Political, local consolidation, diplomacy, and some expansion coverage present. | Needs stronger regional postwar handling and special state mechanics. |
| `soviet_collapse_central_asia_focus_tree` | `common/national_focus/005_soviet_collapse_republics.txt:6549` | 45 | Political and expansion labels are strong; decision hooks exist. | Still heavily flat-reward driven; needs stronger route-specific AI and postwar integration. |
| `soviet_collapse_moldova_focus_tree` | `common/national_focus/005_soviet_collapse_republics.txt:7698` | 48 | Compact non-linear political/corridor tree. | No decision unlocks; diplomacy and expansion are underdeveloped. |
| `soviet_collapse_belarus_focus_tree` | `common/national_focus/005_soviet_collapse_republics.txt:8866` | 53 | Clean compact tree with corridor, forest, foreign, and military surfaces. | Expansion count is only 1 by current detector; route payoffs remain helper-heavy. |
| `soviet_collapse_kazakhstan_focus_tree` | `common/national_focus/005_soviet_collapse_republics.txt:10198` | 92 | Largest republic tree with political, resource, army, diplomacy, and steppe federation surfaces. | Too large and reward-heavy; only 3 expansion-class focuses and 4 decision unlocks for a major republic. |
| `FTH_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:14` | 47 | Full high-chaos custom tree skeleton. | Layout has same-row crowding; expansion payoff is weak for an OP chaos country. |
| `PRA_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:1218` | 22 | Rail identity, rail/supply construction, and 7 decision hooks exist. | Still shallow; needs route mechanics deeper than rail rewards and a small endpoint fork. |
| `TSC_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:1790` | 18 | Basic crisis/special identity exists. | Too shallow for full country depth; no decision hooks. |
| `RMC_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:2267` | 18 | Basic martyr/death-state route exists. | Too shallow; no decision hooks; needs more extreme mechanics. |
| `DSC_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:2751` | 18 | Aggressive dead-army route exists with manpower/core/war-goal hooks and 4 decision hooks. | Still shallow for the requested Dead Soldiers Congress depth; needs a fuller dead-army economy/recruitment/command tree. |
| `NRF_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:3313` | 18 | Naval flavor, dockyards, convoy rewards, and 4 decision hooks exist. | Too shallow; needs real naval war/raiding/port-control route mechanics. |
| `ICD_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:3816` | 18 | Death-state political and military identity exists. | Too shallow and no decision hooks. |
| `BSC_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:4290` | 47 | Broad political, military, diplomacy, and logistics surfaces. | Expansion detector found 0 expansion-class focuses; no decision hooks. |
| `TNC_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:5420` | 47 | Broad regional route skeleton. | Expansion detector found 0 expansion-class focuses; no decision hooks. |
| `ALA_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:6558` | 47 | Broad regional route skeleton. | Only 1 expansion-class focus; no decision hooks. |
| `BBH_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:7678` | 47 | Military/anarchist OP identity is clearer than most. | Only 3 expansion-class focuses; no decision hooks. |
| `KRS_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:8882` | 47 | Port/sailor political and logistics surfaces exist. | Expansion detector found 0 expansion-class focuses; no decision hooks. |
| `UDC_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:10124` | 47 | Military loyalist route skeleton exists. | Expansion detector found 0 expansion-class focuses; no decision hooks. |
| `SDZ_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:11325` | 47 | Security/intelligence flavor exists. | Expansion detector found 0 expansion-class focuses; no decision hooks. |
| `GAC_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:12570` | 47 | Peasant/military route skeleton exists. | Only 1 expansion-class focus; no decision hooks. |
| `DHC_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:13753` | 47 | Host/cossack route skeleton exists. | Expansion detector found 0 expansion-class focuses; no decision hooks. |
| `KHC_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:14959` | 47 | Host/cossack route skeleton exists. | Expansion detector found 0 expansion-class focuses; no decision hooks. |
| `FEV_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:16158` | 47 | Far Eastern route skeleton exists. | Only 1 expansion-class focus; no decision hooks. |
| `SZA_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:17333` | 47 | Siberian administration/logistics tree exists. | Expansion detector found 0 expansion-class focuses; no decision hooks. |
| `UWD_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:18513` | 47 | Worker/industrial route skeleton exists. | Expansion detector found 0 expansion-class focuses; no decision hooks. |
| `MRC_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:19718` | 47 | Mountain confederation route skeleton exists. | Only 2 expansion-class focuses; no decision hooks. |
| `IUL_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:20894` | 47 | Volga/Ural route skeleton exists. | Expansion detector found 0 expansion-class focuses; no decision hooks. |
| `BAC_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:22051` | 47 | Birobidzhan/Amur route skeleton exists. | Only 2 expansion-class focuses; no decision hooks. |
| `ARD_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:23196` | 47 | Arctic port/naval directorate has dockyard, convoy, port, and 3 decision hooks. | Expansion detector found 0 expansion-class focuses; needs more naval war/port-state mechanics. |
| `NLC_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:24395` | 47 | Polar/science route skeleton exists. | Expansion detector found 0 expansion-class focuses; no decision hooks. |
| `CFR_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_factory_successors.txt:15` | 47 | Construction state has governance fork, strategy fork, civilian industry, rail, contracts, dark route, and 4 decision hooks. | Mutual-exclusion line geometry still passes through intervening focuses; some branches are reward-heavy. |
| `OGB_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_factory_successors.txt:1135` | 23 | Compact Volga restoration route with claims/wargoals. | Too shallow for a high-chaos successor; no decision hooks. |
| `MFR_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_factory_successors.txt:1712` | 58 | Arsenal state has industry, military, diplomacy, rivalry, and 3 decision hooks. | Layout has one detected pathline hit and mutual-exclusion line risk; expansion/special mechanics are still thinner than industry. |

## Duplicate Idea And Reward Findings

Direct focus-surface idea additions:

- `add_ideas = 0`
- `swap_ideas = 0`
- `add_timed_idea = 0`
- Duplicate same direct `add_ideas` inside one focus: 0

Direct focus-surface idea removals are limited to 8 cleanup endpoints:

| Focus id | File line | Removed idea |
|---|---:|---|
| `PRA_the_board_overrules_ministers` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:1361` | `pra_dispatcher_court_tensions` |
| `TSC_the_committee_of_instruments` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:1936` | `tsc_field_station_rivalries` |
| `RMC_communes_of_witnesses` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:2371` | `rmc_credal_cell_rivalries` |
| `DSC_witness_officers` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:2857` | `dsc_grave_regiment_rivalries` |
| `NRF_living_harbor_committees` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:3413` | `nrf_drowned_crew_disputes` |
| `ICD_commissars_of_last_addresses` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:3918` | `icd_grave_commissar_rivalries` |
| `mrc_protect_village_autonomy` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:20096` | `mrc_pass_confederation_rivalries` |
| `OGB_the_council_takes_the_seal` | `common/national_focus/005_soviet_collapse_factory_successors.txt:1189` | `ogb_disputed_restored_name` |

Helper-mediated idea additions remain the main source of visible spirit churn:

- `soviet_collapse_update_consolidated_republic_ideas` at `common/scripted_effects/005_soviet_collapse_effects.txt:5459` is called by 100 focuses. It clears staged republic ideas first, so this does not appear to be duplicate same-idea stacking, but it still makes many focus rewards feel like repeated staged-spirit maintenance.
- `soviet_collapse_apply_custom_splinter_doctrine_identity` at `common/scripted_effects/005_soviet_collapse_effects.txt:13194` is called by 19 doctrine focuses and is guarded by `NOT = { has_idea = ... }` for tag-specific internal faction ideas. This is not duplicate same-idea spam, but it is a template rhythm shared across many different chaos tags.
- Many `soviet_collapse_complete_*_endgame` helpers add a final idea. These are usually called by mutually exclusive endpoints or single end states, so no immediate duplicate grant was found in the audited focus graph.

Highest reward repetition risks:

1. `common/national_focus/005_soviet_collapse_custom_splinters.txt`: 548 of 1005 focuses have at least one flat reward; 169 focus blocks directly add equipment stockpiles and 251 directly add buildings.
2. `common/national_focus/005_soviet_collapse_republics.txt`: 305 of 501 focuses have at least one flat reward; 141 depot helper calls and 140 legal recognition helper calls make many republic routes feel similar.
3. `common/national_focus/005_soviet_collapse_factory_successors.txt`: 53 of 128 focuses have at least one flat reward. CFR/MFR are better differentiated than most custom splinters, but CFR still repeats construction mandate/public works helpers and MFR still leans on arsenal/security/client-arms helper cycles.

## Missing Or Simplified Content

High-priority issues first:

1. `PRA_soviet_collapse_focus_tree` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:1218` is stronger than most shallow crisis trees but remains only 22 focuses. It has rail/supply rewards and decision hooks, yet it needs deeper route mechanics: rail corridor mandates, junction-control missions, railway-toll diplomacy, moving-state expansion, and postwar rail integration.
2. `DSC_soviet_collapse_focus_tree` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:2751` is aggressive in its endpoint but still only 18 focuses. The user objective asks for aggressive manpower/cores/war goals; current content has those, but not enough branch depth around dead-army politics, recruitment economy, memorial front claims, and repeated conquest/coring choices.
3. `NRF_soviet_collapse_focus_tree` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:3313` is naval-flavored but only 18 focuses. It needs actual naval war systems: raiding decisions, port-control missions, convoy lane pressure, White Sea/Baltic claims, naval invasion behavior, and naval AI strategies.
4. `ARD_soviet_collapse_focus_tree` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:23196` has 47 focuses and some naval/port content, but the expansion detector found 0 expansion-class focuses. It should become the clean non-revenant northern naval directorate: ships, dockyards, convoy escort/raiding, Arctic port control, and coastal war goals.
5. `CFR_soviet_collapse_focus_tree` at `common/national_focus/005_soviet_collapse_factory_successors.txt:15` now has meaningful civilian industry construction, but it should go further: recurring civilian construction decisions, client-city projects, reconstruction protectorate integration, construction-city subject hooks, and branch-specific AI.
6. `OGB_soviet_collapse_focus_tree` at `common/national_focus/005_soviet_collapse_factory_successors.txt:1135` is a 23-focus successor tree and is still shallow relative to other high-chaos successors.
7. The 47-focus custom splinter trees mostly have political/industry/military/diplomacy labels, but many have 0 detected expansion-class focuses and 0 decision hooks. The worst current route-depth offenders are `BSC`, `TNC`, `KRS`, `UDC`, `SDZ`, `DHC`, `KHC`, `SZA`, `UWD`, `IUL`, `ARD`, and `NLC`.
8. Ukraine, Belarus, and Kazakhstan are broad enough, but still need compactness and route payoff cleanup. Ukraine has only 2 same-row spacing warnings now, but it remains very wide. Belarus is cleaner but has only 1 expansion-class focus by detector. Kazakhstan is very large and needs reward compression plus stronger steppe federation/expansion payoffs.

## Icon Coverage Table

| File | Missing icon assignment | Missing `.gfx` definition | Repeated icon groups | Top repeated icons |
|---|---:|---:|---:|---|
| `common/national_focus/005_soviet_collapse_republics.txt` | 0 | 0 | 22 | `GFX_focus_soviet_collapse_guard_the_radio_stations` x4, `GFX_ukr_soviet_collapse_democratic` x4, `GFX_focus_soviet_collapse_no_masters_in_kyiv_or_moscow` x4, `GFX_focus_soviet_collapse_steppe_supply_congress` x4, `GFX_central_asia_soviet_collapse_rail_and_irrigation_boards` x4 |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | 0 | 0 | 99 | `GFX_focus_FEV_diplomatic_plan` x4, `GFX_focus_SZA_diplomatic_plan` x4, `GFX_focus_MRC_civil_rule` x4, `GFX_focus_MRC_foreign` x4, `GFX_focus_IUL_supply` x4 |
| `common/national_focus/005_soviet_collapse_factory_successors.txt` | 0 | 0 | 11 | `GFX_focus_CFR_municipal_board_elections` x3, `GFX_focus_CFR_concrete_republic` x3, `GFX_focus_CFR_the_builder_state` x3, `GFX_focus_CFR_civilian_hegemony_project` x3 |

Icon conclusion: no load-breaking icon issue was found, but the unique-icon requirement is not satisfied. The biggest visual-quality risk is the custom splinter file.

## Localisation And Reward Mismatch List

| Surface | Status |
|---|---|
| Focus title keys | No missing keys found for the 1634 audited focus ids. |
| Focus description keys | No missing `_desc` keys found for the 1634 audited focus ids. |
| Direct idea reward spam | No direct `add_ideas`, `swap_ideas`, or `add_timed_idea` in scoped focus rewards. |
| Duplicate same direct idea grant | 0 detected. |
| Reward mismatch risk | High. Many focus names imply concrete programs but still resolve into the same few helpers plus small construction/equipment/stat rewards. |
| Hover spam risk | Moderate. Direct idea stacking is gone, but staged-idea update helpers are called from 100 focus rewards and should remain hidden/custom-tooltipped where possible. |

Specific mismatch or thin-payoff targets:

- `common/national_focus/005_soviet_collapse_custom_splinters.txt:1218` `PRA_soviet_collapse_focus_tree`: rail identity is real, but the tree needs more route mechanics than rail/supply rewards.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:2751` `DSC_soviet_collapse_focus_tree`: endpoint is dangerous, but the tree is too short for the promised Dead Soldiers Congress.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:3313` `NRF_soviet_collapse_focus_tree`: naval titles and filters exist, but the reward pattern is still mostly convoy/dockyard/navy XP plus one endpoint.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:23196` `ARD_soviet_collapse_focus_tree`: northern naval directorate has port/dockyard flavor but lacks expansion-class payoffs.
- `common/national_focus/005_soviet_collapse_factory_successors.txt:15` `CFR_soviet_collapse_focus_tree`: good construction identity, but governance and strategy forks need more distinct operating-model consequences.
- `common/national_focus/005_soviet_collapse_factory_successors.txt:1712` `MFR_soviet_collapse_focus_tree`: arsenal content is broad, but expansion/special mechanics still lag industry/military rewards.

## Layout And Pathline Risks

The coordinate audit found no duplicate focus coordinates and no approximate continuous-focus-panel overlap in the three scoped files. The continuous panel check used the declared `continuous_focus_position` values converted from pixels to focus-coordinate units and a conservative panel rectangle. This is not a replacement for in-game screenshots.

Remaining layout risks:

| Tree | File line | Risk |
|---|---:|---|
| `soviet_collapse_ukraine_focus_tree` | `common/national_focus/005_soviet_collapse_republics.txt:17` | Same-row `dx = 1` spacing between `ukr_soviet_collapse_socialist_republic_without_moscow` and `ukr_soviet_collapse_republic_of_laws`; same-row `dx = 1` spacing between `ukr_soviet_collapse_army_supremacy` and `ukr_soviet_collapse_civilian_command_over_the_army`. |
| `FTH_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:14` | Four same-row `dx = 1` spacing pairs: `FTH_commune_supply_ledger`/`FTH_commune_court_registers`, `FTH_grain_and_rifle_stores`/`FTH_tachanka_column_oaths`, `FTH_extreme_gate`/`FTH_commune_court_registers`, `FTH_steppe_airstrips`/`FTH_extreme_path`. |
| `CFR_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_factory_successors.txt:15` | Mutual-exclusion line geometry passes through intervening focus ids: `CFR_elect_the_site_committees` to `CFR_the_concrete_committee` through `CFR_publish_the_planners_charter`; `CFR_rails_first` to `CFR_contracts_first` through `CFR_factories_first`. |
| `MFR_soviet_collapse_focus_tree` | `common/national_focus/005_soviet_collapse_factory_successors.txt:1712` | Same-row `dx = 1` spacing around `MFR_standardize_the_rifle_line`, `MFR_unsafe_production_surge`, `MFR_builders_waste_steel`; one straight-line prerequisite hit from `MFR_rifles_against_the_league` to `MFR_german_orders` through `MFR_rifles_for_the_league`; mutual-exclusion line between `MFR_officers_chair_the_board` and `MFR_merchants_of_ammunition` passes through `MFR_armorers_elect_delegates`. |

## AI Behavior Gaps

- No focus is missing `ai_will_do`.
- Route-aware AI is still inconsistent. Many focuses have base weights plus simple stability/war modifiers, while chaos-country endpoints need stronger `add_ai_strategy` and target checks.
- OP custom splinters should actively prefer conquest, anti-SOV pressure, regional rival targets, and route-specific decisions after taking aggressive endpoints. This is uneven, especially for the 47-focus templated splinters with 0 detected expansion-class focuses.
- Naval actors need naval AI behavior, not only focus weights: `NRF` and `ARD` should push port defense, convoy raiding, naval production, dockyard construction, and coastal target priorities.
- Railway actors need route-aware logistics AI: `PRA` should value rail/supply construction while at war, junction seizure when SOV is weak, and corridor diplomacy when neutral or factionless.
- Major republic AI should make clearer choices between defensive consolidation, diplomacy/recognition, League leadership, and expansion. Ukraine has more bespoke AI than most, but Belarus and Kazakhstan still need route distinction.

## High-Priority Implementation Plan

1. Deepen the shallow special trees first: `PRA`, `DSC`, `NRF`, `TSC`, `RMC`, and `ICD`. These fail the requested "real depth" standard most clearly by focus count and route surface.
2. Give `PRA` a real rail authority loop: focus-gated decisions or missions for rail corridors, junction cities, rail/supply hub construction, toll diplomacy, armored-train deployments, and post-conquest rail integration.
3. Expand `DSC` from an endpoint spike into a dead-army state: manpower pressure, grave-roll recruitment, controlled-state coring/integration, veteran-town decisions, memorial-front war goals, and aggressive AI.
4. Split the northern naval content by role. `NRF` should become the revenant naval war tree with drowned fleet/raiding mechanics; `ARD` should become the naval northern directorate with dockyards, port control, ships, naval invasion/convoy war, and Arctic diplomacy.
5. Convert templated 47-focus custom splinters from shared helper rhythms into lore-specific OP mechanics. Prioritize trees with 0 expansion-class focuses: `BSC`, `TNC`, `KRS`, `UDC`, `SDZ`, `DHC`, `KHC`, `SZA`, `UWD`, `IUL`, `ARD`, `NLC`.
6. Rework `CFR` and `MFR` layout geometry after any route edits. CFR's governance/strategy forks should not draw mutual-exclusion lines through other focuses; MFR needs the same cleanup around the arsenal governance fork and League/order branch.
7. Compact the major republics after reward changes. Ukraine should keep route breadth but reduce path crowding; Belarus should gain stronger expansion/corridor payoffs without becoming linear; Kazakhstan should be compressed around resource/steppe federation decisions.
8. Replace repeated flat rewards with focus-to-decision mechanics. Use existing Soviet Collapse decision categories and helper systems where possible; add new helper or decision hooks only when the route needs persistent gameplay.
9. Run an icon differentiation pass after route shapes settle. The custom splinter file has 99 repeated icon groups and is the highest-value target.
10. Re-run validation and in-game screenshot layout checks for Ukraine, Belarus, CFR, MFR, PRA, DSC, NRF, and ARD before any completion claim.

## Changed Files

- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_29_201916_soviet_collapse_focus_tree_full_audit_handoff.md`

## Changed Focus IDs

None. No focus files were edited in this pass.

## Route Behavior Before And After

No gameplay behavior changed. This handoff records the current route quality state and implementation plan.

## Localisation Keys And Icon IDs Changed

None.

## Validation Run

- Parsed 37 focus trees and 1634 focus blocks across the three scoped files.
- Counted direct idea operations in focus completion rewards: `add_ideas = 0`, `swap_ideas = 0`, `add_timed_idea = 0`, `remove_ideas = 8`.
- Counted helper, flat reward, decision, claim/core, and war-goal usage from focus `completion_reward` blocks.
- Checked missing focus icon assignment: 0.
- Checked focus icon `.gfx` definitions against `interface/*.gfx`: 0 missing.
- Checked focus title and `_desc` localisation keys against `localisation/english/*.yml`: 0 missing.
- Checked missing `ai_will_do`: 0.
- Coordinate audit found 0 duplicate focus coordinates and 0 approximate continuous-focus-panel overlaps in scoped files.

## Skipped Validation

- No in-game launch or screenshot validation was run. The pathline and continuous-panel checks are script-assisted approximations and must be confirmed visually.
- No gameplay validation was run because no gameplay files were changed.
- No broad route redesign was attempted because that exceeds the safe local-patch boundary for this audit.

## Remaining Route Risks

- The full Soviet Collapse focus-tree objective is not complete.
- Direct idea spam appears removed, but helper-driven staged idea updates and repeated flat rewards still make many focus routes feel mechanically similar.
- Several chaos-country trees are not yet extremely overpowered or lore-specific enough.
- Ukraine, Belarus, and Kazakhstan need a final compactness/reward-layout pass after deeper reward changes.
- Repeated icon groups remain a significant readability problem.
- Existing worktree changes predate this handoff; parent review should isolate this handoff from unrelated dirty files.
